"""
Unit tests for HTMLUpdater class.

Tests HTML parsing, section finding, content updating, unverified content removal,
and styling preservation.
"""

import pytest
import tempfile
from pathlib import Path
from extraction_system.mechanics_cleanup.html_updater import (
    HTMLUpdater,
    HTMLUpdateException,
)


class TestHTMLUpdater:
    """Test suite for HTMLUpdater."""
    
    @pytest.fixture
    def sample_html(self):
        """Create sample HTML content for testing."""
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Page</title>
    <style>
        .container { width: 100%; }
        .mechanic-card { padding: 10px; }
    </style>
</head>
<body>
    <nav>
        <ul>
            <li><a href="#section1">Section 1</a></li>
            <li><a href="#section2">Section 2</a></li>
        </ul>
    </nav>
    
    <section id="section1" class="container">
        <h2>Section 1</h2>
        <p>This is section 1 content.</p>
        <div class="mechanic-card">
            <p>Some mechanic info</p>
        </div>
    </section>
    
    <section id="section2" class="container">
        <h2>Section 2</h2>
        <p>This is section 2 content.</p>
        <p>Dev Confirmed: This is unverified content.</p>
        <p>This mechanic uses a formula but has no code reference.</p>
    </section>
    
    <h3>Guild War Matchmaking</h3>
    <div>
        <p>Guild war content here.</p>
    </div>
    
    <footer>
        <p>Footer content</p>
    </footer>
</body>
</html>
"""
    
    @pytest.fixture
    def temp_html_file(self, sample_html):
        """Create a temporary HTML file for testing."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(sample_html)
            temp_path = f.name
        
        yield temp_path
        
        # Cleanup
        Path(temp_path).unlink(missing_ok=True)
    
    @pytest.fixture
    def updater(self, temp_html_file):
        """Create an HTMLUpdater instance."""
        return HTMLUpdater(temp_html_file)
    
    def test_initialization(self, updater, temp_html_file):
        """Test HTMLUpdater initialization."""
        assert updater is not None
        assert updater.html_path == Path(temp_html_file)
        assert updater.soup is not None
        assert len(updater.removed_content) == 0
    
    def test_initialization_file_not_found(self):
        """Test initialization with non-existent file."""
        with pytest.raises(HTMLUpdateException):
            HTMLUpdater("nonexistent.html")
    
    def test_find_section_by_id(self, updater):
        """Test finding section by ID attribute."""
        section = updater.find_section("section1")
        
        assert section is not None
        assert section.name == "section"
        assert section.get('id') == "section1"
    
    def test_find_section_by_heading_text(self, updater):
        """Test finding section by heading text."""
        section = updater.find_section("Guild War Matchmaking")
        
        assert section is not None
        # Should return the heading or its parent
        assert section.name in ["h3", "div", "section"]
    
    def test_find_section_by_class(self, updater):
        """Test finding section by class name."""
        section = updater.find_section("container")
        
        assert section is not None
        assert "container" in section.get('class', [])
    
    def test_find_section_not_found(self, updater):
        """Test finding non-existent section."""
        section = updater.find_section("nonexistent-section")
        
        assert section is None
    
    def test_find_section_partial_match(self, updater):
        """Test finding section by partial heading match."""
        section = updater.find_section("Guild War")
        
        assert section is not None
    
    def test_update_section_by_id(self, updater):
        """Test updating section content by ID."""
        new_content = """
        <div class="updated-content">
            <p>This is updated content.</p>
            <p>With multiple paragraphs.</p>
        </div>
        """
        
        updater.update_section("section1", new_content)
        
        # Verify update
        section = updater.find_section("section1")
        assert section is not None
        
        content_text = section.get_text()
        assert "This is updated content" in content_text
        assert "With multiple paragraphs" in content_text
    
    def test_update_section_preserves_id(self, updater):
        """Test that updating section preserves the section ID."""
        new_content = "<p>New content</p>"
        
        updater.update_section("section1", new_content)
        
        # Verify ID is preserved
        section = updater.find_section("section1")
        assert section is not None
        assert section.get('id') == "section1"
    
    def test_update_section_not_found(self, updater):
        """Test updating non-existent section raises exception."""
        with pytest.raises(HTMLUpdateException):
            updater.update_section("nonexistent", "<p>Content</p>")
    
    def test_update_section_heading(self, updater):
        """Test updating content after a heading."""
        new_content = "<p>Updated guild war content</p>"
        
        updater.update_section("Guild War Matchmaking", new_content)
        
        # Verify update
        heading = updater.soup.find('h3', text='Guild War Matchmaking')
        assert heading is not None
        
        # Check next sibling has updated content
        next_sibling = heading.find_next_sibling()
        assert next_sibling is not None
        assert "Updated guild war content" in next_sibling.get_text()
    
    def test_remove_unverified_content(self, updater):
        """Test removing unverified content."""
        removed = updater.remove_unverified_content("section2")
        
        # Should have removed "Dev Confirmed" content
        assert len(removed) > 0
        
        # Verify content was removed
        section = updater.find_section("section2")
        content_text = section.get_text()
        
        # "Dev Confirmed" should be removed or commented
        # Check that it's not in visible text
        assert "Dev Confirmed" not in content_text or "REMOVED" in str(section)
    
    def test_remove_unverified_content_marks_no_code_ref(self, updater):
        """Test that content without code references is marked."""
        updater.remove_unverified_content("section2")
        
        # Verify that content without code ref is marked
        section = updater.find_section("section2")
        html_str = str(section)
        
        # Should have warning marker
        assert "unverified-warning" in html_str or "Unverified" in html_str
    
    def test_remove_unverified_content_section_not_found(self, updater):
        """Test removing unverified content from non-existent section."""
        removed = updater.remove_unverified_content("nonexistent")
        
        # Should return empty list
        assert len(removed) == 0
    
    def test_preserve_styling(self, updater):
        """Test that styling is preserved."""
        # Store original classes
        section = updater.find_section("section1")
        original_classes = section.get('class', [])
        
        # Update section
        updater.update_section("section1", "<p>New content</p>")
        
        # Preserve styling
        updater.preserve_styling()
        
        # Verify classes are preserved
        section = updater.find_section("section1")
        current_classes = section.get('class', [])
        
        # Original classes should still be present
        for cls in original_classes:
            assert cls in current_classes
    
    def test_preserve_styling_navigation(self, updater):
        """Test that navigation structure is preserved."""
        updater.preserve_styling()
        
        # Verify nav structure
        nav = updater.soup.find('nav')
        assert nav is not None
        
        nav_list = nav.find('ul')
        assert nav_list is not None
    
    def test_preserve_styling_footer(self, updater):
        """Test that footer is preserved."""
        updater.preserve_styling()
        
        # Verify footer exists
        footer = updater.soup.find('footer')
        assert footer is not None
    
    def test_save_to_original_path(self, updater, temp_html_file):
        """Test saving to original path."""
        updater.update_section("section1", "<p>Modified content</p>")
        updater.save()
        
        # Verify file was saved
        assert Path(temp_html_file).exists()
        
        # Verify content was saved
        with open(temp_html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "Modified content" in content
    
    def test_save_to_different_path(self, updater):
        """Test saving to different path."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            output_path = f.name
        
        try:
            updater.update_section("section1", "<p>Modified content</p>")
            updater.save(output_path)
            
            # Verify file was saved
            assert Path(output_path).exists()
            
            # Verify content
            with open(output_path, 'r', encoding='utf-8') as f:
                content = f.read()
                assert "Modified content" in content
        finally:
            Path(output_path).unlink(missing_ok=True)
    
    def test_get_removed_content_report(self, updater):
        """Test generating removed content report."""
        # Remove some content
        updater.remove_unverified_content("section2")
        
        # Generate report
        report = updater.get_removed_content_report()
        
        assert "Removed Content Report" in report
        assert "section2" in report.lower()
    
    def test_get_removed_content_report_empty(self, updater):
        """Test report when no content removed."""
        report = updater.get_removed_content_report()
        
        assert "No content was removed" in report
    
    def test_add_section(self, updater):
        """Test adding a new section."""
        new_content = """
        <h2>New Section</h2>
        <p>This is a new section.</p>
        """
        
        updater.add_section("new-section", new_content)
        
        # Verify section was added
        section = updater.find_section("new-section")
        assert section is not None
        assert section.get('id') == "new-section"
        assert "This is a new section" in section.get_text()
    
    def test_add_section_after_existing(self, updater):
        """Test adding section after existing section."""
        new_content = "<h2>Inserted Section</h2>"
        
        updater.add_section("inserted-section", new_content, after="section1")
        
        # Verify section was added after section1
        section1 = updater.find_section("section1")
        inserted = updater.find_section("inserted-section")
        
        assert section1 is not None
        assert inserted is not None
        
        # Check order (inserted should come after section1)
        all_sections = updater.soup.find_all('section')
        section1_index = all_sections.index(section1)
        inserted_index = all_sections.index(inserted)
        
        assert inserted_index > section1_index
    
    def test_add_section_before_footer(self, updater):
        """Test that new section is added before footer."""
        new_content = "<h2>Before Footer</h2>"
        
        updater.add_section("before-footer", new_content)
        
        # Verify section is before footer
        footer = updater.soup.find('footer')
        new_section = updater.find_section("before-footer")
        
        assert footer is not None
        assert new_section is not None
        
        # Check that new section comes before footer in document order
        all_elements = list(updater.soup.body.children)
        footer_index = all_elements.index(footer)
        section_index = all_elements.index(new_section)
        
        assert section_index < footer_index
    
    def test_update_navigation(self, updater):
        """Test updating navigation menu."""
        updater.update_navigation("new-section", "New Section")
        
        # Verify navigation was updated
        nav = updater.soup.find('nav')
        assert nav is not None
        
        new_link = nav.find('a', href='#new-section')
        assert new_link is not None
        assert new_link.get_text() == "New Section"
    
    def test_update_navigation_existing_link(self, updater):
        """Test updating navigation with existing link."""
        # Add link first time
        updater.update_navigation("section1", "Section 1")
        
        # Try adding again
        updater.update_navigation("section1", "Section 1")
        
        # Should not duplicate
        nav = updater.soup.find('nav')
        links = nav.find_all('a', href='#section1')
        
        # Should only have one link (the original)
        assert len(links) == 1
    
    def test_update_navigation_no_nav(self, updater):
        """Test updating navigation when nav doesn't exist."""
        # Remove nav
        nav = updater.soup.find('nav')
        if nav:
            nav.decompose()
        
        # Should not raise exception
        updater.update_navigation("test", "Test")
    
    def test_multiple_updates_preserve_structure(self, updater):
        """Test that multiple updates preserve HTML structure."""
        # Perform multiple updates
        updater.update_section("section1", "<p>Update 1</p>")
        updater.update_section("section2", "<p>Update 2</p>")
        updater.preserve_styling()
        
        # Verify structure is intact
        assert updater.soup.find('nav') is not None
        assert updater.soup.find('footer') is not None
        assert updater.find_section("section1") is not None
        assert updater.find_section("section2") is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
