"""Documentation generator for game mechanics manual."""

from typing import Dict, List
from pathlib import Path
from datetime import datetime
from extraction_system.core.base import GameMechanic, ConfidenceLevel
from extraction_system.core.logger import ProgressLogger


class DocumentationGenerator:
    """Generates comprehensive markdown documentation."""
    
    def __init__(self, output_file: str, logger: ProgressLogger = None):
        self.output_file = Path(output_file)
        self.logger = logger or ProgressLogger("DocumentationGenerator")
        self.sections: List[Dict[str, any]] = []
    
    def add_section(self, title: str, content: str, confidence: ConfidenceLevel = None):
        """Add a section to the documentation."""
        self.sections.append({
            'title': title,
            'content': content,
            'confidence': confidence
        })
    
    def generate_table_of_contents(self, mechanics_by_category: Dict[str, List[GameMechanic]]) -> str:
        """Generate TOC with links."""
        toc = "## Table of Contents\n\n"
        
        for category in mechanics_by_category.keys():
            toc += f"- [{category}](#{category.lower().replace(' ', '-')})\n"
        
        toc += "\n"
        return toc
    
    def generate_status_section(self, mechanics_by_category: Dict[str, List[GameMechanic]]) -> str:
        """Generate extraction progress status."""
        status = "## Extraction Status\n\n"
        status += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        status += "| Category | Mechanics Extracted | High Confidence | Medium Confidence | Low Confidence |\n"
        status += "|----------|---------------------|-----------------|-------------------|----------------|\n"
        
        for category, mechanics in mechanics_by_category.items():
            total = len(mechanics)
            high = sum(1 for m in mechanics if m.confidence == ConfidenceLevel.HIGH)
            medium = sum(1 for m in mechanics if m.confidence == ConfidenceLevel.MEDIUM)
            low = sum(1 for m in mechanics if m.confidence == ConfidenceLevel.LOW)
            
            status += f"| {category} | {total} | {high} | {medium} | {low} |\n"
        
        status += "\n"
        return status
    
    def format_mechanic(self, mechanic: GameMechanic) -> str:
        """Format a single mechanic."""
        doc = f"### {mechanic.name}\n\n"
        doc += f"**Description:** {mechanic.description}\n\n"
        
        if mechanic.formula:
            doc += f"**Formula:**\n```\n{mechanic.formula}\n```\n\n"
        
        doc += f"**Confidence Level:** {mechanic.confidence.value}\n\n"
        
        if mechanic.data_structures:
            doc += f"**Data Structures:** {', '.join(mechanic.data_structures)}\n\n"
        
        if mechanic.arm_code_location:
            doc += f"**ARM Code Location:** {mechanic.arm_code_location}\n\n"
        
        if mechanic.examples:
            doc += "**Examples:**\n\n"
            for example in mechanic.examples:
                doc += f"- **{example.get('description', 'Example')}**\n"
                if 'inputs' in example:
                    doc += f"  - Inputs: {example['inputs']}\n"
                if 'expected_output' in example:
                    doc += f"  - Expected Output: {example['expected_output']}\n"
            doc += "\n"
        
        if mechanic.notes:
            doc += "**Notes:**\n\n"
            for note in mechanic.notes:
                doc += f"- {note}\n"
            doc += "\n"
        
        doc += "---\n\n"
        return doc
    
    def write_documentation(self, all_mechanics: Dict[str, GameMechanic]):
        """Write complete documentation to file."""
        self.logger.section("Generating Documentation")
        
        # Group mechanics by category
        mechanics_by_category: Dict[str, List[GameMechanic]] = {}
        for mechanic in all_mechanics.values():
            category = mechanic.category
            if category not in mechanics_by_category:
                mechanics_by_category[category] = []
            mechanics_by_category[category].append(mechanic)
        
        # Build document
        doc = "# Complete Game Mechanics Manual\n\n"
        doc += "**Auto-generated documentation of all game mechanics**\n\n"
        doc += "This document contains comprehensive analysis of game mechanics extracted from decompiled code.\n\n"
        
        # Add TOC
        doc += self.generate_table_of_contents(mechanics_by_category)
        
        # Add status
        doc += self.generate_status_section(mechanics_by_category)
        
        # Add each category
        for category, mechanics in sorted(mechanics_by_category.items()):
            doc += f"## {category}\n\n"
            
            for mechanic in sorted(mechanics, key=lambda m: m.name):
                doc += self.format_mechanic(mechanic)
        
        # Write to file
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(doc)
        
        self.logger.info(f"Documentation written to {self.output_file}")
        self.logger.info(f"Total mechanics documented: {len(all_mechanics)}")
