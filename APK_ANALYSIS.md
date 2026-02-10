# Legend of Civilizations APK Analysis

## Overview
- **Package Name**: com.hariwn.legendofcivilizations
- **Version**: 1.8.4 (Build 10804)
- **Engine**: Unity 3D
- **Min SDK**: Android 8.0 (API 26)
- **Target SDK**: Android 16 (API 36)
- **Build Date**: November 20, 2024

## App Architecture

### Technology Stack
1. **Game Engine**: Unity 3D
   - Uses IL2CPP (Intermediate Language to C++) for code compilation
   - Unity version appears to be recent (2023+)
   - Addressables system for asset management

2. **Backend Framework**: Metaplay
   - Custom game server framework
   - Handles multiplayer, progression, and live ops
   - Config file: `SharedGameConfig.mpa` (binary archive)

3. **Key SDKs**:
   - Firebase (Analytics, Crashlytics, Cloud Messaging)
   - Google Play Services (Billing, Auth, Ads)
   - Singular SDK (Analytics/Attribution)
   - Unity IAP (In-App Purchases)
   - Facebook/Instagram integration

## File Structure

### Main APK (`C:\apktool\main-apk-out\`)
```
├── AndroidManifest.xml          # App permissions and components
├── assets/
│   ├── SharedGameConfig.mpa     # Main game configuration (binary)
│   ├── aa/                      # Addressables assets
│   │   ├── catalog.bin          # Asset catalog
│   │   ├── Android/             # Platform-specific bundles
│   │   └── localization/        # Multi-language support
│   └── bin/Data/                # Unity data files
├── smali/                       # Decompiled Java/Kotlin code
├── smali_classes2/              # Additional code
├── smali_classes3/              # Game-specific code
│   └── com/hariwn/              # Main game package
└── res/                         # Android resources
```

### Config APK (`C:\apktool\config-armeabi-out\`)
```
└── lib/armeabi-v7a/
    ├── libil2cpp.so             # Unity IL2CPP runtime (119 MB)
    ├── libunity.so              # Unity engine (16 MB)
    ├── libFirebaseCpp*.so       # Firebase native libs
    └── libcrashlytics*.so       # Crash reporting
```

## Game Configuration Files

### SharedGameConfig.mpa
This is a **binary archive** containing multiple game configuration files:

**Identified Config Modules**:
- `ArenaLeagueLibrary.mpc` - PvP arena leagues/tiers
- `ArenaRewardLibrary.mpc` - Arena rewards
- `DungeonBaseConfig.mpc` - Dungeon system settings
- `DungeonRewardLibrary.mpc` - Dungeon loot tables
- `DungeonRewardEggLibrary.mpc` - Egg rewards from dungeons
- `EggLibrary.mpc` - Egg/gacha system
- `EnemyLibrary.mpc` - Enemy definitions
- `EnemyAgeScalingLibrary.mpc` - Enemy difficulty scaling
- `ForgeConfig.mpc` - Crafting/forge system
- `ForgeUpgradeLibrary.mpc` - Upgrade paths
- `GuildBaseConfig.mpc` - Guild system
- `GuildWarConfig.mpc` - Guild wars/battles
- `GuildWarDayConfigLibrary.mpc` - War schedules
- `GuildWarProgressPassLibrary.mpc` - Battle pass
- `HammerThiefDungeonBattleLibrary.mpc` - Special dungeon
- `IdleConfig.mpc` - Idle/offline progression
- `InAppProducts.mpc` - IAP definitions
- `ItemAgeDropChancesLibrary.mpc` - Loot drop rates
- `ItemBalancingConfig.mpc` - Item stats/balance
- `ItemLevelBracketsLibrary.mpc` - Item level ranges
- `MainBattleConfig.mpc` - Combat system
- `MainGameProgressPassLibrary.mpc` - Main battle pass
- `MountLibrary.mpc` - Mount/pet system
- `MountSummonConfig.mpc` - Mount summoning
- `MountUpgradeLibrary.mpc` - Mount upgrades
- `PetBalancingLibrary.mpc` - Pet stats
- `PetBaseConfig.mpc` - Pet system base
- `PetLibrary.mpc` - Pet definitions
- `PetUpgradeLibrary.mpc` - Pet upgrade paths
- `PlayerSegments.mpc` - Player segmentation (A/B testing)
- `PotionDungeonBattleLibrary.mpc` - Potion dungeon
- `ProfileBaseConfig.mpc` - Player profile settings

### File Format: .mpc (Metaplay Config)
These are **binary serialized** configuration files used by the Metaplay framework. They contain:
- Game balance data
- Loot tables
- Progression curves
- Economy settings
- Content definitions

## Game Mechanics (Based on Config Files)

### Core Systems
1. **Combat System**
   - Main battle configuration
   - Enemy scaling by age/progression
   - Multiple dungeon types (Egg, Hammer Thief, Potion)

2. **Progression**
   - Idle/offline rewards
   - Age-based scaling
   - Item level brackets
   - Multiple upgrade paths

3. **Collection Systems**
   - Mounts (summon, upgrade)
   - Pets (balance, upgrade)
   - Eggs (gacha/loot boxes)
   - Items (drops, crafting)

4. **Social Features**
   - Guilds (emblems, tiers)
   - Guild Wars (daily configs, progress pass)
   - Arena/PvP (leagues, rewards)

5. **Monetization**
   - In-App Purchases
   - Battle Passes (main + guild war)
   - Forge/crafting system
   - Gacha (eggs)

6. **Live Operations**
   - Player segmentation
   - A/B testing support
   - Remote config via Metaplay

## Localization
Supported languages:
- English (en)
- French (fr)
- German (de)
- Italian (it)
- Japanese (ja)
- Korean (ko)
- Portuguese Brazil (pt-br)
- Russian (ru)
- Spanish (es)
- Turkish (tr-tr)

## Permissions
Key permissions requested:
- `INTERNET` - Network access
- `ACCESS_NETWORK_STATE` - Check connectivity
- `BILLING` - In-app purchases
- `POST_NOTIFICATIONS` - Push notifications
- `USE_BIOMETRIC` - Fingerprint auth
- `VIBRATE` - Haptic feedback
- `AD_ID` - Advertising tracking

## Analytics & Tracking
- Firebase Analytics
- Singular SDK (v12.6.1)
- Google Play Services
- Facebook/Instagram tracking

## Next Steps for Analysis

### To Read Game Code:
The game logic is compiled to **IL2CPP native code** (libil2cpp.so), which is very difficult to reverse engineer. However, you can:

1. **Extract Config Files**: Use a custom tool to parse the `.mpa` archive and extract individual `.mpc` files
2. **Decompile IL2CPP**: Use tools like `Il2CppDumper` to extract C# class structures
3. **Analyze Network Traffic**: Monitor API calls to understand server communication
4. **Modify Configs**: Edit and repack the APK with modified configs (requires re-signing)

### Tools Needed:
- **Il2CppDumper** - Extract C# metadata from libil2cpp.so
- **dnSpy** - View decompiled C# code
- **Custom parser** - For .mpa/.mpc binary formats (Metaplay proprietary)
- **Frida/Xposed** - Runtime hooking for live analysis

### Config File Analysis:
The `.mpc` files are binary serialized. To read them, you would need to:
1. Reverse engineer the Metaplay serialization format
2. Or use runtime memory inspection while the game is running
3. Or intercept network traffic to see configs loaded from server

## Security Notes
- App is **not debuggable** (production build)
- Uses **code obfuscation** (IL2CPP)
- Has **certificate pinning** (network_security_config)
- Includes **anti-tampering** (Crashlytics, integrity checks)

## IL2CPP Code Extraction Results

Successfully extracted C# code structure using Il2CppDumper v6.7.46!

**Output Location**: `C:\apktool\il2cpp-output\`

**Generated Files**:
- `dump.cs` (60 MB) - Complete C# class definitions and method signatures
- `DummyDll/` - Reconstructed .NET assemblies for use with decompilers
- `script.json` (174 MB) - Structured metadata
- `il2cpp.h` (168 MB) - C++ header definitions
- `stringliteral.json` (2.3 MB) - All string literals

### Key Assemblies Found:
- `Assembly-CSharp.dll` (1.9 MB) - Main game code
- `Metaplay.dll` (2.9 MB) - Backend framework
- `Metaplay.Generated.Android.dll` (1.6 MB) - Platform-specific code
- `SharedCode.dll` - Shared game logic

### Identified Game Systems (from Code):

**Core Player Model**:
- `PlayerModel` - Main player state
- `PlayerActionBase` - Base class for all player actions
- `PlayerCurrencyModel` - Currency management
- `PlayerForgeModel` - Crafting system
- `PlayerEquipmentModel` - Item equipment (Helmet, Armour, Gloves, Necklace, Ring, Weapon, Shoes, Belt)
- `PlayerSkillCollectionModel` - Skills system
- `PlayerPowerModel` - Power calculation
- `PlayerTechTreeModel` - Tech tree progression
- `PlayerPetCollectionModel` - Pet collection
- `PlayerMountCollectionModel` - Mount collection
- `PlayerDungeonsModel` - Dungeon progress
- `PlayerShopModel` - Shop state
- `PlayerIdleCashModel` - Idle rewards
- `PlayerProfileModel` - Player profile
- `PlayerPvpBattleModel` - PvP battles
- `PlayerGuildModel` - Guild membership
- `PlayerWorldModel` - World/age progression
- `PlayerSetsModel` - Equipment sets

**Combat System**:
- `MainBattleModel` - Main battle state
- `CombatScene` - Battle scene management
- `UnitEntity` - Combat units
- `ProjectileEntity` - Projectiles
- `SkillEntity` - Active skills
- `CombatStats` - HP, Damage, Speed, Crit, Block, Dodge, etc.
- `AttacksSystem` - Attack handling
- `SkillSystem` - Skill buffs and effects

**Item System**:
- `PlayerItemModel` - Individual items
- `ItemBalancingConfig` - Item balance data
- `ItemLevelBracketsConfig` - Level ranges
- `SecondaryStats` - Item secondary stats
- `EquipmentItemInfo` - Equipment details
- `ForgeConfig` - Forge settings
- `ForgeUpgradeLibrary` - Upgrade paths

**Pet & Mount System**:
- `PlayerPetModel` - Pet data
- `PlayerMountModel` - Mount data
- `PetConfig` - Pet configuration
- `MountConfig` - Mount configuration
- `PetUpgradeConfig` - Pet upgrades
- `MountUpgradeConfig` - Mount upgrades
- `MountSummonConfig` - Mount summoning
- `EggConfig` - Egg/gacha system

**Guild System**:
- `GuildModel` - Guild state
- `GuildMemberModel` - Member data
- `GuildWarModel` - Guild wars
- `GuildWarDivisionModel` - War divisions
- `GuildWarBattleModel` - War battles
- `GuildBaseConfig` - Guild settings
- `GuildTierConfig` - Guild tiers

**Arena/PvP**:
- `ArenaLeagueLibrary` - League definitions
- `ArenaRewardLibrary` - Rewards
- `PlayerPvpProfileModel` - PvP profile
- `PvpCombatScene` - PvP battles
- `DivisionModel` - Division system

**Dungeon System**:
- `DungeonBaseConfig` - Dungeon settings
- `DungeonBattleModel` - Dungeon battles
- `HammerThiefDungeonBattleModel` - Special dungeon
- `DungeonRewardConfig` - Loot tables

**Progression**:
- `TechTreeModel` - Tech tree
- `ProgressPassModel` - Battle pass
- `IdleConfig` - Idle rewards
- `PlayerProgressModel` - Overall progress

**Monetization**:
- `InAppProductInfoBase` - IAP products
- `MetaOfferModel` - Special offers
- `DailyDealModel` - Daily deals
- `SubscriptionModel` - Subscriptions
- `PlayerShopModel` - Shop

**Live Ops**:
- `LiveOpsEventModel` - Live events
- `PlayerSegmentInfo` - Player segmentation
- `ExperimentAssignment` - A/B testing

### Config File Classes:
All the `.mpc` files are loaded through these classes:
- `GameConfigLibrary` - Base config library
- `ConfigArchive` - Archive handler
- `GameConfigData` - Config data interface
- Various `*Config` and `*Library` classes for each system

## Summary

Successfully extracted the complete C# code structure from the IL2CPP binary. The game uses a sophisticated Metaplay framework with extensive systems for combat, progression, monetization, and social features. All game mechanics are now readable in the `dump.cs` file, and the DummyDll assemblies can be opened in dnSpy or ILSpy for easier navigation.
