# How Attack Speed Actually Works - Simple Explanation

## The Bottom Line

**Attack Speed is a DIVIDER that makes you attack faster.**

```
Time Between Attacks = Base Attack Time / AttackSpeedMulti
```

## Real Example

Let's say your weapon has:
- **Base Attack Duration**: 2.0 seconds (from weapon config)
- **Base Windup Time**: 0.5 seconds (from weapon config)

### With NO Attack Speed Bonus (AttackSpeedMulti = 1.0):
```
Windup Time = 0.5 / 1.0 = 0.5 seconds
Attack Duration = 2.0 / 1.0 = 2.0 seconds
Total Time Per Attack = 2.5 seconds
Attacks Per Second = 0.4
```

### With +50% Attack Speed (AttackSpeedMulti = 1.5):
```
Windup Time = 0.5 / 1.5 = 0.33 seconds
Attack Duration = 2.0 / 1.5 = 1.33 seconds
Total Time Per Attack = 1.66 seconds
Attacks Per Second = 0.6
```

### With +100% Attack Speed (AttackSpeedMulti = 2.0):
```
Windup Time = 0.5 / 2.0 = 0.25 seconds
Attack Duration = 2.0 / 2.0 = 1.0 seconds
Total Time Per Attack = 1.25 seconds
Attacks Per Second = 0.8
```

## How It's Stored in the Game

### In Your Character Stats:
```csharp
CombatStats {
    AttackSpeedMulti = 1.5  // This is your total attack speed multiplier
}
```

### In Each Unit (Player/Enemy):
```csharp
UnitEntity {
    AttackTimer = 1.33      // Countdown timer (starts at AttackDuration / AttackSpeedMulti)
    AttackDuration = 2.0    // Base time from weapon
    WindUpDuration = 0.5    // Base windup from weapon
}
```

## What Happens Every Frame

The game runs this logic constantly:

```csharp
// Every frame (60 times per second):
AttackTimer -= deltaTime  // Subtract time elapsed (e.g., 0.016 seconds)

if (AttackTimer <= 0) {
    // TIME TO ATTACK!
    
    // 1. Deal damage to target
    DealDamage(target)
    
    // 2. Reset the timer for next attack
    AttackTimer = AttackDuration / AttackSpeedMulti
    
    // Example: AttackTimer = 2.0 / 1.5 = 1.33 seconds
}
```

## Where Attack Speed Comes From

Your `AttackSpeedMulti` is the **sum** of all your attack speed bonuses:

```
AttackSpeedMulti = 1.0 (base)
                 + 0.2 (from weapon)
                 + 0.15 (from gloves)
                 + 0.1 (from ring)
                 + 0.05 (from skill buff)
                 = 1.5 total
```

## Visual Timeline

### Normal Speed (1.0x):
```
|--Windup(0.5s)--|--Attack(2.0s)--|--Windup(0.5s)--|--Attack(2.0s)--|
0s              0.5s            2.5s              3.0s            5.0s
```

### Fast Speed (1.5x):
```
|Windup(0.33s)|Attack(1.33s)|Windup(0.33s)|Attack(1.33s)|
0s          0.33s        1.66s         2.0s        3.33s
```

### Super Fast (2.0x):
```
|Wind(0.25s)|Attack(1.0s)|Wind(0.25s)|Attack(1.0s)|
0s        0.25s       1.25s       1.5s       2.5s
```

## Key Points

1. **Higher number = Faster attacks**
   - 1.0 = normal speed
   - 1.5 = 50% faster
   - 2.0 = twice as fast (double speed)

2. **It affects EVERYTHING**:
   - Windup time (preparation)
   - Attack duration (cooldown)
   - Total time between attacks

3. **It's multiplicative, not additive**:
   - You divide by it, not subtract from it
   - This means diminishing returns at very high values

4. **The formula is simple**:
   ```
   Actual Time = Base Time / AttackSpeedMulti
   ```

## Practical Impact

| AttackSpeedMulti | % Faster | Attacks/Second (2s base) |
|------------------|----------|--------------------------|
| 1.0              | 0%       | 0.5                      |
| 1.2              | 20%      | 0.6                      |
| 1.5              | 50%      | 0.75                     |
| 2.0              | 100%     | 1.0                      |
| 2.5              | 150%     | 1.25                     |
| 3.0              | 200%     | 1.5                      |

## Summary

**Attack Speed makes you attack faster by dividing the time between attacks.**

- Your weapon has a base attack time (e.g., 2 seconds)
- Your gear/skills give you an AttackSpeedMulti (e.g., 1.5)
- Your actual attack time = 2 / 1.5 = 1.33 seconds
- The game counts down from 1.33 seconds, then you attack again

That's it! Simple division.
