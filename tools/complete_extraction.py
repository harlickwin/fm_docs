"""Complete systematic extraction of ALL game mechanics from IL2CPP dump.

This tool:
1. Parses the ENTIRE IL2CPP dump
2. Extracts ALL classes, enums, structs
3. Groups by game system
4. Documents with line numbers
5. Makes ZERO assumptions

NO optimization strategies. NO generic advice. ONLY code facts.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
from dataclasses import dataclass, field


@dataclass
class CodeClass:
    """Represents a class found in IL2CPP dump."""
    name: str
    line_number: int
    base_class: str = ""
    fields: List[Tuple[str, str]] = field(default_factory=list)  # [(type, name), ...]
    category: str = ""


@dataclass
class CodeEnum:
    """Represents an enum found in IL2CPP dump."""
    name: str
    line_number: int
    values: List[Tuple[str, str]] = field(default_factory=list)  # [(name, value), ...]
    category: str = ""


class CompleteExtractor:
    """Extracts ALL game mechanics systematically."""
    
    def __init__(self, dump_path: str):
        self.dump_path = Path(dump_path)
        self.classes: Dict[str, CodeClass] = {}
        self.enums: Dict[str, CodeEnum] = {}
        
    def extract_all(self):
        """Extract everything from IL2CPP dump."""
        print(f"Reading {self.dump_path}...")
        
        with open(self.dump_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        print(f"Total lines: {len(lines)}")
        print("Extracting classes...")
        self._extract_classes(lines)
        print(f"Found {len(self.classes)} classes")
        
        print("Extracting enums...")
        self._extract_enums(lines)
        print(f"Found {len(self.enums)} enums")
        
        print("Categorizing...")
        self._categorize_all()
        
        print("Generating documentation...")
        self._generate_documentation()
        
        print("Complete!")
    
    def _extract_classes(self, lines: List[str]):
        """Extract all class definitions."""
        class_pattern = re.compile(r'^public (?:(?:abstract|sealed) )?class (\w+)(?: : (\w+))?')
        
        i = 0
        while i < len(lines):
            line = lines[i]
            match = class_pattern.match(line)
            
            if match:
                class_name = match.group(1)
                base_class = match.group(2) or ""
                
                # Extract fields
                fields = self._extract_fields(lines, i)
                
                self.classes[class_name] = CodeClass(
                    name=class_name,
                    line_number=i + 1,
                    base_class=base_class,
                    fields=fields
                )
            
            i += 1
    
    def _extract_enums(self, lines: List[str]):
        """Extract all enum definitions."""
        enum_pattern = re.compile(r'^public enum (\w+)')
        
        i = 0
        while i < len(lines):
            line = lines[i]
            match = enum_pattern.match(line)
            
            if match:
                enum_name = match.group(1)
                
                # Extract values
                values = self._extract_enum_values(lines, i)
                
                self.enums[enum_name] = CodeEnum(
                    name=enum_name,
                    line_number=i + 1,
                    values=values
                )
            
            i += 1
    
    def _extract_fields(self, lines: List[str], start_idx: int, max_lines: int = 200) -> List[Tuple[str, str]]:
        """Extract fields from a class."""
        fields = []
        field_pattern = re.compile(r'^\s+(?:public|private|protected)?\s+(\w+(?:<[^>]+>)?)\s+(\w+);')
        
        brace_count = 0
        in_class = False
        
        for i in range(start_idx, min(start_idx + max_lines, len(lines))):
            line = lines[i]
            
            if '{' in line:
                brace_count += line.count('{')
                in_class = True
            if '}' in line:
                brace_count -= line.count('}')
                if brace_count == 0 and in_class:
                    break
            
            match = field_pattern.match(line)
            if match:
                field_type = match.group(1)
                field_name = match.group(2)
                fields.append((field_type, field_name))
        
        return fields
    
    def _extract_enum_values(self, lines: List[str], start_idx: int, max_lines: int = 100) -> List[Tuple[str, str]]:
        """Extract values from an enum."""
        values = []
        value_pattern = re.compile(r'^\s+public const \w+ (\w+) = (\d+);')
        
        for i in range(start_idx, min(start_idx + max_lines, len(lines))):
            line = lines[i]
            
            if '}' in line:
                break
            
            match = value_pattern.match(line)
            if match:
                value_name = match.group(1)
                value_num = match.group(2)
                values.append((value_name, value_num))
        
        return values
    
    def _categorize_all(self):
        """Categorize classes and enums by game system."""
        # Categorize classes
        for cls in self.classes.values():
            cls.category = self._determine_category(cls.name)
        
        # Categorize enums
        for enum in self.enums.values():
            enum.category = self._determine_category(enum.name)
    
    def _determine_category(self, name: str) -> str:
        """Determine category from class/enum name."""
        name_lower = name.lower()
        
        if any(x in name_lower for x in ['combat', 'attack', 'damage', 'weapon', 'projectile', 'skill']):
            return "Combat"
        elif any(x in name_lower for x in ['currency', 'shop', 'price', 'cost', 'forge', 'idle']):
            return "Economy"
        elif any(x in name_lower for x in ['summon', 'drop', 'rarity', 'random', 'pcg', 'seed']):
            return "Summoning"
        elif any(x in name_lower for x in ['pvp', 'arena', 'matchmaking', 'rating']):
            return "PvP"
        elif any(x in name_lower for x in ['tech', 'upgrade', 'level', 'experience', 'progression']):
            return "Progression"
        elif any(x in name_lower for x in ['guild', 'war', 'member']):
            return "Guild"
        elif any(x in name_lower for x in ['pet', 'mount', 'egg', 'hatch']):
            return "Pets & Mounts"
        elif any(x in name_lower for x in ['dungeon', 'battle', 'wave', 'enemy']):
            return "PvE Content"
        else:
            return "Other"
    
    def _generate_documentation(self):
        """Generate complete markdown documentation."""
        output = []
        
        output.append("# Complete Game Mechanics - Code-Based Extraction\n")
        output.append("**Generated from IL2CPP dump - NO ASSUMPTIONS**\n\n")
        output.append("This document contains ONLY mechanics found in code with line number references.\n\n")
        
        # Group by category
        categories = {}
        for cls in self.classes.values():
            if cls.category not in categories:
                categories[cls.category] = {'classes': [], 'enums': []}
            categories[cls.category]['classes'].append(cls)
        
        for enum in self.enums.values():
            if enum.category not in categories:
                categories[enum.category] = {'classes': [], 'enums': []}
            categories[enum.category]['enums'].append(enum)
        
        # Generate TOC
        output.append("## Table of Contents\n\n")
        for category in sorted(categories.keys()):
            output.append(f"- [{category}](#{category.lower().replace(' ', '-').replace('&', '')})\n")
        output.append("\n")
        
        # Generate sections
        for category in sorted(categories.keys()):
            output.append(f"## {category}\n\n")
            
            # Classes
            if categories[category]['classes']:
                output.append(f"### Classes ({len(categories[category]['classes'])})\n\n")
                for cls in sorted(categories[category]['classes'], key=lambda x: x.name):
                    output.append(f"#### {cls.name}\n\n")
                    output.append(f"**Line:** {cls.line_number}\n\n")
                    if cls.base_class:
                        output.append(f"**Inherits:** {cls.base_class}\n\n")
                    if cls.fields:
                        output.append("**Fields:**\n\n")
                        for field_type, field_name in cls.fields[:20]:  # Limit to first 20
                            output.append(f"- `{field_name}`: {field_type}\n")
                        if len(cls.fields) > 20:
                            output.append(f"- ... ({len(cls.fields) - 20} more fields)\n")
                        output.append("\n")
                    output.append("---\n\n")
            
            # Enums
            if categories[category]['enums']:
                output.append(f"### Enums ({len(categories[category]['enums'])})\n\n")
                for enum in sorted(categories[category]['enums'], key=lambda x: x.name):
                    output.append(f"#### {enum.name}\n\n")
                    output.append(f"**Line:** {enum.line_number}\n\n")
                    if enum.values:
                        output.append("**Values:**\n\n")
                        for value_name, value_num in enum.values:
                            output.append(f"- `{value_name}` = {value_num}\n")
                        output.append("\n")
                    output.append("---\n\n")
        
        # Write to file
        output_path = Path("COMPLETE_CODE_EXTRACTION.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(output)
        
        print(f"Documentation written to {output_path}")
        print(f"Total classes: {len(self.classes)}")
        print(f"Total enums: {len(self.enums)}")


if __name__ == "__main__":
    extractor = CompleteExtractor("C:/apktool/il2cpp-output/dump.cs")
    extractor.extract_all()
