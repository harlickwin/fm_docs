# Game Mechanics Manual

**Complete code-based extraction from IL2CPP dump**

This manual documents ONLY mechanics found in code.
Every entry includes line numbers for verification.
NO assumptions. NO optimization strategies. ONLY facts.

**Total Classes:** 1008
**Total Enums:** 1116

## Table of Contents

- [Combat](#combat)
- [Economy](#economy)
- [Guild](#guild)
- [Other](#other)
- [Pets & Mounts](#pets--mounts)
- [Progression](#progression)
- [PvE Content](#pve-content)
- [PvP](#pvp)
- [Summoning](#summoning)

## Combat

**Classes:** 69 | **Enums:** 13

### Enumerations

#### AttackSfx

**Line:** 705778

**Values:**

```
Punch = 0
SwordSmall = 1
WoodBlunt = 3
Throw = 4
LaserSword = 5
HitBig = 7
QuantumMelee = 8
Rifle = 10
Automatic = 11
Pistol = 12
Shotgun = 13
Silencer = 14
Bow = 15
LaserGun = 17
Rocket = 18
Magic = 19
Cannon = 20
MachineGun = 21
BixAxe = 22
None = 99999
```

---

#### AttackType

**Line:** 1057429

**Values:**

```
None = 0
Skill = 1
Melee = 2
Ranged = 3
```

---

#### CombatSkill

**Line:** 1057131

**Values:**

```
Meat = 0
Morale = 1
Arrows = 2
Shuriken = 3
Shout = 4
Meteorite = 5
Berserk = 6
Stampede = 7
Thorns = 8
Bomb = 9
Worm = 10
Lightning = 11
Buff = 12
HigherMorale = 13
RainOfArrows = 14
StrafeRun = 15
CannonBarrage = 16
Drone = 17
```

---

#### CombatState

**Line:** 1057418

**Values:**

```
Idle = 0
WindingUp = 1
OnCooldown = 2
```

---

#### ConnectionHealth

**Line:** 1313869

**Values:**

```
NotConnected = 0
Healthy = 1
Unhealthy = 2
```

---

#### DepthPrimingMode

**Line:** 915649

**Values:**

```
Disabled = 0
Auto = 1
Forced = 2
```

---

#### DllImportSearchPath

**Line:** 229256

**Values:**

```
UseDllDirectoryForDependencies = 256
ApplicationDirectory = 512
UserDirectories = 1024
System32 = 2048
SafeDirectories = 4096
AssemblyDirectory = 2
LegacyBehavior = 0
```

---

#### GlyphPackingMode

**Line:** 1557624

**Values:**

```
BestShortSideFit = 0
BestLongSideFit = 1
BestAreaFit = 2
BottomLeftRule = 3
ContactPointRule = 4
```

---

#### HealthCheckTypeBits

**Line:** 551621

**Values:**

```
GlobalState = 1
Database = 2
```

---

#### PropertyPathPartKind

**Line:** 1461820

**Values:**

```
Name = 0
Index = 1
Key = 2
```

---

#### RefreshProperties

**Line:** 784773

**Values:**

```
None = 0
All = 1
Repaint = 2
```

---

#### SkillTabType

**Line:** 732680

**Values:**

```
Skills = 0
Pets = 1
TechTree = 2
```

---

#### TouchPhase

**Line:** 1580247

**Values:**

```
Began = 0
Moved = 1
Stationary = 2
Ended = 3
Canceled = 4
```

---

### Classes

#### ActivateSkillAction

**Line:** 1056269

**Inherits:** PlayerAction

---

#### ActiveSkillStatTarget

**Line:** 1076972

**Inherits:** StatTargetBase

---

#### AreaProjectileReactiveModel

**Line:** 709218

**Inherits:** ReactiveModel

---

#### ChangeWeaponCheatAction

**Line:** 1068220

**Inherits:** PlayerAction

---

#### CleanupAfterCombat

**Line:** 708483

**Inherits:** IComponent

**Fields:**

```
CombatScene: CombatScene
```

---

#### CleanupDungeonCombatSceneAction

**Line:** 1060806

**Inherits:** PlayerAction

---

#### CleanupPvpCombatAction

**Line:** 1073867

**Inherits:** PlayerAction

---

#### ClearAllSkillsCheatAction

**Line:** 1074722

**Inherits:** PlayerAction

---

#### CombatPhysics

**Line:** 1057748

---

#### CombatScene

**Line:** 1056888

**Fields:**

```
Entities: Entities
EntitiesToDestroy: List<BasicEntity>
_newEntities: List<BasicEntity>
DamageInstances: List<CombatDmg>
_skillSystem: SkillSystem
_attackSystem: AttacksSystem
```

---

#### CombatSceneReactiveModel

**Line:** 709305

**Inherits:** ReactiveModel

---

#### CombatSkillAutoSkillVisual

**Line:** 731904

**Inherits:** MonoBehaviour

**Fields:**

```
Content: GameObject
AutoText: TMP_Text
Background: Image
Button: UnityButton
_isActive: bool
_autoOn: string
_autoOff: string
```

---

#### CombatSkillVisual

**Line:** 731955

**Inherits:** MonoBehaviour

**Fields:**

```
Button: UnityButton
Icon: Image
ActiveCircle: Image
CooldownCircle: Image
RarityBackground: Image
_rarity: Rarity
```

---

#### DefaultGuildSearchParams

**Line:** 569956

**Inherits:** GuildSearchParamsBase

---

#### GuildSearchParamsBase

**Line:** 569924

**Inherits:** IMetaIntegrationConstructible

---

#### GuildWarCombatScene

**Line:** 1069463

---

#### InventorySkillReactiveModel

**Line:** 730644

**Inherits:** ReactiveModel

---

#### PassiveSkillStatTarget

**Line:** 1077013

**Inherits:** StatTargetBase

---

#### PlayerPvpSkillModel

**Line:** 1058577

---

#### PlayerSkillCollectionModel

**Line:** 1075500

---

#### PlayerSkillModel

**Line:** 1075577

---

#### ProjectileInfo

**Line:** 1050768

**Inherits:** IGameConfigData

---

#### ProjectileReactiveModel

**Line:** 709364

**Inherits:** ReactiveModel

---

#### PvpCombatScene

**Line:** 1074367

---

#### PvpCombatSkillVisual

**Line:** 727039

**Inherits:** MonoBehaviour

**Fields:**

```
Icon: Image
ActiveCircle: Image
CooldownCircle: Image
RarityBackground: Image
_rarity: Rarity
```

---

#### PvpProfileSkillVisual

**Line:** 727737

**Inherits:** MonoBehaviour

**Fields:**

```
Visual: SkillVisual
Button: UnityButton
```

---

#### SetAutoActivateSkillStateAction

**Line:** 1074735

**Inherits:** PlayerAction

---

#### SkillActivatedMessage

**Line:** 730516

**Inherits:** IMessage

---

#### SkillBaseConfig

**Line:** 1074990

**Inherits:** GameConfigKeyValue

---

#### SkillBuffs

**Line:** 1057278

**Fields:**

```
TotalAllyHpBuff: FD6
TotalAllyDmgBuff: FD6
TotalEnemyHpBuff: FD6
TotalEnemyDmgBuff: FD6
```

---

#### SkillBuilder

**Line:** 1057188

---

#### SkillCollectionDetailsOpenButton

**Line:** 732071

**Inherits:** UiUnityView

**Fields:**

```
Button: UnityButton
```

---

#### SkillCollectionReactiveModel

**Line:** 730726

**Inherits:** ReactiveModel

---

#### SkillConfig

**Line:** 1075064

**Inherits:** IGameConfigData

---

#### SkillDungeonBattleLibrary

**Line:** 1061255

**Inherits:** DungeonBattleLibrary

---

#### SkillDungeonKeysChangeMessage

**Line:** 712695

**Inherits:** DungeonKeysChangeMessage

---

#### SkillEntity

**Line:** 1057246

**Inherits:** BasicEntity

**Fields:**

```
Skill: CombatSkill
IsAlly: bool
IsActive: bool
IsOnCooldown: bool
Timer: FD6
CooldownDuration: FD6
ActiveDuration: FD6
Damage: FD6
Health: FD6
SlotId: int
```

---

#### SkillEquipAction

**Line:** 1074766

**Inherits:** PlayerAction

---

#### SkillEquippedMessage

**Line:** 730550

**Inherits:** IMessage

---

#### SkillMaxCheatAction

**Line:** 1074809

**Inherits:** PlayerAction

**Fields:**

```
NumberOfLevels: int
```

---

#### SkillPassiveConfig

**Line:** 1075154

**Inherits:** IGameConfigData

---

#### SkillStats

**Line:** 1075250

---

#### SkillSummonAction

**Line:** 1074895

**Inherits:** PlayerAction

---

#### SkillSummonDropChanceConfig

**Line:** 1075285

**Inherits:** IGameConfigData

---

#### SkillSummonTicketsChangeMessage

**Line:** 711803

**Inherits:** CurrencyChangeMessage

---

#### SkillSummonUpgradeConfig

**Line:** 1075390

**Inherits:** IGameConfigData

---

#### SkillTabFeature

**Line:** 732635

**Inherits:** Feature

---

#### SkillTabUiMenuButton

**Line:** 732690

**Inherits:** UiUnityView

**Fields:**

```
Label: TMP_Text
Type: SkillTabType
Button: UnityButton
Selected: GameObject
Unselected: GameObject
RightSideSeparator: GameObject
_sequence: Sequence
```

---

#### SkillUnEquipAction

**Line:** 1074914

**Inherits:** PlayerAction

---

#### SkillUnequippedMessage

**Line:** 730597

**Inherits:** IMessage

---

#### SkillUpgradeAction

**Line:** 1074945

**Inherits:** PlayerAction

---

#### SkillUpgradeConfig

**Line:** 1075432

**Inherits:** IGameConfigData

---

#### SkillUpgradedMessage

**Line:** 730624

**Inherits:** IMessage

---

#### SkillVisual

**Line:** 732470

**Inherits:** MonoBehaviour

**Fields:**

```
Icon: Image
IconCanvasGroup: CanvasGroup
Equip: GameObject
UpgradeArrow: GameObject
Level: TMP_Text
SkillShard: TMP_Text
BackGround: Image
ProgressBar: Image
ProgressObjects: GameObject
MaxedObjects: GameObject
```

---

#### SkillVisualConfig

**Line:** 730487

**Inherits:** ScriptableObject

**Fields:**

```
AnimationView: SummonEntryAnimationView
Skills: SerializableDictionary<CombatSkill, SkillVisualDetails>
```

---

#### SkillVisualDetails

**Line:** 730501

**Fields:**

```
Icon: Sprite
ShowDuration: bool
ProjectilePrefab: ProjectileItem
SkillAnimation: GameObject
```

---

#### SkillsCheatContainer

**Line:** 686375

**Inherits:** AbstractCheatContainer

---

#### SkillsFeature

**Line:** 731446

**Inherits:** Feature

---

#### SkillsLocalizer

**Line:** 721323

**Inherits:** LocalizerBase

---

#### SkillsQuickUpgradeAction

**Line:** 1074845

**Inherits:** PlayerAction

---

#### SkillsRedDotLogic

**Line:** 731488

**Inherits:** IRedDotLogic

**Fields:**

```
_stillLockedSlotsCount: int
```

---

#### SkillsSummonedMessage

**Line:** 730577

**Inherits:** IMessage

---

#### SummonedSkillInfo

**Line:** 1052186

---

#### UnitProjectileConfig

**Line:** 1057677

**Fields:**

```
Radius: F64
Speed: F64
AffectedByGravity: bool
IsAiming: bool
HandOffset: F64Vec2
WeaponOffset: F64Vec2
IsFromSkill: bool
Skill: CombatSkill
```

---

#### WeaponData

**Line:** 713702

**Fields:**

```
AttackRange: float
WindUpTime: float
AttackTime: float
IsRanged: bool
IsAiming: bool
WeaponOffset: Vector2
HandOffset: Vector2
```

---

#### WeaponEquipmentItem

**Line:** 713723

**Inherits:** EquipmentItem

**Fields:**

```
AttackRange: float
IsRanged: bool
IsAiming: bool
ProjectileSpawnPoint: Transform
WeaponData: WeaponData
_tween: Tween
```

---

#### WeaponInfo

**Line:** 1050834

**Inherits:** IGameConfigData

---

#### WeaponItemVisualConfig

**Line:** 713751

**Inherits:** EquipmentItemVisualConfig

**Fields:**

```
AnimationController: AnimatorOverrideController
IsDualWield: bool
HasProjectile: bool
ProjectilePrefab: ProjectileItem
HasSecondary: bool
SecondaryPrefab: SecondaryEquipmentItem
AttackSfx: AttackSfx
ImpactSfx: ImpactSfx
```

---

#### WeaponStatTarget

**Line:** 1076931

**Inherits:** StatTargetBase

---

## Economy

**Classes:** 33 | **Enums:** 6

### Enumerations

#### CurrencyType

**Line:** 1067355

**Values:**

```
Coins = 0
Gems = 1
Hammers = 2
SkillSummonTickets = 3
TechPotions = 4
PvpTickets = 5
ClockWinders = 6
WarBattleTickets = 7
Token = 8
```

---

#### ForgeState

**Line:** 714632

**Values:**

```
Idle = 0
StartForgingAnimation = 1
ForgingAnimation = 2
ForgingAnimationComplete = 3
ItemsForged = 4
```

---

#### GameConfigRuntimeStorageMode

**Line:** 588373

**Values:**

```
Invalid = 0
Deduplicating = 1
Solo = 2
```

---

#### GemSkipTarget

**Line:** 1052346

**Values:**

```
Forge = 0
PetEgg = 1
TechTree = 2
```

---

#### ParticleSystemBakeMeshOptions

**Line:** 1577997

**Values:**

```
BakeRotationAndScale = 1
BakePosition = 2
Default = 0
```

---

#### ShopCategories

**Line:** 729911

**Values:**

```
Gems = 0
Resources = 1
DailyDeals = 2
TokenPacks = 3
```

---

### Classes

#### AutoForgeHammerCountSelectAction

**Line:** 1068151

**Inherits:** PlayerAction

---

#### CheatCurrencyAddAction

**Line:** 1067281

**Inherits:** PlayerAction

---

#### CheatCurrencyRemoveAction

**Line:** 1067324

**Inherits:** PlayerAction

---

#### CurrencyReward

**Line:** 1078791

**Inherits:** PlayerReward

---

#### DeductGuildCreationCostAction

**Line:** 1063530

**Inherits:** PlayerSynchronizedServerActionCore

---

#### DungeonKeysChangeMessage

**Line:** 712630

**Inherits:** IMessage

---

#### ForgeAction

**Line:** 1068319

**Inherits:** PlayerAction

---

#### ForgeAutoSellToggleAgeAction

**Line:** 1068344

**Inherits:** PlayerAction

---

#### ForgeAutoSellTogglePassiveAction

**Line:** 1068375

**Inherits:** PlayerAction

---

#### ForgeConfig

**Line:** 1068745

**Inherits:** GameConfigKeyValue

---

#### ForgeGemSkipAction

**Line:** 1068445

**Inherits:** PlayerAction

---

#### ForgeLevelMaxCheatAction

**Line:** 1068678

**Inherits:** PlayerAction

---

#### ForgeReactiveModel

**Line:** 714814

**Inherits:** ReactiveModel

---

#### ForgeTierUpgradeAction

**Line:** 1068406

**Inherits:** PlayerAction

---

#### ForgeUpgradeClaimAction

**Line:** 1068432

**Inherits:** PlayerAction

---

#### ForgeUpgradeLibrary

**Line:** 1051746

**Inherits:** IGameConfigData

---

#### ForgeUpgradeStartAction

**Line:** 1068419

**Inherits:** PlayerAction

---

#### HammerDungeonKeyChangeMessage

**Line:** 712665

**Inherits:** DungeonKeysChangeMessage

---

#### IdleCashCollectAction

**Line:** 1069799

**Inherits:** PlayerAction

---

#### IdleConfig

**Line:** 1069812

**Inherits:** GameConfigKeyValue

---

#### PetDungeonKeysChangeMessage

**Line:** 712675

**Inherits:** DungeonKeysChangeMessage

---

#### PetEggHatchGemSkipAction

**Line:** 1071180

**Inherits:** PlayerAction

---

#### PlayerCurrencyModel

**Line:** 1067393

---

#### PlayerEventCurrencySpent

**Line:** 1067465

**Inherits:** PlayerEventBase

---

#### PlayerEventForgeUpgradeCompleted

**Line:** 1068560

**Inherits:** PlayerEventBase

---

#### PlayerEventForgeUpgradeStarted

**Line:** 1068458

**Inherits:** PlayerEventBase

---

#### PlayerForgeModel

**Line:** 1068869

---

#### PlayerIdleCashModel

**Line:** 1069875

---

#### PlayerShopModel

**Line:** 1066486

**Inherits:** INextDayListener

---

#### PotionDungeonKeysChangeMessage

**Line:** 712685

**Inherits:** DungeonKeysChangeMessage

---

#### ShopResourcesLibrary

**Line:** 1066614

**Inherits:** IGameConfigData

---

#### ShopVisualConfig

**Line:** 729739

**Inherits:** ScriptableObject

**Fields:**

```
GemsIcons: SerializableDictionary<string, Sprite>
TokenPackIcons: SerializableDictionary<string, Sprite>
ResourceIcons: SerializableDictionary<string, ResourceItem>
DailyDealIcons: SerializableDictionary<DailyDealType, Sprite>
```

---

#### TechTreeNodeUpgradeGemSkipAction

**Line:** 1077580

**Inherits:** PlayerAction

---

## Guild

**Classes:** 216 | **Enums:** 30

### Enumerations

#### AndroidHardwareKeyboardHidden

**Line:** 1487673

**Values:**

```
Undefined = 0
No = 1
Yes = 2
```

---

#### GuildChangeRankResponse

**Line:** 1063696

---

#### GuildClientPhase

**Line:** 570250

**Values:**

```
NoSession = 0
NoGuild = 1
GuildActive = 2
CreatingGuild = 3
JoiningGuild = 4
LoadingEntity = 5
```

---

#### GuildCreateInvitationResponse

**Line:** 571532

---

#### GuildCreationFailedEnum

**Line:** 1063974

**Values:**

```
None = 0
NameNotUnique = 1
TagNotUnique = 2
BadWord = 3
NameEmpty = 4
NameTooLong = 5
TagEmpty = 6
TagTooLong = 7
NameRegexFailed = 8
TagRegexFailed = 9
Other = 10
```

---

#### GuildEventInvokerInfo

**Line:** 567958

---

#### GuildEventMemberRemovedDueToInconsistency

**Line:** 568211

---

#### GuildInspectInvitationResponse

**Line:** 571670

---

#### GuildInviteType

**Line:** 568511

**Values:**

```
InviteCode = 0
```

---

#### GuildJoinRequest

**Line:** 570992

---

#### GuildJoinSetting

**Line:** 1063827

**Values:**

```
Open = 0
Approval = 1
InviteOnly = 2
Closed = 3
```

---

#### GuildLifecyclePhase

**Line:** 568591

**Values:**

```
WaitingForSetup = 0
WaitingForLeader = 1
Running = 2
Closed = 3
```

---

#### GuildMemberKickResponse

**Line:** 1063651

---

#### GuildMemberPlayerDataUpdateKind

**Line:** 569740

**Values:**

```
NewMember = 0
UpdateMember = 1
```

---

#### GuildMemberRole

**Line:** 568575

**Values:**

```
Leader = 0
Commander = 1
Captain = 2
R1 = 11
R2 = 12
R3 = 13
R4 = 14
R5 = 15
```

---

#### GuildMemberRoleEvent

**Line:** 568602

**Values:**

```
MemberAdd = 0
MemberRemove = 1
MemberEdit = 2
```

---

#### GuildMemberTransferLeadershipResponse

**Line:** 1063577

---

#### GuildTabType

**Line:** 719201

**Values:**

```
Members = 0
Missions = 1
Titans = 2
War = 3
```

---

#### GuildTier

**Line:** 1062450

**Values:**

```
S = 0
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
```

---

#### GuildTransactionConsistencyMode

**Line:** 569995

**Values:**

```
Relaxed = 0
EventuallyConsistent = 1
```

---

#### GuildViewResponse

**Line:** 571336

---

#### JsonUnmappedMemberHandling

**Line:** 1003257

**Values:**

```
Skip = 0
Disallow = 1
```

---

#### MemberBindingType

**Line:** 1288325

**Values:**

```
Assignment = 0
MemberBinding = 1
ListBinding = 2
```

---

#### MemberSerialization

**Line:** 1032298

**Values:**

```
OptOut = 0
OptIn = 1
Fields = 2
```

---

#### MemberTypes

**Line:** 265716

**Values:**

```
Constructor = 1
Event = 2
Field = 4
Method = 8
Property = 16
TypeInfo = 32
Custom = 64
NestedType = 128
All = 191
```

---

#### MetaMemberFlags

**Line:** 600822

**Values:**

```
None = 0
Hidden = 1
NoChecksum = 2
Transient = 4
ServerOnly = 3
_LegacyDontUse_ExcludeFromGdprExport = 8
ExcludeFromEventLog = 16
```

---

#### MissingMemberHandling

**Line:** 1032318

**Values:**

```
Ignore = 0
Error = 1
```

---

#### PlayerGuildFetchJoinsResponse

**Line:** 1063786

---

#### UnknownConfigMemberHandling

**Line:** 597253

**Values:**

```
Ignore = 0
Warning = 1
Error = 2
```

---

#### WarTask

**Line:** 1066314

**Values:**

```
SpendCoinsOnForge = 100
StartForgeUpgrade = 101
CompleteForgeUpgrade = 102
ForgePrimitiveEquipment = 1000
ForgeMedievalEquipment = 1001
ForgeEarlyModernEquipment = 1002
ForgeModernEquipment = 1003
ForgeSpaceEquipment = 1004
ForgeInterstellarEquipment = 1005
ForgeMultiverseEquipment = 1006
ForgeQuantumEquipment = 1007
ForgeUnderworldEquipment = 1008
ForgeDivineEquipment = 1009
UseHammerThiefDungeonKey = 2000
UseGhostTownDungeonKey = 2001
UseInvasionDungeonKey = 2002
UseZombieInvasionDungeonKey = 2003
SummonCommonSkill = 3000
SummonRareSkill = 3001
SummonEpicSkill = 3002
SummonLegendarySkill = 3003
SummonUltimateSkill = 3004
SummonMythicSkill = 3005
UpgradeCommonSkill = 4006
UpgradeRareSkill = 4007
UpgradeEpicSkill = 4008
UpgradeLegendarySkill = 4009
UpgradeUltimateSkill = 4010
UpgradeMythicSkill = 4011
HatchCommonEgg = 5000
HatchRareEgg = 5001
HatchEpicEgg = 5002
HatchLegendaryEgg = 5003
HatchUltimateEgg = 5004
HatchMythicEgg = 5005
MergeCommonPet = 6000
MergeRarePet = 6001
MergeEpicPet = 6002
MergeLegendaryPet = 6003
MergeUltimatePet = 6004
MergeMythicPet = 6005
FinishITechTreeUpgrade = 7000
FinishIITechTreeUpgrade = 7001
FinishIIITechTreeUpgrade = 7002
FinishIVTechTreeUpgrade = 7003
FinishVTechTreeUpgrade = 7004
SummonCommonMount = 8000
SummonRareMount = 8001
SummonEpicMount = 8002
SummonLegendaryMount = 8003
SummonUltimateMount = 8004
SummonMythicMount = 8005
MergeCommonMount = 9000
MergeRareMount = 9001
MergeEpicMount = 9002
MergeLegendaryMount = 9003
MergeUltimateMount = 9004
MergeMythicMount = 9005
```

---

### Classes

#### ChatGuildMessageVisual

**Line:** 707720

**Inherits:** MonoBehaviour

**Fields:**

```
MessageText: TMP_Text
TimeText: TMP_Text
```

---

#### ChatJoinedGuildAction

**Line:** 1058864

**Inherits:** PlayerSynchronizedServerActionCore

---

#### ClaimGuildWarRewardAction

**Line:** 1055784

**Inherits:** PlayerAction

---

#### ClaimProgressPassRewardAction

**Line:** 1078358

**Inherits:** PlayerAction

---

#### CleanupGuildWarBattleAction

**Line:** 1069036

**Inherits:** PlayerAction

---

#### ClientGuildModelJournal

**Line:** 567763

**Inherits:** ModelJournal

---

#### ConsumePendingRewardsAction

**Line:** 1079360

**Inherits:** PlayerAction

---

#### DailyDealReward

**Line:** 1078921

**Inherits:** PlayerReward

---

#### DebugGuildSetTierPointsAction

**Line:** 1064331

**Inherits:** GuildActionCore

---

#### DivisionPlayerRewardsBase

**Line:** 564841

**Inherits:** IDivisionRewards

---

#### DungeonEggReward

**Line:** 1078994

**Inherits:** PlayerReward

---

#### DungeonKeyReward

**Line:** 1079026

**Inherits:** PlayerReward

---

#### DungeonKeyRewardMessage

**Line:** 728595

**Inherits:** IMessage

---

#### DungeonRewardConfig

**Line:** 1061177

**Inherits:** IGameConfigData

---

#### DungeonRewardEggConfig

**Line:** 1071460

**Inherits:** IGameConfigData

---

#### DungeonRewardSource

**Line:** 1060818

**Inherits:** IRewardSource

---

#### EmptyGuildClientListener

**Line:** 1051043

**Inherits:** IGuildClientListener

---

#### EmptyGuildModelClientListenerCore

**Line:** 569871

**Inherits:** IGuildModelClientListenerCore

---

#### EmptyGuildModelServerListenerCore

**Line:** 569841

**Inherits:** IGuildModelServerListenerCore

---

#### EmptyGuildServerListener

**Line:** 1051028

**Inherits:** IGuildServerListener

---

#### EmptyGuildWarDivisionModelClientListenerCore

**Line:** 1065789

**Inherits:** IGuildWarDivisionModelClientListenerCore

---

#### EmptyGuildWarDivisionModelServerListenerCore

**Line:** 1065825

**Inherits:** IGuildWarDivisionModelServerListenerCore

---

#### ForeignGuildContext

**Line:** 567644

---

#### ForfeitGuildWarBattleAction

**Line:** 1069049

**Inherits:** PlayerAction

---

#### ForwardRendererData

**Line:** 907249

**Inherits:** ScriptableRendererData

**Fields:**

```
postProcessData: PostProcessData
m_OpaqueLayerMask: LayerMask
m_TransparentLayerMask: LayerMask
m_DefaultStencilState: StencilStateData
m_ShadowTransparentReceive: bool
m_RenderingMode: RenderingMode
m_DepthPrimingMode: DepthPrimingMode
m_AccurateGbufferNormals: bool
m_ClusteredRendering: bool
m_TileSize: TileSize
```

---

#### GetGuildWarBrawlRequest

**Line:** 1064591

**Inherits:** MetaRequest

---

#### GetGuildWarBrawlResponse

**Line:** 1064619

**Inherits:** MetaResponse

**Fields:**

```
BattleModel: GuildWarBattleModel
```

---

#### GuildActionBase

**Line:** 567671

**Inherits:** ModelAction

**Fields:**

```
InvokingPlayerId: EntityId
```

---

#### GuildActionCore

**Line:** 567696

---

#### GuildAddToJoinListRequest

**Line:** 1063474

**Inherits:** MetaRequest

---

#### GuildAddToJoinListResponse

**Line:** 1063513

**Inherits:** MetaResponse

**Fields:**

```
Success: bool
Error: string
```

---

#### GuildBaseConfig

**Line:** 1062172

**Inherits:** GameConfigKeyValue

---

#### GuildBeginViewRequest

**Line:** 571297

**Inherits:** MetaMessage

---

#### GuildBottomUiMenuButton

**Line:** 717614

**Inherits:** BottomUiMenuButton

---

#### GuildChangeRankRequest

**Line:** 1063679

**Inherits:** MetaRequest

**Fields:**

```
PlayerId: EntityId
Role: GuildMemberRole
```

---

#### GuildChangeRankResponse

**Line:** 1063709

**Inherits:** MetaResponse

---

#### GuildClient

**Line:** 570678

---

#### GuildClientActionBase

**Line:** 567686

**Inherits:** GuildActionBase

---

#### GuildClientActionCore

**Line:** 567733

---

#### GuildClientContext

**Line:** 567837

---

#### GuildClientListener

**Line:** 716315

**Inherits:** IGuildModelClientListenerCore

---

#### GuildCreateInvitationRequest

**Line:** 571471

**Inherits:** MetaMessage

---

#### GuildCreateInvitationResponse

**Line:** 571545

**Inherits:** MetaMessage

---

#### GuildCreateInvitationResult

**Line:** 570219

---

#### GuildCreateRequest

**Line:** 570738

**Inherits:** MetaMessage

---

#### GuildCreateResponse

**Line:** 570766

**Inherits:** MetaMessage

---

#### GuildCreationData

**Line:** 1063839

---

#### GuildCreationFailedMessage

**Line:** 1063993

**Inherits:** MetaMessage

**Fields:**

```
FailedReason: GuildCreationFailedEnum
```

---

#### GuildCreationParams

**Line:** 1063933

**Inherits:** GuildCreationParamsBase

---

#### GuildCreationParamsBase

**Line:** 569656

---

#### GuildCreationRequestParams

**Line:** 1063904

**Inherits:** GuildCreationRequestParamsBase

---

#### GuildCreationRequestParamsBase

**Line:** 569695

---

#### GuildDiscoveryInfo

**Line:** 1062766

**Inherits:** GuildDiscoveryInfoBase

---

#### GuildDiscoveryInfoBase

**Line:** 567578

**Fields:**

```
GuildId: EntityId
DisplayName: string
NumMembers: int
MaxNumMembers: int
```

---

#### GuildDiscoveryRequest

**Line:** 571146

**Inherits:** MetaMessage

---

#### GuildDiscoveryResponse

**Line:** 571156

**Inherits:** MetaMessage

**Fields:**

```
GuildInfos: List<GuildDiscoveryInfoBase>
```

---

#### GuildEditTagAndAnnouncementAction

**Line:** 1064362

**Inherits:** GuildActionCore

---

#### GuildEmblemColors

**Line:** 1062396

**Inherits:** IGameConfigData

---

#### GuildEmblemDisplay

**Line:** 718029

**Inherits:** MonoBehaviour

**Fields:**

```
_shapeImage: Image
_iconImage: Image
_handleImage: Image
```

---

#### GuildEmblemInfo

**Line:** 1062893

**Inherits:** IGuildEmblemInfo

---

#### GuildEndViewRequest

**Line:** 571414

**Inherits:** MetaMessage

---

#### GuildEnqueueActionsRequest

**Line:** 570835

**Inherits:** MetaMessage

---

#### GuildEventBase

**Line:** 568408

**Inherits:** EntityEventBase

---

#### GuildEventCreated

**Line:** 568017

**Inherits:** GuildEventBase

---

#### GuildEventDeserializationFailureSubstitute

**Line:** 567863

**Inherits:** GuildEventBase

---

#### GuildEventFounderJoined

**Line:** 568062

**Inherits:** GuildEventBase

---

#### GuildEventLog

**Line:** 568418

**Inherits:** EntityEventLog

---

#### GuildEventLogEntry

**Line:** 568395

**Inherits:** EntityEventLogEntry

---

#### GuildEventMemberJoined

**Line:** 568096

**Inherits:** GuildEventBase

---

#### GuildEventMemberKicked

**Line:** 568164

**Inherits:** GuildEventBase

---

#### GuildEventMemberLeft

**Line:** 568130

**Inherits:** GuildEventBase

---

#### GuildEventMemberRemovedDueToInconsistency

**Line:** 568222

**Inherits:** GuildEventBase

---

#### GuildEventModelSchemaMigrated

**Line:** 568350

**Inherits:** GuildEventBase

---

#### GuildEventNameAndDescriptionChanged

**Line:** 568268

**Inherits:** GuildEventBase

---

#### GuildFormationTest

**Line:** 720365

**Inherits:** MonoBehaviour

**Fields:**

```
MeleeCountGuild1: int
RangedCountGuild1: int
MeleeCountGuild2: int
RangedCountGuild2: int
AnchorX: float
Spacing: float
Flip: bool
```

---

#### GuildHiddenAction

**Line:** 572162

**Inherits:** GuildActionBase

---

#### GuildInspectInvitationRequest

**Line:** 571631

**Inherits:** MetaMessage

---

#### GuildInspectInvitationResponse

**Line:** 571681

**Inherits:** MetaMessage

---

#### GuildInviteInfo

**Line:** 570234

---

#### GuildInviteState

**Line:** 568520

**Fields:**

```
Type: GuildInviteType
CreatedAt: MetaTime
ExpiresAfter: Nullable<MetaDuration>
NumMaxUsages: int
NumTimesUsed: int
InviteCode: GuildInviteCode
```

---

#### GuildInviteUpdate

**Line:** 572109

**Inherits:** GuildActionBase

---

#### GuildInviterAvatarBase

**Line:** 569783

---

#### GuildJoinRequest

**Line:** 571003

**Inherits:** MetaMessage

---

#### GuildJoinRequestObject

**Line:** 1063455

**Fields:**

```
PlayerInfo: PlayerInfo
RequestTime: MetaTime
```

---

#### GuildJoinResponse

**Line:** 571064

**Inherits:** MetaMessage

---

#### GuildLeaveRequest

**Line:** 570806

**Inherits:** MetaMessage

---

#### GuildMemberAdd

**Line:** 571857

**Inherits:** GuildActionBase

---

#### GuildMemberBase

**Line:** 568802

**Fields:**

```
IsOnline: bool
LastOnlineAt: MetaTime
DisplayName: string
LastGuildOpEpoch: int
LastPendingPlayerOpEpoch: int
PendingPlayerOps: MetaDictionary<int, GuildMemberPlayerOpLogEntry>
MemberInstanceId: int
Role: GuildMemberRole
Invites: MetaDictionary<int, GuildInviteState>
```

---

#### GuildMemberDailyScoreContribution

**Line:** 1065961

---

#### GuildMemberEditRole

**Line:** 571804

**Inherits:** GuildClientActionBase

---

#### GuildMemberGuildOpLogEntry

**Line:** 568555

---

#### GuildMemberIsOnlineUpdate

**Line:** 571941

**Inherits:** GuildActionBase

---

#### GuildMemberKick

**Line:** 571762

**Inherits:** GuildClientActionBase

---

#### GuildMemberKickReason

**Line:** 1063605

**Inherits:** IGuildMemberKickReason

---

#### GuildMemberKickRequest

**Line:** 1063634

**Inherits:** MetaRequest

**Fields:**

```
PlayerId: EntityId
KickReason: IGuildMemberKickReason
```

---

#### GuildMemberKickResponse

**Line:** 1063663

**Inherits:** MetaResponse

---

#### GuildMemberModel

**Line:** 1062976

**Inherits:** GuildMemberBase

**Fields:**

```
PlayerInfo: PlayerInfo
```

---

#### GuildMemberPlayerData

**Line:** 1063032

**Inherits:** GuildMemberPlayerDataBase

---

#### GuildMemberPlayerDataBase

**Line:** 569706

---

#### GuildMemberPlayerDataUpdate

**Line:** 571994

**Inherits:** GuildActionBase

---

#### GuildMemberPlayerOpLogEntry

**Line:** 568565

---

#### GuildMemberPrivateStateBase

**Line:** 569750

**Inherits:** MultiplayerMemberPrivateStateBase

---

#### GuildMemberRemove

**Line:** 571910

**Inherits:** GuildActionBase

---

#### GuildMemberRolesUpdate

**Line:** 572078

**Inherits:** GuildActionBase

---

#### GuildMemberTransferLeadershipRequest

**Line:** 1063561

**Inherits:** MetaRequest

**Fields:**

```
PlayerId: EntityId
```

---

#### GuildMemberTransferLeadershipResponse

**Line:** 1063589

**Inherits:** MetaResponse

---

#### GuildMessageCodes

**Line:** 1058007

---

#### GuildModel

**Line:** 1063149

**Inherits:** GuildModelBase

**Fields:**

```
ApprovedInFlightRequests: HashSet<EntityId>
```

---

#### GuildModelBase

**Line:** 568899

---

#### GuildModelRuntimeDataBase

**Line:** 569608

---

#### GuildNameAndDescriptionUpdate

**Line:** 572036

**Inherits:** GuildActionBase

---

#### GuildNotFoundException

**Line:** 716845

**Inherits:** Exception

---

#### GuildPendingMemberKickState

**Line:** 568620

**Fields:**

```
IssuedAt: MetaTime
ReasonOrNull: IGuildMemberKickReason
PendingPlayerOps: MetaDictionary<int, GuildMemberPlayerOpLogEntry>
MemberInstanceId: int
```

---

#### GuildRedDotLogic

**Line:** 719378

**Inherits:** IRedDotLogic

**Fields:**

```
_cachedJoinRequests: HashSet<GuildJoinRequestObject>
```

---

#### GuildRequirementsValidator

**Line:** 569886

**Inherits:** IMetaIntegrationSingleton

---

#### GuildRevokeInvitationRequest

**Line:** 571602

**Inherits:** MetaMessage

---

#### GuildSearchRequest

**Line:** 571173

**Inherits:** MetaMessage

**Fields:**

```
SearchParams: GuildSearchParamsBase
```

---

#### GuildSearchResponse

**Line:** 571189

**Inherits:** MetaMessage

**Fields:**

```
IsError: bool
GuildInfos: List<GuildDiscoveryInfoBase>
```

---

#### GuildSetCurrentDivision

**Line:** 1064884

**Inherits:** GuildActionCore

---

#### GuildSwitchedMessage

**Line:** 571106

**Inherits:** MetaMessage

---

#### GuildTabFeature

**Line:** 718719

**Inherits:** Feature

---

#### GuildTabUiMenuButton

**Line:** 719212

**Inherits:** UiUnityView

**Fields:**

```
Label: TMP_Text
Type: GuildTabType
Button: UnityButton
SelectedHighlight: GameObject
UnselectedHighlight: GameObject
RightSideSeparator: GameObject
_sequence: Sequence
```

---

#### GuildTierConfig

**Line:** 1062465

**Inherits:** IGameConfigData

---

#### GuildTimelineUpdateMessage

**Line:** 570914

**Inherits:** MetaMessage

---

#### GuildTransactionBase

**Line:** 570048

---

#### GuildTransactionRequest

**Line:** 571207

**Inherits:** MetaMessage

---

#### GuildTransactionResponse

**Line:** 571246

**Inherits:** MetaMessage

---

#### GuildUpdateJoinRequests

**Line:** 1064009

**Inherits:** GuildActionBase

---

#### GuildViewEnded

**Line:** 571442

**Inherits:** MetaMessage

---

#### GuildViewResponse

**Line:** 571346

**Inherits:** MetaMessage

---

#### GuildWarAddHistoricalDivisionEntry

**Line:** 1064937

**Inherits:** GuildActionCore

---

#### GuildWarAvatar

**Line:** 1065129

---

#### GuildWarBattleGuildModel

**Line:** 1069088

---

#### GuildWarBattleHistory

**Line:** 1065567

---

#### GuildWarBattleModel

**Line:** 1069227

---

#### GuildWarBattlePlayerProfileModel

**Line:** 1069303

---

#### GuildWarBattleStartAction

**Line:** 1069062

**Inherits:** PlayerAction

---

#### GuildWarBattleStartCheatAction

**Line:** 1069075

**Inherits:** PlayerAction

---

#### GuildWarBattleUi

**Line:** 720515

**Inherits:** MonoBehaviour

**Fields:**

```
Guild1Name: TMP_Text
Guild2Name: TMP_Text
Guild1Power: TMP_Text
Guild2Power: TMP_Text
```

---

#### GuildWarBrawlState

**Line:** 1065683

---

#### GuildWarClient

**Line:** 1065181

**Inherits:** LeagueClient

---

#### GuildWarConcludeAndAssignRewards

**Line:** 1064518

**Inherits:** PlayerSynchronizedServerActionCore

---

#### GuildWarConcludedMessage

**Line:** 1065192

**Inherits:** MetaMessage

---

#### GuildWarConfig

**Line:** 1062587

**Inherits:** GameConfigKeyValue

---

#### GuildWarDayModel

**Line:** 717266

---

#### GuildWarDebugTool

**Line:** 720410

**Inherits:** MonoBehaviour

**Fields:**

```
InputField: TMP_InputField
InfoText: TMP_Text
FlipButton: UnityToggleButton
FetchButton: UnityButton
StartButton: UnityButton
```

---

#### GuildWarDivisionAddOrUpdateParticipant

**Line:** 1064830

**Inherits:** DivisionActionBase

---

#### GuildWarDivisionBattleDayMessage

**Line:** 716931

**Inherits:** IMessage

---

#### GuildWarDivisionClientListener

**Line:** 716940

**Inherits:** IGuildWarDivisionModelClientListenerCore

---

#### GuildWarDivisionClientState

**Line:** 1065362

**Inherits:** DivisionClientStateBase

---

#### GuildWarDivisionHistory

**Line:** 1065237

**Inherits:** IDivisionHistoryEntry

---

#### GuildWarDivisionModel

**Line:** 1065851

**Inherits:** DivisionModelBase

**Fields:**

```
_clientListener: IDivisionModelClientListenerCore
_serverListener: IDivisionModelServerListenerCore
BrawlState: GuildWarBrawlState
```

---

#### GuildWarDivisionModelUpdateTick

**Line:** 716913

**Inherits:** IMessage

---

#### GuildWarDivisionParticipantState

**Line:** 1065733

**Inherits:** DivisionParticipantStateBase

---

#### GuildWarDivisionScore

**Line:** 1066159

**Inherits:** IDivisionScore

---

#### GuildWarDivisionUpdateContribution

**Line:** 1065076

**Inherits:** DivisionActionBase

---

#### GuildWarDivisionUpdateCurrentDay

**Line:** 1064635

**Inherits:** DivisionActionBase

---

#### GuildWarDivisionWarEndedMessage

**Line:** 716922

**Inherits:** IMessage

---

#### GuildWarFeature

**Line:** 720442

**Inherits:** Feature

---

#### GuildWarFormationBuilder

**Line:** 1069576

---

#### GuildWarHistoricalDivisionAdded

**Line:** 1065209

**Inherits:** MetaMessage

---

#### GuildWarMarkAsGivenTicketAction

**Line:** 1064679

**Inherits:** DivisionActionBase

---

#### GuildWarMemberChallengeInformation

**Line:** 1065025

**Fields:**

```
ChallengedMemberId: EntityId
ChallengedBy: EntityId
ChallengedByGuildId: EntityId
ChallengedByMemberInfo: GuildMemberDailyScoreContribution
DidWin: bool
ChallengeTime: MetaTime
```

---

#### GuildWarMemberInfo

**Line:** 1065432

---

#### GuildWarPlayerReward

**Line:** 1065391

**Inherits:** DivisionPlayerRewardsBase

---

#### GuildWarSeasonConcludedAnalyticsEvent

**Line:** 1064135

**Inherits:** GuildEventBase

---

#### GuildWarUpdateBrawlResult

**Line:** 1065001

**Inherits:** DivisionActionBase

**Fields:**

```
BrawlId: EntityId
Result: PvpBattleResult
Winner: EntityId
```

---

#### GuildWarUpdateMemberListAction

**Line:** 1064788

**Inherits:** DivisionActionBase

---

#### GuildWarUpdateMemberProfileAction

**Line:** 1064721

**Inherits:** DivisionActionBase

---

#### GuildWarUpdateNextSeasonStartTimeAction

**Line:** 1064404

**Inherits:** GuildActionCore

---

#### GuildsEnabledCondition

**Line:** 569965

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### GuildsFeature

**Line:** 716904

**Inherits:** Feature

---

#### GuildsLocalizer

**Line:** 721023

**Inherits:** LocalizerBase

---

#### LegacyMountChestReward

**Line:** 1052444

**Inherits:** PlayerReward

---

#### MemberInfo

**Line:** 265656

**Inherits:** ICustomAttributeProvider

---

#### MessageRoutingRuleCurrentGuild

**Line:** 499051

**Inherits:** MessageRoutingRule

---

#### MetaGuildReward

**Line:** 532931

---

#### MetaGuildRewardBase

**Line:** 532917

**Inherits:** MetaReward

---

#### MetaPlayerReward

**Line:** 532977

---

#### MetaPlayerRewardBase

**Line:** 532963

**Inherits:** MetaReward

---

#### MetaReward

**Line:** 533015

---

#### NotInAGuildException

**Line:** 716865

**Inherits:** Exception

---

#### PetEggReward

**Line:** 1079070

**Inherits:** PlayerReward

---

#### PlayerClaimHistoricalPlayerDivisionRewards

**Line:** 565189

**Inherits:** PlayerActionCore

---

#### PlayerEditGuildCooldownTime

**Line:** 1064104

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerEventLiveOpsEventAudienceMembershipChanged

**Line:** 537672

**Inherits:** PlayerEventBase

---

#### PlayerGuildFetchJoinsRequest

**Line:** 1063776

**Inherits:** MetaRequest

---

#### PlayerGuildFetchJoinsResponse

**Line:** 1063797

**Inherits:** MetaResponse

---

#### PlayerGuildInfo

**Line:** 1058488

---

#### PlayerGuildModel

**Line:** 1069593

---

#### PlayerGuildStateCore

**Line:** 533887

**Inherits:** IPlayerGuildState

---

#### PlayerGuildWarModel

**Line:** 1069680

---

#### PlayerGuildWarProgressPass

**Line:** 1069761

---

#### PlayerOnGuildWarLastDayMessage

**Line:** 1066263

**Inherits:** MetaMessage

---

#### PlayerReward

**Line:** 1078781

**Inherits:** MetaPlayerReward

---

#### PlayerRewardTypeCode

**Line:** 1078758

---

#### PlayerSetLiveOpsEventAudienceMembershipFlag

**Line:** 563075

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerUpdateGuildWarStateAction

**Line:** 1064300

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerUpdateGuildWarTicketsAction

**Line:** 1064457

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerUpdateGuildWarTotalPoints

**Line:** 1064549

**Inherits:** PlayerSynchronizedServerActionCore

---

#### ProgressPassPurchaseReward

**Line:** 1079114

**Inherits:** PlayerReward

---

#### ProgressPassReward

**Line:** 1078641

---

#### PublicMemberInfo

**Line:** 1584013

---

#### RequestGlobalGuildLeaderboard

**Line:** 1067102

**Inherits:** MetaRequest

---

#### ResponseGlobalGuildLeaderboardMessage

**Line:** 1067112

**Inherits:** MetaResponse

**Fields:**

```
Leaderboard: MetaDictionary<EntityId, GuildDiscoveryInfo>
```

---

#### RewardCheatAction

**Line:** 1079147

**Inherits:** PlayerAction

---

#### RewardVisualConfig

**Line:** 728556

**Inherits:** ScriptableObject

**Fields:**

```
CurrencyIcons: SerializableDictionary<CurrencyType, Sprite>
```

---

#### SkinReward

**Line:** 1052254

**Inherits:** PlayerReward

---

#### StarterPackageReward

**Line:** 1079189

**Inherits:** PlayerReward

---

#### UpdateGuildAnnouncementAction

**Line:** 1062100

**Inherits:** GuildClientActionBase

---

#### UpdateGuildInfoForPlayer

**Line:** 1064062

**Inherits:** PlayerSynchronizedServerActionCore

---

#### UpdateGuildJoinSettingAction

**Line:** 1062131

**Inherits:** GuildClientActionBase

---

#### ViewGuildRefusedException

**Line:** 570210

**Inherits:** Exception

---

#### WarPointsReward

**Line:** 1079260

**Inherits:** PlayerReward

---

#### WarTaskConfig

**Line:** 1062727

---

#### WarTasksDayConfig

**Line:** 1062673

**Inherits:** IGameConfigData

---

## Other

**Classes:** 508 | **Enums:** 1021

### Enumerations

#### APVConstantBufferRegister

**Line:** 820291

**Values:**

```
GlobalRegister = 6
```

---

#### APVLeakReductionMode

**Line:** 820300

**Values:**

```
None = 0
Performance = 1
Quality = 2
ValidityBased = 1
ValidityAndNormalBased = 2
```

---

#### AcceptRejectRule

**Line:** 1083069

**Values:**

```
None = 0
Cascade = 1
```

---

#### AccessFlags

**Line:** 829126

**Values:**

```
None = 0
Read = 1
Write = 2
Discard = 4
WriteAll = 6
ReadWrite = 3
```

---

#### ActivityIdFormat

**Line:** 1417492

**Values:**

```
Unknown = 0
Hierarchical = 1
W3C = 2
```

---

#### ActivityKind

**Line:** 1418154

**Values:**

```
Internal = 0
Server = 1
Client = 2
Producer = 3
Consumer = 4
```

---

#### ActivitySamplingResult

**Line:** 1418091

**Values:**

```
None = 0
PropagationData = 1
AllData = 2
AllDataAndRecorded = 3
```

---

#### ActivityStatusCode

**Line:** 1417624

**Values:**

```
Unset = 0
Ok = 1
Error = 2
```

---

#### ActivityTraceFlags

**Line:** 1417483

**Values:**

```
None = 0
Recorded = 1
```

---

#### ActivityTrackingOptions

**Line:** 1553877

**Values:**

```
None = 0
SpanId = 1
TraceId = 2
ParentId = 4
TraceState = 8
TraceFlags = 16
Tags = 32
Baggage = 64
```

---

#### AdditionalCanvasShaderChannels

**Line:** 1576383

**Values:**

```
None = 0
TexCoord1 = 1
TexCoord2 = 2
TexCoord3 = 4
Normal = 8
Tangent = 16
```

---

#### AddressFamily

**Line:** 800285

**Values:**

```
Unspecified = 0
Unix = 1
InterNetwork = 2
ImpLink = 3
Pup = 4
Chaos = 5
NS = 6
Ipx = 6
Iso = 7
Osi = 7
Ecma = 8
DataKit = 9
Ccitt = 10
Sna = 11
DecNet = 12
DataLink = 13
Lat = 14
HyperChannel = 15
AppleTalk = 16
NetBios = 17
VoiceView = 18
FireFox = 19
Banyan = 21
Atm = 22
InterNetworkV6 = 23
Cluster = 24
Ieee12844 = 25
Irda = 26
NetworkDesigners = 28
Max = 29
```

---

#### Addressables

**Line:** 1453852

---

#### AddressablesPlatform

**Line:** 1455988

**Values:**

```
Unknown = 0
Windows = 1
OSX = 2
Linux = 3
PS4 = 4
Switch = 5
XboxOne = 6
WebGL = 7
iOS = 8
Android = 9
WindowsUniversal = 10
```

---

#### AdminActionPlacement

**Line:** 601164

**Values:**

```
Gentle = 0
Disruptive = 1
Dangerous = 2
```

---

#### AdvancedUpscalers

**Line:** 809859

**Values:**

```
DLSS = 0
FSR2 = 1
STP = 2
```

---

#### AlertDescription

**Line:** 1448527

**Values:**

```
CloseNotify = 0
UnexpectedMessage = 10
BadRecordMAC = 20
DecryptionFailed_RESERVED = 21
RecordOverflow = 22
DecompressionFailure = 30
HandshakeFailure = 40
NoCertificate_RESERVED = 41
BadCertificate = 42
UnsupportedCertificate = 43
CertificateRevoked = 44
CertificateExpired = 45
CertificateUnknown = 46
IlegalParameter = 47
UnknownCA = 48
AccessDenied = 49
DecodeError = 50
DecryptError = 51
ExportRestriction = 60
ProtocolVersion = 70
InsuficientSecurity = 71
InternalError = 80
UserCancelled = 90
NoRenegotiation = 100
UnsupportedExtension = 110
```

---

#### Align

**Line:** 659892

**Values:**

```
Auto = 0
FlexStart = 1
Center = 2
FlexEnd = 3
Stretch = 4
```

---

#### Allocator

**Line:** 838032

**Values:**

```
Invalid = 0
None = 1
Temp = 2
TempJob = 3
Persistent = 4
AudioKernel = 5
Domain = 6
FirstUserIndex = 64
```

---

#### AlternatingRowBackground

**Line:** 615329

**Values:**

```
None = 0
ContentOnly = 1
All = 2
```

---

#### AnalyticsResult

**Line:** 1586968

**Values:**

```
Ok = 0
NotInitialized = 1
AnalyticsDisabled = 2
TooManyItems = 3
SizeLimitReached = 4
TooManyRequests = 5
InvalidData = 6
UnsupportedPlatform = 7
```

---

#### AnalyticsSessionState

**Line:** 1585329

**Values:**

```
kSessionStopped = 0
kSessionStarted = 1
kSessionPaused = 2
kSessionResumed = 3
```

---

#### AndroidAssetPackError

**Line:** 1487123

**Values:**

```
NoError = 0
```

---

#### AndroidAssetPackStatus

**Line:** 1487107

**Values:**

```
Unknown = 0
Pending = 1
Downloading = 2
Transferring = 3
Completed = 4
Failed = 5
Canceled = 6
WaitingForWifi = 7
NotInstalled = 8
```

---

#### AndroidColorModeHdr

**Line:** 1487411

**Values:**

```
Undefined = 0
No = 4
Yes = 8
```

---

#### AndroidColorModeWideColorGamut

**Line:** 1487421

**Values:**

```
Undefined = 0
No = 1
Yes = 2
```

---

#### AndroidKeyboard

**Line:** 1487683

**Values:**

```
Undefined = 0
NoKeys = 1
Qwerty = 2
_12Key = 3
```

---

#### AndroidKeyboardHidden

**Line:** 1487694

**Values:**

```
Undefined = 0
No = 1
Yes = 2
```

---

#### AndroidNavigation

**Line:** 1487704

**Values:**

```
Undefined = 0
NoNav = 1
Dpad = 2
TrackBall = 3
Wheel = 4
```

---

#### AndroidNavigationHidden

**Line:** 1487716

**Values:**

```
Undefined = 0
No = 1
Yes = 2
```

---

#### AndroidOrientation

**Line:** 1487726

**Values:**

```
Undefined = 0
Portrait = 1
Landscape = 2
```

---

#### AndroidScreenLayoutDirection

**Line:** 1487736

**Values:**

```
LTR = 64
RTL = 128
```

---

#### AndroidScreenLayoutLong

**Line:** 1487745

**Values:**

```
Undefined = 0
No = 16
Yes = 32
```

---

#### AndroidScreenLayoutRound

**Line:** 1487755

**Values:**

```
Undefined = 0
No = 256
Yes = 512
```

---

#### AndroidScreenLayoutSize

**Line:** 1487765

**Values:**

```
Undefined = 0
Small = 1
Normal = 2
Large = 3
XLarge = 4
```

---

#### AndroidStore

**Line:** 1402110

**Values:**

```
GooglePlay = 0
AmazonAppStore = 1
UDP = 2
NotSpecified = 3
```

---

#### AndroidStoreMeta

**Line:** 1402121

**Values:**

```
AndroidStoreStart = 0
AndroidStoreEnd = 2
```

---

#### AndroidTouchScreen

**Line:** 1487777

**Values:**

```
Undefined = 0
NoTouch = 1
Finger = 3
```

---

#### AndroidUIModeNight

**Line:** 1487787

**Values:**

```
Undefined = 0
No = 16
Yes = 32
```

---

#### AndroidUIModeType

**Line:** 1487797

**Values:**

```
Undefined = 0
Normal = 1
Desk = 2
Car = 3
Television = 4
Appliance = 5
Watch = 6
VrHeadset = 7
```

---

#### AngleUnit

**Line:** 644512

**Values:**

```
Degree = 0
Gradian = 1
Radian = 2
Turn = 3
```

---

#### AngularFalloffType

**Line:** 898871

**Values:**

```
LUT = 0
AnalyticAndInnerAngle = 1
```

---

#### AnimatableProperty

**Line:** 1563324

---

#### AntialiasingMode

**Line:** 914941

**Values:**

```
None = 0
FastApproximateAntialiasing = 1
SubpixelMorphologicalAntiAliasing = 2
TemporalAntiAliasing = 3
```

---

#### AntialiasingQuality

**Line:** 914965

**Values:**

```
Low = 0
Medium = 1
High = 2
```

---

#### AppPauseType

**Line:** 684368

**Values:**

```
User = 0
Ad = 1
Shop = 2
```

---

#### AppStore

**Line:** 1406158

**Values:**

```
NotSpecified = 0
GooglePlay = 1
AmazonAppStore = 2
UDP = 3
MacAppStore = 4
AppleAppStore = 5
WinRT = 6
fake = 7
```

---

#### AppStoreMeta

**Line:** 1406174

**Values:**

```
AndroidStoreStart = 1
AndroidStoreEnd = 3
```

---

#### AppUpdateErrorCode

**Line:** 1578764

**Values:**

```
NoError = 0
NoErrorPartiallyAllowed = 1
ErrorUnknown = 2
ErrorApiNotAvailable = 3
ErrorInvalidRequest = 4
ErrorUpdateUnavailable = 5
ErrorUpdateNotAllowed = 6
ErrorDownloadNotPresent = 7
ErrorUpdateInProgress = 8
ErrorInternalError = 9
ErrorUserCanceled = 10
ErrorUpdateFailed = 11
ErrorPlayStoreNotFound = 12
ErrorAppNotOwned = 13
```

---

#### AppUpdateStatus

**Line:** 1579005

**Values:**

```
Unknown = 0
Pending = 1
Downloading = 2
Downloaded = 3
Installing = 4
Installed = 5
Failed = 6
Canceled = 7
```

---

#### AppUpdateType

**Line:** 1579020

**Values:**

```
Flexible = 0
Immediate = 1
```

---

#### AppleStorePromotionVisibility

**Line:** 1405883

**Values:**

```
Default = 0
Hide = 1
Show = 2
```

---

#### ApplicationInstallMode

**Line:** 870396

**Values:**

```
Unknown = 0
Store = 1
DeveloperBuild = 2
Adhoc = 3
Enterprise = 4
Editor = 5
```

---

#### ApplicationMemoryUsage

**Line:** 870343

**Values:**

```
Unknown = 0
Low = 1
Medium = 2
High = 3
Critical = 4
```

---

#### ApplicationPauseStatus

**Line:** 1308176

**Values:**

```
Running = 0
Pausing = 1
ResumedFromPauseThisFrame = 2
```

---

#### ApplicationStateManager

**Line:** 738070

---

#### Architecture

**Line:** 228832

**Values:**

```
X86 = 0
X64 = 1
Arm = 2
Arm64 = 3
```

---

#### ArchiveStatus

**Line:** 837887

**Values:**

```
InProgress = 0
Complete = 1
Failed = 2
```

---

#### Asn1EndOfIndefiniteLengthNodeType

**Line:** 1543961

**Values:**

```
EndOfStream = 0
EndOfNodeFooter = 1
NotEnd = 2
```

---

#### AspectRatioFitter

**Line:** 1354273

---

#### AssemblyContentType

**Line:** 264940

**Values:**

```
Default = 0
WindowsRuntime = 1
```

---

#### AssemblyHashAlgorithm

**Line:** 275928

**Values:**

```
None = 0
MD5 = 32771
SHA1 = 32772
SHA256 = 32780
SHA384 = 32781
SHA512 = 32782
```

---

#### AssemblyNameFlags

**Line:** 265078

**Values:**

```
None = 0
PublicKey = 1
EnableJITcompileOptimizer = 16384
EnableJITcompileTracking = 32768
Retargetable = 256
```

---

#### AssemblyVersionCompatibility

**Line:** 275941

**Values:**

```
SameMachine = 1
SameProcess = 2
SameDomain = 3
```

---

#### AssetBundleResource

**Line:** 1436670

---

#### AssetLoadMode

**Line:** 1436521

**Values:**

```
RequestedAssetAndDependencies = 0
AllPackedAssetsAndDependencies = 1
```

---

#### AssetLoadingSubsystem

**Line:** 837600

**Values:**

```
Other = 0
Texture = 1
VirtualTexture = 2
Mesh = 3
Audio = 4
Scripts = 5
EntitiesScene = 6
EntitiesStreamBinaryReader = 7
FileInfo = 8
ContentLoading = 9
```

---

#### AstNode

**Line:** 769987

---

#### AsyncOperationStatus

**Line:** 1441281

**Values:**

```
None = 0
Succeeded = 1
Failed = 2
```

---

#### AsynchronousBehaviour

**Line:** 1318500

**Values:**

```
Default = 0
ForceSynchronous = 1
```

---

#### AtlasPopulationMode

**Line:** 1347192

**Values:**

```
Static = 0
Dynamic = 1
DynamicOS = 2
```

---

#### AttributeTargets

**Line:** 20437

**Values:**

```
Assembly = 1
Module = 2
Class = 4
Struct = 8
Enum = 16
Constructor = 32
Method = 64
Property = 128
Field = 256
Event = 512
Interface = 1024
Parameter = 2048
Delegate = 4096
ReturnValue = 8192
GenericParameter = 16384
All = 32767
```

---

#### AuthenticationPlatform

**Line:** 499195

**Values:**

```
DeviceId = 0
Development = 1
GooglePlay = 2
GameCenter = 3
GoogleSignIn = 4
SignInWithApple = 5
FacebookLogin = 6
SignInWithAppleTransfer = 7
GameCenter2020 = 8
GameCenter2020UAGT = 9
_ReservedDontUse1 = 10
Ethereum = 11
ImmutableX = 12
CompanyAccount = 13
_ReservedDontUse2 = 14
Steam = 15
WebLogin = 16
_ReservedDontUse3 = 17
```

---

#### AuthenticationSchemes

**Line:** 791365

**Values:**

```
None = 0
Digest = 1
Negotiate = 2
Ntlm = 4
Basic = 8
Anonymous = 32768
IntegratedWindowsAuthentication = 6
```

---

#### AuthenticationTokenProvider

**Line:** 577134

**Values:**

```
None = 0
Google = 1
OAuth2 = 2
```

---

#### AuthorizationErrorCode

**Line:** 1590207

**Values:**

```
Unknown = 1000
Canceled = 1001
InvalidResponse = 1002
NotHandled = 1003
Failed = 1004
```

---

#### AuthorizationStatus

**Line:** 1564114

**Values:**

```
AUTHORIZED = 0
DENIED = 1
NOT_DETERMINED = 2
RESTRICTED = 3
```

---

#### AutoPlay

**Line:** 1424903

**Values:**

```
None = 0
AutoPlaySequences = 1
AutoPlayTweeners = 2
All = 3
```

---

#### AvgResetInterval

**Line:** 1590680

**Values:**

```
Always = 1
VeryFast = 30
Fast = 60
Normal = 120
Slow = 300
Never = 2147483647
```

---

#### Axis

**Line:** 770022

---

#### AxisConstraint

**Line:** 1424915

**Values:**

```
None = 0
X = 2
Y = 4
Z = 8
W = 16
```

---

#### BackgroundPositionKeyword

**Line:** 659977

**Values:**

```
Center = 0
Top = 1
Bottom = 2
Left = 3
Right = 4
```

---

#### BackgroundSizeType

**Line:** 660000

**Values:**

```
Length = 0
Cover = 1
Contain = 2
```

---

#### BadRequestType

**Line:** 685161

**Values:**

```
Unspecified = 0
NoUserTokenSupplied = 1
NoClientVersionSupplied = 2
InvalidClientVersionSupplied = 3
SaveGameIdNotSupplied = 4
DeviceIdNotSupplied = 5
Other = 6
```

---

#### Base64FormattingOptions

**Line:** 21984

**Values:**

```
None = 0
InsertLineBreaks = 1
```

---

#### BatchBufferTarget

**Line:** 897719

**Values:**

```
Unknown = 0
RawBuffer = 1
ConstantBuffer = 2
```

---

#### BatchCullingFlags

**Line:** 897687

**Values:**

```
None = 0
CullLightmappedShadowCasters = 1
```

---

#### BatchCullingProjectionType

**Line:** 897709

**Values:**

```
Unknown = 0
Perspective = 1
Orthographic = 2
```

---

#### BatchCullingViewType

**Line:** 897696

**Values:**

```
Unknown = 0
Camera = 1
Light = 2
Picking = 3
SelectionOutline = 4
Filtering = 5
```

---

#### BatchDrawCommandFlags

**Line:** 897670

**Values:**

```
None = 0
FlipWinding = 1
HasMotion = 2
IsLightMapped = 4
HasSortingPosition = 8
LODCrossFadeKeyword = 16
LODCrossFadeValuePacked = 32
LODCrossFade = 48
UseLegacyLightmapsKeyword = 64
```

---

#### BatchDrawCommandType

**Line:** 897658

**Values:**

```
Direct = 0
Indirect = 1
Procedural = 2
ProceduralIndirect = 3
```

---

#### BigInteger

**Line:** 1449838

---

#### BigQueryAnalyticsFormatMode

**Line:** 605241

**Values:**

```
Ignore = 0
ExtractDictionaryElements = 1
```

---

#### BindingFlags

**Line:** 265160

**Values:**

```
Default = 0
IgnoreCase = 1
DeclaredOnly = 2
Instance = 4
Static = 8
Public = 16
NonPublic = 32
FlattenHierarchy = 64
InvokeMethod = 256
CreateInstance = 512
GetField = 1024
SetField = 2048
GetProperty = 4096
SetProperty = 8192
PutDispProperty = 16384
PutRefDispProperty = 32768
ExactBinding = 65536
SuppressChangeType = 131072
OptionalParamBinding = 262144
IgnoreReturn = 16777216
DoNotWrapExceptions = 33554432
```

---

#### BindingMode

**Line:** 608848

**Values:**

```
TwoWay = 0
ToSource = 1
ToTarget = 2
ToTargetOnce = 3
```

---

#### BindingSourceSelectionMode

**Line:** 615348

**Values:**

```
Manual = 0
AutoAssign = 1
```

---

#### BindingStatus

**Line:** 607235

**Values:**

```
Success = 0
Failure = 1
Pending = 2
```

---

#### BindingUpdateTrigger

**Line:** 607177

**Values:**

```
WhenDirty = 0
OnSourceChanged = 1
EveryUpdate = 2
```

---

#### BiomeSfx

**Line:** 705716

**Values:**

```
GrassLands = 0
Forest = 1
Jungle = 3
Desert = 4
Snow = 10
PostApocalypse = 20
City = 30
Virtual = 50
None = 9999
```

---

#### BlendMode

**Line:** 891736

**Values:**

```
Zero = 0
One = 1
DstColor = 2
SrcColor = 3
OneMinusDstColor = 4
SrcAlpha = 5
OneMinusSrcColor = 6
DstAlpha = 7
OneMinusDstAlpha = 8
SrcAlphaSaturate = 9
OneMinusSrcAlpha = 10
```

---

#### BlendOp

**Line:** 891755

**Values:**

```
Add = 0
Subtract = 1
ReverseSubtract = 2
Min = 3
Max = 4
LogicalClear = 5
LogicalSet = 6
LogicalCopy = 7
LogicalCopyInverted = 8
LogicalNoop = 9
LogicalInvert = 10
LogicalAnd = 11
LogicalNand = 12
LogicalOr = 13
LogicalNor = 14
LogicalXor = 15
LogicalEquivalence = 16
LogicalAndReverse = 17
LogicalAndInverted = 18
LogicalOrReverse = 19
LogicalOrInverted = 20
Multiply = 21
Screen = 22
Overlay = 23
Darken = 24
Lighten = 25
ColorDodge = 26
ColorBurn = 27
HardLight = 28
SoftLight = 29
Difference = 30
Exclusion = 31
HSLHue = 32
HSLSaturation = 33
HSLColor = 34
HSLLuminosity = 35
```

---

#### BloomDownscaleMode

**Line:** 909135

**Values:**

```
Half = 0
Quarter = 1
```

---

#### BoolParameter

**Line:** 826933

---

#### BoundedChannelFullMode

**Line:** 1524525

**Values:**

```
Wait = 0
DropNewest = 1
DropOldest = 2
DropWrite = 3
```

---

#### BuiltinRenderTextureType

**Line:** 891855

**Values:**

```
None = 0
CurrentActive = 1
CameraTarget = 2
Depth = 3
DepthNormals = 4
ResolvedDepth = 5
PrepassNormalsSpec = 7
PrepassLight = 8
PrepassLightSpec = 9
GBuffer0 = 10
GBuffer1 = 11
GBuffer2 = 12
GBuffer3 = 13
Reflections = 14
MotionVectors = 15
GBuffer4 = 16
GBuffer5 = 17
GBuffer6 = 18
GBuffer7 = 19
```

---

#### BuiltinShaderDefine

**Line:** 892330

**Values:**

```
UNITY_NO_DXT5nm = 0
UNITY_NO_RGBM = 1
UNITY_USE_NATIVE_HDR = 2
UNITY_ENABLE_REFLECTION_BUFFERS = 3
UNITY_FRAMEBUFFER_FETCH_AVAILABLE = 4
UNITY_ENABLE_NATIVE_SHADOW_LOOKUPS = 5
UNITY_METAL_SHADOWS_USE_POINT_FILTERING = 6
UNITY_NO_CUBEMAP_ARRAY = 7
UNITY_NO_SCREENSPACE_SHADOWS = 8
UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS = 9
UNITY_PBS_USE_BRDF1 = 10
UNITY_PBS_USE_BRDF2 = 11
UNITY_PBS_USE_BRDF3 = 12
UNITY_NO_FULL_STANDARD_SHADER = 13
UNITY_SPECCUBE_BOX_PROJECTION = 14
UNITY_SPECCUBE_BLENDING = 15
UNITY_ENABLE_DETAIL_NORMALMAP = 16
SHADER_API_MOBILE = 17
SHADER_API_DESKTOP = 18
UNITY_HARDWARE_TIER1 = 19
UNITY_HARDWARE_TIER2 = 20
UNITY_HARDWARE_TIER3 = 21
UNITY_COLORSPACE_GAMMA = 22
UNITY_LIGHT_PROBE_PROXY_VOLUME = 23
UNITY_HALF_PRECISION_FRAGMENT_SHADER_REGISTERS = 24
UNITY_LIGHTMAP_DLDR_ENCODING = 25
UNITY_LIGHTMAP_RGBM_ENCODING = 26
UNITY_LIGHTMAP_FULL_HDR = 27
UNITY_VIRTUAL_TEXTURING = 28
UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION = 29
UNITY_ASTC_NORMALMAP_ENCODING = 30
SHADER_API_GLES30 = 31
SHADER_API_GLES31 = 32
SHADER_API_GLES32 = 33
UNITY_UNIFIED_SHADER_PRECISION_MODEL = 34
UNITY_PLATFORM_SUPPORTS_WAVE_32 = 35
UNITY_PLATFORM_SUPPORTS_WAVE_64 = 36
UNITY_NEEDS_RENDERPASS_FBFETCH_FALLBACK = 37
UNITY_PLATFORM_SUPPORTS_DEPTH_FETCH = 38
```

---

#### BurstCompilerService

**Line:** 869185

---

#### BurstExecutionEnvironment

**Line:** 1330476

**Values:**

```
Default = 0
NonDeterministic = 0
Deterministic = 1
```

---

#### BurstString

**Line:** 1330801

---

#### ButtonLayoutType

**Line:** 1565283

**Values:**

```
Undefined = 0
Column = 1
Row = 2
Grid = 3
```

---

#### ButtonSfx

**Line:** 705814

**Values:**

```
Beveled = 0
Toggle = 1
Simple = 2
```

---

#### ButtonType

**Line:** 1565329

**Values:**

```
AcceptAll = 0
DenyAll = 1
More = 2
Save = 3
```

---

#### CalendarWeekRule

**Line:** 271044

**Values:**

```
FirstDay = 0
FirstFullWeek = 1
FirstFourDayWeek = 2
```

---

#### CallingConvention

**Line:** 229354

**Values:**

```
Winapi = 1
Cdecl = 2
StdCall = 3
ThisCall = 4
FastCall = 5
```

---

#### CallingConventions

**Line:** 265189

**Values:**

```
Standard = 1
VarArgs = 2
Any = 3
HasThis = 32
ExplicitThis = 64
```

---

#### Camera

**Line:** 870800

---

#### CameraClearFlags

**Line:** 875311

**Values:**

```
Skybox = 1
Color = 2
SolidColor = 2
Depth = 3
Nothing = 4
```

---

#### CameraLateLatchMatrixType

**Line:** 892486

**Values:**

```
View = 0
InverseView = 1
ViewProjection = 2
InverseViewProjection = 3
```

---

#### CameraOverrideOption

**Line:** 914920

**Values:**

```
Off = 0
On = 1
UsePipelineSettings = 2
```

---

#### CameraRenderType

**Line:** 914956

**Values:**

```
Base = 0
Overlay = 1
```

---

#### CameraType

**Line:** 875201

**Values:**

```
Game = 1
SceneView = 2
Preview = 4
VR = 8
Reflection = 16
```

---

#### CanvasScaler

**Line:** 1354393

---

#### CanvasUpdate

**Line:** 1351639

**Values:**

```
Prelayout = 0
Layout = 1
PostLayout = 2
PreRender = 3
LatePreRender = 4
MaxUpdateValue = 5
```

---

#### CaretPosition

**Line:** 1229687

**Values:**

```
None = 0
Left = 1
Right = 2
```

---

#### CaseSensitivityType

**Line:** 1322369

**Values:**

```
CaseSensitive = 0
CaseInsensitive = 1
```

---

#### Cer

**Line:** 229983

**Values:**

```
None = 0
MayFail = 1
Success = 2
```

---

#### CharSet

**Line:** 228521

**Values:**

```
None = 1
Ansi = 2
Unicode = 3
Auto = 4
```

---

#### CharacterSubstitutor

**Line:** 1319801

---

#### ChatConnectionState

**Line:** 706365

**Values:**

```
Connected = 0
Connecting = 1
Disconnecting = 2
Disconnected = 3
```

---

#### ChecksumGranularity

**Line:** 576346

**Values:**

```
PerOperation = 0
PerBatch = 1
PerActionSingleTickPerFrame = 2
None = 3
```

---

#### CipherAlgorithmType

**Line:** 778408

**Values:**

```
None = 0
Null = 24576
Aes = 26129
Aes128 = 26126
Aes192 = 26127
Aes256 = 26128
Des = 26113
Rc2 = 26114
Rc4 = 26625
TripleDes = 26115
```

---

#### CipherMode

**Line:** 217941

**Values:**

```
CBC = 1
ECB = 2
OFB = 3
CFB = 4
CTS = 5
```

---

#### CipherSuiteCode

**Line:** 1448618

**Values:**

```
TLS_NULL_WITH_NULL_NULL = 0
TLS_RSA_WITH_NULL_MD5 = 1
TLS_RSA_WITH_NULL_SHA = 2
TLS_RSA_EXPORT_WITH_RC4_40_MD5 = 3
TLS_RSA_WITH_RC4_128_MD5 = 4
TLS_RSA_WITH_RC4_128_SHA = 5
TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5 = 6
TLS_RSA_WITH_IDEA_CBC_SHA = 7
TLS_RSA_EXPORT_WITH_DES40_CBC_SHA = 8
TLS_RSA_WITH_DES_CBC_SHA = 9
TLS_RSA_WITH_3DES_EDE_CBC_SHA = 10
TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA = 11
TLS_DH_DSS_WITH_DES_CBC_SHA = 12
TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA = 13
TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA = 14
TLS_DH_RSA_WITH_DES_CBC_SHA = 15
TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA = 16
TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA = 17
TLS_DHE_DSS_WITH_DES_CBC_SHA = 18
TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA = 19
TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA = 20
TLS_DHE_RSA_WITH_DES_CBC_SHA = 21
TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA = 22
TLS_DH_anon_EXPORT_WITH_RC4_40_MD5 = 23
TLS_DH_anon_WITH_RC4_128_MD5 = 24
TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA = 25
TLS_DH_anon_WITH_DES_CBC_SHA = 26
TLS_DH_anon_WITH_3DES_EDE_CBC_SHA = 27
TLS_RSA_WITH_AES_128_CBC_SHA = 47
TLS_DH_DSS_WITH_AES_128_CBC_SHA = 48
TLS_DH_RSA_WITH_AES_128_CBC_SHA = 49
TLS_DHE_DSS_WITH_AES_128_CBC_SHA = 50
TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 51
TLS_DH_anon_WITH_AES_128_CBC_SHA = 52
TLS_RSA_WITH_AES_256_CBC_SHA = 53
TLS_DH_DSS_WITH_AES_256_CBC_SHA = 54
TLS_DH_RSA_WITH_AES_256_CBC_SHA = 55
TLS_DHE_DSS_WITH_AES_256_CBC_SHA = 56
TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 57
TLS_DH_anon_WITH_AES_256_CBC_SHA = 58
TLS_RSA_WITH_CAMELLIA_128_CBC_SHA = 65
TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA = 66
TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA = 67
TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA = 68
TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA = 69
TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA = 70
TLS_RSA_WITH_CAMELLIA_256_CBC_SHA = 132
TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA = 133
TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA = 134
TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA = 135
TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA = 136
TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA = 137
TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 186
TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256 = 187
TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 188
TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256 = 189
TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 = 190
TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256 = 191
TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 = 192
TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256 = 193
TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256 = 194
TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256 = 195
TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256 = 196
TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256 = 197
TLS_RSA_WITH_SEED_CBC_SHA = 150
TLS_DH_DSS_WITH_SEED_CBC_SHA = 151
TLS_DH_RSA_WITH_SEED_CBC_SHA = 152
TLS_DHE_DSS_WITH_SEED_CBC_SHA = 153
TLS_DHE_RSA_WITH_SEED_CBC_SHA = 154
TLS_DH_anon_WITH_SEED_CBC_SHA = 155
TLS_PSK_WITH_RC4_128_SHA = 138
TLS_PSK_WITH_3DES_EDE_CBC_SHA = 139
TLS_PSK_WITH_AES_128_CBC_SHA = 140
TLS_PSK_WITH_AES_256_CBC_SHA = 141
TLS_DHE_PSK_WITH_RC4_128_SHA = 142
TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA = 143
TLS_DHE_PSK_WITH_AES_128_CBC_SHA = 144
TLS_DHE_PSK_WITH_AES_256_CBC_SHA = 145
TLS_RSA_PSK_WITH_RC4_128_SHA = 146
TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA = 147
TLS_RSA_PSK_WITH_AES_128_CBC_SHA = 148
TLS_RSA_PSK_WITH_AES_256_CBC_SHA = 149
TLS_ECDH_ECDSA_WITH_NULL_SHA = 49153
TLS_ECDH_ECDSA_WITH_RC4_128_SHA = 49154
TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA = 49155
TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA = 49156
TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA = 49157
TLS_ECDHE_ECDSA_WITH_NULL_SHA = 49158
TLS_ECDHE_ECDSA_WITH_RC4_128_SHA = 49159
TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA = 49160
TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = 49161
TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = 49162
TLS_ECDH_RSA_WITH_NULL_SHA = 49163
TLS_ECDH_RSA_WITH_RC4_128_SHA = 49164
TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA = 49165
TLS_ECDH_RSA_WITH_AES_128_CBC_SHA = 49166
```

---

#### ClampedDragger

**Line:** 609815

---

#### ClassInterfaceType

**Line:** 229045

**Values:**

```
None = 0
AutoDispatch = 1
AutoDual = 2
```

---

#### CleanupMode

**Line:** 1597338

**Values:**

```
RemoveComponent = 0
DestroyEntity = 1
```

---

#### ClearFlag

**Line:** 807060

**Values:**

```
None = 0
Color = 1
Depth = 2
Stencil = 4
DepthStencil = 6
ColorStencil = 5
All = 7
```

---

#### ClientAppPauseStatus

**Line:** 533434

**Values:**

```
Running = 0
Paused = 1
Unpausing = 2
```

---

#### ClientCertificateOption

**Line:** 1488190

**Values:**

```
Manual = 0
Automatic = 1
```

---

#### ClientLogEntryType

**Line:** 573980

**Values:**

```
Log = 0
Warning = 1
Error = 2
Assert = 3
Exception = 4
```

---

#### ClientPlatform

**Line:** 500024

**Values:**

```
Unknown = 0
iOS = 1
Android = 2
WebGL = 3
UnityEditor = 4
```

---

#### ClientPlaybackMode

**Line:** 552163

**Values:**

```
Instant = 0
Smooth = 1
```

---

#### ClipType

**Line:** 1361470

**Values:**

```
ctIntersection = 0
ctUnion = 1
ctDifference = 2
ctXor = 3
```

---

#### Clipper2D

**Line:** 899813

---

#### ClipperOffset2D

**Line:** 899902

---

#### CollectionAccessType

**Line:** 869361

**Values:**

```
None = 0
Read = 1
ModifyExistingContent = 2
UpdatedContent = 6
```

---

#### CollectionChangeAction

**Line:** 781255

**Values:**

```
Add = 1
Remove = 2
Refresh = 3
```

---

#### CollectionVirtualizationMethod

**Line:** 615339

**Values:**

```
FixedHeight = 0
DynamicHeight = 1
```

---

#### ColorGamut

**Line:** 875359

**Values:**

```
sRGB = 0
Rec709 = 1
Rec2020 = 2
DisplayP3 = 3
HDR10 = 4
DolbyHDR = 5
P3D65G22 = 6
```

---

#### ColorGradientMode

**Line:** 1348269

**Values:**

```
Single = 0
HorizontalGradient = 1
VerticalGradient = 2
FourCornersGradient = 3
```

---

#### ColorGradingMode

**Line:** 900551

**Values:**

```
LowDynamicRange = 0
HighDynamicRange = 1
```

---

#### ColorMode

**Line:** 1221677

**Values:**

```
Single = 0
HorizontalGradient = 1
VerticalGradient = 2
FourCornersGradient = 3
```

---

#### ColorPrimaries

**Line:** 875375

**Values:**

```
Rec709 = 0
Rec2020 = 1
P3 = 2
```

---

#### ColorSpace

**Line:** 875347

**Values:**

```
Gamma = 0
Linear = 1
```

---

#### ColorTween

**Line:** 1358292

---

#### ColorType

**Line:** 1062162

**Values:**

```
Background = 0
Foreground = 1
```

---

#### ColorWriteMask

**Line:** 891827

**Values:**

```
Alpha = 1
Blue = 2
Green = 4
Red = 8
All = 15
```

---

#### ColumnSortingMode

**Line:** 625989

**Values:**

```
None = 0
Default = 1
Custom = 2
```

---

#### Columns

**Line:** 625670

---

#### ComInterfaceType

**Line:** 229003

**Values:**

```
InterfaceIsDual = 0
InterfaceIsIUnknown = 1
InterfaceIsIDispatch = 2
InterfaceIsIInspectable = 3
```

---

#### CommandBufferExecutionFlags

**Line:** 892450

**Values:**

```
None = 0
AsyncCompute = 2
```

---

#### CommandEvent

**Line:** 1555565

---

#### CommentHandling

**Line:** 1042942

**Values:**

```
Ignore = 0
Load = 1
```

---

#### CompareFunction

**Line:** 891799

**Values:**

```
Disabled = 0
Never = 1
Less = 2
Equal = 3
LessEqual = 4
Greater = 5
NotEqual = 6
GreaterEqual = 7
Always = 8
```

---

#### CompareOptions

**Line:** 271363

**Values:**

```
None = 0
IgnoreCase = 1
IgnoreNonSpace = 2
IgnoreSymbols = 4
IgnoreKanaType = 8
IgnoreWidth = 16
OrdinalIgnoreCase = 268435456
StringSort = 536870912
Ordinal = 1073741824
```

---

#### CompilationRelaxations

**Line:** 253428

**Values:**

```
NoStringInterning = 8
```

---

#### CompiledIdentityConstraint

**Line:** 756623

---

#### CompressionAlgorithm

**Line:** 500131

**Values:**

```
None = 0
Deflate = 1
LZ4 = 2
Zstandard = 3
```

---

#### CompressionMode

**Line:** 789385

**Values:**

```
Decompress = 0
Compress = 1
```

---

#### ComputeBufferMode

**Line:** 872861

**Values:**

```
Immutable = 0
Dynamic = 1
Circular = 2
StreamOut = 3
SubUpdates = 4
```

---

#### ComputeBufferType

**Line:** 875215

**Values:**

```
Default = 0
Raw = 1
Append = 2
Counter = 4
Constant = 8
Structured = 16
DrawIndirect = 256
IndirectArguments = 256
GPUMemory = 512
```

---

#### ComputeQueueType

**Line:** 892408

**Values:**

```
Default = 0
Background = 1
Urgent = 2
```

---

#### Compute_DistanceTransform_EventTypes

**Line:** 1220982

**Values:**

```
Processing = 0
Completed = 1
```

---

#### ConfidenceFactor

**Line:** 1450086

**Values:**

```
ExtraLow = 0
Low = 1
Medium = 2
High = 3
ExtraHigh = 4
Provable = 5
```

---

#### ConfigLexer

**Line:** 526053

---

#### ConfigurableMessageHandler

**Line:** 1496921

---

#### ConfigurationSaveMode

**Line:** 1597877

**Values:**

```
Full = 2
Minimal = 1
Modified = 0
```

---

#### Connecting

**Line:** 1309960

---

#### ConnectionInternalWatchdogType

**Line:** 550266

**Values:**

```
Transport = 0
Resetup = 1
```

---

#### ConnectionLostReason

**Line:** 1306212

**Values:**

```
CouldNotConnect = 0
NoInternetConnection = 1
ConnectionLost = 2
ServerMaintenance = 3
ClientVersionTooOld = 4
DeviceLocalStorageError = 5
PlayerIsBanned = 6
InternalError = 7
CredentialsExpiredOrInvalid = 8
```

---

#### ConnectionStatus

**Line:** 1306660

**Values:**

```
NotConnected = 0
Connecting = 1
Connected = 2
Error = 3
```

---

#### ConsentStatus

**Line:** 1572952

**Values:**

```
Granted = 0
Denied = 1
```

---

#### ConsentType

**Line:** 1572941

**Values:**

```
AdStorage = 0
AnalyticsStorage = 1
AdUserData = 2
AdPersonalization = 3
```

---

#### Consistency

**Line:** 229993

**Values:**

```
MayCorruptProcess = 0
MayCorruptAppDomain = 1
MayCorruptInstance = 2
WillNotCorruptState = 3
```

---

#### ConsoleAlignment

**Line:** 1442564

**Values:**

```
Top = 0
Bottom = 1
```

---

#### ConsoleColor

**Line:** 70927

**Values:**

```
Black = 0
DarkBlue = 1
DarkGreen = 2
DarkCyan = 3
DarkRed = 4
DarkMagenta = 5
DarkYellow = 6
Gray = 7
DarkGray = 8
Blue = 9
Green = 10
Cyan = 11
Red = 12
Magenta = 13
Yellow = 14
White = 15
```

---

#### ConsoleKey

**Line:** 70950

**Values:**

```
Backspace = 8
Tab = 9
Clear = 12
Enter = 13
Pause = 19
Escape = 27
Spacebar = 32
PageUp = 33
PageDown = 34
End = 35
Home = 36
LeftArrow = 37
UpArrow = 38
RightArrow = 39
DownArrow = 40
Select = 41
Print = 42
Execute = 43
PrintScreen = 44
Insert = 45
Delete = 46
Help = 47
D0 = 48
D1 = 49
D2 = 50
D3 = 51
D4 = 52
D5 = 53
D6 = 54
D7 = 55
D8 = 56
D9 = 57
A = 65
B = 66
C = 67
D = 68
E = 69
F = 70
G = 71
H = 72
I = 73
J = 74
K = 75
L = 76
M = 77
N = 78
O = 79
P = 80
Q = 81
R = 82
S = 83
T = 84
U = 85
V = 86
W = 87
X = 88
Y = 89
Z = 90
LeftWindows = 91
RightWindows = 92
Applications = 93
Sleep = 95
NumPad0 = 96
NumPad1 = 97
NumPad2 = 98
NumPad3 = 99
NumPad4 = 100
NumPad5 = 101
NumPad6 = 102
NumPad7 = 103
NumPad8 = 104
NumPad9 = 105
Multiply = 106
Add = 107
Separator = 108
Subtract = 109
Decimal = 110
Divide = 111
F1 = 112
F2 = 113
F3 = 114
F4 = 115
F5 = 116
F6 = 117
F7 = 118
F8 = 119
F9 = 120
F10 = 121
F11 = 122
F12 = 123
F13 = 124
F14 = 125
F15 = 126
F16 = 127
F17 = 128
F18 = 129
```

---

#### ConsoleModifiers

**Line:** 71137

**Values:**

```
Alt = 1
Shift = 2
Control = 4
```

---

#### ConsoleSpecialKey

**Line:** 71147

**Values:**

```
ControlC = 0
ControlBreak = 1
```

---

#### ConstructorHandling

**Line:** 1025842

**Values:**

```
Default = 0
AllowNonPublicDefaultConstructor = 1
```

---

#### ContentCatalogProvider

**Line:** 1456075

---

#### ContentSizeFitter

**Line:** 1354559

---

#### ContextType

**Line:** 641847

**Values:**

```
Player = 0
Editor = 1
```

---

#### ConversionError

**Line:** 1200808

**Values:**

```
None = 0
Overflow = 1
Encoding = 2
CodePoint = 3
```

---

#### CooldownTimerState

**Line:** 696296

**Values:**

```
Idle = 0
Active = 1
Cooldown = 2
```

---

#### CopyDepthMode

**Line:** 916194

**Values:**

```
AfterOpaques = 0
AfterTransparents = 1
ForcePrepass = 2
```

---

#### CopyError

**Line:** 1200799

**Values:**

```
None = 0
Truncation = 1
```

---

#### CopyTextureSupport

**Line:** 892395

**Values:**

```
None = 0
Basic = 1
Copy3D = 2
DifferentTypes = 4
TextureToRT = 8
RTToTexture = 16
```

---

#### Crc8

**Line:** 577514

---

#### CredentialState

**Line:** 1590219

**Values:**

```
Revoked = 0
Authorized = 1
NotFound = 2
Transferred = 3
```

---

#### CryptoStreamMode

**Line:** 217673

**Values:**

```
Read = 0
Write = 1
```

---

#### CspProviderFlags

**Line:** 218045

**Values:**

```
NoFlags = 0
UseMachineKeyStore = 1
UseDefaultKeyContainer = 2
UseNonExportableKey = 4
UseExistingKey = 8
UseArchivableKey = 16
UseUserProtectedKey = 32
NoPrompt = 64
CreateEphemeralKey = 128
```

---

#### CubemapFace

**Line:** 875540

**Values:**

```
PositiveX = 0
NegativeX = 1
PositiveY = 2
NegativeY = 3
PositiveZ = 4
NegativeZ = 5
```

---

#### CullMode

**Line:** 891816

**Values:**

```
Off = 0
Front = 1
Back = 2
```

---

#### CullingOptions

**Line:** 895256

**Values:**

```
None = 0
ForceEvenIfCameraIsNotActive = 1
OcclusionCull = 2
NeedsLighting = 4
NeedsReflectionProbes = 8
Stereo = 16
DisablePerObjectCulling = 32
ShadowCasters = 64
```

---

#### CultureTypes

**Line:** 271425

**Values:**

```
NeutralCultures = 1
SpecificCultures = 2
InstalledWin32Cultures = 4
AllCultures = 7
UserCustomCulture = 8
ReplacementCultures = 16
WindowsOnlyCultures = 32
FrameworkCultures = 64
```

---

#### CursorLockMode

**Line:** 878198

**Values:**

```
None = 0
Locked = 1
Confined = 2
```

---

#### CursorMode

**Line:** 878189

**Values:**

```
Auto = 0
ForceSoftware = 1
```

---

#### CustomErrorsModes

**Line:** 220886

**Values:**

```
On = 0
Off = 1
RemoteOnly = 2
```

---

#### DOTweenSettings

**Line:** 1431190

---

#### DailyDealType

**Line:** 1066945

**Values:**

```
Dungeon = 0
Resource = 1
Pet = 2
Skill = 3
Tech = 4
Mount = 5
```

---

#### DataRowAction

**Line:** 1084730

**Values:**

```
Nothing = 0
Delete = 1
Change = 2
Rollback = 4
Commit = 8
Add = 16
ChangeOriginal = 32
ChangeCurrentAndOriginal = 64
```

---

#### DataRowState

**Line:** 1084870

**Values:**

```
Detached = 1
Unchanged = 2
Added = 4
Deleted = 8
Modified = 16
```

---

#### DataRowVersion

**Line:** 1084882

**Values:**

```
Original = 256
Current = 512
Proposed = 1024
Default = 1536
```

---

#### DataSetDateTime

**Line:** 1085015

**Values:**

```
Local = 1
Unspecified = 2
UnspecifiedLocal = 3
Utc = 4
```

---

#### DataType

**Line:** 1508896

**Values:**

```
Custom = 0
DateTime = 1
Date = 2
Time = 3
Duration = 4
PhoneNumber = 5
Currency = 6
Text = 7
Html = 8
MultilineText = 9
EmailAddress = 10
Password = 11
Url = 12
ImageUrl = 13
CreditCard = 14
PostalCode = 15
Upload = 16
```

---

#### DataViewRowState

**Line:** 1085688

**Values:**

```
None = 0
Unchanged = 2
Added = 4
Deleted = 8
ModifiedCurrent = 16
ModifiedOriginal = 32
OriginalRows = 42
CurrentRows = 22
```

---

#### DatabaseGeneratedOption

**Line:** 1510895

**Values:**

```
None = 0
Identity = 1
Computed = 2
```

---

#### DateFormatHandling

**Line:** 1025851

**Values:**

```
IsoDateFormat = 0
MicrosoftDateFormat = 1
```

---

#### DateParseHandling

**Line:** 1025860

**Values:**

```
None = 0
DateTime = 1
DateTimeOffset = 2
```

---

#### DateTimeKind

**Line:** 22477

**Values:**

```
Unspecified = 0
Utc = 1
Local = 2
```

---

#### DateTimeStyles

**Line:** 272040

**Values:**

```
None = 0
AllowLeadingWhite = 1
AllowTrailingWhite = 2
AllowInnerWhite = 4
AllowWhiteSpaces = 7
NoCurrentDateDefault = 8
AdjustToUniversal = 16
AssumeLocal = 32
AssumeUniversal = 64
RoundtripKind = 128
```

---

#### DateTimeZoneHandling

**Line:** 1025870

**Values:**

```
Local = 0
Utc = 1
Unspecified = 2
RoundtripKind = 3
```

---

#### DayOfWeek

**Line:** 22710

**Values:**

```
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
```

---

#### DebugDisplaySettingsMaterial

**Line:** 901748

---

#### DebugDisplaySettingsRendering

**Line:** 902413

---

#### DebugFullScreenMode

**Line:** 1594294

**Values:**

```
None = 0
Depth = 1
MotionVector = 2
AdditionalLightsShadowMap = 3
MainLightShadowMap = 4
AdditionalLightsCookieAtlas = 5
ReflectionProbeAtlas = 6
STP = 7
```

---

#### DebugLightingFeatureFlags

**Line:** 1594442

**Values:**

```
None = 0
GlobalIllumination = 1
MainLight = 2
AdditionalLights = 4
VertexLighting = 8
Emission = 16
AmbientOcclusion = 32
```

---

#### DebugLightingMode

**Line:** 1594414

**Values:**

```
None = 0
ShadowCascades = 1
LightingWithoutNormalMaps = 2
LightingWithNormalMaps = 3
Reflections = 4
ReflectionsWithSmoothness = 5
GlobalIllumination = 6
```

---

#### DebugManager

**Line:** 812624

---

#### DebugMaterialMode

**Line:** 1594246

**Values:**

```
None = 0
Albedo = 1
Specular = 2
Alpha = 3
Smoothness = 4
AmbientOcclusion = 5
Emission = 6
NormalWorldSpace = 7
NormalTangentSpace = 8
LightingComplexity = 9
Metallic = 10
SpriteMask = 11
RenderingLayerMasks = 12
```

---

#### DebugMaterialValidationMode

**Line:** 1594283

**Values:**

```
None = 0
Albedo = 1
Metallic = 2
```

---

#### DebugMipInfoMode

**Line:** 1594335

**Values:**

```
None = 0
MipStreamingPerformance = 1
MipStreamingStatus = 2
MipStreamingActivity = 3
MipStreamingPriority = 4
MipCount = 5
MipRatio = 6
```

---

#### DebugMipMapModeTerrainTexture

**Line:** 1594360

**Values:**

```
Control = 0
Layer0 = 1
Layer1 = 2
Layer2 = 3
Layer3 = 4
```

---

#### DebugMipMapStatusMode

**Line:** 1594350

**Values:**

```
Material = 0
Texture = 1
```

---

#### DebugOverdrawMode

**Line:** 1594323

**Values:**

```
None = 0
Opaque = 1
Transparent = 2
All = 3
```

---

#### DebugPostProcessingMode

**Line:** 1594377

**Values:**

```
Disabled = 0
Auto = 1
Enabled = 2
```

---

#### DebugProbeShadingMode

**Line:** 818983

**Values:**

```
SH = 0
SHL0 = 1
SHL0L1 = 2
Validity = 3
ValidityOverDilationThreshold = 4
RenderingLayerMasks = 5
InvalidatedByAdjustmentVolumes = 6
Size = 7
SkyOcclusionSH = 8
SkyDirection = 9
ProbeOcclusion = 10
```

---

#### DebugSceneOverrideMode

**Line:** 1594311

**Values:**

```
None = 0
Overdraw = 1
Wireframe = 2
SolidWireframe = 3
ShadedWireframe = 4
```

---

#### DebugUI

**Line:** 814599

---

#### DebugValidationMode

**Line:** 1594388

**Values:**

```
None = 0
HighlightNanInfNegative = 1
HighlightOutsideOfRange = 2
```

---

#### DebugVertexAttributeMode

**Line:** 1594267

**Values:**

```
None = 0
Texcoord0 = 1
Texcoord1 = 2
Texcoord2 = 3
Texcoord3 = 4
Color = 5
Tangent = 6
Normal = 7
```

---

#### DebugWireframeMode

**Line:** 902402

**Values:**

```
None = 0
Wireframe = 1
SolidWireframe = 2
ShadedWireframe = 3
```

---

#### DebuggableAttribute

**Line:** 275226

---

#### DebuggerBrowsableState

**Line:** 275253

**Values:**

```
Never = 0
Collapsed = 2
RootHidden = 3
```

---

#### DecalScaleMode

**Line:** 904249

**Values:**

```
ScaleInvariant = 0
InheritFromHierarchy = 1
```

---

#### DecompressionMethods

**Line:** 794423

**Values:**

```
None = 0
GZip = 1
Deflate = 2
```

---

#### DefaultEventSystem

**Line:** 631530

---

#### DefaultFormat

**Line:** 899403

**Values:**

```
LDR = 0
HDR = 1
DepthStencil = 2
Shadow = 3
Video = 4
```

---

#### DefaultPlayerClientContext

**Line:** 576874

---

#### DefaultTabs

**Line:** 1442537

**Values:**

```
SystemInformation = 0
Options = 1
Console = 2
Profiler = 3
BugReporter = 4
```

---

#### DefaultValueHandling

**Line:** 1025932

**Values:**

```
Include = 0
Ignore = 1
Populate = 2
IgnoreAndPopulate = 3
```

---

#### DelayType

**Line:** 1120976

**Values:**

```
DeltaTime = 0
UnscaledDeltaTime = 1
Realtime = 2
```

---

#### DeltaSpeed

**Line:** 628654

**Values:**

```
Fast = 0
Normal = 1
Slow = 2
```

---

#### DependencyStatus

**Line:** 1491618

**Values:**

```
Available = 0
UnavailableDisabled = 1
UnavailableInvalid = 2
UnavilableMissing = 3
UnavailablePermission = 4
UnavailableUpdaterequired = 5
UnavailableUpdating = 6
UnavailableOther = 7
```

---

#### DepthAccess

**Line:** 829114

**Values:**

```
Read = 1
Write = 2
ReadWrite = 3
```

---

#### DepthBits

**Line:** 822159

**Values:**

```
None = 0
Depth8 = 8
Depth16 = 16
Depth24 = 24
Depth32 = 32
```

---

#### DepthFormat

**Line:** 916229

**Values:**

```
Default = 0
Depth_16 = 90
Depth_24 = 91
Depth_32 = 93
Depth_16_Stencil_8 = 151
Depth_24_Stencil_8 = 92
Depth_32_Stencil_8 = 94
```

---

#### DepthOfFieldMode

**Line:** 909312

**Values:**

```
Off = 0
Gaussian = 1
Bokeh = 2
```

---

#### DepthTextureMode

**Line:** 875324

**Values:**

```
None = 0
Depth = 1
DepthNormals = 2
MotionVectors = 4
```

---

#### DesignerSerializationVisibility

**Line:** 780730

**Values:**

```
Hidden = 0
Visible = 1
Content = 2
```

---

#### DeviceType

**Line:** 885052

**Values:**

```
Unknown = 0
Handheld = 1
Console = 2
Desktop = 3
```

---

#### Dimension

**Line:** 679357

---

#### DirectTransportProtocol

**Line:** 546254

---

#### DiscoveryVersion

**Line:** 1498151

**Values:**

```
Version_1_0 = 0
```

---

#### DisplayStyle

**Line:** 659968

**Values:**

```
Flex = 0
None = 1
```

---

#### DistanceMetric

**Line:** 897009

**Values:**

```
Perspective = 0
Orthographic = 1
CustomAxis = 2
```

---

#### DivisionSeasonPhase

**Line:** 563899

**Values:**

```
NoDivision = 0
Preview = 1
Ongoing = 2
Resolving = 3
Concluded = 4
```

---

#### DownloadStatus

**Line:** 1504390

**Values:**

```
NotStarted = 0
Downloading = 1
Completed = 2
Failed = 3
```

---

#### Downsampling

**Line:** 900510

**Values:**

```
None = 0
_2xBilinear = 1
_4xBox = 2
_4xBilinear = 3
```

---

#### DragVisualMode

**Line:** 632189

**Values:**

```
None = 0
Copy = 1
Move = 2
Rejected = 3
```

---

#### DrivenTransformProperties

**Line:** 885927

**Values:**

```
None = 0
AnchoredPositionX = 2
AnchoredPositionY = 4
AnchoredPositionZ = 8
Rotation = 16
ScaleX = 32
ScaleY = 64
ScaleZ = 128
AnchorMinX = 256
AnchorMinY = 512
AnchorMaxX = 1024
AnchorMaxY = 2048
SizeDeltaX = 4096
SizeDeltaY = 8192
PivotX = 16384
PivotY = 32768
AnchoredPosition = 6
AnchoredPosition3D = 14
Scale = 224
AnchorMin = 768
AnchorMax = 3072
Anchors = 3840
SizeDelta = 12288
Pivot = 49152
```

---

#### DtdProcessing

**Line:** 740784

**Values:**

```
Prohibit = 0
Ignore = 1
Parse = 2
```

---

#### DuplicatePropertyNameHandling

**Line:** 1042951

**Values:**

```
Replace = 0
Ignore = 1
Error = 2
```

---

#### DynamicAtlasFilters

**Line:** 606472

**Values:**

```
None = 0
Readability = 1
Size = 2
Format = 4
ColorSpace = 8
FilterMode = 16
```

---

#### DynamicResScalePolicyType

**Line:** 809601

**Values:**

```
ReturnsPercentage = 0
ReturnsMinMaxLerpFactor = 1
```

---

#### DynamicResScalerSlot

**Line:** 809610

**Values:**

```
User = 0
System = 1
Count = 2
```

---

#### DynamicResUpscaleFilter

**Line:** 809842

**Values:**

```
Bilinear = 0
CatmullRom = 1
Lanczos = 2
ContrastAdaptiveSharpen = 3
EdgeAdaptiveScalingUpres = 4
TAAU = 5
```

---

#### DynamicResolutionHandler

**Line:** 809628

---

#### DynamicResolutionType

**Line:** 809833

**Values:**

```
Software = 0
Hardware = 1
```

---

#### ECCurve

**Line:** 1230438

---

#### ETagAction

**Line:** 1501327

**Values:**

```
Default = 0
Ignore = 1
IfMatch = 2
IfNoneMatch = 3
```

---

#### Ease

**Line:** 1425465

**Values:**

```
Unset = 0
Linear = 1
InSine = 2
OutSine = 3
InOutSine = 4
InQuad = 5
OutQuad = 6
InOutQuad = 7
InCubic = 8
OutCubic = 9
InOutCubic = 10
InQuart = 11
OutQuart = 12
InOutQuart = 13
InQuint = 14
OutQuint = 15
InOutQuint = 16
InExpo = 17
OutExpo = 18
InOutExpo = 19
InCirc = 20
OutCirc = 21
InOutCirc = 22
InElastic = 23
OutElastic = 24
InOutElastic = 25
InBack = 26
OutBack = 27
InOutBack = 28
InBounce = 29
OutBounce = 30
InOutBounce = 31
Flash = 32
InFlash = 33
OutFlash = 34
InOutFlash = 35
INTERNAL_Zero = 36
INTERNAL_Custom = 37
```

---

#### EasingMode

**Line:** 645702

**Values:**

```
Ease = 0
EaseIn = 1
EaseOut = 2
EaseInOut = 3
Linear = 4
EaseInSine = 5
EaseOutSine = 6
EaseInOutSine = 7
EaseInCubic = 8
EaseOutCubic = 9
EaseInOutCubic = 10
EaseInCirc = 11
EaseOutCirc = 12
EaseInOutCirc = 13
EaseInElastic = 14
EaseOutElastic = 15
EaseInOutElastic = 16
EaseInBack = 17
EaseOutBack = 18
EaseInOutBack = 19
EaseInBounce = 20
EaseOutBounce = 21
EaseInOutBounce = 22
```

---

#### EditorBrowsableState

**Line:** 780546

**Values:**

```
Always = 0
Never = 1
Advanced = 2
```

---

#### EditorTextRenderingMode

**Line:** 660020

**Values:**

```
SDF = 0
Bitmap = 1
```

---

#### EncryptionPolicy

**Line:** 802768

**Values:**

```
RequireEncryption = 0
AllowNoEncryption = 1
NoEncryption = 2
```

---

#### EndType

**Line:** 1361513

**Values:**

```
etClosedPolygon = 0
etClosedLine = 1
```

---

#### EntityHandling

**Line:** 740794

**Values:**

```
ExpandEntities = 1
ExpandCharEntities = 2
```

---

#### EntityIndexType

**Line:** 1597445

**Values:**

```
EntityIndex = 0
PrimaryEntityIndex = 1
```

---

#### EntityTimelinePingTraceMarker

**Line:** 553646

---

#### EntryOverrideType

**Line:** 1327475

**Values:**

```
None = 0
Table = 1
Entry = 2
TableAndEntry = 3
```

---

#### EnumDataUtility

**Line:** 882658

---

#### Environment

**Line:** 174675

---

#### EnvironmentFamily

**Line:** 501409

**Values:**

```
Local = 0
Development = 1
Staging = 2
Production = 3
```

---

#### ErrorAction

**Line:** 1322378

**Values:**

```
ThrowError = 0
OutputErrorInResult = 1
Ignore = 2
MaintainTokens = 3
```

---

#### Event

**Line:** 1555654

---

#### EventActivityOptions

**Line:** 275495

**Values:**

```
None = 0
Disable = 2
Recursive = 4
Detachable = 8
```

---

#### EventAttributes

**Line:** 265285

**Values:**

```
None = 0
SpecialName = 512
RTSpecialName = 1024
ReservedMask = 1024
```

---

#### EventCommand

**Line:** 275633

**Values:**

```
Update = 0
```

---

#### EventHandle

**Line:** 1359586

**Values:**

```
Unused = 0
Used = 1
```

---

#### EventInterestOptions

**Line:** 671223

**Values:**

```
Inherit = 0
```

---

#### EventKeywords

**Line:** 275546

**Values:**

```
None = 0
MicrosoftTelemetry = 562949953421312
WdiContext = 562949953421312
WdiDiagnostic = 1125899906842624
Sqm = 2251799813685248
AuditFailure = 4503599627370496
AuditSuccess = 9007199254740992
CorrelationHint = 4503599627370496
EventLogClassic = 36028797018963968
```

---

#### EventModifiers

**Line:** 1555899

---

#### EventOpcode

**Line:** 275527

**Values:**

```
Info = 0
Start = 1
Stop = 2
DataCollectionStart = 3
DataCollectionStop = 4
Extension = 5
Reply = 6
Resume = 7
Suspend = 8
Send = 9
Receive = 240
```

---

#### EventResetMode

**Line:** 178933

**Values:**

```
AutoReset = 0
ManualReset = 1
```

---

#### EventSourceSettings

**Line:** 275811

**Values:**

```
Default = 0
ThrowOnEventWriteErrors = 1
EtwManifestEventFormat = 4
EtwSelfDescribingEventFormat = 8
```

---

#### EventTarget

**Line:** 1597479

**Values:**

```
Any = 0
Self = 1
```

---

#### EventTask

**Line:** 275519

**Values:**

```
None = 0
```

---

#### EventTriggerType

**Line:** 1360055

**Values:**

```
PointerEnter = 0
PointerExit = 1
PointerDown = 2
PointerUp = 3
PointerClick = 4
Drag = 5
Drop = 6
Scroll = 7
UpdateSelected = 8
Select = 9
Deselect = 10
Move = 11
InitializePotentialDrag = 12
BeginDrag = 13
EndDrag = 14
Submit = 15
Cancel = 16
```

---

#### EventType

**Line:** 1597488

**Values:**

```
Added = 0
Removed = 1
```

---

#### ExceptionHandlingClauseOptions

**Line:** 265375

**Values:**

```
Clause = 0
Filter = 1
Finally = 2
Fault = 4
```

---

#### ExchangeAlgorithmType

**Line:** 778425

**Values:**

```
None = 0
DiffieHellman = 43522
RsaKeyX = 41984
RsaSign = 9216
```

---

#### FSharpCoreReflectionProxy

**Line:** 1011875

---

#### FakePurchasing

**Line:** 1312077

---

#### FakeStoreUIMode

**Line:** 1406374

**Values:**

```
Default = 0
StandardUser = 1
DeveloperUser = 2
```

---

#### FallbackBehavior

**Line:** 1318480

**Values:**

```
UseProjectSettings = 0
DontUseFallback = 1
UseFallback = 2
```

---

#### FalloffType

**Line:** 898859

**Values:**

```
InverseSquared = 0
InverseSquaredNoRangeAttenuation = 1
Linear = 2
Legacy = 3
Undefined = 4
```

---

#### FastMemoryFlags

**Line:** 891725

**Values:**

```
None = 0
SpillTop = 1
SpillBottom = 2
```

---

#### Features

**Line:** 1498159

**Values:**

```
LegacyDataResponse = 0
```

---

#### FieldAttributes

**Line:** 265387

**Values:**

```
FieldAccessMask = 7
PrivateScope = 0
Private = 1
FamANDAssem = 2
Assembly = 3
Family = 4
FamORAssem = 5
Public = 6
Static = 16
InitOnly = 32
Literal = 64
NotSerialized = 128
SpecialName = 512
PinvokeImpl = 8192
RTSpecialName = 1024
HasFieldMarshal = 4096
HasDefault = 32768
HasFieldRVA = 256
ReservedMask = 38144
```

---

#### FieldPacking

**Line:** 821454

**Values:**

```
NoPacking = 0
R11G11B10 = 1
PackedFloat = 2
PackedUint = 3
```

---

#### FieldPrecision

**Line:** 821465

**Values:**

```
Half = 0
Real = 1
Default = 2
```

---

#### FileAccess

**Line:** 467752

**Values:**

```
Read = 1
Write = 2
ReadWrite = 3
```

---

#### FileAttributes

**Line:** 469854

**Values:**

```
ReadOnly = 1
Hidden = 2
System = 4
Directory = 16
Archive = 32
Device = 64
Normal = 128
Temporary = 256
SparseFile = 512
ReparsePoint = 1024
Compressed = 2048
Offline = 4096
NotContentIndexed = 8192
Encrypted = 16384
IntegrityStream = 32768
NoScrubData = 131072
```

---

#### FileHandleType

**Line:** 1570450

**Values:**

```
Auto = 0
Tcp = 1
Pipe = 2
```

---

#### FileMode

**Line:** 467809

**Values:**

```
CreateNew = 1
Create = 2
Open = 3
OpenOrCreate = 4
Truncate = 5
Append = 6
```

---

#### FileOptions

**Line:** 467873

**Values:**

```
None = 0
Asynchronous = 1073741824
RandomAccess = 268435456
DeleteOnClose = 67108864
SequentialScan = 134217728
Encrypted = 16384
```

---

#### FileReadType

**Line:** 837805

**Values:**

```
Sync = 0
Async = 1
```

---

#### FileShare

**Line:** 467888

**Values:**

```
None = 0
Read = 1
Write = 2
ReadWrite = 3
Delete = 4
Inheritable = 16
```

---

#### FileState

**Line:** 837583

**Values:**

```
Absent = 0
Exists = 1
```

---

#### FileSystemBuildSource

**Line:** 595519

---

#### FilmGrainLookup

**Line:** 909375

**Values:**

```
Thin1 = 0
Thin2 = 1
Medium1 = 2
Medium2 = 3
Medium3 = 4
Medium4 = 5
Medium5 = 6
Medium6 = 7
Large01 = 8
Large02 = 9
Custom = 10
```

---

#### FilterMode

**Line:** 875428

**Values:**

```
Point = 0
Bilinear = 1
Trilinear = 2
```

---

#### FindObjectsInactive

**Line:** 883919

**Values:**

```
Exclude = 0
Include = 1
```

---

#### FindObjectsSortMode

**Line:** 883910

**Values:**

```
None = 0
InstanceID = 1
```

---

#### FlexDirection

**Line:** 659871

**Values:**

```
Column = 0
ColumnReverse = 1
Row = 2
RowReverse = 3
```

---

#### FloatFormatHandling

**Line:** 1025943

**Values:**

```
String = 0
Symbol = 1
DefaultValue = 2
```

---

#### FloatMode

**Line:** 1329686

**Values:**

```
Default = 0
Strict = 1
Deterministic = 2
Fast = 3
```

---

#### FloatParseHandling

**Line:** 1025953

**Values:**

```
Double = 0
Decimal = 1
```

---

#### FloatPrecision

**Line:** 1329697

**Values:**

```
Standard = 0
High = 1
Medium = 2
Low = 3
```

---

#### FocusType

**Line:** 1451160

**Values:**

```
Native = 0
Keyboard = 1
Passive = 2
```

---

#### FontEngineError

**Line:** 1557580

**Values:**

```
Success = 0
Invalid_File_Path = 1
Invalid_File_Format = 2
Invalid_File_Structure = 3
Invalid_File = 4
Invalid_Table = 8
Invalid_Glyph_Index = 16
Invalid_Character_Code = 17
Invalid_Pixel_Size = 23
Invalid_Library = 33
Invalid_Face = 35
Invalid_Library_or_Face = 41
Atlas_Generation_Cancelled = 100
Invalid_SharedTextureData = 101
OpenTypeLayoutLookup_Mismatch = 116
```

---

#### FontFeatureLookupFlags

**Line:** 1557989

**Values:**

```
None = 0
IgnoreLigatures = 4
IgnoreSpacingAdjustments = 256
```

---

#### FontStyle

**Line:** 1580731

**Values:**

```
Normal = 0
Bold = 1
Italic = 2
BoldAndItalic = 3
```

---

#### FontStyles

**Line:** 1349324

**Values:**

```
Normal = 0
Bold = 1
Italic = 2
Underline = 4
LowerCase = 8
UpperCase = 16
SmallCaps = 32
Strikethrough = 64
Superscript = 128
Subscript = 256
Highlight = 512
```

---

#### FontWeight

**Line:** 1227124

**Values:**

```
Thin = 100
ExtraLight = 200
Light = 300
Regular = 400
Medium = 500
SemiBold = 600
Bold = 700
Heavy = 800
Black = 900
```

---

#### ForceMode2D

**Line:** 1578329

**Values:**

```
Force = 0
Impulse = 1
```

---

#### FormatError

**Line:** 1200778

**Values:**

```
None = 0
Overflow = 1
BadFormatSpecifier = 2
```

---

#### FormatSwizzle

**Line:** 892162

**Values:**

```
FormatSwizzleR = 0
FormatSwizzleG = 1
FormatSwizzleB = 2
FormatSwizzleA = 3
FormatSwizzle0 = 4
FormatSwizzle1 = 5
```

---

#### FormatUsage

**Line:** 899359

**Values:**

```
Sample = 0
Linear = 1
Sparse = 2
Render = 4
Blend = 5
GetPixels = 6
SetPixels = 7
SetPixels32 = 8
ReadPixels = 9
LoadStore = 10
MSAA2x = 11
MSAA4x = 12
MSAA8x = 13
StencilSampling = 16
```

---

#### FormatterAssemblyStyle

**Line:** 226394

**Values:**

```
Simple = 0
Full = 1
```

---

#### FormatterTypeStyle

**Line:** 226384

**Values:**

```
TypesWhenNeeded = 0
TypesAlways = 1
XsdString = 2
```

---

#### Formatting

**Line:** 1025962

**Values:**

```
None = 0
Indented = 1
```

---

#### FormattingHelpers

**Line:** 467056

---

#### FoveatedRenderingCaps

**Line:** 892430

**Values:**

```
None = 0
FoveationImage = 1
NonUniformRaster = 2
ModeChangeOnlyBeforeRenderTargetSet = 4
```

---

#### FoveatedRenderingMode

**Line:** 892441

**Values:**

```
Disabled = 0
Enabled = 1
```

---

#### FtpStatusCode

**Line:** 791471

**Values:**

```
Undefined = 0
RestartMarker = 110
ServiceTemporarilyNotAvailable = 120
DataAlreadyOpen = 125
OpeningData = 150
CommandOK = 200
CommandExtraneous = 202
DirectoryStatus = 212
FileStatus = 213
SystemType = 215
SendUserCommand = 220
ClosingControl = 221
ClosingData = 226
EnteringPassive = 227
LoggedInProceed = 230
ServerWantsSecureSession = 234
FileActionOK = 250
PathnameCreated = 257
SendPasswordCommand = 331
NeedLoginAccount = 332
FileCommandPending = 350
ServiceNotAvailable = 421
CantOpenData = 425
ConnectionClosed = 426
ActionNotTakenFileUnavailableOrBusy = 450
ActionAbortedLocalProcessingError = 451
ActionNotTakenInsufficientSpace = 452
CommandSyntaxError = 500
ArgumentSyntaxError = 501
CommandNotImplemented = 502
BadCommandSequence = 503
NotLoggedIn = 530
AccountNeeded = 532
ActionNotTakenFileUnavailable = 550
ActionAbortedUnknownPageType = 551
FileActionAborted = 552
ActionNotTakenFilenameNotAllowed = 553
```

---

#### FullScreenPassRendererFeature

**Line:** 912307

---

#### Function

**Line:** 770131

---

#### GCHandleType

**Line:** 228903

**Values:**

```
Weak = 0
WeakTrackResurrection = 1
Normal = 2
Pinned = 3
```

---

#### GPUResidentDrawerMode

**Line:** 1378040

**Values:**

```
Disabled = 0
InstancedDrawing = 1
```

---

#### GPUResidentDrawerResources

**Line:** 1377832

---

#### GameConfigDeduplicationOwnership

**Line:** 596202

**Values:**

```
None = 0
Baseline = 1
SinglePatch = 2
```

---

#### GameConfigSpreadsheetReader

**Line:** 599279

---

#### GenerateTestsForBurstCompatibilityAttribute

**Line:** 1184652

---

#### GenericParameterAttributes

**Line:** 265530

**Values:**

```
None = 0
VarianceMask = 3
Covariant = 1
Contravariant = 2
SpecialConstraintMask = 28
ReferenceTypeConstraint = 4
NotNullableValueTypeConstraint = 8
DefaultConstructorConstraint = 16
```

---

#### GizmoSubset

**Line:** 895735

**Values:**

```
PreImageEffects = 0
PostImageEffects = 1
```

---

#### GlyphClassDefinitionType

**Line:** 1557355

**Values:**

```
Undefined = 0
Base = 1
Ligature = 2
Mark = 3
Component = 4
```

---

#### GlyphLoadFlags

**Line:** 1557562

**Values:**

```
LOAD_DEFAULT = 0
LOAD_NO_SCALE = 1
LOAD_NO_HINTING = 2
LOAD_RENDER = 4
LOAD_NO_BITMAP = 8
LOAD_FORCE_AUTOHINT = 32
LOAD_MONOCHROME = 4096
LOAD_NO_AUTOHINT = 32768
LOAD_COLOR = 1048576
LOAD_COMPUTE_METRICS = 2097152
LOAD_BITMAP_METRICS_ONLY = 4194304
```

---

#### GlyphRenderMode

**Line:** 1557603

**Values:**

```
DEFAULT = 0
SMOOTH_HINTED = 4121
SMOOTH = 4117
COLOR_HINTED = 69656
COLOR = 69652
RASTER_HINTED = 4122
RASTER = 4118
SDF = 4134
SDF8 = 8230
SDF16 = 16422
SDF32 = 32806
SDFAA_HINTED = 4169
SDFAA = 4165
```

---

#### GooglePlayProrationMode

**Line:** 1403669

**Values:**

```
UnknownSubscriptionUpgradeDowngradePolicy = 0
ImmediateWithTimeProration = 1
ImmediateAndChargeProratedPrice = 2
ImmediateWithoutProration = 3
Deferred = 4
ImmediateAndChargeFullPrice = 5
```

---

#### GooglePlayReplacementMode

**Line:** 1403655

**Values:**

```
UnknownReplacementMode = 0
WithTimeProration = 1
ChargeProratedPrice = 2
WithoutProration = 3
ChargeFullPrice = 5
Deferred = 4
```

---

#### GooglePurchaseState

**Line:** 1545038

**Values:**

```
Purchased = 0
Cancelled = 1
Refunded = 2
Deferred = 4
```

---

#### GradientMode

**Line:** 878987

**Values:**

```
Blend = 0
Fixed = 1
PerceptualBlend = 2
```

---

#### GraphicRaycaster

**Line:** 1352869

---

#### GraphicsBuffer

**Line:** 874708

---

#### GraphicsDeviceType

**Line:** 891925

**Values:**

```
OpenGL2 = 0
Direct3D9 = 1
Direct3D11 = 2
PlayStation3 = 3
Null = 4
Xbox360 = 6
OpenGLES2 = 8
OpenGLES3 = 11
PlayStationVita = 12
PlayStation4 = 13
XboxOne = 14
PlayStationMobile = 15
Metal = 16
OpenGLCore = 17
Direct3D12 = 18
N3DS = 19
Vulkan = 21
Switch = 22
XboxOneD3D12 = 23
GameCoreXboxOne = 24
GameCoreXboxSeries = 25
PlayStation5 = 26
PlayStation5NGGC = 27
WebGPU = 28
Switch2 = 29
```

---

#### GraphicsFenceType

**Line:** 892522

**Values:**

```
AsyncQueueSynchronisation = 0
CPUSynchronisation = 1
```

---

#### GraphicsFormat

**Line:** 899415

**Values:**

```
None = 0
R8_SRGB = 1
R8G8_SRGB = 2
R8G8B8_SRGB = 3
R8G8B8A8_SRGB = 4
R8_UNorm = 5
R8G8_UNorm = 6
R8G8B8_UNorm = 7
R8G8B8A8_UNorm = 8
R8_SNorm = 9
R8G8_SNorm = 10
R8G8B8_SNorm = 11
R8G8B8A8_SNorm = 12
R8_UInt = 13
R8G8_UInt = 14
R8G8B8_UInt = 15
R8G8B8A8_UInt = 16
R8_SInt = 17
R8G8_SInt = 18
R8G8B8_SInt = 19
R8G8B8A8_SInt = 20
R16_UNorm = 21
R16G16_UNorm = 22
R16G16B16_UNorm = 23
R16G16B16A16_UNorm = 24
R16_SNorm = 25
R16G16_SNorm = 26
R16G16B16_SNorm = 27
R16G16B16A16_SNorm = 28
R16_UInt = 29
R16G16_UInt = 30
R16G16B16_UInt = 31
R16G16B16A16_UInt = 32
R16_SInt = 33
R16G16_SInt = 34
R16G16B16_SInt = 35
R16G16B16A16_SInt = 36
R32_UInt = 37
R32G32_UInt = 38
R32G32B32_UInt = 39
R32G32B32A32_UInt = 40
R32_SInt = 41
R32G32_SInt = 42
R32G32B32_SInt = 43
R32G32B32A32_SInt = 44
R16_SFloat = 45
R16G16_SFloat = 46
R16G16B16_SFloat = 47
R16G16B16A16_SFloat = 48
R32_SFloat = 49
R32G32_SFloat = 50
R32G32B32_SFloat = 51
R32G32B32A32_SFloat = 52
B8G8R8_SRGB = 56
B8G8R8A8_SRGB = 57
B8G8R8_UNorm = 58
B8G8R8A8_UNorm = 59
B8G8R8_SNorm = 60
B8G8R8A8_SNorm = 61
B8G8R8_UInt = 62
B8G8R8A8_UInt = 63
B8G8R8_SInt = 64
B8G8R8A8_SInt = 65
R4G4B4A4_UNormPack16 = 66
B4G4R4A4_UNormPack16 = 67
R5G6B5_UNormPack16 = 68
B5G6R5_UNormPack16 = 69
R5G5B5A1_UNormPack16 = 70
B5G5R5A1_UNormPack16 = 71
A1R5G5B5_UNormPack16 = 72
E5B9G9R9_UFloatPack32 = 73
B10G11R11_UFloatPack32 = 74
A2B10G10R10_UNormPack32 = 75
A2B10G10R10_UIntPack32 = 76
A2B10G10R10_SIntPack32 = 77
A2R10G10B10_UNormPack32 = 78
A2R10G10B10_UIntPack32 = 79
A2R10G10B10_SIntPack32 = 80
A2R10G10B10_XRSRGBPack32 = 81
A2R10G10B10_XRUNormPack32 = 82
R10G10B10_XRSRGBPack32 = 83
R10G10B10_XRUNormPack32 = 84
A10R10G10B10_XRSRGBPack32 = 85
A10R10G10B10_XRUNormPack32 = 86
D16_UNorm = 90
D24_UNorm = 91
D24_UNorm_S8_UInt = 92
D32_SFloat = 93
D32_SFloat_S8_UInt = 94
S8_UInt = 95
RGB_DXT1_SRGB = 96
RGBA_DXT1_SRGB = 96
```

---

#### GraphicsFormatUsage

**Line:** 899381

**Values:**

```
None = 0
Sample = 1
Linear = 2
Sparse = 4
Render = 16
Blend = 32
GetPixels = 64
SetPixels = 128
SetPixels32 = 256
ReadPixels = 512
LoadStore = 1024
MSAA2x = 2048
MSAA4x = 4096
MSAA8x = 8192
StencilSampling = 65536
```

---

#### GraphicsTier

**Line:** 891967

**Values:**

```
Tier1 = 0
Tier2 = 1
Tier3 = 2
```

---

#### GregorianCalendarTypes

**Line:** 273332

**Values:**

```
Localized = 1
USEnglish = 2
MiddleEastFrench = 9
Arabic = 10
TransliteratedEnglish = 11
TransliteratedFrench = 12
```

---

#### GridLayoutGroup

**Line:** 1354650

---

#### GroupAlertBehaviours

**Line:** 1552256

**Values:**

```
GroupAlertAll = 0
GroupAlertSummary = 1
GroupAlertChildren = 2
```

---

#### GroupEvent

**Line:** 1547292

**Values:**

```
Added = 0
Removed = 1
AddedOrRemoved = 2
```

---

#### GroupOperation

**Line:** 1441382

---

#### HDRACESPreset

**Line:** 909730

**Values:**

```
ACES1000Nits = 3
ACES2000Nits = 4
ACES4000Nits = 5
```

---

#### HDRColorBufferPrecision

**Line:** 900488

**Values:**

```
_32Bits = 0
_64Bits = 1
```

---

#### HDRColorspace

**Line:** 820422

**Values:**

```
Rec709 = 0
Rec2020 = 1
P3D65 = 2
```

---

#### HDRDebugMode

**Line:** 1594429

**Values:**

```
None = 0
GamutView = 1
GamutClip = 2
ValuesAbovePaperWhite = 3
```

---

#### HDRDisplaySupportFlags

**Line:** 875642

**Values:**

```
None = 0
Supported = 1
RuntimeSwitchable = 2
AutomaticTonemapping = 4
```

---

#### HDREncoding

**Line:** 820433

**Values:**

```
Linear = 3
PQ = 2
Gamma22 = 4
sRGB = 0
```

---

#### HDROutputUtils

**Line:** 825367

---

#### HDRRangeReduction

**Line:** 820408

**Values:**

```
None = 0
Reinhard = 1
BT2390 = 2
ACES1000Nits = 3
ACES2000Nits = 4
ACES4000Nits = 5
```

---

#### Handshake

**Line:** 555311

---

#### HapticFeedback

**Line:** 692887

**Values:**

```
Selection = 0
Success = 1
Warning = 2
Failure = 3
LightImpact = 4
MediumImpact = 5
HeavyImpact = 6
RigidImpact = 7
SoftImpact = 8
None = 9
```

---

#### HapticPatterns

**Line:** 1579852

---

#### HashAlgorithmType

**Line:** 778436

**Values:**

```
None = 0
Md5 = 32771
Sha1 = 32772
Sha256 = 32780
Sha384 = 32781
Sha512 = 32782
```

---

#### HeaderImageType

**Line:** 1565197

**Values:**

```
Undefined = 0
Extended = 1
Custom = 2
Hidden = 3
```

---

#### HebrewMonthNumbering

**Line:** 1166976

**Values:**

```
Civil = 1
Scriptural = 2
```

---

#### HelpBoxMessageType

**Line:** 617863

**Values:**

```
None = 0
Info = 1
Warning = 2
Error = 3
```

---

#### HexConverter

**Line:** 1519948

---

#### HideFlags

**Line:** 883894

**Values:**

```
None = 0
HideInHierarchy = 1
HideInInspector = 2
DontSaveInEditor = 4
NotEditable = 8
DontSaveInBuild = 16
DontUnloadUnusedAsset = 32
DontSave = 52
HideAndDontSave = 61
```

---

#### HierarchyNodeFlags

**Line:** 1562526

**Values:**

```
None = 0
Expanded = 1
Selected = 2
Cut = 4
Hidden = 8
```

---

#### HierarchyPropertyStorageType

**Line:** 1562644

**Values:**

```
Sparse = 0
Dense = 1
Blob = 2
Default = 1
```

---

#### HierarchySearchFilterOperator

**Line:** 1562656

**Values:**

```
Equal = 0
Contains = 1
Greater = 2
GreaterOrEqual = 3
Lesser = 4
LesserOrEqual = 5
NotEqual = 6
Not = 7
```

---

#### HorizontalAlignmentOptions

**Line:** 1227006

**Values:**

```
Left = 1
Center = 2
Right = 4
Justified = 8
Flush = 16
Geometry = 32
```

---

#### HorizontalWrapMode

**Line:** 1580966

**Values:**

```
Wrap = 0
Overflow = 1
```

---

#### HttpCompletionOption

**Line:** 1488381

**Values:**

```
ResponseContentRead = 0
ResponseHeadersRead = 1
```

---

#### HttpRequestHeader

**Line:** 791627

**Values:**

```
CacheControl = 0
Connection = 1
Date = 2
KeepAlive = 3
Pragma = 4
Trailer = 5
TransferEncoding = 6
Upgrade = 7
Via = 8
Warning = 9
Allow = 10
ContentLength = 11
ContentType = 12
ContentEncoding = 13
ContentLanguage = 14
ContentLocation = 15
ContentMd5 = 16
ContentRange = 17
Expires = 18
LastModified = 19
Accept = 20
AcceptCharset = 21
AcceptEncoding = 22
AcceptLanguage = 23
Authorization = 24
Cookie = 25
Expect = 26
From = 27
Host = 28
IfMatch = 29
IfModifiedSince = 30
IfNoneMatch = 31
IfRange = 32
IfUnmodifiedSince = 33
MaxForwards = 34
ProxyAuthorization = 35
Referer = 36
Range = 37
Te = 38
Translate = 39
UserAgent = 40
```

---

#### HttpStatusCode

**Line:** 790015

**Values:**

```
Continue = 100
SwitchingProtocols = 101
Processing = 102
EarlyHints = 103
OK = 200
Created = 201
Accepted = 202
NonAuthoritativeInformation = 203
NoContent = 204
ResetContent = 205
PartialContent = 206
MultiStatus = 207
AlreadyReported = 208
IMUsed = 226
MultipleChoices = 300
Ambiguous = 300
MovedPermanently = 301
Moved = 301
Found = 302
Redirect = 302
SeeOther = 303
RedirectMethod = 303
NotModified = 304
UseProxy = 305
Unused = 306
TemporaryRedirect = 307
RedirectKeepVerb = 307
PermanentRedirect = 308
BadRequest = 400
Unauthorized = 401
PaymentRequired = 402
Forbidden = 403
NotFound = 404
MethodNotAllowed = 405
NotAcceptable = 406
ProxyAuthenticationRequired = 407
RequestTimeout = 408
Conflict = 409
Gone = 410
LengthRequired = 411
PreconditionFailed = 412
RequestEntityTooLarge = 413
RequestUriTooLong = 414
UnsupportedMediaType = 415
RequestedRangeNotSatisfiable = 416
ExpectationFailed = 417
MisdirectedRequest = 421
UnprocessableEntity = 422
Locked = 423
FailedDependency = 424
UpgradeRequired = 426
PreconditionRequired = 428
TooManyRequests = 429
RequestHeaderFieldsTooLarge = 431
UnavailableForLegalReasons = 451
InternalServerError = 500
NotImplemented = 501
BadGateway = 502
ServiceUnavailable = 503
GatewayTimeout = 504
HttpVersionNotSupported = 505
VariantAlsoNegotiates = 506
InsufficientStorage = 507
LoopDetected = 508
NotExtended = 510
NetworkAuthenticationRequired = 511
```

---

#### HttpTransportType

**Line:** 1583108

**Values:**

```
None = 0
WebSockets = 1
ServerSentEvents = 2
LongPolling = 4
```

---

#### HttpVerb

**Line:** 684772

**Values:**

```
Get = 0
Post = 1
Put = 2
Delete = 3
```

---

#### HubConnectionState

**Line:** 1415706

**Values:**

```
Disconnected = 0
Connected = 1
Connecting = 2
Reconnecting = 3
```

---

#### IAPFakeStoreConfig

**Line:** 1312544

---

#### IAPFlowTracker

**Line:** 1312602

---

#### IAPReceiptExtraction

**Line:** 1313526

---

#### IMECompositionMode

**Line:** 1580259

**Values:**

```
Auto = 0
On = 1
Off = 2
```

---

#### IOControlCode

**Line:** 800323

**Values:**

```
AsyncIO = 2147772029
NonBlockingIO = 2147772030
DataToRead = 1074030207
OobDataRead = 1074033415
AssociateHandle = 2281701377
EnableCircularQueuing = 671088642
Flush = 671088644
GetBroadcastAddress = 1207959557
GetExtensionFunctionPointer = 3355443206
GetQos = 3355443207
GetGroupQos = 3355443208
MultipointLoopback = 2281701385
MulticastScope = 2281701386
SetQos = 2281701387
SetGroupQos = 2281701388
TranslateHandle = 3355443213
RoutingInterfaceQuery = 3355443220
RoutingInterfaceChange = 2281701397
AddressListQuery = 1207959574
AddressListChange = 671088663
QueryTargetPnpHandle = 1207959576
NamespaceChange = 2281701401
AddressListSort = 3355443225
ReceiveAll = 2550136833
ReceiveAllMulticast = 2550136834
ReceiveAllIgmpMulticast = 2550136835
KeepAliveValues = 2550136836
AbsorbRouterAlert = 2550136837
UnicastInterface = 2550136838
LimitBroadcasts = 2550136839
BindToInterface = 2550136840
MulticastInterface = 2550136841
AddMulticastGroupOnInterface = 2550136842
DeleteMulticastGroupFromInterface = 2550136843
```

---

#### IOWriter

**Line:** 566848

---

#### Image

**Line:** 1353095

---

#### ImagePosition

**Line:** 1452092

**Values:**

```
ImageLeft = 0
ImageAbove = 1
ImageOnly = 2
TextOnly = 3
```

---

#### ImpactSfx

**Line:** 705764

**Values:**

```
None = 0
Metal = 1
Rock = 2
Explosion = 3
LightStab = 4
HeavyStab = 5
Glass = 7
```

---

#### ImplicitUseKindFlags

**Line:** 869290

**Values:**

```
Default = 7
Access = 1
Assign = 2
InstantiatedWithFixedConstructorSignature = 4
InstantiatedNoFixedConstructorSignature = 8
```

---

#### ImplicitUseTargetFlags

**Line:** 869303

**Values:**

```
Default = 1
Itself = 1
Members = 2
WithMembers = 3
```

---

#### Importance

**Line:** 1553122

**Values:**

```
None = 0
Low = 2
Default = 3
High = 4
```

---

#### InAppProductType

**Line:** 584115

**Values:**

```
Consumable = 0
NonConsumable = 1
Subscription = 2
```

---

#### InAppPurchaseClientRefuseReason

**Line:** 584539

**Values:**

```
Unknown = 0
CompletionActionFailed = 1
UnityUserCancelled = 2
UnityPurchasingUnavailable = 3
UnityExistingPurchasePending = 4
UnityProductUnavailable = 5
UnitySignatureInvalid = 6
UnityPaymentDeclined = 7
UnityDuplicateTransaction = 8
```

---

#### InAppPurchaseFlowKind

**Line:** 584393

**Values:**

```
ClientDriven = 0
ServerDriven = 1
```

---

#### InAppPurchasePaymentType

**Line:** 584556

**Values:**

```
Normal = 0
Sandbox = 1
```

---

#### InAppPurchaseStatus

**Line:** 584403

**Values:**

```
PendingValidation = 0
Successful = 1
Failed = 2
ReceiptAlreadyUsed = 3
_Reserved_4 = 4
_Reserved_5 = 5
_Reserved_6 = 6
Refunded = 7
MissingContent = 8
UserDeclined = 9
Abandoned = 10
```

---

#### IndexFormat

**Line:** 891630

**Values:**

```
UInt16 = 0
UInt32 = 1
```

---

#### IndirectBufferContext

**Line:** 1381322

---

#### InitResult

**Line:** 1492788

**Values:**

```
Success = 0
FailedMissingDependency = 1
```

---

#### InitializationFailureReason

**Line:** 1530606

**Values:**

```
PurchasingUnavailable = 0
NoProductsAvailable = 1
AppNotKnown = 2
```

---

#### InjectPlayerLoopTimings

**Line:** 1099320

**Values:**

```
All = 65535
Standard = 30037
Minimum = 8464
Initialization = 1
LastInitialization = 2
EarlyUpdate = 4
LastEarlyUpdate = 8
FixedUpdate = 16
LastFixedUpdate = 32
PreUpdate = 64
LastPreUpdate = 128
Update = 256
LastUpdate = 512
PreLateUpdate = 1024
LastPreLateUpdate = 2048
PostLateUpdate = 4096
LastPostLateUpdate = 8192
TimeUpdate = 16384
LastTimeUpdate = 32768
```

---

#### InputField

**Line:** 1353472

---

#### InspectorSort

**Line:** 883133

**Values:**

```
ByName = 0
ByValue = 1
```

---

#### InspectorSortDirection

**Line:** 883142

**Values:**

```
Ascending = 0
Descending = 1
```

---

#### InstantiationKind

**Line:** 1477856

**Values:**

```
Activator = 0
PropertyBagOverride = 1
NotInstantiatable = 2
```

---

#### IntermediateTextureMode

**Line:** 908224

**Values:**

```
Auto = 0
Always = 1
```

---

#### IslamicEpoch

**Line:** 1167096

**Values:**

```
Astronomical = 1
Civil = 2
```

---

#### IslamicLeapYearPattern

**Line:** 1167105

**Values:**

```
Base15 = 1
Base16 = 2
Indian = 3
HabashAlHasib = 4
```

---

#### IsoDayOfWeek

**Line:** 1144355

**Values:**

```
None = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
```

---

#### ItemType

**Line:** 1067865

**Values:**

```
Helmet = 0
Armour = 1
Gloves = 2
Necklace = 3
Ring = 4
Weapon = 5
Shoes = 6
Belt = 7
```

---

#### JTokenType

**Line:** 1046705

**Values:**

```
None = 0
Object = 1
Array = 2
Constructor = 3
Property = 4
Comment = 5
Integer = 6
Float = 7
String = 8
Boolean = 9
Null = 10
Undefined = 11
Date = 12
Raw = 13
Bytes = 14
Guid = 15
Uri = 16
TimeSpan = 17
```

---

#### JoinType

**Line:** 1361504

**Values:**

```
jtRound = 0
```

---

#### JsonCommentHandling

**Line:** 991902

**Values:**

```
Disallow = 0
Skip = 1
Allow = 2
```

---

#### JsonIgnoreCondition

**Line:** 1003212

**Values:**

```
Never = 0
Always = 1
WhenWritingDefault = 2
WhenWritingNull = 3
```

---

#### JsonKnownNamingPolicy

**Line:** 1003223

**Values:**

```
Unspecified = 0
CamelCase = 1
SnakeCaseLower = 2
SnakeCaseUpper = 3
KebabCaseLower = 4
KebabCaseUpper = 5
```

---

#### JsonNumberHandling

**Line:** 1003237

**Values:**

```
Strict = 0
AllowReadingFromString = 1
WriteAsString = 2
AllowNamedFloatingPointLiterals = 4
```

---

#### JsonObjectCreationHandling

**Line:** 1003248

**Values:**

```
Replace = 0
Populate = 1
```

---

#### JsonSchemaType

**Line:** 1042816

**Values:**

```
None = 0
String = 1
Float = 2
Integer = 4
Boolean = 8
Object = 16
Array = 32
Null = 64
Any = 127
```

---

#### JsonSerializationMode

**Line:** 582798

**Values:**

```
Default = 0
GdprExport = 1
AnalyticsEvents = 2
AdminApi = 3
```

---

#### JsonSerializerDefaults

**Line:** 992346

**Values:**

```
General = 0
Web = 1
```

---

#### JsonSerializerTrackedObject

**Line:** 1329076

---

#### JsonSourceGenerationMode

**Line:** 1003306

**Values:**

```
Default = 0
Metadata = 1
Serialization = 2
```

---

#### JsonToken

**Line:** 1030954

**Values:**

```
None = 0
StartObject = 1
StartArray = 2
StartConstructor = 3
PropertyName = 4
Comment = 5
Raw = 6
Integer = 7
Float = 8
String = 9
Boolean = 10
Null = 11
Undefined = 12
EndObject = 13
EndArray = 14
EndConstructor = 15
Date = 16
Bytes = 17
```

---

#### JsonTokenType

**Line:** 993577

**Values:**

```
None = 0
StartObject = 1
EndObject = 2
StartArray = 3
EndArray = 4
PropertyName = 5
Comment = 6
String = 7
Number = 8
True = 9
False = 10
Null = 11
```

---

#### JsonTypeInfoKind

**Line:** 1011784

**Values:**

```
None = 0
Object = 1
Enumerable = 2
Dictionary = 3
```

---

#### JsonUnknownDerivedTypeHandling

**Line:** 1004049

**Values:**

```
FailSerialization = 0
FallBackToBaseType = 1
FallBackToNearestAncestor = 2
```

---

#### JsonUnknownTypeHandling

**Line:** 1003611

**Values:**

```
JsonElement = 0
JsonNode = 1
```

---

#### JsonValueKind

**Line:** 993416

**Values:**

```
Undefined = 0
Object = 1
Array = 2
String = 3
Number = 4
True = 5
False = 6
Null = 7
```

---

#### Justify

**Line:** 659904

**Values:**

```
FlexStart = 0
Center = 1
FlexEnd = 2
SpaceBetween = 3
SpaceAround = 4
SpaceEvenly = 5
```

---

#### KeyCode

**Line:** 878237

**Values:**

```
None = 0
Backspace = 8
Delete = 127
Tab = 9
Clear = 12
Return = 13
Pause = 19
Escape = 27
Space = 32
Keypad0 = 256
Keypad1 = 257
Keypad2 = 258
Keypad3 = 259
Keypad4 = 260
Keypad5 = 261
Keypad6 = 262
Keypad7 = 263
Keypad8 = 264
Keypad9 = 265
KeypadPeriod = 266
KeypadDivide = 267
KeypadMultiply = 268
KeypadMinus = 269
KeypadPlus = 270
KeypadEnter = 271
KeypadEquals = 272
UpArrow = 273
DownArrow = 274
RightArrow = 275
LeftArrow = 276
Insert = 277
Home = 278
End = 279
PageUp = 280
PageDown = 281
F1 = 282
F2 = 283
F3 = 284
F4 = 285
F5 = 286
F6 = 287
F7 = 288
F8 = 289
F9 = 290
F10 = 291
F11 = 292
F12 = 293
F13 = 294
F14 = 295
F15 = 296
Alpha0 = 48
Alpha1 = 49
Alpha2 = 50
Alpha3 = 51
Alpha4 = 52
Alpha5 = 53
Alpha6 = 54
Alpha7 = 55
Alpha8 = 56
Alpha9 = 57
Exclaim = 33
DoubleQuote = 34
Hash = 35
Dollar = 36
Percent = 37
Ampersand = 38
Quote = 39
LeftParen = 40
RightParen = 41
Asterisk = 42
Plus = 43
Comma = 44
Minus = 45
Period = 46
Slash = 47
Colon = 58
Semicolon = 59
Less = 60
Equals = 61
Greater = 62
Question = 63
At = 64
LeftBracket = 91
Backslash = 92
RightBracket = 93
Caret = 94
Underscore = 95
BackQuote = 96
A = 97
B = 98
C = 99
D = 100
E = 101
F = 102
G = 103
H = 104
```

---

#### KeyEvent

**Line:** 1556064

---

#### KeyboardNavigationOperation

**Line:** 641267

**Values:**

```
None = 0
SelectAll = 1
Cancel = 2
Submit = 3
Previous = 4
Next = 5
MoveRight = 6
MoveLeft = 7
PageUp = 8
PageDown = 9
Begin = 10
End = 11
```

---

#### KnownColor

**Line:** 1548958

**Values:**

```
ActiveBorder = 1
ActiveCaption = 2
ActiveCaptionText = 3
AppWorkspace = 4
Control = 5
ControlDark = 6
ControlDarkDark = 7
ControlLight = 8
ControlLightLight = 9
ControlText = 10
Desktop = 11
GrayText = 12
Highlight = 13
HighlightText = 14
HotTrack = 15
InactiveBorder = 16
InactiveCaption = 17
InactiveCaptionText = 18
Info = 19
InfoText = 20
Menu = 21
MenuText = 22
ScrollBar = 23
Window = 24
WindowFrame = 25
WindowText = 26
Transparent = 27
AliceBlue = 28
AntiqueWhite = 29
Aqua = 30
Aquamarine = 31
Azure = 32
Beige = 33
Bisque = 34
Black = 35
BlanchedAlmond = 36
Blue = 37
BlueViolet = 38
Brown = 39
BurlyWood = 40
CadetBlue = 41
Chartreuse = 42
Chocolate = 43
Coral = 44
CornflowerBlue = 45
Cornsilk = 46
Crimson = 47
Cyan = 48
DarkBlue = 49
DarkCyan = 50
DarkGoldenrod = 51
DarkGray = 52
DarkGreen = 53
DarkKhaki = 54
DarkMagenta = 55
DarkOliveGreen = 56
DarkOrange = 57
DarkOrchid = 58
DarkRed = 59
DarkSalmon = 60
DarkSeaGreen = 61
DarkSlateBlue = 62
DarkSlateGray = 63
DarkTurquoise = 64
DarkViolet = 65
DeepPink = 66
DeepSkyBlue = 67
DimGray = 68
DodgerBlue = 69
Firebrick = 70
FloralWhite = 71
ForestGreen = 72
Fuchsia = 73
Gainsboro = 74
GhostWhite = 75
Gold = 76
Goldenrod = 77
Gray = 78
Green = 79
GreenYellow = 80
Honeydew = 81
HotPink = 82
IndianRed = 83
Indigo = 84
Ivory = 85
Khaki = 86
Lavender = 87
LavenderBlush = 88
LawnGreen = 89
LemonChiffon = 90
LightBlue = 91
LightCoral = 92
LightCyan = 93
LightGoldenrodYellow = 94
LightGray = 95
LightGreen = 96
```

---

#### LODCrossFadeDitheringType

**Line:** 900603

**Values:**

```
BayerMatrix = 0
BlueNoise = 1
```

---

#### LODFadeMode

**Line:** 875695

**Values:**

```
None = 0
CrossFade = 1
SpeedTree = 2
```

---

#### Language

**Line:** 1564125

**Values:**

```
Arabic = 0
Catalan = 1
ChineseHongKong = 2
ChineseSimplified = 3
ChineseTraditional = 4
Croatian = 5
Czech = 6
Danish = 7
Dutch = 8
EnglishAustralia = 9
EnglishIndia = 10
EnglishUnitedKingdom = 11
Finnish = 12
French = 13
FrenchCanada = 14
German = 15
Greek = 16
Hebrew = 17
Hindi = 18
Hungarian = 19
Indonesian = 20
Italian = 21
Japanese = 22
Korean = 23
Malay = 24
NorwegianBokmal = 25
Polish = 26
PortuguesePortugal = 27
PortugueseBrazil = 28
Romanian = 29
Russian = 30
Slovak = 31
Spanish = 32
SpanishLatinAmerica = 33
Swedish = 34
Thai = 35
Turkish = 36
Ukrainian = 37
Vietnamese = 38
Other = 39
```

---

#### LanguageDirection

**Line:** 670866

**Values:**

```
Inherit = 0
LTR = 1
RTL = 2
```

---

#### LanguageSelectionSource

**Line:** 533379

**Values:**

```
AccountCreationAutomatic = 0
ServerSideAutomatic = 1
UserDeviceAutomatic = 2
UserSelected = 3
```

---

#### LazyThreadSafetyMode

**Line:** 179021

**Values:**

```
None = 0
PublicationOnly = 1
ExecutionAndPublication = 2
```

---

#### LeaseState

**Line:** 222271

**Values:**

```
Null = 0
Initial = 1
Active = 2
Renewing = 3
Expired = 4
```

---

#### LegalLinksSettings

**Line:** 1564359

**Values:**

```
Undefined = 0
FirstLayerOnly = 1
SecondLayerOnly = 2
Both = 3
Hidden = 4
```

---

#### LengthUnit

**Line:** 656388

**Values:**

```
Pixel = 0
Percent = 1
```

---

#### LibraryVisibility

**Line:** 669283

**Values:**

```
Default = 0
Visible = 1
Hidden = 2
```

---

#### Light2D

**Line:** 1362363

---

#### LightAnchor

**Line:** 803492

---

#### LightCookieFormat

**Line:** 900476

**Values:**

```
GrayscaleLow = 0
GrayscaleHigh = 1
ColorLow = 2
ColorHigh = 3
ColorHDR = 4
```

---

#### LightCookieResolution

**Line:** 900464

**Values:**

```
_256 = 256
_512 = 512
_1024 = 1024
_2048 = 2048
_4096 = 4096
```

---

#### LightLayerEnum

**Line:** 915352

**Values:**

```
Nothing = 0
LightLayerDefault = 1
LightLayer1 = 2
LightLayer2 = 4
LightLayer3 = 8
LightLayer4 = 16
LightLayer5 = 32
LightLayer6 = 64
LightLayer7 = 128
Everything = 255
```

---

#### LightMode

**Line:** 898848

**Values:**

```
Realtime = 0
Mixed = 1
Baked = 2
Unknown = 3
```

---

#### LightProbeSystem

**Line:** 900612

**Values:**

```
LegacyLightProbes = 0
ProbeVolumes = 1
```

---

#### LightProbeUsage

**Line:** 892319

**Values:**

```
Off = 0
BlendProbes = 1
UseProxyVolume = 2
CustomProvided = 4
```

---

#### LightRenderingMode

**Line:** 900521

**Values:**

```
Disabled = 0
PerVertex = 2
PerPixel = 1
```

---

#### LightShadowResolution

**Line:** 891899

**Values:**

```
Low = 0
Medium = 1
High = 2
VeryHigh = 3
```

---

#### LightShadows

**Line:** 875261

**Values:**

```
None = 0
Hard = 1
Soft = 2
```

---

#### LightShape

**Line:** 875251

**Values:**

```
Cone = 0
Pyramid = 1
Box = 2
```

---

#### LightType

**Line:** 898834

**Values:**

```
Directional = 0
Point = 1
Spot = 2
Rectangle = 3
Disc = 4
SpotPyramidShape = 5
SpotBoxShape = 6
```

---

#### LightUnit

**Line:** 891912

**Values:**

```
Lumen = 0
Candela = 1
Lux = 2
Nits = 3
Ev100 = 4
```

---

#### LightmapBakeType

**Line:** 875272

**Values:**

```
Realtime = 4
Baked = 2
Mixed = 1
```

---

#### LightmapsMode

**Line:** 875654

**Values:**

```
NonDirectional = 0
CombinedDirectional = 1
```

---

#### LineInfoHandling

**Line:** 1047126

**Values:**

```
Ignore = 0
Load = 1
```

---

#### LinkBehaviour

**Line:** 1425554

**Values:**

```
PauseOnDisable = 0
PauseOnDisablePlayOnEnable = 1
PauseOnDisableRestartOnEnable = 2
PlayOnEnable = 3
RestartOnEnable = 4
KillOnDisable = 5
KillOnDestroy = 6
CompleteOnDisable = 7
CompleteAndKillOnDisable = 8
RewindOnDisable = 9
RewindAndKillOnDisable = 10
```

---

#### ListChangedType

**Line:** 782365

**Values:**

```
Reset = 0
ItemAdded = 1
ItemDeleted = 2
ItemMoved = 3
ItemChanged = 4
PropertyDescriptorAdded = 5
PropertyDescriptorDeleted = 6
PropertyDescriptorChanged = 7
```

---

#### ListSortDirection

**Line:** 782380

**Values:**

```
Ascending = 0
Descending = 1
```

---

#### ListViewReorderMode

**Line:** 613252

**Values:**

```
Simple = 0
Animated = 1
```

---

#### LoadHint

**Line:** 253386

**Values:**

```
Default = 0
Always = 1
Sometimes = 2
```

---

#### LoadOptions

**Line:** 1561030

**Values:**

```
None = 0
PreserveWhitespace = 1
SetBaseUri = 2
SetLineInfo = 4
```

---

#### LoadSceneMode

**Line:** 888931

**Values:**

```
Single = 0
Additive = 1
```

---

#### LocalPhysicsMode

**Line:** 888941

**Values:**

```
None = 0
Physics2D = 1
Physics3D = 2
```

---

#### LocalServerCodeReceiver

**Line:** 1372424

---

#### LockRecursionPolicy

**Line:** 1304460

**Values:**

```
NoRecursion = 0
SupportsRecursion = 1
```

---

#### LockScreenVisibility

**Line:** 1553133

**Values:**

```
Private = 0
Public = 1
```

---

#### LogBehaviour

**Line:** 1428385

**Values:**

```
Default = 0
Verbose = 1
ErrorsOnly = 2
```

---

#### LogOption

**Line:** 870565

**Values:**

```
None = 0
NoStacktrace = 1
```

---

#### LogType

**Line:** 870553

**Values:**

```
Error = 0
Assert = 1
Warning = 2
Log = 3
Exception = 4
```

---

#### LoginMethod

**Line:** 733857

**Values:**

```
Editor = 0
Google = 1
Apple = 2
Facebook = 3
Email = 4
```

---

#### LoginOptions

**Line:** 1590231

**Values:**

```
None = 0
IncludeFullName = 1
IncludeEmail = 2
```

---

#### LoopType

**Line:** 1425782

**Values:**

```
Restart = 0
Yoyo = 1
Incremental = 2
```

---

#### MSAASamples

**Line:** 822171

**Values:**

```
None = 1
MSAA2x = 2
MSAA4x = 4
MSAA8x = 8
```

---

#### MainScreenType

**Line:** 721594

**Values:**

```
SkillTab = 1
DungeonTab = 2
ShopTab = 3
ArenaTab = 4
GuildTab = 5
```

---

#### MaintenanceModeState

**Line:** 1308186

---

#### MappingType

**Line:** 1086984

**Values:**

```
Element = 1
Attribute = 2
SimpleContent = 3
Hidden = 4
```

---

#### MarkerFlags

**Line:** 837340

**Values:**

```
Default = 0
Script = 2
ScriptInvoke = 32
ScriptDeepProfiler = 64
AvailabilityEditor = 4
AvailabilityNonDevelopment = 8
Warning = 16
Counter = 128
SampleGPU = 256
```

---

#### MaskingOffsetMode

**Line:** 1227085

**Values:**

```
Percentage = 0
Pixel = 1
```

---

#### MaskingTypes

**Line:** 1227050

**Values:**

```
MaskOff = 0
MaskHard = 1
MaskSoft = 2
```

---

#### MatchCasing

**Line:** 469815

**Values:**

```
PlatformDefault = 0
CaseSensitive = 1
CaseInsensitive = 2
```

---

#### MatchType

**Line:** 469825

**Values:**

```
Simple = 0
Win32 = 1
```

---

#### MaterialQuality

**Line:** 825538

**Values:**

```
Low = 1
Medium = 2
High = 4
```

---

#### MergeArrayHandling

**Line:** 1047135

**Values:**

```
Concat = 0
Union = 1
Replace = 2
Merge = 3
```

---

#### MergeNullValueHandling

**Line:** 1047147

**Values:**

```
Ignore = 0
Merge = 1
```

---

#### MeshTopology

**Line:** 875335

**Values:**

```
Triangles = 0
Quads = 2
Lines = 3
LineStrip = 4
Points = 5
```

---

#### MeshUpdateFlags

**Line:** 891640

**Values:**

```
Default = 0
DontValidateIndices = 1
DontResetBoneBounds = 2
DontNotifyMeshUsers = 4
DontRecalculateBounds = 8
```

---

#### MessageDirection

**Line:** 498969

**Values:**

```
Bidirectional = 0
ClientToServer = 1
ServerToClient = 2
ServerInternal = 3
ClientInternal = 4
```

---

#### MetaActivableState

**Line:** 581303

---

#### MetaDeserializationConverter

**Line:** 529095

---

#### MetaDuration

**Line:** 519454

---

#### MetaScheduleTimeMode

**Line:** 532686

**Values:**

```
Utc = 0
Local = 1
```

---

#### MetaSerializableFlags

**Line:** 600717

**Values:**

```
None = 0
ImplicitMembers = 1
AutomaticConstructorDetection = 2
```

---

#### MetaSerializationFlags

**Line:** 529385

**Values:**

```
IncludeAll = 0
SendOverNetwork = 1
ComputeChecksum = 2
Persisted = 4
EntityEventLog = 16
```

---

#### MetadataPropertyHandling

**Line:** 1032308

**Values:**

```
Default = 0
ReadAhead = 1
Ignore = 2
```

---

#### MetadataType

**Line:** 1327147

**Values:**

```
Locale = 1
SharedTableData = 2
StringTable = 4
AssetTable = 8
StringTableEntry = 16
AssetTableEntry = 32
SharedStringTableEntry = 64
SharedAssetTableEntry = 128
LocalizationSettings = 256
AllTables = 12
AllTableEntries = 48
AllSharedTableEntries = 192
All = 511
```

---

#### MetaplayAppLifecycleListener

**Line:** 1306322

---

#### MetaplayFeatureEnabledConditionAttributeUtil

**Line:** 499101

---

#### MethodAttributes

**Line:** 265733

**Values:**

```
MemberAccessMask = 7
PrivateScope = 0
Private = 1
FamANDAssem = 2
Assembly = 3
Family = 4
FamORAssem = 5
Public = 6
Static = 16
Final = 32
Virtual = 64
HideBySig = 128
CheckAccessOnOverride = 512
VtableLayoutMask = 256
ReuseSlot = 0
NewSlot = 256
Abstract = 1024
SpecialName = 2048
PinvokeImpl = 8192
UnmanagedExport = 8
RTSpecialName = 4096
HasSecurity = 16384
RequireSecObject = 32768
ReservedMask = 53248
```

---

#### MethodImplAttributes

**Line:** 265898

**Values:**

```
CodeTypeMask = 3
IL = 0
Native = 1
OPTIL = 2
Runtime = 3
ManagedMask = 4
Unmanaged = 4
Managed = 0
ForwardRef = 16
PreserveSig = 128
InternalCall = 4096
Synchronized = 32
NoInlining = 8
AggressiveInlining = 256
NoOptimization = 64
MaxMethodImplVal = 65535
SecurityMitigations = 1024
```

---

#### MethodImplOptions

**Line:** 253494

**Values:**

```
Unmanaged = 4
ForwardRef = 16
PreserveSig = 128
InternalCall = 4096
Synchronized = 32
NoInlining = 8
AggressiveInlining = 256
NoOptimization = 64
SecurityMitigations = 1024
```

---

#### MidpointRounding

**Line:** 26518

**Values:**

```
ToEven = 0
AwayFromZero = 1
```

---

#### MissingEntryAction

**Line:** 1317330

**Values:**

```
Nothing = 0
AddEntriesToSharedData = 1
RemoveEntriesFromTable = 2
```

---

#### MissingSchemaAction

**Line:** 1087079

**Values:**

```
Add = 1
Ignore = 2
Error = 3
AddWithKey = 4
```

---

#### MissingTranslationBehavior

**Line:** 1318491

**Values:**

```
ShowMissingTranslationMessage = 1
PrintWarning = 2
```

---

#### MixedLightingMode

**Line:** 875282

**Values:**

```
IndirectOnly = 0
Shadowmask = 2
Subtractive = 1
```

---

#### MixedLightingSetup

**Line:** 916918

**Values:**

```
None = 0
ShadowMask = 1
Subtractive = 2
```

---

#### ModelActionExecuteFlags

**Line:** 601128

**Values:**

```
None = 0
LeaderSynchronized = 1
FollowerSynchronized = 4
FollowerUnsynchronized = 8
```

---

#### MonoSslPolicyErrors

**Line:** 1448938

**Values:**

```
None = 0
RemoteCertificateNotAvailable = 1
RemoteCertificateNameMismatch = 2
RemoteCertificateChainErrors = 4
```

---

#### MotionBlurMode

**Line:** 909487

**Values:**

```
CameraOnly = 0
CameraAndObjects = 1
```

---

#### MotionBlurQuality

**Line:** 909496

**Values:**

```
Low = 0
Medium = 1
High = 2
```

---

#### MotionVectorGenerationMode

**Line:** 875668

**Values:**

```
Camera = 0
Object = 1
ForceNoMotion = 2
```

---

#### MouseButton

**Line:** 641467

**Values:**

```
LeftMouse = 0
RightMouse = 1
MiddleMouse = 2
```

---

#### MoveDirection

**Line:** 1360899

**Values:**

```
Left = 0
Up = 1
Right = 2
Down = 3
None = 4
```

---

#### MsaaQuality

**Line:** 900499

**Values:**

```
Disabled = 1
_2x = 2
_4x = 4
_8x = 8
```

---

#### MultiplayerEntityClientPhase

**Line:** 551869

**Values:**

```
NoSession = 0
NoEntity = 1
LoadingEntity = 2
EntityActive = 3
```

---

#### MultiplayerEntityDirectConnectionProtocol

**Line:** 552867

---

#### MultiplierFormatType

**Line:** 736249

**Values:**

```
NoMultiplier = 0
XMultiplier = 1
MultiplierPercentage = 2
Percentage = 3
NegativePercentage = 4
```

---

#### MusicType

**Line:** 705612

**Values:**

```
None = 0
Battle = 1
Menu = 2
```

---

#### NPOTSupport

**Line:** 875449

**Values:**

```
None = 0
Restricted = 1
Full = 2
```

---

#### NamespaceHandling

**Line:** 741442

**Values:**

```
Default = 0
OmitDuplicates = 1
```

---

#### NamespaceList

**Line:** 760478

---

#### NativeArrayOptions

**Line:** 838065

**Values:**

```
UninitializedMemory = 0
ClearMemory = 1
```

---

#### Navigation

**Line:** 1355717

---

#### NavigationEvent

**Line:** 1556241

---

#### NavigationMoveEvent

**Line:** 637178

---

#### NestedTweenFailureBehaviour

**Line:** 1432729

**Values:**

```
TryToPreserveSequence = 0
KillWholeSequence = 1
```

---

#### NetworkInterfaceComponent

**Line:** 798913

**Values:**

```
IPv4 = 0
IPv6 = 1
```

---

#### NetworkReachability

**Line:** 870386

**Values:**

```
NotReachable = 0
ReachableViaCarrierDataNetwork = 1
ReachableViaLocalAreaNetwork = 2
```

---

#### NeutralRangeReductionMode

**Line:** 909721

**Values:**

```
Reinhard = 1
BT2390 = 2
```

---

#### NewLineHandling

**Line:** 741451

**Values:**

```
Replace = 0
Entitize = 1
None = 2
```

---

#### NftMetadataCorePropertyId

**Line:** 581833

**Values:**

```
Name = 0
Description = 1
ImageUrl = 2
```

---

#### NftOwnerAddress

**Line:** 582026

---

#### NftPropertyType

**Line:** 581843

**Values:**

```
Enum = 0
Text = 1
Boolean = 2
Number = 3
```

---

#### NormalizationForm

**Line:** 215056

**Values:**

```
FormC = 1
FormD = 2
FormKC = 5
FormKD = 6
```

---

#### NotificationPresentation

**Line:** 1591167

**Values:**

```
Alert = 1
Badge = 2
Sound = 4
Vibrate = 8
```

---

#### NotificationRepeatInterval

**Line:** 1591350

**Values:**

```
OneTime = 0
Daily = 1
```

---

#### NotificationSettingsSection

**Line:** 1591178

**Values:**

```
Application = 0
Category = 1
```

---

#### NotificationStatus

**Line:** 1552614

**Values:**

```
Unknown = 0
Scheduled = 1
Delivered = 2
```

---

#### NotificationStyle

**Line:** 1552246

**Values:**

```
None = 0
BigPictureStyle = 1
BigTextStyle = 2
```

---

#### NotificationsPermissionStatus

**Line:** 1591448

**Values:**

```
RequestPending = 0
Granted = 1
Denied = 2
```

---

#### NotifyCollectionChangedAction

**Line:** 785809

**Values:**

```
Add = 0
Remove = 1
Replace = 2
Move = 3
Reset = 4
```

---

#### NtlmFlags

**Line:** 1448368

**Values:**

```
NegotiateUnicode = 1
NegotiateOem = 2
RequestTarget = 4
NegotiateNtlm = 512
NegotiateDomainSupplied = 4096
NegotiateWorkstationSupplied = 8192
NegotiateAlwaysSign = 32768
NegotiateNtlm2Key = 524288
Negotiate128 = 536870912
```

---

#### NullValueHandling

**Line:** 1032327

**Values:**

```
Include = 0
Ignore = 1
```

---

#### NumberStyles

**Line:** 272177

**Values:**

```
None = 0
AllowLeadingWhite = 1
AllowTrailingWhite = 2
AllowLeadingSign = 4
AllowTrailingSign = 8
AllowParentheses = 16
AllowDecimalPoint = 32
AllowThousands = 64
AllowExponent = 128
AllowCurrencySymbol = 256
AllowHexSpecifier = 512
Integer = 7
HexNumber = 515
Number = 111
Float = 167
Currency = 383
Any = 511
```

---

#### OTL_FeatureTag

**Line:** 1346793

**Values:**

```
kern = 1801810542
liga = 1818847073
mark = 1835102827
mkmk = 1835756907
```

---

#### ObjectCreationHandling

**Line:** 1032336

**Values:**

```
Auto = 0
Reuse = 1
Replace = 2
```

---

#### ObjectDispatcher

**Line:** 880382

---

#### ObjectGraphDump

**Line:** 521314

---

#### OcclusionTest

**Line:** 1377963

**Values:**

```
None = 0
TestAll = 1
TestCulled = 2
```

---

#### OidGroup

**Line:** 778803

**Values:**

```
All = 0
HashAlgorithm = 1
EncryptionAlgorithm = 2
PublicKeyAlgorithm = 3
SignatureAlgorithm = 4
Attribute = 5
ExtensionOrAttribute = 6
EnhancedKeyUsage = 7
Policy = 8
Template = 9
KeyDerivationFunction = 10
```

---

#### OidcTokenFormat

**Line:** 1372998

**Values:**

```
Standard = 0
Full = 1
FullWithLicences = 2
```

---

#### OpaqueSortMode

**Line:** 891693

**Values:**

```
Default = 0
FrontToBack = 1
NoDistanceSort = 2
```

---

#### OpenFlags

**Line:** 778903

**Values:**

```
ReadOnly = 0
ReadWrite = 1
MaxAllowed = 2
OpenExistingOnly = 4
IncludeArchived = 8
```

---

#### OpenGLESVersion

**Line:** 892497

**Values:**

```
None = 0
OpenGLES20 = 1
OpenGLES30 = 2
OpenGLES31 = 3
OpenGLES31AEP = 4
OpenGLES32 = 5
```

---

#### OperationStatus

**Line:** 466068

**Values:**

```
Done = 0
DestinationTooSmall = 1
NeedMoreData = 2
InvalidData = 3
```

---

#### Operator

**Line:** 770249

---

#### OptimizeFor

**Line:** 1329674

**Values:**

```
Default = 0
Performance = 1
Size = 2
FastCompilation = 3
Balanced = 4
```

---

#### OrientType

**Line:** 1429709

**Values:**

```
None = 0
ToPath = 1
LookAtTransform = 2
LookAtPosition = 3
```

---

#### Overflow

**Line:** 659842

**Values:**

```
Visible = 0
Hidden = 1
```

---

#### OverflowClipBox

**Line:** 659862

**Values:**

```
PaddingBox = 0
ContentBox = 1
```

---

#### PackingRules

**Line:** 821445

**Values:**

```
Exact = 0
Aggressive = 1
```

---

#### PaddingMode

**Line:** 217955

**Values:**

```
None = 1
PKCS7 = 2
Zeros = 3
ANSIX923 = 4
ISO10126 = 5
```

---

#### PanelScaleMode

**Line:** 640195

**Values:**

```
ConstantPixelSize = 0
ConstantPhysicalSize = 1
ScaleWithScreenSize = 2
```

---

#### PanelScreenMatchMode

**Line:** 640205

**Values:**

```
MatchWidthOrHeight = 0
Shrink = 1
Expand = 2
```

---

#### ParallelEtwProvider

**Line:** 191301

---

#### ParameterAttributes

**Line:** 266070

**Values:**

```
None = 0
In = 1
Out = 2
Lcid = 4
Retval = 8
Optional = 16
HasDefault = 4096
HasFieldMarshal = 8192
Reserved3 = 16384
Reserved4 = 32768
ReservedMask = 61440
```

---

#### ParseError

**Line:** 1200788

**Values:**

```
None = 0
Syntax = 1
Overflow = 2
Underflow = 3
```

---

#### Parser

**Line:** 1322707

---

#### ParticleSystemAnimationMode

**Line:** 1577958

**Values:**

```
Grid = 0
Sprites = 1
```

---

#### ParticleSystemCurveMode

**Line:** 1577935

**Values:**

```
Constant = 0
Curve = 1
TwoCurves = 2
TwoConstants = 3
```

---

#### ParticleSystemGradientMode

**Line:** 1577946

**Values:**

```
Color = 0
Gradient = 1
TwoColors = 2
TwoGradients = 3
RandomColor = 4
```

---

#### ParticleSystemRenderMode

**Line:** 1577922

**Values:**

```
Billboard = 0
Stretch = 1
HorizontalBillboard = 2
VerticalBillboard = 3
Mesh = 4
None = 5
```

---

#### ParticleSystemScalingMode

**Line:** 1577986

**Values:**

```
Hierarchy = 0
Local = 1
Shape = 2
```

---

#### ParticleSystemSimulationSpace

**Line:** 1577967

**Values:**

```
Local = 0
World = 1
Custom = 2
```

---

#### ParticleSystemStopBehavior

**Line:** 1577977

**Values:**

```
StopEmittingAndClear = 0
StopEmitting = 1
```

---

#### PathMode

**Line:** 1425572

**Values:**

```
Ignore = 0
Full3D = 1
TopDown2D = 2
Sidescroller2D = 3
```

---

#### PathType

**Line:** 1425583

**Values:**

```
Linear = 0
CatmullRom = 1
CubicBezier = 2
```

---

#### PayoutType

**Line:** 1530747

**Values:**

```
Other = 0
Currency = 1
Item = 2
Resource = 3
```

---

#### PenEventType

**Line:** 1580382

**Values:**

```
NoContact = 0
PenDown = 1
PenUp = 2
```

---

#### PenStatus

**Line:** 1580370

**Values:**

```
None = 0
Contact = 1
Barrel = 2
Inverted = 4
Eraser = 8
```

---

#### PendingDynamicPurchaseContentStatus

**Line:** 583787

**Values:**

```
RequestedByClient = 0
ConfirmedByServer = 1
```

---

#### PendingPurchaseAnalyticsContextStatus

**Line:** 585885

**Values:**

```
RequestedByClient = 0
ConfirmedByServer = 1
```

---

#### PerObjectData

**Line:** 895792

**Values:**

```
None = 0
LightProbe = 1
ReflectionProbes = 2
LightProbeProxyVolume = 4
Lightmaps = 8
LightData = 16
MotionVectors = 32
LightIndices = 64
ReflectionProbeData = 128
OcclusionProbe = 256
OcclusionProbeProxyVolume = 512
ShadowMask = 1024
```

---

#### PeriodUnits

**Line:** 1146636

**Values:**

```
None = 0
Years = 1
Months = 2
Weeks = 4
Days = 8
AllDateUnits = 15
YearMonthDay = 11
Hours = 16
Minutes = 32
Seconds = 64
Milliseconds = 128
Ticks = 256
Nanoseconds = 512
HourMinuteSecond = 112
AllTimeUnits = 1008
DateAndTime = 1019
AllUnits = 1023
```

---

#### PermissionState

**Line:** 217371

**Values:**

```
None = 0
Unrestricted = 1
```

---

#### PermissionStatus

**Line:** 1553459

**Values:**

```
NotRequested = 0
Allowed = 1
Denied = 2
DeniedDontAskAgain = 3
RequestPending = 4
NotificationsBlockedForApp = 5
```

---

#### PersistentListenerMode

**Line:** 886859

**Values:**

```
EventDefined = 0
Void = 1
Object = 2
Int = 3
Float = 4
String = 5
Bool = 6
```

---

#### PersonNameFormatterStyle

**Line:** 1590241

**Values:**

```
Default = 0
Short = 1
Medium = 2
Long = 3
Abbreviated = 4
```

---

#### PickingMode

**Line:** 670857

**Values:**

```
Position = 0
Ignore = 1
```

---

#### PinAlignment

**Line:** 1442549

**Values:**

```
TopLeft = 0
TopRight = 1
BottomLeft = 2
BottomRight = 3
CenterLeft = 4
CenterRight = 5
TopCenter = 6
BottomCenter = 7
```

---

#### PixelPerfectCamera

**Line:** 1363745

---

#### PixelValidationChannels

**Line:** 1594401

**Values:**

```
RGB = 0
R = 1
G = 2
B = 3
A = 4
```

---

#### PlatformID

**Line:** 176590

**Values:**

```
Win32S = 0
Win32Windows = 1
Win32NT = 2
WinCE = 3
Unix = 4
Xbox = 5
MacOSX = 6
```

---

#### PlayerDashboardActionAttribute

**Line:** 601174

---

#### PlayerDebugIncidentUploadMode

**Line:** 542603

**Values:**

```
Normal = 0
SilentlyOmitUploads = 1
RejectIncidents = 2
```

---

#### PlayerDeletionSource

**Line:** 538169

**Values:**

```
Admin = 0
User = 1
System = 2
Unknown = 3
```

---

#### PlayerDeletionStatus

**Line:** 538181

**Values:**

```
None = 0
DeletedByUnknownLegacy = 2
ScheduledByAdmin = 1
DeletedByAdmin = 6
ScheduledByUser = 5
DeletedByUser = 14
ScheduledBySystem = 9
DeletedBySystem = 22
ScheduledByUnknown = 25
DeletedByUnknown = 30
```

---

#### PlayerEventFacebookAuthenticationRevoked

**Line:** 535262

---

#### PlayerEventInAppValidationComplete

**Line:** 535866

---

#### PlayerEventNameChanged

**Line:** 535040

---

#### PlayerEventSocialAuthConflictResolved

**Line:** 535317

---

#### PlayerGender

**Line:** 1052063

**Values:**

```
None = 0
Male = 1
Female = 2
```

---

#### PlayerHandleJoinResponse

**Line:** 1063742

---

#### PlayerLoopTiming

**Line:** 1099296

**Values:**

```
Initialization = 0
LastInitialization = 1
EarlyUpdate = 2
LastEarlyUpdate = 3
FixedUpdate = 4
LastFixedUpdate = 5
PreUpdate = 6
LastPreUpdate = 7
Update = 8
LastUpdate = 9
PreLateUpdate = 10
LastPreLateUpdate = 11
PostLateUpdate = 12
LastPostLateUpdate = 13
TimeUpdate = 14
LastTimeUpdate = 15
```

---

#### PointerEvent

**Line:** 1556331

---

#### PointerEventData

**Line:** 1359181

---

#### PointerType

**Line:** 1450690

**Values:**

```
Mouse = 0
Touch = 1
Pen = 2
```

---

#### PolicyEnforcement

**Line:** 778511

**Values:**

```
Never = 0
WhenSupported = 1
Always = 2
```

---

#### PolyFillType

**Line:** 1361492

**Values:**

```
pftEvenOdd = 0
pftNonZero = 1
pftPositive = 2
pftNegative = 3
```

---

#### PolyType

**Line:** 1361482

**Values:**

```
ptSubject = 0
ptClip = 1
```

---

#### Position

**Line:** 659833

**Values:**

```
Relative = 0
Absolute = 1
```

---

#### PreloadAssetTableMetadata

**Line:** 1327554

---

#### PreloadBehavior

**Line:** 1319410

**Values:**

```
NoPreloading = 0
PreloadSelectedLocale = 1
PreloadSelectedLocaleAndFallbacks = 2
PreloadAllLocales = 3
```

---

#### PreserveReferencesHandling

**Line:** 1032347

**Values:**

```
None = 0
Objects = 1
Arrays = 2
All = 3
```

---

#### PrettyPrintFlag

**Line:** 499149

**Values:**

```
None = 0
SizeOnly = 1
Shorten = 4
Hide = 8
HideInDiff = 16
```

---

#### Priority

**Line:** 837630

**Values:**

```
PriorityLow = 0
PriorityHigh = 1
```

---

#### ProbeAdjustmentVolume

**Line:** 816457

---

#### ProbeReferenceVolume

**Line:** 817612

---

#### ProbeVolume

**Line:** 819105

---

#### ProbeVolumeBlendingTextureMemoryBudget

**Line:** 818962

**Values:**

```
MemoryBudgetLow = 128
MemoryBudgetMedium = 256
MemoryBudgetHigh = 512
```

---

#### ProbeVolumeSHBands

**Line:** 818973

**Values:**

```
SphericalHarmonicsL1 = 1
SphericalHarmonicsL2 = 2
```

---

#### ProbeVolumeTextureMemoryBudget

**Line:** 818951

**Values:**

```
MemoryBudgetLow = 512
MemoryBudgetMedium = 1024
MemoryBudgetHigh = 2048
```

---

#### ProcessWindowStyle

**Line:** 778316

**Values:**

```
Hidden = 1
Maximized = 3
Minimized = 2
Normal = 0
```

---

#### ProcessingState

**Line:** 837792

**Values:**

```
Unknown = 0
InQueue = 1
Reading = 2
Completed = 3
Failed = 4
Canceled = 5
```

---

#### ProcessorArchitecture

**Line:** 266196

**Values:**

```
None = 0
MSIL = 1
X86 = 2
IA64 = 3
Amd64 = 4
Arm = 5
```

---

#### ProductCatalogPayout

**Line:** 1406922

---

#### ProductType

**Line:** 1531092

**Values:**

```
Consumable = 0
NonConsumable = 1
Subscription = 2
```

---

#### ProfilerCategoryColor

**Line:** 837048

**Values:**

```
Render = 0
Scripts = 1
BurstJobs = 2
Other = 3
Physics = 4
Animation = 5
Audio = 6
AudioJob = 7
AudioUpdateJob = 8
Lighting = 9
GC = 10
VSync = 11
Memory = 12
Internal = 13
UI = 14
Build = 15
Input = 16
```

---

#### ProfilerCounterOptions

**Line:** 837126

**Values:**

```
None = 0
FlushOnEndOfFrame = 2
ResetToZeroOnFlush = 4
```

---

#### ProfilerGraphControl

**Line:** 1444692

---

#### ProfilerMarkerDataType

**Line:** 837356

**Values:**

```
InstanceId = 1
Int32 = 2
UInt32 = 3
Int64 = 4
UInt64 = 5
Float = 6
Double = 7
String16 = 9
Blob8 = 11
GfxResourceId = 12
```

---

#### ProfilerMarkerDataUnit

**Line:** 837112

**Values:**

```
Undefined = 0
TimeNanoseconds = 1
Bytes = 2
Count = 3
Percent = 4
FrequencyHz = 5
```

---

#### ProfilerRecorderOptions

**Line:** 837137

**Values:**

```
None = 0
StartImmediately = 1
KeepAliveDuringDomainReload = 2
CollectOnlyOnCurrentThread = 4
WrapAroundWhenCapacityReached = 8
SumAllSamplesInFrame = 16
GpuRecorder = 64
Default = 24
```

---

#### PropagationPhase

**Line:** 635056

**Values:**

```
None = 0
TrickleDown = 1
BubbleUp = 3
AtTarget = 2
DefaultAction = 4
DefaultActionAtTarget = 5
```

---

#### PropertyAttributes

**Line:** 266210

**Values:**

```
None = 0
SpecialName = 512
RTSpecialName = 1024
HasDefault = 4096
Reserved2 = 8192
Reserved3 = 16384
Reserved4 = 32768
ReservedMask = 62464
```

---

#### ProtocolStatus

**Line:** 551655

**Values:**

```
Pending = 0
InvalidGameMagic = 1
WireProtocolVersionMismatch = 2
ClusterRunning = 3
ClusterStarting = 4
ClusterShuttingDown = 5
InMaintenance = 6
```

---

#### ProtocolType

**Line:** 800402

**Values:**

```
IP = 0
IPv6HopByHopOptions = 0
Icmp = 1
Igmp = 2
Ggp = 3
IPv4 = 4
Tcp = 6
Pup = 12
Udp = 17
Idp = 22
IPv6 = 41
IPv6RoutingHeader = 43
IPv6FragmentHeader = 44
IPSecEncapsulatingSecurityPayload = 50
IPSecAuthenticationHeader = 51
IcmpV6 = 58
IPv6NoNextHeader = 59
IPv6DestinationOptions = 60
ND = 77
Raw = 255
Unspecified = 0
Ipx = 1000
Spx = 1256
SpxII = 1257
```

---

#### ProviderBehaviourFlags

**Line:** 1437231

**Values:**

```
None = 0
CanProvideWithFailedDependencies = 1
```

---

#### PublishedAppPlatform

**Line:** 1564895

**Values:**

```
Android = 0
Ios = 1
```

---

#### PurchaseFailureReason

**Line:** 1531172

**Values:**

```
PurchasingUnavailable = 0
ExistingPurchasePending = 1
ProductUnavailable = 2
SignatureInvalid = 3
UserCancelled = 4
PaymentDeclined = 5
DuplicateTransaction = 6
Unknown = 7
```

---

#### PurchaseProcessingResult

**Line:** 1531187

**Values:**

```
Complete = 0
Pending = 1
```

---

#### QueryLastRespondedNotificationState

**Line:** 1591480

**Values:**

```
Pending = 0
NoRespondedNotification = 1
HaveRespondedNotification = 2
```

---

#### QueryTriggerInteraction

**Line:** 1577063

**Values:**

```
UseGlobal = 0
Ignore = 1
Collide = 2
```

---

#### RSASignaturePaddingMode

**Line:** 217846

**Values:**

```
Pkcs1 = 0
Pss = 1
```

---

#### RTClearFlags

**Line:** 892460

**Values:**

```
None = 0
Color = 1
Depth = 2
Stencil = 4
All = 7
DepthStencil = 6
ColorDepth = 3
ColorStencil = 5
```

---

#### RayTracingAccelerationStructureBuildFlags

**Line:** 891619

**Values:**

```
None = 0
PreferFastTrace = 1
PreferFastBuild = 2
MinimizeMemory = 4
```

---

#### ReactionEntryUiView

**Line:** 708048

---

#### ReadState

**Line:** 741648

**Values:**

```
Initial = 0
Interactive = 1
Error = 2
EndOfFile = 3
Closed = 4
```

---

#### ReadStatus

**Line:** 837617

**Values:**

```
Complete = 0
InProgress = 1
Failed = 2
Truncated = 4
Canceled = 5
```

---

#### RealUserStatus

**Line:** 1590253

**Values:**

```
Unsupported = 0
Unknown = 1
LikelyReal = 2
```

---

#### RectTransform

**Line:** 885982

---

#### RedDotReason

**Line:** 695439

**Values:**

```
IdleRewardClaimable = 0
CanStartForgeUpgrade = 10
ForgeUpgradeClaimable = 11
ArenaRewardsTutorial = 20
ArenaRewardsClaimable = 21
CanUseArenaTickets = 22
CanUseDungeonKeys = 30
CanSummonSkills = 40
CanUpgradeSkills = 41
QuickEquipSkillsOptionAvailable = 42
CanSummonMount = 50
CanStartHatchingEggs = 60
HatchedEggsClaimable = 61
QuickEquipPetsOptionAvailable = 62
TechNodeClaimable = 70
GuildJoinRequests = 80
WarEndRewardsClaimable = 81
WarPassRewardsClaimable = 82
CanUseWarTickets = 83
MainProgressPassRewardsClaimable = 90
SteppingStonesFreeResourcePack = 100
```

---

#### ReferenceLoopHandling

**Line:** 1032358

**Values:**

```
Error = 0
Ignore = 1
Serialize = 2
```

---

#### ReflectionProbe

**Line:** 871445

---

#### ReflectionProbeRefreshMode

**Line:** 892299

**Values:**

```
OnAwake = 0
EveryFrame = 1
ViaScripting = 2
```

---

#### ReflectionProbeSortingCriteria

**Line:** 895842

**Values:**

```
None = 0
Importance = 1
Size = 2
ImportanceThenSize = 3
```

---

#### RegexOptions

**Line:** 776856

**Values:**

```
None = 0
IgnoreCase = 1
Multiline = 2
ExplicitCapture = 4
Compiled = 8
Singleline = 16
IgnorePatternWhitespace = 32
RightToLeft = 64
ECMAScript = 256
CultureInvariant = 512
```

---

#### ReloadAttribute

**Line:** 810965

---

#### RenderBufferLoadAction

**Line:** 891703

**Values:**

```
Load = 0
Clear = 1
DontCare = 2
```

---

#### RenderBufferStoreAction

**Line:** 891713

**Values:**

```
Store = 0
Resolve = 1
StoreAndResolve = 2
DontCare = 3
```

---

#### RenderGraphUtils

**Line:** 831965

---

#### RenderGraphUtilsResources

**Line:** 832144

---

#### RenderMode

**Line:** 1576372

**Values:**

```
ScreenSpaceOverlay = 0
ScreenSpaceCamera = 1
WorldSpace = 2
```

---

#### RenderObjects

**Line:** 912479

---

#### RenderPassEvent

**Line:** 911760

**Values:**

```
BeforeRendering = 0
BeforeRenderingShadows = 50
AfterRenderingShadows = 100
BeforeRenderingPrePasses = 150
AfterRenderingPrePasses = 200
BeforeRenderingGbuffer = 210
AfterRenderingGbuffer = 220
BeforeRenderingDeferredLights = 230
AfterRenderingDeferredLights = 240
BeforeRenderingOpaques = 250
AfterRenderingOpaques = 300
BeforeRenderingSkybox = 350
AfterRenderingSkybox = 400
BeforeRenderingTransparents = 450
AfterRenderingTransparents = 500
BeforeRenderingPostProcessing = 550
AfterRenderingPostProcessing = 600
AfterRendering = 1000
```

---

#### RenderPathCompatibility

**Line:** 916205

**Values:**

```
Forward = 1
Deferred = 2
ForwardPlus = 4
All = 7
```

---

#### RenderQueueType

**Line:** 912470

**Values:**

```
Opaque = 0
Transparent = 1
```

---

#### RenderStateMask

**Line:** 896438

**Values:**

```
Nothing = 0
Blend = 1
Raster = 2
Depth = 4
Stencil = 8
Everything = 15
```

---

#### RenderTargetFlags

**Line:** 892243

**Values:**

```
None = 0
ReadOnlyDepth = 1
ReadOnlyStencil = 2
ReadOnlyDepthStencil = 3
```

---

#### RenderTextureCreationFlags

**Line:** 875601

**Values:**

```
MipMap = 1
AutoGenerateMips = 2
SRGB = 4
EyeTexture = 8
EnableRandomWrite = 16
CreatedFromScript = 32
AllowVerticalFlip = 128
NoResolvedColorSurface = 256
DynamicallyScalable = 1024
BindMS = 2048
DynamicallyScalableExplicit = 131072
```

---

#### RenderTextureFormat

**Line:** 875554

**Values:**

```
ARGB32 = 0
Depth = 1
ARGBHalf = 2
Shadowmap = 3
RGB565 = 4
ARGB4444 = 5
ARGB1555 = 6
Default = 7
ARGB2101010 = 8
DefaultHDR = 9
ARGB64 = 10
ARGBFloat = 11
RGFloat = 12
RGHalf = 13
RFloat = 14
RHalf = 15
R8 = 16
ARGBInt = 17
RGInt = 18
RInt = 19
BGRA32 = 20
RGB111110Float = 22
RG32 = 23
RGBAUShort = 24
RG16 = 25
BGRA10101010_XR = 26
BGR101010_XR = 27
R16 = 28
```

---

#### RenderTextureMemoryless

**Line:** 875630

**Values:**

```
None = 0
Color = 1
Depth = 2
MSAA = 4
```

---

#### RenderTextureReadWrite

**Line:** 875619

**Values:**

```
Default = 0
Linear = 1
sRGB = 2
```

---

#### RenderTextureSubElement

**Line:** 892475

**Values:**

```
Color = 0
Depth = 1
Stencil = 2
Default = 3
```

---

#### RendererListStatus

**Line:** 896514

**Values:**

```
kRendererListEmpty = 0
kRendererListPopulated = 1
```

---

#### RendererOverrideOption

**Line:** 914932

**Values:**

```
Custom = 0
UsePipelineSettings = 1
```

---

#### RendererType

**Line:** 900541

**Values:**

```
Custom = 0
UniversalRenderer = 1
_2DRenderer = 2
```

---

#### RenderersParameters

**Line:** 1382652

---

#### RenderingLayerUtils

**Line:** 912971

---

#### RenderingMode

**Line:** 915638

**Values:**

```
Forward = 0
ForwardPlus = 2
Deferred = 1
```

---

#### RenderingPath

**Line:** 875176

**Values:**

```
VertexLit = 0
Forward = 1
DeferredLighting = 2
DeferredShading = 3
```

---

#### Repeat

**Line:** 659989

**Values:**

```
NoRepeat = 0
Space = 1
Round = 2
Repeat = 3
```

---

#### RequestError

**Line:** 1495693

---

#### RequestParameterType

**Line:** 1495180

**Values:**

```
Path = 0
Query = 1
UserDefinedQueries = 2
```

---

#### Required

**Line:** 1032368

**Values:**

```
Default = 0
AllowNull = 1
Always = 2
DisallowNull = 3
```

---

#### ResourceLocation

**Line:** 266359

**Values:**

```
ContainedInAnotherAssembly = 2
ContainedInManifestFile = 4
Embedded = 1
```

---

#### ResourceManager

**Line:** 1434118

---

#### ResponsiveEnable

**Line:** 1506650

---

#### RestrictionType

**Line:** 1564758

**Values:**

```
NotAllowed = 0
RequireConsent = 1
RequireLi = 2
```

---

#### Result

**Line:** 1407725

**Values:**

```
True = 0
False = 1
Unsupported = 2
```

---

#### RewindCallbackMode

**Line:** 1432790

**Values:**

```
FireIfPositionChanged = 0
FireAlwaysWithRewind = 1
FireAlways = 2
```

---

#### RichTextTagParser

**Line:** 1346377

---

#### RigidbodyType2D

**Line:** 1578319

**Values:**

```
Dynamic = 0
Kinematic = 1
Static = 2
```

---

#### RotateMode

**Line:** 1425593

**Values:**

```
Fast = 0
FastBeyond360 = 1
WorldAxisAdd = 2
LocalAxisAdd = 3
```

---

#### Rule

**Line:** 1088466

**Values:**

```
None = 0
Cascade = 1
SetNull = 2
SetDefault = 3
```

---

#### RuntimeInitializeLoadType

**Line:** 883581

**Values:**

```
AfterSceneLoad = 0
BeforeSceneLoad = 1
AfterAssembliesLoaded = 2
BeforeSplashScreen = 3
SubsystemRegistration = 4
```

---

#### RuntimePlatform

**Line:** 870418

**Values:**

```
OSXEditor = 0
OSXPlayer = 1
WindowsPlayer = 2
OSXWebPlayer = 3
OSXDashboardPlayer = 4
WindowsWebPlayer = 5
WindowsEditor = 7
IPhonePlayer = 8
XBOX360 = 10
PS3 = 9
Android = 11
NaCl = 12
FlashPlayer = 15
LinuxPlayer = 13
LinuxEditor = 16
WebGLPlayer = 17
MetroPlayerX86 = 18
WSAPlayerX86 = 18
MetroPlayerX64 = 19
WSAPlayerX64 = 19
MetroPlayerARM = 20
WSAPlayerARM = 20
WP8Player = 21
BlackBerryPlayer = 22
TizenPlayer = 23
PSP2 = 24
PS4 = 25
PSM = 26
XboxOne = 27
SamsungTVPlayer = 28
WiiU = 30
tvOS = 31
Switch = 32
Lumin = 33
Stadia = 34
LinuxHeadlessSimulation = 35
GameCoreXboxSeries = 36
GameCoreXboxOne = 37
PS5 = 38
EmbeddedLinuxArm64 = 39
EmbeddedLinuxArm32 = 40
EmbeddedLinuxX64 = 41
EmbeddedLinuxX86 = 42
LinuxServer = 43
WindowsServer = 44
OSXServer = 45
QNXArm32 = 46
QNXArm64 = 47
QNXX64 = 48
QNXX86 = 49
VisionOS = 50
Switch2 = 51
KeplerArm64 = 52
KeplerX64 = 53
```

---

#### SRMath

**Line:** 1504836

---

#### SRPLensFlareBlendMode

**Line:** 820820

**Values:**

```
Additive = 0
Screen = 1
Premultiply = 2
Lerp = 3
```

---

#### SRPLensFlareColorType

**Line:** 820858

**Values:**

```
Constant = 0
RadialGradient = 1
AngularGradient = 2
```

---

#### SRPLensFlareDistribution

**Line:** 820832

**Values:**

```
Uniform = 0
Curve = 1
Random = 2
```

---

#### SRPLensFlareType

**Line:** 820844

**Values:**

```
Image = 0
Circle = 1
Polygon = 2
Ring = 3
LensFlareDataSRP = 4
```

---

#### SampleCount

**Line:** 913786

**Values:**

```
One = 1
Two = 2
Four = 4
```

---

#### SaveOptions

**Line:** 1561042

**Values:**

```
None = 0
DisableFormatting = 1
OmitDuplicateNamespaces = 2
```

---

#### ScaleMode

**Line:** 1451150

**Values:**

```
StretchToFill = 0
ScaleAndCrop = 1
ScaleToFit = 2
```

---

#### SceneReleaseMode

**Line:** 1437342

**Values:**

```
ReleaseSceneWhenSceneUnloaded = 0
OnlyReleaseSceneOnHandleRelease = 1
```

---

#### ScheduleMode

**Line:** 836702

**Values:**

```
Run = 0
Batched = 1
Parallel = 1
Single = 2
```

---

#### SchemaNames

**Line:** 761945

---

#### SchemaSerializationMode

**Line:** 1088477

**Values:**

```
IncludeSchema = 1
ExcludeSchema = 2
```

---

#### ScrambleMode

**Line:** 1425604

**Values:**

```
None = 0
All = 1
Uppercase = 2
Lowercase = 3
Numerals = 4
Custom = 5
```

---

#### ScreenOrientation

**Line:** 875412

**Values:**

```
Portrait = 1
PortraitUpsideDown = 2
LandscapeLeft = 3
LandscapeRight = 4
AutoRotation = 5
Unknown = 0
Landscape = 3
```

---

#### ScreenSpaceLensFlareResolution

**Line:** 909580

**Values:**

```
Half = 2
Quarter = 4
Eighth = 8
```

---

#### ScriptableRenderPassInput

**Line:** 911748

**Values:**

```
None = 0
Depth = 1
Normal = 2
Color = 4
Motion = 8
```

---

#### ScrollRect

**Line:** 1356201

---

#### ScrollView

**Line:** 627367

---

#### ScrollViewMode

**Line:** 627300

**Values:**

```
Vertical = 0
Horizontal = 1
VerticalAndHorizontal = 2
```

---

#### Scrollbar

**Line:** 1355940

---

#### ScrollerVisibility

**Line:** 627310

**Values:**

```
Auto = 0
AlwaysVisible = 1
Hidden = 2
```

---

#### SearchOption

**Line:** 469834

**Values:**

```
TopDirectoryOnly = 0
AllDirectories = 1
```

---

#### SearchType

**Line:** 892755

**Values:**

```
ProjectPath = 0
BuiltinPath = 1
BuiltinExtraPath = 2
ShaderName = 3
```

---

#### SecondaryStatType

**Line:** 1076395

**Values:**

```
CriticalChance = 0
CriticalMulti = 1
BlockChance = 2
HealthRegen = 3
LifeSteal = 4
DoubleDamageChance = 5
DamageMulti = 6
MeleeDamageMulti = 7
RangedDamageMulti = 8
AttackSpeed = 9
SkillDamageMulti = 10
SkillCooldownMulti = 11
HealthMulti = 12
```

---

#### SectionAlignment

**Line:** 1565241

**Values:**

```
Undefined = 0
Start = 1
Center = 2
End = 3
```

---

#### SecurityAction

**Line:** 217383

**Values:**

```
Demand = 2
Assert = 3
Deny = 4
PermitOnly = 5
LinkDemand = 6
InheritanceDemand = 7
RequestMinimum = 8
RequestOptional = 9
RequestRefuse = 10
```

---

#### SecurityProtocolType

**Line:** 791351

**Values:**

```
SystemDefault = 0
Ssl3 = 48
Tls = 192
Tls11 = 768
Tls12 = 3072
Tls13 = 12288
```

---

#### SeekOrigin

**Line:** 468159

**Values:**

```
Begin = 0
Current = 1
End = 2
```

---

#### SelectMode

**Line:** 800434

**Values:**

```
SelectRead = 0
SelectWrite = 1
SelectError = 2
```

---

#### Selectable

**Line:** 1356593

---

#### SelectionType

**Line:** 641257

**Values:**

```
None = 0
Single = 1
Multiple = 2
```

---

#### SendEventOptions

**Line:** 891343

**Values:**

```
kAppendNone = 0
kAppendBuildGuid = 1
kAppendBuildTarget = 2
```

---

#### SendMessageOptions

**Line:** 870409

**Values:**

```
RequireReceiver = 0
DontRequireReceiver = 1
```

---

#### SerializationFormat

**Line:** 1085006

**Values:**

```
Xml = 0
Binary = 1
```

---

#### ServiceLifetime

**Line:** 1543475

**Values:**

```
Singleton = 0
Scoped = 1
Transient = 2
```

---

#### ServicesInitializationState

**Line:** 1589010

**Values:**

```
Uninitialized = 0
Initializing = 1
Initialized = 2
```

---

#### SessionProtocol

**Line:** 556687

---

#### SessionUtil

**Line:** 545722

---

#### Settings

**Line:** 1442602

---

#### ShEvalMode

**Line:** 900623

**Values:**

```
Auto = 0
PerVertex = 1
Mixed = 2
PerPixel = 3
```

---

#### ShaderPathID

**Line:** 914105

**Values:**

```
Lit = 0
SimpleLit = 1
Unlit = 2
TerrainLit = 3
ParticlesLit = 4
ParticlesSimpleLit = 5
ParticlesUnlit = 6
BakedLit = 7
SpeedTree7 = 8
SpeedTree7Billboard = 9
SpeedTree8 = 10
SpeedTree9 = 11
ComplexLit = 12
```

---

#### ShaderPropertyFlags

**Line:** 898741

**Values:**

```
None = 0
HideInInspector = 1
PerRendererData = 2
NoScaleOffset = 4
Normal = 8
HDR = 16
Gamma = 32
NonModifiableTextureData = 64
MainTexture = 128
MainColor = 256
```

---

#### ShadowCascadesOption

**Line:** 905756

**Values:**

```
NoCascades = 0
TwoCascades = 1
FourCascades = 2
```

---

#### ShadowCaster2D

**Line:** 1365044

---

#### ShadowCastingMode

**Line:** 891888

**Values:**

```
Off = 0
On = 1
TwoSided = 2
ShadowsOnly = 3
```

---

#### ShadowMesh2D

**Line:** 1365497

---

#### ShadowObjectsFilter

**Line:** 875301

**Values:**

```
AllObjects = 0
DynamicOnly = 1
StaticOnly = 2
```

---

#### ShadowQuality

**Line:** 900429

**Values:**

```
Disabled = 0
HardShadows = 1
SoftShadows = 2
```

---

#### ShadowResolution

**Line:** 900451

**Values:**

```
_256 = 256
_512 = 512
_1024 = 1024
_2048 = 2048
_4096 = 4096
_8192 = 8192
```

---

#### ShadowSamplingMode

**Line:** 892309

**Values:**

```
CompareDepths = 0
RawDepth = 1
None = 2
```

---

#### ShadowShape2D

**Line:** 1365610

---

#### ShadowUtility

**Line:** 1365673

---

#### ShadowmaskMode

**Line:** 875292

**Values:**

```
Shadowmask = 0
DistanceShadowmask = 1
```

---

#### SheetsBaseServiceRequest

**Line:** 1383100

---

#### SinglePassStereoMode

**Line:** 892418

**Values:**

```
None = 0
SideBySide = 1
Instancing = 2
Multiview = 3
```

---

#### SingularUnityLogger

**Line:** 1571870

---

#### SliceType

**Line:** 660029

**Values:**

```
Sliced = 0
Tiled = 1
```

---

#### Slider

**Line:** 1356925

---

#### SliderDirection

**Line:** 613904

**Values:**

```
Horizontal = 0
Vertical = 1
```

---

#### SocialAuthenticateResult

**Line:** 543200

---

#### SocketAsyncOperation

**Line:** 800444

**Values:**

```
None = 0
Accept = 1
Connect = 2
Disconnect = 3
Receive = 4
ReceiveFrom = 5
ReceiveMessageFrom = 6
Send = 7
SendPackets = 8
SendTo = 9
```

---

#### SocketError

**Line:** 800461

**Values:**

```
Success = 0
Interrupted = 10004
AccessDenied = 10013
Fault = 10014
InvalidArgument = 10022
TooManyOpenSockets = 10024
WouldBlock = 10035
InProgress = 10036
AlreadyInProgress = 10037
NotSocket = 10038
DestinationAddressRequired = 10039
MessageSize = 10040
ProtocolType = 10041
ProtocolOption = 10042
ProtocolNotSupported = 10043
SocketNotSupported = 10044
OperationNotSupported = 10045
ProtocolFamilyNotSupported = 10046
AddressFamilyNotSupported = 10047
AddressAlreadyInUse = 10048
AddressNotAvailable = 10049
NetworkDown = 10050
NetworkUnreachable = 10051
NetworkReset = 10052
ConnectionAborted = 10053
ConnectionReset = 10054
NoBufferSpaceAvailable = 10055
IsConnected = 10056
NotConnected = 10057
Shutdown = 10058
TimedOut = 10060
ConnectionRefused = 10061
HostDown = 10064
HostUnreachable = 10065
ProcessLimit = 10067
SystemNotReady = 10091
VersionNotSupported = 10092
NotInitialized = 10093
Disconnecting = 10101
TypeNotFound = 10109
HostNotFound = 11001
TryAgain = 11002
NoRecovery = 11003
NoData = 11004
IOPending = 997
OperationAborted = 995
```

---

#### SocketFlags

**Line:** 800516

**Values:**

```
None = 0
OutOfBand = 1
Peek = 2
DontRoute = 4
MaxIOVectorLength = 16
Truncated = 256
ControlDataTruncated = 512
Broadcast = 1024
Multicast = 2048
Partial = 32768
```

---

#### SocketOptionName

**Line:** 800545

**Values:**

```
Debug = 1
AcceptConnection = 2
ReuseAddress = 4
KeepAlive = 8
DontRoute = 16
Broadcast = 32
UseLoopback = 64
Linger = 128
OutOfBandInline = 256
SendBuffer = 4097
ReceiveBuffer = 4098
SendLowWater = 4099
ReceiveLowWater = 4100
SendTimeout = 4101
ReceiveTimeout = 4102
Error = 4103
Type = 4104
ReuseUnicastPort = 12295
MaxConnections = 2147483647
IPOptions = 1
HeaderIncluded = 2
TypeOfService = 3
IpTimeToLive = 4
MulticastInterface = 9
MulticastTimeToLive = 10
MulticastLoopback = 11
AddMembership = 12
DropMembership = 13
DontFragment = 14
AddSourceMembership = 15
DropSourceMembership = 16
BlockSource = 17
UnblockSource = 18
PacketInformation = 19
HopLimit = 21
IPProtectionLevel = 23
IPv6Only = 27
NoDelay = 1
BsdUrgent = 2
Expedited = 2
NoChecksum = 1
ChecksumCoverage = 20
UpdateAcceptContext = 28683
UpdateConnectContext = 28688
```

---

#### SocketShutdown

**Line:** 800598

**Values:**

```
Receive = 0
Send = 1
Both = 2
```

---

#### SocketType

**Line:** 800608

**Values:**

```
Stream = 1
Dgram = 2
Raw = 3
Rdm = 4
Seqpacket = 5
```

---

#### SoftShadowQuality

**Line:** 900439

**Values:**

```
UsePipelineSettings = 0
Low = 1
Medium = 2
High = 3
```

---

#### SortDirection

**Line:** 626386

**Values:**

```
Ascending = 0
Descending = 1
```

---

#### SortingCriteria

**Line:** 896956

**Values:**

```
None = 0
SortingLayer = 1
RenderQueue = 2
BackToFront = 4
QuantizedFrontToBack = 8
OptimizeStateChanges = 16
CanvasOrder = 32
RendererPriority = 64
CommonOpaque = 59
CommonTransparent = 23
```

---

#### SpecialStartupMode

**Line:** 1432758

**Values:**

```
None = 0
SetLookAt = 1
SetShake = 2
SetPunch = 3
SetCameraShakePosition = 4
```

---

#### SpreadsheetsResource

**Line:** 1384444

---

#### SpriteAssetImportFormats

**Line:** 1229940

**Values:**

```
None = 0
TexturePackerJsonArray = 1
```

---

#### SpriteDrawMode

**Line:** 869372

**Values:**

```
Simple = 0
Sliced = 1
Tiled = 2
```

---

#### SpriteMeshType

**Line:** 869469

**Values:**

```
FullRect = 0
Tight = 1
```

---

#### SpritePackingRotation

**Line:** 869478

**Values:**

```
None = 0
FlipHorizontal = 1
FlipVertical = 2
Rotate180 = 3
Any = 15
```

---

#### SqlCompareOptions

**Line:** 1092083

**Values:**

```
None = 0
IgnoreCase = 1
IgnoreNonSpace = 2
IgnoreKanaType = 8
IgnoreWidth = 16
BinarySort = 32768
BinarySort2 = 16384
```

---

#### SslPolicyErrors

**Line:** 802803

**Values:**

```
None = 0
RemoteCertificateNotAvailable = 1
RemoteCertificateNameMismatch = 2
RemoteCertificateChainErrors = 4
```

---

#### SslProtocols

**Line:** 778450

**Values:**

```
None = 0
Ssl2 = 12
Ssl3 = 48
Tls = 192
Tls11 = 768
Tls12 = 3072
Tls13 = 12288
Default = 240
```

---

#### StackTraceLogType

**Line:** 870376

**Values:**

```
None = 0
ScriptOnly = 1
Full = 2
```

---

#### StandaloneInputModule

**Line:** 1360668

---

#### StatNature

**Line:** 1076694

**Values:**

```
Multiplier = 0
Additive = 1
Divisor = 2
OneMinusMultiplier = 3
```

---

#### StatType

**Line:** 1077360

**Values:**

```
Damage = 0
Health = 1
MaxLevel = 2
Experience = 3
Cost = 4
TimerSpeed = 5
SellPrice = 6
MaxCount = 7
Bonus = 8
FreebieChance = 10
CriticalChance = 11
CriticalDamage = 12
BlockChance = 13
HealthRegen = 14
LifeSteal = 15
DoubleDamageChance = 16
AttackSpeed = 17
MoveSpeed = 18
```

---

#### SteamClientHandlingStatus

**Line:** 587077

**Values:**

```
Unknown = 0
Declined = 1
Approved = 2
```

---

#### SteamPeriod

**Line:** 584126

**Values:**

```
Day = 0
Week = 1
Month = 2
Year = 3
```

---

#### SteamPurchasingStatus

**Line:** 534130

**Values:**

```
Locked = 0
Active = 1
Trusted = 2
```

---

#### StencilOp

**Line:** 891840

**Values:**

```
Keep = 0
Zero = 1
Replace = 2
IncrementSaturate = 3
DecrementSaturate = 4
Invert = 5
IncrementWrap = 6
DecrementWrap = 7
```

---

#### SteppingStoneEndReason

**Line:** 1079602

**Values:**

```
Fell = 0
ReachedEnd = 1
```

---

#### StoreActionsOptimization

**Line:** 900560

**Values:**

```
Auto = 0
Discard = 1
Store = 2
```

---

#### StoreLocation

**Line:** 778915

**Values:**

```
CurrentUser = 1
LocalMachine = 2
```

---

#### StoreName

**Line:** 778924

**Values:**

```
AddressBook = 1
AuthRoot = 2
CertificateAuthority = 3
Disallowed = 4
My = 5
Root = 6
TrustedPeople = 7
TrustedPublisher = 8
```

---

#### StoreSpecificPurchaseErrorCode

**Line:** 1407494

**Values:**

```
SKErrorUnknown = 0
SKErrorClientInvalid = 1
SKErrorPaymentCancelled = 2
SKErrorPaymentInvalid = 3
SKErrorPaymentNotAllowed = 4
SKErrorStoreProductNotAvailable = 5
SKErrorCloudServicePermissionDenied = 6
SKErrorCloudServiceNetworkConnectionFailed = 7
SKErrorCloudServiceRevoked = 8
BILLING_RESPONSE_RESULT_OK = 9
BILLING_RESPONSE_RESULT_USER_CANCELED = 10
BILLING_RESPONSE_RESULT_SERVICE_UNAVAILABLE = 11
BILLING_RESPONSE_RESULT_BILLING_UNAVAILABLE = 12
BILLING_RESPONSE_RESULT_ITEM_UNAVAILABLE = 13
BILLING_RESPONSE_RESULT_DEVELOPER_ERROR = 14
BILLING_RESPONSE_RESULT_ERROR = 15
BILLING_RESPONSE_RESULT_ITEM_ALREADY_OWNED = 16
BILLING_RESPONSE_RESULT_ITEM_NOT_OWNED = 17
IABHELPER_ERROR_BASE = 18
IABHELPER_REMOTE_EXCEPTION = 19
IABHELPER_BAD_RESPONSE = 20
IABHELPER_VERIFICATION_FAILED = 21
IABHELPER_SEND_INTENT_FAILED = 22
IABHELPER_USER_CANCELLED = 23
IABHELPER_UNKNOWN_PURCHASE_RESPONSE = 24
IABHELPER_MISSING_TOKEN = 25
IABHELPER_UNKNOWN_ERROR = 26
IABHELPER_SUBSCRIPTIONS_NOT_AVAILABLE = 27
IABHELPER_INVALID_CONSUMPTION = 28
Amazon_ALREADY_PURCHASED = 29
Amazon_FAILED = 30
Amazon_INVALID_SKU = 31
Amazon_NOT_SUPPORTED = 32
Unknown = 33
```

---

#### StreamMessageTransport

**Line:** 547634

---

#### StreamingContextStates

**Line:** 226368

**Values:**

```
CrossProcess = 1
CrossMachine = 2
File = 4
Persistence = 8
Remoting = 16
Other = 32
Clone = 64
CrossAppDomain = 128
All = 255
```

---

#### StringComparison

**Line:** 57733

**Values:**

```
CurrentCulture = 0
CurrentCultureIgnoreCase = 1
InvariantCulture = 2
InvariantCultureIgnoreCase = 3
Ordinal = 4
OrdinalIgnoreCase = 5
```

---

#### StringEscapeHandling

**Line:** 1032379

**Values:**

```
Default = 0
EscapeNonAscii = 1
EscapeHtml = 2
```

---

#### StringSplitOptions

**Line:** 57747

**Values:**

```
None = 0
RemoveEmptyEntries = 1
```

---

#### StyleKeyword

**Line:** 658426

**Values:**

```
Undefined = 0
Null = 1
Auto = 2
None = 3
Initial = 4
```

---

#### SubPassFlags

**Line:** 895046

**Values:**

```
None = 0
ReadOnlyDepth = 2
ReadOnlyStencil = 4
ReadOnlyDepthStencil = 6
```

---

#### SubStringFormatter

**Line:** 1322131

---

#### SubscriptionPeriodUnit

**Line:** 1407735

**Values:**

```
Day = 0
Month = 1
Week = 2
Year = 3
NotAvailable = 4
```

---

#### SubscriptionRenewalStatus

**Line:** 586508

**Values:**

```
Unknown = 0
NotExpectedToRenew = 1
ExpectedToRenew = 2
```

---

#### SubscriptionState

**Line:** 1511104

**Values:**

```
Unsubscribed = 0
Synced = 1
Unsynced = 2
Error = 3
Subscribing = 4
```

---

#### SupportedOnRenderPipelineAttribute

**Line:** 894823

---

#### SupportedRenderingFeatures

**Line:** 897202

---

#### SynchronisationStage

**Line:** 891609

**Values:**

```
VertexProcessing = 0
PixelProcessing = 1
```

---

#### SynchronisationStageFlags

**Line:** 892511

**Values:**

```
VertexProcessing = 1
PixelProcessing = 2
ComputeProcessing = 4
AllGPUOperations = 7
```

---

#### SystemInterfaceFlags

**Line:** 1590846

**Values:**

```
None = 0
IInitializeSystem = 2
IExecuteSystem = 4
ICleanupSystem = 8
ITearDownSystem = 16
IReactiveSystem = 32
```

---

#### SystemLanguage

**Line:** 870502

**Values:**

```
Afrikaans = 0
Arabic = 1
Basque = 2
Belarusian = 3
Bulgarian = 4
Catalan = 5
Chinese = 6
Czech = 7
Danish = 8
Dutch = 9
English = 10
Estonian = 11
Faroese = 12
Finnish = 13
French = 14
German = 15
Greek = 16
Hebrew = 17
Icelandic = 19
Indonesian = 20
Italian = 21
Japanese = 22
Korean = 23
Latvian = 24
Lithuanian = 25
Norwegian = 26
Polish = 27
Portuguese = 28
Romanian = 29
Russian = 30
SerboCroatian = 31
Slovak = 32
Slovenian = 33
Spanish = 34
Swedish = 35
Thai = 36
Turkish = 37
Ukrainian = 38
Vietnamese = 39
ChineseSimplified = 40
ChineseTraditional = 41
Hindi = 42
Unknown = 43
Hungarian = 18
```

---

#### TMP_Compatibility

**Line:** 1221717

---

#### TMP_InputField

**Line:** 1223874

---

#### TMP_TextElementType

**Line:** 1227041

**Values:**

```
Character = 0
Sprite = 1
```

---

#### TMP_VertexDataUpdateFlags

**Line:** 1221179

**Values:**

```
None = 0
Vertices = 1
Uv0 = 2
Uv2 = 4
Uv4 = 8
Colors32 = 16
All = 255
```

---

#### TableEntryReference

**Line:** 1318336

---

#### TableReference

**Line:** 1318222

---

#### TagUnitType

**Line:** 1225720

**Values:**

```
Pixels = 0
FontUnits = 1
Percentage = 2
```

---

#### TagValueType

**Line:** 1225709

**Values:**

```
None = 0
NumericalValue = 1
StringValue = 2
ColorValue = 4
```

---

#### TaskContinuationOptions

**Line:** 211699

**Values:**

```
None = 0
PreferFairness = 1
LongRunning = 2
AttachedToParent = 4
DenyChildAttach = 8
HideScheduler = 16
LazyCancellation = 32
RunContinuationsAsynchronously = 64
NotOnRanToCompletion = 65536
NotOnFaulted = 131072
NotOnCanceled = 262144
OnlyOnRanToCompletion = 393216
OnlyOnFaulted = 327680
OnlyOnCanceled = 196608
ExecuteSynchronously = 524288
```

---

#### TaskCreationOptions

**Line:** 211669

**Values:**

```
None = 0
PreferFairness = 1
LongRunning = 2
AttachedToParent = 4
DenyChildAttach = 8
HideScheduler = 16
RunContinuationsAsynchronously = 64
```

---

#### TaskStatus

**Line:** 209499

**Values:**

```
Created = 0
WaitingForActivation = 1
WaitingToRun = 2
Running = 3
WaitingForChildrenToComplete = 4
RanToCompletion = 5
Canceled = 6
Faulted = 7
```

---

#### TemporalAAQuality

**Line:** 914416

**Values:**

```
VeryLow = 0
Low = 1
Medium = 2
High = 3
VeryHigh = 4
```

---

#### TextAlignmentOptions

**Line:** 1226962

**Values:**

```
TopLeft = 257
Top = 258
TopRight = 260
TopJustified = 264
TopFlush = 272
TopGeoAligned = 288
Left = 513
Center = 514
Right = 516
Justified = 520
Flush = 528
CenterGeoAligned = 544
BottomLeft = 1025
Bottom = 1026
BottomRight = 1028
BottomJustified = 1032
BottomFlush = 1040
BottomGeoAligned = 1056
BaselineLeft = 2049
Baseline = 2050
BaselineRight = 2052
BaselineJustified = 2056
BaselineFlush = 2064
BaselineGeoAligned = 2080
MidlineLeft = 4097
Midline = 4098
MidlineRight = 4100
MidlineJustified = 4104
MidlineFlush = 4112
MidlineGeoAligned = 4128
CaplineLeft = 8193
Capline = 8194
CaplineRight = 8196
CaplineJustified = 8200
CaplineFlush = 8208
CaplineGeoAligned = 8224
Converted = 65535
```

---

#### TextAnchor

**Line:** 1580941

**Values:**

```
UpperLeft = 0
UpperCenter = 1
UpperRight = 2
MiddleLeft = 3
MiddleCenter = 4
MiddleRight = 5
LowerLeft = 6
LowerCenter = 7
LowerRight = 8
```

---

#### TextClipping

**Line:** 1452103

**Values:**

```
Overflow = 0
Clip = 1
Ellipsis = 2
```

---

#### TextContainerAnchors

**Line:** 1220142

**Values:**

```
TopLeft = 0
Top = 1
TopRight = 2
Left = 3
Middle = 4
Right = 5
BottomLeft = 6
Bottom = 7
BottomRight = 8
Custom = 9
```

---

#### TextEditor

**Line:** 1453124

---

#### TextElementType

**Line:** 1348710

**Values:**

```
Character = 1
Sprite = 2
```

---

#### TextFontWeight

**Line:** 1347142

**Values:**

```
Thin = 100
ExtraLight = 200
Light = 300
Regular = 400
Medium = 500
SemiBold = 600
Bold = 700
Heavy = 800
Black = 900
```

---

#### TextGeneratorType

**Line:** 1580957

**Values:**

```
Standard = 0
Advanced = 1
```

---

#### TextOverflow

**Line:** 659927

**Values:**

```
Clip = 0
Ellipsis = 1
```

---

#### TextOverflowModes

**Line:** 1227060

**Values:**

```
Overflow = 0
Ellipsis = 1
Masking = 2
Truncate = 3
ScrollRect = 4
Page = 5
Linked = 6
```

---

#### TextOverflowPosition

**Line:** 659917

**Values:**

```
End = 0
Start = 1
Middle = 2
```

---

#### TextRenderFlags

**Line:** 1227032

**Values:**

```
DontRender = 0
Render = 255
```

---

#### TextWrappingModes

**Line:** 1227074

**Values:**

```
NoWrap = 0
Normal = 1
PreserveWhitespace = 2
PreserveWhitespaceNoWrap = 3
```

---

#### TextureCreationFlags

**Line:** 899343

**Values:**

```
None = 0
MipChain = 1
DontInitializePixels = 4
Crunch = 64
DontUploadUponCreate = 1024
IgnoreMipmapLimit = 2048
```

---

#### TextureDimension

**Line:** 892379

**Values:**

```
None = 0
Any = 1
Tex2D = 2
Tex3D = 3
Cube = 4
Tex2DArray = 5
CubeArray = 6
```

---

#### TextureFormat

**Line:** 875460

**Values:**

```
Alpha8 = 1
ARGB4444 = 2
RGB24 = 3
RGBA32 = 4
ARGB32 = 5
RGB565 = 7
R16 = 9
DXT1 = 10
DXT5 = 12
RGBA4444 = 13
BGRA32 = 14
RHalf = 15
RGHalf = 16
RGBAHalf = 17
RFloat = 18
RGFloat = 19
RGBAFloat = 20
YUY2 = 21
RGB9e5Float = 22
BC4 = 26
BC5 = 27
BC6H = 24
BC7 = 25
DXT1Crunched = 28
DXT5Crunched = 29
PVRTC_RGB2 = 30
PVRTC_RGBA2 = 31
PVRTC_RGB4 = 32
PVRTC_RGBA4 = 33
ETC_RGB4 = 34
EAC_R = 41
EAC_R_SIGNED = 42
EAC_RG = 43
EAC_RG_SIGNED = 44
ETC2_RGB = 45
ETC2_RGBA1 = 46
ETC2_RGBA8 = 47
ASTC_4x4 = 48
ASTC_5x5 = 49
ASTC_6x6 = 50
ASTC_8x8 = 51
ASTC_10x10 = 52
ASTC_12x12 = 53
RG16 = 62
R8 = 63
ETC_RGB4Crunched = 64
ETC2_RGBA8Crunched = 65
ASTC_HDR_4x4 = 66
ASTC_HDR_5x5 = 67
ASTC_HDR_6x6 = 68
ASTC_HDR_8x8 = 69
ASTC_HDR_10x10 = 70
ASTC_HDR_12x12 = 71
RG32 = 72
RGB48 = 73
RGBA64 = 74
R8_SIGNED = 75
RG16_SIGNED = 76
RGB24_SIGNED = 77
RGBA32_SIGNED = 78
R16_SIGNED = 79
RG32_SIGNED = 80
RGB48_SIGNED = 81
RGBA64_SIGNED = 82
```

---

#### TextureMappingOptions

**Line:** 1227094

**Values:**

```
Character = 0
Line = 1
Paragraph = 2
MatchAspect = 3
```

---

#### TextureSizeMode

**Line:** 831763

**Values:**

```
Explicit = 0
Scale = 1
Functor = 2
```

---

#### TextureWrapMode

**Line:** 875438

**Values:**

```
Repeat = 0
Clamp = 1
Mirror = 2
MirrorOnce = 3
```

---

#### ThreadState

**Line:** 179122

**Values:**

```
Running = 0
StopRequested = 1
SuspendRequested = 2
Background = 4
Unstarted = 8
Stopped = 16
WaitSleepJoin = 32
Suspended = 64
AbortRequested = 128
Aborted = 256
```

---

#### TimeSpanFormatOptions

**Line:** 1321168

**Values:**

```
InheritDefaults = 0
Abbreviate = 1
AbbreviateOff = 2
LessThan = 4
LessThanOff = 8
TruncateShortest = 16
TruncateAuto = 32
TruncateFill = 64
TruncateFull = 128
RangeMilliSeconds = 256
RangeSeconds = 512
RangeMinutes = 1024
RangeHours = 2048
RangeDays = 4096
RangeWeeks = 8192
```

---

#### TimeSpanStyles

**Line:** 272591

**Values:**

```
None = 0
AssumeNegative = 1
```

---

#### TimeUnit

**Line:** 659473

**Values:**

```
Second = 0
Millisecond = 1
```

---

#### TimelineSlot

**Line:** 603311

---

#### TimerState

**Line:** 696319

**Values:**

```
Idle = 0
InProgress = 1
Done = 2
```

---

#### TinyBenchmark

**Line:** 524664

---

#### TlsMessageTransport

**Line:** 548302

---

#### TlsProtocols

**Line:** 1449213

**Values:**

```
Zero = 0
Tls10Client = 128
Tls10Server = 64
Tls10 = 192
Tls11Client = 512
Tls11Server = 256
Tls11 = 768
Tls12Client = 2048
Tls12Server = 1024
Tls12 = 3072
ClientMask = 2688
ServerMask = 1344
```

---

#### Toggle

**Line:** 1357444

---

#### Token

**Line:** 1490429

---

#### TonemappingMode

**Line:** 909711

**Values:**

```
None = 0
Neutral = 1
ACES = 2
```

---

#### TouchScreenKeyboard

**Line:** 885677

---

#### TouchScreenKeyboardType

**Line:** 885846

**Values:**

```
Default = 0
ASCIICapable = 1
NumbersAndPunctuation = 2
URL = 3
NumberPad = 4
PhonePad = 5
NamePhonePad = 6
EmailAddress = 7
NintendoNetworkAccount = 8
Social = 9
Search = 10
DecimalPad = 11
OneTimeCode = 12
```

---

#### TouchType

**Line:** 1580269

**Values:**

```
Direct = 0
Indirect = 1
Stylus = 2
```

---

#### TraceEventType

**Line:** 777545

**Values:**

```
Critical = 1
Error = 2
Warning = 4
Information = 8
Verbose = 16
Start = 256
Stop = 512
Suspend = 1024
Resume = 2048
Transfer = 4096
```

---

#### TraceOptions

**Line:** 777785

**Values:**

```
None = 0
LogicalOperationStack = 1
DateTime = 2
Timestamp = 4
ProcessId = 8
ThreadId = 16
Callstack = 32
```

---

#### TransferFormat

**Line:** 1570716

**Values:**

```
Binary = 1
Text = 2
```

---

#### TransferFunction

**Line:** 875399

**Values:**

```
sRGB = 0
BT1886 = 1
PQ = 2
Linear = 3
Gamma22 = 4
```

---

#### TransformOriginOffset

**Line:** 659936

**Values:**

```
Left = 1
Right = 2
Top = 3
Bottom = 4
Center = 5
```

---

#### TransientError

**Line:** 1310253

---

#### TranslationLocale

**Line:** 1406793

**Values:**

```
zh_TW = 0
cs_CZ = 1
da_DK = 2
nl_NL = 3
en_US = 4
fr_FR = 5
fi_FI = 6
de_DE = 7
iw_IL = 8
hi_IN = 9
it_IT = 10
ja_JP = 11
ko_KR = 12
no_NO = 13
pl_PL = 14
pt_PT = 15
ru_RU = 16
es_ES = 17
sv_SE = 18
zh_CN = 19
en_AU = 20
en_CA = 21
en_GB = 22
fr_CA = 23
el_GR = 24
id_ID = 25
ms_MY = 26
pt_BR = 27
es_MX = 28
th_TH = 29
tr_TR = 30
vi_VN = 31
```

---

#### TransparencySortMode

**Line:** 875189

**Values:**

```
Default = 0
Perspective = 1
Orthographic = 2
CustomAxis = 3
```

---

#### TrickleDown

**Line:** 634871

**Values:**

```
NoTrickleDown = 0
TrickleDown = 1
```

---

#### TweenType

**Line:** 1429065

**Values:**

```
Tweener = 0
Sequence = 1
Callback = 2
```

---

#### TwoPaneSplitViewOrientation

**Line:** 630083

**Values:**

```
Horizontal = 0
Vertical = 1
```

---

#### TypeAttributes

**Line:** 267040

**Values:**

```
VisibilityMask = 7
NotPublic = 0
Public = 1
NestedPublic = 2
NestedPrivate = 3
NestedFamily = 4
NestedAssembly = 5
NestedFamANDAssem = 6
NestedFamORAssem = 7
LayoutMask = 24
AutoLayout = 0
SequentialLayout = 8
ExplicitLayout = 16
ClassSemanticsMask = 32
Class = 0
Interface = 32
Abstract = 128
Sealed = 256
SpecialName = 1024
Import = 4096
Serializable = 8192
WindowsRuntime = 16384
StringFormatMask = 196608
AnsiClass = 0
UnicodeClass = 65536
AutoClass = 131072
CustomFormatClass = 196608
CustomFormatMask = 12582912
BeforeFieldInit = 1048576
RTSpecialName = 2048
HasSecurity = 262144
ReservedMask = 264192
```

---

#### TypeCode

**Line:** 59505

**Values:**

```
Empty = 0
Object = 1
DBNull = 2
Boolean = 3
Char = 4
SByte = 5
Byte = 6
Int16 = 7
UInt16 = 8
Int32 = 9
UInt32 = 10
Int64 = 11
UInt64 = 12
Single = 13
Double = 14
Decimal = 15
DateTime = 16
String = 18
```

---

#### TypeGenerationOptions

**Line:** 1458034

**Values:**

```
None = 0
ValueType = 2
ReferenceType = 4
Default = 6
```

---

#### TypeInferenceRules

**Line:** 834935

**Values:**

```
TypeReferencedByFirstArgument = 0
TypeReferencedBySecondArgument = 1
ArrayOfTypeReferencedByFirstArgument = 2
TypeOfFirstArgument = 3
```

---

#### TypeNameAssemblyFormatHandling

**Line:** 1032389

**Values:**

```
Simple = 0
Full = 1
```

---

#### TypeNameHandling

**Line:** 1032399

**Values:**

```
None = 0
Objects = 1
Arrays = 2
All = 3
Auto = 4
```

---

#### UIParticle

**Line:** 1563400

---

#### UIParticleAttractor

**Line:** 1563772

---

#### UISubset

**Line:** 897443

**Values:**

```
UIToolkit_UGUI = 1
LowLevel = 2
```

---

#### UISystemProfilerApi

**Line:** 1576689

---

#### UVChannelFlags

**Line:** 1578072

**Values:**

```
UV0 = 1
UV1 = 2
UV2 = 4
UV3 = 8
```

---

#### UltimateResourceFallbackLocation

**Line:** 264340

**Values:**

```
MainAssembly = 0
Satellite = 1
```

---

#### UnauthorizedType

**Line:** 685279

**Values:**

```
Undefined = 0
UserBanned = 1
UserTimedOut = 2
UserTokenInvalid = 3
UserTokenMismatch = 4
UserNotFound = 5
```

---

#### UndefinedSchemaIdHandling

**Line:** 1042886

**Values:**

```
None = 0
UseTypeName = 1
UseAssemblyQualifiedName = 2
```

---

#### UniTaskStatus

**Line:** 1097328

**Values:**

```
Pending = 0
Succeeded = 1
Faulted = 2
Canceled = 3
```

---

#### UnicodeCategory

**Line:** 272600

**Values:**

```
UppercaseLetter = 0
LowercaseLetter = 1
TitlecaseLetter = 2
ModifierLetter = 3
OtherLetter = 4
NonSpacingMark = 5
SpacingCombiningMark = 6
EnclosingMark = 7
DecimalDigitNumber = 8
LetterNumber = 9
OtherNumber = 10
SpaceSeparator = 11
LineSeparator = 12
ParagraphSeparator = 13
Control = 14
Format = 15
Surrogate = 16
PrivateUse = 17
ConnectorPunctuation = 18
DashPunctuation = 19
OpenPunctuation = 20
ClosePunctuation = 21
InitialQuotePunctuation = 22
FinalQuotePunctuation = 23
OtherPunctuation = 24
MathSymbol = 25
CurrencySymbol = 26
ModifierSymbol = 27
OtherSymbol = 28
OtherNotAssigned = 29
```

---

#### UnicodeDecodingConformance

**Line:** 799046

**Values:**

```
Auto = 0
Strict = 1
Compat = 2
Loose = 3
```

---

#### UnicodeEncodingConformance

**Line:** 799057

**Values:**

```
Auto = 0
Strict = 1
Compat = 2
```

---

#### UnityEventCallState

**Line:** 887496

**Values:**

```
Off = 0
EditorAndRuntime = 1
RuntimeOnly = 2
```

---

#### UnityTls

**Line:** 771376

---

#### UnityWebRequest

**Line:** 1566247

---

#### UniversalResource

**Line:** 916250

**Values:**

```
BackBufferColor = 0
BackBufferDepth = 1
CameraColor = 2
CameraDepth = 3
MainShadowsTexture = 4
AdditionalShadowsTexture = 5
GBuffer0 = 6
GBuffer1 = 7
GBuffer2 = 8
GBuffer3 = 9
GBuffer4 = 10
GBuffer5 = 11
GBuffer6 = 12
CameraOpaqueTexture = 13
CameraDepthTexture = 14
CameraNormalsTexture = 15
MotionVectorColor = 16
MotionVectorDepth = 17
InternalColorLut = 18
DebugScreenColor = 19
DebugScreenDepth = 20
AfterPostProcessColor = 21
OverlayUITexture = 22
RenderingLayersTexture = 23
DBuffer0 = 24
DBuffer1 = 25
DBuffer2 = 26
DBufferDepth = 27
SSAOTexture = 28
```

---

#### UnloadSceneOptions

**Line:** 888968

**Values:**

```
None = 0
UnloadAllEmbeddedSceneObjects = 1
```

---

#### UnmanagedType

**Line:** 229138

**Values:**

```
Bool = 2
I1 = 3
U1 = 4
I2 = 5
U2 = 6
I4 = 7
U4 = 8
I8 = 9
U8 = 10
R4 = 11
R8 = 12
Currency = 15
BStr = 19
LPStr = 20
LPWStr = 21
LPTStr = 22
ByValTStr = 23
IUnknown = 25
IDispatch = 26
Struct = 27
Interface = 28
SafeArray = 29
ByValArray = 30
SysInt = 31
SysUInt = 32
VBByRefStr = 34
AnsiBStr = 35
TBStr = 36
VariantBool = 37
FunctionPtr = 38
AsAny = 40
LPArray = 42
LPStruct = 43
CustomMarshaler = 44
Error = 45
IInspectable = 46
HString = 47
LPUTF8Str = 48
```

---

#### UpdateAvailability

**Line:** 1579029

**Values:**

```
Unknown = 0
UpdateNotAvailable = 1
UpdateAvailable = 2
DeveloperTriggeredUpdateInProgress = 3
```

---

#### UpdateNotice

**Line:** 1432770

**Values:**

```
None = 0
RewindStep = 1
```

---

#### UpdateType

**Line:** 1429075

**Values:**

```
Normal = 0
Late = 1
Fixed = 2
Manual = 3
```

---

#### UploadStatus

**Line:** 1501496

**Values:**

```
NotStarted = 0
Starting = 1
Uploading = 2
Completed = 3
Failed = 4
```

---

#### UpscalingFilterSelection

**Line:** 900583

**Values:**

```
Auto = 0
Linear = 1
Point = 2
FSR = 3
STP = 4
```

---

#### UriComponents

**Line:** 774586

**Values:**

```
Scheme = 1
UserInfo = 2
Host = 4
Port = 8
Path = 16
Query = 32
Fragment = 64
StrongPort = 128
NormalizedHost = 256
KeepDelimiter = 1073741824
AbsoluteUri = 127
HostAndPort = 132
StrongAuthority = 134
SchemeAndServer = 13
HttpRequestUrl = 61
PathAndQuery = 48
```

---

#### UriFormat

**Line:** 774610

**Values:**

```
UriEscaped = 1
Unescaped = 2
SafeUnescaped = 3
```

---

#### UriHostNameType

**Line:** 774714

**Values:**

```
Unknown = 0
Basic = 1
Dns = 2
IPv4 = 3
IPv6 = 4
```

---

#### UriIdnScope

**Line:** 774620

**Values:**

```
None = 0
AllExceptIntranet = 1
All = 2
```

---

#### UriKind

**Line:** 774575

**Values:**

```
RelativeOrAbsolute = 0
Absolute = 1
Relative = 2
```

---

#### UsageHints

**Line:** 641886

**Values:**

```
None = 0
DynamicTransform = 1
GroupTransform = 2
MaskContainer = 4
DynamicColor = 8
```

---

#### UsercentricsAnalyticsEventType

**Line:** 1564875

**Values:**

```
CmpShown = 0
AcceptAllFirstLayer = 1
DenyAllFirstLayer = 2
SaveFirstLayer = 3
AcceptAllSecondLayer = 4
DenyAllSecondLayer = 5
SaveSecondLayer = 6
ImprintLink = 7
MoreInformationLink = 8
PrivacyPolicyLink = 9
CcpaTogglesOn = 10
CcpaTogglesOff = 11
```

---

#### UsercentricsConsentType

**Line:** 1564510

**Values:**

```
Explicit = 0
Implicit = 1
```

---

#### UsercentricsLayout

**Line:** 1565153

**Values:**

```
Undefined = 0
Full = 1
Sheet = 2
PopupBottom = 3
PopupCenter = 4
```

---

#### UsercentricsNetworkMode

**Line:** 1564443

**Values:**

```
World = 0
EU = 1
```

---

#### UsercentricsUserInteraction

**Line:** 1564535

**Values:**

```
AcceptAll = 0
DenyAll = 1
Granular = 2
NoInteraction = 3
```

---

#### UsercentricsVariant

**Line:** 1564905

**Values:**

```
Default = 0
CCPA = 1
TCF = 2
```

---

#### UxmlAttributeDescription

**Line:** 668413

---

#### UxmlSerializedData

**Line:** 669847

---

#### VFXCameraBufferTypes

**Line:** 1587525

**Values:**

```
None = 0
Depth = 1
Color = 2
Normal = 4
```

---

#### VRTextureUsage

**Line:** 875589

**Values:**

```
None = 0
OneEye = 1
TwoEyes = 2
DeviceSpecific = 3
```

---

#### ValidationType

**Line:** 741965

**Values:**

```
None = 0
Auto = 1
DTD = 2
XDR = 3
Schema = 4
```

---

#### ValueTaskSourceOnCompletedFlags

**Line:** 213714

**Values:**

```
None = 0
UseSchedulingContext = 1
FlowExecutionContext = 2
```

---

#### ValueTaskSourceStatus

**Line:** 213724

**Values:**

```
Pending = 0
Succeeded = 1
Faulted = 2
Canceled = 3
```

---

#### VarEnum

**Line:** 229085

**Values:**

```
VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_R4 = 4
VT_R8 = 5
VT_CY = 6
VT_DATE = 7
VT_BSTR = 8
VT_DISPATCH = 9
VT_ERROR = 10
VT_BOOL = 11
VT_VARIANT = 12
VT_UNKNOWN = 13
VT_DECIMAL = 14
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_INT = 22
VT_UINT = 23
VT_VOID = 24
VT_HRESULT = 25
VT_PTR = 26
VT_SAFEARRAY = 27
VT_CARRAY = 28
VT_USERDEFINED = 29
VT_LPSTR = 30
VT_LPWSTR = 31
VT_RECORD = 36
VT_FILETIME = 64
VT_BLOB = 65
VT_STREAM = 66
VT_STORAGE = 67
VT_STREAMED_OBJECT = 68
VT_STORED_OBJECT = 69
VT_BLOB_OBJECT = 70
VT_CF = 71
VT_CLSID = 72
VT_VECTOR = 4096
VT_ARRAY = 8192
VT_BYREF = 16384
```

---

#### VarIntConst

**Line:** 566820

**Values:**

```
Zero = 0
MinusOne = 1
One = 2
Sixteen = 32
```

---

#### Variant

**Line:** 1493654

---

#### VersionChangeType

**Line:** 641857

**Values:**

```
Bindings = 1
ViewData = 2
Hierarchy = 4
Layout = 8
StyleSheet = 16
Styles = 32
Overflow = 64
BorderRadius = 128
BorderWidth = 256
Transform = 512
Size = 1024
Repaint = 2048
Opacity = 4096
Color = 8192
RenderHints = 16384
TransitionProperty = 32768
EventCallbackCategories = 65536
DisableRendering = 131072
BindingRegistration = 262144
DataSource = 524288
Picking = 1048576
```

---

#### VertexAttribute

**Line:** 891672

**Values:**

```
Position = 0
Normal = 1
Tangent = 2
Color = 3
TexCoord0 = 4
TexCoord1 = 5
TexCoord2 = 6
TexCoord3 = 7
TexCoord4 = 8
TexCoord5 = 9
TexCoord6 = 10
TexCoord7 = 11
BlendWeight = 12
BlendIndices = 13
```

---

#### VertexAttributeFormat

**Line:** 891652

**Values:**

```
Float32 = 0
Float16 = 1
UNorm8 = 2
SNorm8 = 3
UNorm16 = 4
SNorm16 = 5
UInt8 = 6
SInt8 = 7
UInt16 = 8
SInt16 = 9
UInt32 = 10
SInt32 = 11
```

---

#### VertexSortingOrder

**Line:** 1225334

**Values:**

```
Normal = 0
Reverse = 1
```

---

#### VerticalAlignmentOptions

**Line:** 1227019

**Values:**

```
Top = 256
Middle = 512
Bottom = 1024
Baseline = 2048
Geometry = 4096
Capline = 8192
```

---

#### VerticalWrapMode

**Line:** 1580975

**Values:**

```
Truncate = 0
Overflow = 1
```

---

#### Visibility

**Line:** 659948

**Values:**

```
Visible = 0
Hidden = 1
```

---

#### VisitExceptionKind

**Line:** 1457327

**Values:**

```
None = 0
Internal = 1
Visitor = 2
All = 3
```

---

#### VisitReturnCode

**Line:** 1457983

**Values:**

```
Ok = 0
NullContainer = 1
InvalidContainerType = 2
MissingPropertyBag = 3
InvalidPath = 4
InvalidCast = 5
AccessViolation = 6
```

---

#### VisualElement

**Line:** 651373

---

#### VisualElementFocusRing

**Line:** 671369

---

#### VolumeFrameworkUpdateMode

**Line:** 900570

**Values:**

```
EveryFrame = 0
ViaScripting = 1
UsePipelineSettings = 2
```

---

#### WaitTimeoutMode

**Line:** 884694

**Values:**

```
Realtime = 0
InGameTime = 1
```

---

#### WebExceptionStatus

**Line:** 792117

**Values:**

```
Success = 0
NameResolutionFailure = 1
ConnectFailure = 2
ReceiveFailure = 3
SendFailure = 4
PipelineFailure = 5
RequestCanceled = 6
ProtocolError = 7
ConnectionClosed = 8
TrustFailure = 9
SecureChannelFailure = 10
ServerProtocolViolation = 11
KeepAliveFailure = 12
Pending = 13
Timeout = 14
ProxyNameResolutionFailure = 15
UnknownError = 16
MessageLengthLimitExceeded = 17
CacheEntryNotFound = 18
RequestProhibitedByCachePolicy = 19
RequestProhibitedByProxy = 20
```

---

#### WebSocketCloseStatus

**Line:** 802424

**Values:**

```
NormalClosure = 1000
EndpointUnavailable = 1001
ProtocolError = 1002
InvalidMessageType = 1003
Empty = 1005
InvalidPayloadData = 1007
PolicyViolation = 1008
MessageTooBig = 1009
MandatoryExtension = 1010
InternalServerError = 1011
```

---

#### WebSocketError

**Line:** 802441

**Values:**

```
Success = 0
InvalidMessageType = 1
Faulted = 2
NativeError = 3
NotAWebSocket = 4
UnsupportedVersion = 5
UnsupportedProtocol = 6
HeaderError = 7
ConnectionClosedPrematurely = 8
InvalidState = 9
```

---

#### WebSocketMessageType

**Line:** 802513

**Values:**

```
Text = 0
Binary = 1
Close = 2
```

---

#### WebSocketState

**Line:** 802564

**Values:**

```
None = 0
Connecting = 1
Open = 2
CloseSent = 3
CloseReceived = 4
Closed = 5
Aborted = 6
```

---

#### WeightedMode

**Line:** 869715

**Values:**

```
None = 0
In = 1
Out = 2
Both = 3
```

---

#### WellKnownObjectMode

**Line:** 221866

**Values:**

```
Singleton = 1
SingleCall = 2
```

---

#### WhitePoint

**Line:** 875388

**Values:**

```
D65 = 0
```

---

#### WhiteSpace

**Line:** 659957

**Values:**

```
Normal = 0
NoWrap = 1
Pre = 2
PreWrap = 3
```

---

#### WhitespaceHandling

**Line:** 741979

**Values:**

```
All = 0
Significant = 1
None = 2
```

---

#### WindowsAccountType

**Line:** 220382

**Values:**

```
Normal = 0
Guest = 1
System = 2
Anonymous = 3
```

---

#### WireDataType

**Line:** 532065

**Values:**

```
Invalid = 0
Null = 1
VarInt = 2
VarInt128 = 3
F32 = 4
F32Vec2 = 5
F32Vec3 = 6
F64 = 7
F64Vec2 = 8
F64Vec3 = 9
Float32 = 10
Float64 = 11
String = 12
Bytes = 13
AbstractStruct = 14
NullableStruct = 15
Struct = 16
EndStruct = 17
ValueCollection = 18
KeyValueCollection = 19
ObjectTable = 20
NullableVarInt = 21
NullableVarInt128 = 22
NullableF32 = 23
NullableF32Vec2 = 24
NullableF32Vec3 = 25
NullableF64 = 26
NullableF64Vec2 = 27
NullableF64Vec3 = 28
NullableFloat32 = 29
NullableFloat64 = 30
MetaGuid = 31
NullableMetaGuid = 32
```

---

#### WireMessageWriteQueue

**Line:** 551472

---

#### WirePacketCompression

**Line:** 551611

**Values:**

```
None = 0
Deflate = 1
```

---

#### WirePacketType

**Line:** 551599

**Values:**

```
None = 0
Message = 1
Ping = 2
PingResponse = 3
HealthCheck = 4
```

---

#### Wrap

**Line:** 659882

**Values:**

```
NoWrap = 0
Wrap = 1
WrapReverse = 2
```

---

#### WrapMode

**Line:** 869799

**Values:**

```
Once = 1
Loop = 2
PingPong = 4
Default = 0
ClampForever = 8
Clamp = 1
```

---

#### WriteState

**Line:** 1032411

**Values:**

```
Error = 0
Closed = 1
Object = 2
Array = 3
Constructor = 4
Property = 5
Start = 6
```

---

#### X500DistinguishedNameFlags

**Line:** 778940

**Values:**

```
None = 0
Reversed = 1
UseSemicolons = 16
DoNotUsePlusSign = 32
DoNotUseQuotes = 64
UseCommas = 128
UseNewLines = 256
UseUTF8Encoding = 4096
UseT61Encoding = 8192
ForceUTF8Encoding = 16384
```

---

#### X509ChainStatusFlags

**Line:** 1447967

**Values:**

```
InvalidBasicConstraints = 1024
NoError = 0
NotSignatureValid = 8
NotTimeNested = 2
NotTimeValid = 1
PartialChain = 65536
UntrustedRoot = 32
```

---

#### X509ContentType

**Line:** 220005

**Values:**

```
Unknown = 0
Cert = 1
SerializedCert = 2
Pfx = 3
Pkcs12 = 3
SerializedStore = 4
Pkcs7 = 5
Authenticode = 6
```

---

#### X509FindType

**Line:** 778991

**Values:**

```
FindByThumbprint = 0
FindBySubjectName = 1
FindBySubjectDistinguishedName = 2
FindByIssuerName = 3
FindByIssuerDistinguishedName = 4
FindBySerialNumber = 5
FindByTimeValid = 6
FindByTimeNotYetValid = 7
FindByTimeExpired = 8
FindByTemplateName = 9
FindByApplicationPolicy = 10
FindByCertificatePolicy = 11
FindByExtension = 12
FindByKeyUsage = 13
FindBySubjectKeyIdentifier = 14
```

---

#### X509KeyStorageFlags

**Line:** 220021

**Values:**

```
DefaultKeySet = 0
UserKeySet = 1
MachineKeySet = 2
Exportable = 4
UserProtected = 8
PersistKeySet = 16
EphemeralKeySet = 32
```

---

#### X509KeyUsageFlags

**Line:** 779014

**Values:**

```
None = 0
EncipherOnly = 1
CrlSign = 2
KeyCertSign = 4
KeyAgreement = 8
DataEncipherment = 16
KeyEncipherment = 32
NonRepudiation = 64
DigitalSignature = 128
DecipherOnly = 32768
```

---

#### X509NameType

**Line:** 779031

**Values:**

```
SimpleName = 0
EmailName = 1
UpnName = 2
DnsName = 3
DnsFromAlternativeName = 4
UrlName = 5
```

---

#### X509RevocationFlag

**Line:** 779044

**Values:**

```
EndCertificateOnly = 0
EntireChain = 1
ExcludeRoot = 2
```

---

#### X509RevocationMode

**Line:** 779054

**Values:**

```
NoCheck = 0
Online = 1
Offline = 2
```

---

#### X509SubjectKeyIdentifierHashAlgorithm

**Line:** 779064

**Values:**

```
Sha1 = 0
ShortSha1 = 1
CapiSha1 = 2
```

---

#### X509VerificationFlags

**Line:** 779075

**Values:**

```
NoFlag = 0
IgnoreNotTimeValid = 1
IgnoreCtlNotTimeValid = 2
IgnoreNotTimeNested = 4
IgnoreInvalidBasicConstraints = 8
AllowUnknownCertificateAuthority = 16
IgnoreWrongUsage = 32
IgnoreInvalidName = 64
IgnoreInvalidPolicy = 128
IgnoreEndRevocationUnknown = 256
IgnoreCtlSignerRevocationUnknown = 512
IgnoreCertificateAuthorityRevocationUnknown = 1024
IgnoreRootRevocationUnknown = 2048
AllFlags = 4095
```

---

#### X86

**Line:** 1345491

---

#### XObjectChange

**Line:** 1561018

**Values:**

```
Add = 0
Remove = 1
Name = 2
Value = 3
```

---

#### XmlDateTimeSerializationMode

**Line:** 751443

**Values:**

```
Local = 0
Utc = 1
Unspecified = 2
RoundtripKind = 3
```

---

#### XmlNamespaceScope

**Line:** 752344

**Values:**

```
All = 0
ExcludeXml = 1
Local = 2
```

---

#### XmlNodeChangedAction

**Line:** 749166

**Values:**

```
Insert = 0
Remove = 1
Change = 2
```

---

#### XmlNodeType

**Line:** 752428

**Values:**

```
None = 0
Element = 1
Attribute = 2
Text = 3
CDATA = 4
EntityReference = 5
Entity = 6
ProcessingInstruction = 7
Comment = 8
Document = 9
DocumentType = 10
DocumentFragment = 11
Notation = 12
Whitespace = 13
SignificantWhitespace = 14
EndElement = 15
EndEntity = 16
XmlDeclaration = 17
```

---

#### XmlOutputMethod

**Line:** 747041

**Values:**

```
Xml = 0
Html = 1
Text = 2
AutoDetect = 3
```

---

#### XmlReadMode

**Line:** 1089660

**Values:**

```
Auto = 0
ReadSchema = 1
IgnoreSchema = 2
InferSchema = 3
DiffGram = 4
Fragment = 5
InferTypedSchema = 6
```

---

#### XmlSchemaContentProcessing

**Line:** 764673

**Values:**

```
None = 0
Skip = 1
Lax = 2
Strict = 3
```

---

#### XmlSchemaContentType

**Line:** 764688

**Values:**

```
TextOnly = 0
Empty = 1
ElementOnly = 2
Mixed = 3
```

---

#### XmlSchemaDatatypeVariety

**Line:** 757580

**Values:**

```
Atomic = 0
List = 1
Union = 2
```

---

#### XmlSchemaDerivationMethod

**Line:** 764809

**Values:**

```
Empty = 0
Substitution = 1
Extension = 2
Restriction = 4
List = 8
Union = 16
All = 255
None = 256
```

---

#### XmlSchemaForm

**Line:** 765442

**Values:**

```
None = 0
Qualified = 1
Unqualified = 2
```

---

#### XmlSchemaInference

**Line:** 760315

---

#### XmlSchemaUse

**Line:** 767108

**Values:**

```
None = 0
Optional = 1
Prohibited = 2
Required = 3
```

---

#### XmlSchemaValidationFlags

**Line:** 767161

**Values:**

```
None = 0
ProcessInlineSchema = 1
ProcessSchemaLocation = 2
ReportValidationWarnings = 4
ProcessIdentityConstraints = 8
AllowXmlAttributes = 16
```

---

#### XmlSchemaValidity

**Line:** 767553

**Values:**

```
NotKnown = 0
Valid = 1
Invalid = 2
```

---

#### XmlSeverityType

**Line:** 767563

**Values:**

```
Error = 0
Warning = 1
```

---

#### XmlSpace

**Line:** 743707

**Values:**

```
None = 0
Default = 1
Preserve = 2
```

---

#### XmlTokenizedType

**Line:** 751258

**Values:**

```
CDATA = 0
ID = 1
IDREF = 2
IDREFS = 3
ENTITY = 4
ENTITIES = 5
NMTOKEN = 6
NMTOKENS = 7
NOTATION = 8
ENUMERATION = 9
QName = 10
NCName = 11
None = 12
```

---

#### XmlTypeCode

**Line:** 767572

**Values:**

```
None = 0
Item = 1
Node = 2
Document = 3
Element = 4
Attribute = 5
Namespace = 6
ProcessingInstruction = 7
Comment = 8
Text = 9
AnyAtomicType = 10
UntypedAtomic = 11
String = 12
Boolean = 13
Decimal = 14
Float = 15
Double = 16
Duration = 17
DateTime = 18
Time = 19
Date = 20
GYearMonth = 21
GYear = 22
GMonthDay = 23
GDay = 24
GMonth = 25
HexBinary = 26
Base64Binary = 27
AnyUri = 28
QName = 29
Notation = 30
NormalizedString = 31
Token = 32
Language = 33
NmToken = 34
Name = 35
NCName = 36
Id = 37
Idref = 38
Entity = 39
Integer = 40
NonPositiveInteger = 41
NegativeInteger = 42
Long = 43
Int = 44
Short = 45
Byte = 46
NonNegativeInteger = 47
UnsignedLong = 48
UnsignedInt = 49
UnsignedShort = 50
UnsignedByte = 51
PositiveInteger = 52
YearMonthDuration = 53
DayTimeDuration = 54
```

---

#### XmlWriteMode

**Line:** 1089804

**Values:**

```
WriteSchema = 0
IgnoreSchema = 1
DiffGram = 2
```

---

#### XsdDuration

**Line:** 769744

---

#### ZoneEqualityComparer

**Line:** 1149828

---

#### math

**Line:** 920422

---

### Classes

#### AbstractEventData

**Line:** 1359122

**Fields:**

```
m_Used: bool
```

---

#### AbstractTypeDeserializationFailureInfo

**Line:** 573472

---

#### Action

**Line:** 1230240

---

#### AdaptiveIconsInfo

**Line:** 1325207

**Inherits:** IMetadata

**Fields:**

```
m_Adaptive_idpi: AdaptiveIcon
m_Adaptive_mdpi: AdaptiveIcon
m_Adaptive_hdpi: AdaptiveIcon
m_Adaptive_xhdpi: AdaptiveIcon
m_Adaptive_xxhdpi: AdaptiveIcon
m_Adaptive_xxxhdpi: AdaptiveIcon
AdaptiveIcons: List<AdaptiveIcon>
```

---

#### AdditionalConsentModeData

**Line:** 1564988

**Fields:**

```
acString: string
adTechProviders: List<AdTechProvider>
```

---

#### AdditionalMessageData

**Line:** 595236

---

#### AgeGateConfig

**Line:** 739031

**Inherits:** ScriptableObject

**Fields:**

```
SettingsPerCountryCode: SerializableDictionary<string, AgeGateSettings>
DefaultSettings: AgeGateSettings
```

---

#### AgeVisualConfig

**Line:** 711394

**Inherits:** ScriptableObject

**Fields:**

```
Name: string
Color: Color
ItemBackground: ItemBackgroundView
Icon: Sprite
MapElementViews: List<MapElementView>
MapBackgroundColor: Color
```

---

#### AnalyticsSessionInfo

**Line:** 1585352

---

#### AndroidAssetPackInfo

**Line:** 1487143

---

#### AndroidAssetPackState

**Line:** 1487175

---

#### AndroidNotificationIntentData

**Line:** 1553385

---

#### AnimationState

**Line:** 1575325

**Inherits:** TrackedReference

---

#### AppInfo

**Line:** 1325148

**Inherits:** IMetadata

**Fields:**

```
m_DisplayName: LocalizedString
```

---

#### AppUpdateInfo

**Line:** 1578785

---

#### AsnEncodedData

**Line:** 778834

**Fields:**

```
_oid: Oid
```

---

#### AttributeInfo

**Line:** 1584000

---

#### AxisEventData

**Line:** 1359087

**Inherits:** BaseEventData

---

#### BaseConfig

**Line:** 1059158

**Inherits:** GameConfigKeyValue

---

#### BaseEventData

**Line:** 1359146

**Inherits:** AbstractEventData

---

#### BiomeSfxConfig

**Line:** 705622

**Inherits:** ScriptableObject

---

#### CCPAData

**Line:** 1564835

**Fields:**

```
version: int
noticeGiven: bool
optedOut: bool
lspact: bool
uspString: string
```

---

#### CacheInitializationData

**Line:** 1457028

**Fields:**

```
m_CompressionEnabled: bool
m_CacheDirectoryOverride: string
m_LimitCacheSize: bool
m_MaximumCacheSize: long
```

---

#### CandlestickData

**Line:** 1388344

**Inherits:** IDirectResponseSchema

---

#### CellData

**Line:** 1388500

**Inherits:** IDirectResponseSchema

---

#### ChangeSkinVisibilityAction

**Line:** 1075657

**Inherits:** PlayerAction

---

#### ChartData

**Line:** 1388944

**Inherits:** IDirectResponseSchema

---

#### ChatBlockUserAction

**Line:** 1058802

**Inherits:** PlayerAction

---

#### ChatInitializeAction

**Line:** 1058781

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Token: string
ChannelId: string
```

---

#### ChatModel

**Line:** 1058907

---

#### ChatOnboardingAction

**Line:** 1059035

**Inherits:** PlayerAction

**Fields:**

```
IsUnderAge: bool
```

---

#### ChatUnblockUserAction

**Line:** 1058833

**Inherits:** PlayerAction

---

#### CheatModel

**Line:** 1056432

---

#### CityInfo

**Line:** 538759

**Inherits:** IEquatable

---

#### ClientBuildData

**Line:** 1305084

**Inherits:** IMetaIntegrationSingleton

---

#### ClientGameConfigBuildApiConfig

**Line:** 577145

---

#### ClientLoggingConfig

**Line:** 577118

**Fields:**

```
LogLevel: LogLevel
```

---

#### ClientPlayerModelJournal

**Line:** 576551

**Inherits:** ModelJournal

---

#### CmpData

**Line:** 1564944

**Fields:**

```
activeVariant: UsercentricsVariant
publishedApps: List<PublishedApp>
userLocation: UsercentricsLocation
```

---

#### CompareInfo

**Line:** 271134

**Inherits:** IDeserializationCallback

**Fields:**

```
m_name: string
_sortName: string
m_SortVersion: SortVersion
culture: int
collator: ISimpleCollator
```

---

#### ConnectionConfig

**Line:** 1306704

**Fields:**

```
ConnectAttemptsMaxCount: int
ConnectAttemptInterval: TimeSpan
SessionResumptionAttemptMaxDuration: TimeSpan
MaxSessionRetainingPauseDuration: TimeSpan
MaxSessionRetainingFrameDuration: TimeSpan
MaxNonErrorMaskingPauseDuration: TimeSpan
ConnectTimeout: TimeSpan
ServerIdentifyTimeout: TimeSpan
ServerSessionInitTimeout: TimeSpan
ConfigFetchAttemptsMaxCount: int
ConfigFetchTimeout: TimeSpan
CloseFlushTimeout: TimeSpan
ServerStatusHintCheckDelay: TimeSpan
ServerStatusHintConnectTimeout: TimeSpan
SessionPingPongDurationIncidentThreshold: TimeSpan
MaxSessionPingPongDurationIncidentsPerSession: int
```

---

#### ConnectionEndpointConfig

**Line:** 577062

**Fields:**

```
ServerHost: string
ServerPort: int
ServerPortForWebSocket: int
EnableTls: bool
CdnBaseUrl: string
PublicWebApiUrl: string
```

---

#### ConnectionGameConfigInfo

**Line:** 1306817

---

#### ConnectionState

**Line:** 1306671

---

#### ConsentData

**Line:** 738637

---

#### ConstructorInfo

**Line:** 265202

**Inherits:** MethodBase

---

#### ContentCatalogData

**Line:** 1456684

**Fields:**

```
LocalHash: string
location: IResourceLocation
m_LocatorId: string
m_BuildResultHash: string
m_InstanceProviderData: ObjectInitializationData
m_SceneProviderData: ObjectInitializationData
m_ResourceProviderData: List<ObjectInitializationData>
m_Entries: IList<ContentCatalogDataEntry>
```

---

#### ContextInfo

**Line:** 1547889

---

#### CoordinatesInfo

**Line:** 538815

**Inherits:** IEquatable

---

#### CountryComplianceLibrary

**Line:** 1059116

**Inherits:** IGameConfigData

---

#### CryptoConfig

**Line:** 219623

---

#### CultureInfo

**Line:** 274671

**Inherits:** ICloneable

**Fields:**

```
m_isReadOnly: bool
cultureID: int
parent_lcid: int
datetime_index: int
number_index: int
default_calendar_type: int
m_useUserOverride: bool
numInfo: NumberFormatInfo
dateTimeInfo: DateTimeFormatInfo
textInfo: TextInfo
m_name: string
englishname: string
nativename: string
iso3lang: string
iso2lang: string
win3lang: string
territory: string
compareInfo: CompareInfo
m_dataItem: int
calendar: Calendar
parent_culture: CultureInfo
constructed: bool
m_cultureData: CultureData
m_isInherited: bool
```

---

#### CustomAttributeData

**Line:** 268010

**Fields:**

```
ctorInfo: ConstructorInfo
ctorArgs: IList<CustomAttributeTypedArgument>
namedArgs: IList<CustomAttributeNamedArgument>
```

---

#### CustomMessageData

**Line:** 1057958

---

#### DailyDealConfig

**Line:** 1066810

---

#### DailyDealLibrary

**Line:** 1066768

**Inherits:** IGameConfigData

---

#### DailyDealModel

**Line:** 1066864

---

#### DailyScoreData

**Line:** 1066038

---

#### DateTimeFormatInfo

**Line:** 271484

**Inherits:** IFormatProvider

**Fields:**

```
_cultureData: CultureData
_name: string
_langName: string
_compareInfo: CompareInfo
_cultureInfo: CultureInfo
amDesignator: string
pmDesignator: string
dateSeparator: string
generalShortTimePattern: string
generalLongTimePattern: string
timeSeparator: string
monthDayPattern: string
dateTimeOffsetPattern: string
calendar: Calendar
firstDayOfWeek: int
calendarWeekRule: int
fullDateTimePattern: string
longDatePattern: string
shortDatePattern: string
yearMonthPattern: string
longTimePattern: string
shortTimePattern: string
_isReadOnly: bool
formatFlags: DateTimeFormatFlags
_fullTimeSpanPositivePattern: string
_fullTimeSpanNegativePattern: string
```

---

#### DebugDisplaySettingsStats

**Line:** 811760

---

#### DebugDisplayStats

**Line:** 812311

**Fields:**

```
m_TimeSinceLastAvgValue: float
m_AccumulatedFrames: int
m_HiddenProfileIds: HashSet<TProfileId>
averageProfilerTimingsOverASecond: bool
hideEmptyScopes: bool
```

---

#### DeduplicatingGameConfigLibrary

**Line:** 590226

---

#### DefaultInAppProductInfo

**Line:** 584354

**Inherits:** InAppProductInfoBase

---

#### DefaultMetaOfferGroupInfo

**Line:** 544979

**Inherits:** MetaOfferGroupInfoBase

---

#### DefaultMetaOfferGroupModel

**Line:** 544560

**Inherits:** MetaOfferGroupModelBase

---

#### DefaultMetaOfferInfo

**Line:** 545332

**Inherits:** MetaOfferInfoBase

---

#### DefaultMetaOfferPerGroupState

**Line:** 543820

**Inherits:** MetaOfferPerGroupStateBase

---

#### DefaultMetaOfferPerPlayerState

**Line:** 543830

**Inherits:** MetaOfferPerPlayerStateBase

---

#### DefaultPersistedOfflineState

**Line:** 1305481

---

#### DefaultPlayerClientContext

**Line:** 576913

**Inherits:** IPlayerClientContext

**Fields:**

```
_log: LogChannel
_playerId: EntityId
_sendMessageToServer: Func<MetaMessage, bool>
_checksumGranularity: ChecksumGranularity
_startTime: MetaTime
_currentTime: MetaTime
_timeSinceLastTick: MetaDuration
_actionsLastFlushedAt: MetaTime
_lastFlushedOperationsAt: JournalPosition
_markers: MetaDictionary<JournalPosition, DefaultPlayerClientContext.ActionMarker>
_runningActionId: int
_logicVersion: int
_playerJournal: ClientPlayerModelJournal
_isDisconnected: bool
_operationsBuffer: List<PlayerFlushActions.Operation>
_checksumsBuffer: List<uint>
_actionTypesDebugBuffer: List<Type>
```

---

#### DefaultPlayerMailItem

**Line:** 561562

**Inherits:** PlayerMailItem

---

#### DefaultPlayerMetaOfferGroupsModel

**Line:** 544577

**Inherits:** PlayerMetaOfferGroupsModelBase

---

#### DefaultPlayerSegmentBasicInfoSourceItem

**Line:** 542525

**Inherits:** PlayerSegmentBasicInfoSourceItemBase

---

#### DefaultPlayerSegmentInfo

**Line:** 542113

**Inherits:** PlayerSegmentInfoBase

---

#### DevOverwritePlayerStateFailure

**Line:** 556005

**Inherits:** MetaResponse

**Fields:**

```
Reason: string
```

---

#### DevOverwritePlayerStateRequest

**Line:** 555977

**Inherits:** MetaRequest

---

#### DevPlayerOverwrite

**Line:** 1304799

**Inherits:** MonoBehaviour

**Fields:**

```
ImportPlayer: string
```

---

#### DirectoryInfo

**Line:** 469395

**Inherits:** FileSystemInfo

---

#### DivisionClientState

**Line:** 1051184

**Inherits:** DivisionClientStateBase

---

#### DivisionDebugAction

**Line:** 566210

**Inherits:** DivisionActionBase

---

#### DivisionEntityClientData

**Line:** 566179

**Inherits:** EntityClientData

---

#### DocumentationInfo

**Line:** 816357

---

#### DynamicEnumTypeInfo

**Line:** 500893

**Fields:**

```
_baseDynamicEnumType: Type
_allValuesList: IList
_nameToValue: Dictionary<string, IDynamicEnum>
_idToValue: Dictionary<int, IDynamicEnum>
```

---

#### EmptyPlayerDivisionModelClientListenerCore

**Line:** 566112

**Inherits:** IPlayerDivisionModelClientListenerCore

---

#### EmptyPlayerDivisionModelServerListenerCore

**Line:** 566131

**Inherits:** IPlayerDivisionModelServerListenerCore

---

#### EmptyPlayerModelClientListener

**Line:** 1073524

**Inherits:** IPlayerModelClientListener

---

#### EmptyPlayerModelClientListenerCore

**Line:** 533335

**Inherits:** IPlayerModelClientListenerCore

---

#### EmptyPlayerModelClientListenerCoreInternal

**Line:** 533317

**Inherits:** IPlayerModelClientListenerCoreInternal

---

#### EmptyPlayerModelServerListener

**Line:** 1073425

**Inherits:** IPlayerModelServerListener

---

#### EmptyPlayerModelServerListenerCore

**Line:** 533257

**Inherits:** IPlayerModelServerListenerCore

---

#### EntityClientData

**Line:** 553293

---

#### EntityClientDebugConfig

**Line:** 576476

---

#### EntityInitialState

**Line:** 553447

---

#### EnvironmentConfig

**Line:** 577155

**Inherits:** IMetaIntegrationConstructible

**Fields:**

```
Version: int
Id: string
DisplayName: string
Description: string
ConnectionEndpointConfig: ConnectionEndpointConfig
ClientLoggingConfig: ClientLoggingConfig
ClientGameConfigBuildApiConfig: ClientGameConfigBuildApiConfig
```

---

#### EquipItemAction

**Line:** 1067522

**Inherits:** PlayerAction

---

#### EquipmentItemInfo

**Line:** 1067592

**Inherits:** IGameConfigData

---

#### EquipmentItemVisualConfig

**Line:** 713646

**Inherits:** ScriptableObject

**Fields:**

```
Icon: Sprite
Prefab: EquipmentItem
```

---

#### ErrorState

**Line:** 1310009

**Inherits:** ConnectionState

---

#### EventInfo

**Line:** 265309

**Inherits:** MemberInfo

---

#### ExceptionDispatchInfo

**Line:** 229949

**Fields:**

```
m_Exception: Exception
m_stackTrace: object
```

---

#### ExitSteppingStonesSceneAction

**Line:** 1079373

**Inherits:** PlayerAction

---

#### ExtendableEventState

**Line:** 578655

**Fields:**

```
LastExtensionStartedAt: Nullable<MetaTime>
LatestActivationNumExtended: int
NumSoftFinalizedInLatestActivation: int
```

---

#### FastAction

**Line:** 1346772

---

#### FieldInfo

**Line:** 265414

**Inherits:** MemberInfo

---

#### FileInfo

**Line:** 469654

**Inherits:** FileSystemInfo

---

#### FileSystemInfo

**Line:** 469753

**Inherits:** MarshalByRefObject

**Fields:**

```
_fileStatus: FileStatus
FullPath: string
OriginalPath: string
_name: string
```

---

#### FontData

**Line:** 1352465

**Inherits:** ISerializationCallbackReceiver

**Fields:**

```
m_Font: Font
m_FontSize: int
m_FontStyle: FontStyle
m_BestFit: bool
m_MinSize: int
m_MaxSize: int
m_Alignment: TextAnchor
m_AlignByGeometry: bool
m_RichText: bool
m_HorizontalOverflow: HorizontalWrapMode
m_VerticalOverflow: VerticalWrapMode
m_LineSpacing: float
```

---

#### FormattingInfo

**Line:** 1323414

**Inherits:** IFormattingInfo

---

#### FullEquipCheatAction

**Line:** 1068632

**Inherits:** PlayerAction

---

#### FullGameConfig

**Line:** 591728

---

#### GUIStyleState

**Line:** 1451698

**Fields:**

```
m_Ptr: IntPtr
```

---

#### GameConfigBuildState

**Line:** 592812

**Fields:**

```
_builder: GameConfigBuildState<TConfig>
```

---

#### GameConfigEntryInfo

**Line:** 598495

---

#### GameConfigLibrary

**Line:** 588842

**Fields:**

```
_aliasToRealKey: MetaDictionary<object, object>
```

---

#### GameConfigMetaData

**Line:** 591606

**Fields:**

```
BuildSourceMetadata: MetaDictionary<string, GameConfigBuildSourceMetadata>
```

---

#### GameConfigParseKeyValuePipelineConfig

**Line:** 597240

---

#### GameConfigParseLibraryPipelineConfig

**Line:** 597227

---

#### GameConfigRepositoryConfig

**Line:** 598591

---

#### GameConfigRepositoryData

**Line:** 598655

**Inherits:** IGeneratedData

---

#### GameConfigSourceInfo

**Line:** 598723

---

#### GameConfigSpreadsheetSourceInfo

**Line:** 598744

**Inherits:** GameConfigSourceInfo

---

#### GameConfigTypeInfo

**Line:** 598454

---

#### GameEngineRuntimeInfo

**Line:** 572210

---

#### GamePauseAction

**Line:** 1056818

**Inherits:** PlayerAction

---

#### GameUnPauseAction

**Line:** 1056831

**Inherits:** PlayerAction

---

#### GenderChangeAction

**Line:** 1052001

**Inherits:** PlayerAction

---

#### GeneratedClientBuildData

**Line:** 704887

**Inherits:** ClientBuildData

---

#### GetPlayerInfoRequest

**Line:** 1074118

**Inherits:** MetaRequest

---

#### GetPlayerInfoResponse

**Line:** 1074146

**Inherits:** MetaResponse

---

#### GoogleSheetSourceInfo

**Line:** 598792

**Inherits:** GameConfigSpreadsheetSourceInfo

---

#### GridData

**Line:** 1393735

**Inherits:** IDirectResponseSchema

---

#### HierarchyViewModel

**Line:** 1562910

**Inherits:** IDisposable

**Fields:**

```
m_Ptr: IntPtr
m_NodesPtr: IntPtr
m_NodesCount: int
m_Version: int
```

---

#### IAPFakeStoreConfig

**Line:** 1312555

**Inherits:** ScriptableObject

**Fields:**

```
LocalizedPriceStringFormat: string
IsoCurrencyCode: string
InitIsSynchronous: bool
AsyncInitDelay: float
ForceInitFailure: bool
DisabledProductIds: List<string>
PurchaseIsSynchronous: bool
AsyncPurchaseDelay: float
ForcePurchaseFailure: bool
UseFixedTransactionId: bool
FixedTransactionId: string
ForceIllFormedReceipt: bool
ForceInvalidSignature: bool
ValidationDelay: float
ValidationTransientErrorProbability: float
PretendSubscriptionIsFamilyShared: bool
IgnorePurchaseConfirmation: bool
```

---

#### IconChangeAction

**Line:** 1052032

**Inherits:** PlayerAction

---

#### InAppProductInfo

**Line:** 1051158

**Inherits:** InAppProductInfoBase

---

#### InAppPurchaseEventPlatformState

**Line:** 586376

---

#### InAppPurchaseEventRefundState

**Line:** 584444

---

#### InAppPurchaseRefundData

**Line:** 584516

---

#### InAppPurchaseTransactionInfo

**Line:** 585013

---

#### IncidentApplicationInfo

**Line:** 574481

---

#### IncidentDashboardInfo

**Line:** 575813

---

#### IncidentGameConfigInfo

**Line:** 574460

**Fields:**

```
SharedConfigBaselineVersion: ContentHash
SharedConfigPatchesVersion: ContentHash
```

---

#### IntegrationConfig

**Line:** 502833

---

#### InvalidPKCS7Data

**Line:** 1545290

**Inherits:** IAPSecurityException

---

#### InvalidRSAData

**Line:** 1545347

**Inherits:** IAPSecurityException

---

#### InvalidX509Data

**Line:** 1544948

**Inherits:** IAPSecurityException

---

#### ItemBalancingConfig

**Line:** 1051694

**Inherits:** GameConfigKeyValue

**Fields:**

```
LevelScalingBase: F64
SellBasePrice: F64
PlayerMeleeDamageMultiplier: F64
EnemyRangedDamageMultiplier: F64
PlayerPowerDamageMultiplier: F64
PlayerBaseCritDamage: F64
ItemBaseMaxLevel: F64
```

---

#### JsonParameterInfo

**Line:** 1013007

**Fields:**

```
_attributeProvider: ICustomAttributeProvider
```

---

#### JsonPropertyInfo

**Line:** 1013433

**Fields:**

```
_effectiveConverter: JsonConverter
_customConverter: JsonConverter
_untypedGet: Func<object, object>
_untypedSet: Action<object, object>
_isUserSpecifiedSetter: bool
_shouldSerialize: Func<object, object, bool>
_isUserSpecifiedShouldSerialize: bool
_ignoreCondition: Nullable<JsonIgnoreCondition>
AttributeProviderFactory: Func<ICustomAttributeProvider>
_attributeProvider: ICustomAttributeProvider
_objectCreationHandling: Nullable<JsonObjectCreationHandling>
_isGetNullable: bool
_isSetNullable: bool
_isExtensionDataProperty: bool
_isRequired: bool
_name: string
_order: int
_jsonTypeInfo: JsonTypeInfo
_numberHandling: Nullable<JsonNumberHandling>
_index: int
```

---

#### JsonTypeInfo

**Line:** 1017280

**Fields:**

```
_propertyIndex: Dictionary<string, JsonPropertyInfo>
_onSerializing: Action<object>
_onSerialized: Action<object>
_onDeserializing: Action<object>
_onDeserialized: Action<object>
_createObject: Func<object>
_sourceGenDelayedPropertyInitializer: Func<JsonSerializerContext, JsonPropertyInfo[]>
_polymorphismOptions: JsonPolymorphismOptions
_elementTypeInfo: JsonTypeInfo
_keyTypeInfo: JsonTypeInfo
_numberHandling: Nullable<JsonNumberHandling>
_unmappedMemberHandling: Nullable<JsonUnmappedMemberHandling>
_preferredPropertyObjectCreationHandling: Nullable<JsonObjectCreationHandling>
_originatingResolver: IJsonTypeInfoResolver
ConstructorAttributeProviderFactory: Func<ICustomAttributeProvider>
_constructorAttributeProvider: ICustomAttributeProvider
_cachedConfigureError: ExceptionDispatchInfo
_ancestorPolymorhicType: JsonTypeInfo
_isAncestorPolymorphicTypeResolved: bool
_parameterInfoValuesIndex: Dictionary<JsonTypeInfo.ParameterLookupKey, JsonParameterInfoValues>
```

---

#### LanguageInfo

**Line:** 561597

**Inherits:** IGameConfigData

---

#### LegacyIconsInfo

**Line:** 1325355

**Inherits:** IMetadata

**Fields:**

```
m_Legacy_idpi: LocalizedTexture
m_Legacy_mdpi: LocalizedTexture
m_Legacy_hdpi: LocalizedTexture
m_Legacy_xhdpi: LocalizedTexture
m_Legacy_xxhdpi: LocalizedTexture
m_Legacy_xxxhdpi: LocalizedTexture
LegacyIcons: List<LocalizedTexture>
```

---

#### LegacyPlayerAuthEntry

**Line:** 534091

---

#### LegacyPlayerMail

**Line:** 561321

**Inherits:** MetaInGameMail

---

#### LiveOpsEventScheduleInfo

**Line:** 562258

---

#### LiveOpsEventTemplateConfigData

**Line:** 562144

---

#### LocalVariableInfo

**Line:** 268121

**Fields:**

```
type: Type
is_pinned: bool
position: ushort
```

---

#### MainChatUIModel

**Line:** 707178

**Fields:**

```
_currentChatRoomId: string
_subscribedGuildId: string
OnWorldUnreadCount: Action<int>
OnGuildUnreadCount: Action<int>
OnReset: Action
OnChatMessage: Action<ChatItem>
OnChatReaction: Action<long, string, string[]>
```

---

#### ManifestResourceInfo

**Line:** 265609

---

#### MeshWriteData

**Line:** 643445

**Fields:**

```
m_Vertices: NativeSlice<Vertex>
m_Indices: NativeSlice<ushort>
currentIndex: int
currentVertex: int
```

---

#### MessageRoutingRuleOwnedPlayer

**Line:** 499042

**Inherits:** MessageRoutingRule

---

#### MetaActivableRepositoryConfig

**Line:** 579551

---

#### MetaActivableState

**Line:** 581586

---

#### MetaOfferPerPlayerStateBase

**Line:** 543742

---

#### MetaSerializerTypeInfo

**Line:** 530579

**Fields:**

```
Specs: MetaDictionary<Type, MetaSerializableType>
FullTypeHash: uint
```

---

#### MetaplayClientCreatePlayerContextFunc

**Line:** 1313826

**Inherits:** MulticastDelegate

---

#### MetaplayClientState

**Line:** 1313917

**Inherits:** ISessionContextProvider

**Fields:**

```
_hasHandledCurrentConnectionError: bool
_hasHadSessionForCurrentConnection: bool
_pendingSessionFuncs: Queue<Action>
_clientServices: MetaplayUnitySubClientServices
```

---

#### MethodInfo

**Line:** 265923

**Inherits:** MethodBase

---

#### MiniGameState

**Line:** 1079570

**Fields:**

```
EndReason: Nullable<SteppingStoneEndReason>
```

---

#### ModelAction

**Line:** 601532

---

#### MonoTlsConnectionInfo

**Line:** 1448891

---

#### NextDayModel

**Line:** 1078105

**Inherits:** ITickable

---

#### NextDayTriggerCheatAction

**Line:** 1078147

**Inherits:** PlayerAction

---

#### NoopAction

**Line:** 604083

**Inherits:** ModelAction

---

#### NumberFormatInfo

**Line:** 273554

**Inherits:** ICloneable

**Fields:**

```
positiveSign: string
negativeSign: string
numberDecimalSeparator: string
numberGroupSeparator: string
currencyGroupSeparator: string
currencyDecimalSeparator: string
currencySymbol: string
ansiCurrencySymbol: string
nanSymbol: string
positiveInfinitySymbol: string
negativeInfinitySymbol: string
percentDecimalSeparator: string
percentGroupSeparator: string
percentSymbol: string
perMilleSymbol: string
m_dataItem: int
numberDecimalDigits: int
currencyDecimalDigits: int
currencyPositivePattern: int
currencyNegativePattern: int
numberNegativePattern: int
percentPositivePattern: int
percentNegativePattern: int
percentDecimalDigits: int
digitSubstitution: int
isReadOnly: bool
m_useUserOverride: bool
m_isInvariant: bool
validForParseAsNumber: bool
validForParseAsCurrency: bool
```

---

#### ParallelLoopState

**Line:** 191353

---

#### ParameterInfo

**Line:** 266089

**Inherits:** ICustomAttributeProvider

**Fields:**

```
AttrsImpl: ParameterAttributes
ClassImpl: Type
DefaultValueImpl: object
MemberImpl: MemberInfo
NameImpl: string
PositionImpl: int
```

---

#### PlayerAckActions

**Line:** 538068

**Inherits:** MetaMessage

---

#### PlayerAckIncidentReportUpload

**Line:** 576205

**Inherits:** MetaMessage

---

#### PlayerAction

**Line:** 1072348

**Inherits:** PlayerActionCore

---

#### PlayerActionBase

**Line:** 534274

**Inherits:** ModelAction

---

#### PlayerActionCore

**Line:** 534284

---

#### PlayerAddFirebaseMessagingToken

**Line:** 543110

**Inherits:** PlayerActionCore

---

#### PlayerAddHistoricalDivisionEntry

**Line:** 565290

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerAddLiveOpsEvent

**Line:** 562883

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerAddMail

**Line:** 534578

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerAddNft

**Line:** 582104

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Nft: MetaNft
```

---

#### PlayerAttachAuthentication

**Line:** 543391

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerAuthEntryBase

**Line:** 534448

---

#### PlayerAvailableIncidentReports

**Line:** 576106

**Inherits:** MetaMessage

---

#### PlayerBanInfo

**Line:** 534495

---

#### PlayerCancelNftTransaction

**Line:** 582480

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Transaction: PlayerNftTransaction
```

---

#### PlayerCancelScheduledDeletionRequest

**Line:** 538159

**Inherits:** MetaMessage

---

#### PlayerChangeLanguage

**Line:** 534848

**Inherits:** PlayerActionCore

---

#### PlayerChangeName

**Line:** 534921

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerChangeOwnNameRequest

**Line:** 538119

**Inherits:** MetaMessage

---

#### PlayerChatProfile

**Line:** 1057851

---

#### PlayerChecksumMismatch

**Line:** 537834

**Inherits:** MetaMessage

---

#### PlayerChecksumMismatchConnectionError

**Line:** 1314383

**Inherits:** TransientError

**Fields:**

```
TickNumber: long
Action: PlayerActionBase
ModelDiff: string
VagueDifferencePathsMaybe: List<string>
```

---

#### PlayerChecksumMismatchDetails

**Line:** 537885

**Inherits:** MetaMessage

---

#### PlayerClaimPendingInAppPurchase

**Line:** 585350

**Inherits:** PlayerActionCore

---

#### PlayerClearLiveOpsEventUpdates

**Line:** 563119

**Inherits:** PlayerActionCore

---

#### PlayerClearPendingDuplicateInAppPurchase

**Line:** 585381

**Inherits:** PlayerActionCore

---

#### PlayerCompanyAccountAuthEntry

**Line:** 534530

**Inherits:** PlayerAuthEntryBase

---

#### PlayerCondition

**Line:** 534543

---

#### PlayerConfirmPendingDynamicPurchaseContent

**Line:** 583797

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerConfirmPendingNonDynamicPurchaseAnalyticsContext

**Line:** 585948

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerConnection

**Line:** 890576

**Inherits:** ScriptableObject

**Fields:**

```
m_PlayerEditorConnectionEvents: PlayerEditorConnectionEvents
m_connectedPlayers: List<int>
m_IsInitilized: bool
```

---

#### PlayerConsumeMail

**Line:** 534656

**Inherits:** PlayerActionCore

---

#### PlayerDailyDealsModel

**Line:** 1067017

**Inherits:** INextDayListener

---

#### PlayerDashboardActionAttribute

**Line:** 601213

**Inherits:** Attribute

---

#### PlayerDashboardActionAuditLogPayloadCore

**Line:** 534395

**Inherits:** PlayerEventPayloadBase

---

#### PlayerDebugAddMailToSelf

**Line:** 534625

**Inherits:** PlayerActionCore

---

#### PlayerDebugConfig

**Line:** 576423

---

#### PlayerDebugForceSetActivablePhase

**Line:** 579177

**Inherits:** PlayerActionCore

**Fields:**

```
KindId: MetaActivableKindId
ActivableIdStr: string
Phase: Nullable<MetaActivableState.DebugPhase>
```

---

#### PlayerDebugRemoveSubscription

**Line:** 586860

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerDeleteMail

**Line:** 534738

**Inherits:** PlayerActionCore

---

#### PlayerDetachAuthentication

**Line:** 543433

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerDeviceEntry

**Line:** 538227

---

#### PlayerDeviceIdAuthEntry

**Line:** 538344

**Inherits:** PlayerAuthEntryBase

---

#### PlayerDevicePushNotifications

**Line:** 543082

**Fields:**

```
FirebaseMessagingToken: string
```

---

#### PlayerDivisionActionBase

**Line:** 565679

**Inherits:** DivisionActionBase

---

#### PlayerDivisionAddOrUpdateParticipant

**Line:** 565695

**Inherits:** PlayerDivisionActionBase

---

#### PlayerDivisionAvatarBase

**Line:** 565811

---

#### PlayerDivisionConcludedMessage

**Line:** 1055921

**Inherits:** MetaMessage

---

#### PlayerDivisionHistoryEntry

**Line:** 1051194

**Inherits:** PlayerDivisionHistoryEntryBase

---

#### PlayerDivisionHistoryEntryBase

**Line:** 565574

**Inherits:** IDivisionHistoryEntry

---

#### PlayerDivisionMatchEvent

**Line:** 1051247

**Inherits:** DivisionScoreEventBase

---

#### PlayerDivisionModel

**Line:** 1051369

**Inherits:** PlayerDivisionModelBase

---

#### PlayerDivisionModelBase

**Line:** 565956

**Fields:**

```
_BackingField_ServerListenerCore: IPlayerDivisionModelServerListenerCore
_BackingField_ClientListenerCore: IPlayerDivisionModelClientListenerCore
```

---

#### PlayerDivisionParticipantConclusionResultBase

**Line:** 563758

---

#### PlayerDivisionParticipantState

**Line:** 1051315

**Inherits:** PlayerDivisionParticipantStateBase

---

#### PlayerDivisionParticipantStateBase

**Line:** 565821

---

#### PlayerDivisionScore

**Line:** 1051401

**Inherits:** IDivisionScore

**Fields:**

```
Stars: int
LastActionAt: MetaTime
OldTotalPower: long
TotalPower: UInt128
```

---

#### PlayerDivisionUpdateContribution

**Line:** 565749

**Inherits:** PlayerDivisionActionBase

---

#### PlayerEditorConnectionEvents

**Line:** 890676

**Fields:**

```
m_messageTypeId: string
subscriberCount: int
```

---

#### PlayerEnqueueSynchronizedServerAction

**Line:** 542772

**Inherits:** MetaMessage

---

#### PlayerEquipmentModel

**Line:** 1067881

---

#### PlayerEventActorCrashed

**Line:** 537280

**Inherits:** PlayerEventBase

---

#### PlayerEventAppStartPerformance

**Line:** 537361

**Inherits:** PlayerEventBase

---

#### PlayerEventBase

**Line:** 538386

**Inherits:** EntityEventBase

---

#### PlayerEventClientConnected

**Line:** 535400

**Inherits:** PlayerEventBase

---

#### PlayerEventClientDisconnected

**Line:** 535532

**Inherits:** PlayerEventBase

---

#### PlayerEventDeleted

**Line:** 537126

**Inherits:** PlayerEventBase

---

#### PlayerEventDeserializationFailureSubstitute

**Line:** 535007

**Inherits:** PlayerEventBase

---

#### PlayerEventFacebookAuthenticationRevoked

**Line:** 535272

**Inherits:** PlayerEventBase

---

#### PlayerEventIAPSubscriptionDisabledDueToReuse

**Line:** 536990

**Inherits:** PlayerEventBase

---

#### PlayerEventIAPSubscriptionStateUpdated

**Line:** 536907

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseAbandoned

**Line:** 536477

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseClientRefused

**Line:** 536024

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseHandledByClient

**Line:** 536333

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseInitiated

**Line:** 536202

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseInitiationStarted

**Line:** 536095

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseRefunded

**Line:** 536751

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchaseRestored

**Line:** 536620

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppPurchased

**Line:** 535578

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppValidationComplete

**Line:** 535881

**Inherits:** PlayerEventBase

---

#### PlayerEventInAppValidationStarted

**Line:** 535748

**Inherits:** PlayerEventBase

---

#### PlayerEventIncidentRecorded

**Line:** 537187

**Inherits:** PlayerEventBase

---

#### PlayerEventLiveOpsEventAdded

**Line:** 537451

**Inherits:** PlayerEventBase

---

#### PlayerEventLiveOpsEventParamsChanged

**Line:** 537729

**Inherits:** PlayerEventBase

---

#### PlayerEventLiveOpsEventPhaseChanged

**Line:** 537602

**Inherits:** PlayerEventBase

---

#### PlayerEventLog

**Line:** 538396

**Inherits:** EntityEventLog

---

#### PlayerEventLogEntry

**Line:** 538373

**Inherits:** EntityEventLogEntry

---

#### PlayerEventMainGameProgress

**Line:** 1073754

**Inherits:** PlayerEventBase

---

#### PlayerEventModelSchemaMigrated

**Line:** 537142

**Inherits:** PlayerEventBase

---

#### PlayerEventNameChanged

**Line:** 535050

**Inherits:** PlayerEventBase

---

#### PlayerEventPayloadBase

**Line:** 578596

**Inherits:** EventPayloadBase

---

#### PlayerEventPendingDynamicPurchaseContentAssigned

**Line:** 535108

**Inherits:** PlayerEventBase

---

#### PlayerEventPendingStaticPurchaseContextAssigned

**Line:** 535192

**Inherits:** PlayerEventBase

---

#### PlayerEventSocialAuthConflictResolved

**Line:** 535330

**Inherits:** PlayerEventBase

---

#### PlayerExecuteNftTransaction

**Line:** 582441

**Inherits:** PlayerUnsynchronizedServerActionCore

**Fields:**

```
Transaction: PlayerNftTransaction
Nfts: MetaDictionary<NftKey, MetaNft>
```

---

#### PlayerExecuteUnsynchronizedServerAction

**Line:** 542929

**Inherits:** MetaMessage

---

#### PlayerFinalizeNftTransaction

**Line:** 582461

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Transaction: PlayerNftTransaction
```

---

#### PlayerFlushActions

**Line:** 538015

**Inherits:** MetaMessage

---

#### PlayerForceDeleteMail

**Line:** 534778

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerGenderDisplay

**Line:** 726007

**Inherits:** UiUnityView

**Fields:**

```
Gender: TMP_Text
_gender: PlayerGender
```

---

#### PlayerGlobalLeaderboardModel

**Line:** 1067223

**Fields:**

```
MinPowerTop: long
```

---

#### PlayerHandleInAppPurchaseRefund

**Line:** 585508

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerHandleInAppPurchaseRefundLegacy

**Line:** 585454

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerHandleJoinRequest

**Line:** 1063725

**Inherits:** MetaRequest

**Fields:**

```
PlayerId: EntityId
Approved: bool
```

---

#### PlayerHandleJoinResponse

**Line:** 1063760

**Inherits:** MetaResponse

---

#### PlayerIconVisual

**Line:** 726083

**Inherits:** MonoBehaviour

**Fields:**

```
Icon: Image
SelectIcon: GameObject
Button: UnityButton
_id: int
```

---

#### PlayerIconsConfig

**Line:** 725923

**Inherits:** ScriptableObject

**Fields:**

```
Icons: List<Sprite>
AdminIcon: Sprite
```

---

#### PlayerInAppPurchaseClientRefused

**Line:** 585412

**Inherits:** PlayerActionCore

---

#### PlayerInAppPurchaseValidated

**Line:** 585228

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerInAppPurchased

**Line:** 585194

**Inherits:** PlayerActionCore

---

#### PlayerIncidentReport

**Line:** 575524

---

#### PlayerIncidentUploadUrlRequest

**Line:** 576234

**Inherits:** MetaMessage

---

#### PlayerIncidentUploadUrlResponse

**Line:** 576284

**Inherits:** MetaMessage

---

#### PlayerIncidentUtil

**Line:** 575997

---

#### PlayerInfo

**Line:** 1072573

**Inherits:** IPlayerInfo

---

#### PlayerInitiateServerDrivenPurchase

**Line:** 586070

**Inherits:** PlayerActionCore

---

#### PlayerItemModel

**Line:** 1068034

---

#### PlayerLastDivisionModel

**Line:** 1056239

**Inherits:** INextDayListener

**Fields:**

```
LastDivisionLeaderboard: MetaDictionary<int, PlayerDivisionParticipantState>
LastDivisionIndex: DivisionIndex
OwnIndex: int
NextDivisionTime: MetaTime
PromotionDisplayed: int
ArenaRewardTutorialDisplayed: bool
```

---

#### PlayerLeaderboardEntry

**Line:** 1067133

**Inherits:** ILeaderboardEntry

---

#### PlayerLiveOpsEventInfo

**Line:** 562216

---

#### PlayerLiveOpsEventModel

**Line:** 562449

---

#### PlayerLiveOpsEventServerOnlyModel

**Line:** 562803

---

#### PlayerLiveOpsEventsModel

**Line:** 562715

---

#### PlayerLiveOpsEventsServerOnlyModel

**Line:** 562765

---

#### PlayerLoginEvent

**Line:** 538884

---

#### PlayerLoop

**Line:** 889021

---

#### PlayerLoopTimer

**Line:** 1099485

**Inherits:** IDisposable

**Fields:**

```
isRunning: bool
tryStop: bool
isDisposed: bool
```

---

#### PlayerMailItem

**Line:** 561463

**Fields:**

```
_contents: MetaInGameMail
```

---

#### PlayerMeleeOnlyStatTarget

**Line:** 1076864

**Inherits:** StatTargetBase

---

#### PlayerMetaOfferGroupsModelBase

**Line:** 544305

---

#### PlayerMiscSavegame

**Line:** 1070076

**Fields:**

```
InstallDate: MetaTime
InstallVersion: string
HasRated: bool
PlayerAge: int
PlayerCountry: string
```

---

#### PlayerModel

**Line:** 1072724

**Inherits:** PlayerModelBase

**Fields:**

```
RegionalOffset: MetaDuration
_tickables: List<ITickable>
_nextDayListeners: List<INextDayListener>
```

---

#### PlayerModelBase

**Line:** 541466

---

#### PlayerModelRuntimeDataBase

**Line:** 541504

---

#### PlayerModelSessionInitAction

**Line:** 1078345

**Inherits:** PlayerAction

---

#### PlayerNameChangeActionConfirmed

**Line:** 1052106

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerNameChangeRequest

**Line:** 1052074

**Inherits:** MetaRequest

**Fields:**

```
UpdatedName: string
```

---

#### PlayerNameChangeResponse

**Line:** 1052090

**Inherits:** MetaResponse

**Fields:**

```
Error: string
```

---

#### PlayerNameInputValidator

**Line:** 725962

**Inherits:** TMP_InputValidator

---

#### PlayerNftSubModel

**Line:** 582723

---

#### PlayerNftTransaction

**Line:** 582399

---

#### PlayerNftTransactionRequest

**Line:** 582425

**Inherits:** MetaMessage

**Fields:**

```
Transaction: PlayerNftTransaction
```

---

#### PlayerNftTransactionState

**Line:** 582761

---

#### PlayerPendingSynchronizedServerActions

**Line:** 533365

---

#### PlayerPowerModel

**Line:** 1076265

---

#### PlayerPrefLocaleSelector

**Line:** 1319448

**Inherits:** IStartupLocaleSelector

**Fields:**

```
m_PlayerPreferenceKey: string
```

---

#### PlayerPrefs

**Line:** 880699

---

#### PlayerPrefsException

**Line:** 880689

**Inherits:** Exception

---

#### PlayerPrefsFeature

**Line:** 693727

**Inherits:** Feature

---

#### PlayerPreparePurchaseContext

**Line:** 585895

**Inherits:** PlayerActionCore

---

#### PlayerPreparePurchaseMetaOffer

**Line:** 543880

**Inherits:** PlayerActionCore

---

#### PlayerProfileModel

**Line:** 1052137

---

#### PlayerProfileResponseAction

**Line:** 1058637

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Profile: PlayerPvpProfileModel
```

---

#### PlayerProfileTestModel

**Line:** 1058655

---

#### PlayerProgressModel

**Line:** 1073811

---

#### PlayerPropertyConstant

**Line:** 541927

---

#### PlayerPropertyId

**Line:** 541563

---

#### PlayerPropertyIdParser

**Line:** 1079325

**Inherits:** ConfigParserProvider

---

#### PlayerPropertyIdTotalIapSpend

**Line:** 1079341

**Inherits:** TypedPlayerPropertyId

---

#### PlayerPropertyLogicVersion

**Line:** 533067

**Inherits:** TypedPlayerPropertyId

---

#### PlayerPropertyPlayerbaseSubsetNumber

**Line:** 533086

**Inherits:** TypedPlayerPropertyId

**Fields:**

```
NumSubsets: int
Modifier: uint
```

---

#### PlayerPropertyRequirement

**Line:** 541654

---

#### PlayerPushNotifications

**Line:** 543044

**Fields:**

```
_devices: MetaDictionary<string, PlayerDevicePushNotifications>
```

---

#### PlayerRangedOnlyStatTarget

**Line:** 1076851

**Inherits:** StatTargetBase

---

#### PlayerRefreshMetaOffers

**Line:** 543840

**Inherits:** PlayerActionCore

**Fields:**

```
_partialRefreshInfo: Nullable<MetaOfferGroupsRefreshInfo>
```

---

#### PlayerRemoveNft

**Line:** 582142

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Key: NftKey
```

---

#### PlayerRequestIncidentReportUploads

**Line:** 576134

**Inherits:** MetaMessage

---

#### PlayerRequirementsValidator

**Line:** 542004

**Inherits:** IMetaIntegrationSingleton

---

#### PlayerResourcesModel

**Line:** 1066389

---

#### PlayerRunLiveOpsPhaseSequence

**Line:** 562963

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerScheduleDeletionRequest

**Line:** 538148

**Inherits:** MetaMessage

---

#### PlayerSegmentBasicCondition

**Line:** 542203

**Inherits:** PlayerCondition

---

#### PlayerSegmentBasicInfoSourceItemBase

**Line:** 542290

---

#### PlayerSegmentId

**Line:** 542027

**Inherits:** StringId

---

#### PlayerSegmentInfoBase

**Line:** 542038

**Inherits:** IGameConfigData

---

#### PlayerServerCleanupRemoveFirebaseMessagingToken

**Line:** 543141

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerServerDebugForceSetActivablePhase

**Line:** 579199

**Inherits:** PlayerUnsynchronizedServerActionCore

**Fields:**

```
KindId: MetaActivableKindId
ActivableIdStr: string
Phase: Nullable<MetaActivableState.DebugPhase>
```

---

#### PlayerServerDrivenInAppPurchaseHandledByClient

**Line:** 586260

**Inherits:** PlayerActionCore

---

#### PlayerServerDrivenPurchaseAbandoned

**Line:** 586302

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerServerDrivenPurchaseInitiated

**Line:** 586185

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerServerDrivenPurchaseInitiating

**Line:** 586123

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerServerDrivenPurchaseRestoring

**Line:** 586154

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerSessionDebugMode

**Line:** 542539

**Fields:**

```
parameters: PlayerSessionDebugModeParameters
```

---

#### PlayerSessionDebugModeCounter

**Line:** 542585

**Inherits:** PlayerSessionDebugMode

**Fields:**

```
forNextNumSessions: int
```

---

#### PlayerSessionDebugModeParameters

**Line:** 542566

**Fields:**

```
EnableEntityDebugConfig: bool
IncidentUploadMode: PlayerDebugIncidentUploadMode
```

---

#### PlayerSetCurrentDivision

**Line:** 565236

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerSetIsOnline

**Line:** 534817

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerSetIsScheduledForDeletionAt

**Line:** 534952

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerSetSubscriptionInstanceDisablementDueToReuse

**Line:** 586753

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerSetUnscheduledForDeletion

**Line:** 534994

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerSetsModel

**Line:** 1074654

---

#### PlayerSkinCollectionModel

**Line:** 1076057

---

#### PlayerSkinModel

**Line:** 1076136

**Inherits:** ISetPiece

---

#### PlayerSkinMultiplierStatTarget

**Line:** 1076877

**Inherits:** StatTargetBase

---

#### PlayerStarterPackagesModel

**Line:** 1066542

---

#### PlayerStatTarget

**Line:** 1076838

**Inherits:** StatTargetBase

---

#### PlayerStatistics

**Line:** 1073690

**Inherits:** PlayerStatisticsBase

---

#### PlayerStatisticsBase

**Line:** 542616

---

#### PlayerStatisticsCore

**Line:** 542705

**Inherits:** PlayerStatisticsBase

---

#### PlayerSubClientStateBase

**Line:** 542715

---

#### PlayerSubscriptionsModel

**Line:** 586400

---

#### PlayerSynchronizedServerActionBase

**Line:** 542726

**Inherits:** PlayerActionBase

---

#### PlayerSynchronizedServerActionCore

**Line:** 542735

---

#### PlayerSynchronizedServerActionMarker

**Line:** 542811

**Inherits:** PlayerActionCore

---

#### PlayerTimeZoneInfo

**Line:** 542842

---

#### PlayerToggleMailIsRead

**Line:** 534691

**Inherits:** PlayerActionCore

---

#### PlayerTransactionFinalizingActionBase

**Line:** 534321

**Inherits:** PlayerSynchronizedServerActionBase

---

#### PlayerTransactionFinalizingActionCore

**Line:** 534330

---

#### PlayerUnsynchronizedServerActionBase

**Line:** 542883

**Inherits:** PlayerActionBase

---

#### PlayerUnsynchronizedServerActionCore

**Line:** 542892

---

#### PlayerUnsynchronizedServerActionMarker

**Line:** 542968

**Inherits:** PlayerActionCore

---

#### PlayerUpdateBannedStatus

**Line:** 534890

**Inherits:** PlayerUnsynchronizedServerActionCore

---

#### PlayerUpdateEventLiveOpsEventParams

**Line:** 563019

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerUpdateInAppPurchaseHistory

**Line:** 585539

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerUpdateNft

**Line:** 582123

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
Nft: MetaNft
```

---

#### PlayerUpdateSubscriptionInstanceState

**Line:** 586711

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerUploadIncidentReport

**Line:** 576163

**Inherits:** MetaMessage

---

#### PlayerUploadedIncidentReportToUrl

**Line:** 576336

**Inherits:** MetaMessage

---

#### PlayerWorldModel

**Line:** 1078319

---

#### PointerEventData

**Line:** 1359192

**Inherits:** BaseEventData

**Fields:**

```
m_PointerPress: GameObject
hovered: List<GameObject>
```

---

#### PostProcessData

**Line:** 900398

**Inherits:** ScriptableObject

---

#### PowerReactiveModel

**Line:** 726271

**Inherits:** ReactiveModel

---

#### PrepareDailyDealPurchaseAction

**Line:** 1051059

**Inherits:** PlayerAction

---

#### ProbeVolumePerSceneData

**Line:** 819911

**Inherits:** MonoBehaviour

**Fields:**

```
serializedBakingSet: ProbeVolumeBakingSet
sceneGUID: string
obsoleteAsset: ObsoleteProbeVolumeAsset
obsoleteCellSharedDataAsset: TextAsset
obsoleteCellSupportDataAsset: TextAsset
obsoleteSerializedScenarios: List<ProbeVolumePerSceneData.ObsoleteSerializablePerScenarioDataItem>
```

---

#### ProbeVolumeSceneData

**Line:** 819999

**Fields:**

```
parentAsset: Object
obsoleteSceneBounds: SerializedDictionary<string, Bounds>
obsoleteHasProbeVolumes: SerializedDictionary<string, bool>
```

---

#### ProcessStartInfo

**Line:** 778073

**Fields:**

```
fileName: string
arguments: string
directory: string
verb: string
windowStyle: ProcessWindowStyle
errorDialog: bool
errorDialogParentHandle: IntPtr
useShellExecute: bool
userName: string
domain: string
password: SecureString
passwordInClearText: string
loadUserProfile: bool
redirectStandardInput: bool
redirectStandardOutput: bool
redirectStandardError: bool
standardOutputEncoding: Encoding
standardErrorEncoding: Encoding
createNoWindow: bool
weakParentProcess: WeakReference
environmentVariables: StringDictionary
_argumentList: Collection<string>
environment: IDictionary<string, string>
```

---

#### ProfileBaseConfig

**Line:** 1073716

**Inherits:** GameConfigKeyValue

---

#### ProgressPassModel

**Line:** 1078721

---

#### PropertyInfo

**Line:** 266226

**Inherits:** MemberInfo

---

#### RateUsAction

**Line:** 1069970

**Inherits:** PlayerAction

---

#### ReactiveModel

**Line:** 694543

---

#### ReceiveOldLeaderboardAction

**Line:** 1055937

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
LeaderboardEntries: MetaDictionary<int, PlayerDivisionParticipantState>
DivisionIndex: DivisionIndex
ParticipantIndex: int
NextDivisionTime: MetaTime
```

---

#### RefreshDailyDealsAction

**Line:** 1051105

**Inherits:** PlayerSynchronizedServerActionCore

---

#### RegionInfo

**Line:** 275054

**Fields:**

```
regionId: int
iso2Name: string
iso3Name: string
win3Name: string
englishName: string
nativeName: string
currencySymbol: string
isoCurrencySymbol: string
currencyEnglishName: string
currencyNativeName: string
```

---

#### Renderer2DData

**Line:** 1364295

**Inherits:** ScriptableRendererData

**Fields:**

```
m_LayerMask: LayerMask
m_TransparencySortMode: TransparencySortMode
m_TransparencySortAxis: Vector3
m_HDREmulationScale: float
m_LightRenderTextureScale: float
m_UseDepthStencilBuffer: bool
m_UseCameraSortingLayersTexture: bool
m_CameraSortingLayersTextureBound: int
m_CameraSortingLayerDownsamplingMethod: Downsampling
m_MaxLightRenderTextureCount: uint
m_MaxShadowRenderTextureCount: uint
m_PostProcessData: PostProcessData
normalsRenderTarget: RTHandle
cameraSortingLayerRenderTarget: RTHandle
```

---

#### RequestActivateSteppingStonesAutoRunAction

**Line:** 1079904

**Inherits:** PlayerAction

---

#### RequestAutoRunSteppingStonesAction

**Line:** 1079386

**Inherits:** PlayerAction

---

#### RequestCreateSteppingStonesRunAction

**Line:** 1079399

**Inherits:** PlayerAction

---

#### RequestPlayerProfileAction

**Line:** 1058618

**Inherits:** PlayerAction

**Fields:**

```
PlayerId: string
```

---

#### ResourceLocationData

**Line:** 1456796

**Fields:**

```
m_InternalId: string
m_Provider: string
m_ResourceType: SerializedType
_Data: object
```

---

#### ResourceLocatorInfo

**Line:** 1453650

---

#### ResourceManagerRuntimeData

**Line:** 1457194

**Fields:**

```
m_buildTarget: string
m_SettingsHash: string
m_CatalogLocations: List<ResourceLocationData>
m_LogResourceManagerExceptions: bool
m_ExtraInitializationData: List<ObjectInitializationData>
m_DisableCatalogUpdateOnStart: bool
m_IsLocalCatalogInBundle: bool
m_CertificateHandlerType: SerializedType
m_AddressablesVersion: string
m_maxConcurrentWebRequests: int
m_CatalogRequestsTimeout: int
```

---

#### ResourcePurchaseAction

**Line:** 1051127

**Inherits:** PlayerAction

---

#### RoomInfo

**Line:** 1527853

**Inherits:** IEquatable

---

#### RoundIconsInfo

**Line:** 1325281

**Inherits:** IMetadata

**Fields:**

```
m_Round_idpi: LocalizedTexture
m_Round_mdpi: LocalizedTexture
m_Round_hdpi: LocalizedTexture
m_Round_xhdpi: LocalizedTexture
m_Round_xxhdpi: LocalizedTexture
m_Round_xxxhdpi: LocalizedTexture
RoundIcons: List<LocalizedTexture>
```

---

#### RowData

**Line:** 1397821

**Inherits:** IDirectResponseSchema

---

#### ScriptableAudioConfig

**Line:** 698820

**Inherits:** ScriptableObject

**Fields:**

```
_sfxConfig: SfxConfig
_biomeSfxConfig: BiomeSfxConfig
```

---

#### ScriptableMainCanvasConfig

**Line:** 698846

**Inherits:** ScriptableObject

**Fields:**

```
_referenceResolution: Vector2
```

---

#### ScriptableRendererData

**Line:** 906625

**Inherits:** ScriptableObject

**Fields:**

```
m_RendererFeatures: List<ScriptableRendererFeature>
m_RendererFeatureMap: List<long>
m_UseNativeRenderPass: bool
m_StripShadowsOffVariants: bool
m_StripAdditionalLightOffVariants: bool
```

---

#### ScriptableVisualConfig

**Line:** 698866

**Inherits:** ScriptableObject

**Fields:**

```
_slotsConfig: SlotsConfig
_worldVisualConfig: WorldVisualConfig
_skillVisualConfig: SkillVisualConfig
_techTreeVisualConfig: TechTreeVisualConfig
_petCollectionVisualConfig: PetCollectionVisualConfig
_dungeonVisualConfig: DungeonVisualConfig
_rewardVisualConfig: RewardVisualConfig
_shopVisualConfig: ShopVisualConfig
_mountCollectionVisualConfig: MountCollectionVisualConfig
_playerIconsConfig: PlayerIconsConfig
_arenaVisualConfig: ArenaVisualConfig
_skinsVisualConfig: SkinsVisualConfig
```

---

#### SecondaryStatItemUnlockLibrary

**Line:** 1067757

**Inherits:** IGameConfigData

---

#### SecondaryStatLibrary

**Line:** 1067799

**Inherits:** IGameConfigData

---

#### SecondaryStats

**Line:** 1076360

---

#### SellItemAction

**Line:** 1067557

**Inherits:** PlayerAction

---

#### SerializationInfo

**Line:** 226189

**Fields:**

```
m_nameToIndex: Dictionary<string, int>
m_currMember: int
m_converter: IFormatterConverter
m_fullTypeName: string
m_assemName: string
objectType: Type
isFullTypeNameSetExplicit: bool
isAssemblyNameSetExplicit: bool
requireSameTokenInPartialTrust: bool
```

---

#### ServerDrivenInAppPurchaseEventState

**Line:** 585979

---

#### ServerGameConfig

**Line:** 1079517

**Inherits:** ServerGameConfigBase

---

#### SessionParticipantState

**Line:** 545410

---

#### SessionResumptionInfo

**Line:** 545551

---

#### SetBonusConfig

**Line:** 1074604

---

#### SetConfig

**Line:** 1074562

**Inherits:** IGameConfigData

---

#### SetInstallVersionAction

**Line:** 1069983

**Inherits:** PlayerAction

---

#### SetPlatformSpecificData

**Line:** 534229

**Inherits:** PlayerSynchronizedServerActionCore

---

#### SetPlayerAgeAction

**Line:** 1070014

**Inherits:** PlayerAction

---

#### SetPlayerCountryAction

**Line:** 1070045

**Inherits:** PlayerAction

---

#### SfxConfig

**Line:** 705667

**Inherits:** ScriptableObject

**Fields:**

```
BattleSfxMasterVolume: float
SkillSfxMasterVolume: float
CoinCollect: AudioClip
AutoForgeEnable: AudioClip
SellGear: AudioClip
EquipGear: AudioClip
ButtonDown: AudioClip
ButtonUp: AudioClip
UpgradeMeta: AudioClip
CardSummon: AudioClip
HatchEgg: AudioClip
SummonSpells: AudioClip
WindingClock: AudioClip
ForgeUpgrade: AudioClip
TechComplete: AudioClip
CollectCurrencies: AudioClip
DungeonEnter: AudioClip
ArrowsSkill: AudioClip
MeatActivate: AudioClip
MoraleActivate: AudioClip
Shurikens: AudioClip
BerserkActivate: AudioClip
BuffActivate: AudioClip
HigherMoraleActivate: AudioClip
Jump: AudioClip
ShatterTile: AudioClip
```

---

#### SharedGameConfig

**Line:** 1059596

**Inherits:** SharedGameConfigBase

---

#### SharedTableData

**Line:** 1317932

**Inherits:** ScriptableObject

**Fields:**

```
m_TableCollectionName: string
m_TableCollectionNameGuidString: string
m_Entries: List<SharedTableData.SharedTableEntry>
m_Metadata: MetadataCollection
m_KeyGenerator: IKeyGenerator
m_TableCollectionNameGuid: Guid
m_IdDictionary: Dictionary<long, SharedTableData.SharedTableEntry>
m_KeyDictionary: Dictionary<string, SharedTableData.SharedTableEntry>
```

---

#### SimplePlayerMail

**Line:** 561393

**Inherits:** MetaInGameMail

---

#### SingularAdData

**Line:** 1571286

**Inherits:** Dictionary

---

#### SinkProviderData

**Line:** 222982

**Fields:**

```
sinkName: string
children: ArrayList
properties: Hashtable
```

---

#### SkinCheatAction

**Line:** 1075700

**Inherits:** PlayerAction

---

#### SkinCollectionVisualConfig

**Line:** 732804

**Inherits:** ScriptableObject

---

#### SkinConfig

**Line:** 1075859

**Inherits:** IGameConfigData

---

#### SkinEquipAction

**Line:** 1075740

**Inherits:** PlayerAction

---

#### SkinUnequipAction

**Line:** 1075775

**Inherits:** PlayerAction

---

#### SkinVisualConfig

**Line:** 732835

**Fields:**

```
Name: string
Icon: Sprite
Prefab: SpriteRenderer
```

---

#### SkinsVisualConfig

**Line:** 732818

**Inherits:** ScriptableObject

**Fields:**

```
SkinConfigs: List<SkinCollectionVisualConfig>
SkinAnimationView: SummonEntryAnimationView
```

---

#### SlotsConfig

**Line:** 711378

**Inherits:** ScriptableObject

**Fields:**

```
_slotIcons: SerializableDictionary<ItemType, Sprite>
```

---

#### SpanAction

**Line:** 464756

---

#### SpreadsheetFileSourceInfo

**Line:** 598762

**Inherits:** GameConfigSpreadsheetSourceInfo

---

#### StatConfig

**Line:** 1076416

**Inherits:** IGameConfigData

---

#### Stats

**Line:** 1076707

---

#### SteamPlatformData

**Line:** 534141

**Inherits:** IPlatformSpecificData

---

#### SteamPlatformState

**Line:** 586944

**Inherits:** InAppPurchaseEventPlatformState

---

#### StencilStateData

**Line:** 900412

**Fields:**

```
overrideStencilState: bool
stencilReference: int
stencilCompareFunction: CompareFunction
passOperation: StencilOp
failOperation: StencilOp
zFailOperation: StencilOp
```

---

#### StepToStoneAction

**Line:** 1079412

**Inherits:** PlayerAction

---

#### SteppingStonesEventConfig

**Line:** 1052489

**Inherits:** LiveOpsEventContent

---

#### SteppingStonesEventModel

**Line:** 1052661

**Inherits:** PlayerLiveOpsEventModel

**Fields:**

```
CanAutoRun: bool
```

---

#### StringInfo

**Line:** 273769

**Fields:**

```
m_str: string
```

---

#### SubscriptionInfo

**Line:** 1407615

---

#### SubscriptionInstanceModel

**Line:** 586519

---

#### SubscriptionModel

**Line:** 586438

---

#### SubsystemsAnalyticInfo

**Line:** 1586861

**Inherits:** SubsystemsAnalyticBase

**Fields:**

```
id: string
plugin_name: string
version: string
library_name: string
```

---

#### SymbolDocumentInfo

**Line:** 1289799

---

#### SystemInfo

**Line:** 1590859

**Fields:**

```
parentSystemInfo: SystemInfo
isActive: bool
_accumulatedExecutionDuration: double
_minExecutionDuration: double
_maxExecutionDuration: double
_executionDurationsCount: int
_accumulatedCleanupDuration: double
_minCleanupDuration: double
_maxCleanupDuration: double
_cleanupDurationsCount: int
```

---

#### TCFData

**Line:** 1564547

**Fields:**

```
features: List<TCFFeature>
purposes: List<TCFPurpose>
specialFeatures: List<TCFSpecialFeature>
specialPurposes: List<TCFSpecialPurpose>
stacks: List<TCFStack>
vendors: List<TCFVendor>
tcString: string
```

---

#### TMP_TextInfo

**Line:** 1228733

**Fields:**

```
textComponent: TMP_Text
characterCount: int
spriteCount: int
spaceCount: int
wordCount: int
linkCount: int
lineCount: int
pageCount: int
materialCount: int
```

---

#### TerrainData

**Line:** 1581985

**Inherits:** Object

---

#### TextInfo

**Line:** 273910

**Inherits:** ICloneable

**Fields:**

```
m_listSeparator: string
m_isReadOnly: bool
m_cultureName: string
m_cultureData: CultureData
m_textInfoName: string
m_IsAsciiCasingSameAsInvariant: Nullable<bool>
customCultureName: string
m_useUserOverride: bool
m_win32LangID: int
```

---

#### TimeCheatAction

**Line:** 1078288

**Inherits:** PlayerAction

---

#### TimeSkipCheatAction

**Line:** 1078256

**Inherits:** PlayerAction

---

#### TimeTextInfo

**Line:** 1321290

---

#### TimeZoneInfo

**Line:** 4239

**Inherits:** IEquatable

---

#### TimerModel

**Line:** 1078169

---

#### TypeInfo

**Line:** 267254

**Inherits:** Type

---

#### TypedPlayerPropertyId

**Line:** 541585

---

#### UnitEntityReactiveModel

**Line:** 709447

**Inherits:** ReactiveModel

---

#### UnityAction

**Line:** 888227

---

#### UnityPlatformInfo

**Line:** 574331

**Fields:**

```
_nextReachabilityUpdateAt: DateTime
```

---

#### UnitySystemInfo

**Line:** 574058

**Fields:**

```
_nextBatteryUpdateAt: DateTime
```

---

#### UniversalAdditionalCameraData

**Line:** 915055

**Inherits:** MonoBehaviour

**Fields:**

```
m_RenderShadows: bool
m_RequiresDepthTextureOption: CameraOverrideOption
m_RequiresOpaqueTextureOption: CameraOverrideOption
m_CameraType: CameraRenderType
m_Cameras: List<Camera>
m_RendererIndex: int
m_VolumeLayerMask: LayerMask
m_VolumeTrigger: Transform
m_VolumeFrameworkUpdateModeOption: VolumeFrameworkUpdateMode
m_RenderPostProcessing: bool
m_Antialiasing: AntialiasingMode
m_AntialiasingQuality: AntialiasingQuality
m_StopNaN: bool
m_Dithering: bool
m_ClearDepth: bool
m_AllowXRRendering: bool
m_AllowHDROutput: bool
m_UseScreenCoordOverride: bool
m_ScreenSizeOverride: Vector4
m_ScreenCoordScaleBias: Vector4
m_Camera: Camera
m_RequiresDepthTexture: bool
m_RequiresColorTexture: bool
m_Version: float
m_MotionVectorsPersistentData: MotionVectorsPersistentData
m_History: UniversalCameraHistory
m_VolumeStack: VolumeStack
```

---

#### UniversalAdditionalLightData

**Line:** 915382

**Inherits:** MonoBehaviour

**Fields:**

```
m_Version: int
m_UsePipelineSettings: bool
m_Light: Light
m_AdditionalLightsShadowResolutionTier: int
m_LightLayerMask: LightLayerEnum
m_RenderingLayers: uint
m_CustomShadowLayers: bool
m_ShadowLayerMask: LightLayerEnum
m_ShadowRenderingLayers: uint
m_LightCookieSize: Vector2
m_LightCookieOffset: Vector2
m_SoftShadowQuality: SoftShadowQuality
```

---

#### UniversalCameraData

**Line:** 907406

**Inherits:** ContextItem

**Fields:**

```
m_ViewMatrix: Matrix4x4
m_ProjectionMatrix: Matrix4x4
m_JitterMatrix: Matrix4x4
camera: Camera
m_HistoryManager: UniversalCameraHistory
renderType: CameraRenderType
targetTexture: RenderTexture
cameraTargetDescriptor: RenderTextureDescriptor
pixelRect: Rect
useScreenCoordOverride: bool
screenSizeOverride: Vector4
screenCoordScaleBias: Vector4
pixelWidth: int
pixelHeight: int
aspectRatio: float
renderScale: float
imageScalingMode: ImageScalingMode
upscalingFilter: ImageUpscalingFilter
fsrOverrideSharpness: bool
fsrSharpness: float
hdrColorBufferPrecision: HDRColorBufferPrecision
clearDepth: bool
cameraType: CameraType
isDefaultViewport: bool
isHdrEnabled: bool
allowHDROutput: bool
isAlphaOutputEnabled: bool
requiresDepthTexture: bool
requiresOpaqueTexture: bool
postProcessingRequiresDepthTexture: bool
... (21 more fields)
```

---

#### UniversalLightData

**Line:** 907597

**Inherits:** ContextItem

**Fields:**

```
mainLightIndex: int
additionalLightsCount: int
maxPerObjectAdditionalLightsCount: int
visibleLights: NativeArray<VisibleLight>
shadeAdditionalLightsPerVertex: bool
supportsMixedLighting: bool
reflectionProbeBoxProjection: bool
reflectionProbeBlending: bool
supportsLightLayers: bool
supportsAdditionalLights: bool
```

---

#### UniversalPostProcessingData

**Line:** 907621

**Inherits:** ContextItem

**Fields:**

```
isEnabled: bool
gradingMode: ColorGradingMode
lutSize: int
useFastSRGBLinearConversion: bool
supportScreenSpaceLensFlare: bool
supportDataDrivenLensFlare: bool
```

---

#### UniversalRendererData

**Line:** 906793

**Inherits:** ScriptableRendererData

**Fields:**

```
postProcessData: PostProcessData
m_AssetVersion: int
m_OpaqueLayerMask: LayerMask
m_TransparentLayerMask: LayerMask
m_DefaultStencilState: StencilStateData
m_ShadowTransparentReceive: bool
m_RenderingMode: RenderingMode
m_DepthPrimingMode: DepthPrimingMode
m_CopyDepthMode: CopyDepthMode
m_DepthAttachmentFormat: DepthFormat
m_DepthTextureFormat: DepthFormat
m_AccurateGbufferNormals: bool
m_IntermediateTextureMode: IntermediateTextureMode
m_StripShadowsOffVariants: bool
m_StripAdditionalLightOffVariants: bool
```

---

#### UniversalRenderingData

**Line:** 907641

**Inherits:** ContextItem

**Fields:**

```
m_CommandBuffer: CommandBuffer
cullResults: CullingResults
supportsDynamicBatching: bool
perObjectData: PerObjectData
```

---

#### UniversalResourceData

**Line:** 907752

**Inherits:** UniversalResourceDataBase

**Fields:**

```
_backBufferColor: TextureHandle
_backBufferDepth: TextureHandle
_cameraColor: TextureHandle
_cameraDepth: TextureHandle
_mainShadowsTexture: TextureHandle
_additionalShadowsTexture: TextureHandle
_cameraOpaqueTexture: TextureHandle
_cameraDepthTexture: TextureHandle
_cameraNormalsTexture: TextureHandle
_motionVectorColor: TextureHandle
_motionVectorDepth: TextureHandle
_internalColorLut: TextureHandle
_debugScreenColor: TextureHandle
_debugScreenDepth: TextureHandle
_afterPostProcessColor: TextureHandle
_overlayUITexture: TextureHandle
_renderingLayersTexture: TextureHandle
_dBufferDepth: TextureHandle
_ssaoTexture: TextureHandle
_stpDebugView: TextureHandle
```

---

#### UniversalShadowData

**Line:** 907978

**Inherits:** ContextItem

**Fields:**

```
supportsMainLightShadows: bool
mainLightShadowsEnabled: bool
mainLightShadowmapWidth: int
mainLightShadowmapHeight: int
mainLightShadowCascadesCount: int
mainLightShadowCascadesSplit: Vector3
mainLightShadowCascadeBorder: float
supportsAdditionalLightShadows: bool
additionalLightShadowsEnabled: bool
additionalLightsShadowmapWidth: int
additionalLightsShadowmapHeight: int
supportsSoftShadows: bool
shadowmapDepthBufferBits: int
bias: List<Vector4>
resolution: List<int>
isKeywordAdditionalLightShadowsEnabled: bool
isKeywordSoftShadowsEnabled: bool
mainLightShadowResolution: int
mainLightRenderTargetWidth: int
mainLightRenderTargetHeight: int
visibleLightsShadowCullingInfos: NativeArray<URPLightShadowCullingInfos>
shadowAtlasLayout: AdditionalLightsShadowAtlasLayout
```

---

#### UxmlSerializedData

**Line:** 669858

**Fields:**

```
uxmlAssetId: int
```

---

#### VFXSpawnerState

**Line:** 1587704

**Inherits:** IDisposable

**Fields:**

```
m_Ptr: IntPtr
m_Owner: bool
m_WrapEventAttribute: VFXEventAttribute
```

---

#### WorldIndexConfig

**Line:** 1060727

**Inherits:** IGameConfigData

---

#### WorldModel

**Line:** 1079732

**Inherits:** ISchemaMigratable

**Fields:**

```
WorldIndex: WorldIndex
LastPlayerOnlineAt: MetaTime
CreatedAt: MetaTime
```

---

#### WorldVisualConfig

**Line:** 711521

**Inherits:** ScriptableObject

**Fields:**

```
SheetConnection: GoogleSheetConnection
WeaponLibrarySheetName: string
ProjectileLibrarySheetName: string
DefaultWeapon: EquipmentItemVisualConfig
AgeConfigs: List<AgeVisualConfig>
ChatPvpMap: PvpMapData
ArenaPvpMap: PvpMapData
GuildWarMap: PvpMapData
```

---

#### XCData

**Line:** 1560193

**Inherits:** XText

---

#### XRSystemData

**Line:** 906777

**Inherits:** ScriptableObject

---

#### XmlCharacterData

**Line:** 748140

**Inherits:** XmlLinkedNode

**Fields:**

```
data: string
```

---

#### XmlSchemaAppInfo

**Line:** 763840

**Inherits:** XmlSchemaObject

**Fields:**

```
source: string
```

---

#### XmlSchemaContentModel

**Line:** 764654

**Inherits:** XmlSchemaAnnotated

---

#### XmlSchemaInfo

**Line:** 765764

**Inherits:** IXmlSchemaInfo

**Fields:**

```
isDefault: bool
isNil: bool
schemaElement: XmlSchemaElement
schemaAttribute: XmlSchemaAttribute
schemaType: XmlSchemaType
memberType: XmlSchemaSimpleType
validity: XmlSchemaValidity
contentType: XmlSchemaContentType
```

---

## Pets & Mounts

**Classes:** 54 | **Enums:** 3

### Enumerations

#### PetBalancingType

**Line:** 1071661

**Values:**

```
Balanced = 0
Damage = 1
Health = 2
```

---

#### PetMovement

**Line:** 725224

---

#### PhysicsShapeType2D

**Line:** 1578338

**Values:**

```
Circle = 0
Capsule = 1
Polygon = 2
Edges = 3
```

---

### Classes

#### EggConfig

**Line:** 1071565

**Inherits:** IGameConfigData

---

#### EggDungeonBattleLibrary

**Line:** 1061275

**Inherits:** DungeonBattleLibrary

---

#### EggReactiveModel

**Line:** 723750

**Inherits:** ReactiveModel

---

#### HatchedPetInfo

**Line:** 1051840

---

#### MountCheatContainer

**Line:** 722128

**Inherits:** AbstractCheatContainer

---

#### MountCollectionEntryUiVisual

**Line:** 722276

**Inherits:** MonoBehaviour

**Fields:**

```
MountUiVisual: MountUiVisual
MountEquippedVisual: MountEquippedVisual
Button: UnityButton
```

---

#### MountCollectionVisualConfig

**Line:** 722175

**Inherits:** ScriptableObject

**Fields:**

```
SheetConnection: GoogleSheetConnection
MountsLibrarySheetName: string
MountAnimationView: SummonEntryAnimationView
```

---

#### MountCollider

**Line:** 722833

**Inherits:** MonoBehaviour

**Fields:**

```
Radius: float
```

---

#### MountEquipAction

**Line:** 1070152

**Inherits:** PlayerAction

---

#### MountEquippedVisual

**Line:** 722412

**Inherits:** MonoBehaviour

**Fields:**

```
Equipped: GameObject
CanvasGroup: CanvasGroup
```

---

#### MountId

**Line:** 1070431

**Inherits:** IEquatable

---

#### MountLibrary

**Line:** 1070484

**Inherits:** IGameConfigData

---

#### MountMergeAction

**Line:** 1070203

**Inherits:** PlayerAction

---

#### MountMergeEntryUiVisual

**Line:** 722489

**Inherits:** MonoBehaviour

**Fields:**

```
MountUiVisual: MountUiVisual
MountEquippedVisual: MountEquippedVisual
Button: UnityButton
SelectedMark: GameObject
IconCanvasGroup: CanvasGroup
Mount: PlayerMountModel
```

---

#### MountStatTarget

**Line:** 1077054

**Inherits:** StatTargetBase

---

#### MountStats

**Line:** 1070550

---

#### MountUiVisual

**Line:** 722798

**Inherits:** MonoBehaviour

**Fields:**

```
Icon: Image
Level: TMP_Text
Background: Image
```

---

#### MountUnEquipAction

**Line:** 1070396

**Inherits:** PlayerAction

---

#### MountVisualConfig

**Line:** 722210

**Fields:**

```
Icon: Sprite
Prefab: MountView
MountName: string
```

---

#### MountsRedDotLogic

**Line:** 722252

**Inherits:** IRedDotLogic

---

#### PetBalancingConfig

**Line:** 1071607

**Inherits:** IGameConfigData

---

#### PetBaseConfig

**Line:** 1071672

**Inherits:** GameConfigKeyValue

---

#### PetCheatAction

**Line:** 1071036

**Inherits:** PlayerAction

---

#### PetCheatContainer

**Line:** 723306

**Inherits:** AbstractCheatContainer

---

#### PetCollectionReactiveModel

**Line:** 723887

**Inherits:** ReactiveModel

---

#### PetCollectionVisualConfig

**Line:** 723526

**Inherits:** ScriptableObject

**Fields:**

```
PetAnimationView: SummonEntryAnimationView
EggAnimationView: SummonEntryAnimationView
```

---

#### PetConfig

**Line:** 1071746

**Inherits:** IGameConfigData

---

#### PetEggCheatAction

**Line:** 1071090

**Inherits:** PlayerAction

---

#### PetEggHatchClaimAction

**Line:** 1071252

**Inherits:** PlayerAction

---

#### PetEggHatchSlotPurchaseAction

**Line:** 1071132

**Inherits:** PlayerAction

---

#### PetEggHatchStartAction

**Line:** 1071145

**Inherits:** PlayerAction

---

#### PetEquipAction

**Line:** 1071290

**Inherits:** PlayerAction

---

#### PetEquippedMessage

**Line:** 723642

**Inherits:** IMessage

---

#### PetFeature

**Line:** 724009

**Inherits:** Feature

---

#### PetHatchedMessage

**Line:** 723669

**Inherits:** IMessage

---

#### PetId

**Line:** 1071788

**Inherits:** IEquatable

---

#### PetMergeAction

**Line:** 1071368

**Inherits:** PlayerAction

---

#### PetMovement

**Line:** 725233

**Inherits:** MonoBehaviour

**Fields:**

```
FollowAnchor: Transform
Pet: Transform
_timer: float
_dist: float
_targetPos: Vector2
MinSpeed: float
MaxSpeed: float
MovementRadius: float
_yOffset: float
```

---

#### PetMovementBehaviour

**Line:** 725260

**Inherits:** MonoBehaviour

**Fields:**

```
Body: Transform
MinSpeed: float
MaxSpeed: float
HopLenght: float
HopHeight: float
MaxAngle: float
StretchAmount: float
_timer: float
_anchorPos: Vector2
_targetPos: Vector2
_position: Vector2
_dist: float
_moveMulti: float
```

---

#### PetReactiveModel

**Line:** 723927

**Inherits:** ReactiveModel

---

#### PetStatTarget

**Line:** 1077306

**Inherits:** StatTargetBase

---

#### PetStats

**Line:** 1071933

---

#### PetUnEquipAction

**Line:** 1071425

**Inherits:** PlayerAction

---

#### PetUnequippedMessage

**Line:** 723689

**Inherits:** IMessage

---

#### PetVisual

**Line:** 725204

**Inherits:** MonoBehaviour

**Fields:**

```
_offset: Vector2
PetMovement: PetMovementBehaviour
```

---

#### PetVisualConfig

**Line:** 723557

**Fields:**

```
PetIcon: Sprite
PetPrefab: PetVisual
PetName: string
```

---

#### PetsLocalizer

**Line:** 721280

**Inherits:** LocalizerBase

---

#### PetsRedDotLogic

**Line:** 724063

**Inherits:** IRedDotLogic

**Fields:**

```
_stillLockedPetSlotsCount: int
_alreadyMarkedClaimableHatchSlotsIds: HashSet<int>
```

---

#### PlayerEggModel

**Line:** 1072016

---

#### PlayerMountCollectionModel

**Line:** 1070869

---

#### PlayerMountModel

**Line:** 1070946

---

#### PlayerPetCollectionModel

**Line:** 1072162

---

#### PlayerPetModel

**Line:** 1072248

---

#### SecondaryStatPetUnlockLibrary

**Line:** 1071974

**Inherits:** IGameConfigData

---

## Progression

**Classes:** 29 | **Enums:** 30

### Enumerations

#### AlertLevel

**Line:** 1448518

**Values:**

```
Warning = 1
Fatal = 2
```

---

#### AuthenticationLevel

**Line:** 802758

**Values:**

```
None = 0
MutualAuthRequested = 1
MutualAuthRequired = 2
```

---

#### BindingLogLevel

**Line:** 608859

**Values:**

```
None = 0
Once = 1
All = 2
```

---

#### CompressionLevel

**Line:** 789375

**Values:**

```
Optimal = 0
Fastest = 1
NoCompression = 2
```

---

#### ConformanceLevel

**Line:** 740774

**Values:**

```
Auto = 0
Fragment = 1
Document = 2
```

---

#### DirectConnectionUpgradeRefuseReason

**Line:** 553883

**Values:**

```
Unknown = 0
DisabledInEntitySettings = 1
DisabledInServerSettings = 2
NoPublicIpOnServer = 3
ServerFailedToOpenPort = 4
```

---

#### EventLevel

**Line:** 275506

**Values:**

```
LogAlways = 0
Critical = 1
Error = 2
Warning = 3
Informational = 4
Verbose = 5
```

---

#### Expander

**Line:** 1319916

---

#### ExponentialBackOffPolicy

**Line:** 1497267

**Values:**

```
None = 0
Exception = 1
UnsuccessfulResponse503 = 2
```

---

#### ExpressionType

**Line:** 1287138

**Values:**

```
Add = 0
AddChecked = 1
And = 2
AndAlso = 3
ArrayLength = 4
ArrayIndex = 5
Call = 6
Coalesce = 7
Conditional = 8
Constant = 9
Convert = 10
ConvertChecked = 11
Divide = 12
Equal = 13
ExclusiveOr = 14
GreaterThan = 15
GreaterThanOrEqual = 16
Invoke = 17
Lambda = 18
LeftShift = 19
LessThan = 20
LessThanOrEqual = 21
ListInit = 22
MemberAccess = 23
MemberInit = 24
Modulo = 25
Multiply = 26
MultiplyChecked = 27
Negate = 28
UnaryPlus = 29
NegateChecked = 30
New = 31
NewArrayInit = 32
NewArrayBounds = 33
Not = 34
NotEqual = 35
Or = 36
OrElse = 37
Parameter = 38
Power = 39
Quote = 40
RightShift = 41
Subtract = 42
SubtractChecked = 43
TypeAs = 44
TypeIs = 45
Assign = 46
Block = 47
DebugInfo = 48
Decrement = 49
Dynamic = 50
Default = 51
Extension = 52
Goto = 53
Increment = 54
Index = 55
Label = 56
RuntimeVariables = 57
Loop = 58
Switch = 59
Throw = 60
Try = 61
Unbox = 62
AddAssign = 63
AndAssign = 64
DivideAssign = 65
ExclusiveOrAssign = 66
LeftShiftAssign = 67
ModuloAssign = 68
MultiplyAssign = 69
OrAssign = 70
PowerAssign = 71
RightShiftAssign = 72
SubtractAssign = 73
AddAssignChecked = 74
MultiplyAssignChecked = 75
SubtractAssignChecked = 76
PreIncrementAssign = 77
PreDecrementAssign = 78
PostIncrementAssign = 79
PostDecrementAssign = 80
TypeEqual = 81
OnesComplement = 82
IsTrue = 83
IsFalse = 84
```

---

#### GameConfigLogLevel

**Line:** 595222

**Values:**

```
NotSet = 0
Verbose = 1
Debug = 2
Information = 3
Warning = 4
Error = 5
```

---

#### GotoExpressionKind

**Line:** 1287361

**Values:**

```
Goto = 0
Return = 1
Break = 2
Continue = 3
```

---

#### IPProtectionLevel

**Line:** 800364

**Values:**

```
Unrestricted = 10
EdgeRestricted = 20
Restricted = 30
```

---

#### LogLevel

**Line:** 1596433

**Values:**

```
On = 0
Trace = 1
Debug = 2
Info = 3
Warn = 4
Error = 5
Fatal = 6
Off = 7
```

---

#### NtlmAuthLevel

**Line:** 1448356

**Values:**

```
LM_and_NTLM = 0
LM_and_NTLM_and_try_NTLMv2_Session = 1
NTLM_only = 2
NTLMv2_only = 3
```

---

#### PipelineDebugLevel

**Line:** 900532

**Values:**

```
Disabled = 0
Profiling = 1
```

---

#### PlayerEventExperimentAssignment

**Line:** 537035

---

#### RequestCacheLevel

**Line:** 799177

**Values:**

```
Default = 0
BypassCache = 1
CacheOnly = 2
CacheIfAvailable = 3
Revalidate = 4
Reload = 5
NoCacheNoStore = 6
```

---

#### ShaderVariantLogLevel

**Line:** 905767

**Values:**

```
Disabled = 0
OnlyUniversalRPShaders = 1
AllShaders = 2
```

---

#### SocketOptionLevel

**Line:** 800533

**Values:**

```
Socket = 65535
IP = 0
IPv6 = 41
Tcp = 6
Udp = 17
```

---

#### TechTreeNodeType

**Line:** 1077725

**Values:**

```
WeaponBonus = 0
HelmetBonus = 1
BodyBonus = 2
ShoeBonus = 3
GloveBonus = 4
BeltBonus = 5
NecklaceBonus = 6
RingBonus = 7
WeaponLevelUp = 8
HelmetLevelUp = 9
BodyLevelUp = 10
ShoeLevelUp = 11
GloveLevelUp = 12
BeltLevelUp = 13
NecklaceLevelUp = 14
RingLevelUp = 15
MountDamage = 16
MountHealth = 17
ExtraMountChance = 18
MountSummonCost = 19
ForgeTimerSpeed = 20
ForgeUpgradeCost = 21
EquipmentSellPrice = 22
AutoForge = 23
HammerOfflineReward = 24
CoinOfflineReward = 25
MaxOfflineReward = 26
FreeForgeChance = 27
HammerThiefHammerReward = 28
HammerThiefCoinReward = 29
SkillDamage = 30
SkillPassiveDamage = 31
SkillPassiveHealth = 32
GhostTownSkillBonus = 33
SkillSummonCost = 34
PetBonusDamage = 35
PetBonusHealth = 36
ExtraEggChance = 37
CommonEggTimer = 38
RareEggTimer = 39
EpicEggTimer = 40
LegendaryEggTimer = 41
UltimateEggTimer = 42
MythicEggTimer = 43
ZombieRushTechPotions = 44
TechNodeUpgradeCost = 45
TechResearchTimer = 46
```

---

#### TechTreeType

**Line:** 1077896

**Values:**

```
Forge = 0
Power = 1
SkillsPetTech = 2
```

---

#### TokenImpersonationLevel

**Line:** 220353

**Values:**

```
None = 0
Anonymous = 1
Identification = 2
Impersonation = 3
Delegation = 4
```

---

#### TraceLevel

**Line:** 777618

**Values:**

```
Off = 0
Error = 1
Warning = 2
Info = 3
Verbose = 4
```

---

#### TypeFilterLevel

**Line:** 226403

**Values:**

```
Low = 2
Full = 3
```

---

#### UsercentricsLoggerLevel

**Line:** 1564431

**Values:**

```
None = 0
Error = 1
Warning = 2
Debug = 3
```

---

#### XPathNamespaceScope

**Line:** 752792

**Values:**

```
All = 0
ExcludeXml = 1
Local = 2
```

---

#### XPathNodeType

**Line:** 752937

**Values:**

```
Root = 0
Element = 1
Attribute = 2
Namespace = 3
Text = 4
SignificantWhitespace = 5
Whitespace = 6
ProcessingInstruction = 7
Comment = 8
All = 9
```

---

#### XPathResultType

**Line:** 752725

**Values:**

```
Number = 0
String = 1
Boolean = 2
NodeSet = 3
Navigator = 1
Any = 5
Error = 6
```

---

#### XPathScanner

**Line:** 770491

---

### Classes

#### ItemCreateCheatAction

**Line:** 1068692

**Inherits:** PlayerAction

---

#### ItemLevelBracketsConfig

**Line:** 1067703

**Inherits:** IGameConfigData

---

#### MountCreateCheatAction

**Line:** 1070099

**Inherits:** PlayerAction

---

#### MountPetLevelCheatAction

**Line:** 1070250

**Inherits:** PlayerAction

---

#### MountUpgradeInfo

**Line:** 1070818

---

#### MountUpgradeLibrary

**Line:** 1070776

**Inherits:** IGameConfigData

---

#### PetUpgradeConfig

**Line:** 1071841

**Inherits:** IGameConfigData

---

#### PetUpgradeInfo

**Line:** 1071883

---

#### PetUpgradedMessage

**Line:** 723716

**Inherits:** IMessage

---

#### PlayerEventExperimentAssignment

**Line:** 537045

**Inherits:** PlayerEventBase

---

#### PlayerEventTechTreeNodeUpgradeCompleted

**Line:** 1077386

**Inherits:** PlayerEventBase

---

#### PlayerEventTechTreeNodeUpgradeStarted

**Line:** 1077443

**Inherits:** PlayerEventBase

---

#### PlayerEventTierUpgrade

**Line:** 1068503

**Inherits:** PlayerEventBase

---

#### PlayerExperimentId

**Line:** 538406

**Inherits:** StringId

---

#### PlayerExperimentInfo

**Line:** 538501

**Inherits:** IGameConfigData

---

#### PlayerExperimentsState

**Line:** 533405

**Inherits:** IEquatable

**Fields:**

```
ExperimentGroupAssignment: MetaDictionary<PlayerExperimentId, PlayerExperimentsState.ExperimentAssignment>
```

---

#### PlayerTechTreeModel

**Line:** 1078033

---

#### TechTreeCategoryVisualConfig

**Line:** 735190

**Fields:**

```
Icon: Sprite
TitleLocaKey: string
```

---

#### TechTreeLibrary

**Line:** 1077642

**Inherits:** IGameConfigData

---

#### TechTreeMaxCheatAction

**Line:** 1077525

**Inherits:** PlayerAction

---

#### TechTreeNodeInfo

**Line:** 1077822

---

#### TechTreeNodeModel

**Line:** 1078077

**Fields:**

```
Level: int
```

---

#### TechTreeNodeUpgradeClaimAction

**Line:** 1077538

**Inherits:** PlayerAction

---

#### TechTreeNodeUpgradeStartAction

**Line:** 1077622

**Inherits:** PlayerAction

**Fields:**

```
TechTreeType: TechTreeType
NodeId: int
```

---

#### TechTreeNodeVisualConfig

**Line:** 735177

**Fields:**

```
Icon: Sprite
```

---

#### TechTreePositionLibrary

**Line:** 1077780

**Inherits:** IGameConfigData

---

#### TechTreeUpgradeInfo

**Line:** 1077949

---

#### TechTreeUpgradeLibrary

**Line:** 1077907

**Inherits:** IGameConfigData

---

#### TechTreeVisualConfig

**Line:** 735159

**Inherits:** ScriptableObject

**Fields:**

```
Nodes: SerializableDictionary<TechTreeNodeType, TechTreeNodeVisualConfig>
XSpacing: float
YSpacing: float
YTopPadding: float
YBottomPadding: float
Categories: SerializableDictionary<TechTreeType, TechTreeCategoryVisualConfig>
```

---

## PvE Content

**Classes:** 43 | **Enums:** 3

### Enumerations

#### BattleMode

**Line:** 1056395

**Values:**

```
None = 0
MainBattle = 1
DungeonBattle = 2
PvpBattle = 3
GuildWarBattle = 4
```

---

#### BattleState

**Line:** 1056514

**Values:**

```
None = 0
ReadyToStartWave = 1
WaveFinished = 2
Running = 3
Paused = 4
Won = 5
Lost = 6
```

---

#### DungeonType

**Line:** 1061243

**Values:**

```
Hammer = 0
Skill = 1
Pet = 2
Potion = 3
```

---

### Classes

#### BattleNormalSpeedCheatAction

**Line:** 1056805

**Inherits:** PlayerAction

---

#### BattleSpeedUpCheatAction

**Line:** 1056791

**Inherits:** PlayerAction

---

#### ChangeBattleCheatAction

**Line:** 1056342

**Inherits:** PlayerAction

---

#### CleanupDungeonBattleAction

**Line:** 1060793

**Inherits:** PlayerAction

---

#### DungeonBaseConfig

**Line:** 1061151

**Inherits:** GameConfigKeyValue

---

#### DungeonBattleFeature

**Line:** 713188

**Inherits:** Feature

---

#### DungeonBattleLibrary

**Line:** 1061285

---

#### DungeonBattleReactiveModel

**Line:** 713197

**Inherits:** ReactiveModel

---

#### DungeonCheatContainer

**Line:** 712422

**Inherits:** AbstractCheatContainer

---

#### DungeonFeature

**Line:** 712553

**Inherits:** Feature

---

#### DungeonReactiveModel

**Line:** 712704

**Inherits:** ReactiveModel

**Fields:**

```
DungeonModel: PlayerDungeonModel
```

---

#### DungeonRedDotLogic

**Line:** 712593

**Inherits:** IRedDotLogic

**Fields:**

```
_stillLockedDungeonsCount: int
```

---

#### DungeonStatTarget

**Line:** 1077253

**Inherits:** StatTargetBase

---

#### DungeonVisualConfig

**Line:** 712487

**Inherits:** ScriptableObject

**Fields:**

```
Dungeons: SerializableDictionary<DungeonType, DungeonVisualData>
```

---

#### DungeonVisualData

**Line:** 712500

**Fields:**

```
BackgroundImage: Sprite
DungeonTitle: string
KeyImage: Sprite
MapElementViews: List<MapElementView>
MapBackgroundColor: Color
```

---

#### DungeonWinCheatAction

**Line:** 1060843

**Inherits:** PlayerAction

---

#### DungeonsLocalizer

**Line:** 720934

**Inherits:** LocalizerBase

---

#### DungeonsMaxCheatAction

**Line:** 1060829

**Inherits:** PlayerAction

---

#### EnemyAgeScalingConfig

**Line:** 1059543

**Inherits:** IGameConfigData

---

#### EnemyConfig

**Line:** 1059477

**Inherits:** IGameConfigData

---

#### FinishDungeonBattleAction

**Line:** 1060885

**Inherits:** PlayerAction

---

#### HammerThiefDungeonBattleLibrary

**Line:** 1061405

**Inherits:** IGameConfigData

---

#### HammerThiefDungeonBattleModel

**Line:** 1061471

**Inherits:** IDungeonBattleModel

---

#### MainBattleConfig

**Line:** 1059256

**Inherits:** GameConfigKeyValue

---

#### MainBattleLibrary

**Line:** 1059306

**Inherits:** IGameConfigData

---

#### MainBattleModel

**Line:** 1056551

---

#### MainBattleReactiveModel

**Line:** 710088

**Inherits:** ReactiveModel

---

#### NormalDungeonBattleModel

**Line:** 1061700

**Inherits:** IDungeonBattleModel

---

#### PauseBattleCheatAction

**Line:** 1056763

**Inherits:** PlayerAction

---

#### PlayerDungeonModel

**Line:** 1061848

---

#### PlayerDungeonsModel

**Line:** 1061913

**Inherits:** INextDayListener

---

#### PlayerEventDungeonCompleted

**Line:** 1060898

**Inherits:** PlayerEventBase

---

#### PlayerEventDungeonEntered

**Line:** 1060943

**Inherits:** PlayerEventBase

---

#### PlayerEventDungeonFailed

**Line:** 1060988

**Inherits:** PlayerEventBase

---

#### PlayerEventDungeonSweptLast

**Line:** 1061033

**Inherits:** PlayerEventBase

---

#### PlayerPropertyIdMainBattleProgress

**Line:** 1079307

**Inherits:** TypedPlayerPropertyId

---

#### PotionDungeonBattleLibrary

**Line:** 1061265

**Inherits:** DungeonBattleLibrary

---

#### SetupDungeonBattleAction

**Line:** 1061078

**Inherits:** PlayerAction

---

#### SetupMainBattleAction

**Line:** 1056718

**Inherits:** PlayerAction

---

#### SweepDungeonAction

**Line:** 1061120

**Inherits:** PlayerAction

---

#### SwitchBackToMainBattleAction

**Line:** 1056749

**Inherits:** PlayerAction

---

#### UnPauseBattleCheatAction

**Line:** 1056777

**Inherits:** PlayerAction

---

#### WaveConfig

**Line:** 1059401

---

## PvP

**Classes:** 43 | **Enums:** 6

### Enumerations

#### LeagueClientPhase

**Line:** 565346

**Values:**

```
NoSession = 0
NoDivision = 1
LoadingDivision = 2
DivisionActive = 3
```

---

#### LeagueJoinRefuseReason

**Line:** 565371

**Values:**

```
UnknownReason = 0
LeagueNotEnabled = 1
LeagueNotStarted = 2
SeasonMigrationInProgress = 3
RequirementsNotMet = 4
AlreadyInLeague = 5
```

---

#### OperatingSystemFamily

**Line:** 885041

**Values:**

```
Other = 0
MacOSX = 1
Windows = 2
Linux = 3
```

---

#### PvpBattleResult

**Line:** 1074354

**Values:**

```
NotFinished = 0
Draw = 1
Party1Win = 2
Party2Win = 3
Forfeit = 4
```

---

#### PvpBattleState

**Line:** 1074342

**Values:**

```
None = 0
Running = 1
CombatFinished = 2
Finished = 3
```

---

#### PvpBattleType

**Line:** 1074230

**Values:**

```
Test = 0
Chat = 1
ChatReplay = 2
Arena = 3
GuildWar = 4
```

---

### Classes

#### ArenaFeature

**Line:** 704914

**Inherits:** Feature

---

#### ArenaLeagueLibrary

**Line:** 1056078

**Inherits:** IGameConfigData

---

#### ArenaLeagueRewards

**Line:** 1056177

---

#### ArenaLocalizer

**Line:** 720874

**Inherits:** LocalizerBase

---

#### ArenaMatchupOption

**Line:** 1056025

---

#### ArenaPromotionDisplayedAction

**Line:** 1055814

**Inherits:** PlayerAction

---

#### ArenaPvpBattleStartAction

**Line:** 1055845

**Inherits:** PlayerAction

---

#### ArenaRedDotLogic

**Line:** 704923

**Inherits:** IRedDotLogic

---

#### ArenaRefreshAvatars

**Line:** 1055876

**Inherits:** DivisionActionBase

---

#### ArenaRewardEntryVisual

**Line:** 705340

**Inherits:** MonoBehaviour

**Fields:**

```
RewardText: TMP_Text
```

---

#### ArenaRewardGridVisual

**Line:** 705352

**Inherits:** MonoBehaviour

**Fields:**

```
RewardGrid: Transform
RewardPrefab: ArenaRewardEntryVisual
```

---

#### ArenaRewardLibrary

**Line:** 1056132

**Inherits:** IGameConfigData

---

#### ArenaRewardRankEntryVisual

**Line:** 705371

**Inherits:** MonoBehaviour

**Fields:**

```
ArenaRewardGridVisual: ArenaRewardGridVisual
RankText: TMP_Text
RankIcon: Image
```

---

#### ArenaTutorialDisplayedAction

**Line:** 1055907

**Inherits:** PlayerAction

---

#### ArenaVisualConfig

**Line:** 704988

**Inherits:** ScriptableObject

---

#### ForfeitPvpAction

**Line:** 1073880

**Inherits:** PlayerAction

---

#### GetPlayerPvpProfileRequest

**Line:** 1074174

**Inherits:** MetaRequest

---

#### GetPlayerPvpProfileResponse

**Line:** 1074202

**Inherits:** MetaResponse

---

#### GuildLeaguesEnabledCondition

**Line:** 566161

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### GuildWarPvpBattleStartAction

**Line:** 1062005

**Inherits:** PlayerAction

---

#### LeagueVisualConfig

**Line:** 705002

**Fields:**

```
LeagueIcon: Sprite
LeagueName: string
```

---

#### PlayerLeagueAvatar

**Line:** 1051426

**Inherits:** PlayerDivisionAvatarBase

---

#### PlayerLeagueClient

**Line:** 720865

**Inherits:** LeagueClient

---

#### PlayerLeaguesEnabledCondition

**Line:** 566146

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### PlayerPvpBattleModel

**Line:** 1074243

---

#### PlayerPvpCharacterSerializerUi

**Line:** 728015

**Inherits:** PlayerPvpCharacterView

**Fields:**

```
InputField: TMP_InputField
SerializeButton: UnityButton
LoadButton: UnityButton
SaveButton: UnityButton
SavePvpProfileViewPrefab: SavePvpProfileView
```

---

#### PlayerPvpItemModel

**Line:** 1058122

---

#### PlayerPvpMountModel

**Line:** 1058175

---

#### PlayerPvpPetModel

**Line:** 1058228

---

#### PlayerPvpProfileCharacterScene

**Line:** 727355

**Inherits:** MonoBehaviour

**Fields:**

```
Views: List<PlayerPvpCharacterView>
Camera: Camera
```

---

#### PlayerPvpProfileModel

**Line:** 1058294

---

#### PlayerPvpProfileQuickSaveStorage

**Line:** 727972

**Inherits:** ScriptableObject

**Fields:**

```
Profiles: List<PvpProfileQuickSaveEntry>
```

---

#### PlayerPvpSkinCollectionModel

**Line:** 1075968

---

#### PvpBaseConfig

**Line:** 1074008

**Inherits:** GameConfigKeyValue

---

#### PvpBattleStartAction

**Line:** 1073893

**Inherits:** PlayerAction

---

#### PvpMapData

**Line:** 711508

**Fields:**

```
MapElementViews: List<MapElementView>
MapBackgroundColor: Color
```

---

#### PvpMatchInfo

**Line:** 1074508

**Fields:**

```
Player1: PlayerPvpProfileModel
Player2: PlayerPvpProfileModel
Result: PvpBattleResult
BattleSeed: ulong
PvpBattleType: PvpBattleType
Player1Id: EntityId
Player2Id: EntityId
```

---

#### PvpProfilePetVisual

**Line:** 727656

**Inherits:** MonoBehaviour

**Fields:**

```
Icon: Image
Background: Image
Level: TMP_Text
Button: UnityButton
```

---

#### PvpReplayBattleStartAction

**Line:** 1073946

**Inherits:** PlayerAction

---

#### RunArenaPvpBattleAction

**Line:** 1055956

**Inherits:** PlayerSynchronizedServerActionCore

---

#### RunGuildWarPvpBattleAction

**Line:** 1062047

**Inherits:** PlayerSynchronizedServerActionCore

---

#### ShareLastChatPvpAction

**Line:** 1073977

**Inherits:** PlayerAction

---

#### UpdateNextArenaTime

**Line:** 1056009

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

```
NextDivisionTime: MetaTime
```

---

## Summoning

**Classes:** 13 | **Enums:** 4

### Enumerations

#### DragAndDropPosition

**Line:** 632108

**Values:**

```
OverItem = 0
BetweenItems = 1
OutsideItems = 2
```

---

#### DropdownMenuAction

**Line:** 632670

---

#### Rarity

**Line:** 1074976

**Values:**

```
Common = 0
Rare = 1
Epic = 2
Legendary = 3
Ultimate = 4
Mythic = 5
```

---

#### SummonEntryAnimationView

**Line:** 716132

---

### Classes

#### DragAndDropData

**Line:** 631969

---

#### DropdownMenuAction

**Line:** 632682

**Inherits:** DropdownMenuItem

---

#### DropdownMenuEventInfo

**Line:** 632613

---

#### ItemAgeDropChanceInfo

**Line:** 1051541

**Inherits:** IGameConfigData

---

#### MountRarityVisualConfig

**Line:** 722197

**Inherits:** ScriptableObject

---

#### MountSummonAction

**Line:** 1070328

**Inherits:** PlayerAction

---

#### MountSummonCheatAction

**Line:** 1070362

**Inherits:** PlayerAction

---

#### MountSummonConfig

**Line:** 1070591

**Inherits:** GameConfigKeyValue

---

#### MountSummonDropChanceConfig

**Line:** 1070629

**Inherits:** IGameConfigData

---

#### MountSummonUpgradeConfig

**Line:** 1070734

**Inherits:** IGameConfigData

---

#### MountsSummonedMessage

**Line:** 722228

**Inherits:** IMessage

---

#### PetRarityVisualConfig

**Line:** 723544

**Inherits:** ScriptableObject

---

#### SummonAnimationData

**Line:** 716056

**Fields:**

```
Icon: Sprite
AnimationView: SummonEntryAnimationView
IsNew: bool
Rarity: Nullable<Rarity>
Text: string
```

---

