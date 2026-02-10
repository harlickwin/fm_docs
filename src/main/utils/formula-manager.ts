/**
 * Formula Configuration Manager
 * Manages game formula configurations
 */

import { app } from 'electron';
import * as fs from 'fs';
import * as path from 'path';
import { FormulaConfig, ValidationResult } from '../../shared/formula-types';

export class FormulaConfigManager {
  private formulasDir: string;

  constructor() {
    const userDataPath = app.getPath('userData');
    this.formulasDir = path.join(userDataPath, 'formulas');
    this.ensureDirectoryExists();
  }

  /**
   * Ensure formulas directory exists
   */
  private ensureDirectoryExists(): void {
    if (!fs.existsSync(this.formulasDir)) {
      fs.mkdirSync(this.formulasDir, { recursive: true });
    }
  }

  /**
   * Get default formula configuration
   */
  getDefault(): FormulaConfig {
    return {
      id: 'default-v1',
      name: 'Default Game Formulas',
      description: 'Standard game balance formulas',
      version: '1.0.0',
      createdAt: Date.now(),
      
      attackSpeedTiers: [
        { minPercent: 0, maxPercent: 25, attackInterval: 1.0 },
        { minPercent: 25, maxPercent: 50, attackInterval: 0.9 },
        { minPercent: 50, maxPercent: 75, attackInterval: 0.8 },
        { minPercent: 75, maxPercent: 100, attackInterval: 0.7 },
        { minPercent: 100, maxPercent: 150, attackInterval: 0.6 },
        { minPercent: 150, maxPercent: 200, attackInterval: 0.5 },
        { minPercent: 200, maxPercent: 300, attackInterval: 0.4 },
        { minPercent: 300, maxPercent: 400, attackInterval: 0.3 },
      ],
      
      doubleAttackDelays: {
        normal: 0.2,
        highAttackSpeed: 0.1,
      },
      
      criticalHit: {
        baseDamageMultiplier: 1.2,
      },
      
      meleeMovementDelay: 2.2,
      
      caps: {
        attackSpeed: 400,
        critChance: 100,
        doubleChance: 100,
      },
    };
  }

  /**
   * Load formula configuration by ID
   */
  async load(id: string): Promise<FormulaConfig | null> {
    try {
      // Check if it's the default
      if (id === 'default-v1') {
        return this.getDefault();
      }

      const filePath = path.join(this.formulasDir, `${id}.json`);
      
      if (!fs.existsSync(filePath)) {
        return null;
      }

      const content = fs.readFileSync(filePath, 'utf-8');
      const config = JSON.parse(content) as FormulaConfig;

      return config;
    } catch (error) {
      console.error('Error loading formula config:', error);
      return null;
    }
  }

  /**
   * Save formula configuration
   */
  async save(config: FormulaConfig): Promise<void> {
    try {
      // Validate before saving
      const validation = this.validate(config);
      if (!validation.valid) {
        throw new Error(`Invalid formula config: ${validation.errors.join(', ')}`);
      }

      const filePath = path.join(this.formulasDir, `${config.id}.json`);
      const content = JSON.stringify(config, null, 2);
      
      fs.writeFileSync(filePath, content, 'utf-8');
    } catch (error) {
      console.error('Error saving formula config:', error);
      throw error;
    }
  }

  /**
   * List all formula configurations
   */
  async list(): Promise<FormulaConfig[]> {
    try {
      const configs: FormulaConfig[] = [];

      // Always include default
      configs.push(this.getDefault());

      // Load custom configs
      if (!fs.existsSync(this.formulasDir)) {
        return configs;
      }

      const files = fs.readdirSync(this.formulasDir);
      
      for (const file of files) {
        if (file.endsWith('.json')) {
          const filePath = path.join(this.formulasDir, file);
          const content = fs.readFileSync(filePath, 'utf-8');
          const config = JSON.parse(content) as FormulaConfig;
          configs.push(config);
        }
      }

      return configs;
    } catch (error) {
      console.error('Error listing formula configs:', error);
      return [this.getDefault()];
    }
  }

  /**
   * Delete formula configuration
   */
  async delete(id: string): Promise<void> {
    try {
      // Cannot delete default
      if (id === 'default-v1') {
        throw new Error('Cannot delete default formula configuration');
      }

      const filePath = path.join(this.formulasDir, `${id}.json`);
      
      if (fs.existsSync(filePath)) {
        fs.unlinkSync(filePath);
      }
    } catch (error) {
      console.error('Error deleting formula config:', error);
      throw error;
    }
  }

  /**
   * Validate formula configuration
   */
  validate(config: FormulaConfig): ValidationResult {
    const errors: string[] = [];
    const warnings: string[] = [];

    // Check required fields
    if (!config.id) errors.push('ID is required');
    if (!config.name) errors.push('Name is required');
    if (!config.version) errors.push('Version is required');

    // Validate attack speed tiers
    if (!config.attackSpeedTiers || config.attackSpeedTiers.length === 0) {
      errors.push('At least one attack speed tier is required');
    } else {
      // Check for overlaps and gaps
      const sortedTiers = [...config.attackSpeedTiers].sort((a, b) => a.minPercent - b.minPercent);
      
      for (let i = 0; i < sortedTiers.length; i++) {
        const tier = sortedTiers[i];
        
        // Validate tier values
        if (tier.minPercent < 0) {
          errors.push(`Tier ${i + 1}: minPercent cannot be negative`);
        }
        if (tier.maxPercent <= tier.minPercent) {
          errors.push(`Tier ${i + 1}: maxPercent must be greater than minPercent`);
        }
        if (tier.attackInterval <= 0) {
          errors.push(`Tier ${i + 1}: attackInterval must be positive`);
        }

        // Check for gaps
        if (i > 0) {
          const prevTier = sortedTiers[i - 1];
          if (tier.minPercent > prevTier.maxPercent) {
            warnings.push(`Gap between tier ${i} and tier ${i + 1}`);
          }
          if (tier.minPercent < prevTier.maxPercent) {
            warnings.push(`Overlap between tier ${i} and tier ${i + 1}`);
          }
        }
      }
    }

    // Validate double attack delays
    if (!config.doubleAttackDelays) {
      errors.push('Double attack delays are required');
    } else {
      if (config.doubleAttackDelays.normal <= 0) {
        errors.push('Normal double attack delay must be positive');
      }
      if (config.doubleAttackDelays.highAttackSpeed <= 0) {
        errors.push('High attack speed double attack delay must be positive');
      }
      if (config.doubleAttackDelays.highAttackSpeed > config.doubleAttackDelays.normal) {
        warnings.push('High attack speed delay is greater than normal delay');
      }
    }

    // Validate critical hit config
    if (!config.criticalHit) {
      errors.push('Critical hit configuration is required');
    } else {
      if (config.criticalHit.baseDamageMultiplier <= 1.0) {
        warnings.push('Critical damage multiplier should be greater than 1.0');
      }
      if (config.criticalHit.baseDamageMultiplier > 5.0) {
        warnings.push('Critical damage multiplier seems very high (>5.0)');
      }
    }

    // Validate melee movement delay
    if (config.meleeMovementDelay <= 0) {
      errors.push('Melee movement delay must be positive');
    }
    if (config.meleeMovementDelay > 10) {
      warnings.push('Melee movement delay seems very high (>10)');
    }

    // Validate caps
    if (!config.caps) {
      errors.push('Stat caps are required');
    } else {
      if (config.caps.attackSpeed <= 0) {
        errors.push('Attack speed cap must be positive');
      }
      if (config.caps.critChance <= 0 || config.caps.critChance > 100) {
        errors.push('Crit chance cap must be between 0 and 100');
      }
      if (config.caps.doubleChance <= 0 || config.caps.doubleChance > 100) {
        errors.push('Double chance cap must be between 0 and 100');
      }
    }

    return {
      valid: errors.length === 0,
      errors,
      warnings,
    };
  }

  /**
   * Create a new formula configuration from default
   */
  createFromDefault(name: string, description: string): FormulaConfig {
    const defaultConfig = this.getDefault();
    const id = `custom-${Date.now()}`;

    return {
      ...defaultConfig,
      id,
      name,
      description,
      createdAt: Date.now(),
    };
  }

  /**
   * Duplicate an existing configuration
   */
  async duplicate(sourceId: string, newName: string): Promise<FormulaConfig | null> {
    try {
      const source = await this.load(sourceId);
      if (!source) {
        return null;
      }

      const newId = `custom-${Date.now()}`;
      const duplicated: FormulaConfig = {
        ...source,
        id: newId,
        name: newName,
        description: `Copy of ${source.name}`,
        createdAt: Date.now(),
      };

      await this.save(duplicated);
      return duplicated;
    } catch (error) {
      console.error('Error duplicating formula config:', error);
      return null;
    }
  }

  /**
   * Export formula configuration to JSON string
   */
  export(config: FormulaConfig): string {
    return JSON.stringify(config, null, 2);
  }

  /**
   * Import formula configuration from JSON string
   */
  import(jsonString: string): FormulaConfig | null {
    try {
      const config = JSON.parse(jsonString) as FormulaConfig;
      
      // Validate imported config
      const validation = this.validate(config);
      if (!validation.valid) {
        console.error('Invalid imported config:', validation.errors);
        return null;
      }

      // Generate new ID to avoid conflicts
      config.id = `imported-${Date.now()}`;
      config.createdAt = Date.now();

      return config;
    } catch (error) {
      console.error('Error importing formula config:', error);
      return null;
    }
  }
}
