"""
HTML Updater for mechanics cleanup extraction.

Updates existing HTML files while preserving structure, styling, and navigation.
Uses BeautifulSoup for parsing and manipulation.
"""

from pathlib import Path
from typing import Optional, List, Dict
from bs4 import BeautifulSoup, Tag, NavigableString, Comment
import re

from extraction_system.mechanics_cleanup.logger import get_logger
from extraction_system.mechanics_cleanup.error_handler import (
    ErrorHandler,
    HTMLUpdateException
)


class HTMLUpdater:
    """Updates existing HTML files while preserving structure and styling."""
    
    def __init__(self, html_path: str):
        """
        Initialize with path to HTML file.
        
        Args:
            html_path: Path to the HTML file to update
            
        Raises:
            HTMLUpdateException: If HTML file doesn't exist or can't be parsed
        """
        self.html_path = Path(html_path)
        self.logger = get_logger()
        self.error_handler = ErrorHandler()
        
        if not self.html_path.exists():
            error = self.error_handler.handle_file_not_found(
                str(self.html_path),
                "HTMLUpdater initialization"
            )
            raise HTMLUpdateException(
                f"HTML file not found: {self.html_path}",
                error
            )
        
        # Load and parse HTML
        try:
            with open(self.html_path, 'r', encoding='utf-8') as f:
                self.html_content = f.read()
            
            self.soup = BeautifulSoup(self.html_content, 'html.parser')
            self.logger.info(f"HTMLUpdater initialized with: {self.html_path}")
        except Exception as e:
            self.logger.error(f"Failed to parse HTML: {e}")
            raise HTMLUpdateException(
                f"Failed to parse HTML file: {self.html_path}",
                {"error": str(e)}
            )
        
        # Track removed content for logging
        self.removed_content: List[Dict[str, str]] = []
        
        # Store original CSS classes for preservation
        self.original_classes: Dict[str, List[str]] = {}
    
    def find_section(self, section_id: str) -> Optional[Tag]:
        """
        Find section by ID or heading.
        
        Searches for:
        1. Element with matching id attribute
        2. Heading element with matching text
        3. Element with matching class name
        
        Args:
            section_id: Section identifier (id, heading text, or class name)
            
        Returns:
            BeautifulSoup Tag element or None if not found
        """
        self.logger.info(f"Searching for section: {section_id}")
        
        # Try finding by ID attribute
        section = self.soup.find(id=section_id)
        if section:
            self.logger.info(f"Found section by id: {section_id}")
            return section
        
        # Try finding by heading text (h1-h6)
        for heading_level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = self.soup.find_all(heading_level)
            for heading in headings:
                heading_text = heading.get_text(strip=True)
                if heading_text.lower() == section_id.lower():
                    # Return the parent section or the heading itself
                    parent = heading.find_parent(['section', 'div', 'article'])
                    if parent:
                        self.logger.info(
                            f"Found section by heading text: {section_id} "
                            f"(parent: {parent.name})"
                        )
                        return parent
                    else:
                        self.logger.info(f"Found heading: {section_id}")
                        return heading
        
        # Try finding by class name
        section = self.soup.find(class_=section_id)
        if section:
            self.logger.info(f"Found section by class: {section_id}")
            return section
        
        # Try partial match on heading text
        for heading_level in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = self.soup.find_all(heading_level)
            for heading in headings:
                heading_text = heading.get_text(strip=True).lower()
                if section_id.lower() in heading_text:
                    parent = heading.find_parent(['section', 'div', 'article'])
                    if parent:
                        self.logger.info(
                            f"Found section by partial heading match: {section_id}"
                        )
                        return parent
                    else:
                        return heading
        
        self.logger.warning(f"Section not found: {section_id}")
        return None
    
    def update_section(self, section_id: str, new_content: str) -> None:
        """
        Update section content while preserving structure.
        
        Args:
            section_id: Section identifier
            new_content: New HTML content for the section
            
        Raises:
            HTMLUpdateException: If section not found or update fails
        """
        self.logger.info(f"Updating section: {section_id}")
        
        # Find the section
        section = self.find_section(section_id)
        
        if not section:
            self.logger.error(f"Cannot update section - not found: {section_id}")
            raise HTMLUpdateException(
                f"Section not found: {section_id}",
                {"section_id": section_id, "html_path": str(self.html_path)}
            )
        
        # Store original classes before update
        if section.get('class'):
            self.original_classes[section_id] = section.get('class')
        
        # Parse new content
        new_soup = BeautifulSoup(new_content, 'html.parser')
        
        # If section is a heading, update the content after it
        if section.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            # Find or create a container after the heading
            next_sibling = section.find_next_sibling()
            
            if next_sibling and next_sibling.name == 'div':
                # Update existing div
                next_sibling.clear()
                for element in new_soup:
                    if isinstance(element, Tag):
                        next_sibling.append(element)
            else:
                # Create new div after heading
                new_div = self.soup.new_tag('div')
                for element in new_soup:
                    if isinstance(element, Tag):
                        new_div.append(element)
                section.insert_after(new_div)
        else:
            # Replace section content
            # Preserve the section tag and its attributes
            section.clear()
            
            # Add new content
            for element in new_soup:
                if isinstance(element, Tag):
                    section.append(element)
        
        # Preserve styling
        self.preserve_styling()
        
        self.logger.info(f"Successfully updated section: {section_id}")
    
    def remove_unverified_content(self, section_id: str) -> List[str]:
        """
        Remove content that cannot be verified with logging.
        
        Searches for content marked as unverified or lacking code references.
        Logs all removed content for review.
        
        Args:
            section_id: Section identifier to search within
            
        Returns:
            List of removed content descriptions
        """
        self.logger.info(f"Removing unverified content from section: {section_id}")
        
        removed = []
        
        # Find the section
        section = self.find_section(section_id)
        
        if not section:
            self.logger.warning(f"Section not found for cleanup: {section_id}")
            return removed
        
        # Find elements marked as unverified
        unverified_indicators = [
            'unverified',
            'needs verification',
            'TBD',
            'to be determined',
            'dev confirmed',  # Remove "Dev Confirmed" claims without code refs
        ]
        
        # Search for text containing unverified indicators
        for element in section.find_all(string=True):
            if isinstance(element, NavigableString):
                text_lower = str(element).lower()
                
                for indicator in unverified_indicators:
                    if indicator in text_lower:
                        # Get parent element
                        parent = element.find_parent()
                        if parent:
                            # Log the removed content
                            removed_text = parent.get_text(strip=True)
                            removed.append(removed_text)
                            
                            # Add HTML comment before removing
                            comment = Comment(
                                f" REMOVED: {removed_text[:100]}... "
                                f"Reason: Unverified content. "
                            )
                            parent.insert_before(comment)
                            
                            # Remove the element
                            parent.decompose()
                            
                            self.logger.info(
                                f"Removed unverified content: {removed_text[:50]}..."
                            )
                            
                            # Track removal
                            self.removed_content.append({
                                'section': section_id,
                                'content': removed_text,
                                'reason': f'Contains indicator: {indicator}'
                            })
                            
                            break
        
        # Find elements without code references
        # Look for claims that should have code references but don't
        claim_indicators = [
            'formula',
            'calculation',
            'algorithm',
            'mechanic',
            'system',
        ]
        
        for element in section.find_all(['p', 'div', 'li']):
            text_lower = element.get_text().lower()
            
            # Check if element makes a claim
            has_claim = any(indicator in text_lower for indicator in claim_indicators)
            
            if has_claim:
                # Check if element has a code reference
                has_code_ref = (
                    element.find('a', class_='code-ref') is not None or
                    element.find(text=re.compile(r'line \d+', re.IGNORECASE)) is not None or
                    element.find('code') is not None
                )
                
                if not has_code_ref:
                    # This is a claim without verification
                    removed_text = element.get_text(strip=True)
                    
                    # Add warning instead of removing (less aggressive)
                    warning = self.soup.new_tag('span', **{'class': 'unverified-warning'})
                    warning.string = ' ⚠️ [Unverified - no code reference]'
                    element.append(warning)
                    
                    self.logger.warning(
                        f"Marked as unverified (no code ref): {removed_text[:50]}..."
                    )
                    
                    # Track for reporting
                    self.removed_content.append({
                        'section': section_id,
                        'content': removed_text,
                        'reason': 'No code reference found'
                    })
        
        self.logger.info(
            f"Removed/marked {len(removed)} unverified items from {section_id}"
        )
        
        return removed
    
    def preserve_styling(self) -> None:
        """
        Ensure CSS classes and structure are maintained.
        
        Restores original CSS classes and validates structure integrity.
        """
        self.logger.info("Preserving styling and structure")
        
        # Restore original classes where stored
        for section_id, classes in self.original_classes.items():
            section = self.find_section(section_id)
            if section:
                # Merge original classes with any new classes
                current_classes = section.get('class', [])
                merged_classes = list(set(classes + current_classes))
                section['class'] = merged_classes
        
        # Ensure responsive classes are present
        responsive_classes = ['container', 'row', 'col', 'responsive']
        
        for cls in responsive_classes:
            elements = self.soup.find_all(class_=cls)
            for element in elements:
                # Verify class is still present
                if cls not in element.get('class', []):
                    element['class'] = element.get('class', []) + [cls]
        
        # Ensure navigation structure is intact
        nav = self.soup.find('nav')
        if nav:
            # Verify nav has proper structure
            if not nav.find('ul'):
                self.logger.warning("Navigation missing <ul> structure")
        
        # Ensure footer is intact
        footer = self.soup.find('footer')
        if not footer:
            self.logger.warning("Footer element not found")
        
        self.logger.info("Styling preservation complete")
    
    def save(self, output_path: Optional[str] = None) -> None:
        """
        Save updated HTML.
        
        Args:
            output_path: Optional output path (defaults to original path)
        """
        save_path = Path(output_path) if output_path else self.html_path
        
        self.logger.info(f"Saving updated HTML to: {save_path}")
        
        # Ensure output directory exists
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Format HTML with proper indentation
        html_output = self.soup.prettify()
        
        # Write to file
        try:
            with open(save_path, 'w', encoding='utf-8') as f:
                f.write(html_output)
            
            self.logger.info(f"Successfully saved HTML: {save_path}")
        except Exception as e:
            self.logger.error(f"Failed to save HTML: {e}")
            raise HTMLUpdateException(
                f"Failed to save HTML file: {save_path}",
                {"error": str(e)}
            )
    
    def get_removed_content_report(self) -> str:
        """
        Generate report of removed content.
        
        Returns:
            Markdown-formatted report of removed content
        """
        if not self.removed_content:
            return "No content was removed."
        
        report_lines = [
            "# Removed Content Report",
            f"\nTotal items removed/marked: {len(self.removed_content)}\n",
        ]
        
        # Group by section
        by_section: Dict[str, List[Dict[str, str]]] = {}
        for item in self.removed_content:
            section = item['section']
            if section not in by_section:
                by_section[section] = []
            by_section[section].append(item)
        
        # Generate report by section
        for section, items in by_section.items():
            report_lines.append(f"## Section: {section}\n")
            report_lines.append(f"Items: {len(items)}\n")
            
            for i, item in enumerate(items, 1):
                report_lines.append(f"### Item {i}")
                report_lines.append(f"**Reason:** {item['reason']}")
                report_lines.append(f"**Content:** {item['content'][:200]}...")
                report_lines.append("")
        
        return '\n'.join(report_lines)
    
    def add_section(self, section_id: str, content: str, after: Optional[str] = None) -> None:
        """
        Add a new section to the HTML.
        
        Args:
            section_id: ID for the new section
            content: HTML content for the section
            after: Optional section ID to insert after (defaults to end of body)
        """
        self.logger.info(f"Adding new section: {section_id}")
        
        # Parse new content
        new_soup = BeautifulSoup(content, 'html.parser')
        
        # Create section container
        new_section = self.soup.new_tag('section', id=section_id)
        
        # Add content to section
        for element in new_soup:
            if isinstance(element, Tag):
                new_section.append(element)
        
        # Find insertion point
        if after:
            after_section = self.find_section(after)
            if after_section:
                after_section.insert_after(new_section)
                self.logger.info(f"Inserted section after: {after}")
            else:
                self.logger.warning(f"After section not found: {after}, appending to body")
                self.soup.body.append(new_section)
        else:
            # Append to body (before footer if exists)
            footer = self.soup.find('footer')
            if footer:
                footer.insert_before(new_section)
            else:
                self.soup.body.append(new_section)
        
        self.logger.info(f"Successfully added section: {section_id}")
    
    def update_navigation(self, section_id: str, section_title: str) -> None:
        """
        Update navigation menu to include new section.
        
        Args:
            section_id: ID of the section
            section_title: Display title for navigation
        """
        self.logger.info(f"Updating navigation for section: {section_id}")
        
        # Find navigation
        nav = self.soup.find('nav')
        if not nav:
            self.logger.warning("Navigation not found, cannot update")
            return
        
        # Find navigation list
        nav_list = nav.find('ul')
        if not nav_list:
            self.logger.warning("Navigation list not found, cannot update")
            return
        
        # Check if link already exists
        existing_link = nav_list.find('a', href=f'#{section_id}')
        if existing_link:
            self.logger.info(f"Navigation link already exists for: {section_id}")
            return
        
        # Create new navigation item
        new_item = self.soup.new_tag('li')
        new_link = self.soup.new_tag('a', href=f'#{section_id}')
        new_link.string = section_title
        new_item.append(new_link)
        
        # Append to navigation list
        nav_list.append(new_item)
        
        self.logger.info(f"Added navigation link for: {section_id}")
