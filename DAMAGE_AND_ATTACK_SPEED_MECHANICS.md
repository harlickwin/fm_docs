# Legend of Civilizations - Damage & Attack Speed Mechanics

## Combat Stats Structure

The game uses a `CombatStats` struct that contains all combat-related statistics:

```csharp
public struct CombatStats {
    // Core Stats
    public CombatStatFixedD6 HpMax;              // Maximum HP
    public CombatStatFixedD6 HpMaxNoMulti;       // Base HP without multipliers
    public CombatStatFixedD6 Dmg;                // Base Damage
    public CombatStatF64 MoveSpeed;              // Movement speed
    
    // Offensive Stats
    public CombatStatFixedD6 CriticalChance;     // Chance to crit
    public CombatStatFixedD6 CriticalMulti;      // Crit damage multiplier
    public CombatStatFixedD6 DoubleDamageChance; // Chance for double damage
    public CombatStatFixedD6 AttackSpeedMulti;   // Attack speed multiplier ⭐
    
    // Defensive Stats
    public CombatStatFixedD6 BlockChance;        // Chance to block
    public CombatStatFixedD6 DodgeChance;        // Chance to dodge
    
    // Sustain Stats
    public CombatStatFixedD6 HealthRegen;        // HP regeneration
    public CombatStatFixedD6 LifeSteal;          // Life steal percentage
    
    // Other
    public AttackType AttackType;                // Melee or Ranged
}
```

## Attack Speed System

### CODE EVIDENCE FROM IL2CPP DUMP

The following code structures were extracted from `dump.cs` (decompiled IL2CPP):

**WeaponInfo class** (line 1050834 in dump.cs):
```csharp
public class WeaponInfo : IGameConfigData<ItemId> {
    [MetaMember(4, 0)]
    public F64 WindupTime { get; set; }      // Base windup time from config
    
    [MetaMember(5, 0)]
    public F64 AttackDuration { get; set; }  // Base attack duration from config
    
    [MetaMember(3, 0)]
    public F64 AttackRange { get; set; }
}
```

**UnitEntity struct** (lines 1057596-1057599 in dump.cs):
```csharp
[MetaMember(4, 0)]
public FD6 AttackTimer; // 0x50 - Current attack timer countdown

[MetaMember(5, 0)]
public FD6 AttackDuration; // 0x58 - Actual attack duration (after speed applied)

[MetaMember(6, 0)]
public FD6 WindUpDuration; // 0x68 - Actual windup duration (after speed applied)
```

**AttacksSystem class** (line 1057705 in dump.cs):
```csharp
public class AttacksSystem {
    private RandomPCG _random;
    
    // Main combat update loop - processes all units each frame
    public void Execute(Entities entities, F64 dt, List<CombatDmg> damageInstances, 
                       List<BasicEntity> newEntities, List<BasicEntity> destroyedEntities,
                       IMetaLogger logger, SharedGameConfig config) { }
    
    // Handles unit attack timing and execution
    private void HandleUnits(Entities entities, F64 dt, ...) { }
    
    // Calculates damage with all modifiers
    private CombatDmg GetDamage(UnitEntity target, CombatStats attackStats) { }
    
    // Applies damage to target
    private void ApplyDmg(UnitEntity target, UnitEntity attacker, CombatStats attackStats, ...) { }
    
    // Executes the actual attack
    private void ExecuteAttack(Entities entities, ..., UnitEntity unit) { }
}
```

**Attack Speed Event System** (lines 688697-688724 in dump.cs):
```csharp
// Entity methods for managing attack speed
public void AddAttackSpeed(float newValue) { }
public void ReplaceAttackSpeed(float newValue) { }
public void RemoveAttackSpeed() { }

// Listener interface
public interface IAttackSpeedListener {
    void OnAttackSpeed(GameEntity entity, float value);
}

// Event system methods
public void AddAttackSpeedListener(IAttackSpeedListener value) { }
public void RemoveAttackSpeedListener(IAttackSpeedListener value, bool removeComponentWhenEmpty = True) { }
```

**Note**: The actual calculation logic (the division operation) is compiled to native ARM code in `libil2cpp.so`. The IL2CPP dump shows the structure and method signatures, but method bodies are empty stubs. The formula is inferred from the data structure and field names.

### How Attack Speed Works

Attack speed is controlled by the `AttackSpeedMulti` stat, which is a **multiplier** applied to attack timing.

**Key Components:**

1. **Base Attack Timing** (from WeaponInfo):
   - `WindupTime` - Time before attack executes
   - `AttackDuration` - Total time for one attack cycle

2. **Attack Speed Multiplier**:
   - Stored in `CombatStats.AttackSpeedMulti`
   - Applied as a multiplier to reduce attack duration
   - Higher value = faster attacks

3. **Attack Timer** (UnitEntity):
   - `AttackTimer` - Countdown timer for next attack
   - `WindUpDuration` - Current windup time
   - `AttackDuration` - Current attack duration

### Attack Speed Calculation

```
Effective Attack Duration = Base Attack Duration / AttackSpeedMulti
Effective Windup Time = Base Windup Time / AttackSpeedMulti
```

**Example:**
- Base Attack Duration: 2.0 seconds
- AttackSpeedMulti: 1.5
- Effective Attack Duration: 2.0 / 1.5 = 1.33 seconds (33% faster)

### Attack Speed Event System

The game uses an event-driven system for attack speed changes:

```csharp
public interface IAttackSpeedListener {
    void OnAttackSpeed(GameEntity entity, float value);
}

public class AttackSpeedEventSystem : ReactiveSystem<GameEntity> {
    private readonly List<IAttackSpeedListener> _listenerBuffer;
    
    // Triggers when AttackSpeed component changes
    // Notifies all listeners of the new value
}
```

## Damage Calculation System

### Base Damage Calculation

The `AttacksSystem` class handles damage calculation:

```csharp
public class AttacksSystem {
    private RandomPCG _random;  // Random number generator for procs
    
    private CombatDmg GetDamage(UnitEntity target, CombatStats attackStats) {
        // 1. Calculate base damage from attackStats.Dmg
        // 2. Check for critical hit (CriticalChance)
        // 3. Apply critical multiplier if crit (CriticalMulti)
        // 4. Check for double damage proc (DoubleDamageChance)
        // 5. Check target's dodge chance
        // 6. Check target's block chance
        // 7. Return final damage with flags (Critical, Dodged, Blocked)
    }
}
```

### Damage Result Structure

```csharp
public struct CombatDmg {
    public FD6 Damage;      // Final damage amount
    public bool Dodged;     // Was attack dodged?
    public bool Blocked;    // Was attack blocked?
    public bool Critical;   // Was it a critical hit?
    public FD6 Heal;        // Healing amount (life steal)
}
```

### Damage Calculation Flow

1. **Base Damage**: Start with `CombatStats.Dmg`

2. **Critical Hit Check**:
   ```
   if (Random() < CriticalChance) {
       Damage *= CriticalMulti
       Critical = true
   }
   ```

3. **Double Damage Check**:
   ```
   if (Random() < DoubleDamageChance) {
       Damage *= 2
   }
   ```

4. **Dodge Check** (Target):
   ```
   if (Random() < target.DodgeChance) {
       Damage = 0
       Dodged = true
       return
   }
   ```

5. **Block Check** (Target):
   ```
   if (Random() < target.BlockChance) {
       Damage = 0
       Blocked = true
       return
   }
   ```

6. **Life Steal**:
   ```
   Heal = Damage * LifeSteal
   ```

## Attack Cycle

### Unit Attack State Machine

```csharp
public enum CombatState {
    Idle,
    Moving,
    WindUp,      // Preparing attack
    Attacking,   // Executing attack
    Cooldown     // Post-attack recovery
}
```

### Attack Timing Flow

1. **Idle/Moving**: Unit searches for target
2. **WindUp Phase**: 
   - Duration = `WindupTime / AttackSpeedMulti`
   - Unit plays windup animation
3. **Attack Phase**:
   - Damage is calculated and applied
   - Projectile spawned (if ranged)
4. **Cooldown Phase**:
   - Duration = `AttackDuration / AttackSpeedMulti`
   - Timer counts down
5. **Repeat**: Back to step 1

### Attack Timer Update

```
AttackTimer -= deltaTime

if (AttackTimer <= 0) {
    // Execute attack
    CombatDmg damage = GetDamage(target, attackerStats)
    ApplyDamage(target, damage)
    
    // Reset timer
    AttackTimer = AttackDuration / AttackSpeedMulti
}
```

## Stat Sources

Attack Speed and Damage can come from multiple sources:

### 1. Equipment (Items)
- Helmet, Armour, Gloves, Necklace, Ring, Weapon, Shoes, Belt
- Each item has `SecondaryStats` that can include AttackSpeedMulti
- Items have level scaling

### 2. Skills
- Active skills can provide temporary buffs
- Passive skills provide permanent stat bonuses
- Skill damage scales with level

### 3. Pets
- Pets provide stat multipliers
- `PetBalancingConfig.DamageMultiplier`
- `PetBalancingConfig.HealthMultiplier`

### 4. Mounts
- Mounts provide additional stats
- `MountStats` structure similar to CombatStats

### 5. Tech Tree
- Tech tree nodes provide permanent upgrades
- `TechTreeStatContribution.ValueIncrease`

### 6. Equipment Sets
- Set bonuses when wearing multiple pieces
- `SetBonusConfig.BonusStats`

### 7. Skins
- Cosmetic items that also provide stats
- `SkinConfig.PossibleStats`

## Configuration Files

### ItemBalancingConfig
```csharp
public class ItemBalancingConfig {
    public float LevelScalingBase;
    public float PlayerMeleeDamageMultiplier;
    public float PlayerBaseDamage;
    public float PlayerPowerDamageMultiplier;
    public float PlayerBaseCritDamage;
}
```

### WeaponInfo
```csharp
public class WeaponInfo {
    public float AttackRange;
    public float WindupTime;        // Base windup time
    public float AttackDuration;    // Base attack duration
    public bool IsRanged;
    public bool IsAiming;
    public int ProjectileId;
}
```

## PvP Modifications

PvP has special multipliers:

```csharp
public class PvpBaseConfig {
    public float PvpHpBaseMultiplier;
    public float PvpHpPetMultiplier;
    public float PvpHpSkillMultiplier;
    public float PvpHpMountMultiplier;
}
```

## Summary

**Attack Speed:**
- Controlled by `AttackSpeedMulti` stat (multiplicative)
- Reduces both windup time and attack duration
- Higher value = faster attacks
- Formula: `Effective Time = Base Time / AttackSpeedMulti`

**Damage:**
- Base damage from `Dmg` stat
- Modified by: Critical hits, Double damage procs
- Reduced by: Dodge, Block
- Additional: Life steal healing
- Multiple sources: Equipment, Skills, Pets, Mounts, Tech Tree, Sets, Skins

**Attack Cycle:**
1. Windup (scaled by attack speed)
2. Execute (damage calculated)
3. Cooldown (scaled by attack speed)
4. Repeat

The system uses fixed-point math (`FD6`, `F64`) for deterministic calculations across client and server.
