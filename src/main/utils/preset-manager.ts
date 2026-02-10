/**
 * Preset Manager
 * Handles saving, loading, and managing configuration presets
 */

import * as fs from 'fs/promises';
import * as path from 'path';
import { app } from 'electron';
import { ConfigPreset, TournamentConfig } from '../../shared/types';

export class PresetManager {
  private presetsDir: string;

  constructor() {
    this.presetsDir = path.join(app.getPath('userData'), 'presets');
  }

  /**
   * Ensure presets directory exists
   */
  private async ensurePresetsDir(): Promise<void> {
    try {
      await fs.access(this.presetsDir);
    } catch {
      await fs.mkdir(this.presetsDir, { recursive: true });
    }
  }

  /**
   * Get path to preset file
   */
  private getPresetPath(id: string): string {
    return path.join(this.presetsDir, `${id}.json`);
  }

  /**
   * Save a preset
   */
  async save(preset: ConfigPreset): Promise<void> {
    await this.ensurePresetsDir();
    const presetPath = this.getPresetPath(preset.id);
    await fs.writeFile(presetPath, JSON.stringify(preset, null, 2), 'utf-8');
  }

  /**
   * Load a preset by ID
   */
  async load(id: string): Promise<ConfigPreset | null> {
    try {
      const presetPath = this.getPresetPath(id);
      const data = await fs.readFile(presetPath, 'utf-8');
      return JSON.parse(data) as ConfigPreset;
    } catch {
      return null;
    }
  }

  /**
   * List all available presets
   */
  async list(): Promise<ConfigPreset[]> {
    await this.ensurePresetsDir();
    
    try {
      const files = await fs.readdir(this.presetsDir);
      const presets: ConfigPreset[] = [];

      for (const file of files) {
        if (file.endsWith('.json')) {
          try {
            const data = await fs.readFile(path.join(this.presetsDir, file), 'utf-8');
            const preset = JSON.parse(data) as ConfigPreset;
            presets.push(preset);
          } catch {
            // Skip invalid preset files
            continue;
          }
        }
      }

      return presets;
    } catch {
      return [];
    }
  }

  /**
   * Delete a preset
   */
  async delete(id: string): Promise<void> {
    const presetPath = this.getPresetPath(id);
    try {
      await fs.unlink(presetPath);
    } catch {
      // Preset doesn't exist, ignore
    }
  }

  /**
   * Get built-in presets
   */
  getBuiltInPresets(): ConfigPreset[] {
    return [
      {
        id: 'quick-test',
        name: 'Quick Test',
        description: 'Fast tournament for testing (1,000 builds)',
        config: {
          substats: {
            damage: false,
            meleeDamage: false,
            rangedDamage: true,
            criticalChance: true,
            criticalDamage: true,
            attackSpeed: true,
            doubleChance: true,
            health: true,
            healthRegen: true,
            lifesteal: true,
            blockChance: false,
            skillCooldown: false,
            skillDamage: false,
          },
          weaponTypes: {
            ranged: true,
            melee: false,
          },
          substatMultiplier: 0.75,
          targetBuilds: 1000,
          includeMetaBuild: true,
        },
      },
      {
        id: 'ranged-focused',
        name: 'Ranged Focused',
        description: 'Ranged weapons with offensive substats (10,000 builds)',
        config: {
          substats: {
            damage: false,
            meleeDamage: false,
            rangedDamage: true,
            criticalChance: true,
            criticalDamage: true,
            attackSpeed: true,
            doubleChance: true,
            health: true,
            healthRegen: true,
            lifesteal: true,
            blockChance: false,
            skillCooldown: false,
            skillDamage: false,
          },
          weaponTypes: {
            ranged: true,
            melee: false,
          },
          substatMultiplier: 0.75,
          targetBuilds: 10000,
          includeMetaBuild: true,
        },
      },
      {
        id: 'melee-focused',
        name: 'Melee Focused',
        description: 'Melee weapons with offensive substats (10,000 builds)',
        config: {
          substats: {
            damage: false,
            meleeDamage: true,
            rangedDamage: false,
            criticalChance: true,
            criticalDamage: true,
            attackSpeed: true,
            doubleChance: true,
            health: true,
            healthRegen: true,
            lifesteal: true,
            blockChance: true,
            skillCooldown: false,
            skillDamage: false,
          },
          weaponTypes: {
            ranged: false,
            melee: true,
          },
          substatMultiplier: 0.75,
          targetBuilds: 10000,
          includeMetaBuild: true,
        },
      },
      {
        id: 'full-tournament',
        name: 'Full Tournament',
        description: 'Comprehensive tournament with all weapon types (50,000 builds)',
        config: {
          substats: {
            damage: false,
            meleeDamage: true,
            rangedDamage: true,
            criticalChance: true,
            criticalDamage: true,
            attackSpeed: true,
            doubleChance: true,
            health: true,
            healthRegen: true,
            lifesteal: true,
            blockChance: true,
            skillCooldown: false,
            skillDamage: false,
          },
          weaponTypes: {
            ranged: true,
            melee: true,
          },
          substatMultiplier: 0.75,
          targetBuilds: 50000,
          includeMetaBuild: true,
        },
      },
      {
        id: 'balanced-medium',
        name: 'Balanced Medium',
        description: 'Balanced configuration for medium-sized tournaments (25,000 builds)',
        config: {
          substats: {
            damage: false,
            meleeDamage: true,
            rangedDamage: true,
            criticalChance: true,
            criticalDamage: true,
            attackSpeed: true,
            doubleChance: true,
            health: true,
            healthRegen: true,
            lifesteal: true,
            blockChance: true,
            skillCooldown: false,
            skillDamage: false,
          },
          weaponTypes: {
            ranged: true,
            melee: true,
          },
          substatMultiplier: 0.75,
          targetBuilds: 25000,
          includeMetaBuild: true,
        },
      },
    ];
  }
}
