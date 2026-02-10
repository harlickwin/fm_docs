"""Command-line interface for extraction system."""

import argparse
import sys
from pathlib import Path
from extraction_system.core.config import ExtractionConfig
from extraction_system.pipeline.extraction_pipeline import ExtractionPipeline


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Game Mechanics Extraction System - Extract and document all game mechanics"
    )
    
    parser.add_argument(
        '--config',
        type=str,
        default='extraction_system/config.yaml',
        help='Path to configuration file (default: extraction_system/config.yaml)'
    )
    
    parser.add_argument(
        '--mode',
        type=str,
        choices=['full', 'single', 'resume', 'verify'],
        default='full',
        help='Extraction mode (default: full)'
    )
    
    parser.add_argument(
        '--system',
        type=str,
        choices=['Combat', 'Summoning', 'PvP', 'Progression', 'Economy'],
        help='Single system to extract (for single mode)'
    )
    
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help='Disable caching'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Error: Configuration file not found: {config_path}")
        sys.exit(1)
    
    try:
        config = ExtractionConfig.from_yaml(str(config_path))
        
        # Override config with CLI args
        if args.no_cache:
            config.use_cache = False
        
        if args.verbose:
            config.log_level = "DEBUG"
        
        if args.mode == 'single' and args.system:
            config.priority_systems = [args.system]
        
        # Run pipeline
        pipeline = ExtractionPipeline(config)
        pipeline.run()
        
        print("\n✓ Extraction complete!")
        print(f"Documentation written to: {config.output_manual_path}")
        
    except Exception as e:
        print(f"\n✗ Extraction failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
