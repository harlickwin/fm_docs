"""
Knowledge Gap Tracker for mechanics cleanup extraction.

Maintains a comprehensive list of information we couldn't verify from code,
following the zero-hallucination policy.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from pathlib import Path
from enum import Enum


class GapPriority(Enum):
    """Priority levels for knowledge gaps."""
    HIGH = "HIGH"  # Critical for documentation, affects major mechanics
    MEDIUM = "MEDIUM"  # Important but not critical, affects specific features
    LOW = "LOW"  # Nice to have, minor impact


@dataclass
class KnowledgeGap:
    """Represents a piece of information we couldn't verify from code."""
    category: str  # "guild_war", "dungeon", "pvp", "shop", "combat", "rng"
    title: str  # Short description
    description: str  # Detailed explanation of what's missing
    searched_patterns: List[str]  # What we searched for
    searched_locations: List[str]  # Where we searched (file paths, line ranges)
    potential_sources: List[str]  # Where this info might exist
    impact: GapPriority  # How important is this gap
    related_mechanics: List[str]  # What mechanics are affected
    notes: str = ""  # Additional context
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


class KnowledgeGapTracker:
    """Tracks all knowledge gaps during extraction."""
    
    def __init__(self):
        """Initialize the knowledge gap tracker."""
        self.gaps: List[KnowledgeGap] = []
        self.search_stats = {
            "total_searches": 0,
            "found": 0,
            "not_found": 0,
            "partial": 0
        }
    
    def add_gap(self, gap: KnowledgeGap) -> None:
        """
        Add a knowledge gap to the tracker.
        
        Args:
            gap: KnowledgeGap instance
        """
        self.gaps.append(gap)
        self.search_stats["not_found"] += 1
    
    def record_search(self, found: bool, partial: bool = False) -> None:
        """
        Record a search attempt.
        
        Args:
            found: Whether the search found what it was looking for
            partial: Whether the search found a partial match
        """
        self.search_stats["total_searches"] += 1
        if found:
            self.search_stats["found"] += 1
        if partial:
            self.search_stats["partial"] += 1
    
    def get_gaps_by_category(self, category: str) -> List[KnowledgeGap]:
        """
        Get all gaps for a specific category.
        
        Args:
            category: Category name
            
        Returns:
            List of KnowledgeGap instances
        """
        return [gap for gap in self.gaps if gap.category == category]
    
    def get_gaps_by_priority(self, priority: GapPriority) -> List[KnowledgeGap]:
        """
        Get all gaps with a specific priority.
        
        Args:
            priority: GapPriority enum value
            
        Returns:
            List of KnowledgeGap instances
        """
        return [gap for gap in self.gaps if gap.impact == priority]
    
    def get_gap_statistics(self) -> Dict[str, int]:
        """
        Get statistics about knowledge gaps.
        
        Returns:
            Dictionary with gap statistics
        """
        return {
            "total_gaps": len(self.gaps),
            "high_priority": len(self.get_gaps_by_priority(GapPriority.HIGH)),
            "medium_priority": len(self.get_gaps_by_priority(GapPriority.MEDIUM)),
            "low_priority": len(self.get_gaps_by_priority(GapPriority.LOW)),
            "by_category": {
                category: len(self.get_gaps_by_category(category))
                for category in ["guild_war", "dungeon", "pvp", "shop", "combat", "rng"]
            }
        }
    
    def generate_summary(self) -> str:
        """
        Generate markdown summary of all knowledge gaps.
        
        Returns:
            Markdown-formatted string
        """
        stats = self.get_gap_statistics()
        
        md = "# Knowledge Gaps Summary\n\n"
        md += f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        md += "## Overview\n\n"
        md += "This document tracks all information we attempted to find but could not verify from code.\n\n"
        
        md += "## Statistics\n\n"
        md += f"- **Total Gaps**: {stats['total_gaps']}\n"
        md += f"- **High Priority**: {stats['high_priority']}\n"
        md += f"- **Medium Priority**: {stats['medium_priority']}\n"
        md += f"- **Low Priority**: {stats['low_priority']}\n\n"
        
        md += "### By Category\n\n"
        for category, count in stats['by_category'].items():
            md += f"- **{category.replace('_', ' ').title()}**: {count}\n"
        md += "\n"
        
        # High priority gaps
        high_gaps = self.get_gaps_by_priority(GapPriority.HIGH)
        if high_gaps:
            md += "## High Priority Gaps\n\n"
            for gap in high_gaps:
                md += self._format_gap(gap)
        
        # Medium priority gaps
        medium_gaps = self.get_gaps_by_priority(GapPriority.MEDIUM)
        if medium_gaps:
            md += "## Medium Priority Gaps\n\n"
            for gap in medium_gaps:
                md += self._format_gap(gap)
        
        # Low priority gaps
        low_gaps = self.get_gaps_by_priority(GapPriority.LOW)
        if low_gaps:
            md += "## Low Priority Gaps\n\n"
            for gap in low_gaps:
                md += self._format_gap(gap)
        
        # Search summary
        md += "## Search Summary\n\n"
        md += f"**Total Searches**: {self.search_stats['total_searches']}\n\n"
        md += f"**Found**: {self.search_stats['found']}\n\n"
        md += f"**Not Found**: {self.search_stats['not_found']}\n\n"
        md += f"**Partial Matches**: {self.search_stats['partial']}\n\n"
        
        if self.search_stats['total_searches'] > 0:
            success_rate = (self.search_stats['found'] / self.search_stats['total_searches']) * 100
            md += f"**Success Rate**: {success_rate:.1f}%\n\n"
        
        # Most common missing data
        md += "## Most Common Missing Data\n\n"
        missing_types = self._categorize_missing_data()
        for missing_type, count in sorted(missing_types.items(), key=lambda x: x[1], reverse=True):
            md += f"- **{missing_type}**: {count} instances\n"
        md += "\n"
        
        # Next steps
        md += "## Next Steps\n\n"
        md += self._generate_next_steps()
        
        return md
    
    def _format_gap(self, gap: KnowledgeGap) -> str:
        """Format a single gap as markdown."""
        md = f"### {gap.category.replace('_', ' ').title()}: {gap.title}\n\n"
        md += f"**Status**: UNVERIFIED\n\n"
        
        md += "**Searched For**:\n\n"
        for pattern in gap.searched_patterns:
            md += f"- Pattern: `{pattern}`\n"
        for location in gap.searched_locations:
            md += f"- Location: {location}\n"
        md += "\n"
        
        md += "**What's Missing**:\n\n"
        md += f"{gap.description}\n\n"
        
        if gap.potential_sources:
            md += "**Potential Sources**:\n\n"
            for source in gap.potential_sources:
                md += f"- {source}\n"
            md += "\n"
        
        md += f"**Impact**: {gap.impact.value} - "
        if gap.related_mechanics:
            md += f"Affects {', '.join(gap.related_mechanics)}\n\n"
        else:
            md += "Impact on mechanics unclear\n\n"
        
        if gap.notes:
            md += f"**Notes**: {gap.notes}\n\n"
        
        md += "---\n\n"
        return md
    
    def _categorize_missing_data(self) -> Dict[str, int]:
        """Categorize types of missing data."""
        categories = {}
        for gap in self.gaps:
            # Simple categorization based on description keywords
            desc_lower = gap.description.lower()
            if "config" in desc_lower or "value" in desc_lower:
                categories["Configuration values"] = categories.get("Configuration values", 0) + 1
            elif "server" in desc_lower:
                categories["Server-side logic"] = categories.get("Server-side logic", 0) + 1
            elif "native" in desc_lower or "arm" in desc_lower:
                categories["Native code implementations"] = categories.get("Native code implementations", 0) + 1
            elif "formula" in desc_lower or "calculation" in desc_lower:
                categories["Formula details"] = categories.get("Formula details", 0) + 1
            else:
                categories["Other"] = categories.get("Other", 0) + 1
        return categories
    
    def _generate_next_steps(self) -> str:
        """Generate suggested next steps based on gaps."""
        md = ""
        
        # Check for common patterns
        has_config_gaps = any("config" in gap.description.lower() for gap in self.gaps)
        has_native_gaps = any("native" in gap.description.lower() or "arm" in gap.description.lower() for gap in self.gaps)
        has_server_gaps = any("server" in gap.description.lower() for gap in self.gaps)
        
        step_num = 1
        
        if has_config_gaps:
            md += f"{step_num}. **Analyze .mpa config files** - May contain missing configuration values\n"
            step_num += 1
        
        if has_native_gaps:
            md += f"{step_num}. **Analyze ARM code in libil2cpp.so** - May contain native implementations\n"
            step_num += 1
        
        if has_server_gaps:
            md += f"{step_num}. **Decompile server code** - If accessible, may reveal server-side logic\n"
            step_num += 1
        
        md += f"{step_num}. **Test in-game** - Empirically determine missing values through gameplay testing\n"
        step_num += 1
        
        md += f"{step_num}. **Review game updates** - Check if newer versions expose more information\n"
        
        return md
    
    def export_to_file(self, output_path: str) -> None:
        """
        Export knowledge gaps to a markdown file.
        
        Args:
            output_path: Path to output file
        """
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        content = self.generate_summary()
        output_file.write_text(content, encoding='utf-8')
        
        print(f"Knowledge gaps exported to: {output_path}")
    
    def clear(self) -> None:
        """Clear all gaps and reset statistics."""
        self.gaps.clear()
        self.search_stats = {
            "total_searches": 0,
            "found": 0,
            "not_found": 0,
            "partial": 0
        }


# Global tracker instance
_tracker: Optional[KnowledgeGapTracker] = None


def get_tracker() -> KnowledgeGapTracker:
    """Get or create the global tracker instance."""
    global _tracker
    if _tracker is None:
        _tracker = KnowledgeGapTracker()
    return _tracker


def init_tracker() -> KnowledgeGapTracker:
    """
    Initialize a new global tracker instance.
    
    Returns:
        Initialized tracker instance
    """
    global _tracker
    _tracker = KnowledgeGapTracker()
    return _tracker
