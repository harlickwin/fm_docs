"""Main extraction pipeline orchestrator."""

import json
import time
from pathlib import Path
from typing import Dict, Optional
from extraction_system.core.config import ExtractionConfig
from extraction_system.core.base import GameMechanic, ExtractionProgress
from extraction_system.core.logger import ProgressLogger
from extraction_system.parsers.il2cpp_parser import IL2CPPParser
from extraction_system.mappers.address_mapper import AddressMapper
from extraction_system.extractors.function_extractor import FunctionExtractor
from extraction_system.extractors.pattern_finder import PatternFinder
from extraction_system.analyzers.combat_analyzer import CombatAnalyzer
from extraction_system.analyzers.summoning_analyzer import SummoningAnalyzer
from extraction_system.analyzers.pvp_analyzer import PvPAnalyzer
from extraction_system.analyzers.progression_analyzer import ProgressionAnalyzer
from extraction_system.analyzers.economy_analyzer import EconomyAnalyzer
from extraction_system.verification.verification_engine import VerificationEngine
from extraction_system.documentation.doc_generator import DocumentationGenerator


class ExtractionPipeline:
    """Orchestrates the complete extraction process."""
    
    def __init__(self, config: ExtractionConfig):
        self.config = config
        self.logger = ProgressLogger("ExtractionPipeline", config.log_file, config.log_level)
        self.progress = ExtractionProgress()
        self.all_mechanics: Dict[str, GameMechanic] = {}
        
        # Initialize components
        self.il2cpp_parser: Optional[IL2CPPParser] = None
        self.address_mapper: Optional[AddressMapper] = None
        self.function_extractor: Optional[FunctionExtractor] = None
        self.pattern_finder: Optional[PatternFinder] = None
        self.verification_engine: Optional[VerificationEngine] = None
        self.doc_generator: Optional[DocumentationGenerator] = None
    
    def run(self):
        """Run the complete extraction pipeline."""
        self.logger.section("GAME MECHANICS EXTRACTION PIPELINE")
        self.logger.info("Starting autonomous extraction process")
        
        self.progress.start_time = time.time()
        self.progress.total_systems = len(self.config.priority_systems)
        
        try:
            # Step 1: Initialize components
            self._initialize_components()
            
            # Step 2: Parse IL2CPP dump
            self._parse_il2cpp()
            
            # Step 3: Build address mapping
            self._build_address_mapping()
            
            # Step 4: Extract mechanics for each system
            self._extract_all_systems()
            
            # Step 5: Verify mechanics
            self._verify_mechanics()
            
            # Step 6: Generate documentation
            self._generate_documentation()
            
            # Step 7: Generate summary
            self._generate_summary()
            
            self.logger.section("EXTRACTION COMPLETE")
            
        except Exception as e:
            self.logger.error(f"Pipeline error: {e}")
            self.progress.errors.append(str(e))
            raise
    
    def _initialize_components(self):
        """Initialize all pipeline components."""
        self.logger.section("Initializing Components")
        
        self.il2cpp_parser = IL2CPPParser(self.config.il2cpp_dump_path, self.logger)
        self.function_extractor = FunctionExtractor(self.config.ghidra_export_path, self.logger)
        self.pattern_finder = PatternFinder(self.config.ghidra_export_path, self.logger)
        self.verification_engine = VerificationEngine(self.logger)
        self.doc_generator = DocumentationGenerator(self.config.output_manual_path, self.logger)
        
        self.logger.info("All components initialized")
    
    def _parse_il2cpp(self):
        """Parse IL2CPP dump."""
        self.logger.section("Step 1: Parsing IL2CPP Dump")
        
        # Check cache
        cache_path = Path(self.config.il2cpp_cache_path)
        if self.config.use_cache and cache_path.exists():
            self.logger.info("Loading IL2CPP data from cache")
            # Would load from cache here
        
        self.il2cpp_parser.parse()
        
        # Save cache
        if self.config.use_cache:
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            # Would save to cache here
    
    def _build_address_mapping(self):
        """Build address mapping."""
        self.logger.section("Step 2: Building Address Mapping")
        
        self.address_mapper = AddressMapper(self.il2cpp_parser, self.config.ghidra_export_path, self.logger)
        
        # Check cache
        mapping_path = Path(self.config.address_mapping_path)
        if self.config.use_cache and mapping_path.exists():
            self.logger.info("Loading address mapping from cache")
            self.address_mapper.load_mapping(str(mapping_path))
        else:
            self.address_mapper.build_mapping()
            
            # Save cache
            if self.config.use_cache:
                self.address_mapper.save_mapping(self.config.address_mapping_path)
    
    def _extract_all_systems(self):
        """Extract mechanics for all game systems."""
        self.logger.section("Step 3: Extracting Game Mechanics")
        
        for i, system in enumerate(self.config.priority_systems):
            self.progress.current_system = system
            self.progress.completed_systems = i
            
            self.logger.section(f"Extracting {system} System ({i+1}/{self.progress.total_systems})")
            
            try:
                mechanics = self._extract_system(system)
                self.all_mechanics.update(mechanics)
                
                self.progress.completed_systems = i + 1
                self._save_checkpoint()
                
            except Exception as e:
                self.logger.error(f"Error extracting {system}: {e}")
                self.progress.errors.append(f"{system}: {e}")
                continue
    
    def _extract_system(self, system: str) -> Dict[str, GameMechanic]:
        """Extract mechanics for a specific system."""
        if system == "Combat":
            analyzer = CombatAnalyzer(
                self.il2cpp_parser, self.address_mapper,
                self.function_extractor, self.pattern_finder, self.logger
            )
            return analyzer.analyze_all()
        
        elif system == "Summoning":
            analyzer = SummoningAnalyzer(
                self.il2cpp_parser, self.address_mapper,
                self.function_extractor, self.pattern_finder, self.logger
            )
            return analyzer.analyze_all()
        
        elif system == "PvP":
            analyzer = PvPAnalyzer(
                self.il2cpp_parser, self.address_mapper,
                self.function_extractor, self.logger
            )
            return analyzer.analyze_all()
        
        elif system == "Progression":
            analyzer = ProgressionAnalyzer(
                self.il2cpp_parser, self.address_mapper,
                self.function_extractor, self.logger
            )
            return analyzer.analyze_all()
        
        elif system == "Economy":
            analyzer = EconomyAnalyzer(
                self.il2cpp_parser, self.address_mapper,
                self.function_extractor, self.logger
            )
            return analyzer.analyze_all()
        
        return {}
    
    def _verify_mechanics(self):
        """Verify all extracted mechanics."""
        self.logger.section("Step 4: Verifying Mechanics")
        
        if self.config.run_verification:
            self.verification_engine.verify_all_mechanics(self.all_mechanics)
        else:
            self.logger.info("Verification skipped (disabled in config)")
    
    def _generate_documentation(self):
        """Generate comprehensive documentation."""
        self.logger.section("Step 5: Generating Documentation")
        
        self.doc_generator.write_documentation(self.all_mechanics)
    
    def _generate_summary(self):
        """Generate extraction summary report."""
        self.logger.section("Extraction Summary")
        
        elapsed = time.time() - self.progress.start_time
        
        self.logger.info(f"Total mechanics extracted: {len(self.all_mechanics)}")
        self.logger.info(f"Systems processed: {self.progress.completed_systems}/{self.progress.total_systems}")
        self.logger.info(f"Errors encountered: {len(self.progress.errors)}")
        self.logger.info(f"Time elapsed: {elapsed/60:.1f} minutes")
        
        if self.progress.errors:
            self.logger.warning("Errors:")
            for error in self.progress.errors:
                self.logger.warning(f"  - {error}")
    
    def _save_checkpoint(self):
        """Save progress checkpoint."""
        checkpoint_path = Path(self.config.checkpoint_path)
        checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
        
        checkpoint_data = {
            'completed_systems': self.progress.completed_systems,
            'current_system': self.progress.current_system,
            'total_mechanics': len(self.all_mechanics),
            'errors': self.progress.errors,
            'timestamp': time.time()
        }
        
        with open(checkpoint_path, 'w') as f:
            json.dump(checkpoint_data, f, indent=2)
        
        self.logger.debug(f"Checkpoint saved: {checkpoint_path}")
