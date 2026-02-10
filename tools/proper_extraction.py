"""Proper game mechanics extraction - focuses on Config/Model/Info classes only.

Extracts ONLY game mechanics, not framework/Unity classes.
Documents with line numbers and relationships.
NO assumptions. NO optimization strategies.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class GameClass:
    """A game mechanics class."""
    name: str
    line_number: int
    base_class: str = ""
    fields: List[Tuple[str, str]] = field(default_factory=list)
    category: str = ""
    
    def is_game_mechanics(self) -> bool:
        """Check if this is a game mechanics class (not framework)."""
        # Include: Config, Model, Info, Library, Action, State, Data
        # Exclude: View, Component, System (Unity/framework)
        mechanics_suffixes = ['Config', 'Model', 'Info', 'Library', 'Action', 'State', 'Data', 'Stats', 'Reward']
        framework_suffixes = ['View', 'Component', 'System', 'Controller', 'Manager', 'Service']
        
        # Check if it's a mechanics class
        if any(self.name.endswith(suffix) for suffix in mechanics_suffixes):
            return True
        
        # Exclude framework classes
        if any(self.name.endswith(suffix) for suffix in framework_suffixes):
            return False
        
        # Include if it has game-related keywords
        game_keywords = ['Player', 'Combat', 'Weapon', 'Skill', 'Pet', 'Mount', 'Guild', 'Arena', 'Dungeon']
        return any(keyword in self.name for keyword in game_keywords)


@dataclass
class GameEnum:
    """A game enum."""
    name: str
    line_number: int
    values: List[Tuple[str, str]] = field(default_factory=list)
    category: str = ""


class ProperExtractor:
    """Extracts game mechanics properly."""
    
    def __init__(self, dump_path: str):
        self.dump_path = Path(dump_path)
        self.classes: Dict[str, GameClass] = {}
        self.enums: Dict[str, GameEnum] = {}
        self.lines: List[str] = []
        
    def extract_all(self):
        """Extract all game mechanics."""
        print(f"Reading {self.dump_path}...")
        with open(self.dump_path, 'r', encoding='utf-8', errors='ignore') as f:
            self.lines = f.readlines()
        
        print(f"Total lines: {len(self.lines)}")
        
        print("Extracting classes...")
        self._extract_classes()
        
        # Filter to game mechanics only
        game_classes = {name: cls for name, cls in self.classes.items() if cls.is_game_mechanics()}
        self.classes = game_classes
        print(f"Found {len(self.classes)} game mechanics classes")
        
        print("Extracting enums...")
        self._extract_enums()
        print(f"Found {len(self.enums)} enums")
        
        print("Categorizing...")
        self._categorize_all()
        
        print("Generating manual...")
        self._generate_manual()
        
        print("Complete!")
    
    def _extract_classes(self):
        """Extract all class definitions."""
        class_pattern = re.compile(r'^public (?:(?:abstract|sealed) )?class (\w+)(?: : (\w+))?')
        
        for i, line in enumerate(self.lines):
            match = class_pattern.match(line)
            if match:
                class_name = match.group(1)
                base_class = match.group(2) or ""
                fields = self._extract_fields(i)
                
                self.classes[class_name] = GameClass(
                    name=class_name,
                    line_number=i + 1,
                    base_class=base_class,
                    fields=fields
                )
    
    def _extract_enums(self):
        """Extract all enum definitions."""
        enum_pattern = re.compile(r'^public enum (\w+)')
        
        for i, line in enumerate(self.lines):
            match = enum_pattern.match(line)
            if match:
                enum_name = match.group(1)
                values = self._extract_enum_values(i)
                
                self.enums[enum_name] = GameEnum(
                    name=enum_name,
                    line_number=i + 1,
                    values=values
                )
    
    def _extract_fields(self, start_idx: int, max_lines: int = 200) -> List[Tuple[str, str]]:
        """Extract fields from a class."""
        fields = []
        field_pattern = re.compile(r'^\s+(?:public|private|protected|internal)?\s+(?:\[[\w\(\),\s]+\]\s+)?(\w+(?:<[^>]+>)?)\s+(\w+);')
        backing_field_pattern = re.compile(r'<(\w+)>k__BackingField')
        
        brace_count = 0
        in_class = False
        seen_fields = set()
        
        for i in range(start_idx, min(start_idx + max_lines, len(self.lines))):
            line = self.lines[i]
            
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
                
                # Clean up backing field names
                backing_match = backing_field_pattern.match(field_name)
                if backing_match:
                    field_name = backing_match.group(1)
                
                # Avoid duplicates (backing fields and properties)
                if field_name not in seen_fields:
                    fields.append((field_type, field_name))
                    seen_fields.add(field_name)
        
        return fields
    
    def _extract_enum_values(self, start_idx: int, max_lines: int = 100) -> List[Tuple[str, str]]:
        """Extract values from an enum."""
        values = []
        value_pattern = re.compile(r'^\s+public const \w+ (\w+) = (\d+);')
        
        for i in range(start_idx, min(start_idx + max_lines, len(self.lines))):
            line = self.lines[i]
            
            if '}' in line:
                break
            
            match = value_pattern.match(line)
            if match:
                values.append((match.group(1), match.group(2)))
        
        return values
    
    def _categorize_all(self):
        """Categorize by game system."""
        for cls in self.classes.values():
            cls.category = self._determine_category(cls.name)
        
        for enum in self.enums.values():
            enum.category = self._determine_category(enum.name)
    
    def _determine_category(self, name: str) -> str:
        """Determine category from name."""
        name_lower = name.lower()
        
        categories = {
            "Combat": ['combat', 'attack', 'damage', 'weapon', 'projectile', 'skill', 'hp', 'health'],
            "Economy": ['currency', 'shop', 'price', 'cost', 'forge', 'idle', 'coin', 'gem'],
            "Summoning": ['summon', 'drop', 'rarity', 'random', 'pcg', 'seed', 'gacha'],
            "PvP": ['pvp', 'arena', 'matchmaking', 'rating', 'league'],
            "Progression": ['tech', 'upgrade', 'level', 'experience', 'progression', 'xp'],
            "Guild": ['guild', 'war', 'member', 'clan'],
            "Pets & Mounts": ['pet', 'mount', 'egg', 'hatch'],
            "PvE Content": ['dungeon', 'battle', 'wave', 'enemy', 'boss'],
        }
        
        for category, keywords in categories.items():
            if any(kw in name_lower for kw in keywords):
                return category
        
        return "Other"
    
    def _generate_manual(self):
        """Generate the proper game mechanics manual."""
        output = []
        
        # Header
        output.append("# Game Mechanics Manual\n\n")
        output.append("**Complete code-based extraction from IL2CPP dump**\n\n")
        output.append("This manual documents ONLY mechanics found in code.\n")
        output.append("Every entry includes line numbers for verification.\n")
        output.append("NO assumptions. NO optimization strategies. ONLY facts.\n\n")
        
        # Stats
        output.append(f"**Total Classes:** {len(self.classes)}\n")
        output.append(f"**Total Enums:** {len(self.enums)}\n\n")
        
        # Group by category
        categories = defaultdict(lambda: {'classes': [], 'enums': []})
        for cls in self.classes.values():
            categories[cls.category]['classes'].append(cls)
        for enum in self.enums.values():
            categories[enum.category]['enums'].append(enum)
        
        # TOC
        output.append("## Table of Contents\n\n")
        for category in sorted(categories.keys()):
            anchor = category.lower().replace(' ', '-').replace('&', '')
            output.append(f"- [{category}](#{anchor})\n")
        output.append("\n")
        
        # Generate sections
        for category in sorted(categories.keys()):
            self._generate_category_section(output, category, categories[category])
        
        # Write
        output_path = Path("GAME_MECHANICS_MANUAL.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.writelines(output)
        
        print(f"\nManual written to {output_path}")
        print(f"Classes documented: {len(self.classes)}")
        print(f"Enums documented: {len(self.enums)}")
    
    def _generate_category_section(self, output: List[str], category: str, items: Dict):
        """Generate a category section."""
        output.append(f"## {category}\n\n")
        
        # Summary
        num_classes = len(items['classes'])
        num_enums = len(items['enums'])
        output.append(f"**Classes:** {num_classes} | **Enums:** {num_enums}\n\n")
        
        # Enums first (they're usually simpler)
        if items['enums']:
            output.append("### Enumerations\n\n")
            for enum in sorted(items['enums'], key=lambda x: x.name):
                self._generate_enum_entry(output, enum)
        
        # Then classes
        if items['classes']:
            output.append("### Classes\n\n")
            for cls in sorted(items['classes'], key=lambda x: x.name):
                self._generate_class_entry(output, cls)
    
    def _generate_enum_entry(self, output: List[str], enum: GameEnum):
        """Generate an enum entry."""
        output.append(f"#### {enum.name}\n\n")
        output.append(f"**Line:** {enum.line_number}\n\n")
        
        if enum.values:
            output.append("**Values:**\n\n")
            output.append("```\n")
            for name, value in enum.values:
                output.append(f"{name} = {value}\n")
            output.append("```\n\n")
        
        output.append("---\n\n")
    
    def _generate_class_entry(self, output: List[str], cls: GameClass):
        """Generate a class entry."""
        output.append(f"#### {cls.name}\n\n")
        output.append(f"**Line:** {cls.line_number}\n\n")
        
        if cls.base_class:
            output.append(f"**Inherits:** {cls.base_class}\n\n")
        
        if cls.fields:
            output.append("**Fields:**\n\n")
            output.append("```\n")
            for field_type, field_name in cls.fields[:30]:  # Limit display
                output.append(f"{field_name}: {field_type}\n")
            if len(cls.fields) > 30:
                output.append(f"... ({len(cls.fields) - 30} more fields)\n")
            output.append("```\n\n")
        
        output.append("---\n\n")


if __name__ == "__main__":
    extractor = ProperExtractor("C:/apktool/il2cpp-output/dump.cs")
    extractor.extract_all()
