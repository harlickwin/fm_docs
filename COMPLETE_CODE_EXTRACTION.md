# Complete Game Mechanics - Code-Based Extraction
**Generated from IL2CPP dump - NO ASSUMPTIONS**

This document contains ONLY mechanics found in code with line number references.

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

### Classes (154)

#### ActivateSkillAction

**Line:** 1056269

**Inherits:** PlayerAction

---

#### ActiveSkillStatTarget

**Line:** 1076972

**Inherits:** StatTargetBase

---

#### AreaProjectile

**Line:** 1057091

**Inherits:** BasicEntity

**Fields:**

- `Position`: F64Vec2
- `Velocity`: F64Vec2
- `PulseDuration`: F64
- `PulseTimer`: F64
- `Duration`: F64
- `Timer`: F64
- `Skill`: CombatSkill
- `Radius`: F64
- `Destroyed`: bool
- `IsAlly`: bool
- `HasPulse`: bool
- `HasFinalPulse`: bool
- `UnitId`: int
- `SourceStats`: CombatStats

---

#### AreaProjectileComponent

**Line:** 731368

**Inherits:** IComponent

---

#### AreaProjectileReactiveModel

**Line:** 709218

**Inherits:** ReactiveModel

---

#### AreaProjectileView

**Line:** 731402

**Inherits:** GameUnityView

**Fields:**

- `Radius`: Transform
- `Timer`: Transform

---

#### AttackSpeedComponent

**Line:** 709082

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### AttackSpeedEventSystem

**Line:** 701598

**Inherits:** ReactiveSystem

---

#### AttackSpeedListenerComponent

**Line:** 699440

**Inherits:** IComponent

**Fields:**

- `value`: List<IAttackSpeedListener>

---

#### AttacksSystem

**Line:** 1057705

**Fields:**

- `_random`: RandomPCG

---

#### AutoActivateSkillUiView

**Line:** 731871

**Inherits:** UiUnityView

**Fields:**

- `AutoText`: TMP_Text
- `Background`: Image
- `_feature`: GameEntity
- `Button`: UnityButton

---

#### BerserkSkillView

**Line:** 730752

**Inherits:** TemporaryEffectView

**Fields:**

- `_destroyTween`: Tween
- `ParticleSystem`: ParticleSystem

---

#### BombSkillView

**Line:** 730779

**Inherits:** GameUnityView

**Fields:**

- `Bomb`: Transform
- `Explosion`: ParticleSystem
- `Explode`: AudioClip
- `_sequence`: Sequence

---

#### BuffSkillView

**Line:** 730808

**Inherits:** TemporaryEffectView

**Fields:**

- `_destroyTween`: Tween

---

#### CannonBarrageSkillView

**Line:** 731039

**Inherits:** GameUnityView

**Fields:**

- `Ball`: Transform
- `Trail`: TrailRenderer
- `Explosion`: ParticleSystem
- `ExplosionSound`: AudioClip
- `_sequence`: Sequence

---

#### ChangeWeaponCheatAction

**Line:** 1068220

**Inherits:** PlayerAction

---

#### CleanupAfterCombat

**Line:** 708483

**Inherits:** IComponent

**Fields:**

- `CombatScene`: CombatScene

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

#### CombatEntityIdComponent

**Line:** 709021

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### CombatPhysics

**Line:** 1057748

---

#### CombatScene

**Line:** 1056888

**Fields:**

- `Entities`: Entities
- `EntitiesToDestroy`: List<BasicEntity>
- `_newEntities`: List<BasicEntity>
- `DamageInstances`: List<CombatDmg>
- `_skillSystem`: SkillSystem
- `_attackSystem`: AttacksSystem

---

#### CombatSceneCreatedComponent

**Line:** 709035

**Inherits:** IComponent

---

#### CombatSceneReactiveModel

**Line:** 709305

**Inherits:** ReactiveModel

---

#### CombatSkillAutoSkillVisual

**Line:** 731904

**Inherits:** MonoBehaviour

**Fields:**

- `Content`: GameObject
- `AutoText`: TMP_Text
- `Background`: Image
- `Button`: UnityButton
- `_isActive`: bool
- `_autoOn`: string
- `_autoOff`: string

---

#### CombatSkillManagerUiView

**Line:** 731931

**Inherits:** UiUnityView

**Fields:**

- `SkillParent`: Transform
- `CombatSkillVisualPrefab`: CombatSkillVisual
- `CombatSkillAutoSkillVisualPrefab`: CombatSkillAutoSkillVisual

---

#### CombatSkillVisual

**Line:** 731955

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `Icon`: Image
- `ActiveCircle`: Image
- `CooldownCircle`: Image
- `RarityBackground`: Image
- `_rarity`: Rarity

---

#### CombatStateComponent

**Line:** 709045

**Inherits:** IComponent

**Fields:**

- `Value`: CombatState

---

#### CombatStateEventSystem

**Line:** 701726

**Inherits:** ReactiveSystem

---

#### CombatStateListenerComponent

**Line:** 699518

**Inherits:** IComponent

**Fields:**

- `value`: List<ICombatStateListener>

---

#### CombatSyncSystem

**Line:** 708998

**Inherits:** IExecuteSystem

**Fields:**

- `_reactiveCombatManager`: ReactiveCombatManager

---

#### DestroyCombatSceneCreatedGameSystem

**Line:** 703917

**Inherits:** ICleanupSystem

---

#### DoubleAttackComponent

**Line:** 709072

**Inherits:** IComponent

---

#### DoubleAttackEventSystem

**Line:** 701810

**Inherits:** ReactiveSystem

---

#### DoubleAttackListenerComponent

**Line:** 699570

**Inherits:** IComponent

**Fields:**

- `value`: List<IDoubleAttackListener>

---

#### EquippedWeaponIdComponent

**Line:** 710572

**Inherits:** IComponent

**Fields:**

- `Value`: ItemId

---

#### EquippedWeaponIdEventSystem

**Line:** 701915

**Inherits:** ReactiveSystem

---

#### EquippedWeaponIdListenerComponent

**Line:** 699635

**Inherits:** IComponent

**Fields:**

- `value`: List<IEquippedWeaponIdListener>

---

#### GuildWarCombatScene

**Line:** 1069463

---

#### HigherMoraleSkillView

**Line:** 730909

**Inherits:** TemporaryEffectView

**Fields:**

- `_destroyTween`: Tween
- `RingTransform`: Transform
- `GroundCircleTransform`: Transform
- `GroundCircleParentTransform`: Transform
- `ParticleSystem`: ParticleSystem
- `RingHeadOffset`: float

---

#### InventorySkillComponent

**Line:** 730397

**Inherits:** IComponent

---

#### InventorySkillReactiveModel

**Line:** 730644

**Inherits:** ReactiveModel

---

#### LastSkillTabTypeComponent

**Line:** 732594

**Inherits:** IComponent

**Fields:**

- `Value`: SkillTabType

---

#### MeatSkillView

**Line:** 730979

**Inherits:** TemporaryEffectView

**Fields:**

- `_destroyTween`: Tween
- `IconParent`: Transform
- `IconTransform`: Transform
- `_timer`: float
- `pulseMax`: float
- `pulseMin`: float
- `HeadOffset`: float

---

#### MeteoriteSkillView

**Line:** 731061

**Inherits:** GameUnityView

**Fields:**

- `Meteorite`: Transform
- `Explosion`: ParticleSystem
- `MeteoriteImpact`: AudioClip
- `_sequence`: Sequence

---

#### MoraleSkillView

**Line:** 731090

**Inherits:** TemporaryEffectView

**Fields:**

- `_destroyTween`: Tween

---

#### PassiveSkillStatTarget

**Line:** 1077013

**Inherits:** StatTargetBase

---

#### PlayerPvpProfileSkillUiView

**Line:** 727374

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `Skills`: List<PvpProfileSkillVisual>

---

#### PlayerPvpSkillModel

**Line:** 1058577

---

#### PlayerPvpSkillPopupUiView

**Line:** 727581

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `Level`: TMP_Text
- `Background`: Image
- `Name`: TMP_Text
- `SkillDescription`: TMP_Text
- `Passive`: TMP_Text

---

#### PlayerSkillCollectionModel

**Line:** 1075500

---

#### PlayerSkillModel

**Line:** 1075577

---

#### ProjectileEntity

**Line:** 1057033

**Inherits:** BasicEntity

**Fields:**

- `Position`: F64Vec2
- `Velocity`: F64Vec2
- `IsAlly`: bool
- `IsAffectedByGravity`: bool
- `WeaponId`: ItemId
- `TargetPos`: F64Vec2
- `Radius`: F64
- `Speed`: F64
- `Destroyed`: bool
- `TargetId`: int
- `CollidedWithId`: int
- `Duration`: F64
- `Timer`: F64
- `IsFromSkill`: bool
- `Skill`: CombatSkill
- `SourceStats`: CombatStats

---

#### ProjectileInfo

**Line:** 1050768

**Inherits:** IGameConfigData

---

#### ProjectileItem

**Line:** 713671

**Inherits:** MonoBehaviour

**Fields:**

- `IsAffectedByGravity`: bool
- `AlignToVelocity`: bool
- `ProjectileSpeed`: float
- `HitRadius`: float
- `Rotates`: bool
- `RotationSpeed`: float

---

#### ProjectileReactiveModel

**Line:** 709364

**Inherits:** ReactiveModel

---

#### ProjectileTestView

**Line:** 710482

**Inherits:** MonoBehaviour

**Fields:**

- `ProjectileTransform`: Transform
- `_alignWithVelocity`: bool
- `_velocityValue`: Vector2
- `_duration`: float
- `_velocity`: Vector2
- `_position`: Vector2
- `_rotates`: bool
- `_rotationSpeed`: float

---

#### ProjectileView

**Line:** 710507

**Inherits:** GameUnityView

**Fields:**

- `ProjectileTransform`: Transform
- `_alignWithVelocity`: bool
- `_velocityValue`: Vector2
- `_duration`: float
- `_velocity`: Vector2
- `_position`: Vector2
- `_rotates`: bool
- `_rotationSpeed`: float

---

#### PvpCombatScene

**Line:** 1074367

---

#### PvpCombatSkillManagerUiView

**Line:** 727016

**Inherits:** UiUnityView

**Fields:**

- `SkillParent`: Transform
- `CombatSkillVisualPrefab`: PvpCombatSkillVisual

---

#### PvpCombatSkillVisual

**Line:** 727039

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `ActiveCircle`: Image
- `CooldownCircle`: Image
- `RarityBackground`: Image
- `_rarity`: Rarity

---

#### PvpProfileSkillVisual

**Line:** 727737

**Inherits:** MonoBehaviour

**Fields:**

- `Visual`: SkillVisual
- `Button`: UnityButton

---

#### QuickEquipSkillActionUiView

**Line:** 732023

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### QuickEquipSkillsRedDotUiView

**Line:** 732041

**Inherits:** RedDotUiView

---

#### RainOfArrowsSkillView

**Line:** 731112

**Inherits:** GameUnityView

**Fields:**

- `DestroyTime`: float
- `Duration`: float
- `ArrowParticles`: ParticleSystem
- `_sequence`: Sequence
- `_soundSequence`: Sequence

---

#### ReactiveCombatManager

**Line:** 710128

**Inherits:** IDisposable

**Fields:**

- `_currentCombat`: CombatScene

---

#### RemoveDoubleAttackGameSystem

**Line:** 703997

**Inherits:** ICleanupSystem

---

#### SetAutoActivateSkillStateAction

**Line:** 1074735

**Inherits:** PlayerAction

---

#### ShoutSkillView

**Line:** 731189

**Inherits:** TemporaryEffectView

**Fields:**

- `_sequence`: Sequence
- `RingParticles`: ParticleSystem
- `ShoutSound`: AudioClip

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

- `TotalAllyHpBuff`: FD6
- `TotalAllyDmgBuff`: FD6
- `TotalEnemyHpBuff`: FD6
- `TotalEnemyDmgBuff`: FD6

---

#### SkillBuilder

**Line:** 1057188

---

#### SkillCheatSystem

**Line:** 686691

**Inherits:** CheatSystem

---

#### SkillCollectionDetailsOpenButton

**Line:** 732071

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### SkillCollectionReactiveModel

**Line:** 730726

**Inherits:** ReactiveModel

---

#### SkillCollectionReactiveModelComponent

**Line:** 730419

**Inherits:** IComponent

**Fields:**

- `Value`: SkillCollectionReactiveModel

---

#### SkillCollectionUiView

**Line:** 732089

**Inherits:** UiUnityView

**Fields:**

- `SkillsCollectedText`: TMP_Text
- `SkillParent`: Transform
- `_feature`: GameEntity

---

#### SkillCombatSlotsParentUiView

**Line:** 732118

**Inherits:** UiUnityView

**Fields:**

- `Parent`: Transform

---

#### SkillCombatUiView

**Line:** 732133

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton
- `Icon`: Image
- `ActiveCircle`: Image
- `CooldownCircle`: Image
- `RarityBackground`: Image
- `_skill`: GameEntity
- `_fillTween`: Tween

---

#### SkillConfig

**Line:** 1075064

**Inherits:** IGameConfigData

---

#### SkillDetailsUiView

**Line:** 732166

**Inherits:** UiUnityView

**Fields:**

- `SkillName`: TMP_Text
- `SkillDescription`: TMP_Text
- `Passive`: TMP_Text
- `_skill`: GameEntity

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

- `Skill`: CombatSkill
- `IsAlly`: bool
- `IsActive`: bool
- `IsOnCooldown`: bool
- `Timer`: FD6
- `CooldownDuration`: FD6
- `ActiveDuration`: FD6
- `Damage`: FD6
- `Health`: FD6
- `SlotId`: int

---

#### SkillEquipAction

**Line:** 1074766

**Inherits:** PlayerAction

---

#### SkillEquipButtonUiView

**Line:** 732193

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton
- `EquipText`: TMP_Text
- `ButtonImage`: Image
- `_skill`: GameEntity

---

#### SkillEquippedMessage

**Line:** 730550

**Inherits:** IMessage

---

#### SkillInSlotUiSyncSystem

**Line:** 731699

**Inherits:** ReactiveSystem

---

#### SkillInSlotView

**Line:** 732226

**Inherits:** UiUnityView

**Fields:**

- `SkillVisual`: SkillVisual
- `_skill`: GameEntity

---

#### SkillInventorySlotUiView

**Line:** 732251

**Inherits:** UiUnityView

**Fields:**

- `SkillParent`: Transform
- `LockedButton`: UnityButton
- `LockIcon`: GameObject
- `_slot`: GameEntity

---

#### SkillMainMenuTabRedDotUiView

**Line:** 732620

**Inherits:** RedDotUiView

---

#### SkillMaxCheatAction

**Line:** 1074809

**Inherits:** PlayerAction

**Fields:**

- `NumberOfLevels`: int

---

#### SkillPassiveConfig

**Line:** 1075154

**Inherits:** IGameConfigData

---

#### SkillReactiveModelInitializeSystem

**Line:** 731594

**Inherits:** IInitializeSystem

---

#### SkillReactiveModelSyncSystem

**Line:** 731612

**Inherits:** IExecuteSystem

---

#### SkillSlotComponent

**Line:** 730431

**Inherits:** IComponent

---

#### SkillSlotUiComponent

**Line:** 730441

**Inherits:** IComponent

---

#### SkillSlotUiCreateSystem

**Line:** 731659

**Inherits:** ReactiveSystem

---

#### SkillSlotUnlockUpdateSystem

**Line:** 731720

**Inherits:** ReactiveSystem

---

#### SkillSlotsParentUiView

**Line:** 732284

**Inherits:** UiUnityView

**Fields:**

- `Parent`: Transform

---

#### SkillSortSystem

**Line:** 731766

**Inherits:** ReactiveSystem

---

#### SkillStats

**Line:** 1075250

---

#### SkillStatsComponent

**Line:** 730451

**Inherits:** IComponent

**Fields:**

- `Value`: SkillStats

---

#### SkillStatsEventSystem

**Line:** 702631

**Inherits:** ReactiveSystem

---

#### SkillStatsListenerComponent

**Line:** 700077

**Inherits:** IComponent

**Fields:**

- `value`: List<ISkillStatsListener>

---

#### SkillSummonAction

**Line:** 1074895

**Inherits:** PlayerAction

---

#### SkillSummonActionButtonUiView

**Line:** 732299

**Inherits:** ActionButtonUiView

**Fields:**

- `SummonCount`: TMP_Text

---

#### SkillSummonDetailsUiView

**Line:** 732350

**Inherits:** MonoBehaviour

**Fields:**

- `Parent`: Transform
- `Prefab`: SummonUpgradeEntry
- `LabelLevel`: TMP_Text
- `PreviousButton`: UnityButton
- `NextButton`: UnityButton
- `_summonUpgradeEntries`: List<SummonUpgradeEntry>
- `_level`: int

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

#### SkillSystem

**Line:** 1057352

**Fields:**

- `_skillBuffs`: SkillBuffs
- `_random`: PseudoRandom

---

#### SkillTabFeature

**Line:** 732635

**Inherits:** Feature

---

#### SkillTabFeatureInitializeSystem

**Line:** 732644

**Inherits:** IInitializeSystem

---

#### SkillTabRedDotUiView

**Line:** 732380

**Inherits:** RedDotUiView

---

#### SkillTabTypeComponent

**Line:** 732608

**Inherits:** IComponent

**Fields:**

- `Value`: SkillTabType

---

#### SkillTabUiMenuButton

**Line:** 732690

**Inherits:** UiUnityView

**Fields:**

- `Label`: TMP_Text
- `Type`: SkillTabType
- `Button`: UnityButton
- `Selected`: GameObject
- `Unselected`: GameObject
- `RightSideSeparator`: GameObject
- `_sequence`: Sequence

---

#### SkillTabUiView

**Line:** 732720

**Inherits:** UiUnityView

**Fields:**

- `ContentParent`: Transform

---

#### SkillTabsCloseSystem

**Line:** 732659

**Inherits:** ReactiveSystem

---

#### SkillTotalPassiveSyncSystem

**Line:** 731787

**Inherits:** ReactiveSystem

---

#### SkillTypeComponent

**Line:** 730463

**Inherits:** IComponent

**Fields:**

- `Value`: CombatSkill

---

#### SkillUiCreateSystem

**Line:** 731829

**Inherits:** ReactiveSystem

---

#### SkillUiSyncSystem

**Line:** 731850

**Inherits:** ReactiveSystem

---

#### SkillUiView

**Line:** 732395

**Inherits:** UiUnityView

**Fields:**

- `SkillVisual`: SkillVisual
- `_skill`: GameEntity

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

#### SkillUpgradeButtonUiView

**Line:** 732438

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton
- `ButtonImage`: Image
- `_skill`: GameEntity

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

- `Icon`: Image
- `IconCanvasGroup`: CanvasGroup
- `Equip`: GameObject
- `UpgradeArrow`: GameObject
- `Level`: TMP_Text
- `SkillShard`: TMP_Text
- `BackGround`: Image
- `ProgressBar`: Image
- `ProgressObjects`: GameObject
- `MaxedObjects`: GameObject

---

#### SkillVisualConfig

**Line:** 730487

**Inherits:** ScriptableObject

**Fields:**

- `AnimationView`: SummonEntryAnimationView
- `Skills`: SerializableDictionary<CombatSkill, SkillVisualDetails>

---

#### SkillVisualDetails

**Line:** 730501

**Fields:**

- `Icon`: Sprite
- `ShowDuration`: bool
- `ProjectilePrefab`: ProjectileItem
- `SkillAnimation`: GameObject

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

- `_stillLockedSlotsCount`: int

---

#### SkillsSummonedMessage

**Line:** 730577

**Inherits:** IMessage

---

#### SummonSkillsRedDotUiView

**Line:** 732521

**Inherits:** RedDotUiView

---

#### SummonedSkillInfo

**Line:** 1052186

---

#### ThronsSkillView

**Line:** 731308

**Inherits:** GameUnityView

**Fields:**

- `_sequence`: Sequence
- `Stab`: AudioClip

---

#### TotalSkillPassiveUiView

**Line:** 732536

**Inherits:** UiUnityView

**Fields:**

- `_feature`: GameEntity
- `PassiveText`: TMP_Text

---

#### UnitProjectileConfig

**Line:** 1057677

**Fields:**

- `Radius`: F64
- `Speed`: F64
- `AffectedByGravity`: bool
- `IsAiming`: bool
- `HandOffset`: F64Vec2
- `WeaponOffset`: F64Vec2
- `IsFromSkill`: bool
- `Skill`: CombatSkill

---

#### UpgradeAllSkillButtonUiView

**Line:** 732558

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton
- `_skills`: IGroup<GameEntity>

---

#### UpgradeSkillsRedDotUiView

**Line:** 732577

**Inherits:** RedDotUiView

---

#### WeaponData

**Line:** 713702

**Fields:**

- `AttackRange`: float
- `WindUpTime`: float
- `AttackTime`: float
- `IsRanged`: bool
- `IsAiming`: bool
- `WeaponOffset`: Vector2
- `HandOffset`: Vector2

---

#### WeaponEquipmentItem

**Line:** 713723

**Inherits:** EquipmentItem

**Fields:**

- `AttackRange`: float
- `IsRanged`: bool
- `IsAiming`: bool
- `ProjectileSpawnPoint`: Transform
- `WeaponData`: WeaponData
- `_tween`: Tween

---

#### WeaponInfo

**Line:** 1050834

**Inherits:** IGameConfigData

---

#### WeaponItemVisualConfig

**Line:** 713751

**Inherits:** EquipmentItemVisualConfig

**Fields:**

- `AnimationController`: AnimatorOverrideController
- `IsDualWield`: bool
- `HasProjectile`: bool
- `ProjectilePrefab`: ProjectileItem
- `HasSecondary`: bool
- `SecondaryPrefab`: SecondaryEquipmentItem
- `AttackSfx`: AttackSfx
- `ImpactSfx`: ImpactSfx

---

#### WeaponStatTarget

**Line:** 1076931

**Inherits:** StatTargetBase

---

#### WormSkillView

**Line:** 731343

**Inherits:** GameUnityView

**Fields:**

- `DestroyTime`: float
- `WormExplosion`: AudioClip
- `WormRoar`: AudioClip
- `_sequence`: Sequence

---

### Enums (5)

#### AttackSfx

**Line:** 705778

**Values:**

- `Punch` = 0
- `SwordSmall` = 1
- `WoodBlunt` = 3
- `Throw` = 4
- `LaserSword` = 5
- `HitBig` = 7
- `QuantumMelee` = 8
- `Rifle` = 10
- `Automatic` = 11
- `Pistol` = 12
- `Shotgun` = 13
- `Silencer` = 14
- `Bow` = 15
- `LaserGun` = 17
- `Rocket` = 18
- `Magic` = 19
- `Cannon` = 20
- `MachineGun` = 21
- `BixAxe` = 22
- `None` = 99999

---

#### AttackType

**Line:** 1057429

**Values:**

- `None` = 0
- `Skill` = 1
- `Melee` = 2
- `Ranged` = 3

---

#### CombatSkill

**Line:** 1057131

**Values:**

- `Meat` = 0
- `Morale` = 1
- `Arrows` = 2
- `Shuriken` = 3
- `Shout` = 4
- `Meteorite` = 5
- `Berserk` = 6
- `Stampede` = 7
- `Thorns` = 8
- `Bomb` = 9
- `Worm` = 10
- `Lightning` = 11
- `Buff` = 12
- `HigherMorale` = 13
- `RainOfArrows` = 14
- `StrafeRun` = 15
- `CannonBarrage` = 16
- `Drone` = 17

---

#### CombatState

**Line:** 1057418

**Values:**

- `Idle` = 0
- `WindingUp` = 1
- `OnCooldown` = 2

---

#### SkillTabType

**Line:** 732680

**Values:**

- `Skills` = 0
- `Pets` = 1
- `TechTree` = 2

---

## Economy

### Classes (118)

#### AutoForgeCountUiView

**Line:** 715032

**Inherits:** UiUnityView

**Fields:**

- `ForgeCountText`: TMP_Text
- `_forge`: GameEntity

---

#### AutoForgeEntry

**Line:** 715057

**Inherits:** MonoBehaviour

**Fields:**

- `AgeIcon`: Image
- `AgeBackgroundParent`: Transform
- `AgeLabel`: TMP_Text
- `CurrentProbabilityLabel`: TMP_Text
- `CheckIcon`: GameObject
- `CheckBoxButton`: UnityButton

---

#### AutoForgeHammerCountPopupUiView

**Line:** 715173

**Inherits:** UiUnityView

**Fields:**

- `AutoForgeHammerPopupEntryPrefab`: AutoForgeHammerPopupEntry
- `Parent`: Transform
- `Target`: Transform
- `Close`: UnityButton
- `Open`: UnityButton
- `OpenArrow`: Image
- `_tween`: Tween

---

#### AutoForgeHammerCountSelectAction

**Line:** 1068151

**Inherits:** PlayerAction

---

#### AutoForgeHammerPopupEntry

**Line:** 715077

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `LockedText`: TMP_Text
- `UnlockedText`: TMP_Text
- `Seperator`: GameObject
- `LockedIcon`: Image

---

#### AutoForgeOpenButtonUiView

**Line:** 715197

**Inherits:** UiUnityView

**Fields:**

- `LockedButton`: UnityButton
- `InactiveButton`: UnityButton
- `ActiveButton`: UnityButton
- `_autoForge`: GameEntity
- `_tween`: Tween

---

#### AutoForgePassiveEntry

**Line:** 715246

**Inherits:** MonoBehaviour

**Fields:**

- `PassiveLabel`: TMP_Text
- `CheckIcon`: GameObject
- `CheckBoxButton`: UnityButton

---

#### AutoForgePopupUiView

**Line:** 715295

**Inherits:** UiUnityView

**Fields:**

- `ForgeUpgradeEntry`: AutoForgeEntry
- `AutoForgePassiveEntry`: AutoForgePassiveEntry
- `AgeEntryParent`: Transform
- `PassiveEntryParent`: Transform
- `FilterToggle`: ColoredToggle
- `FilterToggleButton`: UnityButton
- `PassiveSection`: GameObject
- `_oldKeepAges`: List<int>
- `_oldPassives`: List<SecondaryStatType>

---

#### AutoForgeStartButtonUiView

**Line:** 715338

**Inherits:** UiUnityView

**Fields:**

- `StartButton`: UnityButton

---

#### CheatCurrencyAddAction

**Line:** 1067281

**Inherits:** PlayerAction

---

#### CheatCurrencyRemoveAction

**Line:** 1067324

**Inherits:** PlayerAction

---

#### ConcurrencyCheckAttribute

**Line:** 1508782

**Inherits:** Attribute

---

#### CostButtonUiView

**Line:** 735860

**Inherits:** UiUnityView

**Fields:**

- `PriceButton`: PriceUnityButton
- `DisabledButtonColor`: Color
- `DefaultTextColor`: Color
- `_activeColor`: Color
- `_cost`: long
- `_currency`: long

---

#### CurrencyBonusStatTarget

**Line:** 1077149

**Inherits:** StatTargetBase

---

#### CurrencyChangeMessage

**Line:** 711738

**Inherits:** IMessage

---

#### CurrencyCheatContainer

**Line:** 711544

**Inherits:** AbstractCheatContainer

**Fields:**

- `_useDebugAdService`: bool

---

#### CurrencyCheatSystem

**Line:** 711879

**Inherits:** CheatSystem

---

#### CurrencyComponent

**Line:** 711660

**Inherits:** IComponent

**Fields:**

- `Value`: CurrencyType

---

#### CurrencyEntitasUiView

**Line:** 711975

**Inherits:** UiUnityView

**Fields:**

- `CurrencyType`: CurrencyType
- `CoinLabel`: TextMeshProUGUI
- `ShowIcon`: bool
- `_gameListenerEntity`: GameEntityRef

---

#### CurrencyFeature

**Line:** 711708

**Inherits:** Feature

---

#### CurrencyInitializeSystem

**Line:** 711903

**Inherits:** IInitializeSystem

---

#### CurrencyProgressKey

**Line:** 1078535

**Inherits:** ProgressKeyBase

---

#### CurrencyReward

**Line:** 1078791

**Inherits:** PlayerReward

---

#### CurrencyRewardMessage

**Line:** 728568

**Inherits:** IMessage

---

#### CurrencySyncSystem

**Line:** 711921

**Inherits:** IExecuteSystem

---

#### CurrencyTypeComponent

**Line:** 711673

**Inherits:** IComponent

**Fields:**

- `Value`: CurrencyType

---

#### CurrencyUiView

**Line:** 712002

**Inherits:** MonoBehaviour

**Fields:**

- `CurrencyType`: CurrencyType
- `CoinLabel`: TextMeshProUGUI
- `ShowIcon`: bool

---

#### CurrencyWithParticleUiView

**Line:** 715416

**Inherits:** UiUnityView

**Fields:**

- `CoinLabel`: TextMeshProUGUI
- `CurrencyType`: CurrencyType
- `ParticlePrefab`: LootUiParticleView
- `ParticleParent`: Transform
- `_pool`: Pool<LootUiParticleView>
- `ShowIcon`: bool
- `Format`: bool
- `_gameListenerEntity`: GameEntityRef
- `_sequenceList`: List<Sequence>

---

#### DeductGuildCreationCostAction

**Line:** 1063530

**Inherits:** PlayerSynchronizedServerActionCore

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

#### ForgeCheatContainer

**Line:** 685946

**Inherits:** AbstractCheatContainer

---

#### ForgeCheatSystem

**Line:** 686605

**Inherits:** CheatSystem

**Fields:**

- `_fullEquipAge`: int
- `_incrementalIdx`: int

---

#### ForgeConfig

**Line:** 1068745

**Inherits:** GameConfigKeyValue

---

#### ForgeFeatureInitializeSystem

**Line:** 714861

**Inherits:** IInitializeSystem

---

#### ForgeGemSkipAction

**Line:** 1068445

**Inherits:** PlayerAction

---

#### ForgeGemSkipSystem

**Line:** 714876

**Inherits:** ReactiveSystem

---

#### ForgeLevelMaxCheatAction

**Line:** 1068678

**Inherits:** PlayerAction

---

#### ForgeLevelUiView

**Line:** 715463

**Inherits:** UiUnityView

**Fields:**

- `Level`: TMP_Text
- `_feature`: GameEntityRef

---

#### ForgeLocalizer

**Line:** 720965

**Inherits:** LocalizerBase

---

#### ForgeModelComponent

**Line:** 714620

**Inherits:** IComponent

**Fields:**

- `Value`: ForgeReactiveModel

---

#### ForgeModelInitializeSystem

**Line:** 714897

**Inherits:** IInitializeSystem

**Fields:**

- `_forgeUpgrade`: GameEntity
- `_forge`: GameEntity
- `_forgeGemSkip`: GameEntity

---

#### ForgeModelSyncSystem

**Line:** 714939

**Inherits:** IExecuteSystem

---

#### ForgePopupOpenSystem

**Line:** 714954

**Inherits:** ReactiveSystem

---

#### ForgePushNotificationSystem

**Line:** 714975

**Inherits:** ReactiveSystem

---

#### ForgeReactiveModel

**Line:** 714814

**Inherits:** ReactiveModel

---

#### ForgeRedDotLogic

**Line:** 714670

**Inherits:** IRedDotLogic

**Fields:**

- `_forgeClaimAlreadyMarked`: bool
- `_forgeUpgradeAlreadyMarked`: bool

---

#### ForgeRedDotUiView

**Line:** 715491

**Inherits:** RedDotUiView

---

#### ForgeShineView

**Line:** 715506

**Inherits:** UiUnityView

**Fields:**

- `Anvil`: Image
- `_gameListenerEntity`: GameEntityRef

---

#### ForgeSmallUpgradeTimerUiView

**Line:** 715535

**Inherits:** UiUnityView

**Fields:**

- `TimerText`: TMP_Text
- `_upgradeFeature`: GameEntity

---

#### ForgeStatTarget

**Line:** 1077095

**Inherits:** StatTargetBase

---

#### ForgeStateUiView

**Line:** 714464

**Inherits:** UiUnityView

**Fields:**

- `AnvilView`: AnvilView
- `_forgeFeature`: GameEntity
- `_autoForgeFeature`: GameEntity
- `State`: TMP_Text
- `_timer`: float
- `_itemSoldOpenPending`: bool
- `_state`: ForgeState

---

#### ForgeTierEntry

**Line:** 715563

**Inherits:** MonoBehaviour

**Fields:**

- `TierImage`: Image
- `TierSeperator`: Image
- `_tween`: Tween

---

#### ForgeTierUpgradeAction

**Line:** 1068406

**Inherits:** PlayerAction

---

#### ForgeTierUpgradeActionActionButtonUiView

**Line:** 715593

**Inherits:** ActionButtonUiView

**Fields:**

- `TierUpUpgrade`: TMP_Text

---

#### ForgeTierUpgradedMessage

**Line:** 714726

**Inherits:** IMessage

---

#### ForgeTierView

**Line:** 715623

**Inherits:** MonoBehaviour

**Fields:**

- `_entries`: List<ForgeTierEntry>
- `ForgeTierPrefab`: ForgeTierEntry
- `ForgeTierEntryContainer`: Transform

---

#### ForgeUpgradeActionButtonUiView

**Line:** 715649

**Inherits:** ActionButtonUiView

---

#### ForgeUpgradeButtonUiView

**Line:** 715676

**Inherits:** UiUnityView

**Fields:**

- `LevelUpgradeButtonView`: ForgeUpgradeActionButtonUiView
- `TierUpgradeButtonView`: ForgeTierUpgradeActionActionButtonUiView
- `ForgeTierUpgradeParent`: GameObject
- `_upgradeFeature`: GameEntity
- `Maxed`: TMP_Text

---

#### ForgeUpgradeClaimAction

**Line:** 1068432

**Inherits:** PlayerAction

---

#### ForgeUpgradeClaimSystem

**Line:** 714996

**Inherits:** ReactiveSystem

---

#### ForgeUpgradeClaimUiVIew

**Line:** 715707

**Inherits:** UiUnityView

**Fields:**

- `ClaimButton`: UnityButton
- `_upgradeFeature`: GameEntity

---

#### ForgeUpgradeEntry

**Line:** 715762

**Inherits:** MonoBehaviour

**Fields:**

- `AgeIcon`: Image
- `AgeBackgroundParent`: Transform
- `AgeLabel`: TMP_Text
- `CurrentProbabilityLabel`: TMP_Text
- `NextProbabilityLabel`: TMP_Text
- `NextChanceBackground`: Image
- `_numberAnimation`: Sequence
- `_backGround`: ItemBackgroundView

---

#### ForgeUpgradeLibrary

**Line:** 1051746

**Inherits:** IGameConfigData

---

#### ForgeUpgradePopupUiView

**Line:** 715787

**Inherits:** UiUnityView

**Fields:**

- `ForgeUpgradeEntry`: ForgeUpgradeEntry
- `AgeEntryParent`: Transform
- `CurrentLevelLabel`: TMP_Text
- `Arrow`: GameObject
- `NextLevelLabel`: TMP_Text
- `_forgeFeature`: GameEntity

---

#### ForgeUpgradeSkipUiVIew

**Line:** 715817

**Inherits:** UiUnityView

**Fields:**

- `GemSkipButton`: PriceButtonEntitasUiView
- `FreeSkipButton`: BeveledUnityButton
- `_upgradeFeature`: GameEntity
- `_gemSkip`: GameEntity
- `_forge`: GameEntity

---

#### ForgeUpgradeStartAction

**Line:** 1068419

**Inherits:** PlayerAction

---

#### ForgeUpgradeTimerUiView

**Line:** 715851

**Inherits:** UiUnityView

**Fields:**

- `TimerText`: TMP_Text
- `DescriptionText`: TMP_Text
- `UpgradeInProgressText`: TMP_Text
- `ProgressBar`: Image
- `_upgradeFeature`: GameEntity
- `TimerParent`: GameObject

---

#### ForgeUpgradeUnlockSystem

**Line:** 715017

**Inherits:** IExecuteSystem

---

#### ForgeUpgradedMessage

**Line:** 714746

**Inherits:** IMessage

---

#### ForgedItemUiView

**Line:** 713969

**Inherits:** UiUnityView

**Fields:**

- `OldItemVisuals`: List<GameObject>
- `EquipButton`: UnityButton
- `SellButton`: UnityButton
- `CloseButton`: UnityButton
- `OldItemVisual`: ItemVisual
- `NewItemVisual`: ItemVisual
- `_currentItem`: PlayerItemModel
- `_oldItem`: PlayerItemModel

---

#### FreeForgeProcUiView

**Line:** 714513

**Inherits:** MonoBehaviour

**Fields:**

- `FreeForgeProcEffectPrefab`: TMP_Text

---

#### IdleAnimationUiView

**Line:** 720634

**Inherits:** UiUnityView

**Fields:**

- `ZZZPrefab`: GameObject

---

#### IdleCashCollectAction

**Line:** 1069799

**Inherits:** PlayerAction

---

#### IdleCashFeature

**Line:** 720577

**Inherits:** Feature

---

#### IdleCashInitializeSystem

**Line:** 720604

**Inherits:** IInitializeSystem

---

#### IdleCashRedDotLogic

**Line:** 720586

**Inherits:** IRedDotLogic

---

#### IdleCashUiView

**Line:** 720649

**Inherits:** UiUnityView

**Fields:**

- `Collect`: UnityButton
- `CollectButtonImage`: Image
- `RewardText`: TMP_Text
- `IdleTimeText`: TMP_Text
- `HammerRateText`: TMP_Text
- `HammerRateImage`: Image
- `CoinRateText`: TMP_Text
- `CoinRateImage`: Image
- `_smoothingTimer`: float
- `_timeStep`: float
- `_previousSeconds`: FD6
- `_previousMinutes`: FD6
- `_lastCoins`: FD6
- `_lastHammers`: FD6
- `_maxSeconds`: FD6

---

#### IdleCashUnlockSystem

**Line:** 720619

**Inherits:** IExecuteSystem

---

#### IdleConfig

**Line:** 1069812

**Inherits:** GameConfigKeyValue

---

#### IdleRewardRedDotUiView

**Line:** 720711

**Inherits:** RedDotUiView

---

#### IdleRewardSource

**Line:** 1069960

**Inherits:** IRewardSource

---

#### OfflineCurrencyStatTarget

**Line:** 1077212

**Inherits:** StatTargetBase

---

#### OnItemForgedMessage

**Line:** 714787

**Inherits:** IMessage

---

#### OpenShopButtonUiView

**Line:** 712025

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### OpenShopButtonView

**Line:** 712043

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `ScrollToSection`: bool
- `Category`: ShopCategories

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

#### Price

**Line:** 1406757

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `value`: Decimal
- `num`: double

---

#### PriceButtonEntitasUiView

**Line:** 712064

**Inherits:** MonoBehaviour

**Fields:**

- `PriceButton`: PriceUnityButton
- `DisabledButtonColor`: Color
- `_activeColor`: Color
- `_defaultTextColor`: Color
- `_priceEntity`: GameEntity
- `_inactiveColor`: Color
- `_contexts`: Contexts

---

#### PriceButtonUiView

**Line:** 712195

**Inherits:** MonoBehaviour

**Fields:**

- `PriceButton`: PriceUnityButton
- `HasIcon`: bool
- `HasTitle`: bool
- `Icon`: Image
- `Title`: TMP_Text
- `LoadingIndicator`: GameObject
- `ButtonContent`: GameObject
- `ActiveButtonColor`: Color
- `InActiveButtonColor`: Color
- `ActiveTextColor`: Color
- `InactiveTextColor`: Color
- `_isAffordable`: Func<bool>
- `_isDisabled`: Func<bool>
- `_onBought`: Action
- `_onMessageReceived`: Action

---

#### PriceComponent

**Line:** 711686

**Inherits:** IComponent

**Fields:**

- `Value`: long

---

#### PriceEventSystem

**Line:** 702526

**Inherits:** ReactiveSystem

---

#### PriceListenerComponent

**Line:** 700012

**Inherits:** IComponent

**Fields:**

- `value`: List<IPriceListener>

---

#### PriceUnityButton

**Line:** 735992

**Inherits:** MonoBehaviour

**Fields:**

- `ButtonImage`: Image
- `PriceLabel`: TMP_Text
- `Button`: UnityButton

---

#### SelectedAutoForgeCountUiView

**Line:** 715923

**Inherits:** UiUnityView

**Fields:**

- `_forge`: GameEntity
- `Count`: TMP_Text

---

#### ShopButtonTabRedDotUiView

**Line:** 729896

**Inherits:** RedDotUiView

---

#### ShopFeature

**Line:** 729863

**Inherits:** Feature

---

#### ShopFeatureInitializeSystem

**Line:** 730200

**Inherits:** IInitializeSystem

---

#### ShopLocalizer

**Line:** 721305

**Inherits:** LocalizerBase

---

#### ShopResourceBuySystem

**Line:** 730215

**Inherits:** ReactiveSystem

---

#### ShopResourceId

**Line:** 1066604

**Inherits:** StringId

---

#### ShopResourceIdComponent

**Line:** 729726

**Inherits:** IComponent

**Fields:**

- `Value`: ShopResourceId

---

#### ShopResourceUiView

**Line:** 730284

**Inherits:** UiUnityView

**Fields:**

- `Icon`: Image
- `Reward`: TMP_Text
- `BuyButton`: PriceButtonEntitasUiView
- `_shopResource`: GameEntity

---

#### ShopResourceViewCreateSystem

**Line:** 730272

**Inherits:** ShopViewEntryCreateSystem

---

#### ShopResourcesInitializeSystem

**Line:** 730236

**Inherits:** IInitializeSystem

---

#### ShopResourcesLibrary

**Line:** 1066614

**Inherits:** IGameConfigData

---

#### ShopUiView

**Line:** 729962

**Inherits:** UiUnityView

**Fields:**

- `GemPackParent`: RectTransform
- `TokenPacksParent`: RectTransform
- `ResourcesParent`: RectTransform
- `DailyDealParent`: RectTransform
- `TokenPacksBanner`: GameObject
- `ResourcesBanner`: GameObject
- `ScrollRect`: ScrollRect
- `ScrollSpeed`: float

---

#### ShopViewEntryCreateSystem

**Line:** 729872

**Inherits:** ReactiveSystem

---

#### ShopVisualConfig

**Line:** 729739

**Inherits:** ScriptableObject

**Fields:**

- `GemsIcons`: SerializableDictionary<string, Sprite>
- `TokenPackIcons`: SerializableDictionary<string, Sprite>
- `ResourceIcons`: SerializableDictionary<string, ResourceItem>
- `DailyDealIcons`: SerializableDictionary<DailyDealType, Sprite>

---

#### TryForgeComponent

**Line:** 714332

**Inherits:** IComponent

---

#### TryForgeUiView

**Line:** 714592

**Inherits:** UiUnityView

**Fields:**

- `ForgeButton`: AnvilButtonView

---

### Enums (4)

#### CurrencyType

**Line:** 1067355

**Values:**

- `Coins` = 0
- `Gems` = 1
- `Hammers` = 2
- `SkillSummonTickets` = 3
- `TechPotions` = 4
- `PvpTickets` = 5
- `ClockWinders` = 6
- `WarBattleTickets` = 7
- `Token` = 8

---

#### ForgeState

**Line:** 714632

**Values:**

- `Idle` = 0
- `StartForgingAnimation` = 1
- `ForgingAnimation` = 2
- `ForgingAnimationComplete` = 3
- `ItemsForged` = 4

---

#### ParticleSystemBakeMeshOptions

**Line:** 1577997

**Values:**

- `BakeRotationAndScale` = 1
- `BakePosition` = 2
- `Default` = 0

---

#### ShopCategories

**Line:** 729911

**Values:**

- `Gems` = 0
- `Resources` = 1
- `DailyDeals` = 2
- `TokenPacks` = 3

---

## Guild

### Classes (360)

#### AfterWarPanelUiView

**Line:** 719440

**Inherits:** MonoBehaviour

---

#### AnyWarRewardRedDotUiView

**Line:** 719449

**Inherits:** RedDotUiView

---

#### CallerMemberNameAttribute

**Line:** 231115

**Inherits:** Attribute

---

#### ChatGuildMessageVisual

**Line:** 707720

**Inherits:** MonoBehaviour

**Fields:**

- `MessageText`: TMP_Text
- `TimeText`: TMP_Text

---

#### ChatJoinedGuildAction

**Line:** 1058864

**Inherits:** PlayerSynchronizedServerActionCore

---

#### CheatRewardSource

**Line:** 1075730

**Inherits:** IRewardSource

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

#### CultureAwareComparer

**Line:** 57624

**Inherits:** StringComparer

**Fields:**

- `_options`: CompareOptions

---

#### CurrentGuildEmblemView

**Line:** 717495

**Inherits:** MonoBehaviour

**Fields:**

- `_display`: GuildEmblemDisplay

---

#### DailyDealReward

**Line:** 1078921

**Inherits:** PlayerReward

---

#### DailyDealRewardProxy

**Line:** 1078962

**Inherits:** PlayerReward

---

#### DailyRewardEntryVisual

**Line:** 730079

**Inherits:** MonoBehaviour

**Fields:**

- `RewardText`: TMP_Text

---

#### DailyRewardView

**Line:** 730091

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `TitleText`: TMP_Text
- `BuyButton`: UnityButton
- `PriceText`: TMP_Text
- `RewardPrefab`: DailyRewardEntryVisual
- `RewardsParent`: Transform
- `RewardOrigin`: Transform
- `_dailyDealModel`: DailyDealModel
- `_productId`: InAppProductId
- `_dealSize`: int

---

#### DataMemberAttribute

**Line:** 1596469

**Inherits:** Attribute

**Fields:**

- `name`: string
- `order`: int
- `isRequired`: bool
- `emitDefaultValue`: bool

---

#### DebugGuildSetTierPointsAction

**Line:** 1064331

**Inherits:** GuildActionCore

---

#### DefaultGuildSearchParams

**Line:** 569956

**Inherits:** GuildSearchParamsBase

---

#### DefaultMemberAttribute

**Line:** 265264

**Inherits:** Attribute

---

#### DeleteMemberBinder

**Line:** 1300051

**Inherits:** DynamicMetaObjectBinder

---

#### DivisionPlayerRewardsBase

**Line:** 564841

**Inherits:** IDivisionRewards

---

#### DivisionRewardClaimResult

**Line:** 565357

**Fields:**

- `DivisionIndex`: DivisionIndex
- `GrantedRewards`: IDivisionRewards

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

#### DungeonsRewardUiView

**Line:** 713019

**Inherits:** UiUnityView

**Fields:**

- `_dungeon`: GameEntity
- `RewardText`: TMP_Text
- `RewardAmountText`: TMP_Text
- `EggText`: TMP_Text
- `EggInfoButton`: UnityButton

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

#### EntityKeyMemberConverter

**Line:** 1048513

**Inherits:** JsonConverter

---

#### EnumMemberAttribute

**Line:** 1596500

**Inherits:** Attribute

**Fields:**

- `value`: string
- `isValueSetExplicitly`: bool

---

#### FailingActionWarningListener

**Line:** 605134

---

#### ForeignGuildContext

**Line:** 567644

---

#### ForfeitGuildWarBattleAction

**Line:** 1069049

**Inherits:** PlayerAction

---

#### ForwardLights

**Line:** 918856

**Fields:**

- `m_AdditionalLightsBufferId`: int
- `m_AdditionalLightsIndicesId`: int
- `m_MixedLightingSetup`: MixedLightingSetup
- `m_UseStructuredBuffer`: bool
- `m_UseForwardPlus`: bool
- `m_DirectionalLightCount`: int
- `m_ActualTileWidth`: int
- `m_TileResolution`: int2
- `m_CullingHandle`: JobHandle
- `m_ZBins`: NativeArray<uint>
- `m_ZBinsBuffer`: GraphicsBuffer
- `m_TileMasks`: NativeArray<uint>
- `m_TileMasksBuffer`: GraphicsBuffer
- `m_LightCookieManager`: LightCookieManager
- `m_ReflectionProbeManager`: ReflectionProbeManager
- `m_WordsPerTile`: int
- `m_ZBinScale`: float
- `m_ZBinOffset`: float
- `m_LightCount`: int
- `m_BinCount`: int

---

#### ForwardRendererData

**Line:** 907249

**Inherits:** ScriptableRendererData

**Fields:**

- `postProcessData`: PostProcessData
- `m_OpaqueLayerMask`: LayerMask
- `m_TransparentLayerMask`: LayerMask
- `m_DefaultStencilState`: StencilStateData
- `m_ShadowTransparentReceive`: bool
- `m_RenderingMode`: RenderingMode
- `m_DepthPrimingMode`: DepthPrimingMode
- `m_AccurateGbufferNormals`: bool
- `m_ClusteredRendering`: bool
- `m_TileSize`: TileSize

---

#### GetGuildWarBrawlRequest

**Line:** 1064591

**Inherits:** MetaRequest

---

#### GetGuildWarBrawlResponse

**Line:** 1064619

**Inherits:** MetaResponse

**Fields:**

- `BattleModel`: GuildWarBattleModel

---

#### GetMemberBinder

**Line:** 1300787

**Inherits:** DynamicMetaObjectBinder

---

#### GetMemberDelegate

**Line:** 531329

---

#### GuildActionBase

**Line:** 567671

**Inherits:** ModelAction

**Fields:**

- `InvokingPlayerId`: EntityId

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

- `Success`: bool
- `Error`: string

---

#### GuildAgeGateView

**Line:** 717599

**Inherits:** MonoBehaviour

**Fields:**

- `Target`: GameObject

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

- `PlayerId`: EntityId
- `Role`: GuildMemberRole

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

#### GuildCreateView

**Line:** 717713

**Inherits:** MonoBehaviour

**Fields:**

- `_closeButton`: UnityButton
- `_guildEmblemDisplay`: GuildEmblemDisplay
- `_guildNameInput`: TMP_InputField
- `_guildTagInput`: TMP_InputField
- `_editGuildNameButton`: UnityButton
- `_editGuildTagButton`: UnityButton
- `_editGuildEmblemButton`: UnityButton
- `_editGuildJoinSettingButton`: UnityButton
- `_createButton`: PriceUnityButton
- `_guildNameAlreadyExistsText`: GameObject
- `_tagNotUniqueText`: GameObject
- `_badWordText`: TMP_Text
- `_internalErrorText`: GameObject
- `_nameRulesViolationText`: GameObject
- `_tagRulesViolationText`: GameObject
- `_openJoinText`: GameObject
- `_approvalJoinText`: GameObject
- `_guildEmblemInfo`: GuildEmblemInfo
- `_guildJoinSetting`: GuildJoinSetting
- `_createRunning`: bool

---

#### GuildCreationData

**Line:** 1063839

---

#### GuildCreationFailedMessage

**Line:** 1063993

**Inherits:** MetaMessage

**Fields:**

- `FailedReason`: GuildCreationFailedEnum

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

#### GuildDayPointsScoreUiView

**Line:** 719654

**Inherits:** MonoBehaviour

**Fields:**

- `PointsLeft`: TMP_Text
- `PointsRight`: TMP_Text
- `_warManager`: GuildWarManager

---

#### GuildDiscoveryEntryButtonsView

**Line:** 717807

**Inherits:** MonoBehaviour

**Fields:**

- `_fullText`: TMP_Text
- `_requestSentText`: TMP_Text
- `_joinButton`: UnityButton
- `_requestJoinButton`: UnityButton
- `_guildInfo`: GuildDiscoveryInfo
- `_joinCallback`: Action<GuildDiscoveryInfo>
- `_requestJoinCallback`: Action<GuildDiscoveryInfo>

---

#### GuildDiscoveryEntryView

**Line:** 717857

**Inherits:** MonoBehaviour

**Fields:**

- `_guildInfoView`: GuildInfoView
- `_buttonsView`: GuildDiscoveryEntryButtonsView

---

#### GuildDiscoveryInfo

**Line:** 1062766

**Inherits:** GuildDiscoveryInfoBase

---

#### GuildDiscoveryInfoBase

**Line:** 567578

**Fields:**

- `GuildId`: EntityId
- `DisplayName`: string
- `NumMembers`: int
- `MaxNumMembers`: int

---

#### GuildDiscoveryRequest

**Line:** 571146

**Inherits:** MetaMessage

---

#### GuildDiscoveryResponse

**Line:** 571156

**Inherits:** MetaMessage

**Fields:**

- `GuildInfos`: List<GuildDiscoveryInfoBase>

---

#### GuildDiscoveryView

**Line:** 717957

**Inherits:** UiUnityView

**Fields:**

- `_searchText`: TMP_InputField
- `_searchTextBackground`: Image
- `_searchButton`: UnityButton
- `_createGuildButton`: UnityButton
- `_noGuildsFoundObject`: GameObject
- `_guildsCooldownText`: TMP_Text
- `_searchResultParent`: GameObject
- `_guildDiscoveryEntryPrefab`: GuildDiscoveryEntryView
- `_searchSpinner`: GameObject
- `_runningActions`: bool
- `_guildManager`: GuildManager
- `tks`: CancellationTokenSource

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

- `_shapeImage`: Image
- `_iconImage`: Image
- `_handleImage`: Image

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

- `MeleeCountGuild1`: int
- `RangedCountGuild1`: int
- `MeleeCountGuild2`: int
- `RangedCountGuild2`: int
- `AnchorX`: float
- `Spacing`: float
- `Flip`: bool

---

#### GuildGlobalLeaderboardEntryUiView

**Line:** 718125

**Inherits:** MonoBehaviour

**Fields:**

- `RankIcon`: Image
- `Rank`: TMP_Text
- `Background`: UnityUiElement
- `_guildInfoView`: GuildInfoView
- `_guildInfo`: GuildDiscoveryInfo

---

#### GuildGlobalLeaderboardUiView

**Line:** 718195

**Inherits:** MonoBehaviour

**Fields:**

- `EntryParent`: Transform
- `EntryUiPrefab`: GuildGlobalLeaderboardEntryUiView
- `Loading`: GameObject
- `ServerText`: TMP_Text
- `tks`: CancellationTokenSource

---

#### GuildHiddenAction

**Line:** 572162

**Inherits:** GuildActionBase

---

#### GuildInfoButtonUiView

**Line:** 718236

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `_guildInfo`: GuildDiscoveryInfo

---

#### GuildInfoPopupView

**Line:** 718292

**Inherits:** MonoBehaviour

**Fields:**

- `_guildInfoView`: GuildInfoView
- `_memberListView`: GuildMemberListView
- `_loading`: GameObject

---

#### GuildInfoView

**Line:** 718382

**Inherits:** MonoBehaviour

**Fields:**

- `_emblemDisplay`: GuildEmblemDisplay
- `_guildNameText`: TMP_Text
- `_guildTierText`: TMP_Text
- `_guildServerText`: TMP_Text
- `_totalPowerText`: TMP_Text
- `_memberCountText`: TMP_Text
- `_button`: UnityButton

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

- `Type`: GuildInviteType
- `CreatedAt`: MetaTime
- `ExpiresAfter`: Nullable<MetaDuration>
- `NumMaxUsages`: int
- `NumTimesUsed`: int
- `InviteCode`: GuildInviteCode

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

- `PlayerInfo`: PlayerInfo
- `RequestTime`: MetaTime

---

#### GuildJoinRequestView

**Line:** 718522

**Inherits:** MonoBehaviour

**Fields:**

- `ApproveButton`: UnityButton
- `DismissButton`: UnityButton
- `_miniProfileView`: PlayerMiniProfileUiView
- `_joinRequest`: GuildJoinRequestObject

---

#### GuildJoinRequestsPopupView

**Line:** 718494

**Inherits:** MonoBehaviour

**Fields:**

- `_requestPrefab`: GuildJoinRequestView
- `_requestsParent`: Transform
- `_context`: UiContext
- `tks`: CancellationTokenSource
- `fetchTks`: CancellationTokenSource

---

#### GuildJoinRequestsRedDotUiView

**Line:** 719680

**Inherits:** RedDotUiView

---

#### GuildJoinResponse

**Line:** 571064

**Inherits:** MetaMessage

---

#### GuildLeaguesEnabledCondition

**Line:** 566161

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### GuildLeaveRequest

**Line:** 570806

**Inherits:** MetaMessage

---

#### GuildManager

**Line:** 716671

**Inherits:** IDisposable

**Fields:**

- `_guildCreationErrorTcs`: TaskCompletionSource<GuildCreationFailedEnum>
- `OnGuildUpdated`: Action

---

#### GuildMemberAdd

**Line:** 571857

**Inherits:** GuildActionBase

---

#### GuildMemberBase

**Line:** 568802

**Fields:**

- `IsOnline`: bool
- `LastOnlineAt`: MetaTime
- `DisplayName`: string
- `LastGuildOpEpoch`: int
- `LastPendingPlayerOpEpoch`: int
- `PendingPlayerOps`: MetaDictionary<int, GuildMemberPlayerOpLogEntry>
- `MemberInstanceId`: int
- `Role`: GuildMemberRole
- `Invites`: MetaDictionary<int, GuildInviteState>

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

#### GuildMemberInfoView

**Line:** 718849

**Inherits:** MonoBehaviour

**Fields:**

- `_view`: GuildMemberView
- `_roleEditButton`: UnityButton
- `_kickButton`: UnityButton
- `_leaveButton`: UnityButton
- `_closeButton`: UnityButton
- `_guildMember`: GuildMemberModel
- `_guildManager`: GuildManager
- `_isWaiting`: bool

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

- `PlayerId`: EntityId
- `KickReason`: IGuildMemberKickReason

---

#### GuildMemberKickResponse

**Line:** 1063663

**Inherits:** MetaResponse

---

#### GuildMemberListView

**Line:** 718944

**Inherits:** MonoBehaviour

**Fields:**

- `_guildMemberView`: GuildMemberView
- `_roleSeparatorPrefab`: RoleView
- `_contentParent`: Transform

---

#### GuildMemberModel

**Line:** 1062976

**Inherits:** GuildMemberBase

**Fields:**

- `PlayerInfo`: PlayerInfo

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

#### GuildMemberRoleAssignmentView

**Line:** 719043

**Inherits:** MonoBehaviour

**Fields:**

- `_toggleGroup`: ToggleGroup
- `_roleTogglePrefab`: RoleAssignmentToggle
- `_toggleParent`: Transform
- `_toggleBlockingOverlay`: GameObject
- `_cancelButton`: UnityButton
- `_confirmButton`: UnityButton
- `_transferLeadershipButton`: UnityButton
- `_memberView`: GuildMemberView
- `_startRole`: GuildMemberRole
- `_selectedRole`: GuildMemberRole
- `_guildMember`: GuildMemberModel
- `_guildManager`: GuildManager
- `_isWaiting`: bool
- `_canPlaySounds`: bool

---

#### GuildMemberRolesUpdate

**Line:** 572078

**Inherits:** GuildActionBase

---

#### GuildMemberTransferLeadershipRequest

**Line:** 1063561

**Inherits:** MetaRequest

**Fields:**

- `PlayerId`: EntityId

---

#### GuildMemberTransferLeadershipResponse

**Line:** 1063589

**Inherits:** MetaResponse

---

#### GuildMemberView

**Line:** 719167

**Inherits:** MonoBehaviour

**Fields:**

- `_miniProfileView`: PlayerMiniProfileUiView
- `_roleText`: TMP_Text
- `_bgImage`: Image
- `_onClickCallback`: Action<IGuildMemberInfo>
- `_memberInfo`: IGuildMemberInfo
- `_isPlayer`: bool

---

#### GuildMembersFeatureInitializeSystem

**Line:** 717405

**Inherits:** IInitializeSystem

---

#### GuildMembersFeatureUnlockSystem

**Line:** 717420

**Inherits:** IExecuteSystem

---

#### GuildMembersTabView

**Line:** 719111

**Inherits:** UiUnityView

**Fields:**

- `GuildInfoView`: GuildInfoView
- `AnnouncementText`: TMP_InputField
- `EditAnnouncementButton`: UnityButton
- `AcceptAnnouncementEditButton`: UnityButton
- `CancelAnnouncementEditButton`: UnityButton
- `ShowRolesButton`: UnityButton
- `OpenClanSettingsButton`: UnityButton
- `MemberListView`: GuildMemberListView
- `_isEditingAnnouncement`: bool

---

#### GuildMessageCodes

**Line:** 1058007

---

#### GuildMissionsFeatureInitializeSystem

**Line:** 717435

**Inherits:** IInitializeSystem

---

#### GuildModel

**Line:** 1063149

**Inherits:** GuildModelBase

**Fields:**

- `ApprovedInFlightRequests`: HashSet<EntityId>

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

- `IssuedAt`: MetaTime
- `ReasonOrNull`: IGuildMemberKickReason
- `PendingPlayerOps`: MetaDictionary<int, GuildMemberPlayerOpLogEntry>
- `MemberInstanceId`: int

---

#### GuildRedDotLogic

**Line:** 719378

**Inherits:** IRedDotLogic

**Fields:**

- `_cachedJoinRequests`: HashSet<GuildJoinRequestObject>

---

#### GuildRequirementsValidator

**Line:** 569886

**Inherits:** IMetaIntegrationSingleton

---

#### GuildRevokeInvitationRequest

**Line:** 571602

**Inherits:** MetaMessage

---

#### GuildSearchParamsBase

**Line:** 569924

**Inherits:** IMetaIntegrationConstructible

---

#### GuildSearchRequest

**Line:** 571173

**Inherits:** MetaMessage

**Fields:**

- `SearchParams`: GuildSearchParamsBase

---

#### GuildSearchResponse

**Line:** 571189

**Inherits:** MetaMessage

**Fields:**

- `IsError`: bool
- `GuildInfos`: List<GuildDiscoveryInfoBase>

---

#### GuildSetCurrentDivision

**Line:** 1064884

**Inherits:** GuildActionCore

---

#### GuildSettingsPopupView

**Line:** 718617

**Inherits:** MonoBehaviour

**Fields:**

- `_editGuildJoinSettingButton`: UnityButton
- `_openJoinText`: GameObject
- `_approvalJoinText`: GameObject
- `_openJoinRequestsButton`: UnityButton
- `_guildNameInput`: TMP_InputField
- `_guildTagInput`: TMP_InputField
- `_guildJoinSetting`: GuildJoinSetting

---

#### GuildSwitchedMessage

**Line:** 571106

**Inherits:** MetaMessage

---

#### GuildTabCloseOnNoGuildSystem

**Line:** 718728

**Inherits:** IExecuteSystem

---

#### GuildTabFeature

**Line:** 718719

**Inherits:** Feature

---

#### GuildTabFeatureInitializeSystem

**Line:** 718743

**Inherits:** IInitializeSystem

---

#### GuildTabRedDotUiView

**Line:** 718657

**Inherits:** RedDotUiView

---

#### GuildTabTypeComponent

**Line:** 718693

**Inherits:** IComponent

**Fields:**

- `Value`: GuildTabType

---

#### GuildTabUiMenuButton

**Line:** 719212

**Inherits:** UiUnityView

**Fields:**

- `Label`: TMP_Text
- `Type`: GuildTabType
- `Button`: UnityButton
- `SelectedHighlight`: GameObject
- `UnselectedHighlight`: GameObject
- `RightSideSeparator`: GameObject
- `_sequence`: Sequence

---

#### GuildTabUiView

**Line:** 719242

**Inherits:** UiUnityView

**Fields:**

- `ContentParent`: Transform

---

#### GuildTabsCloseSystem

**Line:** 718758

**Inherits:** ReactiveSystem

---

#### GuildTierConfig

**Line:** 1062465

**Inherits:** IGameConfigData

---

#### GuildTierRewardsPopupUiView

**Line:** 719695

**Inherits:** MonoBehaviour

**Fields:**

- `TitleText`: TMP_Text
- `WinRewards`: ArenaRewardGridVisual
- `LoseRewards`: ArenaRewardGridVisual
- `InfoButton`: UnityButton
- `_warManager`: GuildWarManager

---

#### GuildTiersPopupUiView

**Line:** 719717

**Inherits:** MonoBehaviour

**Fields:**

- `TierEntryPrefab`: SummonUpgradeEntry
- `Parent`: RectTransform
- `SubtitleText`: TMP_Text
- `_warManager`: GuildWarManager

---

#### GuildTimelineUpdateMessage

**Line:** 570914

**Inherits:** MetaMessage

---

#### GuildTitansFeatureInitializeSystem

**Line:** 717465

**Inherits:** IInitializeSystem

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

#### GuildWarBannerView

**Line:** 720475

**Inherits:** MonoBehaviour

**Fields:**

- `_shapeImage`: SpriteRenderer
- `_iconImage`: SpriteRenderer
- `_handleImage`: SpriteRenderer

---

#### GuildWarBattleGuildModel

**Line:** 1069088

---

#### GuildWarBattleHistory

**Line:** 1065567

---

#### GuildWarBattleMapSystem

**Line:** 710404

**Inherits:** ReactiveSystem

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

#### GuildWarBattleSyncSystem

**Line:** 720451

**Inherits:** IExecuteSystem

**Fields:**

- `_state`: PvpBattleState
- `_transitionTimer`: float
- `_transitioning`: bool

---

#### GuildWarBattleTimerUiView

**Line:** 720495

**Inherits:** UiUnityView

**Fields:**

- `TimerText`: TMP_Text
- `ProgressBar`: Image
- `ClockHandAnimation`: ClockHandAnimation

---

#### GuildWarBattleUi

**Line:** 720515

**Inherits:** MonoBehaviour

**Fields:**

- `Guild1Name`: TMP_Text
- `Guild2Name`: TMP_Text
- `Guild1Power`: TMP_Text
- `Guild2Power`: TMP_Text

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

- `InputField`: TMP_InputField
- `InfoText`: TMP_Text
- `FlipButton`: UnityToggleButton
- `FetchButton`: UnityButton
- `StartButton`: UnityButton

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

- `_clientListener`: IDivisionModelClientListenerCore
- `_serverListener`: IDivisionModelServerListenerCore
- `BrawlState`: GuildWarBrawlState

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

#### GuildWarLastDayUiView

**Line:** 719758

**Inherits:** MonoBehaviour

**Fields:**

- `AttackButton`: UnityButton
- `BrawlText`: TMP_Text
- `WarEndedText`: TMP_Text
- `ReplayBrawlButton`: UnityButton
- `WinAllOutBrawlActionEntry`: DayActionEntryUiView
- `_warManager`: GuildWarManager

---

#### GuildWarLeaveButtonUiView

**Line:** 720533

**Inherits:** MonoBehaviour

**Fields:**

- `LeaveButton`: BeveledUnityButton

---

#### GuildWarMVPUiView

**Line:** 719794

**Inherits:** MonoBehaviour

**Fields:**

- `MiniProfileUiView`: PlayerMiniProfileUiView
- `MVPContainer`: GameObject
- `Opponent`: bool
- `_warManager`: GuildWarManager

---

#### GuildWarManager

**Line:** 717022

**Inherits:** IMessageReceiver

**Fields:**

- `_playerId`: EntityId

---

#### GuildWarMarkAsGivenTicketAction

**Line:** 1064679

**Inherits:** DivisionActionBase

---

#### GuildWarMemberChallengeInformation

**Line:** 1065025

**Fields:**

- `ChallengedMemberId`: EntityId
- `ChallengedBy`: EntityId
- `ChallengedByGuildId`: EntityId
- `ChallengedByMemberInfo`: GuildMemberDailyScoreContribution
- `DidWin`: bool
- `ChallengeTime`: MetaTime

---

#### GuildWarMemberInfo

**Line:** 1065432

---

#### GuildWarNormalDayUiView

**Line:** 719831

**Inherits:** MonoBehaviour

**Fields:**

- `ActionPrefab`: DayActionEntryUiView
- `ActionsContainer`: RectTransform

---

#### GuildWarOpponentGuildMemberListUiView

**Line:** 719868

**Inherits:** MonoBehaviour

**Fields:**

- `OpponentGuildEntryPrefab`: OpponentGuildEntryUiView
- `EntriesParent`: RectTransform
- `TicketsText`: TMP_Text
- `ResetText`: TMP_Text
- `LogButton`: UnityButton
- `_warManager`: GuildWarManager

---

#### GuildWarPlayerReward

**Line:** 1065391

**Inherits:** DivisionPlayerRewardsBase

---

#### GuildWarProgressBarUiView

**Line:** 719894

**Inherits:** MonoBehaviour

**Fields:**

- `RightWarProgress`: RectTransform
- `LeftWarProgress`: RectTransform
- `LeftWarProgressText`: TMP_Text
- `RightWarProgressText`: TMP_Text
- `_warManager`: GuildWarManager
- `_lastPercent`: float

---

#### GuildWarSeasonConcludedAnalyticsEvent

**Line:** 1064135

**Inherits:** GuildEventBase

---

#### GuildWarSpinnerUiView

**Line:** 720554

**Inherits:** MonoBehaviour

**Fields:**

- `_tween`: Tween
- `Target`: Transform
- `LoopDuration`: float

---

#### GuildWarTabUiView

**Line:** 719257

**Inherits:** MonoBehaviour

**Fields:**

- `DayContainer`: RectTransform
- `NormalDayPrefab`: GuildWarNormalDayUiView
- `LastDayPrefab`: GuildWarLastDayUiView
- `AfterWarPanelPrefab`: AfterWarPanelUiView
- `MyGuildInfo`: GuildInfoView
- `OpponentGuildInfo`: GuildInfoView
- `ProgressBarArea`: GuildWarProgressBarUiView
- `DayPointsScoreUiView`: GuildDayPointsScoreUiView
- `SubHeader1Text`: TMP_Text
- `SubHeader2Text`: TMP_Text
- `SubHeader3Text`: TMP_Text
- `RightGuildBackground`: Image
- `LeftGuildBackground`: Image
- `RightGuildWarResultText`: TMP_Text
- `LeftGuildWarResultText`: TMP_Text
- `RewardsButton`: UnityButton
- `DaysResultsButton`: UnityButton
- `PreWarPanel`: GameObject
- `FinalizingPanel`: GameObject
- `ContentPanel`: GameObject
- ... (6 more fields)

---

#### GuildWarUpdateBrawlResult

**Line:** 1065001

**Inherits:** DivisionActionBase

**Fields:**

- `BrawlId`: EntityId
- `Result`: PvpBattleResult
- `Winner`: EntityId

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

#### GuildWarsFeatureInitializeSystem

**Line:** 717480

**Inherits:** IInitializeSystem

---

#### GuildsEnabledCondition

**Line:** 569965

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### GuildsFeature

**Line:** 716904

**Inherits:** Feature

---

#### GuildsFeatureInitializeSystem

**Line:** 717450

**Inherits:** IInitializeSystem

---

#### GuildsLocalizer

**Line:** 721023

**Inherits:** LocalizerBase

---

#### IapRewardSource

**Line:** 1066379

**Inherits:** IRewardSource

---

#### IgnoreDataMemberAttribute

**Line:** 1596523

**Inherits:** Attribute

---

#### IgnoreWarningAttribute

**Line:** 1346111

**Inherits:** Attribute

---

#### InGameMailRewardListValidator

**Line:** 561245

**Inherits:** MetaFormValidator

---

#### InvokeMemberBinder

**Line:** 1300855

**Inherits:** DynamicMetaObjectBinder

---

#### InvokeOnMemberDeserializationFailureMethodDelegate

**Line:** 531505

---

#### JsonStringEnumMemberNameAttribute

**Line:** 1008269

**Inherits:** Attribute

---

#### JsonUnmappedMemberHandlingAttribute

**Line:** 1003891

**Inherits:** JsonAttribute

---

#### KeyboardAwareRectTransform

**Line:** 737337

**Inherits:** UiUnityView

**Fields:**

- `InputField`: TMP_InputField
- `OffsetNew`: float
- `MoveSpeed`: float
- `rectTransform`: RectTransform
- `rootCanvas`: RectTransform
- `previousKeyboardHeight`: float
- `isKeyboardVisible`: bool
- `targetHeight`: float
- `_keyboardRoutine`: Coroutine

---

#### LastGuildTabTypeComponent

**Line:** 718707

**Inherits:** IComponent

**Fields:**

- `Value`: GuildTabType

---

#### LegacyMountChestReward

**Line:** 1052444

**Inherits:** PlayerReward

---

#### MemberAccessException

**Line:** 25533

**Inherits:** SystemException

---

#### MemberAssignment

**Line:** 1288310

**Inherits:** MemberBinding

---

#### MemberBinding

**Line:** 1288335

---

#### MemberDescriptor

**Line:** 783624

**Fields:**

- `name`: string
- `displayName`: string
- `nameHash`: int
- `attributeCollection`: AttributeCollection
- `attributesFiltered`: bool
- `attributesFilled`: bool
- `metadataVersion`: int
- `category`: string
- `description`: string
- `lockCookie`: object

---

#### MemberExpression

**Line:** 1288360

**Inherits:** Expression

---

#### MemberFilter

**Line:** 265643

**Inherits:** MulticastDelegate

---

#### MemberInfo

**Line:** 265656

**Inherits:** ICustomAttributeProvider

---

#### MemberInitExpression

**Line:** 1288447

**Inherits:** Expression

---

#### MemberListBinding

**Line:** 1288471

**Inherits:** MemberBinding

---

#### MemberMemberBinding

**Line:** 1288488

**Inherits:** MemberBinding

---

#### MessageRoutingRuleCurrentGuild

**Line:** 499051

**Inherits:** MessageRoutingRule

---

#### MetaAllowNoSerializedMembers

**Line:** 601073

**Inherits:** Attribute

---

#### MetaAllowNonReservedMembersAttribute

**Line:** 600878

**Inherits:** Attribute

---

#### MetaBlockedMembersAttribute

**Line:** 600851

**Inherits:** Attribute

---

#### MetaFormDerivedMembersOnlyAttribute

**Line:** 572466

**Inherits:** Attribute

---

#### MetaForwardingLogger

**Line:** 519671

**Inherits:** MetaLoggerBase

**Fields:**

- `_bufferedEvents`: Queue<MetaForwardingLogger.Event>
- `_flushingBuffer`: Queue<MetaForwardingLogger.Event>
- `_numDroppedFromBuffer`: int
- `_lock`: object
- `_sink`: IMetaLogger
- `_maxBufferSize`: int
- `_autoflushAfter`: TimeSpan
- `_timer`: MetaTimer

---

#### MetaGuildReward

**Line:** 532931

---

#### MetaGuildRewardBase

**Line:** 532917

**Inherits:** MetaReward

---

#### MetaImplicitMembersDefaultRangeForMostDerivedClassAttribute

**Line:** 600808

**Inherits:** Attribute

---

#### MetaImplicitMembersRangeAttribute

**Line:** 600794

**Inherits:** Attribute

---

#### MetaMemberAttribute

**Line:** 600837

**Inherits:** Attribute

---

#### MetaMemberFlagAttribute

**Line:** 600926

**Inherits:** Attribute

---

#### MetaOnMemberDeserializationFailureAttribute

**Line:** 601016

**Inherits:** Attribute

---

#### MetaPlayerReward

**Line:** 532977

---

#### MetaPlayerRewardBase

**Line:** 532963

**Inherits:** MetaReward

---

#### MetaReservedMembersAttribute

**Line:** 600864

**Inherits:** Attribute

---

#### MetaReward

**Line:** 533015

---

#### MetaRewardSourceProvider

**Line:** 533028

**Inherits:** IMetaIntegrationSingleton

---

#### MetaSerializableMember

**Line:** 530197

**Fields:**

- `OnDeserializationFailureMethod`: MethodInfo
- `_resolvedMemberInfo`: MemberInfo

---

#### MetaSerializableMemberDeepCompare

**Line:** 530688

**Inherits:** EqualityComparer

---

#### MissingMemberException

**Line:** 72487

**Inherits:** MemberAccessException

**Fields:**

- `ClassName`: string
- `MemberName`: string

---

#### MultiplayerMemberPrivateStateBase

**Line:** 551826

---

#### NewArrayExpression

**Line:** 1288868

**Inherits:** Expression

---

#### NextWarTimerUiView

**Line:** 719956

**Inherits:** MonoBehaviour

**Fields:**

- `NextWarTimerText`: TMP_Text
- `_warManager`: GuildWarManager

---

#### NotInAGuildException

**Line:** 716865

**Inherits:** Exception

---

#### OpponentGuildEntryUiView

**Line:** 719995

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerProfile`: PlayerMiniProfileUiView
- `AttackButton`: UnityButton
- `DefeatedByText`: TMP_Text
- `PointsToGainText`: TMP_Text
- `TicketsRequiredText`: TMP_Text

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

#### PlayerRewardComponent

**Line:** 729705

**Inherits:** IComponent

**Fields:**

- `Value`: PlayerReward

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

#### PossibleSkinRewardsUiView

**Line:** 734678

**Inherits:** MonoBehaviour

**Fields:**

- `Slots`: List<RectTransform>
- `SkinRewardPrefab`: SkinVisualUiView
- `RewardEntry`: RewardEntryView

---

#### ProgressPassPurchaseReward

**Line:** 1079114

**Inherits:** PlayerReward

---

#### ProgressPassReward

**Line:** 1078641

---

#### ProgressPassRewardClaimedMessage

**Line:** 726423

**Inherits:** IMessage

---

#### ProgressPassRewardSource

**Line:** 1078421

**Inherits:** IRewardSource

---

#### PublicMemberInfo

**Line:** 1584013

---

#### ReflectedMemberProperty

**Line:** 1462209

---

#### RequestGlobalGuildLeaderboard

**Line:** 1067102

**Inherits:** MetaRequest

---

#### RequiredMemberAttribute

**Line:** 888621

**Inherits:** Attribute

---

#### ResolvedPurchaseMetaRewards

**Line:** 584576

**Inherits:** ResolvedPurchaseContentBase

---

#### ResponseGlobalGuildLeaderboardMessage

**Line:** 1067112

**Inherits:** MetaResponse

**Fields:**

- `Leaderboard`: MetaDictionary<EntityId, GuildDiscoveryInfo>

---

#### RewardCheatAction

**Line:** 1079147

**Inherits:** PlayerAction

---

#### RewardCheatSystem

**Line:** 686676

**Inherits:** CheatSystem

---

#### RewardEntryView

**Line:** 726788

**Inherits:** MonoBehaviour

**Fields:**

- `RewardText`: TMP_Text

---

#### RewardFeature

**Line:** 728631

**Inherits:** Feature

---

#### RewardParsers

**Line:** 1052472

**Inherits:** ConfigParserProvider

---

#### RewardParticlesView

**Line:** 728686

**Inherits:** UiUnityView

**Fields:**

- `ParticlePrefab`: RewardUiParticleView
- `Parent`: Transform
- `Origin`: Transform
- `NextOrigin`: Nullable<Vector3>
- `Targets`: List<RewardParticlesView.RewardParticleTarget>
- `_targetsDict`: Dictionary<CurrencyType, Transform>
- `DungeonKeyTarget`: Transform
- `MountTarget`: Transform
- `_particlePool`: Pool<RewardUiParticleView>
- `_gameListener`: GameEntity
- `_sequences`: List<Sequence>

---

#### RewardUiCreateSystem

**Line:** 728640

**Inherits:** IInitializeSystem

---

#### RewardUiParticleView

**Line:** 728746

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image

---

#### RewardVisualConfig

**Line:** 728556

**Inherits:** ScriptableObject

**Fields:**

- `CurrencyIcons`: SerializableDictionary<CurrencyType, Sprite>

---

#### RewardsContainerView

**Line:** 726816

**Inherits:** MonoBehaviour

**Fields:**

- `LockedColor`: Color
- `UnlockedColor`: Color
- `ClaimableColor`: Color
- `ClaimableSecondaryColor`: Color
- `ClaimedColor`: Color
- `ParticleRewardOrigin`: RectTransform
- `RewardsContainer`: RectTransform
- `ContainerBG`: Image
- `TickIcon`: Image
- `LockIcon`: Image
- `RewardButton`: UnityButton
- `RewardEntryPrefab`: RewardEntryView
- `_rewardEntries`: List<RewardEntryView>
- `_claimed`: bool
- `_thresholdReached`: bool
- `_isLocked`: bool
- `_claimAction`: Action
- `_claimableTween`: Tween

---

#### SetMemberBinder

**Line:** 1300906

**Inherits:** DynamicMetaObjectBinder

---

#### SetMemberDelegate

**Line:** 531367

---

#### SkinReward

**Line:** 1052254

**Inherits:** PlayerReward

---

#### SkinRewardEntryView

**Line:** 733146

**Inherits:** MonoBehaviour

**Fields:**

- `SkinVisualUiView`: SkinVisualUiView
- `SkinName`: TMP_Text
- `SkinDescription`: TMP_Text

---

#### StarterPackageReward

**Line:** 1079189

**Inherits:** PlayerReward

---

#### SteppingStoneRewardEntryUiView

**Line:** 734759

**Inherits:** MonoBehaviour

**Fields:**

- `RewardGridVisual`: ArenaRewardGridVisual
- `PossibleSkinRewardsPrefab`: PossibleSkinRewardsUiView
- `MajorRewardsParent`: RectTransform
- `NoRewardText`: TMP_Text
- `TileText`: TMP_Text
- `_rewards`: List<PlayerReward>

---

#### SteppingStoneRewardsUiView

**Line:** 734830

**Inherits:** MonoBehaviour

**Fields:**

- `ClaimButton`: UnityButton
- `TitleText`: TMP_Text
- `TextRewardsVisual`: ArenaRewardGridVisual
- `SkinRewardDetailsPrefab`: SkinDetailsUiView
- `SkinRewardsParent`: RectTransform

---

#### TypeForwardedFromAttribute

**Line:** 234454

**Inherits:** Attribute

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

#### ValidateObjectMembersAttribute

**Line:** 1540864

**Inherits:** Attribute

---

#### ViewGuildRefusedException

**Line:** 570210

**Inherits:** Exception

---

#### WarContributionRankingsUiView

**Line:** 720146

**Inherits:** MonoBehaviour

**Fields:**

- `Tabs`: List<TabButton>
- `EntriesParent`: RectTransform
- `TabsParent`: RectTransform
- `WarEntryUiViewPrefab`: WarRankingsEntryUiView
- `DayWeekText`: TMP_Text
- `GuildInfoView`: GuildInfoView
- `LoadingIndicator`: GameObject
- `_warManager`: GuildWarManager
- `_guildManager`: GuildManager
- `_isOwnContributions`: bool

---

#### WarEndRewardsRedDotUiView

**Line:** 720185

**Inherits:** RedDotUiView

---

#### WarPointsProgressKey

**Line:** 1078594

**Inherits:** ProgressKeyBase

---

#### WarPointsReward

**Line:** 1079260

**Inherits:** PlayerReward

---

#### WarRankingsEntryUiView

**Line:** 720216

**Inherits:** MonoBehaviour

**Fields:**

- `RankLabel`: TMP_Text
- `PlayerProfile`: PlayerMiniProfileUiView
- `Background`: Image

---

#### WarResultsPopupUiView

**Line:** 720269

**Inherits:** MonoBehaviour

**Fields:**

- `DayResultsEntryPrefab`: DayResultsEntryUiView
- `MyGuildInfo`: GuildInfoView
- `OpponentGuildInfo`: GuildInfoView
- `DayResultsContainer`: RectTransform
- `_warManager`: GuildWarManager

---

#### WarRewardsPopupUiView

**Line:** 720292

**Inherits:** MonoBehaviour

**Fields:**

- `WarProgressPass`: ProgressPassPanelView
- `ClaimedText`: GameObject
- `TitleText`: TMP_Text
- `TotalPointsText`: TMP_Text
- `CollectButtonText`: TMP_Text
- `ClanRewardsDescriptionText`: TMP_Text
- `CollectButton`: UnityButton
- `CollectButtonImage`: Image
- `ArenaRewardGridVisual`: ArenaRewardGridVisual
- `GuildTierRewardsInfoButton`: UnityButton
- `_warManager`: GuildWarManager

---

#### WarTabRedDotUiView

**Line:** 720335

**Inherits:** RedDotUiView

---

#### WarTaskConfig

**Line:** 1062727

---

#### WarTasksDayConfig

**Line:** 1062673

**Inherits:** IGameConfigData

---

#### WarTicketsChangeMessage

**Line:** 711833

**Inherits:** CurrencyChangeMessage

---

#### WarTicketsRedDotUiView

**Line:** 720350

**Inherits:** RedDotUiView

---

#### WarningHeaderValue

**Line:** 1491410

**Inherits:** ICloneable

---

#### XmlMemberMapping

**Line:** 754048

---

#### XmlMembersMapping

**Line:** 754053

**Inherits:** XmlMapping

**Fields:**

- `_hasWrapperElement`: bool

---

#### XmlReflectionMember

**Line:** 754199

**Fields:**

- `isReturnValue`: bool
- `memberName`: string
- `memberType`: Type
- `xmlAttributes`: XmlAttributes
- `declaringType`: Type

---

### Enums (30)

#### AndroidHardwareKeyboardHidden

**Line:** 1487673

**Values:**

- `Undefined` = 0
- `No` = 1
- `Yes` = 2

---

#### GuildChangeRankResponse

**Line:** 1063696

---

#### GuildClientPhase

**Line:** 570250

**Values:**

- `NoSession` = 0
- `NoGuild` = 1
- `GuildActive` = 2
- `CreatingGuild` = 3
- `JoiningGuild` = 4
- `LoadingEntity` = 5

---

#### GuildCreateInvitationResponse

**Line:** 571532

---

#### GuildCreationFailedEnum

**Line:** 1063974

**Values:**

- `None` = 0
- `NameNotUnique` = 1
- `TagNotUnique` = 2
- `BadWord` = 3
- `NameEmpty` = 4
- `NameTooLong` = 5
- `TagEmpty` = 6
- `TagTooLong` = 7
- `NameRegexFailed` = 8
- `TagRegexFailed` = 9
- `Other` = 10

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

- `InviteCode` = 0

---

#### GuildJoinRequest

**Line:** 570992

---

#### GuildJoinSetting

**Line:** 1063827

**Values:**

- `Open` = 0
- `Approval` = 1
- `InviteOnly` = 2
- `Closed` = 3

---

#### GuildLifecyclePhase

**Line:** 568591

**Values:**

- `WaitingForSetup` = 0
- `WaitingForLeader` = 1
- `Running` = 2
- `Closed` = 3

---

#### GuildMemberKickResponse

**Line:** 1063651

---

#### GuildMemberPlayerDataUpdateKind

**Line:** 569740

**Values:**

- `NewMember` = 0
- `UpdateMember` = 1

---

#### GuildMemberRole

**Line:** 568575

**Values:**

- `Leader` = 0
- `Commander` = 1
- `Captain` = 2
- `R1` = 11
- `R2` = 12
- `R3` = 13
- `R4` = 14
- `R5` = 15

---

#### GuildMemberRoleEvent

**Line:** 568602

**Values:**

- `MemberAdd` = 0
- `MemberRemove` = 1
- `MemberEdit` = 2

---

#### GuildMemberTransferLeadershipResponse

**Line:** 1063577

---

#### GuildTabType

**Line:** 719201

**Values:**

- `Members` = 0
- `Missions` = 1
- `Titans` = 2
- `War` = 3

---

#### GuildTier

**Line:** 1062450

**Values:**

- `S` = 0
- `A` = 1
- `B` = 2
- `C` = 3
- `D` = 4
- `E` = 5
- `F` = 6

---

#### GuildTransactionConsistencyMode

**Line:** 569995

**Values:**

- `Relaxed` = 0
- `EventuallyConsistent` = 1

---

#### GuildViewResponse

**Line:** 571336

---

#### JsonUnmappedMemberHandling

**Line:** 1003257

**Values:**

- `Skip` = 0
- `Disallow` = 1

---

#### MemberBindingType

**Line:** 1288325

**Values:**

- `Assignment` = 0
- `MemberBinding` = 1
- `ListBinding` = 2

---

#### MemberSerialization

**Line:** 1032298

**Values:**

- `OptOut` = 0
- `OptIn` = 1
- `Fields` = 2

---

#### MemberTypes

**Line:** 265716

**Values:**

- `Constructor` = 1
- `Event` = 2
- `Field` = 4
- `Method` = 8
- `Property` = 16
- `TypeInfo` = 32
- `Custom` = 64
- `NestedType` = 128
- `All` = 191

---

#### MetaMemberFlags

**Line:** 600822

**Values:**

- `None` = 0
- `Hidden` = 1
- `NoChecksum` = 2
- `Transient` = 4
- `ServerOnly` = 3
- `_LegacyDontUse_ExcludeFromGdprExport` = 8
- `ExcludeFromEventLog` = 16

---

#### MissingMemberHandling

**Line:** 1032318

**Values:**

- `Ignore` = 0
- `Error` = 1

---

#### PlayerGuildFetchJoinsResponse

**Line:** 1063786

---

#### UnknownConfigMemberHandling

**Line:** 597253

**Values:**

- `Ignore` = 0
- `Warning` = 1
- `Error` = 2

---

#### WarTask

**Line:** 1066314

**Values:**

- `SpendCoinsOnForge` = 100
- `StartForgeUpgrade` = 101
- `CompleteForgeUpgrade` = 102
- `ForgePrimitiveEquipment` = 1000
- `ForgeMedievalEquipment` = 1001
- `ForgeEarlyModernEquipment` = 1002
- `ForgeModernEquipment` = 1003
- `ForgeSpaceEquipment` = 1004
- `ForgeInterstellarEquipment` = 1005
- `ForgeMultiverseEquipment` = 1006
- `ForgeQuantumEquipment` = 1007
- `ForgeUnderworldEquipment` = 1008
- `ForgeDivineEquipment` = 1009
- `UseHammerThiefDungeonKey` = 2000
- `UseGhostTownDungeonKey` = 2001
- `UseInvasionDungeonKey` = 2002
- `UseZombieInvasionDungeonKey` = 2003
- `SummonCommonSkill` = 3000
- `SummonRareSkill` = 3001
- `SummonEpicSkill` = 3002
- `SummonLegendarySkill` = 3003
- `SummonUltimateSkill` = 3004
- `SummonMythicSkill` = 3005
- `UpgradeCommonSkill` = 4006
- `UpgradeRareSkill` = 4007
- `UpgradeEpicSkill` = 4008
- `UpgradeLegendarySkill` = 4009
- `UpgradeUltimateSkill` = 4010
- `UpgradeMythicSkill` = 4011
- `HatchCommonEgg` = 5000
- `HatchRareEgg` = 5001
- `HatchEpicEgg` = 5002
- `HatchLegendaryEgg` = 5003
- `HatchUltimateEgg` = 5004
- `HatchMythicEgg` = 5005
- `MergeCommonPet` = 6000
- `MergeRarePet` = 6001
- `MergeEpicPet` = 6002
- `MergeLegendaryPet` = 6003
- `MergeUltimatePet` = 6004
- `MergeMythicPet` = 6005
- `FinishITechTreeUpgrade` = 7000
- `FinishIITechTreeUpgrade` = 7001
- `FinishIIITechTreeUpgrade` = 7002
- `FinishIVTechTreeUpgrade` = 7003
- `FinishVTechTreeUpgrade` = 7004
- `SummonCommonMount` = 8000
- `SummonRareMount` = 8001
- `SummonEpicMount` = 8002
- `SummonLegendaryMount` = 8003
- `SummonUltimateMount` = 8004
- `SummonMythicMount` = 8005
- `MergeCommonMount` = 9000
- `MergeRareMount` = 9001
- `MergeEpicMount` = 9002
- `MergeLegendaryMount` = 9003
- `MergeUltimateMount` = 9004
- `MergeMythicMount` = 9005

---

## Other

### Classes (5353)

#### ABSSequentiable

**Line:** 1430396

---

#### ABSTweenPlugin

**Line:** 1429927

---

#### APVLeakReductionModeParameter

**Line:** 820135

**Inherits:** VolumeParameter

---

#### ARC4Managed

**Line:** 1449232

**Inherits:** RC4

**Fields:**

- `x`: byte
- `y`: byte
- `m_disposed`: bool

---

#### ASCIIEncoding

**Line:** 214024

**Inherits:** Encoding

---

#### ASN1

**Line:** 1447091

**Fields:**

- `m_nTag`: byte
- `elist`: ArrayList

---

#### ATTLocalizationMessage

**Line:** 1564100

**Fields:**

- `Language`: Language
- `PopupMessage`: string
- `ManualIsoCode`: string

---

#### AbandonedMutexException

**Line:** 178785

**Inherits:** SystemException

**Fields:**

- `_mutexIndex`: int
- `_mutex`: Mutex

---

#### AbstractCheatContainer

**Line:** 685474

**Inherits:** INotifyPropertyChanged

**Fields:**

- `_contexts`: Contexts
- `PropertyChanged`: PropertyChangedEventHandler

---

#### AbstractEntityIndex

**Line:** 1545840

---

#### AbstractEntityIndexAttribute

**Line:** 1597413

**Inherits:** Attribute

---

#### AbstractEventData

**Line:** 1359122

**Fields:**

- `m_Used`: bool

---

#### AbstractProgressBar

**Line:** 626891

**Inherits:** BindableElement

**Fields:**

- `m_LowValue`: float
- `m_HighValue`: float
- `m_Value`: float

---

#### AbstractPurchasingModule

**Line:** 1532038

**Inherits:** IPurchasingModule

**Fields:**

- `m_Binder`: IPurchasingBinder

---

#### AbstractStore

**Line:** 1532081

**Inherits:** IStore

---

#### AbstractTypeDeserializationFailureInfo

**Line:** 573472

---

#### Accenter

**Line:** 1319769

**Inherits:** CharacterSubstitutor

---

#### AccessTokenWithHeaders

**Line:** 1368887

---

#### AccessViolationException

**Line:** 4586

**Inherits:** SystemException

---

#### AccountButtonUiView

**Line:** 729101

**Inherits:** MonoBehaviour

**Fields:**

- `AccountButton`: UnityButton
- `TickIcon`: GameObject
- `Target`: GameObject
- `SettingsColorView`: SettingsColorView

---

#### AckMessage

**Line:** 1568640

**Inherits:** HubMessage

---

#### Action

**Line:** 1230240

---

#### ActionButtonUiView

**Line:** 711939

**Inherits:** MonoBehaviour

**Fields:**

- `ButtonImage`: Image
- `Label`: TMP_Text
- `Button`: UnityButton
- `CustomBackgroundColors`: bool
- `CustomTextColors`: bool
- `ActiveButtonColor`: Color
- `DisabledButtonColor`: Color
- `ActiveTextColor`: Color
- `DisabledTextColor`: Color

---

#### ActionCompleteCallback

**Line:** 1442439

**Inherits:** MulticastDelegate

---

#### ActionControl

**Line:** 1444807

**Inherits:** OptionsControlBase

**Fields:**

- `_method`: MethodReference
- `Button`: Button
- `Title`: Text

---

#### ActivatedClientTypeEntry

**Line:** 220833

**Inherits:** TypeEntry

**Fields:**

- `applicationUrl`: string
- `obj_type`: Type

---

#### ActivatedServiceTypeEntry

**Line:** 220864

**Inherits:** TypeEntry

**Fields:**

- `obj_type`: Type

---

#### Activator

**Line:** 171815

---

#### ActivatorUtilitiesConstructorAttribute

**Line:** 1542436

**Inherits:** Attribute

---

#### ActiveComponent

**Line:** 729417

**Inherits:** IComponent

---

#### ActiveEventSystem

**Line:** 700928

**Inherits:** ReactiveSystem

---

#### ActiveListenerComponent

**Line:** 699050

**Inherits:** IComponent

**Fields:**

- `value`: List<IActiveListener>

---

#### ActiveRemovedEventSystem

**Line:** 700949

**Inherits:** ReactiveSystem

---

#### ActiveRemovedListenerComponent

**Line:** 699063

**Inherits:** IComponent

**Fields:**

- `value`: List<IActiveRemovedListener>

---

#### Activity

**Line:** 1417055

**Inherits:** IDisposable

**Fields:**

- `_traceState`: string
- `_currentChildId`: int
- `_id`: string
- `_rootId`: string
- `_parentId`: string
- `_parentSpanId`: string
- `_traceId`: string
- `_spanId`: string
- `_w3CIdFlags`: byte
- `_parentTraceFlags`: byte
- `_links`: DiagLinkedList<ActivityLink>
- `_events`: DiagLinkedList<ActivityEvent>
- `_customProperties`: Dictionary<string, object>
- `_displayName`: string
- `_statusCode`: ActivityStatusCode
- `_statusDescription`: string
- `_previousActiveActivity`: Activity

---

#### ActivityListener

**Line:** 1418296

**Inherits:** IDisposable

---

#### ActivitySource

**Line:** 1418495

**Inherits:** IDisposable

**Fields:**

- `_listeners`: SynchronizedList<ActivityListener>

---

#### ActivityTagsCollection

**Line:** 1417671

**Inherits:** IDictionary

---

#### AdaptiveIcon

**Line:** 1325173

**Fields:**

- `m_Background`: LocalizedTexture
- `m_Foreground`: LocalizedTexture

---

#### AdaptiveIconsInfo

**Line:** 1325207

**Inherits:** IMetadata

**Fields:**

- `m_Adaptive_idpi`: AdaptiveIcon
- `m_Adaptive_mdpi`: AdaptiveIcon
- `m_Adaptive_hdpi`: AdaptiveIcon
- `m_Adaptive_xhdpi`: AdaptiveIcon
- `m_Adaptive_xxhdpi`: AdaptiveIcon
- `m_Adaptive_xxxhdpi`: AdaptiveIcon

---

#### AddBandingRequest

**Line:** 1384876

**Inherits:** IDirectResponseSchema

---

#### AddBandingResponse

**Line:** 1384912

**Inherits:** IDirectResponseSchema

---

#### AddChartRequest

**Line:** 1384948

**Inherits:** IDirectResponseSchema

---

#### AddChartResponse

**Line:** 1384984

**Inherits:** IDirectResponseSchema

---

#### AddComponentMenu

**Line:** 881545

**Inherits:** Attribute

**Fields:**

- `m_AddComponentMenu`: string
- `m_Ordering`: int

---

#### AddConditionalFormatRuleRequest

**Line:** 1385020

**Inherits:** IDirectResponseSchema

---

#### AddCooldownSystem

**Line:** 696329

**Inherits:** MultiReactiveSystem

---

#### AddDataSourceRequest

**Line:** 1385068

**Inherits:** IDirectResponseSchema

---

#### AddDataSourceResponse

**Line:** 1385104

**Inherits:** IDirectResponseSchema

---

#### AddDimensionGroupRequest

**Line:** 1385152

**Inherits:** IDirectResponseSchema

---

#### AddDimensionGroupResponse

**Line:** 1385188

**Inherits:** IDirectResponseSchema

---

#### AddFilterViewRequest

**Line:** 1385224

**Inherits:** IDirectResponseSchema

---

#### AddFilterViewResponse

**Line:** 1385260

**Inherits:** IDirectResponseSchema

---

#### AddNamedRangeRequest

**Line:** 1385296

**Inherits:** IDirectResponseSchema

---

#### AddNamedRangeResponse

**Line:** 1385332

**Inherits:** IDirectResponseSchema

---

#### AddProtectedRangeRequest

**Line:** 1385368

**Inherits:** IDirectResponseSchema

---

#### AddProtectedRangeResponse

**Line:** 1385404

**Inherits:** IDirectResponseSchema

---

#### AddSheetRequest

**Line:** 1385440

**Inherits:** IDirectResponseSchema

---

#### AddSheetResponse

**Line:** 1385476

**Inherits:** IDirectResponseSchema

---

#### AddSlicerRequest

**Line:** 1385512

**Inherits:** IDirectResponseSchema

---

#### AddSlicerResponse

**Line:** 1385548

**Inherits:** IDirectResponseSchema

---

#### AddUserToChannelRequest

**Line:** 1526436

**Inherits:** IEquatable

---

#### AddedInVersionAttribute

**Line:** 600901

**Inherits:** Attribute

---

#### AddingNewEventArgs

**Line:** 780962

**Inherits:** EventArgs

---

#### AddingNewEventHandler

**Line:** 780982

**Inherits:** MulticastDelegate

---

#### AdditionalConsentModeData

**Line:** 1564988

**Fields:**

- `acString`: string
- `adTechProviders`: List<AdTechProvider>

---

#### AdditionalLightsShadowCasterPass

**Line:** 918666

**Inherits:** ScriptableRenderPass

**Fields:**

- `renderTargetWidth`: int
- `renderTargetHeight`: int
- `m_CreateEmptyShadowmap`: bool
- `m_SetKeywordForEmptyShadowmap`: bool
- `m_EmptyShadowmapNeedsClear`: bool
- `m_IssuedMessageAboutShadowSlicesTooMany`: bool
- `m_IssuedMessageAboutShadowMapsRescale`: bool
- `m_IssuedMessageAboutShadowMapsTooBig`: bool
- `m_IssuedMessageAboutRemovedShadowSlices`: bool
- `m_MaxShadowDistanceSq`: float
- `m_CascadeBorder`: float
- `m_EmptyAdditionalLightShadowmapTexture`: RTHandle
- `m_AdditionalLightShadowDescriptor`: RenderTextureDescriptor

---

#### AdditionalMessageData

**Line:** 595236

---

#### AdditionalPropertyAttribute

**Line:** 807877

**Inherits:** Attribute

---

#### AddressInUseException

**Line:** 1570380

**Inherits:** InvalidOperationException

---

#### AeadParameters

**Line:** 1519027

**Inherits:** ICipherParameters

---

#### Aes

**Line:** 217856

**Inherits:** SymmetricAlgorithm

---

#### AesCryptoServiceProvider

**Line:** 1230601

**Inherits:** Aes

---

#### AesManaged

**Line:** 1230512

**Inherits:** Aes

**Fields:**

- `m_rijndael`: RijndaelManaged

---

#### AffordableComponent

**Line:** 711638

**Inherits:** IComponent

---

#### AffordableEventSystem

**Line:** 700970

**Inherits:** ReactiveSystem

---

#### AffordableListenerComponent

**Line:** 699076

**Inherits:** IComponent

**Fields:**

- `value`: List<IAffordableListener>

---

#### AffordableRemovedEventSystem

**Line:** 700991

**Inherits:** ReactiveSystem

---

#### AffordableRemovedListenerComponent

**Line:** 699089

**Inherits:** IComponent

**Fields:**

- `value`: List<IAffordableRemovedListener>

---

#### AffordableSystem

**Line:** 711842

**Inherits:** ReactiveSystem

---

#### AfterGameBarrierComponent

**Line:** 685357

**Inherits:** IComponent

**Fields:**

- `Value`: Barrier

---

#### AgeComponent

**Line:** 710009

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### AgeGateConfig

**Line:** 739031

**Inherits:** ScriptableObject

**Fields:**

- `SettingsPerCountryCode`: SerializableDictionary<string, AgeGateSettings>
- `DefaultSettings`: AgeGateSettings

---

#### AgeGatePopupView

**Line:** 739085

**Inherits:** MonoBehaviour

**Fields:**

- `Title`: TMP_Text
- `TOSText`: TMP_Text
- `AgeSliderObject`: GameObject
- `AgeSlider`: AgeSlider
- `ContinueButton`: UnityButton
- `AgeText`: TMP_Text
- `TOSGameObject`: GameObject
- `_settings`: AgeGateSettings
- `_userLocation`: string
- `_onTosAccepted`: Action

---

#### AgeGateSettings

**Line:** 739048

**Fields:**

- `ShowAgeSlider`: bool
- `AgeToShowTOS`: int

---

#### AgeSlider

**Line:** 739118

**Inherits:** MonoBehaviour

**Fields:**

- `Slider`: Slider
- `_onSliderChanged`: Action<int>

---

#### AgeVisualConfig

**Line:** 711394

**Inherits:** ScriptableObject

**Fields:**

- `Name`: string
- `Color`: Color
- `ItemBackground`: ItemBackgroundView
- `Icon`: Sprite
- `MapElementViews`: List<MapElementView>
- `MapBackgroundColor`: Color

---

#### AggregateException

**Line:** 19260

**Inherits:** Exception

**Fields:**

- `m_innerExceptions`: ReadOnlyCollection<Exception>

---

#### AiModerationSettingsDto

**Line:** 1529577

**Inherits:** IEquatable

---

#### AimTest

**Line:** 709667

**Inherits:** MonoBehaviour

**Fields:**

- `WeaponConfig`: WeaponItemVisualConfig
- `Rig`: CharacterRig
- `Target`: Transform
- `_weaponConfig`: WeaponItemVisualConfig
- `_weapon`: WeaponEquipmentItem

---

#### AimView

**Line:** 710722

**Inherits:** GameUnityView

**Fields:**

- `Rig`: CharacterRig
- `_isAiming`: bool
- `_affectedByGravity`: bool
- `_weaponData`: WeaponData
- `_projSpeed`: float

---

#### AimingTestView

**Line:** 710647

**Inherits:** MonoBehaviour

**Fields:**

- `Target`: Transform
- `CharacterRig`: CharacterRig
- `WeaponConfig`: WeaponItemVisualConfig
- `ProjectileTestView`: ProjectileTestView
- `_timer`: float
- `_weaponConfig`: WeaponItemVisualConfig
- `_weapon`: WeaponEquipmentItem
- `_centreOfMass`: Vector2

---

#### Alert

**Line:** 1448559

**Fields:**

- `level`: AlertLevel
- `description`: AlertDescription

---

#### Allocator2D

**Line:** 672524

**Fields:**

- `rect`: RectInt
- `allocator`: BestFitAllocator
- `alloc`: Alloc

---

#### AllocatorManager

**Line:** 1168911

---

#### AllyComponent

**Line:** 710638

**Inherits:** IComponent

---

#### AlwaysLinkAssemblyAttribute

**Line:** 888590

**Inherits:** Attribute

---

#### AlwaysOnTopUiView

**Line:** 697086

**Inherits:** MonoBehaviour

---

#### AmazonAppStoreStoreExtensions

**Line:** 1402017

**Inherits:** IAmazonExtensions

---

#### AmazonApps

**Line:** 1402005

---

#### AmbienceAudioSource

**Line:** 705901

**Inherits:** GameUnityView

**Fields:**

- `Source`: AudioSource

---

#### AmbienceMuteSaveSystem

**Line:** 684535

**Inherits:** ReactiveSystem

---

#### AmbienceSettingsView

**Line:** 729128

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton
- `Toggle`: ColoredToggle
- `_audioListener`: AudioEntity

---

#### AmbienceSfxComponent

**Line:** 705575

**Inherits:** IComponent

---

#### AmbientValueAttribute

**Line:** 780995

**Inherits:** Attribute

---

#### AmbiguousImplementationException

**Line:** 220777

**Inherits:** Exception

---

#### AmbiguousMatchException

**Line:** 264897

**Inherits:** SystemException

---

#### AmbiguousTimeException

**Line:** 1142432

**Inherits:** ArgumentOutOfRangeException

---

#### AmbiguousTimeResolver

**Line:** 1148607

**Inherits:** MulticastDelegate

---

#### AnalyticsContextBase

**Line:** 605936

**Inherits:** IMetaIntegration

---

#### AnalyticsContextDeserializationFailureSubstitute

**Line:** 573398

**Inherits:** AnalyticsContextBase

---

#### AnalyticsEventAttribute

**Line:** 605165

**Inherits:** Attribute

---

#### AnalyticsEventBase

**Line:** 891354

**Fields:**

- `eventName`: string
- `eventVersion`: int
- `eventPrefix`: string
- `sendEventOptions`: SendEventOptions

---

#### AnalyticsEventCategoryAttribute

**Line:** 605192

**Inherits:** Attribute

---

#### AnalyticsEventCustomizations

**Line:** 605484

**Inherits:** IMetaIntegrationSingleton

---

#### AnalyticsEventHandler

**Line:** 605360

**Fields:**

- `_eventHandler`: Action<TContext, TEvent>

---

#### AnalyticsEventKeywordsAttribute

**Line:** 605217

**Inherits:** Attribute

---

#### AnalyticsEventKeywordsCore

**Line:** 605438

---

#### AnalyticsEventRegistry

**Line:** 605786

---

#### AnalyticsEventSpec

**Line:** 605540

---

#### AnalyticsLabel

**Line:** 605998

**Inherits:** DynamicEnum

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

#### AndroidAssetPackUseMobileDataRequestResult

**Line:** 1487195

---

#### AndroidConfiguration

**Line:** 1487463

---

#### AndroidJavaClass

**Line:** 1486778

**Inherits:** AndroidJavaObject

---

#### AndroidJavaException

**Line:** 1486050

**Inherits:** Exception

**Fields:**

- `mJavaStackTrace`: string

---

#### AndroidJavaObject

**Line:** 1486156

**Inherits:** IDisposable

---

#### AndroidJavaProxy

**Line:** 1486108

---

#### AndroidJavaRunnable

**Line:** 1486038

**Inherits:** MulticastDelegate

---

#### AndroidLocalNotification

**Line:** 693881

**Inherits:** ILocalNotification

**Fields:**

- `_pushNote`: AndroidNotification

---

#### AndroidLocale

**Line:** 1487431

---

#### AndroidNotificationCenter

**Line:** 1552974

---

#### AndroidNotificationIntentData

**Line:** 1553385

---

#### AndroidOptions

**Line:** 1564392

**Fields:**

- `DisableSystemBackButton`: bool
- `StatusBarColor`: string
- `ShowWindowInFullscreen`: bool

---

#### AndroidPushNotificationService

**Line:** 693966

**Inherits:** IPushNotificationService

**Fields:**

- `_defaultChannel`: Nullable<AndroidNotificationChannel>

---

#### AndroidReceivedNotificationMainThreadDispatcher

**Line:** 1553430

**Inherits:** MonoBehaviour

**Fields:**

- `m_ReceivedNotificationQueue`: List<AndroidJavaObject>
- `m_ReceivedNotificationList`: List<AndroidJavaObject>

---

#### AnimatableProperty

**Line:** 1563337

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `m_Name`: string

---

#### AnimationClip

**Line:** 1575404

**Inherits:** Motion

---

#### AnimationCurve

**Line:** 869824

**Inherits:** IEquatable

**Fields:**

- `m_RequiresNativeCleanup`: bool

---

#### AnimationCurveParameter

**Line:** 827734

**Inherits:** VolumeParameter

---

#### AnimationEvent

**Line:** 1575374

---

#### AnimationState

**Line:** 1575325

**Inherits:** TrackedReference

---

#### AnimationTriggers

**Line:** 1351483

**Fields:**

- `m_NormalTrigger`: string
- `m_HighlightedTrigger`: string
- `m_PressedTrigger`: string
- `m_SelectedTrigger`: string
- `m_DisabledTrigger`: string

---

#### Animator

**Line:** 1575529

**Inherits:** Behaviour

---

#### AnimatorOverrideController

**Line:** 1575635

**Inherits:** RuntimeAnimatorController

---

#### AnnualDatePattern

**Line:** 1151087

**Inherits:** IPattern

---

#### AnvilButton

**Line:** 735787

**Inherits:** UnityButton

---

#### AnvilButtonView

**Line:** 714341

**Inherits:** MonoBehaviour

**Fields:**

- `AnvilButton`: AnvilButton
- `HammerLabel`: TMP_Text
- `_priceEntity`: GameEntity
- `_contexts`: Contexts

---

#### AnvilView

**Line:** 714386

**Inherits:** MonoBehaviour

**Fields:**

- `ItemsParent`: Transform
- `ItemsCanvasGroup`: CanvasGroup
- `ForgeContainer`: GameObject
- `RevealItemSound`: AudioClip
- `Flare`: Image
- `FlareCanvasGroup`: CanvasGroup
- `_animator`: Animator
- `_fadeTween`: Tween
- `_nextFlareColor`: Color

---

#### AnyAppSystemsInitializedEventSystem

**Line:** 701056

**Inherits:** ReactiveSystem

---

#### AnyAppSystemsInitializedListenerComponent

**Line:** 699128

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyAppSystemsInitializedListener>

---

#### AnyDeathEffectEventSystem

**Line:** 701102

**Inherits:** ReactiveSystem

---

#### AnyDeathEffectListenerComponent

**Line:** 699154

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyDeathEffectListener>

---

#### AnyDmgEventSystem

**Line:** 701125

**Inherits:** ReactiveSystem

---

#### AnyDmgListenerComponent

**Line:** 699167

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyDmgListener>

---

#### AnyMainScreenTypeEventSystem

**Line:** 701148

**Inherits:** ReactiveSystem

---

#### AnyMainScreenTypeListenerComponent

**Line:** 699180

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMainScreenTypeListener>

---

#### AnyMuteAmbienceEventSystem

**Line:** 701171

**Inherits:** ReactiveSystem

---

#### AnyMuteAmbienceListenerComponent

**Line:** 699193

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteAmbienceListener>

---

#### AnyMuteAmbienceRemovedEventSystem

**Line:** 701194

**Inherits:** ReactiveSystem

---

#### AnyMuteAmbienceRemovedListenerComponent

**Line:** 699206

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteAmbienceRemovedListener>

---

#### AnyMuteAudioEventSystem

**Line:** 701217

**Inherits:** ReactiveSystem

---

#### AnyMuteAudioListenerComponent

**Line:** 699219

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteAudioListener>

---

#### AnyMuteAudioRemovedEventSystem

**Line:** 701240

**Inherits:** ReactiveSystem

---

#### AnyMuteAudioRemovedListenerComponent

**Line:** 699232

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteAudioRemovedListener>

---

#### AnyMuteHapticsEventSystem

**Line:** 701263

**Inherits:** ReactiveSystem

---

#### AnyMuteHapticsListenerComponent

**Line:** 699245

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteHapticsListener>

---

#### AnyMuteHapticsRemovedEventSystem

**Line:** 701286

**Inherits:** ReactiveSystem

---

#### AnyMuteHapticsRemovedListenerComponent

**Line:** 699258

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteHapticsRemovedListener>

---

#### AnyMuteMusicEventSystem

**Line:** 701309

**Inherits:** ReactiveSystem

---

#### AnyMuteMusicListenerComponent

**Line:** 699271

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteMusicListener>

---

#### AnyMuteMusicRemovedEventSystem

**Line:** 701332

**Inherits:** ReactiveSystem

---

#### AnyMuteMusicRemovedListenerComponent

**Line:** 699284

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyMuteMusicRemovedListener>

---

#### AnyOpenEventSystem

**Line:** 701355

**Inherits:** ReactiveSystem

---

#### AnyOpenListenerComponent

**Line:** 699297

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyOpenListener>

---

#### AnyOpenRemovedEventSystem

**Line:** 701378

**Inherits:** ReactiveSystem

---

#### AnyOpenRemovedListenerComponent

**Line:** 699310

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyOpenRemovedListener>

---

#### AnyPlayMusicEventSystem

**Line:** 701401

**Inherits:** ReactiveSystem

---

#### AnyPlayMusicListenerComponent

**Line:** 699323

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyPlayMusicListener>

---

#### AnySafeAreaEventSystem

**Line:** 701424

**Inherits:** ReactiveSystem

---

#### AnySafeAreaListenerComponent

**Line:** 699336

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnySafeAreaListener>

---

#### AnySellCoinsEventSystem

**Line:** 701447

**Inherits:** ReactiveSystem

---

#### AnySellCoinsListenerComponent

**Line:** 699349

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnySellCoinsListener>

---

#### AppAnyDestroyedEventSystem

**Line:** 701470

**Inherits:** ReactiveSystem

---

#### AppAnyDestroyedListenerComponent

**Line:** 699362

**Inherits:** IComponent

**Fields:**

- `value`: List<IAppAnyDestroyedListener>

---

#### AppAttribute

**Line:** 697535

**Inherits:** ContextAttribute

---

#### AppCheatContainer

**Line:** 685803

**Inherits:** AbstractCheatContainer

**Fields:**

- `_frameRate`: int
- `_timeScale`: float

---

#### AppContext

**Line:** 687404

**Inherits:** Context

**Fields:**

- `_nextId`: long

---

#### AppController

**Line:** 684074

**Inherits:** IContextController

**Fields:**

- `_appSystems`: AppSystems

---

#### AppControllerComponent

**Line:** 684112

**Inherits:** IComponent

**Fields:**

- `Value`: AppController

---

#### AppDestroySystem

**Line:** 686775

**Inherits:** ReactiveSystem

---

#### AppDestroyedEventSystem

**Line:** 701493

**Inherits:** ReactiveSystem

---

#### AppDestroyedListenerComponent

**Line:** 699375

**Inherits:** IComponent

**Fields:**

- `value`: List<IAppDestroyedListener>

---

#### AppDomain

**Line:** 174417

**Inherits:** MarshalByRefObject

**Fields:**

- `_mono_app_domain`: IntPtr
- `_evidence`: object
- `_granted`: object
- `_principalPolicy`: int
- `AssemblyLoad`: AssemblyLoadEventHandler
- `AssemblyResolve`: ResolveEventHandler
- `DomainUnload`: EventHandler
- `ProcessExit`: EventHandler
- `ResourceResolve`: ResolveEventHandler
- `TypeResolve`: ResolveEventHandler
- `UnhandledException`: UnhandledExceptionEventHandler
- `FirstChanceException`: EventHandler<FirstChanceExceptionEventArgs>
- `_domain_manager`: object
- `ReflectionOnlyAssemblyResolve`: ResolveEventHandler
- `_activation`: object
- `_applicationIdentity`: object
- `compatibility_switch`: List<string>

---

#### AppDomainSetup

**Line:** 174871

**Fields:**

- `application_base`: string
- `application_name`: string
- `cache_path`: string
- `configuration_file`: string
- `dynamic_base`: string
- `license_file`: string
- `private_bin_path`: string
- `private_bin_path_probe`: string
- `shadow_copy_directories`: string
- `shadow_copy_files`: string
- `publisher_policy`: bool
- `path_changed`: bool
- `loader_optimization`: int
- `disallow_binding_redirects`: bool
- `disallow_code_downloads`: bool
- `_activationArguments`: object
- `domain_initializer`: object
- `application_trust`: object
- `disallow_appbase_probe`: bool
- `manager_assembly`: string
- ... (1 more fields)

---

#### AppDomainUnloadedException

**Line:** 72395

**Inherits:** SystemException

---

#### AppEntity

**Line:** 686973

**Inherits:** Entity

---

#### AppEntityRef

**Line:** 686943

**Inherits:** EntityRef

---

#### AppEventSystems

**Line:** 699031

**Inherits:** Feature

---

#### AppInfo

**Line:** 1325148

**Inherits:** IMetadata

**Fields:**

- `m_DisplayName`: LocalizedString

---

#### AppMatcher

**Line:** 697582

---

#### AppOptions

**Line:** 1491509

**Inherits:** IDisposable

---

#### AppPauseFeature

**Line:** 684345

**Inherits:** Feature

---

#### AppPauseRemoveSystem

**Line:** 684378

**Inherits:** ReactiveSystem

---

#### AppPauseSystem

**Line:** 684399

**Inherits:** ReactiveSystem

---

#### AppPauseTypeComponent

**Line:** 684356

**Inherits:** IComponent

**Fields:**

- `Value`: AppPauseType

---

#### AppPausedComponent

**Line:** 684126

**Inherits:** IComponent

---

#### AppSpecificBadRequestException

**Line:** 685229

**Inherits:** BadRequestException

---

#### AppStartButton

**Line:** 735796

**Inherits:** UnityButton

**Fields:**

- `Image`: Image
- `ButtonScale`: float
- `_defaultColor`: Nullable<Color>
- `_anchoredPos`: Vector2

---

#### AppSystems

**Line:** 684101

**Inherits:** Feature

---

#### AppSystemsComponent

**Line:** 698521

**Inherits:** IComponent

**Fields:**

- `value`: AppSystems

---

#### AppSystemsInitializeSystem

**Line:** 684261

**Inherits:** IInitializeSystem

---

#### AppSystemsInitializeTimeoutComponent

**Line:** 684149

**Inherits:** IComponent

---

#### AppSystemsInitializedComponent

**Line:** 684138

**Inherits:** IComponent

---

#### AppTrackingTransparency

**Line:** 1564072

**Inherits:** Singleton

**Fields:**

- `EnglishDefaultMessage`: string
- `LocalizationMessages`: List<ATTLocalizationMessage>

---

#### AppUpdateAsyncOperation

**Line:** 1579040

---

#### AppUpdateInfo

**Line:** 1578785

---

#### AppUpdateManager

**Line:** 1578836

---

#### AppUpdateOptions

**Line:** 1578857

---

#### AppUpdateRequest

**Line:** 1578909

**Inherits:** CustomYieldInstruction

**Fields:**

- `Completed`: Action<AppUpdateRequest>

---

#### AppUtilPINVOKE

**Line:** 1493924

---

#### AppVersionInitSystem

**Line:** 684185

**Inherits:** IInitSystem

---

#### AppendCellsRequest

**Line:** 1385584

**Inherits:** IDirectResponseSchema

---

#### AppendDimensionRequest

**Line:** 1385644

**Inherits:** IDirectResponseSchema

---

#### AppendValuesResponse

**Line:** 1385704

**Inherits:** IDirectResponseSchema

---

#### AppleAppStore

**Line:** 1405329

---

#### AppleAuthManager

**Line:** 1589565

**Inherits:** IAppleAuthManager

---

#### AppleInAppPurchaseReceipt

**Line:** 1594620

**Inherits:** IPurchaseReceipt

---

#### AppleProductMetadata

**Line:** 1405353

**Inherits:** ProductMetadata

---

#### AppleReceipt

**Line:** 1594529

---

#### AppleReceiptParser

**Line:** 1544666

---

#### AppleSignInWrapper

**Line:** 733458

**Inherits:** Singleton

**Fields:**

- `_appleAuthManager`: IAppleAuthManager
- `_credential`: ICredential

---

#### AppleValidator

**Line:** 1544650

**Fields:**

- `cert`: X509Cert
- `parser`: AppleReceiptParser

---

#### Application

**Line:** 870045

---

#### ApplicationException

**Line:** 19322

**Inherits:** Exception

---

#### ApplicationMemoryHelper

**Line:** 684243

**Inherits:** MonoBehaviour

---

#### ApplicationStateManager

**Line:** 738282

**Inherits:** MonoBehaviour

**Fields:**

- `_onStateTransitionDone`: Action
- `_isInitialized`: bool
- `LoadingScreenViewPrefab`: LoadingScreenView
- `UsercentricsWrapper`: UsercentricsWrapper
- `_delayedListenerFuncs`: List<Action>

---

#### ApplyComponent

**Line:** 696051

**Inherits:** IComponent

---

#### ApplyEventSystem

**Line:** 701514

**Inherits:** ReactiveSystem

---

#### ApplyListenerComponent

**Line:** 699388

**Inherits:** IComponent

**Fields:**

- `value`: List<IApplyListener>

---

#### ApplyRemovedEventSystem

**Line:** 701535

**Inherits:** ReactiveSystem

---

#### ApplyRemovedListenerComponent

**Line:** 699401

**Inherits:** IComponent

**Fields:**

- `value`: List<IApplyRemovedListener>

---

#### ArgumentException

**Line:** 19341

**Inherits:** SystemException

**Fields:**

- `_paramName`: string

---

#### ArgumentNullException

**Line:** 19378

**Inherits:** ArgumentException

---

#### ArgumentOutOfRangeException

**Line:** 19397

**Inherits:** ArgumentException

**Fields:**

- `_actualValue`: object

---

#### ArithmeticException

**Line:** 19434

**Inherits:** SystemException

---

#### Arm

**Line:** 1331561

---

#### ArmourEquipmentItem

**Line:** 713625

**Inherits:** EquipmentItem

---

#### Array

**Line:** 124351

**Inherits:** ICollection

---

#### ArrayConverter

**Line:** 781030

**Inherits:** CollectionConverter

---

#### ArrayList

**Line:** 277596

**Inherits:** IList

**Fields:**

- `_size`: int
- `_version`: int
- `_syncRoot`: object

---

#### ArrayPool

**Line:** 464814

---

#### ArrayPropertyBag

**Line:** 1462275

---

#### ArraySizeTrackedProperty

**Line:** 1328951

**Inherits:** UIntTrackedProperty

---

#### ArrayTypeMismatchException

**Line:** 20379

**Inherits:** SystemException

---

#### Asn1Node

**Line:** 1543971

---

#### AsnEncodedData

**Line:** 778834

---

#### AspectRatioFitter

**Line:** 1354289

**Inherits:** UIBehaviour

**Fields:**

- `m_AspectRatio`: float
- `m_Rect`: RectTransform
- `m_DelayedSetDirty`: bool
- `m_DoesParentExist`: bool
- `m_Tracker`: DrivenRectTransformTracker

---

#### Assembly

**Line:** 267683

**Inherits:** ICustomAttributeProvider

---

#### AssemblyBuilder

**Line:** 269272

**Inherits:** Assembly

---

#### AssemblyCompanyAttribute

**Line:** 264913

**Inherits:** Attribute

---

#### AssemblyConfigurationAttribute

**Line:** 264927

**Inherits:** Attribute

---

#### AssemblyCopyrightAttribute

**Line:** 264950

**Inherits:** Attribute

---

#### AssemblyDefaultAliasAttribute

**Line:** 264964

**Inherits:** Attribute

---

#### AssemblyDelaySignAttribute

**Line:** 264978

**Inherits:** Attribute

---

#### AssemblyDescriptionAttribute

**Line:** 264992

**Inherits:** Attribute

---

#### AssemblyFileVersionAttribute

**Line:** 265006

**Inherits:** Attribute

---

#### AssemblyInformationalVersionAttribute

**Line:** 265027

**Inherits:** Attribute

---

#### AssemblyIsEditorAssembly

**Line:** 881701

**Inherits:** Attribute

---

#### AssemblyKeyFileAttribute

**Line:** 265048

**Inherits:** Attribute

---

#### AssemblyLoadEventArgs

**Line:** 20391

**Inherits:** EventArgs

---

#### AssemblyLoadEventHandler

**Line:** 20405

**Inherits:** MulticastDelegate

---

#### AssemblyMetadataAttribute

**Line:** 265062

**Inherits:** Attribute

---

#### AssemblyName

**Line:** 267877

**Inherits:** ICloneable

**Fields:**

- `name`: string
- `codebase`: string
- `major`: int
- `minor`: int
- `build`: int
- `revision`: int
- `cultureinfo`: CultureInfo
- `flags`: AssemblyNameFlags
- `hashalg`: AssemblyHashAlgorithm
- `keypair`: StrongNameKeyPair
- `versioncompat`: AssemblyVersionCompatibility
- `version`: Version
- `processor_architecture`: ProcessorArchitecture
- `contentType`: AssemblyContentType

---

#### AssemblyProductAttribute

**Line:** 265091

**Inherits:** Attribute

---

#### AssemblyResolver

**Line:** 1583932

---

#### AssemblyTitleAttribute

**Line:** 265105

**Inherits:** Attribute

---

#### AssemblyTrademarkAttribute

**Line:** 265119

**Inherits:** Attribute

---

#### AssertionException

**Line:** 891303

**Inherits:** Exception

**Fields:**

- `m_UserMessage`: string

---

#### AssetBundle

**Line:** 1589317

**Inherits:** Object

---

#### AssetBundleCreateRequest

**Line:** 1589422

**Inherits:** AsyncOperation

---

#### AssetBundleProvider

**Line:** 1436850

**Inherits:** ResourceProviderBase

---

#### AssetBundleRecompressOperation

**Line:** 1589443

**Inherits:** AsyncOperation

---

#### AssetBundleRequest

**Line:** 1589461

**Inherits:** ResourceRequest

---

#### AssetBundleRequestOptions

**Line:** 1436540

**Inherits:** ILocationSizeData

**Fields:**

- `m_Hash`: string
- `m_Crc`: uint
- `m_Timeout`: int
- `m_ChunkedTransfer`: bool
- `m_RedirectLimit`: int
- `m_RetryCount`: int
- `m_BundleName`: string
- `m_AssetLoadMode`: AssetLoadMode
- `m_BundleSize`: long
- `m_UseCrcForCachedBundles`: bool
- `m_UseUWRForLocalBundles`: bool
- `m_ClearOtherCachedVersionsWhenLoaded`: bool

---

#### AssetBundleResource

**Line:** 1436711

**Inherits:** IAssetBundleResource

**Fields:**

- `m_AssetBundle`: AssetBundle
- `m_RequestOperation`: AsyncOperation
- `m_RequestCompletedCallbackCalled`: bool
- `m_Retries`: int
- `m_Source`: BundleSource
- `m_BytesToDownload`: long
- `m_DownloadedBytes`: long
- `m_Completed`: bool
- `m_UnloadOperation`: AssetBundleUnloadOperation
- `m_TransformedInternalId`: string
- `m_PreloadRequest`: AssetBundleRequest
- `m_PreloadCompleted`: bool
- `m_LastDownloadedByteCount`: ulong
- `m_TimeoutTimer`: float
- `m_TimeoutOverFrames`: int
- `m_LastFrameCount`: int
- `m_TimeSecSinceLastUpdate`: float

---

#### AssetBundleUnloadOperation

**Line:** 1589505

**Inherits:** AsyncOperation

---

#### AssetDatabaseRefreshAnalytic

**Line:** 1586986

**Inherits:** AnalyticsEventBase

**Fields:**

- `isV2`: bool
- `Imports_Imported`: long
- `Imports_ImportedInProcess`: long
- `Imports_ImportedOutOfProcess`: long
- `Imports_Refresh`: long
- `Imports_DomainReload`: long
- `CacheServer_MetadataRequested`: long
- `CacheServer_MetadataDownloaded`: long
- `CacheServer_MetadataFailedToDownload`: long
- `CacheServer_MetadataUploaded`: long
- `CacheServer_ArtifactsFailedToUpload`: long
- `CacheServer_MetadataVersionsDownloaded`: long
- `CacheServer_MetadataMatched`: long
- `CacheServer_ArtifactsDownloaded`: long
- `CacheServer_ArtifactFilesDownloaded`: long
- `CacheServer_ArtifactFilesFailedToDownload`: long
- `CacheServer_ArtifactsUploaded`: long
- `CacheServer_ArtifactFilesUploaded`: long
- `CacheServer_ArtifactFilesFailedToUpload`: long
- `CacheServer_Connects`: long
- ... (1 more fields)

---

#### AssetLabelReference

**Line:** 1455508

**Inherits:** IKeyEvaluator

**Fields:**

- `m_LabelString`: string

---

#### AssetReference

**Line:** 1455650

**Inherits:** IKeyEvaluator

**Fields:**

- `m_SubObjectName`: string
- `m_SubObjectType`: string
- `m_Operation`: AsyncOperationHandle

---

#### AssetReferenceAtlasedSprite

**Line:** 1455634

**Inherits:** AssetReferenceT

---

#### AssetReferenceGameObject

**Line:** 1455581

**Inherits:** AssetReferenceT

---

#### AssetReferenceSprite

**Line:** 1455621

**Inherits:** AssetReferenceT

---

#### AssetReferenceT

**Line:** 1455542

---

#### AssetReferenceTexture

**Line:** 1455591

**Inherits:** AssetReferenceT

---

#### AssetReferenceTexture2D

**Line:** 1455601

**Inherits:** AssetReferenceT

---

#### AssetReferenceTexture3D

**Line:** 1455611

**Inherits:** AssetReferenceT

---

#### AssetReferenceUILabelRestriction

**Line:** 1453592

**Inherits:** AssetReferenceUIRestriction

**Fields:**

- `m_CachedToString`: string

---

#### AssetReferenceUIRestriction

**Line:** 1453576

**Inherits:** Attribute

---

#### AssetTable

**Line:** 1317146

**Inherits:** DetailedLocalizationTable

**Fields:**

- `m_PreloadOperationHandle`: AsyncOperationHandle

---

#### AssetTableEntry

**Line:** 1317069

**Inherits:** TableEntry

**Fields:**

- `m_GuidCache`: string
- `m_SubAssetNameCache`: string

---

#### AssociationAttribute

**Line:** 1508675

**Inherits:** Attribute

---

#### AssumeRangeAttribute

**Line:** 1346066

**Inherits:** Attribute

---

#### AsymmetricAlgorithm

**Line:** 217873

**Inherits:** IDisposable

**Fields:**

- `KeySizeValue`: int

---

#### AsymmetricSignatureDeformatter

**Line:** 217911

---

#### AsymmetricSignatureFormatter

**Line:** 217930

---

#### AsyncAnimatorIKTrigger

**Line:** 1132371

**Inherits:** AsyncTriggerBase

---

#### AsyncAnimatorMoveTrigger

**Line:** 1132405

**Inherits:** AsyncTriggerBase

---

#### AsyncApplicationFocusTrigger

**Line:** 1132439

**Inherits:** AsyncTriggerBase

---

#### AsyncApplicationPauseTrigger

**Line:** 1132473

**Inherits:** AsyncTriggerBase

---

#### AsyncApplicationQuitTrigger

**Line:** 1132507

**Inherits:** AsyncTriggerBase

---

#### AsyncAudioFilterReadTrigger

**Line:** 1132542

**Inherits:** AsyncTriggerBase

---

#### AsyncAwakeTrigger

**Line:** 1128556

**Inherits:** AsyncTriggerBase

---

#### AsyncBecameInvisibleTrigger

**Line:** 1132576

**Inherits:** AsyncTriggerBase

---

#### AsyncBecameVisibleTrigger

**Line:** 1132610

**Inherits:** AsyncTriggerBase

---

#### AsyncBeforeTransformParentChangedTrigger

**Line:** 1132644

**Inherits:** AsyncTriggerBase

---

#### AsyncBeginDragTrigger

**Line:** 1134005

**Inherits:** AsyncTriggerBase

---

#### AsyncCallback

**Line:** 20418

**Inherits:** MulticastDelegate

---

#### AsyncCancelTrigger

**Line:** 1134039

**Inherits:** AsyncTriggerBase

---

#### AsyncCollisionEnter2DTrigger

**Line:** 1132746

**Inherits:** AsyncTriggerBase

---

#### AsyncCollisionEnterTrigger

**Line:** 1132712

**Inherits:** AsyncTriggerBase

---

#### AsyncCollisionExit2DTrigger

**Line:** 1132814

**Inherits:** AsyncTriggerBase

---

#### AsyncCollisionExitTrigger

**Line:** 1132780

**Inherits:** AsyncTriggerBase

---

#### AsyncCollisionStay2DTrigger

**Line:** 1132882

**Inherits:** AsyncTriggerBase

---

#### AsyncCollisionStayTrigger

**Line:** 1132848

**Inherits:** AsyncTriggerBase

---

#### AsyncControllerColliderHitTrigger

**Line:** 1132916

**Inherits:** AsyncTriggerBase

---

#### AsyncDeselectTrigger

**Line:** 1134073

**Inherits:** AsyncTriggerBase

---

#### AsyncDestroyTrigger

**Line:** 1128605

**Inherits:** MonoBehaviour

**Fields:**

- `awakeCalled`: bool
- `called`: bool
- `cancellationTokenSource`: CancellationTokenSource

---

#### AsyncDisableTrigger

**Line:** 1132950

**Inherits:** AsyncTriggerBase

---

#### AsyncDragTrigger

**Line:** 1134107

**Inherits:** AsyncTriggerBase

---

#### AsyncDrawGizmosSelectedTrigger

**Line:** 1133018

**Inherits:** AsyncTriggerBase

---

#### AsyncDrawGizmosTrigger

**Line:** 1132984

**Inherits:** AsyncTriggerBase

---

#### AsyncEnableTrigger

**Line:** 1133052

**Inherits:** AsyncTriggerBase

---

#### AsyncEndDragTrigger

**Line:** 1134175

**Inherits:** AsyncTriggerBase

---

#### AsyncFixedUpdateTrigger

**Line:** 1132303

**Inherits:** AsyncTriggerBase

---

#### AsyncGUITrigger

**Line:** 1133086

**Inherits:** AsyncTriggerBase

---

#### AsyncInitializePotentialDragTrigger

**Line:** 1134209

**Inherits:** AsyncTriggerBase

---

#### AsyncInstantiateOperation

**Line:** 881328

---

#### AsyncIteratorStateMachineAttribute

**Line:** 230083

**Inherits:** StateMachineAttribute

---

#### AsyncJointBreak2DTrigger

**Line:** 1133154

**Inherits:** AsyncTriggerBase

---

#### AsyncJointBreakTrigger

**Line:** 1133120

**Inherits:** AsyncTriggerBase

---

#### AsyncLateUpdateTrigger

**Line:** 1132337

**Inherits:** AsyncTriggerBase

---

#### AsyncLazy

**Line:** 1094892

**Fields:**

- `completionSource`: UniTaskCompletionSource<T>
- `syncLock`: object
- `initialized`: bool

---

#### AsyncLocal

**Line:** 178807

---

#### AsyncMethodBuilderAttribute

**Line:** 230093

**Inherits:** Attribute

---

#### AsyncMoveTrigger

**Line:** 1134243

**Inherits:** AsyncTriggerBase

---

#### AsyncOnCanvasGroupChangedTrigger

**Line:** 1132678

**Inherits:** AsyncTriggerBase

---

#### AsyncOperation

**Line:** 881396

**Inherits:** YieldInstruction

**Fields:**

- `m_completeCallback`: Action<AsyncOperation>

---

#### AsyncOperationBase

**Line:** 1438459

**Fields:**

- `m_referenceCount`: int
- `m_DestroyedAction`: DelegateList<AsyncOperationHandle>
- `m_OnDestroyAction`: Action<IAsyncOperation>
- `m_dependencyCompleteAction`: Action<AsyncOperationHandle>
- `Executed`: Action
- `m_taskCompletionSource`: TaskCompletionSource<TObject>
- `m_taskCompletionSourceTypeless`: TaskCompletionSource<object>
- `m_InDeferredCallbackQueue`: bool
- `m_UpdateCallbacks`: DelegateList<float>
- `m_UpdateCallback`: Action<float>

---

#### AsyncParticleCollisionTrigger

**Line:** 1133188

**Inherits:** AsyncTriggerBase

---

#### AsyncParticleSystemStoppedTrigger

**Line:** 1133222

**Inherits:** AsyncTriggerBase

---

#### AsyncParticleTriggerTrigger

**Line:** 1133256

**Inherits:** AsyncTriggerBase

---

#### AsyncParticleUpdateJobScheduledTrigger

**Line:** 1133290

**Inherits:** AsyncTriggerBase

---

#### AsyncPointerClickTrigger

**Line:** 1134277

**Inherits:** AsyncTriggerBase

---

#### AsyncPointerDownTrigger

**Line:** 1134311

**Inherits:** AsyncTriggerBase

---

#### AsyncPointerEnterTrigger

**Line:** 1134345

**Inherits:** AsyncTriggerBase

---

#### AsyncPointerExitTrigger

**Line:** 1134379

**Inherits:** AsyncTriggerBase

---

#### AsyncPointerUpTrigger

**Line:** 1134413

**Inherits:** AsyncTriggerBase

---

#### AsyncPollSourceSet

**Line:** 546052

**Fields:**

- `_count`: int
- `_deadlineAt`: Nullable<DateTime>
- `_ct`: CancellationToken
- `_alreadyTriggered`: bool
- `_cachedDeadlineTask`: Task
- `_cachedDeadlineAt`: DateTime
- `_cachedDeadlineCt`: CancellationToken

---

#### AsyncPostRenderTrigger

**Line:** 1133324

**Inherits:** AsyncTriggerBase

---

#### AsyncPreCullTrigger

**Line:** 1133358

**Inherits:** AsyncTriggerBase

---

#### AsyncPreRenderTrigger

**Line:** 1133392

**Inherits:** AsyncTriggerBase

---

#### AsyncReactiveProperty

**Line:** 1095420

**Fields:**

- `triggerEvent`: TriggerEvent<T>
- `latestValue`: T

---

#### AsyncReadManagerMetricsFilters

**Line:** 837870

---

#### AsyncRectTransformDimensionsChangeTrigger

**Line:** 1133426

**Inherits:** AsyncTriggerBase

---

#### AsyncRectTransformRemovedTrigger

**Line:** 1133460

**Inherits:** AsyncTriggerBase

---

#### AsyncRenderImageTrigger

**Line:** 1133495

**Inherits:** AsyncTriggerBase

---

#### AsyncRenderObjectTrigger

**Line:** 1133529

**Inherits:** AsyncTriggerBase

---

#### AsyncResetTrigger

**Line:** 1133937

**Inherits:** AsyncTriggerBase

---

#### AsyncResult

**Line:** 223561

**Inherits:** IAsyncResult

**Fields:**

- `async_state`: object
- `handle`: WaitHandle
- `async_delegate`: object
- `data`: IntPtr
- `object_data`: object
- `sync_completed`: bool
- `completed`: bool
- `endinvoke_called`: bool
- `async_callback`: object
- `current`: ExecutionContext
- `original`: ExecutionContext
- `add_time`: long
- `call_message`: MonoMethodMessage
- `message_ctrl`: IMessageCtrl
- `reply_message`: IMessage
- `orig_cb`: WaitCallback

---

#### AsyncScrollTrigger

**Line:** 1134447

**Inherits:** AsyncTriggerBase

---

#### AsyncSelectTrigger

**Line:** 1134481

**Inherits:** AsyncTriggerBase

---

#### AsyncServerInitializedTrigger

**Line:** 1133563

**Inherits:** AsyncTriggerBase

---

#### AsyncStartTrigger

**Line:** 1128635

**Inherits:** AsyncTriggerBase

**Fields:**

- `called`: bool

---

#### AsyncStateMachineAttribute

**Line:** 230108

**Inherits:** StateMachineAttribute

---

#### AsyncSubmitTrigger

**Line:** 1134515

**Inherits:** AsyncTriggerBase

---

#### AsyncTransformChildrenChangedTrigger

**Line:** 1133597

**Inherits:** AsyncTriggerBase

---

#### AsyncTransformParentChangedTrigger

**Line:** 1133631

**Inherits:** AsyncTriggerBase

---

#### AsyncTriggerBase

**Line:** 1129237

**Fields:**

- `triggerEvent`: TriggerEvent<T>

---

#### AsyncTriggerEnter2DTrigger

**Line:** 1133699

**Inherits:** AsyncTriggerBase

---

#### AsyncTriggerEnterTrigger

**Line:** 1133665

**Inherits:** AsyncTriggerBase

---

#### AsyncTriggerExit2DTrigger

**Line:** 1133767

**Inherits:** AsyncTriggerBase

---

#### AsyncTriggerExitTrigger

**Line:** 1133733

**Inherits:** AsyncTriggerBase

---

#### AsyncTriggerHandler

**Line:** 1129481

**Fields:**

- `cancellationToken`: CancellationToken
- `registration`: CancellationTokenRegistration
- `isDisposed`: bool
- `callOnce`: bool
- `core`: UniTaskCompletionSourceCore<T>

---

#### AsyncTriggerStay2DTrigger

**Line:** 1133835

**Inherits:** AsyncTriggerBase

---

#### AsyncTriggerStayTrigger

**Line:** 1133801

**Inherits:** AsyncTriggerBase

---

#### AsyncUnityEventHandler

**Line:** 1126820

**Fields:**

- `cancellationToken`: CancellationToken
- `registration`: CancellationTokenRegistration
- `isDisposed`: bool
- `callOnce`: bool
- `core`: UniTaskCompletionSourceCore<T>

---

#### AsyncUpdateSelectedTrigger

**Line:** 1134549

**Inherits:** AsyncTriggerBase

---

#### AsyncUpdateTrigger

**Line:** 1133971

**Inherits:** AsyncTriggerBase

---

#### AsyncValidateTrigger

**Line:** 1133869

**Inherits:** AsyncTriggerBase

---

#### AsyncWillRenderObjectTrigger

**Line:** 1133903

**Inherits:** AsyncTriggerBase

---

#### AtlasSpriteProvider

**Line:** 1436905

**Inherits:** ResourceProviderBase

---

#### AttachToPanelEvent

**Line:** 637443

**Inherits:** PanelChangedEventBase

---

#### Attribute

**Line:** 172020

---

#### AttributeCollection

**Line:** 781057

**Inherits:** ICollection

**Fields:**

- `_index`: int

---

#### AttributeInfo

**Line:** 1584000

---

#### AttributeProviderAttribute

**Line:** 781122

**Inherits:** Attribute

---

#### AttributeUsageAttribute

**Line:** 20462

**Inherits:** Attribute

**Fields:**

- `_attributeTarget`: AttributeTargets
- `_allowMultiple`: bool
- `_inherited`: bool

---

#### AudioAnyDestroyedEventSystem

**Line:** 701619

**Inherits:** ReactiveSystem

---

#### AudioAnyDestroyedListenerComponent

**Line:** 699453

**Inherits:** IComponent

**Fields:**

- `value`: List<IAudioAnyDestroyedListener>

---

#### AudioAttribute

**Line:** 697727

**Inherits:** ContextAttribute

---

#### AudioBehaviour

**Line:** 1587976

**Inherits:** Behaviour

---

#### AudioCleanupSystems

**Line:** 697736

**Inherits:** Feature

---

#### AudioClip

**Line:** 1587951

**Inherits:** AudioResource

---

#### AudioClipComponent

**Line:** 684434

**Inherits:** IComponent

**Fields:**

- `Value`: AudioClip

---

#### AudioConfigComponent

**Line:** 698779

**Inherits:** IComponent

**Fields:**

- `Value`: IAudioConfig

---

#### AudioContext

**Line:** 697809

**Inherits:** Context

---

#### AudioDestroySystem

**Line:** 686802

**Inherits:** ReactiveSystem

---

#### AudioDestroyedEventSystem

**Line:** 701642

**Inherits:** ReactiveSystem

---

#### AudioDestroyedListenerComponent

**Line:** 699466

**Inherits:** IComponent

**Fields:**

- `value`: List<IAudioDestroyedListener>

---

#### AudioEntity

**Line:** 697885

**Inherits:** Entity

---

#### AudioEventSystems

**Line:** 699040

**Inherits:** Feature

---

#### AudioFeature

**Line:** 684423

**Inherits:** Feature

---

#### AudioHelper

**Line:** 705856

---

#### AudioListener

**Line:** 1587987

**Inherits:** AudioBehaviour

---

#### AudioMatcher

**Line:** 698338

---

#### AudioMixer

**Line:** 1588145

**Inherits:** Object

---

#### AudioMuteSaveSystem

**Line:** 684559

**Inherits:** ReactiveSystem

---

#### AudioResource

**Line:** 1588112

**Inherits:** Object

---

#### AudioSampleProvider

**Line:** 1588089

---

#### AudioSettings

**Line:** 1587890

---

#### AudioSettingsView

**Line:** 729160

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton
- `Toggle`: ColoredToggle
- `_audioListener`: AudioEntity

---

#### AudioSource

**Line:** 1587993

**Inherits:** AudioBehaviour

---

#### AudioSourceComponent

**Line:** 684447

**Inherits:** IComponent

**Fields:**

- `Value`: AudioSource

---

#### AudioSourceIdComponent

**Line:** 739508

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### AudioSourceView

**Line:** 684652

**Inherits:** MonoBehaviourSingleton

**Fields:**

- `AudioSource`: AudioSource

---

#### AuthWebUtility

**Line:** 1374457

---

#### AuthenticatedStream

**Line:** 802728

**Inherits:** Stream

**Fields:**

- `_InnerStream`: Stream
- `_LeaveStreamOpen`: bool

---

#### AuthenticationException

**Line:** 778393

**Inherits:** SystemException

---

#### AuthenticationHeaderValue

**Line:** 1488979

**Inherits:** ICloneable

---

#### AuthenticationKey

**Line:** 499221

**Inherits:** IEquatable

**Fields:**

- `Platform`: AuthenticationPlatform
- `Id`: string

---

#### AuthenticationManager

**Line:** 794230

---

#### AuthenticationSchemeSelector

**Line:** 791379

**Inherits:** MulticastDelegate

---

#### AuthenticodeBase

**Line:** 1449706

**Fields:**

- `fs`: Stream
- `blockNo`: int
- `blockLength`: int
- `peOffset`: int
- `dirSecurityOffset`: int
- `dirSecuritySize`: int
- `coffSymbolTableOffset`: int
- `pe64`: bool

---

#### AuthenticodeDeformatter

**Line:** 1449753

**Inherits:** AuthenticodeBase

**Fields:**

- `filename`: string
- `coll`: X509CertificateCollection
- `signedHash`: ASN1
- `timestamp`: DateTime
- `signingCertificate`: X509Certificate
- `reason`: int
- `trustedRoot`: bool
- `trustedTimestampRoot`: bool
- `signerChain`: X509Chain
- `timestampChain`: X509Chain

---

#### AuthorityKeyIdentifierExtension

**Line:** 1448159

**Inherits:** X509Extension

---

#### Authorization

**Line:** 791391

**Fields:**

- `m_Message`: string
- `m_Complete`: bool

---

#### AuthorizationCodeFlow

**Line:** 1376078

**Inherits:** IHttpAuthorizationFlow

---

#### AuthorizationCodeInstalledApp

**Line:** 1369009

**Inherits:** IAuthorizationCodeInstalledApp

---

#### AuthorizationCodeRequestUrl

**Line:** 1374869

**Inherits:** AuthorizationRequestUrl

---

#### AuthorizationCodeResponseUrl

**Line:** 1374470

---

#### AuthorizationCodeTokenRequest

**Line:** 1374881

**Inherits:** TokenRequest

---

#### AuthorizationCodeWebApp

**Line:** 1374395

---

#### AuthorizationRequestUrl

**Line:** 1374930

---

#### AutoFillRequest

**Line:** 1385764

**Inherits:** IDirectResponseSchema

---

#### AutoInitialize

**Line:** 1564258

**Inherits:** MonoBehaviour

**Fields:**

- `Enabled`: bool

---

#### AutoResetEvent

**Line:** 178924

**Inherits:** EventWaitHandle

---

#### AutoResetUniTaskCompletionSource

**Line:** 1122625

**Fields:**

- `nextNode`: AutoResetUniTaskCompletionSource<T>
- `core`: UniTaskCompletionSourceCore<T>
- `version`: short

---

#### AutoResizeDimensionsRequest

**Line:** 1385824

**Inherits:** IDirectResponseSchema

---

#### AutoRunProbabilitiesPopupUiView

**Line:** 734581

**Inherits:** MonoBehaviour

**Fields:**

- `EntryPrefab`: SummonUpgradeEntry
- `EntriesParent`: RectTransform

---

#### AutoRunSteppingStonesResponse

**Line:** 1079443

**Inherits:** PlayerSynchronizedServerActionCore

---

#### AutoSteppingStonesRunResultsMessage

**Line:** 733969

**Inherits:** IMessage

---

#### AvailableComponent

**Line:** 684460

**Inherits:** IComponent

---

#### AvailableTransport

**Line:** 1583059

---

#### Awaitable

**Line:** 882173

**Fields:**

- `_awaitable`: Awaitable
- `_result`: T

---

#### AwsExternalAccountCredential

**Line:** 1369667

**Inherits:** ExternalAccountCredential

---

#### AxisEventData

**Line:** 1359087

**Inherits:** BaseEventData

---

#### BackButtonSystem

**Line:** 736986

**Inherits:** IExecuteSystem

---

#### BackOffHandler

**Line:** 1496813

**Inherits:** IHttpUnsuccessfulResponseHandler

---

#### BadImageFormatException

**Line:** 20497

**Inherits:** SystemException

**Fields:**

- `_fileName`: string
- `_fusionLog`: string

---

#### BadRequestException

**Line:** 685175

**Inherits:** Exception

---

#### BanUserRequest

**Line:** 1528505

**Inherits:** IEquatable

---

#### BandedRange

**Line:** 1385872

**Inherits:** IDirectResponseSchema

---

#### BandingProperties

**Line:** 1385944

**Inherits:** IDirectResponseSchema

---

#### BannerSettings

**Line:** 1564282

**Fields:**

- `generalStyleSettings`: GeneralStyleSettings
- `firstLayerStyleSettings`: FirstLayerStyleSettings
- `secondLayerStyleSettings`: SecondLayerStyleSettings
- `variantName`: string

---

#### Barrier

**Line:** 685346

**Inherits:** Feature

---

#### BaseBoolField

**Line:** 612729

**Inherits:** BaseField

**Fields:**

- `m_Label`: Label
- `m_OriginalText`: string

---

#### BaseClientService

**Line:** 1502768

**Inherits:** IClientService

---

#### BaseCommandBuffer

**Line:** 804426

---

#### BaseCompositeField

**Line:** 613021

**Fields:**

- `m_Fields`: List<TField>
- `m_ShouldUpdateDisplay`: bool
- `m_ForceUpdateDisplay`: bool

---

#### BaseConfig

**Line:** 1059158

**Inherits:** GameConfigKeyValue

---

#### BaseConnectionContext

**Line:** 1569816

**Inherits:** IAsyncDisposable

---

#### BaseEventData

**Line:** 1359146

**Inherits:** AbstractEventData

---

#### BaseField

**Line:** 618365

**Fields:**

- `m_LabelWidthRatio`: float
- `m_LabelExtraPadding`: float
- `m_LabelBaseMinWidth`: float
- `m_VisualInput`: VisualElement
- `viewDataRestored`: Action
- `m_Value`: TValueType
- `onValidateValue`: Func<TValueType, TValueType>
- `m_ShowMixedValue`: bool
- `m_MixedValueLabel`: Label
- `m_SkipValidation`: bool
- `m_CachedContextWidthElement`: VisualElement
- `m_CachedInspectorElement`: VisualElement

---

#### BaseFieldMouseDragger

**Line:** 639349

---

#### BaseFieldTraits

**Line:** 621181

**Fields:**

- `m_Value`: TValueUxmlAttributeType

---

#### BaseInput

**Line:** 1360364

**Inherits:** UIBehaviour

---

#### BaseInputModule

**Line:** 1360436

**Inherits:** UIBehaviour

**Fields:**

- `m_RaycastResultCache`: List<RaycastResult>
- `m_SendPointerHoverToParent`: bool
- `m_AxisEventData`: AxisEventData
- `m_EventSystem`: EventSystem
- `m_BaseEventData`: BaseEventData
- `m_InputOverride`: BaseInput
- `m_DefaultInput`: BaseInput

---

#### BaseItemVisual

**Line:** 713911

**Inherits:** MonoBehaviour

**Fields:**

- `Level`: TMP_Text
- `Icon`: Image
- `BackgroundParent`: Transform
- `_backgroundViewInstance`: ItemBackgroundView

---

#### BaseListView

**Line:** 613301

**Inherits:** BaseVerticalCollectionView

**Fields:**

- `m_ShowBoundCollectionSize`: bool
- `m_ShowFoldoutHeader`: bool
- `m_HeaderTitle`: string
- `drawnHeader`: VisualElement
- `m_MakeHeader`: Func<VisualElement>
- `drawnFooter`: VisualElement
- `m_MakeFooter`: Func<VisualElement>
- `m_ShowAddRemoveFooter`: bool
- `itemsSourceSizeChanged`: Action
- `m_TrackedItem`: IVisualElementScheduledItem
- `m_TrackCount`: Action
- `m_WhileAutoAssign`: Func<bool>
- `m_BindingSourceSelectionMode`: BindingSourceSelectionMode
- `m_ListViewLabel`: Label
- `m_Foldout`: Foldout
- `m_ArraySizeField`: TextField
- `m_IsOverMultiEditLimit`: bool
- `m_Footer`: VisualElement
- `m_AddButton`: Button
- `m_RemoveButton`: Button
- ... (11 more fields)

---

#### BaseListViewController

**Line:** 610263

**Inherits:** CollectionViewController

**Fields:**

- `itemsSourceSizeChanged`: Action

---

#### BaseLogger

**Line:** 1496025

**Inherits:** ILogger

---

#### BaseMeshEffect

**Line:** 1357863

**Inherits:** UIBehaviour

**Fields:**

- `m_Graphic`: Graphic

---

#### BaseNumberConverter

**Line:** 781146

**Inherits:** TypeConverter

---

#### BasePopupField

**Line:** 613684

**Fields:**

- `m_TextElement`: TextElement
- `m_ArrowElement`: VisualElement
- `m_ScheduledShowMenuItem`: IVisualElementScheduledItem

---

#### BaseRaycaster

**Line:** 1360932

**Inherits:** UIBehaviour

**Fields:**

- `m_RootRaycaster`: BaseRaycaster

---

#### BaseRenderFunc

**Line:** 829301

---

#### BaseSlider

**Line:** 613948

**Fields:**

- `m_AdjustedPageSizeFromClick`: float
- `m_IsEditingTextField`: bool
- `m_Fill`: bool
- `m_LowValue`: TValueType
- `m_HighValue`: TValueType
- `m_PageSize`: float
- `m_ShowInputField`: bool
- `m_DragElementStartPos`: Rect
- `onSetValueWithoutNotify`: Action<TValueType>
- `m_Direction`: SliderDirection
- `m_Inverted`: bool

---

#### BaseTreeView

**Line:** 615195

**Inherits:** BaseVerticalCollectionView

**Fields:**

- `itemExpandedChanged`: Action<TreeViewExpansionChangedArgs>
- `m_AutoExpand`: bool
- `m_ExpandedItemIds`: List<int>

---

#### BaseTreeViewController

**Line:** 610634

**Inherits:** CollectionViewController

**Fields:**

- `m_TreeViewDataProperty`: IHierarchyProperty<int>
- `m_HierarchyHasPendingChanged`: bool
- `itemExpandedChanged`: Action<TreeViewExpansionChangedArgs>

---

#### BaseUxmlFactory

**Line:** 669524

---

#### BaseUxmlTraits

**Line:** 669409

---

#### BaseVertexEffect

**Line:** 1357848

---

#### BaseVerticalCollectionView

**Line:** 615598

**Inherits:** BindableElement

**Fields:**

- `itemIndexChanged`: Action<int, int>
- `itemsSourceChanged`: Action
- `m_SelectionNotChanged`: Action
- `canStartDrag`: Func<CanStartDragArgs, bool>
- `setupDragAndDrop`: Func<SetupDragAndDropArgs, StartDragArgs>
- `dragAndDropUpdate`: Func<HandleDragAndDropArgs, DragVisualMode>
- `handleDrop`: Func<HandleDragAndDropArgs, DragVisualMode>
- `m_SelectionType`: SelectionType
- `m_HorizontalScrollingEnabled`: bool
- `m_ShowAlternatingRowBackgrounds`: AlternatingRowBackground
- `m_VirtualizationMethod`: CollectionVirtualizationMethod
- `m_ViewController`: CollectionViewController
- `m_VirtualizationController`: CollectionVirtualizationController
- `m_NavigationManipulator`: KeyboardNavigationManipulator
- `m_SelectedIds`: List<int>
- `m_LastHeight`: float
- `m_IsRangeSelectionDirectionUp`: bool
- `m_Dragger`: ListViewDragger
- `m_ItemIndexChangedCallback`: Action<int, int>
- `m_ItemsSourceChangedCallback`: Action
- ... (4 more fields)

---

#### BaselineValueFormat

**Line:** 1386064

**Inherits:** IDirectResponseSchema

---

#### BasicChartAxis

**Line:** 1386184

**Inherits:** IDirectResponseSchema

---

#### BasicChartDomain

**Line:** 1386268

**Inherits:** IDirectResponseSchema

---

#### BasicChartSeries

**Line:** 1386316

**Inherits:** IDirectResponseSchema

---

#### BasicChartSpec

**Line:** 1386448

**Inherits:** IDirectResponseSchema

---

#### BasicConstraintsExtension

**Line:** 1448186

**Inherits:** X509Extension

**Fields:**

- `cA`: bool
- `pathLenConstraint`: int

---

#### BasicEntity

**Line:** 1057389

**Fields:**

- `Id`: int

---

#### BasicEntityTypeCodes

**Line:** 1057402

---

#### BasicFilter

**Line:** 1386616

**Inherits:** IDirectResponseSchema

---

#### BasicMessageDispatcher

**Line:** 554188

**Inherits:** IMessageDispatcher

**Fields:**

- `_pendingRequests`: ConcurrentDictionary<int, BasicMessageDispatcher.RequestCompleteFn>
- `_runningRequestId`: int
- `_isDispatching`: bool

---

#### BasicSeriesDataPointStyleOverride

**Line:** 1386688

**Inherits:** IDirectResponseSchema

---

#### BatchClearValuesByDataFilterRequest

**Line:** 1386760

**Inherits:** IDirectResponseSchema

---

#### BatchClearValuesByDataFilterResponse

**Line:** 1386796

**Inherits:** IDirectResponseSchema

---

#### BatchClearValuesRequest

**Line:** 1386844

**Inherits:** IDirectResponseSchema

---

#### BatchClearValuesResponse

**Line:** 1386880

**Inherits:** IDirectResponseSchema

---

#### BatchGetValuesByDataFilterRequest

**Line:** 1386928

**Inherits:** IDirectResponseSchema

---

#### BatchGetValuesByDataFilterResponse

**Line:** 1387000

**Inherits:** IDirectResponseSchema

---

#### BatchGetValuesResponse

**Line:** 1387048

**Inherits:** IDirectResponseSchema

---

#### BatchLayer

**Line:** 1376615

---

#### BatchRendererGroup

**Line:** 898035

**Inherits:** IDisposable

**Fields:**

- `m_GroupHandle`: IntPtr

---

#### BatchRequest

**Line:** 1503298

---

#### BatchUpdateSpreadsheetRequest

**Line:** 1387096

**Inherits:** IDirectResponseSchema

---

#### BatchUpdateSpreadsheetResponse

**Line:** 1387168

**Inherits:** IDirectResponseSchema

---

#### BatchUpdateValuesByDataFilterRequest

**Line:** 1387228

**Inherits:** IDirectResponseSchema

---

#### BatchUpdateValuesByDataFilterResponse

**Line:** 1387312

**Inherits:** IDirectResponseSchema

---

#### BatchUpdateValuesRequest

**Line:** 1387408

**Inherits:** IDirectResponseSchema

---

#### BatchUpdateValuesResponse

**Line:** 1387492

**Inherits:** IDirectResponseSchema

---

#### BclDateTimeZone

**Line:** 1148329

**Inherits:** DateTimeZone

---

#### BclDateTimeZoneSource

**Line:** 1148407

**Inherits:** IDateTimeZoneSource

---

#### BearerToken

**Line:** 1369834

---

#### BeforeGameBarrierComponent

**Line:** 685371

**Inherits:** IComponent

**Fields:**

- `Value`: Barrier

---

#### Behaviour

**Line:** 882227

**Inherits:** Component

---

#### BeveledUnityButton

**Line:** 735826

**Inherits:** UnityButton

**Fields:**

- `Image`: Image
- `ButtonScale`: float
- `_defaultColor`: Nullable<Color>
- `IndicatesInteractableState`: bool
- `_anchoredPos`: Vector2

---

#### BigInteger

**Line:** 1449928

**Fields:**

- `length`: uint

---

#### BigQueryAnalyticsFormatAttribute

**Line:** 605251

**Inherits:** Attribute

---

#### BigQueryAnalyticsNameAttribute

**Line:** 605276

**Inherits:** Attribute

---

#### BigQueryAnalyticsRecursionLimitAttribute

**Line:** 605301

**Inherits:** Attribute

---

#### BigQueryDataSourceSpec

**Line:** 1387588

**Inherits:** IDirectResponseSchema

---

#### BigQueryQuerySpec

**Line:** 1387648

**Inherits:** IDirectResponseSchema

---

#### BigQueryTableSpec

**Line:** 1387684

**Inherits:** IDirectResponseSchema

---

#### BinaryCatalogInitialization

**Line:** 1436950

**Inherits:** IInitializableObject

---

#### BinaryConverter

**Line:** 1048238

**Inherits:** JsonConverter

---

#### BinaryExpression

**Line:** 1284764

**Inherits:** Expression

---

#### BinaryFormatter

**Line:** 227265

---

#### BinaryOperationBinder

**Line:** 1299819

**Inherits:** DynamicMetaObjectBinder

---

#### BinaryReader

**Line:** 470450

**Inherits:** IDisposable

**Fields:**

- `m_stream`: Stream
- `m_decoder`: Decoder
- `m_maxCharsSize`: int
- `m_2BytesPerChar`: bool
- `m_isMemoryStream`: bool
- `m_leaveOpen`: bool

---

#### BinaryStorageBuffer

**Line:** 1435342

**Fields:**

- `totalBytes`: uint
- `defaulChunkSize`: uint
- `chunks`: List<BinaryStorageBuffer.Writer.Chunk>
- `existingValues`: Dictionary<Hash128, uint>
- `serializationAdapters`: Dictionary<Type, BinaryStorageBuffer.ISerializationAdapter>

---

#### BinaryWriter

**Line:** 470564

**Inherits:** IDisposable

**Fields:**

- `OutStream`: Stream
- `_encoding`: Encoding
- `_encoder`: Encoder
- `_leaveOpen`: bool
- `_maxChars`: int

---

#### BindIPEndPoint

**Line:** 794283

**Inherits:** MulticastDelegate

---

#### BindableElement

**Line:** 607054

**Inherits:** VisualElement

---

#### Binder

**Line:** 265132

---

#### Binding

**Line:** 607117

**Fields:**

- `m_Dirty`: bool
- `m_UpdateTrigger`: BindingUpdateTrigger

---

#### BindingRestrictions

**Line:** 1299962

---

#### BiomeSfxConfig

**Line:** 705622

**Inherits:** ScriptableObject

---

#### BiomeSfxContainer

**Line:** 705635

**Fields:**

- `Biome`: BiomeSfx
- `Clip`: AudioClip
- `Volume`: float

---

#### BitArray

**Line:** 277283

**Inherits:** ICollection

**Fields:**

- `m_length`: int
- `_version`: int
- `_syncRoot`: object

---

#### BlackScreenFadeUiView

**Line:** 737132

**Inherits:** MonoBehaviourSingleton

**Fields:**

- `_cg`: CanvasGroup

---

#### BlackScreenTransitionUiView

**Line:** 737161

**Inherits:** UiUnityView

**Fields:**

- `_cg`: CanvasGroup
- `_sequence`: Sequence

---

#### BlobConfigArchiveProvider

**Line:** 587901

**Inherits:** ConfigArchiveProvider

**Fields:**

- `_blobProvider`: IBlobProvider
- `_configName`: string

---

#### BlobProviderError

**Line:** 587190

**Inherits:** Exception

---

#### BlobStoragePutHints

**Line:** 499860

**Fields:**

- `ContentType`: string

---

#### BlockExpression

**Line:** 1285816

**Inherits:** Expression

---

#### BlockListEntry

**Line:** 708425

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerMiniProfileUiView`: PlayerMiniProfileUiView
- `_profile`: PlayerChatProfile

---

#### BlockListSettingsView

**Line:** 729192

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton

---

#### BlockListView

**Line:** 708444

**Inherits:** MonoBehaviour

**Fields:**

- `Content`: Transform
- `BlockListEntryPrefab`: BlockListEntry
- `_cancellationTokenSource`: CancellationTokenSource

---

#### Bloom

**Line:** 906712

**Inherits:** VolumeComponent

**Fields:**

- `skipIterations`: ClampedIntParameter
- `threshold`: MinFloatParameter
- `intensity`: MinFloatParameter
- `scatter`: ClampedFloatParameter
- `clamp`: MinFloatParameter
- `tint`: ColorParameter
- `highQualityFiltering`: BoolParameter
- `downscale`: DownscaleParameter
- `maxIterations`: ClampedIntParameter
- `dirtTexture`: TextureParameter
- `dirtIntensity`: MinFloatParameter

---

#### BlurEvent

**Line:** 635479

**Inherits:** FocusEventBase

---

#### BoolControl

**Line:** 1444838

**Inherits:** DataBoundControl

**Fields:**

- `Title`: Text
- `Toggle`: Toggle

---

#### BoolGlobalVariable

**Line:** 1321560

**Inherits:** BoolVariable

---

#### BoolParameter

**Line:** 826944

**Inherits:** VolumeParameter

---

#### BoolTrackedProperty

**Line:** 1328971

**Inherits:** TrackedProperty

---

#### BoolVariable

**Line:** 1324397

**Inherits:** Variable

---

#### BooleanCondition

**Line:** 1387744

**Inherits:** IDirectResponseSchema

---

#### BooleanConverter

**Line:** 781186

**Inherits:** TypeConverter

---

#### BooleanRule

**Line:** 1387792

**Inherits:** IDirectResponseSchema

---

#### BooleanSwitch

**Line:** 777399

**Inherits:** Switch

---

#### Border

**Line:** 1387840

**Inherits:** IDirectResponseSchema

---

#### Borders

**Line:** 1387912

**Inherits:** IDirectResponseSchema

---

#### BottomUiMenuButton

**Line:** 721687

**Inherits:** UiUnityView

**Fields:**

- `Type`: MainScreenType
- `OpenButton`: UnityButton
- `CloseButton`: UnityButton

---

#### BottomUiView

**Line:** 721722

**Inherits:** UiUnityView

---

#### BoundedChannelOptions

**Line:** 1524667

**Inherits:** ChannelOptions

**Fields:**

- `_capacity`: int
- `_mode`: BoundedChannelFullMode

---

#### BoundsField

**Line:** 616104

**Inherits:** BaseField

**Fields:**

- `m_CenterField`: Vector3Field
- `m_ExtentsField`: Vector3Field

---

#### BoundsIntField

**Line:** 616174

**Inherits:** BaseField

**Fields:**

- `m_PositionField`: Vector3IntField
- `m_SizeField`: Vector3IntField

---

#### Box

**Line:** 616222

**Inherits:** VisualElement

---

#### BoxCollider2D

**Line:** 1578724

**Inherits:** Collider2D

---

#### BrowsableAttribute

**Line:** 780557

**Inherits:** Attribute

---

#### BsonObjectId

**Line:** 1049961

---

#### BsonObjectIdConverter

**Line:** 1048272

**Inherits:** JsonConverter

---

#### BsonReader

**Line:** 1050012

**Inherits:** JsonReader

**Fields:**

- `_currentElementType`: BsonType
- `_readRootValueAsArray`: bool
- `_jsonNet35BinaryCompatibility`: bool
- `_dateTimeKindHandling`: DateTimeKind

---

#### BsonWriter

**Line:** 1050457

**Inherits:** JsonWriter

**Fields:**

- `_root`: BsonToken
- `_parent`: BsonToken
- `_propertyName`: string

---

#### BubbleChartSpec

**Line:** 1387984

**Inherits:** IDirectResponseSchema

---

#### BubbleSparkle

**Line:** 721737

**Inherits:** MonoBehaviour

---

#### BufferedLogRecord

**Line:** 1536956

---

#### BufferedRTHandleSystem

**Line:** 822088

**Inherits:** IDisposable

**Fields:**

- `m_RTHandles`: Dictionary<int, RTHandle[]>
- `m_RTHandleSystem`: RTHandleSystem
- `m_DisposedValue`: bool

---

#### BugReport

**Line:** 1445030

**Fields:**

- `ConsoleLog`: List<ConsoleEntry>
- `Email`: string
- `UserDescription`: string

---

#### BugReportApi

**Line:** 1446689

**Fields:**

- `_isBusy`: bool
- `_webRequest`: UnityWebRequest

---

#### BugReportApiService

**Line:** 1445560

**Inherits:** SRServiceBase

**Fields:**

- `_completeCallback`: BugReportCompleteCallback
- `_errorMessage`: string
- `_isBusy`: bool
- `_previousProgress`: float
- `_progressCallback`: BugReportProgressCallback
- `_reportApi`: BugReportApi

---

#### BugReportCompleteCallback

**Line:** 1445046

**Inherits:** MulticastDelegate

---

#### BugReportPopoverRoot

**Line:** 1443430

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `CanvasGroup`: CanvasGroup
- `Container`: RectTransform

---

#### BugReportPopoverService

**Line:** 1445635

**Inherits:** SRServiceBase

**Fields:**

- `_callback`: BugReportCompleteCallback
- `_isVisible`: bool
- `_popover`: BugReportPopoverRoot
- `_sheet`: BugReportSheetController

---

#### BugReportProgressCallback

**Line:** 1445064

**Inherits:** MulticastDelegate

---

#### BugReportScreenshotUtil

**Line:** 1446794

---

#### BugReportSheetController

**Line:** 1443484

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `ButtonContainer`: GameObject
- `ButtonText`: Text
- `CancelButton`: Button
- `CancelPressed`: Action
- `DescriptionField`: InputField
- `EmailField`: InputField
- `ProgressBar`: Slider
- `ResultMessageText`: Text
- `ScreenshotComplete`: Action
- `SubmitButton`: Button
- `SubmitComplete`: Action<bool, string>
- `TakingScreenshot`: Action

---

#### BugReportTabController

**Line:** 1443103

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `BugReportSheetPrefab`: BugReportSheetController
- `Container`: RectTransform

---

#### BuildAssetBundleAnalytic

**Line:** 1587046

**Inherits:** AnalyticsEventBase

**Fields:**

- `success`: bool
- `error`: string

---

#### BullView

**Line:** 731146

**Inherits:** MonoBehaviour

**Fields:**

- `_restPosition`: Vector3
- `_timer`: float
- `_speed`: float
- `_circleRadius`: float

---

#### BundledAssetProvider

**Line:** 1437140

**Inherits:** ResourceProviderBase

---

#### BurstAuthorizedExternalMethodAttribute

**Line:** 869166

**Inherits:** Attribute

---

#### BurstCompatibleAttribute

**Line:** 1184643

**Inherits:** Attribute

---

#### BurstCompileAttribute

**Line:** 1329709

**Inherits:** Attribute

---

#### BurstCompilerOptions

**Line:** 1330158

**Fields:**

- `_enableBurstCompilation`: bool
- `_enableBurstCompileSynchronously`: bool
- `_enableBurstSafetyChecks`: bool
- `_enableBurstTimings`: bool
- `_enableBurstDebug`: bool
- `_forceEnableBurstSafetyChecks`: bool

---

#### BurstDiscardAttribute

**Line:** 869176

**Inherits:** Attribute

---

#### Button

**Line:** 1351603

**Inherits:** Selectable

---

#### ButtonAttribute

**Line:** 696432

**Inherits:** Attribute

---

#### ButtonLayout

**Line:** 1565253

**Fields:**

- `type`: ButtonLayoutType
- `buttons`: List<ButtonSettings>
- `gridButtons`: List<ButtonSettingsRow>

---

#### ButtonSettings

**Line:** 1565308

**Fields:**

- `type`: ButtonType
- `textSize`: float
- `textColor`: string
- `backgroundColor`: string
- `cornerRadius`: float
- `isAllCaps`: bool

---

#### ButtonSettingsRow

**Line:** 1565295

**Fields:**

- `buttons`: List<ButtonSettings>

---

#### ButtonStripField

**Line:** 616341

---

#### BypassElement

**Line:** 803089

**Inherits:** ConfigurationElement

---

#### BypassElementCollection

**Line:** 803095

**Inherits:** ConfigurationElementCollection

---

#### ByteArrayContent

**Line:** 1488167

**Inherits:** HttpContent

---

#### ByteConverter

**Line:** 781213

**Inherits:** BaseNumberConverter

---

#### ByteTrackedProperty

**Line:** 1328841

**Inherits:** TrackedProperty

---

#### ByteVariable

**Line:** 1324461

**Inherits:** Variable

---

#### CCPAData

**Line:** 1564835

**Fields:**

- `version`: int
- `noticeGiven`: bool
- `optedOut`: bool
- `lspact`: bool
- `uspString`: string

---

#### CLSCompliantAttribute

**Line:** 20890

**Inherits:** Attribute

**Fields:**

- `_compliant`: bool

---

#### COMException

**Line:** 228938

**Inherits:** ExternalException

---

#### CacheControlHeaderValue

**Line:** 1489038

**Inherits:** ICloneable

**Fields:**

- `extensions`: List<NameValueHeaderValue>
- `no_cache_headers`: List<string>
- `private_headers`: List<string>

---

#### CacheInitialization

**Line:** 1457006

**Inherits:** IInitializableObject

---

#### CacheInitializationData

**Line:** 1457028

**Fields:**

- `m_CompressionEnabled`: bool
- `m_CacheDirectoryOverride`: string
- `m_LimitCacheSize`: bool
- `m_MaximumCacheSize`: long

---

#### Caching

**Line:** 870677

---

#### CachingBlobProvider

**Line:** 587334

**Inherits:** IBlobProvider

**Fields:**

- `_provider`: IBlobProvider
- `_cache`: IBlobProvider

---

#### Calendar

**Line:** 272926

**Inherits:** ICloneable

**Fields:**

- `m_isReadOnly`: bool

---

#### CalendarSystem

**Line:** 1142804

---

#### CallContext

**Line:** 223344

---

#### CallResult

**Line:** 684684

---

#### CallSite

**Line:** 1298850

**Fields:**

- `Target`: T

---

#### CallSiteBinder

**Line:** 1298999

---

#### CallbackEventHandler

**Line:** 635153

**Inherits:** IEventHandler

---

#### CallerFilePathAttribute

**Line:** 231095

**Inherits:** Attribute

---

#### CallerLineNumberAttribute

**Line:** 231105

**Inherits:** Attribute

---

#### CamelCaseNamingStrategy

**Line:** 1037836

**Inherits:** NamingStrategy

---

#### CamelCasePropertyNamesContractResolver

**Line:** 1037857

**Inherits:** DefaultContractResolver

---

#### Camera

**Line:** 870830

**Inherits:** Behaviour

---

#### CameraHistoryItem

**Line:** 804288

**Inherits:** ContextItem

**Fields:**

- `m_owner`: BufferedRTHandleSystem
- `m_TypeId`: uint

---

#### CameraSwitcher

**Line:** 804325

**Inherits:** MonoBehaviour

**Fields:**

- `m_CurrentCameraIndex`: int
- `m_OriginalCamera`: Camera
- `m_OriginalCameraPosition`: Vector3
- `m_OriginalCameraRotation`: Quaternion
- `m_CurrentCamera`: Camera
- `m_DebugEntryEnumIndex`: int

---

#### CanBeNullAttribute

**Line:** 869249

**Inherits:** Attribute

---

#### CancelDataSourceRefreshRequest

**Line:** 1388152

**Inherits:** IDirectResponseSchema

---

#### CancelDataSourceRefreshResponse

**Line:** 1388212

**Inherits:** IDirectResponseSchema

---

#### CancelDataSourceRefreshStatus

**Line:** 1388248

**Inherits:** IDirectResponseSchema

---

#### CancelInvocationMessage

**Line:** 1568664

**Inherits:** HubInvocationMessage

---

#### CancellationChangeToken

**Line:** 1559020

**Inherits:** IChangeToken

---

#### CancellationTokenEqualityComparer

**Line:** 1096081

**Inherits:** IEqualityComparer

---

#### CancellationTokenSource

**Line:** 179549

**Inherits:** IDisposable

**Fields:**

- `_kernelEvent`: ManualResetEvent
- `_state`: int
- `_threadIDExecutingCallbacks`: int
- `_disposed`: bool
- `_executingCallback`: CancellationCallbackInfo
- `_timer`: Timer

---

#### CandlestickChartSpec

**Line:** 1388296

**Inherits:** IDirectResponseSchema

---

#### CandlestickData

**Line:** 1388344

**Inherits:** IDirectResponseSchema

---

#### CandlestickDomain

**Line:** 1388416

**Inherits:** IDirectResponseSchema

---

#### CandlestickSeries

**Line:** 1388464

**Inherits:** IDirectResponseSchema

---

#### CannotUnloadAppDomainException

**Line:** 72408

**Inherits:** SystemException

---

#### CannotWriteCredentialsOnDiskError

**Line:** 1306686

**Inherits:** Exception

---

#### Canvas

**Line:** 1576413

**Inherits:** Behaviour

---

#### CanvasGroup

**Line:** 1576048

**Inherits:** Behaviour

---

#### CanvasRenderer

**Line:** 1576120

**Inherits:** Component

---

#### CanvasScaler

**Line:** 1354409

**Inherits:** UIBehaviour

**Fields:**

- `m_ReferencePixelsPerUnit`: float
- `m_ScaleFactor`: float
- `m_ReferenceResolution`: Vector2
- `m_MatchWidthOrHeight`: float
- `m_FallbackScreenDPI`: float
- `m_DefaultSpriteDPI`: float
- `m_DynamicPixelsPerUnit`: float
- `m_Canvas`: Canvas
- `m_PrevScaleFactor`: float
- `m_PrevReferencePixelsPerUnit`: float
- `m_PresetInfoIsWorld`: bool

---

#### CanvasUpdateRegistry

**Line:** 1351676

**Fields:**

- `m_PerformingLayoutUpdate`: bool
- `m_PerformingGraphicUpdate`: bool

---

#### Capture

**Line:** 775288

---

#### CaptureCollection

**Line:** 775386

**Inherits:** IList

---

#### CaseInsensitiveComparer

**Line:** 276458

**Inherits:** IComparer

**Fields:**

- `_compareInfo`: CompareInfo

---

#### CaseInsensitiveHashCodeProvider

**Line:** 276478

**Inherits:** IHashCodeProvider

---

#### CatchBlock

**Line:** 1286232

---

#### CategoryAttribute

**Line:** 783404

**Inherits:** Attribute

**Fields:**

- `localized`: bool
- `categoryValue`: string

---

#### CategoryGroup

**Line:** 1443564

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `Container`: RectTransform
- `Header`: Text
- `Background`: GameObject
- `SelectionToggle`: Toggle
- `_selectionModeEnabled`: bool

---

#### CategoryInfoAttribute

**Line:** 888324

**Inherits:** Attribute

---

#### CellData

**Line:** 1388500

**Inherits:** IDirectResponseSchema

---

#### CellFormat

**Line:** 1388668

**Inherits:** IDirectResponseSchema

---

#### CertificateHandler

**Line:** 1565965

**Inherits:** IDisposable

---

#### ChaCha20Poly1305

**Line:** 1519188

**Inherits:** IAeadCipher

**Fields:**

- `mAadCount`: ulong
- `mDataCount`: ulong
- `mBufPos`: int

---

#### ChaCha7539Engine

**Line:** 1519493

**Inherits:** Salsa20Engine

---

#### ChallengeResponse

**Line:** 1448215

**Inherits:** IDisposable

**Fields:**

- `_disposed`: bool

---

#### ChangeEvent

**Line:** 633396

---

#### ChangeSkinVisibilityAction

**Line:** 1075657

**Inherits:** PlayerAction

---

#### Channel

**Line:** 1525349

---

#### ChannelClosedException

**Line:** 1524599

**Inherits:** InvalidOperationException

---

#### ChannelDefinition

**Line:** 694003

---

#### ChannelMixer

**Line:** 909157

**Inherits:** VolumeComponent

**Fields:**

- `redOutRedIn`: ClampedFloatParameter
- `redOutGreenIn`: ClampedFloatParameter
- `redOutBlueIn`: ClampedFloatParameter
- `greenOutRedIn`: ClampedFloatParameter
- `greenOutGreenIn`: ClampedFloatParameter
- `greenOutBlueIn`: ClampedFloatParameter
- `blueOutRedIn`: ClampedFloatParameter
- `blueOutGreenIn`: ClampedFloatParameter
- `blueOutBlueIn`: ClampedFloatParameter

---

#### ChannelOptions

**Line:** 1524621

---

#### ChannelReader

**Line:** 1524967

---

#### ChannelServices

**Line:** 222689

---

#### ChannelWriter

**Line:** 1525229

---

#### CharConverter

**Line:** 781237

**Inherits:** TypeConverter

---

#### CharEnumerator

**Line:** 21120

**Inherits:** IEnumerator

**Fields:**

- `_str`: string
- `_index`: int
- `_currentElement`: char

---

#### CharTrackedProperty

**Line:** 1328861

**Inherits:** TrackedProperty

---

#### CharVector

**Line:** 1492257

**Fields:**

- `collectionRef`: CharVector
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### Character

**Line:** 1346676

**Inherits:** TextElement

---

#### CharacterController

**Line:** 1576777

**Inherits:** Collider

---

#### CharacterRig

**Line:** 710753

**Inherits:** MonoBehaviour

**Fields:**

- `SpineParent`: Transform
- `HpBarParent`: Transform
- `HeadParent`: Transform
- `BodyParent`: Transform
- `WristSecondaryParent`: Transform
- `HandSecondaryParent`: Transform
- `WeaponSecondaryParent`: Transform
- `WristPrimaryParent`: Transform
- `HandPrimaryParent`: Transform
- `WeaponPrimaryParent`: Transform
- `_onFire`: Action

---

#### CharacterSubstitutor

**Line:** 1319812

**Inherits:** IPseudoLocalizationMethod

**Fields:**

- `m_ReplacementsMap`: List<CharacterSubstitutor.CharReplacement>
- `m_ReplacementList`: List<char>

---

#### ChartAxisViewWindowOptions

**Line:** 1388836

**Inherits:** IDirectResponseSchema

---

#### ChartCustomNumberFormatOptions

**Line:** 1388896

**Inherits:** IDirectResponseSchema

---

#### ChartData

**Line:** 1388944

**Inherits:** IDirectResponseSchema

---

#### ChartDateTimeRule

**Line:** 1389016

**Inherits:** IDirectResponseSchema

---

#### ChartGroupRule

**Line:** 1389052

**Inherits:** IDirectResponseSchema

---

#### ChartHistogramRule

**Line:** 1389100

**Inherits:** IDirectResponseSchema

---

#### ChartSourceRange

**Line:** 1389160

**Inherits:** IDirectResponseSchema

---

#### ChartSpec

**Line:** 1389196

**Inherits:** IDirectResponseSchema

---

#### ChatBlockUserAction

**Line:** 1058802

**Inherits:** PlayerAction

---

#### ChatEntry

**Line:** 1058683

---

#### ChatEntryVisual

**Line:** 707664

**Inherits:** MonoBehaviour

**Fields:**

- `_playerMiniProfileUiView`: PlayerMiniProfileUiView
- `MessageText`: TMP_Text
- `MessageTextContainer`: GameObject
- `TimeText`: TMP_Text
- `PvpResultView`: PvpResultUiView
- `ReplayButton`: PvpReplayButtonUiView
- `PvpButton`: HoldDownButton
- `ChatMessageButton`: HoldDownButton

---

#### ChatFeature

**Line:** 705990

**Inherits:** Feature

---

#### ChatFeatureUnlockedMessage

**Line:** 737663

**Inherits:** FeatureUnlockedMessage

---

#### ChatInitializeAction

**Line:** 1058781

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

- `Token`: string
- `ChannelId`: string

---

#### ChatInputValidator

**Line:** 725936

**Inherits:** TMP_InputValidator

**Fields:**

- `_maxLength`: int

---

#### ChatLocalizer

**Line:** 720913

**Inherits:** LocalizerBase

---

#### ChatModel

**Line:** 1058907

---

#### ChatOnboardingAction

**Line:** 1059035

**Inherits:** PlayerAction

**Fields:**

- `IsUnderAge`: bool

---

#### ChatReportView

**Line:** 706062

**Inherits:** UiUnityView

**Fields:**

- `SubmitButton`: UnityButton
- `_chatService`: IChatService

---

#### ChatRoomSettingsDto

**Line:** 1529223

**Inherits:** IEquatable

---

#### ChatServiceComponent

**Line:** 706088

**Inherits:** IComponent

**Fields:**

- `Value`: IChatService

---

#### ChatTextInputUiView

**Line:** 707769

**Inherits:** MonoBehaviour

**Fields:**

- `InputField`: TMP_InputField
- `_chatService`: IChatService
- `_mainChatUiModel`: MainChatUIModel

---

#### ChatUiView

**Line:** 707830

**Inherits:** MonoBehaviour

**Fields:**

- `ChatEntryPrefab`: ChatEntryVisual
- `ChatGuildMessageEntryPrefab`: ChatGuildMessageVisual
- `Parent`: Transform
- `Loading`: GameObject
- `ScrollRectTransform`: RectTransform
- `SwitchRoomTabs`: RectTransform
- `SwitchToWorldButton`: InvisibleButton
- `SwitchToGuildButton`: InvisibleButton
- `WorldSelectedImage`: GameObject
- `GuildSelectedImage`: GameObject
- `WorldNotificationContainer`: GameObject
- `GuildNotificationContainer`: GameObject
- `WorldNotificationText`: TMP_Text
- `GuildNotificationText`: TMP_Text
- `_mainChatUiModel`: MainChatUIModel

---

#### ChatUnblockUserAction

**Line:** 1058833

**Inherits:** PlayerAction

---

#### CheatDesyncSystem

**Line:** 711864

**Inherits:** CheatSystem

---

#### CheatInitBehaviour

**Line:** 738433

**Inherits:** MonoBehaviour

---

#### CheatModel

**Line:** 1056432

---

#### CheatSystem

**Line:** 686566

**Inherits:** IExecuteSystem

---

#### CheatsFeature

**Line:** 685465

**Inherits:** Feature

---

#### CheatsOpenSystem

**Line:** 686551

**Inherits:** CheatSystem

---

#### CheckProfanityRequest

**Line:** 1528809

**Inherits:** IEquatable

---

#### CheckProfanityResponse

**Line:** 1528885

**Inherits:** IEquatable

---

#### CheckoutException

**Line:** 784854

**Inherits:** ExternalException

---

#### ChecksumUtilTest

**Line:** 525646

---

#### ChooseFormatter

**Line:** 1321570

**Inherits:** FormatterBase

**Fields:**

- `m_SplitChar`: char

---

#### ChooseLoginUiView

**Line:** 728861

**Inherits:** MonoBehaviour

**Fields:**

- `GoogleLoginButton`: UnityButton
- `AppleLoginButton`: UnityButton
- `EditorLoginButton`: UnityButton

---

#### ChromaticAberration

**Line:** 909196

**Inherits:** VolumeComponent

**Fields:**

- `intensity`: ClampedFloatParameter

---

#### CinemachineUniversalPixelPerfect

**Line:** 1361244

**Inherits:** MonoBehaviour

---

#### CipherKeyGenerator

**Line:** 1518249

**Fields:**

- `uninitialised`: bool
- `defaultStrength`: int

---

#### CircularBuffer

**Line:** 1442065

**Fields:**

- `_end`: int
- `_count`: int
- `_start`: int

---

#### CircularDependencyException

**Line:** 1512771

**Inherits:** ServicesInitializationException

---

#### CityInfo

**Line:** 538759

**Inherits:** IEquatable

---

#### Claim

**Line:** 220497

**Fields:**

- `m_issuer`: string
- `m_originalIssuer`: string
- `m_type`: string
- `m_value`: string
- `m_valueType`: string
- `m_properties`: Dictionary<string, string>
- `m_propertyLock`: object
- `m_subject`: ClaimsIdentity

---

#### ClaimComponent

**Line:** 692976

**Inherits:** IComponent

---

#### ClaimEventSystem

**Line:** 701705

**Inherits:** ReactiveSystem

---

#### ClaimListenerComponent

**Line:** 699505

**Inherits:** IComponent

**Fields:**

- `value`: List<IClaimListener>

---

#### ClaimableComponent

**Line:** 714610

**Inherits:** IComponent

---

#### ClaimedComponent

**Line:** 692986

**Inherits:** IComponent

---

#### ClaimedEventSystem

**Line:** 701684

**Inherits:** ReactiveSystem

---

#### ClaimedListenerComponent

**Line:** 699492

**Inherits:** IComponent

**Fields:**

- `value`: List<IClaimedListener>

---

#### ClaimsIdentity

**Line:** 220609

**Inherits:** IIdentity

**Fields:**

- `m_instanceClaims`: List<Claim>
- `m_nameType`: string
- `m_roleType`: string
- `m_version`: string
- `m_actor`: ClaimsIdentity
- `m_authenticationType`: string
- `m_bootstrapContext`: object
- `m_label`: string
- `m_serializedNameType`: string
- `m_serializedRoleType`: string
- `m_serializedClaims`: string

---

#### ClaimsPrincipal

**Line:** 220726

**Inherits:** IPrincipal

**Fields:**

- `m_version`: string
- `m_serializedClaimsIdentities`: string
- `m_identities`: List<ClaimsIdentity>

---

#### ClampedFloatParameter

**Line:** 827265

**Inherits:** FloatParameter

**Fields:**

- `min`: float
- `max`: float

---

#### ClampedIntParameter

**Line:** 827100

**Inherits:** IntParameter

**Fields:**

- `min`: int
- `max`: int

---

#### ClassInterfaceAttribute

**Line:** 229057

**Inherits:** Attribute

---

#### CleanupAttribute

**Line:** 1597326

**Inherits:** Attribute

---

#### ClearBasicFilterRequest

**Line:** 1389508

**Inherits:** IDirectResponseSchema

---

#### ClearValuesRequest

**Line:** 1389544

**Inherits:** IDirectResponseSchema

---

#### ClearValuesResponse

**Line:** 1389568

**Inherits:** IDirectResponseSchema

---

#### ClickEvent

**Line:** 638729

**Inherits:** PointerEventBase

---

#### ClickHelperView

**Line:** 737201

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `_isPointerDown`: bool
- `_timeSinceFirstClick`: float
- `_timeSincePreviousFakeClick`: float
- `_interval`: float
- `StartInterval`: float
- `MinInterval`: float
- `Delay`: float

---

#### Clickable

**Line:** 610130

**Inherits:** PointerManipulator

**Fields:**

- `clickedWithEventInfo`: Action<EventBase>
- `clicked`: Action
- `m_ActivePointerId`: int
- `m_AcceptClicksIfDisabled`: bool
- `m_Repeater`: IVisualElementScheduledItem
- `m_PendingActivePseudoStateReset`: IVisualElementScheduledItem

---

#### ClientAvailableIncidentReport

**Line:** 576040

---

#### ClientBuildData

**Line:** 1305084

**Inherits:** IMetaIntegrationSingleton

---

#### ClientDrivenIAPClientDelegate

**Line:** 1312460

**Inherits:** IAPClientDelegate

---

#### ClientDrivenIAPSharedDelegate

**Line:** 583999

**Inherits:** IAPSharedDelegate

---

#### ClientEventBase

**Line:** 605926

**Inherits:** AnalyticsEventBase

---

#### ClientEventConnectionFailure

**Line:** 576358

**Inherits:** ClientEventBase

---

#### ClientGameConfigBuildApiConfig

**Line:** 577145

---

#### ClientLifecycleHintPausing

**Line:** 554295

**Inherits:** MetaMessage

---

#### ClientLifecycleHintSessionStarted

**Line:** 554448

**Inherits:** MetaMessage

---

#### ClientLifecycleHintUnpaused

**Line:** 554375

**Inherits:** MetaMessage

---

#### ClientLifecycleHintUnpausing

**Line:** 554346

**Inherits:** MetaMessage

---

#### ClientListener

**Line:** 737783

**Inherits:** IPlayerModelClientListener

---

#### ClientLogEntry

**Line:** 573993

---

#### ClientLoggingConfig

**Line:** 577118

**Fields:**

- `LogLevel`: LogLevel

---

#### ClientMultiplayerEntityContextInitArgs

**Line:** 552119

---

#### ClientMultiplayerEntityModelJournal

**Line:** 552149

---

#### ClientPlayerModelJournal

**Line:** 576551

**Inherits:** ModelJournal

---

#### ClientSecrets

**Line:** 1369843

---

#### ClientServiceRequest

**Line:** 1503626

---

#### ClientSessionNegotiationResources

**Line:** 576575

**Fields:**

- `ConfigArchives`: MetaDictionary<ContentHash, ConfigArchive>
- `PatchArchives`: MetaDictionary<ContentHash, GameConfigSpecializationPatches>
- `ActiveLanguage`: LocalizationLanguage

---

#### ClientSessionStartResources

**Line:** 576603

---

#### ClientSlot

**Line:** 576645

**Inherits:** DynamicEnum

---

#### ClientSlotCore

**Line:** 576655

**Inherits:** ClientSlot

---

#### ClientSlotLeague

**Line:** 1079759

**Inherits:** ClientSlot

---

#### ClientTerminatedConnectionConnectionError

**Line:** 1308789

**Inherits:** TransientError

---

#### ClientVersion

**Line:** 738583

---

#### ClientWebSocket

**Line:** 801936

**Inherits:** WebSocket

**Fields:**

- `_innerWebSocket`: WebSocketHandle
- `_state`: int

---

#### ClientWebSocketOptions

**Line:** 801995

**Fields:**

- `_isReadOnly`: bool
- `_keepAliveInterval`: TimeSpan
- `_useDefaultCredentials`: bool
- `_credentials`: ICredentials
- `_proxy`: IWebProxy
- `_clientCertificates`: X509CertificateCollection
- `_cookies`: CookieContainer
- `_receiveBufferSize`: int
- `_sendBufferSize`: int

---

#### ClipperRegistry

**Line:** 1351861

---

#### ClockHandAnimation

**Line:** 737097

**Inherits:** MonoBehaviour

**Fields:**

- `ClockHand`: Transform
- `_sequence`: Sequence

---

#### ClockWindersChangeMessage

**Line:** 711718

**Inherits:** CurrencyChangeMessage

---

#### CloseButtonUiView

**Line:** 737229

**Inherits:** UiUnityView

**Fields:**

- `CloseButton`: UnityButton

---

#### CloseMessage

**Line:** 1568676

**Inherits:** HubMessage

---

#### Clouds

**Line:** 734597

**Inherits:** MonoBehaviour

**Fields:**

- `MinMaxSpeed`: Vector2
- `MaxX`: float

---

#### CmpData

**Line:** 1564944

**Fields:**

- `activeVariant`: UsercentricsVariant
- `publishedApps`: List<PublishedApp>
- `userLocation`: UsercentricsLocation

---

#### CodeAccessPermission

**Line:** 216725

**Inherits:** IPermission

---

#### CodeIdentifier

**Line:** 752954

---

#### CodePagesEncodingProvider

**Line:** 1597958

**Inherits:** EncodingProvider

---

#### CoinsChangeMessage

**Line:** 711728

**Inherits:** CurrencyChangeMessage

---

#### CollabOperationAnalytic

**Line:** 1587066

**Inherits:** AnalyticsEventBase

**Fields:**

- `category`: string
- `operation`: string
- `result`: string
- `start_ts`: long
- `duration`: long

---

#### Collection

**Line:** 285346

**Fields:**

- `items`: IList<T>

---

#### CollectionAccessAttribute

**Line:** 869346

**Inherits:** Attribute

---

#### CollectionBase

**Line:** 276497

**Inherits:** IList

**Fields:**

- `_list`: ArrayList

---

#### CollectionChangeEventArgs

**Line:** 781265

**Inherits:** EventArgs

---

#### CollectionChangeEventHandler

**Line:** 781292

**Inherits:** MulticastDelegate

---

#### CollectionConverter

**Line:** 783443

**Inherits:** TypeConverter

---

#### CollectionPool

**Line:** 890024

---

#### CollectionViewController

**Line:** 610825

**Inherits:** IDisposable

**Fields:**

- `m_View`: BaseVerticalCollectionView
- `m_ItemsSource`: IList
- `itemsSourceChanged`: Action
- `itemIndexChanged`: Action<int, int>

---

#### Collector

**Line:** 1547576

**Fields:**

- `_addEntityCache`: GroupChanged<TEntity>
- `_toStringCache`: string
- `_toStringBuilder`: StringBuilder

---

#### CollectorException

**Line:** 1547682

**Inherits:** EntitasException

---

#### Collider

**Line:** 1576782

**Inherits:** Component

---

#### Collider2D

**Line:** 1578673

**Inherits:** Behaviour

---

#### Collision

**Line:** 1576735

**Fields:**

- `m_Header`: ContactPairHeader
- `m_Pair`: ContactPair
- `m_Flipped`: bool

---

#### Collision2D

**Line:** 1578479

---

#### Color

**Line:** 1389616

**Inherits:** IDirectResponseSchema

---

#### ColorAdjustments

**Line:** 909219

**Inherits:** VolumeComponent

**Fields:**

- `postExposure`: FloatParameter
- `contrast`: ClampedFloatParameter
- `colorFilter`: ColorParameter
- `hueShift`: ClampedFloatParameter
- `saturation`: ClampedFloatParameter

---

#### ColorCurves

**Line:** 909250

**Inherits:** VolumeComponent

**Fields:**

- `master`: TextureCurveParameter
- `red`: TextureCurveParameter
- `green`: TextureCurveParameter
- `blue`: TextureCurveParameter
- `hueVsHue`: TextureCurveParameter
- `hueVsSat`: TextureCurveParameter
- `satVsSat`: TextureCurveParameter
- `lumVsSat`: TextureCurveParameter

---

#### ColorGamutUtility

**Line:** 873354

---

#### ColorGradingLutPass

**Line:** 919052

**Inherits:** ScriptableRenderPass

**Fields:**

- `m_InternalLut`: RTHandle
- `m_AllowColorGradingACESHDR`: bool

---

#### ColorLookup

**Line:** 909287

**Inherits:** VolumeComponent

**Fields:**

- `texture`: TextureParameter
- `contribution`: ClampedFloatParameter

---

#### ColorParameter

**Line:** 827364

**Inherits:** VolumeParameter

**Fields:**

- `hdr`: bool
- `showAlpha`: bool
- `showEyeDropper`: bool

---

#### ColorPlugin

**Line:** 1429293

**Inherits:** ABSTweenPlugin

---

#### ColorStyle

**Line:** 1389688

**Inherits:** IDirectResponseSchema

---

#### ColorTween

**Line:** 1358302

---

#### ColorUsageAttribute

**Line:** 880890

**Inherits:** PropertyAttribute

---

#### ColorUtility

**Line:** 878940

---

#### ColoredToggle

**Line:** 728887

**Inherits:** MonoBehaviour

**Fields:**

- `Parent`: RectTransform
- `Child`: RectTransform
- `BackgroundImage`: Image
- `_isActive`: bool
- `_tween`: Sequence

---

#### Column

**Line:** 625160

**Inherits:** INotifyBindablePropertyChanged

**Fields:**

- `m_Name`: string
- `m_Title`: string
- `m_Icon`: Background
- `m_Visible`: bool
- `m_Width`: Length
- `m_MinWidth`: Length
- `m_MaxWidth`: Length
- `m_DesiredWidth`: float
- `m_Stretchable`: bool
- `m_Sortable`: bool
- `m_Optional`: bool
- `m_Resizable`: bool
- `m_HeaderTemplate`: VisualTreeAsset
- `m_CellTemplate`: VisualTreeAsset
- `m_MakeHeader`: Func<VisualElement>
- `m_BindHeader`: Action<VisualElement>
- `m_UnbindHeader`: Action<VisualElement>
- `m_DestroyHeader`: Action<VisualElement>
- `m_MakeCell`: Func<VisualElement>
- `m_BindCell`: Action<VisualElement, int>
- ... (4 more fields)

---

#### ColumnAttribute

**Line:** 1510824

**Inherits:** Attribute

**Fields:**

- `_order`: int
- `_typeName`: string

---

#### Columns

**Line:** 625758

**Inherits:** ICollection

**Fields:**

- `m_Columns`: IList<Column>
- `m_DisplayColumns`: List<Column>
- `m_VisibleColumns`: List<Column>
- `m_VisibleColumnsDirty`: bool
- `m_Reorderable`: bool
- `m_Resizable`: bool
- `m_ResizePreview`: bool
- `m_PrimaryColumnName`: string
- `propertyChanged`: EventHandler<BindablePropertyChangedEventArgs>
- `changed`: Action<ColumnsDataType>
- `columnAdded`: Action<Column, int>
- `columnRemoved`: Action<Column>
- `columnChanged`: Action<Column, ColumnDataType>
- `columnResized`: Action<Column>
- `columnReordered`: Action<Column, int, int>

---

#### ComCompatibleVersionAttribute

**Line:** 229337

**Inherits:** Attribute

---

#### ComDefaultInterfaceAttribute

**Line:** 229031

**Inherits:** Attribute

---

#### ComImportAttribute

**Line:** 229188

**Inherits:** Attribute

---

#### ComVisibleAttribute

**Line:** 229071

**Inherits:** Attribute

---

#### ComingSoonButton

**Line:** 721756

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### CommandBuffer

**Line:** 892956

**Inherits:** IDisposable

---

#### CommandEventBase

**Line:** 634004

**Fields:**

- `m_CommandName`: string

---

#### CommandLineLocaleSelector

**Line:** 1319422

**Inherits:** IStartupLocaleSelector

**Fields:**

- `m_CommandLineArgument`: string

---

#### Comment

**Line:** 1327275

**Inherits:** IMetadata

**Fields:**

- `m_CommentText`: string

---

#### CompId

**Line:** 1059063

**Inherits:** IEquatable

---

#### CompanyIdLoginFlowException

**Line:** 1314660

**Inherits:** Exception

**Fields:**

- `Phase`: string

---

#### CompanyIdLoginFlowHelper

**Line:** 1314553

**Fields:**

- `access_token`: string
- `expires_in`: int

---

#### CompareAttribute

**Line:** 1508734

**Inherits:** ValidationAttribute

---

#### CompareInfo

**Line:** 271134

**Inherits:** IDeserializationCallback

**Fields:**

- `m_name`: string
- `_sortName`: string
- `m_SortVersion`: SortVersion
- `culture`: int
- `collator`: ISimpleCollator

---

#### Comparer

**Line:** 424522

---

#### Comparison

**Line:** 15718

---

#### CompilationRelaxationsAttribute

**Line:** 253439

**Inherits:** Attribute

**Fields:**

- `m_relaxations`: int

---

#### CompilerGeneratedAttribute

**Line:** 231126

**Inherits:** Attribute

---

#### CompletionDispatcher

**Line:** 500036

**Fields:**

- `_cb`: Action<T>
- `_tcs`: TaskCompletionSource<T>

---

#### CompletionMessage

**Line:** 1568713

**Inherits:** HubInvocationMessage

---

#### ComplexTypeAttribute

**Line:** 1510865

**Inherits:** Attribute

---

#### ComplianceTrackingSystem

**Line:** 738832

**Inherits:** IInitSystem

---

#### Component

**Line:** 882336

**Inherits:** Object

---

#### ComponentCollection

**Line:** 780593

**Inherits:** ReadOnlyCollectionBase

---

#### ComponentConverter

**Line:** 783518

**Inherits:** ReferenceConverter

---

#### ComponentNameAttribute

**Line:** 1597361

**Inherits:** Attribute

---

#### ComponentSingleton

**Line:** 1435692

---

#### CompositePatternBuilder

**Line:** 1151389

---

#### CompositeShadowCaster2D

**Line:** 1365006

**Inherits:** ShadowCasterGroup2D

---

#### ComputeBuffer

**Line:** 884798

**Inherits:** IDisposable

---

#### ComputeCommandBuffer

**Line:** 804503

**Inherits:** BaseCommandBuffer

---

#### ComputeCredential

**Line:** 1370176

**Inherits:** ServiceCredential

---

#### ComputeGraphContext

**Line:** 829226

**Inherits:** IDerivedRendergraphContext

**Fields:**

- `wrappedContext`: InternalRenderGraphContext
- `cmd`: ComputeCommandBuffer

---

#### ComputeShader

**Line:** 884916

**Inherits:** Object

---

#### Compute_DT_EventArgs

**Line:** 1221050

**Fields:**

- `EventType`: Compute_DistanceTransform_EventTypes
- `ProgressPercentage`: float

---

#### ConcreteTypeVisitor

**Line:** 1471089

**Inherits:** IPropertyBagVisitor

---

#### ConcurrentBag

**Line:** 786287

**Fields:**

- `_emptyToNonEmptyListTransitionCount`: long

---

#### ConcurrentCache

**Line:** 500236

---

#### ConcurrentDictionary

**Line:** 279968

**Fields:**

- `_comparer`: IEqualityComparer<TKey>
- `_budget`: int
- `_serializationConcurrencyLevel`: int
- `_serializationCapacity`: int

---

#### ConcurrentQueue

**Line:** 278382

**Fields:**

- `_crossSegmentLock`: object

---

#### ConcurrentStack

**Line:** 285227

---

#### ConditionValue

**Line:** 1389736

**Inherits:** IDirectResponseSchema

---

#### ConditionalAttribute

**Line:** 275165

**Inherits:** Attribute

---

#### ConditionalExpression

**Line:** 1286322

**Inherits:** Expression

---

#### ConditionalFormatRule

**Line:** 1389784

**Inherits:** IDirectResponseSchema

---

#### ConditionalFormatter

**Line:** 1321606

**Inherits:** FormatterBase

---

#### ConditionalWeakTable

**Line:** 253664

**Fields:**

- `_lock`: object
- `size`: int

---

#### ConfigArchive

**Line:** 587537

---

#### ConfigArchiveEntry

**Line:** 587444

---

#### ConfigAttribute

**Line:** 1597799

**Inherits:** Attribute

---

#### ConfigHeaderAttribute

**Line:** 1597809

**Inherits:** Attribute

---

#### ConfigInitializeSystem

**Line:** 698791

**Inherits:** IInitializeSystem

---

#### ConfigLexer

**Line:** 526148

---

#### ConfigParser

**Line:** 526560

**Fields:**

- `_useCustomParserFromDerivedLUT`: Dictionary<Type, Type[]>

---

#### ConfigParserProvider

**Line:** 526869

**Inherits:** IMetaIntegration

---

#### ConfigPatchIdSet

**Line:** 596240

---

#### ConfigurableHttpClient

**Line:** 1496893

**Inherits:** HttpClient

---

#### ConfigurableMessageHandler

**Line:** 1497038

**Inherits:** DelegatingHandler

**Fields:**

- `_loggingRequestId`: int
- `_instanceLogger`: ILogger
- `numTries`: int
- `numRedirects`: int

---

#### ConfigurationBuilder

**Line:** 1530411

---

#### ConfigurationCollectionAttribute

**Line:** 1597898

**Inherits:** Attribute

---

#### ConfigurationElement

**Line:** 1597838

---

#### ConfigurationElementCollection

**Line:** 1597893

**Inherits:** ConfigurationElement

---

#### ConfigurationPropertyCollection

**Line:** 1597888

---

#### ConfigurationSection

**Line:** 1597859

**Inherits:** ConfigurationElement

---

#### ConfigurationSectionGroup

**Line:** 1597907

---

#### ConfigureCanvasFromSettings

**Line:** 1443602

**Inherits:** SRMonoBehaviour

**Fields:**

- `_canvas`: Canvas
- `_canvasScaler`: CanvasScaler
- `_originalScale`: float
- `_lastSetScale`: float
- `_settings`: Settings

---

#### ConfigureNamedOptions

**Line:** 1538522

---

#### ConfigureOptions

**Line:** 1538645

---

#### ConfirmationDialogView

**Line:** 718779

**Inherits:** MonoBehaviour

**Fields:**

- `_confirmButton`: UnityButton
- `_cancelButton`: UnityButton

---

#### ConflictException

**Line:** 685094

**Inherits:** Exception

---

#### ConflictResponse

**Line:** 685074

---

#### Connected

**Line:** 1309991

**Inherits:** ConnectionState

---

#### ConnectedToServer

**Line:** 498520

**Inherits:** MetaMessage

**Fields:**

- `ChosenHostname`: string
- `IsIPv4`: bool
- `TlsPeerDescription`: string
- `DnsResolutionDuration`: TimeSpan
- `TcpConnectDuration`: TimeSpan
- `TlsHandshakeDuration`: TimeSpan
- `TlsCertificateFailed`: bool
- `ConnectedAt`: DateTime

---

#### Connecting

**Line:** 1309972

**Inherits:** ConnectionState

---

#### ConnectionAbortedException

**Line:** 1570394

**Inherits:** OperationCanceledException

---

#### ConnectionBuilder

**Line:** 1569919

**Inherits:** IConnectionBuilder

---

#### ConnectionConfig

**Line:** 1306704

**Fields:**

- `ConnectAttemptsMaxCount`: int
- `ConnectAttemptInterval`: TimeSpan
- `SessionResumptionAttemptMaxDuration`: TimeSpan
- `MaxSessionRetainingPauseDuration`: TimeSpan
- `MaxSessionRetainingFrameDuration`: TimeSpan
- `MaxNonErrorMaskingPauseDuration`: TimeSpan
- `ConnectTimeout`: TimeSpan
- `ServerIdentifyTimeout`: TimeSpan
- `ServerSessionInitTimeout`: TimeSpan
- `ConfigFetchAttemptsMaxCount`: int
- `ConfigFetchTimeout`: TimeSpan
- `CloseFlushTimeout`: TimeSpan
- `ServerStatusHintCheckDelay`: TimeSpan
- `ServerStatusHintConnectTimeout`: TimeSpan
- `SessionPingPongDurationIncidentThreshold`: TimeSpan
- `MaxSessionPingPongDurationIncidentsPerSession`: int

---

#### ConnectionContext

**Line:** 1570081

**Inherits:** BaseConnectionContext

---

#### ConnectionDelegate

**Line:** 1570105

**Inherits:** MulticastDelegate

---

#### ConnectionEndpointConfig

**Line:** 577062

**Fields:**

- `ServerHost`: string
- `ServerPort`: int
- `ServerPortForWebSocket`: int
- `EnableTls`: bool
- `CdnBaseUrl`: string
- `PublicWebApiUrl`: string

---

#### ConnectionErrorPopoverScript

**Line:** 738021

**Inherits:** MonoBehaviour

**Fields:**

- `Container`: GameObject
- `Header1Label`: TMP_Text
- `Subheader1Label`: TMP_Text
- `Subheader2Label`: TMP_Text
- `Header2Label`: TMP_Text
- `MainActionButton`: UnityButton
- `MainActionButtonLabel`: TMP_Text
- `SubButtonLabel`: TMP_Text
- `ReconnectButton`: UnityButton
- `ContactSupportButton`: UnityButton

---

#### ConnectionGameConfigInfo

**Line:** 1306817

---

#### ConnectionHandler

**Line:** 1570124

---

#### ConnectionHandshakeFailure

**Line:** 498554

**Inherits:** MetaMessage

---

#### ConnectionItems

**Line:** 1570139

**Inherits:** IDictionary

---

#### ConnectionLostEvent

**Line:** 1306136

---

#### ConnectionManagementElement

**Line:** 803104

**Inherits:** ConfigurationElement

---

#### ConnectionManagementElementCollection

**Line:** 803110

**Inherits:** ConfigurationElementCollection

---

#### ConnectionManagementSection

**Line:** 803119

**Inherits:** ConfigurationSection

---

#### ConnectionResetException

**Line:** 1570411

**Inherits:** IOException

---

#### ConnectionState

**Line:** 1306671

---

#### ConsentApplied

**Line:** 1564972

**Fields:**

- `name`: string
- `templateId`: string
- `consent`: bool
- `mediated`: bool

---

#### ConsentData

**Line:** 738637

---

#### ConsoleCancelEventArgs

**Line:** 70903

**Inherits:** EventArgs

---

#### ConsoleCancelEventHandler

**Line:** 70890

**Inherits:** MulticastDelegate

---

#### ConsoleColors

**Line:** 1583413

---

#### ConsoleEntry

**Line:** 1445156

**Fields:**

- `_messagePreview`: string
- `_stackTracePreview`: string
- `Count`: int
- `LogType`: LogType
- `Message`: string
- `StackTrace`: string

---

#### ConsoleEntryView

**Line:** 1444129

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_count`: int
- `_hasCount`: bool
- `_prevData`: ConsoleEntry
- `_rectTransform`: RectTransform
- `Count`: Text
- `CountContainer`: CanvasGroup
- `ImageStyle`: StyleComponent
- `Message`: Text
- `StackTrace`: Text

---

#### ConsoleLogControl

**Line:** 1444202

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_consoleScrollLayoutGroup`: VirtualVerticalLayoutGroup
- `_consoleScrollRect`: ScrollRect
- `_isDirty`: bool
- `_scrollPosition`: Nullable<Vector2>
- `_showErrors`: bool
- `_showInfo`: bool
- `_showWarnings`: bool
- `SelectedItemChanged`: Action<ConsoleEntry>
- `_filter`: string

---

#### ConsoleLogger

**Line:** 1496127

**Inherits:** BaseLogger

---

#### ConsoleTabController

**Line:** 1443133

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_consoleCanvas`: Canvas
- `_isDirty`: bool
- `ConsoleLogControl`: ConsoleLogControl
- `PinToggle`: Toggle
- `StackTraceScrollRect`: ScrollRect
- `StackTraceText`: Text
- `ToggleErrors`: Toggle
- `ToggleErrorsText`: Text
- `ToggleInfo`: Toggle
- `ToggleInfoText`: Text
- `ToggleWarnings`: Toggle
- `ToggleWarningsText`: Text
- `FilterToggle`: Toggle
- `FilterField`: InputField
- `FilterBarContainer`: GameObject

---

#### ConsoleTabQuickViewControl

**Line:** 1443627

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_prevErrorCount`: int
- `_prevInfoCount`: int
- `_prevWarningCount`: int
- `ConsoleService`: IConsoleService
- `ErrorCountText`: Text
- `InfoCountText`: Text
- `WarningCountText`: Text

---

#### ConsoleUpdatedEventHandler

**Line:** 1445091

**Inherits:** MulticastDelegate

---

#### ConstantBuffer

**Line:** 807275

**Fields:**

- `m_GlobalBindings`: HashSet<int>
- `m_GPUConstantBuffer`: ComputeBuffer

---

#### ConstantBufferBase

**Line:** 807263

---

#### ConstantExpression

**Line:** 1286409

**Inherits:** Expression

---

#### Constraint

**Line:** 1083375

**Fields:**

- `_schemaName`: string
- `_inCollection`: bool
- `_dataSet`: DataSet

---

#### ConstraintCollection

**Line:** 1083467

**Inherits:** InternalDataCollectionBase

**Fields:**

- `_defaultNameIndex`: int
- `_onCollectionChanged`: CollectionChangeEventHandler
- `_fLoadForeignKeyConstraintsOnly`: bool

---

#### ConstraintException

**Line:** 1080763

**Inherits:** DataException

---

#### ConstructionCall

**Line:** 223859

**Inherits:** MethodCall

**Fields:**

- `_activator`: IActivator
- `_contextProperties`: IList
- `_activationType`: Type
- `_activationTypeName`: string
- `_isContextOk`: bool
- `_sourceProxy`: RemotingProxy

---

#### ConstructionResponse

**Line:** 223959

**Inherits:** MethodResponse

---

#### ConstructorBuilder

**Line:** 269276

**Inherits:** ConstructorInfo

---

#### ConstructorInfo

**Line:** 265202

**Inherits:** MethodBase

---

#### ContainerPropertyBag

**Line:** 1462316

---

#### ContentCatalogData

**Line:** 1456684

**Fields:**

- `LocalHash`: string
- `m_InstanceProviderData`: ObjectInitializationData
- `m_SceneProviderData`: ObjectInitializationData
- `m_Entries`: IList<ContentCatalogDataEntry>

---

#### ContentCatalogDataEntry

**Line:** 1456226

---

#### ContentCatalogProvider

**Line:** 1456206

**Inherits:** ResourceProviderBase

**Fields:**

- `DisableCatalogUpdateOnStart`: bool
- `IsLocalCatalogInBundle`: bool

---

#### ContentDispositionHeaderValue

**Line:** 1489319

**Inherits:** ICloneable

**Fields:**

- `dispositionType`: string
- `parameters`: List<NameValueHeaderValue>

---

#### ContentFitTMPText

**Line:** 736515

**Inherits:** MonoBehaviour

**Fields:**

- `rectTransform`: RectTransform
- `CopySource`: TMP_Text
- `Padding`: Vector2
- `FitWidth`: bool
- `FitHeight`: bool

---

#### ContentFitText

**Line:** 1506253

**Inherits:** UIBehaviour

**Fields:**

- `CopySource`: SRText
- `Padding`: Vector2

---

#### ContentRangeHeaderValue

**Line:** 1489356

**Inherits:** ICloneable

**Fields:**

- `unit`: string

---

#### ContentSizeFitter

**Line:** 1354572

**Inherits:** UIBehaviour

**Fields:**

- `m_Rect`: RectTransform
- `m_Tracker`: DrivenRectTransformTracker

---

#### Context

**Line:** 1546750

**Fields:**

- `OnEntityCreated`: ContextEntityChanged
- `OnEntityWillBeDestroyed`: ContextEntityChanged
- `OnEntityDestroyed`: ContextEntityChanged
- `OnGroupCreated`: ContextGroupChanged
- `_creationIndex`: int
- `_lastEntityId`: int

---

#### ContextAttribute

**Line:** 1597348

**Inherits:** Attribute

---

#### ContextBoundObject

**Line:** 172813

**Inherits:** MarshalByRefObject

---

#### ContextCallback

**Line:** 180415

**Inherits:** MulticastDelegate

---

#### ContextClickEvent

**Line:** 636591

**Inherits:** MouseEventBase

---

#### ContextContainer

**Line:** 807790

**Inherits:** IDisposable

**Fields:**

- `m_ActiveItemIndices`: List<uint>

---

#### ContextDoesNotContainEntityException

**Line:** 1547343

**Inherits:** EntitasException

---

#### ContextEntityChanged

**Line:** 1547912

**Inherits:** MulticastDelegate

---

#### ContextEntityIndexDoesAlreadyExistException

**Line:** 1547352

**Inherits:** EntitasException

---

#### ContextEntityIndexDoesNotExistException

**Line:** 1547361

**Inherits:** EntitasException

---

#### ContextGroupChanged

**Line:** 1547930

**Inherits:** MulticastDelegate

---

#### ContextInfo

**Line:** 1547889

---

#### ContextInfoException

**Line:** 1547413

**Inherits:** EntitasException

---

#### ContextItem

**Line:** 807850

---

#### ContextMenu

**Line:** 881601

**Inherits:** Attribute

---

#### ContextObserver

**Line:** 1590599

**Fields:**

- `_toStringBuilder`: StringBuilder

---

#### ContextObserverBehaviour

**Line:** 1590642

**Inherits:** MonoBehaviour

**Fields:**

- `_contextObserver`: ContextObserver

---

#### ContextStaticAttribute

**Line:** 172825

**Inherits:** Attribute

---

#### ContextStillHasRetainedEntitiesException

**Line:** 1547395

**Inherits:** EntitasException

---

#### Contexts

**Line:** 687805

**Inherits:** IContexts

---

#### ContextualMenuManager

**Line:** 612644

---

#### ContextualMenuManipulator

**Line:** 612681

**Inherits:** PointerManipulator

**Fields:**

- `m_MenuBuilder`: Action<ContextualMenuPopulateEvent>

---

#### ContextualMenuPopulateEvent

**Line:** 636944

**Inherits:** MouseEventBase

**Fields:**

- `m_ContextualMenuManager`: ContextualMenuManager

---

#### ContinuousEvent

**Line:** 1585324

---

#### ControllerColliderHit

**Line:** 1576763

---

#### ConversionValuesParams

**Line:** 1571173

**Fields:**

- `_value`: int
- `_coarse`: int
- `_lock`: bool

---

#### ConvertBinder

**Line:** 1299995

**Inherits:** DynamicMetaObjectBinder

---

#### ConvertChildProxiesToUiEntities

**Line:** 697239

**Inherits:** UiUnityView

**Fields:**

- `ChildProxies`: List<UiUnityViewProxy>

---

#### ConvertToEntityBehaviour

**Line:** 697101

**Inherits:** MonoBehaviour

---

#### ConvertToGameEntity

**Line:** 697120

**Inherits:** ConvertToEntityBehaviour

---

#### ConvertToUiEntity

**Line:** 697263

**Inherits:** ConvertToEntityBehaviour

---

#### Converter

**Line:** 17336

---

#### ConverterGroup

**Line:** 607490

---

#### Cookie

**Line:** 793161

**Fields:**

- `m_comment`: string
- `m_commentUri`: Uri
- `m_cookieVariant`: CookieVariant
- `m_discard`: bool
- `m_domain`: string
- `m_domain_implicit`: bool
- `m_expires`: DateTime
- `m_name`: string
- `m_path`: string
- `m_path_implicit`: bool
- `m_port`: string
- `m_port_implicit`: bool
- `m_secure`: bool
- `m_httpOnly`: bool
- `m_timeStamp`: DateTime
- `m_value`: string
- `m_version`: int
- `m_domainKey`: string

---

#### CookieCollection

**Line:** 793536

**Inherits:** ICollection

**Fields:**

- `m_list`: ArrayList
- `m_TimeStamp`: DateTime
- `m_has_other_versions`: bool
- `m_IsReadOnly`: bool

---

#### CookieContainer

**Line:** 793623

**Fields:**

- `m_domainTable`: Hashtable
- `m_maxCookieSize`: int
- `m_maxCookies`: int
- `m_maxCookiesPerDomain`: int
- `m_count`: int
- `m_fqdnMyDomain`: string

---

#### CookieException

**Line:** 793738

**Inherits:** FormatException

---

#### CooldownComponent

**Line:** 696219

**Inherits:** IComponent

**Fields:**

- `Value`: double

---

#### CooldownTimerStateComponent

**Line:** 696284

**Inherits:** IComponent

**Fields:**

- `Value`: CooldownTimerState

---

#### CooldownTimerStateEventSystem

**Line:** 701747

**Inherits:** ReactiveSystem

---

#### CooldownTimerStateListenerComponent

**Line:** 699531

**Inherits:** IComponent

**Fields:**

- `value`: List<ICooldownTimerStateListener>

---

#### CoordinatesInfo

**Line:** 538815

**Inherits:** IEquatable

---

#### CopyColorPass

**Line:** 919135

**Inherits:** ScriptableRenderPass

**Fields:**

- `m_SampleOffsetShaderHandle`: int
- `m_SamplingMaterial`: Material
- `m_DownsamplingMethod`: Downsampling
- `m_CopyColorMaterial`: Material

---

#### CopyDepthPass

**Line:** 919258

**Inherits:** ScriptableRenderPass

**Fields:**

- `m_CopyDepthMaterial`: Material

---

#### CopyLayoutElement

**Line:** 1506326

**Inherits:** UIBehaviour

**Fields:**

- `CopyMinHeight`: bool
- `CopyMinWidth`: bool
- `CopyPreferredHeight`: bool
- `CopyPreferredWidth`: bool
- `CopySource`: RectTransform
- `PaddingMinHeight`: float
- `PaddingMinWidth`: float
- `PaddingPreferredHeight`: float
- `PaddingPreferredWidth`: float

---

#### CopyPasteRequest

**Line:** 1389844

**Inherits:** IDirectResponseSchema

---

#### CopyPreferredSize

**Line:** 1506385

**Inherits:** LayoutElement

**Fields:**

- `CopySource`: RectTransform
- `PaddingHeight`: float
- `PaddingWidth`: float

---

#### CopyRectSize

**Line:** 714239

**Inherits:** MonoBehaviour

**Fields:**

- `_sourceRect`: RectTransform

---

#### CopySheetToAnotherSpreadsheetRequest

**Line:** 1389916

**Inherits:** IDirectResponseSchema

---

#### CopySizeIntoLayoutElement

**Line:** 1506416

**Inherits:** LayoutElement

**Fields:**

- `CopySource`: RectTransform
- `PaddingHeight`: float
- `PaddingWidth`: float
- `SetPreferredSize`: bool
- `SetMinimumSize`: bool

---

#### CopyableEvent

**Line:** 500561

**Fields:**

- `_invoker`: Action<T1, T2, T3, T4, T5, T6, T7>

---

#### CorePackageRegistry

**Line:** 1512931

---

#### CoreRPHelpURLAttribute

**Line:** 816312

**Inherits:** HelpURLAttribute

---

#### CoreRegistry

**Line:** 1513030

---

#### Coroutine

**Line:** 882583

**Inherits:** YieldInstruction

---

#### CorrelationManager

**Line:** 777408

---

#### Counter

**Line:** 1421956

---

#### CountryComplianceLibrary

**Line:** 1059116

**Inherits:** IGameConfigData

---

#### CrashlyticsInternalPINVOKE

**Line:** 1567630

---

#### CreateAssetMenuAttribute

**Line:** 881562

**Inherits:** Attribute

---

#### CreateDeveloperMetadataRequest

**Line:** 1389952

**Inherits:** IDirectResponseSchema

---

#### CreateDeveloperMetadataResponse

**Line:** 1389988

**Inherits:** IDirectResponseSchema

---

#### CreateHttpClientArgs

**Line:** 1497525

---

#### CreateInstanceBinder

**Line:** 1300021

**Inherits:** DynamicMetaObjectBinder

---

#### CreateInstanceDelegate

**Line:** 531543

---

#### CreateInstanceWithParametersDelegate

**Line:** 531593

---

#### CreateOrUpdateUserRequest

**Line:** 1526349

**Inherits:** IEquatable

---

#### CreatePropertyAttribute

**Line:** 1457998

**Inherits:** RequiredMemberAttribute

---

#### CreateSteppingStonesRunResponse

**Line:** 1079474

**Inherits:** PlayerSynchronizedServerActionCore

---

#### CredentialCache

**Line:** 791418

---

#### CredentialsStore

**Line:** 1305350

**Fields:**

- `_preloadTask`: Task<CredentialsStore.ICredentialsData>

---

#### CreditCardAttribute

**Line:** 1508792

**Inherits:** DataTypeAttribute

---

#### CriticalFinalizerObject

**Line:** 230030

---

#### CrossContextDelegate

**Line:** 222568

**Inherits:** MulticastDelegate

---

#### CrossPlatformValidator

**Line:** 1545011

**Fields:**

- `google`: GooglePlayValidator
- `apple`: AppleValidator
- `googleBundleId`: string
- `appleBundleId`: string

---

#### CryptoConfig

**Line:** 219623

---

#### CryptoConvert

**Line:** 1449302

---

#### CryptoException

**Line:** 1518295

**Inherits:** Exception

---

#### CryptoStream

**Line:** 217536

**Inherits:** Stream

**Fields:**

- `_inputBufferIndex`: int
- `_inputBlockSize`: int
- `_outputBufferIndex`: int
- `_outputBlockSize`: int
- `_canRead`: bool
- `_canWrite`: bool
- `_finalBlockTransformed`: bool
- `_lazyAsyncActiveSemaphore`: SemaphoreSlim

---

#### CryptographicException

**Line:** 218004

**Inherits:** SystemException

---

#### CryptographicUnexpectedOperationException

**Line:** 218027

**Inherits:** CryptographicException

---

#### CspParameters

**Line:** 218062

**Fields:**

- `ProviderType`: int
- `ProviderName`: string
- `KeyContainerName`: string
- `KeyNumber`: int
- `m_flags`: int

---

#### CsvStream

**Line:** 526920

**Inherits:** IDisposable

**Fields:**

- `_reader`: StreamReader
- `_separator`: char

---

#### Cubemap

**Line:** 876936

**Inherits:** Texture

---

#### CubemapArray

**Line:** 877238

**Inherits:** Texture

---

#### CubemapParameter

**Line:** 827570

**Inherits:** VolumeParameter

---

#### CubicBezierPath

**Line:** 722931

**Inherits:** IPath

---

#### CullingGroup

**Line:** 871355

**Inherits:** IDisposable

---

#### CultureInfo

**Line:** 274671

**Inherits:** ICloneable

**Fields:**

- `m_isReadOnly`: bool
- `cultureID`: int
- `parent_lcid`: int
- `datetime_index`: int
- `number_index`: int
- `default_calendar_type`: int
- `m_useUserOverride`: bool
- `textInfo`: TextInfo
- `englishname`: string
- `nativename`: string
- `iso3lang`: string
- `iso2lang`: string
- `win3lang`: string
- `territory`: string
- `compareInfo`: CompareInfo
- `m_dataItem`: int
- `calendar`: Calendar
- `parent_culture`: CultureInfo
- `constructed`: bool

---

#### CultureInfoConverter

**Line:** 781337

**Inherits:** TypeConverter

---

#### CultureNotFoundException

**Line:** 271380

**Inherits:** ArgumentException

**Fields:**

- `_invalidCultureName`: string
- `_invalidCultureId`: Nullable<int>

---

#### CurrentPipelineHelpURLAttribute

**Line:** 816326

**Inherits:** HelpURLAttribute

---

#### Cursor

**Line:** 878209

---

#### CustomAttributeData

**Line:** 268010

**Fields:**

- `ctorInfo`: ConstructorInfo
- `ctorArgs`: IList<CustomAttributeTypedArgument>
- `namedArgs`: IList<CustomAttributeNamedArgument>

---

#### CustomAttributeFormatException

**Line:** 265245

**Inherits:** FormatException

---

#### CustomBinding

**Line:** 608650

**Inherits:** Binding

---

#### CustomComparerIdParser

**Line:** 1079291

**Inherits:** ConfigParserProvider

---

#### CustomComponentNameAttribute

**Line:** 1597375

**Inherits:** Attribute

---

#### CustomConstantAttribute

**Line:** 234116

**Inherits:** Attribute

---

#### CustomConstructorResolver

**Line:** 727855

**Inherits:** DefaultContractResolver

---

#### CustomCreationConverter

**Line:** 1048292

---

#### CustomEntityIndexAttribute

**Line:** 1597388

**Inherits:** Attribute

---

#### CustomMessageData

**Line:** 1057958

---

#### CustomPluralRuleProvider

**Line:** 1322068

**Inherits:** IFormatProvider

---

#### CustomRenderTexture

**Line:** 877722

**Inherits:** RenderTexture

---

#### CustomSampler

**Line:** 886592

**Inherits:** Sampler

---

#### CustomStyleResolvedEvent

**Line:** 638977

**Inherits:** EventBase

---

#### CustomTrackedObjectAttribute

**Line:** 1327726

**Inherits:** Attribute

---

#### CustomTypeDescriptor

**Line:** 781380

**Inherits:** ICustomTypeDescriptor

---

#### CustomValidationAttribute

**Line:** 1508829

**Inherits:** ValidationAttribute

**Fields:**

- `_isSingleArgumentMethod`: bool
- `_lastMessage`: string
- `_methodInfo`: MethodInfo
- `_firstParameterType`: Type
- `_typeId`: Tuple<string, Type>

---

#### CustomYieldInstruction

**Line:** 882617

**Inherits:** IEnumerator

---

#### CutPasteRequest

**Line:** 1390024

**Inherits:** IDirectResponseSchema

---

#### CutoutMaskUI

**Line:** 714259

**Inherits:** Image

---

#### DBNull

**Line:** 22014

**Inherits:** ISerializable

---

#### DES

**Line:** 218097

**Inherits:** SymmetricAlgorithm

---

#### DESCryptoServiceProvider

**Line:** 218138

**Inherits:** DES

---

#### DOGetter

**Line:** 1430411

---

#### DOSetter

**Line:** 1430617

---

#### DOTween

**Line:** 1425067

---

#### DOTweenCYInstruction

**Line:** 1551424

---

#### DOTweenComponent

**Line:** 1431118

**Inherits:** MonoBehaviour

**Fields:**

- `inspectorUpdater`: int
- `_unscaledTime`: float
- `_unscaledDeltaTime`: float
- `_paused`: bool
- `_pausedTime`: float
- `_isQuitting`: bool
- `_duplicateToDestroy`: bool

---

#### DOTweenSettings

**Line:** 1431235

**Inherits:** ScriptableObject

**Fields:**

- `useSafeMode`: bool
- `timeScale`: float
- `useSmoothDeltaTime`: bool
- `maxSmoothUnscaledTime`: float
- `rewindCallbackMode`: RewindCallbackMode
- `showUnityEditorReport`: bool
- `logBehaviour`: LogBehaviour
- `drawGizmos`: bool
- `defaultRecyclable`: bool
- `defaultAutoPlay`: AutoPlay
- `defaultUpdateType`: UpdateType
- `defaultTimeScaleIndependent`: bool
- `defaultEaseType`: Ease
- `defaultEaseOvershootOrAmplitude`: float
- `defaultEasePeriod`: float
- `defaultAutoKill`: bool
- `defaultLoopType`: LoopType
- `debugMode`: bool
- `debugStoreTargetId`: bool
- `showPreviewPanel`: bool
- ... (2 more fields)

---

#### DSA

**Line:** 218176

**Inherits:** AsymmetricAlgorithm

---

#### DSACryptoServiceProvider

**Line:** 219707

**Inherits:** DSA

**Fields:**

- `store`: KeyPairPersistence
- `persistKey`: bool
- `persisted`: bool
- `privateKeyExportable`: bool
- `m_disposed`: bool
- `dsa`: DSAManaged

---

#### DSAManaged

**Line:** 2471

---

#### DSASignatureDeformatter

**Line:** 218204

**Inherits:** AsymmetricSignatureDeformatter

**Fields:**

- `_dsaKey`: DSA
- `_oid`: string

---

#### DSASignatureFormatter

**Line:** 218230

**Inherits:** AsymmetricSignatureFormatter

**Fields:**

- `_oid`: string

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

#### DailyDealModelComponent

**Line:** 729994

**Inherits:** IComponent

**Fields:**

- `Value`: DailyDealModel

---

#### DailyDealPurchaseContent

**Line:** 1078856

**Inherits:** DynamicPurchaseContent

---

#### DailyDealViewCreateSystem

**Line:** 730052

**Inherits:** ShopViewEntryCreateSystem

---

#### DailyScoreData

**Line:** 1066038

---

#### DataBinding

**Line:** 608663

**Inherits:** Binding

**Fields:**

- `m_BindingMode`: BindingMode
- `m_SourceToUiConverters`: ConverterGroup
- `m_UiToSourceConverters`: ConverterGroup

---

#### DataBoundControl

**Line:** 1444291

**Inherits:** OptionsControlBase

**Fields:**

- `_hasStarted`: bool
- `_isReadOnly`: bool
- `_prevValue`: object
- `_prop`: PropertyReference

---

#### DataColumn

**Line:** 1080133

**Inherits:** MarshalByValueComponent

**Fields:**

- `_allowNull`: bool
- `_caption`: string
- `_columnName`: string
- `_dataType`: Type
- `_storageType`: StorageType
- `_dateTimeMode`: DataSetDateTime
- `_expression`: DataExpression
- `_maxLength`: int
- `_ordinal`: int
- `_readOnly`: bool
- `_unique`: bool
- `_isSqlType`: bool
- `_implementsINullable`: bool
- `_implementsIChangeTracking`: bool
- `_implementsIRevertibleChangeTracking`: bool
- `_implementsIXMLSerializable`: bool
- `_defaultValueIsNull`: bool
- `_storage`: DataStorage
- `_autoInc`: AutoIncrementValue
- `_columnPrefix`: string
- ... (1 more fields)

---

#### DataColumnChangeEventArgs

**Line:** 1083672

**Inherits:** EventArgs

**Fields:**

- `_column`: DataColumn

---

#### DataColumnChangeEventHandler

**Line:** 1083705

**Inherits:** MulticastDelegate

---

#### DataColumnCollection

**Line:** 1083719

**Inherits:** InternalDataCollectionBase

**Fields:**

- `_defaultNameIndex`: int
- `_fInClear`: bool
- `_nColumnsImplementingIChangeTracking`: int
- `_nColumnsImplementingIRevertibleChangeTracking`: int
- `CollectionChanged`: CollectionChangeEventHandler
- `CollectionChanging`: CollectionChangeEventHandler
- `ColumnPropertyChanged`: CollectionChangeEventHandler

---

#### DataContractAttribute

**Line:** 1596453

**Inherits:** Attribute

**Fields:**

- `isReference`: bool

---

#### DataException

**Line:** 1080744

**Inherits:** SystemException

---

#### DataExecutionStatus

**Line:** 1390084

**Inherits:** IDirectResponseSchema

**Fields:**

- `_lastRefreshTimeRaw`: string
- `_lastRefreshTime`: object

---

#### DataFilter

**Line:** 1390171

**Inherits:** IDirectResponseSchema

---

#### DataFilterValueRange

**Line:** 1390231

**Inherits:** IDirectResponseSchema

---

#### DataLabel

**Line:** 1390291

**Inherits:** IDirectResponseSchema

---

#### DataLengthException

**Line:** 1518323

**Inherits:** CryptoException

---

#### DataProcessingServices

**Line:** 738670

---

#### DataRelation

**Line:** 1084056

**Fields:**

- `_dataSet`: DataSet
- `_childKey`: DataKey
- `_parentKey`: DataKey
- `_parentKeyConstraint`: UniqueConstraint
- `_childKeyConstraint`: ForeignKeyConstraint
- `_checkMultipleNested`: bool
- `PropertyChanging`: PropertyChangedEventHandler

---

#### DataRelationCollection

**Line:** 1084341

**Inherits:** InternalDataCollectionBase

**Fields:**

- `_inTransition`: DataRelation
- `_defaultNameIndex`: int
- `_onCollectionChangedDelegate`: CollectionChangeEventHandler
- `_onCollectionChangingDelegate`: CollectionChangeEventHandler

---

#### DataRetention

**Line:** 1564769

**Fields:**

- `purposes`: RetentionPeriod
- `specialPurposes`: RetentionPeriod
- `_stdRetention`: string

---

#### DataRow

**Line:** 1084477

**Fields:**

- `_lastChangedColumn`: DataColumn
- `_countColumnChange`: int
- `_error`: DataError
- `_rbTreeNodeId`: int

---

#### DataRowBuilder

**Line:** 1084716

---

#### DataRowChangeEventArgs

**Line:** 1084745

**Inherits:** EventArgs

---

#### DataRowChangeEventHandler

**Line:** 1084760

**Inherits:** MulticastDelegate

---

#### DataRowCollection

**Line:** 1084788

**Inherits:** InternalDataCollectionBase

---

#### DataRowView

**Line:** 1084894

**Inherits:** ICustomTypeDescriptor

**Fields:**

- `_delayBeginEdit`: bool
- `PropertyChanged`: PropertyChangedEventHandler

---

#### DataSet

**Line:** 1081693

**Inherits:** MarshalByValueComponent

**Fields:**

- `_defaultViewManager`: DataViewManager
- `_dataSetName`: string
- `_datasetPrefix`: string
- `_enforceConstraints`: bool
- `_caseSensitive`: bool
- `_culture`: CultureInfo
- `_cultureUserSet`: bool
- `_remotingFormat`: SerializationFormat
- `_defaultViewManagerLock`: object
- `PropertyChanging`: PropertyChangedEventHandler
- `MergeFailed`: MergeFailedEventHandler
- `DataRowCreated`: DataRowCreatedEventHandler
- `ClearFunctionCalled`: DataSetClearEventhandler

---

#### DataSetConverter

**Line:** 1048351

**Inherits:** JsonConverter

---

#### DataSource

**Line:** 1390363

**Inherits:** IDirectResponseSchema

---

#### DataSourceChartProperties

**Line:** 1390435

**Inherits:** IDirectResponseSchema

---

#### DataSourceColumn

**Line:** 1390483

**Inherits:** IDirectResponseSchema

---

#### DataSourceColumnReference

**Line:** 1390531

**Inherits:** IDirectResponseSchema

---

#### DataSourceFormula

**Line:** 1390567

**Inherits:** IDirectResponseSchema

---

#### DataSourceObjectReference

**Line:** 1390615

**Inherits:** IDirectResponseSchema

---

#### DataSourceObjectReferences

**Line:** 1390699

**Inherits:** IDirectResponseSchema

---

#### DataSourceParameter

**Line:** 1390735

**Inherits:** IDirectResponseSchema

---

#### DataSourceRefreshDailySchedule

**Line:** 1390795

**Inherits:** IDirectResponseSchema

---

#### DataSourceRefreshMonthlySchedule

**Line:** 1390831

**Inherits:** IDirectResponseSchema

---

#### DataSourceRefreshSchedule

**Line:** 1390879

**Inherits:** IDirectResponseSchema

---

#### DataSourceRefreshWeeklySchedule

**Line:** 1390975

**Inherits:** IDirectResponseSchema

---

#### DataSourceSheetDimensionRange

**Line:** 1391023

**Inherits:** IDirectResponseSchema

---

#### DataSourceSheetProperties

**Line:** 1391071

**Inherits:** IDirectResponseSchema

---

#### DataSourceSpec

**Line:** 1391131

**Inherits:** IDirectResponseSchema

---

#### DataSourceTable

**Line:** 1391191

**Inherits:** IDirectResponseSchema

---

#### DataTable

**Line:** 1082048

**Inherits:** MarshalByValueComponent

**Fields:**

- `_dataSet`: DataSet
- `_defaultView`: DataView
- `_elementColumnCount`: int
- `_shadowIndexes`: List<Index>
- `_shadowCount`: int
- `_tableName`: string
- `_tablePrefix`: string
- `_culture`: CultureInfo
- `_cultureUserSet`: bool
- `_compareInfo`: CompareInfo
- `_compareFlags`: CompareOptions
- `_formatProvider`: IFormatProvider
- `_hashCodeProvider`: StringComparer
- `_caseSensitive`: bool
- `_caseSensitiveUserSet`: bool
- `_typeName`: object
- `_loadIndex`: Index
- `_loadIndexwithOriginalAdded`: Index
- `_loadIndexwithCurrentDeleted`: Index
- `_suspendIndexEvents`: int
- ... (18 more fields)

---

#### DataTableClearEventArgs

**Line:** 1085026

**Inherits:** EventArgs

---

#### DataTableClearEventHandler

**Line:** 1085039

**Inherits:** MulticastDelegate

---

#### DataTableCollection

**Line:** 1085054

**Inherits:** InternalDataCollectionBase

**Fields:**

- `_defaultNameIndex`: int
- `_onCollectionChangedDelegate`: CollectionChangeEventHandler
- `_onCollectionChangingDelegate`: CollectionChangeEventHandler

---

#### DataTableConverter

**Line:** 1048371

**Inherits:** JsonConverter

---

#### DataTableNewRowEventArgs

**Line:** 1085170

**Inherits:** EventArgs

---

#### DataTableNewRowEventHandler

**Line:** 1085183

**Inherits:** MulticastDelegate

---

#### DataTypeAttribute

**Line:** 1508923

**Inherits:** ValidationAttribute

---

#### DataUtility

**Line:** 899764

---

#### DataValidationRule

**Line:** 1391299

**Inherits:** IDirectResponseSchema

---

#### DataView

**Line:** 1085275

**Inherits:** MarshalByValueComponent

**Fields:**

- `_dataViewManager`: DataViewManager
- `_table`: DataTable
- `_locked`: bool
- `_index`: Index
- `_findIndexes`: Dictionary<string, Index>
- `_sort`: string
- `_comparison`: Comparison<DataRow>
- `_rowFilter`: IFilter
- `_recordStates`: DataViewRowState
- `_shouldOpen`: bool
- `_open`: bool
- `_allowNew`: bool
- `_allowEdit`: bool
- `_allowDelete`: bool
- `_applyDefaultSort`: bool
- `_addNewMoved`: ListChangedEventArgs
- `_onListChanged`: ListChangedEventHandler
- `_delayedSort`: string
- `_delayedRecordStates`: DataViewRowState
- `_fInitInProgress`: bool
- ... (3 more fields)

---

#### DataViewManager

**Line:** 1085654

**Inherits:** MarshalByValueComponent

**Fields:**

- `_dataViewSettingsCollection`: DataViewSettingCollection

---

#### DataViewSetting

**Line:** 1085704

**Fields:**

- `_dataViewManager`: DataViewManager
- `_table`: DataTable
- `_sort`: string
- `_rowFilter`: string
- `_rowStateFilter`: DataViewRowState
- `_applyDefaultSort`: bool

---

#### DataViewSettingCollection

**Line:** 1085746

---

#### DatabaseGeneratedAttribute

**Line:** 1510875

**Inherits:** Attribute

---

#### DateInterval

**Line:** 1143267

**Inherits:** IEquatable

---

#### DateTimeConstantAttribute

**Line:** 234133

**Inherits:** CustomConstantAttribute

**Fields:**

- `_date`: DateTime

---

#### DateTimeConverter

**Line:** 781431

**Inherits:** TypeConverter

---

#### DateTimeConverterBase

**Line:** 1048395

**Inherits:** JsonConverter

---

#### DateTimeFormatInfo

**Line:** 271484

**Inherits:** IFormatProvider

**Fields:**

- `_cultureData`: CultureData
- `_name`: string
- `_langName`: string
- `_compareInfo`: CompareInfo
- `_cultureInfo`: CultureInfo
- `amDesignator`: string
- `pmDesignator`: string
- `dateSeparator`: string
- `generalShortTimePattern`: string
- `generalLongTimePattern`: string
- `timeSeparator`: string
- `monthDayPattern`: string
- `dateTimeOffsetPattern`: string
- `calendar`: Calendar
- `firstDayOfWeek`: int
- `calendarWeekRule`: int
- `fullDateTimePattern`: string
- `longDatePattern`: string
- `shortDatePattern`: string
- `yearMonthPattern`: string
- ... (5 more fields)

---

#### DateTimeOffsetConverter

**Line:** 783533

**Inherits:** TypeConverter

---

#### DateTimeRule

**Line:** 1391371

**Inherits:** IDirectResponseSchema

---

#### DateTimeZone

**Line:** 1143406

**Inherits:** IZoneIntervalMap

---

#### DateTimeZoneCache

**Line:** 1148553

**Inherits:** IDateTimeZoneProvider

---

#### DateTimeZoneNotFoundException

**Line:** 1148597

**Inherits:** TimeZoneNotFoundException

---

#### DayActionEntryUiView

**Line:** 719573

**Inherits:** MonoBehaviour

**Fields:**

- `ActionText`: TMP_Text
- `PointsText`: TMP_Text

---

#### DayResultsDetailsPopupUiView

**Line:** 719589

**Inherits:** MonoBehaviour

**Fields:**

- `DayText`: TMP_Text
- `ResultsText`: TMP_Text
- `ActionsParent`: RectTransform
- `ActionEntryPrefab`: DayActionEntryUiView
- `_warManager`: GuildWarManager

---

#### DayResultsEntryUiView

**Line:** 719624

**Inherits:** MonoBehaviour

**Fields:**

- `GuildTagText`: TMP_Text
- `PointsText`: TMP_Text
- `DayText`: TMP_Text
- `Button`: UnityButton
- `ProfileObject`: GameObject
- `ProfileUiView`: PlayerMiniProfileUiView
- `_dayIdx`: int
- `_model`: GuildWarDayModel
- `_warManager`: GuildWarManager
- `_guildManager`: GuildManager

---

#### DeallocateOnJobCompletionAttribute

**Line:** 837999

**Inherits:** Attribute

---

#### DeathEffectComponent

**Line:** 710586

**Inherits:** IComponent

---

#### Debug

**Line:** 871540

---

#### DebugCameraServiceImpl

**Line:** 1445685

**Inherits:** IDebugCameraService

**Fields:**

- `_debugCamera`: Camera

---

#### DebugDisplayGPUResidentDrawer

**Line:** 1377045

**Inherits:** IDebugDisplaySettingsData

**Fields:**

- `occluderDebugViewEnable`: bool

---

#### DebugDisplaySettings

**Line:** 811412

---

#### DebugDisplaySettingsHDROutput

**Line:** 811617

---

#### DebugDisplaySettingsLighting

**Line:** 901687

**Inherits:** IDebugDisplaySettingsData

---

#### DebugDisplaySettingsMaterial

**Line:** 902224

**Inherits:** IDebugDisplaySettingsData

**Fields:**

- `m_AlbedoHueTolerance`: float
- `m_AlbedoSaturationTolerance`: float

---

#### DebugDisplaySettingsPanel

**Line:** 811669

---

#### DebugDisplaySettingsRendering

**Line:** 903106

**Inherits:** IDebugDisplaySettingsData

**Fields:**

- `m_WireframeMode`: DebugWireframeMode
- `m_Overdraw`: bool
- `m_OverdrawMode`: DebugOverdrawMode

---

#### DebugDisplaySettingsStats

**Line:** 811760

---

#### DebugDisplaySettingsUI

**Line:** 811836

**Inherits:** IDebugData

**Fields:**

- `m_DisposablePanels`: IEnumerable<IDebugDisplaySettingsPanelDisposable>
- `m_Settings`: IDebugDisplaySettings

---

#### DebugDisplaySettingsVolume

**Line:** 812105

**Inherits:** IDebugDisplaySettingsData

---

#### DebugDisplayStats

**Line:** 812311

**Fields:**

- `m_TimeSinceLastAvgValue`: float
- `m_AccumulatedFrames`: int
- `m_HiddenProfileIds`: HashSet<TProfileId>
- `averageProfilerTimingsOverASecond`: bool
- `hideEmptyScopes`: bool

---

#### DebugFrameTiming

**Line:** 812459

**Fields:**

- `m_Sample`: FrameTimeSample

---

#### DebugInfoExpression

**Line:** 1286461

**Inherits:** Expression

---

#### DebugLocalNotification

**Line:** 694058

**Inherits:** ILocalNotification

---

#### DebugManager

**Line:** 812704

**Fields:**

- `m_ReadOnlyPanels`: ReadOnlyCollection<DebugUI.Panel>
- `onDisplayRuntimeUIChanged`: Action<bool>
- `onSetDirty`: Action
- `resetData`: Action
- `refreshEditorRequested`: bool
- `m_RequestedPanelIndex`: Nullable<int>
- `m_Root`: GameObject
- `m_RootUICanvas`: DebugUIHandlerCanvas
- `m_PersistentRoot`: GameObject
- `m_RootUIPersistentCanvas`: DebugUIHandlerPersistentCanvas
- `m_EnableRuntimeUI`: bool

---

#### DebugNotificationService

**Line:** 694186

**Inherits:** IPushNotificationService

---

#### DebugOverlay

**Line:** 813028

**Fields:**

- `m_InitialPositionX`: int
- `m_ScreenWidth`: int

---

#### DebugPanelBackgroundBehaviour

**Line:** 1443664

**Inherits:** SRMonoBehaviour

**Fields:**

- `_defaultKey`: string
- `_isTransparent`: bool
- `_styleComponent`: StyleComponent
- `TransparentStyleKey`: string

---

#### DebugPanelRoot

**Line:** 1443016

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `Canvas`: Canvas
- `CanvasGroup`: CanvasGroup
- `TabController`: DebuggerTabController

---

#### DebugPanelServiceImpl

**Line:** 1445704

**Inherits:** ScriptableObject

**Fields:**

- `_debugPanelRootObject`: DebugPanelRoot
- `VisibilityChanged`: Action<IDebugPanelService, bool>
- `_isVisible`: bool
- `_cursorWasVisible`: Nullable<bool>
- `_cursorLockMode`: Nullable<CursorLockMode>

---

#### DebugShapes

**Line:** 813085

**Fields:**

- `m_sphereMesh`: Mesh
- `m_boxMesh`: Mesh
- `m_coneMesh`: Mesh
- `m_pyramidMesh`: Mesh

---

#### DebugSystems

**Line:** 1590693

**Inherits:** Systems

**Fields:**

- `paused`: bool
- `_name`: string
- `_systems`: List<ISystem>
- `_gameObject`: GameObject
- `_systemInfo`: SystemInfo
- `_initializeSystemInfos`: List<SystemInfo>
- `_executeSystemInfos`: List<SystemInfo>
- `_cleanupSystemInfos`: List<SystemInfo>
- `_tearDownSystemInfos`: List<SystemInfo>
- `_stopwatch`: Stopwatch
- `_executeDuration`: double
- `_cleanupDuration`: double

---

#### DebugSystemsBehaviour

**Line:** 1590824

**Inherits:** MonoBehaviour

**Fields:**

- `_systems`: DebugSystems

---

#### DebugTracker

**Line:** 696481

**Inherits:** ITracker

---

#### DebugTriggerImpl

**Line:** 1445760

**Inherits:** SRServiceBase

**Fields:**

- `_position`: PinAlignment
- `_trigger`: TriggerRoot
- `_consoleService`: IConsoleService

---

#### DebugUI

**Line:** 814797

---

#### DebugUIHandlerBitField

**Line:** 833227

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `toggles`: List<DebugUIHandlerIndirectToggle>
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerButton

**Line:** 833270

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text

---

#### DebugUIHandlerCanvas

**Line:** 833350

**Inherits:** MonoBehaviour

**Fields:**

- `m_DebugTreeState`: int
- `m_PrefabsMap`: Dictionary<Type, Transform>
- `panelPrefab`: Transform
- `prefabs`: List<DebugUIPrefabBundle>
- `m_UIPanels`: List<DebugUIHandlerPanel>
- `m_SelectedPanel`: int
- `m_SelectedWidget`: DebugUIHandlerWidget
- `m_CurrentQueryPath`: string

---

#### DebugUIHandlerColor

**Line:** 833420

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `colorImage`: Image
- `fieldR`: DebugUIHandlerIndirectFloatField
- `fieldG`: DebugUIHandlerIndirectFloatField
- `fieldB`: DebugUIHandlerIndirectFloatField
- `fieldA`: DebugUIHandlerIndirectFloatField
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerContainer

**Line:** 833530

**Inherits:** MonoBehaviour

**Fields:**

- `contentHolder`: RectTransform

---

#### DebugUIHandlerEnumField

**Line:** 833555

**Inherits:** DebugUIHandlerField

---

#### DebugUIHandlerEnumHistory

**Line:** 833612

**Inherits:** DebugUIHandlerEnumField

---

#### DebugUIHandlerField

**Line:** 833635

**Fields:**

- `nextButtonText`: Text
- `previousButtonText`: Text
- `nameLabel`: Text
- `valueLabel`: Text

---

#### DebugUIHandlerFloatField

**Line:** 833704

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text

---

#### DebugUIHandlerFoldout

**Line:** 833739

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerGroup

**Line:** 833780

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `header`: Transform
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerHBox

**Line:** 833804

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerIndirectFloatField

**Line:** 833825

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text
- `getter`: Func<float>
- `setter`: Action<float>
- `incStepGetter`: Func<float>
- `incStepMultGetter`: Func<float>
- `decimalsGetter`: Func<float>

---

#### DebugUIHandlerIndirectToggle

**Line:** 833864

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: Toggle
- `checkmarkImage`: Image
- `getter`: Func<int, bool>
- `setter`: Action<int, bool>

---

#### DebugUIHandlerIntField

**Line:** 833899

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text

---

#### DebugUIHandlerMessageBox

**Line:** 833934

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text

---

#### DebugUIHandlerObject

**Line:** 833963

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text

---

#### DebugUIHandlerObjectList

**Line:** 833985

**Inherits:** DebugUIHandlerField

**Fields:**

- `m_Index`: int

---

#### DebugUIHandlerObjectPopupField

**Line:** 834009

**Inherits:** DebugUIHandlerField

**Fields:**

- `m_Index`: int

---

#### DebugUIHandlerPanel

**Line:** 834036

**Inherits:** MonoBehaviour

**Fields:**

- `nameLabel`: Text
- `scrollRect`: ScrollRect
- `viewport`: RectTransform
- `Canvas`: DebugUIHandlerCanvas
- `m_ScrollTransform`: RectTransform
- `m_ContentTransform`: RectTransform
- `m_MaskTransform`: RectTransform
- `m_ScrollTarget`: DebugUIHandlerWidget

---

#### DebugUIHandlerProgressBar

**Line:** 834148

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text
- `progressBarRect`: RectTransform
- `m_Timer`: float

---

#### DebugUIHandlerRenderingLayerField

**Line:** 834182

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `toggles`: List<DebugUIHandlerIndirectToggle>
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerRow

**Line:** 834225

**Inherits:** DebugUIHandlerFoldout

**Fields:**

- `m_Timer`: float

---

#### DebugUIHandlerToggle

**Line:** 834252

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: Toggle
- `checkmarkImage`: Image

---

#### DebugUIHandlerToggleHistory

**Line:** 834324

**Inherits:** DebugUIHandlerToggle

---

#### DebugUIHandlerUIntField

**Line:** 834347

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text

---

#### DebugUIHandlerVBox

**Line:** 834455

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerValue

**Line:** 834382

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text

---

#### DebugUIHandlerValueTuple

**Line:** 834416

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueLabel`: Text
- `m_Timer`: float

---

#### DebugUIHandlerVector2

**Line:** 834476

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `fieldX`: DebugUIHandlerIndirectFloatField
- `fieldY`: DebugUIHandlerIndirectFloatField
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerVector3

**Line:** 834548

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `fieldX`: DebugUIHandlerIndirectFloatField
- `fieldY`: DebugUIHandlerIndirectFloatField
- `fieldZ`: DebugUIHandlerIndirectFloatField
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerVector4

**Line:** 834629

**Inherits:** DebugUIHandlerWidget

**Fields:**

- `nameLabel`: Text
- `valueToggle`: UIFoldout
- `fieldX`: DebugUIHandlerIndirectFloatField
- `fieldY`: DebugUIHandlerIndirectFloatField
- `fieldZ`: DebugUIHandlerIndirectFloatField
- `fieldW`: DebugUIHandlerIndirectFloatField
- `m_Container`: DebugUIHandlerContainer

---

#### DebugUIHandlerWidget

**Line:** 834719

**Inherits:** MonoBehaviour

**Fields:**

- `colorDefault`: Color
- `colorSelected`: Color

---

#### DebugUIPrefabBundle

**Line:** 833296

**Fields:**

- `type`: string
- `prefab`: RectTransform

---

#### DebuggableAttribute

**Line:** 275240

**Inherits:** Attribute

---

#### Debugger

**Line:** 275318

---

#### DebuggerBrowsableAttribute

**Line:** 275265

**Inherits:** Attribute

**Fields:**

- `state`: DebuggerBrowsableState

---

#### DebuggerDisplayAttribute

**Line:** 275293

**Inherits:** Attribute

**Fields:**

- `name`: string
- `value`: string
- `type`: string

---

#### DebuggerHiddenAttribute

**Line:** 275203

**Inherits:** Attribute

---

#### DebuggerNonUserCodeAttribute

**Line:** 275215

**Inherits:** Attribute

---

#### DebuggerStepThroughAttribute

**Line:** 275191

**Inherits:** Attribute

---

#### DebuggerTabController

**Line:** 1442960

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_aboutTabInstance`: SRTab
- `_activeTab`: Nullable<DefaultTabs>
- `_hasStarted`: bool
- `AboutTab`: SRTab
- `TabController`: SRTabController

---

#### DebuggerTypeProxyAttribute

**Line:** 275279

**Inherits:** Attribute

**Fields:**

- `typeName`: string

---

#### DecalProjector

**Line:** 904279

**Inherits:** MonoBehaviour

**Fields:**

- `m_Material`: Material
- `m_DrawDistance`: float
- `m_FadeScale`: float
- `m_StartAngleFade`: float
- `m_EndAngleFade`: float
- `m_UVScale`: Vector2
- `m_UVBias`: Vector2
- `m_DecalLayerMask`: uint
- `m_ScaleMode`: DecalScaleMode
- `m_FadeFactor`: float
- `m_OldMaterial`: Material
- `m_OldDrawDistance`: float
- `m_OldFadeScale`: float
- `m_OldStartAngleFade`: float
- `m_OldEndAngleFade`: float
- `m_OldUVScale`: Vector2
- `m_OldUVBias`: Vector2
- `m_OldScaleMode`: DecalScaleMode
- `m_OldOffset`: Vector3
- `m_OldSize`: Vector3
- ... (1 more fields)

---

#### DecalRendererFeature

**Line:** 912172

**Inherits:** ScriptableRendererFeature

**Fields:**

- `m_Settings`: DecalSettings
- `m_Technique`: DecalTechnique
- `m_DBufferSettings`: DBufferSettings
- `m_ScreenSpaceSettings`: DecalScreenSpaceSettings
- `m_RecreateSystems`: bool
- `m_DecalPreviewPass`: DecalPreviewPass
- `m_DecalEntityManager`: DecalEntityManager
- `m_DecalUpdateCachedSystem`: DecalUpdateCachedSystem
- `m_DecalUpdateCullingGroupSystem`: DecalUpdateCullingGroupSystem
- `m_DecalUpdateCulledSystem`: DecalUpdateCulledSystem
- `m_DecalCreateDrawCallSystem`: DecalCreateDrawCallSystem
- `m_DrawErrorSystem`: DecalDrawErrorSystem
- `m_CopyDepthPass`: DBufferCopyDepthPass
- `m_DBufferRenderPass`: DBufferRenderPass
- `m_ForwardEmissivePass`: DecalForwardEmissivePass
- `m_DecalDrawDBufferSystem`: DecalDrawDBufferSystem
- `m_DecalDrawForwardEmissiveSystem`: DecalDrawFowardEmissiveSystem
- `m_DBufferClearMaterial`: Material
- `m_ScreenSpaceDecalRenderPass`: DecalScreenSpaceRenderPass
- `m_DecalDrawScreenSpaceSystem`: DecalDrawScreenSpaceSystem
- ... (4 more fields)

---

#### DecimalConstantAttribute

**Line:** 234150

**Inherits:** Attribute

**Fields:**

- `_dec`: Decimal

---

#### DecimalConverter

**Line:** 781452

**Inherits:** BaseNumberConverter

---

#### Decoder

**Line:** 214104

---

#### DecoderExceptionFallback

**Line:** 214239

**Inherits:** DecoderFallback

---

#### DecoderExceptionFallbackBuffer

**Line:** 214263

**Inherits:** DecoderFallbackBuffer

---

#### DecoderFallback

**Line:** 214308

---

#### DecoderFallbackBuffer

**Line:** 214338

---

#### DecoderFallbackException

**Line:** 214288

**Inherits:** ArgumentException

**Fields:**

- `_index`: int

---

#### DecoderReplacementFallback

**Line:** 214437

**Inherits:** DecoderFallback

**Fields:**

- `_strDefault`: string

---

#### DecoderReplacementFallbackBuffer

**Line:** 214477

**Inherits:** DecoderFallbackBuffer

**Fields:**

- `_strDefault`: string
- `_fallbackCount`: int
- `_fallbackIndex`: int

---

#### DecompressionSizeLimitExceeded

**Line:** 500142

**Inherits:** Exception

---

#### DeduplicatingGameConfigLibrary

**Line:** 590226

---

#### DefaultAllocationStrategy

**Line:** 1436022

**Inherits:** IAllocationStrategy

---

#### DefaultAllocator

**Line:** 557703

**Inherits:** IMemoryAllocator

---

#### DefaultConnectionContext

**Line:** 1570245

**Inherits:** ConnectionContext

---

#### DefaultContractResolver

**Line:** 1038197

**Inherits:** IContractResolver

---

#### DefaultCoreOptionsProvider

**Line:** 520121

**Inherits:** IMetaplayCoreOptionsProvider

---

#### DefaultDependencyAttribute

**Line:** 253398

**Inherits:** Attribute

**Fields:**

- `loadHint`: LoadHint

---

#### DefaultDllImportSearchPathsAttribute

**Line:** 229272

**Inherits:** Attribute

---

#### DefaultEnvironmentConfigProvider

**Line:** 576754

**Inherits:** IEnvironmentConfigProvider

**Fields:**

- `_activeEnvironmentId`: string
- `_activeEnvironmentIdEditorOverride`: string
- `_activeEnvironmentIdRuntimeOverride`: string
- `_environmentConfigs`: List<EnvironmentConfig>

---

#### DefaultEventAttribute

**Line:** 781487

**Inherits:** Attribute

---

#### DefaultExecutionOrder

**Line:** 881681

**Inherits:** Attribute

**Fields:**

- `m_Order`: int

---

#### DefaultExpression

**Line:** 1286494

**Inherits:** Expression

---

#### DefaultFormatter

**Line:** 1321637

**Inherits:** FormatterBase

---

#### DefaultGameConfigBuild

**Line:** 594576

**Inherits:** GameConfigBuildTemplate

---

#### DefaultGameConfigBuildParameters

**Line:** 594919

**Inherits:** GameConfigBuildParameters

---

#### DefaultGameConfigSourceFetcherProvider

**Line:** 596080

**Inherits:** GameConfigSourceFetcherProvider

---

#### DefaultInAppProductInfo

**Line:** 584354

**Inherits:** InAppProductInfoBase

---

#### DefaultInAppPurchaseEvent

**Line:** 585003

**Inherits:** InAppPurchaseEvent

---

#### DefaultInAppPurchaseHistory

**Line:** 585834

**Inherits:** InAppPurchaseHistory

---

#### DefaultJsonNameTable

**Line:** 1025898

**Inherits:** JsonNameTable

**Fields:**

- `_count`: int
- `_mask`: int

---

#### DefaultJsonTypeInfoResolver

**Line:** 1008532

**Inherits:** IJsonTypeInfoResolver

**Fields:**

- `_mutable`: bool

---

#### DefaultLocalizationsBuildParameters

**Line:** 600148

**Inherits:** LocalizationsBuildParameters

---

#### DefaultMetaOfferGroupInfo

**Line:** 544979

**Inherits:** MetaOfferGroupInfoBase

---

#### DefaultMetaOfferGroupModel

**Line:** 544560

**Inherits:** MetaOfferGroupModelBase

---

#### DefaultMetaOfferGroupSourceConfigItem

**Line:** 544991

**Inherits:** MetaOfferGroupSourceConfigItemBase

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

#### DefaultMetaOfferSourceConfigItem

**Line:** 545344

**Inherits:** MetaOfferSourceConfigItemBase

---

#### DefaultMetaplayConnectionDelegate

**Line:** 1313712

**Inherits:** IMetaplayClientConnectionDelegate

---

#### DefaultMetaplayLocalizationDelegate

**Line:** 1313780

**Inherits:** IMetaplayLocalizationDelegate

---

#### DefaultMultiColumnTreeViewController

**Line:** 610936

**Fields:**

- `m_TreeDataController`: TreeDataController<T>

---

#### DefaultNamingStrategy

**Line:** 1038449

**Inherits:** NamingStrategy

---

#### DefaultOfflineServer

**Line:** 1305715

**Inherits:** IOfflineServer

**Fields:**

- `_log`: LogChannel
- `_transport`: OfflineServerTransport
- `_logicVersion`: int
- `_offlineOptions`: MetaplayOfflineOptions
- `_gameConfig`: ISharedGameConfig
- `_localizationVersions`: MetaDictionary<LanguageId, ContentHash>
- `_playerJournal`: IClientPlayerModelJournal
- `_postponedActions`: Queue<DefaultOfflineServer.JournalPositionedAction>
- `_sessionStartState`: Nullable<DefaultOfflineServer.SessionStartState>
- `_sessionStartFailure`: Exception
- `_nextChannelId`: int
- `_channelEntities`: MetaDictionary<int, DefaultOfflineServer.ChannelEntity>

---

#### DefaultPersistedOfflineState

**Line:** 1305481

---

#### DefaultPlayerClientContext

**Line:** 576913

**Inherits:** IPlayerClientContext

**Fields:**

- `_log`: LogChannel
- `_playerId`: EntityId
- `_sendMessageToServer`: Func<MetaMessage, bool>
- `_checksumGranularity`: ChecksumGranularity
- `_startTime`: MetaTime
- `_currentTime`: MetaTime
- `_timeSinceLastTick`: MetaDuration
- `_actionsLastFlushedAt`: MetaTime
- `_lastFlushedOperationsAt`: JournalPosition
- `_markers`: MetaDictionary<JournalPosition, DefaultPlayerClientContext.ActionMarker>
- `_runningActionId`: int
- `_logicVersion`: int
- `_playerJournal`: ClientPlayerModelJournal
- `_isDisconnected`: bool
- `_operationsBuffer`: List<PlayerFlushActions.Operation>
- `_checksumsBuffer`: List<uint>
- `_actionTypesDebugBuffer`: List<Type>

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

#### DefaultPropertyAttribute

**Line:** 781518

**Inherits:** Attribute

---

#### DefaultProxySection

**Line:** 803134

**Inherits:** ConfigurationSection

---

#### DefaultSerializationBinder

**Line:** 1038493

**Inherits:** SerializationBinder

---

#### DefaultServiceProviderFactory

**Line:** 1499016

**Inherits:** IServiceProviderFactory

---

#### DefaultSource

**Line:** 1321656

**Inherits:** ISource

---

#### DefaultTraceListener

**Line:** 778248

**Inherits:** TraceListener

**Fields:**

- `logFileName`: string

---

#### DefaultTreeViewController

**Line:** 611039

**Fields:**

- `m_TreeDataController`: TreeDataController<T>

---

#### DefaultValueAttribute

**Line:** 890739

**Inherits:** Attribute

**Fields:**

- `DefaultValue`: object

---

#### DeflateStream

**Line:** 789536

**Inherits:** Stream

**Fields:**

- `base_stream`: Stream
- `mode`: CompressionMode
- `leaveOpen`: bool
- `disposed`: bool
- `native`: DeflateStreamNative

---

#### DelayedAttribute

**Line:** 880912

**Inherits:** PropertyAttribute

---

#### Delegate

**Line:** 175113

**Inherits:** ICloneable

**Fields:**

- `method_ptr`: IntPtr
- `invoke_impl`: IntPtr
- `m_target`: object
- `method`: IntPtr
- `delegate_trampoline`: IntPtr
- `extra_arg`: IntPtr
- `method_code`: IntPtr
- `interp_method`: IntPtr
- `interp_invoke_impl`: IntPtr
- `method_info`: MethodInfo
- `original_method_info`: MethodInfo
- `data`: DelegateData
- `method_is_virtual`: bool

---

#### DelegateProperty

**Line:** 1458145

---

#### DelegatingHandler

**Line:** 1488199

**Inherits:** HttpMessageHandler

**Fields:**

- `disposed`: bool
- `handler`: HttpMessageHandler

---

#### DeleteAccountUiView

**Line:** 728913

**Inherits:** MonoBehaviour

**Fields:**

- `DeleteAccountButton`: UnityButton

---

#### DeleteBandingRequest

**Line:** 1391407

**Inherits:** IDirectResponseSchema

---

#### DeleteConditionalFormatRuleRequest

**Line:** 1391443

**Inherits:** IDirectResponseSchema

---

#### DeleteConditionalFormatRuleResponse

**Line:** 1391491

**Inherits:** IDirectResponseSchema

---

#### DeleteDataSourceRequest

**Line:** 1391527

**Inherits:** IDirectResponseSchema

---

#### DeleteDeveloperMetadataRequest

**Line:** 1391563

**Inherits:** IDirectResponseSchema

---

#### DeleteDeveloperMetadataResponse

**Line:** 1391599

**Inherits:** IDirectResponseSchema

---

#### DeleteDimensionGroupRequest

**Line:** 1391635

**Inherits:** IDirectResponseSchema

---

#### DeleteDimensionGroupResponse

**Line:** 1391671

**Inherits:** IDirectResponseSchema

---

#### DeleteDimensionRequest

**Line:** 1391707

**Inherits:** IDirectResponseSchema

---

#### DeleteDuplicatesRequest

**Line:** 1391743

**Inherits:** IDirectResponseSchema

---

#### DeleteDuplicatesResponse

**Line:** 1391791

**Inherits:** IDirectResponseSchema

---

#### DeleteEmbeddedObjectRequest

**Line:** 1391827

**Inherits:** IDirectResponseSchema

---

#### DeleteFilterViewRequest

**Line:** 1391863

**Inherits:** IDirectResponseSchema

---

#### DeleteIndexBinder

**Line:** 1300036

**Inherits:** DynamicMetaObjectBinder

---

#### DeleteMessageRequest

**Line:** 1527364

**Inherits:** IEquatable

---

#### DeleteNamedRangeRequest

**Line:** 1391899

**Inherits:** IDirectResponseSchema

---

#### DeleteProtectedRangeRequest

**Line:** 1391935

**Inherits:** IDirectResponseSchema

---

#### DeleteRangeRequest

**Line:** 1391971

**Inherits:** IDirectResponseSchema

---

#### DeleteReactionRequest

**Line:** 1526806

**Inherits:** IEquatable

---

#### DeleteSheetRequest

**Line:** 1392019

**Inherits:** IDirectResponseSchema

---

#### DeletedRowInaccessibleException

**Line:** 1080779

**Inherits:** DataException

---

#### DependencyAttribute

**Line:** 253412

**Inherits:** Attribute

**Fields:**

- `dependentAssembly`: string
- `loadHint`: LoadHint

---

#### DepthNormalOnlyPass

**Line:** 919469

**Inherits:** ScriptableRenderPass

**Fields:**

- `m_FilteringSettings`: FilteringSettings

---

#### DepthOfField

**Line:** 909325

**Inherits:** VolumeComponent

**Fields:**

- `mode`: DepthOfFieldModeParameter
- `gaussianStart`: MinFloatParameter
- `gaussianEnd`: MinFloatParameter
- `gaussianMaxRadius`: ClampedFloatParameter
- `highQualitySampling`: BoolParameter
- `focusDistance`: MinFloatParameter
- `aperture`: ClampedFloatParameter
- `focalLength`: ClampedFloatParameter
- `bladeCount`: ClampedIntParameter
- `bladeCurvature`: ClampedFloatParameter
- `bladeRotation`: ClampedFloatParameter

---

#### DepthOfFieldModeParameter

**Line:** 909366

**Inherits:** VolumeParameter

---

#### DepthOnlyPass

**Line:** 919621

**Inherits:** ScriptableRenderPass

**Fields:**

- `depthStencilFormat`: GraphicsFormat
- `m_FilteringSettings`: FilteringSettings

---

#### DescriptionAttribute

**Line:** 780606

**Inherits:** Attribute

---

#### DeserializationConverterDeepCompare

**Line:** 530667

**Inherits:** EqualityComparer

---

#### DeserializationConverters

**Line:** 529217

**Fields:**

- `_baseType`: Type
- `_derivedType`: Type

---

#### DesignOnlyAttribute

**Line:** 780651

**Inherits:** Attribute

---

#### DesignTimeVisibleAttribute

**Line:** 781621

**Inherits:** Attribute

---

#### DesignerCategoryAttribute

**Line:** 780687

**Inherits:** Attribute

---

#### DesignerOptionService

**Line:** 785109

---

#### DesignerSerializationVisibilityAttribute

**Line:** 780741

**Inherits:** Attribute

---

#### DestroyAfterDurationView

**Line:** 731424

**Inherits:** GameUnityView

**Fields:**

- `_tween`: Tween

---

#### DestroyAudioClipAudioSystem

**Line:** 698488

**Inherits:** ICleanupSystem

---

#### DestroyDeathEffectGameSystem

**Line:** 703933

**Inherits:** ICleanupSystem

---

#### DestroyDmgGameSystem

**Line:** 703949

**Inherits:** ICleanupSystem

---

#### DestroyFeature

**Line:** 686766

**Inherits:** Feature

---

#### DestroyHapticFeedbackAudioSystem

**Line:** 698504

**Inherits:** ICleanupSystem

---

#### DestroyOnCloseUiView

**Line:** 737247

**Inherits:** UiUnityView

---

#### DestroySellCoinsGameSystem

**Line:** 703965

**Inherits:** ICleanupSystem

---

#### DestroyedComponent

**Line:** 686757

**Inherits:** IComponent

---

#### DetachFromPanelEvent

**Line:** 637475

**Inherits:** PanelChangedEventBase

---

#### DetailedLocalizationTable

**Line:** 1317386

**Fields:**

- `m_TableEntries`: Dictionary<long, TEntry>

---

#### DevOverwritePlayerStateFailure

**Line:** 556005

**Inherits:** MetaResponse

**Fields:**

- `Reason`: string

---

#### DevOverwritePlayerStateRequest

**Line:** 555977

**Inherits:** MetaRequest

---

#### DevPlayerOverwrite

**Line:** 1304799

**Inherits:** MonoBehaviour

**Fields:**

- `ImportPlayer`: string

---

#### DevSavePathProvider

**Line:** 712386

---

#### DevSaveViewEntry

**Line:** 712408

**Inherits:** MonoBehaviour

**Fields:**

- `SavegameName`: TMP_Text
- `LoadButton`: UnityButton
- `DeleteButton`: UnityButton

---

#### DevSavegameButtonUiView

**Line:** 712263

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton

---

#### DevSavegameListView

**Line:** 712360

**Inherits:** MonoBehaviour

**Fields:**

- `SaveEntry`: DevSaveViewEntry
- `Parent`: Transform

---

#### DeveloperMetadata

**Line:** 1392055

**Inherits:** IDirectResponseSchema

---

#### DeveloperMetadataLocation

**Line:** 1392139

**Inherits:** IDirectResponseSchema

---

#### DeveloperMetadataLookup

**Line:** 1392211

**Inherits:** IDirectResponseSchema

---

#### DevelopmentOnlyActionAttribute

**Line:** 601093

**Inherits:** Attribute

---

#### DevelopmentReceiptAndSignature

**Line:** 1313674

**Fields:**

- `Receipt`: string
- `Signature`: string

---

#### DevelopmentReceiptContent

**Line:** 1313656

**Fields:**

- `productId`: string
- `transactionId`: string
- `originalTransactionId`: string
- `validationDelaySeconds`: float
- `validationTransientErrorProbability`: float
- `subscriptionIsAcquiredViaFamilySharing`: bool
- `paymentType`: string

---

#### DeviceFeature

**Line:** 686889

**Inherits:** Feature

---

#### DeviceIdNotSuppliedException

**Line:** 685220

**Inherits:** BadRequestException

---

#### DeviceMultitouchSystem

**Line:** 686898

**Inherits:** IInitializeSystem

---

#### DevicePerformanceSystem

**Line:** 686913

**Inherits:** IInitializeSystem

---

#### DeviceRunInBackgroundSystem

**Line:** 686928

**Inherits:** IInitializeSystem

---

#### DiagnosticListener

**Line:** 1418849

**Inherits:** DiagnosticSource

**Fields:**

- `_next`: DiagnosticListener
- `_disposed`: bool

---

#### DiagnosticSource

**Line:** 1418704

---

#### DiagnosticsConfigurationHandler

**Line:** 803312

**Inherits:** IConfigurationSectionHandler

---

#### DiagnosticsTraceWriter

**Line:** 1038526

**Inherits:** ITraceWriter

---

#### DialogResult

**Line:** 696692

---

#### Dictionary

**Line:** 329120

**Fields:**

- `_count`: int
- `_freeList`: int
- `_freeCount`: int
- `_version`: int
- `_comparer`: IEqualityComparer<TKey>
- `_syncRoot`: object

---

#### DictionaryDrawerSettingsAttribute

**Line:** 695556

**Inherits:** PropertyAttribute

---

#### DictionaryPropertyBag

**Line:** 1463316

---

#### DictionarySource

**Line:** 1321686

**Inherits:** ISource

---

#### DimensionGroup

**Line:** 1392319

**Inherits:** IDirectResponseSchema

---

#### DimensionProperties

**Line:** 1392379

**Inherits:** IDirectResponseSchema

---

#### DimensionRange

**Line:** 1392463

**Inherits:** IDirectResponseSchema

---

#### DirectConnectionClientError

**Line:** 1305979

**Inherits:** Exception

---

#### DirectTransportClient

**Line:** 546214

---

#### DirectTransportRouterBase

**Line:** 546402

**Fields:**

- `_defaultSocket4`: Socket
- `_defaultSocket6`: Socket

---

#### DirectoryInfo

**Line:** 469395

**Inherits:** FileSystemInfo

---

#### DirectoryNotFoundException

**Line:** 467702

**Inherits:** IOException

---

#### DisabledComponent

**Line:** 696062

**Inherits:** IComponent

---

#### DisabledEventSystem

**Line:** 701768

**Inherits:** ReactiveSystem

---

#### DisabledListenerComponent

**Line:** 699544

**Inherits:** IComponent

**Fields:**

- `value`: List<IDisabledListener>

---

#### DisabledRemovedEventSystem

**Line:** 701789

**Inherits:** ReactiveSystem

---

#### DisabledRemovedListenerComponent

**Line:** 699557

**Inherits:** IComponent

**Fields:**

- `value`: List<IDisabledRemovedListener>

---

#### DisallowMultipleComponent

**Line:** 881517

**Inherits:** Attribute

---

#### DisallowMultipleRendererFeature

**Line:** 912283

**Inherits:** Attribute

---

#### DisallowNullAttribute

**Line:** 275833

**Inherits:** Attribute

---

#### DisconnectedFromServer

**Line:** 498544

**Inherits:** MetaMessage

---

#### DiscreteEvaluationAttribute

**Line:** 1575738

**Inherits:** Attribute

---

#### DiscriminatedUnionConverter

**Line:** 1048478

**Inherits:** JsonConverter

---

#### DiskBlobStorage

**Line:** 499957

**Inherits:** IBlobStorage

**Fields:**

- `_dirName`: string

---

#### Dispatcher

**Line:** 696153

---

#### Display

**Line:** 872615

---

#### DisplayAttribute

**Line:** 1508982

**Inherits:** Attribute

**Fields:**

- `_autoGenerateField`: Nullable<bool>
- `_autoGenerateFilter`: Nullable<bool>
- `_order`: Nullable<int>
- `_resourceType`: Type

---

#### DisplayColumnAttribute

**Line:** 1509094

**Inherits:** Attribute

---

#### DisplayFormatAttribute

**Line:** 1509139

**Inherits:** Attribute

---

#### DisplayInfoAttribute

**Line:** 807863

**Inherits:** Attribute

**Fields:**

- `name`: string
- `order`: int

---

#### DisplayNameAttribute

**Line:** 1314879

**Inherits:** Attribute

---

#### DistributedContextPropagator

**Line:** 1419712

---

#### DistributedUIDGenerator

**Line:** 1317701

**Inherits:** IKeyGenerator

**Fields:**

- `m_CustomEpoch`: long
- `m_LastTimestamp`: long
- `m_Sequence`: long
- `m_MachineId`: int

---

#### DivideByZeroException

**Line:** 22725

**Inherits:** ArithmeticException

---

#### DivisionActionBase

**Line:** 563263

**Inherits:** ModelAction

**Fields:**

- `InvokingParticipantId`: EntityId
- `InvokingPlayerId`: EntityId

---

#### DivisionClientContext

**Line:** 563322

**Fields:**

- `_playerId`: EntityId
- `_participantId`: EntityId
- `_clientSlot`: ClientSlot

---

#### DivisionClientListener

**Line:** 737942

**Inherits:** IPlayerDivisionModelClientListenerCore

---

#### DivisionClientState

**Line:** 1051184

**Inherits:** DivisionClientStateBase

---

#### DivisionClientStateBase

**Line:** 563429

---

#### DivisionConclude

**Line:** 563279

**Inherits:** DivisionActionBase

---

#### DivisionConcludeSeasonDebug

**Line:** 566304

**Inherits:** DivisionDebugAction

---

#### DivisionDebugAction

**Line:** 566210

**Inherits:** DivisionActionBase

---

#### DivisionEntityClientData

**Line:** 566179

**Inherits:** EntityClientData

---

#### DivisionEventBase

**Line:** 563700

**Inherits:** EntityEventBase

---

#### DivisionEventCreated

**Line:** 563619

**Inherits:** DivisionEventBase

---

#### DivisionEventParticipantJoined

**Line:** 563654

**Inherits:** DivisionEventBase

---

#### DivisionModelBase

**Line:** 564278

---

#### DivisionModelRuntimeDataBase

**Line:** 563911

---

#### DivisionParticipantRemove

**Line:** 563292

**Inherits:** DivisionActionBase

---

#### DivisionParticipantStateBase

**Line:** 563956

---

#### DivisionScoreEventBase

**Line:** 564911

---

#### DivisionSetSeasonEndsAtDebug

**Line:** 566273

**Inherits:** DivisionDebugAction

---

#### DivisionUpdateSeasonScheduleDebug

**Line:** 566220

**Inherits:** DivisionDebugAction

---

#### DllImportAttribute

**Line:** 229286

**Inherits:** Attribute

**Fields:**

- `EntryPoint`: string
- `CharSet`: CharSet
- `SetLastError`: bool
- `ExactSpelling`: bool
- `PreserveSig`: bool
- `CallingConvention`: CallingConvention
- `BestFitMapping`: bool
- `ThrowOnUnmappableChar`: bool

---

#### DllNotFoundException

**Line:** 22744

**Inherits:** TypeLoadException

---

#### DmgComponent

**Line:** 709096

**Inherits:** IComponent

**Fields:**

- `Value`: DmgInfo

---

#### DmgNumberLabel

**Line:** 709730

**Inherits:** MonoBehaviour

**Fields:**

- `Label`: TextMeshPro
- `CritColor`: Color
- `BlockColor`: Color
- `LifeStealColor`: Color
- `_tween`: Sequence

---

#### DmgNumbersView

**Line:** 709776

**Inherits:** GameUnityView

**Fields:**

- `_dmgLabelPool`: Pool<DmgNumberLabel>
- `LabelPrefab`: DmgNumberLabel

---

#### DoNotDestroyOnCloseComponent

**Line:** 736180

**Inherits:** IComponent

---

#### DoNotNormalizeAttribute

**Line:** 949810

**Inherits:** PropertyAttribute

---

#### DockConsoleController

**Line:** 1443685

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_isDirty`: bool
- `_isDragging`: bool
- `_pointersOver`: int
- `BottomHandle`: GameObject
- `CanvasGroup`: CanvasGroup
- `Console`: ConsoleLogControl
- `Dropdown`: GameObject
- `DropdownToggleSprite`: Image
- `TextErrors`: Text
- `TextInfo`: Text
- `TextWarnings`: Text
- `ToggleErrors`: Toggle
- `ToggleInfo`: Toggle
- `ToggleWarnings`: Toggle
- `TopBar`: GameObject
- `TopHandle`: GameObject

---

#### DockConsoleServiceImpl

**Line:** 1445812

**Inherits:** IDockConsoleService

**Fields:**

- `_alignment`: ConsoleAlignment
- `_consoleRoot`: DockConsoleController
- `_didSuspendTrigger`: bool
- `_isExpanded`: bool
- `_isVisible`: bool

---

#### DocumentationInfo

**Line:** 816357

---

#### DoesNotReturnAttribute

**Line:** 275905

**Inherits:** Attribute

---

#### DoesNotReturnIfAttribute

**Line:** 275915

**Inherits:** Attribute

---

#### DontCreatePropertyAttribute

**Line:** 1458024

**Inherits:** Attribute

---

#### DontDrawComponentAttribute

**Line:** 1590995

**Inherits:** Attribute

---

#### DontGenerateAttribute

**Line:** 1597401

**Inherits:** Attribute

---

#### DoubleConverter

**Line:** 781656

**Inherits:** BaseNumberConverter

---

#### DoubleField

**Line:** 617077

**Inherits:** TextValueField

---

#### DoublePlugin

**Line:** 1429119

**Inherits:** ABSTweenPlugin

---

#### DoubleTrackedProperty

**Line:** 1328941

**Inherits:** TrackedProperty

---

#### DoubleVariable

**Line:** 1324749

**Inherits:** Variable

---

#### DownloadHandler

**Line:** 1566010

**Inherits:** IDisposable

---

#### DownloadHandlerAssetBundle

**Line:** 1592760

**Inherits:** DownloadHandler

---

#### DownloadHandlerBuffer

**Line:** 1566126

**Inherits:** DownloadHandler

**Fields:**

- `m_NativeData`: NativeArray<byte>

---

#### DownloadTaskWrapper

**Line:** 498411

**Fields:**

- `_task`: Task<TResult>
- `_lockedException`: Exception
- `_lockedTimeout`: bool

---

#### DownscaleParameter

**Line:** 909145

**Inherits:** VolumeParameter

---

#### DragHandle

**Line:** 1506454

**Inherits:** MonoBehaviour

**Fields:**

- `_canvasScaler`: CanvasScaler
- `_delta`: float
- `_startValue`: float
- `Invert`: bool
- `MaxSize`: float
- `TargetLayoutElement`: LayoutElement
- `TargetRectTransform`: RectTransform

---

#### DrawObjectsPass

**Line:** 919728

**Inherits:** ScriptableRenderPass

**Fields:**

- `m_FilteringSettings`: FilteringSettings
- `m_RenderStateBlock`: RenderStateBlock
- `m_ShaderTagIdList`: List<ShaderTagId>
- `m_IsOpaque`: bool
- `m_IsActiveTargetBackBuffer`: bool
- `m_ShouldTransparentsReceiveShadows`: bool

---

#### DrawSkyboxPass

**Line:** 910184

**Inherits:** ScriptableRenderPass

---

#### DriveNotFoundException

**Line:** 469328

**Inherits:** IOException

---

#### DroneView

**Line:** 730877

**Inherits:** GameUnityView

**Fields:**

- `_currentPosition`: Vector2
- `_currentVelocity`: Vector2
- `_timer`: float
- `_maxTimer`: float
- `_blockMove`: bool
- `_flySequence`: Sequence
- `Drone`: Transform
- `Shadow`: Transform
- `Rig`: CharacterRig

---

#### DuplicateFilterViewRequest

**Line:** 1392535

**Inherits:** IDirectResponseSchema

---

#### DuplicateFilterViewResponse

**Line:** 1392571

**Inherits:** IDirectResponseSchema

---

#### DuplicateNameException

**Line:** 1080795

**Inherits:** DataException

---

#### DuplicateSheetRequest

**Line:** 1392607

**Inherits:** IDirectResponseSchema

---

#### DuplicateSheetResponse

**Line:** 1392679

**Inherits:** IDirectResponseSchema

---

#### DurationComponent

**Line:** 696071

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### DurationPattern

**Line:** 1151724

**Inherits:** IPattern

---

#### DynamicArray

**Line:** 808552

---

#### DynamicAtlasCustomFilter

**Line:** 606485

**Inherits:** MulticastDelegate

---

#### DynamicAtlasSettings

**Line:** 640041

**Fields:**

- `m_MinAtlasSize`: int
- `m_MaxAtlasSize`: int
- `m_MaxSubTextureSize`: int
- `m_ActiveFilters`: DynamicAtlasFilters
- `m_CustomFilter`: DynamicAtlasCustomFilter

---

#### DynamicEnum

**Line:** 500670

---

#### DynamicEnumFactoryAttribute

**Line:** 500644

**Inherits:** Attribute

---

#### DynamicEnumRegistry

**Line:** 500937

**Fields:**

- `_infos`: Dictionary<Type, DynamicEnumTypeInfo>

---

#### DynamicEnumTypeConverter

**Line:** 500862

**Inherits:** StringTypeConverterHelper

**Fields:**

- `_dynamicEnumType`: Type

---

#### DynamicEnumTypeInfo

**Line:** 500893

**Fields:**

- `_baseDynamicEnumType`: Type
- `_allValuesList`: IList
- `_nameToValue`: Dictionary<string, IDynamicEnum>
- `_idToValue`: Dictionary<int, IDynamicEnum>

---

#### DynamicMetaObject

**Line:** 1300084

---

#### DynamicMetaObjectBinder

**Line:** 1300178

**Inherits:** CallSiteBinder

---

#### DynamicMethod

**Line:** 269325

**Inherits:** MethodInfo

---

#### DynamicPurchaseContent

**Line:** 583738

---

#### DynamicResolutionHandler

**Line:** 809638

**Fields:**

- `m_Enabled`: bool
- `m_UseMipBias`: bool
- `m_MinScreenFraction`: float
- `m_MaxScreenFraction`: float
- `m_CurrentFraction`: float
- `m_ForcingRes`: bool
- `m_CurrentCameraRequest`: bool
- `m_PrevFraction`: float
- `m_ForceSoftwareFallback`: bool
- `m_RunUpscalerFilterOnFullResolution`: bool
- `m_PrevHWScaleWidth`: float
- `m_PrevHWScaleHeight`: float
- `m_LastScaledSize`: Vector2Int
- `cachedOriginalSize`: Vector2Int
- `type`: DynamicResolutionType
- `m_CachedSettings`: GlobalDynamicResolutionSettings
- `m_OwnerCameraWeakRef`: WeakReference

---

#### DynamicString

**Line:** 809809

**Inherits:** DynamicArray

---

#### DynamicToggleChild

**Line:** 736812

**Inherits:** MonoBehaviour

**Fields:**

- `ToggleComponent`: Toggle
- `ItemParent`: Transform

---

#### DynamicToggleGroup

**Line:** 736843

**Inherits:** MonoBehaviour

**Fields:**

- `_iconTogglePrefab`: DynamicToggleChild
- `_iconGridParent`: Transform
- `_toggleGroup`: ToggleGroup
- `_selectedIndex`: int

---

#### ECDsa

**Line:** 1230586

**Inherits:** AsymmetricAlgorithm

---

#### EarlyInitHelpers

**Line:** 1167801

---

#### EaseCurve

**Line:** 1432998

---

#### EaseFactory

**Line:** 1425527

---

#### EaseFunction

**Line:** 1425029

**Inherits:** MulticastDelegate

---

#### EditableAttribute

**Line:** 1509215

**Inherits:** Attribute

---

#### EditorAttribute

**Line:** 781685

**Inherits:** Attribute

**Fields:**

- `_typeId`: string

---

#### EditorBrowsableAttribute

**Line:** 780528

**Inherits:** Attribute

**Fields:**

- `browsableState`: EditorBrowsableState

---

#### Editors

**Line:** 1392715

**Inherits:** IDirectResponseSchema

---

#### ElapsedEventArgs

**Line:** 775276

**Inherits:** EventArgs

**Fields:**

- `time`: DateTime

---

#### ElapsedEventHandler

**Line:** 775153

**Inherits:** MulticastDelegate

---

#### ElementInfoAttribute

**Line:** 888299

**Inherits:** Attribute

---

#### ElementInit

**Line:** 1286521

**Inherits:** IArgumentProvider

---

#### EmailAddressAttribute

**Line:** 1509247

**Inherits:** DataTypeAttribute

---

#### EmbeddedChart

**Line:** 1392775

**Inherits:** IDirectResponseSchema

---

#### EmbeddedObjectBorder

**Line:** 1392847

**Inherits:** IDirectResponseSchema

---

#### EmbeddedObjectPosition

**Line:** 1392895

**Inherits:** IDirectResponseSchema

---

#### EmptyEntityLogSystem

**Line:** 695504

**Inherits:** IExecuteSystem

---

#### EmptyGameConfigDataResolver

**Line:** 588046

**Inherits:** IGameConfigDataResolver

---

#### EmptyGraphic

**Line:** 714280

**Inherits:** Graphic

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

#### EnableNotificationsButtonView

**Line:** 694383

**Inherits:** UiUnityView

**Fields:**

- `_button`: UnityButton

---

#### Encapsulator

**Line:** 1319882

**Inherits:** IPseudoLocalizationMethod

**Fields:**

- `m_Start`: string
- `m_End`: string

---

#### Encoder

**Line:** 214510

---

#### EncoderExceptionFallback

**Line:** 214638

**Inherits:** EncoderFallback

---

#### EncoderExceptionFallbackBuffer

**Line:** 214662

**Inherits:** EncoderFallbackBuffer

---

#### EncoderFallback

**Line:** 214715

---

#### EncoderFallbackBuffer

**Line:** 214745

---

#### EncoderFallbackException

**Line:** 214690

**Inherits:** ArgumentException

**Fields:**

- `_charUnknown`: char
- `_charUnknownHigh`: char
- `_charUnknownLow`: char
- `_index`: int

---

#### EncoderReplacementFallback

**Line:** 214854

**Inherits:** EncoderFallback

**Fields:**

- `_strDefault`: string

---

#### EncoderReplacementFallbackBuffer

**Line:** 214894

**Inherits:** EncoderFallbackBuffer

**Fields:**

- `_strDefault`: string
- `_fallbackCount`: int
- `_fallbackIndex`: int

---

#### Encoding

**Line:** 216236

**Inherits:** ICloneable

**Fields:**

- `m_isReadOnly`: bool

---

#### EncodingProvider

**Line:** 214978

---

#### EndOfStreamException

**Line:** 467718

**Inherits:** IOException

---

#### EndPoint

**Line:** 791450

---

#### EndlessComponent

**Line:** 696233

**Inherits:** IComponent

---

#### EngineEmitter

**Line:** 1437930

**Inherits:** IProfilerEmitter

---

#### EntitasException

**Line:** 1547903

**Inherits:** Exception

---

#### EntitasPopupUiView

**Line:** 737265

**Inherits:** UiUnityView

**Fields:**

- `CanvasGroup`: CanvasGroup
- `Container`: RectTransform
- `SkipBackgroundClick`: bool
- `SkipCloseButton`: bool
- `CloseButton`: UnityButton
- `BackgroundButton`: UnityButton
- `_openTween`: Sequence

---

#### Entities

**Line:** 1056939

**Fields:**

- `_entityId`: int
- `_playerEntityId`: int
- `_enemyPlayerEntityId`: int
- `_units`: MetaDictionary<int, UnitEntity>
- `_allySkills`: MetaDictionary<CombatSkill, SkillEntity>
- `_enemySkills`: MetaDictionary<CombatSkill, SkillEntity>
- `_projectiles`: MetaDictionary<int, ProjectileEntity>
- `_areaProjectiles`: MetaDictionary<int, AreaProjectile>

---

#### Entity

**Line:** 1546289

**Inherits:** IEntity

**Fields:**

- `OnComponentAdded`: EntityComponentChanged
- `OnComponentRemoved`: EntityComponentChanged
- `OnComponentReplaced`: EntityComponentReplaced
- `OnEntityReleased`: EntityEvent
- `OnDestroyEntity`: EntityEvent
- `_creationIndex`: int
- `_isEnabled`: bool
- `_totalComponents`: int
- `_contextInfo`: ContextInfo
- `_aerc`: IAERC
- `_toStringCache`: string
- `_toStringBuilder`: StringBuilder

---

#### EntityActivated

**Line:** 553814

**Inherits:** MetaMessage

---

#### EntityAlreadyHasComponentException

**Line:** 1547463

**Inherits:** EntitasException

---

#### EntityBehaviour

**Line:** 1591005

**Inherits:** MonoBehaviour

**Fields:**

- `_context`: IContext
- `_entity`: IEntity
- `_entityBehaviourPool`: Stack<EntityBehaviour>
- `_cachedName`: string

---

#### EntityChecksumMismatchDetails

**Line:** 553596

**Inherits:** MetaMessage

**Fields:**

- `Tick`: long
- `Operation`: int

---

#### EntityClientData

**Line:** 553293

---

#### EntityClientDebugConfig

**Line:** 576476

---

#### EntityClientToServerEnvelope

**Line:** 553696

**Inherits:** MetaMessage

---

#### EntityComponentChanged

**Line:** 1548108

**Inherits:** MulticastDelegate

---

#### EntityComponentReplaced

**Line:** 1548126

**Inherits:** MulticastDelegate

---

#### EntityConnectionDowngrade

**Line:** 553992

**Inherits:** MetaMessage

---

#### EntityDoesNotHaveComponentException

**Line:** 1547472

**Inherits:** EntitasException

---

#### EntityEnqueueActionsRequest

**Line:** 553513

**Inherits:** MetaMessage

---

#### EntityEqualityComparer

**Line:** 1547422

---

#### EntityEvent

**Line:** 1548144

**Inherits:** MulticastDelegate

---

#### EntityEventBase

**Line:** 573431

**Inherits:** AnalyticsEventBase

---

#### EntityEventLog

**Line:** 573454

---

#### EntityEventLogEntry

**Line:** 573187

---

#### EntityIndex

**Line:** 1545751

---

#### EntityIndexAttribute

**Line:** 1597426

**Inherits:** AbstractEntityIndexAttribute

---

#### EntityIndexException

**Line:** 1547558

**Inherits:** EntitasException

---

#### EntityIndexGetMethodAttribute

**Line:** 1597436

**Inherits:** Attribute

---

#### EntityInitialState

**Line:** 553447

---

#### EntityIsAlreadyRetainedByOwnerException

**Line:** 1547481

**Inherits:** EntitasException

---

#### EntityIsNotDestroyedException

**Line:** 1547404

**Inherits:** EntitasException

---

#### EntityIsNotEnabledException

**Line:** 1547490

**Inherits:** EntitasException

---

#### EntityIsNotRetainedByOwnerException

**Line:** 1547499

**Inherits:** EntitasException

---

#### EntityKindRegistry

**Line:** 501330

---

#### EntityKindRegistryAttribute

**Line:** 498933

**Inherits:** Attribute

---

#### EntityLink

**Line:** 1597741

**Inherits:** MonoBehaviour

**Fields:**

- `_entity`: IEntity
- `_applicationIsQuitting`: bool

---

#### EntityMessageDispatcher

**Line:** 551701

**Inherits:** BasicMessageDispatcher

**Fields:**

- `_rootDispatcher`: IMessageDispatcher
- `_channel`: int
- `_logicVersion`: int
- `_config`: ISharedGameConfig
- `_bufferChannel`: int
- `_overrideSendMethod`: Func<MetaMessage, bool>

---

#### EntityRef

**Line:** 739520

---

#### EntityServerToClientEnvelope

**Line:** 553735

**Inherits:** MetaMessage

---

#### EntitySwitchedMessage

**Line:** 553774

**Inherits:** MetaMessage

---

#### EntityTagHeaderValue

**Line:** 1489422

**Inherits:** ICloneable

---

#### EntityTimelinePingTraceMarker

**Line:** 553656

**Inherits:** MetaMessage

---

#### EntityTimelinePingTraceQuery

**Line:** 553618

**Inherits:** MetaMessage

---

#### EntityTimelineUpdateMessage

**Line:** 553541

**Inherits:** MetaMessage

---

#### EntryPointNotFoundException

**Line:** 22891

**Inherits:** TypeLoadException

---

#### Enum

**Line:** 173056

**Inherits:** ValueType

---

#### EnumAsIntConverter

**Line:** 583080

**Inherits:** JsonConverter

---

#### EnumBuilder

**Line:** 269411

**Inherits:** TypeInfo

---

#### EnumControl

**Line:** 1444868

**Inherits:** DataBoundControl

**Fields:**

- `_lastValue`: object
- `_values`: Array
- `ContentLayoutElement`: LayoutElement
- `Spinner`: SRSpinner
- `Title`: Text
- `Value`: Text

---

#### EnumConverter

**Line:** 783554

**Inherits:** TypeConverter

**Fields:**

- `type`: Type

---

#### EnumDataTypeAttribute

**Line:** 1509263

**Inherits:** DataTypeAttribute

---

#### EnumField

**Line:** 617221

**Inherits:** BaseField

**Fields:**

- `m_EnumType`: Type
- `m_IncludeObsoleteValues`: bool
- `m_TextElement`: TextElement
- `m_ArrowElement`: VisualElement
- `m_EnumData`: EnumData

---

#### EnumMap

**Line:** 755970

---

#### EnumParameter

**Line:** 826919

---

#### EnumTrackedProperty

**Line:** 1328961

**Inherits:** IntTrackedProperty

---

#### EnumerationOptions

**Line:** 469413

---

#### EnumeratorCancellationAttribute

**Line:** 264096

**Inherits:** Attribute

---

#### EnvironmentConfig

**Line:** 577155

**Inherits:** IMetaIntegrationConstructible

**Fields:**

- `Version`: int
- `Id`: string
- `DisplayName`: string
- `Description`: string
- `ConnectionEndpointConfig`: ConnectionEndpointConfig
- `ClientLoggingConfig`: ClientLoggingConfig
- `ClientGameConfigBuildApiConfig`: ClientGameConfigBuildApiConfig

---

#### EqualityComparer

**Line:** 436213

---

#### EquipItemAction

**Line:** 1067522

**Inherits:** PlayerAction

---

#### EquipmentFeature

**Line:** 713772

**Inherits:** Feature

---

#### EquipmentFeatureInitSystem

**Line:** 713875

**Inherits:** IInitializeSystem

---

#### EquipmentItem

**Line:** 713634

**Inherits:** MonoBehaviour

---

#### EquipmentItemInfo

**Line:** 1067592

**Inherits:** IGameConfigData

---

#### EquipmentItemVisualConfig

**Line:** 713646

**Inherits:** ScriptableObject

**Fields:**

- `Icon`: Sprite
- `Prefab`: EquipmentItem

---

#### EquipmentStatTarget

**Line:** 1076890

**Inherits:** StatTargetBase

---

#### EquippedArmourIdComponent

**Line:** 710546

**Inherits:** IComponent

**Fields:**

- `Value`: ItemId

---

#### EquippedArmourIdEventSystem

**Line:** 701831

**Inherits:** ReactiveSystem

---

#### EquippedArmourIdListenerComponent

**Line:** 699583

**Inherits:** IComponent

**Fields:**

- `value`: List<IEquippedArmourIdListener>

---

#### EquippedComponent

**Line:** 725317

**Inherits:** IComponent

---

#### EquippedEventSystem

**Line:** 701852

**Inherits:** ReactiveSystem

---

#### EquippedHelmetIdComponent

**Line:** 710533

**Inherits:** IComponent

**Fields:**

- `Value`: ItemId

---

#### EquippedHelmetIdEventSystem

**Line:** 701873

**Inherits:** ReactiveSystem

---

#### EquippedHelmetIdListenerComponent

**Line:** 699596

**Inherits:** IComponent

**Fields:**

- `value`: List<IEquippedHelmetIdListener>

---

#### EquippedItemPopupUiView

**Line:** 713929

**Inherits:** UiUnityView

**Fields:**

- `Item`: ItemVisual

---

#### EquippedListenerComponent

**Line:** 699609

**Inherits:** IComponent

**Fields:**

- `value`: List<IEquippedListener>

---

#### EquippedRemovedEventSystem

**Line:** 701894

**Inherits:** ReactiveSystem

---

#### EquippedRemovedListenerComponent

**Line:** 699622

**Inherits:** IComponent

**Fields:**

- `value`: List<IEquippedRemovedListener>

---

#### EquippedSetPieceMessage

**Line:** 728770

**Inherits:** IMessage

---

#### Era

**Line:** 1166693

---

#### ErrorContext

**Line:** 1038559

---

#### ErrorEventArgs

**Line:** 1038630

**Inherits:** EventArgs

---

#### ErrorNotifier

**Line:** 1443789

**Inherits:** MonoBehaviour

**Fields:**

- `_animator`: Animator
- `_triggerHash`: int
- `_hideTime`: float
- `_isShowing`: bool
- `_queueWarning`: bool

---

#### ErrorResponse

**Line:** 1529125

**Inherits:** IEquatable

---

#### ErrorState

**Line:** 1310009

**Inherits:** ConnectionState

---

#### ErrorValue

**Line:** 1392955

**Inherits:** IDirectResponseSchema

---

#### ErrorWrapper

**Line:** 228953

**Fields:**

- `m_ErrorCode`: int

---

#### EvaluateException

**Line:** 1086402

**Inherits:** InvalidExpressionException

---

#### Event

**Line:** 1450266

---

#### EventArgs

**Line:** 22907

---

#### EventAttribute

**Line:** 1597465

**Inherits:** Attribute

---

#### EventBase

**Line:** 634525

**Fields:**

- `m_RefCount`: int

---

#### EventBuilder

**Line:** 269534

---

#### EventCallback

**Line:** 634656

---

#### EventCommandEventArgs

**Line:** 275644

**Inherits:** EventArgs

---

#### EventDescriptor

**Line:** 781723

**Inherits:** MemberDescriptor

---

#### EventDescriptorCollection

**Line:** 781771

**Inherits:** ICollection

**Fields:**

- `_eventsOwned`: bool
- `_needSort`: bool

---

#### EventDispatcher

**Line:** 632890

**Fields:**

- `m_Queue`: Queue<EventDispatcher.EventRecord>
- `m_GateCount`: uint
- `m_GateDepth`: uint
- `m_DispatchStackFrame`: int
- `m_CurrentEvent`: EventBase
- `m_DispatchContexts`: Stack<EventDispatcher.DispatchContext>
- `m_Immediate`: bool

---

#### EventHandler

**Line:** 22934

---

#### EventHandlerList

**Line:** 780832

**Inherits:** IDisposable

**Fields:**

- `_parent`: Component

---

#### EventInfo

**Line:** 265309

**Inherits:** MemberInfo

---

#### EventInterestAttribute

**Line:** 671241

**Inherits:** Attribute

---

#### EventPayloadBase

**Line:** 578557

---

#### EventSource

**Line:** 275691

**Inherits:** IDisposable

---

#### EventSourceAttribute

**Line:** 275783

**Inherits:** Attribute

---

#### EventSystem

**Line:** 1359788

**Inherits:** UIBehaviour

**Fields:**

- `m_SystemInputModules`: List<BaseInputModule>
- `m_CurrentInputModule`: BaseInputModule
- `m_FirstSelected`: GameObject
- `m_sendNavigationEvents`: bool
- `m_DragThreshold`: int
- `m_CurrentSelected`: GameObject
- `m_HasFocus`: bool
- `m_SelectionGuard`: bool
- `m_DummyData`: BaseEventData
- `m_Started`: bool
- `m_IsTrackingUIToolkitPanels`: bool

---

#### EventTrigger

**Line:** 1359969

**Inherits:** MonoBehaviour

**Fields:**

- `m_Delegates`: List<EventTrigger.Entry>

---

#### EventWaitHandle

**Line:** 180396

**Inherits:** WaitHandle

---

#### Evidence

**Line:** 217334

**Inherits:** ICollection

**Fields:**

- `_locked`: bool
- `hostEvidenceList`: ArrayList
- `assemblyEvidenceList`: ArrayList

---

#### Exception

**Line:** 173312

**Inherits:** ISerializable

**Fields:**

- `_className`: string
- `_data`: IDictionary
- `_innerException`: Exception
- `_helpURL`: string
- `_stackTrace`: object
- `_stackTraceString`: string
- `_remoteStackTraceString`: string
- `_remoteStackIndex`: int
- `_dynamicMethods`: object
- `_source`: string
- `_safeSerializationManager`: SafeSerializationManager
- `caught_in_unmanaged`: int

---

#### ExceptionDispatchInfo

**Line:** 229949

**Fields:**

- `m_Exception`: Exception
- `m_stackTrace`: object

---

#### ExceptionHandlingClause

**Line:** 268099

---

#### ExceptionRecorder

**Line:** 1418275

**Inherits:** MulticastDelegate

---

#### ExcludeEntryFromExport

**Line:** 1327303

**Inherits:** IMetadata

---

#### ExcludeFromBurstCompatTestingAttribute

**Line:** 1184690

**Inherits:** Attribute

---

#### ExcludeFromCodeCoverageAttribute

**Line:** 778383

**Inherits:** Attribute

---

#### ExcludeFromDocsAttribute

**Line:** 890764

**Inherits:** Attribute

---

#### ExcludeFromEventLogAttribute

**Line:** 600990

**Inherits:** MetaMemberFlagAttribute

---

#### ExcludeFromGdprExportAttribute

**Line:** 600707

**Inherits:** Attribute

---

#### ExcludeFromObjectFactoryAttribute

**Line:** 882764

**Inherits:** Attribute

---

#### ExcludeFromPresetAttribute

**Line:** 881707

**Inherits:** Attribute

---

#### ExecuteAlways

**Line:** 881632

**Inherits:** Attribute

---

#### ExecuteCommandEvent

**Line:** 634132

**Inherits:** CommandEventBase

---

#### ExecuteEvents

**Line:** 1360079

---

#### ExecuteInEditMode

**Line:** 881622

**Inherits:** Attribute

---

#### ExecutionContext

**Line:** 180574

**Inherits:** IDisposable

**Fields:**

- `_syncContext`: SynchronizationContext
- `_syncContextNoFlow`: SynchronizationContext
- `_logicalCallContext`: LogicalCallContext
- `_illogicalCallContext`: IllogicalCallContext
- `_localValues`: Dictionary<IAsyncLocal, object>
- `_localChangeNotifications`: List<IAsyncLocal>

---

#### ExecutionEngineException

**Line:** 22976

**Inherits:** SystemException

---

#### ExitGUIException

**Line:** 1452408

**Inherits:** Exception

---

#### ExitSteppingStonesSceneAction

**Line:** 1079373

**Inherits:** PlayerAction

---

#### ExpandableObjectConverter

**Line:** 781909

**Inherits:** TypeConverter

---

#### Expander

**Line:** 1319974

**Inherits:** IPseudoLocalizationMethod

**Fields:**

- `m_ExpansionRules`: List<Expander.ExpansionRule>
- `m_MinimumStringLength`: int
- `m_PaddingCharacters`: List<char>

---

#### ExpandoObject

**Line:** 1300646

**Inherits:** IDynamicMetaObjectProvider

**Fields:**

- `_count`: int
- `_propertyChanged`: PropertyChangedEventHandler

---

#### ExpandoObjectConverter

**Line:** 1048547

**Inherits:** JsonConverter

---

#### ExperimentVariantId

**Line:** 533145

**Inherits:** StringId

---

#### ExplicitNullConverter

**Line:** 1496479

**Inherits:** JsonConverter

---

#### ExponentialBackOff

**Line:** 1494990

**Inherits:** IBackOff

**Fields:**

- `random`: Random

---

#### ExponentialBackOffInitializer

**Line:** 1497277

**Inherits:** IConfigurableHttpClientInitializer

---

#### Expression

**Line:** 1287872

---

#### ExpressionEvaluator

**Line:** 871781

---

#### ExpressionVisitor

**Line:** 1287230

---

#### ExtendableEventParams

**Line:** 578606

**Fields:**

- `MaxExtensionsPerActivation`: int
- `ExtensionDuration`: MetaDuration
- `ExtensionReviewDuration`: MetaDuration

---

#### ExtendableEventSet

**Line:** 578802

---

#### ExtendableEventState

**Line:** 578655

**Fields:**

- `LastExtensionStartedAt`: Nullable<MetaTime>
- `LatestActivationNumExtended`: int
- `NumSoftFinalizedInLatestActivation`: int

---

#### ExtendedProtectionPolicy

**Line:** 778475

**Inherits:** ISerializable

---

#### ExtendedProtectionPolicyTypeConverter

**Line:** 778496

**Inherits:** TypeConverter

---

#### ExtendedValue

**Line:** 1393003

**Inherits:** IDirectResponseSchema

---

#### ExtenderProvidedPropertyAttribute

**Line:** 781971

**Inherits:** Attribute

---

#### ExtensionAttribute

**Line:** 234170

**Inherits:** Attribute

---

#### ExtensionDataGetter

**Line:** 1038997

**Inherits:** MulticastDelegate

---

#### ExtensionDataSetter

**Line:** 1038978

**Inherits:** MulticastDelegate

---

#### ExternalAccountCredential

**Line:** 1370694

**Inherits:** ServiceCredential

---

#### ExternalException

**Line:** 228533

**Inherits:** SystemException

---

#### F128Converter

**Line:** 558180

**Inherits:** JsonConverter

---

#### F1DConverter

**Line:** 558359

**Inherits:** JsonConverter

---

#### FD6Converter

**Line:** 560889

**Inherits:** JsonConverter

---

#### FSharpCoreReflectionProxy

**Line:** 1011890

---

#### FablAssertException

**Line:** 1596424

**Inherits:** Exception

---

#### FaceInfo_Legacy

**Line:** 1223191

**Fields:**

- `Name`: string
- `PointSize`: float
- `Scale`: float
- `CharacterCount`: int
- `LineHeight`: float
- `Baseline`: float
- `Ascender`: float
- `CapHeight`: float
- `Descender`: float
- `CenterLine`: float
- `SuperscriptOffset`: float
- `SubscriptOffset`: float
- `SubSize`: float
- `Underline`: float
- `UnderlineThickness`: float
- `strikethrough`: float
- `strikethroughThickness`: float
- `TabWidth`: float
- `Padding`: float
- `AtlasWidth`: float
- ... (1 more fields)

---

#### Factory

**Line:** 1597708

---

#### FakeAmazonExtensions

**Line:** 1402041

**Inherits:** IAmazonExtensions

---

#### FakeGooglePlayStoreConfiguration

**Line:** 1403383

**Inherits:** IGooglePlayConfiguration

---

#### FakeGooglePlayStoreExtensions

**Line:** 1403419

**Inherits:** IGooglePlayStoreExtensions

---

#### FakePurchasing

**Line:** 1312101

---

#### FakeStore

**Line:** 1312254

**Inherits:** FakePurchasing

**Fields:**

- `_config`: IAPFakeStoreConfig
- `_pendingTransactions`: HashSet<string>

---

#### FakeUDPExtension

**Line:** 1404844

**Inherits:** IUDPExtensions

---

#### FallbackLocale

**Line:** 1327314

**Inherits:** IMetadata

**Fields:**

- `m_Locale`: Locale

---

#### FastAction

**Line:** 1346772

---

#### FaultInjectingMessageTransport

**Line:** 546786

**Inherits:** MessageTransport

**Fields:**

- `_innerTransport`: IMessageTransport
- `_errored`: bool
- `_haltedEvents`: List<object>
- `_haltedCommands`: List<object>
- `_numHaltedMessages`: int
- `_streamReadTimeoutTimer`: MetaTimer
- `_streamReadWarningTimer`: MetaTimer
- `_readWarningActive`: bool
- `_onConnectEmitted`: bool
- `_openRequested`: bool
- `_openCompleted`: bool

---

#### Feature

**Line:** 702768

**Inherits:** Systems

---

#### FeatureCollection

**Line:** 1584682

**Inherits:** IFeatureCollection

**Fields:**

- `_features`: IDictionary<Type, object>
- `_containerRevision`: int

---

#### FeatureComponent

**Line:** 729668

**Inherits:** IComponent

**Fields:**

- `Value`: string

---

#### FeatureLockUiView

**Line:** 721774

**Inherits:** UiUnityView

**Fields:**

- `Feature`: string
- `UnlockedElements`: GameObject
- `LockedElements`: GameObject
- `LockedButton`: UnityButton
- `_featureEntity`: GameEntity

---

#### FeatureUnlockedMessage

**Line:** 737622

**Inherits:** IMessage

---

#### FeedbackService

**Line:** 728309

---

#### FieldAccessException

**Line:** 22992

**Inherits:** MemberAccessException

---

#### FieldBuilder

**Line:** 269538

**Inherits:** FieldInfo

---

#### FieldInfo

**Line:** 265414

**Inherits:** MemberInfo

---

#### FieldMouseDragger

**Line:** 639365

**Fields:**

- `m_DragElement`: VisualElement
- `m_DragHotZone`: Rect

---

#### FieldOffsetAttribute

**Line:** 229323

**Inherits:** Attribute

---

#### FileDataStore

**Line:** 1501366

**Inherits:** IDataStore

---

#### FileExtensionsAttribute

**Line:** 1509321

**Inherits:** DataTypeAttribute

**Fields:**

- `_extensions`: string

---

#### FileHandleEndPoint

**Line:** 1570423

**Inherits:** EndPoint

---

#### FileInfo

**Line:** 469654

**Inherits:** FileSystemInfo

---

#### FileLoadException

**Line:** 467763

**Inherits:** IOException

---

#### FileNotFoundException

**Line:** 467823

**Inherits:** IOException

---

#### FileSourcedExternalAccountCredential

**Line:** 1370878

**Inherits:** ExternalAccountCredential

---

#### FileStream

**Line:** 470817

**Inherits:** Stream

**Fields:**

- `name`: string
- `safeHandle`: SafeFileHandle
- `isExposed`: bool
- `append_startpos`: long
- `access`: FileAccess
- `owner`: bool
- `async`: bool
- `canseek`: bool
- `anonymous`: bool
- `buf_dirty`: bool
- `buf_size`: int
- `buf_length`: int
- `buf_offset`: int
- `buf_start`: long

---

#### FileSystemBuildSource

**Line:** 595530

**Inherits:** GameConfigBuildSource

---

#### FileSystemEnumerable

**Line:** 471679

---

#### FileSystemEnumerator

**Line:** 471875

**Fields:**

- `_currentPath`: string
- `_directoryHandle`: IntPtr
- `_lastEntryFound`: bool
- `_pending`: Queue<string>
- `_current`: TResult

---

#### FileSystemInfo

**Line:** 469753

**Inherits:** MarshalByRefObject

**Fields:**

- `_fileStatus`: FileStatus
- `FullPath`: string
- `OriginalPath`: string

---

#### FileUtilImplFileSystem

**Line:** 578327

---

#### FileWebRequest

**Line:** 793763

**Inherits:** WebRequest

**Fields:**

- `m_connectionGroupName`: string
- `m_contentLength`: long
- `m_credentials`: ICredentials
- `m_fileAccess`: FileAccess
- `m_headers`: WebHeaderCollection
- `m_method`: string
- `m_preauthenticate`: bool
- `m_proxy`: IWebProxy
- `m_readerEvent`: ManualResetEvent
- `m_readPending`: bool
- `m_response`: WebResponse
- `m_stream`: Stream
- `m_syncHint`: bool
- `m_timeout`: int
- `m_uri`: Uri
- `m_writePending`: bool
- `m_writing`: bool
- `m_WriteAResult`: LazyAsyncResult
- `m_ReadAResult`: LazyAsyncResult
- `m_Aborted`: int

---

#### FileWebResponse

**Line:** 793959

**Inherits:** WebResponse

**Fields:**

- `m_closed`: bool
- `m_contentLength`: long
- `m_fileAccess`: FileAccess
- `m_headers`: WebHeaderCollection
- `m_stream`: Stream
- `m_uri`: Uri

---

#### FilmGrain

**Line:** 909396

**Inherits:** VolumeComponent

**Fields:**

- `type`: FilmGrainLookupParameter
- `intensity`: ClampedFloatParameter
- `response`: ClampedFloatParameter
- `texture`: NoInterpTextureParameter

---

#### FilmGrainLookupParameter

**Line:** 909423

**Inherits:** VolumeParameter

---

#### FilterCriteria

**Line:** 1393087

**Inherits:** IDirectResponseSchema

---

#### FilterSpec

**Line:** 1393183

**Inherits:** IDirectResponseSchema

---

#### FilterUIHintAttribute

**Line:** 1509368

**Inherits:** Attribute

---

#### FilterView

**Line:** 1393243

**Inherits:** IDirectResponseSchema

---

#### FinalBarrierComponent

**Line:** 685385

**Inherits:** IComponent

**Fields:**

- `Value`: Barrier

---

#### FinalBlitPass

**Line:** 919903

**Inherits:** ScriptableRenderPass

**Fields:**

- `m_Source`: RTHandle

---

#### FindReplaceRequest

**Line:** 1393351

**Inherits:** IDirectResponseSchema

---

#### FindReplaceResponse

**Line:** 1393483

**Inherits:** IDirectResponseSchema

---

#### FirebaseAnalyticsFormatter

**Line:** 606274

**Fields:**

- `_eventFormatters`: MetaDictionary<Type, FirebaseAnalyticsFormatter.EventFormatter>

---

#### FirebaseAnalyticsIgnoreAttribute

**Line:** 605326

**Inherits:** Attribute

---

#### FirebaseAnalyticsInternalPINVOKE

**Line:** 1573621

---

#### FirebaseAnalyticsNameAttribute

**Line:** 605336

**Inherits:** Attribute

---

#### FirebaseApp

**Line:** 1493064

**Inherits:** IDisposable

**Fields:**

- `swigCPtr`: HandleRef
- `swigCMemOwn`: bool
- `name`: string
- `AppDisposed`: EventHandler
- `appPlatform`: FirebaseAppPlatform

---

#### FirebaseAppCheckStatus

**Line:** 692751

**Inherits:** IComponent

**Fields:**

- `IsFailed`: bool

---

#### FirebaseAppCheckStatusEventSystem

**Line:** 701957

**Inherits:** ReactiveSystem

---

#### FirebaseAppCheckStatusListenerComponent

**Line:** 699661

**Inherits:** IComponent

**Fields:**

- `value`: List<IFirebaseAppCheckStatusListener>

---

#### FirebaseCrashlyticsFrame

**Line:** 1567352

**Inherits:** IDisposable

**Fields:**

- `swigCPtr`: HandleRef
- `swigCMemOwn`: bool

---

#### FirebaseException

**Line:** 1491633

**Inherits:** Exception

---

#### FirebaseFeature

**Line:** 692774

**Inherits:** Feature

---

#### FirebaseInitComponent

**Line:** 692765

**Inherits:** IComponent

---

#### FirebaseInitializeSystem

**Line:** 692819

**Inherits:** IInitializeSystem

---

#### FirebaseTrackUserPseudoIdSystem

**Line:** 692855

**Inherits:** ReactiveSystem

---

#### FirstChanceExceptionEventArgs

**Line:** 229935

**Inherits:** EventArgs

---

#### FirstLayerSettings

**Line:** 1564852

**Fields:**

- `title`: string
- `description`: string
- `additionalInfo`: string
- `resurfaceNote`: string
- `vendorListLinkTitle`: string
- `manageSettingsLinkTitle`: string
- `purposesLabel`: string
- `featuresLabel`: string
- `acceptAllButton`: string
- `denyAllButton`: string
- `saveButton`: string

---

#### FirstLayerStyleSettings

**Line:** 1565129

**Fields:**

- `layout`: UsercentricsLayout
- `headerImage`: HeaderImageSettings
- `title`: TitleSettings
- `message`: MessageSettings
- `buttonLayout`: ButtonLayout
- `backgroundColor`: string
- `cornerRadius`: float
- `overlayColor`: string
- `overlayAlpha`: float

---

#### FirstTimeUnlockComponent

**Line:** 729463

**Inherits:** IComponent

---

#### FixedBufferAttribute

**Line:** 234180

**Inherits:** Attribute

---

#### FlagPrefixAttribute

**Line:** 1597518

**Inherits:** Attribute

---

#### FlagsAttribute

**Line:** 23009

**Inherits:** Attribute

---

#### FlashGraphic

**Line:** 1506511

**Inherits:** UIBehaviour

**Fields:**

- `DecayTime`: float
- `DefaultColor`: Color
- `FlashColor`: Color
- `Target`: Graphic

---

#### FlatButton

**Line:** 735883

**Inherits:** UnityButton

**Fields:**

- `BackgroundImage`: Image
- `HasClickSfx`: bool
- `_playAnimation`: bool
- `_onClick`: Action
- `_onInactiveClick`: Action
- `_sequence`: Sequence

---

#### FlatIOBuffer

**Line:** 557730

**Inherits:** RWIOBufferBase

**Fields:**

- `_allocation`: MemoryAllocation
- `_count`: int

---

#### FloatField

**Line:** 617363

**Inherits:** TextValueField

---

#### FloatGlobalVariable

**Line:** 1321527

**Inherits:** FloatVariable

---

#### FloatParameter

**Line:** 827148

**Inherits:** VolumeParameter

---

#### FloatPlugin

**Line:** 1429634

**Inherits:** ABSTweenPlugin

---

#### FloatRangeParameter

**Line:** 827313

**Inherits:** VolumeParameter

**Fields:**

- `min`: float
- `max`: float

---

#### FloatTrackedProperty

**Line:** 1328931

**Inherits:** TrackedProperty

---

#### FloatTween

**Line:** 1358377

---

#### FloatVariable

**Line:** 1324717

**Inherits:** Variable

---

#### FlowLayoutGroup

**Line:** 1507094

**Inherits:** LayoutGroup

**Fields:**

- `_layoutHeight`: float
- `ChildForceExpandHeight`: bool
- `ChildForceExpandWidth`: bool
- `Spacing`: float

---

#### FocusChangeDirection

**Line:** 639846

**Inherits:** IDisposable

---

#### FocusController

**Line:** 639919

**Fields:**

- `m_SelectedTextElement`: TextElement
- `m_FocusedElements`: List<FocusController.FocusedElement>
- `m_LastFocusedElement`: Focusable
- `m_PendingFocusCount`: int

---

#### FocusEvent

**Line:** 635552

**Inherits:** FocusEventBase

---

#### FocusEventBase

**Line:** 635288

---

#### FocusInEvent

**Line:** 635511

**Inherits:** FocusEventBase

---

#### FocusOutEvent

**Line:** 635438

**Inherits:** FocusEventBase

---

#### Focusable

**Line:** 639754

**Inherits:** CallbackEventHandler

**Fields:**

- `m_Focusable`: bool
- `m_TabIndex`: int
- `m_DelegatesFocus`: bool
- `m_ExcludeFromFocusRing`: bool

---

#### Foldout

**Line:** 617431

**Inherits:** BindableElement

**Fields:**

- `m_Container`: VisualElement
- `m_Value`: bool
- `m_NavigationManipulator`: KeyboardNavigationManipulator

---

#### Font

**Line:** 1581043

**Inherits:** Object

---

#### FontAsset

**Line:** 1347230

**Inherits:** TextAsset

**Fields:**

- `m_SourceFontFile`: Font
- `m_AtlasPopulationMode`: AtlasPopulationMode
- `m_FamilyNameHashCode`: int
- `m_StyleNameHashCode`: int
- `m_IsMultiAtlasTexturesEnabled`: bool
- `m_GetFontFeatures`: bool
- `m_ClearDynamicDataOnBuild`: bool
- `m_UsedGlyphRects`: List<GlyphRect>
- `m_FreeGlyphRects`: List<GlyphRect>
- `m_NativeFontAsset`: IntPtr
- `m_GlyphsToRender`: List<Glyph>
- `m_GlyphsRendered`: List<Glyph>
- `m_GlyphIndexList`: List<uint>
- `m_GlyphIndexListNewlyAdded`: List<uint>

---

#### FontData

**Line:** 1352465

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `m_Font`: Font
- `m_FontSize`: int
- `m_FontStyle`: FontStyle
- `m_BestFit`: bool
- `m_MinSize`: int
- `m_MaxSize`: int
- `m_Alignment`: TextAnchor
- `m_AlignByGeometry`: bool
- `m_RichText`: bool
- `m_HorizontalOverflow`: HorizontalWrapMode
- `m_VerticalOverflow`: VerticalWrapMode
- `m_LineSpacing`: float

---

#### FontEngine

**Line:** 1557650

---

#### FontFeatureTable

**Line:** 1346846

**Fields:**

- `m_GlyphPairAdjustmentRecords`: List<GlyphPairAdjustmentRecord>

---

#### ForbiddenException

**Line:** 685036

**Inherits:** Exception

---

#### ForbiddenResponse

**Line:** 685016

---

#### ForceMetaIntegrationAttribute

**Line:** 498947

**Inherits:** Attribute

---

#### ForceSerializeByValueAttribute

**Line:** 582810

**Inherits:** Attribute

---

#### ForceUpdatePositionComponent

**Line:** 685411

**Inherits:** IComponent

**Fields:**

- `Value`: Vector2

---

#### ForeignKeyAttribute

**Line:** 1510908

**Inherits:** Attribute

---

#### ForeignKeyConstraint

**Line:** 1086822

**Inherits:** Constraint

**Fields:**

- `_childKey`: DataKey
- `_parentKey`: DataKey

---

#### ForgingFeature

**Line:** 714717

**Inherits:** Feature

---

#### FormUrlEncodedContent

**Line:** 1488230

**Inherits:** ByteArrayContent

---

#### FormValidationContext

**Line:** 572799

---

#### FormValidationResult

**Line:** 572769

---

#### Format

**Line:** 1322512

**Inherits:** FormatItem

**Fields:**

- `parent`: Placeholder
- `m_Splits`: List<Format.SplitList>
- `splitCacheChar`: char
- `splitCache`: IList<Format>

---

#### FormatCache

**Line:** 1323216

**Fields:**

- `Table`: LocalizationTable

---

#### FormatDelegate

**Line:** 1320863

**Inherits:** IFormattable

---

#### FormatDetails

**Line:** 1323266

---

#### FormatException

**Line:** 23019

**Inherits:** SystemException

---

#### FormatItem

**Line:** 1322641

**Fields:**

- `baseString`: string
- `endIndex`: int
- `SmartSettings`: SmartSettings
- `startIndex`: int
- `m_RawText`: string

---

#### FormationBuilder

**Line:** 1050683

---

#### FormationTest

**Line:** 710687

**Inherits:** MonoBehaviour

**Fields:**

- `Count`: int
- `Distance`: float

---

#### FormattableString

**Line:** 23037

**Inherits:** IFormattable

---

#### FormatterBase

**Line:** 1323561

**Inherits:** IFormatter

---

#### FormatterConverter

**Line:** 225183

**Inherits:** IFormatterConverter

---

#### FormattingErrorEventArgs

**Line:** 1320141

**Inherits:** EventArgs

---

#### FormattingException

**Line:** 1323366

**Inherits:** Exception

---

#### FormattingInfo

**Line:** 1323414

**Inherits:** IFormattingInfo

---

#### FormerlySerializedAsAttribute

**Line:** 888286

**Inherits:** Attribute

**Fields:**

- `m_oldName`: string

---

#### FrameworkName

**Line:** 775108

**Inherits:** IEquatable

**Fields:**

- `m_fullName`: string

---

#### FreeCamera

**Line:** 804377

**Inherits:** MonoBehaviour

**Fields:**

- `m_LookSpeedController`: float
- `m_LookSpeedMouse`: float
- `m_MoveSpeed`: float
- `m_MoveSpeedIncrement`: float
- `m_Turbo`: float
- `inputRotateAxisX`: float
- `inputRotateAxisY`: float
- `inputChangeSpeed`: float
- `inputVertical`: float
- `inputHorizontal`: float
- `inputYAxis`: float
- `leftShiftBoost`: bool
- `leftShift`: bool
- `fire1`: bool

---

#### FromKeyedServicesAttribute

**Line:** 1542477

**Inherits:** Attribute

---

#### FtpWebRequest

**Line:** 790933

**Inherits:** WebRequest

**Fields:**

- `_syncObject`: object
- `_authInfo`: ICredentials
- `_methodInfo`: FtpMethodInfo
- `_renameTo`: string
- `_getRequestStreamStarted`: bool
- `_getResponseStarted`: bool
- `_startTime`: DateTime
- `_timeout`: int
- `_remainingTimeout`: int
- `_contentLength`: long
- `_contentOffset`: long
- `_clientCertificates`: X509CertificateCollection
- `_passive`: bool
- `_binary`: bool
- `_connectionGroupName`: string
- `_async`: bool
- `_aborted`: bool
- `_timedOut`: bool
- `_exception`: Exception
- `_enableSsl`: bool
- ... (9 more fields)

---

#### FtpWebResponse

**Line:** 791180

**Inherits:** WebResponse

**Fields:**

- `_contentLength`: long
- `_responseUri`: Uri
- `_statusCode`: FtpStatusCode
- `_statusLine`: string
- `_ftpRequestHeaders`: WebHeaderCollection
- `_lastModified`: DateTime
- `_bannerMessage`: string
- `_welcomeMessage`: string
- `_exitMessage`: string

---

#### FullEquipCheatAction

**Line:** 1068632

**Inherits:** PlayerAction

---

#### FullGameConfig

**Line:** 591728

---

#### FullGameConfigImportResources

**Line:** 587997

---

#### FullGameConfigPatch

**Line:** 591810

---

#### FullGameConfigPatchEnvelope

**Line:** 591858

---

#### FullScreenPassRendererFeature

**Line:** 912427

**Inherits:** ScriptableRendererFeature

**Fields:**

- `fetchColorBuffer`: bool
- `requirements`: ScriptableRenderPassInput
- `passMaterial`: Material
- `passIndex`: int
- `bindDepthStencilAttachment`: bool

---

#### Func

**Line:** 1230416

---

#### FutureBool

**Line:** 1492678

---

#### FutureString

**Line:** 1492461

---

#### FutureVoid

**Line:** 1492571

---

#### Future_LongLong

**Line:** 1573196

---

#### GDPROpenView

**Line:** 738710

**Inherits:** UiUnityView

**Fields:**

- `OpenButton`: UnityButton

---

#### GDPRSingleton

**Line:** 738728

---

#### GL

**Line:** 873029

---

#### GPUResidentDrawer

**Line:** 1377428

**Fields:**

- `m_ContextIntPtr`: IntPtr
- `m_Settings`: GPUResidentDrawerSettings
- `m_GPUDrivenProcessor`: GPUDrivenProcessor
- `m_BatchersContext`: RenderersBatchersContext
- `m_Batcher`: GPUResidentBatcher
- `m_Dispatcher`: ObjectDispatcher

---

#### GUI

**Line:** 1450766

---

#### GUIContent

**Line:** 1451060

**Fields:**

- `m_Text`: string
- `m_Image`: Texture
- `m_Tooltip`: string
- `m_TextWithWhitespace`: string
- `OnTextChanged`: Action

---

#### GUILayout

**Line:** 1451171

---

#### GUILayoutOption

**Line:** 1451225

---

#### GUILayoutUtility

**Line:** 1451268

---

#### GUISettings

**Line:** 1451362

**Fields:**

- `m_DoubleClickSelectsWord`: bool
- `m_TripleClickSelectsLine`: bool
- `m_CursorColor`: Color
- `m_CursorFlashSpeed`: float
- `m_SelectionColor`: Color

---

#### GUISkin

**Line:** 1451399

**Inherits:** ScriptableObject

**Fields:**

- `m_Font`: Font
- `m_box`: GUIStyle
- `m_button`: GUIStyle
- `m_toggle`: GUIStyle
- `m_label`: GUIStyle
- `m_textField`: GUIStyle
- `m_textArea`: GUIStyle
- `m_window`: GUIStyle
- `m_horizontalSlider`: GUIStyle
- `m_horizontalSliderThumb`: GUIStyle
- `m_horizontalSliderThumbExtent`: GUIStyle
- `m_verticalSlider`: GUIStyle
- `m_verticalSliderThumb`: GUIStyle
- `m_verticalSliderThumbExtent`: GUIStyle
- `m_SliderMixed`: GUIStyle
- `m_horizontalScrollbar`: GUIStyle
- `m_horizontalScrollbarThumb`: GUIStyle
- `m_horizontalScrollbarLeftButton`: GUIStyle
- `m_horizontalScrollbarRightButton`: GUIStyle
- `m_verticalScrollbar`: GUIStyle
- ... (6 more fields)

---

#### GUIStyle

**Line:** 1451754

**Fields:**

- `m_Normal`: GUIStyleState
- `m_Hover`: GUIStyleState
- `m_Active`: GUIStyleState
- `m_Focused`: GUIStyleState
- `m_OnNormal`: GUIStyleState
- `m_OnHover`: GUIStyleState
- `m_OnActive`: GUIStyleState
- `m_OnFocused`: GUIStyleState
- `m_Border`: RectOffset
- `m_Padding`: RectOffset
- `m_Margin`: RectOffset
- `m_Overflow`: RectOffset
- `m_Name`: string

---

#### GUIStyleState

**Line:** 1451698

---

#### GUITargetAttribute

**Line:** 1452114

**Inherits:** Attribute

---

#### GUIUtility

**Line:** 1452133

---

#### GZipStream

**Line:** 789394

**Inherits:** Stream

**Fields:**

- `_deflateStream`: DeflateStream

---

#### GameAnyDestroyedEventSystem

**Line:** 701978

**Inherits:** ReactiveSystem

---

#### GameAnyDestroyedListenerComponent

**Line:** 699674

**Inherits:** IComponent

**Fields:**

- `value`: List<IGameAnyDestroyedListener>

---

#### GameAttribute

**Line:** 703705

**Inherits:** ContextAttribute

---

#### GameAudioFeature

**Line:** 705805

**Inherits:** Feature

---

#### GameBarrierComponent

**Line:** 685399

**Inherits:** IComponent

**Fields:**

- `Value`: Barrier

---

#### GameCleanupSystems

**Line:** 703714

**Inherits:** Feature

---

#### GameConfigBase

**Line:** 591035

**Inherits:** IGameConfig

---

#### GameConfigBinarySerialization

**Line:** 592120

---

#### GameConfigBuild

**Line:** 593632

**Inherits:** IMetaIntegrationConstructible

---

#### GameConfigBuildDebugOptions

**Line:** 592181

**Fields:**

- `EnableDebugPrints`: bool
- `EnableDebugDumpCheck`: bool
- `OnlyValidateBaseline`: bool

---

#### GameConfigBuildFailed

**Line:** 592160

**Inherits:** Exception

---

#### GameConfigBuildIntegration

**Line:** 594644

**Inherits:** IMetaIntegrationSingleton

---

#### GameConfigBuildLog

**Line:** 594782

**Fields:**

- `_messages`: List<GameConfigBuildMessage>
- `_numErrorsAtStartOfLocalErrorScope`: int

---

#### GameConfigBuildMessage

**Line:** 594728

**Fields:**

- `SourceInfo`: string
- `ShortSource`: string
- `SourceLocation`: string
- `LocationUrl`: string
- `ItemId`: string
- `VariantId`: string
- `Level`: GameConfigLogLevel
- `Message`: string
- `Exception`: string
- `CallerFileName`: string
- `CallerMemberName`: string
- `CallerLineNumber`: int

---

#### GameConfigBuildParameters

**Line:** 594897

**Inherits:** IMetaIntegration

**Fields:**

- `DefaultSource`: GameConfigBuildSource

---

#### GameConfigBuildReport

**Line:** 595134

---

#### GameConfigBuildSource

**Line:** 595426

---

#### GameConfigBuildSourceMetadata

**Line:** 596164

---

#### GameConfigBuildState

**Line:** 592812

**Fields:**

- `_builder`: GameConfigBuildState<TConfig>

---

#### GameConfigBuildSummary

**Line:** 595010

---

#### GameConfigBuildTemplate

**Line:** 594562

---

#### GameConfigEntryAttribute

**Line:** 587088

**Inherits:** Attribute

---

#### GameConfigEntryInfo

**Line:** 598495

---

#### GameConfigEntryPatch

**Line:** 597620

---

#### GameConfigEntryTransformAttribute

**Line:** 587103

**Inherits:** Attribute

---

#### GameConfigFactory

**Line:** 591885

**Inherits:** IMetaIntegrationSingleton

---

#### GameConfigImportExceptions

**Line:** 590821

---

#### GameConfigImportParams

**Line:** 596946

---

#### GameConfigImportResources

**Line:** 596975

**Fields:**

- `DeduplicationBaseline`: IGameConfig
- `DeduplicationSingleVariantSpecializations`: MetaDictionary<ExperimentVariantPair, IGameConfig>

---

#### GameConfigImporter

**Line:** 590623

**Fields:**

- `_importParams`: GameConfigImportParams

---

#### GameConfigKeyValue

**Line:** 588359

---

#### GameConfigLibrary

**Line:** 588842

**Fields:**

- `_aliasToRealKey`: MetaDictionary<object, object>

---

#### GameConfigLibraryDeduplicationStorage

**Line:** 596511

**Fields:**

- `NumBaselineItems`: int

---

#### GameConfigLibraryPatch

**Line:** 597778

**Fields:**

- `_replacedItems`: BuiltinGameConfigLibrary<TKey, TInfo>
- `_appendedItems`: BuiltinGameConfigLibrary<TKey, TInfo>

---

#### GameConfigLibraryPatchedItemEntry

**Line:** 596735

---

#### GameConfigMetaData

**Line:** 591606

**Fields:**

- `BuildSourceMetadata`: MetaDictionary<string, GameConfigBuildSourceMetadata>

---

#### GameConfigOutputItemParser

**Line:** 597033

---

#### GameConfigParseKeyValuePipelineConfig

**Line:** 597240

---

#### GameConfigParseLibraryPipelineConfig

**Line:** 597227

---

#### GameConfigPatch

**Line:** 597454

**Fields:**

- `_entryPatches`: Dictionary<string, GameConfigEntryPatch>

---

#### GameConfigPatchEnvelope

**Line:** 597507

**Fields:**

- `_serializedEntryPatches`: MetaDictionary<string, byte[]>

---

#### GameConfigPatchUtil

**Line:** 597541

**Fields:**

- `_baseResolver`: IGameConfigDataResolver
- `_entryPatches`: MetaDictionary<string, GameConfigEntryPatch>

---

#### GameConfigRepository

**Line:** 598667

**Fields:**

- `_gameConfigTypes`: Dictionary<Type, GameConfigTypeInfo>

---

#### GameConfigRepositoryConfig

**Line:** 598591

---

#### GameConfigRepositoryData

**Line:** 598655

**Inherits:** IGeneratedData

---

#### GameConfigSourceFetcherConfigCore

**Line:** 596121

**Inherits:** IGameConfigSourceFetcherConfig

**Fields:**

- `GoogleCredentialsJson`: string
- `GoogleCredentialsFilePath`: string
- `LocalFileSourcesPath`: string

---

#### GameConfigSourceFetcherProvider

**Line:** 595955

---

#### GameConfigSourceInfo

**Line:** 598723

---

#### GameConfigSourceLocation

**Line:** 598824

---

#### GameConfigSourceMapping

**Line:** 598921

---

#### GameConfigSpecializationPatches

**Line:** 599029

---

#### GameConfigSpreadsheetLocation

**Line:** 598881

**Inherits:** GameConfigSourceLocation

---

#### GameConfigSpreadsheetReader

**Line:** 599264

**Fields:**

- `Children`: MetaDictionary<GameConfigSyntaxTree.NodeMemberId, GameConfigSpreadsheetReader.PathNode>

---

#### GameConfigSpreadsheetSourceInfo

**Line:** 598744

**Inherits:** GameConfigSourceInfo

---

#### GameConfigStructurePatch

**Line:** 598304

**Fields:**

- `_replacementValues`: TStructure
- `_replacedMemberTagIds`: OrderedSet<int>

---

#### GameConfigSyntaxAdapterAttribute

**Line:** 587173

**Inherits:** Attribute

---

#### GameConfigSyntaxTree

**Line:** 599763

---

#### GameConfigTypeInfo

**Line:** 598454

---

#### GameConfigValidationMessage

**Line:** 595252

---

#### GameConfigValidationResult

**Line:** 594950

**Fields:**

- `_sourceMappingScope`: List<GameConfigSourceMapping>
- `_variantScope`: string

---

#### GameContext

**Line:** 691048

**Inherits:** Context

**Fields:**

- `_nextId`: long

---

#### GameDestroySystem

**Line:** 686829

**Inherits:** ReactiveSystem

---

#### GameDestroyedEventSystem

**Line:** 702001

**Inherits:** ReactiveSystem

---

#### GameDestroyedListenerComponent

**Line:** 699687

**Inherits:** IComponent

**Fields:**

- `value`: List<IGameDestroyedListener>

---

#### GameEngineRuntimeInfo

**Line:** 572210

---

#### GameEntity

**Line:** 687977

**Inherits:** Entity

---

#### GameEntityRef

**Line:** 687947

**Inherits:** EntityRef

---

#### GameEntityRefComponent

**Line:** 687681

**Inherits:** IComponent

**Fields:**

- `Value`: GameEntityRef

---

#### GameEntityRefEventSystem

**Line:** 702022

**Inherits:** ReactiveSystem

---

#### GameEntityRefListenerComponent

**Line:** 699700

**Inherits:** IComponent

**Fields:**

- `value`: List<IGameEntityRefListener>

---

#### GameEntityRefRemovedEventSystem

**Line:** 702043

**Inherits:** ReactiveSystem

---

#### GameEntityRefRemovedListenerComponent

**Line:** 699713

**Inherits:** IComponent

**Fields:**

- `value`: List<IGameEntityRefRemovedListener>

---

#### GameEntityRefsComponent

**Line:** 687696

**Inherits:** IComponent

**Fields:**

- `Value`: List<GameEntityRef>

---

#### GameEntityRefsEventSystem

**Line:** 702064

**Inherits:** ReactiveSystem

---

#### GameEntityRefsListenerComponent

**Line:** 699726

**Inherits:** IComponent

**Fields:**

- `value`: List<IGameEntityRefsListener>

---

#### GameEntityRefsRemovedEventSystem

**Line:** 702085

**Inherits:** ReactiveSystem

---

#### GameEntityRefsRemovedListenerComponent

**Line:** 699739

**Inherits:** IComponent

**Fields:**

- `value`: List<IGameEntityRefsRemovedListener>

---

#### GameEventSystems

**Line:** 700154

**Inherits:** Feature

---

#### GameInitializeFeature

**Line:** 684158

**Inherits:** Feature

---

#### GameMatcher

**Line:** 702780

---

#### GameObject

**Line:** 882795

**Inherits:** Object

---

#### GameObjectLinkComponent

**Line:** 739346

**Inherits:** IComponent

**Fields:**

- `Value`: GameObject

---

#### GameObjectLocalizer

**Line:** 1327795

**Inherits:** MonoBehaviour

**Fields:**

- `m_TrackedObjects`: List<TrackedObject>
- `m_CurrentLocale`: Locale
- `m_IgnoreChange`: bool

---

#### GamePauseAction

**Line:** 1056818

**Inherits:** PlayerAction

---

#### GameServerEndpointResult

**Line:** 549690

**Fields:**

- `LegacyHostname`: string
- `LegacyGatewaysByPort`: MetaDictionary<int, SocketProbeResult>
- `GatewaysByHost`: MetaDictionary<string, SocketProbeResult>

---

#### GameSystems

**Line:** 739159

**Inherits:** Feature

---

#### GameSystemsCreateSystem

**Line:** 684276

**Inherits:** ReactiveSystem

---

#### GameTickMessage

**Line:** 721964

**Inherits:** IMessage

---

#### GameUnPauseAction

**Line:** 1056831

**Inherits:** PlayerAction

---

#### GameUnityView

**Line:** 697133

**Inherits:** UnityView

---

#### GameUnityViewProxy

**Line:** 697144

**Inherits:** UnityViewProxy

---

#### Gauge

**Line:** 1422174

---

#### GdprSettingsView

**Line:** 729210

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton

---

#### GemPackUiView

**Line:** 730158

**Inherits:** UiUnityView

**Fields:**

- `Icon`: Image
- `Title`: TMP_Text
- `BuyButton`: UnityButton
- `PriceText`: TMP_Text
- `_pack`: GameEntity

---

#### GemPackViewCreateSystem

**Line:** 730146

**Inherits:** ShopViewEntryCreateSystem

---

#### GemsChangeMessage

**Line:** 711773

**Inherits:** CurrencyChangeMessage

---

#### GenderChangeAction

**Line:** 1052001

**Inherits:** PlayerAction

---

#### GeneralDigest

**Line:** 1519632

**Inherits:** IDigest

**Fields:**

- `xBufOff`: int
- `byteCount`: long

---

#### GeneralLocalizer

**Line:** 720984

**Inherits:** LocalizerBase

---

#### GeneralStyleSettings

**Line:** 1564301

**Fields:**

- `androidDisableSystemBackButton`: bool
- `androidStatusBarColor`: string
- `androidWindowFullscreen`: bool
- `textColor`: string
- `layerBackgroundColor`: string
- `layerBackgroundSecondaryColor`: string
- `linkColor`: string
- `tabColor`: string
- `bordersColor`: string
- `toggleStyleSettings`: ToggleStyleSettings
- `logoImageUrl`: string
- `links`: LegalLinksSettings

---

#### GenerateHLSL

**Line:** 821476

**Inherits:** Attribute

**Fields:**

- `packingRules`: PackingRules
- `containsPackedFields`: bool
- `needAccessors`: bool
- `needSetters`: bool
- `needParamDebug`: bool
- `paramDefinesStart`: int
- `omitStructDeclaration`: bool
- `generateCBuffer`: bool
- `constantRegister`: int
- `sourcePath`: string

---

#### GeneratePropertyBagsForTypesQualifiedWithAttribute

**Line:** 1458046

**Inherits:** Attribute

---

#### GenerateTestsForBurstCompatibilityAttribute

**Line:** 1184663

**Inherits:** Attribute

**Fields:**

- `RequiredUnityDefine`: string

---

#### GeneratedClientBuildData

**Line:** 704887

**Inherits:** ClientBuildData

---

#### GeneratedCodeAttribute

**Line:** 777385

**Inherits:** Attribute

---

#### GenericIdentity

**Line:** 220294

**Inherits:** ClaimsIdentity

---

#### GenericPool

**Line:** 890316

---

#### GenericPopupMessageView

**Line:** 728979

**Inherits:** MonoBehaviour

**Fields:**

- `TitleText`: TMP_Text
- `BodyText`: TMP_Text
- `ButtonText`: TMP_Text
- `CloseButton`: UnityButton
- `Container`: RectTransform
- `_onClose`: Action

---

#### GenericPrincipal

**Line:** 220367

**Inherits:** ClaimsPrincipal

**Fields:**

- `m_identity`: IIdentity

---

#### GenericStack

**Line:** 834966

**Inherits:** Stack

---

#### GenericTypeParameterBuilder

**Line:** 269585

**Inherits:** TypeInfo

---

#### GenericValidationException

**Line:** 1545002

**Inherits:** IAPSecurityException

---

#### GeolocationRuleset

**Line:** 1565031

**Fields:**

- `activeSettingsId`: string
- `bannerRequiredAtLocation`: bool

---

#### GeometryChangedEvent

**Line:** 635987

**Inherits:** EventBase

---

#### GeometryUtility

**Line:** 872031

---

#### GetAnalyticsEventKeywordsFunc

**Line:** 605451

**Inherits:** MulticastDelegate

---

#### GetBadWordListResponse

**Line:** 1528038

**Inherits:** IEquatable

---

#### GetChatRoomSettingsRequest

**Line:** 1527625

**Inherits:** IEquatable

---

#### GetChatRoomSettingsResponse

**Line:** 1527701

**Inherits:** IEquatable

---

#### GetChatRoomsResponse

**Line:** 1527777

**Inherits:** IEquatable

---

#### GetIndexBinder

**Line:** 1300772

**Inherits:** DynamicMetaObjectBinder

---

#### GetModerationScoresRequest

**Line:** 1528657

**Inherits:** IEquatable

---

#### GetModerationScoresResponse

**Line:** 1528733

**Inherits:** IEquatable

---

#### GetPlayerInfoRequest

**Line:** 1074118

**Inherits:** MetaRequest

---

#### GetPlayerInfoResponse

**Line:** 1074146

**Inherits:** MetaResponse

---

#### GetSpreadsheetByDataFilterRequest

**Line:** 1393567

**Inherits:** IDirectResponseSchema

---

#### GetTokenRequest

**Line:** 1526197

**Inherits:** IEquatable

---

#### GetTokenResponse

**Line:** 1526273

**Inherits:** IEquatable

---

#### GetUserSummaryResponse

**Line:** 1528961

**Inherits:** IEquatable

---

#### GetUsersResponse

**Line:** 1526610

**Inherits:** IEquatable

---

#### GetWhitelistResponse

**Line:** 1528190

**Inherits:** IEquatable

---

#### Gizmos

**Line:** 872505

---

#### GlobalLeaderboardPlayerEntryView

**Line:** 716194

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerRank`: TMP_Text
- `PlayerRankIcon`: Image
- `Background`: UnityUiElement
- `PlayerMiniProfileUiView`: PlayerMiniProfileUiView
- `_profile`: PlayerLeaderboardEntry

---

#### GlobalLeaderboardUiView

**Line:** 716261

**Inherits:** UiUnityView

**Fields:**

- `EntryParent`: Transform
- `EntryPrefab`: GlobalLeaderboardPlayerEntryView
- `Loading`: GameObject
- `ServerText`: TMP_Text
- `cts`: CancellationTokenSource

---

#### GlobalOptions

**Line:** 1061984

**Inherits:** IMetaplayCoreOptionsProvider

---

#### GlobalVariable

**Line:** 1321511

---

#### GlobalVariablesGroup

**Line:** 1321500

**Inherits:** VariablesGroupAsset

---

#### GlobalVariablesSource

**Line:** 1321700

**Inherits:** PersistentVariablesSource

---

#### Glyph

**Line:** 1557488

**Fields:**

- `m_Index`: uint
- `m_Metrics`: GlyphMetrics
- `m_GlyphRect`: GlyphRect
- `m_Scale`: float
- `m_AtlasIndex`: int
- `m_ClassDefinitionType`: GlyphClassDefinitionType

---

#### GoogleApiException

**Line:** 1494771

**Inherits:** Exception

---

#### GoogleAssertionTokenRequest

**Line:** 1375008

**Inherits:** TokenRequest

---

#### GoogleAuthorizationCodeFlow

**Line:** 1376318

**Inherits:** AuthorizationCodeFlow

---

#### GoogleAuthorizationCodeRequestUrl

**Line:** 1375033

**Inherits:** AuthorizationCodeRequestUrl

---

#### GoogleClientSecrets

**Line:** 1371041

---

#### GoogleCredential

**Line:** 1371188

**Inherits:** ICredential

---

#### GoogleJsonWebSignature

**Line:** 1367682

---

#### GooglePlay

**Line:** 1403474

---

#### GooglePlayReceipt

**Line:** 1545049

**Inherits:** IPurchaseReceipt

---

#### GoogleProductMetadata

**Line:** 1404092

**Inherits:** ProductMetadata

---

#### GoogleSheetBuildSource

**Line:** 595461

**Inherits:** GameConfigBuildSource

---

#### GoogleSheetBuildSourceMetadata

**Line:** 596174

**Inherits:** GameConfigBuildSourceMetadata

---

#### GoogleSheetConnection

**Line:** 729682

**Inherits:** ScriptableObject

**Fields:**

- `SpreadsheetId`: string

---

#### GoogleSheetSourceInfo

**Line:** 598792

**Inherits:** GameConfigSpreadsheetSourceInfo

---

#### GoogleSignInWrapper

**Line:** 733567

**Inherits:** Singleton

---

#### GoogleWebAuthorizationBroker

**Line:** 1371429

---

#### GotoExpression

**Line:** 1287373

**Inherits:** Expression

---

#### Gradient

**Line:** 879008

**Inherits:** IEquatable

**Fields:**

- `m_RequiresNativeCleanup`: bool

---

#### GradientRule

**Line:** 1393615

**Inherits:** IDirectResponseSchema

---

#### Graphic

**Line:** 1352625

**Inherits:** UIBehaviour

**Fields:**

- `m_Material`: Material
- `m_Color`: Color
- `m_SkipLayoutUpdate`: bool
- `m_SkipMaterialUpdate`: bool
- `m_RaycastTarget`: bool
- `m_RaycastTargetCache`: bool
- `m_RaycastPadding`: Vector4
- `m_RectTransform`: RectTransform
- `m_CanvasRenderer`: CanvasRenderer
- `m_Canvas`: Canvas
- `m_VertsDirty`: bool
- `m_MaterialDirty`: bool
- `m_OnDirtyLayoutCallback`: UnityAction
- `m_OnDirtyVertsCallback`: UnityAction
- `m_OnDirtyMaterialCallback`: UnityAction
- `m_CachedMesh`: Mesh

---

#### GraphicRaycaster

**Line:** 1352903

**Inherits:** BaseRaycaster

**Fields:**

- `m_IgnoreReversedGraphics`: bool
- `m_BlockingMask`: LayerMask
- `m_Canvas`: Canvas
- `m_RaycastResults`: List<Graphic>

---

#### GraphicRegistry

**Line:** 1352974

---

#### Graphics

**Line:** 872881

---

#### GraphicsBuffer

**Line:** 874729

**Inherits:** IDisposable

---

#### GraphicsFormatUtility

**Line:** 899583

---

#### GraphicsSettings

**Line:** 892586

**Inherits:** Object

---

#### GregorianCalendar

**Line:** 273112

**Inherits:** Calendar

---

#### GridCoordinate

**Line:** 1393675

**Inherits:** IDirectResponseSchema

---

#### GridData

**Line:** 1393735

**Inherits:** IDirectResponseSchema

---

#### GridLayoutGroup

**Line:** 1354661

**Inherits:** LayoutGroup

**Fields:**

- `m_CellSize`: Vector2
- `m_Spacing`: Vector2
- `m_ConstraintCount`: int

---

#### GridProperties

**Line:** 1393819

**Inherits:** IDirectResponseSchema

---

#### GridRange

**Line:** 1393927

**Inherits:** IDirectResponseSchema

---

#### Group

**Line:** 1546467

**Fields:**

- `OnEntityAdded`: GroupChanged<TEntity>
- `OnEntityRemoved`: GroupChanged<TEntity>
- `OnEntityUpdated`: GroupUpdated<TEntity>
- `_singleEntityCache`: TEntity
- `_toStringCache`: string

---

#### GroupBox

**Line:** 617733

**Inherits:** BindableElement

**Fields:**

- `m_TitleLabel`: Label

---

#### GroupChanged

**Line:** 1548311

---

#### GroupCollection

**Line:** 775577

**Inherits:** IList

---

#### GroupSingleEntityException

**Line:** 1547544

---

#### GroupUpdated

**Line:** 1548349

---

#### GuestCredentials

**Line:** 1305988

**Fields:**

- `DeviceId`: string
- `AuthToken`: string
- `PlayerId`: EntityId

---

#### GuestCredentialsSerializer

**Line:** 1306015

**Fields:**

- `DeviceId`: string
- `AuthToken`: string
- `PlayerId`: EntityId

---

#### GuidAttribute

**Line:** 229199

**Inherits:** Attribute

---

#### GuidComponent

**Line:** 713562

**Inherits:** IComponent

**Fields:**

- `Value`: Guid

---

#### GuidConverter

**Line:** 782029

**Inherits:** TypeConverter

---

#### HDRACESPresetParameter

**Line:** 909801

**Inherits:** VolumeParameter

---

#### HDROutputSettings

**Line:** 873236

**Fields:**

- `m_DisplayIndex`: int

---

#### HLSLArray

**Line:** 821519

**Inherits:** Attribute

**Fields:**

- `arraySize`: int
- `elementType`: Type

---

#### HMAC

**Line:** 218243

**Inherits:** KeyedHashAlgorithm

**Fields:**

- `blockSizeValue`: int
- `m_hashing`: bool

---

#### HMACMD5

**Line:** 218299

**Inherits:** HMAC

---

#### HMACRIPEMD160

**Line:** 218312

**Inherits:** HMAC

---

#### HMACSHA1

**Line:** 218325

**Inherits:** HMAC

---

#### HMACSHA256

**Line:** 218341

**Inherits:** HMAC

---

#### HMACSHA384

**Line:** 218354

**Inherits:** HMAC

**Fields:**

- `m_useLegacyBlockSize`: bool

---

#### HMACSHA512

**Line:** 218376

**Inherits:** HMAC

**Fields:**

- `m_useLegacyBlockSize`: bool

---

#### HableCurve

**Line:** 825217

---

#### HammersChangeMessage

**Line:** 711783

**Inherits:** CurrencyChangeMessage

---

#### HandleExceptionArgs

**Line:** 1497602

---

#### HandleManager

**Line:** 1443822

**Inherits:** SRMonoBehaviour

**Fields:**

- `_hasSet`: bool
- `BottomHandle`: GameObject
- `BottomLeftHandle`: GameObject
- `BottomRightHandle`: GameObject
- `DefaultAlignment`: PinAlignment
- `LeftHandle`: GameObject
- `RightHandle`: GameObject
- `TopHandle`: GameObject
- `TopLeftHandle`: GameObject
- `TopRightHandle`: GameObject

---

#### HandleProcessCorruptedStateExceptionsAttribute

**Line:** 229940

**Inherits:** Attribute

---

#### HandleUnsuccessfulResponseArgs

**Line:** 1497692

---

#### Handshake

**Line:** 555479

---

#### HandshakeRequestMessage

**Line:** 1568818

**Inherits:** HubMessage

---

#### HandshakeResponseMessage

**Line:** 1568847

**Inherits:** HubMessage

---

#### HapticClip

**Line:** 1579692

**Inherits:** ScriptableObject

**Fields:**

- `gamepadRumble`: GamepadRumble

---

#### HapticFeedbackComponent

**Line:** 692875

**Inherits:** IComponent

**Fields:**

- `Value`: HapticFeedback

---

#### HapticFeedbackFeature

**Line:** 692917

**Inherits:** Feature

---

#### HapticFeedbackSystem

**Line:** 692926

**Inherits:** ReactiveSystem

---

#### HapticReceiver

**Line:** 1579952

**Inherits:** MonoBehaviour

**Fields:**

- `_outputLevel`: float
- `_hapticsEnabled`: bool

---

#### HapticSource

**Line:** 1580025

**Inherits:** MonoBehaviour

**Fields:**

- `clip`: HapticClip
- `priority`: int
- `seekTime`: float
- `_loop`: bool
- `_level`: float
- `_frequencyShift`: float

---

#### HapticsMuteSaveSystem

**Line:** 692950

**Inherits:** ReactiveSystem

---

#### HapticsSettingsView

**Line:** 729228

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton
- `Toggle`: ColoredToggle
- `_audioListener`: AudioEntity

---

#### HardcodedClientDrivenIAPClientDummyDelegate

**Line:** 1312523

**Inherits:** ClientDrivenIAPClientDelegate

---

#### HardcodedClientDrivenIAPSharedDummyDelegate

**Line:** 584068

**Inherits:** ClientDrivenIAPSharedDelegate

---

#### Hash128Field

**Line:** 617815

**Inherits:** TextInputBaseField

---

#### HashAlgorithm

**Line:** 217694

**Inherits:** IDisposable

**Fields:**

- `_disposed`: bool
- `HashSizeValue`: int
- `State`: int

---

#### HashSet

**Line:** 1301984

**Fields:**

- `_count`: int
- `_lastIndex`: int
- `_freeList`: int
- `_comparer`: IEqualityComparer<T>
- `_version`: int
- `_siInfo`: SerializationInfo

---

#### HashSetPropertyBag

**Line:** 1463349

---

#### Hashtable

**Line:** 277932

**Inherits:** IDictionary

**Fields:**

- `_count`: int
- `_occupancy`: int
- `_loadsize`: int
- `_loadFactor`: float
- `_version`: int
- `_isWriterInProgress`: bool
- `_keys`: ICollection
- `_values`: ICollection
- `_keycomparer`: IEqualityComparer
- `_syncRoot`: object

---

#### Header

**Line:** 224058

---

#### HeaderAttribute

**Line:** 880823

**Inherits:** PropertyAttribute

---

#### HeaderHandler

**Line:** 224063

**Inherits:** MulticastDelegate

---

#### HeaderImageSettings

**Line:** 1565166

**Fields:**

- `imageType`: HeaderImageType
- `imageUrl`: string
- `alignment`: SectionAlignment
- `height`: float

---

#### HelmetEquipmentItem

**Line:** 713659

**Inherits:** EquipmentItem

**Fields:**

- `HpBarOffset`: float

---

#### HelpBox

**Line:** 617901

**Inherits:** VisualElement

**Fields:**

- `m_HelpBoxMessageType`: HelpBoxMessageType
- `m_Icon`: VisualElement
- `m_IconClass`: string
- `m_Label`: Label

---

#### HelpURLAttribute

**Line:** 881659

**Inherits:** Attribute

---

#### HideInCallstackAttribute

**Line:** 881653

**Inherits:** Attribute

---

#### HideInDebugUIAttribute

**Line:** 807887

**Inherits:** Attribute

---

#### HideInInspector

**Line:** 881642

**Inherits:** Attribute

---

#### Hierarchy

**Line:** 1562014

**Inherits:** IDisposable

**Fields:**

- `m_Ptr`: IntPtr

---

#### HierarchyCommandList

**Line:** 1562218

**Inherits:** IDisposable

**Fields:**

- `m_Ptr`: IntPtr

---

#### HierarchyFlattened

**Line:** 1562290

**Inherits:** IDisposable

**Fields:**

- `m_Ptr`: IntPtr
- `m_NodesPtr`: IntPtr
- `m_NodesCount`: int
- `m_Version`: int

---

#### HierarchyNodeTypeHandlerBase

**Line:** 1561623

---

#### HierarchySearchQueryDescriptor

**Line:** 1562772

---

#### HierarchyViewModel

**Line:** 1562910

**Inherits:** IDisposable

**Fields:**

- `m_Ptr`: IntPtr
- `m_NodesPtr`: IntPtr
- `m_NodesCount`: int
- `m_Version`: int

---

#### HijriCalendar

**Line:** 273347

**Inherits:** Calendar

**Fields:**

- `m_HijriAdvance`: int

---

#### Histogram

**Line:** 1422252

---

#### HistogramChartSpec

**Line:** 1394011

**Inherits:** IDirectResponseSchema

---

#### HistogramRule

**Line:** 1394095

**Inherits:** IDirectResponseSchema

---

#### HistogramSeries

**Line:** 1394155

**Inherits:** IDirectResponseSchema

---

#### HitComponent

**Line:** 709120

**Inherits:** IComponent

---

#### HitEventSystem

**Line:** 702106

**Inherits:** ReactiveSystem

---

#### HitListenerComponent

**Line:** 699752

**Inherits:** IComponent

**Fields:**

- `value`: List<IHitListener>

---

#### HitSfxContainer

**Line:** 705733

**Fields:**

- `AttackSfx`: AttackSfx
- `Volume`: float

---

#### HoldDownButton

**Line:** 735910

**Inherits:** UnityButton

**Fields:**

- `HoldDuration`: float
- `Repeating`: bool
- `RepeatCount`: int
- `_holdTimer`: Timer
- `_currentRepeat`: int

---

#### HorizontalLayoutGroup

**Line:** 1354744

**Inherits:** HorizontalOrVerticalLayoutGroup

---

#### HorizontalOrVerticalLayoutGroup

**Line:** 1354766

**Inherits:** LayoutGroup

**Fields:**

- `m_Spacing`: float
- `m_ChildForceExpandWidth`: bool
- `m_ChildForceExpandHeight`: bool
- `m_ChildControlWidth`: bool
- `m_ChildControlHeight`: bool
- `m_ChildScaleWidth`: bool
- `m_ChildScaleHeight`: bool
- `m_ReverseArrangement`: bool

---

#### HpBarView

**Line:** 709802

**Inherits:** GameUnityView

**Fields:**

- `HpBar`: Renderer
- `AlwaysDisplayed`: bool
- `_fill`: float
- `_mpb`: Material
- `_fillTween`: Tweener

---

#### HpComponent

**Line:** 709130

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### HpEventSystem

**Line:** 702127

**Inherits:** ReactiveSystem

---

#### HpListenerComponent

**Line:** 699765

**Inherits:** IComponent

**Fields:**

- `value`: List<IHpListener>

---

#### HpView

**Line:** 709852

**Inherits:** GameUnityView

**Fields:**

- `HpLabel`: TMP_Text

---

#### HtmlEncoder

**Line:** 1521887

**Inherits:** TextEncoder

---

#### HttpBlobProvider

**Line:** 587409

**Inherits:** IBlobProvider

**Fields:**

- `_httpClient`: MetaHttpClient
- `_primaryBaseUrl`: string
- `_secondaryBaseUrlMaybe`: string
- `_uriSuffix`: string

---

#### HttpClient

**Line:** 1488294

**Inherits:** HttpMessageInvoker

**Fields:**

- `base_address`: Uri
- `cts`: CancellationTokenSource
- `disposed`: bool
- `headers`: HttpRequestHeaders
- `buffer_size`: long
- `timeout`: TimeSpan

---

#### HttpClientFactory

**Line:** 1497336

**Inherits:** IHttpClientFactory

---

#### HttpClientFromMessageHandlerFactory

**Line:** 1497464

**Inherits:** IHttpClientFactory

---

#### HttpClientHandler

**Line:** 1487850

**Inherits:** HttpMessageHandler

**Fields:**

- `_clientCertificateOptions`: ClientCertificateOption

---

#### HttpConnection

**Line:** 1482540

**Inherits:** ConnectionContext

**Fields:**

- `_started`: bool
- `_disposed`: bool
- `_hasInherentKeepAlive`: bool
- `_transport`: ITransport
- `_connectionId`: string

---

#### HttpConnectionFactory

**Line:** 1482706

**Inherits:** IConnectionFactory

---

#### HttpConnectionOptions

**Line:** 1482728

**Fields:**

- `_headers`: IDictionary<string, string>
- `_clientCertificates`: X509CertificateCollection
- `_cookies`: CookieContainer
- `_credentials`: ICredentials
- `_proxy`: IWebProxy
- `_useDefaultCredentials`: Nullable<bool>
- `_webSocketConfiguration`: Action<ClientWebSocketOptions>
- `_transportPipeOptions`: PipeOptions
- `_appPipeOptions`: PipeOptions
- `_transportMaxBufferSize`: long
- `_applicationMaxBufferSize`: long

---

#### HttpContent

**Line:** 1488512

**Inherits:** IDisposable

**Fields:**

- `stream`: Stream
- `disposed`: bool
- `headers`: HttpContentHeaders

---

#### HttpContentHeaders

**Line:** 1489827

**Inherits:** HttpHeaders

---

#### HttpContinueDelegate

**Line:** 791868

**Inherits:** MulticastDelegate

---

#### HttpHeaderValueCollection

**Line:** 1489921

**Fields:**

- `invalidValues`: List<string>

---

#### HttpHeaders

**Line:** 1490139

**Inherits:** IEnumerable

---

#### HttpListener

**Line:** 794983

**Inherits:** IDisposable

**Fields:**

- `tlsProvider`: MonoTlsProvider
- `tlsSettings`: MonoTlsSettings
- `certificate`: X509Certificate
- `auth_schemes`: AuthenticationSchemes
- `prefixes`: HttpListenerPrefixCollection
- `auth_selector`: AuthenticationSchemeSelector
- `realm`: string
- `ignore_write_exceptions`: bool
- `listening`: bool
- `disposed`: bool
- `registry`: Hashtable
- `ctx_queue`: ArrayList
- `wait_queue`: ArrayList
- `connections`: Hashtable
- `defaultServiceNames`: ServiceNameStore
- `extendedProtectionPolicy`: ExtendedProtectionPolicy

---

#### HttpListenerBasicIdentity

**Line:** 795088

**Inherits:** GenericIdentity

**Fields:**

- `password`: string

---

#### HttpListenerContext

**Line:** 795100

**Fields:**

- `request`: HttpListenerRequest
- `response`: HttpListenerResponse
- `user`: IPrincipal
- `cnc`: HttpConnection
- `error`: string
- `err_status`: int

---

#### HttpListenerException

**Line:** 791516

**Inherits:** Win32Exception

---

#### HttpListenerPrefixCollection

**Line:** 795156

**Inherits:** ICollection

**Fields:**

- `prefixes`: List<string>
- `listener`: HttpListener

---

#### HttpListenerRequest

**Line:** 795200

**Fields:**

- `content_length`: long
- `cl_set`: bool
- `cookies`: CookieCollection
- `headers`: WebHeaderCollection
- `method`: string
- `input_stream`: Stream
- `version`: Version
- `query_string`: NameValueCollection
- `raw_url`: string
- `url`: Uri
- `referrer`: Uri
- `context`: HttpListenerContext
- `is_chunked`: bool
- `ka_set`: bool
- `keep_alive`: bool

---

#### HttpListenerResponse

**Line:** 795303

**Inherits:** IDisposable

**Fields:**

- `disposed`: bool
- `content_encoding`: Encoding
- `content_length`: long
- `cl_set`: bool
- `content_type`: string
- `cookies`: CookieCollection
- `headers`: WebHeaderCollection
- `keep_alive`: bool
- `output_stream`: ResponseStream
- `version`: Version
- `location`: string
- `status_code`: int
- `status_description`: string
- `chunked`: bool
- `context`: HttpListenerContext
- `force_close_chunked`: bool

---

#### HttpMessageHandler

**Line:** 1488590

**Inherits:** IDisposable

---

#### HttpMessageInvoker

**Line:** 1488608

**Inherits:** IDisposable

---

#### HttpMethod

**Line:** 1488630

**Inherits:** IEquatable

---

#### HttpRequestException

**Line:** 1488693

**Inherits:** Exception

---

#### HttpRequestHeaders

**Line:** 1490327

**Inherits:** HttpHeaders

**Fields:**

- `expectContinue`: Nullable<bool>

---

#### HttpRequestMessage

**Line:** 1488708

**Inherits:** IDisposable

**Fields:**

- `headers`: HttpRequestHeaders
- `method`: HttpMethod
- `version`: Version
- `properties`: Dictionary<string, object>
- `uri`: Uri
- `is_used`: bool
- `disposed`: bool

---

#### HttpRequestProbeResult

**Line:** 549655

---

#### HttpRequestProbeStatus

**Line:** 549587

---

#### HttpResponseHeaders

**Line:** 1490410

**Inherits:** HttpHeaders

---

#### HttpResponseMessage

**Line:** 1488786

**Inherits:** IDisposable

**Fields:**

- `headers`: HttpResponseHeaders
- `reasonPhrase`: string
- `statusCode`: HttpStatusCode
- `version`: Version
- `disposed`: bool

---

#### HttpVersion

**Line:** 790088

---

#### HttpWebRequest

**Line:** 795693

**Inherits:** WebRequest

**Fields:**

- `requestUri`: Uri
- `actualUri`: Uri
- `hostChanged`: bool
- `allowAutoRedirect`: bool
- `allowBuffering`: bool
- `certificates`: X509CertificateCollection
- `connectionGroup`: string
- `haveContentLength`: bool
- `contentLength`: long
- `continueDelegate`: HttpContinueDelegate
- `cookieContainer`: CookieContainer
- `credentials`: ICredentials
- `haveResponse`: bool
- `requestSent`: bool
- `webHeaders`: WebHeaderCollection
- `keepAlive`: bool
- `maxAutoRedirect`: int
- `mediaType`: string
- `method`: string
- `initialMethod`: string
- ... (30 more fields)

---

#### HttpWebRequestElement

**Line:** 803167

**Inherits:** ConfigurationElement

---

#### HttpWebResponse

**Line:** 796146

**Inherits:** WebResponse

**Fields:**

- `uri`: Uri
- `webHeaders`: WebHeaderCollection
- `cookieCollection`: CookieCollection
- `method`: string
- `version`: Version
- `statusCode`: HttpStatusCode
- `statusDescription`: string
- `contentLength`: long
- `contentType`: string
- `cookie_container`: CookieContainer
- `disposed`: bool
- `stream`: Stream

---

#### HubConnection

**Line:** 1413219

**Inherits:** IAsyncDisposable

**Fields:**

- `_disposed`: bool
- `Closed`: Func<Exception, Task>
- `Reconnecting`: Func<Exception, Task>
- `Reconnected`: Func<string, Task>

---

#### HubConnectionBuilder

**Line:** 1413559

**Inherits:** IHubConnectionBuilder

**Fields:**

- `_hubConnectionBuilt`: bool

---

#### HubConnectionOptions

**Line:** 1415660

---

#### HubException

**Line:** 1568562

**Inherits:** Exception

---

#### HubInvocationMessage

**Line:** 1568874

**Inherits:** HubMessage

---

#### HubMessage

**Line:** 1568906

---

#### HubMethodInvocationMessage

**Line:** 1568917

**Inherits:** HubInvocationMessage

---

#### IAPClientDelegate

**Line:** 1312391

**Inherits:** IMetaIntegration

---

#### IAPClientDelegateApple

**Line:** 1312504

**Inherits:** HardcodedClientDrivenIAPClientDummyDelegate

---

#### IAPClientDelegateDevelopment

**Line:** 1312514

**Inherits:** HardcodedClientDrivenIAPClientDummyDelegate

---

#### IAPClientDelegateGoogle

**Line:** 1312494

**Inherits:** HardcodedClientDrivenIAPClientDummyDelegate

---

#### IAPClientDelegateRegistry

**Line:** 1312484

**Inherits:** IAPDelegateRegistry

---

#### IAPClientDelegateSteam

**Line:** 1313622

**Inherits:** IAPClientDelegateSteamUnvailableDummy

---

#### IAPClientDelegateSteamUnvailableDummy

**Line:** 1313631

**Inherits:** ServerDrivenIAPClientDelegate

---

#### IAPDelegateAttribute

**Line:** 583725

**Inherits:** Attribute

---

#### IAPDelegateRegistry

**Line:** 583901

**Fields:**

- `_platformToDelegate`: Dictionary<InAppPurchasePlatform, TDelegateBase>

---

#### IAPFakeStoreConfig

**Line:** 1312555

**Inherits:** ScriptableObject

**Fields:**

- `LocalizedPriceStringFormat`: string
- `IsoCurrencyCode`: string
- `InitIsSynchronous`: bool
- `AsyncInitDelay`: float
- `ForceInitFailure`: bool
- `DisabledProductIds`: List<string>
- `PurchaseIsSynchronous`: bool
- `AsyncPurchaseDelay`: float
- `ForcePurchaseFailure`: bool
- `UseFixedTransactionId`: bool
- `FixedTransactionId`: string
- `ForceIllFormedReceipt`: bool
- `ForceInvalidSignature`: bool
- `ValidationDelay`: float
- `ValidationTransientErrorProbability`: float
- `PretendSubscriptionIsFamilyShared`: bool
- `IgnorePurchaseConfirmation`: bool

---

#### IAPFlowTracker

**Line:** 1312653

**Fields:**

- `_bestEffortLastKnownFlowSteps`: Dictionary<InAppProductId, IAPFlowTracker.FlowStepInfo>
- `_iapManager`: IAPManager

---

#### IAPManager

**Line:** 1313238

**Inherits:** IDetailedStoreListener

**Fields:**

- `_log`: LogChannel
- `_sessionContextProvider`: ISessionContextProvider
- `_explicitPlatformMaybe`: InAppPurchasePlatform
- `_usesServerDrivenPlatform`: bool
- `_serverDrivenPlatformStoreIsAvailable`: bool
- `_storeInitFailure`: Nullable<IAPManager.StoreInitializationFailure>
- `_pendingMetaplaySessionFuncs`: Queue<Action>
- `_pendingStoreFuncs`: Queue<Action>
- `_delayedPlayerModelListenerFinishedPurchases`: Queue<InAppPurchaseEvent>
- `_pendingDynamicPurchases`: HashSet<InAppProductId>
- `_pendingStaticPurchaseContexts`: HashSet<InAppProductId>
- `_clientDelegates`: Dictionary<InAppPurchasePlatform, IAPClientDelegate>
- `_startedServerDrivenPurchaseClientHandlingTransactions`: HashSet<string>

---

#### IAPReceiptExtraction

**Line:** 1313578

---

#### IAPSecurityException

**Line:** 1594754

**Inherits:** Exception

---

#### IAPSharedDelegate

**Line:** 583932

**Inherits:** IMetaIntegration

---

#### IAPSharedDelegateApple

**Line:** 584049

**Inherits:** HardcodedClientDrivenIAPSharedDummyDelegate

---

#### IAPSharedDelegateDevelopment

**Line:** 584059

**Inherits:** HardcodedClientDrivenIAPSharedDummyDelegate

---

#### IAPSharedDelegateGoogle

**Line:** 584039

**Inherits:** HardcodedClientDrivenIAPSharedDummyDelegate

---

#### IAPSharedDelegateRegistry

**Line:** 584092

**Inherits:** IAPDelegateRegistry

---

#### IAPSharedDelegateSteam

**Line:** 586908

**Inherits:** ServerDrivenIAPSharedDelegate

---

#### ICameraHistoryReadAccess

**Line:** 804248

---

#### IDs

**Line:** 1530384

**Inherits:** IEnumerable

---

#### IGoogleSheetFetcherImpl

**Line:** 525698

---

#### IJobFilterExtensions

**Line:** 1167883

---

#### IJobForExtensions

**Line:** 835710

---

#### IJobParallelForDeferExtensions

**Line:** 1168733

---

#### IJobParallelForExtensions

**Line:** 836009

---

#### IJobParallelForTransformExtensions

**Line:** 886631

---

#### ILGenerator

**Line:** 269708

---

#### IMGUIContainer

**Line:** 641013

**Inherits:** VisualElement

**Fields:**

- `m_OnGUIHandler`: Action
- `m_ObjectGUIState`: ObjectGUIState
- `m_CullingEnabled`: bool
- `m_IsFocusDelegated`: bool
- `m_RefreshCachedLayout`: bool
- `m_CachedClippingRect`: Rect
- `m_CachedTransform`: Matrix4x4
- `m_ContextType`: ContextType
- `lostFocus`: bool
- `receivedFocus`: bool
- `focusChangeDirection`: FocusChangeDirection
- `hasFocusableControls`: bool
- `newKeyboardFocusControlID`: int

---

#### IMGUIEvent

**Line:** 639324

**Inherits:** EventBase

---

#### IODecodingError

**Line:** 566419

**Inherits:** Exception

---

#### IOException

**Line:** 467902

**Inherits:** SystemException

---

#### IOReader

**Line:** 566434

**Inherits:** IDisposable

**Fields:**

- `_reader`: LowLevelIOReader

---

#### IOReaderStream

**Line:** 566759

**Inherits:** Stream

**Fields:**

- `_reader`: LowLevelIOReader

---

#### IOWriter

**Line:** 566858

**Inherits:** IDisposable

---

#### IOWriterStream

**Line:** 567164

**Inherits:** Stream

**Fields:**

- `_writer`: LowLevelIOWriter

---

#### IPAddress

**Line:** 790113

**Fields:**

- `_addressOrScopeId`: uint
- `_toString`: string
- `_hashCode`: int

---

#### IPEndPoint

**Line:** 790269

**Inherits:** EndPoint

**Fields:**

- `_address`: IPAddress
- `_port`: int

---

#### IPGlobalProperties

**Line:** 798873

---

#### IPHostEntry

**Line:** 791711

**Fields:**

- `hostName`: string

---

#### ISessionCredentialService

**Line:** 546974

---

#### IapFeature

**Line:** 693045

**Inherits:** Feature

---

#### IapFeatureInitSystem

**Line:** 693098

**Inherits:** IInitializeSystem

---

#### IapIdComponent

**Line:** 692996

**Inherits:** IComponent

**Fields:**

- `Value`: InAppProductId

---

#### IapInitSystem

**Line:** 693134

**Inherits:** IExecuteSystem

---

#### IapProductInfoComponent

**Line:** 693009

**Inherits:** IComponent

**Fields:**

- `Value`: InAppProductInfo

---

#### IapPurchaseComponent

**Line:** 693024

**Inherits:** IComponent

---

#### IapPurchaseEventSystem

**Line:** 702148

**Inherits:** ReactiveSystem

---

#### IapPurchaseListenerComponent

**Line:** 699778

**Inherits:** IComponent

**Fields:**

- `value`: List<IIapPurchaseListener>

---

#### IapPurchasePossibleComponent

**Line:** 693036

**Inherits:** IComponent

---

#### IapPurchasePossibleEventSystem

**Line:** 702169

**Inherits:** ReactiveSystem

---

#### IapPurchasePossibleListenerComponent

**Line:** 699791

**Inherits:** IComponent

**Fields:**

- `value`: List<IIapPurchasePossibleListener>

---

#### IapPurchasePossibleRemovedEventSystem

**Line:** 702190

**Inherits:** ReactiveSystem

---

#### IapPurchasePossibleRemovedListenerComponent

**Line:** 699804

**Inherits:** IComponent

**Fields:**

- `value`: List<IIapPurchasePossibleRemovedListener>

---

#### IapPurchasedMessage

**Line:** 729768

**Inherits:** IMessage

---

#### IconChangeAction

**Line:** 1052032

**Inherits:** PlayerAction

---

#### IdAndName

**Line:** 1564730

**Fields:**

- `id`: int
- `name`: string

---

#### IdComponent

**Line:** 739494

**Inherits:** IComponent

**Fields:**

- `Value`: long

---

#### IdnMapping

**Line:** 274956

**Fields:**

- `allow_unassigned`: bool
- `use_std3`: bool
- `puny`: Punycode

---

#### IgnoreBackButtonComponent

**Line:** 736190

**Inherits:** IComponent

---

#### IgnoreSection

**Line:** 1597911

**Inherits:** ConfigurationSection

---

#### IgnoredByDeepProfilerAttribute

**Line:** 837009

**Inherits:** Attribute

---

#### Image

**Line:** 1353108

**Inherits:** MaskableGraphic

**Fields:**

- `m_Sprite`: Sprite
- `m_OverrideSprite`: Sprite
- `m_PreserveAspect`: bool
- `m_FillCenter`: bool
- `m_FillAmount`: float
- `m_FillClockwise`: bool
- `m_FillOrigin`: int
- `m_AlphaHitTestMinimumThreshold`: float
- `m_Tracked`: bool
- `m_UseSpriteMesh`: bool
- `m_PixelsPerUnitMultiplier`: float
- `m_CachedReferencePixelsPerUnit`: float

---

#### ImmutableXLoginChallengeRequest

**Line:** 499662

**Inherits:** MetaRequest

---

#### ImmutableXLoginChallengeResponse

**Line:** 499701

**Inherits:** MetaResponse

---

#### ImpactSfxComponent

**Line:** 705585

**Inherits:** IComponent

**Fields:**

- `Value`: ImpactSfx

---

#### ImpactSfxContainer

**Line:** 705749

**Fields:**

- `ImpactSfx`: ImpactSfx
- `Volume`: float

---

#### ImpersonatedCredential

**Line:** 1371867

**Inherits:** ServiceCredential

---

#### ImportAttribute

**Line:** 1505886

**Inherits:** Attribute

---

#### InAppProductId

**Line:** 584102

**Inherits:** StringId

---

#### InAppProductInfo

**Line:** 1051158

**Inherits:** InAppProductInfoBase

---

#### InAppProductInfoBase

**Line:** 584159

**Inherits:** IGameConfigData

---

#### InAppPurchaseEvent

**Line:** 584609

**Inherits:** IMetaIntegrationConstructible

---

#### InAppPurchaseEventPlatformState

**Line:** 586376

---

#### InAppPurchaseEventRefundState

**Line:** 584444

---

#### InAppPurchaseHistory

**Line:** 585692

---

#### InAppPurchasePendingRefundHandling

**Line:** 584485

---

#### InAppPurchasePlatform

**Line:** 584364

**Inherits:** DynamicEnum

---

#### InAppPurchasePlatformSteam

**Line:** 586891

**Inherits:** InAppPurchasePlatform

---

#### InAppPurchaseRefundData

**Line:** 584516

---

#### InAppPurchaseRefundReason

**Line:** 584422

**Inherits:** DynamicEnum

---

#### InAppPurchaseRefundResult

**Line:** 584529

---

#### InAppPurchaseTransactionInfo

**Line:** 585013

---

#### InAttribute

**Line:** 229224

**Inherits:** Attribute

---

#### InGameMailIntegration

**Line:** 561574

**Inherits:** IMetaIntegrationSingleton

---

#### InRowChangingEventException

**Line:** 1080811

**Inherits:** DataException

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

- `SharedConfigBaselineVersion`: ContentHash
- `SharedConfigPatchesVersion`: ContentHash

---

#### IncidentRepository

**Line:** 1311319

**Fields:**

- `_log`: LogChannel
- `_latestReportData`: Dictionary<string, byte[]>
- `_pendingDeletes`: HashSet<string>
- `_executor`: TaskQueueExecutor

---

#### IncidentTracker

**Line:** 1311407

**Fields:**

- `_log`: LogChannel
- `_incidentThrottle`: PeriodThrottle
- `_unitySystemInfo`: UnitySystemInfo
- `_unityPlatformInfo`: UnityPlatformInfo
- `_latestGameConfigInfo`: IncidentGameConfigInfo
- `_latestTlsPeerDescription`: string
- `_sessionToken`: SessionToken
- `_connectionErrorReportedForCurrentConnectionAttempt`: bool
- `_nextDroppedUnhandledExceptionsLogPrintAt`: DateTime
- `_numDroppedUnhandledExceptionsTotal`: int
- `_numDroppedUnhandledExceptionsLastTime`: int
- `_logHistoryTracker`: LogHistoryTracker
- `_pendingAnalyticsEvents`: List<PlayerEventIncidentRecorded>
- `_pendingAnalyticsEventsLock`: object

---

#### IncidentUploader

**Line:** 1311608

**Fields:**

- `_lock`: object
- `_nextProposalAt`: DateTime
- `_nextUploadAt`: DateTime
- `_incidentsToUpload`: Queue<string>
- `_ongoingUploadIncident`: string
- `_debugDiagnostics`: LoginIncidentReportDebugDiagnostics
- `_requestResponseLock`: object
- `_nextUploadUrlRequestId`: int

---

#### IncludeAdditionalRPAssets

**Line:** 821319

**Inherits:** IRenderPipelineGraphicsSettings

**Fields:**

- `m_IncludeReferencedInScenes`: bool
- `m_IncludeAssetsByLabel`: bool
- `m_LabelToInclude`: string

---

#### IncludeOnlyInJsonSerializationModeAttribute

**Line:** 582840

**Inherits:** Attribute

---

#### IncrementAttribute

**Line:** 1442928

**Inherits:** Attribute

---

#### IndentedStringBuilder

**Line:** 529255

**Fields:**

- `_outputDebugCode`: bool
- `_sb`: StringBuilder
- `_level`: int

---

#### IndexComponent

**Line:** 729473

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### IndexEventSystem

**Line:** 702211

**Inherits:** ReactiveSystem

---

#### IndexExpression

**Line:** 1287455

**Inherits:** Expression

**Fields:**

- `_arguments`: IReadOnlyList<Expression>

---

#### IndexListenerComponent

**Line:** 699817

**Inherits:** IComponent

**Fields:**

- `value`: List<IIndexListener>

---

#### IndexOutOfRangeException

**Line:** 24531

**Inherits:** SystemException

---

#### IndexedCollectionPropertyBag

**Line:** 1464936

---

#### InfoBlock

**Line:** 1444391

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `Content`: Text
- `Title`: Text

---

#### InfoEntry

**Line:** 1442491

**Fields:**

- `_valueGetter`: Func<object>

---

#### InfoTabController

**Line:** 1443224

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_infoBlocks`: Dictionary<string, InfoBlock>
- `InfoBlockPrefab`: InfoBlock
- `LayoutContainer`: RectTransform

---

#### InheritColour

**Line:** 1506544

**Inherits:** SRMonoBehaviour

**Fields:**

- `_graphic`: Graphic
- `From`: Graphic

---

#### InitAttribute

**Line:** 704061

**Inherits:** ContextAttribute

---

#### InitContext

**Line:** 704109

**Inherits:** Context

---

#### InitEntity

**Line:** 704118

**Inherits:** Entity

---

#### InitMatcher

**Line:** 704127

---

#### InitSystems

**Line:** 684201

**Inherits:** IDisposable

---

#### InitializationException

**Line:** 1491667

**Inherits:** Exception

---

#### InitializationOptions

**Line:** 1588916

---

#### InitializePushNotificationFrameworkSystem

**Line:** 694329

**Inherits:** IInitializeSystem

---

#### InitializePushNotificationSystem

**Line:** 694344

**Inherits:** IInitializeSystem

---

#### InitializeVideoFingerSystem

**Line:** 697503

**Inherits:** IInitializeSystem

---

#### Input

**Line:** 1580427

---

#### InputAttribute

**Line:** 704148

**Inherits:** ContextAttribute

---

#### InputContext

**Line:** 704196

**Inherits:** Context

---

#### InputEntity

**Line:** 704205

**Inherits:** Entity

---

#### InputEvent

**Line:** 635638

**Inherits:** EventBase

---

#### InputField

**Line:** 1353619

**Inherits:** Selectable

**Fields:**

- `m_Keyboard`: TouchScreenKeyboard
- `m_TextComponent`: Text
- `m_Placeholder`: Graphic
- `m_AsteriskChar`: char
- `m_KeyboardType`: TouchScreenKeyboardType
- `m_HideMobileInput`: bool
- `m_CharacterLimit`: int
- `m_CaretColor`: Color
- `m_CustomCaretColor`: bool
- `m_SelectionColor`: Color
- `m_Text`: string
- `m_CaretBlinkRate`: float
- `m_CaretWidth`: int
- `m_ReadOnly`: bool
- `m_ShouldActivateOnSelect`: bool
- `m_CaretPosition`: int
- `m_CaretSelectPosition`: int
- `caretRectTrans`: RectTransform
- `m_InputTextCache`: TextGenerator
- `m_CachedInputRenderer`: CanvasRenderer
- ... (19 more fields)

---

#### InputMatcher

**Line:** 704214

---

#### InsertDimensionRequest

**Line:** 1394215

**Inherits:** IDirectResponseSchema

---

#### InsertRangeRequest

**Line:** 1394263

**Inherits:** IDirectResponseSchema

---

#### InspectorNameAttribute

**Line:** 880781

**Inherits:** PropertyAttribute

---

#### InspectorOrderAttribute

**Line:** 883107

**Inherits:** PropertyAttribute

---

#### InstanceDescriptor

**Line:** 785118

---

#### InstanceProvider

**Line:** 1437213

**Inherits:** IInstanceProvider

---

#### InstantPattern

**Line:** 1152301

**Inherits:** IPattern

---

#### Instrument

**Line:** 1422535

---

#### InstrumentAdvice

**Line:** 1422330

---

#### InsufficientExecutionStackException

**Line:** 24550

**Inherits:** SystemException

---

#### Int128Converter

**Line:** 560907

**Inherits:** JsonConverter

---

#### Int16Converter

**Line:** 782199

**Inherits:** BaseNumberConverter

---

#### Int32Converter

**Line:** 782223

**Inherits:** BaseNumberConverter

---

#### Int64Converter

**Line:** 782247

**Inherits:** BaseNumberConverter

---

#### IntGlobalVariable

**Line:** 1321549

**Inherits:** IntVariable

---

#### IntIntMap

**Line:** 1573306

**Fields:**

- `collectionRef`: IntIntMap
- `keyCollection`: IList<int>
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### IntParameter

**Line:** 826983

**Inherits:** VolumeParameter

---

#### IntPlugin

**Line:** 1429326

**Inherits:** ABSTweenPlugin

---

#### IntTrackedProperty

**Line:** 1328891

**Inherits:** TrackedProperty

---

#### IntVariable

**Line:** 1324557

**Inherits:** Variable

---

#### IntegerField

**Line:** 624515

**Inherits:** TextValueField

---

#### IntegrationAssembly

**Line:** 502998

---

#### IntegrationConfig

**Line:** 502833

---

#### IntegrationDataSet

**Line:** 502858

---

#### IntegrationRegistry

**Line:** 503313

**Inherits:** IIntegrationRegistry

**Fields:**

- `_registry`: Dictionary<Type, Type[]>
- `_singletons`: Dictionary<Type, IMetaIntegrationSingleton>

---

#### IntegrationTypeInfoMap

**Line:** 503154

---

#### InterfaceTypeAttribute

**Line:** 229017

**Inherits:** Attribute

---

#### InternalDataCollectionBase

**Line:** 1083094

**Inherits:** ICollection

---

#### InternalOptionsRegistry

**Line:** 1446811

**Fields:**

- `_registeredContainers`: List<object>
- `_handler`: Action<object>

---

#### InternalRemotingServices

**Line:** 221052

---

#### InternalRenderGraphContext

**Line:** 829140

---

#### InternalServerErrorResponse

**Line:** 685103

---

#### InternalsVisibleToAttribute

**Line:** 253461

**Inherits:** Attribute

**Fields:**

- `_assemblyName`: string
- `_allInternalsVisible`: bool

---

#### InterpolationPoint

**Line:** 1394311

**Inherits:** IDirectResponseSchema

---

#### Interval

**Line:** 1394383

**Inherits:** IDirectResponseSchema

**Fields:**

- `_endTimeRaw`: string
- `_endTime`: object
- `_startTimeRaw`: string
- `_startTime`: object

---

#### InvalidBundleIdException

**Line:** 1544966

**Inherits:** IAPSecurityException

---

#### InvalidCastException

**Line:** 24896

**Inherits:** SystemException

---

#### InvalidCipherTextException

**Line:** 1518436

**Inherits:** CryptoException

---

#### InvalidClientVersionSuppliedException

**Line:** 685202

**Inherits:** BadRequestException

---

#### InvalidConstraintException

**Line:** 1080827

**Inherits:** DataException

---

#### InvalidDataException

**Line:** 789357

**Inherits:** SystemException

---

#### InvalidDateTimeZoneSourceException

**Line:** 1148752

**Inherits:** Exception

---

#### InvalidEnumArgumentException

**Line:** 780908

**Inherits:** ArgumentException

---

#### InvalidExpressionException

**Line:** 1086386

**Inherits:** DataException

---

#### InvalidFilterCriteriaException

**Line:** 265591

**Inherits:** ApplicationException

---

#### InvalidImportException

**Line:** 895744

**Inherits:** Exception

---

#### InvalidJwtException

**Line:** 1367709

**Inherits:** Exception

---

#### InvalidKeyException

**Line:** 1453736

**Inherits:** Exception

**Fields:**

- `m_Addressables`: AddressablesImpl

---

#### InvalidNodaDataException

**Line:** 1148019

**Inherits:** Exception

---

#### InvalidOperationException

**Line:** 24915

**Inherits:** SystemException

---

#### InvalidPKCS7Data

**Line:** 1545290

**Inherits:** IAPSecurityException

---

#### InvalidPatternException

**Line:** 1152471

**Inherits:** FormatException

---

#### InvalidProductTypeException

**Line:** 1407770

**Inherits:** ReceiptParserException

---

#### InvalidProgramException

**Line:** 24934

**Inherits:** SystemException

---

#### InvalidPublicKeyException

**Line:** 1544993

**Inherits:** IAPSecurityException

---

#### InvalidRSAData

**Line:** 1545347

**Inherits:** IAPSecurityException

---

#### InvalidReceiptDataException

**Line:** 1544975

**Inherits:** IAPSecurityException

---

#### InvalidSignatureException

**Line:** 1594766

**Inherits:** IAPSecurityException

---

#### InvalidTimeFormat

**Line:** 1544939

**Inherits:** IAPSecurityException

---

#### InvalidTimeZoneException

**Line:** 24951

**Inherits:** Exception

---

#### InvalidX509Data

**Line:** 1544948

**Inherits:** IAPSecurityException

---

#### InventoryItemVisual

**Line:** 714006

**Inherits:** MonoBehaviour

**Fields:**

- `BaseItemVisual`: BaseItemVisual
- `Button`: UnityButton
- `_item`: PlayerItemModel

---

#### InventoryManagerUiView

**Line:** 714026

**Inherits:** UiUnityView

**Fields:**

- `Slots`: List<Transform>
- `SlotPrefab`: SlotVisual
- `ItemPrefab`: InventoryItemVisual
- `_inventoryItems`: Dictionary<ItemType, InventoryItemVisual>
- `_playerItemModels`: Dictionary<ItemType, PlayerItemModel>

---

#### InventoryOverlayUiView

**Line:** 714054

**Inherits:** UiUnityView

**Fields:**

- `PanelOpenOverlay`: GameObject

---

#### InventoryUiCreateSystem

**Line:** 713890

**Inherits:** ReactiveSystem

---

#### InversePropertyAttribute

**Line:** 1510931

**Inherits:** Attribute

---

#### InvisibleButton

**Line:** 735974

**Inherits:** UnityButton

**Fields:**

- `HasClickSfx`: bool

---

#### InvocationBindingFailureMessage

**Line:** 1569107

**Inherits:** HubInvocationMessage

---

#### InvocationExpression

**Line:** 1287505

**Inherits:** Expression

---

#### InvocationMessage

**Line:** 1568983

**Inherits:** HubMethodInvocationMessage

---

#### InvokeBinder

**Line:** 1300840

**Inherits:** DynamicMetaObjectBinder

---

#### InvokeOnDeserializedMethodDelegate

**Line:** 531405

---

#### InvokeOnDeserializedMethodWithParamsDelegate

**Line:** 531455

---

#### Ipv6Element

**Line:** 803182

**Inherits:** ConfigurationElement

---

#### IsByRefLikeAttribute

**Line:** 234306

**Inherits:** Attribute

---

#### IsMatchFormatter

**Line:** 1321710

**Inherits:** FormatterBase

---

#### IsReadOnlyAttribute

**Line:** 234316

**Inherits:** Attribute

---

#### IsoCodeAttribute

**Line:** 1564213

**Inherits:** Attribute

---

#### IsoDateTimeConverter

**Line:** 1048582

**Inherits:** DateTimeConverterBase

**Fields:**

- `_dateTimeStyles`: DateTimeStyles
- `_dateTimeFormat`: string
- `_culture`: CultureInfo

---

#### ItemBackgroundView

**Line:** 711437

**Inherits:** MonoBehaviour

**Fields:**

- `BaseImage`: Image
- `Outline`: Image

---

#### ItemBalancingConfig

**Line:** 1051694

**Inherits:** GameConfigKeyValue

**Fields:**

- `LevelScalingBase`: F64
- `SellBasePrice`: F64
- `PlayerMeleeDamageMultiplier`: F64
- `EnemyRangedDamageMultiplier`: F64
- `PlayerPowerDamageMultiplier`: F64
- `PlayerBaseCritDamage`: F64
- `ItemBaseMaxLevel`: F64

---

#### ItemCheatContainer

**Line:** 686050

**Inherits:** AbstractCheatContainer

---

#### ItemEquippedMessage

**Line:** 713781

**Inherits:** IMessage

---

#### ItemId

**Line:** 1067634

**Inherits:** IEquatable

---

#### ItemLocalizer

**Line:** 721121

**Inherits:** LocalizerBase

---

#### ItemPreviewVisual

**Line:** 714097

**Inherits:** MonoBehaviour

**Fields:**

- `BaseItemVisual`: BaseItemVisual
- `Button`: UnityButton

---

#### ItemSoldMessage

**Line:** 714766

**Inherits:** IMessage

---

#### ItemUnequippedMessage

**Line:** 713801

**Inherits:** IMessage

---

#### ItemVisual

**Line:** 714116

**Inherits:** MonoBehaviour

**Fields:**

- `BaseItemVisual`: BaseItemVisual
- `Name`: TMP_Text
- `Stats`: TMP_Text
- `NewText`: TMP_Text

---

#### ItemWasSoldComponent

**Line:** 714323

**Inherits:** IComponent

---

#### ItemsMarkedForSellingComponent

**Line:** 713575

**Inherits:** IComponent

**Fields:**

- `Value`: HashSet<Guid>

---

#### IterativeCalculationSettings

**Line:** 1394461

**Inherits:** IDirectResponseSchema

---

#### IteratorStateMachineAttribute

**Line:** 234331

**Inherits:** StateMachineAttribute

---

#### JArray

**Line:** 1043720

**Inherits:** JContainer

---

#### JConstructor

**Line:** 1043907

**Inherits:** JContainer

**Fields:**

- `_name`: string

---

#### JContainer

**Line:** 1044126

**Inherits:** JToken

**Fields:**

- `_syncRoot`: object
- `_busy`: bool

---

#### JObject

**Line:** 1044765

**Inherits:** JContainer

**Fields:**

- `PropertyChanged`: PropertyChangedEventHandler
- `PropertyChanging`: PropertyChangingEventHandler

---

#### JProperty

**Line:** 1045188

**Inherits:** JContainer

---

#### JPropertyDescriptor

**Line:** 1045306

**Inherits:** PropertyDescriptor

---

#### JRaw

**Line:** 1045461

**Inherits:** JValue

---

#### JToken

**Line:** 1045979

**Inherits:** IJEnumerable

**Fields:**

- `_parent`: JContainer
- `_previous`: JToken
- `_next`: JToken
- `_annotations`: object

---

#### JTokenEqualityComparer

**Line:** 1046617

**Inherits:** IEqualityComparer

---

#### JTokenReader

**Line:** 1046636

**Inherits:** JsonReader

**Fields:**

- `_initialPath`: string
- `_parent`: JToken
- `_current`: JToken

---

#### JTokenWriter

**Line:** 1046732

**Inherits:** JsonWriter

**Fields:**

- `_token`: JContainer
- `_parent`: JContainer
- `_value`: JValue
- `_current`: JToken

---

#### JValue

**Line:** 1046903

**Inherits:** JToken

**Fields:**

- `_valueType`: JTokenType
- `_value`: object

---

#### JapaneseCalendar

**Line:** 273456

**Inherits:** Calendar

---

#### JavaScriptDateTimeConverter

**Line:** 1048633

**Inherits:** DateTimeConverterBase

---

#### JavaScriptEncoder

**Line:** 1521982

**Inherits:** TextEncoder

---

#### JobProducerTypeAttribute

**Line:** 836678

**Inherits:** Attribute

---

#### JobSystem

**Line:** 1547074

**Fields:**

- `_threadsRunning`: int

---

#### JoinChatRoomRequest

**Line:** 1527940

**Inherits:** IEquatable

---

#### Joint2D

**Line:** 1578730

**Inherits:** Behaviour

---

#### JournalModelActionImmutabilityChecker

**Line:** 605032

**Fields:**

- `_beforeBuffer`: FlatIOBuffer
- `_afterBuffer`: FlatIOBuffer

---

#### JournalModelChecksumChecker

**Line:** 604967

**Fields:**

- `_consistencyBuffer`: FlatIOBuffer

---

#### JournalModelCloningChecker

**Line:** 604836

**Fields:**

- `_checkCloningBuffer`: FlatIOBuffer

---

#### JournalModelModifyHistoryChecker

**Line:** 605066

**Fields:**

- `_beforeBuffer`: FlatIOBuffer
- `_afterBuffer`: FlatIOBuffer
- `_beforeResolver`: IGameConfigDataResolver
- `_beforeLogicVersion`: int

---

#### JournalModelOutsideModificationChecker

**Line:** 604877

**Fields:**

- `_outsideModificationBeforeBuffer`: FlatIOBuffer
- `_outsideModificationAfterBuffer`: FlatIOBuffer

---

#### JsonArray

**Line:** 999258

**Inherits:** JsonNode

**Fields:**

- `_jsonElement`: Nullable<JsonElement>
- `_list`: List<JsonNode>

---

#### JsonArrayAttribute

**Line:** 1026014

**Inherits:** JsonContainerAttribute

**Fields:**

- `_allowNullItems`: bool

---

#### JsonArrayContract

**Line:** 1038747

**Inherits:** JsonContainerContract

**Fields:**

- `_genericWrapperType`: Type
- `_genericWrapperCreator`: ObjectConstructor<object>
- `_genericTemporaryCollectionCreator`: Func<object>
- `_parameterizedCreator`: ObjectConstructor<object>
- `_overrideCreator`: ObjectConstructor<object>

---

#### JsonAssetProvider

**Line:** 1437426

**Inherits:** TextDataProvider

---

#### JsonAttribute

**Line:** 1003203

**Inherits:** Attribute

---

#### JsonCloneSettings

**Line:** 1045487

---

#### JsonCollectionInfoValues

**Line:** 1012087

---

#### JsonConstructorAttribute

**Line:** 1026043

**Inherits:** Attribute

---

#### JsonContainerAttribute

**Line:** 1026055

**Inherits:** Attribute

**Fields:**

- `_namingStrategyType`: Type

---

#### JsonContainerContract

**Line:** 1038853

**Inherits:** JsonContract

**Fields:**

- `_itemContract`: JsonContract
- `_finalItemContract`: JsonContract

---

#### JsonContract

**Line:** 1039052

**Fields:**

- `_onDeserializedCallbacks`: List<SerializationCallback>
- `_onDeserializingCallbacks`: List<SerializationCallback>
- `_onSerializedCallbacks`: List<SerializationCallback>
- `_onSerializingCallbacks`: List<SerializationCallback>
- `_onErrorCallbacks`: List<SerializationErrorCallback>
- `_createdType`: Type

---

#### JsonConverter

**Line:** 1026542

---

#### JsonConverterAttribute

**Line:** 1026599

**Inherits:** Attribute

---

#### JsonConverterCollection

**Line:** 1026630

**Inherits:** Collection

---

#### JsonConverterFactory

**Line:** 1005322

**Inherits:** JsonConverter

---

#### JsonCredentialParameters

**Line:** 1372168

---

#### JsonDerivedTypeAttribute

**Line:** 1003686

**Inherits:** JsonAttribute

---

#### JsonDictionaryAttribute

**Line:** 1026640

**Inherits:** JsonContainerAttribute

---

#### JsonDictionaryContract

**Line:** 1039207

**Inherits:** JsonContainerContract

**Fields:**

- `_genericWrapperType`: Type
- `_genericWrapperCreator`: ObjectConstructor<object>
- `_genericTemporaryDictionaryCreator`: Func<object>
- `_overrideCreator`: ObjectConstructor<object>
- `_parameterizedCreator`: ObjectConstructor<object>

---

#### JsonDocument

**Line:** 992695

**Inherits:** IDisposable

**Fields:**

- `_utf8Json`: ReadOnlyMemory<byte>
- `_extraPooledByteBufferWriter`: PooledByteBufferWriter

---

#### JsonDynamicContract

**Line:** 1039315

**Inherits:** JsonContainerContract

---

#### JsonException

**Line:** 1026656

**Inherits:** Exception

---

#### JsonExcludeReadOnlyProperties

**Line:** 582820

**Inherits:** Attribute

---

#### JsonExplicitNullAttribute

**Line:** 1496446

**Inherits:** Attribute

---

#### JsonExtensionDataAttribute

**Line:** 1026678

**Inherits:** Attribute

---

#### JsonHubProtocol

**Line:** 1572759

**Inherits:** IHubProtocol

---

#### JsonHubProtocolOptions

**Line:** 1572708

---

#### JsonISerializableContract

**Line:** 1039484

**Inherits:** JsonContainerContract

---

#### JsonIgnoreAttribute

**Line:** 1026714

**Inherits:** Attribute

---

#### JsonIncludeAttribute

**Line:** 1003757

**Inherits:** JsonAttribute

---

#### JsonLinqContract

**Line:** 1039511

**Inherits:** JsonContract

---

#### JsonLoadSettings

**Line:** 1045516

**Fields:**

- `_commentHandling`: CommentHandling
- `_lineInfoHandling`: LineInfoHandling
- `_duplicatePropertyNameHandling`: DuplicatePropertyNameHandling

---

#### JsonMergeSettings

**Line:** 1045553

**Fields:**

- `_mergeArrayHandling`: MergeArrayHandling
- `_mergeNullValueHandling`: MergeNullValueHandling
- `_propertyNameComparison`: StringComparison

---

#### JsonNameTable

**Line:** 1026723

---

#### JsonNamingPolicy

**Line:** 991848

---

#### JsonNode

**Line:** 999569

**Fields:**

- `_parent`: JsonNode
- `_options`: Nullable<JsonNodeOptions>

---

#### JsonNumberEnumConverter

**Line:** 1003979

---

#### JsonNumberHandlingAttribute

**Line:** 1003767

**Inherits:** JsonAttribute

---

#### JsonObject

**Line:** 1000105

**Inherits:** JsonNode

**Fields:**

- `_jsonElement`: Nullable<JsonElement>
- `_dictionary`: OrderedDictionary<string, JsonNode>

---

#### JsonObjectAttribute

**Line:** 1026737

**Inherits:** JsonContainerAttribute

**Fields:**

- `_memberSerialization`: MemberSerialization

---

#### JsonObjectContract

**Line:** 1039523

**Inherits:** JsonContainerContract

**Fields:**

- `_hasRequiredOrDefaultValueProperties`: Nullable<bool>
- `_overrideCreator`: ObjectConstructor<object>
- `_parameterizedCreator`: ObjectConstructor<object>
- `_creatorParameters`: JsonPropertyCollection
- `_extensionDataValueType`: Type

---

#### JsonObjectCreationHandlingAttribute

**Line:** 1003621

**Inherits:** JsonAttribute

---

#### JsonObjectInfoValues

**Line:** 1012738

---

#### JsonParameterInfo

**Line:** 1013007

**Fields:**

- `_attributeProvider`: ICustomAttributeProvider

---

#### JsonParameterInfoValues

**Line:** 1012912

---

#### JsonPolymorphicAttribute

**Line:** 1003790

**Inherits:** JsonAttribute

---

#### JsonPolymorphismOptions

**Line:** 1008851

**Fields:**

- `_ignoreUnrecognizedTypeDiscriminators`: bool
- `_unknownDerivedTypeHandling`: JsonUnknownDerivedTypeHandling
- `_typeDiscriminatorPropertyName`: string

---

#### JsonPrimitiveContract

**Line:** 1039673

**Inherits:** JsonContract

---

#### JsonProperty

**Line:** 1039703

**Fields:**

- `_defaultValue`: object
- `_hasGeneratedDefaultValue`: bool
- `_propertyName`: string
- `_propertyType`: Type

---

#### JsonPropertyAttribute

**Line:** 1026841

**Inherits:** Attribute

---

#### JsonPropertyCollection

**Line:** 1040059

**Inherits:** KeyedCollection

---

#### JsonPropertyInfo

**Line:** 1013433

**Fields:**

- `_customConverter`: JsonConverter
- `_isUserSpecifiedSetter`: bool
- `_isUserSpecifiedShouldSerialize`: bool
- `_ignoreCondition`: Nullable<JsonIgnoreCondition>
- `_attributeProvider`: ICustomAttributeProvider
- `_objectCreationHandling`: Nullable<JsonObjectCreationHandling>
- `_isGetNullable`: bool
- `_isExtensionDataProperty`: bool
- `_name`: string
- `_order`: int
- `_jsonTypeInfo`: JsonTypeInfo
- `_numberHandling`: Nullable<JsonNumberHandling>
- `_index`: int

---

#### JsonPropertyInfoValues

**Line:** 1016747

---

#### JsonPropertyNameAttribute

**Line:** 1003839

**Inherits:** JsonAttribute

---

#### JsonPropertyOrderAttribute

**Line:** 1003870

**Inherits:** JsonAttribute

---

#### JsonReader

**Line:** 1027149

**Inherits:** IDisposable

**Fields:**

- `_tokenType`: JsonToken
- `_value`: object
- `_currentPosition`: JsonPosition
- `_culture`: CultureInfo
- `_dateTimeZoneHandling`: DateTimeZoneHandling
- `_maxDepth`: Nullable<int>
- `_hasExceededMaxDepth`: bool
- `_dateFormatString`: string
- `_stack`: List<JsonPosition>

---

#### JsonReaderException

**Line:** 1027472

**Inherits:** JsonException

---

#### JsonRequiredAttribute

**Line:** 1027531

**Inherits:** Attribute

---

#### JsonSchema

**Line:** 1041591

---

#### JsonSchemaException

**Line:** 1042160

**Inherits:** JsonException

---

#### JsonSchemaExporterOptions

**Line:** 999003

---

#### JsonSchemaGenerator

**Line:** 1042250

**Fields:**

- `_contractResolver`: IContractResolver
- `_resolver`: JsonSchemaResolver
- `_currentSchema`: JsonSchema

---

#### JsonSchemaResolver

**Line:** 1042787

---

#### JsonSelectSettings

**Line:** 1045590

---

#### JsonSerializableAttribute

**Line:** 1003269

**Inherits:** JsonAttribute

---

#### JsonSerializationErrorLogger

**Line:** 583607

---

#### JsonSerializationException

**Line:** 1027543

**Inherits:** JsonException

---

#### JsonSerializeNullCollectionAsEmptyAttribute

**Line:** 582830

**Inherits:** Attribute

---

#### JsonSerializer

**Line:** 1027603

**Fields:**

- `_referenceResolver`: IReferenceResolver
- `_formatting`: Nullable<Formatting>
- `_dateFormatHandling`: Nullable<DateFormatHandling>
- `_dateTimeZoneHandling`: Nullable<DateTimeZoneHandling>
- `_dateParseHandling`: Nullable<DateParseHandling>
- `_floatFormatHandling`: Nullable<FloatFormatHandling>
- `_floatParseHandling`: Nullable<FloatParseHandling>
- `_stringEscapeHandling`: Nullable<StringEscapeHandling>
- `_culture`: CultureInfo
- `_maxDepth`: Nullable<int>
- `_maxDepthSet`: bool
- `_checkAdditionalContent`: Nullable<bool>
- `_dateFormatString`: string
- `_dateFormatStringSet`: bool
- `Error`: EventHandler<ErrorEventArgs>

---

#### JsonSerializerContext

**Line:** 1004009

**Inherits:** IJsonTypeInfoResolver

**Fields:**

- `_options`: JsonSerializerOptions

---

#### JsonSerializerOptions

**Line:** 996218

**Fields:**

- `_lastTypeInfo`: JsonTypeInfo
- `_objectTypeInfo`: JsonTypeInfo
- `_typeInfoResolver`: IJsonTypeInfoResolver
- `_dictionaryKeyPolicy`: JsonNamingPolicy
- `_jsonPropertyNamingPolicy`: JsonNamingPolicy
- `_readCommentHandling`: JsonCommentHandling
- `_referenceHandler`: ReferenceHandler
- `_encoder`: JavaScriptEncoder
- `_defaultIgnoreCondition`: JsonIgnoreCondition
- `_numberHandling`: JsonNumberHandling
- `_preferredObjectCreationHandling`: JsonObjectCreationHandling
- `_unknownTypeHandling`: JsonUnknownTypeHandling
- `_unmappedMemberHandling`: JsonUnmappedMemberHandling
- `_defaultBufferSize`: int
- `_maxDepth`: int
- `_allowOutOfOrderMetadataProperties`: bool
- `_allowTrailingCommas`: bool
- `_respectNullableAnnotations`: bool
- `_respectRequiredConstructorParameters`: bool
- `_ignoreNullValues`: bool
- ... (12 more fields)

---

#### JsonSerializerSettings

**Line:** 1028001

---

#### JsonSerializerTrackedObject

**Line:** 1329215

**Inherits:** TrackedObject

---

#### JsonSourceGenerationOptionsAttribute

**Line:** 1003319

**Inherits:** JsonAttribute

---

#### JsonStringContract

**Line:** 1040809

**Inherits:** JsonPrimitiveContract

---

#### JsonStringEnumConverter

**Line:** 1008243

**Inherits:** JsonConverterFactory

---

#### JsonTextReader

**Line:** 1029326

**Inherits:** JsonReader

**Fields:**

- `_charsUsed`: int
- `_charPos`: int
- `_lineStartPos`: int
- `_lineNumber`: int
- `_isEndOfFile`: bool
- `_stringBuffer`: StringBuffer
- `_stringReference`: StringReference
- `_arrayPool`: IArrayPool<char>

---

#### JsonTextWriter

**Line:** 1030316

**Inherits:** JsonWriter

**Fields:**

- `_base64Encoder`: Base64Encoder
- `_indentChar`: char
- `_indentation`: int
- `_quoteChar`: char
- `_quoteName`: bool
- `_arrayPool`: IArrayPool<char>

---

#### JsonTypeInfo

**Line:** 1017280

**Fields:**

- `_propertyIndex`: Dictionary<string, JsonPropertyInfo>
- `_onSerializing`: Action<object>
- `_onSerialized`: Action<object>
- `_onDeserializing`: Action<object>
- `_onDeserialized`: Action<object>
- `_sourceGenDelayedPropertyInitializer`: Func<JsonSerializerContext, JsonPropertyInfo[]>
- `_elementTypeInfo`: JsonTypeInfo
- `_keyTypeInfo`: JsonTypeInfo
- `_numberHandling`: Nullable<JsonNumberHandling>
- `_unmappedMemberHandling`: Nullable<JsonUnmappedMemberHandling>
- `_preferredPropertyObjectCreationHandling`: Nullable<JsonObjectCreationHandling>
- `_originatingResolver`: IJsonTypeInfoResolver
- `_constructorAttributeProvider`: ICustomAttributeProvider
- `_cachedConfigureError`: ExceptionDispatchInfo
- `_ancestorPolymorhicType`: JsonTypeInfo
- `_isAncestorPolymorphicTypeResolved`: bool

---

#### JsonValidatingReader

**Line:** 1031136

**Inherits:** JsonReader

**Fields:**

- `_schema`: JsonSchema
- `_model`: JsonSchemaModel
- `ValidationEventHandler`: ValidationEventHandler

---

#### JsonValue

**Line:** 1000275

**Inherits:** JsonNode

---

#### JsonWebSignature

**Line:** 1367869

---

#### JsonWebToken

**Line:** 1368075

---

#### JsonWriter

**Line:** 1031574

**Inherits:** IDisposable

**Fields:**

- `_stack`: List<JsonPosition>
- `_currentPosition`: JsonPosition
- `_formatting`: Formatting
- `_dateFormatHandling`: DateFormatHandling
- `_dateTimeZoneHandling`: DateTimeZoneHandling
- `_stringEscapeHandling`: StringEscapeHandling
- `_floatFormatHandling`: FloatFormatHandling
- `_dateFormatString`: string
- `_culture`: CultureInfo

---

#### JsonWriterException

**Line:** 1032257

**Inherits:** JsonException

---

#### Kcp

**Line:** 1582266

---

#### KebabCaseNamingStrategy

**Line:** 1040976

**Inherits:** NamingStrategy

---

#### KerningPair

**Line:** 1223309

**Fields:**

- `m_FirstGlyph`: uint
- `m_FirstGlyphAdjustments`: GlyphValueRecord_Legacy
- `m_SecondGlyph`: uint
- `m_SecondGlyphAdjustments`: GlyphValueRecord_Legacy
- `xOffset`: float
- `m_IgnoreSpacingAdjustments`: bool

---

#### KerningTable

**Line:** 1223452

**Fields:**

- `kerningPairs`: List<KerningPair>

---

#### KeyAttribute

**Line:** 1509421

**Inherits:** Attribute

---

#### KeyBuilder

**Line:** 1449329

---

#### KeyDownEvent

**Line:** 635898

**Inherits:** KeyboardEventBase

---

#### KeyGenerationParameters

**Line:** 1518475

**Fields:**

- `random`: SecureRandom
- `strength`: int

---

#### KeyNotFoundException

**Line:** 348808

**Inherits:** SystemException

---

#### KeyParameter

**Line:** 1519065

**Inherits:** ICipherParameters

---

#### KeySizes

**Line:** 217968

**Fields:**

- `m_minSize`: int
- `m_maxSize`: int
- `m_skipSize`: int

---

#### KeyUpEvent

**Line:** 635954

**Inherits:** KeyboardEventBase

---

#### KeyValueCollectionPropertyBag

**Line:** 1465340

---

#### KeyValueFormat

**Line:** 1394509

**Inherits:** IDirectResponseSchema

---

#### KeyValuePairConverter

**Line:** 1048650

**Inherits:** JsonConverter

---

#### KeyValuePairPropertyBag

**Line:** 1465527

---

#### KeyboardEventBase

**Line:** 635700

---

#### KeyboardNavigationManipulator

**Line:** 641294

**Inherits:** Manipulator

---

#### KeyboardShortcutListenerService

**Line:** 1445858

**Inherits:** SRServiceBase

**Fields:**

- `_shortcuts`: List<Settings.KeyboardShortcut>

---

#### KeyedCollection

**Line:** 310755

**Fields:**

- `dict`: Dictionary<TKey, TItem>
- `keyCount`: int

---

#### KeyedHashAlgorithm

**Line:** 218425

**Inherits:** HashAlgorithm

---

#### KeyframeUtility

**Line:** 825860

---

#### LODGroup

**Line:** 875709

**Inherits:** Component

---

#### LRUCacheAllocationStrategy

**Line:** 1436037

**Inherits:** IAllocationStrategy

**Fields:**

- `m_poolMaxSize`: int
- `m_poolInitialCapacity`: int
- `m_poolCacheMaxSize`: int

---

#### Label

**Line:** 624573

**Inherits:** TextElement

---

#### LabelExpression

**Line:** 1287728

**Inherits:** Expression

---

#### LabelTarget

**Line:** 1287769

---

#### LambdaExpression

**Line:** 1287800

**Inherits:** Expression

---

#### LanguageButton

**Line:** 721468

**Inherits:** MonoBehaviour

**Fields:**

- `Text`: TMP_Text
- `Button`: UnityButton
- `SelectedIndicator`: GameObject

---

#### LanguageId

**Line:** 561587

**Inherits:** StringId

---

#### LanguageIdMapping

**Line:** 1310736

**Inherits:** IMetaIntegrationSingleton

---

#### LanguageInfo

**Line:** 561597

**Inherits:** IGameConfigData

---

#### LanguageSelectorPopup

**Line:** 721499

**Inherits:** MonoBehaviour

**Fields:**

- `Parent`: Transform
- `LanguageButtonPrefab`: LanguageButton

---

#### LanguageSettingsView

**Line:** 729264

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: FlatButton

---

#### LastOnlineView

**Line:** 718672

**Inherits:** MonoBehaviour

**Fields:**

- `_lastOnlineText`: TMP_Text

---

#### LastOpenProfileComponent

**Line:** 706101

**Inherits:** IComponent

**Fields:**

- `Sender`: object

---

#### LatencySimulationMessageTransport

**Line:** 547118

**Inherits:** MessageTransport

**Fields:**

- `_innerTransport`: IMessageTransport
- `_halvedLatency`: int
- `_disposed`: bool

---

#### LayerMaskParameter

**Line:** 826961

**Inherits:** VolumeParameter

---

#### LayoutElement

**Line:** 1354937

**Inherits:** UIBehaviour

**Fields:**

- `m_IgnoreLayout`: bool
- `m_MinWidth`: float
- `m_MinHeight`: float
- `m_PreferredWidth`: float
- `m_PreferredHeight`: float
- `m_FlexibleWidth`: float
- `m_FlexibleHeight`: float
- `m_LayoutPriority`: int

---

#### LayoutGroup

**Line:** 1355088

**Inherits:** UIBehaviour

**Fields:**

- `m_Padding`: RectOffset
- `m_ChildAlignment`: TextAnchor
- `m_Rect`: RectTransform
- `m_Tracker`: DrivenRectTransformTracker
- `m_TotalMinSize`: Vector2
- `m_TotalPreferredSize`: Vector2
- `m_TotalFlexibleSize`: Vector2
- `m_RectChildren`: List<RectTransform>

---

#### LayoutRebuilder

**Line:** 1355298

**Inherits:** ICanvasElement

**Fields:**

- `m_ToRebuild`: RectTransform
- `m_CachedHashFromTransform`: int

---

#### Lazy

**Line:** 25030

**Fields:**

- `_state`: LazyHelper
- `_factory`: Func<T>
- `_value`: T

---

#### LeagueClient

**Line:** 565384

**Fields:**

- `DivisionSeasonPhaseChanged`: Action
- `_applyClientListeners`: Action<TDivisionModel>

---

#### LeagueVisualConfig

**Line:** 705002

**Fields:**

- `LeagueIcon`: Sprite
- `LeagueName`: string

---

#### LeaguesEnabledCondition

**Line:** 565172

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### LegacyIconsInfo

**Line:** 1325355

**Inherits:** IMetadata

**Fields:**

- `m_Legacy_idpi`: LocalizedTexture
- `m_Legacy_mdpi`: LocalizedTexture
- `m_Legacy_hdpi`: LocalizedTexture
- `m_Legacy_xhdpi`: LocalizedTexture
- `m_Legacy_xxhdpi`: LocalizedTexture
- `m_Legacy_xxxhdpi`: LocalizedTexture

---

#### LegacyMetaActivableSet

**Line:** 581102

---

#### LegacyPlayerAuthEntry

**Line:** 534091

---

#### LegacyPlayerMail

**Line:** 561321

**Inherits:** MetaInGameMail

---

#### LegacyServerGameConfigBase

**Line:** 600290

**Inherits:** ServerGameConfigBase

---

#### LegacySharedGameConfigBase

**Line:** 600585

**Inherits:** LegacySharedGameConfigTemplate

---

#### LegacySharedGameConfigTemplate

**Line:** 600571

---

#### LensDistortion

**Line:** 909435

**Inherits:** VolumeComponent

**Fields:**

- `intensity`: ClampedFloatParameter
- `xMultiplier`: ClampedFloatParameter
- `yMultiplier`: ClampedFloatParameter
- `center`: Vector2Parameter
- `scale`: ClampedFloatParameter

---

#### LensFlareCommonSRP

**Line:** 820517

---

#### LensFlareComponentSRP

**Line:** 820743

**Inherits:** MonoBehaviour

**Fields:**

- `m_LensFlareData`: LensFlareDataSRP
- `intensity`: float
- `maxAttenuationDistance`: float
- `maxAttenuationScale`: float
- `distanceAttenuationCurve`: AnimationCurve
- `scaleByDistanceCurve`: AnimationCurve
- `attenuationByLightShape`: bool
- `radialScreenAttenuationCurve`: AnimationCurve
- `useOcclusion`: bool
- `useBackgroundCloudOcclusion`: bool
- `environmentOcclusion`: bool
- `useWaterOcclusion`: bool
- `occlusionRadius`: float
- `sampleCount`: uint
- `occlusionOffset`: float
- `scale`: float
- `allowOffScreen`: bool
- `volumetricCloudOcclusion`: bool
- `occlusionRemapCurve`: TextureCurve
- `lightOverride`: Light

---

#### LensFlareDataElementSRP

**Line:** 820869

**Fields:**

- `lensFlareDataSRP`: LensFlareDataSRP
- `visible`: bool
- `position`: float
- `positionOffset`: Vector2
- `angularOffset`: float
- `translationScale`: Vector2
- `ringThickness`: float
- `hoopFactor`: float
- `noiseAmplitude`: float
- `noiseFrequency`: int
- `noiseSpeed`: float
- `shapeCutOffSpeed`: float
- `shapeCutOffRadius`: float
- `m_LocalIntensity`: float
- `lensFlareTexture`: Texture
- `uniformScale`: float
- `sizeXY`: Vector2
- `allowMultipleElement`: bool
- `m_Count`: int
- `preserveAspectRatio`: bool
- ... (30 more fields)

---

#### LensFlareDataSRP

**Line:** 821009

**Inherits:** ScriptableObject

---

#### LessmoreChatLogger

**Line:** 706477

**Inherits:** ILogger

---

#### LessmoreChatService

**Line:** 707003

**Inherits:** IChatService

**Fields:**

- `_client`: HubConnection
- `_lastSendTime`: DateTimeOffset
- `_spamCount`: int
- `OnConnectionState`: Action<ChatConnectionState>
- `OnIncomingMessage`: Action<string, ChatItem>
- `OnReactionUpdated`: Action<string, long, string, string[]>
- `OnDeletedMessage`: Action<string, long>

---

#### LicensingErrorAnalytic

**Line:** 1587089

**Inherits:** AnalyticsEventBase

**Fields:**

- `licensingErrorType`: string
- `additionalData`: string
- `errorMessage`: string
- `correlationId`: string
- `sessionId`: string

---

#### LicensingInitAnalytic

**Line:** 1587112

**Inherits:** AnalyticsEventBase

**Fields:**

- `licensingProtocolVersion`: string
- `licensingClientVersion`: string
- `channelType`: string
- `initTime`: double
- `isLegacy`: bool
- `sessionId`: string
- `correlationId`: string

---

#### LifetimeServices

**Line:** 222284

---

#### LiftGammaGain

**Line:** 909466

**Inherits:** VolumeComponent

**Fields:**

- `lift`: Vector4Parameter
- `gamma`: Vector4Parameter
- `gain`: Vector4Parameter

---

#### Light

**Line:** 874937

**Inherits:** Behaviour

**Fields:**

- `m_BakedIndex`: int

---

#### Light2D

**Line:** 1362387

**Inherits:** Light2DBase

**Fields:**

- `m_BlendStyleIndex`: int
- `m_FalloffIntensity`: float
- `m_Color`: Color
- `m_Intensity`: float
- `m_LightVolumeIntensity`: float
- `m_LightVolumeEnabled`: bool
- `m_LightCookieSprite`: Sprite
- `m_DeprecatedPointLightCookieSprite`: Sprite
- `m_LightOrder`: int
- `m_AlphaBlendOnOverlap`: bool
- `m_NormalMapDistance`: float
- `m_UseNormalMap`: bool
- `m_ShadowsEnabled`: bool
- `m_ShadowIntensity`: float
- `m_ShadowSoftness`: float
- `m_ShadowSoftnessFalloffIntensity`: float
- `m_ShadowVolumeIntensityEnabled`: bool
- `m_ShadowVolumeIntensity`: float
- `m_Mesh`: Mesh
- `m_PreviousLightCookieSprite`: int
- ... (16 more fields)

---

#### Light2DBase

**Line:** 899954

**Inherits:** MonoBehaviour

---

#### LightAnchor

**Line:** 803513

**Inherits:** MonoBehaviour

**Fields:**

- `m_Distance`: float
- `m_AnchorPositionOverride`: Transform
- `m_AnchorPositionOffset`: Vector3
- `m_Yaw`: float
- `m_Pitch`: float
- `m_Roll`: float

---

#### LightProbeProxyVolume

**Line:** 875664

**Inherits:** Behaviour

---

#### LightProbes

**Line:** 873205

**Inherits:** Object

---

#### LightingSettings

**Line:** 871883

**Inherits:** Object

---

#### LightmapSettings

**Line:** 873200

**Inherits:** Object

---

#### Lightmapping

**Line:** 899110

---

#### LightningView

**Line:** 730951

**Inherits:** GameUnityView

**Fields:**

- `LightningSprite`: SpriteRenderer
- `_sequence`: Sequence

---

#### LimitedReadStream

**Line:** 503443

**Inherits:** Stream

**Fields:**

- `_underlying`: Stream
- `_limit`: int
- `_numReadSoFar`: int

---

#### LineRenderer

**Line:** 873543

**Inherits:** Renderer

---

#### LineStyle

**Line:** 1394557

**Inherits:** IDirectResponseSchema

---

#### LinearIntPath

**Line:** 723094

**Inherits:** IPath

---

#### LinearPath

**Line:** 723140

**Inherits:** IPath

---

#### LinearPath2D

**Line:** 723187

**Inherits:** IPath

---

#### LingerOption

**Line:** 800375

**Fields:**

- `enabled`: bool
- `lingerTime`: int

---

#### Link

**Line:** 1394605

**Inherits:** IDirectResponseSchema

---

#### LinkAccountUiView

**Line:** 728999

**Inherits:** MonoBehaviour

**Fields:**

- `LoginButton`: UnityButton
- `LogoutButton`: UnityButton
- `DeleteAccountButton`: UnityButton
- `ErrorText`: TMP_Text

---

#### LinkClickInTextUiView

**Line:** 729029

**Inherits:** MonoBehaviour

**Fields:**

- `Text`: TMP_Text

---

#### LinkedList

**Line:** 786880

**Fields:**

- `_syncRoot`: object
- `_siInfo`: SerializationInfo

---

#### LinkedListNode

**Line:** 787762

---

#### LinkedListNodeCache

**Line:** 1436077

**Fields:**

- `m_maxNodesAllowed`: int
- `m_NodesCreated`: int

---

#### List

**Line:** 356879

**Fields:**

- `_size`: int
- `_version`: int
- `_syncRoot`: object

---

#### ListBindableAttribute

**Line:** 782272

**Inherits:** Attribute

**Fields:**

- `_isDefault`: bool

---

#### ListChangedEventArgs

**Line:** 810607

---

#### ListChangedEventHandler

**Line:** 810628

---

#### ListDictionary

**Line:** 785357

**Inherits:** IDictionary

**Fields:**

- `version`: int
- `count`: int
- `_syncRoot`: object

---

#### ListFormatter

**Line:** 1321745

**Inherits:** FormatterBase

**Fields:**

- `m_SmartSettings`: SmartSettings

---

#### ListInitExpression

**Line:** 1288237

**Inherits:** Expression

---

#### ListPropertyBag

**Line:** 1465586

---

#### ListView

**Line:** 624617

**Inherits:** BaseListView

**Fields:**

- `m_MakeItem`: Func<VisualElement>
- `m_TemplateMakeItem`: Func<VisualElement>
- `m_ItemTemplate`: VisualTreeAsset
- `m_BindItem`: Action<VisualElement, int>
- `m_UnbindItem`: Action<VisualElement, int>
- `m_DestroyItem`: Action<VisualElement>

---

#### ListViewController

**Line:** 611142

**Inherits:** BaseListViewController

---

#### LiteralText

**Line:** 1322692

**Inherits:** FormatItem

---

#### LiveOpsEventAttribute

**Line:** 562072

**Inherits:** Attribute

---

#### LiveOpsEventContent

**Line:** 562046

**Inherits:** IMetaIntegration

---

#### LiveOpsEventPhase

**Line:** 562639

**Inherits:** DynamicEnum

**Fields:**

- `_indexInPhaseSequence`: int

---

#### LiveOpsEventScheduleInfo

**Line:** 562258

---

#### LiveOpsEventTemplateConfigData

**Line:** 562144

---

#### LiveOpsEventTemplateId

**Line:** 563251

**Inherits:** StringId

---

#### LiveOpsEventTypeRegistry

**Line:** 563225

---

#### LoadingBar

**Line:** 1585810

**Inherits:** MonoBehaviour

**Fields:**

- `OutlineWidth`: float
- `InnerBorderWidth`: float
- `ResizeAutomatically`: bool
- `Progress`: float
- `Background`: RectTransform
- `Outline`: RectTransform
- `ProgressHolder`: RectTransform
- `ProgressFill`: RectTransform
- `AssetBundleDownloadToInstallRatio`: float

---

#### LoadingScreen

**Line:** 1585930

**Inherits:** MonoBehaviour

**Fields:**

- `AssetBundleUrl`: string
- `LoadingBar`: LoadingBar
- `RetryButton`: Button
- `_bundle`: AssetBundle
- `_assetBundleRetrievalAttemptCount`: int
- `_maxLoadingBarProgress`: float
- `_downloading`: bool

---

#### LoadingScreenView

**Line:** 738477

**Inherits:** MonoBehaviour

**Fields:**

- `ConnectingText`: TMP_Text
- `AnimationDuration`: float
- `_seq`: Sequence

---

#### LoadingSpinnerBehaviour

**Line:** 1443864

**Inherits:** SRMonoBehaviour

**Fields:**

- `_dt`: float
- `FrameCount`: int
- `SpinDuration`: float

---

#### LocConfigBuildIntegration

**Line:** 1050959

**Inherits:** GameConfigBuildIntegration

---

#### LocalBuilder

**Line:** 269783

**Inherits:** LocalVariableInfo

**Fields:**

- `name`: string
- `startOffset`: int
- `endOffset`: int

---

#### LocalCertificateSelectionCallback

**Line:** 802778

**Inherits:** MulticastDelegate

---

#### LocalDataStoreSlot

**Line:** 171738

**Fields:**

- `m_mgr`: LocalDataStoreMgr
- `m_slot`: int
- `m_cookie`: long

---

#### LocalDatePattern

**Line:** 1152584

**Inherits:** IPattern

---

#### LocalDateTimePattern

**Line:** 1152993

**Inherits:** IPattern

---

#### LocalServerCodeReceiver

**Line:** 1372928

**Inherits:** ICodeReceiver

**Fields:**

- `_callbackUriTemplate`: string
- `redirectUri`: string

---

#### LocalTimePattern

**Line:** 1153451

**Inherits:** IPattern

---

#### LocalVariableInfo

**Line:** 268121

---

#### Locale

**Line:** 1315030

**Inherits:** ScriptableObject

**Fields:**

- `m_Identifier`: LocaleIdentifier
- `m_Metadata`: MetadataCollection
- `m_LocaleName`: string
- `m_CustomFormatCultureCode`: string
- `m_UseCustomFormatter`: bool
- `m_SortOrder`: ushort
- `m_Formatter`: IFormatProvider

---

#### LocaleMessage

**Line:** 721436

**Inherits:** IMessage

---

#### LocalesProvider

**Line:** 1319093

**Inherits:** ILocalesProvider

**Fields:**

- `m_LoadOperation`: AsyncOperationHandle

---

#### LocalizationDownloadCache

**Line:** 1310968

**Fields:**

- `_log`: LogChannel
- `_downloadDir`: string
- `_lock`: object
- `_cached`: MetaDictionary<LanguageId, LocalizationDownloadCache.LanguageLocalizationFiles>
- `_lastTimestamp`: uint
- `_initTask`: Task

---

#### LocalizationInitSystem

**Line:** 721456

**Inherits:** IInitSystem

---

#### LocalizationLanguage

**Line:** 561668

---

#### LocalizationLanguageProvider

**Line:** 561782

**Fields:**

- `_basePath`: string

---

#### LocalizationSettings

**Line:** 1319183

**Inherits:** ScriptableObject

**Fields:**

- `m_StartupSelectors`: List<IStartupLocaleSelector>
- `m_AvailableLocales`: ILocalesProvider
- `m_AssetDatabase`: LocalizedAssetDatabase
- `m_StringDatabase`: LocalizedStringDatabase
- `m_Metadata`: MetadataCollection
- `m_PreloadBehavior`: PreloadBehavior
- `m_InitializeSynchronously`: bool
- `m_SelectedLocaleAsync`: AsyncOperationHandle<Locale>
- `m_ProjectLocale`: Locale

---

#### LocalizationTable

**Line:** 1317788

**Inherits:** ScriptableObject

**Fields:**

- `m_LocaleId`: LocaleIdentifier
- `m_SharedData`: SharedTableData
- `m_Metadata`: MetadataCollection
- `m_TableData`: List<TableEntryData>

---

#### LocalizationsBuild

**Line:** 600224

**Inherits:** IMetaIntegrationConstructible

**Fields:**

- `_fetcher`: BuildSourceFetcherAndMetadata

---

#### LocalizationsBuildParameters

**Line:** 600132

**Inherits:** IMetaIntegration

**Fields:**

- `DefaultSource`: GameConfigBuildSource

---

#### LocalizationsEnabledCondition

**Line:** 561808

**Inherits:** MetaplayFeatureEnabledConditionAttribute

---

#### LocalizeAudioClipEvent

**Line:** 1326886

**Inherits:** LocalizedAssetEvent

---

#### LocalizeSpriteEvent

**Line:** 1327062

**Inherits:** LocalizedAssetEvent

---

#### LocalizeStringEvent

**Line:** 1327072

**Inherits:** LocalizedMonoBehaviour

**Fields:**

- `m_StringReference`: LocalizedString
- `m_FormatArguments`: List<Object>
- `m_UpdateString`: UnityEventString

---

#### LocalizeTextureEvent

**Line:** 1327137

**Inherits:** LocalizedAssetEvent

---

#### LocalizedAsset

**Line:** 1315609

**Fields:**

- `m_SelectedLocaleChanged`: Action<Locale>
- `m_PreviousLoadingOperation`: AsyncOperationHandle<TObject>
- `m_CurrentValue`: TObject

---

#### LocalizedAssetBase

**Line:** 1315432

**Inherits:** LocalizedReference

---

#### LocalizedAssetBehaviour

**Line:** 1326896

**Fields:**

- `m_LocalizedAssetReference`: TReference

---

#### LocalizedAssetDatabase

**Line:** 1318428

**Inherits:** LocalizedDatabase

---

#### LocalizedAssetEvent

**Line:** 1326990

**Fields:**

- `m_UpdateAsset`: TEvent

---

#### LocalizedAssetProperty

**Line:** 1327905

**Inherits:** ITrackedProperty

**Fields:**

- `m_Localized`: LocalizedAssetBase
- `m_PropertyPath`: string

---

#### LocalizedAssetTable

**Line:** 1315860

**Inherits:** LocalizedTable

---

#### LocalizedAudioClip

**Line:** 1315168

**Inherits:** LocalizedAsset

---

#### LocalizedDatabase

**Line:** 1318577

**Fields:**

- `m_DefaultTableReference`: TableReference
- `m_CustomTableProvider`: ITableProvider
- `m_CustomTablePostprocessor`: ITablePostprocessor
- `m_AsynchronousBehaviour`: AsynchronousBehaviour
- `m_UseFallback`: bool
- `m_ReleaseNextFrame`: Action<AsyncOperationHandle>

---

#### LocalizedFont

**Line:** 1315411

**Inherits:** LocalizedAsset

---

#### LocalizedGameObject

**Line:** 1315198

**Inherits:** LocalizedAsset

---

#### LocalizedGameObjectEvent

**Line:** 1327036

**Inherits:** LocalizedAssetEvent

**Fields:**

- `m_Current`: GameObject

---

#### LocalizedMaterial

**Line:** 1315258

**Inherits:** LocalizedAsset

---

#### LocalizedMesh

**Line:** 1315228

**Inherits:** LocalizedAsset

---

#### LocalizedMonoBehaviour

**Line:** 1327052

**Inherits:** MonoBehaviour

---

#### LocalizedObject

**Line:** 1315288

**Inherits:** LocalizedAsset

---

#### LocalizedProductDescription

**Line:** 1406881

**Fields:**

- `googleLocale`: TranslationLocale
- `title`: string
- `description`: string

---

#### LocalizedReference

**Line:** 1315922

**Inherits:** CustomBinding

**Fields:**

- `m_TableReference`: TableReference
- `m_TableEntryReference`: TableEntryReference
- `m_FallbackState`: FallbackBehavior
- `m_WaitForCompletion`: bool
- `m_ActivatedCount`: int

---

#### LocalizedSprite

**Line:** 1315318

**Inherits:** LocalizedAsset

---

#### LocalizedString

**Line:** 1316263

**Inherits:** LocalizedReference

**Fields:**

- `m_LocalVariables`: List<VariableNameValuePair>
- `m_ChangeHandler`: CallbackArray<LocalizedString.ChangeHandler>
- `m_CurrentStringChangedValue`: string
- `m_WaitingForVariablesEndUpdate`: bool
- `ValueChanged`: Action<IVariable>
- `m_UxmlLocalVariables`: List<LocalVariable>

---

#### LocalizedStringDatabase

**Line:** 1318951

**Inherits:** LocalizedDatabase

**Fields:**

- `m_MissingTranslationState`: MissingTranslationBehavior
- `m_NoTranslationFoundMessage`: string
- `m_SmartFormat`: SmartFormatter
- `m_MissingTranslationTable`: StringTable

---

#### LocalizedStringProperty

**Line:** 1327940

**Inherits:** ITrackedProperty

**Fields:**

- `m_Localized`: LocalizedString
- `m_PropertyPath`: string

---

#### LocalizedStringTable

**Line:** 1316482

**Inherits:** LocalizedTable

---

#### LocalizedTable

**Line:** 1316539

**Fields:**

- `m_TableReference`: TableReference
- `m_SelectedLocaleChanged`: Action<Locale>

---

#### LocalizedTexture

**Line:** 1315348

**Inherits:** LocalizedAsset

---

#### LocalizedTmpFont

**Line:** 1315381

**Inherits:** LocalizedAsset

---

#### LocalizerBase

**Line:** 721248

---

#### Lock

**Line:** 179874

**Fields:**

- `_lock`: object

---

#### LockRecursionException

**Line:** 179032

**Inherits:** Exception

---

#### LockedComponent

**Line:** 729487

**Inherits:** IComponent

---

#### LockedEventSystem

**Line:** 702253

**Inherits:** ReactiveSystem

---

#### LockedListenerComponent

**Line:** 699843

**Inherits:** IComponent

**Fields:**

- `value`: List<ILockedListener>

---

#### LockedRemovedEventSystem

**Line:** 702274

**Inherits:** ReactiveSystem

---

#### LockedRemovedListenerComponent

**Line:** 699856

**Inherits:** IComponent

**Fields:**

- `value`: List<ILockedRemovedListener>

---

#### LogChannel

**Line:** 519945

**Inherits:** MetaLoggerBase

---

#### LogDefineOptions

**Line:** 1533278

---

#### LogDelegate

**Line:** 1596334

**Inherits:** MulticastDelegate

---

#### LogEntryUiView

**Line:** 719938

**Inherits:** MonoBehaviour

**Fields:**

- `LogContainer`: RectTransform
- `Background`: Image
- `MessageText`: TMP_Text
- `TimeText`: TMP_Text

---

#### LogHistoryTracker

**Line:** 1311692

**Inherits:** IDisposable

**Fields:**

- `_started`: bool
- `_logRingBufferLock`: object
- `_logRingBuffer`: Queue<ClientLogEntry>

---

#### LogTemplateFormatter

**Line:** 503497

---

#### Logger

**Line:** 1596352

**Fields:**

- `OnLog`: LogDelegate

---

#### LoggerExternalScopeProvider

**Line:** 1533494

**Inherits:** IExternalScopeProvider

---

#### LoggerFactory

**Line:** 1554782

**Inherits:** ILoggerFactory

**Fields:**

- `_disposed`: bool
- `_filterOptions`: LoggerFilterOptions
- `_scopeProvider`: IExternalScopeProvider

---

#### LoggerFactoryOptions

**Line:** 1554848

---

#### LoggerFilterOptions

**Line:** 1555111

---

#### LoggerFilterRule

**Line:** 1555162

---

#### LoggerMessageAttribute

**Line:** 1536556

**Inherits:** Attribute

---

#### LoggingInitializeSystem

**Line:** 693231

**Inherits:** IInitializeSystem

---

#### LoggingQueue

**Line:** 693151

**Inherits:** IComponent

**Fields:**

- `Exceptions`: Queue<Exception>
- `Logs`: Queue<string>

---

#### LogicalCallContext

**Line:** 223431

**Inherits:** ISerializable

**Fields:**

- `m_Datastore`: Hashtable
- `m_RemotingData`: CallContextRemotingData
- `m_SecurityData`: CallContextSecurityData
- `m_HostContext`: object
- `m_IsCorrelationMgr`: bool

---

#### LoginDebugDiagnostics

**Line:** 557026

**Fields:**

- `Timestamp`: MetaTime
- `Session`: LoginSessionDebugDiagnostics
- `ServerConnection`: LoginServerConnectionDebugDiagnostics
- `Transport`: LoginTransportDebugDiagnostics
- `IncidentReport`: LoginIncidentReportDebugDiagnostics
- `MainLoop`: LoginMainLoopDebugDiagnostics
- `CurrentPauseDuration`: Nullable<MetaDuration>
- `DurationSincePauseEnd`: Nullable<MetaDuration>
- `DurationSinceConnectionUpdate`: Nullable<MetaDuration>
- `DurationSincePlayerContextUpdate`: Nullable<MetaDuration>
- `ExpectSessionResumptionPing`: bool
- `DiagnosticsError`: string

---

#### LoginIncidentReportDebugDiagnostics

**Line:** 557319

**Fields:**

- `CurrentPendingIncidents`: int
- `CurrentRequestedIncidents`: int
- `TotalUploadRequestMessages`: int
- `TotalRequestedIncidents`: int
- `AcknowledgedIncidents`: int
- `UploadsAttempted`: int
- `UploadUnavailable`: int
- `UploadException`: int
- `UploadTooLarge`: int
- `UploadsSent`: int

---

#### LoginMainLoopDebugDiagnostics

**Line:** 557354

**Fields:**

- `UpdatesStarted`: int
- `UpdatesEndedPrematurely`: int
- `UpdatesEndedNormally`: int

---

#### LoginServerConnectionDebugDiagnostics

**Line:** 557193

**Fields:**

- `TransportsCreated`: int
- `SessionMessageEnqueuesAttempted`: int
- `SessionMessageImmediateSendEnqueues`: int
- `FirstSessionMessageSentAtMS`: long
- `SessionMessagesDelayedSendEnqueues`: int
- `SessionMessagesEnqueues`: int
- `SessionMessagesDelayedSent`: int
- `StreamClosedErrors`: int
- `StreamIOFailedErrors`: int
- `StreamExecutorErrors`: int
- `ConnectTimeoutErrors`: int
- `HeaderTimeoutErrors`: int
- `ReadTimeoutErrors`: int
- `WriteTimeoutErrors`: int
- `OtherErrors`: int
- `HellosSent`: int
- `InitialLoginsSent`: int
- `ResumptionLoginsSent`: int
- `HellosReceived`: int
- `LoginSuccessesReceived`: int
- ... (3 more fields)

---

#### LoginSessionDebugDiagnostics

**Line:** 557087

---

#### LoginTransportDebugDiagnostics

**Line:** 557264

**Fields:**

- `WritesStarted`: int
- `WritesCompleted`: int
- `ReadsStarted`: int
- `ReadsCompleted`: int
- `MetaMessageEnqueuesAttempted`: int
- `MetaMessageUnconnectedEnqueuesAttempted`: int
- `MetaMessageDisposedEnqueuesAttempted`: int
- `MetaMessagePacketSizesExceeded`: int
- `MetaMessageClosingEnqueuesAttempted`: int
- `MetaMessagesEnqueued`: int
- `PacketEnqueuesAttempted`: int
- `PacketsEnqueued`: int
- `BytesEnqueued`: int
- `MetaMessagesWritten`: int
- `PacketsWritten`: int
- `BytesWritten`: int
- `BytesRead`: int
- `PacketsRead`: int
- `MetaMessagesRead`: int
- `MetaMessagesReceived`: int

---

#### LongField

**Line:** 624745

**Inherits:** TextValueField

---

#### LongPlugin

**Line:** 1429152

**Inherits:** ABSTweenPlugin

---

#### LongPressButton

**Line:** 1506573

**Inherits:** Button

**Fields:**

- `_handled`: bool
- `_pressed`: bool
- `_pressedTime`: float
- `LongPressDuration`: float

---

#### LongTrackedProperty

**Line:** 1328911

**Inherits:** TrackedProperty

---

#### LongVariable

**Line:** 1324621

**Inherits:** Variable

---

#### LookDirectionComponent

**Line:** 709181

**Inherits:** IComponent

**Fields:**

- `Value`: Vector2

---

#### LookerDataSourceSpec

**Line:** 1394641

**Inherits:** IDirectResponseSchema

---

#### Lookup

**Line:** 1282823

**Fields:**

- `comparer`: IEqualityComparer<TKey>
- `count`: int

---

#### LoopCountComponent

**Line:** 696244

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### LoopExpression

**Line:** 1288262

**Inherits:** Expression

---

#### LootParticle

**Line:** 709921

**Inherits:** MonoBehaviour

**Fields:**

- `_sequence`: Sequence

---

#### LootUiParticleView

**Line:** 715902

**Inherits:** MonoBehaviour

---

#### LootView

**Line:** 709980

**Inherits:** GameUnityView

**Fields:**

- `CoinParticle`: LootParticle
- `HammerParticle`: LootParticle

---

#### MACTripleDES

**Line:** 218450

**Inherits:** KeyedHashAlgorithm

**Fields:**

- `m_encryptor`: ICryptoTransform
- `_cs`: CryptoStream
- `_ts`: TailStream
- `m_bytesPerBlock`: int
- `des`: TripleDES

---

#### MD2

**Line:** 1449347

**Inherits:** HashAlgorithm

---

#### MD2Managed

**Line:** 1449359

**Inherits:** MD2

**Fields:**

- `count`: int

---

#### MD4

**Line:** 1449394

**Inherits:** HashAlgorithm

---

#### MD4Managed

**Line:** 1449406

**Inherits:** MD4

---

#### MD5

**Line:** 218544

**Inherits:** HashAlgorithm

---

#### MD5CryptoServiceProvider

**Line:** 219761

**Inherits:** MD5

**Fields:**

- `count`: ulong
- `_ProcessingBufferCount`: int

---

#### MacAppStore

**Line:** 1405893

---

#### MailAddress

**Line:** 801210

---

#### MailFeature

**Line:** 721518

**Inherits:** Feature

---

#### MailSystem

**Line:** 721527

**Inherits:** IExecuteSystem

---

#### MainCameraView

**Line:** 685423

**Inherits:** MonoBehaviour

**Fields:**

- `Cam`: Camera
- `_moveTween`: Tween
- `LockPos`: bool

---

#### MainCanvas

**Line:** 693624

**Inherits:** UiUnityView

**Fields:**

- `Canvas`: Canvas
- `CanvasScaler`: CanvasScaler
- `_lastAdjustedAspect`: float
- `_mainCamera`: Camera

---

#### MainCanvasComponent

**Line:** 693248

**Inherits:** IComponent

---

#### MainCanvasConfigComponent

**Line:** 698807

**Inherits:** IComponent

**Fields:**

- `Value`: IMainCanvasConfig

---

#### MainCanvasFeature

**Line:** 693301

**Inherits:** Feature

---

#### MainCanvasInitializeSystem

**Line:** 693694

**Inherits:** IInitializeSystem

---

#### MainChatUIModel

**Line:** 707178

**Fields:**

- `_currentChatRoomId`: string
- `_subscribedGuildId`: string
- `OnWorldUnreadCount`: Action<int>
- `OnGuildUnreadCount`: Action<int>
- `OnReset`: Action
- `OnChatMessage`: Action<ChatItem>
- `OnChatReaction`: Action<long, string, string[]>

---

#### MainGameProgressPassBubbleView

**Line:** 726894

**Inherits:** MonoBehaviour

**Fields:**

- `OpenButton`: UnityButton
- `Content`: GameObject

---

#### MainGameProgressPassRedDotUiView

**Line:** 726934

**Inherits:** RedDotUiView

---

#### MainLightShadowCasterPass

**Line:** 920102

**Inherits:** ScriptableRenderPass

**Fields:**

- `renderTargetWidth`: int
- `renderTargetHeight`: int
- `m_ShadowCasterCascadesCount`: int
- `m_CreateEmptyShadowmap`: bool
- `m_SetKeywordForEmptyShadowmap`: bool
- `m_EmptyShadowmapNeedsClear`: bool
- `m_CascadeBorder`: float
- `m_MaxShadowDistanceSq`: float
- `m_EmptyMainLightShadowmapTexture`: RTHandle
- `m_MainLightShadowDescriptor`: RenderTextureDescriptor

---

#### MainScreenTypeComponent

**Line:** 721582

**Inherits:** IComponent

**Fields:**

- `Value`: MainScreenType

---

#### MainThreadDispatcherComponent

**Line:** 696124

**Inherits:** IComponent

**Fields:**

- `Value`: Dispatcher

---

#### MainThreadDispatcherSystem

**Line:** 696186

**Inherits:** IInitializeSystem

---

#### MainUiView

**Line:** 721811

**Inherits:** UiUnityView

**Fields:**

- `InventoryParent`: Transform

---

#### ManagementBaseObject

**Line:** 1585109

**Inherits:** Component

---

#### ManagementClass

**Line:** 1585141

**Inherits:** ManagementObject

---

#### ManagementObject

**Line:** 1585161

**Inherits:** ManagementBaseObject

---

#### ManagementObjectCollection

**Line:** 1585196

---

#### ManifestResourceInfo

**Line:** 265609

---

#### Manipulator

**Line:** 641440

**Inherits:** IManipulator

**Fields:**

- `m_Target`: VisualElement

---

#### ManualResetEvent

**Line:** 179047

**Inherits:** EventWaitHandle

---

#### ManualResetEventSlim

**Line:** 179282

**Inherits:** IDisposable

**Fields:**

- `m_lock`: object
- `m_eventObj`: ManualResetEvent
- `m_combinedState`: int

---

#### ManualRule

**Line:** 1394701

**Inherits:** IDirectResponseSchema

---

#### ManualRuleGroup

**Line:** 1394737

**Inherits:** IDirectResponseSchema

---

#### MapElementComponent

**Line:** 710374

**Inherits:** IComponent

---

#### MapElementView

**Line:** 710470

**Inherits:** GameUnityView

---

#### MapZone

**Line:** 1150887

**Inherits:** IEquatable

---

#### MarketingCheatContainer

**Line:** 686240

**Inherits:** AbstractCheatContainer

**Fields:**

- `_mainCanvasActive`: bool

---

#### MarshalAsAttribute

**Line:** 229863

**Inherits:** Attribute

**Fields:**

- `MarshalCookie`: string
- `MarshalType`: string
- `MarshalTypeRef`: Type
- `SafeArrayUserDefinedSubType`: Type
- `utype`: UnmanagedType
- `ArraySubType`: UnmanagedType
- `SafeArraySubType`: VarEnum
- `SizeConst`: int
- `IidParameterIndex`: int
- `SizeParamIndex`: short

---

#### MarshalByRefObject

**Line:** 176325

**Fields:**

- `_identity`: object

---

#### MarshalByValueComponent

**Line:** 782391

**Inherits:** IComponent

**Fields:**

- `_site`: ISite
- `_events`: EventHandlerList

---

#### MarshalDirectiveException

**Line:** 228584

**Inherits:** SystemException

---

#### Mask

**Line:** 1355486

**Inherits:** UIBehaviour

**Fields:**

- `m_RectTransform`: RectTransform
- `m_ShowMaskGraphic`: bool
- `m_Graphic`: Graphic
- `m_MaskMaterial`: Material
- `m_UnmaskMaterial`: Material

---

#### MaskUtilities

**Line:** 1355650

---

#### MaskableGraphic

**Line:** 1355549

**Inherits:** Graphic

**Fields:**

- `m_ShouldRecalculateStencil`: bool
- `m_MaskMaterial`: Material
- `m_ParentMask`: RectMask2D
- `m_Maskable`: bool
- `m_IsMaskingGraphic`: bool
- `m_IncludeForMasking`: bool
- `m_ShouldRecalculate`: bool
- `m_StencilValue`: int

---

#### Match

**Line:** 775699

**Inherits:** Group

---

#### MatchCollection

**Line:** 775826

**Inherits:** IList

**Fields:**

- `_done`: bool
- `_startat`: int
- `_prevlen`: int

---

#### MatchEvaluator

**Line:** 776192

**Inherits:** MulticastDelegate

---

#### MatchedDeveloperMetadata

**Line:** 1394785

**Inherits:** IDirectResponseSchema

---

#### MatchedValueRange

**Line:** 1394833

**Inherits:** IDirectResponseSchema

---

#### Matcher

**Line:** 1545498

**Fields:**

- `_toStringCache`: string
- `_toStringBuilder`: StringBuilder
- `_hash`: int
- `_isHashCached`: bool

---

#### MatcherException

**Line:** 1547567

**Inherits:** Exception

---

#### Material

**Line:** 874205

**Inherits:** Object

---

#### MaterialParameter

**Line:** 827757

**Inherits:** VolumeParameter

---

#### MaterialPropertyBlock

**Line:** 873582

---

#### MaterialReferenceManager

**Line:** 1220023

**Fields:**

- `m_FontMaterialReferenceLookup`: Dictionary<int, Material>
- `m_FontAssetReferenceLookup`: Dictionary<int, TMP_FontAsset>
- `m_SpriteAssetReferenceLookup`: Dictionary<int, TMP_SpriteAsset>
- `m_ColorGradientReferenceLookup`: Dictionary<int, TMP_ColorGradient>

---

#### MaxBytesExceededException

**Line:** 1518499

**Inherits:** CryptoException

---

#### MaxCollectionSizeAttribute

**Line:** 600888

**Inherits:** Attribute

---

#### MaxFloatParameter

**Line:** 827219

**Inherits:** FloatParameter

**Fields:**

- `max`: float

---

#### MaxHpComponent

**Line:** 709143

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### MaxHpEventSystem

**Line:** 702358

**Inherits:** ReactiveSystem

---

#### MaxHpListenerComponent

**Line:** 699908

**Inherits:** IComponent

**Fields:**

- `value`: List<IMaxHpListener>

---

#### MaxIntParameter

**Line:** 827054

**Inherits:** IntParameter

**Fields:**

- `max`: int

---

#### MaxLengthAttribute

**Line:** 1509531

**Inherits:** ValidationAttribute

---

#### MaxUrlLengthInterceptor

**Line:** 1497821

**Inherits:** IHttpExecuteInterceptor

---

#### MaxedComponent

**Line:** 729454

**Inherits:** IComponent

---

#### MaxedEventSystem

**Line:** 702316

**Inherits:** ReactiveSystem

---

#### MaxedListenerComponent

**Line:** 699882

**Inherits:** IComponent

**Fields:**

- `value`: List<IMaxedListener>

---

#### MaxedRemovedEventSystem

**Line:** 702337

**Inherits:** ReactiveSystem

---

#### MaxedRemovedListenerComponent

**Line:** 699895

**Inherits:** IComponent

**Fields:**

- `value`: List<IMaxedRemovedListener>

---

#### MaybeNullAttribute

**Line:** 275843

**Inherits:** Attribute

---

#### MaybeNullWhenAttribute

**Line:** 275863

**Inherits:** Attribute

---

#### MeansImplicitUseAttribute

**Line:** 869269

**Inherits:** Attribute

---

#### MeasurementCallback

**Line:** 1423393

---

#### MediaDownloader

**Line:** 1504653

**Inherits:** IMediaDownloader

**Fields:**

- `chunkSize`: int
- `ProgressChanged`: Action<IDownloadProgress>

---

#### MediaTypeHeaderValue

**Line:** 1490598

**Inherits:** ICloneable

---

#### MediaTypeWithQualityHeaderValue

**Line:** 1490652

**Inherits:** MediaTypeHeaderValue

---

#### MemoableResetException

**Line:** 1517863

**Inherits:** InvalidCastException

---

#### MemoryLogger

**Line:** 1496208

**Inherits:** BaseLogger

---

#### MemoryManager

**Line:** 465037

---

#### MemoryPool

**Line:** 465975

---

#### MemorySnapshotMetadata

**Line:** 837496

---

#### MemoryStream

**Line:** 467924

**Inherits:** Stream

**Fields:**

- `_origin`: int
- `_position`: int
- `_length`: int
- `_capacity`: int
- `_expandable`: bool
- `_writable`: bool
- `_exposable`: bool
- `_isOpen`: bool
- `_lastReadTask`: Task<int>

---

#### MemoryTraceWriter

**Line:** 1040997

**Inherits:** ITraceWriter

---

#### MergeCellsRequest

**Line:** 1394881

**Inherits:** IDirectResponseSchema

---

#### MergeFailedEventArgs

**Line:** 1086995

**Inherits:** EventArgs

---

#### MergeFailedEventHandler

**Line:** 1087017

**Inherits:** MulticastDelegate

---

#### MergePossibleComponent

**Line:** 723420

**Inherits:** IComponent

---

#### MergePossibleEventSystem

**Line:** 702379

**Inherits:** ReactiveSystem

---

#### MergePossibleListenerComponent

**Line:** 699921

**Inherits:** IComponent

**Fields:**

- `value`: List<IMergePossibleListener>

---

#### MergePossibleRemovedEventSystem

**Line:** 702400

**Inherits:** ReactiveSystem

---

#### MergePossibleRemovedListenerComponent

**Line:** 699934

**Inherits:** IComponent

**Fields:**

- `value`: List<IMergePossibleRemovedListener>

---

#### Mesh

**Line:** 875744

**Inherits:** Object

---

#### MeshFilter

**Line:** 875154

**Inherits:** Component

---

#### MeshGenerationContext

**Line:** 643489

**Fields:**

- `m_Painter2D`: Painter2D
- `m_MeshWriteDataPool`: MeshWriteDataPool
- `m_Allocator`: TempMeshAllocatorImpl
- `m_MeshGenerationDeferrer`: MeshGenerationDeferrer
- `m_MeshGenerationNodeManager`: MeshGenerationNodeManager

---

#### MeshRenderer

**Line:** 875685

**Inherits:** Renderer

---

#### MeshWriteData

**Line:** 643445

---

#### Message

**Line:** 1319698

---

#### MessageBase

**Line:** 1448314

**Fields:**

- `_type`: int
- `_flags`: NtlmFlags

---

#### MessageDispatcher

**Line:** 1306289

**Inherits:** BasicMessageDispatcher

**Fields:**

- `_serverConnection`: ServerConnection

---

#### MessageEventArgs

**Line:** 890514

**Fields:**

- `playerId`: int

---

#### MessageFragment

**Line:** 1319537

**Fields:**

- `m_OriginalString`: string
- `m_StartIndex`: int
- `m_EndIndex`: int
- `m_CachedToString`: string

---

#### MessageHandler

**Line:** 556919

---

#### MessageRetentionSettingsDto

**Line:** 1529404

**Inherits:** IEquatable

---

#### MessageRoutingRule

**Line:** 499009

**Inherits:** Attribute

---

#### MessageRoutingRuleEntityChannel

**Line:** 499060

**Inherits:** MessageRoutingRule

---

#### MessageRoutingRuleOwnedPlayer

**Line:** 499042

**Inherits:** MessageRoutingRule

---

#### MessageRoutingRuleProtocol

**Line:** 499018

**Inherits:** MessageRoutingRule

---

#### MessageRoutingRuleSession

**Line:** 499027

**Inherits:** MessageRoutingRule

---

#### MessageSettings

**Line:** 1565224

**Fields:**

- `textSize`: float
- `alignment`: SectionAlignment
- `textColor`: string
- `linkTextColor`: string
- `underlineLink`: bool

---

#### MessageTransport

**Line:** 547403

**Inherits:** IMessageTransport

---

#### MessageTransportConnectionUtil

**Line:** 548843

**Fields:**

- `Stream`: NetworkStream
- `Hostname`: string
- `Af`: AddressFamily
- `DnsResolutionDuration`: TimeSpan
- `TcpOpenDuration`: TimeSpan

---

#### MessageTransportInfoWrapperMessage

**Line:** 498582

**Inherits:** MetaMessage

---

#### MessageTransportLatencySampleMessage

**Line:** 498611

**Inherits:** MetaMessage

---

#### MessageTransportPingTracker

**Line:** 548982

**Fields:**

- `_pingSentAt`: Dictionary<int, DateTime>

---

#### MessageTransportWriteFence

**Line:** 547270

---

#### MetaActionResult

**Line:** 601407

---

#### MetaActionResultUnhandledException

**Line:** 601491

**Inherits:** MetaActionResult

---

#### MetaActivableCategoryId

**Line:** 579392

**Inherits:** StringId

---

#### MetaActivableCategoryMetadataAttribute

**Line:** 579402

**Inherits:** PreserveAttribute

---

#### MetaActivableConfigDataAttribute

**Line:** 579489

**Inherits:** Attribute

---

#### MetaActivableCooldownSpec

**Line:** 579160

---

#### MetaActivableKindId

**Line:** 579382

**Inherits:** StringId

---

#### MetaActivableKindMetadataAttribute

**Line:** 579447

**Inherits:** PreserveAttribute

---

#### MetaActivableLifetimeSpec

**Line:** 579308

---

#### MetaActivableParams

**Line:** 579330

**Fields:**

- `IsEnabled`: bool
- `AdditionalConditions`: List<PlayerCondition>
- `Lifetime`: MetaActivableLifetimeSpec
- `IsTransient`: bool
- `Schedule`: MetaScheduleBase
- `MaxActivations`: Nullable<int>
- `MaxTotalConsumes`: Nullable<int>
- `MaxConsumesPerActivation`: Nullable<int>
- `Cooldown`: MetaActivableCooldownSpec
- `AllowActivationAdjustment`: bool

---

#### MetaActivablePrecursorCondition

**Line:** 578857

---

#### MetaActivableRepository

**Line:** 580087

**Fields:**

- `_categories`: MetaDictionary<MetaActivableCategoryId, MetaActivableRepository.CategorySpec>
- `_kinds`: MetaDictionary<MetaActivableKindId, MetaActivableRepository.KindSpec>
- `_concreteActivableStateTypeToKindId`: Dictionary<Type, MetaActivableKindId>

---

#### MetaActivableRepositoryConfig

**Line:** 579551

---

#### MetaActivableSet

**Line:** 580453

**Fields:**

- `_activableStates`: MetaDictionary<TId, TActivableState>
- `_erroneousActivableStates`: MetaDictionary<TId, TActivableState>

---

#### MetaActivableSetAttribute

**Line:** 579524

**Inherits:** Attribute

---

#### MetaActivableState

**Line:** 581586

---

#### MetaActivableStateStorage

**Line:** 581166

---

#### MetaActivableTimelineSettings

**Line:** 579061

**Inherits:** IGameConfigBuildTimeValidate

---

#### MetaActivableVisibleStatus

**Line:** 581088

---

#### MetaAllowNondeterministicCollectionAttribute

**Line:** 601083

**Inherits:** Attribute

---

#### MetaAssertException

**Line:** 503737

**Inherits:** Exception

---

#### MetaCalendarPeriodTypeConverter

**Line:** 532487

**Inherits:** TypeConverter

---

#### MetaClientLogger

**Line:** 503518

**Inherits:** MetaLoggerBase

---

#### MetaConfigId

**Line:** 503555

---

#### MetaDelay

**Line:** 527795

**Fields:**

- `OnFinished`: Action

---

#### MetaDescriptionAttribute

**Line:** 498957

**Inherits:** Attribute

---

#### MetaDeserializationConstructorAttribute

**Line:** 600784

**Inherits:** Attribute

---

#### MetaDeserializationConvertFromConcreteDerivedTypeAttribute

**Line:** 529044

**Inherits:** MetaDeserializationConverterAttributeBase

**Fields:**

- `_concreteType`: Type

---

#### MetaDeserializationConvertFromConcreteDerivedTypeStructAttribute

**Line:** 529062

**Inherits:** MetaDeserializationConverterAttributeBase

**Fields:**

- `_concreteType`: Type

---

#### MetaDeserializationConvertFromIntegrationImplementationAttribute

**Line:** 529080

**Inherits:** MetaDeserializationConverterAttributeBase

---

#### MetaDeserializationConvertFromStructAttribute

**Line:** 529029

**Inherits:** MetaDeserializationConverterAttributeBase

---

#### MetaDeserializationConverter

**Line:** 529104

---

#### MetaDeserializationConverterAttributeBase

**Line:** 529135

**Inherits:** Attribute

---

#### MetaDictionary

**Line:** 511398

**Fields:**

- `_count`: int
- `_nextFreeEntry`: int
- `_iterationFirst`: int
- `_iterationLast`: int
- `_version`: uint
- `_pendingSerializationInfo`: SerializationInfo

---

#### MetaEventLog

**Line:** 573864

**Fields:**

- `RunningEntryId`: int
- `LatestSegmentEntries`: List<TEntry>
- `RunningSegmentId`: int
- `PreviousSegmentLastEntryUniqueId`: MetaUInt128
- `OldestAvailableSegmentId`: int
- `OldestPossiblyExistingPersistedSegmentId`: int
- `HasOngoingSegmentDeletionInBackground`: bool
- `_legacyPersistedSegmentMetadatas`: List<LegacyMetaEventLogSegmentMetadata>

---

#### MetaEventLogEntry

**Line:** 573782

---

#### MetaFormClassValidatorAttribute

**Line:** 572914

**Inherits:** Attribute

---

#### MetaFormConfigLibraryItemReference

**Line:** 572516

**Inherits:** Attribute

---

#### MetaFormDeprecatedAttribute

**Line:** 572476

**Inherits:** Attribute

---

#### MetaFormDisplayPropsAttribute

**Line:** 572634

**Inherits:** MetaFormFieldDecoratorBaseAttribute

---

#### MetaFormDontCaptureDefaultAttribute

**Line:** 572506

**Inherits:** Attribute

---

#### MetaFormExcludeDerivedTypeAttribute

**Line:** 572578

**Inherits:** MetaFormFieldDecoratorBaseAttribute

---

#### MetaFormFieldContextAttribute

**Line:** 572357

**Inherits:** MetaFormFieldMultiDecoratorBaseAttribute

**Fields:**

- `Key`: string
- `Value`: object

---

#### MetaFormFieldCustomValidatorAttribute

**Line:** 572439

**Inherits:** MetaFormFieldValidatorBaseAttribute

**Fields:**

- `_validatorType`: Type

---

#### MetaFormFieldDecoratorBaseAttribute

**Line:** 572310

**Inherits:** Attribute

---

#### MetaFormFieldMultiDecoratorBaseAttribute

**Line:** 572334

**Inherits:** Attribute

---

#### MetaFormFieldTypeHintAttribute

**Line:** 572380

**Inherits:** MetaFormFieldDecoratorBaseAttribute

---

#### MetaFormFieldValidatorBaseAttribute

**Line:** 572408

**Inherits:** MetaFormFieldMultiDecoratorBaseAttribute

---

#### MetaFormHiddenAttribute

**Line:** 572486

**Inherits:** Attribute

---

#### MetaFormLayoutOrderHintAttribute

**Line:** 572606

**Inherits:** MetaFormFieldDecoratorBaseAttribute

---

#### MetaFormNotEditableAttribute

**Line:** 572537

**Inherits:** MetaFormFieldDecoratorBaseAttribute

---

#### MetaFormRangeAttribute

**Line:** 572727

**Inherits:** MetaFormFieldTypeHintAttribute

---

#### MetaFormTextAreaAttribute

**Line:** 572684

**Inherits:** MetaFormFieldTypeHintAttribute

---

#### MetaFormUseAsContextAttribute

**Line:** 572496

**Inherits:** Attribute

---

#### MetaFormValidator

**Line:** 572877

---

#### MetaGameConfigBuildConstructorAttribute

**Line:** 587129

**Inherits:** Attribute

---

#### MetaHttpClient

**Line:** 549354

**Inherits:** IDisposable

**Fields:**

- `_httpClient`: HttpClient

---

#### MetaHttpRequestError

**Line:** 549295

**Inherits:** Exception

---

#### MetaHttpResponse

**Line:** 549250

**Inherits:** IDisposable

---

#### MetaInGameMail

**Line:** 561261

---

#### MetaLoggerBase

**Line:** 519866

**Inherits:** IMetaLogger

---

#### MetaMessage

**Line:** 520003

---

#### MetaMessageAttribute

**Line:** 498982

**Inherits:** Attribute

---

#### MetaMessageRepository

**Line:** 557425

**Fields:**

- `_specFromCode`: Dictionary<int, MetaMessageSpec>
- `_specFromType`: Dictionary<Type, MetaMessageSpec>

---

#### MetaMessageSpec

**Line:** 557387

---

#### MetaNft

**Line:** 581940

**Inherits:** ISchemaMigratable

**Fields:**

- `TokenId`: NftId
- `OwnerEntity`: EntityId
- `OwnerAddress`: NftOwnerAddress
- `IsMinted`: bool
- `UpdateCounter`: ulong

---

#### MetaNftAttribute

**Line:** 582091

**Inherits:** Attribute

**Fields:**

- `CollectionId`: NftCollectionId

---

#### MetaNullLogger

**Line:** 519924

**Inherits:** MetaLoggerBase

---

#### MetaOfferGroupId

**Line:** 544613

**Inherits:** StringId

---

#### MetaOfferGroupInfoBase

**Line:** 544624

**Inherits:** IMetaActivableConfigData

---

#### MetaOfferGroupModelBase

**Line:** 544080

**Inherits:** MetaActivableState

---

#### MetaOfferGroupOfferDynamicPurchaseContent

**Line:** 544016

**Inherits:** DynamicPurchaseContent

---

#### MetaOfferGroupPrecursorCondition

**Line:** 544003

**Inherits:** MetaActivablePrecursorCondition

---

#### MetaOfferGroupSourceConfigItemBase

**Line:** 544944

---

#### MetaOfferId

**Line:** 545004

**Inherits:** StringId

---

#### MetaOfferInfoBase

**Line:** 545036

**Inherits:** IGameConfigData

---

#### MetaOfferPerGroupStateBase

**Line:** 543560

---

#### MetaOfferPerPlayerStateBase

**Line:** 543742

---

#### MetaOfferPrecursorCondition

**Line:** 543941

**Inherits:** PlayerCondition

---

#### MetaOfferSourceConfigItemBase

**Line:** 545298

---

#### MetaOnDeserializedAttribute

**Line:** 601006

**Inherits:** Attribute

---

#### MetaPlayConnectionHealthUiView

**Line:** 721826

**Inherits:** UiUnityView

**Fields:**

- `UnhealthyConnectionIndicator`: GameObject
- `_connectionHealth`: ConnectionHealth

---

#### MetaPlayEnvironmentView

**Line:** 721845

**Inherits:** UiUnityView

**Fields:**

- `EnvironmentText`: TMP_Text

---

#### MetaRecurringCalendarSchedule

**Line:** 532776

**Inherits:** MetaScheduleBase

---

#### MetaRef

**Line:** 520687

**Fields:**

- `_key`: object
- `_item`: TItem

---

#### MetaRefUtil

**Line:** 520898

---

#### MetaRequest

**Line:** 557473

---

#### MetaRequestMessage

**Line:** 555884

**Inherits:** MetaMessage

---

#### MetaResponse

**Line:** 557485

---

#### MetaResponseMessage

**Line:** 555920

**Inherits:** MetaMessage

---

#### MetaScheduleBase

**Line:** 532617

---

#### MetaSerializableAttribute

**Line:** 600728

**Inherits:** Attribute

---

#### MetaSerializableDerivedAttribute

**Line:** 600759

**Inherits:** Attribute

---

#### MetaSerializableType

**Line:** 530343

**Fields:**

- `_deserializationConstructor`: ConstructorInfo
- `_constructorParameterValues`: Dictionary<int, object>

---

#### MetaSerializableTypeDeepCompare

**Line:** 530709

**Inherits:** EqualityComparer

---

#### MetaSerializableTypeGetterAttribute

**Line:** 601039

**Inherits:** Attribute

---

#### MetaSerializableTypeProviderAttribute

**Line:** 601029

**Inherits:** Attribute

---

#### MetaSerialization

**Line:** 529690

---

#### MetaSerializationDepthExceededException

**Line:** 529372

**Inherits:** MetaSerializationException

---

#### MetaSerializationException

**Line:** 529302

**Inherits:** Exception

---

#### MetaSerializationMetaRefTraversalParams

**Line:** 529553

---

#### MetaSerializerTypeInfo

**Line:** 530579

**Fields:**

- `Specs`: MetaDictionary<Type, MetaSerializableType>
- `FullTypeHash`: uint

---

#### MetaSerializerTypeInfoDeepCompare

**Line:** 530730

**Inherits:** EqualityComparer

---

#### MetaSerializerTypeRegistry

**Line:** 530608

**Fields:**

- `_typeInfo`: MetaSerializerTypeInfo

---

#### MetaTimeTypeConverter

**Line:** 521067

**Inherits:** TypeConverter

---

#### MetaTimer

**Line:** 528263

**Inherits:** IDisposable

**Fields:**

- `_timer`: Timer

---

#### MetaTypeMissingInLogicVersionSerializationException

**Line:** 529317

**Inherits:** MetaSerializationException

---

#### MetaUnknownDerivedTypeDeserializationException

**Line:** 529344

**Inherits:** MetaSerializationException

---

#### MetaValidateInFutureAttribute

**Line:** 573011

**Inherits:** MetaFormFieldValidatorBaseAttribute

---

#### MetaValidateInRangeAttribute

**Line:** 573061

**Inherits:** MetaFormFieldValidatorBaseAttribute

---

#### MetaValidateInRangeFloatAttribute

**Line:** 573131

**Inherits:** MetaFormFieldValidatorBaseAttribute

---

#### MetaValidateRequiredAttribute

**Line:** 572961

**Inherits:** MetaFormFieldValidatorBaseAttribute

---

#### MetaVersionRange

**Line:** 521089

---

#### MetaWireDataTypeMismatchDeserializationException

**Line:** 529357

**Inherits:** MetaSerializationException

---

#### MetadataAttribute

**Line:** 1327193

**Inherits:** Attribute

---

#### MetadataCollection

**Line:** 1327408

**Inherits:** IMetadataCollection

**Fields:**

- `m_Items`: List<IMetadata>

---

#### MetadataTypeAttribute

**Line:** 1509632

**Inherits:** Attribute

---

#### MetalPatchShaderComputeBufferAnalytic

**Line:** 1587137

**Inherits:** AnalyticsEventBase

---

#### MetaplayAppInfoOptions

**Line:** 1313844

**Fields:**

- `BuildVersion`: Nullable<BuildVersion>

---

#### MetaplayClient

**Line:** 738445

**Inherits:** MetaplayClientBase

---

#### MetaplayClientBase

**Line:** 1314067

---

#### MetaplayClientCreatePlayerContextFunc

**Line:** 1313826

**Inherits:** MulticastDelegate

---

#### MetaplayClientOptions

**Line:** 1313801

**Fields:**

- `AutoCreateMetaplaySDKBehavior`: bool
- `LifecycleDelegate`: IMetaplayLifecycleDelegate
- `ConnectionConfig`: ConnectionConfig
- `OfflineOptions`: MetaplayOfflineOptions
- `AppInfoOptions`: MetaplayAppInfoOptions
- `IAPOptions`: MetaplayIAPOptions
- `ConnectionDelegate`: IMetaplayClientConnectionDelegate
- `LocalizationDelegate`: IMetaplayLocalizationDelegate
- `AnalyticsDelegate`: IMetaplayClientAnalyticsDelegate
- `SocialAuthenticationDelegate`: IMetaplayClientSocialAuthenticationDelegate
- `GameConfigDelegate`: IMetaplayClientGameConfigDelegate
- `CreatePlayerContext`: MetaplayClientCreatePlayerContextFunc
- `ActiveEnvironmentIdOverride`: string

---

#### MetaplayClientState

**Line:** 1313917

**Inherits:** ISessionContextProvider

**Fields:**

- `_hasHandledCurrentConnectionError`: bool
- `_hasHadSessionForCurrentConnection`: bool
- `_pendingSessionFuncs`: Queue<Action>
- `_clientServices`: MetaplayUnitySubClientServices

---

#### MetaplayClientStore

**Line:** 577279

**Inherits:** IDisposable

---

#### MetaplayConnection

**Line:** 1307614

**Fields:**

- `Config`: ConnectionConfig
- `SessionStartResources`: ClientSessionStartResources
- `_serverConnection`: ServerConnection
- `_supervisionLoop`: IEnumerator<MetaplayConnection.Marker>
- `_cancellation`: CancellationTokenSource
- `_flushEnqueuedMessagesBeforeClose`: bool
- `_supervisionLoopRunning`: bool
- `_messagesToDispatch`: List<MetaMessage>
- `_statistics`: ConnectionStatistics
- `_sdkHook`: IMetaplayConnectionSDKHook
- `_messageDispatchSuspended`: bool
- `_suspendedDispatchMessages`: List<MetaMessage>
- `_logForwardingBuffer`: MetaForwardingLogger
- `_pauseTerminationTimer`: MetaTimer
- `_offlineOptions`: MetaplayOfflineOptions
- `_sessionNonceService`: SessionNonceService
- `_sessionGuidService`: UnitySessionGuidService
- `_sessionCredentialService`: ISessionCredentialService
- `_sessionCredentialServiceInitTask`: Task<EntityId>
- `_isUnpausingThisFrame`: bool
- ... (3 more fields)

---

#### MetaplayCoreOptions

**Line:** 520080

---

#### MetaplayFeatureEnabledConditionAttribute

**Line:** 499086

**Inherits:** Attribute

---

#### MetaplayFeatureFlags

**Line:** 520012

---

#### MetaplayIAPOptions

**Line:** 1313856

**Fields:**

- `EnableIAPManager`: bool
- `PurchasePlatform`: InAppPurchasePlatform

---

#### MetaplayJsonContractResolver

**Line:** 583514

**Inherits:** DefaultContractResolver

---

#### MetaplayKcpReceiver

**Line:** 1582486

**Fields:**

- `rcv_queue`: Queue<MetaplayKcpReceiver.RecvSegment>
- `rcv_buf`: List<MetaplayKcpReceiver.RecvSegment>
- `rcv_nxt`: uint

---

#### MetaplayLocalizationManager

**Line:** 1308064

**Fields:**

- `_log`: LogChannel
- `_dlCache`: LocalizationDownloadCache
- `_builtinLanguages`: MetaDictionary<LanguageId, ContentHash>
- `_stopCts`: CancellationTokenSource
- `_serverLocalizationVersions`: MetaDictionary<LanguageId, ContentHash>
- `_delegate`: IMetaplayLocalizationDelegate
- `_hasSession`: bool

---

#### MetaplayLogs

**Line:** 1308124

**Fields:**

- `_logger`: IMetaLogger
- `_defaultLogLevel`: LogLevel
- `_logLevelOverrides`: Dictionary<string, LogLevel>

---

#### MetaplayOfflineOptions

**Line:** 1305415

**Fields:**

- `PersistState`: bool

---

#### MetaplayReadyMessage

**Line:** 711351

**Inherits:** IMessage

---

#### MetaplaySDKBehavior

**Line:** 1308824

**Inherits:** MonoBehaviour

**Fields:**

- `_wasAutoCreated`: bool
- `_isDuplicate`: bool
- `_latencySimulationTransport`: LatencySimulationMessageTransport
- `EnableLatencySimulation`: bool
- `ArtificialAddedLatency`: int

---

#### MetaplayUnitySubClientServices

**Line:** 1308859

**Inherits:** IMetaplaySubClientServices

---

#### Meter

**Line:** 1423028

**Inherits:** IDisposable

**Fields:**

- `_instruments`: List<Instrument>

---

#### MeterListener

**Line:** 1423667

**Inherits:** IDisposable

**Fields:**

- `_disposed`: bool
- `_byteMeasurementCallback`: MeasurementCallback<byte>
- `_shortMeasurementCallback`: MeasurementCallback<short>
- `_intMeasurementCallback`: MeasurementCallback<int>
- `_longMeasurementCallback`: MeasurementCallback<long>
- `_floatMeasurementCallback`: MeasurementCallback<float>
- `_doubleMeasurementCallback`: MeasurementCallback<double>
- `_decimalMeasurementCallback`: MeasurementCallback<Decimal>

---

#### MeterOptions

**Line:** 1424100

**Fields:**

- `_name`: string

---

#### MethodAccessException

**Line:** 26503

**Inherits:** MemberAccessException

---

#### MethodBase

**Line:** 265765

**Inherits:** MemberInfo

---

#### MethodBuilder

**Line:** 269793

**Inherits:** MethodInfo

---

#### MethodCall

**Line:** 224201

**Inherits:** IMethodCallMessage

**Fields:**

- `_uri`: string
- `_typeName`: string
- `_methodName`: string
- `_methodBase`: MethodBase
- `_callContext`: LogicalCallContext
- `_targetIdentity`: Identity
- `ExternalProperties`: IDictionary
- `InternalProperties`: IDictionary

---

#### MethodCallExpression

**Line:** 1288506

**Inherits:** Expression

---

#### MethodInfo

**Line:** 265923

**Inherits:** MethodBase

---

#### MethodReference

**Line:** 1507943

**Fields:**

- `_method`: MethodInfo
- `_target`: object

---

#### MethodResponse

**Line:** 224472

**Inherits:** IMethodReturnMessage

**Fields:**

- `_methodName`: string
- `_uri`: string
- `_typeName`: string
- `_methodBase`: MethodBase
- `_returnValue`: object
- `_exception`: Exception
- `_inArgInfo`: ArgInfo
- `_callMsg`: IMethodCallMessage
- `_callContext`: LogicalCallContext
- `_targetIdentity`: Identity
- `ExternalProperties`: IDictionary
- `InternalProperties`: IDictionary

---

#### MigrationFromVersionAttribute

**Line:** 604113

**Inherits:** Attribute

---

#### MinAttribute

**Line:** 880850

**Inherits:** PropertyAttribute

---

#### MinFloatParameter

**Line:** 827173

**Inherits:** FloatParameter

**Fields:**

- `min`: float

---

#### MinIntParameter

**Line:** 827008

**Inherits:** IntParameter

**Fields:**

- `min`: int

---

#### MinLengthAttribute

**Line:** 1509651

**Inherits:** ValidationAttribute

---

#### MinMaxSlider

**Line:** 624823

**Inherits:** BaseField

**Fields:**

- `m_DragElementStartPos`: Vector2
- `m_ValueStartPos`: Vector2
- `m_MinLimit`: float
- `m_MaxLimit`: float

---

#### MiniGameState

**Line:** 1079570

**Fields:**

- `EndReason`: Nullable<SteppingStoneEndReason>

---

#### MiniJson

**Line:** 1592460

---

#### Mirror

**Line:** 1320044

**Inherits:** IPseudoLocalizationMethod

---

#### Missing

**Line:** 265980

**Inherits:** ISerializable

---

#### MissingFieldException

**Line:** 72462

**Inherits:** MissingMemberException

---

#### MissingManifestResourceException

**Line:** 264118

**Inherits:** SystemException

---

#### MissingMetadataException

**Line:** 267419

**Inherits:** TypeAccessException

---

#### MissingMethodException

**Line:** 26528

**Inherits:** MissingMemberException

---

#### MissingPropertyBagException

**Line:** 1458064

**Inherits:** Exception

---

#### MissingReferenceException

**Line:** 883754

**Inherits:** Exception

---

#### MissingSatelliteAssemblyException

**Line:** 264134

**Inherits:** SystemException

**Fields:**

- `_cultureName`: string

---

#### MissingStoreSecretException

**Line:** 1544984

**Inherits:** IAPSecurityException

---

#### MobileMenuController

**Line:** 1443039

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_closeButton`: Button
- `_maxMenuWidth`: float
- `_peekAmount`: float
- `_targetXPosition`: float
- `Content`: RectTransform
- `Menu`: RectTransform
- `OpenButton`: Button
- `TabController`: SRTabController

---

#### ModelAction

**Line:** 601532

---

#### ModelActionAttribute

**Line:** 601103

**Inherits:** Attribute

---

#### ModelActionExecuteFlagsAttribute

**Line:** 601140

**Inherits:** Attribute

---

#### ModelActionRepository

**Line:** 601633

---

#### ModelActionSpec

**Line:** 601597

---

#### ModelJournal

**Line:** 603075

**Fields:**

- `_log`: LogChannel
- `_recycledChecksumBuffer`: FlatIOBuffer
- `_expectedChecksum`: uint
- `_executingTick`: long
- `_executingAction`: ModelAction

---

#### ModelJournalListenerBase

**Line:** 604309

**Fields:**

- `_source`: IJournalCheckerDataSource
- `_leasedChecksumSerializationBuffer`: IOBuffer
- `_ownedChecksumSerializationBuffer`: IOBuffer
- `_leasedChecksum`: Nullable<uint>
- `_ownedChecksum`: Nullable<uint>
- `_isDisabled`: bool
- `_isPaused`: bool

---

#### Module

**Line:** 265999

**Inherits:** ICustomAttributeProvider

---

#### ModuleBuilder

**Line:** 269842

**Inherits:** Module

---

#### MonitoringDescriptionAttribute

**Line:** 778301

**Inherits:** DescriptionAttribute

---

#### MonoBehaviour

**Line:** 883258

**Inherits:** Behaviour

**Fields:**

- `m_CancellationTokenSource`: CancellationTokenSource

---

#### MonoBehaviourSingleton

**Line:** 729508

---

#### MonoLocalCertificateSelectionCallback

**Line:** 1448961

**Inherits:** MulticastDelegate

---

#### MonoPInvokeCallbackAttribute

**Line:** 834911

**Inherits:** Attribute

---

#### MonoRemoteCertificateValidationCallback

**Line:** 1448949

**Inherits:** MulticastDelegate

---

#### MonoTlsConnectionInfo

**Line:** 1448891

---

#### MonoTlsProvider

**Line:** 1448973

---

#### MonoTlsSettings

**Line:** 1449021

**Fields:**

- `cloned`: bool
- `checkCertName`: bool
- `checkCertRevocationStatus`: bool
- `useServicePointManagerCallback`: Nullable<bool>
- `skipSystemValidators`: bool
- `callbackNeedsChain`: bool
- `certificateValidator`: ICertificateValidator

---

#### Motion

**Line:** 1575706

**Inherits:** Object

---

#### MotionBlur

**Line:** 909509

**Inherits:** VolumeComponent

**Fields:**

- `mode`: MotionBlurModeParameter
- `quality`: MotionBlurQualityParameter
- `intensity`: ClampedFloatParameter
- `clamp`: ClampedFloatParameter

---

#### MotionBlurModeParameter

**Line:** 909536

**Inherits:** VolumeParameter

---

#### MotionBlurQualityParameter

**Line:** 909546

**Inherits:** VolumeParameter

---

#### MotionVectorRenderPass

**Line:** 910413

**Fields:**

- `motionData`: MotionVectorsPersistentData
- `xr`: XRPass

---

#### MouseCaptureEvent

**Line:** 633177

**Inherits:** MouseCaptureEventBase

---

#### MouseCaptureEventBase

**Line:** 633108

---

#### MouseCaptureOutEvent

**Line:** 633142

**Inherits:** MouseCaptureEventBase

---

#### MouseDownEvent

**Line:** 636452

**Inherits:** MouseEventBase

---

#### MouseEnterEvent

**Line:** 636690

**Inherits:** MouseEventBase

---

#### MouseEnterWindowEvent

**Line:** 636852

**Inherits:** MouseEventBase

---

#### MouseEventBase

**Line:** 636108

---

#### MouseLeaveEvent

**Line:** 636732

**Inherits:** MouseEventBase

---

#### MouseLeaveWindowEvent

**Line:** 636897

**Inherits:** MouseEventBase

---

#### MouseManipulator

**Line:** 641492

**Inherits:** Manipulator

---

#### MouseMoveEvent

**Line:** 636550

**Inherits:** MouseEventBase

---

#### MouseOutEvent

**Line:** 636813

**Inherits:** MouseEventBase

---

#### MouseOverEvent

**Line:** 636774

**Inherits:** MouseEventBase

---

#### MousePositionDebug

**Line:** 815229

---

#### MouseUpEvent

**Line:** 636499

**Inherits:** MouseEventBase

---

#### MoveDimensionRequest

**Line:** 1394929

**Inherits:** IDirectResponseSchema

---

#### MoveNextSource

**Line:** 1099123

**Inherits:** IUniTaskSource

**Fields:**

- `completionSource`: UniTaskCompletionSourceCore<bool>

---

#### MoveToTargetSystem

**Line:** 1057772

---

#### MovedFromAttribute

**Line:** 888650

**Inherits:** Attribute

---

#### MultiColumnController

**Line:** 625999

**Inherits:** IDisposable

**Fields:**

- `columnSortingChanged`: Action
- `headerContextMenuPopulateEvent`: Action<ContextualMenuPopulateEvent, Column>
- `m_SortedToSourceIndex`: List<int>
- `m_SourceToSortedIndex`: List<int>
- `m_SortingMode`: ColumnSortingMode
- `m_View`: BaseVerticalCollectionView
- `m_HeaderContainer`: VisualElement
- `m_MultiColumnHeader`: MultiColumnCollectionHeader

---

#### MultiColumnListView

**Line:** 626202

**Inherits:** BaseListView

**Fields:**

- `m_Columns`: Columns
- `m_SortingMode`: ColumnSortingMode
- `m_SortColumnDescriptions`: SortColumnDescriptions
- `m_SortedColumns`: List<SortColumnDescription>
- `columnSortingChanged`: Action
- `headerContextMenuPopulateEvent`: Action<ContextualMenuPopulateEvent, Column>

---

#### MultiColumnListViewController

**Line:** 611169

**Inherits:** BaseListViewController

**Fields:**

- `m_ColumnController`: MultiColumnController

---

#### MultiColumnTreeView

**Line:** 626308

**Inherits:** BaseTreeView

**Fields:**

- `m_Columns`: Columns
- `m_SortingMode`: ColumnSortingMode
- `m_SortColumnDescriptions`: SortColumnDescriptions
- `m_SortedColumns`: List<SortColumnDescription>
- `columnSortingChanged`: Action
- `headerContextMenuPopulateEvent`: Action<ContextualMenuPopulateEvent, Column>

---

#### MultiColumnTreeViewController

**Line:** 611229

**Inherits:** BaseTreeViewController

**Fields:**

- `m_ColumnController`: MultiColumnController

---

#### MultiReactiveSystem

**Line:** 1548839

**Fields:**

- `_toStringCache`: string

---

#### MultiTapButton

**Line:** 1444406

**Inherits:** Button

**Fields:**

- `_lastTap`: float
- `_tapCount`: int
- `RequiredTapCount`: int
- `ResetTime`: float

---

#### MulticastDelegate

**Line:** 176486

**Inherits:** Delegate

---

#### MulticastNotSupportedException

**Line:** 26553

**Inherits:** SystemException

---

#### MulticastOption

**Line:** 800398

---

#### MultilineAttribute

**Line:** 880863

**Inherits:** PropertyAttribute

---

#### MultilineStringConverter

**Line:** 782431

**Inherits:** TypeConverter

---

#### MultipartContent

**Line:** 1488892

**Inherits:** HttpContent

**Fields:**

- `nested_content`: List<HttpContent>

---

#### MultiplayerEntityClientBase

**Line:** 552061

---

#### MultiplayerEntityClientContext

**Line:** 552354

**Fields:**

- `_pendingActions`: List<ModelAction>
- `_previousUpdateAt`: MetaTime
- `_playbackDelta`: MetaDuration
- `_playbackBuffer`: Queue<EntityTimelineUpdateMessage>
- `_playbackBufferOpNdx`: int
- `_playbackOpBuffer`: List<PlaybackOp>
- `_playbackFfCarry`: float
- `_playbackFfReported`: bool
- `_playbackStallOngoing`: bool
- `_playbackStallStartedAt`: DateTime
- `_nextUpdateExpectedAt`: DateTime
- `_nextUpdateTick`: long
- `_latencyMeasurementLastSampleAt`: DateTime
- `_latencyMeasurementTraceIdInFlight`: uint
- `_latencyMeasurementTraceComplete`: bool
- `_latencyMeasurementPingIdInFlight`: int
- `_latencyMeasurementPingComplete`: bool
- `_directConnectionUpgradeNextSynAt`: DateTime
- `_directConnectionKcp`: Kcp
- `_pendingDirectMessages`: List<byte[]>
- ... (9 more fields)

---

#### MultiplayerEntityDirectConnectionProtocol

**Line:** 552921

---

#### MultiplayerModelBase

**Line:** 553021

---

#### MultiplayerModelRuntimeDataBase

**Line:** 552976

---

#### MultiplexedConnectionBuilder

**Line:** 1570610

**Inherits:** IMultiplexedConnectionBuilder

---

#### MultiplexedConnectionContext

**Line:** 1570637

**Inherits:** BaseConnectionContext

---

#### MultiplexedConnectionDelegate

**Line:** 1570653

**Inherits:** MulticastDelegate

---

#### MusicMuteSaveSystem

**Line:** 684583

**Inherits:** ReactiveSystem

---

#### MusicPlayerView

**Line:** 705933

**Inherits:** MonoBehaviour

**Fields:**

- `MenuMusic`: AudioClip
- `CombatMusic`: AudioClip
- `AudioSource`: AudioSource
- `_audioListener`: AudioEntity
- `_transition`: Sequence
- `_volume`: float
- `_defaultVolume`: float

---

#### MusicSettingsView

**Line:** 729297

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton
- `Toggle`: ColoredToggle
- `_audioListener`: AudioEntity

---

#### MustReloginError

**Line:** 1306695

**Inherits:** Exception

---

#### MustUseReturnValueAttribute

**Line:** 869336

**Inherits:** Attribute

---

#### MuteAmbienceComponent

**Line:** 684473

**Inherits:** IComponent

---

#### MuteAudioComponent

**Line:** 684486

**Inherits:** IComponent

---

#### MuteHapticsComponent

**Line:** 692908

**Inherits:** IComponent

---

#### MuteMusicComponent

**Line:** 684499

**Inherits:** IComponent

---

#### MuteUserRequest

**Line:** 1528342

**Inherits:** IEquatable

---

#### MutedLabelUiView

**Line:** 707932

**Inherits:** MonoBehaviour

**Fields:**

- `_chatModel`: MainChatUIModel
- `MutedLabelText`: TMP_Text
- `InputFieldContainer`: GameObject
- `_mutedLoca`: string

---

#### Mutex

**Line:** 181907

**Inherits:** WaitHandle

---

#### NameComponent

**Line:** 710595

**Inherits:** IComponent

**Fields:**

- `Value`: string

---

#### NameObjectCollectionBase

**Line:** 785999

**Inherits:** ICollection

**Fields:**

- `_readOnly`: bool
- `_entriesArray`: ArrayList
- `_keyComparer`: IEqualityComparer
- `_entriesTable`: Hashtable
- `_serializationInfo`: SerializationInfo
- `_version`: int
- `_syncRoot`: object

---

#### NameTable

**Line:** 750718

**Inherits:** XmlNameTable

**Fields:**

- `count`: int
- `mask`: int
- `hashCodeRandomizer`: int

---

#### NameValueCollection

**Line:** 785436

**Inherits:** NameObjectCollectionBase

---

#### NameValueHeaderValue

**Line:** 1490670

**Inherits:** ICloneable

---

#### NameValueWithParametersHeaderValue

**Line:** 1490735

**Inherits:** NameValueHeaderValue

**Fields:**

- `parameters`: List<NameValueHeaderValue>

---

#### NamedPermissionSet

**Line:** 216763

**Inherits:** PermissionSet

**Fields:**

- `name`: string
- `description`: string

---

#### NamedPipeEndPoint

**Line:** 1570674

**Inherits:** EndPoint

---

#### NamedPipeServerStream

**Line:** 1301506

**Inherits:** PipeStream

---

#### NamedRange

**Line:** 1394977

**Inherits:** IDirectResponseSchema

---

#### NamingStrategy

**Line:** 1041034

---

#### NativeContainerAttribute

**Line:** 864150

**Inherits:** Attribute

---

#### NativeContainerIsAtomicWriteOnlyAttribute

**Line:** 864172

**Inherits:** Attribute

---

#### NativeContainerIsReadOnlyAttribute

**Line:** 864161

**Inherits:** Attribute

---

#### NativeContainerNeedsThreadIndexAttribute

**Line:** 864228

**Inherits:** Attribute

---

#### NativeContainerSupportsDeallocateOnJobCompletionAttribute

**Line:** 864194

**Inherits:** Attribute

---

#### NativeContainerSupportsDeferredConvertListToArray

**Line:** 864205

**Inherits:** Attribute

---

#### NativeContainerSupportsMinMaxWriteRestrictionAttribute

**Line:** 864183

**Inherits:** Attribute

---

#### NativeDisableContainerSafetyRestrictionAttribute

**Line:** 864255

**Inherits:** Attribute

---

#### NativeDisableParallelForRestrictionAttribute

**Line:** 838022

**Inherits:** Attribute

---

#### NativeDisableUnsafePtrRestrictionAttribute

**Line:** 864244

**Inherits:** Attribute

---

#### NativeFixedLengthAttribute

**Line:** 838010

**Inherits:** Attribute

---

#### NativeMatchesParallelForLengthAttribute

**Line:** 838016

**Inherits:** Attribute

---

#### NativeSetThreadIndexAttribute

**Line:** 864216

**Inherits:** Attribute

---

#### NavMesh

**Line:** 1593800

---

#### NavigateFocusRing

**Line:** 640110

---

#### NavigationCancelEvent

**Line:** 637292

**Inherits:** NavigationEventBase

---

#### NavigationEventBase

**Line:** 637058

---

#### NavigationMoveEvent

**Line:** 637212

**Inherits:** NavigationEventBase

---

#### NavigationSubmitEvent

**Line:** 637324

**Inherits:** NavigationEventBase

---

#### NavmeshBakingAnalytic

**Line:** 1587153

**Inherits:** AnalyticsEventBase

**Fields:**

- `new_nav_api`: bool
- `bake_at_runtime`: bool
- `height_meshes_count`: int
- `offmesh_links_count`: int

---

#### NegotiationResponse

**Line:** 1583168

---

#### NestedGlobalVariablesGroup

**Line:** 1321490

**Inherits:** NestedVariablesGroup

---

#### NestedVariablesGroup

**Line:** 1324835

**Inherits:** Variable

---

#### NetEventSource

**Line:** 789848

---

#### NetSectionGroup

**Line:** 803197

**Inherits:** ConfigurationSectionGroup

---

#### NetworkCredential

**Line:** 791919

**Inherits:** ICredentials

**Fields:**

- `m_domain`: string
- `m_userName`: string
- `m_password`: SecureString

---

#### NetworkDiagnosticReport

**Line:** 549748

---

#### NetworkDiagnosticsManager

**Line:** 1308937

**Fields:**

- `_reportTask`: Task

---

#### NetworkInformationException

**Line:** 798895

**Inherits:** Win32Exception

---

#### NetworkProbe

**Line:** 1309003

**Inherits:** IDisposable

**Fields:**

- `_task`: Task
- `_cts`: CancellationTokenSource
- `_result`: int

---

#### NetworkStream

**Line:** 799221

**Inherits:** Stream

**Fields:**

- `_readable`: bool
- `_writeable`: bool
- `_closeTimeout`: int
- `_cleanedUp`: bool
- `_currentReadTimeout`: int
- `_currentWriteTimeout`: int

---

#### NeutralRangeReductionModeParameter

**Line:** 909791

**Inherits:** VolumeParameter

---

#### NeutralResourcesLanguageAttribute

**Line:** 264153

**Inherits:** Attribute

---

#### NewExpression

**Line:** 1288935

**Inherits:** Expression

**Fields:**

- `_arguments`: IReadOnlyList<Expression>

---

#### NewtonsoftJsonContractResolver

**Line:** 1496503

**Inherits:** DefaultContractResolver

---

#### NewtonsoftJsonSerializer

**Line:** 1496561

**Inherits:** IJsonSerializer

---

#### NextDayMessage

**Line:** 729555

**Inherits:** IMessage

---

#### NextDayModel

**Line:** 1078105

**Inherits:** ITickable

---

#### NextDayTriggerCheatAction

**Line:** 1078147

**Inherits:** PlayerAction

---

#### NftClient

**Line:** 582197

**Inherits:** IMetaplaySubClient

**Fields:**

- `_clientServices`: IMetaplaySubClientServices
- `_log`: LogChannel

---

#### NftCollectionId

**Line:** 582081

**Inherits:** StringId

---

#### NftMetadataCorePropertyAttribute

**Line:** 582244

**Inherits:** Attribute

**Fields:**

- `Id`: Nullable<NftMetadataCorePropertyId>

---

#### NftMetadataCustomPropertyAttribute

**Line:** 582260

**Inherits:** Attribute

---

#### NftMetadataImportContext

**Line:** 582001

---

#### NftMetadataSpec

**Line:** 582332

---

#### NftSchemaMigrationContext

**Line:** 582013

---

#### NftTypeRegistry

**Line:** 582555

---

#### NftTypeSpec

**Line:** 582511

**Fields:**

- `NftType`: Type
- `TypeName`: string
- `CollectionId`: NftCollectionId
- `MetadataSpec`: NftMetadataSpec

---

#### NoAliasAttribute

**Line:** 1331262

**Inherits:** Attribute

---

#### NoChecksumAttribute

**Line:** 600974

**Inherits:** MetaMemberFlagAttribute

---

#### NoClientVersionSuppliedException

**Line:** 685193

**Inherits:** BadRequestException

---

#### NoInterpClampedFloatParameter

**Line:** 827289

**Inherits:** VolumeParameter

**Fields:**

- `min`: float
- `max`: float

---

#### NoInterpClampedIntParameter

**Line:** 827124

**Inherits:** VolumeParameter

**Fields:**

- `min`: int
- `max`: int

---

#### NoInterpColorParameter

**Line:** 827386

**Inherits:** VolumeParameter

**Fields:**

- `hdr`: bool
- `showAlpha`: bool
- `showEyeDropper`: bool

---

#### NoInterpCubemapParameter

**Line:** 827584

**Inherits:** VolumeParameter

---

#### NoInterpFloatParameter

**Line:** 827162

**Inherits:** VolumeParameter

---

#### NoInterpFloatRangeParameter

**Line:** 827340

**Inherits:** VolumeParameter

**Fields:**

- `min`: float
- `max`: float

---

#### NoInterpIntParameter

**Line:** 826997

**Inherits:** VolumeParameter

---

#### NoInterpMaxFloatParameter

**Line:** 827242

**Inherits:** VolumeParameter

**Fields:**

- `max`: float

---

#### NoInterpMaxIntParameter

**Line:** 827077

**Inherits:** VolumeParameter

**Fields:**

- `max`: int

---

#### NoInterpMinFloatParameter

**Line:** 827196

**Inherits:** VolumeParameter

**Fields:**

- `min`: float

---

#### NoInterpMinIntParameter

**Line:** 827031

**Inherits:** VolumeParameter

**Fields:**

- `min`: int

---

#### NoInterpRenderTextureParameter

**Line:** 827556

**Inherits:** VolumeParameter

---

#### NoInterpTextureParameter

**Line:** 827500

**Inherits:** VolumeParameter

---

#### NoInterpVector2Parameter

**Line:** 827419

**Inherits:** VolumeParameter

---

#### NoInterpVector3Parameter

**Line:** 827444

**Inherits:** VolumeParameter

---

#### NoInterpVector4Parameter

**Line:** 827469

**Inherits:** VolumeParameter

---

#### NoNullAllowedException

**Line:** 1080843

**Inherits:** DataException

---

#### NoTransportSupportedException

**Line:** 1482946

**Inherits:** Exception

---

#### NoUserTokenSuppliedException

**Line:** 685184

**Inherits:** BadRequestException

---

#### NonEventAttribute

**Line:** 275823

**Inherits:** Attribute

---

#### NonSerializedAttribute

**Line:** 26569

**Inherits:** Attribute

---

#### NoopAction

**Line:** 604083

**Inherits:** ModelAction

---

#### NotAllowed

**Line:** 716874

**Inherits:** Exception

---

#### NotConnected

**Line:** 1309945

**Inherits:** ConnectionState

---

#### NotEnoughPermissionsException

**Line:** 716886

**Inherits:** Exception

---

#### NotFoundException

**Line:** 685065

**Inherits:** Exception

---

#### NotFoundResponse

**Line:** 685045

---

#### NotImplementedException

**Line:** 26579

**Inherits:** SystemException

---

#### NotInitializedException

**Line:** 1565110

**Inherits:** Exception

---

#### NotKeyableAttribute

**Line:** 1575744

**Inherits:** Attribute

---

#### NotMappedAttribute

**Line:** 1510952

**Inherits:** Attribute

---

#### NotNullAttribute

**Line:** 869259

**Inherits:** Attribute

---

#### NotNullIfNotNullAttribute

**Line:** 275891

**Inherits:** Attribute

---

#### NotNullWhenAttribute

**Line:** 275877

**Inherits:** Attribute

---

#### NotSupportedException

**Line:** 26595

**Inherits:** SystemException

---

#### NothingChangedException

**Line:** 716895

**Inherits:** Exception

---

#### NotificationAnimation

**Line:** 722913

**Inherits:** MonoBehaviour

**Fields:**

- `_seq`: Sequence

---

#### NotificationCenter

**Line:** 1591249

---

#### NotificationsPermissionRequest

**Line:** 1591458

**Inherits:** CustomYieldInstruction

**Fields:**

- `request`: PermissionRequest

---

#### NotifyCollectionChangedEventArgs

**Line:** 785821

**Inherits:** EventArgs

**Fields:**

- `_action`: NotifyCollectionChangedAction
- `_newItems`: IList
- `_oldItems`: IList
- `_newStartingIndex`: int
- `_oldStartingIndex`: int

---

#### NotifyCollectionChangedEventHandler

**Line:** 785858

**Inherits:** MulticastDelegate

---

#### NotifyParentPropertyAttribute

**Line:** 784740

**Inherits:** Attribute

**Fields:**

- `notifyParent`: bool

---

#### NullChecksumEvaluator

**Line:** 525574

**Inherits:** IChecksumContext

---

#### NullDataStore

**Line:** 1501431

**Inherits:** IDataStore

---

#### NullLogger

**Line:** 1537293

---

#### NullLoggerFactory

**Line:** 1537234

**Inherits:** ILoggerFactory

---

#### NullLoggerProvider

**Line:** 1537261

**Inherits:** ILoggerProvider

---

#### NullProductIdException

**Line:** 1407779

**Inherits:** ReceiptParserException

---

#### NullReceiptException

**Line:** 1407788

**Inherits:** ReceiptParserException

---

#### NullReferenceException

**Line:** 26614

**Inherits:** SystemException

---

#### NullableConverter

**Line:** 782449

**Inherits:** TypeConverter

---

#### NumberControl

**Line:** 1444920

**Inherits:** DataBoundControl

**Fields:**

- `_lastValue`: string
- `_type`: Type
- `DownNumberButton`: SRNumberButton
- `NumberSpinner`: SRNumberSpinner
- `Title`: Text
- `UpNumberButton`: SRNumberButton

---

#### NumberFormat

**Line:** 1395037

**Inherits:** IDirectResponseSchema

---

#### NumberFormatInfo

**Line:** 273554

**Inherits:** ICloneable

---

#### NumberRangeAttribute

**Line:** 1442914

**Inherits:** Attribute

---

#### Numbers

**Line:** 736340

---

#### OAuth2AuthenticationPlatformUserBase

**Line:** 578469

**Inherits:** IWebLoginAuthenticationPlatformUserInfo

---

#### ObjRef

**Line:** 221069

**Inherits:** IObjectReference

**Fields:**

- `channel_info`: IChannelInfo
- `uri`: string
- `typeInfo`: IRemotingTypeInfo
- `envoyInfo`: IEnvoyInfo
- `flags`: int
- `_serverType`: Type

---

#### Object

**Line:** 883968

**Fields:**

- `m_CachedPtr`: IntPtr

---

#### ObjectCache

**Line:** 1583322

---

#### ObjectConstructor

**Line:** 1041103

---

#### ObjectDisposedException

**Line:** 30838

**Inherits:** InvalidOperationException

**Fields:**

- `_objectName`: string

---

#### ObjectFactory

**Line:** 1542644

---

#### ObjectGraphDump

**Line:** 521386

**Fields:**

- `_typeFieldsCache`: Dictionary<Type, FieldInfo[]>

---

#### ObjectIDGenerator

**Line:** 225515

---

#### ObjectManager

**Line:** 225547

**Fields:**

- `m_onDeserializationHandler`: DeserializationEventHandler
- `m_onDeserializedHandler`: SerializationEventHandler

---

#### ObjectParameter

**Line:** 827643

---

#### ObjectPool

**Line:** 1583369

---

#### ObjectVariable

**Line:** 1324781

**Inherits:** Variable

---

#### ObservableCounter

**Line:** 1424286

---

#### ObservableGauge

**Line:** 1424351

---

#### ObservableInstrument

**Line:** 1424416

---

#### ObservableList

**Line:** 810679

**Fields:**

- `m_List`: IList<T>
- `ItemAdded`: ListChangedEventHandler<T>
- `ItemRemoved`: ListChangedEventHandler<T>

---

#### ObservableUpDownCounter

**Line:** 1424475

---

#### ObsoleteAttribute

**Line:** 30874

**Inherits:** Attribute

**Fields:**

- `_message`: string
- `_error`: bool

---

#### OfferPlacementId

**Line:** 544603

**Inherits:** StringId

---

#### OfflineChatService

**Line:** 707463

**Inherits:** IChatService

**Fields:**

- `connected`: bool
- `OnIncomingMessage`: Action<string, ChatItem>
- `OnDeletedMessage`: Action<string, long>
- `OnReactionUpdated`: Action<string, long, string, string[]>
- `OnConnectionState`: Action<ChatConnectionState>
- `OnRoomJoined`: Action<string>

---

#### OfflineServerTransport

**Line:** 1305928

**Inherits:** MessageTransport

**Fields:**

- `_log`: LogChannel
- `_server`: IOfflineServer
- `_isConnected`: bool
- `_openEnqueued`: bool
- `_closeEnqueued`: bool
- `_closeErrorPayload`: object
- `_incomingMessages`: List<MetaMessage>
- `_outgoingInfos`: List<MessageTransport.Info>
- `_updateCompletion`: TaskCompletionSource<int>
- `_pendingLatencySamples`: List<MessageTransportLatencySampleMessage>

---

#### OfflineTimerStatTarget

**Line:** 1077190

**Inherits:** StatTargetBase

---

#### OffsetDatePattern

**Line:** 1153767

**Inherits:** IPattern

---

#### OffsetDateTime

**Line:** 1145649

---

#### OffsetDateTimePattern

**Line:** 1154074

**Inherits:** IPattern

---

#### OffsetPattern

**Line:** 1154416

**Inherits:** IPattern

---

#### OffsetTimePattern

**Line:** 1154730

**Inherits:** IPattern

---

#### Oid

**Line:** 778689

**Fields:**

- `_value`: string
- `_friendlyName`: string
- `_group`: OidGroup

---

#### OidCollection

**Line:** 778732

**Inherits:** ICollection

---

#### OidEnumerator

**Line:** 778774

**Inherits:** IEnumerator

**Fields:**

- `_current`: int

---

#### OidcToken

**Line:** 1372977

---

#### OidcTokenOptions

**Line:** 1373008

---

#### OkResponse

**Line:** 685007

---

#### OldClientListenerInitSystem

**Line:** 738532

**Inherits:** IInitSystem

---

#### OnDemandRendering

**Line:** 892804

---

#### OnDeserializedAttribute

**Line:** 226107

**Inherits:** Attribute

---

#### OnDeserializingAttribute

**Line:** 226096

**Inherits:** Attribute

---

#### OnErrorAttribute

**Line:** 1041155

**Inherits:** Attribute

---

#### OnSerializedAttribute

**Line:** 226085

**Inherits:** Attribute

---

#### OnSerializingAttribute

**Line:** 226074

**Inherits:** Attribute

---

#### OneWayAttribute

**Line:** 224730

**Inherits:** Attribute

---

#### OpCodes

**Line:** 269898

---

#### OpenComponent

**Line:** 736204

**Inherits:** IComponent

---

#### OpenEventSystem

**Line:** 702421

**Inherits:** ReactiveSystem

---

#### OpenListenerComponent

**Line:** 699947

**Inherits:** IComponent

**Fields:**

- `value`: List<IOpenListener>

---

#### OpenRemovedEventSystem

**Line:** 702442

**Inherits:** ReactiveSystem

---

#### OpenRemovedListenerComponent

**Line:** 699960

**Inherits:** IComponent

**Fields:**

- `value`: List<IOpenRemovedListener>

---

#### OpenSettingsView

**Line:** 729045

**Inherits:** UiUnityView

**Fields:**

- `OpenButton`: UnityButton

---

#### OperationCanceledException

**Line:** 30904

**Inherits:** SystemException

**Fields:**

- `_cancellationToken`: CancellationToken

---

#### OperationException

**Line:** 1434934

**Inherits:** Exception

---

#### OpinionView

**Line:** 728486

**Inherits:** MonoBehaviour

**Fields:**

- `SubmitButton`: UnityButton
- `CloseButton`: UnityButton
- `InputField`: TMP_InputField

---

#### OptionDefinition

**Line:** 1446865

---

#### OptionalAttribute

**Line:** 229246

**Inherits:** Attribute

---

#### OptionalFieldAttribute

**Line:** 226054

**Inherits:** Attribute

**Fields:**

- `versionAdded`: int

---

#### OptionsBuilder

**Line:** 1539338

---

#### OptionsCache

**Line:** 1539725

---

#### OptionsControlBase

**Line:** 1444351

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_selectionModeEnabled`: bool
- `SelectionModeToggle`: Toggle
- `Option`: OptionDefinition

---

#### OptionsFactory

**Line:** 1539796

---

#### OptionsManager

**Line:** 1539868

---

#### OptionsMonitor

**Line:** 1540007

**Fields:**

- `_onChange`: Action<TOptions, string>

---

#### OptionsServiceImpl

**Line:** 1445883

**Inherits:** IOptionsService

**Fields:**

- `OptionsUpdated`: EventHandler
- `OptionsValueUpdated`: EventHandler<PropertyChangedEventArgs>

---

#### OptionsTabController

**Line:** 1443318

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_queueRefresh`: bool
- `_selectionModeEnabled`: bool
- `_optionCanvas`: Canvas
- `ActionControlPrefab`: ActionControl
- `CategoryGroupPrefab`: CategoryGroup
- `ContentContainer`: RectTransform
- `NoOptionsNotice`: GameObject
- `PinButton`: Toggle
- `PinPromptSpacer`: GameObject
- `PinPromptText`: GameObject
- `_isTogglingCategory`: bool

---

#### OptionsValidationException

**Line:** 1540152

**Inherits:** Exception

---

#### OptionsValidatorAttribute

**Line:** 1540191

**Inherits:** Attribute

---

#### OptionsWrapper

**Line:** 1540202

---

#### OrderedDictionary

**Line:** 989161

---

#### OrderedSet

**Line:** 521872

**Fields:**

- `_count`: int
- `_nextFreeEntry`: int
- `_iterationFirst`: int
- `_iterationLast`: int
- `_version`: uint
- `_pendingSerializetionInfo`: SerializationInfo

---

#### OrdinalComparer

**Line:** 57662

**Inherits:** StringComparer

---

#### OrgChartSpec

**Line:** 1395085

**Inherits:** IDirectResponseSchema

---

#### OutAttribute

**Line:** 229235

**Inherits:** Attribute

---

#### OutOfMemoryException

**Line:** 72523

**Inherits:** SystemException

---

#### Outline

**Line:** 1357923

**Inherits:** Shadow

---

#### OutputLengthException

**Line:** 1518515

**Inherits:** DataLengthException

---

#### OverflowException

**Line:** 30944

**Inherits:** ArithmeticException

---

#### OverlayAreaParentComponent

**Line:** 693259

**Inherits:** IComponent

**Fields:**

- `Value`: Transform

---

#### OverlayPosition

**Line:** 1395205

**Inherits:** IDirectResponseSchema

---

#### PKCS1

**Line:** 1449464

---

#### PKCS12

**Line:** 1447465

**Inherits:** ICloneable

**Fields:**

- `_keyBags`: ArrayList
- `_secretBags`: ArrayList
- `_certs`: X509CertificateCollection
- `_keyBagsChanged`: bool
- `_secretBagsChanged`: bool
- `_certsChanged`: bool
- `_iterations`: int
- `_safeBags`: ArrayList
- `_rng`: RandomNumberGenerator

---

#### PKCS7

**Line:** 1447384

---

#### PKCS8

**Line:** 1449597

---

#### PackageManagerAddPackageAnalytic

**Line:** 1587234

**Inherits:** PackageManagerBaseAnalytic

---

#### PackageManagerBaseAnalytic

**Line:** 1587214

**Inherits:** AnalyticsEventBase

**Fields:**

- `start_ts`: long
- `duration`: long
- `blocking`: bool
- `package_id`: string
- `status_code`: int
- `error_message`: string

---

#### PackageManagerEmbedPackageAnalytic

**Line:** 1587306

**Inherits:** PackageManagerBaseAnalytic

---

#### PackageManagerRemovePackageAnalytic

**Line:** 1587266

**Inherits:** PackageManagerBaseAnalytic

---

#### PackageManagerResetPackageAnalytic

**Line:** 1587322

**Inherits:** PackageManagerBaseAnalytic

---

#### PackageManagerResolveErrorPackageAnalytic

**Line:** 1587338

**Inherits:** PackageManagerBaseAnalytic

**Fields:**

- `reason`: string
- `action`: string

---

#### PackageManagerResolvePackageAnalytic

**Line:** 1587282

**Inherits:** PackageManagerBaseAnalytic

---

#### PackageManagerStartServerPackageAnalytic

**Line:** 1587358

**Inherits:** PackageManagerBaseAnalytic

---

#### PackageManagerTestAnalytic

**Line:** 1587250

**Inherits:** PackageManagerBaseAnalytic

---

#### PackedPlayModeBuildLogs

**Line:** 1453527

**Fields:**

- `m_RuntimeBuildLogs`: List<PackedPlayModeBuildLogs.RuntimeBuildLog>

---

#### PackingAttribute

**Line:** 821533

**Inherits:** Attribute

**Fields:**

- `packingScheme`: FieldPacking
- `offsetInSource`: int
- `sizeInBits`: int
- `isDirection`: bool
- `sRGBDisplay`: bool
- `checkIsNormalized`: bool
- `preprocessor`: string

---

#### Padding

**Line:** 1395289

**Inherits:** IDirectResponseSchema

---

#### Page

**Line:** 676707

**Fields:**

- `cpuData`: NativeArray<T>
- `updateRanges`: NativeArray<GfxUpdateBufferRange>
- `allocator`: GPUBufferAllocator
- `m_ElemStride`: uint
- `m_UpdateRangeMin`: uint
- `m_UpdateRangeMax`: uint
- `m_UpdateRangesEnqueued`: uint
- `m_UpdateRangesBatchStart`: uint
- `m_UpdateRangesSaturated`: bool

---

#### PageStreamer

**Line:** 1504254

---

#### Painter2D

**Line:** 643776

**Inherits:** IDisposable

**Fields:**

- `m_Ctx`: MeshGenerationContext
- `m_JobSnapshots`: List<Painter2D.Painter2DJobData>
- `m_JobParameters`: NativeArray<Painter2D.Painter2DJobData>
- `m_Disposed`: bool
- `m_OnMeshGenerationDelegate`: MeshGenerationCallback

---

#### PanelChangedEventBase

**Line:** 637337

---

#### PanelEventHandler

**Line:** 1358905

**Inherits:** UIBehaviour

**Fields:**

- `m_Panel`: BaseRuntimePanel
- `m_LastClickTime`: float
- `m_Selecting`: bool
- `m_Event`: Event

---

#### PanelRaycaster

**Line:** 1359038

**Inherits:** BaseRaycaster

**Fields:**

- `m_Panel`: BaseRuntimePanel

---

#### PanelSettings

**Line:** 640272

**Inherits:** ScriptableObject

**Fields:**

- `themeUss`: ThemeStyleSheet
- `m_DisableNoThemeWarning`: bool
- `m_TargetTexture`: RenderTexture
- `m_RenderMode`: PanelRenderMode
- `m_WorldSpaceLayer`: int
- `m_ScaleMode`: PanelScaleMode
- `m_ReferenceSpritePixelsPerUnit`: float
- `m_PixelsPerUnit`: float
- `m_Scale`: float
- `m_ReferenceDpi`: float
- `m_FallbackDpi`: float
- `m_ReferenceResolution`: Vector2Int
- `m_ScreenMatchMode`: PanelScreenMatchMode
- `m_Match`: float
- `m_SortingOrder`: float
- `m_TargetDisplay`: int
- `m_BindingLogLevel`: BindingLogLevel
- `m_ClearDepthStencil`: bool
- `m_ClearColor`: bool
- `m_ColorClearValue`: Color
- ... (15 more fields)

---

#### PanelTextSettings

**Line:** 665551

**Inherits:** TextSettings

---

#### PaniniProjection

**Line:** 909558

**Inherits:** VolumeComponent

**Fields:**

- `distance`: ClampedFloatParameter
- `cropToFit`: ClampedFloatParameter

---

#### ParallelEtwProvider

**Line:** 191311

---

#### ParallelLoopState

**Line:** 191353

---

#### ParallelOptions

**Line:** 191174

**Fields:**

- `_scheduler`: TaskScheduler
- `_maxDegreeOfParallelism`: int
- `_cancellationToken`: CancellationToken

---

#### ParamArrayAttribute

**Line:** 30963

**Inherits:** Attribute

---

#### Parameter

**Line:** 1573139

**Inherits:** IDisposable

---

#### ParameterBuilder

**Line:** 270136

---

#### ParameterCollection

**Line:** 1495891

**Inherits:** List

---

#### ParameterExpression

**Line:** 1288989

**Inherits:** Expression

---

#### ParameterInfo

**Line:** 266089

**Inherits:** ICustomAttributeProvider

**Fields:**

- `AttrsImpl`: ParameterAttributes
- `ClassImpl`: Type
- `DefaultValueImpl`: object
- `MemberImpl`: MemberInfo
- `NameImpl`: string
- `PositionImpl`: int

---

#### ParameterizedThreadStart

**Line:** 179056

**Inherits:** MulticastDelegate

---

#### ParametersWithIV

**Line:** 1519119

**Inherits:** ICipherParameters

---

#### ParseAsDerivedTypeAttribute

**Line:** 587116

**Inherits:** Attribute

---

#### ParseError

**Line:** 526038

**Inherits:** Exception

---

#### ParseResult

**Line:** 1155603

---

#### Parser

**Line:** 1322785

**Fields:**

- `m_OpeningBrace`: char
- `m_ClosingBrace`: char
- `m_Settings`: SmartSettings
- `m_AlphanumericSelectors`: bool
- `m_AllowedSelectorChars`: string
- `m_Operators`: string
- `m_AlternativeEscaping`: bool
- `m_AlternativeEscapeChar`: char
- `OnParsingFailure`: EventHandler<ParsingErrorEventArgs>

---

#### ParsingErrorEventArgs

**Line:** 1322868

**Inherits:** EventArgs

---

#### ParsingErrors

**Line:** 1322962

**Inherits:** Exception

**Fields:**

- `result`: Format

---

#### ParticleSystem

**Line:** 1577751

**Inherits:** Component

---

#### ParticleSystemRenderer

**Line:** 1578011

**Inherits:** Renderer

---

#### PasteDataRequest

**Line:** 1395361

**Inherits:** IDirectResponseSchema

---

#### Path

**Line:** 1430274

**Fields:**

- `_incrementalClone`: Path
- `_incrementalIndex`: int
- `_decoder`: ABSPathDecoder
- `_changed`: bool

---

#### PathChain

**Line:** 723236

**Inherits:** IPath

---

#### PathPlugin

**Line:** 1429251

**Inherits:** ABSTweenPlugin

---

#### PathTooLongException

**Line:** 468119

**Inherits:** IOException

---

#### PathVisitor

**Line:** 1471468

**Inherits:** IPropertyBagVisitor

**Fields:**

- `m_PathIndex`: int

---

#### PayloadDeserializer

**Line:** 1589895

**Inherits:** IPayloadDeserializer

---

#### PayoutDefinition

**Line:** 1530674

**Fields:**

- `m_Type`: PayoutType
- `m_Subtype`: string
- `m_Quantity`: double
- `m_Data`: string

---

#### PendingDynamicPurchaseContent

**Line:** 583760

**Fields:**

- `Content`: DynamicPurchaseContent
- `DeviceId`: string
- `Status`: PendingDynamicPurchaseContentStatus
- `GameProductAnalyticsId`: string
- `GameAnalyticsContext`: PurchaseAnalyticsContext

---

#### PendingItemManagerUiView

**Line:** 714568

**Inherits:** UiUnityView

**Fields:**

- `Parent`: Transform
- `Anvil`: AnvilView
- `ItemPreviewPrefab`: ItemPreviewVisual
- `_itemPreviews`: Dictionary<Guid, ItemPreviewVisual>

---

#### PendingNonDynamicPurchaseContext

**Line:** 585860

**Fields:**

- `GameProductAnalyticsId`: string
- `GameAnalyticsContext`: PurchaseAnalyticsContext
- `DeviceId`: string
- `Status`: PendingPurchaseAnalyticsContextStatus

---

#### PerformDynamicRes

**Line:** 809583

**Inherits:** MulticastDelegate

---

#### PerformanceCountersElement

**Line:** 803221

**Inherits:** ConfigurationElement

---

#### Period

**Line:** 1146207

**Inherits:** IEquatable

---

#### PeriodBuilder

**Line:** 1146487

**Inherits:** IXmlSerializable

---

#### PeriodPattern

**Line:** 1158195

**Inherits:** IPattern

---

#### PeriodThrottle

**Line:** 523464

**Fields:**

- `_lock`: object
- `_periodStart`: DateTime
- `_numEventsInPeriod`: int

---

#### PermissionCallbacks

**Line:** 1487323

**Inherits:** AndroidJavaProxy

**Fields:**

- `PermissionGranted`: Action<string>
- `PermissionDenied`: Action<string>
- `PermissionDeniedAndDontAskAgain`: Action<string>
- `PermissionRequestDismissed`: Action<string>

---

#### PermissionRequest

**Line:** 1553472

---

#### PermissionSet

**Line:** 216805

**Inherits:** ISecurityEncodable

**Fields:**

- `state`: PermissionState
- `list`: ArrayList
- `_declsec`: bool

---

#### PersianCalendar

**Line:** 272819

**Inherits:** Calendar

---

#### PersistentVariablesSource

**Line:** 1321921

**Inherits:** ISource

**Fields:**

- `m_Groups`: List<PersistentVariablesSource.NameValuePair>
- `m_GroupLookup`: Dictionary<string, PersistentVariablesSource.NameValuePair>

---

#### PhoneAttribute

**Line:** 1509683

**Inherits:** DataTypeAttribute

---

#### Physics

**Line:** 1576821

---

#### Physics2D

**Line:** 1578229

---

#### Physics2DRaycaster

**Line:** 1360987

**Inherits:** PhysicsRaycaster

---

#### PhysicsRaycaster

**Line:** 1361022

**Inherits:** BaseRaycaster

**Fields:**

- `m_EventCamera`: Camera
- `m_EventMask`: LayerMask
- `m_MaxRayIntersections`: int
- `m_LastMaxRayIntersections`: int

---

#### PhysicsShapeGroup2D

**Line:** 1578403

---

#### PhysicsSystem

**Line:** 1057784

---

#### PieChartSpec

**Line:** 1395445

**Inherits:** IDirectResponseSchema

---

#### PinEntryCompleteCallback

**Line:** 1445421

**Inherits:** MulticastDelegate

---

#### PinEntryControl

**Line:** 1444459

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_isVisible`: bool
- `_numbers`: List<int>
- `Background`: Image
- `CanCancel`: bool
- `CancelButton`: Button
- `CancelButtonText`: Text
- `CanvasGroup`: CanvasGroup
- `DotAnimator`: Animator
- `PromptText`: Text
- `Complete`: PinEntryControlCallback

---

#### PinEntryControlCallback

**Line:** 1444424

**Inherits:** MulticastDelegate

---

#### PinEntryServiceImpl

**Line:** 1445939

**Inherits:** SRServiceBase

**Fields:**

- `_callback`: PinEntryCompleteCallback
- `_isVisible`: bool
- `_pinControl`: PinEntryControl
- `_requiredPin`: List<int>

---

#### PingMessage

**Line:** 1569134

**Inherits:** HubMessage

---

#### PinnedUIRoot

**Line:** 1443881

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `Canvas`: Canvas
- `Container`: RectTransform
- `DockConsoleController`: DockConsoleController
- `Options`: GameObject
- `OptionsLayoutGroup`: FlowLayoutGroup
- `Profiler`: GameObject
- `ProfilerHandleManager`: HandleManager
- `ProfilerVerticalLayoutGroup`: VerticalLayoutGroup

---

#### PinnedUIServiceImpl

**Line:** 1445980

**Inherits:** SRServiceBase

**Fields:**

- `_queueRefresh`: bool
- `_uiRoot`: PinnedUIRoot
- `OptionPinStateChanged`: Action<OptionDefinition, bool>
- `OptionsCanvasCreated`: Action<RectTransform>

---

#### PinnedUiCanvasCreated

**Line:** 1442457

**Inherits:** MulticastDelegate

---

#### Pipe

**Line:** 1515415

**Fields:**

- `_bufferSegmentPool`: BufferSegmentStack
- `_unconsumedBytes`: long
- `_unflushedBytes`: long
- `_readerAwaitable`: PipeAwaitable
- `_writerAwaitable`: PipeAwaitable
- `_writerCompletion`: PipeCompletion
- `_readerCompletion`: PipeCompletion
- `_lastExaminedIndex`: long
- `_readHead`: BufferSegment
- `_readHeadIndex`: int
- `_disposed`: bool
- `_readTail`: BufferSegment
- `_readTailIndex`: int
- `_minimumReadBytes`: int
- `_writingHead`: BufferSegment
- `_writingHeadMemory`: Memory<byte>
- `_writingHeadBytesBuffered`: int
- `_operationState`: PipeOperationState

---

#### PipeOptions

**Line:** 1515854

---

#### PipeReader

**Line:** 1516060

**Fields:**

- `_stream`: PipeReaderStream

---

#### PipeScheduler

**Line:** 1516306

---

#### PipeStream

**Line:** 1301522

**Inherits:** Stream

**Fields:**

- `_handle`: SafePipeHandle
- `_canRead`: bool
- `_canWrite`: bool
- `_isAsync`: bool
- `_state`: PipeState

---

#### PipeWriter

**Line:** 1516363

**Inherits:** IBufferWriter

**Fields:**

- `_stream`: PipeWriterStream

---

#### PivotFilterCriteria

**Line:** 1395529

**Inherits:** IDirectResponseSchema

---

#### PivotFilterSpec

**Line:** 1395589

**Inherits:** IDirectResponseSchema

---

#### PivotGroup

**Line:** 1395649

**Inherits:** IDirectResponseSchema

---

#### PivotGroupLimit

**Line:** 1395793

**Inherits:** IDirectResponseSchema

---

#### PivotGroupRule

**Line:** 1395841

**Inherits:** IDirectResponseSchema

---

#### PivotGroupSortValueBucket

**Line:** 1395901

**Inherits:** IDirectResponseSchema

---

#### PivotGroupValueMetadata

**Line:** 1395949

**Inherits:** IDirectResponseSchema

---

#### PivotTable

**Line:** 1395997

**Inherits:** IDirectResponseSchema

---

#### PivotValue

**Line:** 1396129

**Inherits:** IDirectResponseSchema

---

#### PixelPerfectCamera

**Line:** 1363769

**Inherits:** MonoBehaviour

**Fields:**

- `m_AssetsPPU`: int
- `m_RefResolutionX`: int
- `m_RefResolutionY`: int
- `m_Camera`: Camera
- `m_Internal`: PixelPerfectCameraInternal
- `m_CinemachineCompatibilityMode`: bool

---

#### PkceGoogleAuthorizationCodeFlow

**Line:** 1376490

**Inherits:** GoogleAuthorizationCodeFlow

---

#### Placeholder

**Line:** 1323004

**Inherits:** FormatItem

---

#### PlatformMappingService

**Line:** 1456006

---

#### PlatformNotSupportedException

**Line:** 31066

**Inherits:** NotSupportedException

---

#### PlatformOverride

**Line:** 1327516

**Inherits:** IEntryOverride

**Fields:**

- `m_PlatformOverrides`: List<PlatformOverride.PlatformOverrideData>

---

#### PlatformSupportException

**Line:** 1565119

**Inherits:** Exception

---

#### PlayAsyncOperation

**Line:** 1585594

---

#### PlayAsyncOperationImpl

**Line:** 1586057

**Fields:**

- `_result`: TResult

---

#### PlayAudioClipSystem

**Line:** 684623

**Inherits:** ReactiveSystem

---

#### PlayCoreEventHandler

**Line:** 1592879

**Inherits:** MonoBehaviour

---

#### PlayCoreOnFailureListener

**Line:** 1592975

**Inherits:** AndroidJavaProxy

**Fields:**

- `OnTaskFailed`: Action<string, int>

---

#### PlayCoreOnSuccessListener

**Line:** 1593062

**Fields:**

- `OnTaskSucceeded`: Action<TAndroidJava>

---

#### PlayMusicComponent

**Line:** 705600

**Inherits:** IComponent

**Fields:**

- `Value`: MusicType

---

#### PlayServicesTask

**Line:** 1593106

---

#### PlayableAsset

**Line:** 890888

**Inherits:** ScriptableObject

---

#### PlayableBehaviour

**Line:** 890920

**Inherits:** IPlayableBehaviour

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

- `Nft`: MetaNft

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

- `Transaction`: PlayerNftTransaction

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

- `TickNumber`: long
- `Action`: PlayerActionBase
- `ModelDiff`: string
- `VagueDifferencePathsMaybe`: List<string>

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

- `m_PlayerEditorConnectionEvents`: PlayerEditorConnectionEvents
- `m_connectedPlayers`: List<int>
- `m_IsInitilized`: bool

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

- `KindId`: MetaActivableKindId
- `ActivableIdStr`: string
- `Phase`: Nullable<MetaActivableState.DebugPhase>

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

- `FirebaseMessagingToken`: string

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

- `_BackingField_ServerListenerCore`: IPlayerDivisionModelServerListenerCore
- `_BackingField_ClientListenerCore`: IPlayerDivisionModelClientListenerCore

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

- `Stars`: int
- `LastActionAt`: MetaTime
- `OldTotalPower`: long
- `TotalPower`: UInt128

---

#### PlayerDivisionUpdateContribution

**Line:** 565749

**Inherits:** PlayerDivisionActionBase

---

#### PlayerEditorConnectionEvents

**Line:** 890676

**Fields:**

- `m_messageTypeId`: string
- `subscriberCount`: int

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

#### PlayerEventExperimentAssignment

**Line:** 537045

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

- `Transaction`: PlayerNftTransaction
- `Nfts`: MetaDictionary<NftKey, MetaNft>

---

#### PlayerExecuteUnsynchronizedServerAction

**Line:** 542929

**Inherits:** MetaMessage

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

- `ExperimentGroupAssignment`: MetaDictionary<PlayerExperimentId, PlayerExperimentsState.ExperimentAssignment>

---

#### PlayerFinalizeNftTransaction

**Line:** 582461

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

- `Transaction`: PlayerNftTransaction

---

#### PlayerFlushActions

**Line:** 538015

**Inherits:** MetaMessage

---

#### PlayerForceDeleteMail

**Line:** 534778

**Inherits:** PlayerSynchronizedServerActionCore

---

#### PlayerGenderChangeUiView

**Line:** 725974

**Inherits:** UiUnityView

**Fields:**

- `MaleSelectIcon`: GameObject
- `FemaleSelectIcon`: GameObject
- `MaleButton`: UnityButton
- `FemaleButton`: UnityButton

---

#### PlayerGenderDisplay

**Line:** 726007

**Inherits:** UiUnityView

**Fields:**

- `Gender`: TMP_Text
- `_gender`: PlayerGender

---

#### PlayerGlobalLeaderboardModel

**Line:** 1067223

**Fields:**

- `MinPowerTop`: long

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

- `PlayerId`: EntityId
- `Approved`: bool

---

#### PlayerHandleJoinResponse

**Line:** 1063760

**Inherits:** MetaResponse

---

#### PlayerIconChangeUiView

**Line:** 726029

**Inherits:** UiUnityView

**Fields:**

- `IconPrefab`: PlayerIconVisual
- `Parent`: Transform

---

#### PlayerIconUiView

**Line:** 726045

**Inherits:** UiUnityView

**Fields:**

- `_currentIconId`: int
- `Icon`: Image

---

#### PlayerIconVisual

**Line:** 726083

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `SelectIcon`: GameObject
- `Button`: UnityButton
- `_id`: int

---

#### PlayerIconsConfig

**Line:** 725923

**Inherits:** ScriptableObject

**Fields:**

- `Icons`: List<Sprite>
- `AdminIcon`: Sprite

---

#### PlayerIdView

**Line:** 721861

**Inherits:** UiUnityView

**Fields:**

- `PlayerIdText`: TMP_Text

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

- `LastDivisionLeaderboard`: MetaDictionary<int, PlayerDivisionParticipantState>
- `LastDivisionIndex`: DivisionIndex
- `OwnIndex`: int
- `NextDivisionTime`: MetaTime
- `PromotionDisplayed`: int
- `ArenaRewardTutorialDisplayed`: bool

---

#### PlayerLeaderboardEntry

**Line:** 1067133

**Inherits:** ILeaderboardEntry

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

#### PlayerLoopSystem

**Line:** 888991

---

#### PlayerLoopTimer

**Line:** 1099485

**Inherits:** IDisposable

**Fields:**

- `isRunning`: bool
- `tryStop`: bool
- `isDisposed`: bool

---

#### PlayerMailItem

**Line:** 561463

**Fields:**

- `_contents`: MetaInGameMail

---

#### PlayerMeleeOnlyStatTarget

**Line:** 1076864

**Inherits:** StatTargetBase

---

#### PlayerMetaOfferGroupsModelBase

**Line:** 544305

---

#### PlayerMiniProfileUiView

**Line:** 727224

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerName`: TMP_Text
- `PowerText`: TMP_Text
- `LastOnlineText`: TMP_Text
- `_guildParent`: GameObject
- `_guildTagText`: TMP_Text
- `_guildEmblemDisplay`: GuildEmblemDisplay
- `Icon`: Image
- `Button`: UnityButton

---

#### PlayerMiscSavegame

**Line:** 1070076

**Fields:**

- `InstallDate`: MetaTime
- `InstallVersion`: string
- `HasRated`: bool
- `PlayerAge`: int
- `PlayerCountry`: string

---

#### PlayerModel

**Line:** 1072724

**Inherits:** PlayerModelBase

**Fields:**

- `RegionalOffset`: MetaDuration
- `_tickables`: List<ITickable>
- `_nextDayListeners`: List<INextDayListener>

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

- `UpdatedName`: string

---

#### PlayerNameChangeResponse

**Line:** 1052090

**Inherits:** MetaResponse

**Fields:**

- `Error`: string

---

#### PlayerNameChangeUiView

**Line:** 726124

**Inherits:** UiUnityView

**Fields:**

- `_inputField`: TMP_InputField
- `_error`: TMP_Text
- `_loading`: GameObject
- `_buttons`: GameObject
- `_priceButton`: CostButtonUiView
- `_playerName`: string

---

#### PlayerNameInputValidator

**Line:** 725962

**Inherits:** TMP_InputValidator

---

#### PlayerNameUiView

**Line:** 726165

**Inherits:** UiUnityView

**Fields:**

- `PlayerName`: TMP_Text
- `_playerName`: string

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

- `Transaction`: PlayerNftTransaction

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

#### PlayerPowerUiView

**Line:** 726379

**Inherits:** UiUnityView

**Fields:**

- `PlayerPower`: TMP_Text
- `_powerFeature`: GameEntity

---

#### PlayerPrefLocaleSelector

**Line:** 1319448

**Inherits:** IStartupLocaleSelector

**Fields:**

- `m_PlayerPreferenceKey`: string

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

#### PlayerPrefsSaveSystem

**Line:** 693736

**Inherits:** ReactiveSystem

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

- `Profile`: PlayerPvpProfileModel

---

#### PlayerProfileTestModel

**Line:** 1058655

---

#### PlayerProfileUiView

**Line:** 726187

**Inherits:** UiUnityView

**Fields:**

- `EditNameButton`: UnityButton
- `EditGenderButton`: UnityButton
- `EditAvatarButton`: UnityButton

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

- `NumSubsets`: int
- `Modifier`: uint

---

#### PlayerPropertyRequirement

**Line:** 541654

---

#### PlayerPushNotifications

**Line:** 543044

**Fields:**

- `_devices`: MetaDictionary<string, PlayerDevicePushNotifications>

---

#### PlayerRangedOnlyStatTarget

**Line:** 1076851

**Inherits:** StatTargetBase

---

#### PlayerRefreshMetaOffers

**Line:** 543840

**Inherits:** PlayerActionCore

**Fields:**

- `_partialRefreshInfo`: Nullable<MetaOfferGroupsRefreshInfo>

---

#### PlayerRemoveNft

**Line:** 582142

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

- `Key`: NftKey

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

- `KindId`: MetaActivableKindId
- `ActivableIdStr`: string
- `Phase`: Nullable<MetaActivableState.DebugPhase>

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

- `parameters`: PlayerSessionDebugModeParameters

---

#### PlayerSessionDebugModeCounter

**Line:** 542585

**Inherits:** PlayerSessionDebugMode

**Fields:**

- `forNextNumSessions`: int

---

#### PlayerSessionDebugModeParameters

**Line:** 542566

**Fields:**

- `EnableEntityDebugConfig`: bool
- `IncidentUploadMode`: PlayerDebugIncidentUploadMode

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

#### PlayerUnitComponent

**Line:** 710607

**Inherits:** IComponent

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

- `Nft`: MetaNft

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

#### PlayerWorldView

**Line:** 705534

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerWorld`: TMP_Text

---

#### PluralLocalizationFormatter

**Line:** 1322032

**Inherits:** FormatterBase

**Fields:**

- `m_DefaultTwoLetterISOLanguageName`: string

---

#### PluralRules

**Line:** 1320882

---

#### PointStyle

**Line:** 1396225

**Inherits:** IDirectResponseSchema

---

#### Pointer

**Line:** 266177

**Inherits:** ISerializable

---

#### PointerCancelEvent

**Line:** 638685

**Inherits:** PointerEventBase

---

#### PointerCaptureEvent

**Line:** 633093

**Inherits:** PointerCaptureEventBase

---

#### PointerCaptureEventBase

**Line:** 632961

---

#### PointerCaptureOutEvent

**Line:** 633058

**Inherits:** PointerCaptureEventBase

---

#### PointerDownEvent

**Line:** 638528

**Inherits:** PointerEventBase

---

#### PointerDownLinkTagEvent

**Line:** 680636

**Inherits:** PointerEventBase

---

#### PointerEnterEvent

**Line:** 638771

**Inherits:** PointerEventBase

---

#### PointerEventBase

**Line:** 637802

**Fields:**

- `m_AltitudeNeedsConversion`: bool
- `m_AzimuthNeedsConversion`: bool
- `m_AltitudeAngle`: float
- `m_AzimuthAngle`: float
- `m_TiltNeeded`: bool
- `m_Tilt`: Vector2

---

#### PointerEventData

**Line:** 1359192

**Inherits:** BaseEventData

**Fields:**

- `m_PointerPress`: GameObject
- `hovered`: List<GameObject>

---

#### PointerInputModule

**Line:** 1360605

**Inherits:** BaseInputModule

**Fields:**

- `m_PointerData`: Dictionary<int, PointerEventData>

---

#### PointerLeaveEvent

**Line:** 638816

**Inherits:** PointerEventBase

---

#### PointerManipulator

**Line:** 642965

**Inherits:** MouseManipulator

**Fields:**

- `m_CurrentPointerId`: int

---

#### PointerMoveEvent

**Line:** 638573

**Inherits:** PointerEventBase

---

#### PointerMoveLinkTagEvent

**Line:** 680533

**Inherits:** PointerEventBase

---

#### PointerOutEvent

**Line:** 638897

**Inherits:** PointerEventBase

---

#### PointerOutLinkTagEvent

**Line:** 680595

**Inherits:** PointerEventBase

---

#### PointerOverEvent

**Line:** 638861

**Inherits:** PointerEventBase

---

#### PointerOverLinkTagEvent

**Line:** 680471

**Inherits:** PointerEventBase

---

#### PointerUpEvent

**Line:** 638641

**Inherits:** PointerEventBase

---

#### PointerUpLinkTagEvent

**Line:** 680697

**Inherits:** PointerEventBase

---

#### Poly1305

**Line:** 1519366

**Inherits:** IMac

**Fields:**

- `r0`: uint
- `r1`: uint
- `r2`: uint
- `r3`: uint
- `r4`: uint
- `s1`: uint
- `s2`: uint
- `s3`: uint
- `s4`: uint
- `k0`: uint
- `k1`: uint
- `k2`: uint
- `k3`: uint
- `currentBlockOffset`: int
- `h0`: uint
- `h1`: uint
- `h2`: uint
- `h3`: uint
- `h4`: uint

---

#### Poly1305KeyGenerator

**Line:** 1519459

**Inherits:** CipherKeyGenerator

---

#### Pool

**Line:** 1582513

---

#### PoolAllocator

**Line:** 557811

**Inherits:** IMemoryAllocator

---

#### PoolComponent

**Line:** 739361

**Inherits:** IComponent

**Fields:**

- `ResourceId`: string
- `Pool`: ObjectPool<GameObject>
- `Parent`: Transform

---

#### PoolIdComponent

**Line:** 693770

**Inherits:** IComponent

**Fields:**

- `Value`: string

---

#### PooledComponent

**Line:** 693759

**Inherits:** IComponent

---

#### PopupClosedMessage

**Line:** 696665

**Inherits:** IMessage

---

#### PopupField

**Line:** 626690

**Fields:**

- `m_Index`: int

---

#### PopupOpenedMessage

**Line:** 696638

**Inherits:** IMessage

---

#### PopupUiView

**Line:** 737401

**Inherits:** MonoBehaviour

**Fields:**

- `CanvasGroup`: CanvasGroup
- `Container`: RectTransform
- `SkipBackgroundClick`: bool
- `_prefabId`: string
- `CloseButton`: UnityButton
- `BackgroundButton`: UnityButton

---

#### PopupWindow

**Line:** 626849

**Inherits:** TextElement

**Fields:**

- `m_ContentContainer`: VisualElement

---

#### PositionAsUV1

**Line:** 1357936

**Inherits:** BaseMeshEffect

---

#### PositionComponent

**Line:** 709156

**Inherits:** IComponent

**Fields:**

- `Value`: Vector2

---

#### PositionEventSystem

**Line:** 702484

**Inherits:** ReactiveSystem

---

#### PositionListenerComponent

**Line:** 699986

**Inherits:** IComponent

**Fields:**

- `value`: List<IPositionListener>

---

#### PositionUpdateView

**Line:** 710793

**Inherits:** GameUnityView

**Fields:**

- `_currentPosition`: Vector2
- `_currentVelocity`: Vector2
- `_timer`: float
- `_maxTimer`: float

---

#### PostConfigureOptions

**Line:** 1540660

---

#### PostConstructorAttribute

**Line:** 1597498

**Inherits:** Attribute

---

#### PostNormalizeAttribute

**Line:** 949801

**Inherits:** PropertyAttribute

---

#### PostProcessData

**Line:** 900398

**Inherits:** ScriptableObject

---

#### PowerComponent

**Line:** 713613

**Inherits:** IComponent

**Fields:**

- `Value`: UInt128

---

#### PowerEventSystem

**Line:** 702505

**Inherits:** ReactiveSystem

---

#### PowerFeature

**Line:** 726324

**Inherits:** Feature

---

#### PowerListenerComponent

**Line:** 699999

**Inherits:** IComponent

**Fields:**

- `value`: List<IPowerListener>

---

#### PowerModelComponent

**Line:** 726259

**Inherits:** IComponent

**Fields:**

- `Value`: PowerReactiveModel

---

#### PowerModelInitializeSystem

**Line:** 726349

**Inherits:** IInitializeSystem

---

#### PowerModelSyncSystem

**Line:** 726364

**Inherits:** IExecuteSystem

---

#### PowerOfTwoTextureAtlas

**Line:** 822215

**Inherits:** Texture2DAtlas

**Fields:**

- `m_RequestedTextures`: Dictionary<int, Vector2Int>

---

#### PowerReactiveModel

**Line:** 726271

**Inherits:** ReactiveModel

---

#### PowerUpdateMessage

**Line:** 726297

**Inherits:** IMessage

---

#### PrePrepareMethodAttribute

**Line:** 230021

**Inherits:** Attribute

---

#### Predicate

**Line:** 17364

---

#### PrefabIdComponent

**Line:** 739379

**Inherits:** IComponent

**Fields:**

- `Value`: string

---

#### PreferBinarySerialization

**Line:** 884761

**Inherits:** Attribute

---

#### PreloadAssetTableMetadata

**Line:** 1327565

**Inherits:** IMetadata

---

#### PrepareDailyDealPurchaseAction

**Line:** 1051059

**Inherits:** PlayerAction

---

#### PreserveAttribute

**Line:** 888601

**Inherits:** Attribute

---

#### PreserveSigAttribute

**Line:** 229213

**Inherits:** Attribute

---

#### PreserveTags

**Line:** 1320060

**Inherits:** IPseudoLocalizationMethod

**Fields:**

- `m_Opening`: char
- `m_Closing`: char

---

#### PrettyPrint

**Line:** 523650

---

#### PrettyPrintAttribute

**Line:** 499161

**Inherits:** Attribute

---

#### PrimalityTest

**Line:** 1450099

**Inherits:** MulticastDelegate

---

#### PrimalityTests

**Line:** 1450111

---

#### PrimaryEntityIndex

**Line:** 1546080

---

#### PrimaryEntityIndexAttribute

**Line:** 1597455

**Inherits:** AbstractEntityIndexAttribute

---

#### PrimeGeneratorBase

**Line:** 1450123

---

#### PrivateKey

**Line:** 1449805

**Fields:**

- `encrypted`: bool
- `rsa`: RSA
- `weak`: bool
- `keyType`: int

---

#### ProbeAdjustmentVolume

**Line:** 816479

**Inherits:** MonoBehaviour

**Fields:**

- `size`: Vector3
- `radius`: float
- `intensityScale`: float
- `overriddenDilationThreshold`: float
- `virtualOffsetRotation`: Vector3
- `virtualOffsetDistance`: float
- `geometryBias`: float
- `virtualOffsetThreshold`: float
- `rayOriginBias`: float
- `skyDirection`: Vector3
- `directSampleCount`: int
- `indirectSampleCount`: int
- `sampleCountMultiplier`: int
- `maxBounces`: int
- `skyOcclusionSampleCount`: int
- `skyOcclusionMaxBounces`: int
- `renderingLayerMask`: byte
- `invalidateProbes`: bool
- `overrideDilationThreshold`: bool

---

#### ProbeReferenceVolume

**Line:** 817934

**Fields:**

- `m_EmptyIndexBuffer`: ComputeBuffer
- `m_IsInitialized`: bool
- `m_SupportScenarios`: bool
- `m_SupportScenarioBlending`: bool
- `m_ForceNoDiskStreaming`: bool
- `m_SupportDiskStreaming`: bool
- `m_SupportGPUStreaming`: bool
- `m_UseStreamingAssets`: bool
- `m_MinBrickSize`: float
- `m_MaxSubdivision`: int
- `m_ProbeOffset`: Vector3
- `m_Pool`: ProbeBrickPool
- `m_Index`: ProbeBrickIndex
- `m_CellIndices`: ProbeGlobalIndirection
- `m_BlendingPool`: ProbeBrickBlendingPool
- `m_TmpSrcChunks`: List<ProbeBrickPool.BrickChunkAlloc>
- `m_CurrGlobalBounds`: Bounds
- `m_CellPool`: ObjectPool<ProbeReferenceVolume.Cell>
- `m_TemporaryDataLocationMemCost`: int
- `minLoadedCellPos`: Vector3Int
- ... (54 more fields)

---

#### ProbeTouchupVolume

**Line:** 816025

**Inherits:** ProbeAdjustmentVolume

---

#### ProbeVolume

**Line:** 819128

**Inherits:** MonoBehaviour

**Fields:**

- `size`: Vector3
- `overrideRendererFilters`: bool
- `minRendererVolumeSize`: float
- `objectLayerMask`: LayerMask
- `lowestSubdivLevelOverride`: int
- `highestSubdivLevelOverride`: int
- `overridesSubdivLevels`: bool
- `fillEmptySpaces`: bool
- `globalVolume`: bool

---

#### ProbeVolumeBakingSet

**Line:** 819351

**Inherits:** ScriptableObject

**Fields:**

- `m_SceneGUIDs`: List<string>
- `m_TotalIndexList`: List<int>
- `m_SerializedPerSceneCellList`: List<ProbeVolumeBakingSet.SerializedPerSceneCellList>
- `m_OtherScenario`: string
- `m_ScenarioBlendingFactor`: float
- `m_ReadCommandArray`: ReadCommandArray
- `m_ReadCommandBuffer`: NativeArray<ReadCommand>
- `m_PrunedIndexList`: List<int>
- `m_PrunedScenarioIndexList`: List<int>
- `probeOffset`: Vector3
- `simplificationLevels`: int
- `minDistanceBetweenProbes`: float
- `renderersLayerMask`: LayerMask
- `minRendererVolumeSize`: float
- `skyOcclusion`: bool
- `skyOcclusionBakingSamples`: int
- `skyOcclusionBakingBounces`: int
- `skyOcclusionAverageAlbedo`: float
- `skyOcclusionBackFaceCulling`: bool
- `skyOcclusionShadingDirection`: bool
- ... (3 more fields)

---

#### ProbeVolumePerSceneData

**Line:** 819911

**Inherits:** MonoBehaviour

**Fields:**

- `obsoleteSerializedScenarios`: List<ProbeVolumePerSceneData.ObsoleteSerializablePerScenarioDataItem>

---

#### ProbeVolumeSceneData

**Line:** 819999

---

#### ProbeVolumesOptions

**Line:** 820147

**Inherits:** VolumeComponent

**Fields:**

- `normalBias`: ClampedFloatParameter
- `viewBias`: ClampedFloatParameter
- `scaleBiasWithMinProbeDistance`: BoolParameter
- `samplingNoise`: ClampedFloatParameter
- `animateSamplingNoise`: BoolParameter
- `leakReductionMode`: APVLeakReductionModeParameter
- `minValidDotProductValue`: ClampedFloatParameter
- `occlusionOnlyReflectionNormalization`: BoolParameter
- `intensityMultiplier`: ClampedFloatParameter
- `skyOcclusionIntensityMultiplier`: ClampedFloatParameter
- `worldOffset`: Vector3Parameter

---

#### Process

**Line:** 777876

**Inherits:** Component

**Fields:**

- `haveProcessId`: bool
- `processId`: int
- `haveProcessHandle`: bool
- `m_processHandle`: SafeProcessHandle
- `isRemoteMachine`: bool
- `machineName`: string
- `m_processAccess`: int
- `threads`: ProcessThreadCollection
- `modules`: ProcessModuleCollection
- `haveWorkingSetLimits`: bool
- `havePriorityClass`: bool
- `startInfo`: ProcessStartInfo
- `watchForExit`: bool
- `watchingForExit`: bool
- `onExited`: EventHandler
- `exited`: bool
- `exitCode`: int
- `signaled`: bool
- `haveExitTime`: bool
- `raisedOnExited`: bool
- ... (8 more fields)

---

#### ProcessModuleCollection

**Line:** 778068

**Inherits:** ReadOnlyCollectionBase

---

#### ProcessStartInfo

**Line:** 778073

**Fields:**

- `fileName`: string
- `arguments`: string
- `directory`: string
- `verb`: string
- `windowStyle`: ProcessWindowStyle
- `errorDialog`: bool
- `errorDialogParentHandle`: IntPtr
- `useShellExecute`: bool
- `userName`: string
- `domain`: string
- `password`: SecureString
- `passwordInClearText`: string
- `loadUserProfile`: bool
- `redirectStandardInput`: bool
- `redirectStandardOutput`: bool
- `redirectStandardError`: bool
- `standardOutputEncoding`: Encoding
- `standardErrorEncoding`: Encoding
- `createNoWindow`: bool
- `weakParentProcess`: WeakReference
- ... (2 more fields)

---

#### ProcessThreadCollection

**Line:** 778235

**Inherits:** ReadOnlyCollectionBase

---

#### Product

**Line:** 1530758

---

#### ProductCatalog

**Line:** 1407169

**Fields:**

- `appleSKU`: string
- `appleTeamID`: string
- `enableCodelessAutoInitialization`: bool
- `enableUnityGamingServicesAutoInitialization`: bool
- `products`: List<ProductCatalogItem>

---

#### ProductCatalogItem

**Line:** 1407070

**Fields:**

- `id`: string
- `type`: ProductType
- `storeIDs`: List<StoreID>
- `defaultDescription`: LocalizedProductDescription
- `screenshotPath`: string
- `applePriceTier`: int
- `googlePrice`: Price
- `pricingTemplateID`: string
- `descriptions`: List<LocalizedProductDescription>
- `udpPrice`: Price
- `payouts`: List<ProductCatalogPayout>

---

#### ProductCatalogPayout

**Line:** 1406934

**Fields:**

- `t`: string
- `st`: string
- `q`: double
- `d`: string

---

#### ProductCollection

**Line:** 1530886

**Fields:**

- `m_IdToProduct`: Dictionary<string, Product>
- `m_StoreSpecificIdToProduct`: Dictionary<string, Product>

---

#### ProductDefinition

**Line:** 1530928

---

#### ProductDescription

**Line:** 1532211

**Fields:**

- `type`: ProductType

---

#### ProductHeaderValue

**Line:** 1490917

**Inherits:** ICloneable

---

#### ProductInfoHeaderValue

**Line:** 1490970

**Inherits:** ICloneable

---

#### ProductMetadata

**Line:** 1531018

---

#### ProfileBaseConfig

**Line:** 1073716

**Inherits:** GameConfigKeyValue

---

#### Profiler

**Line:** 886447

---

#### ProfilerCameraListener

**Line:** 1446403

**Inherits:** MonoBehaviour

**Fields:**

- `_camera`: Camera
- `_stopwatch`: Stopwatch
- `RenderDurationCallback`: Action<ProfilerCameraListener, double>

---

#### ProfilerEnableControl

**Line:** 1444636

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_previousState`: bool
- `ButtonText`: Text
- `EnableButton`: Button
- `Text`: Text

---

#### ProfilerFPSLabel

**Line:** 1442992

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_nextUpdate`: float
- `_profilerService`: IProfilerService
- `UpdateFrequency`: float
- `_text`: Text

---

#### ProfilerGraphAxisLabel

**Line:** 1444667

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_prevFrameTime`: float
- `_queuedFrameTime`: Nullable<float>
- `_yPosition`: float
- `Text`: Text

---

#### ProfilerGraphControl

**Line:** 1444704

**Inherits:** Graphic

**Fields:**

- `FloatingScale`: bool
- `TargetFpsUseApplication`: bool
- `DrawAxes`: bool
- `TargetFps`: int
- `Clip`: bool
- `VerticalPadding`: int
- `_profilerService`: IProfilerService
- `_clipBounds`: Rect

---

#### ProfilerLateUpdateListener

**Line:** 1446433

**Inherits:** MonoBehaviour

**Fields:**

- `OnLateUpdate`: Action

---

#### ProfilerMemoryBlock

**Line:** 1444569

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_lastRefresh`: float
- `CurrentUsedText`: Text
- `Slider`: Slider
- `TotalAllocatedText`: Text

---

#### ProfilerMonoBlock

**Line:** 1444603

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_lastRefresh`: float
- `CurrentUsedText`: Text
- `NotSupportedMessage`: GameObject
- `Slider`: Slider
- `TotalAllocatedText`: Text
- `_isSupported`: bool

---

#### ProfilerServiceImpl

**Line:** 1446448

**Inherits:** SRServiceBase

**Fields:**

- `_lateUpdateListener`: ProfilerLateUpdateListener
- `_updateDuration`: double
- `_renderStartTime`: double
- `_renderDuration`: double
- `_camerasThisFrame`: int

---

#### ProfilerTabController

**Line:** 1443401

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_isDirty`: bool
- `PinToggle`: Toggle

---

#### ProfilingSampler

**Line:** 815288

**Fields:**

- `m_Recorder`: Recorder
- `m_InlineRecorder`: Recorder

---

#### ProgressBar

**Line:** 626978

**Inherits:** AbstractProgressBar

---

#### ProgressKeyBase

**Line:** 1078460

**Inherits:** IEquatable

---

#### ProgressKeysTypeCode

**Line:** 1078445

---

#### ProgressPassModel

**Line:** 1078721

---

#### ProgressPassPanelView

**Line:** 726614

**Inherits:** MonoBehaviour

**Fields:**

- `Purchasable`: bool
- `ActivatePassButton`: UnityButton
- `PassPriceText`: TMP_Text
- `ProgressTracksSubPanel`: ProgressTracksSubPanelView
- `_passPurchased`: bool
- `PassIdx`: int
- `AutoInit`: bool

---

#### ProgressPassParsers

**Line:** 1052364

**Inherits:** ConfigParserProvider

---

#### ProgressPassPurchasedMessage

**Line:** 726402

**Inherits:** IMessage

---

#### ProgressPassRedDotLogic

**Line:** 726575

**Inherits:** IRedDotLogic

**Fields:**

- `_cachedClaimableRewardsCount`: int

---

#### ProgressPassTier

**Line:** 1078667

**Inherits:** IGameConfigData

---

#### ProgressTrackTierEntryView

**Line:** 726761

**Inherits:** MonoBehaviour

**Fields:**

- `RectTransform`: RectTransform
- `RewardContainers`: List<RewardsContainerView>
- `ProgressText`: TMP_Text
- `ProgressKeyBackground`: Image
- `ProgressPassTier`: ProgressPassTier

---

#### ProgressTracksSubPanelView

**Line:** 726698

**Inherits:** MonoBehaviour

**Fields:**

- `Content`: RectTransform
- `ScrollRect`: ScrollRect
- `ContentLayoutGroup`: HorizontalOrVerticalLayoutGroup
- `TierEntryPrefab`: ProgressTrackTierEntryView
- `MiddleProgressBar`: RectTransform
- `_lastReachedTierIndex`: int
- `_allTiers`: List<ProgressPassTier>
- `_horizontal`: bool

---

#### ProjectSettingsInformationAnalytic

**Line:** 1587175

**Inherits:** AnalyticsEventBase

**Fields:**

- `agent_types_count`: int
- `areas_count`: int

---

#### Property

**Line:** 1458258

**Fields:**

- `m_Attributes`: List<Attribute>

---

#### PropertyAttribute

**Line:** 880762

**Inherits:** Attribute

---

#### PropertyBag

**Line:** 1466302

---

#### PropertyBuilder

**Line:** 270140

**Inherits:** PropertyInfo

---

#### PropertyChangedEventArgs

**Line:** 783349

**Inherits:** EventArgs

---

#### PropertyChangedEventHandler

**Line:** 783367

**Inherits:** MulticastDelegate

---

#### PropertyChangingEventArgs

**Line:** 783379

**Inherits:** EventArgs

---

#### PropertyChangingEventHandler

**Line:** 783391

**Inherits:** MulticastDelegate

---

#### PropertyCollection

**Line:** 1087109

**Inherits:** Hashtable

---

#### PropertyDescriptor

**Line:** 782519

**Inherits:** MemberDescriptor

**Fields:**

- `_converter`: TypeConverter
- `_valueChangedHandlers`: Hashtable
- `_editorCount`: int

---

#### PropertyDescriptorCollection

**Line:** 782643

**Inherits:** ICollection

**Fields:**

- `_cachedFoundProperties`: IDictionary
- `_cachedIgnoreCase`: bool
- `_propsOwned`: bool
- `_needSort`: bool
- `_readOnly`: bool

---

#### PropertyGetter

**Line:** 1458101

---

#### PropertyInfo

**Line:** 266226

**Inherits:** MemberInfo

---

#### PropertyReference

**Line:** 1507965

---

#### PropertySetter

**Line:** 1458123

---

#### ProtectedRange

**Line:** 1396273

**Inherits:** IDirectResponseSchema

---

#### ProtocolViolationException

**Line:** 791972

**Inherits:** InvalidOperationException

---

#### ProvidePropertyAttribute

**Line:** 782829

**Inherits:** Attribute

---

#### ProviderAliasAttribute

**Line:** 1555406

**Inherits:** Attribute

---

#### ProviderException

**Line:** 1434946

**Inherits:** OperationException

---

#### ProviderLoadRequestOptions

**Line:** 1437522

**Fields:**

- `m_IgnoreFailures`: bool
- `m_WebRequestTimeout`: int

---

#### ProxyAttribute

**Line:** 221947

**Inherits:** Attribute

---

#### ProxyElement

**Line:** 803152

**Inherits:** ConfigurationElement

---

#### PseudoLocale

**Line:** 1320095

**Inherits:** Locale

**Fields:**

- `m_Methods`: List<IPseudoLocalizationMethod>

---

#### PublicAPIAttribute

**Line:** 869316

**Inherits:** Attribute

---

#### PublicKey

**Line:** 779096

**Fields:**

- `_keyValue`: AsnEncodedData
- `_params`: AsnEncodedData
- `_oid`: Oid

---

#### PublishedApp

**Line:** 1564916

**Fields:**

- `bundleId`: string
- `platform`: PublishedAppPlatform

---

#### PulseDurationComponent

**Line:** 731390

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### PulseTimerComponent

**Line:** 731378

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### PulseTimerEventSystem

**Line:** 702547

**Inherits:** ReactiveSystem

---

#### PulseTimerListenerComponent

**Line:** 700025

**Inherits:** IComponent

**Fields:**

- `value`: List<IPulseTimerListener>

---

#### PurchaseAnalyticsContext

**Line:** 585847

---

#### PurchaseEventArgs

**Line:** 1531102

---

#### PurchaseFailedEventArgs

**Line:** 1531126

---

#### PurchaseFailureDescription

**Line:** 1532275

---

#### PurchasedComponent

**Line:** 729717

**Inherits:** IComponent

---

#### PureAttribute

**Line:** 869326

**Inherits:** Attribute

---

#### PureQuaternionPlugin

**Line:** 1430357

**Inherits:** ABSTweenPlugin

---

#### PushNotificationService

**Line:** 694287

**Inherits:** IPushNotificationService

**Fields:**

- `_platformService`: IPushNotificationService

---

#### PushNotificationServiceComponent

**Line:** 693869

**Inherits:** IComponent

**Fields:**

- `Value`: IPushNotificationService

---

#### PushNotificationsFeature

**Line:** 694320

**Inherits:** Feature

---

#### QuadraticBezierPath

**Line:** 722970

**Inherits:** IPath

---

#### QualitySettings

**Line:** 873417

**Inherits:** Object

---

#### QuaternionPlugin

**Line:** 1429359

**Inherits:** ABSTweenPlugin

---

#### QueryLastRespondedNotificationOp

**Line:** 1591490

**Inherits:** CustomYieldInstruction

**Fields:**

- `notification`: Nullable<Notification>
- `state`: QueryLastRespondedNotificationState

---

#### Queue

**Line:** 409073

**Fields:**

- `_head`: int
- `_tail`: int
- `_size`: int
- `_version`: int
- `_syncRoot`: object

---

#### QuickSaveGridUiView

**Line:** 728083

**Inherits:** MonoBehaviour

**Fields:**

- `QuickSaveViewEntryPrefab`: QuickSaveViewEntry
- `Parent`: Transform

---

#### QuickSavePathProvider

**Line:** 727950

---

#### QuickSaveViewEntry

**Line:** 728105

**Inherits:** MonoBehaviour

**Fields:**

- `SavegameName`: TMP_Text
- `LoadButton`: UnityButton
- `DeleteButton`: UnityButton

---

#### RC2

**Line:** 218585

**Inherits:** SymmetricAlgorithm

**Fields:**

- `EffectiveKeySizeValue`: int

---

#### RC2CryptoServiceProvider

**Line:** 218616

**Inherits:** RC2

**Fields:**

- `m_use40bitSalt`: bool

---

#### RC4

**Line:** 1449601

**Inherits:** SymmetricAlgorithm

---

#### RFC3339DateTimeConverter

**Line:** 1496455

**Inherits:** JsonConverter

---

#### RIPEMD160

**Line:** 218801

**Inherits:** HashAlgorithm

---

#### RIPEMD160Managed

**Line:** 218814

**Inherits:** RIPEMD160

**Fields:**

- `_count`: long

---

#### RNGCryptoServiceProvider

**Line:** 219829

**Inherits:** RandomNumberGenerator

**Fields:**

- `_handle`: IntPtr

---

#### RSA

**Line:** 218882

**Inherits:** AsymmetricAlgorithm

---

#### RSACryptoServiceProvider

**Line:** 218925

**Inherits:** RSA

**Fields:**

- `store`: KeyPairPersistence
- `persistKey`: bool
- `persisted`: bool
- `privateKeyExportable`: bool
- `m_disposed`: bool
- `rsa`: RSAManaged

---

#### RSAManaged

**Line:** 1449641

**Inherits:** RSA

**Fields:**

- `isCRTpossible`: bool
- `keyBlinding`: bool
- `keypairGenerated`: bool
- `m_disposed`: bool
- `d`: BigInteger
- `p`: BigInteger
- `q`: BigInteger
- `dp`: BigInteger
- `dq`: BigInteger
- `qInv`: BigInteger
- `n`: BigInteger
- `e`: BigInteger

---

#### RSAPKCS1SignatureDeformatter

**Line:** 219870

**Inherits:** AsymmetricSignatureDeformatter

**Fields:**

- `rsa`: RSA
- `hashName`: string

---

#### RSAPKCS1SignatureFormatter

**Line:** 219896

**Inherits:** AsymmetricSignatureFormatter

---

#### RSASignaturePadding

**Line:** 217805

**Inherits:** IEquatable

---

#### RTHandle

**Line:** 822307

---

#### RTHandleSystem

**Line:** 822812

**Inherits:** IDisposable

**Fields:**

- `m_HardwareDynamicResRequested`: bool
- `m_AutoSizedRTs`: HashSet<RTHandle>
- `m_ResizeOnDemandRTs`: HashSet<RTHandle>
- `m_RTHandleProperties`: RTHandleProperties
- `m_MaxWidths`: int
- `m_MaxHeights`: int

---

#### RWIOBufferBase

**Line:** 567496

**Inherits:** IOBuffer

---

#### RadioButton

**Line:** 627013

**Inherits:** BaseBoolField

**Fields:**

- `m_CheckmarkBackground`: VisualElement

---

#### RadioButtonGroup

**Line:** 627154

**Inherits:** BaseField

**Fields:**

- `m_ChoiceRadioButtonContainer`: VisualElement
- `m_ContentContainer`: VisualElement
- `m_GetAllRadioButtonsQuery`: UQueryBuilder<RadioButton>
- `m_SelectedRadioButton`: RadioButton
- `m_UpdatingButtons`: bool
- `m_Choices`: List<string>

---

#### RadiusComponent

**Line:** 709194

**Inherits:** IComponent

**Fields:**

- `Value`: float

---

#### RadiusEventSystem

**Line:** 702568

**Inherits:** ReactiveSystem

---

#### RadiusListenerComponent

**Line:** 700038

**Inherits:** IComponent

**Fields:**

- `value`: List<IRadiusListener>

---

#### RangeAttribute

**Line:** 1509762

**Inherits:** ValidationAttribute

---

#### RangeConditionHeaderValue

**Line:** 1491026

**Inherits:** ICloneable

---

#### RangeHeaderValue

**Line:** 1491079

**Inherits:** ICloneable

**Fields:**

- `ranges`: List<RangeItemHeaderValue>
- `unit`: string

---

#### RangeItemHeaderValue

**Line:** 1491120

**Inherits:** ICloneable

---

#### RankException

**Line:** 31138

**Inherits:** SystemException

---

#### RasterCommandBuffer

**Line:** 805798

**Inherits:** BaseCommandBuffer

---

#### RateTheGameView

**Line:** 728509

**Inherits:** MonoBehaviour

**Fields:**

- `Stars5`: UnityButton
- `Stars1to4`: UnityButton

---

#### RateUsAction

**Line:** 1069970

**Inherits:** PlayerAction

---

#### RateUsCheatContainer

**Line:** 686281

**Inherits:** AbstractCheatContainer

---

#### RateUsSystem

**Line:** 728471

**Inherits:** IInitSystem

---

#### RateUsView

**Line:** 728534

**Inherits:** MonoBehaviour

**Fields:**

- `YesButton`: UnityButton
- `NoButton`: UnityButton

---

#### RawColorHistory

**Line:** 908014

**Inherits:** CameraHistoryItem

**Fields:**

- `m_Descriptor`: RenderTextureDescriptor
- `m_DescKey`: Hash128

---

#### RawDepthHistory

**Line:** 908059

**Inherits:** CameraHistoryItem

**Fields:**

- `m_Descriptor`: RenderTextureDescriptor
- `m_DescKey`: Hash128

---

#### RawImage

**Line:** 1355804

**Inherits:** MaskableGraphic

**Fields:**

- `m_Texture`: Texture
- `m_UVRect`: Rect

---

#### RawResult

**Line:** 1569150

---

#### RayTracingAccelerationStructure

**Line:** 892865

**Inherits:** IDisposable

---

#### RayTracingShader

**Line:** 898658

**Inherits:** Object

---

#### RaysCoordinatesToUV2

**Line:** 714180

**Inherits:** BaseMeshEffect

**Fields:**

- `_offset`: Vector2
- `_fitWidth`: bool
- `_fitHeight`: bool

---

#### ReactableUiView

**Line:** 707990

**Inherits:** MonoBehaviour

**Fields:**

- `ReactionPicker`: RectTransform
- `Layout`: LayoutGroup
- `ActiveReactionsParent`: RectTransform
- `ReactionPickerGrid`: GridLayoutGroup
- `ActiveReactionsGrid`: GridLayoutGroup
- `ReactionEntryPrefab`: ReactionEntryUiView
- `HoldToSelectButton`: HoldDownButton
- `ReactionPickerMaxColumnCount`: int
- `ActiveReactionsMaxColumnCount`: int
- `_reactionPickerSequence`: Sequence
- `_activeReactions`: List<ReactionEntryUiView>
- `_pickerEntries`: List<ReactionEntryUiView>
- `_cachedMessageId`: long

---

#### ReactionEntryUiView

**Line:** 708091

**Inherits:** MonoBehaviour

**Fields:**

- `ReactionText`: TMP_Text
- `BackgroundImage`: Image
- `ReactionButton`: UnityButton
- `ContentTransform`: RectTransform
- `_messageId`: long
- `_defaultBackgroundColor`: Color

---

#### ReactionItem

**Line:** 706351

**Fields:**

- `RoomId`: string
- `MessageId`: long
- `UserIdsByReaction`: Dictionary<string, string[]>

---

#### ReactiveDictionary

**Line:** 694402

---

#### ReactiveModel

**Line:** 694543

---

#### ReactiveProperty

**Line:** 694681

**Fields:**

- `_value`: TValue
- `_hasValue`: bool
- `_isDisposed`: bool

---

#### ReactiveSet

**Line:** 695003

---

#### ReactiveSystem

**Line:** 1547193

**Fields:**

- `_toStringCache`: string

---

#### ReadOnlyAsyncReactiveProperty

**Line:** 1095930

**Fields:**

- `triggerEvent`: TriggerEvent<T>
- `latestValue`: T
- `enumerator`: IUniTaskAsyncEnumerator<T>

---

#### ReadOnlyAttribute

**Line:** 837977

**Inherits:** Attribute

---

#### ReadOnlyCollection

**Line:** 285744

**Fields:**

- `list`: IList<T>
- `_syncRoot`: object

---

#### ReadOnlyCollectionBase

**Line:** 276704

**Inherits:** ICollection

**Fields:**

- `_list`: ArrayList

---

#### ReadOnlyCollectionBuilder

**Line:** 1299259

**Fields:**

- `_size`: int
- `_version`: int

---

#### ReadOnlyControl

**Line:** 1444973

**Inherits:** DataBoundControl

**Fields:**

- `ValueText`: Text
- `Title`: Text

---

#### ReadOnlyDictionary

**Line:** 311389

**Fields:**

- `_syncRoot`: object

---

#### ReadOnlyException

**Line:** 1080859

**Inherits:** DataException

---

#### ReadOnlyMemoryStream

**Line:** 523817

**Inherits:** Stream

---

#### ReadOnlyMessageFragment

**Line:** 1319657

**Inherits:** MessageFragment

---

#### ReadOnlySequenceSegment

**Line:** 466807

---

#### ReaderWriterLock

**Line:** 181939

**Inherits:** CriticalFinalizerObject

**Fields:**

- `seq_num`: int
- `state`: int
- `readers`: int
- `writer_lock_owner`: int
- `writer_queue`: LockQueue
- `reader_locks`: Hashtable

---

#### ReaderWriterLockSlim

**Line:** 1304508

**Inherits:** IDisposable

**Fields:**

- `fIsReentrant`: bool
- `myLock`: int
- `numWriteWaiters`: uint
- `numReadWaiters`: uint
- `numWriteUpgradeWaiters`: uint
- `numUpgradeWaiters`: uint
- `fNoWaiters`: bool
- `upgradeLockOwnerId`: int
- `writeLockOwnerId`: int
- `writeEvent`: EventWaitHandle
- `readEvent`: EventWaitHandle
- `upgradeEvent`: EventWaitHandle
- `waitUpgradeEvent`: EventWaitHandle
- `lockID`: long
- `fUpgradeThreadHoldingRead`: bool
- `owners`: uint
- `fDisposed`: bool

---

#### RealProxy

**Line:** 222004

**Fields:**

- `class_to_proxy`: Type
- `_targetDomainId`: int
- `_objTP`: object
- `_stubData`: object

---

#### ReceiptParserException

**Line:** 1407758

**Inherits:** Exception

---

#### ReceiveOldLeaderboardAction

**Line:** 1055937

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

- `LeaderboardEntries`: MetaDictionary<int, PlayerDivisionParticipantState>
- `DivisionIndex`: DivisionIndex
- `ParticipantIndex`: int
- `NextDivisionTime`: MetaTime

---

#### Recorder

**Line:** 886498

**Fields:**

- `m_RecorderCPU`: ProfilerRecorder
- `m_RecorderGPU`: ProfilerRecorder

---

#### RecreatePipelineOnChangeAttribute

**Line:** 892933

**Inherits:** Attribute

---

#### RectField

**Line:** 616447

**Inherits:** BaseCompositeField

---

#### RectIntField

**Line:** 616549

**Inherits:** BaseCompositeField

---

#### RectMask2D

**Line:** 1355853

**Inherits:** UIBehaviour

**Fields:**

- `m_RectTransform`: RectTransform
- `m_MaskableTargets`: HashSet<MaskableGraphic>
- `m_ClipTargets`: HashSet<IClippable>
- `m_ShouldRecalculateClipRects`: bool
- `m_Clippers`: List<RectMask2D>
- `m_LastClipRectCanvasSpace`: Rect
- `m_ForceClip`: bool
- `m_Padding`: Vector4
- `m_Softness`: Vector2Int
- `m_Canvas`: Canvas

---

#### RectOffset

**Line:** 872384

**Inherits:** IFormattable

---

#### RectOffsetPlugin

**Line:** 1429392

**Inherits:** ABSTweenPlugin

---

#### RectPlugin

**Line:** 1429431

**Inherits:** ABSTweenPlugin

---

#### RectTransform

**Line:** 886005

**Inherits:** Transform

---

#### RectTransformUtility

**Line:** 1576315

---

#### RedDotChangeMessage

**Line:** 695212

**Inherits:** IMessage

---

#### RedDotEntry

**Line:** 695293

**Inherits:** IEquatable

---

#### RedDotId

**Line:** 695228

**Inherits:** IRedDotEntryDatum

---

#### RedDotManager

**Line:** 695383

**Inherits:** Singleton

**Fields:**

- `_redDotLogics`: List<IRedDotLogic>

---

#### RedDotUiView

**Line:** 695467

**Inherits:** MonoBehaviour

**Fields:**

- `RedDotGameObject`: GameObject
- `EntryData`: IRedDotEntryDatum

---

#### ReferenceConverter

**Line:** 782868

**Inherits:** TypeConverter

**Fields:**

- `_type`: Type

---

#### ReferenceHandler

**Line:** 1008439

---

#### ReferenceResolver

**Line:** 1008474

---

#### RefillHammerUiView

**Line:** 730180

**Inherits:** UiUnityView

**Fields:**

- `Reward`: TMP_Text
- `BuyButton`: PriceButtonEntitasUiView
- `_shopResource`: GameEntity

---

#### ReflectionAttributeProvider

**Line:** 1041166

**Inherits:** IAttributeProvider

---

#### ReflectionMethodsCache

**Line:** 1357721

---

#### ReflectionProbe

**Line:** 871455

**Inherits:** Behaviour

---

#### ReflectionSource

**Line:** 1322104

**Inherits:** ISource

---

#### ReflectionTypeLoadException

**Line:** 266315

**Inherits:** SystemException

---

#### ReflectionValueProvider

**Line:** 1041186

**Inherits:** IValueProvider

---

#### RefreshCancellationStatus

**Line:** 1396429

**Inherits:** IDirectResponseSchema

---

#### RefreshChatStateMessage

**Line:** 708186

**Inherits:** IMessage

---

#### RefreshDailyDealsAction

**Line:** 1051105

**Inherits:** PlayerSynchronizedServerActionCore

---

#### RefreshDailyDealsViewsSystem

**Line:** 730064

**Inherits:** IExecuteSystem

---

#### RefreshDataSourceObjectExecutionStatus

**Line:** 1396477

**Inherits:** IDirectResponseSchema

---

#### RefreshDataSourceRequest

**Line:** 1396525

**Inherits:** IDirectResponseSchema

---

#### RefreshDataSourceResponse

**Line:** 1396597

**Inherits:** IDirectResponseSchema

---

#### RefreshEventArgs

**Line:** 782946

**Inherits:** EventArgs

---

#### RefreshEventHandler

**Line:** 782959

**Inherits:** MulticastDelegate

---

#### RefreshKeyCounter

**Line:** 523948

**Fields:**

- `_drainingGeneration`: OrderedSet<TKey>
- `_fillingGeneration`: OrderedSet<TKey>
- `_updateCycle`: int

---

#### RefreshPropertiesAttribute

**Line:** 784784

**Inherits:** Attribute

**Fields:**

- `refresh`: RefreshProperties

---

#### RefreshTokenRequest

**Line:** 1375324

**Inherits:** TokenRequest

---

#### Regex

**Line:** 776016

**Inherits:** ISerializable

---

#### RegexConverter

**Line:** 1048681

**Inherits:** JsonConverter

---

#### RegexMatchTimeoutException

**Line:** 776736

**Inherits:** TimeoutException

---

#### RegexRunner

**Line:** 777203

**Fields:**

- `_timeout`: int
- `_ignoreTimeout`: bool
- `_timeoutOccursAt`: int
- `_timeoutChecksToSkip`: int

---

#### RegexRunnerFactory

**Line:** 777305

---

#### RegexValidator

**Line:** 717356

**Inherits:** TMP_InputValidator

---

#### RegionInfo

**Line:** 275054

**Fields:**

- `regionId`: int
- `iso2Name`: string
- `iso3Name`: string
- `win3Name`: string
- `englishName`: string
- `nativeName`: string
- `currencySymbol`: string
- `isoCurrencySymbol`: string
- `currencyEnglishName`: string
- `currencyNativeName`: string

---

#### RegisterGenericJobTypeAttribute

**Line:** 1168866

**Inherits:** Attribute

**Fields:**

- `ConcreteType`: Type

---

#### RegisterMigrationsFunctionAttribute

**Line:** 604126

**Inherits:** Attribute

---

#### RegisterUxmlCacheAttribute

**Line:** 669384

**Inherits:** Attribute

---

#### RegisteredWaitHandle

**Line:** 181976

**Inherits:** MarshalByRefObject

**Fields:**

- `_waitObject`: WaitHandle
- `_callback`: WaitOrTimerCallback
- `_state`: object
- `_finalEvent`: WaitHandle
- `_cancelEvent`: ManualResetEvent
- `_timeout`: TimeSpan
- `_callsInProcess`: int
- `_executeOnlyOnce`: bool
- `_unregistered`: bool

---

#### RegularExpressionAttribute

**Line:** 1509881

**Inherits:** ValidationAttribute

---

#### ReliabilityContractAttribute

**Line:** 230005

**Inherits:** Attribute

---

#### ReloadAttribute

**Line:** 810976

**Inherits:** Attribute

---

#### ReloadGroupAttribute

**Line:** 810992

**Inherits:** Attribute

---

#### RemainingSecondsComponent

**Line:** 696257

**Inherits:** IComponent

**Fields:**

- `Value`: long

---

#### RemainingSecondsEventSystem

**Line:** 702589

**Inherits:** ReactiveSystem

---

#### RemainingSecondsListenerComponent

**Line:** 700051

**Inherits:** IComponent

**Fields:**

- `value`: List<IRemainingSecondsListener>

---

#### RemainingSecondsView

**Line:** 696402

**Inherits:** MonoBehaviour

**Fields:**

- `TimerText`: TMP_Text
- `Digits`: int
- `Text`: string
- `TextColor`: Color
- `TimeColor`: Color
- `_timerEntity`: GameEntity

---

#### RemoteCertificateValidationCallback

**Line:** 802790

**Inherits:** MulticastDelegate

---

#### RemoteConfigSettings

**Line:** 1585280

**Fields:**

- `Updated`: Action<bool>

---

#### RemoteProviderException

**Line:** 1434966

**Inherits:** ProviderException

---

#### RemoteSettings

**Line:** 1585233

---

#### RemotingException

**Line:** 221387

**Inherits:** SystemException

---

#### RemotingSurrogateSelector

**Line:** 224765

**Inherits:** ISurrogateSelector

**Fields:**

- `_next`: ISurrogateSelector

---

#### RemoveClaimGameSystem

**Line:** 703981

**Inherits:** ICleanupSystem

---

#### RemoveHitGameSystem

**Line:** 704013

**Inherits:** ICleanupSystem

---

#### RemoveIapPurchaseGameSystem

**Line:** 704029

**Inherits:** ICleanupSystem

---

#### RemoveTryBuyGameSystem

**Line:** 704045

**Inherits:** ICleanupSystem

---

#### RemoveUserFromChannelRequest

**Line:** 1526523

**Inherits:** IEquatable

---

#### RemovedInVersionAttribute

**Line:** 600914

**Inherits:** Attribute

---

#### RenderGraph

**Line:** 828602

**Fields:**

- `nativeCompiler`: NativePassCompiler
- `m_RenderGraphPool`: RenderGraphObjectPool
- `m_builderInstance`: RenderGraphBuilders
- `m_RendererLists`: List<RendererListHandle>
- `m_DebugParameters`: RenderGraphDebugParams
- `m_FrameInformationLogger`: RenderGraphLogger
- `m_DefaultResources`: RenderGraphDefaultResources
- `m_DefaultProfilingSamplers`: Dictionary<int, ProfilingSampler>
- `m_RenderGraphContext`: InternalRenderGraphContext
- `m_PreviousCommandBuffer`: CommandBuffer
- `m_CompilationCache`: RenderGraphCompilationCache
- `m_CullingStack`: Stack<int>
- `m_CurrentExecutionName`: string
- `m_ExecutionCount`: int
- `m_CurrentFrameIndex`: int
- `m_CurrentImmediatePassIndex`: int
- `m_ExecutionExceptionWasRaised`: bool
- `m_HasRenderGraphBegun`: bool
- `m_RendererListCulling`: bool
- `m_EnableCompilationCaching`: bool
- ... (3 more fields)

---

#### RenderGraphDefaultResources

**Line:** 829650

**Fields:**

- `m_BlackTexture2D`: RTHandle
- `m_WhiteTexture2D`: RTHandle
- `m_ShadowTexture2D`: RTHandle

---

#### RenderGraphGlobalSettings

**Line:** 821082

**Inherits:** IRenderPipelineGraphicsSettings

**Fields:**

- `m_EnableCompilationCaching`: bool
- `m_EnableValidityChecks`: bool

---

#### RenderGraphObjectPool

**Line:** 829942

**Fields:**

- `m_AllocatedMaterialPropertyBlocks`: List<MaterialPropertyBlock>

---

#### RenderGraphSettings

**Line:** 913862

**Inherits:** IRenderPipelineGraphicsSettings

**Fields:**

- `m_EnableRenderCompatibilityMode`: bool

---

#### RenderObjects

**Line:** 912548

**Inherits:** ScriptableRendererFeature

**Fields:**

- `renderObjectsPass`: RenderObjectsPass

---

#### RenderObjectsPass

**Line:** 911460

**Inherits:** ScriptableRenderPass

**Fields:**

- `renderQueueType`: RenderQueueType
- `m_FilteringSettings`: FilteringSettings
- `m_ShaderTagIdList`: List<ShaderTagId>
- `m_RenderStateBlock`: RenderStateBlock

---

#### RenderPipeline

**Line:** 895863

---

#### RenderPipelineAsset

**Line:** 896078

---

#### RenderPipelineGlobalSettings

**Line:** 896122

**Inherits:** ScriptableObject

---

#### RenderPipelineGraphicsSettingsCollection

**Line:** 892888

**Fields:**

- `m_List`: List<IRenderPipelineGraphicsSettings>

---

#### RenderPipelineGraphicsSettingsContainer

**Line:** 821226

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `m_RuntimeSettings`: RenderPipelineGraphicsSettingsCollection

---

#### RenderPipelineResources

**Line:** 821252

**Inherits:** ScriptableObject

---

#### RenderSettings

**Line:** 874005

**Inherits:** Object

---

#### RenderTexture

**Line:** 877324

**Inherits:** Texture

---

#### RenderTextureParameter

**Line:** 827542

**Inherits:** VolumeParameter

---

#### Renderer

**Line:** 873825

**Inherits:** Component

---

#### Renderer2DData

**Line:** 1364295

**Inherits:** ScriptableRendererData

**Fields:**

- `m_LayerMask`: LayerMask
- `m_TransparencySortMode`: TransparencySortMode
- `m_TransparencySortAxis`: Vector3
- `m_HDREmulationScale`: float
- `m_LightRenderTextureScale`: float
- `m_UseDepthStencilBuffer`: bool
- `m_UseCameraSortingLayersTexture`: bool
- `m_CameraSortingLayersTextureBound`: int
- `m_CameraSortingLayerDownsamplingMethod`: Downsampling
- `m_MaxLightRenderTextureCount`: uint
- `m_MaxShadowRenderTextureCount`: uint
- `m_PostProcessData`: PostProcessData

---

#### RenderingLayerMaskParameter

**Line:** 826972

**Inherits:** VolumeParameter

---

#### RepeatButton

**Line:** 627268

**Inherits:** TextElement

**Fields:**

- `m_Clickable`: Clickable
- `m_AcceptClicksIfDisabled`: bool

---

#### RepeatCellRequest

**Line:** 1396633

**Inherits:** IDirectResponseSchema

---

#### Repeatable

**Line:** 1495078

---

#### ReportMessageRequest

**Line:** 1527141

**Inherits:** IEquatable

---

#### Request

**Line:** 1396693

**Inherits:** IDirectResponseSchema

---

#### RequestActivateSteppingStonesAutoRunAction

**Line:** 1079904

**Inherits:** PlayerAction

---

#### RequestAutoRunSteppingStonesAction

**Line:** 1079386

**Inherits:** PlayerAction

---

#### RequestBuilder

**Line:** 1495606

**Fields:**

- `method`: string

---

#### RequestCachePolicy

**Line:** 799191

**Fields:**

- `m_Level`: RequestCacheLevel

---

#### RequestCreateSteppingStonesRunAction

**Line:** 1079399

**Inherits:** PlayerAction

---

#### RequestError

**Line:** 1495701

---

#### RequestFailedException

**Line:** 1589079

**Inherits:** Exception

---

#### RequestGlobalLeaderboardMessage

**Line:** 1067076

**Inherits:** MetaRequest

---

#### RequestParameterAttribute

**Line:** 1495154

**Inherits:** Attribute

---

#### RequestPlayerProfileAction

**Line:** 1058618

**Inherits:** PlayerAction

**Fields:**

- `PlayerId`: string

---

#### RequestResponseAttribute

**Line:** 499070

**Inherits:** Attribute

---

#### RequireComponent

**Line:** 881528

**Inherits:** Attribute

**Fields:**

- `m_Type0`: Type
- `m_Type1`: Type
- `m_Type2`: Type

---

#### RequireImplementorsAttribute

**Line:** 888611

**Inherits:** Attribute

---

#### RequiredAttribute

**Line:** 1509956

**Inherits:** ValidationAttribute

---

#### RequiredFieldAttribute

**Line:** 1505844

**Inherits:** Attribute

**Fields:**

- `_autoCreate`: bool
- `_autoSearch`: bool
- `_editorOnly`: bool

---

#### ResetPushNotesSystem

**Line:** 694362

**Inherits:** ReactiveSystem

---

#### ResetTimerSystem

**Line:** 696351

**Inherits:** MultiReactiveSystem

---

#### ResolveEventArgs

**Line:** 43666

**Inherits:** EventArgs

---

#### ResolveEventHandler

**Line:** 43691

**Inherits:** MulticastDelegate

---

#### ResolvedPurchaseContentBase

**Line:** 584566

---

#### ResourceFormattedPathsAttribute

**Line:** 892794

**Inherits:** ResourcePathsBaseAttribute

---

#### ResourceItem

**Line:** 729755

**Fields:**

- `AutoCreate`: bool
- `Icon`: Sprite

---

#### ResourceLimit

**Line:** 1066718

---

#### ResourceLocationBase

**Line:** 1437812

**Inherits:** IResourceLocation

**Fields:**

- `m_Name`: string
- `m_Id`: string
- `m_ProviderId`: string
- `m_Data`: object
- `m_DependencyHashCode`: int
- `m_HashCode`: int
- `m_Type`: Type
- `m_Dependencies`: List<IResourceLocation>
- `m_PrimaryKey`: string

---

#### ResourceLocationComparer

**Line:** 1437797

**Inherits:** IEqualityComparer

---

#### ResourceLocationData

**Line:** 1456796

**Fields:**

- `m_InternalId`: string
- `m_Provider`: string
- `m_ResourceType`: SerializedType
- `_Data`: object

---

#### ResourceLocationMap

**Line:** 1456874

**Inherits:** IResourceLocator

---

#### ResourceLocatorInfo

**Line:** 1453650

---

#### ResourceManager

**Line:** 1434365

**Inherits:** IDisposable

**Fields:**

- `m_ResourceProviders`: ListWithEvents<IResourceProvider>
- `m_allocator`: IAllocationStrategy
- `m_UpdateReceiversToRemove`: List<IUpdateReceiver>
- `m_UpdatingReceivers`: bool
- `m_InsideUpdateMethod`: bool
- `m_AssetOperationCache`: Dictionary<IOperationCacheKey, IAsyncOperation>
- `m_TrackedInstanceOperations`: HashSet<ResourceManager.InstanceOperation>
- `m_DeferredCompleteCallbacks`: List<IAsyncOperation>
- `m_InsideExecuteDeferredCallbacksMethod`: bool
- `m_DeferredCallbacksToRegister`: List<ResourceManager.DeferredCallbackRegisterRequest>
- `m_ReleaseOpNonCached`: Action<IAsyncOperation>
- `m_ReleaseOpCached`: Action<IAsyncOperation>
- `m_ReleaseInstanceOp`: Action<IAsyncOperation>
- `m_RegisteredForCallbacks`: bool
- `m_ProviderOperationTypeCache`: Dictionary<Type, Type>

---

#### ResourceManagerException

**Line:** 1434870

**Inherits:** Exception

---

#### ResourceManagerRuntimeData

**Line:** 1457194

**Fields:**

- `m_buildTarget`: string
- `m_SettingsHash`: string
- `m_CatalogLocations`: List<ResourceLocationData>
- `m_LogResourceManagerExceptions`: bool
- `m_ExtraInitializationData`: List<ObjectInitializationData>
- `m_DisableCatalogUpdateOnStart`: bool
- `m_IsLocalCatalogInBundle`: bool
- `m_CertificateHandlerType`: SerializedType
- `m_AddressablesVersion`: string
- `m_maxConcurrentWebRequests`: int
- `m_CatalogRequestsTimeout`: int

---

#### ResourcePackUiView

**Line:** 730379

**Inherits:** MonoBehaviour

**Fields:**

- `PriceButton`: PriceButtonUiView

---

#### ResourcePathAttribute

**Line:** 892776

**Inherits:** ResourcePathsBaseAttribute

---

#### ResourcePathsAttribute

**Line:** 892785

**Inherits:** ResourcePathsBaseAttribute

---

#### ResourcePathsBaseAttribute

**Line:** 892767

**Inherits:** Attribute

---

#### ResourceProviderBase

**Line:** 1437477

**Inherits:** IResourceProvider

**Fields:**

- `m_ProviderId`: string
- `m_BehaviourFlags`: ProviderBehaviourFlags

---

#### ResourcePurchaseAction

**Line:** 1051127

**Inherits:** PlayerAction

---

#### ResourcePurchaseLog

**Line:** 1066436

---

#### ResourcePurchasedMessage

**Line:** 729808

**Inherits:** IMessage

**Fields:**

- `ShopResourceId`: ShopResourceId

---

#### ResourceReader

**Line:** 264740

**Inherits:** IResourceReader

**Fields:**

- `_store`: BinaryReader
- `_nameSectionOffset`: long
- `_dataSectionOffset`: long
- `_objFormatter`: BinaryFormatter
- `_numResources`: int
- `_ums`: UnmanagedMemoryStream
- `_version`: int

---

#### ResourceRefreshedMessage

**Line:** 729820

**Inherits:** IMessage

---

#### ResourceRequest

**Line:** 881097

**Inherits:** AsyncOperation

---

#### ResourceSet

**Line:** 264842

**Inherits:** IDisposable

**Fields:**

- `Reader`: IResourceReader
- `Table`: Hashtable
- `_caseInsensitiveTable`: Hashtable

---

#### Resources

**Line:** 881209

---

#### ResourcesAPI

**Line:** 881163

---

#### Response

**Line:** 1397509

**Inherits:** IDirectResponseSchema

---

#### ResponseGlobalLeaderboardMessage

**Line:** 1067086

**Inherits:** MetaResponse

**Fields:**

- `Leaderboard`: MetaDictionary<EntityId, PlayerLeaderboardEntry>

---

#### ResponsiveBase

**Line:** 1506616

**Inherits:** SRMonoBehaviour

**Fields:**

- `_queueRefresh`: bool

---

#### ResponsiveEnable

**Line:** 1506674

**Inherits:** ResponsiveBase

---

#### ResponsiveResize

**Line:** 1506712

**Inherits:** ResponsiveBase

---

#### RestartParticlesOnEnable

**Line:** 714293

**Inherits:** MonoBehaviour

**Fields:**

- `_particleSystem`: ParticleSystem

---

#### ResumableUpload

**Line:** 1502426

**Fields:**

- `ResponseReceived`: Action<TResponse>

---

#### ResumableUploadOptions

**Line:** 1502493

---

#### RetentionPeriod

**Line:** 1564790

**Fields:**

- `idAndPeriod`: Dictionary<int, int>

---

#### RetryConditionHeaderValue

**Line:** 1491167

**Inherits:** ICloneable

---

#### RetryContext

**Line:** 1415739

---

#### RetrySteppingStonesPopupUiView

**Line:** 734695

**Inherits:** MonoBehaviour

**Fields:**

- `RetryPriceButton`: PriceButtonUiView
- `CloseButton`: UnityButton

---

#### ReturnMessage

**Line:** 224787

**Inherits:** IMethodReturnMessage

**Fields:**

- `_callCtx`: LogicalCallContext
- `_returnValue`: object
- `_uri`: string
- `_exception`: Exception
- `_methodBase`: MethodBase
- `_methodName`: string
- `_typeName`: string
- `_properties`: MethodReturnDictionary
- `_targetIdentity`: Identity
- `_inArgInfo`: ArgInfo

---

#### Rigidbody

**Line:** 1577339

**Inherits:** Component

---

#### Rigidbody2D

**Line:** 1578572

**Inherits:** Component

---

#### Rijndael

**Line:** 218651

**Inherits:** SymmetricAlgorithm

---

#### RijndaelManaged

**Line:** 218668

**Inherits:** Rijndael

---

#### RijndaelManagedTransform

**Line:** 218703

**Inherits:** ICryptoTransform

**Fields:**

- `m_cipherMode`: CipherMode
- `m_paddingValue`: PaddingMode
- `m_transformMode`: RijndaelManagedTransformMode
- `m_blockSizeBits`: int
- `m_blockSizeBytes`: int
- `m_inputBlockSize`: int
- `m_outputBlockSize`: int
- `m_Nr`: int
- `m_Nb`: int
- `m_Nk`: int

---

#### RoleView

**Line:** 719362

**Inherits:** MonoBehaviour

**Fields:**

- `_roleNameText`: TMP_Text

---

#### RomanNumerals

**Line:** 735409

---

#### RoomInfo

**Line:** 1527853

**Inherits:** IEquatable

---

#### RootDesignerSerializerAttribute

**Line:** 785155

**Inherits:** Attribute

**Fields:**

- `_typeId`: string

---

#### RoundIconsInfo

**Line:** 1325281

**Inherits:** IMetadata

**Fields:**

- `m_Round_idpi`: LocalizedTexture
- `m_Round_mdpi`: LocalizedTexture
- `m_Round_hdpi`: LocalizedTexture
- `m_Round_xhdpi`: LocalizedTexture
- `m_Round_xxhdpi`: LocalizedTexture
- `m_Round_xxxhdpi`: LocalizedTexture

---

#### RowData

**Line:** 1397821

**Inherits:** IDirectResponseSchema

---

#### RowNotInTableException

**Line:** 1080875

**Inherits:** DataException

---

#### RuleCache

**Line:** 1299657

---

#### RuntimeAnimatorController

**Line:** 1575718

**Inherits:** Object

---

#### RuntimeCompatibilityAttribute

**Line:** 234342

**Inherits:** Attribute

---

#### RuntimeInitializeOnLoadMethodAttribute

**Line:** 883595

**Inherits:** PreserveAttribute

**Fields:**

- `m_LoadType`: RuntimeInitializeLoadType

---

#### RuntimeTypeInfoProvider

**Line:** 530745

---

#### RuntimeVariablesExpression

**Line:** 1289178

**Inherits:** Expression

---

#### RuntimeWrappedException

**Line:** 234379

**Inherits:** Exception

**Fields:**

- `_wrappedException`: object

---

#### SByteConverter

**Line:** 782971

**Inherits:** BaseNumberConverter

---

#### SByteTrackedProperty

**Line:** 1328851

**Inherits:** TrackedProperty

---

#### SByteVariable

**Line:** 1324429

**Inherits:** Variable

---

#### SHA1

**Line:** 219022

**Inherits:** HashAlgorithm

---

#### SHA1CryptoServiceProvider

**Line:** 219946

**Inherits:** SHA1

**Fields:**

- `sha`: SHA1Internal

---

#### SHA1Managed

**Line:** 219035

**Inherits:** SHA1

**Fields:**

- `_count`: long

---

#### SHA256

**Line:** 219075

**Inherits:** HashAlgorithm

---

#### SHA256Managed

**Line:** 219088

**Inherits:** SHA256

**Fields:**

- `_count`: long

---

#### SHA384

**Line:** 219153

**Inherits:** HashAlgorithm

---

#### SHA384Managed

**Line:** 219166

**Inherits:** SHA384

**Fields:**

- `_count`: ulong

---

#### SHA512

**Line:** 219231

**Inherits:** HashAlgorithm

---

#### SHA512Managed

**Line:** 219244

**Inherits:** SHA512

**Fields:**

- `_count`: ulong

---

#### SRAutoSingleton

**Line:** 1508030

---

#### SRDebugService

**Line:** 1446084

**Inherits:** IDebugService

**Fields:**

- `PanelVisibilityChanged`: VisibilityChangedDelegate
- `PinnedUiCanvasCreated`: PinnedUiCanvasCreated
- `_entryCodeEnabled`: bool
- `_hasAuthorised`: bool
- `_queuedTab`: Nullable<DefaultTabs>
- `_worldSpaceTransform`: RectTransform

---

#### SRDebugStrings

**Line:** 1447002

---

#### SRDebuggerInit

**Line:** 1442898

**Inherits:** SRMonoBehaviourEx

---

#### SRDependencyServiceBase

**Line:** 1507475

**Fields:**

- `_isLoaded`: bool

---

#### SRList

**Line:** 1505320

**Fields:**

- `_count`: int
- `_equalityComparer`: EqualityComparer<T>
- `_readOnlyWrapper`: ReadOnlyCollection<T>

---

#### SRMonoBehaviour

**Line:** 1505762

**Inherits:** MonoBehaviour

**Fields:**

- `_collider`: Collider
- `_transform`: Transform
- `_rigidBody`: Rigidbody
- `_gameObject`: GameObject
- `_rigidbody2D`: Rigidbody2D
- `_collider2D`: Collider2D

---

#### SRMonoBehaviourEx

**Line:** 1505912

**Inherits:** SRMonoBehaviour

---

#### SRNumberButton

**Line:** 1506764

**Inherits:** Button

**Fields:**

- `_delayTime`: float
- `_downTime`: float
- `_isDown`: bool
- `Amount`: double
- `TargetField`: SRNumberSpinner

---

#### SRNumberSpinner

**Line:** 1506795

**Inherits:** InputField

**Fields:**

- `_currentValue`: double
- `_dragStartAmount`: double
- `_dragStep`: double
- `DragSensitivity`: float
- `MaxValue`: double
- `MinValue`: double

---

#### SROptions

**Line:** 685648

**Inherits:** INotifyPropertyChanged

**Fields:**

- `PropertyChanged`: SROptionsPropertyChanged
- `InterfacePropertyChangedEventHandler`: PropertyChangedEventHandler

---

#### SROptionsPropertyChanged

**Line:** 704896

**Inherits:** MulticastDelegate

---

#### SRPProfilerService

**Line:** 1446555

**Inherits:** SRServiceBase

**Fields:**

- `_lateUpdateListener`: ProfilerLateUpdateListener
- `_updateDuration`: double
- `_renderStartTime`: double
- `_renderDuration`: double

---

#### SRRetinaScaler

**Line:** 1506835

**Inherits:** SRMonoBehaviour

**Fields:**

- `_retinaScale`: float
- `_thresholdDpi`: int
- `_disablePixelPerfect`: bool

---

#### SRSceneServiceBase

**Line:** 1507615

**Fields:**

- `_rootObject`: TImpl

---

#### SRServiceBase

**Line:** 1507703

---

#### SRServiceManager

**Line:** 1507824

**Inherits:** SRAutoSingleton

**Fields:**

- `_serviceStubs`: List<SRServiceManager.ServiceStub>

---

#### SRSingleton

**Line:** 1508084

---

#### SRSpinner

**Line:** 1506876

**Inherits:** Selectable

**Fields:**

- `_dragDelta`: float
- `DragThreshold`: float

---

#### SRTab

**Line:** 1443955

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `HeaderExtraContent`: RectTransform
- `Icon`: Sprite
- `IconExtraContent`: RectTransform
- `IconStyleKey`: string
- `SortIndex`: int
- `TabButton`: SRTabButton
- `_title`: string
- `_longTitle`: string
- `_key`: string

---

#### SRTabButton

**Line:** 1444777

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `ActiveToggle`: Behaviour
- `Button`: Button
- `ExtraContentContainer`: RectTransform
- `IconStyleComponent`: StyleComponent
- `TitleText`: Text

---

#### SRTabController

**Line:** 1444034

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `_activeTab`: SRTab
- `TabButtonContainer`: RectTransform
- `TabButtonPrefab`: SRTabButton
- `TabContentsContainer`: RectTransform
- `TabHeaderContentContainer`: RectTransform
- `TabHeaderText`: Text
- `ActiveTabChanged`: Action<SRTabController, SRTab>

---

#### SRText

**Line:** 1506922

**Inherits:** Text

**Fields:**

- `LayoutDirty`: Action<SRText>

---

#### STAThreadAttribute

**Line:** 57776

**Inherits:** Attribute

---

#### STP

**Line:** 821737

**Fields:**

- `m_hash`: Hash128

---

#### SafeAERC

**Line:** 1547860

**Inherits:** IAERC

---

#### SafeAreaComponent

**Line:** 693274

**Inherits:** IComponent

**Fields:**

- `TopPadding`: float
- `BottomPadding`: float

---

#### SafeAreaParentComponent

**Line:** 693289

**Inherits:** IComponent

**Fields:**

- `Value`: Transform

---

#### SafeAreaSystem

**Line:** 693709

**Inherits:** IInitializeSystem

---

#### SafeAreaView

**Line:** 693667

**Inherits:** UiUnityView

**Fields:**

- `SafeArea`: RectTransform
- `SafeAreaParent`: RectTransform
- `OverlayParent`: Transform
- `_gameContextListener`: GameEntity

---

#### SafeBuffer

**Line:** 228914

**Inherits:** SafeHandleZeroOrMinusOneIsInvalid

**Fields:**

- `_numBytes`: UIntPtr

---

#### SafeFileHandle

**Line:** 2963

**Inherits:** SafeHandleZeroOrMinusOneIsInvalid

---

#### SafeHandle

**Line:** 229366

**Inherits:** CriticalFinalizerObject

**Fields:**

- `handle`: IntPtr
- `_state`: int
- `_ownsHandle`: bool
- `_fullyInitialized`: bool

---

#### SafeHandleMinusOneIsInvalid

**Line:** 3004

**Inherits:** SafeHandle

---

#### SafeHandleZeroOrMinusOneIsInvalid

**Line:** 2988

**Inherits:** SafeHandle

---

#### SafePipeHandle

**Line:** 1230077

**Inherits:** SafeHandleZeroOrMinusOneIsInvalid

---

#### SafeProcessHandle

**Line:** 773688

**Inherits:** SafeHandleZeroOrMinusOneIsInvalid

---

#### SafeSerializationEventArgs

**Line:** 225981

**Inherits:** EventArgs

**Fields:**

- `m_streamingContext`: StreamingContext
- `m_serializedStates`: List<object>

---

#### SafeWaitHandle

**Line:** 2975

**Inherits:** SafeHandleZeroOrMinusOneIsInvalid

---

#### Salsa20Engine

**Line:** 1519548

**Inherits:** IStreamCipher

**Fields:**

- `rounds`: int
- `cW0`: uint
- `cW1`: uint
- `cW2`: uint

---

#### SampleActivity

**Line:** 1418213

---

#### Sampler

**Line:** 886552

---

#### SanityCheckFeature

**Line:** 695495

**Inherits:** Feature

---

#### SatelliteContractVersionAttribute

**Line:** 264320

**Inherits:** Attribute

---

#### SaveGameIdNotSuppliedException

**Line:** 685211

**Inherits:** BadRequestException

---

#### ScaffoldColumnAttribute

**Line:** 1509985

**Inherits:** Attribute

---

#### ScaleFunc

**Line:** 822545

**Inherits:** MulticastDelegate

---

#### SceneManager

**Line:** 888802

---

#### SceneManagerAPI

**Line:** 888762

---

#### SceneProvider

**Line:** 1437647

**Inherits:** ISceneProvider2

---

#### SceneRenderPipeline

**Line:** 825637

**Inherits:** MonoBehaviour

---

#### SceneRoot

**Line:** 684317

**Inherits:** MonoBehaviour

**Fields:**

- `_contexts`: Contexts
- `_appController`: AppController
- `_updateSystems`: UpdateSystems
- `_initSystems`: InitSystems

---

#### ScheduledMaintenanceModeForClient

**Line:** 555574

---

#### SchemaMigrationError

**Line:** 604176

**Inherits:** Exception

---

#### SchemaMigrationRegistry

**Line:** 604147

**Fields:**

- `_migrators`: Dictionary<Type, SchemaMigrator>

---

#### SchemaMigrator

**Line:** 604218

---

#### ScorecardChartSpec

**Line:** 1397857

**Inherits:** IDirectResponseSchema

---

#### Screen

**Line:** 872785

---

#### ScreenCaptureFeature

**Line:** 695519

**Inherits:** Feature

---

#### ScreenCaptureSystem

**Line:** 695537

**Inherits:** CheatSystem

---

#### ScreenSpaceAmbientOcclusion

**Line:** 912735

**Inherits:** ScriptableRendererFeature

**Fields:**

- `m_Settings`: ScreenSpaceAmbientOcclusionSettings
- `m_Material`: Material
- `m_SSAOPass`: ScreenSpaceAmbientOcclusionPass
- `m_Shader`: Shader

---

#### ScreenSpaceLensFlare

**Line:** 909593

**Inherits:** VolumeComponent

**Fields:**

- `intensity`: MinFloatParameter
- `tintColor`: ColorParameter
- `bloomMip`: ClampedIntParameter
- `firstFlareIntensity`: MinFloatParameter
- `secondaryFlareIntensity`: MinFloatParameter
- `warpedFlareIntensity`: MinFloatParameter
- `warpedFlareScale`: Vector2Parameter
- `samples`: ClampedIntParameter
- `sampleDimmer`: ClampedFloatParameter
- `vignetteEffect`: ClampedFloatParameter
- `startingPosition`: ClampedFloatParameter
- `scale`: ClampedFloatParameter
- `streaksIntensity`: MinFloatParameter
- `streaksLength`: ClampedFloatParameter
- `streaksOrientation`: FloatParameter
- `streaksThreshold`: ClampedFloatParameter
- `resolution`: ScreenSpaceLensFlareResolutionParameter
- `chromaticAbberationIntensity`: ClampedFloatParameter

---

#### ScreenSpaceLensFlareResolutionParameter

**Line:** 909641

**Inherits:** VolumeParameter

---

#### ScriptableAudioConfig

**Line:** 698820

**Inherits:** ScriptableObject

**Fields:**

- `_sfxConfig`: SfxConfig
- `_biomeSfxConfig`: BiomeSfxConfig

---

#### ScriptableMainCanvasConfig

**Line:** 698846

**Inherits:** ScriptableObject

**Fields:**

- `_referenceResolution`: Vector2

---

#### ScriptableObject

**Line:** 883620

**Inherits:** Object

---

#### ScriptableRenderPass

**Line:** 905422

**Inherits:** IRenderGraphRecorder

**Fields:**

- `m_DepthStoreAction`: RenderBufferStoreAction
- `m_OverriddenDepthStoreAction`: bool
- `m_ProfingSampler`: ProfilingSampler
- `m_PassName`: string
- `m_RenderGraphSettings`: RenderGraphSettings
- `m_DepthAttachment`: RTHandle
- `m_Input`: ScriptableRenderPassInput
- `m_ClearFlag`: ClearFlag
- `m_ClearColor`: Color

---

#### ScriptableRenderer

**Line:** 906084

**Inherits:** IDisposable

**Fields:**

- `m_LastBeginSubpassPassIndex`: int
- `m_MergeableRenderPassesMap`: Dictionary<Hash128, int[]>
- `m_RenderPassesAttachmentCount`: Dictionary<Hash128, int>
- `m_firstPassIndexOfLastMergeableGroup`: int
- `m_ActiveDepthAttachmentDescriptor`: AttachmentDescriptor
- `m_StoreActionsOptimizationSetting`: StoreActionsOptimization
- `m_ActiveRenderPassQueue`: List<ScriptableRenderPass>
- `m_RendererFeatures`: List<ScriptableRendererFeature>
- `m_CameraColorTarget`: RTHandle
- `m_CameraDepthTarget`: RTHandle
- `m_CameraResolveTarget`: RTHandle
- `m_FirstTimeCameraColorTargetIsBound`: bool
- `m_FirstTimeCameraDepthTargetIsBound`: bool
- `m_IsPipelineExecuting`: bool
- `m_frameData`: ContextContainer

---

#### ScriptableRendererData

**Line:** 906625

**Inherits:** ScriptableObject

**Fields:**

- `m_UseNativeRenderPass`: bool
- `m_StripShadowsOffVariants`: bool
- `m_StripAdditionalLightOffVariants`: bool

---

#### ScriptableRendererFeature

**Line:** 913797

**Inherits:** ScriptableObject

**Fields:**

- `m_Active`: bool

---

#### ScriptableVisualConfig

**Line:** 698866

**Inherits:** ScriptableObject

**Fields:**

- `_slotsConfig`: SlotsConfig
- `_worldVisualConfig`: WorldVisualConfig
- `_skillVisualConfig`: SkillVisualConfig
- `_techTreeVisualConfig`: TechTreeVisualConfig
- `_petCollectionVisualConfig`: PetCollectionVisualConfig
- `_dungeonVisualConfig`: DungeonVisualConfig
- `_rewardVisualConfig`: RewardVisualConfig
- `_shopVisualConfig`: ShopVisualConfig
- `_mountCollectionVisualConfig`: MountCollectionVisualConfig
- `_playerIconsConfig`: PlayerIconsConfig
- `_arenaVisualConfig`: ArenaVisualConfig
- `_skinsVisualConfig`: SkinsVisualConfig

---

#### ScrollRect

**Line:** 1356226

**Inherits:** UIBehaviour

**Fields:**

- `m_Content`: RectTransform
- `m_Horizontal`: bool
- `m_Vertical`: bool
- `m_Elasticity`: float
- `m_Inertia`: bool
- `m_DecelerationRate`: float
- `m_ScrollSensitivity`: float
- `m_Viewport`: RectTransform
- `m_HorizontalScrollbar`: Scrollbar
- `m_VerticalScrollbar`: Scrollbar
- `m_HorizontalScrollbarSpacing`: float
- `m_VerticalScrollbarSpacing`: float
- `m_PointerStartLocalCursor`: Vector2
- `m_ContentStartPosition`: Vector2
- `m_ViewRect`: RectTransform
- `m_ContentBounds`: Bounds
- `m_ViewBounds`: Bounds
- `m_Velocity`: Vector2
- `m_Dragging`: bool
- `m_Scrolling`: bool
- ... (12 more fields)

---

#### ScrollRectPatch

**Line:** 1443910

**Inherits:** MonoBehaviour

**Fields:**

- `Content`: RectTransform
- `ReplaceMask`: Mask
- `Viewport`: RectTransform

---

#### ScrollSettingsBehaviour

**Line:** 1443928

**Inherits:** MonoBehaviour

---

#### ScrollShadowEffect

**Line:** 737441

**Inherits:** MonoBehaviour

**Fields:**

- `scrollRect`: ScrollRect
- `shadowImage`: Image
- `isTopShadow`: bool
- `MaxAlpha`: float
- `MinAlpha`: float
- `MinContentHeightShowShadow`: int
- `contentRectTransform`: RectTransform

---

#### ScrollToBottomBehaviour

**Line:** 1506730

**Inherits:** MonoBehaviour

**Fields:**

- `_scrollRect`: ScrollRect
- `_canvasGroup`: CanvasGroup

---

#### ScrollView

**Line:** 627387

**Inherits:** VisualElement

**Fields:**

- `m_FirstLayoutPass`: int
- `m_HorizontalScrollerVisibility`: ScrollerVisibility
- `m_VerticalScrollerVisibility`: ScrollerVisibility
- `m_ElasticAnimationIntervalMs`: long
- `m_AttachedRootVisualContainer`: VisualElement
- `m_SingleLineHeight`: float
- `m_SingleLineHeightDirtyFlag`: bool
- `m_ScrollOffset`: Vector2
- `m_HorizontalPageSize`: float
- `m_VerticalPageSize`: float
- `m_MouseWheelScrollSize`: float
- `m_ScrollDecelerationRate`: float
- `k_ScaledPixelsPerPointMultiplier`: float
- `k_TouchScrollInertiaBaseTimeInterval`: float
- `m_Elasticity`: float
- `m_ContentContainer`: VisualElement
- `m_ContentAndVerticalScrollContainer`: VisualElement
- `previousVerticalTouchScrollTimeStamp`: float
- `previousHorizontalTouchScrollTimeStamp`: float
- `elapsedTimeSinceLastVerticalTouchScroll`: float
- ... (16 more fields)

---

#### Scrollbar

**Line:** 1356014

**Inherits:** Selectable

**Fields:**

- `m_HandleRect`: RectTransform
- `m_Value`: float
- `m_Size`: float
- `m_NumberOfSteps`: int
- `m_ContainerRect`: RectTransform
- `m_Offset`: Vector2
- `m_Tracker`: DrivenRectTransformTracker
- `m_PointerDownRepeat`: Coroutine
- `isPointerDownAndNotDragging`: bool
- `m_DelayedUpdateVisuals`: bool

---

#### Scroller

**Line:** 627828

**Inherits:** VisualElement

**Fields:**

- `valueChanged`: Action<float>

---

#### ScrollingFillAnimator

**Line:** 1585984

**Inherits:** MonoBehaviour

**Fields:**

- `ScrollSpeed`: float
- `_image`: RawImage
- `_rectTransform`: RectTransform

---

#### SearchDeveloperMetadataRequest

**Line:** 1397977

**Inherits:** IDirectResponseSchema

---

#### SearchDeveloperMetadataResponse

**Line:** 1398013

**Inherits:** IDirectResponseSchema

---

#### SecondLayerStyleSettings

**Line:** 1564328

**Fields:**

- `showCloseButton`: bool

---

#### SecondaryEquipmentItem

**Line:** 713692

**Inherits:** EquipmentItem

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

#### SecureString

**Line:** 216882

**Inherits:** IDisposable

**Fields:**

- `length`: int
- `disposed`: bool

---

#### SecurityElement

**Line:** 216956

**Fields:**

- `text`: string
- `tag`: string
- `attributes`: ArrayList
- `children`: ArrayList

---

#### SecurityException

**Line:** 217041

**Inherits:** SystemException

**Fields:**

- `permissionState`: string

---

#### SegmentedIOBuffer

**Line:** 557858

**Inherits:** RWIOBufferBase

**Fields:**

- `_segments`: List<SegmentedIOBuffer.Segment>
- `_totalBytes`: int

---

#### Selectable

**Line:** 1356620

**Inherits:** UIBehaviour

**Fields:**

- `m_EnableCalled`: bool
- `m_Navigation`: Navigation
- `m_Colors`: ColorBlock
- `m_SpriteState`: SpriteState
- `m_AnimationTriggers`: AnimationTriggers
- `m_Interactable`: bool
- `m_TargetGraphic`: Graphic
- `m_GroupsAllowInteraction`: bool
- `m_CurrentIndex`: int

---

#### SelectedComponent

**Line:** 723508

**Inherits:** IComponent

---

#### SelectionBaseAttribute

**Line:** 883684

**Inherits:** Attribute

---

#### Selector

**Line:** 1323085

**Inherits:** FormatItem

**Fields:**

- `m_Operator`: string

---

#### SellBetterItemUiView

**Line:** 714140

**Inherits:** UiUnityView

**Fields:**

- `Cancel`: UnityButton
- `Confirm`: UnityButton
- `_itemToSell`: PlayerItemModel
- `_oldItem`: PlayerItemModel
- `_currentItem`: PlayerItemModel

---

#### SellCoinsComponent

**Line:** 714646

**Inherits:** IComponent

**Fields:**

- `Value`: long

---

#### SellItemAction

**Line:** 1067557

**Inherits:** PlayerAction

---

#### SellParticleView

**Line:** 716017

**Inherits:** MonoBehaviour

**Fields:**

- `Label`: TextMeshProUGUI
- `Coin`: Image
- `_sequence`: Sequence

---

#### SellParticlesView

**Line:** 715962

**Inherits:** UiUnityView

**Fields:**

- `ParticlePrefab`: SellParticleView
- `Parent`: Transform
- `_particlePool`: Pool<SellParticleView>
- `_gameListener`: GameEntity

---

#### SemaphoreFullException

**Line:** 179069

**Inherits:** SystemException

---

#### SemaphoreSlim

**Line:** 179939

**Inherits:** IDisposable

**Fields:**

- `m_currentCount`: int
- `m_waitCount`: int
- `m_lockObj`: object
- `m_waitHandle`: ManualResetEvent

---

#### SendGameBuildAnalytic

**Line:** 1587195

**Inherits:** AnalyticsEventBase

**Fields:**

- `navmesh_count`: int

---

#### SendMessageRequest

**Line:** 1526926

**Inherits:** IEquatable

---

#### SendMessageResponse

**Line:** 1527065

**Inherits:** IEquatable

---

#### SendOrPostCallback

**Line:** 179081

**Inherits:** MulticastDelegate

---

#### SendReactionRequest

**Line:** 1526686

**Inherits:** IEquatable

---

#### SensitiveAttribute

**Line:** 499139

**Inherits:** Attribute

---

#### Sequence

**Line:** 1425792

**Inherits:** Tween

---

#### SequenceMessage

**Line:** 1569174

**Inherits:** HubMessage

---

#### SequentialIDGenerator

**Line:** 1317763

**Inherits:** IKeyGenerator

**Fields:**

- `m_NextAvailableId`: long

---

#### SequentialSearchPrimeGeneratorBase

**Line:** 1450149

**Inherits:** PrimeGeneratorBase

---

#### SerializableAttribute

**Line:** 43814

**Inherits:** Attribute

---

#### SerializableDictionary

**Line:** 695660

---

#### SerializableDictionaryBoxed

**Line:** 695810

---

#### SerializableEnum

**Line:** 811020

**Fields:**

- `m_EnumValueAsString`: string
- `m_EnumTypeAsString`: string

---

#### SerializableKVP

**Line:** 695870

**Fields:**

- `_key`: K
- `_value`: V

---

#### SerializableKVPBoxed

**Line:** 695974

**Fields:**

- `_key`: K
- `_values`: List<V>

---

#### SerializationBinder

**Line:** 225255

---

#### SerializationCallback

**Line:** 1038940

**Inherits:** MulticastDelegate

---

#### SerializationErrorCallback

**Line:** 1038959

**Inherits:** MulticastDelegate

---

#### SerializationEventHandler

**Line:** 225171

**Inherits:** MulticastDelegate

---

#### SerializationException

**Line:** 225065

**Inherits:** SystemException

---

#### SerializationInfo

**Line:** 226189

**Fields:**

- `m_nameToIndex`: Dictionary<string, int>
- `m_fullTypeName`: string
- `m_assemName`: string
- `objectType`: Type
- `isFullTypeNameSetExplicit`: bool
- `isAssemblyNameSetExplicit`: bool
- `requireSameTokenInPartialTrust`: bool

---

#### SerializationInfoEnumerator

**Line:** 225114

**Inherits:** IEnumerator

**Fields:**

- `_currItem`: int
- `_current`: bool

---

#### SerializationObjectManager

**Line:** 225351

**Fields:**

- `_onSerializedHandler`: SerializationEventHandler

---

#### SerializeField

**Line:** 884738

**Inherits:** Attribute

---

#### SerializeReference

**Line:** 884749

**Inherits:** Attribute

---

#### SerializedDictionary

**Line:** 811198

**Fields:**

- `m_Keys`: List<SK>
- `m_Values`: List<SV>

---

#### SerializedObjectComparer

**Line:** 530819

**Fields:**

- `FirstName`: string
- `SecondName`: string
- `Type`: Type

---

#### SerializedTypeRestrictionAttribute

**Line:** 1436065

**Inherits:** Attribute

**Fields:**

- `type`: Type

---

#### ServerCheatContainer

**Line:** 686334

**Inherits:** AbstractCheatContainer

---

#### ServerConnection

**Line:** 550992

**Fields:**

- `_transport`: IMessageTransport
- `_transportLock`: object
- `_incomingLock`: object
- `_incomingMessages`: List<MetaMessage>
- `_handshakePhase`: ServerHandshakePhase
- `_enqueueCloseLock`: object
- `_closeEnqueued`: bool
- `_clientAppPauseStatus`: ClientAppPauseStatus
- `_currentSessionStartQueryId`: int
- `_currentSessionSendQueueLock`: object
- `_terminatingErrorTask`: TaskCompletionSource<MessageTransport.Error>
- `_connectionStartTime`: DateTime
- `_watchdogDeadlineAt`: DateTime
- `_watchdogDeadlineLastDuration`: TimeSpan
- `_watchdogLock`: object
- `_enableWatchdog`: bool
- `_reportWatchdogViolation`: Action
- `_previousWatchdogCheckAt`: DateTime
- `_disposeCts`: CancellationTokenSource
- `_nextLatencySampleId`: int
- ... (5 more fields)

---

#### ServerDrivenIAPClientDelegate

**Line:** 1312433

**Inherits:** IAPClientDelegate

---

#### ServerDrivenIAPSharedDelegate

**Line:** 583978

**Inherits:** IAPSharedDelegate

---

#### ServerDrivenInAppPurchaseClientHandlingResponse

**Line:** 586029

---

#### ServerDrivenInAppPurchaseClientHandlingResult

**Line:** 586387

---

#### ServerDrivenInAppPurchaseEventState

**Line:** 585979

---

#### ServerDrivenInAppPurchaseInitiationParams

**Line:** 586365

---

#### ServerEndpoint

**Line:** 557573

---

#### ServerGameConfig

**Line:** 1079517

**Inherits:** ServerGameConfigBase

---

#### ServerGameConfigBase

**Line:** 600264

**Inherits:** GameConfigBase

**Fields:**

- `_playerExperimentsIntegration`: IGameConfigLibrary<PlayerExperimentId, PlayerExperimentInfo>

---

#### ServerGateway

**Line:** 557507

---

#### ServerGatewayScheduler

**Line:** 551222

**Fields:**

- `_lastGatewayWasSuccess`: bool
- `_isInitialConnect`: bool
- `_currentIndex`: int

---

#### ServerGatewaySpec

**Line:** 577040

**Fields:**

- `Id`: string
- `ServerHost`: string
- `ServerPort`: int

---

#### ServerOnlyAttribute

**Line:** 600958

**Inherits:** MetaMemberFlagAttribute

---

#### ServerRankingsTextView

**Line:** 726217

**Inherits:** MonoBehaviour

**Fields:**

- `ServerText`: TMP_Text

---

#### ServerTimeUiView

**Line:** 729063

**Inherits:** UiUnityView

**Fields:**

- `TimeText`: TMP_Text

---

#### ServiceAccountCredential

**Line:** 1373385

**Inherits:** ServiceCredential

**Fields:**

- `_jwts`: LinkedList<ServiceAccountCredential.JwtCacheEntry>

---

#### ServiceAttribute

**Line:** 1507317

**Inherits:** PreserveAttribute

---

#### ServiceCollection

**Line:** 1542707

**Inherits:** IServiceCollection

**Fields:**

- `_isReadOnly`: bool

---

#### ServiceConstructorAttribute

**Line:** 1507367

**Inherits:** PreserveAttribute

---

#### ServiceContext

**Line:** 704422

**Inherits:** Context

---

#### ServiceCredential

**Line:** 1373730

**Inherits:** ICredential

---

#### ServiceDescriptor

**Line:** 1543133

**Fields:**

- `_implementationType`: Type
- `_implementationInstance`: object
- `_implementationFactory`: object

---

#### ServiceEntity

**Line:** 704475

**Inherits:** Entity

---

#### ServiceKeyAttribute

**Line:** 1543466

**Inherits:** Attribute

---

#### ServiceMatcher

**Line:** 704520

---

#### ServiceNameCollection

**Line:** 778468

**Inherits:** ReadOnlyCollectionBase

---

#### ServicePoint

**Line:** 796703

**Fields:**

- `lastDnsResolve`: DateTime
- `protocolVersion`: Version
- `host`: IPHostEntry
- `usesProxy`: bool
- `sendContinue`: bool
- `useConnect`: bool
- `hostE`: object
- `useNagle`: bool
- `endPointCallback`: BindIPEndPoint
- `tcp_keepalive`: bool
- `tcp_keepalive_time`: int
- `tcp_keepalive_interval`: int
- `disposed`: bool
- `connectionLeaseTimeout`: int
- `receiveBufferSize`: int
- `connectionLimit`: int
- `maxIdleTime`: int
- `m_ServerCertificateOrBytes`: object
- `m_ClientCertificateOrBytes`: object

---

#### ServicePointManager

**Line:** 796862

---

#### ServicePointManagerElement

**Line:** 803236

**Inherits:** ConfigurationElement

---

#### ServiceProvider

**Line:** 1499303

**Inherits:** IServiceProvider

**Fields:**

- `_disposed`: bool

---

#### ServiceProviderOptions

**Line:** 1499416

---

#### ServiceSelectorAttribute

**Line:** 1507342

**Inherits:** PreserveAttribute

---

#### ServicesCreationException

**Line:** 1588986

**Inherits:** Exception

---

#### ServicesInitializationException

**Line:** 1588995

**Inherits:** Exception

---

#### SessionAcknowledgementMessage

**Line:** 555856

**Inherits:** SessionControlMessage

---

#### SessionControlMessage

**Line:** 555845

**Inherits:** MetaMessage

---

#### SessionForceTerminateMessage

**Line:** 555818

**Inherits:** MetaMessage

---

#### SessionForceTerminateReason

**Line:** 555808

---

#### SessionMetaRequestMessage

**Line:** 555957

**Inherits:** MetaRequestMessage

---

#### SessionMetaResponseMessage

**Line:** 555967

**Inherits:** MetaResponseMessage

---

#### SessionNonceService

**Line:** 551270

**Fields:**

- `_sessionConnectionIndex`: uint
- `_sessionNonce`: uint

---

#### SessionParticipantState

**Line:** 545410

---

#### SessionPing

**Line:** 555513

**Inherits:** MetaMessage

**Fields:**

- `Id`: int

---

#### SessionPong

**Line:** 555529

**Inherits:** MetaMessage

**Fields:**

- `Id`: int

---

#### SessionProtocol

**Line:** 556896

**Fields:**

- `GenerateIncidentReport`: bool

---

#### SessionResumptionInfo

**Line:** 545551

---

#### SessionUtil

**Line:** 545828

---

#### SetBadWordListRequest

**Line:** 1528114

**Inherits:** IEquatable

---

#### SetBasicFilterRequest

**Line:** 1398049

**Inherits:** IDirectResponseSchema

---

#### SetBonusConfig

**Line:** 1074604

---

#### SetConfig

**Line:** 1074562

**Inherits:** IGameConfigData

---

#### SetDataValidationRequest

**Line:** 1398085

**Inherits:** IDirectResponseSchema

---

#### SetId

**Line:** 1074552

**Inherits:** StringId

---

#### SetIndexBinder

**Line:** 1300891

**Inherits:** DynamicMetaObjectBinder

---

#### SetInstallVersionAction

**Line:** 1069983

**Inherits:** PlayerAction

---

#### SetLayerFromSettings

**Line:** 1443943

**Inherits:** SRMonoBehaviour

---

#### SetPlatformSpecificData

**Line:** 534229

**Inherits:** PlayerSynchronizedServerActionCore

---

#### SetPlayerAgeAction

**Line:** 1070014

**Inherits:** PlayerAction

---

#### SetPlayerAgeSystem

**Line:** 739061

**Inherits:** IInitSystem

---

#### SetPlayerCountryAction

**Line:** 1070045

**Inherits:** PlayerAction

---

#### SetPlayerCountrySystem

**Line:** 739073

**Inherits:** IInitSystem

---

#### SetPropertyBagBase

**Line:** 1471023

---

#### SetWhitelistRequest

**Line:** 1528266

**Inherits:** IEquatable

---

#### Settings

**Line:** 1442656

**Inherits:** ScriptableObject

**Fields:**

- `PropertyChanged`: PropertyChangedEventHandler
- `_isEnabled`: bool
- `_defaultTab`: DefaultTabs
- `_errorNotification`: bool
- `_enableKeyboardShortcuts`: bool
- `_keyboardModifierControl`: bool
- `_keyboardModifierAlt`: bool
- `_keyboardModifierShift`: bool
- `_keyboardEscapeClose`: bool
- `_enableBackgroundTransparency`: bool
- `_collapseDuplicateLogEntries`: bool
- `_richTextInConsole`: bool
- `_requireEntryCode`: bool
- `_requireEntryCodeEveryTime`: bool
- `_useDebugCamera`: bool
- `_debugLayer`: int
- `_debugCameraDepth`: float
- `_apiKey`: string
- `_enableBugReporter`: bool
- `_profilerAlignment`: PinAlignment
- ... (8 more fields)

---

#### SettingsBindableAttribute

**Line:** 782996

**Inherits:** Attribute

---

#### SettingsColorView

**Line:** 729084

**Inherits:** MonoBehaviour

**Fields:**

- `Parent`: Transform

---

#### SettingsMenuTabUiView

**Line:** 726232

**Inherits:** UiUnityView

**Fields:**

- `PlayerProfileButton`: UnityButton
- `SettingsButton`: UnityButton
- `PlayerProfileTab`: GameObject
- `SettingsTab`: GameObject
- `PlayerProfileHighlight`: GameObject
- `SettingsHighlight`: GameObject

---

#### SettingsSection

**Line:** 803206

**Inherits:** ConfigurationSection

---

#### SfxConfig

**Line:** 705667

**Inherits:** ScriptableObject

**Fields:**

- `BattleSfxMasterVolume`: float
- `SkillSfxMasterVolume`: float
- `CoinCollect`: AudioClip
- `AutoForgeEnable`: AudioClip
- `SellGear`: AudioClip
- `EquipGear`: AudioClip
- `ButtonDown`: AudioClip
- `ButtonUp`: AudioClip
- `UpgradeMeta`: AudioClip
- `CardSummon`: AudioClip
- `HatchEgg`: AudioClip
- `SummonSpells`: AudioClip
- `WindingClock`: AudioClip
- `ForgeUpgrade`: AudioClip
- `TechComplete`: AudioClip
- `CollectCurrencies`: AudioClip
- `DungeonEnter`: AudioClip
- `ArrowsSkill`: AudioClip
- `MeatActivate`: AudioClip
- `MoraleActivate`: AudioClip
- ... (6 more fields)

---

#### Sha256Digest

**Line:** 1519704

**Inherits:** GeneralDigest

**Fields:**

- `H1`: uint
- `H2`: uint
- `H3`: uint
- `H4`: uint
- `H5`: uint
- `H6`: uint
- `H7`: uint
- `H8`: uint
- `xOff`: int

---

#### Shader

**Line:** 874081

**Inherits:** Object

---

#### ShaderDebugPrintManager

**Line:** 815466

**Fields:**

- `m_OutputBuffers`: List<GraphicsBuffer>
- `m_ReadbackRequests`: List<AsyncGPUReadbackRequest>
- `m_BufferReadCompleteAction`: Action<AsyncGPUReadbackRequest>
- `m_FrameCounter`: int
- `m_FrameCleared`: bool
- `m_OutputLine`: string
- `m_OutputAction`: Action<string>

---

#### ShaderResources

**Line:** 907011

**Fields:**

- `blitPS`: Shader
- `copyDepthPS`: Shader
- `screenSpaceShadowPS`: Shader
- `samplingPS`: Shader
- `stencilDeferredPS`: Shader
- `fallbackErrorPS`: Shader
- `fallbackLoadingPS`: Shader
- `materialErrorPS`: Shader
- `cameraMotionVector`: Shader
- `screenSpaceLensFlare`: Shader
- `dataDrivenLensFlare`: Shader

---

#### ShaderStrippingSetting

**Line:** 821391

**Inherits:** IRenderPipelineGraphicsSettings

**Fields:**

- `m_ExportShaderVariants`: bool
- `m_ShaderVariantLogLevel`: ShaderVariantLogLevel
- `m_StripRuntimeDebugShaders`: bool

---

#### Shadow

**Line:** 1357949

**Inherits:** BaseMeshEffect

**Fields:**

- `m_EffectColor`: Color
- `m_EffectDistance`: Vector2
- `m_UseGraphicAlpha`: bool

---

#### ShadowCaster2D

**Line:** 1365068

**Inherits:** ShadowCasterGroup2D

**Fields:**

- `m_HasRenderer`: bool
- `m_UseRendererSilhouette`: bool
- `m_CastsShadows`: bool
- `m_SelfShadows`: bool
- `m_AlphaCutoff`: float
- `m_ShapePathHash`: int
- `m_InstanceId`: int
- `m_ShadowShape2DComponent`: Component
- `m_ShadowShape2DProvider`: ShadowShape2DProvider
- `m_PreviousShadowGroup`: int
- `m_PreviousCastsShadows`: bool
- `m_PreviousPathHash`: int
- `m_SpriteMaterialCount`: int

---

#### ShadowCasterGroup2D

**Line:** 1365262

**Inherits:** MonoBehaviour

**Fields:**

- `m_ShadowCasters`: List<ShadowCaster2D>

---

#### ShadowShape2D

**Line:** 1365619

---

#### ShadowShape2DProvider

**Line:** 1365643

---

#### ShadowsMidtonesHighlights

**Line:** 909653

**Inherits:** VolumeComponent

**Fields:**

- `shadows`: Vector4Parameter
- `midtones`: Vector4Parameter
- `highlights`: Vector4Parameter
- `shadowsStart`: MinFloatParameter
- `shadowsEnd`: MinFloatParameter
- `highlightsStart`: MinFloatParameter
- `highlightsEnd`: MinFloatParameter

---

#### SharedBetweenAnimatorsAttribute

**Line:** 1575257

**Inherits:** Attribute

---

#### SharedGameConfig

**Line:** 1059596

**Inherits:** SharedGameConfigBase

---

#### SharedGameConfigBase

**Line:** 600337

**Inherits:** GameConfigBase

**Fields:**

- `_languagesIntegration`: IGameConfigLibrary<LanguageId, LanguageInfo>
- `_inAppProductsIntegration`: IGameConfigLibrary<InAppProductId, InAppProductInfoBase>
- `_playerSegmentsIntegration`: IGameConfigLibrary<PlayerSegmentId, PlayerSegmentInfoBase>
- `_offersIntegration`: IGameConfigLibrary<MetaOfferId, MetaOfferInfoBase>
- `_offerGroupsIntegration`: IGameConfigLibrary<MetaOfferGroupId, MetaOfferGroupInfoBase>

---

#### SharedTableCollectionMetadata

**Line:** 1327620

**Inherits:** IMetadata

**Fields:**

- `m_Entries`: List<SharedTableCollectionMetadata.Item>

---

#### SharedTableData

**Line:** 1317932

**Inherits:** ScriptableObject

**Fields:**

- `m_TableCollectionName`: string
- `m_TableCollectionNameGuidString`: string
- `m_Entries`: List<SharedTableData.SharedTableEntry>
- `m_Metadata`: MetadataCollection
- `m_KeyGenerator`: IKeyGenerator
- `m_TableCollectionNameGuid`: Guid
- `m_IdDictionary`: Dictionary<long, SharedTableData.SharedTableEntry>
- `m_KeyDictionary`: Dictionary<string, SharedTableData.SharedTableEntry>

---

#### SharedTableEntryMetadata

**Line:** 1327677

**Inherits:** IMetadata

**Fields:**

- `m_Entries`: List<long>
- `m_SharedEntries`: List<SharedTableEntryMetadata.Entry>
- `m_EntriesLookup`: HashSet<long>

---

#### Sheet

**Line:** 1398133

**Inherits:** IDirectResponseSchema

---

#### SheetProperties

**Line:** 1398313

**Inherits:** IDirectResponseSchema

---

#### SheetsBaseServiceRequest

**Line:** 1383113

---

#### SheetsService

**Line:** 1383034

**Inherits:** BaseClientService

---

#### ShortLinkCallback

**Line:** 1571466

**Inherits:** MulticastDelegate

---

#### ShortLinkParams

**Line:** 1571243

**Fields:**

- `data`: string
- `error`: string

---

#### ShortTrackedProperty

**Line:** 1328871

**Inherits:** TrackedProperty

---

#### ShortVariable

**Line:** 1324493

**Inherits:** Variable

---

#### ShowIfAttribute

**Line:** 696453

**Inherits:** PropertyAttribute

---

#### SignComponent

**Line:** 709058

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### SignEventSystem

**Line:** 702610

**Inherits:** ReactiveSystem

---

#### SignListenerComponent

**Line:** 700064

**Inherits:** IComponent

**Fields:**

- `value`: List<ISignListener>

---

#### SignatureDescription

**Line:** 219309

**Fields:**

- `_strKey`: string
- `_strDigest`: string
- `_strFormatter`: string
- `_strDeformatter`: string

---

#### SignatureHelper

**Line:** 270196

---

#### SignedTokenVerificationOptions

**Line:** 1368539

**Fields:**

- `_clock`: IClock

---

#### SimpleLoggerImplementation

**Line:** 693207

**Inherits:** ILoggerImplementation

---

#### SimpleMailPopupUiView

**Line:** 721542

**Inherits:** UiUnityView

**Fields:**

- `Title`: TMP_Text
- `Body`: TMP_Text
- `Rewards`: TMP_Text
- `ClaimButton`: UnityButton

---

#### SimpleMetaplayServiceProvider

**Line:** 520609

**Inherits:** IMetaplayServiceProvider

**Fields:**

- `_services`: Dictionary<Type, SimpleMetaplayServiceProvider.ServiceDescriptor>

---

#### SimpleOpenPopupButtonEntitasUiView

**Line:** 737471

**Inherits:** UiUnityView

**Fields:**

- `Asset`: string
- `OpenPopupButton`: UnityButton

---

#### SimpleOpenPopupButtonUiView

**Line:** 737491

**Inherits:** MonoBehaviour

**Fields:**

- `Asset`: string
- `OpenPopupButton`: UnityButton

---

#### SimplePlayerMail

**Line:** 561393

**Inherits:** MetaInGameMail

---

#### SimpleServiceInitializers

**Line:** 520524

**Inherits:** IServiceInitializers

---

#### SimpleUnityButton

**Line:** 736006

**Inherits:** UnityButton

**Fields:**

- `_tween`: Tween

---

#### SingleConverter

**Line:** 783027

**Inherits:** BaseNumberConverter

---

#### SingleEntityException

**Line:** 1547720

**Inherits:** EntitasException

---

#### SingleError

**Line:** 1495765

---

#### SingleStaticDataBuildSource

**Line:** 595564

**Inherits:** GameConfigBuildSource

---

#### Singleton

**Line:** 1565421

---

#### SingularAdData

**Line:** 1571286

**Inherits:** Dictionary

---

#### SingularInitSystem

**Line:** 696083

**Inherits:** IInitializeSystem

---

#### SingularLinkParams

**Line:** 1571405

**Fields:**

- `_deeplink`: string
- `_passthrough`: string
- `_isDeferred`: bool
- `_urlParameters`: Dictionary<string, string>

---

#### SingularSDK

**Line:** 1571563

**Inherits:** MonoBehaviour

**Fields:**

- `SingularAPIKey`: string
- `SingularAPISecret`: string
- `InitializeOnAwake`: bool
- `enableLogging`: bool
- `logLevel`: int
- `autoIAPComplete`: bool
- `clipboardAttribution`: bool
- `SKANEnabled`: bool
- `manualSKANConversionManagement`: bool
- `waitForTrackingAuthorizationWithTimeoutInterval`: int
- `facebookAppId`: string
- `collectOAID`: bool
- `limitedIdentifiersEnabled`: bool
- `globalProperties`: Dictionary<string, SingularSDK.SingularGlobalProperty>
- `ddlTimeoutSec`: long
- `sessionTimeoutSec`: long
- `shortlinkResolveTimeout`: long
- `resolvedSingularLinkParams`: SingularLinkParams
- `resolvedSingularLinkTime`: int

---

#### SingularTracker

**Line:** 696502

**Inherits:** ITracker

---

#### SinkProviderData

**Line:** 222982

**Fields:**

- `sinkName`: string
- `children`: ArrayList
- `properties`: Hashtable

---

#### SkinAddedMessage

**Line:** 732853

**Inherits:** IMessage

---

#### SkinCheatAction

**Line:** 1075700

**Inherits:** PlayerAction

---

#### SkinCheatContainer

**Line:** 732753

**Inherits:** AbstractCheatContainer

---

#### SkinCollectionEntryUiView

**Line:** 732982

**Inherits:** MonoBehaviour

**Fields:**

- `SkinVisualUiView`: SkinVisualUiView
- `Button`: UnityButton

---

#### SkinCollectionPopupUiView

**Line:** 733023

**Inherits:** MonoBehaviour

**Fields:**

- `SkinEntryPrefab`: SkinCollectionEntryUiView
- `SkinsParent`: RectTransform
- `VisibilityToggle`: ColoredToggle
- `ToggleButton`: UnityButton
- `TitleText`: TMP_Text
- `_currentType`: ItemType

---

#### SkinCollectionVisualConfig

**Line:** 732804

**Inherits:** ScriptableObject

---

#### SkinConfig

**Line:** 1075859

**Inherits:** IGameConfigData

---

#### SkinDetailsPopupUiView

**Line:** 733058

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `ButtonBG`: Image
- `ButtonText`: TMP_Text
- `SkinDetailsUiView`: SkinDetailsUiView

---

#### SkinDetailsUiView

**Line:** 733107

**Inherits:** MonoBehaviour

**Fields:**

- `SkinVisualUiView`: SkinVisualUiView
- `SkinName`: TMP_Text
- `SkinDescription`: TMP_Text
- `ShortForm`: bool
- `_isEquipped`: bool
- `_skinVisualConfig`: SkinVisualConfig

---

#### SkinEquipAction

**Line:** 1075740

**Inherits:** PlayerAction

---

#### SkinEquipmentVisual

**Line:** 710817

**Inherits:** MonoBehaviour

**Fields:**

- `EquipmentVisual`: UnitEquipmentVisual
- `VisibleSkins`: Dictionary<ItemType, SpriteRenderer>

---

#### SkinEquippedMessage

**Line:** 732880

**Inherits:** IMessage

---

#### SkinId

**Line:** 1076201

**Inherits:** IEquatable

---

#### SkinSlotUiView

**Line:** 733193

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `EmptySlotPrefab`: GameObject
- `Button`: UnityButton
- `_slotType`: ItemType
- `_emptySlotInstance`: GameObject

---

#### SkinUiViewManager

**Line:** 733253

**Inherits:** MonoBehaviour

**Fields:**

- `SkinSlotPrefab`: SkinSlotUiView
- `Slots`: List<Transform>
- `_skinSlots`: Dictionary<ItemType, SkinSlotUiView>

---

#### SkinUnequipAction

**Line:** 1075775

**Inherits:** PlayerAction

---

#### SkinUnequippedMessage

**Line:** 732904

**Inherits:** IMessage

---

#### SkinVisibilityChangedMessage

**Line:** 732928

**Inherits:** IMessage

---

#### SkinVisualConfig

**Line:** 732835

**Fields:**

- `Name`: string
- `Icon`: Sprite
- `Prefab`: SpriteRenderer

---

#### SkinVisualUiView

**Line:** 733279

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `Equipped`: GameObject
- `CanvasGroup`: CanvasGroup

---

#### SkinnedMeshRenderer

**Line:** 875680

**Inherits:** Renderer

---

#### SkinsLocalizer

**Line:** 721344

**Inherits:** LocalizerBase

---

#### SkinsVisualConfig

**Line:** 732818

**Inherits:** ScriptableObject

**Fields:**

- `SkinConfigs`: List<SkinCollectionVisualConfig>
- `SkinAnimationView`: SummonEntryAnimationView

---

#### SkipLocalsInitAttribute

**Line:** 1346121

**Inherits:** Attribute

---

#### SkippedTimeException

**Line:** 1146663

**Inherits:** ArgumentOutOfRangeException

---

#### SkippedTimeResolver

**Line:** 1148625

**Inherits:** MulticastDelegate

---

#### Skybox

**Line:** 875137

**Inherits:** Behaviour

---

#### Slicer

**Line:** 1398457

**Inherits:** IDirectResponseSchema

---

#### SlicerSpec

**Line:** 1398517

**Inherits:** IDirectResponseSchema

---

#### Slider

**Line:** 1356958

**Inherits:** Selectable

**Fields:**

- `m_FillRect`: RectTransform
- `m_HandleRect`: RectTransform
- `m_MinValue`: float
- `m_MaxValue`: float
- `m_WholeNumbers`: bool
- `m_Value`: float
- `m_FillImage`: Image
- `m_FillTransform`: Transform
- `m_FillContainerRect`: RectTransform
- `m_HandleTransform`: Transform
- `m_HandleContainerRect`: RectTransform
- `m_Offset`: Vector2
- `m_Tracker`: DrivenRectTransformTracker
- `m_DelayedUpdateVisuals`: bool

---

#### SliderInt

**Line:** 628045

**Inherits:** BaseSlider

---

#### SlomoFeature

**Line:** 696098

**Inherits:** Feature

---

#### SlomoSystem

**Line:** 696107

**Inherits:** IExecuteSystem

---

#### SlotIdComponent

**Line:** 730475

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### SlotVisual

**Line:** 714165

**Inherits:** MonoBehaviour

**Fields:**

- `SlotIcon`: Image

---

#### SlotsConfig

**Line:** 711378

**Inherits:** ScriptableObject

**Fields:**

- `_slotIcons`: SerializableDictionary<ItemType, Sprite>

---

#### SmallChatEntryVisual

**Line:** 708174

**Inherits:** MonoBehaviour

**Fields:**

- `MessageText`: TMP_Text

---

#### SmallChatUiView

**Line:** 708195

**Inherits:** UiUnityView

**Fields:**

- `SmallChatEntryVisualPrefab`: SmallChatEntryVisual
- `Parent`: Transform
- `ChatOpenButton`: UnityButton
- `ChatContainer`: GameObject
- `UnreadCountContainer`: GameObject
- `UnreadCount`: TMP_Text
- `_chatModel`: ChatModel
- `initialized`: bool

---

#### SmartFormatTag

**Line:** 1327716

**Inherits:** SharedTableEntryMetadata

---

#### SmartFormatter

**Line:** 1320261

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `m_Settings`: SmartSettings
- `m_Parser`: Parser
- `m_Sources`: List<ISource>
- `m_Formatters`: List<IFormatter>
- `m_NotEmptyFormatterExtensionNames`: List<string>
- `OnFormattingFailure`: EventHandler<FormattingErrorEventArgs>

---

#### SmartSettings

**Line:** 1322390

**Fields:**

- `m_FormatErrorAction`: ErrorAction
- `m_ParseErrorAction`: ErrorAction
- `m_CaseSensitivity`: CaseSensitivityType
- `m_ConvertCharacterStringLiterals`: bool

---

#### SnakeCaseNamingStrategy

**Line:** 1041225

**Inherits:** NamingStrategy

---

#### SoapAttribute

**Line:** 223192

**Inherits:** Attribute

**Fields:**

- `_useAttribute`: bool
- `ProtXmlNamespace`: string
- `ReflectInfo`: object

---

#### SoapFieldAttribute

**Line:** 223221

**Inherits:** SoapAttribute

**Fields:**

- `_elementName`: string
- `_isElement`: bool

---

#### SoapMethodAttribute

**Line:** 223248

**Inherits:** SoapAttribute

**Fields:**

- `_responseElement`: string
- `_responseNamespace`: string
- `_returnElement`: string
- `_soapAction`: string
- `_useAttribute`: bool
- `_namespace`: string

---

#### SoapParameterAttribute

**Line:** 223280

**Inherits:** SoapAttribute

---

#### SoapServices

**Line:** 221712

---

#### SoapTypeAttribute

**Line:** 223291

**Inherits:** SoapAttribute

**Fields:**

- `_useAttribute`: bool
- `_xmlElementName`: string
- `_xmlNamespace`: string
- `_xmlTypeName`: string
- `_xmlTypeNamespace`: string
- `_isType`: bool
- `_isElement`: bool

---

#### SocialAuthManager

**Line:** 1309173

**Fields:**

- `_socialAuthenticationDelegate`: IMetaplayClientSocialAuthenticationDelegate
- `_bufferedClaims`: MetaDictionary<AuthenticationPlatform, SocialAuthenticationClaimBase>
- `_connected`: bool

---

#### SocialAuthenticateDetach

**Line:** 543363

**Inherits:** MetaMessage

---

#### SocialAuthenticateForceReconnect

**Line:** 543334

**Inherits:** MetaMessage

---

#### SocialAuthenticateForceReconnectConnectionError

**Line:** 1314374

**Inherits:** TransientError

---

#### SocialAuthenticateRequest

**Line:** 543172

**Inherits:** MetaRequest

---

#### SocialAuthenticateResolveConflict

**Line:** 543295

**Inherits:** MetaMessage

---

#### SocialAuthenticateResult

**Line:** 543211

**Inherits:** MetaResponse

---

#### SocialAuthenticationClaimBase

**Line:** 499258

---

#### SocialAuthenticationClaimCompanyId

**Line:** 499762

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimDevelopment

**Line:** 499274

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimFacebookLogin

**Line:** 499519

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimGameCenter

**Line:** 499418

**Inherits:** SocialAuthenticationClaimBase

**Fields:**

- `LegacyUserId`: string
- `PublicKeyUrl`: string
- `Timestamp`: ulong
- `Signature`: string
- `Salt`: string
- `BundleId`: string
- `GameCenter2020MigrationClaim`: SocialAuthenticationClaimGameCenter2020

---

#### SocialAuthenticationClaimGameCenter2020

**Line:** 499552

**Inherits:** SocialAuthenticationClaimBase

**Fields:**

- `TeamPlayerId`: string
- `GamePlayerId`: string
- `PublicKeyUrl`: string
- `Timestamp`: ulong
- `Signature`: string
- `Salt`: string
- `BundleId`: string

---

#### SocialAuthenticationClaimGooglePlayV1

**Line:** 499340

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimGooglePlayV2

**Line:** 499385

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimGoogleSignIn

**Line:** 499453

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimImmutableX

**Line:** 499587

**Inherits:** SocialAuthenticationClaimBase

**Fields:**

- `_challengeTimestamp`: MetaTime

---

#### SocialAuthenticationClaimSignInWithApple

**Line:** 499486

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimSteam

**Line:** 499307

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialAuthenticationClaimWebLogin

**Line:** 499795

**Inherits:** SocialAuthenticationClaimBase

---

#### SocialLoginMessage

**Line:** 738498

**Inherits:** IMessage

---

#### Socket

**Line:** 799705

**Inherits:** IDisposable

**Fields:**

- `is_closed`: bool
- `is_listening`: bool
- `linger_timeout`: int
- `addressFamily`: AddressFamily
- `socketType`: SocketType
- `protocolType`: ProtocolType
- `m_IntCleanedUp`: int

---

#### SocketAddress

**Line:** 791994

**Fields:**

- `m_changed`: bool
- `m_hash`: int

---

#### SocketAsyncEventArgs

**Line:** 800748

**Inherits:** EventArgs

**Fields:**

- `disposed`: bool
- `remote_ep`: EndPoint
- `current_socket`: Socket
- `Completed`: EventHandler<SocketAsyncEventArgs>
- `_buffer`: Memory<byte>
- `_offset`: int
- `_count`: int
- `_bufferIsExplicitArray`: bool

---

#### SocketElement

**Line:** 803251

**Inherits:** ConfigurationElement

---

#### SocketException

**Line:** 800244

**Inherits:** Win32Exception

**Fields:**

- `m_EndPoint`: EndPoint

---

#### SocketProbeResult

**Line:** 549504

---

#### SocketProbeStep

**Line:** 549442

---

#### SortAttribute

**Line:** 1442941

**Inherits:** Attribute

---

#### SortByIndexUiView

**Line:** 732497

**Inherits:** UiUnityView

**Fields:**

- `_entity`: GameEntity

---

#### SortColumnDescription

**Line:** 626450

**Inherits:** INotifyBindablePropertyChanged

**Fields:**

- `m_ColumnIndex`: int
- `m_ColumnName`: string
- `m_SortDirection`: SortDirection
- `propertyChanged`: EventHandler<BindablePropertyChangedEventArgs>
- `changed`: Action<SortColumnDescription>

---

#### SortColumnDescriptions

**Line:** 626595

**Inherits:** ICollection

**Fields:**

- `changed`: Action

---

#### SortKey

**Line:** 274235

---

#### SortRangeRequest

**Line:** 1398649

**Inherits:** IDirectResponseSchema

---

#### SortSpec

**Line:** 1398697

**Inherits:** IDirectResponseSchema

---

#### SortVersion

**Line:** 272202

---

#### SortedList

**Line:** 788688

**Fields:**

- `_size`: int
- `version`: int
- `comparer`: IComparer<TKey>
- `_syncRoot`: object

---

#### SortingGroup

**Line:** 891448

**Inherits:** Behaviour

---

#### SourceAndDestination

**Line:** 1398805

**Inherits:** IDirectResponseSchema

---

#### SpaceAttribute

**Line:** 880807

**Inherits:** PropertyAttribute

---

#### SpanAction

**Line:** 464756

---

#### SparseIndex

**Line:** 1545388

---

#### SpecificLocaleSelector

**Line:** 1319477

**Inherits:** IStartupLocaleSelector

**Fields:**

- `m_LocaleId`: LocaleIdentifier

---

#### SphericalHarmonicsL2Utils

**Line:** 820371

---

#### SpikeVisual

**Line:** 731290

**Inherits:** MonoBehaviour

**Fields:**

- `Spike`: Transform
- `Hole`: Transform
- `RetractedHeight`: float
- `ExtendedHeight`: float

---

#### SplitToning

**Line:** 909687

**Inherits:** VolumeComponent

**Fields:**

- `shadows`: ColorParameter
- `highlights`: ColorParameter
- `balance`: ClampedFloatParameter

---

#### Spreadsheet

**Line:** 1398865

**Inherits:** IDirectResponseSchema

---

#### SpreadsheetContent

**Line:** 600671

---

#### SpreadsheetFileSourceInfo

**Line:** 598762

**Inherits:** GameConfigSpreadsheetSourceInfo

---

#### SpreadsheetProperties

**Line:** 1398985

**Inherits:** IDirectResponseSchema

---

#### SpreadsheetTheme

**Line:** 1399105

**Inherits:** IDirectResponseSchema

---

#### SpreadsheetsResource

**Line:** 1384828

---

#### Sprite

**Line:** 869504

**Inherits:** Object

---

#### SpriteAsset

**Line:** 1348051

**Inherits:** TextAsset

**Fields:**

- `m_SpriteCharacterTable`: List<SpriteCharacter>
- `m_SpriteGlyphTable`: List<SpriteGlyph>
- `fallbackSpriteAssets`: List<SpriteAsset>

---

#### SpriteAtlas

**Line:** 900141

**Inherits:** Object

---

#### SpriteAtlasManager

**Line:** 900103

---

#### SpriteGlyph

**Line:** 1348202

**Inherits:** Glyph

**Fields:**

- `sprite`: Sprite

---

#### SpriteMask

**Line:** 1593855

**Inherits:** Renderer

---

#### SpriteRenderer

**Line:** 869384

**Inherits:** Renderer

**Fields:**

- `m_SpriteChangeEvent`: UnityEvent<SpriteRenderer>

---

#### SpriteShapeRenderer

**Line:** 1594211

**Inherits:** Renderer

---

#### SpriteSwapUnityButton

**Line:** 736033

**Inherits:** UnityButton

**Fields:**

- `Image`: Image
- `UnPressedSprite`: Sprite
- `PressedSprite`: Sprite
- `IndicatesInteractableState`: bool
- `UseColor`: bool
- `DisabledSprite`: Sprite
- `DisabledColor`: Color

---

#### SqlBytes

**Line:** 1090710

**Inherits:** INullable

**Fields:**

- `_lCurLen`: long
- `_state`: SqlBytesCharsState

---

#### SqlChars

**Line:** 1090784

**Inherits:** INullable

**Fields:**

- `_lCurLen`: long
- `_state`: SqlBytesCharsState

---

#### SqlNullValueException

**Line:** 1092246

**Inherits:** SqlTypeException

---

#### SqlTruncateException

**Line:** 1092268

**Inherits:** SqlTypeException

---

#### SqlTypeException

**Line:** 1092224

**Inherits:** SystemException

---

#### SqlXml

**Line:** 1092313

**Inherits:** INullable

**Fields:**

- `_createSqlReaderMethodInfo`: MethodInfo
- `_fNotNull`: bool
- `_stream`: Stream
- `_firstCreateReader`: bool

---

#### SseItemParser

**Line:** 1586731

---

#### SseParser

**Line:** 1586500

**Fields:**

- `_used`: int
- `_lineOffset`: int
- `_lineLength`: int
- `_newlineIndex`: int
- `_lastSearchedForNewline`: int
- `_eof`: bool
- `_dataLength`: int
- `_dataAppended`: bool
- `_eventType`: string

---

#### SslClientAuthenticationOptions

**Line:** 802602

**Fields:**

- `_encryptionPolicy`: EncryptionPolicy
- `_checkCertificateRevocation`: X509RevocationMode
- `_enabledSslProtocols`: SslProtocols
- `_allowRenegotiation`: bool

---

#### SslServerAuthenticationOptions

**Line:** 802674

**Fields:**

- `_checkCertificateRevocation`: X509RevocationMode
- `_enabledSslProtocols`: SslProtocols
- `_encryptionPolicy`: EncryptionPolicy
- `_allowRenegotiation`: bool

---

#### SslStream

**Line:** 802855

**Inherits:** AuthenticatedStream

**Fields:**

- `provider`: MobileTlsProvider
- `settings`: MonoTlsSettings
- `validationCallback`: RemoteCertificateValidationCallback
- `selectionCallback`: LocalCertificateSelectionCallback
- `impl`: MobileAuthenticatedStream
- `explicitSettings`: bool

---

#### Stack

**Line:** 410664

**Fields:**

- `_size`: int
- `_version`: int
- `_syncRoot`: object

---

#### StackFrame

**Line:** 275345

**Fields:**

- `ilOffset`: int
- `nativeOffset`: int
- `methodAddress`: long
- `methodIndex`: uint
- `methodBase`: MethodBase
- `fileName`: string
- `lineNumber`: int
- `columnNumber`: int
- `internalMethodName`: string

---

#### StackFrames

**Line:** 1567160

**Fields:**

- `collectionRef`: StackFrames
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### StackOverflowException

**Line:** 57554

**Inherits:** SystemException

---

#### StackTrace

**Line:** 275415

**Fields:**

- `debug_info`: bool

---

#### StageRuntimeInterface

**Line:** 833199

**Fields:**

- `m_AddGameObject`: Func<bool, GameObject>
- `m_GetCamera`: Func<Camera>
- `m_GetSunLight`: Func<Light>
- `SRPData`: object

---

#### StallSummaryAnalytic

**Line:** 1587445

**Inherits:** AnalyticsEventBase

**Fields:**

- `Duration`: double

---

#### StampedeView

**Line:** 731170

**Inherits:** GameUnityView

**Fields:**

- `StampedeSound`: AudioClip
- `Bulls`: List<BullView>

---

#### StandaloneInputModule

**Line:** 1360678

**Inherits:** PointerInputModule

**Fields:**

- `m_PrevActionTime`: float
- `m_LastMoveVector`: Vector2
- `m_ConsecutiveMoveCount`: int
- `m_LastMousePosition`: Vector2
- `m_MousePosition`: Vector2
- `m_CurrentFocusedGameObject`: GameObject
- `m_InputPointerEvent`: PointerEventData
- `m_HorizontalAxis`: string
- `m_VerticalAxis`: string
- `m_SubmitButton`: string
- `m_CancelButton`: string
- `m_InputActionsPerSecond`: float
- `m_RepeatDelay`: float
- `m_ForceModuleActive`: bool

---

#### StandardConsoleService

**Line:** 1446209

**Inherits:** IConsoleService

**Fields:**

- `_hasCleared`: bool
- `_consoleEntries`: CircularBuffer<ConsoleEntry>
- `Updated`: ConsoleUpdatedEventHandler
- `Error`: ConsoleUpdatedEventHandler

---

#### StandardMappingAsUV2

**Line:** 714308

**Inherits:** BaseMeshEffect

---

#### StandardPurchasingModule

**Line:** 1407296

**Inherits:** AbstractPurchasingModule

**Fields:**

- `windowsStore`: WinRTStore

---

#### StandardResponse

**Line:** 1495190

---

#### StandardSystemInformationService

**Line:** 1446372

**Inherits:** ISystemInformationService

---

#### StarterPackageBubbleUiView

**Line:** 730323

**Inherits:** UiUnityView

**Fields:**

- `OpenButton`: UnityButton
- `Icon`: Image
- `Content`: GameObject
- `TimerText`: TMP_Text
- `_starterPackage`: GameEntity

---

#### StarterPackageInitializeSystem

**Line:** 730308

**Inherits:** IInitializeSystem

---

#### StarterPackageUiView

**Line:** 730348

**Inherits:** UiUnityView

**Fields:**

- `Title`: TMP_Text
- `BuyButton`: UnityButton
- `PriceText`: TMP_Text
- `ItemVisual`: ItemVisual
- `_pack`: GameEntity

---

#### StatConfig

**Line:** 1076416

**Inherits:** IGameConfigData

---

#### StatContribution

**Line:** 1076564

---

#### StatContributions

**Line:** 1075196

---

#### StatNode

**Line:** 1076511

**Inherits:** IEquatable

---

#### StatTargetBase

**Line:** 1076816

**Inherits:** IEquatable

---

#### StateMachineAttribute

**Line:** 234408

**Inherits:** Attribute

---

#### StateMachineBehaviour

**Line:** 1575262

**Inherits:** ScriptableObject

---

#### StaticBlobProvider

**Line:** 587214

**Inherits:** IBlobProvider

**Fields:**

- `_version`: ContentHash

---

#### StaticConfigArchiveProvider

**Line:** 587841

**Inherits:** ConfigArchiveProvider

**Fields:**

- `_archive`: ConfigArchive

---

#### StaticDataDictionaryBuildSource

**Line:** 595615

**Inherits:** GameConfigBuildSource

---

#### Stats

**Line:** 1076707

---

#### StatsLocalizer

**Line:** 721371

**Inherits:** LocalizerBase

---

#### StatsParsers

**Line:** 1052310

**Inherits:** ConfigParserProvider

---

#### StayLastSiblingUiView

**Line:** 697218

**Inherits:** MonoBehaviour

---

#### SteamClientHandlingResult

**Line:** 587045

**Inherits:** ServerDrivenInAppPurchaseClientHandlingResult

---

#### SteamCredentialsProvider

**Line:** 1309242

**Inherits:** ISocialCredentialsProvider

---

#### SteamInitiationParams

**Line:** 586927

**Inherits:** ServerDrivenInAppPurchaseInitiationParams

**Fields:**

- `UseWebUserSession`: bool

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

- `overrideStencilState`: bool
- `stencilReference`: int
- `stencilCompareFunction`: CompareFunction
- `passOperation`: StencilOp
- `failOperation`: StencilOp
- `zFailOperation`: StencilOp

---

#### StepToStoneAction

**Line:** 1079412

**Inherits:** PlayerAction

---

#### SteppedToStoneMessage

**Line:** 733989

**Inherits:** IMessage

---

#### SteppingStoneFreeResourcePackRedDotUiView

**Line:** 734723

**Inherits:** RedDotUiView

---

#### SteppingStoneMiniGame

**Line:** 1079612

---

#### SteppingStones

**Line:** 1079666

**Inherits:** IRewardSource

---

#### SteppingStonesBubbleUiView

**Line:** 734852

**Inherits:** MonoBehaviour

**Fields:**

- `OpenButton`: UnityButton
- `Content`: GameObject

---

#### SteppingStonesCharacter

**Line:** 734917

**Inherits:** MonoBehaviour

**Fields:**

- `CharacterStartPosition`: Transform
- `CharacterEndPosition`: Transform
- `Character`: Rigidbody2D
- `CharacterShadow`: SpriteRenderer
- `SortingGroup`: SortingGroup
- `_jump`: Sequence
- `_shadowLocalOffset`: Vector2

---

#### SteppingStonesEventConcludedMessage

**Line:** 734047

**Inherits:** IMessage

---

#### SteppingStonesEventConfig

**Line:** 1052489

**Inherits:** LiveOpsEventContent

---

#### SteppingStonesEventModel

**Line:** 1052661

**Inherits:** PlayerLiveOpsEventModel

**Fields:**

- `CanAutoRun`: bool

---

#### SteppingStonesEventStartedMessage

**Line:** 734067

**Inherits:** IMessage

---

#### SteppingStonesInfoPopupUiView

**Line:** 734966

**Inherits:** MonoBehaviour

**Fields:**

- `RewardEntryPrefab`: SteppingStoneRewardEntryUiView
- `Separator`: RectTransform
- `RewardsParent`: RectTransform
- `_rewardEntries`: List<SteppingStoneRewardEntryUiView>

---

#### SteppingStonesManager

**Line:** 734204

**Inherits:** MonoBehaviourSingleton

**Fields:**

- `SafeAreaView`: SafeAreaView
- `Character`: SteppingStonesCharacter
- `TilesParent`: Transform
- `TileSpacing`: Vector2
- `EndAreaXOffset`: float
- `_instantiatedTiles`: List<TileView>
- `EndPlatform`: GameObject
- `_eventConfig`: SteppingStonesEventConfig
- `_eventModel`: SteppingStonesEventModel
- `_nextStonesValidated`: bool

---

#### SteppingStonesMiniGameEndedMessage

**Line:** 734009

**Inherits:** IMessage

---

#### SteppingStonesPopupUiView

**Line:** 734984

**Inherits:** MonoBehaviour

**Fields:**

- `PopupView`: PopupUiView
- `InfoButton`: UnityButton
- `OneAttemptPriceButton`: PriceButtonUiView
- `AutoPriceButton`: PriceButtonUiView
- `AutoInfoButton`: UnityButton
- `OpenShopButton`: UnityButton
- `AutoRunButtonText`: TMP_Text
- `AutoRunButtonDescription`: TMP_Text

---

#### SteppingStonesRedDotLogic

**Line:** 734299

**Inherits:** IRedDotLogic

---

#### SteppingStonesRunCreatedMessage

**Line:** 734087

**Inherits:** IMessage

---

#### SteppingStonesSystem

**Line:** 734435

**Inherits:** IInitSystem

---

#### SteppingStonesTimerUiView

**Line:** 735045

**Inherits:** MonoBehaviour

**Fields:**

- `TimerText`: TMP_Text
- `_eventModel`: SteppingStonesEventModel

---

#### StoneIndicatorArrowUiView

**Line:** 735082

**Inherits:** MonoBehaviour

**Fields:**

- `Arrow`: Transform
- `YOffsetFromStone`: float
- `IdleTimeThreshold`: float
- `AnimationDuration`: float
- `AnimationHeight`: float
- `_instantiatedArrows`: List<Transform>

---

#### StonesValidatedMessage

**Line:** 734096

**Inherits:** IMessage

---

#### Stopwatch

**Line:** 778327

**Fields:**

- `elapsed`: long
- `started`: long
- `is_running`: bool

---

#### StorageBlobProvider

**Line:** 587281

**Inherits:** IBlobProvider

**Fields:**

- `_storage`: IBlobStorage

---

#### StoreID

**Line:** 1406780

**Fields:**

- `store`: string
- `id`: string

---

#### StoreNotSupportedException

**Line:** 1544957

**Inherits:** IAPSecurityException

---

#### StoreSubscriptionInfoNotSupportedException

**Line:** 1407797

**Inherits:** ReceiptParserException

---

#### StrafeRunView

**Line:** 731257

**Inherits:** GameUnityView

**Fields:**

- `Dir`: Vector2
- `PlaneParent`: Transform
- `Plane`: Transform
- `Bullets`: Transform
- `Shadow`: Transform
- `PlaneSound`: AudioClip
- `MachineGunSound`: AudioClip
- `_squence`: Sequence

---

#### Stream

**Line:** 470217

**Inherits:** MarshalByRefObject

**Fields:**

- `_asyncActiveSemaphore`: SemaphoreSlim

---

#### StreamBindingFailureMessage

**Line:** 1569200

**Inherits:** HubMessage

---

#### StreamContent

**Line:** 1488930

**Inherits:** HttpContent

**Fields:**

- `contentCopied`: bool

---

#### StreamInterceptor

**Line:** 1497248

**Inherits:** MulticastDelegate

---

#### StreamInvocationMessage

**Line:** 1569028

**Inherits:** HubMethodInvocationMessage

---

#### StreamItemMessage

**Line:** 1569229

**Inherits:** HubInvocationMessage

---

#### StreamMessageTransport

**Line:** 548098

**Inherits:** WireMessageTransport

**Fields:**

- `_lock`: object
- `_cts`: CancellationTokenSource
- `_abortOpenTcs`: TaskCompletionSource<object>
- `_writeQueue`: WireMessageWriteQueue
- `_writeBufferContentLength`: int
- `_writeBufferNumMetaMessages`: int
- `_writeBufferNumPackets`: int
- `_readBuffer`: WireMessageReadBuffer
- `_pingTracker`: MessageTransportPingTracker
- `_debugDiagnostics`: LoginTransportDebugDiagnostics

---

#### StreamMessageTransportPreconnection

**Line:** 549229

---

#### StreamPipeReaderOptions

**Line:** 1516872

---

#### StreamPipeWriterOptions

**Line:** 1517121

---

#### StreamReader

**Line:** 468313

**Inherits:** TextReader

**Fields:**

- `_stream`: Stream
- `_encoding`: Encoding
- `_decoder`: Decoder
- `_charPos`: int
- `_charLen`: int
- `_byteLen`: int
- `_bytePos`: int
- `_maxCharsPerBuffer`: int
- `_detectEncoding`: bool
- `_checkPreamble`: bool
- `_isBlocked`: bool
- `_closable`: bool
- `_asyncReadTask`: Task

---

#### StreamWriter

**Line:** 468613

**Inherits:** TextWriter

**Fields:**

- `_stream`: Stream
- `_encoding`: Encoding
- `_encoder`: Encoder
- `_charPos`: int
- `_charLen`: int
- `_autoFlush`: bool
- `_haveWrittenPreamble`: bool
- `_closable`: bool
- `_asyncWriteTask`: Task

---

#### String

**Line:** 3193

**Inherits:** IComparable

**Fields:**

- `_stringLength`: int
- `_firstChar`: char

---

#### StringBuilder

**Line:** 215069

**Inherits:** ISerializable

---

#### StringCollection

**Line:** 785686

**Inherits:** IList

---

#### StringComparer

**Line:** 57570

**Inherits:** IComparer

---

#### StringContent

**Line:** 1488964

**Inherits:** ByteArrayContent

---

#### StringControl

**Line:** 1445000

**Inherits:** DataBoundControl

**Fields:**

- `InputField`: InputField
- `Title`: Text

---

#### StringConverter

**Line:** 783055

**Inherits:** TypeConverter

---

#### StringDictionary

**Line:** 785781

**Inherits:** IEnumerable

---

#### StringEnumConverter

**Line:** 1048723

**Inherits:** JsonConverter

---

#### StringFreezingAttribute

**Line:** 234430

**Inherits:** Attribute

---

#### StringGlobalVariable

**Line:** 1321538

**Inherits:** StringVariable

---

#### StringId

**Line:** 524091

---

#### StringIdBase

**Line:** 578151

**Inherits:** IStringId

---

#### StringIdTypeConverter

**Line:** 524189

**Inherits:** StringTypeConverterHelper

**Fields:**

- `_stringIdType`: Type

---

#### StringInfo

**Line:** 273769

**Fields:**

- `m_str`: string

---

#### StringLengthAttribute

**Line:** 1510027

**Inherits:** ValidationAttribute

---

#### StringList

**Line:** 1492053

**Fields:**

- `collectionRef`: StringList
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### StringOutput

**Line:** 1323130

**Inherits:** IOutput

---

#### StringPlugin

**Line:** 1429563

**Inherits:** ABSTweenPlugin

---

#### StringReader

**Line:** 470668

**Inherits:** TextReader

**Fields:**

- `_s`: string
- `_pos`: int
- `_length`: int

---

#### StringSegmentComparer

**Line:** 1559630

**Inherits:** IComparer

---

#### StringStringMap

**Line:** 1491894

**Fields:**

- `collectionRef`: StringStringMap
- `keyCollection`: IList<string>
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### StringTable

**Line:** 1318157

**Inherits:** DetailedLocalizationTable

---

#### StringTableEntry

**Line:** 1318080

**Inherits:** TableEntry

**Fields:**

- `m_FormatCache`: FormatCache

---

#### StringTrackedProperty

**Line:** 1328987

**Inherits:** TrackedProperty

---

#### StringTypeConverterHelper

**Line:** 524267

---

#### StringValueAttribute

**Line:** 1495268

**Inherits:** Attribute

---

#### StringVariable

**Line:** 1324685

**Inherits:** Variable

---

#### StringWithQualityHeaderValue

**Line:** 1491220

**Inherits:** ICloneable

---

#### StringWriter

**Line:** 470717

**Inherits:** TextWriter

**Fields:**

- `_sb`: StringBuilder
- `_isOpen`: bool

---

#### StrongBox

**Line:** 1299724

**Fields:**

- `Value`: T

---

#### StrongNameKeyPair

**Line:** 269251

**Inherits:** ISerializable

**Fields:**

- `_keyPairContainer`: string
- `_keyPairExported`: bool

---

#### Style

**Line:** 1507031

**Fields:**

- `ActiveColor`: Color
- `DisabledColor`: Color
- `HoverColor`: Color
- `Image`: Sprite
- `NormalColor`: Color

---

#### StyleComponent

**Line:** 1506948

**Inherits:** SRMonoBehaviour

**Fields:**

- `_activeStyle`: Style
- `_cachedRoot`: StyleRoot
- `_graphic`: Graphic
- `_hasStarted`: bool
- `_image`: Image
- `_selectable`: Selectable
- `_styleKey`: string
- `IgnoreImage`: bool

---

#### StyleRoot

**Line:** 1506999

**Inherits:** SRMonoBehaviour

**Fields:**

- `_activeStyleSheet`: StyleSheet
- `StyleSheet`: StyleSheet

---

#### StyleSheet

**Line:** 1507054

**Inherits:** ScriptableObject

**Fields:**

- `_keys`: List<string>
- `_styles`: List<Style>
- `Parent`: StyleSheet

---

#### SubStringFormatter

**Line:** 1322142

**Inherits:** FormatterBase

**Fields:**

- `m_ParameterDelimiter`: char
- `m_NullDisplayString`: string

---

#### SubUiCleanupSystem

**Line:** 737010

**Inherits:** ReactiveSystem

---

#### SubUiDestroySystem

**Line:** 737031

**Inherits:** ReactiveSystem

---

#### SubUiElements

**Line:** 736214

**Inherits:** IComponent

**Fields:**

- `Value`: List<UiEntityRef>

---

#### SubjectTokenException

**Line:** 1370529

**Inherits:** Exception

---

#### SubscriptionInfo

**Line:** 1407615

---

#### SubscriptionInstanceModel

**Line:** 586519

---

#### SubscriptionManager

**Line:** 1407574

---

#### SubscriptionModel

**Line:** 586438

---

#### SubscriptionQueryResult

**Line:** 586806

---

#### SubsystemsAnalyticBase

**Line:** 1586814

**Inherits:** AnalyticsEventBase

**Fields:**

- `subsystem`: string

---

#### SubsystemsAnalyticInfo

**Line:** 1586861

**Inherits:** SubsystemsAnalyticBase

**Fields:**

- `id`: string
- `plugin_name`: string
- `version`: string
- `library_name`: string

---

#### SubsystemsAnalyticStart

**Line:** 1586829

**Inherits:** SubsystemsAnalyticBase

---

#### SubsystemsAnalyticStop

**Line:** 1586845

**Inherits:** SubsystemsAnalyticBase

---

#### SupportedOnRenderPipelineAttribute

**Line:** 894858

**Inherits:** Attribute

---

#### SupportedOnRendererAttribute

**Line:** 914393

**Inherits:** Attribute

---

#### SupportedRenderingFeatures

**Line:** 897213

---

#### SupportedSchemaVersionsAttribute

**Line:** 604100

**Inherits:** Attribute

---

#### SurfaceDataAttributes

**Line:** 821498

**Inherits:** Attribute

**Fields:**

- `isDirection`: bool
- `sRGBDisplay`: bool
- `precision`: FieldPrecision
- `checkIsNormalized`: bool
- `preprocessor`: string

---

#### Switch

**Line:** 777426

**Fields:**

- `switchValueString`: string
- `defaultValue`: string

---

#### SwitchCase

**Line:** 1289736

---

#### SwitchExpression

**Line:** 1289761

**Inherits:** Expression

---

#### SymbolDocumentInfo

**Line:** 1289799

---

#### SymmetricAlgorithm

**Line:** 219400

**Inherits:** IDisposable

**Fields:**

- `BlockSizeValue`: int
- `FeedbackSizeValue`: int
- `KeySizeValue`: int
- `ModeValue`: CipherMode
- `PaddingValue`: PaddingMode

---

#### SynchronizationContext

**Line:** 180822

**Fields:**

- `_props`: SynchronizationContextProperties

---

#### SynchronizationLockException

**Line:** 179094

**Inherits:** SystemException

---

#### SyntaxErrorException

**Line:** 1086418

**Inherits:** InvalidExpressionException

---

#### SystemClock

**Line:** 1495053

**Inherits:** IClock

---

#### SystemException

**Line:** 57757

**Inherits:** Exception

---

#### SystemInfo

**Line:** 1590859

**Fields:**

- `parentSystemInfo`: SystemInfo
- `isActive`: bool
- `_accumulatedExecutionDuration`: double
- `_minExecutionDuration`: double
- `_maxExecutionDuration`: double
- `_executionDurationsCount`: int
- `_accumulatedCleanupDuration`: double
- `_minCleanupDuration`: double
- `_maxCleanupDuration`: double
- `_cleanupDurationsCount`: int

---

#### SystemLocaleSelector

**Line:** 1319503

**Inherits:** IStartupLocaleSelector

---

#### Systems

**Line:** 1547154

**Inherits:** IInitializeSystem

---

#### TCFData

**Line:** 1564547

**Fields:**

- `features`: List<TCFFeature>
- `purposes`: List<TCFPurpose>
- `specialFeatures`: List<TCFSpecialFeature>
- `specialPurposes`: List<TCFSpecialPurpose>
- `stacks`: List<TCFStack>
- `vendors`: List<TCFVendor>
- `tcString`: string

---

#### TCFFeature

**Line:** 1564566

**Fields:**

- `purposeDescription`: string
- `descriptionLegal`: string
- `id`: int
- `name`: string

---

#### TCFHelper

**Line:** 738820

---

#### TCFPurpose

**Line:** 1564582

**Fields:**

- `purposeDescription`: string
- `descriptionLegal`: string
- `id`: int
- `name`: string
- `isPartOfASelectedStack`: bool
- `showConsentToggle`: bool
- `showLegitimateInterestToggle`: bool
- `_consent`: string
- `_legitimateInterestConsent`: string
- `_stackId`: string

---

#### TCFSpecialFeature

**Line:** 1564618

**Fields:**

- `purposeDescription`: string
- `descriptionLegal`: string
- `id`: int
- `name`: string
- `isPartOfASelectedStack`: bool
- `showConsentToggle`: bool
- `_consent`: string
- `_stackId`: string

---

#### TCFSpecialPurpose

**Line:** 1564648

**Fields:**

- `purposeDescription`: string
- `descriptionLegal`: string
- `id`: int
- `name`: string

---

#### TCFStack

**Line:** 1564664

**Fields:**

- `description`: string
- `id`: int
- `name`: string
- `purposeIds`: List<int>
- `specialFeatureIds`: List<int>

---

#### TCFVendor

**Line:** 1564681

**Fields:**

- `features`: List<IdAndName>
- `flexiblePurposes`: List<IdAndName>
- `id`: int
- `legitimateInterestPurposes`: List<IdAndName>
- `name`: string
- `policyUrl`: string
- `purposes`: List<IdAndName>
- `restrictions`: List<TCFVendorRestriction>
- `specialFeatures`: List<IdAndName>
- `specialPurposes`: List<IdAndName>
- `showConsentToggle`: bool
- `showLegitimateInterestToggle`: bool
- `usesNonCookieAccess`: bool
- `deviceStorageDisclosureUrl`: string
- `usesCookies`: bool
- `cookieRefresh`: bool
- `dataSharedOutsideEU`: bool
- `dataRetention`: DataRetention
- `dataCategories`: List<IdAndName>
- `vendorUrls`: List<VendorUrl>
- ... (3 more fields)

---

#### TCFVendorRestriction

**Line:** 1564744

**Fields:**

- `purposeId`: int
- `restrictionType`: RestrictionType

---

#### TMP_Asset

**Line:** 1221410

**Inherits:** ScriptableObject

---

#### TMP_Character

**Line:** 1221473

**Inherits:** TMP_TextElement

---

#### TMP_ColorGradient

**Line:** 1221690

**Inherits:** ScriptableObject

**Fields:**

- `colorMode`: ColorMode
- `topLeft`: Color
- `topRight`: Color
- `bottomLeft`: Color
- `bottomRight`: Color

---

#### TMP_FontAsset

**Line:** 1222684

**Inherits:** TMP_Asset

**Fields:**

- `m_SourceFontFile`: Font
- `m_SourceFontFilePath`: string
- `m_AtlasPopulationMode`: AtlasPopulationMode
- `m_FamilyNameHashCode`: int
- `m_StyleNameHashCode`: int
- `m_IsMultiAtlasTexturesEnabled`: bool
- `m_GetFontFeatures`: bool
- `m_ClearDynamicDataOnBuild`: bool
- `m_UsedGlyphRects`: List<GlyphRect>
- `m_FreeGlyphRects`: List<GlyphRect>
- `normalStyle`: float
- `normalSpacingOffset`: float
- `boldStyle`: float
- `boldSpacing`: float
- `italicStyle`: byte
- `tabSize`: byte
- `m_fontInfo`: FaceInfo_Legacy
- `fallbackFontAssets`: List<TMP_FontAsset>
- `atlas`: Texture2D
- `m_GlyphsToRender`: List<Glyph>
- ... (3 more fields)

---

#### TMP_FontAssetUtilities

**Line:** 1223503

---

#### TMP_FontFeatureTable

**Line:** 1223760

---

#### TMP_Glyph

**Line:** 1223224

**Inherits:** TMP_TextElement_Legacy

---

#### TMP_GlyphPairAdjustmentRecord

**Line:** 1223658

---

#### TMP_InputField

**Line:** 1224042

**Inherits:** Selectable

**Fields:**

- `m_SoftKeyboard`: TouchScreenKeyboard
- `m_RectTransform`: RectTransform
- `m_TextViewport`: RectTransform
- `m_TextComponentRectMask`: RectMask2D
- `m_TextViewportRectMask`: RectMask2D
- `m_TextComponent`: TMP_Text
- `m_TextComponentRectTransform`: RectTransform
- `m_Placeholder`: Graphic
- `m_VerticalScrollbar`: Scrollbar
- `m_VerticalScrollbarEventHandler`: TMP_ScrollbarEventHandler
- `m_IsDrivenByLayoutComponents`: bool
- `m_LayoutGroup`: LayoutGroup
- `m_IScrollHandlerParent`: IScrollHandler
- `m_ScrollPosition`: float
- `m_ScrollSensitivity`: float
- `m_AsteriskChar`: char
- `m_KeyboardType`: TouchScreenKeyboardType
- `m_HideMobileInput`: bool
- `m_HideSoftKeyboard`: bool
- `m_RegexValue`: string
- ... (62 more fields)

---

#### TMP_InputValidator

**Line:** 1225041

**Inherits:** ScriptableObject

---

#### TMP_ResourceManager

**Line:** 1225517

---

#### TMP_ScrollbarEventHandler

**Line:** 1225756

**Inherits:** MonoBehaviour

**Fields:**

- `isSelected`: bool

---

#### TMP_SelectionCaret

**Line:** 1225778

**Inherits:** MaskableGraphic

---

#### TMP_Settings

**Line:** 1225809

**Inherits:** ScriptableObject

**Fields:**

- `m_TextWrappingMode`: TextWrappingModes
- `m_enableKerning`: bool
- `m_ActiveFontFeatures`: List<OTL_FeatureTag>
- `m_enableExtraPadding`: bool
- `m_enableTintAllSprites`: bool
- `m_enableParseEscapeCharacters`: bool
- `m_EnableRaycastTarget`: bool
- `m_GetFontFeaturesAtRuntime`: bool
- `m_missingGlyphCharacter`: int
- `m_ClearDynamicDataOnBuild`: bool
- `m_warningsDisabled`: bool
- `m_defaultFontAsset`: TMP_FontAsset
- `m_defaultFontAssetPath`: string
- `m_defaultFontSize`: float
- `m_defaultAutoSizeMinRatio`: float
- `m_defaultAutoSizeMaxRatio`: float
- `m_defaultTextMeshProTextContainerSize`: Vector2
- `m_defaultTextMeshProUITextContainerSize`: Vector2
- `m_autoSizeTextContainer`: bool
- `m_IsTextObjectScaleStatic`: bool
- ... (14 more fields)

---

#### TMP_Sprite

**Line:** 1226224

**Inherits:** TMP_TextElement_Legacy

**Fields:**

- `name`: string
- `hashCode`: int
- `unicode`: int
- `pivot`: Vector2
- `sprite`: Sprite

---

#### TMP_SpriteAnimator

**Line:** 1226293

**Inherits:** MonoBehaviour

**Fields:**

- `m_animations`: Dictionary<int, bool>
- `m_TextComponent`: TMP_Text

---

#### TMP_SpriteAsset

**Line:** 1226352

**Inherits:** TMP_Asset

**Fields:**

- `spriteSheet`: Texture
- `m_SpriteCharacterTable`: List<TMP_SpriteCharacter>
- `m_GlyphTable`: List<TMP_SpriteGlyph>
- `spriteInfoList`: List<TMP_Sprite>
- `fallbackSpriteAssets`: List<TMP_SpriteAsset>

---

#### TMP_SpriteGlyph

**Line:** 1226482

**Inherits:** Glyph

**Fields:**

- `sprite`: Sprite

---

#### TMP_Style

**Line:** 1226501

**Fields:**

- `m_Name`: string
- `m_HashCode`: int
- `m_OpeningDefinition`: string
- `m_ClosingDefinition`: string

---

#### TMP_StyleSheet

**Line:** 1226566

**Inherits:** ScriptableObject

**Fields:**

- `m_StyleList`: List<TMP_Style>
- `m_StyleLookupDictionary`: Dictionary<int, TMP_Style>

---

#### TMP_SubMesh

**Line:** 1226603

**Inherits:** MonoBehaviour

**Fields:**

- `m_fontAsset`: TMP_FontAsset
- `m_spriteAsset`: TMP_SpriteAsset
- `m_material`: Material
- `m_sharedMaterial`: Material
- `m_fallbackMaterial`: Material
- `m_fallbackSourceMaterial`: Material
- `m_isDefaultMaterial`: bool
- `m_padding`: float
- `m_renderer`: Renderer
- `m_meshFilter`: MeshFilter
- `m_mesh`: Mesh
- `m_TextComponent`: TextMeshPro
- `m_isRegisteredForEvents`: bool

---

#### TMP_SubMeshUI

**Line:** 1226756

**Inherits:** MaskableGraphic

**Fields:**

- `m_fontAsset`: TMP_FontAsset
- `m_spriteAsset`: TMP_SpriteAsset
- `m_material`: Material
- `m_sharedMaterial`: Material
- `m_fallbackMaterial`: Material
- `m_fallbackSourceMaterial`: Material
- `m_isDefaultMaterial`: bool
- `m_padding`: float
- `m_mesh`: Mesh
- `m_TextComponent`: TextMeshProUGUI
- `m_isRegisteredForEvents`: bool
- `m_materialDirty`: bool
- `m_materialReferenceIndex`: int
- `m_RootCanvasTransform`: Transform

---

#### TMP_Text

**Line:** 1227270

**Inherits:** MaskableGraphic

**Fields:**

- `m_text`: string
- `m_IsTextBackingStringDirty`: bool
- `m_TextPreprocessor`: ITextPreprocessor
- `m_isRightToLeft`: bool
- `m_fontAsset`: TMP_FontAsset
- `m_currentFontAsset`: TMP_FontAsset
- `m_isSDFShader`: bool
- `m_sharedMaterial`: Material
- `m_currentMaterial`: Material
- `m_currentMaterialIndex`: int
- `m_fontMaterial`: Material
- `m_isMaterialDirty`: bool
- `m_fontColor32`: Color32
- `m_fontColor`: Color
- `m_underlineColor`: Color32
- `m_strikethroughColor`: Color32
- `m_enableVertexGradient`: bool
- `m_colorMode`: ColorMode
- `m_fontColorGradient`: VertexGradient
- `m_fontColorGradientPreset`: TMP_ColorGradient
- ... (101 more fields)

---

#### TMP_TextElement

**Line:** 1228649

---

#### TMP_TextElement_Legacy

**Line:** 1228712

**Fields:**

- `id`: int
- `x`: float
- `y`: float
- `width`: float
- `height`: float
- `xOffset`: float
- `yOffset`: float
- `xAdvance`: float
- `scale`: float

---

#### TMP_TextInfo

**Line:** 1228733

**Fields:**

- `textComponent`: TMP_Text
- `characterCount`: int
- `spriteCount`: int
- `spaceCount`: int
- `wordCount`: int
- `linkCount`: int
- `lineCount`: int
- `pageCount`: int
- `materialCount`: int

---

#### TMP_TextParsingUtilities

**Line:** 1228835

---

#### TMP_UpdateManager

**Line:** 1229812

---

#### TMP_UpdateRegistry

**Line:** 1229891

**Fields:**

- `m_LayoutQueueLookup`: HashSet<int>
- `m_GraphicQueueLookup`: HashSet<int>

---

#### TaaHistory

**Line:** 908178

**Inherits:** CameraHistoryItem

**Fields:**

- `m_Descriptor`: RenderTextureDescriptor
- `m_DescKey`: Hash128

---

#### Tab

**Line:** 628144

**Inherits:** VisualElement

**Fields:**

- `selected`: Action<Tab>
- `closing`: Func<bool>
- `closed`: Action<Tab>
- `m_Label`: string
- `m_IconImage`: Background
- `m_Closeable`: bool
- `m_ContentContainer`: VisualElement
- `m_DragHandle`: VisualElement
- `m_CloseButton`: VisualElement
- `m_TabHeader`: VisualElement
- `m_TabHeaderImage`: Image
- `m_TabHeaderLabel`: Label

---

#### TabBackButtonUiView

**Line:** 732735

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### TabButton

**Line:** 720015

**Fields:**

- `Button`: UnityButton
- `SelectedHighlight`: GameObject
- `Label`: TMP_Text

---

#### TabView

**Line:** 628555

**Inherits:** VisualElement

**Fields:**

- `m_HeaderContainer`: VisualElement
- `m_ContentContainer`: VisualElement
- `m_Tabs`: List<Tab>
- `m_TabHeaders`: List<VisualElement>
- `m_ActiveTab`: Tab
- `m_ApplyingViewState`: bool
- `m_Reordering`: bool
- `activeTabChanged`: Action<Tab, Tab>
- `tabReordered`: Action<int, int>
- `tabClosed`: Action<Tab, int>
- `m_Reorderable`: bool

---

#### TableAttribute

**Line:** 1510964

**Inherits:** Attribute

**Fields:**

- `_schema`: string

---

#### TableEntry

**Line:** 1317199

**Inherits:** IMetadataCollection

---

#### TaggedSerializedInspector

**Line:** 530902

**Inherits:** TaggedWirePushParser

**Fields:**

- `_stack`: List<TaggedSerializedInspector.ObjectInfo>
- `_keyStack`: List<TaggedSerializedInspector.ObjectInfo>
- `_memberTagId`: int
- `_memberName`: string
- `_parsingKvKey`: bool
- `_valueIndex`: int
- `_currentNullablePrimitiveType`: WireDataType
- `_lastStructPayloadEnd`: int
- `_consumedUpTo`: int
- `_nextTypeSpec`: MetaSerializableType
- `_nextRawType`: Type

---

#### TaggedSerializerRoslyn

**Line:** 531183

---

#### TaggedWirePushParser

**Line:** 531924

---

#### TaiwanCalendar

**Line:** 273827

**Inherits:** Calendar

---

#### TargetComponent

**Line:** 723517

**Inherits:** IComponent

---

#### TargetException

**Line:** 266989

**Inherits:** ApplicationException

---

#### TargetFrameworkAttribute

**Line:** 224976

**Inherits:** Attribute

**Fields:**

- `_frameworkName`: string
- `_frameworkDisplayName`: string

---

#### TargetInvocationException

**Line:** 267008

**Inherits:** ApplicationException

---

#### TargetParameterCountException

**Line:** 267024

**Inherits:** ApplicationException

---

#### TargetPositionComponent

**Line:** 709206

**Inherits:** IComponent

**Fields:**

- `Value`: Vector2

---

#### Task

**Line:** 209694

**Inherits:** IThreadPoolWorkItem

**Fields:**

- `m_taskId`: int
- `m_continuationObject`: object

---

#### TaskCanceledException

**Line:** 182292

**Inherits:** OperationCanceledException

---

#### TaskCompletionSource

**Line:** 182310

---

#### TaskFactory

**Line:** 213305

---

#### TaskOnFailureListener

**Line:** 1593238

**Inherits:** AndroidJavaProxy

**Fields:**

- `OnTaskFailed`: Action<string, int>

---

#### TaskOnSuccessListener

**Line:** 1593355

**Fields:**

- `OnTaskSucceeded`: Action<TAndroidJava>

---

#### TaskQueueExecutor

**Line:** 528804

**Fields:**

- `_worker`: Task

---

#### TaskReplicator

**Line:** 191503

---

#### TaskScheduler

**Line:** 213416

**Fields:**

- `m_taskSchedulerId`: int

---

#### TaskSchedulerException

**Line:** 182855

**Inherits:** Exception

---

#### TcpClient

**Line:** 800621

**Inherits:** IDisposable

**Fields:**

- `m_ClientSocket`: Socket
- `m_Active`: bool
- `m_DataStream`: NetworkStream
- `m_Family`: AddressFamily
- `m_CleanedUp`: bool

---

#### TcpListener

**Line:** 800682

**Fields:**

- `m_ServerSocketEP`: IPEndPoint
- `m_ServerSocket`: Socket
- `m_Active`: bool
- `m_ExclusiveAddressUse`: bool

---

#### TcpMessageTransport

**Line:** 548286

**Inherits:** StreamMessageTransport

---

#### TemplateContainer

**Line:** 665174

**Inherits:** BindableElement

**Fields:**

- `m_ContentContainer`: VisualElement
- `m_TemplateSource`: VisualTreeAsset

---

#### TemplateFormatter

**Line:** 1322217

**Inherits:** FormatterBase

**Fields:**

- `m_Templates`: List<TemplateFormatter.Template>
- `m_TemplatesDict`: IDictionary<string, Format>
- `m_Formatter`: SmartFormatter

---

#### TemporaryEffectView

**Line:** 730939

**Inherits:** MonoBehaviour

---

#### TerminalError

**Line:** 1310626

**Inherits:** ErrorState

---

#### Terrain

**Line:** 1581876

**Inherits:** Behaviour

---

#### TerrainCallbacks

**Line:** 1581931

---

#### TerrainData

**Line:** 1581985

**Inherits:** Object

---

#### TerrainMap

**Line:** 1582075

**Fields:**

- `m_patchSize`: Vector3
- `m_errorCode`: TerrainMapStatusCode
- `m_terrainTiles`: Dictionary<TerrainTileCoord, Terrain>

---

#### TestError

**Line:** 686366

**Inherits:** TransientError

---

#### Text

**Line:** 1357253

**Inherits:** MaskableGraphic

**Fields:**

- `m_FontData`: FontData
- `m_Text`: string
- `m_TextCache`: TextGenerator
- `m_TextCacheForLayout`: TextGenerator
- `m_DisableFontTextureRebuiltCallback`: bool

---

#### TextAreaAttribute

**Line:** 880876

**Inherits:** PropertyAttribute

---

#### TextAsset

**Line:** 1348216

**Inherits:** ScriptableObject

---

#### TextColorGradient

**Line:** 1348283

**Inherits:** ScriptableObject

**Fields:**

- `colorMode`: ColorGradientMode
- `topLeft`: Color
- `topRight`: Color
- `bottomLeft`: Color
- `bottomRight`: Color

---

#### TextComponent

**Line:** 736227

**Inherits:** IComponent

**Fields:**

- `Value`: string

---

#### TextContainer

**Line:** 1220160

**Inherits:** UIBehaviour

**Fields:**

- `m_hasChanged`: bool
- `m_pivot`: Vector2
- `m_anchorPosition`: TextContainerAnchors
- `m_rect`: Rect
- `m_isDefaultWidth`: bool
- `m_isDefaultHeight`: bool
- `m_isAutoFitting`: bool
- `m_margins`: Vector4
- `m_rectTransform`: RectTransform
- `m_textMeshPro`: TextMeshPro

---

#### TextDataProvider

**Line:** 1437715

**Inherits:** ResourceProviderBase

---

#### TextEditor

**Line:** 1453133

**Fields:**

- `m_TextSelecting`: TextSelectingUtilities
- `keyboardOnScreen`: TouchScreenKeyboard
- `controlID`: int
- `style`: GUIStyle
- `hasHorizontalCursorPos`: bool
- `isPasswordField`: bool
- `scrollOffset`: Vector2
- `m_TextWithWhitespace`: string
- `graphicalCursorPos`: Vector2
- `lastCursorPos`: Vector2
- `previousContentSize`: Vector2

---

#### TextElement

**Line:** 1348720

**Fields:**

- `m_ElementType`: TextElementType

---

#### TextEncoder

**Line:** 1522007

---

#### TextEncoderSettings

**Line:** 1522151

**Fields:**

- `_allowedCodePointsBitmap`: AllowedBmpCodePointsBitmap

---

#### TextField

**Line:** 621386

**Inherits:** TextInputBaseField

---

#### TextFormat

**Line:** 1399153

**Inherits:** IDirectResponseSchema

---

#### TextFormatRun

**Line:** 1399285

**Inherits:** IDirectResponseSchema

---

#### TextGenerator

**Line:** 1580800

**Inherits:** IDisposable

**Fields:**

- `m_LastString`: string
- `m_LastSettings`: TextGenerationSettings
- `m_HasGenerated`: bool
- `m_LastValid`: TextGenerationError
- `m_CachedVerts`: bool
- `m_CachedCharacters`: bool
- `m_CachedLines`: bool

---

#### TextInfo

**Line:** 273910

**Inherits:** ICloneable

**Fields:**

- `m_listSeparator`: string
- `m_isReadOnly`: bool
- `m_cultureName`: string
- `m_cultureData`: CultureData
- `m_textInfoName`: string
- `m_IsAsciiCasingSameAsInvariant`: Nullable<bool>
- `customCultureName`: string

---

#### TextInputBaseField

**Line:** 622497

---

#### TextMeshPro

**Line:** 1220312

**Inherits:** TMP_Text

**Fields:**

- `OnPreRenderText`: Action<TMP_TextInfo>
- `m_hasFontAssetChanged`: bool
- `m_previousLossyScaleY`: float
- `m_renderer`: Renderer
- `m_meshFilter`: MeshFilter
- `m_isFirstAllocation`: bool
- `m_max_characters`: int
- `m_max_numberOfLines`: int
- `m_maskType`: MaskingTypes
- `m_EnvMapMatrix`: Matrix4x4
- `m_isRegisteredForEvents`: bool
- `materialIndexPairs`: Dictionary<int, int>

---

#### TextMeshProUGUI

**Line:** 1220694

**Inherits:** TMP_Text

**Fields:**

- `m_isRebuildingLayout`: bool
- `m_DelayedGraphicRebuild`: Coroutine
- `m_DelayedMaterialRebuild`: Coroutine
- `m_ShouldUpdateCulling`: bool
- `m_ClipRect`: Rect
- `m_ValidRect`: bool
- `OnPreRenderText`: Action<TMP_TextInfo>
- `m_hasFontAssetChanged`: bool
- `m_previousLossyScaleY`: float
- `m_canvasRenderer`: CanvasRenderer
- `m_canvas`: Canvas
- `m_CanvasScaleFactor`: float
- `m_isFirstAllocation`: bool
- `m_max_characters`: int
- `m_baseMaterial`: Material
- `m_isScrollRegionSet`: bool
- `m_maskOffset`: Vector4
- `m_EnvMapMatrix`: Matrix4x4
- `m_isRegisteredForEvents`: bool
- `materialIndexPairs`: Dictionary<int, int>

---

#### TextPosition

**Line:** 1399333

**Inherits:** IDirectResponseSchema

---

#### TextReader

**Line:** 468883

**Inherits:** MarshalByRefObject

---

#### TextRotation

**Line:** 1399369

**Inherits:** IDirectResponseSchema

---

#### TextSettings

**Line:** 1348350

**Inherits:** ScriptableObject

**Fields:**

- `m_Version`: string
- `m_DefaultFontAsset`: FontAsset
- `m_DefaultFontAssetPath`: string
- `m_FallbackFontAssets`: List<FontAsset>
- `m_MatchMaterialPreset`: bool
- `m_MissingCharacterUnicode`: int
- `m_ClearDynamicDataOnBuild`: bool
- `m_EnableEmojiSupport`: bool
- `m_EmojiFallbackTextAssets`: List<TextAsset>
- `m_DefaultSpriteAsset`: SpriteAsset
- `m_DefaultSpriteAssetPath`: string
- `m_FallbackSpriteAssets`: List<SpriteAsset>
- `m_MissingSpriteCharacterUnicode`: uint
- `m_DefaultStyleSheet`: TextStyleSheet
- `m_StyleSheetsResourcePath`: string
- `m_DefaultColorGradientPresetsPath`: string
- `m_UnicodeLineBreakingRules`: UnicodeLineBreakingRules
- `m_DisplayWarnings`: bool
- `m_NativeTextSettings`: IntPtr
- `m_IsNativeTextSettingsDirty`: bool

---

#### TextStyle

**Line:** 1348613

**Fields:**

- `m_Name`: string
- `m_HashCode`: int
- `m_OpeningDefinition`: string
- `m_ClosingDefinition`: string

---

#### TextStyleSheet

**Line:** 1348661

**Inherits:** ScriptableObject

**Fields:**

- `m_StyleList`: List<TextStyle>
- `m_StyleLookupDictionary`: Dictionary<int, TextStyle>
- `styleLookupLock`: object

---

#### TextToColumnsRequest

**Line:** 1399417

**Inherits:** IDirectResponseSchema

---

#### TextValueField

**Line:** 628965

**Fields:**

- `m_Dragger`: BaseFieldMouseDragger
- `m_ForceUpdateDisplay`: bool

---

#### TextValueFieldTraits

**Line:** 629460

**Fields:**

- `m_PlaceholderText`: UxmlStringAttributeDescription
- `m_HidePlaceholderOnFocus`: UxmlBoolAttributeDescription
- `m_IsReadOnly`: UxmlBoolAttributeDescription
- `m_IsDelayed`: UxmlBoolAttributeDescription

---

#### TextWriter

**Line:** 469097

**Inherits:** MarshalByRefObject

**Fields:**

- `CoreNewLineStr`: string
- `_internalFormatProvider`: IFormatProvider

---

#### TextWriterOutput

**Line:** 1323163

**Inherits:** IOutput

---

#### Texture

**Line:** 876491

**Inherits:** Object

---

#### Texture2D

**Line:** 876727

**Inherits:** Texture

---

#### Texture2DArray

**Line:** 877154

**Inherits:** Texture

---

#### Texture2DAtlas

**Line:** 823032

**Fields:**

- `m_IsAtlasTextureOwner`: bool
- `m_AtlasAllocator`: AtlasAllocator
- `m_IsGPUTextureUpToDate`: Dictionary<int, int>
- `m_TextureHashes`: Dictionary<int, int>

---

#### Texture2DParameter

**Line:** 827514

**Inherits:** VolumeParameter

---

#### Texture3D

**Line:** 877029

**Inherits:** Texture

---

#### Texture3DParameter

**Line:** 827528

**Inherits:** VolumeParameter

---

#### TextureCurve

**Line:** 825648

**Inherits:** IDisposable

**Fields:**

- `m_Loop`: bool
- `m_ZeroValue`: float
- `m_Range`: float
- `m_Curve`: AnimationCurve
- `m_LoopingCurve`: AnimationCurve
- `m_Texture`: Texture2D
- `m_IsCurveDirty`: bool
- `m_IsTextureDirty`: bool

---

#### TextureCurveParameter

**Line:** 825725

**Inherits:** VolumeParameter

---

#### TextureGradient

**Line:** 825738

**Inherits:** IDisposable

**Fields:**

- `m_Gradient`: Gradient
- `m_Texture`: Texture2D
- `m_RequestedTextureSize`: int
- `m_IsTextureDirty`: bool
- `m_Precise`: bool
- `mode`: GradientMode
- `colorSpace`: ColorSpace

---

#### TextureGradientParameter

**Line:** 825814

**Inherits:** VolumeParameter

---

#### TexturePacker_JsonArray

**Line:** 1230021

---

#### TextureParameter

**Line:** 827480

**Inherits:** VolumeParameter

**Fields:**

- `dimension`: TextureDimension

---

#### ThaiBuddhistCalendar

**Line:** 274034

**Inherits:** Calendar

---

#### ThemeColorPair

**Line:** 1399477

**Inherits:** IDirectResponseSchema

---

#### ThemeStyleSheet

**Line:** 665124

**Inherits:** StyleSheet

---

#### ThiefView

**Line:** 712519

**Inherits:** GameUnityView

**Fields:**

- `_currentPosition`: Vector2
- `_currentVelocity`: Vector2
- `_timer`: float
- `_maxTimer`: float
- `_blockMove`: bool
- `_flySequence`: Sequence
- `DeathSound`: AudioClip
- `AliveParent`: GameObject
- `DeadParent`: GameObject
- `HpBar`: GameObject

---

#### Thread

**Line:** 181001

**Inherits:** CriticalFinalizerObject

**Fields:**

- `internal_thread`: InternalThread
- `m_ThreadStartArg`: object
- `pending_exception`: object
- `m_Delegate`: MulticastDelegate
- `m_ExecutionContext`: ExecutionContext
- `m_ExecutionContextBelongsToOuterScope`: bool
- `principal`: IPrincipal
- `principal_version`: int

---

#### ThreadAbortException

**Line:** 181245

**Inherits:** SystemException

---

#### ThreadInterruptedException

**Line:** 181259

**Inherits:** SystemException

---

#### ThreadLocal

**Line:** 180192

**Fields:**

- `m_valueFactory`: Func<T>
- `m_idComplement`: int
- `m_initialized`: bool
- `m_trackAllValues`: bool

---

#### ThreadStart

**Line:** 179109

**Inherits:** MulticastDelegate

---

#### ThreadStateException

**Line:** 179140

**Inherits:** SystemException

---

#### ThreadStaticAttribute

**Line:** 57787

**Inherits:** Attribute

---

#### ThreadsFeature

**Line:** 696208

**Inherits:** Feature

---

#### TickedUiView

**Line:** 697314

**Inherits:** UiUnityView

**Fields:**

- `isTicking`: bool
- `ticker`: Coroutine

---

#### TileView

**Line:** 735120

**Inherits:** MonoBehaviour

**Fields:**

- `TileCrumbleVFXPrefab`: ParticleSystem
- `EventTrigger`: EventTrigger
- `SpriteRenderer`: SpriteRenderer

---

#### Time

**Line:** 885581

---

#### TimeCheatAction

**Line:** 1078288

**Inherits:** PlayerAction

---

#### TimeCheatContainer

**Line:** 686434

**Inherits:** AbstractCheatContainer

---

#### TimeCheatSystem

**Line:** 686721

**Inherits:** CheatSystem

---

#### TimeFormatter

**Line:** 1322265

**Inherits:** FormatterBase

**Fields:**

- `m_DefaultFormatOptions`: TimeSpanFormatOptions
- `m_DefaultTwoLetterIsoLanguageName`: string

---

#### TimeOfDay

**Line:** 1399525

**Inherits:** IDirectResponseSchema

---

#### TimeProvider

**Line:** 1581290

---

#### TimeSkipCheatAction

**Line:** 1078256

**Inherits:** PlayerAction

---

#### TimeSpanConverter

**Line:** 783070

**Inherits:** TypeConverter

---

#### TimeSpanUnits

**Line:** 1407535

**Fields:**

- `days`: double
- `months`: int
- `years`: int

---

#### TimeTextInfo

**Line:** 1321290

---

#### TimeUiView

**Line:** 721889

**Inherits:** UiUnityView

**Fields:**

- `ClockText`: TMP_Text
- `_timer`: float

---

#### TimeZone

**Line:** 57981

---

#### TimeZoneInfo

**Line:** 4239

**Inherits:** IEquatable

---

#### TimeZoneNotFoundException

**Line:** 58002

**Inherits:** Exception

---

#### Timeline

**Line:** 603388

**Fields:**

- `_version`: uint
- `_hasCheckpointModel`: bool
- `_checkpointBlob`: SerializedModel
- `_checkpointObj`: TModel
- `_checkpointRTData`: IModelRuntimeData<TModel>
- `_checkpointChecksum`: uint
- `_checkpointPosition`: JournalPosition
- `_stagedModel`: TModel
- `_stagedOps`: List<TOp>
- `_stagedPosition`: JournalPosition
- `_stagedSteps`: MetaDictionary<JournalPosition, TStep>

---

#### TimelineEntry

**Line:** 1309263

---

#### TimelineHistory

**Line:** 1309313

**Inherits:** ITimelineHistory

**Fields:**

- `_buffers`: Stack<SegmentedIOBuffer>

---

#### TimelineHistoryListener

**Line:** 603995

---

#### TimeoutController

**Line:** 1099832

**Inherits:** IDisposable

**Fields:**

- `timeoutSource`: CancellationTokenSource
- `linkedSource`: CancellationTokenSource
- `timer`: PlayerLoopTimer
- `isDisposed`: bool

---

#### TimeoutException

**Line:** 58021

**Inherits:** SystemException

---

#### Timer

**Line:** 775167

**Inherits:** Component

**Fields:**

- `interval`: double
- `enabled`: bool
- `initializing`: bool
- `delayedEnable`: bool
- `onIntervalElapsed`: ElapsedEventHandler
- `autoReset`: bool
- `synchronizingObject`: ISynchronizeInvoke
- `disposed`: bool
- `timer`: Timer
- `callback`: TimerCallback
- `cookie`: object

---

#### TimerCallback

**Line:** 182202

**Inherits:** MulticastDelegate

---

#### TimerComponent

**Line:** 696271

**Inherits:** IComponent

**Fields:**

- `Value`: double

---

#### TimerFeature

**Line:** 696393

**Inherits:** Feature

---

#### TimerModel

**Line:** 1078169

---

#### TimerProgressComponent

**Line:** 714658

**Inherits:** IComponent

**Fields:**

- `Value`: double

---

#### TimerStateComponent

**Line:** 696307

**Inherits:** IComponent

**Fields:**

- `Value`: TimerState

---

#### TimerStateEventSystem

**Line:** 702652

**Inherits:** ReactiveSystem

---

#### TimerStateListenerComponent

**Line:** 700090

**Inherits:** IComponent

**Fields:**

- `value`: List<ITimerStateListener>

---

#### TimerSystem

**Line:** 696369

**Inherits:** IExecuteSystem

---

#### TimerUiView

**Line:** 735716

**Inherits:** MonoBehaviour

**Fields:**

- `TimerText`: TMP_Text
- `TimerParent`: GameObject
- `_node`: GameEntity
- `_state`: TimerState
- `_remainingSeconds`: int

---

#### TimersDescriptionAttribute

**Line:** 775258

**Inherits:** DescriptionAttribute

**Fields:**

- `replaced`: bool

---

#### TimestampAttribute

**Line:** 1510070

**Inherits:** Attribute

---

#### TinyBenchmark

**Line:** 524711

---

#### TitleSettings

**Line:** 1565209

**Fields:**

- `alignment`: SectionAlignment
- `textSize`: float
- `textColor`: string

---

#### TlsException

**Line:** 1449197

**Inherits:** Exception

**Fields:**

- `alert`: Alert

---

#### TlsMessageTransport

**Line:** 548379

**Inherits:** TcpMessageTransport

---

#### ToastBarUiView

**Line:** 737535

**Inherits:** UiUnityView

**Fields:**

- `Visual`: ToastBarVisual
- `_sequence`: Sequence

---

#### ToastBarUiViewInitializeSystem

**Line:** 737520

**Inherits:** IInitializeSystem

---

#### ToastBarVisual

**Line:** 737557

**Inherits:** MonoBehaviour

**Fields:**

- `Background`: Image
- `BackgroundOutline`: Image
- `TextParent`: GameObject
- `Text`: TMP_Text
- `_backGroundAlpha`: float

---

#### Toggle

**Line:** 1357465

**Inherits:** Selectable

**Fields:**

- `graphic`: Graphic
- `m_Group`: ToggleGroup
- `m_IsOn`: bool

---

#### ToggleButtonGroup

**Line:** 629614

**Inherits:** BaseField

**Fields:**

- `m_ButtonGroupContainer`: VisualElement
- `m_Buttons`: List<Button>
- `m_EmptyLabel`: VisualElement
- `m_IsMultipleSelection`: bool
- `m_AllowEmptySelection`: bool

---

#### ToggleGroup

**Line:** 1357575

**Inherits:** UIBehaviour

**Fields:**

- `m_AllowSwitchOff`: bool
- `m_Toggles`: List<Toggle>

---

#### ToggleStyleSettings

**Line:** 1564341

**Fields:**

- `activeBackgroundColor`: string
- `inactiveBackgroundColor`: string
- `disabledBackgroundColor`: string
- `activeThumbColor`: string
- `inactiveThumbColor`: string
- `disabledThumbColor`: string

---

#### TokenErrorResponse

**Line:** 1374599

---

#### TokenPacksCreationSystem

**Line:** 734554

**Inherits:** IInitSystem

**Fields:**

- `_createdTokenPacks`: List<ResourcePackUiView>

---

#### TokenRequest

**Line:** 1375693

---

#### TokenResponse

**Line:** 1374676

---

#### TokenResponseException

**Line:** 1374839

**Inherits:** Exception

---

#### TokensChangeMessage

**Line:** 711823

**Inherits:** CurrencyChangeMessage

---

#### Tonemapping

**Line:** 909743

**Inherits:** VolumeComponent

**Fields:**

- `mode`: TonemappingModeParameter
- `neutralHDRRangeReductionMode`: NeutralRangeReductionModeParameter
- `acesPreset`: HDRACESPresetParameter
- `hueShiftAmount`: ClampedFloatParameter
- `detectPaperWhite`: BoolParameter
- `paperWhite`: ClampedFloatParameter
- `detectBrightnessLimits`: BoolParameter
- `minNits`: ClampedFloatParameter
- `maxNits`: ClampedFloatParameter

---

#### TonemappingModeParameter

**Line:** 909781

**Inherits:** VolumeParameter

---

#### ToolboxItemAttribute

**Line:** 781585

**Inherits:** Attribute

**Fields:**

- `_toolboxItemTypeName`: string

---

#### TooltipAttribute

**Line:** 880794

**Inherits:** PropertyAttribute

---

#### TooltipEvent

**Line:** 639016

**Inherits:** EventBase

---

#### TouchInputModule

**Line:** 1360835

**Inherits:** PointerInputModule

**Fields:**

- `m_LastMousePosition`: Vector2
- `m_MousePosition`: Vector2
- `m_InputPointerEvent`: PointerEventData
- `m_ForceModuleActive`: bool

---

#### TouchScreenKeyboard

**Line:** 885699

---

#### Trace

**Line:** 777471

---

#### TraceEventCache

**Line:** 777494

**Fields:**

- `timeStamp`: long
- `dateTime`: DateTime
- `stackTrace`: string

---

#### TraceFilter

**Line:** 777567

---

#### TraceListener

**Line:** 777630

**Inherits:** MarshalByRefObject

**Fields:**

- `indentLevel`: int
- `indentSize`: int
- `traceOptions`: TraceOptions
- `needIndent`: bool
- `listenerName`: string
- `filter`: TraceFilter

---

#### TraceListenerCollection

**Line:** 777710

**Inherits:** IList

**Fields:**

- `list`: ArrayList

---

#### TraceSwitch

**Line:** 777800

**Inherits:** Switch

---

#### TrackedLayoutGroup

**Line:** 1329583

**Inherits:** JsonSerializerTrackedObject

---

#### TrackedMeshFilter

**Line:** 1329262

**Inherits:** TrackedObject

**Fields:**

- `m_CurrentOperation`: AsyncOperationHandle<Mesh>

---

#### TrackedMonoBehaviourObject

**Line:** 1329289

**Inherits:** JsonSerializerTrackedObject

**Fields:**

- `m_Changed`: UnityEvent

---

#### TrackedObject

**Line:** 1329326

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `m_Target`: Object

---

#### TrackedProperty

**Line:** 1328072

**Fields:**

- `m_PropertyPath`: string

---

#### TrackedRectTransform

**Line:** 1329402

**Inherits:** TrackedTransform

**Fields:**

- `m_AnchorPosToApply`: Vector3
- `m_AnchorMinToApply`: Vector2
- `m_AnchorMaxToApply`: Vector2
- `m_PivotToApply`: Vector2
- `m_SizeDeltaToApply`: Vector2

---

#### TrackedReference

**Line:** 883853

---

#### TrackedTransform

**Line:** 1329486

**Inherits:** TrackedObject

**Fields:**

- `m_PositionToApply`: Vector3
- `m_RotationToApply`: Quaternion
- `m_ScaleToApply`: Vector3

---

#### TrackedUGuiGraphic

**Line:** 1329553

**Inherits:** JsonSerializerTrackedObject

---

#### TrackingEventParams

**Line:** 696542

---

#### TrackingEvents

**Line:** 696529

---

#### TrackingService

**Line:** 696599

**Inherits:** ITracker

---

#### TrackingServiceExtensions

**Line:** 696623

---

#### TrackingServices

**Line:** 221924

---

#### TrailRenderer

**Line:** 873484

**Inherits:** Renderer

---

#### TransactionPlanningFailure

**Line:** 569986

**Inherits:** Exception

---

#### TransferCodingHeaderValue

**Line:** 1491276

**Inherits:** ICloneable

---

#### TransferCodingWithQualityHeaderValue

**Line:** 1491320

**Inherits:** TransferCodingHeaderValue

---

#### Transform

**Line:** 886170

**Inherits:** Component

---

#### TransientAttribute

**Line:** 600942

**Inherits:** MetaMemberFlagAttribute

---

#### TransientError

**Line:** 1310276

**Inherits:** ErrorState

---

#### TransitionCancelEvent

**Line:** 639291

**Inherits:** TransitionEventBase

---

#### TransitionEndEvent

**Line:** 639259

**Inherits:** TransitionEventBase

---

#### TransitionEventBase

**Line:** 639107

---

#### TransitionRunEvent

**Line:** 639195

**Inherits:** TransitionEventBase

---

#### TransitionStartEvent

**Line:** 639227

**Inherits:** TransitionEventBase

---

#### TranslationId

**Line:** 561642

**Inherits:** StringId

---

#### TransportContext

**Line:** 792044

---

#### TransportFailedException

**Line:** 1482958

**Inherits:** Exception

---

#### TransportQosMonitor

**Line:** 551308

**Fields:**

- `_isWriteHealthy`: bool
- `_isReadHealthy`: bool
- `_hasHandshakedConnection`: bool
- `_hasTransport`: bool
- `_lastSentSessionResumptionPingId`: int
- `_lastReceivedSessionResumptionPongId`: int
- `_sessionResumptionPingIdCounter`: int
- `_lastSessionResumptionPingSentAt`: DateTime
- `_hasBeenHealthy`: bool
- `_externalSources`: HashSet<TransportQosMonitor.IWarningSource>

---

#### TreeConnector

**Line:** 735735

**Inherits:** MonoBehaviour

**Fields:**

- `RectTransform`: RectTransform
- `LineThickness`: float

---

#### TreeView

**Line:** 629791

**Inherits:** BaseTreeView

**Fields:**

- `m_MakeItem`: Func<VisualElement>
- `m_TemplateMakeItem`: Func<VisualElement>
- `m_ItemTemplate`: VisualTreeAsset
- `m_BindItem`: Action<VisualElement, int>
- `m_UnbindItem`: Action<VisualElement, int>
- `m_DestroyItem`: Action<VisualElement>

---

#### TreeViewController

**Line:** 611337

**Inherits:** BaseTreeViewController

---

#### TreeViewExpansionChangedArgs

**Line:** 615142

---

#### TreemapChartColorScale

**Line:** 1399597

**Inherits:** IDirectResponseSchema

---

#### TreemapChartSpec

**Line:** 1399717

**Inherits:** IDirectResponseSchema

---

#### TriggerRoot

**Line:** 1444089

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `Canvas`: Canvas
- `TapHoldButton`: LongPressButton
- `TriggerTransform`: RectTransform
- `ErrorNotifier`: ErrorNotifier
- `TripleTapButton`: MultiTapButton

---

#### TrimWhitespaceRequest

**Line:** 1399897

**Inherits:** IDirectResponseSchema

---

#### TrimWhitespaceResponse

**Line:** 1399933

**Inherits:** IDirectResponseSchema

---

#### TripleDES

**Line:** 219506

**Inherits:** SymmetricAlgorithm

---

#### TripleDESCryptoServiceProvider

**Line:** 219544

**Inherits:** TripleDES

---

#### TryBuyComponent

**Line:** 711699

**Inherits:** IComponent

---

#### TryExpression

**Line:** 1289821

**Inherits:** Expression

---

#### Tuple

**Line:** 58659

---

#### TupleElementNamesAttribute

**Line:** 234441

**Inherits:** Attribute

---

#### Tween

**Line:** 1428395

**Inherits:** ABSSequentiable

**Fields:**

- `timeScale`: float
- `isBackwards`: bool
- `id`: object
- `stringId`: string
- `intId`: int
- `target`: object
- `onPlay`: TweenCallback
- `onPause`: TweenCallback
- `onRewind`: TweenCallback
- `onUpdate`: TweenCallback
- `onStepComplete`: TweenCallback
- `onComplete`: TweenCallback
- `onKill`: TweenCallback
- `onWaypointChange`: TweenCallback<int>
- `easeOvershootOrAmplitude`: float
- `easePeriod`: float
- `debugTargetId`: string

---

#### TweenCallback

**Line:** 1424967

---

#### TweenParams

**Line:** 1427772

---

#### Tweener

**Line:** 1428541

**Inherits:** Tween

---

#### TweenerCore

**Line:** 1431709

**Fields:**

- `startValue`: T2
- `endValue`: T2
- `changeValue`: T2
- `plugOptions`: TPlugOptions
- `getter`: DOGetter<T1>
- `setter`: DOSetter<T1>

---

#### TwoPaneSplitView

**Line:** 629952

**Inherits:** VisualElement

**Fields:**

- `m_LeftPane`: VisualElement
- `m_RightPane`: VisualElement
- `m_FixedPane`: VisualElement
- `m_FlexedPane`: VisualElement
- `m_FixedPaneDimension`: float
- `m_DragLine`: VisualElement
- `m_DragLineAnchor`: VisualElement
- `m_CollapseMode`: bool
- `m_PendingCollapseToExecute`: bool
- `m_CollapsedChildIndex`: int
- `m_Content`: VisualElement
- `m_Orientation`: TwoPaneSplitViewOrientation
- `m_FixedPaneIndex`: int
- `m_FixedPaneInitialDimension`: float

---

#### Type

**Line:** 58935

**Inherits:** MemberInfo

---

#### Type1Message

**Line:** 1448403

**Inherits:** MessageBase

**Fields:**

- `_host`: string
- `_domain`: string

---

#### Type2Message

**Line:** 1448432

**Inherits:** MessageBase

**Fields:**

- `_targetName`: string

---

#### Type3Message

**Line:** 1448469

**Inherits:** MessageBase

**Fields:**

- `_level`: NtlmAuthLevel
- `_host`: string
- `_domain`: string
- `_username`: string
- `_password`: string
- `_type2`: Type2Message

---

#### TypeAccessException

**Line:** 59493

**Inherits:** TypeLoadException

---

#### TypeBinaryExpression

**Line:** 1289880

**Inherits:** Expression

---

#### TypeBuilder

**Line:** 270200

**Inherits:** TypeInfo

---

#### TypeConverter

**Line:** 1472447

---

#### TypeConverterAttribute

**Line:** 783092

**Inherits:** Attribute

---

#### TypeDelegator

**Line:** 267079

**Inherits:** TypeInfo

**Fields:**

- `typeImpl`: Type

---

#### TypeDescriptionProvider

**Line:** 783137

---

#### TypeDescriptionProviderAttribute

**Line:** 783181

**Inherits:** Attribute

---

#### TypeDescriptor

**Line:** 784534

---

#### TypeEntry

**Line:** 221779

**Fields:**

- `assembly_name`: string
- `type_name`: string

---

#### TypeFilter

**Line:** 267242

**Inherits:** MulticastDelegate

---

#### TypeInferenceRuleAttribute

**Line:** 834948

**Inherits:** Attribute

---

#### TypeInfo

**Line:** 267254

**Inherits:** Type

---

#### TypeInitializationException

**Line:** 59531

**Inherits:** SystemException

**Fields:**

- `_typeName`: string

---

#### TypeListConverter

**Line:** 783201

**Inherits:** TypeConverter

---

#### TypeLoadException

**Line:** 174312

**Inherits:** SystemException

**Fields:**

- `ClassName`: string
- `AssemblyName`: string
- `MessageArg`: string

---

#### TypedPlayerPropertyId

**Line:** 541585

---

#### TypedUxmlAttributeDescription

**Line:** 668557

---

#### TzdbDateTimeZoneSource

**Line:** 1149566

**Inherits:** IDateTimeZoneSource

---

#### TzdbZone1970Location

**Line:** 1149716

---

#### TzdbZoneLocation

**Line:** 1149769

---

#### UCConstants

**Line:** 1565496

---

#### UDP

**Line:** 1404906

---

#### UIBehaviour

**Line:** 1361115

**Inherits:** MonoBehaviour

---

#### UIDocument

**Line:** 640691

**Inherits:** MonoBehaviour

**Fields:**

- `m_PanelSettings`: PanelSettings
- `m_PreviousPanelSettings`: PanelSettings
- `m_ParentUI`: UIDocument
- `m_ChildrenContent`: UIDocumentList
- `m_ChildrenContentCopy`: List<UIDocument>
- `sourceAsset`: VisualTreeAsset
- `m_RootVisualElement`: VisualElement
- `m_RuntimePanel`: RuntimePanel
- `m_FirstChildInsertIndex`: int
- `m_SortingOrder`: float
- `m_WorldSpaceWidth`: float
- `m_WorldSpaceHeight`: float
- `m_RootHasWorldTransform`: bool

---

#### UIElementsRuntimeUtility

**Line:** 667093

---

#### UIFoldout

**Line:** 834809

**Inherits:** Toggle

**Fields:**

- `content`: GameObject
- `arrowOpened`: GameObject
- `arrowClosed`: GameObject

---

#### UIHintAttribute

**Line:** 1510149

**Inherits:** Attribute

---

#### UIParticle

**Line:** 1563457

**Inherits:** MaskableGraphic

**Fields:**

- `m_IgnoreCanvasScaler`: bool
- `m_Scale3D`: Vector3
- `m_Particles`: List<ParticleSystem>
- `m_GroupId`: int
- `m_GroupMaxId`: int
- `m_UseCustomView`: bool
- `m_CustomViewSize`: float
- `_bakeCamera`: Camera
- `_canvas`: Canvas
- `_groupId`: int
- `_isScaleStored`: bool
- `_storedScale`: Vector3
- `_tracker`: DrivenRectTransformTracker

---

#### UIParticleAttractor

**Line:** 1563782

**Inherits:** MonoBehaviour

**Fields:**

- `m_ParticleSystem`: ParticleSystem
- `m_DestinationRadius`: float
- `m_DelayRate`: float
- `m_MaxSpeed`: float
- `m_OnAttracted`: UnityEvent
- `_uiParticle`: UIParticle

---

#### UIRenderer

**Line:** 641665

**Inherits:** Renderer

---

#### UInt128Converter

**Line:** 561206

**Inherits:** JsonConverter

---

#### UInt16Converter

**Line:** 783235

**Inherits:** BaseNumberConverter

---

#### UInt32Converter

**Line:** 783259

**Inherits:** BaseNumberConverter

---

#### UInt64Converter

**Line:** 783283

**Inherits:** BaseNumberConverter

---

#### UIntTrackedProperty

**Line:** 1328901

**Inherits:** TrackedProperty

---

#### UIntVariable

**Line:** 1324589

**Inherits:** Variable

---

#### ULongTrackedProperty

**Line:** 1328921

**Inherits:** TrackedProperty

---

#### ULongVariable

**Line:** 1324653

**Inherits:** Variable

---

#### URPDefaultVolumeProfileSettings

**Line:** 913908

**Inherits:** IDefaultVolumeProfileSettings

**Fields:**

- `m_VolumeProfile`: VolumeProfile

---

#### URPShaderStrippingSetting

**Line:** 913949

**Inherits:** IRenderPipelineGraphicsSettings

**Fields:**

- `m_StripUnusedPostProcessingVariants`: bool
- `m_StripUnusedVariants`: bool
- `m_StripScreenCoordOverrideVariants`: bool

---

#### UShortTrackedProperty

**Line:** 1328881

**Inherits:** TrackedProperty

---

#### UShortVariable

**Line:** 1324525

**Inherits:** Variable

---

#### UTF32Encoding

**Line:** 215343

**Inherits:** Encoding

**Fields:**

- `_emitUTF32ByteOrderMark`: bool
- `_isThrowException`: bool
- `_bigEndian`: bool

---

#### UTF7Encoding

**Line:** 215563

**Inherits:** Encoding

**Fields:**

- `_allowOptionals`: bool

---

#### UTF8Encoding

**Line:** 215718

**Inherits:** Encoding

**Fields:**

- `_isThrowException`: bool

---

#### UiAnyDestroyedEventSystem

**Line:** 702673

**Inherits:** ReactiveSystem

---

#### UiAnyDestroyedListenerComponent

**Line:** 700103

**Inherits:** IComponent

**Fields:**

- `value`: List<IUiAnyDestroyedListener>

---

#### UiAttribute

**Line:** 704820

**Inherits:** ContextAttribute

---

#### UiCheatSystem

**Line:** 686736

**Inherits:** CheatSystem

---

#### UiContext

**Line:** 692086

**Inherits:** Context

**Fields:**

- `_nextId`: long

---

#### UiDestroySystem

**Line:** 686859

**Inherits:** ReactiveSystem

---

#### UiDestroyedEventSystem

**Line:** 702696

**Inherits:** ReactiveSystem

---

#### UiDestroyedListenerComponent

**Line:** 700116

**Inherits:** IComponent

**Fields:**

- `value`: List<IUiDestroyedListener>

---

#### UiEntity

**Line:** 691308

**Inherits:** Entity

---

#### UiEntityRef

**Line:** 691278

**Inherits:** EntityRef

---

#### UiEntityRefComponent

**Line:** 687708

**Inherits:** IComponent

**Fields:**

- `Value`: UiEntityRef

---

#### UiEventSystems

**Line:** 702759

**Inherits:** Feature

---

#### UiFeature

**Line:** 737192

**Inherits:** Feature

---

#### UiGameRefCleanupSystem

**Line:** 737055

**Inherits:** ReactiveSystem

---

#### UiHover

**Line:** 721924

**Inherits:** MonoBehaviour

**Fields:**

- `Amplitude`: float
- `Frequency`: float
- `_rectTransform`: RectTransform

---

#### UiMatcher

**Line:** 704580

---

#### UiPulse

**Line:** 721944

**Inherits:** MonoBehaviour

**Fields:**

- `Amplitude`: float
- `Frequency`: float
- `_rectTransform`: RectTransform

---

#### UiRefCleanupSystem

**Line:** 737076

**Inherits:** ReactiveSystem

---

#### UiUnityView

**Line:** 697357

**Inherits:** UnityView

---

#### UiUnityViewProxy

**Line:** 697368

**Inherits:** UnityViewProxy

---

#### UintPlugin

**Line:** 1429464

**Inherits:** ABSTweenPlugin

---

#### UlongPlugin

**Line:** 1429185

**Inherits:** ABSTweenPlugin

---

#### UmAlQuraCalendar

**Line:** 274124

**Inherits:** Calendar

---

#### UnaryExpression

**Line:** 1289925

**Inherits:** Expression

---

#### UnaryOperationBinder

**Line:** 1300950

**Inherits:** DynamicMetaObjectBinder

---

#### UnassignedReferenceException

**Line:** 883738

**Inherits:** Exception

---

#### UnauthorizedAccessException

**Line:** 59898

**Inherits:** SystemException

---

#### UnauthorizedException

**Line:** 685292

**Inherits:** Exception

---

#### UnbanUserRequest

**Line:** 1528581

**Inherits:** IEquatable

---

#### UnboundedChannelOptions

**Line:** 1524696

**Inherits:** ChannelOptions

---

#### UnequippedSetPieceMessage

**Line:** 728790

**Inherits:** IMessage

---

#### UnhandledExceptionEventArgs

**Line:** 59917

**Inherits:** EventArgs

**Fields:**

- `_exception`: object
- `_isTerminating`: bool

---

#### UnhandledExceptionEventHandler

**Line:** 59941

**Inherits:** MulticastDelegate

---

#### UnhandledModelExecutionException

**Line:** 604248

**Inherits:** Exception

---

#### UniClipboard

**Line:** 1596031

---

#### UniTaskCompletionSource

**Line:** 1122955

**Fields:**

- `cancellationToken`: CancellationToken
- `result`: T
- `exception`: ExceptionHolder
- `gate`: object
- `singleContinuation`: Action<object>
- `singleState`: object
- `intStatus`: int
- `handled`: bool

---

#### UniTaskSynchronizationContext

**Line:** 1125150

**Inherits:** SynchronizationContext

---

#### UnicodeEncoding

**Line:** 215863

**Inherits:** Encoding

---

#### UnicodeLineBreakingRules

**Line:** 1351393

**Fields:**

- `m_UnicodeLineBreakingRules`: TextAsset
- `m_LeadingCharacters`: TextAsset
- `m_FollowingCharacters`: TextAsset
- `m_UseModernHangulLineBreakingRules`: bool
- `m_LeadingCharactersLookup`: HashSet<uint>
- `m_FollowingCharactersLookup`: HashSet<uint>

---

#### UnicodeRange

**Line:** 1520648

---

#### UnifiedReceipt

**Line:** 1531546

**Fields:**

- `Payload`: string
- `Store`: string
- `TransactionID`: string

---

#### UniqueAttribute

**Line:** 1597508

**Inherits:** Attribute

---

#### UniqueConstraint

**Line:** 1089037

**Inherits:** Constraint

**Fields:**

- `_key`: DataKey
- `_constraintIndex`: Index

---

#### UniqueStat

**Line:** 1076458

**Inherits:** IEquatable

---

#### UniqueViewComponent

**Line:** 736240

**Inherits:** IComponent

---

#### UnitAnimationView

**Line:** 710857

**Inherits:** GameUnityView

**Fields:**

- `Animator`: Animator
- `_attackSpeed`: float

---

#### UnitColorManager

**Line:** 710885

---

#### UnitComponent

**Line:** 710616

**Inherits:** IComponent

---

#### UnitCurrentEquipmentVisual

**Line:** 710917

**Inherits:** UnitEquipmentVisual

**Fields:**

- `SkinEquipmentVisual`: SkinEquipmentVisual

---

#### UnitDeathEffectsView

**Line:** 710932

**Inherits:** GameUnityView

**Fields:**

- `DeathEffect`: ParticleSystem
- `GroundSplatter`: ParticleSystem
- `_disableGroundPlatter`: bool
- `_offset`: Vector2

---

#### UnitEntity

**Line:** 1057581

**Inherits:** BasicEntity

**Fields:**

- `Position`: F64Vec2
- `CenterOfMass`: F64Vec2
- `UnitOffSet`: F64Vec2
- `Velocity`: F64Vec2
- `IsAlly`: bool
- `IsPlayer`: bool
- `AttackDuration`: FD6
- `WindUpDuration`: FD6
- `AttackTimer`: FD6
- `State`: CombatState
- `Sign`: int
- `HelmetId`: ItemId
- `ArmourId`: ItemId
- `WeaponId`: ItemId
- `TargetPos`: F64Vec2
- `LookDirection`: F64Vec2
- `IsSolid`: bool
- `Radius`: F64
- `AttackRange`: F64
- `UnitProjectileConfig`: UnitProjectileConfig
- ... (15 more fields)

---

#### UnitEntityReactiveModel

**Line:** 709447

**Inherits:** ReactiveModel

---

#### UnitEquipmentView

**Line:** 710953

**Inherits:** GameUnityView

**Fields:**

- `Visual`: UnitEquipmentVisual
- `SkinVisual`: SkinEquipmentVisual

---

#### UnitEquipmentVisual

**Line:** 710990

**Inherits:** MonoBehaviour

**Fields:**

- `Rig`: CharacterRig
- `_secondaryWeapon`: EquipmentItem
- `_hitTween`: Tweener
- `_attackSfx`: AttackSfx
- `VisibleItems`: Dictionary<ItemType, EquipmentItem>

---

#### UnitIdComponent

**Line:** 710625

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### UnitNameView

**Line:** 711038

**Inherits:** GameUnityView

**Fields:**

- `Name`: TMP_Text
- `_hasName`: bool

---

#### UnitOffsetMath

**Line:** 710703

**Inherits:** MonoBehaviour

**Fields:**

- `Rig`: Transform
- `Hand`: Transform
- `WeaponTip`: Transform
- `Target`: Transform
- `Rot`: Transform

---

#### UnitSkinColorView

**Line:** 711057

**Inherits:** GameUnityView

**Fields:**

- `BodyColorSprites`: List<SpriteRenderer>
- `SkinColorSprites`: List<SpriteRenderer>

---

#### UnitView

**Line:** 711076

**Inherits:** GameUnityView

**Fields:**

- `ColliderTransform`: Transform
- `_timer`: float
- `_currentPosition`: Vector2
- `_currentVelocity`: Vector2

---

#### UnityAction

**Line:** 888227

---

#### UnityButton

**Line:** 736072

**Inherits:** MonoBehaviour

**Fields:**

- `_onClick`: Action
- `_isInteractable`: bool
- `_isPressed`: bool
- `_ignorePointerClick`: bool

---

#### UnityCredentialService

**Line:** 1309594

**Inherits:** ISessionCredentialService

**Fields:**

- `Log`: LogChannel
- `_guestCredentialsStore`: CredentialsStore
- `_guestCredentials`: Nullable<ISessionCredentialService.GuestCredentials>
- `_socialCredentialsProviders`: List<ISocialCredentialsProvider>

---

#### UnityEvent

**Line:** 888250

---

#### UnityEventAudioClip

**Line:** 1326836

**Inherits:** UnityEvent

---

#### UnityEventBase

**Line:** 887629

**Inherits:** ISerializationCallbackReceiver

**Fields:**

- `m_Calls`: InvokableCallList
- `m_PersistentCalls`: PersistentCallGroup
- `m_CallsDirty`: bool

---

#### UnityEventGameObject

**Line:** 1326846

**Inherits:** UnityEvent

---

#### UnityEventHandlerAsyncEnumerable

**Line:** 1127541

---

#### UnityEventSprite

**Line:** 1326856

**Inherits:** UnityEvent

---

#### UnityEventString

**Line:** 1326866

**Inherits:** UnityEvent

---

#### UnityEventTexture

**Line:** 1326876

**Inherits:** UnityEvent

---

#### UnityException

**Line:** 883722

**Inherits:** Exception

---

#### UnityGameEngineIntegration

**Line:** 1305018

**Inherits:** IGameEngineIntegration

---

#### UnityLogger

**Line:** 1309675

---

#### UnityObjectProperty

**Line:** 1329017

**Inherits:** ITrackedPropertyValue

**Fields:**

- `m_PropertyPath`: string
- `m_TypeString`: string
- `m_VariantData`: List<UnityObjectProperty.LocaleIdentifierValuePair>

---

#### UnityPlatformInfo

**Line:** 574331

**Fields:**

- `_nextReachabilityUpdateAt`: DateTime

---

#### UnityPurchasing

**Line:** 1531594

---

#### UnityReceipt

**Line:** 1313697

**Fields:**

- `Store`: string
- `TransactionID`: string
- `Payload`: string
- `IsMetaplayFakeStore`: bool

---

#### UnitySystemInfo

**Line:** 574058

**Fields:**

- `_nextBatteryUpdateAt`: DateTime

---

#### UnityTls

**Line:** 771885

---

#### UnityToggleButton

**Line:** 736141

**Inherits:** UnityButton

**Fields:**

- `HasClickSfx`: bool
- `ToggleObject`: GameObject

---

#### UnityUiElement

**Line:** 737511

**Inherits:** Image

---

#### UnityView

**Line:** 697383

**Fields:**

- `_contexts`: Contexts
- `_linkedEntity`: T

---

#### UnityViewProxy

**Line:** 697434

**Fields:**

- `Contexts`: Contexts
- `LinkedEntity`: T
- `_destroyGameObject`: bool
- `_gameObjectName`: string

---

#### UnityWebRequest

**Line:** 1566269

**Inherits:** IDisposable

---

#### UnityWebRequestAsyncOperation

**Line:** 1566162

**Inherits:** AsyncOperation

---

#### UnityWebRequestException

**Line:** 1127896

**Inherits:** Exception

**Fields:**

- `msg`: string

---

#### UnityWebRequestResult

**Line:** 1436454

---

#### UnityWebRequestUtilities

**Line:** 1436426

---

#### UniversalAdditionalCameraData

**Line:** 915055

**Inherits:** MonoBehaviour

**Fields:**

- `m_RenderShadows`: bool
- `m_RequiresDepthTextureOption`: CameraOverrideOption
- `m_RequiresOpaqueTextureOption`: CameraOverrideOption
- `m_CameraType`: CameraRenderType
- `m_Cameras`: List<Camera>
- `m_RendererIndex`: int
- `m_VolumeLayerMask`: LayerMask
- `m_VolumeTrigger`: Transform
- `m_VolumeFrameworkUpdateModeOption`: VolumeFrameworkUpdateMode
- `m_RenderPostProcessing`: bool
- `m_Antialiasing`: AntialiasingMode
- `m_AntialiasingQuality`: AntialiasingQuality
- `m_StopNaN`: bool
- `m_Dithering`: bool
- `m_ClearDepth`: bool
- `m_AllowXRRendering`: bool
- `m_AllowHDROutput`: bool
- `m_UseScreenCoordOverride`: bool
- `m_ScreenSizeOverride`: Vector4
- `m_ScreenCoordScaleBias`: Vector4
- ... (6 more fields)

---

#### UniversalAdditionalLightData

**Line:** 915382

**Inherits:** MonoBehaviour

**Fields:**

- `m_Version`: int
- `m_UsePipelineSettings`: bool
- `m_Light`: Light
- `m_AdditionalLightsShadowResolutionTier`: int
- `m_LightLayerMask`: LightLayerEnum
- `m_RenderingLayers`: uint
- `m_CustomShadowLayers`: bool
- `m_ShadowLayerMask`: LightLayerEnum
- `m_ShadowRenderingLayers`: uint
- `m_LightCookieSize`: Vector2
- `m_LightCookieOffset`: Vector2
- `m_SoftShadowQuality`: SoftShadowQuality

---

#### UniversalCameraData

**Line:** 907406

**Inherits:** ContextItem

**Fields:**

- `m_ViewMatrix`: Matrix4x4
- `m_ProjectionMatrix`: Matrix4x4
- `m_JitterMatrix`: Matrix4x4
- `camera`: Camera
- `renderType`: CameraRenderType
- `targetTexture`: RenderTexture
- `cameraTargetDescriptor`: RenderTextureDescriptor
- `renderScale`: float
- `clearDepth`: bool
- `cameraType`: CameraType
- `isDefaultViewport`: bool
- `isHdrEnabled`: bool
- `allowHDROutput`: bool
- `isAlphaOutputEnabled`: bool
- `requiresDepthTexture`: bool
- `requiresOpaqueTexture`: bool
- `postProcessingRequiresDepthTexture`: bool
- `xrRendering`: bool
- `defaultOpaqueSortFlags`: SortingCriteria
- `maxShadowDistance`: float
- ... (12 more fields)

---

#### UniversalCameraHistory

**Line:** 915554

**Inherits:** ICameraHistoryReadAccess

**Fields:**

- `m_Version`: int
- `m_HistoryTextures`: BufferedRTHandleSystem

---

#### UniversalLightData

**Line:** 907597

**Inherits:** ContextItem

**Fields:**

- `mainLightIndex`: int
- `additionalLightsCount`: int
- `maxPerObjectAdditionalLightsCount`: int
- `visibleLights`: NativeArray<VisibleLight>
- `shadeAdditionalLightsPerVertex`: bool
- `supportsMixedLighting`: bool
- `reflectionProbeBoxProjection`: bool
- `reflectionProbeBlending`: bool
- `supportsLightLayers`: bool
- `supportsAdditionalLights`: bool

---

#### UniversalPostProcessingData

**Line:** 907621

**Inherits:** ContextItem

**Fields:**

- `isEnabled`: bool
- `gradingMode`: ColorGradingMode
- `lutSize`: int
- `useFastSRGBLinearConversion`: bool
- `supportScreenSpaceLensFlare`: bool
- `supportDataDrivenLensFlare`: bool

---

#### UniversalRenderPipeline

**Line:** 916564

**Inherits:** RenderPipeline

**Fields:**

- `m_GlobalSettings`: UniversalRenderPipelineGlobalSettings
- `cameraComparison`: Comparison<Camera>

---

#### UniversalRenderPipelineAsset

**Line:** 900677

**Inherits:** RenderPipelineAsset

**Fields:**

- `k_AssetVersion`: int
- `k_AssetPreviousVersion`: int
- `m_RendererType`: RendererType
- `m_RequireDepthTexture`: bool
- `m_RequireOpaqueTexture`: bool
- `m_OpaqueDownsampling`: Downsampling
- `m_SupportsTerrainHoles`: bool
- `m_SupportsHDR`: bool
- `m_HDRColorBufferPrecision`: HDRColorBufferPrecision
- `m_MSAA`: MsaaQuality
- `m_RenderScale`: float
- `m_UpscalingFilter`: UpscalingFilterSelection
- `m_FsrOverrideSharpness`: bool
- `m_FsrSharpness`: float
- `m_EnableLODCrossFade`: bool
- `m_LODCrossFadeDitheringType`: LODCrossFadeDitheringType
- `m_ShEvalMode`: ShEvalMode
- `m_LightProbeSystem`: LightProbeSystem
- `m_ProbeVolumeMemoryBudget`: ProbeVolumeTextureMemoryBudget
- `m_ProbeVolumeBlendingMemoryBudget`: ProbeVolumeBlendingTextureMemoryBudget
- ... (58 more fields)

---

#### UniversalRenderPipelineDebugDisplaySettings

**Line:** 903764

**Inherits:** DebugDisplaySettings

---

#### UniversalRenderPipelineDebugShaders

**Line:** 913381

**Inherits:** IRenderPipelineResources

**Fields:**

- `m_DebugReplacementPS`: Shader
- `m_HdrDebugViewPS`: Shader
- `m_ProbeVolumeSamplingDebugComputeShader`: ComputeShader

---

#### UniversalRenderPipelineEditorResources

**Line:** 906993

**Inherits:** ScriptableObject

---

#### UniversalRenderPipelineRuntimeShaders

**Line:** 913436

**Inherits:** IRenderPipelineResources

**Fields:**

- `m_Version`: int
- `m_FallbackErrorShader`: Shader
- `m_SamplingPS`: Shader
- `m_TerrainDetailLit`: Shader
- `m_TerrainDetailGrassBillboard`: Shader
- `m_TerrainDetailGrass`: Shader

---

#### UniversalRenderPipelineRuntimeTextures

**Line:** 913545

**Inherits:** IRenderPipelineResources

**Fields:**

- `m_Version`: int
- `m_BlueNoise64LTex`: Texture2D
- `m_BayerMatrixTex`: Texture2D
- `m_DebugFontTex`: Texture2D

---

#### UniversalRenderPipelineRuntimeXRResources

**Line:** 913603

**Inherits:** IRenderPipelineResources

**Fields:**

- `m_xrOcclusionMeshPS`: Shader
- `m_xrMirrorViewPS`: Shader
- `m_xrMotionVector`: Shader

---

#### UniversalRenderPipelineVolumeDebugSettings

**Line:** 903908

**Inherits:** VolumeDebugSettings

---

#### UniversalRenderer

**Line:** 915763

**Inherits:** ScriptableRenderer

**Fields:**

- `m_Clustering`: bool
- `m_DepthPrepass`: DepthOnlyPass
- `m_DepthNormalPrepass`: DepthNormalOnlyPass
- `m_PrimedDepthCopyPass`: CopyDepthPass
- `m_MotionVectorPass`: MotionVectorRenderPass
- `m_MainLightShadowCasterPass`: MainLightShadowCasterPass
- `m_AdditionalLightsShadowCasterPass`: AdditionalLightsShadowCasterPass
- `m_GBufferPass`: GBufferPass
- `m_GBufferCopyDepthPass`: CopyDepthPass
- `m_DeferredPass`: DeferredPass
- `m_RenderOpaqueForwardOnlyPass`: DrawObjectsPass
- `m_RenderOpaqueForwardPass`: DrawObjectsPass
- `m_RenderOpaqueForwardWithRenderingLayersPass`: DrawObjectsWithRenderingLayersPass
- `m_DrawSkyboxPass`: DrawSkyboxPass
- `m_CopyDepthPass`: CopyDepthPass
- `m_CopyColorPass`: CopyColorPass
- `m_TransparentSettingsPass`: TransparentSettingsPass
- `m_RenderTransparentForwardPass`: DrawObjectsPass
- `m_OnRenderObjectCallbackPass`: InvokeOnRenderObjectCallbackPass
- `m_FinalBlitPass`: FinalBlitPass
- ... (37 more fields)

---

#### UniversalRendererData

**Line:** 906793

**Inherits:** ScriptableRendererData

**Fields:**

- `postProcessData`: PostProcessData
- `m_AssetVersion`: int
- `m_OpaqueLayerMask`: LayerMask
- `m_TransparentLayerMask`: LayerMask
- `m_DefaultStencilState`: StencilStateData
- `m_ShadowTransparentReceive`: bool
- `m_RenderingMode`: RenderingMode
- `m_DepthPrimingMode`: DepthPrimingMode
- `m_CopyDepthMode`: CopyDepthMode
- `m_DepthAttachmentFormat`: DepthFormat
- `m_DepthTextureFormat`: DepthFormat
- `m_AccurateGbufferNormals`: bool
- `m_IntermediateTextureMode`: IntermediateTextureMode
- `m_StripShadowsOffVariants`: bool
- `m_StripAdditionalLightOffVariants`: bool

---

#### UniversalRendererResources

**Line:** 913312

**Inherits:** IRenderPipelineResources

**Fields:**

- `m_Version`: int
- `m_CopyDepthPS`: Shader
- `m_CameraMotionVector`: Shader
- `m_StencilDeferredPS`: Shader
- `m_DBufferClear`: Shader

---

#### UniversalRenderingData

**Line:** 907641

**Inherits:** ContextItem

**Fields:**

- `cullResults`: CullingResults
- `supportsDynamicBatching`: bool
- `perObjectData`: PerObjectData

---

#### UniversalResourceData

**Line:** 907752

**Inherits:** UniversalResourceDataBase

**Fields:**

- `_backBufferColor`: TextureHandle
- `_backBufferDepth`: TextureHandle
- `_cameraColor`: TextureHandle
- `_cameraDepth`: TextureHandle
- `_mainShadowsTexture`: TextureHandle
- `_additionalShadowsTexture`: TextureHandle
- `_cameraOpaqueTexture`: TextureHandle
- `_cameraDepthTexture`: TextureHandle
- `_cameraNormalsTexture`: TextureHandle
- `_motionVectorColor`: TextureHandle
- `_motionVectorDepth`: TextureHandle
- `_internalColorLut`: TextureHandle
- `_afterPostProcessColor`: TextureHandle
- `_overlayUITexture`: TextureHandle
- `_renderingLayersTexture`: TextureHandle
- `_dBufferDepth`: TextureHandle
- `_ssaoTexture`: TextureHandle
- `_stpDebugView`: TextureHandle

---

#### UniversalResourceDataBase

**Line:** 907707

**Inherits:** ContextItem

---

#### UniversalShadowData

**Line:** 907978

**Inherits:** ContextItem

**Fields:**

- `supportsMainLightShadows`: bool
- `mainLightShadowmapWidth`: int
- `mainLightShadowmapHeight`: int
- `mainLightShadowCascadesCount`: int
- `mainLightShadowCascadesSplit`: Vector3
- `mainLightShadowCascadeBorder`: float
- `supportsAdditionalLightShadows`: bool
- `additionalLightsShadowmapWidth`: int
- `additionalLightsShadowmapHeight`: int
- `supportsSoftShadows`: bool
- `shadowmapDepthBufferBits`: int
- `bias`: List<Vector4>
- `resolution`: List<int>

---

#### UnixDateTimeConverter

**Line:** 1048797

**Inherits:** DateTimeConverterBase

---

#### UnknownResourceProviderException

**Line:** 1434891

**Inherits:** ResourceManagerException

---

#### UnlockCondition

**Line:** 1060640

**Inherits:** IGameConfigData

---

#### UnlockConditionComponent

**Line:** 729496

**Inherits:** IComponent

**Fields:**

- `Value`: UnlockCondition

---

#### UnlockManager

**Line:** 737591

**Inherits:** IMessageReceiver

---

#### UnlockSystem

**Line:** 737672

**Inherits:** ReactiveSystem

---

#### UnmanagedFunctionPointerAttribute

**Line:** 228983

**Inherits:** Attribute

**Fields:**

- `m_callingConvention`: CallingConvention

---

#### UnmanagedMarshal

**Line:** 270329

---

#### UnmanagedMemoryStream

**Line:** 469205

**Inherits:** Stream

**Fields:**

- `_buffer`: SafeBuffer
- `_length`: long
- `_capacity`: long
- `_position`: long
- `_offset`: long
- `_access`: FileAccess
- `_lastReadTask`: Task<int>

---

#### UnmergeCellsRequest

**Line:** 1399969

**Inherits:** IDirectResponseSchema

---

#### UnmuteUserRequest

**Line:** 1528429

**Inherits:** IEquatable

---

#### UnobservedTaskExceptionEventArgs

**Line:** 213539

**Inherits:** EventArgs

**Fields:**

- `m_exception`: AggregateException

---

#### UnparsableValueException

**Line:** 1158750

**Inherits:** FormatException

---

#### UnreferencedObjectEventArgs

**Line:** 753114

**Inherits:** EventArgs

**Fields:**

- `o`: object
- `id`: string

---

#### UnreferencedObjectEventHandler

**Line:** 753102

**Inherits:** MulticastDelegate

---

#### UnsafeAERC

**Line:** 1547836

**Inherits:** IAERC

**Fields:**

- `_retainCount`: int

---

#### UnsafeCommandBuffer

**Line:** 806188

**Inherits:** BaseCommandBuffer

---

#### UnsafeGraphContext

**Line:** 829257

**Inherits:** IDerivedRendergraphContext

**Fields:**

- `wrappedContext`: InternalRenderGraphContext
- `cmd`: UnsafeCommandBuffer

---

#### UnsafeValueTypeAttribute

**Line:** 234476

**Inherits:** Attribute

---

#### Unselectable

**Line:** 1507075

**Inherits:** SRMonoBehaviour

**Fields:**

- `_suspectedSelected`: bool

---

#### UnsignedIntegerField

**Line:** 630208

**Inherits:** TextValueField

---

#### UnsignedLongField

**Line:** 630297

**Inherits:** TextValueField

---

#### UnsupportedSignerInfoVersion

**Line:** 1545299

**Inherits:** IAPSecurityException

---

#### UpDownCounter

**Line:** 1424767

---

#### UpdateBandingRequest

**Line:** 1400005

**Inherits:** IDirectResponseSchema

---

#### UpdateBordersRequest

**Line:** 1400053

**Inherits:** IDirectResponseSchema

---

#### UpdateCellsRequest

**Line:** 1400161

**Inherits:** IDirectResponseSchema

---

#### UpdateConditionalFormatRuleRequest

**Line:** 1400281

**Inherits:** IDirectResponseSchema

---

#### UpdateConditionalFormatRuleResponse

**Line:** 1400353

**Inherits:** IDirectResponseSchema

---

#### UpdateDataSourceRequest

**Line:** 1400425

**Inherits:** IDirectResponseSchema

---

#### UpdateDataSourceResponse

**Line:** 1400473

**Inherits:** IDirectResponseSchema

---

#### UpdateDeveloperMetadataRequest

**Line:** 1400521

**Inherits:** IDirectResponseSchema

---

#### UpdateDeveloperMetadataResponse

**Line:** 1400581

**Inherits:** IDirectResponseSchema

---

#### UpdateDimensionGroupRequest

**Line:** 1400617

**Inherits:** IDirectResponseSchema

---

#### UpdateDimensionPropertiesRequest

**Line:** 1400665

**Inherits:** IDirectResponseSchema

---

#### UpdateEmbeddedObjectBorderRequest

**Line:** 1400737

**Inherits:** IDirectResponseSchema

---

#### UpdateEmbeddedObjectPositionRequest

**Line:** 1400797

**Inherits:** IDirectResponseSchema

---

#### UpdateEmbeddedObjectPositionResponse

**Line:** 1400857

**Inherits:** IDirectResponseSchema

---

#### UpdateFilterViewRequest

**Line:** 1400893

**Inherits:** IDirectResponseSchema

---

#### UpdateLocalizationVersions

**Line:** 555546

**Inherits:** MetaMessage

---

#### UpdateMessageRequest

**Line:** 1527250

**Inherits:** IEquatable

---

#### UpdateNamedRangeRequest

**Line:** 1400941

**Inherits:** IDirectResponseSchema

---

#### UpdateProtectedRangeRequest

**Line:** 1400989

**Inherits:** IDirectResponseSchema

---

#### UpdateScheduledMaintenanceMode

**Line:** 555627

**Inherits:** MetaMessage

---

#### UpdateSheetPropertiesRequest

**Line:** 1401037

**Inherits:** IDirectResponseSchema

---

#### UpdateSlicerSpecRequest

**Line:** 1401085

**Inherits:** IDirectResponseSchema

---

#### UpdateSpreadsheetPropertiesRequest

**Line:** 1401145

**Inherits:** IDirectResponseSchema

---

#### UpdateSystems

**Line:** 684228

**Fields:**

- `_updateSystems`: List<IUpdateSystem>

---

#### UpdateValuesByDataFilterResponse

**Line:** 1401193

**Inherits:** IDirectResponseSchema

---

#### UpdateValuesResponse

**Line:** 1401289

**Inherits:** IDirectResponseSchema

---

#### UploadHandler

**Line:** 1566634

**Inherits:** IDisposable

---

#### UploadHandlerRaw

**Line:** 1566676

**Inherits:** UploadHandler

**Fields:**

- `m_Payload`: NativeArray<byte>

---

#### Uri

**Line:** 774084

**Inherits:** ISerializable

**Fields:**

- `m_String`: string
- `m_originalUnicodeString`: string
- `m_Syntax`: UriParser
- `m_DnsSafeHost`: string
- `m_iriParsing`: bool

---

#### UriBuilder

**Line:** 773802

**Fields:**

- `_changed`: bool
- `_fragment`: string
- `_host`: string
- `_password`: string
- `_path`: string
- `_port`: int
- `_query`: string
- `_scheme`: string
- `_schemeDelimiter`: string
- `_uri`: Uri
- `_username`: string

---

#### UriEndPoint

**Line:** 1570727

**Inherits:** EndPoint

---

#### UriFormatException

**Line:** 774554

**Inherits:** FormatException

---

#### UriParser

**Line:** 774744

**Fields:**

- `m_Flags`: UriSyntaxFlags
- `m_UpdatableFlags`: UriSyntaxFlags
- `m_UpdatableFlagsUsed`: bool
- `m_Port`: int
- `m_Scheme`: string

---

#### UriTypeConverter

**Line:** 775083

**Inherits:** TypeConverter

---

#### UrlAttribute

**Line:** 1510193

**Inherits:** DataTypeAttribute

---

#### UrlEncoder

**Line:** 1522241

**Inherits:** TextEncoder

---

#### UrlSourcedExternalAccountCredential

**Line:** 1374050

**Inherits:** ExternalAccountCredential

---

#### UseCustomParserFromDerivedAttribute

**Line:** 498923

**Inherits:** Attribute

---

#### UserBannedException

**Line:** 685301

**Inherits:** UnauthorizedException

---

#### UserCredential

**Line:** 1374231

**Inherits:** IGoogleCredential

---

#### UserMutedMessage

**Line:** 706113

**Inherits:** IMessage

**Fields:**

- `MutedUntil`: DateTimeOffset

---

#### UserNotFoundException

**Line:** 685337

**Inherits:** UnauthorizedException

---

#### UserReactionEntryUiView

**Line:** 708287

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerMiniProfileUiView`: PlayerMiniProfileUiView
- `ReactionEntryUiView`: ReactionEntryUiView
- `LoadingIndicator`: GameObject
- `ContentTransform`: RectTransform

---

#### UserReactionsListPopupUiView

**Line:** 708377

**Inherits:** MonoBehaviour

**Fields:**

- `Content`: RectTransform
- `ReactionEntriesParent`: RectTransform
- `UserReactionsScrollParent`: RectTransform
- `UserReactionEntryUiViewPrefab`: UserReactionEntryUiView
- `ReactionEntryUiViewPrefab`: ReactionEntryUiView
- `ActiveReactionsEntriesGrid`: GridLayoutGroup
- `MainLayoutGroup`: LayoutGroup
- `ActiveReactionsMaxColumnCount`: int
- `_userReactionEntries`: List<UserReactionEntryUiView>
- `_reactionEntries`: List<ReactionEntryUiView>
- `_chatService`: IChatService
- `_mainChatUiModel`: MainChatUIModel
- `_messageId`: long

---

#### UserTimedOutException

**Line:** 685310

**Inherits:** UnauthorizedException

---

#### UserTokenInvalidException

**Line:** 685319

**Inherits:** UnauthorizedException

---

#### UserTokenMismatchException

**Line:** 685328

**Inherits:** UnauthorizedException

---

#### Usercentrics

**Line:** 1565665

**Inherits:** Singleton

**Fields:**

- `SettingsID`: string
- `RulesetID`: string
- `Options`: UsercentricsOptions
- `onDismissCallback`: UnityAction<UsercentricsConsentUserResponse>
- `initializeCallback`: UnityAction<UsercentricsReadyStatus>
- `initializeErrorCallback`: UnityAction<string>
- `tcfDataCallback`: UnityAction<TCFData>
- `restoreSessionSuccessCallback`: UnityAction<UsercentricsReadyStatus>
- `restoreSessionErrorCallback`: UnityAction<string>
- `clearSessionSuccessCallback`: UnityAction<UsercentricsReadyStatus>
- `clearSessionErrorCallback`: UnityAction<string>

---

#### UsercentricsConsentHistoryEntry

**Line:** 1564495

**Fields:**

- `status`: bool
- `type`: UsercentricsConsentType
- `timestampInMillis`: long

---

#### UsercentricsConsentUserResponse

**Line:** 1564520

**Fields:**

- `userInteraction`: UsercentricsUserInteraction
- `consents`: List<UsercentricsServiceConsent>
- `controllerId`: string

---

#### UsercentricsLocation

**Line:** 1564930

**Fields:**

- `countryCode`: string
- `regionCode`: string

---

#### UsercentricsMediationEvent

**Line:** 1564959

**Fields:**

- `applied`: List<ConsentApplied>

---

#### UsercentricsOptions

**Line:** 1564372

**Fields:**

- `DefaultLanguage`: string
- `Version`: string
- `DebugMode`: bool
- `TimeoutMillis`: long
- `NetworkMode`: UsercentricsNetworkMode
- `ConsentMediation`: bool
- `InitTimeoutMillis`: long
- `Android`: AndroidOptions

---

#### UsercentricsOptionsInternal

**Line:** 1564407

**Fields:**

- `settingsId`: string
- `ruleSetId`: string
- `defaultLanguage`: string
- `version`: string
- `timeoutMillis`: long
- `loggerLevel`: UsercentricsLoggerLevel
- `networkMode`: UsercentricsNetworkMode
- `consentMediation`: bool
- `initTimeoutMillis`: long

---

#### UsercentricsReadyStatus

**Line:** 1564453

**Fields:**

- `shouldCollectConsent`: bool
- `consents`: List<UsercentricsServiceConsent>
- `geolocationRuleset`: GeolocationRuleset
- `location`: UsercentricsLocation

---

#### UsercentricsServiceConsent

**Line:** 1564469

**Fields:**

- `templateId`: string
- `status`: bool
- `history`: List<UsercentricsConsentHistoryEntry>
- `dataProcessor`: string
- `version`: string
- `isEssential`: bool
- `_type`: string
- `category`: string

---

#### UsercentricsServiceConsentWrapper

**Line:** 1565085

**Fields:**

- `consents`: List<UsercentricsServiceConsent>

---

#### UsercentricsUpdatedConsentEvent

**Line:** 1564818

**Fields:**

- `consents`: List<UsercentricsServiceConsent>
- `controllerId`: string
- `tcString`: string
- `uspString`: string
- `acString`: string

---

#### UsercentricsUserDecision

**Line:** 1565058

**Fields:**

- `serviceId`: string
- `consent`: bool

---

#### UsercentricsUserDecisionListWrapper

**Line:** 1565072

**Fields:**

- `decisions`: List<UsercentricsUserDecision>

---

#### UsercentricsWrapper

**Line:** 738982

**Inherits:** MonoBehaviour

**Fields:**

- `Config`: AgeGateConfig
- `MainCanvasContainer`: RectTransform
- `_onConsentFinished`: Action

---

#### Utf8JsonWriter

**Line:** 997395

**Inherits:** IDisposable

**Fields:**

- `_output`: IBufferWriter<byte>
- `_stream`: Stream
- `_arrayBufferWriter`: ArrayBufferWriter<byte>
- `_memory`: Memory<byte>
- `_inObject`: bool
- `_commentAfterNoneOrPropertyName`: bool
- `_tokenType`: JsonTokenType
- `_bitStack`: BitStack
- `_currentDepth`: int
- `_options`: JsonWriterOptions
- `_indentByte`: byte
- `_indentLength`: int
- `_newLineLength`: int

---

#### Util

**Line:** 525024

---

#### Utility

**Line:** 672202

**Fields:**

- `buffer`: IntPtr
- `elemCount`: int
- `elemStride`: int

---

#### UxmlAssetAttributeDescription

**Line:** 668383

---

#### UxmlAttributeAttribute

**Line:** 669308

**Inherits:** Attribute

**Fields:**

- `name`: string

---

#### UxmlAttributeDescription

**Line:** 668424

---

#### UxmlAttributeOverridesFactory

**Line:** 668284

**Inherits:** UxmlFactory

---

#### UxmlAttributeOverridesTraits

**Line:** 668307

**Inherits:** UxmlTraits

**Fields:**

- `m_ElementName`: UxmlStringAttributeDescription

---

#### UxmlBoolAttributeDescription

**Line:** 668979

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlDoubleAttributeDescription

**Line:** 668792

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlElementAttribute

**Line:** 669294

**Inherits:** Attribute

**Fields:**

- `visibility`: LibraryVisibility

---

#### UxmlEnumAttributeDescription

**Line:** 669102

---

#### UxmlEnumeration

**Line:** 669901

**Inherits:** UxmlTypeRestriction

**Fields:**

- `m_Values`: List<string>

---

#### UxmlFactory

**Line:** 669658

---

#### UxmlFloatAttributeDescription

**Line:** 668756

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlHash128AttributeDescription

**Line:** 669195

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlIgnoreAttribute

**Line:** 669328

**Inherits:** Attribute

---

#### UxmlIntAttributeDescription

**Line:** 668832

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlLongAttributeDescription

**Line:** 668943

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlObjectAttribute

**Line:** 669338

**Inherits:** Attribute

---

#### UxmlObjectReferenceAttribute

**Line:** 669348

**Inherits:** Attribute

**Fields:**

- `name`: string

---

#### UxmlRootElementFactory

**Line:** 668171

**Inherits:** UxmlFactory

---

#### UxmlRootElementTraits

**Line:** 668194

**Inherits:** UxmlTraits

**Fields:**

- `m_Name`: UxmlStringAttributeDescription
- `m_Class`: UxmlStringAttributeDescription

---

#### UxmlSerializedData

**Line:** 669858

---

#### UxmlStringAttributeDescription

**Line:** 668720

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlStyleFactory

**Line:** 668208

**Inherits:** UxmlFactory

---

#### UxmlStyleTraits

**Line:** 668231

**Inherits:** UxmlTraits

**Fields:**

- `m_Name`: UxmlStringAttributeDescription
- `m_Path`: UxmlStringAttributeDescription
- `m_Src`: UxmlStringAttributeDescription

---

#### UxmlTemplateFactory

**Line:** 668246

**Inherits:** UxmlFactory

---

#### UxmlTemplateTraits

**Line:** 668269

**Inherits:** UxmlTraits

**Fields:**

- `m_Name`: UxmlStringAttributeDescription
- `m_Path`: UxmlStringAttributeDescription
- `m_Src`: UxmlStringAttributeDescription

---

#### UxmlTraits

**Line:** 669431

**Inherits:** BaseUxmlTraits

---

#### UxmlTypeAttributeDescription

**Line:** 668994

---

#### UxmlTypeRestriction

**Line:** 669889

**Inherits:** IEquatable

---

#### UxmlUnsignedIntAttributeDescription

**Line:** 668871

**Inherits:** TypedUxmlAttributeDescription

---

#### UxmlUnsignedLongAttributeDescription

**Line:** 668907

**Inherits:** TypedUxmlAttributeDescription

---

#### VCProviderAnalytics

**Line:** 1587504

**Inherits:** AnalyticsEventBase

**Fields:**

- `Mode`: string

---

#### VFXEventAttribute

**Line:** 1587547

**Inherits:** IDisposable

**Fields:**

- `m_Ptr`: IntPtr
- `m_Owner`: bool
- `m_VfxAsset`: VisualEffectAsset

---

#### VFXExpressionValues

**Line:** 1587594

---

#### VFXRenderer

**Line:** 1587819

**Inherits:** Renderer

---

#### VFXSpawnerCallbacks

**Line:** 1587684

**Inherits:** ScriptableObject

---

#### VFXSpawnerState

**Line:** 1587704

**Inherits:** IDisposable

**Fields:**

- `m_Ptr`: IntPtr
- `m_Owner`: bool
- `m_WrapEventAttribute`: VFXEventAttribute

---

#### VRDeviceActiveControllersAnalytic

**Line:** 1586952

**Inherits:** VRDeviceAnalyticBase

---

#### VRDeviceAnalyticAspect

**Line:** 1586895

**Inherits:** VRDeviceAnalyticBase

**Fields:**

- `vr_aspect_ratio`: float

---

#### VRDeviceAnalyticBase

**Line:** 1586883

**Inherits:** AnalyticsEventBase

---

#### VRDeviceMirrorAnalytic

**Line:** 1586914

**Inherits:** VRDeviceAnalyticBase

**Fields:**

- `vr_device_mirror_mode`: bool

---

#### VRDeviceUserAnalytic

**Line:** 1586933

**Inherits:** VRDeviceAnalyticBase

**Fields:**

- `vr_user_presence`: int

---

#### ValidateCommandEvent

**Line:** 634100

**Inherits:** CommandEventBase

---

#### ValidateEnumeratedItemsAttribute

**Line:** 1540837

**Inherits:** Attribute

---

#### ValidateNextSteppingStonesResponse

**Line:** 1079505

**Inherits:** PlayerSynchronizedServerActionCore

---

#### ValidateOptions

**Line:** 1541356

---

#### ValidateOptionsResult

**Line:** 1541482

---

#### ValidateOptionsResultBuilder

**Line:** 1541574

**Fields:**

- `_errors`: List<string>

---

#### ValidationAttribute

**Line:** 1510277

**Inherits:** Attribute

**Fields:**

- `_errorMessage`: string
- `_errorMessageResourceAccessor`: Func<string>
- `_errorMessageResourceName`: string
- `_errorMessageResourceType`: Type
- `_hasBaseIsValid`: bool
- `_defaultErrorMessage`: string

---

#### ValidationContext

**Line:** 1510540

**Inherits:** IServiceProvider

**Fields:**

- `_displayName`: string
- `_serviceProvider`: Func<Type, object>

---

#### ValidationEventArgs

**Line:** 1042897

**Inherits:** EventArgs

---

#### ValidationEventHandler

**Line:** 1042924

**Inherits:** MulticastDelegate

---

#### ValidationException

**Line:** 1510612

**Inherits:** Exception

**Fields:**

- `_validationResult`: ValidationResult

---

#### ValidationResult

**Line:** 1510664

---

#### ValueAnimation

**Line:** 680954

**Fields:**

- `m_StartTimeMs`: long
- `m_DurationMs`: int
- `_from`: T
- `fromValueSet`: bool

---

#### ValueRange

**Line:** 1401385

**Inherits:** IDirectResponseSchema

---

#### ValueTupleSource

**Line:** 1322306

**Inherits:** ISource

**Fields:**

- `m_Formatter`: SmartFormatter

---

#### ValueType

**Line:** 177889

---

#### Variable

**Line:** 1323915

**Fields:**

- `m_Value`: T
- `ValueChanged`: Action<IVariable>

---

#### VariablesGroupAsset

**Line:** 1324974

**Inherits:** ScriptableObject

**Fields:**

- `m_VariableLookup`: Dictionary<string, VariableNameValuePair>

---

#### VariantList

**Line:** 1493462

**Fields:**

- `collectionRef`: VariantList
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### VariantVariantMap

**Line:** 1493303

**Fields:**

- `collectionRef`: VariantVariantMap
- `keyCollection`: IList<Variant>
- `currentIndex`: int
- `currentObject`: object
- `currentSize`: int

---

#### Vector2Field

**Line:** 616633

**Inherits:** BaseCompositeField

---

#### Vector2IntField

**Line:** 616912

**Inherits:** BaseCompositeField

---

#### Vector2Parameter

**Line:** 827405

**Inherits:** VolumeParameter

---

#### Vector2Plugin

**Line:** 1429497

**Inherits:** ABSTweenPlugin

---

#### Vector3ArrayPlugin

**Line:** 1429218

**Inherits:** ABSTweenPlugin

---

#### Vector3Field

**Line:** 616726

**Inherits:** BaseCompositeField

---

#### Vector3IntField

**Line:** 617005

**Inherits:** BaseCompositeField

---

#### Vector3Parameter

**Line:** 827430

**Inherits:** VolumeParameter

---

#### Vector3Plugin

**Line:** 1429667

**Inherits:** ABSTweenPlugin

---

#### Vector4Field

**Line:** 616828

**Inherits:** BaseCompositeField

---

#### Vector4Parameter

**Line:** 827455

**Inherits:** VolumeParameter

---

#### Vector4Plugin

**Line:** 1429530

**Inherits:** ABSTweenPlugin

---

#### VectorImage

**Line:** 670780

**Inherits:** ScriptableObject

---

#### VelocityComponent

**Line:** 709169

**Inherits:** IComponent

**Fields:**

- `Value`: Vector2

---

#### VelocityEventSystem

**Line:** 702717

**Inherits:** ReactiveSystem

---

#### VelocityListenerComponent

**Line:** 700129

**Inherits:** IComponent

**Fields:**

- `value`: List<IVelocityListener>

---

#### VendorUrl

**Line:** 1564803

**Fields:**

- `langId`: string
- `privacy`: string
- `legIntClaim`: string

---

#### Version

**Line:** 70719

**Inherits:** ICloneable

---

#### VersionConverter

**Line:** 1048836

**Inherits:** JsonConverter

---

#### VersionHeaderBuilder

**Line:** 1504325

---

#### VersionNotFoundException

**Line:** 1080891

**Inherits:** DataException

---

#### VersionTextBehaviour

**Line:** 1444111

**Inherits:** SRMonoBehaviourEx

**Fields:**

- `Format`: string
- `Text`: Text

---

#### VertexHelper

**Line:** 1357763

**Inherits:** IDisposable

**Fields:**

- `m_Positions`: List<Vector3>
- `m_Colors`: List<Color32>
- `m_Uv0S`: List<Vector4>
- `m_Uv1S`: List<Vector4>
- `m_Uv2S`: List<Vector4>
- `m_Uv3S`: List<Vector4>
- `m_Normals`: List<Vector3>
- `m_Tangents`: List<Vector4>
- `m_Indices`: List<int>
- `m_ListsInitalized`: bool

---

#### VerticalLayoutGroup

**Line:** 1355461

**Inherits:** HorizontalOrVerticalLayoutGroup

---

#### ViaHeaderValue

**Line:** 1491335

**Inherits:** ICloneable

---

#### VideoFingerView

**Line:** 697518

**Inherits:** UiUnityView

**Fields:**

- `_isActive`: bool
- `_targetScale`: float
- `Finger`: GameObject

---

#### Vignette

**Line:** 909813

**Inherits:** VolumeComponent

**Fields:**

- `color`: ColorParameter
- `center`: Vector2Parameter
- `intensity`: ClampedFloatParameter
- `smoothness`: ClampedFloatParameter
- `rounded`: BoolParameter

---

#### VirtualSparseSet

**Line:** 1545419

**Fields:**

- `_denseCount`: int

---

#### VirtualVerticalLayoutGroup

**Line:** 1507189

**Inherits:** LayoutGroup

**Fields:**

- `_isDirty`: bool
- `_rowCache`: SRList<VirtualVerticalLayoutGroup.Row>
- `_scrollRect`: ScrollRect
- `_selectedIndex`: int
- `_selectedItem`: object
- `_visibleItemCount`: int
- `_visibleRows`: SRList<VirtualVerticalLayoutGroup.Row>
- `AltRowStyleSheet`: StyleSheet
- `EnableSelection`: bool
- `ItemPrefab`: RectTransform
- `RowPadding`: int
- `RowStyleSheet`: StyleSheet
- `SelectedRowStyleSheet`: StyleSheet
- `Spacing`: float
- `StickToBottom`: bool
- `_itemHeight`: float

---

#### VisibilityAttribute

**Line:** 1512701

**Inherits:** PropertyAttribute

---

#### VisibilityChangedDelegate

**Line:** 1442421

**Inherits:** MulticastDelegate

---

#### VisibleForTestOnly

**Line:** 1495576

**Inherits:** Attribute

---

#### VisibleSkinsComponent

**Line:** 710559

**Inherits:** IComponent

**Fields:**

- `Value`: MetaDictionary<ItemType, SkinId>

---

#### VisibleSkinsEventSystem

**Line:** 702738

**Inherits:** ReactiveSystem

---

#### VisibleSkinsListenerComponent

**Line:** 700142

**Inherits:** IComponent

**Fields:**

- `value`: List<IVisibleSkinsListener>

---

#### VisualConfigComponent

**Line:** 698952

**Inherits:** IComponent

**Fields:**

- `Value`: IVisualConfig

---

#### VisualEffect

**Line:** 1587786

**Inherits:** Behaviour

**Fields:**

- `m_cachedEventAttribute`: VFXEventAttribute
- `outputEventReceived`: Action<VFXOutputEventArgs>

---

#### VisualEffectAsset

**Line:** 1587753

**Inherits:** VisualEffectObject

---

#### VisualEffectObject

**Line:** 1587746

**Inherits:** Object

---

#### VisualElement

**Line:** 651719

**Inherits:** Focusable

**Fields:**

- `m_Name`: string
- `m_ClassList`: List<string>
- `m_PropertyBag`: Dictionary<PropertyName, object>
- `m_ViewDataKey`: string
- `m_RenderHints`: RenderHints
- `m_Layout`: Rect
- `m_BoundingBox`: Rect
- `m_WorldBoundingBox`: Rect
- `m_WorldTransformCache`: Matrix4x4
- `m_WorldTransformInverseCache`: Matrix4x4
- `m_WorldClip`: Rect
- `m_WorldClipMinusGroup`: Rect
- `m_WorldClipIsInfinite`: bool
- `m_PseudoStates`: PseudoStates
- `m_PickingMode`: PickingMode
- `m_LayoutNode`: LayoutNode
- `m_EnabledSelf`: bool
- `m_LanguageDirection`: LanguageDirection
- `m_LocalLanguageDirection`: LanguageDirection
- `m_defaultMaterial`: Material
- ... (17 more fields)

---

#### VisualElementFocusChangeDirection

**Line:** 671285

**Inherits:** FocusChangeDirection

---

#### VisualElementFocusRing

**Line:** 671394

**Inherits:** IFocusRing

**Fields:**

- `m_FocusRing`: List<VisualElementFocusRing.FocusRingRecord>

---

#### VisualTreeAsset

**Line:** 670311

**Inherits:** ScriptableObject

**Fields:**

- `m_ImportedWithErrors`: bool
- `m_HasUpdatedUrls`: bool
- `m_ImportedWithWarnings`: bool
- `m_Usings`: List<VisualTreeAsset.UsingEntry>
- `m_UxmlObjectEntries`: List<VisualTreeAsset.UxmlObjectEntry>
- `m_UxmlObjectIds`: List<int>
- `m_AssetEntries`: List<VisualTreeAsset.AssetEntry>
- `m_Slots`: List<VisualTreeAsset.SlotDefinition>
- `m_ContentContainerId`: int
- `m_ContentHash`: int

---

#### VoidResult

**Line:** 1585755

---

#### Volume

**Line:** 825892

**Inherits:** MonoBehaviour

**Fields:**

- `m_IsGlobal`: bool
- `priority`: float
- `blendDistance`: float
- `weight`: float
- `sharedProfile`: VolumeProfile
- `m_PreviousLayer`: int
- `m_PreviousPriority`: float
- `m_InternalProfile`: VolumeProfile

---

#### VolumeComponent

**Line:** 826087

**Inherits:** ScriptableObject

**Fields:**

- `active`: bool
- `m_ParameterReadOnlyCollection`: ReadOnlyCollection<VolumeParameter>

---

#### VolumeComponentDeprecated

**Line:** 826044

**Inherits:** Attribute

---

#### VolumeComponentMenu

**Line:** 826009

**Inherits:** Attribute

---

#### VolumeComponentMenuForRenderPipeline

**Line:** 826022

**Inherits:** VolumeComponentMenu

---

#### VolumeDebugSettings

**Line:** 815700

**Fields:**

- `m_SelectedCameraIndex`: int
- `m_Cameras`: List<Camera>

---

#### VolumeManager

**Line:** 816090

**Fields:**

- `m_DefaultStack`: VolumeStack

---

#### VolumeParameter

**Line:** 826248

**Fields:**

- `m_Value`: T

---

#### VolumeProfile

**Line:** 827799

**Inherits:** ScriptableObject

**Fields:**

- `components`: List<VolumeComponent>

---

#### VolumeRequiresRendererFeatures

**Line:** 917928

**Inherits:** Attribute

---

#### VolumeStack

**Line:** 827908

**Inherits:** IDisposable

---

#### WWWForm

**Line:** 1565885

---

#### WaitCallback

**Line:** 181284

**Inherits:** MulticastDelegate

---

#### WaitForEndOfFrame

**Line:** 884634

**Inherits:** YieldInstruction

---

#### WaitForFixedUpdate

**Line:** 884644

**Inherits:** YieldInstruction

---

#### WaitForSeconds

**Line:** 884649

**Inherits:** YieldInstruction

---

#### WaitForSecondsRealtime

**Line:** 884661

**Inherits:** CustomYieldInstruction

**Fields:**

- `m_WaitUntilTime`: float

---

#### WaitHandle

**Line:** 181676

**Inherits:** MarshalByRefObject

**Fields:**

- `waitHandle`: IntPtr

---

#### WaitHandleCannotBeOpenedException

**Line:** 179168

**Inherits:** ApplicationException

---

#### WaitOrTimerCallback

**Line:** 181297

**Inherits:** MulticastDelegate

---

#### WaitUntil

**Line:** 884703

**Inherits:** CustomYieldInstruction

---

#### WaterfallChartColumnStyle

**Line:** 1401445

**Inherits:** IDirectResponseSchema

---

#### WaterfallChartCustomSubtotal

**Line:** 1401505

**Inherits:** IDirectResponseSchema

---

#### WaterfallChartDomain

**Line:** 1401565

**Inherits:** IDirectResponseSchema

---

#### WaterfallChartSeries

**Line:** 1401613

**Inherits:** IDirectResponseSchema

---

#### WaterfallChartSpec

**Line:** 1401721

**Inherits:** IDirectResponseSchema

---

#### Watermark

**Line:** 894896

---

#### WeakReference

**Line:** 178006

**Fields:**

- `handle`: GCHandle
- `trackResurrection`: bool

---

#### WebException

**Line:** 792049

**Inherits:** InvalidOperationException

**Fields:**

- `m_Status`: WebExceptionStatus
- `m_Response`: WebResponse
- `m_InternalStatus`: WebExceptionInternalStatus

---

#### WebHeaderCollection

**Line:** 792196

**Inherits:** NameValueCollection

**Fields:**

- `m_NumCommonHeaders`: int
- `m_InnerCollection`: NameValueCollection
- `m_Type`: WebHeaderCollectionType

---

#### WebLoginCredentialsProvider

**Line:** 1309802

**Inherits:** ISocialCredentialsProvider

---

#### WebProxy

**Line:** 794031

**Inherits:** IWebProxy

**Fields:**

- `_UseRegistry`: bool
- `_BypassOnLocal`: bool
- `m_EnableAutoproxy`: bool
- `_ProxyAddress`: Uri
- `_BypassList`: ArrayList
- `_Credentials`: ICredentials
- `_ProxyHostAddresses`: Hashtable
- `m_ScriptEngine`: AutoWebProxyScriptEngine

---

#### WebProxyScriptElement

**Line:** 803266

**Inherits:** ConfigurationElement

---

#### WebRequest

**Line:** 792393

**Inherits:** MarshalByRefObject

**Fields:**

- `m_AuthenticationLevel`: AuthenticationLevel
- `m_ImpersonationLevel`: TokenImpersonationLevel
- `m_CachePolicy`: RequestCachePolicy
- `m_CacheProtocol`: RequestCacheProtocol
- `m_CacheBinding`: RequestCacheBinding

---

#### WebRequestModuleElement

**Line:** 803307

**Inherits:** ConfigurationElement

---

#### WebRequestModuleElementCollection

**Line:** 803298

**Inherits:** ConfigurationElementCollection

---

#### WebRequestModulesSection

**Line:** 803281

**Inherits:** ConfigurationSection

---

#### WebRequestQueueOperation

**Line:** 1434804

**Fields:**

- `m_Completed`: bool
- `Result`: UnityWebRequestAsyncOperation
- `OnComplete`: Action<UnityWebRequestAsyncOperation>

---

#### WebResponse

**Line:** 792569

**Inherits:** MarshalByRefObject

**Fields:**

- `m_IsFromCache`: bool

---

#### WebSocket

**Line:** 802375

**Inherits:** IDisposable

---

#### WebSocketConnectionContext

**Line:** 1482980

---

#### WebSocketConnector

**Line:** 526998

---

#### WebSocketException

**Line:** 802459

**Inherits:** Win32Exception

---

#### WebSocketReceiveResult

**Line:** 802523

---

#### WebSocketTransport

**Line:** 548544

**Inherits:** WireMessageTransport

**Fields:**

- `_cts`: CancellationTokenSource
- `_log`: IMetaLogger
- `_debugDiagnostics`: LoginTransportDebugDiagnostics
- `_onConnectedInvoked`: bool
- `_receivedServerHello`: bool
- `_receivedProtocolHeader`: bool
- `_lastMessageReceivedAt`: DateTime
- `_callbackErrorSource`: TaskCompletionSource<int>
- `_errorEmitted`: bool
- `_writeQueue`: WireMessageWriteQueue
- `_readBuffer`: WireMessageReadBuffer
- `_pingTracker`: MessageTransportPingTracker
- `_socketId`: int
- `_keepAliveTimeout`: Nullable<DateTime>
- `_headerTimeout`: Nullable<DateTime>

---

#### WellKnownClientTypeEntry

**Line:** 221833

**Inherits:** TypeEntry

**Fields:**

- `obj_type`: Type
- `obj_url`: string
- `app_url`: string

---

#### WellKnownServiceTypeEntry

**Line:** 221876

**Inherits:** TypeEntry

**Fields:**

- `obj_type`: Type
- `obj_uri`: string
- `obj_mode`: WellKnownObjectMode

---

#### WheelEvent

**Line:** 636623

**Inherits:** MouseEventBase

---

#### WhiteBalance

**Line:** 909844

**Inherits:** VolumeComponent

**Fields:**

- `temperature`: ClampedFloatParameter
- `tint`: ClampedFloatParameter

---

#### Win32Exception

**Line:** 784700

**Inherits:** ExternalException

---

#### WinProductDescription

**Line:** 1595898

---

#### WindowsIdentity

**Line:** 220395

**Inherits:** ClaimsIdentity

**Fields:**

- `_token`: IntPtr
- `_type`: string
- `_account`: WindowsAccountType
- `_authenticated`: bool
- `_name`: string
- `_info`: SerializationInfo

---

#### WindowsImpersonationContext

**Line:** 220464

**Inherits:** IDisposable

**Fields:**

- `_token`: IntPtr
- `undo`: bool

---

#### WindowsStore

**Line:** 1408257

---

#### WindowsZones

**Line:** 1150985

---

#### WireMessageTransport

**Line:** 547607

**Inherits:** MessageTransport

---

#### WireMessageWriteQueue

**Line:** 551423

---

#### WorldIndexConfig

**Line:** 1060727

**Inherits:** IGameConfigData

---

#### WorldModel

**Line:** 1079732

**Inherits:** ISchemaMigratable

**Fields:**

- `WorldIndex`: WorldIndex
- `LastPlayerOnlineAt`: MetaTime
- `CreatedAt`: MetaTime

---

#### WorldVisualConfig

**Line:** 711521

**Inherits:** ScriptableObject

**Fields:**

- `SheetConnection`: GoogleSheetConnection
- `WeaponLibrarySheetName`: string
- `ProjectileLibrarySheetName`: string
- `DefaultWeapon`: EquipmentItemVisualConfig
- `AgeConfigs`: List<AgeVisualConfig>
- `ChatPvpMap`: PvpMapData
- `ArenaPvpMap`: PvpMapData
- `GuildWarMap`: PvpMapData

---

#### WritableMessageFragment

**Line:** 1319612

**Inherits:** MessageFragment

---

#### WriteAccessRequiredAttribute

**Line:** 864233

**Inherits:** Attribute

---

#### WriteOnlyAttribute

**Line:** 837988

**Inherits:** Attribute

---

#### WriteUsSettingsView

**Line:** 729329

**Inherits:** UiUnityView

**Fields:**

- `Button`: FlatButton

---

#### X500DistinguishedName

**Line:** 779142

**Inherits:** AsnEncodedData

**Fields:**

- `name`: string

---

#### X501

**Line:** 1447582

---

#### X509BasicConstraintsExtension

**Line:** 779179

**Inherits:** X509Extension

**Fields:**

- `_certificateAuthority`: bool
- `_hasPathLengthConstraint`: bool
- `_pathLengthConstraint`: int
- `_status`: AsnDecodeStatus

---

#### X509Certificate

**Line:** 1447707

**Inherits:** ISerializable

**Fields:**

- `decoder`: ASN1
- `m_from`: DateTime
- `m_until`: DateTime
- `issuer`: ASN1
- `m_issuername`: string
- `m_keyalgo`: string
- `subject`: ASN1
- `m_subject`: string
- `m_signaturealgo`: string
- `_rsa`: RSA
- `_dsa`: DSA
- `version`: int
- `extensions`: X509ExtensionCollection

---

#### X509Certificate2

**Line:** 779229

**Inherits:** X509Certificate

**Fields:**

- `lazySignatureAlgorithm`: Oid
- `lazyVersion`: int
- `lazySubjectName`: X500DistinguishedName
- `lazyIssuerName`: X500DistinguishedName
- `lazyPublicKey`: PublicKey
- `lazyPrivateKey`: AsymmetricAlgorithm
- `lazyExtensions`: X509ExtensionCollection

---

#### X509Certificate2Collection

**Line:** 779343

**Inherits:** X509CertificateCollection

---

#### X509Certificate2Enumerator

**Line:** 779387

**Inherits:** IEnumerator

**Fields:**

- `enumerator`: IEnumerator

---

#### X509CertificateCollection

**Line:** 1447880

**Inherits:** CollectionBase

---

#### X509Chain

**Line:** 1447919

**Fields:**

- `roots`: X509CertificateCollection
- `certs`: X509CertificateCollection
- `_root`: X509Certificate
- `_chain`: X509CertificateCollection
- `_status`: X509ChainStatusFlags

---

#### X509ChainElement

**Line:** 779790

**Fields:**

- `certificate`: X509Certificate2
- `info`: string
- `compressed_status_flags`: X509ChainStatusFlags

---

#### X509ChainElementCollection

**Line:** 779832

**Inherits:** ICollection

**Fields:**

- `_list`: ArrayList

---

#### X509ChainElementEnumerator

**Line:** 779880

**Inherits:** IEnumerator

**Fields:**

- `enumerator`: IEnumerator

---

#### X509ChainPolicy

**Line:** 780100

**Fields:**

- `apps`: OidCollection
- `cert`: OidCollection
- `store`: X509CertificateCollection
- `store2`: X509Certificate2Collection
- `rflag`: X509RevocationFlag
- `mode`: X509RevocationMode
- `timeout`: TimeSpan
- `vflags`: X509VerificationFlags
- `vtime`: DateTime

---

#### X509Crl

**Line:** 1447647

**Fields:**

- `issuer`: string
- `version`: byte
- `thisUpdate`: DateTime
- `nextUpdate`: DateTime
- `entries`: ArrayList
- `signatureOID`: string
- `extensions`: X509ExtensionCollection

---

#### X509EnhancedKeyUsageExtension

**Line:** 780180

**Inherits:** X509Extension

**Fields:**

- `_enhKeyUsage`: OidCollection
- `_status`: AsnDecodeStatus

---

#### X509Extension

**Line:** 1447981

**Fields:**

- `extnOid`: string
- `extnCritical`: bool
- `extnValue`: ASN1

---

#### X509ExtensionCollection

**Line:** 1448031

**Inherits:** CollectionBase

**Fields:**

- `readOnly`: bool

---

#### X509ExtensionEnumerator

**Line:** 780294

**Inherits:** IEnumerator

**Fields:**

- `enumerator`: IEnumerator

---

#### X509KeyUsageExtension

**Line:** 780344

**Inherits:** X509Extension

**Fields:**

- `_keyUsages`: X509KeyUsageFlags
- `_status`: AsnDecodeStatus

---

#### X509Store

**Line:** 1448058

**Fields:**

- `_storePath`: string
- `_certificates`: X509CertificateCollection
- `_crls`: ArrayList
- `_crl`: bool
- `_newFormat`: bool

---

#### X509StoreManager

**Line:** 1448102

---

#### X509Stores

**Line:** 1448136

**Fields:**

- `_storePath`: string
- `_newFormat`: bool
- `_trusted`: X509Store

---

#### X509SubjectKeyIdentifierExtension

**Line:** 780426

**Inherits:** X509Extension

**Fields:**

- `_ski`: string
- `_status`: AsnDecodeStatus

---

#### XAttribute

**Line:** 1560146

**Inherits:** XObject

---

#### XCData

**Line:** 1560193

**Inherits:** XText

---

#### XComment

**Line:** 1560217

**Inherits:** XNode

---

#### XContainer

**Line:** 1560376

**Inherits:** XNode

---

#### XDeclaration

**Line:** 1560471

**Fields:**

- `_version`: string
- `_encoding`: string
- `_standalone`: string

---

#### XDocument

**Line:** 1560511

**Inherits:** XContainer

**Fields:**

- `_declaration`: XDeclaration

---

#### XDocumentType

**Line:** 1560575

**Inherits:** XNode

**Fields:**

- `_name`: string
- `_publicId`: string
- `_systemId`: string
- `_internalSubset`: string

---

#### XElement

**Line:** 1560674

**Inherits:** XContainer

---

#### XElementFormatter

**Line:** 1322322

**Inherits:** FormatterBase

---

#### XHashtable

**Line:** 1560773

---

#### XName

**Line:** 1561053

**Inherits:** IEquatable

**Fields:**

- `_ns`: XNamespace
- `_localName`: string
- `_hashCode`: int

---

#### XNamespace

**Line:** 1561112

**Fields:**

- `_namespaceName`: string
- `_hashCode`: int
- `_names`: XHashtable<XName>

---

#### XNode

**Line:** 1561188

**Inherits:** XObject

---

#### XObject

**Line:** 1561218

**Inherits:** IXmlLineInfo

---

#### XObjectChangeEventArgs

**Line:** 1561300

**Inherits:** EventArgs

**Fields:**

- `_objectChange`: XObjectChange

---

#### XPathDocument

**Line:** 752648

**Fields:**

- `idxXmlNmsp`: int
- `nameTable`: XmlNameTable
- `hasLineInfo`: bool
- `mapNmsp`: Dictionary<XPathNodeRef, XPathNodeRef>

---

#### XPathException

**Line:** 752678

**Inherits:** SystemException

**Fields:**

- `res`: string
- `message`: string

---

#### XPathItem

**Line:** 752739

---

#### XPathNavigator

**Line:** 752803

**Inherits:** XPathItem

---

#### XProcessingInstruction

**Line:** 1561319

**Inherits:** XNode

---

#### XRLayout

**Line:** 803659

---

#### XRPass

**Line:** 803801

---

#### XRSRPSettings

**Line:** 827985

---

#### XRSystemData

**Line:** 906777

**Inherits:** ScriptableObject

---

#### XStreamingElement

**Line:** 1561361

---

#### XText

**Line:** 1561369

**Inherits:** XNode

---

#### XmlAnyAttributeAttribute

**Line:** 753454

**Inherits:** Attribute

---

#### XmlAnyElementAttribute

**Line:** 753464

**Inherits:** Attribute

**Fields:**

- `elementName`: string
- `ns`: string
- `order`: int

---

#### XmlAnyElementAttributes

**Line:** 753496

**Inherits:** CollectionBase

---

#### XmlArrayAttribute

**Line:** 753522

**Inherits:** Attribute

**Fields:**

- `elementName`: string
- `form`: XmlSchemaForm
- `isNullable`: bool
- `ns`: string
- `order`: int

---

#### XmlArrayItemAttribute

**Line:** 753561

**Inherits:** Attribute

**Fields:**

- `dataType`: string
- `elementName`: string
- `form`: XmlSchemaForm
- `ns`: string
- `isNullable`: bool
- `isNullableSpecified`: bool
- `nestingLevel`: int
- `type`: Type

---

#### XmlArrayItemAttributes

**Line:** 753615

**Inherits:** CollectionBase

---

#### XmlAtomicValue

**Line:** 763246

**Inherits:** XPathItem

**Fields:**

- `xmlType`: XmlSchemaType
- `objVal`: object
- `clrType`: TypeCode

---

#### XmlAttribute

**Line:** 747864

**Inherits:** XmlNode

**Fields:**

- `name`: XmlName
- `lastChild`: XmlLinkedNode

---

#### XmlAttributeAttribute

**Line:** 753637

**Inherits:** Attribute

**Fields:**

- `attributeName`: string
- `dataType`: string
- `type`: Type
- `form`: XmlSchemaForm
- `ns`: string

---

#### XmlAttributeCollection

**Line:** 748014

**Inherits:** XmlNamedNodeMap

---

#### XmlAttributeEventArgs

**Line:** 753031

**Inherits:** EventArgs

**Fields:**

- `o`: object
- `attr`: XmlAttribute
- `qnames`: string
- `lineNumber`: int
- `linePosition`: int

---

#### XmlAttributeEventHandler

**Line:** 753019

**Inherits:** MulticastDelegate

---

#### XmlAttributeOverrides

**Line:** 753678

**Fields:**

- `overrides`: Hashtable

---

#### XmlAttributes

**Line:** 753706

**Fields:**

- `xmlAnyAttribute`: XmlAnyAttributeAttribute
- `xmlAnyElements`: XmlAnyElementAttributes
- `xmlArray`: XmlArrayAttribute
- `xmlArrayItems`: XmlArrayItemAttributes
- `xmlAttribute`: XmlAttributeAttribute
- `xmlChoiceIdentifier`: XmlChoiceIdentifierAttribute
- `xmlDefaultValue`: object
- `xmlElements`: XmlElementAttributes
- `xmlEnum`: XmlEnumAttribute
- `xmlIgnore`: bool
- `xmlns`: bool
- `xmlRoot`: XmlRootAttribute
- `xmlText`: XmlTextAttribute
- `xmlType`: XmlTypeAttribute

---

#### XmlCDataSection

**Line:** 748100

**Inherits:** XmlCharacterData

---

#### XmlCharacterData

**Line:** 748140

**Inherits:** XmlLinkedNode

**Fields:**

- `data`: string

---

#### XmlChoiceIdentifierAttribute

**Line:** 753800

**Inherits:** Attribute

**Fields:**

- `memberName`: string

---

#### XmlComment

**Line:** 748235

**Inherits:** XmlCharacterData

---

#### XmlConvert

**Line:** 751454

---

#### XmlDeclaration

**Line:** 748267

**Inherits:** XmlLinkedNode

**Fields:**

- `version`: string
- `encoding`: string
- `standalone`: string

---

#### XmlDocument

**Line:** 748342

**Inherits:** XmlNode

**Fields:**

- `implementation`: XmlImplementation
- `domNameTable`: DomNameTable
- `lastChild`: XmlLinkedNode
- `entities`: XmlNamedNodeMap
- `htElementIdMap`: Hashtable
- `htElementIDAttrDecl`: Hashtable
- `schemaInfo`: SchemaInfo
- `schemas`: XmlSchemaSet
- `reportValidity`: bool
- `actualLoadingStatus`: bool
- `onNodeInsertingDelegate`: XmlNodeChangedEventHandler
- `onNodeInsertedDelegate`: XmlNodeChangedEventHandler
- `onNodeRemovingDelegate`: XmlNodeChangedEventHandler
- `onNodeRemovedDelegate`: XmlNodeChangedEventHandler
- `onNodeChangingDelegate`: XmlNodeChangedEventHandler
- `onNodeChangedDelegate`: XmlNodeChangedEventHandler
- `preserveWhitespace`: bool
- `isLoading`: bool
- `resolver`: XmlResolver

---

#### XmlDocumentFragment

**Line:** 748700

**Inherits:** XmlNode

**Fields:**

- `lastChild`: XmlLinkedNode

---

#### XmlDocumentType

**Line:** 748767

**Inherits:** XmlLinkedNode

**Fields:**

- `name`: string
- `publicId`: string
- `systemId`: string
- `internalSubset`: string
- `namespaces`: bool
- `entities`: XmlNamedNodeMap
- `notations`: XmlNamedNodeMap
- `schemaInfo`: SchemaInfo

---

#### XmlElement

**Line:** 748844

**Inherits:** XmlLinkedNode

**Fields:**

- `name`: XmlName
- `attributes`: XmlAttributeCollection
- `lastChild`: XmlLinkedNode

---

#### XmlElementAttribute

**Line:** 753846

**Inherits:** Attribute

**Fields:**

- `dataType`: string
- `elementName`: string
- `form`: XmlSchemaForm
- `ns`: string
- `isNullable`: bool
- `type`: Type
- `order`: int

---

#### XmlElementAttributes

**Line:** 753901

**Inherits:** CollectionBase

---

#### XmlElementEventArgs

**Line:** 753059

**Inherits:** EventArgs

**Fields:**

- `o`: object
- `elem`: XmlElement
- `qnames`: string
- `lineNumber`: int
- `linePosition`: int

---

#### XmlElementEventHandler

**Line:** 753047

**Inherits:** MulticastDelegate

---

#### XmlEntity

**Line:** 749006

**Inherits:** XmlNode

**Fields:**

- `publicId`: string
- `systemId`: string
- `notationName`: string
- `name`: string
- `unparsedReplacementStr`: string
- `baseURI`: string
- `lastChild`: XmlLinkedNode
- `childrenFoliating`: bool

---

#### XmlEntityReference

**Line:** 749088

**Inherits:** XmlLinkedNode

**Fields:**

- `name`: string
- `lastChild`: XmlLinkedNode

---

#### XmlEnumAttribute

**Line:** 753927

**Inherits:** Attribute

**Fields:**

- `name`: string

---

#### XmlException

**Line:** 752218

**Inherits:** SystemException

**Fields:**

- `res`: string
- `lineNumber`: int
- `linePosition`: int
- `sourceUri`: string
- `message`: string

---

#### XmlIgnoreAttribute

**Line:** 753949

**Inherits:** Attribute

---

#### XmlImplementation

**Line:** 749176

**Fields:**

- `nameTable`: XmlNameTable

---

#### XmlIncludeAttribute

**Line:** 753959

**Inherits:** Attribute

**Fields:**

- `type`: Type

---

#### XmlLinkedNode

**Line:** 749200

**Inherits:** XmlNode

---

#### XmlMapping

**Line:** 753974

**Fields:**

- `map`: ObjectMap
- `relatedMaps`: ArrayList
- `format`: SerializationFormat
- `source`: SerializationSource
- `key`: string

---

#### XmlNameTable

**Line:** 752326

---

#### XmlNamedNodeMap

**Line:** 749509

**Inherits:** IEnumerable

---

#### XmlNamespaceDeclarationsAttribute

**Line:** 754074

**Inherits:** Attribute

---

#### XmlNamespaceManager

**Line:** 752369

**Inherits:** IXmlNamespaceResolver

**Fields:**

- `lastDecl`: int
- `nameTable`: XmlNameTable
- `scopeId`: int
- `hashTable`: Dictionary<string, int>
- `useHashtable`: bool
- `xml`: string
- `xmlNs`: string

---

#### XmlNode

**Line:** 749560

**Inherits:** ICloneable

---

#### XmlNodeChangedEventArgs

**Line:** 749786

**Inherits:** EventArgs

**Fields:**

- `action`: XmlNodeChangedAction
- `node`: XmlNode
- `oldParent`: XmlNode
- `newParent`: XmlNode
- `oldValue`: string
- `newValue`: string

---

#### XmlNodeChangedEventHandler

**Line:** 749809

**Inherits:** MulticastDelegate

---

#### XmlNodeConverter

**Line:** 1049725

**Inherits:** JsonConverter

---

#### XmlNodeEventArgs

**Line:** 753087

**Inherits:** EventArgs

**Fields:**

- `o`: object
- `xmlNode`: XmlNode
- `lineNumber`: int
- `linePosition`: int

---

#### XmlNodeEventHandler

**Line:** 753075

**Inherits:** MulticastDelegate

---

#### XmlNodeList

**Line:** 749822

**Inherits:** IEnumerable

---

#### XmlNodeReader

**Line:** 750066

**Inherits:** XmlReader

**Fields:**

- `readerNav`: XmlNodeReaderNavigator
- `nodeType`: XmlNodeType
- `curDepth`: int
- `readState`: ReadState
- `fEOF`: bool
- `bResolveEntity`: bool
- `bStartFromDocument`: bool
- `bInReadBinary`: bool
- `readBinaryHelper`: ReadContentAsBinaryHelper

---

#### XmlNotation

**Line:** 750246

**Inherits:** XmlNode

**Fields:**

- `publicId`: string
- `systemId`: string
- `name`: string

---

#### XmlParserContext

**Line:** 743048

**Fields:**

- `_nt`: XmlNameTable
- `_nsMgr`: XmlNamespaceManager
- `_docTypeName`: string
- `_pubId`: string
- `_sysId`: string
- `_internalSubset`: string
- `_xmlLang`: string
- `_xmlSpace`: XmlSpace
- `_baseURI`: string
- `_encoding`: Encoding

---

#### XmlProcessingInstruction

**Line:** 750291

**Inherits:** XmlLinkedNode

**Fields:**

- `target`: string
- `data`: string

---

#### XmlQualifiedName

**Line:** 752466

**Fields:**

- `name`: string
- `ns`: string
- `hash`: int

---

#### XmlReader

**Line:** 743238

**Inherits:** IDisposable

---

#### XmlReaderSection

**Line:** 756039

---

#### XmlReaderSettings

**Line:** 743504

**Fields:**

- `useAsync`: bool
- `nameTable`: XmlNameTable
- `xmlResolver`: XmlResolver
- `lineNumberOffset`: int
- `linePositionOffset`: int
- `conformanceLevel`: ConformanceLevel
- `checkCharacters`: bool
- `maxCharactersInDocument`: long
- `maxCharactersFromEntities`: long
- `ignoreWhitespace`: bool
- `ignorePIs`: bool
- `ignoreComments`: bool
- `dtdProcessing`: DtdProcessing
- `validationType`: ValidationType
- `validationFlags`: XmlSchemaValidationFlags
- `schemas`: XmlSchemaSet
- `valEventHandler`: ValidationEventHandler
- `closeInput`: bool
- `isReadOnly`: bool

---

#### XmlReflectionImporter

**Line:** 754104

**Fields:**

- `initialDefaultNamespace`: string
- `attributeOverrides`: XmlAttributeOverrides
- `includedTypes`: ArrayList
- `helper`: ReflectionHelper
- `arrayChoiceCount`: int
- `relatedMaps`: ArrayList
- `allowPrivateTypes`: bool

---

#### XmlResolver

**Line:** 752550

---

#### XmlRootAttribute

**Line:** 754241

**Inherits:** Attribute

**Fields:**

- `dataType`: string
- `elementName`: string
- `isNullable`: bool
- `ns`: string

---

#### XmlSchema

**Line:** 763337

**Inherits:** XmlSchemaObject

**Fields:**

- `attributeFormDefault`: XmlSchemaForm
- `elementFormDefault`: XmlSchemaForm
- `blockDefault`: XmlSchemaDerivationMethod
- `finalDefault`: XmlSchemaDerivationMethod
- `targetNs`: string
- `version`: string
- `includes`: XmlSchemaObjectCollection
- `items`: XmlSchemaObjectCollection
- `id`: string
- `isCompiled`: bool
- `isCompiledBySet`: bool
- `isPreprocessed`: bool
- `isRedefined`: bool
- `errorCount`: int
- `attributes`: XmlSchemaObjectTable
- `attributeGroups`: XmlSchemaObjectTable
- `elements`: XmlSchemaObjectTable
- `types`: XmlSchemaObjectTable
- `groups`: XmlSchemaObjectTable
- `notations`: XmlSchemaObjectTable
- ... (8 more fields)

---

#### XmlSchemaAll

**Line:** 763603

**Inherits:** XmlSchemaGroupBase

**Fields:**

- `items`: XmlSchemaObjectCollection

---

#### XmlSchemaAnnotated

**Line:** 763629

**Inherits:** XmlSchemaObject

**Fields:**

- `id`: string
- `annotation`: XmlSchemaAnnotation

---

#### XmlSchemaAnnotation

**Line:** 763683

**Inherits:** XmlSchemaObject

**Fields:**

- `id`: string
- `items`: XmlSchemaObjectCollection

---

#### XmlSchemaAny

**Line:** 763724

**Inherits:** XmlSchemaParticle

**Fields:**

- `ns`: string
- `processContents`: XmlSchemaContentProcessing
- `namespaceList`: NamespaceList

---

#### XmlSchemaAnyAttribute

**Line:** 763782

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `ns`: string
- `processContents`: XmlSchemaContentProcessing
- `namespaceList`: NamespaceList

---

#### XmlSchemaAppInfo

**Line:** 763840

**Inherits:** XmlSchemaObject

**Fields:**

- `source`: string

---

#### XmlSchemaAttribute

**Line:** 763869

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `defaultValue`: string
- `fixedValue`: string
- `name`: string
- `form`: XmlSchemaForm
- `use`: XmlSchemaUse
- `refName`: XmlQualifiedName
- `typeName`: XmlQualifiedName
- `qualifiedName`: XmlQualifiedName
- `type`: XmlSchemaSimpleType
- `attributeType`: XmlSchemaSimpleType
- `attDef`: SchemaAttDef

---

#### XmlSchemaAttributeGroup

**Line:** 764000

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `name`: string
- `attributes`: XmlSchemaObjectCollection
- `anyAttribute`: XmlSchemaAnyAttribute
- `qname`: XmlQualifiedName
- `redefined`: XmlSchemaAttributeGroup
- `attributeUses`: XmlSchemaObjectTable
- `attributeWildcard`: XmlSchemaAnyAttribute
- `selfReferenceCount`: int

---

#### XmlSchemaAttributeGroupRef

**Line:** 764096

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `refName`: XmlQualifiedName

---

#### XmlSchemaChoice

**Line:** 764118

**Inherits:** XmlSchemaGroupBase

**Fields:**

- `items`: XmlSchemaObjectCollection

---

#### XmlSchemaCollection

**Line:** 764150

**Inherits:** ICollection

**Fields:**

- `collection`: Hashtable
- `nameTable`: XmlNameTable
- `schemaNames`: SchemaNames
- `wLock`: ReaderWriterLock
- `timeout`: int
- `isThreadSafe`: bool
- `validationEventHandler`: ValidationEventHandler
- `xmlResolver`: XmlResolver

---

#### XmlSchemaCollectionEnumerator

**Line:** 764264

**Inherits:** IEnumerator

**Fields:**

- `enumerator`: IDictionaryEnumerator

---

#### XmlSchemaCompilationSettings

**Line:** 764299

**Fields:**

- `enableUpaCheck`: bool

---

#### XmlSchemaComplexContent

**Line:** 764317

**Inherits:** XmlSchemaContentModel

**Fields:**

- `content`: XmlSchemaContent
- `isMixed`: bool
- `hasMixedAttribute`: bool

---

#### XmlSchemaComplexContentExtension

**Line:** 764355

**Inherits:** XmlSchemaContent

**Fields:**

- `particle`: XmlSchemaParticle
- `attributes`: XmlSchemaObjectCollection
- `anyAttribute`: XmlSchemaAnyAttribute
- `baseTypeName`: XmlQualifiedName

---

#### XmlSchemaComplexContentRestriction

**Line:** 764408

**Inherits:** XmlSchemaContent

**Fields:**

- `particle`: XmlSchemaParticle
- `attributes`: XmlSchemaObjectCollection
- `anyAttribute`: XmlSchemaAnyAttribute
- `baseTypeName`: XmlQualifiedName

---

#### XmlSchemaComplexType

**Line:** 764461

**Inherits:** XmlSchemaType

**Fields:**

- `block`: XmlSchemaDerivationMethod
- `contentModel`: XmlSchemaContentModel
- `particle`: XmlSchemaParticle
- `attributes`: XmlSchemaObjectCollection
- `anyAttribute`: XmlSchemaAnyAttribute
- `contentTypeParticle`: XmlSchemaParticle
- `blockResolved`: XmlSchemaDerivationMethod
- `localElements`: XmlSchemaObjectTable
- `attributeUses`: XmlSchemaObjectTable
- `attributeWildcard`: XmlSchemaAnyAttribute
- `pvFlags`: byte

---

#### XmlSchemaContent

**Line:** 764645

**Inherits:** XmlSchemaAnnotated

---

#### XmlSchemaContentModel

**Line:** 764654

**Inherits:** XmlSchemaAnnotated

---

#### XmlSchemaDatatype

**Line:** 764699

---

#### XmlSchemaDocumentation

**Line:** 764832

**Inherits:** XmlSchemaObject

**Fields:**

- `source`: string
- `language`: string

---

#### XmlSchemaElement

**Line:** 764868

**Inherits:** XmlSchemaParticle

**Fields:**

- `isAbstract`: bool
- `hasAbstractAttribute`: bool
- `isNillable`: bool
- `hasNillableAttribute`: bool
- `isLocalTypeDerivationChecked`: bool
- `block`: XmlSchemaDerivationMethod
- `final`: XmlSchemaDerivationMethod
- `form`: XmlSchemaForm
- `defaultValue`: string
- `fixedValue`: string
- `name`: string
- `refName`: XmlQualifiedName
- `substitutionGroup`: XmlQualifiedName
- `typeName`: XmlQualifiedName
- `type`: XmlSchemaType
- `qualifiedName`: XmlQualifiedName
- `elementType`: XmlSchemaType
- `blockResolved`: XmlSchemaDerivationMethod
- `finalResolved`: XmlSchemaDerivationMethod
- `constraints`: XmlSchemaObjectCollection
- ... (1 more fields)

---

#### XmlSchemaEnumerationFacet

**Line:** 765370

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaException

**Line:** 765094

**Inherits:** SystemException

**Fields:**

- `res`: string
- `sourceUri`: string
- `lineNumber`: int
- `linePosition`: int
- `sourceSchemaObject`: XmlSchemaObject
- `message`: string

---

#### XmlSchemaExternal

**Line:** 765196

**Inherits:** XmlSchemaObject

**Fields:**

- `location`: string
- `baseUri`: Uri
- `schema`: XmlSchema
- `id`: string
- `compositor`: Compositor

---

#### XmlSchemaFacet

**Line:** 765285

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `value`: string
- `isFixed`: bool
- `facetType`: FacetType

---

#### XmlSchemaFractionDigitsFacet

**Line:** 765424

**Inherits:** XmlSchemaNumericFacet

---

#### XmlSchemaGroup

**Line:** 765455

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `name`: string
- `particle`: XmlSchemaGroupBase
- `canonicalParticle`: XmlSchemaParticle
- `qname`: XmlQualifiedName
- `redefined`: XmlSchemaGroup
- `selfReferenceCount`: int

---

#### XmlSchemaGroupBase

**Line:** 765538

**Inherits:** XmlSchemaParticle

---

#### XmlSchemaGroupRef

**Line:** 765557

**Inherits:** XmlSchemaParticle

**Fields:**

- `refName`: XmlQualifiedName
- `particle`: XmlSchemaGroupBase
- `refined`: XmlSchemaGroup

---

#### XmlSchemaIdentityConstraint

**Line:** 765597

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `name`: string
- `selector`: XmlSchemaXPath
- `fields`: XmlSchemaObjectCollection
- `qualifiedName`: XmlQualifiedName
- `compiledConstraint`: CompiledIdentityConstraint

---

#### XmlSchemaImport

**Line:** 765723

**Inherits:** XmlSchemaExternal

**Fields:**

- `ns`: string
- `annotation`: XmlSchemaAnnotation

---

#### XmlSchemaInclude

**Line:** 765749

**Inherits:** XmlSchemaExternal

**Fields:**

- `annotation`: XmlSchemaAnnotation

---

#### XmlSchemaInference

**Line:** 760324

**Fields:**

- `rootSchema`: XmlSchema
- `schemaSet`: XmlSchemaSet
- `xtr`: XmlReader
- `nametable`: NameTable
- `TargetNamespace`: string
- `NamespaceManager`: XmlNamespaceManager
- `schemaList`: ArrayList

---

#### XmlSchemaInferenceException

**Line:** 760457

**Inherits:** XmlSchemaException

---

#### XmlSchemaInfo

**Line:** 765764

**Inherits:** IXmlSchemaInfo

**Fields:**

- `isDefault`: bool
- `isNil`: bool
- `schemaElement`: XmlSchemaElement
- `schemaAttribute`: XmlSchemaAttribute
- `schemaType`: XmlSchemaType
- `memberType`: XmlSchemaSimpleType
- `validity`: XmlSchemaValidity
- `contentType`: XmlSchemaContentType

---

#### XmlSchemaKey

**Line:** 765692

**Inherits:** XmlSchemaIdentityConstraint

---

#### XmlSchemaKeyref

**Line:** 765701

**Inherits:** XmlSchemaIdentityConstraint

**Fields:**

- `refer`: XmlQualifiedName

---

#### XmlSchemaLengthFacet

**Line:** 765334

**Inherits:** XmlSchemaNumericFacet

---

#### XmlSchemaMaxExclusiveFacet

**Line:** 765397

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaMaxInclusiveFacet

**Line:** 765406

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaMaxLengthFacet

**Line:** 765352

**Inherits:** XmlSchemaNumericFacet

---

#### XmlSchemaMinExclusiveFacet

**Line:** 765379

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaMinInclusiveFacet

**Line:** 765388

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaMinLengthFacet

**Line:** 765343

**Inherits:** XmlSchemaNumericFacet

---

#### XmlSchemaNotation

**Line:** 765856

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `name`: string
- `publicId`: string
- `systemId`: string
- `qname`: XmlQualifiedName

---

#### XmlSchemaNumericFacet

**Line:** 765325

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaObject

**Line:** 765913

**Fields:**

- `lineNum`: int
- `linePos`: int
- `sourceUri`: string
- `namespaces`: XmlSerializerNamespaces
- `parent`: XmlSchemaObject
- `isProcessing`: bool

---

#### XmlSchemaObjectCollection

**Line:** 766015

**Inherits:** CollectionBase

**Fields:**

- `parent`: XmlSchemaObject

---

#### XmlSchemaObjectEnumerator

**Line:** 766066

**Inherits:** IEnumerator

**Fields:**

- `enumerator`: IEnumerator

---

#### XmlSchemaObjectTable

**Line:** 766206

**Fields:**

- `table`: Dictionary<XmlQualifiedName, XmlSchemaObject>
- `entries`: List<XmlSchemaObjectTable.XmlSchemaObjectEntry>

---

#### XmlSchemaParticle

**Line:** 766283

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `minOccurs`: Decimal
- `maxOccurs`: Decimal

---

#### XmlSchemaPatternFacet

**Line:** 765361

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaProviderAttribute

**Line:** 754293

**Inherits:** Attribute

**Fields:**

- `_methodName`: string
- `_isAny`: bool

---

#### XmlSchemaRedefine

**Line:** 766346

**Inherits:** XmlSchemaExternal

**Fields:**

- `items`: XmlSchemaObjectCollection
- `attributeGroups`: XmlSchemaObjectTable
- `types`: XmlSchemaObjectTable
- `groups`: XmlSchemaObjectTable

---

#### XmlSchemaSequence

**Line:** 766390

**Inherits:** XmlSchemaGroupBase

**Fields:**

- `items`: XmlSchemaObjectCollection

---

#### XmlSchemaSet

**Line:** 766420

**Fields:**

- `nameTable`: XmlNameTable
- `schemaNames`: SchemaNames
- `schemas`: SortedList
- `internalEventHandler`: ValidationEventHandler
- `eventHandler`: ValidationEventHandler
- `isCompiled`: bool
- `schemaLocations`: Hashtable
- `chameleonSchemas`: Hashtable
- `targetNamespaces`: Hashtable
- `compileAll`: bool
- `cachedCompiledInfo`: SchemaInfo
- `readerSettings`: XmlReaderSettings
- `schemaForSchema`: XmlSchema
- `compilationSettings`: XmlSchemaCompilationSettings
- `typeExtensions`: XmlSchemaObjectTable
- `internalSyncObject`: object

---

#### XmlSchemaSimpleContent

**Line:** 766617

**Inherits:** XmlSchemaContentModel

**Fields:**

- `content`: XmlSchemaContent

---

#### XmlSchemaSimpleContentExtension

**Line:** 766640

**Inherits:** XmlSchemaContent

**Fields:**

- `attributes`: XmlSchemaObjectCollection
- `anyAttribute`: XmlSchemaAnyAttribute
- `baseTypeName`: XmlQualifiedName

---

#### XmlSchemaSimpleContentRestriction

**Line:** 766681

**Inherits:** XmlSchemaContent

**Fields:**

- `baseTypeName`: XmlQualifiedName
- `baseType`: XmlSchemaSimpleType
- `facets`: XmlSchemaObjectCollection
- `attributes`: XmlSchemaObjectCollection
- `anyAttribute`: XmlSchemaAnyAttribute

---

#### XmlSchemaSimpleType

**Line:** 766748

**Inherits:** XmlSchemaType

**Fields:**

- `content`: XmlSchemaSimpleTypeContent

---

#### XmlSchemaSimpleTypeContent

**Line:** 766775

**Inherits:** XmlSchemaAnnotated

---

#### XmlSchemaSimpleTypeList

**Line:** 766784

**Inherits:** XmlSchemaSimpleTypeContent

**Fields:**

- `itemTypeName`: XmlQualifiedName
- `itemType`: XmlSchemaSimpleType
- `baseItemType`: XmlSchemaSimpleType

---

#### XmlSchemaSimpleTypeRestriction

**Line:** 766827

**Inherits:** XmlSchemaSimpleTypeContent

**Fields:**

- `baseTypeName`: XmlQualifiedName
- `baseType`: XmlSchemaSimpleType
- `facets`: XmlSchemaObjectCollection

---

#### XmlSchemaSimpleTypeUnion

**Line:** 766878

**Inherits:** XmlSchemaSimpleTypeContent

**Fields:**

- `baseTypes`: XmlSchemaObjectCollection

---

#### XmlSchemaTotalDigitsFacet

**Line:** 765415

**Inherits:** XmlSchemaNumericFacet

---

#### XmlSchemaType

**Line:** 766965

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `name`: string
- `final`: XmlSchemaDerivationMethod
- `derivedBy`: XmlSchemaDerivationMethod
- `baseSchemaType`: XmlSchemaType
- `datatype`: XmlSchemaDatatype
- `finalResolved`: XmlSchemaDerivationMethod
- `elementDecl`: SchemaElementDecl
- `qname`: XmlQualifiedName
- `redefined`: XmlSchemaType
- `contentType`: XmlSchemaContentType

---

#### XmlSchemaUnique

**Line:** 765683

**Inherits:** XmlSchemaIdentityConstraint

---

#### XmlSchemaValidationException

**Line:** 767124

**Inherits:** XmlSchemaException

---

#### XmlSchemaValidator

**Line:** 767208

**Fields:**

- `schemaSet`: XmlSchemaSet
- `validationFlags`: XmlSchemaValidationFlags
- `startIDConstraint`: int
- `isRoot`: bool
- `rootHasSchema`: bool
- `attrValid`: bool
- `checkEntity`: bool
- `compiledSchemaInfo`: SchemaInfo
- `dtdSchemaInfo`: IDtdInfo
- `validatedNamespaces`: Hashtable
- `validationStack`: HWStack
- `context`: ValidationState
- `currentState`: ValidatorState
- `attPresence`: Hashtable
- `wildID`: SchemaAttDef
- `IDs`: Hashtable
- `idRefListHead`: IdRefNode
- `contextQName`: XmlQualifiedName
- `NsXs`: string
- `NsXsi`: string
- ... (19 more fields)

---

#### XmlSchemaWhiteSpaceFacet

**Line:** 765433

**Inherits:** XmlSchemaFacet

---

#### XmlSchemaXPath

**Line:** 765660

**Inherits:** XmlSchemaAnnotated

**Fields:**

- `xpath`: string

---

#### XmlSerializationCollectionFixupCallback

**Line:** 754319

**Inherits:** MulticastDelegate

---

#### XmlSerializationFixupCallback

**Line:** 754331

**Inherits:** MulticastDelegate

---

#### XmlSerializationGeneratedCode

**Line:** 754343

---

#### XmlSerializationReadCallback

**Line:** 754352

**Inherits:** MulticastDelegate

---

#### XmlSerializationReader

**Line:** 754472

**Inherits:** XmlSerializationGeneratedCode

**Fields:**

- `document`: XmlDocument
- `reader`: XmlReader
- `fixups`: ArrayList
- `collFixups`: Hashtable
- `collItemFixups`: ArrayList
- `typesCallbacks`: Hashtable
- `noIDTargets`: ArrayList
- `targets`: Hashtable
- `delayedListFixups`: Hashtable
- `eventSource`: XmlSerializer
- `delayedFixupId`: int
- `referencedObjects`: Hashtable
- `readCount`: int
- `whileIterationCount`: int
- `w3SchemaNS`: string
- `w3InstanceNS`: string
- `w3InstanceNS2000`: string
- `w3InstanceNS1999`: string
- `soapNS`: string
- `wsdlNS`: string
- ... (5 more fields)

---

#### XmlSerializationWriteCallback

**Line:** 754824

**Inherits:** MulticastDelegate

---

#### XmlSerializationWriter

**Line:** 754851

**Inherits:** XmlSerializationGeneratedCode

**Fields:**

- `idGenerator`: ObjectIDGenerator
- `qnameCount`: int
- `topLevelElement`: bool
- `namespaces`: ArrayList
- `writer`: XmlWriter
- `referencedElements`: Queue
- `callbacks`: Hashtable
- `serializedObjects`: Hashtable

---

#### XmlSerializer

**Line:** 755139

**Fields:**

- `customSerializer`: bool
- `typeMapping`: XmlMapping
- `onUnreferencedObject`: UnreferencedObjectEventHandler
- `onUnknownAttribute`: XmlAttributeEventHandler
- `onUnknownElement`: XmlElementEventHandler
- `onUnknownNode`: XmlNodeEventHandler

---

#### XmlSerializerFactory

**Line:** 755216

---

#### XmlSerializerImplementation

**Line:** 755240

---

#### XmlSerializerNamespaces

**Line:** 752978

**Fields:**

- `namespaces`: Hashtable

---

#### XmlSignificantWhitespace

**Line:** 750345

**Inherits:** XmlCharacterData

---

#### XmlSource

**Line:** 1322357

**Inherits:** ISource

---

#### XmlSyntaxException

**Line:** 216664

**Inherits:** SystemException

---

#### XmlText

**Line:** 750392

**Inherits:** XmlCharacterData

---

#### XmlTextAttribute

**Line:** 755253

**Inherits:** Attribute

**Fields:**

- `dataType`: string
- `type`: Type

---

#### XmlTextReader

**Line:** 743787

**Inherits:** XmlReader

**Fields:**

- `impl`: XmlTextReaderImpl

---

#### XmlTextWriter

**Line:** 745550

**Inherits:** XmlWriter

**Fields:**

- `textWriter`: TextWriter
- `xmlEncoder`: XmlTextEncoder
- `encoding`: Encoding
- `formatting`: Formatting
- `indented`: bool
- `indentation`: int
- `indentChar`: char
- `top`: int
- `base64Encoder`: XmlTextWriterBase64Encoder
- `quoteChar`: char
- `curQuoteChar`: char
- `namespaces`: bool
- `prefixForXmlNs`: string
- `flush`: bool
- `nsTop`: int
- `nsHashtable`: Dictionary<string, int>
- `useNsHashtable`: bool
- `xmlCharType`: XmlCharType

---

#### XmlTypeAttribute

**Line:** 755280

**Inherits:** Attribute

**Fields:**

- `includeInSchema`: bool
- `ns`: string
- `typeName`: string

---

#### XmlTypeMapping

**Line:** 755720

**Inherits:** XmlMapping

**Fields:**

- `xmlType`: string
- `xmlTypeNamespace`: string
- `type`: TypeData
- `baseMap`: XmlTypeMapping
- `multiReferenceType`: bool
- `includeInSchema`: bool
- `isNullable`: bool
- `isAny`: bool
- `_derivedTypes`: ArrayList

---

#### XmlUrlResolver

**Line:** 752593

**Inherits:** XmlResolver

**Fields:**

- `_credentials`: ICredentials
- `_proxy`: IWebProxy
- `_cachePolicy`: RequestCachePolicy

---

#### XmlValidatingReader

**Line:** 746041

**Inherits:** XmlReader

**Fields:**

- `impl`: XmlValidatingReaderImpl

---

#### XmlValueGetter

**Line:** 767148

**Inherits:** MulticastDelegate

---

#### XmlWhitespace

**Line:** 750485

**Inherits:** XmlCharacterData

---

#### XmlWriter

**Line:** 746912

**Inherits:** IDisposable

---

#### XmlWriterSettings

**Line:** 747072

**Fields:**

- `useAsync`: bool
- `encoding`: Encoding
- `omitXmlDecl`: bool
- `newLineHandling`: NewLineHandling
- `newLineChars`: string
- `indent`: TriState
- `indentChars`: string
- `newLineOnAttributes`: bool
- `closeOutput`: bool
- `namespaceHandling`: NamespaceHandling
- `conformanceLevel`: ConformanceLevel
- `checkCharacters`: bool
- `writeEndDocumentOnClose`: bool
- `outputMethod`: XmlOutputMethod
- `cdataSections`: List<XmlQualifiedName>
- `doNotEscapeUriAttributes`: bool
- `mergeCDataSections`: bool
- `mediaType`: string
- `docTypeSystem`: string
- `docTypePublic`: string
- ... (3 more fields)

---

#### YearMonthPattern

**Line:** 1158903

**Inherits:** IPattern

---

#### YieldInstruction

**Line:** 884728

---

#### YouMadeALotOfProgressPopupSystem

**Line:** 733869

**Inherits:** IInitSystem

**Fields:**

- `_shownBattleIdsPopups`: List<MainBattleId>

---

#### ZoneEqualityComparer

**Line:** 1149938

**Inherits:** IEqualityComparer

---

#### ZoneInterval

**Line:** 1149987

**Inherits:** IEquatable

---

#### ZoneLocalMapping

**Line:** 1150125

---

#### ZoneLocalMappingResolver

**Line:** 1148644

**Inherits:** MulticastDelegate

---

#### ZonedClock

**Line:** 1147067

**Inherits:** IClock

---

#### ZonedDateTime

**Line:** 1147126

---

#### ZonedDateTimePattern

**Line:** 1159183

**Inherits:** IPattern

---

#### iOSGoogleSignIn

**Line:** 1591705

**Inherits:** MonoBehaviour

**Fields:**

- `_isLoading`: bool
- `_idToken`: string
- `_errorMessage`: string

---

### Enums (1042)

#### APVConstantBufferRegister

**Line:** 820291

**Values:**

- `GlobalRegister` = 6

---

#### APVLeakReductionMode

**Line:** 820300

**Values:**

- `None` = 0
- `Performance` = 1
- `Quality` = 2
- `ValidityBased` = 1
- `ValidityAndNormalBased` = 2

---

#### AcceptRejectRule

**Line:** 1083069

**Values:**

- `None` = 0
- `Cascade` = 1

---

#### AccessFlags

**Line:** 829126

**Values:**

- `None` = 0
- `Read` = 1
- `Write` = 2
- `Discard` = 4
- `WriteAll` = 6
- `ReadWrite` = 3

---

#### ActivityIdFormat

**Line:** 1417492

**Values:**

- `Unknown` = 0
- `Hierarchical` = 1
- `W3C` = 2

---

#### ActivityKind

**Line:** 1418154

**Values:**

- `Internal` = 0
- `Server` = 1
- `Client` = 2
- `Producer` = 3
- `Consumer` = 4

---

#### ActivitySamplingResult

**Line:** 1418091

**Values:**

- `None` = 0
- `PropagationData` = 1
- `AllData` = 2
- `AllDataAndRecorded` = 3

---

#### ActivityStatusCode

**Line:** 1417624

**Values:**

- `Unset` = 0
- `Ok` = 1
- `Error` = 2

---

#### ActivityTraceFlags

**Line:** 1417483

**Values:**

- `None` = 0
- `Recorded` = 1

---

#### ActivityTrackingOptions

**Line:** 1553877

**Values:**

- `None` = 0
- `SpanId` = 1
- `TraceId` = 2
- `ParentId` = 4
- `TraceState` = 8
- `TraceFlags` = 16
- `Tags` = 32
- `Baggage` = 64

---

#### AdditionalCanvasShaderChannels

**Line:** 1576383

**Values:**

- `None` = 0
- `TexCoord1` = 1
- `TexCoord2` = 2
- `TexCoord3` = 4
- `Normal` = 8
- `Tangent` = 16

---

#### AddressFamily

**Line:** 800285

**Values:**

- `Unspecified` = 0
- `Unix` = 1
- `InterNetwork` = 2
- `ImpLink` = 3
- `Pup` = 4
- `Chaos` = 5
- `NS` = 6
- `Ipx` = 6
- `Iso` = 7
- `Osi` = 7
- `Ecma` = 8
- `DataKit` = 9
- `Ccitt` = 10
- `Sna` = 11
- `DecNet` = 12
- `DataLink` = 13
- `Lat` = 14
- `HyperChannel` = 15
- `AppleTalk` = 16
- `NetBios` = 17
- `VoiceView` = 18
- `FireFox` = 19
- `Banyan` = 21
- `Atm` = 22
- `InterNetworkV6` = 23
- `Cluster` = 24
- `Ieee12844` = 25
- `Irda` = 26
- `NetworkDesigners` = 28
- `Max` = 29

---

#### Addressables

**Line:** 1453852

---

#### AddressablesPlatform

**Line:** 1455988

**Values:**

- `Unknown` = 0
- `Windows` = 1
- `OSX` = 2
- `Linux` = 3
- `PS4` = 4
- `Switch` = 5
- `XboxOne` = 6
- `WebGL` = 7
- `iOS` = 8
- `Android` = 9
- `WindowsUniversal` = 10

---

#### AdminActionPlacement

**Line:** 601164

**Values:**

- `Gentle` = 0
- `Disruptive` = 1
- `Dangerous` = 2

---

#### AdvancedUpscalers

**Line:** 809859

**Values:**

- `DLSS` = 0
- `FSR2` = 1
- `STP` = 2

---

#### AlertDescription

**Line:** 1448527

**Values:**

- `CloseNotify` = 0
- `UnexpectedMessage` = 10
- `BadRecordMAC` = 20
- `DecryptionFailed_RESERVED` = 21
- `RecordOverflow` = 22
- `DecompressionFailure` = 30
- `HandshakeFailure` = 40
- `NoCertificate_RESERVED` = 41
- `BadCertificate` = 42
- `UnsupportedCertificate` = 43
- `CertificateRevoked` = 44
- `CertificateExpired` = 45
- `CertificateUnknown` = 46
- `IlegalParameter` = 47
- `UnknownCA` = 48
- `AccessDenied` = 49
- `DecodeError` = 50
- `DecryptError` = 51
- `ExportRestriction` = 60
- `ProtocolVersion` = 70
- `InsuficientSecurity` = 71
- `InternalError` = 80
- `UserCancelled` = 90
- `NoRenegotiation` = 100
- `UnsupportedExtension` = 110

---

#### Align

**Line:** 659892

**Values:**

- `Auto` = 0
- `FlexStart` = 1
- `Center` = 2
- `FlexEnd` = 3
- `Stretch` = 4

---

#### Allocator

**Line:** 838032

**Values:**

- `Invalid` = 0
- `None` = 1
- `Temp` = 2
- `TempJob` = 3
- `Persistent` = 4
- `AudioKernel` = 5
- `Domain` = 6
- `FirstUserIndex` = 64

---

#### AlternatingRowBackground

**Line:** 615329

**Values:**

- `None` = 0
- `ContentOnly` = 1
- `All` = 2

---

#### AnalyticsResult

**Line:** 1586968

**Values:**

- `Ok` = 0
- `NotInitialized` = 1
- `AnalyticsDisabled` = 2
- `TooManyItems` = 3
- `SizeLimitReached` = 4
- `TooManyRequests` = 5
- `InvalidData` = 6
- `UnsupportedPlatform` = 7

---

#### AnalyticsSessionState

**Line:** 1585329

**Values:**

- `kSessionStopped` = 0
- `kSessionStarted` = 1
- `kSessionPaused` = 2
- `kSessionResumed` = 3

---

#### AndroidAssetPackError

**Line:** 1487123

**Values:**

- `NoError` = 0

---

#### AndroidAssetPackStatus

**Line:** 1487107

**Values:**

- `Unknown` = 0
- `Pending` = 1
- `Downloading` = 2
- `Transferring` = 3
- `Completed` = 4
- `Failed` = 5
- `Canceled` = 6
- `WaitingForWifi` = 7
- `NotInstalled` = 8

---

#### AndroidColorModeHdr

**Line:** 1487411

**Values:**

- `Undefined` = 0
- `No` = 4
- `Yes` = 8

---

#### AndroidColorModeWideColorGamut

**Line:** 1487421

**Values:**

- `Undefined` = 0
- `No` = 1
- `Yes` = 2

---

#### AndroidKeyboard

**Line:** 1487683

**Values:**

- `Undefined` = 0
- `NoKeys` = 1
- `Qwerty` = 2
- `_12Key` = 3

---

#### AndroidKeyboardHidden

**Line:** 1487694

**Values:**

- `Undefined` = 0
- `No` = 1
- `Yes` = 2

---

#### AndroidNavigation

**Line:** 1487704

**Values:**

- `Undefined` = 0
- `NoNav` = 1
- `Dpad` = 2
- `TrackBall` = 3
- `Wheel` = 4

---

#### AndroidNavigationHidden

**Line:** 1487716

**Values:**

- `Undefined` = 0
- `No` = 1
- `Yes` = 2

---

#### AndroidOrientation

**Line:** 1487726

**Values:**

- `Undefined` = 0
- `Portrait` = 1
- `Landscape` = 2

---

#### AndroidScreenLayoutDirection

**Line:** 1487736

**Values:**

- `LTR` = 64
- `RTL` = 128

---

#### AndroidScreenLayoutLong

**Line:** 1487745

**Values:**

- `Undefined` = 0
- `No` = 16
- `Yes` = 32

---

#### AndroidScreenLayoutRound

**Line:** 1487755

**Values:**

- `Undefined` = 0
- `No` = 256
- `Yes` = 512

---

#### AndroidScreenLayoutSize

**Line:** 1487765

**Values:**

- `Undefined` = 0
- `Small` = 1
- `Normal` = 2
- `Large` = 3
- `XLarge` = 4

---

#### AndroidStore

**Line:** 1402110

**Values:**

- `GooglePlay` = 0
- `AmazonAppStore` = 1
- `UDP` = 2
- `NotSpecified` = 3

---

#### AndroidStoreMeta

**Line:** 1402121

**Values:**

- `AndroidStoreStart` = 0
- `AndroidStoreEnd` = 2

---

#### AndroidTouchScreen

**Line:** 1487777

**Values:**

- `Undefined` = 0
- `NoTouch` = 1
- `Finger` = 3

---

#### AndroidUIModeNight

**Line:** 1487787

**Values:**

- `Undefined` = 0
- `No` = 16
- `Yes` = 32

---

#### AndroidUIModeType

**Line:** 1487797

**Values:**

- `Undefined` = 0
- `Normal` = 1
- `Desk` = 2
- `Car` = 3
- `Television` = 4
- `Appliance` = 5
- `Watch` = 6
- `VrHeadset` = 7

---

#### AngleUnit

**Line:** 644512

**Values:**

- `Degree` = 0
- `Gradian` = 1
- `Radian` = 2
- `Turn` = 3

---

#### AngularFalloffType

**Line:** 898871

**Values:**

- `LUT` = 0
- `AnalyticAndInnerAngle` = 1

---

#### AnimatableProperty

**Line:** 1563324

---

#### AntialiasingMode

**Line:** 914941

**Values:**

- `None` = 0
- `FastApproximateAntialiasing` = 1
- `SubpixelMorphologicalAntiAliasing` = 2
- `TemporalAntiAliasing` = 3

---

#### AntialiasingQuality

**Line:** 914965

**Values:**

- `Low` = 0
- `Medium` = 1
- `High` = 2

---

#### AppPauseType

**Line:** 684368

**Values:**

- `User` = 0
- `Ad` = 1
- `Shop` = 2

---

#### AppStore

**Line:** 1406158

**Values:**

- `NotSpecified` = 0
- `GooglePlay` = 1
- `AmazonAppStore` = 2
- `UDP` = 3
- `MacAppStore` = 4
- `AppleAppStore` = 5
- `WinRT` = 6
- `fake` = 7

---

#### AppStoreMeta

**Line:** 1406174

**Values:**

- `AndroidStoreStart` = 1
- `AndroidStoreEnd` = 3

---

#### AppUpdateErrorCode

**Line:** 1578764

**Values:**

- `NoError` = 0
- `NoErrorPartiallyAllowed` = 1
- `ErrorUnknown` = 2
- `ErrorApiNotAvailable` = 3
- `ErrorInvalidRequest` = 4
- `ErrorUpdateUnavailable` = 5
- `ErrorUpdateNotAllowed` = 6
- `ErrorDownloadNotPresent` = 7
- `ErrorUpdateInProgress` = 8
- `ErrorInternalError` = 9
- `ErrorUserCanceled` = 10
- `ErrorUpdateFailed` = 11
- `ErrorPlayStoreNotFound` = 12
- `ErrorAppNotOwned` = 13

---

#### AppUpdateStatus

**Line:** 1579005

**Values:**

- `Unknown` = 0
- `Pending` = 1
- `Downloading` = 2
- `Downloaded` = 3
- `Installing` = 4
- `Installed` = 5
- `Failed` = 6
- `Canceled` = 7

---

#### AppUpdateType

**Line:** 1579020

**Values:**

- `Flexible` = 0
- `Immediate` = 1

---

#### AppleStorePromotionVisibility

**Line:** 1405883

**Values:**

- `Default` = 0
- `Hide` = 1
- `Show` = 2

---

#### ApplicationInstallMode

**Line:** 870396

**Values:**

- `Unknown` = 0
- `Store` = 1
- `DeveloperBuild` = 2
- `Adhoc` = 3
- `Enterprise` = 4
- `Editor` = 5

---

#### ApplicationMemoryUsage

**Line:** 870343

**Values:**

- `Unknown` = 0
- `Low` = 1
- `Medium` = 2
- `High` = 3
- `Critical` = 4

---

#### ApplicationPauseStatus

**Line:** 1308176

**Values:**

- `Running` = 0
- `Pausing` = 1
- `ResumedFromPauseThisFrame` = 2

---

#### ApplicationStateManager

**Line:** 738070

---

#### Architecture

**Line:** 228832

**Values:**

- `X86` = 0
- `X64` = 1
- `Arm` = 2
- `Arm64` = 3

---

#### ArchiveStatus

**Line:** 837887

**Values:**

- `InProgress` = 0
- `Complete` = 1
- `Failed` = 2

---

#### Asn1EndOfIndefiniteLengthNodeType

**Line:** 1543961

**Values:**

- `EndOfStream` = 0
- `EndOfNodeFooter` = 1
- `NotEnd` = 2

---

#### AspectRatioFitter

**Line:** 1354273

---

#### AssemblyContentType

**Line:** 264940

**Values:**

- `Default` = 0
- `WindowsRuntime` = 1

---

#### AssemblyHashAlgorithm

**Line:** 275928

**Values:**

- `None` = 0
- `MD5` = 32771
- `SHA1` = 32772
- `SHA256` = 32780
- `SHA384` = 32781
- `SHA512` = 32782

---

#### AssemblyNameFlags

**Line:** 265078

**Values:**

- `None` = 0
- `PublicKey` = 1
- `EnableJITcompileOptimizer` = 16384
- `EnableJITcompileTracking` = 32768
- `Retargetable` = 256

---

#### AssemblyVersionCompatibility

**Line:** 275941

**Values:**

- `SameMachine` = 1
- `SameProcess` = 2
- `SameDomain` = 3

---

#### AssetBundleResource

**Line:** 1436670

---

#### AssetLoadMode

**Line:** 1436521

**Values:**

- `RequestedAssetAndDependencies` = 0
- `AllPackedAssetsAndDependencies` = 1

---

#### AssetLoadingSubsystem

**Line:** 837600

**Values:**

- `Other` = 0
- `Texture` = 1
- `VirtualTexture` = 2
- `Mesh` = 3
- `Audio` = 4
- `Scripts` = 5
- `EntitiesScene` = 6
- `EntitiesStreamBinaryReader` = 7
- `FileInfo` = 8
- `ContentLoading` = 9

---

#### AstNode

**Line:** 769987

---

#### AsyncOperationStatus

**Line:** 1441281

**Values:**

- `None` = 0
- `Succeeded` = 1
- `Failed` = 2

---

#### AsynchronousBehaviour

**Line:** 1318500

**Values:**

- `Default` = 0
- `ForceSynchronous` = 1

---

#### AtlasPopulationMode

**Line:** 1347192

**Values:**

- `Static` = 0
- `Dynamic` = 1
- `DynamicOS` = 2

---

#### AttributeTargets

**Line:** 20437

**Values:**

- `Assembly` = 1
- `Module` = 2
- `Class` = 4
- `Struct` = 8
- `Enum` = 16
- `Constructor` = 32
- `Method` = 64
- `Property` = 128
- `Field` = 256
- `Event` = 512
- `Interface` = 1024
- `Parameter` = 2048
- `Delegate` = 4096
- `ReturnValue` = 8192
- `GenericParameter` = 16384
- `All` = 32767

---

#### AuthenticationPlatform

**Line:** 499195

**Values:**

- `DeviceId` = 0
- `Development` = 1
- `GooglePlay` = 2
- `GameCenter` = 3
- `GoogleSignIn` = 4
- `SignInWithApple` = 5
- `FacebookLogin` = 6
- `SignInWithAppleTransfer` = 7
- `GameCenter2020` = 8
- `GameCenter2020UAGT` = 9
- `_ReservedDontUse1` = 10
- `Ethereum` = 11
- `ImmutableX` = 12
- `CompanyAccount` = 13
- `_ReservedDontUse2` = 14
- `Steam` = 15
- `WebLogin` = 16
- `_ReservedDontUse3` = 17

---

#### AuthenticationSchemes

**Line:** 791365

**Values:**

- `None` = 0
- `Digest` = 1
- `Negotiate` = 2
- `Ntlm` = 4
- `Basic` = 8
- `Anonymous` = 32768
- `IntegratedWindowsAuthentication` = 6

---

#### AuthenticationTokenProvider

**Line:** 577134

**Values:**

- `None` = 0
- `Google` = 1
- `OAuth2` = 2

---

#### AuthorizationErrorCode

**Line:** 1590207

**Values:**

- `Unknown` = 1000
- `Canceled` = 1001
- `InvalidResponse` = 1002
- `NotHandled` = 1003
- `Failed` = 1004

---

#### AuthorizationStatus

**Line:** 1564114

**Values:**

- `AUTHORIZED` = 0
- `DENIED` = 1
- `NOT_DETERMINED` = 2
- `RESTRICTED` = 3

---

#### AutoPlay

**Line:** 1424903

**Values:**

- `None` = 0
- `AutoPlaySequences` = 1
- `AutoPlayTweeners` = 2
- `All` = 3

---

#### AvgResetInterval

**Line:** 1590680

**Values:**

- `Always` = 1
- `VeryFast` = 30
- `Fast` = 60
- `Normal` = 120
- `Slow` = 300
- `Never` = 2147483647

---

#### Axis

**Line:** 770022

---

#### AxisConstraint

**Line:** 1424915

**Values:**

- `None` = 0
- `X` = 2
- `Y` = 4
- `Z` = 8
- `W` = 16

---

#### BackgroundPositionKeyword

**Line:** 659977

**Values:**

- `Center` = 0
- `Top` = 1
- `Bottom` = 2
- `Left` = 3
- `Right` = 4

---

#### BackgroundSizeType

**Line:** 660000

**Values:**

- `Length` = 0
- `Cover` = 1
- `Contain` = 2

---

#### BadRequestType

**Line:** 685161

**Values:**

- `Unspecified` = 0
- `NoUserTokenSupplied` = 1
- `NoClientVersionSupplied` = 2
- `InvalidClientVersionSupplied` = 3
- `SaveGameIdNotSupplied` = 4
- `DeviceIdNotSupplied` = 5
- `Other` = 6

---

#### Base64FormattingOptions

**Line:** 21984

**Values:**

- `None` = 0
- `InsertLineBreaks` = 1

---

#### BatchBufferTarget

**Line:** 897719

**Values:**

- `Unknown` = 0
- `RawBuffer` = 1
- `ConstantBuffer` = 2

---

#### BatchCullingFlags

**Line:** 897687

**Values:**

- `None` = 0
- `CullLightmappedShadowCasters` = 1

---

#### BatchCullingProjectionType

**Line:** 897709

**Values:**

- `Unknown` = 0
- `Perspective` = 1
- `Orthographic` = 2

---

#### BatchCullingViewType

**Line:** 897696

**Values:**

- `Unknown` = 0
- `Camera` = 1
- `Light` = 2
- `Picking` = 3
- `SelectionOutline` = 4
- `Filtering` = 5

---

#### BatchDrawCommandFlags

**Line:** 897670

**Values:**

- `None` = 0
- `FlipWinding` = 1
- `HasMotion` = 2
- `IsLightMapped` = 4
- `HasSortingPosition` = 8
- `LODCrossFadeKeyword` = 16
- `LODCrossFadeValuePacked` = 32
- `LODCrossFade` = 48
- `UseLegacyLightmapsKeyword` = 64

---

#### BatchDrawCommandType

**Line:** 897658

**Values:**

- `Direct` = 0
- `Indirect` = 1
- `Procedural` = 2
- `ProceduralIndirect` = 3

---

#### BigInteger

**Line:** 1449838

---

#### BigQueryAnalyticsFormatMode

**Line:** 605241

**Values:**

- `Ignore` = 0
- `ExtractDictionaryElements` = 1

---

#### BindingFlags

**Line:** 265160

**Values:**

- `Default` = 0
- `IgnoreCase` = 1
- `DeclaredOnly` = 2
- `Instance` = 4
- `Static` = 8
- `Public` = 16
- `NonPublic` = 32
- `FlattenHierarchy` = 64
- `InvokeMethod` = 256
- `CreateInstance` = 512
- `GetField` = 1024
- `SetField` = 2048
- `GetProperty` = 4096
- `SetProperty` = 8192
- `PutDispProperty` = 16384
- `PutRefDispProperty` = 32768
- `ExactBinding` = 65536
- `SuppressChangeType` = 131072
- `OptionalParamBinding` = 262144
- `IgnoreReturn` = 16777216
- `DoNotWrapExceptions` = 33554432

---

#### BindingMode

**Line:** 608848

**Values:**

- `TwoWay` = 0
- `ToSource` = 1
- `ToTarget` = 2
- `ToTargetOnce` = 3

---

#### BindingSourceSelectionMode

**Line:** 615348

**Values:**

- `Manual` = 0
- `AutoAssign` = 1

---

#### BindingStatus

**Line:** 607235

**Values:**

- `Success` = 0
- `Failure` = 1
- `Pending` = 2

---

#### BindingUpdateTrigger

**Line:** 607177

**Values:**

- `WhenDirty` = 0
- `OnSourceChanged` = 1
- `EveryUpdate` = 2

---

#### BiomeSfx

**Line:** 705716

**Values:**

- `GrassLands` = 0
- `Forest` = 1
- `Jungle` = 3
- `Desert` = 4
- `Snow` = 10
- `PostApocalypse` = 20
- `City` = 30
- `Virtual` = 50
- `None` = 9999

---

#### BlendMode

**Line:** 891736

**Values:**

- `Zero` = 0
- `One` = 1
- `DstColor` = 2
- `SrcColor` = 3
- `OneMinusDstColor` = 4
- `SrcAlpha` = 5
- `OneMinusSrcColor` = 6
- `DstAlpha` = 7
- `OneMinusDstAlpha` = 8
- `SrcAlphaSaturate` = 9
- `OneMinusSrcAlpha` = 10

---

#### BlendOp

**Line:** 891755

**Values:**

- `Add` = 0
- `Subtract` = 1
- `ReverseSubtract` = 2
- `Min` = 3
- `Max` = 4
- `LogicalClear` = 5
- `LogicalSet` = 6
- `LogicalCopy` = 7
- `LogicalCopyInverted` = 8
- `LogicalNoop` = 9
- `LogicalInvert` = 10
- `LogicalAnd` = 11
- `LogicalNand` = 12
- `LogicalOr` = 13
- `LogicalNor` = 14
- `LogicalXor` = 15
- `LogicalEquivalence` = 16
- `LogicalAndReverse` = 17
- `LogicalAndInverted` = 18
- `LogicalOrReverse` = 19
- `LogicalOrInverted` = 20
- `Multiply` = 21
- `Screen` = 22
- `Overlay` = 23
- `Darken` = 24
- `Lighten` = 25
- `ColorDodge` = 26
- `ColorBurn` = 27
- `HardLight` = 28
- `SoftLight` = 29
- `Difference` = 30
- `Exclusion` = 31
- `HSLHue` = 32
- `HSLSaturation` = 33
- `HSLColor` = 34
- `HSLLuminosity` = 35

---

#### BloomDownscaleMode

**Line:** 909135

**Values:**

- `Half` = 0
- `Quarter` = 1

---

#### BoolParameter

**Line:** 826933

---

#### BoundedChannelFullMode

**Line:** 1524525

**Values:**

- `Wait` = 0
- `DropNewest` = 1
- `DropOldest` = 2
- `DropWrite` = 3

---

#### BuiltinRenderTextureType

**Line:** 891855

**Values:**

- `None` = 0
- `CurrentActive` = 1
- `CameraTarget` = 2
- `Depth` = 3
- `DepthNormals` = 4
- `ResolvedDepth` = 5
- `PrepassNormalsSpec` = 7
- `PrepassLight` = 8
- `PrepassLightSpec` = 9
- `GBuffer0` = 10
- `GBuffer1` = 11
- `GBuffer2` = 12
- `GBuffer3` = 13
- `Reflections` = 14
- `MotionVectors` = 15
- `GBuffer4` = 16
- `GBuffer5` = 17
- `GBuffer6` = 18
- `GBuffer7` = 19

---

#### BuiltinShaderDefine

**Line:** 892330

**Values:**

- `UNITY_NO_DXT5nm` = 0
- `UNITY_NO_RGBM` = 1
- `UNITY_USE_NATIVE_HDR` = 2
- `UNITY_ENABLE_REFLECTION_BUFFERS` = 3
- `UNITY_FRAMEBUFFER_FETCH_AVAILABLE` = 4
- `UNITY_ENABLE_NATIVE_SHADOW_LOOKUPS` = 5
- `UNITY_METAL_SHADOWS_USE_POINT_FILTERING` = 6
- `UNITY_NO_CUBEMAP_ARRAY` = 7
- `UNITY_NO_SCREENSPACE_SHADOWS` = 8
- `UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS` = 9
- `UNITY_PBS_USE_BRDF1` = 10
- `UNITY_PBS_USE_BRDF2` = 11
- `UNITY_PBS_USE_BRDF3` = 12
- `UNITY_NO_FULL_STANDARD_SHADER` = 13
- `UNITY_SPECCUBE_BOX_PROJECTION` = 14
- `UNITY_SPECCUBE_BLENDING` = 15
- `UNITY_ENABLE_DETAIL_NORMALMAP` = 16
- `SHADER_API_MOBILE` = 17
- `SHADER_API_DESKTOP` = 18
- `UNITY_HARDWARE_TIER1` = 19
- `UNITY_HARDWARE_TIER2` = 20
- `UNITY_HARDWARE_TIER3` = 21
- `UNITY_COLORSPACE_GAMMA` = 22
- `UNITY_LIGHT_PROBE_PROXY_VOLUME` = 23
- `UNITY_HALF_PRECISION_FRAGMENT_SHADER_REGISTERS` = 24
- `UNITY_LIGHTMAP_DLDR_ENCODING` = 25
- `UNITY_LIGHTMAP_RGBM_ENCODING` = 26
- `UNITY_LIGHTMAP_FULL_HDR` = 27
- `UNITY_VIRTUAL_TEXTURING` = 28
- `UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION` = 29
- `UNITY_ASTC_NORMALMAP_ENCODING` = 30
- `SHADER_API_GLES30` = 31
- `SHADER_API_GLES31` = 32
- `SHADER_API_GLES32` = 33
- `UNITY_UNIFIED_SHADER_PRECISION_MODEL` = 34
- `UNITY_PLATFORM_SUPPORTS_WAVE_32` = 35
- `UNITY_PLATFORM_SUPPORTS_WAVE_64` = 36
- `UNITY_NEEDS_RENDERPASS_FBFETCH_FALLBACK` = 37
- `UNITY_PLATFORM_SUPPORTS_DEPTH_FETCH` = 38

---

#### BurstCompilerService

**Line:** 869185

---

#### BurstExecutionEnvironment

**Line:** 1330476

**Values:**

- `Default` = 0
- `NonDeterministic` = 0
- `Deterministic` = 1

---

#### BurstString

**Line:** 1330801

---

#### ButtonLayoutType

**Line:** 1565283

**Values:**

- `Undefined` = 0
- `Column` = 1
- `Row` = 2
- `Grid` = 3

---

#### ButtonSfx

**Line:** 705814

**Values:**

- `Beveled` = 0
- `Toggle` = 1
- `Simple` = 2

---

#### ButtonType

**Line:** 1565329

**Values:**

- `AcceptAll` = 0
- `DenyAll` = 1
- `More` = 2
- `Save` = 3

---

#### CalendarWeekRule

**Line:** 271044

**Values:**

- `FirstDay` = 0
- `FirstFullWeek` = 1
- `FirstFourDayWeek` = 2

---

#### CallingConvention

**Line:** 229354

**Values:**

- `Winapi` = 1
- `Cdecl` = 2
- `StdCall` = 3
- `ThisCall` = 4
- `FastCall` = 5

---

#### CallingConventions

**Line:** 265189

**Values:**

- `Standard` = 1
- `VarArgs` = 2
- `Any` = 3
- `HasThis` = 32
- `ExplicitThis` = 64

---

#### Camera

**Line:** 870800

---

#### CameraClearFlags

**Line:** 875311

**Values:**

- `Skybox` = 1
- `Color` = 2
- `SolidColor` = 2
- `Depth` = 3
- `Nothing` = 4

---

#### CameraLateLatchMatrixType

**Line:** 892486

**Values:**

- `View` = 0
- `InverseView` = 1
- `ViewProjection` = 2
- `InverseViewProjection` = 3

---

#### CameraOverrideOption

**Line:** 914920

**Values:**

- `Off` = 0
- `On` = 1
- `UsePipelineSettings` = 2

---

#### CameraRenderType

**Line:** 914956

**Values:**

- `Base` = 0
- `Overlay` = 1

---

#### CameraType

**Line:** 875201

**Values:**

- `Game` = 1
- `SceneView` = 2
- `Preview` = 4
- `VR` = 8
- `Reflection` = 16

---

#### CanvasScaler

**Line:** 1354393

---

#### CanvasUpdate

**Line:** 1351639

**Values:**

- `Prelayout` = 0
- `Layout` = 1
- `PostLayout` = 2
- `PreRender` = 3
- `LatePreRender` = 4
- `MaxUpdateValue` = 5

---

#### CaretPosition

**Line:** 1229687

**Values:**

- `None` = 0
- `Left` = 1
- `Right` = 2

---

#### CaseSensitivityType

**Line:** 1322369

**Values:**

- `CaseSensitive` = 0
- `CaseInsensitive` = 1

---

#### Cer

**Line:** 229983

**Values:**

- `None` = 0
- `MayFail` = 1
- `Success` = 2

---

#### CharSet

**Line:** 228521

**Values:**

- `None` = 1
- `Ansi` = 2
- `Unicode` = 3
- `Auto` = 4

---

#### CharacterSubstitutor

**Line:** 1319801

---

#### ChatConnectionState

**Line:** 706365

**Values:**

- `Connected` = 0
- `Connecting` = 1
- `Disconnecting` = 2
- `Disconnected` = 3

---

#### ChecksumGranularity

**Line:** 576346

**Values:**

- `PerOperation` = 0
- `PerBatch` = 1
- `PerActionSingleTickPerFrame` = 2
- `None` = 3

---

#### CipherAlgorithmType

**Line:** 778408

**Values:**

- `None` = 0
- `Null` = 24576
- `Aes` = 26129
- `Aes128` = 26126
- `Aes192` = 26127
- `Aes256` = 26128
- `Des` = 26113
- `Rc2` = 26114
- `Rc4` = 26625
- `TripleDes` = 26115

---

#### CipherMode

**Line:** 217941

**Values:**

- `CBC` = 1
- `ECB` = 2
- `OFB` = 3
- `CFB` = 4
- `CTS` = 5

---

#### CipherSuiteCode

**Line:** 1448618

**Values:**

- `TLS_NULL_WITH_NULL_NULL` = 0
- `TLS_RSA_WITH_NULL_MD5` = 1
- `TLS_RSA_WITH_NULL_SHA` = 2
- `TLS_RSA_EXPORT_WITH_RC4_40_MD5` = 3
- `TLS_RSA_WITH_RC4_128_MD5` = 4
- `TLS_RSA_WITH_RC4_128_SHA` = 5
- `TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5` = 6
- `TLS_RSA_WITH_IDEA_CBC_SHA` = 7
- `TLS_RSA_EXPORT_WITH_DES40_CBC_SHA` = 8
- `TLS_RSA_WITH_DES_CBC_SHA` = 9
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA` = 10
- `TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA` = 11
- `TLS_DH_DSS_WITH_DES_CBC_SHA` = 12
- `TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA` = 13
- `TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA` = 14
- `TLS_DH_RSA_WITH_DES_CBC_SHA` = 15
- `TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA` = 16
- `TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA` = 17
- `TLS_DHE_DSS_WITH_DES_CBC_SHA` = 18
- `TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA` = 19
- `TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA` = 20
- `TLS_DHE_RSA_WITH_DES_CBC_SHA` = 21
- `TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA` = 22
- `TLS_DH_anon_EXPORT_WITH_RC4_40_MD5` = 23
- `TLS_DH_anon_WITH_RC4_128_MD5` = 24
- `TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA` = 25
- `TLS_DH_anon_WITH_DES_CBC_SHA` = 26
- `TLS_DH_anon_WITH_3DES_EDE_CBC_SHA` = 27
- `TLS_RSA_WITH_AES_128_CBC_SHA` = 47
- `TLS_DH_DSS_WITH_AES_128_CBC_SHA` = 48
- `TLS_DH_RSA_WITH_AES_128_CBC_SHA` = 49
- `TLS_DHE_DSS_WITH_AES_128_CBC_SHA` = 50
- `TLS_DHE_RSA_WITH_AES_128_CBC_SHA` = 51
- `TLS_DH_anon_WITH_AES_128_CBC_SHA` = 52
- `TLS_RSA_WITH_AES_256_CBC_SHA` = 53
- `TLS_DH_DSS_WITH_AES_256_CBC_SHA` = 54
- `TLS_DH_RSA_WITH_AES_256_CBC_SHA` = 55
- `TLS_DHE_DSS_WITH_AES_256_CBC_SHA` = 56
- `TLS_DHE_RSA_WITH_AES_256_CBC_SHA` = 57
- `TLS_DH_anon_WITH_AES_256_CBC_SHA` = 58
- `TLS_RSA_WITH_CAMELLIA_128_CBC_SHA` = 65
- `TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA` = 66
- `TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA` = 67
- `TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA` = 68
- `TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA` = 69
- `TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA` = 70
- `TLS_RSA_WITH_CAMELLIA_256_CBC_SHA` = 132
- `TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA` = 133
- `TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA` = 134
- `TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA` = 135
- `TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA` = 136
- `TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA` = 137
- `TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256` = 186
- `TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256` = 187
- `TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256` = 188
- `TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256` = 189
- `TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256` = 190
- `TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256` = 191
- `TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256` = 192
- `TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256` = 193
- `TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256` = 194
- `TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256` = 195
- `TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256` = 196
- `TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256` = 197
- `TLS_RSA_WITH_SEED_CBC_SHA` = 150
- `TLS_DH_DSS_WITH_SEED_CBC_SHA` = 151
- `TLS_DH_RSA_WITH_SEED_CBC_SHA` = 152
- `TLS_DHE_DSS_WITH_SEED_CBC_SHA` = 153
- `TLS_DHE_RSA_WITH_SEED_CBC_SHA` = 154
- `TLS_DH_anon_WITH_SEED_CBC_SHA` = 155
- `TLS_PSK_WITH_RC4_128_SHA` = 138
- `TLS_PSK_WITH_3DES_EDE_CBC_SHA` = 139
- `TLS_PSK_WITH_AES_128_CBC_SHA` = 140
- `TLS_PSK_WITH_AES_256_CBC_SHA` = 141
- `TLS_DHE_PSK_WITH_RC4_128_SHA` = 142
- `TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA` = 143
- `TLS_DHE_PSK_WITH_AES_128_CBC_SHA` = 144
- `TLS_DHE_PSK_WITH_AES_256_CBC_SHA` = 145
- `TLS_RSA_PSK_WITH_RC4_128_SHA` = 146
- `TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA` = 147
- `TLS_RSA_PSK_WITH_AES_128_CBC_SHA` = 148
- `TLS_RSA_PSK_WITH_AES_256_CBC_SHA` = 149
- `TLS_ECDH_ECDSA_WITH_NULL_SHA` = 49153
- `TLS_ECDH_ECDSA_WITH_RC4_128_SHA` = 49154
- `TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA` = 49155
- `TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA` = 49156
- `TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA` = 49157
- `TLS_ECDHE_ECDSA_WITH_NULL_SHA` = 49158
- `TLS_ECDHE_ECDSA_WITH_RC4_128_SHA` = 49159
- `TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA` = 49160
- `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA` = 49161
- `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA` = 49162
- `TLS_ECDH_RSA_WITH_NULL_SHA` = 49163
- `TLS_ECDH_RSA_WITH_RC4_128_SHA` = 49164
- `TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA` = 49165
- `TLS_ECDH_RSA_WITH_AES_128_CBC_SHA` = 49166

---

#### ClampedDragger

**Line:** 609815

---

#### ClassInterfaceType

**Line:** 229045

**Values:**

- `None` = 0
- `AutoDispatch` = 1
- `AutoDual` = 2

---

#### CleanupMode

**Line:** 1597338

**Values:**

- `RemoveComponent` = 0
- `DestroyEntity` = 1

---

#### ClearFlag

**Line:** 807060

**Values:**

- `None` = 0
- `Color` = 1
- `Depth` = 2
- `Stencil` = 4
- `DepthStencil` = 6
- `ColorStencil` = 5
- `All` = 7

---

#### ClientAppPauseStatus

**Line:** 533434

**Values:**

- `Running` = 0
- `Paused` = 1
- `Unpausing` = 2

---

#### ClientCertificateOption

**Line:** 1488190

**Values:**

- `Manual` = 0
- `Automatic` = 1

---

#### ClientLogEntryType

**Line:** 573980

**Values:**

- `Log` = 0
- `Warning` = 1
- `Error` = 2
- `Assert` = 3
- `Exception` = 4

---

#### ClientPlatform

**Line:** 500024

**Values:**

- `Unknown` = 0
- `iOS` = 1
- `Android` = 2
- `WebGL` = 3
- `UnityEditor` = 4

---

#### ClientPlaybackMode

**Line:** 552163

**Values:**

- `Instant` = 0
- `Smooth` = 1

---

#### ClipType

**Line:** 1361470

**Values:**

- `ctIntersection` = 0
- `ctUnion` = 1
- `ctDifference` = 2
- `ctXor` = 3

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

- `None` = 0
- `Read` = 1
- `ModifyExistingContent` = 2
- `UpdatedContent` = 6

---

#### CollectionChangeAction

**Line:** 781255

**Values:**

- `Add` = 1
- `Remove` = 2
- `Refresh` = 3

---

#### CollectionVirtualizationMethod

**Line:** 615339

**Values:**

- `FixedHeight` = 0
- `DynamicHeight` = 1

---

#### ColorGamut

**Line:** 875359

**Values:**

- `sRGB` = 0
- `Rec709` = 1
- `Rec2020` = 2
- `DisplayP3` = 3
- `HDR10` = 4
- `DolbyHDR` = 5
- `P3D65G22` = 6

---

#### ColorGradientMode

**Line:** 1348269

**Values:**

- `Single` = 0
- `HorizontalGradient` = 1
- `VerticalGradient` = 2
- `FourCornersGradient` = 3

---

#### ColorGradingMode

**Line:** 900551

**Values:**

- `LowDynamicRange` = 0
- `HighDynamicRange` = 1

---

#### ColorMode

**Line:** 1221677

**Values:**

- `Single` = 0
- `HorizontalGradient` = 1
- `VerticalGradient` = 2
- `FourCornersGradient` = 3

---

#### ColorPrimaries

**Line:** 875375

**Values:**

- `Rec709` = 0
- `Rec2020` = 1
- `P3` = 2

---

#### ColorSpace

**Line:** 875347

**Values:**

- `Gamma` = 0
- `Linear` = 1

---

#### ColorTween

**Line:** 1358292

---

#### ColorType

**Line:** 1062162

**Values:**

- `Background` = 0
- `Foreground` = 1

---

#### ColorWriteMask

**Line:** 891827

**Values:**

- `Alpha` = 1
- `Blue` = 2
- `Green` = 4
- `Red` = 8
- `All` = 15

---

#### ColumnSortingMode

**Line:** 625989

**Values:**

- `None` = 0
- `Default` = 1
- `Custom` = 2

---

#### Columns

**Line:** 625670

---

#### ComInterfaceType

**Line:** 229003

**Values:**

- `InterfaceIsDual` = 0
- `InterfaceIsIUnknown` = 1
- `InterfaceIsIDispatch` = 2
- `InterfaceIsIInspectable` = 3

---

#### CommandBufferExecutionFlags

**Line:** 892450

**Values:**

- `None` = 0
- `AsyncCompute` = 2

---

#### CommandEvent

**Line:** 1555565

---

#### CommentHandling

**Line:** 1042942

**Values:**

- `Ignore` = 0
- `Load` = 1

---

#### CompareFunction

**Line:** 891799

**Values:**

- `Disabled` = 0
- `Never` = 1
- `Less` = 2
- `Equal` = 3
- `LessEqual` = 4
- `Greater` = 5
- `NotEqual` = 6
- `GreaterEqual` = 7
- `Always` = 8

---

#### CompareOptions

**Line:** 271363

**Values:**

- `None` = 0
- `IgnoreCase` = 1
- `IgnoreNonSpace` = 2
- `IgnoreSymbols` = 4
- `IgnoreKanaType` = 8
- `IgnoreWidth` = 16
- `OrdinalIgnoreCase` = 268435456
- `StringSort` = 536870912
- `Ordinal` = 1073741824

---

#### CompilationRelaxations

**Line:** 253428

**Values:**

- `NoStringInterning` = 8

---

#### CompiledIdentityConstraint

**Line:** 756623

---

#### CompressionAlgorithm

**Line:** 500131

**Values:**

- `None` = 0
- `Deflate` = 1
- `LZ4` = 2
- `Zstandard` = 3

---

#### CompressionMode

**Line:** 789385

**Values:**

- `Decompress` = 0
- `Compress` = 1

---

#### ComputeBufferMode

**Line:** 872861

**Values:**

- `Immutable` = 0
- `Dynamic` = 1
- `Circular` = 2
- `StreamOut` = 3
- `SubUpdates` = 4

---

#### ComputeBufferType

**Line:** 875215

**Values:**

- `Default` = 0
- `Raw` = 1
- `Append` = 2
- `Counter` = 4
- `Constant` = 8
- `Structured` = 16
- `DrawIndirect` = 256
- `IndirectArguments` = 256
- `GPUMemory` = 512

---

#### ComputeQueueType

**Line:** 892408

**Values:**

- `Default` = 0
- `Background` = 1
- `Urgent` = 2

---

#### Compute_DistanceTransform_EventTypes

**Line:** 1220982

**Values:**

- `Processing` = 0
- `Completed` = 1

---

#### ConfidenceFactor

**Line:** 1450086

**Values:**

- `ExtraLow` = 0
- `Low` = 1
- `Medium` = 2
- `High` = 3
- `ExtraHigh` = 4
- `Provable` = 5

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

- `Full` = 2
- `Minimal` = 1
- `Modified` = 0

---

#### Connecting

**Line:** 1309960

---

#### ConnectionHealth

**Line:** 1313869

**Values:**

- `NotConnected` = 0
- `Healthy` = 1
- `Unhealthy` = 2

---

#### ConnectionInternalWatchdogType

**Line:** 550266

**Values:**

- `Transport` = 0
- `Resetup` = 1

---

#### ConnectionLostReason

**Line:** 1306212

**Values:**

- `CouldNotConnect` = 0
- `NoInternetConnection` = 1
- `ConnectionLost` = 2
- `ServerMaintenance` = 3
- `ClientVersionTooOld` = 4
- `DeviceLocalStorageError` = 5
- `PlayerIsBanned` = 6
- `InternalError` = 7
- `CredentialsExpiredOrInvalid` = 8

---

#### ConnectionStatus

**Line:** 1306660

**Values:**

- `NotConnected` = 0
- `Connecting` = 1
- `Connected` = 2
- `Error` = 3

---

#### ConsentStatus

**Line:** 1572952

**Values:**

- `Granted` = 0
- `Denied` = 1

---

#### ConsentType

**Line:** 1572941

**Values:**

- `AdStorage` = 0
- `AnalyticsStorage` = 1
- `AdUserData` = 2
- `AdPersonalization` = 3

---

#### Consistency

**Line:** 229993

**Values:**

- `MayCorruptProcess` = 0
- `MayCorruptAppDomain` = 1
- `MayCorruptInstance` = 2
- `WillNotCorruptState` = 3

---

#### ConsoleAlignment

**Line:** 1442564

**Values:**

- `Top` = 0
- `Bottom` = 1

---

#### ConsoleColor

**Line:** 70927

**Values:**

- `Black` = 0
- `DarkBlue` = 1
- `DarkGreen` = 2
- `DarkCyan` = 3
- `DarkRed` = 4
- `DarkMagenta` = 5
- `DarkYellow` = 6
- `Gray` = 7
- `DarkGray` = 8
- `Blue` = 9
- `Green` = 10
- `Cyan` = 11
- `Red` = 12
- `Magenta` = 13
- `Yellow` = 14
- `White` = 15

---

#### ConsoleKey

**Line:** 70950

**Values:**

- `Backspace` = 8
- `Tab` = 9
- `Clear` = 12
- `Enter` = 13
- `Pause` = 19
- `Escape` = 27
- `Spacebar` = 32
- `PageUp` = 33
- `PageDown` = 34
- `End` = 35
- `Home` = 36
- `LeftArrow` = 37
- `UpArrow` = 38
- `RightArrow` = 39
- `DownArrow` = 40
- `Select` = 41
- `Print` = 42
- `Execute` = 43
- `PrintScreen` = 44
- `Insert` = 45
- `Delete` = 46
- `Help` = 47
- `D0` = 48
- `D1` = 49
- `D2` = 50
- `D3` = 51
- `D4` = 52
- `D5` = 53
- `D6` = 54
- `D7` = 55
- `D8` = 56
- `D9` = 57
- `A` = 65
- `B` = 66
- `C` = 67
- `D` = 68
- `E` = 69
- `F` = 70
- `G` = 71
- `H` = 72
- `I` = 73
- `J` = 74
- `K` = 75
- `L` = 76
- `M` = 77
- `N` = 78
- `O` = 79
- `P` = 80
- `Q` = 81
- `R` = 82
- `S` = 83
- `T` = 84
- `U` = 85
- `V` = 86
- `W` = 87
- `X` = 88
- `Y` = 89
- `Z` = 90
- `LeftWindows` = 91
- `RightWindows` = 92
- `Applications` = 93
- `Sleep` = 95
- `NumPad0` = 96
- `NumPad1` = 97
- `NumPad2` = 98
- `NumPad3` = 99
- `NumPad4` = 100
- `NumPad5` = 101
- `NumPad6` = 102
- `NumPad7` = 103
- `NumPad8` = 104
- `NumPad9` = 105
- `Multiply` = 106
- `Add` = 107
- `Separator` = 108
- `Subtract` = 109
- `Decimal` = 110
- `Divide` = 111
- `F1` = 112
- `F2` = 113
- `F3` = 114
- `F4` = 115
- `F5` = 116
- `F6` = 117
- `F7` = 118
- `F8` = 119
- `F9` = 120
- `F10` = 121
- `F11` = 122
- `F12` = 123
- `F13` = 124
- `F14` = 125
- `F15` = 126
- `F16` = 127
- `F17` = 128
- `F18` = 129

---

#### ConsoleModifiers

**Line:** 71137

**Values:**

- `Alt` = 1
- `Shift` = 2
- `Control` = 4

---

#### ConsoleSpecialKey

**Line:** 71147

**Values:**

- `ControlC` = 0
- `ControlBreak` = 1

---

#### ConstructorHandling

**Line:** 1025842

**Values:**

- `Default` = 0
- `AllowNonPublicDefaultConstructor` = 1

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

- `Player` = 0
- `Editor` = 1

---

#### ConversionError

**Line:** 1200808

**Values:**

- `None` = 0
- `Overflow` = 1
- `Encoding` = 2
- `CodePoint` = 3

---

#### CooldownTimerState

**Line:** 696296

**Values:**

- `Idle` = 0
- `Active` = 1
- `Cooldown` = 2

---

#### CopyDepthMode

**Line:** 916194

**Values:**

- `AfterOpaques` = 0
- `AfterTransparents` = 1
- `ForcePrepass` = 2

---

#### CopyError

**Line:** 1200799

**Values:**

- `None` = 0
- `Truncation` = 1

---

#### CopyTextureSupport

**Line:** 892395

**Values:**

- `None` = 0
- `Basic` = 1
- `Copy3D` = 2
- `DifferentTypes` = 4
- `TextureToRT` = 8
- `RTToTexture` = 16

---

#### Crc8

**Line:** 577514

---

#### CredentialState

**Line:** 1590219

**Values:**

- `Revoked` = 0
- `Authorized` = 1
- `NotFound` = 2
- `Transferred` = 3

---

#### CryptoStreamMode

**Line:** 217673

**Values:**

- `Read` = 0
- `Write` = 1

---

#### CspProviderFlags

**Line:** 218045

**Values:**

- `NoFlags` = 0
- `UseMachineKeyStore` = 1
- `UseDefaultKeyContainer` = 2
- `UseNonExportableKey` = 4
- `UseExistingKey` = 8
- `UseArchivableKey` = 16
- `UseUserProtectedKey` = 32
- `NoPrompt` = 64
- `CreateEphemeralKey` = 128

---

#### CubemapFace

**Line:** 875540

**Values:**

- `PositiveX` = 0
- `NegativeX` = 1
- `PositiveY` = 2
- `NegativeY` = 3
- `PositiveZ` = 4
- `NegativeZ` = 5

---

#### CullMode

**Line:** 891816

**Values:**

- `Off` = 0
- `Front` = 1
- `Back` = 2

---

#### CullingOptions

**Line:** 895256

**Values:**

- `None` = 0
- `ForceEvenIfCameraIsNotActive` = 1
- `OcclusionCull` = 2
- `NeedsLighting` = 4
- `NeedsReflectionProbes` = 8
- `Stereo` = 16
- `DisablePerObjectCulling` = 32
- `ShadowCasters` = 64

---

#### CultureTypes

**Line:** 271425

**Values:**

- `NeutralCultures` = 1
- `SpecificCultures` = 2
- `InstalledWin32Cultures` = 4
- `AllCultures` = 7
- `UserCustomCulture` = 8
- `ReplacementCultures` = 16
- `WindowsOnlyCultures` = 32
- `FrameworkCultures` = 64

---

#### CursorLockMode

**Line:** 878198

**Values:**

- `None` = 0
- `Locked` = 1
- `Confined` = 2

---

#### CursorMode

**Line:** 878189

**Values:**

- `Auto` = 0
- `ForceSoftware` = 1

---

#### CustomErrorsModes

**Line:** 220886

**Values:**

- `On` = 0
- `Off` = 1
- `RemoteOnly` = 2

---

#### DOTweenSettings

**Line:** 1431190

---

#### DailyDealType

**Line:** 1066945

**Values:**

- `Dungeon` = 0
- `Resource` = 1
- `Pet` = 2
- `Skill` = 3
- `Tech` = 4
- `Mount` = 5

---

#### DataRowAction

**Line:** 1084730

**Values:**

- `Nothing` = 0
- `Delete` = 1
- `Change` = 2
- `Rollback` = 4
- `Commit` = 8
- `Add` = 16
- `ChangeOriginal` = 32
- `ChangeCurrentAndOriginal` = 64

---

#### DataRowState

**Line:** 1084870

**Values:**

- `Detached` = 1
- `Unchanged` = 2
- `Added` = 4
- `Deleted` = 8
- `Modified` = 16

---

#### DataRowVersion

**Line:** 1084882

**Values:**

- `Original` = 256
- `Current` = 512
- `Proposed` = 1024
- `Default` = 1536

---

#### DataSetDateTime

**Line:** 1085015

**Values:**

- `Local` = 1
- `Unspecified` = 2
- `UnspecifiedLocal` = 3
- `Utc` = 4

---

#### DataType

**Line:** 1508896

**Values:**

- `Custom` = 0
- `DateTime` = 1
- `Date` = 2
- `Time` = 3
- `Duration` = 4
- `PhoneNumber` = 5
- `Currency` = 6
- `Text` = 7
- `Html` = 8
- `MultilineText` = 9
- `EmailAddress` = 10
- `Password` = 11
- `Url` = 12
- `ImageUrl` = 13
- `CreditCard` = 14
- `PostalCode` = 15
- `Upload` = 16

---

#### DataViewRowState

**Line:** 1085688

**Values:**

- `None` = 0
- `Unchanged` = 2
- `Added` = 4
- `Deleted` = 8
- `ModifiedCurrent` = 16
- `ModifiedOriginal` = 32
- `OriginalRows` = 42
- `CurrentRows` = 22

---

#### DatabaseGeneratedOption

**Line:** 1510895

**Values:**

- `None` = 0
- `Identity` = 1
- `Computed` = 2

---

#### DateFormatHandling

**Line:** 1025851

**Values:**

- `IsoDateFormat` = 0
- `MicrosoftDateFormat` = 1

---

#### DateParseHandling

**Line:** 1025860

**Values:**

- `None` = 0
- `DateTime` = 1
- `DateTimeOffset` = 2

---

#### DateTimeKind

**Line:** 22477

**Values:**

- `Unspecified` = 0
- `Utc` = 1
- `Local` = 2

---

#### DateTimeStyles

**Line:** 272040

**Values:**

- `None` = 0
- `AllowLeadingWhite` = 1
- `AllowTrailingWhite` = 2
- `AllowInnerWhite` = 4
- `AllowWhiteSpaces` = 7
- `NoCurrentDateDefault` = 8
- `AdjustToUniversal` = 16
- `AssumeLocal` = 32
- `AssumeUniversal` = 64
- `RoundtripKind` = 128

---

#### DateTimeZoneHandling

**Line:** 1025870

**Values:**

- `Local` = 0
- `Utc` = 1
- `Unspecified` = 2
- `RoundtripKind` = 3

---

#### DayOfWeek

**Line:** 22710

**Values:**

- `Sunday` = 0
- `Monday` = 1
- `Tuesday` = 2
- `Wednesday` = 3
- `Thursday` = 4
- `Friday` = 5
- `Saturday` = 6

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

- `None` = 0
- `Depth` = 1
- `MotionVector` = 2
- `AdditionalLightsShadowMap` = 3
- `MainLightShadowMap` = 4
- `AdditionalLightsCookieAtlas` = 5
- `ReflectionProbeAtlas` = 6
- `STP` = 7

---

#### DebugLightingFeatureFlags

**Line:** 1594442

**Values:**

- `None` = 0
- `GlobalIllumination` = 1
- `MainLight` = 2
- `AdditionalLights` = 4
- `VertexLighting` = 8
- `Emission` = 16
- `AmbientOcclusion` = 32

---

#### DebugLightingMode

**Line:** 1594414

**Values:**

- `None` = 0
- `ShadowCascades` = 1
- `LightingWithoutNormalMaps` = 2
- `LightingWithNormalMaps` = 3
- `Reflections` = 4
- `ReflectionsWithSmoothness` = 5
- `GlobalIllumination` = 6

---

#### DebugManager

**Line:** 812624

---

#### DebugMaterialMode

**Line:** 1594246

**Values:**

- `None` = 0
- `Albedo` = 1
- `Specular` = 2
- `Alpha` = 3
- `Smoothness` = 4
- `AmbientOcclusion` = 5
- `Emission` = 6
- `NormalWorldSpace` = 7
- `NormalTangentSpace` = 8
- `LightingComplexity` = 9
- `Metallic` = 10
- `SpriteMask` = 11
- `RenderingLayerMasks` = 12

---

#### DebugMaterialValidationMode

**Line:** 1594283

**Values:**

- `None` = 0
- `Albedo` = 1
- `Metallic` = 2

---

#### DebugMipInfoMode

**Line:** 1594335

**Values:**

- `None` = 0
- `MipStreamingPerformance` = 1
- `MipStreamingStatus` = 2
- `MipStreamingActivity` = 3
- `MipStreamingPriority` = 4
- `MipCount` = 5
- `MipRatio` = 6

---

#### DebugMipMapModeTerrainTexture

**Line:** 1594360

**Values:**

- `Control` = 0
- `Layer0` = 1
- `Layer1` = 2
- `Layer2` = 3
- `Layer3` = 4

---

#### DebugMipMapStatusMode

**Line:** 1594350

**Values:**

- `Material` = 0
- `Texture` = 1

---

#### DebugOverdrawMode

**Line:** 1594323

**Values:**

- `None` = 0
- `Opaque` = 1
- `Transparent` = 2
- `All` = 3

---

#### DebugPostProcessingMode

**Line:** 1594377

**Values:**

- `Disabled` = 0
- `Auto` = 1
- `Enabled` = 2

---

#### DebugProbeShadingMode

**Line:** 818983

**Values:**

- `SH` = 0
- `SHL0` = 1
- `SHL0L1` = 2
- `Validity` = 3
- `ValidityOverDilationThreshold` = 4
- `RenderingLayerMasks` = 5
- `InvalidatedByAdjustmentVolumes` = 6
- `Size` = 7
- `SkyOcclusionSH` = 8
- `SkyDirection` = 9
- `ProbeOcclusion` = 10

---

#### DebugSceneOverrideMode

**Line:** 1594311

**Values:**

- `None` = 0
- `Overdraw` = 1
- `Wireframe` = 2
- `SolidWireframe` = 3
- `ShadedWireframe` = 4

---

#### DebugUI

**Line:** 814599

---

#### DebugValidationMode

**Line:** 1594388

**Values:**

- `None` = 0
- `HighlightNanInfNegative` = 1
- `HighlightOutsideOfRange` = 2

---

#### DebugVertexAttributeMode

**Line:** 1594267

**Values:**

- `None` = 0
- `Texcoord0` = 1
- `Texcoord1` = 2
- `Texcoord2` = 3
- `Texcoord3` = 4
- `Color` = 5
- `Tangent` = 6
- `Normal` = 7

---

#### DebugWireframeMode

**Line:** 902402

**Values:**

- `None` = 0
- `Wireframe` = 1
- `SolidWireframe` = 2
- `ShadedWireframe` = 3

---

#### DebuggableAttribute

**Line:** 275226

---

#### DebuggerBrowsableState

**Line:** 275253

**Values:**

- `Never` = 0
- `Collapsed` = 2
- `RootHidden` = 3

---

#### DecalScaleMode

**Line:** 904249

**Values:**

- `ScaleInvariant` = 0
- `InheritFromHierarchy` = 1

---

#### DecompressionMethods

**Line:** 794423

**Values:**

- `None` = 0
- `GZip` = 1
- `Deflate` = 2

---

#### DefaultEventSystem

**Line:** 631530

---

#### DefaultFormat

**Line:** 899403

**Values:**

- `LDR` = 0
- `HDR` = 1
- `DepthStencil` = 2
- `Shadow` = 3
- `Video` = 4

---

#### DefaultPlayerClientContext

**Line:** 576874

---

#### DefaultTabs

**Line:** 1442537

**Values:**

- `SystemInformation` = 0
- `Options` = 1
- `Console` = 2
- `Profiler` = 3
- `BugReporter` = 4

---

#### DefaultValueHandling

**Line:** 1025932

**Values:**

- `Include` = 0
- `Ignore` = 1
- `Populate` = 2
- `IgnoreAndPopulate` = 3

---

#### DelayType

**Line:** 1120976

**Values:**

- `DeltaTime` = 0
- `UnscaledDeltaTime` = 1
- `Realtime` = 2

---

#### DeltaSpeed

**Line:** 628654

**Values:**

- `Fast` = 0
- `Normal` = 1
- `Slow` = 2

---

#### DependencyStatus

**Line:** 1491618

**Values:**

- `Available` = 0
- `UnavailableDisabled` = 1
- `UnavailableInvalid` = 2
- `UnavilableMissing` = 3
- `UnavailablePermission` = 4
- `UnavailableUpdaterequired` = 5
- `UnavailableUpdating` = 6
- `UnavailableOther` = 7

---

#### DepthAccess

**Line:** 829114

**Values:**

- `Read` = 1
- `Write` = 2
- `ReadWrite` = 3

---

#### DepthBits

**Line:** 822159

**Values:**

- `None` = 0
- `Depth8` = 8
- `Depth16` = 16
- `Depth24` = 24
- `Depth32` = 32

---

#### DepthFormat

**Line:** 916229

**Values:**

- `Default` = 0
- `Depth_16` = 90
- `Depth_24` = 91
- `Depth_32` = 93
- `Depth_16_Stencil_8` = 151
- `Depth_24_Stencil_8` = 92
- `Depth_32_Stencil_8` = 94

---

#### DepthOfFieldMode

**Line:** 909312

**Values:**

- `Off` = 0
- `Gaussian` = 1
- `Bokeh` = 2

---

#### DepthPrimingMode

**Line:** 915649

**Values:**

- `Disabled` = 0
- `Auto` = 1
- `Forced` = 2

---

#### DepthTextureMode

**Line:** 875324

**Values:**

- `None` = 0
- `Depth` = 1
- `DepthNormals` = 2
- `MotionVectors` = 4

---

#### DesignerSerializationVisibility

**Line:** 780730

**Values:**

- `Hidden` = 0
- `Visible` = 1
- `Content` = 2

---

#### DeviceType

**Line:** 885052

**Values:**

- `Unknown` = 0
- `Handheld` = 1
- `Console` = 2
- `Desktop` = 3

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

- `Version_1_0` = 0

---

#### DisplayStyle

**Line:** 659968

**Values:**

- `Flex` = 0
- `None` = 1

---

#### DistanceMetric

**Line:** 897009

**Values:**

- `Perspective` = 0
- `Orthographic` = 1
- `CustomAxis` = 2

---

#### DivisionSeasonPhase

**Line:** 563899

**Values:**

- `NoDivision` = 0
- `Preview` = 1
- `Ongoing` = 2
- `Resolving` = 3
- `Concluded` = 4

---

#### DllImportSearchPath

**Line:** 229256

**Values:**

- `UseDllDirectoryForDependencies` = 256
- `ApplicationDirectory` = 512
- `UserDirectories` = 1024
- `System32` = 2048
- `SafeDirectories` = 4096
- `AssemblyDirectory` = 2
- `LegacyBehavior` = 0

---

#### DownloadStatus

**Line:** 1504390

**Values:**

- `NotStarted` = 0
- `Downloading` = 1
- `Completed` = 2
- `Failed` = 3

---

#### Downsampling

**Line:** 900510

**Values:**

- `None` = 0
- `_2xBilinear` = 1
- `_4xBox` = 2
- `_4xBilinear` = 3

---

#### DragVisualMode

**Line:** 632189

**Values:**

- `None` = 0
- `Copy` = 1
- `Move` = 2
- `Rejected` = 3

---

#### DrivenTransformProperties

**Line:** 885927

**Values:**

- `None` = 0
- `AnchoredPositionX` = 2
- `AnchoredPositionY` = 4
- `AnchoredPositionZ` = 8
- `Rotation` = 16
- `ScaleX` = 32
- `ScaleY` = 64
- `ScaleZ` = 128
- `AnchorMinX` = 256
- `AnchorMinY` = 512
- `AnchorMaxX` = 1024
- `AnchorMaxY` = 2048
- `SizeDeltaX` = 4096
- `SizeDeltaY` = 8192
- `PivotX` = 16384
- `PivotY` = 32768
- `AnchoredPosition` = 6
- `AnchoredPosition3D` = 14
- `Scale` = 224
- `AnchorMin` = 768
- `AnchorMax` = 3072
- `Anchors` = 3840
- `SizeDelta` = 12288
- `Pivot` = 49152

---

#### DtdProcessing

**Line:** 740784

**Values:**

- `Prohibit` = 0
- `Ignore` = 1
- `Parse` = 2

---

#### DuplicatePropertyNameHandling

**Line:** 1042951

**Values:**

- `Replace` = 0
- `Ignore` = 1
- `Error` = 2

---

#### DynamicAtlasFilters

**Line:** 606472

**Values:**

- `None` = 0
- `Readability` = 1
- `Size` = 2
- `Format` = 4
- `ColorSpace` = 8
- `FilterMode` = 16

---

#### DynamicResScalePolicyType

**Line:** 809601

**Values:**

- `ReturnsPercentage` = 0
- `ReturnsMinMaxLerpFactor` = 1

---

#### DynamicResScalerSlot

**Line:** 809610

**Values:**

- `User` = 0
- `System` = 1
- `Count` = 2

---

#### DynamicResUpscaleFilter

**Line:** 809842

**Values:**

- `Bilinear` = 0
- `CatmullRom` = 1
- `Lanczos` = 2
- `ContrastAdaptiveSharpen` = 3
- `EdgeAdaptiveScalingUpres` = 4
- `TAAU` = 5

---

#### DynamicResolutionHandler

**Line:** 809628

---

#### DynamicResolutionType

**Line:** 809833

**Values:**

- `Software` = 0
- `Hardware` = 1

---

#### ECCurve

**Line:** 1230438

---

#### ETagAction

**Line:** 1501327

**Values:**

- `Default` = 0
- `Ignore` = 1
- `IfMatch` = 2
- `IfNoneMatch` = 3

---

#### Ease

**Line:** 1425465

**Values:**

- `Unset` = 0
- `Linear` = 1
- `InSine` = 2
- `OutSine` = 3
- `InOutSine` = 4
- `InQuad` = 5
- `OutQuad` = 6
- `InOutQuad` = 7
- `InCubic` = 8
- `OutCubic` = 9
- `InOutCubic` = 10
- `InQuart` = 11
- `OutQuart` = 12
- `InOutQuart` = 13
- `InQuint` = 14
- `OutQuint` = 15
- `InOutQuint` = 16
- `InExpo` = 17
- `OutExpo` = 18
- `InOutExpo` = 19
- `InCirc` = 20
- `OutCirc` = 21
- `InOutCirc` = 22
- `InElastic` = 23
- `OutElastic` = 24
- `InOutElastic` = 25
- `InBack` = 26
- `OutBack` = 27
- `InOutBack` = 28
- `InBounce` = 29
- `OutBounce` = 30
- `InOutBounce` = 31
- `Flash` = 32
- `InFlash` = 33
- `OutFlash` = 34
- `InOutFlash` = 35
- `INTERNAL_Zero` = 36
- `INTERNAL_Custom` = 37

---

#### EasingMode

**Line:** 645702

**Values:**

- `Ease` = 0
- `EaseIn` = 1
- `EaseOut` = 2
- `EaseInOut` = 3
- `Linear` = 4
- `EaseInSine` = 5
- `EaseOutSine` = 6
- `EaseInOutSine` = 7
- `EaseInCubic` = 8
- `EaseOutCubic` = 9
- `EaseInOutCubic` = 10
- `EaseInCirc` = 11
- `EaseOutCirc` = 12
- `EaseInOutCirc` = 13
- `EaseInElastic` = 14
- `EaseOutElastic` = 15
- `EaseInOutElastic` = 16
- `EaseInBack` = 17
- `EaseOutBack` = 18
- `EaseInOutBack` = 19
- `EaseInBounce` = 20
- `EaseOutBounce` = 21
- `EaseInOutBounce` = 22

---

#### EditorBrowsableState

**Line:** 780546

**Values:**

- `Always` = 0
- `Never` = 1
- `Advanced` = 2

---

#### EditorTextRenderingMode

**Line:** 660020

**Values:**

- `SDF` = 0
- `Bitmap` = 1

---

#### EncryptionPolicy

**Line:** 802768

**Values:**

- `RequireEncryption` = 0
- `AllowNoEncryption` = 1
- `NoEncryption` = 2

---

#### EndType

**Line:** 1361513

**Values:**

- `etClosedPolygon` = 0
- `etClosedLine` = 1

---

#### EntityHandling

**Line:** 740794

**Values:**

- `ExpandEntities` = 1
- `ExpandCharEntities` = 2

---

#### EntityIndexType

**Line:** 1597445

**Values:**

- `EntityIndex` = 0
- `PrimaryEntityIndex` = 1

---

#### EntityTimelinePingTraceMarker

**Line:** 553646

---

#### EntryOverrideType

**Line:** 1327475

**Values:**

- `None` = 0
- `Table` = 1
- `Entry` = 2
- `TableAndEntry` = 3

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

- `Local` = 0
- `Development` = 1
- `Staging` = 2
- `Production` = 3

---

#### ErrorAction

**Line:** 1322378

**Values:**

- `ThrowError` = 0
- `OutputErrorInResult` = 1
- `Ignore` = 2
- `MaintainTokens` = 3

---

#### Event

**Line:** 1555654

---

#### EventActivityOptions

**Line:** 275495

**Values:**

- `None` = 0
- `Disable` = 2
- `Recursive` = 4
- `Detachable` = 8

---

#### EventAttributes

**Line:** 265285

**Values:**

- `None` = 0
- `SpecialName` = 512
- `RTSpecialName` = 1024
- `ReservedMask` = 1024

---

#### EventCommand

**Line:** 275633

**Values:**

- `Update` = 0

---

#### EventHandle

**Line:** 1359586

**Values:**

- `Unused` = 0
- `Used` = 1

---

#### EventInterestOptions

**Line:** 671223

**Values:**

- `Inherit` = 0

---

#### EventKeywords

**Line:** 275546

**Values:**

- `None` = 0
- `MicrosoftTelemetry` = 562949953421312
- `WdiContext` = 562949953421312
- `WdiDiagnostic` = 1125899906842624
- `Sqm` = 2251799813685248
- `AuditFailure` = 4503599627370496
- `AuditSuccess` = 9007199254740992
- `CorrelationHint` = 4503599627370496
- `EventLogClassic` = 36028797018963968

---

#### EventModifiers

**Line:** 1555899

---

#### EventOpcode

**Line:** 275527

**Values:**

- `Info` = 0
- `Start` = 1
- `Stop` = 2
- `DataCollectionStart` = 3
- `DataCollectionStop` = 4
- `Extension` = 5
- `Reply` = 6
- `Resume` = 7
- `Suspend` = 8
- `Send` = 9
- `Receive` = 240

---

#### EventResetMode

**Line:** 178933

**Values:**

- `AutoReset` = 0
- `ManualReset` = 1

---

#### EventSourceSettings

**Line:** 275811

**Values:**

- `Default` = 0
- `ThrowOnEventWriteErrors` = 1
- `EtwManifestEventFormat` = 4
- `EtwSelfDescribingEventFormat` = 8

---

#### EventTarget

**Line:** 1597479

**Values:**

- `Any` = 0
- `Self` = 1

---

#### EventTask

**Line:** 275519

**Values:**

- `None` = 0

---

#### EventTriggerType

**Line:** 1360055

**Values:**

- `PointerEnter` = 0
- `PointerExit` = 1
- `PointerDown` = 2
- `PointerUp` = 3
- `PointerClick` = 4
- `Drag` = 5
- `Drop` = 6
- `Scroll` = 7
- `UpdateSelected` = 8
- `Select` = 9
- `Deselect` = 10
- `Move` = 11
- `InitializePotentialDrag` = 12
- `BeginDrag` = 13
- `EndDrag` = 14
- `Submit` = 15
- `Cancel` = 16

---

#### EventType

**Line:** 1597488

**Values:**

- `Added` = 0
- `Removed` = 1

---

#### ExceptionHandlingClauseOptions

**Line:** 265375

**Values:**

- `Clause` = 0
- `Filter` = 1
- `Finally` = 2
- `Fault` = 4

---

#### ExchangeAlgorithmType

**Line:** 778425

**Values:**

- `None` = 0
- `DiffieHellman` = 43522
- `RsaKeyX` = 41984
- `RsaSign` = 9216

---

#### Expander

**Line:** 1319916

---

#### ExponentialBackOffPolicy

**Line:** 1497267

**Values:**

- `None` = 0
- `Exception` = 1
- `UnsuccessfulResponse503` = 2

---

#### ExpressionType

**Line:** 1287138

**Values:**

- `Add` = 0
- `AddChecked` = 1
- `And` = 2
- `AndAlso` = 3
- `ArrayLength` = 4
- `ArrayIndex` = 5
- `Call` = 6
- `Coalesce` = 7
- `Conditional` = 8
- `Constant` = 9
- `Convert` = 10
- `ConvertChecked` = 11
- `Divide` = 12
- `Equal` = 13
- `ExclusiveOr` = 14
- `GreaterThan` = 15
- `GreaterThanOrEqual` = 16
- `Invoke` = 17
- `Lambda` = 18
- `LeftShift` = 19
- `LessThan` = 20
- `LessThanOrEqual` = 21
- `ListInit` = 22
- `MemberAccess` = 23
- `MemberInit` = 24
- `Modulo` = 25
- `Multiply` = 26
- `MultiplyChecked` = 27
- `Negate` = 28
- `UnaryPlus` = 29
- `NegateChecked` = 30
- `New` = 31
- `NewArrayInit` = 32
- `NewArrayBounds` = 33
- `Not` = 34
- `NotEqual` = 35
- `Or` = 36
- `OrElse` = 37
- `Parameter` = 38
- `Power` = 39
- `Quote` = 40
- `RightShift` = 41
- `Subtract` = 42
- `SubtractChecked` = 43
- `TypeAs` = 44
- `TypeIs` = 45
- `Assign` = 46
- `Block` = 47
- `DebugInfo` = 48
- `Decrement` = 49
- `Dynamic` = 50
- `Default` = 51
- `Extension` = 52
- `Goto` = 53
- `Increment` = 54
- `Index` = 55
- `Label` = 56
- `RuntimeVariables` = 57
- `Loop` = 58
- `Switch` = 59
- `Throw` = 60
- `Try` = 61
- `Unbox` = 62
- `AddAssign` = 63
- `AndAssign` = 64
- `DivideAssign` = 65
- `ExclusiveOrAssign` = 66
- `LeftShiftAssign` = 67
- `ModuloAssign` = 68
- `MultiplyAssign` = 69
- `OrAssign` = 70
- `PowerAssign` = 71
- `RightShiftAssign` = 72
- `SubtractAssign` = 73
- `AddAssignChecked` = 74
- `MultiplyAssignChecked` = 75
- `SubtractAssignChecked` = 76
- `PreIncrementAssign` = 77
- `PreDecrementAssign` = 78
- `PostIncrementAssign` = 79
- `PostDecrementAssign` = 80
- `TypeEqual` = 81
- `OnesComplement` = 82
- `IsTrue` = 83
- `IsFalse` = 84

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

- `Default` = 0
- `StandardUser` = 1
- `DeveloperUser` = 2

---

#### FallbackBehavior

**Line:** 1318480

**Values:**

- `UseProjectSettings` = 0
- `DontUseFallback` = 1
- `UseFallback` = 2

---

#### FalloffType

**Line:** 898859

**Values:**

- `InverseSquared` = 0
- `InverseSquaredNoRangeAttenuation` = 1
- `Linear` = 2
- `Legacy` = 3
- `Undefined` = 4

---

#### FastMemoryFlags

**Line:** 891725

**Values:**

- `None` = 0
- `SpillTop` = 1
- `SpillBottom` = 2

---

#### Features

**Line:** 1498159

**Values:**

- `LegacyDataResponse` = 0

---

#### FieldAttributes

**Line:** 265387

**Values:**

- `FieldAccessMask` = 7
- `PrivateScope` = 0
- `Private` = 1
- `FamANDAssem` = 2
- `Assembly` = 3
- `Family` = 4
- `FamORAssem` = 5
- `Public` = 6
- `Static` = 16
- `InitOnly` = 32
- `Literal` = 64
- `NotSerialized` = 128
- `SpecialName` = 512
- `PinvokeImpl` = 8192
- `RTSpecialName` = 1024
- `HasFieldMarshal` = 4096
- `HasDefault` = 32768
- `HasFieldRVA` = 256
- `ReservedMask` = 38144

---

#### FieldPacking

**Line:** 821454

**Values:**

- `NoPacking` = 0
- `R11G11B10` = 1
- `PackedFloat` = 2
- `PackedUint` = 3

---

#### FieldPrecision

**Line:** 821465

**Values:**

- `Half` = 0
- `Real` = 1
- `Default` = 2

---

#### FileAccess

**Line:** 467752

**Values:**

- `Read` = 1
- `Write` = 2
- `ReadWrite` = 3

---

#### FileAttributes

**Line:** 469854

**Values:**

- `ReadOnly` = 1
- `Hidden` = 2
- `System` = 4
- `Directory` = 16
- `Archive` = 32
- `Device` = 64
- `Normal` = 128
- `Temporary` = 256
- `SparseFile` = 512
- `ReparsePoint` = 1024
- `Compressed` = 2048
- `Offline` = 4096
- `NotContentIndexed` = 8192
- `Encrypted` = 16384
- `IntegrityStream` = 32768
- `NoScrubData` = 131072

---

#### FileHandleType

**Line:** 1570450

**Values:**

- `Auto` = 0
- `Tcp` = 1
- `Pipe` = 2

---

#### FileMode

**Line:** 467809

**Values:**

- `CreateNew` = 1
- `Create` = 2
- `Open` = 3
- `OpenOrCreate` = 4
- `Truncate` = 5
- `Append` = 6

---

#### FileOptions

**Line:** 467873

**Values:**

- `None` = 0
- `Asynchronous` = 1073741824
- `RandomAccess` = 268435456
- `DeleteOnClose` = 67108864
- `SequentialScan` = 134217728
- `Encrypted` = 16384

---

#### FileReadType

**Line:** 837805

**Values:**

- `Sync` = 0
- `Async` = 1

---

#### FileShare

**Line:** 467888

**Values:**

- `None` = 0
- `Read` = 1
- `Write` = 2
- `ReadWrite` = 3
- `Delete` = 4
- `Inheritable` = 16

---

#### FileState

**Line:** 837583

**Values:**

- `Absent` = 0
- `Exists` = 1

---

#### FileSystemBuildSource

**Line:** 595519

---

#### FilmGrainLookup

**Line:** 909375

**Values:**

- `Thin1` = 0
- `Thin2` = 1
- `Medium1` = 2
- `Medium2` = 3
- `Medium3` = 4
- `Medium4` = 5
- `Medium5` = 6
- `Medium6` = 7
- `Large01` = 8
- `Large02` = 9
- `Custom` = 10

---

#### FilterMode

**Line:** 875428

**Values:**

- `Point` = 0
- `Bilinear` = 1
- `Trilinear` = 2

---

#### FindObjectsInactive

**Line:** 883919

**Values:**

- `Exclude` = 0
- `Include` = 1

---

#### FindObjectsSortMode

**Line:** 883910

**Values:**

- `None` = 0
- `InstanceID` = 1

---

#### FlexDirection

**Line:** 659871

**Values:**

- `Column` = 0
- `ColumnReverse` = 1
- `Row` = 2
- `RowReverse` = 3

---

#### FloatFormatHandling

**Line:** 1025943

**Values:**

- `String` = 0
- `Symbol` = 1
- `DefaultValue` = 2

---

#### FloatMode

**Line:** 1329686

**Values:**

- `Default` = 0
- `Strict` = 1
- `Deterministic` = 2
- `Fast` = 3

---

#### FloatParseHandling

**Line:** 1025953

**Values:**

- `Double` = 0
- `Decimal` = 1

---

#### FloatPrecision

**Line:** 1329697

**Values:**

- `Standard` = 0
- `High` = 1
- `Medium` = 2
- `Low` = 3

---

#### FocusType

**Line:** 1451160

**Values:**

- `Native` = 0
- `Keyboard` = 1
- `Passive` = 2

---

#### FontEngineError

**Line:** 1557580

**Values:**

- `Success` = 0
- `Invalid_File_Path` = 1
- `Invalid_File_Format` = 2
- `Invalid_File_Structure` = 3
- `Invalid_File` = 4
- `Invalid_Table` = 8
- `Invalid_Glyph_Index` = 16
- `Invalid_Character_Code` = 17
- `Invalid_Pixel_Size` = 23
- `Invalid_Library` = 33
- `Invalid_Face` = 35
- `Invalid_Library_or_Face` = 41
- `Atlas_Generation_Cancelled` = 100
- `Invalid_SharedTextureData` = 101
- `OpenTypeLayoutLookup_Mismatch` = 116

---

#### FontFeatureLookupFlags

**Line:** 1557989

**Values:**

- `None` = 0
- `IgnoreLigatures` = 4
- `IgnoreSpacingAdjustments` = 256

---

#### FontStyle

**Line:** 1580731

**Values:**

- `Normal` = 0
- `Bold` = 1
- `Italic` = 2
- `BoldAndItalic` = 3

---

#### FontStyles

**Line:** 1349324

**Values:**

- `Normal` = 0
- `Bold` = 1
- `Italic` = 2
- `Underline` = 4
- `LowerCase` = 8
- `UpperCase` = 16
- `SmallCaps` = 32
- `Strikethrough` = 64
- `Superscript` = 128
- `Subscript` = 256
- `Highlight` = 512

---

#### FontWeight

**Line:** 1227124

**Values:**

- `Thin` = 100
- `ExtraLight` = 200
- `Light` = 300
- `Regular` = 400
- `Medium` = 500
- `SemiBold` = 600
- `Bold` = 700
- `Heavy` = 800
- `Black` = 900

---

#### ForceMode2D

**Line:** 1578329

**Values:**

- `Force` = 0
- `Impulse` = 1

---

#### FormatError

**Line:** 1200778

**Values:**

- `None` = 0
- `Overflow` = 1
- `BadFormatSpecifier` = 2

---

#### FormatSwizzle

**Line:** 892162

**Values:**

- `FormatSwizzleR` = 0
- `FormatSwizzleG` = 1
- `FormatSwizzleB` = 2
- `FormatSwizzleA` = 3
- `FormatSwizzle0` = 4
- `FormatSwizzle1` = 5

---

#### FormatUsage

**Line:** 899359

**Values:**

- `Sample` = 0
- `Linear` = 1
- `Sparse` = 2
- `Render` = 4
- `Blend` = 5
- `GetPixels` = 6
- `SetPixels` = 7
- `SetPixels32` = 8
- `ReadPixels` = 9
- `LoadStore` = 10
- `MSAA2x` = 11
- `MSAA4x` = 12
- `MSAA8x` = 13
- `StencilSampling` = 16

---

#### FormatterAssemblyStyle

**Line:** 226394

**Values:**

- `Simple` = 0
- `Full` = 1

---

#### FormatterTypeStyle

**Line:** 226384

**Values:**

- `TypesWhenNeeded` = 0
- `TypesAlways` = 1
- `XsdString` = 2

---

#### Formatting

**Line:** 1025962

**Values:**

- `None` = 0
- `Indented` = 1

---

#### FormattingHelpers

**Line:** 467056

---

#### FoveatedRenderingCaps

**Line:** 892430

**Values:**

- `None` = 0
- `FoveationImage` = 1
- `NonUniformRaster` = 2
- `ModeChangeOnlyBeforeRenderTargetSet` = 4

---

#### FoveatedRenderingMode

**Line:** 892441

**Values:**

- `Disabled` = 0
- `Enabled` = 1

---

#### FtpStatusCode

**Line:** 791471

**Values:**

- `Undefined` = 0
- `RestartMarker` = 110
- `ServiceTemporarilyNotAvailable` = 120
- `DataAlreadyOpen` = 125
- `OpeningData` = 150
- `CommandOK` = 200
- `CommandExtraneous` = 202
- `DirectoryStatus` = 212
- `FileStatus` = 213
- `SystemType` = 215
- `SendUserCommand` = 220
- `ClosingControl` = 221
- `ClosingData` = 226
- `EnteringPassive` = 227
- `LoggedInProceed` = 230
- `ServerWantsSecureSession` = 234
- `FileActionOK` = 250
- `PathnameCreated` = 257
- `SendPasswordCommand` = 331
- `NeedLoginAccount` = 332
- `FileCommandPending` = 350
- `ServiceNotAvailable` = 421
- `CantOpenData` = 425
- `ConnectionClosed` = 426
- `ActionNotTakenFileUnavailableOrBusy` = 450
- `ActionAbortedLocalProcessingError` = 451
- `ActionNotTakenInsufficientSpace` = 452
- `CommandSyntaxError` = 500
- `ArgumentSyntaxError` = 501
- `CommandNotImplemented` = 502
- `BadCommandSequence` = 503
- `NotLoggedIn` = 530
- `AccountNeeded` = 532
- `ActionNotTakenFileUnavailable` = 550
- `ActionAbortedUnknownPageType` = 551
- `FileActionAborted` = 552
- `ActionNotTakenFilenameNotAllowed` = 553

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

- `Weak` = 0
- `WeakTrackResurrection` = 1
- `Normal` = 2
- `Pinned` = 3

---

#### GPUResidentDrawerMode

**Line:** 1378040

**Values:**

- `Disabled` = 0
- `InstancedDrawing` = 1

---

#### GPUResidentDrawerResources

**Line:** 1377832

---

#### GameConfigDeduplicationOwnership

**Line:** 596202

**Values:**

- `None` = 0
- `Baseline` = 1
- `SinglePatch` = 2

---

#### GameConfigRuntimeStorageMode

**Line:** 588373

**Values:**

- `Invalid` = 0
- `Deduplicating` = 1
- `Solo` = 2

---

#### GameConfigSpreadsheetReader

**Line:** 599279

---

#### GemSkipTarget

**Line:** 1052346

**Values:**

- `Forge` = 0
- `PetEgg` = 1
- `TechTree` = 2

---

#### GenerateTestsForBurstCompatibilityAttribute

**Line:** 1184652

---

#### GenericParameterAttributes

**Line:** 265530

**Values:**

- `None` = 0
- `VarianceMask` = 3
- `Covariant` = 1
- `Contravariant` = 2
- `SpecialConstraintMask` = 28
- `ReferenceTypeConstraint` = 4
- `NotNullableValueTypeConstraint` = 8
- `DefaultConstructorConstraint` = 16

---

#### GizmoSubset

**Line:** 895735

**Values:**

- `PreImageEffects` = 0
- `PostImageEffects` = 1

---

#### GlyphClassDefinitionType

**Line:** 1557355

**Values:**

- `Undefined` = 0
- `Base` = 1
- `Ligature` = 2
- `Mark` = 3
- `Component` = 4

---

#### GlyphLoadFlags

**Line:** 1557562

**Values:**

- `LOAD_DEFAULT` = 0
- `LOAD_NO_SCALE` = 1
- `LOAD_NO_HINTING` = 2
- `LOAD_RENDER` = 4
- `LOAD_NO_BITMAP` = 8
- `LOAD_FORCE_AUTOHINT` = 32
- `LOAD_MONOCHROME` = 4096
- `LOAD_NO_AUTOHINT` = 32768
- `LOAD_COLOR` = 1048576
- `LOAD_COMPUTE_METRICS` = 2097152
- `LOAD_BITMAP_METRICS_ONLY` = 4194304

---

#### GlyphPackingMode

**Line:** 1557624

**Values:**

- `BestShortSideFit` = 0
- `BestLongSideFit` = 1
- `BestAreaFit` = 2
- `BottomLeftRule` = 3
- `ContactPointRule` = 4

---

#### GlyphRenderMode

**Line:** 1557603

**Values:**

- `DEFAULT` = 0
- `SMOOTH_HINTED` = 4121
- `SMOOTH` = 4117
- `COLOR_HINTED` = 69656
- `COLOR` = 69652
- `RASTER_HINTED` = 4122
- `RASTER` = 4118
- `SDF` = 4134
- `SDF8` = 8230
- `SDF16` = 16422
- `SDF32` = 32806
- `SDFAA_HINTED` = 4169
- `SDFAA` = 4165

---

#### GooglePlayProrationMode

**Line:** 1403669

**Values:**

- `UnknownSubscriptionUpgradeDowngradePolicy` = 0
- `ImmediateWithTimeProration` = 1
- `ImmediateAndChargeProratedPrice` = 2
- `ImmediateWithoutProration` = 3
- `Deferred` = 4
- `ImmediateAndChargeFullPrice` = 5

---

#### GooglePlayReplacementMode

**Line:** 1403655

**Values:**

- `UnknownReplacementMode` = 0
- `WithTimeProration` = 1
- `ChargeProratedPrice` = 2
- `WithoutProration` = 3
- `ChargeFullPrice` = 5
- `Deferred` = 4

---

#### GooglePurchaseState

**Line:** 1545038

**Values:**

- `Purchased` = 0
- `Cancelled` = 1
- `Refunded` = 2
- `Deferred` = 4

---

#### GotoExpressionKind

**Line:** 1287361

**Values:**

- `Goto` = 0
- `Return` = 1
- `Break` = 2
- `Continue` = 3

---

#### GradientMode

**Line:** 878987

**Values:**

- `Blend` = 0
- `Fixed` = 1
- `PerceptualBlend` = 2

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

- `OpenGL2` = 0
- `Direct3D9` = 1
- `Direct3D11` = 2
- `PlayStation3` = 3
- `Null` = 4
- `Xbox360` = 6
- `OpenGLES2` = 8
- `OpenGLES3` = 11
- `PlayStationVita` = 12
- `PlayStation4` = 13
- `XboxOne` = 14
- `PlayStationMobile` = 15
- `Metal` = 16
- `OpenGLCore` = 17
- `Direct3D12` = 18
- `N3DS` = 19
- `Vulkan` = 21
- `Switch` = 22
- `XboxOneD3D12` = 23
- `GameCoreXboxOne` = 24
- `GameCoreXboxSeries` = 25
- `PlayStation5` = 26
- `PlayStation5NGGC` = 27
- `WebGPU` = 28
- `Switch2` = 29

---

#### GraphicsFenceType

**Line:** 892522

**Values:**

- `AsyncQueueSynchronisation` = 0
- `CPUSynchronisation` = 1

---

#### GraphicsFormat

**Line:** 899415

**Values:**

- `None` = 0
- `R8_SRGB` = 1
- `R8G8_SRGB` = 2
- `R8G8B8_SRGB` = 3
- `R8G8B8A8_SRGB` = 4
- `R8_UNorm` = 5
- `R8G8_UNorm` = 6
- `R8G8B8_UNorm` = 7
- `R8G8B8A8_UNorm` = 8
- `R8_SNorm` = 9
- `R8G8_SNorm` = 10
- `R8G8B8_SNorm` = 11
- `R8G8B8A8_SNorm` = 12
- `R8_UInt` = 13
- `R8G8_UInt` = 14
- `R8G8B8_UInt` = 15
- `R8G8B8A8_UInt` = 16
- `R8_SInt` = 17
- `R8G8_SInt` = 18
- `R8G8B8_SInt` = 19
- `R8G8B8A8_SInt` = 20
- `R16_UNorm` = 21
- `R16G16_UNorm` = 22
- `R16G16B16_UNorm` = 23
- `R16G16B16A16_UNorm` = 24
- `R16_SNorm` = 25
- `R16G16_SNorm` = 26
- `R16G16B16_SNorm` = 27
- `R16G16B16A16_SNorm` = 28
- `R16_UInt` = 29
- `R16G16_UInt` = 30
- `R16G16B16_UInt` = 31
- `R16G16B16A16_UInt` = 32
- `R16_SInt` = 33
- `R16G16_SInt` = 34
- `R16G16B16_SInt` = 35
- `R16G16B16A16_SInt` = 36
- `R32_UInt` = 37
- `R32G32_UInt` = 38
- `R32G32B32_UInt` = 39
- `R32G32B32A32_UInt` = 40
- `R32_SInt` = 41
- `R32G32_SInt` = 42
- `R32G32B32_SInt` = 43
- `R32G32B32A32_SInt` = 44
- `R16_SFloat` = 45
- `R16G16_SFloat` = 46
- `R16G16B16_SFloat` = 47
- `R16G16B16A16_SFloat` = 48
- `R32_SFloat` = 49
- `R32G32_SFloat` = 50
- `R32G32B32_SFloat` = 51
- `R32G32B32A32_SFloat` = 52
- `B8G8R8_SRGB` = 56
- `B8G8R8A8_SRGB` = 57
- `B8G8R8_UNorm` = 58
- `B8G8R8A8_UNorm` = 59
- `B8G8R8_SNorm` = 60
- `B8G8R8A8_SNorm` = 61
- `B8G8R8_UInt` = 62
- `B8G8R8A8_UInt` = 63
- `B8G8R8_SInt` = 64
- `B8G8R8A8_SInt` = 65
- `R4G4B4A4_UNormPack16` = 66
- `B4G4R4A4_UNormPack16` = 67
- `R5G6B5_UNormPack16` = 68
- `B5G6R5_UNormPack16` = 69
- `R5G5B5A1_UNormPack16` = 70
- `B5G5R5A1_UNormPack16` = 71
- `A1R5G5B5_UNormPack16` = 72
- `E5B9G9R9_UFloatPack32` = 73
- `B10G11R11_UFloatPack32` = 74
- `A2B10G10R10_UNormPack32` = 75
- `A2B10G10R10_UIntPack32` = 76
- `A2B10G10R10_SIntPack32` = 77
- `A2R10G10B10_UNormPack32` = 78
- `A2R10G10B10_UIntPack32` = 79
- `A2R10G10B10_SIntPack32` = 80
- `A2R10G10B10_XRSRGBPack32` = 81
- `A2R10G10B10_XRUNormPack32` = 82
- `R10G10B10_XRSRGBPack32` = 83
- `R10G10B10_XRUNormPack32` = 84
- `A10R10G10B10_XRSRGBPack32` = 85
- `A10R10G10B10_XRUNormPack32` = 86
- `D16_UNorm` = 90
- `D24_UNorm` = 91
- `D24_UNorm_S8_UInt` = 92
- `D32_SFloat` = 93
- `D32_SFloat_S8_UInt` = 94
- `S8_UInt` = 95
- `RGB_DXT1_SRGB` = 96
- `RGBA_DXT1_SRGB` = 96

---

#### GraphicsFormatUsage

**Line:** 899381

**Values:**

- `None` = 0
- `Sample` = 1
- `Linear` = 2
- `Sparse` = 4
- `Render` = 16
- `Blend` = 32
- `GetPixels` = 64
- `SetPixels` = 128
- `SetPixels32` = 256
- `ReadPixels` = 512
- `LoadStore` = 1024
- `MSAA2x` = 2048
- `MSAA4x` = 4096
- `MSAA8x` = 8192
- `StencilSampling` = 65536

---

#### GraphicsTier

**Line:** 891967

**Values:**

- `Tier1` = 0
- `Tier2` = 1
- `Tier3` = 2

---

#### GregorianCalendarTypes

**Line:** 273332

**Values:**

- `Localized` = 1
- `USEnglish` = 2
- `MiddleEastFrench` = 9
- `Arabic` = 10
- `TransliteratedEnglish` = 11
- `TransliteratedFrench` = 12

---

#### GridLayoutGroup

**Line:** 1354650

---

#### GroupAlertBehaviours

**Line:** 1552256

**Values:**

- `GroupAlertAll` = 0
- `GroupAlertSummary` = 1
- `GroupAlertChildren` = 2

---

#### GroupEvent

**Line:** 1547292

**Values:**

- `Added` = 0
- `Removed` = 1
- `AddedOrRemoved` = 2

---

#### GroupOperation

**Line:** 1441382

---

#### HDRACESPreset

**Line:** 909730

**Values:**

- `ACES1000Nits` = 3
- `ACES2000Nits` = 4
- `ACES4000Nits` = 5

---

#### HDRColorBufferPrecision

**Line:** 900488

**Values:**

- `_32Bits` = 0
- `_64Bits` = 1

---

#### HDRColorspace

**Line:** 820422

**Values:**

- `Rec709` = 0
- `Rec2020` = 1
- `P3D65` = 2

---

#### HDRDebugMode

**Line:** 1594429

**Values:**

- `None` = 0
- `GamutView` = 1
- `GamutClip` = 2
- `ValuesAbovePaperWhite` = 3

---

#### HDRDisplaySupportFlags

**Line:** 875642

**Values:**

- `None` = 0
- `Supported` = 1
- `RuntimeSwitchable` = 2
- `AutomaticTonemapping` = 4

---

#### HDREncoding

**Line:** 820433

**Values:**

- `Linear` = 3
- `PQ` = 2
- `Gamma22` = 4
- `sRGB` = 0

---

#### HDROutputUtils

**Line:** 825367

---

#### HDRRangeReduction

**Line:** 820408

**Values:**

- `None` = 0
- `Reinhard` = 1
- `BT2390` = 2
- `ACES1000Nits` = 3
- `ACES2000Nits` = 4
- `ACES4000Nits` = 5

---

#### Handshake

**Line:** 555311

---

#### HapticFeedback

**Line:** 692887

**Values:**

- `Selection` = 0
- `Success` = 1
- `Warning` = 2
- `Failure` = 3
- `LightImpact` = 4
- `MediumImpact` = 5
- `HeavyImpact` = 6
- `RigidImpact` = 7
- `SoftImpact` = 8
- `None` = 9

---

#### HapticPatterns

**Line:** 1579852

---

#### HashAlgorithmType

**Line:** 778436

**Values:**

- `None` = 0
- `Md5` = 32771
- `Sha1` = 32772
- `Sha256` = 32780
- `Sha384` = 32781
- `Sha512` = 32782

---

#### HeaderImageType

**Line:** 1565197

**Values:**

- `Undefined` = 0
- `Extended` = 1
- `Custom` = 2
- `Hidden` = 3

---

#### HealthCheckTypeBits

**Line:** 551621

**Values:**

- `GlobalState` = 1
- `Database` = 2

---

#### HebrewMonthNumbering

**Line:** 1166976

**Values:**

- `Civil` = 1
- `Scriptural` = 2

---

#### HelpBoxMessageType

**Line:** 617863

**Values:**

- `None` = 0
- `Info` = 1
- `Warning` = 2
- `Error` = 3

---

#### HexConverter

**Line:** 1519948

---

#### HideFlags

**Line:** 883894

**Values:**

- `None` = 0
- `HideInHierarchy` = 1
- `HideInInspector` = 2
- `DontSaveInEditor` = 4
- `NotEditable` = 8
- `DontSaveInBuild` = 16
- `DontUnloadUnusedAsset` = 32
- `DontSave` = 52
- `HideAndDontSave` = 61

---

#### HierarchyNodeFlags

**Line:** 1562526

**Values:**

- `None` = 0
- `Expanded` = 1
- `Selected` = 2
- `Cut` = 4
- `Hidden` = 8

---

#### HierarchyPropertyStorageType

**Line:** 1562644

**Values:**

- `Sparse` = 0
- `Dense` = 1
- `Blob` = 2
- `Default` = 1

---

#### HierarchySearchFilterOperator

**Line:** 1562656

**Values:**

- `Equal` = 0
- `Contains` = 1
- `Greater` = 2
- `GreaterOrEqual` = 3
- `Lesser` = 4
- `LesserOrEqual` = 5
- `NotEqual` = 6
- `Not` = 7

---

#### HorizontalAlignmentOptions

**Line:** 1227006

**Values:**

- `Left` = 1
- `Center` = 2
- `Right` = 4
- `Justified` = 8
- `Flush` = 16
- `Geometry` = 32

---

#### HorizontalWrapMode

**Line:** 1580966

**Values:**

- `Wrap` = 0
- `Overflow` = 1

---

#### HttpCompletionOption

**Line:** 1488381

**Values:**

- `ResponseContentRead` = 0
- `ResponseHeadersRead` = 1

---

#### HttpRequestHeader

**Line:** 791627

**Values:**

- `CacheControl` = 0
- `Connection` = 1
- `Date` = 2
- `KeepAlive` = 3
- `Pragma` = 4
- `Trailer` = 5
- `TransferEncoding` = 6
- `Upgrade` = 7
- `Via` = 8
- `Warning` = 9
- `Allow` = 10
- `ContentLength` = 11
- `ContentType` = 12
- `ContentEncoding` = 13
- `ContentLanguage` = 14
- `ContentLocation` = 15
- `ContentMd5` = 16
- `ContentRange` = 17
- `Expires` = 18
- `LastModified` = 19
- `Accept` = 20
- `AcceptCharset` = 21
- `AcceptEncoding` = 22
- `AcceptLanguage` = 23
- `Authorization` = 24
- `Cookie` = 25
- `Expect` = 26
- `From` = 27
- `Host` = 28
- `IfMatch` = 29
- `IfModifiedSince` = 30
- `IfNoneMatch` = 31
- `IfRange` = 32
- `IfUnmodifiedSince` = 33
- `MaxForwards` = 34
- `ProxyAuthorization` = 35
- `Referer` = 36
- `Range` = 37
- `Te` = 38
- `Translate` = 39
- `UserAgent` = 40

---

#### HttpStatusCode

**Line:** 790015

**Values:**

- `Continue` = 100
- `SwitchingProtocols` = 101
- `Processing` = 102
- `EarlyHints` = 103
- `OK` = 200
- `Created` = 201
- `Accepted` = 202
- `NonAuthoritativeInformation` = 203
- `NoContent` = 204
- `ResetContent` = 205
- `PartialContent` = 206
- `MultiStatus` = 207
- `AlreadyReported` = 208
- `IMUsed` = 226
- `MultipleChoices` = 300
- `Ambiguous` = 300
- `MovedPermanently` = 301
- `Moved` = 301
- `Found` = 302
- `Redirect` = 302
- `SeeOther` = 303
- `RedirectMethod` = 303
- `NotModified` = 304
- `UseProxy` = 305
- `Unused` = 306
- `TemporaryRedirect` = 307
- `RedirectKeepVerb` = 307
- `PermanentRedirect` = 308
- `BadRequest` = 400
- `Unauthorized` = 401
- `PaymentRequired` = 402
- `Forbidden` = 403
- `NotFound` = 404
- `MethodNotAllowed` = 405
- `NotAcceptable` = 406
- `ProxyAuthenticationRequired` = 407
- `RequestTimeout` = 408
- `Conflict` = 409
- `Gone` = 410
- `LengthRequired` = 411
- `PreconditionFailed` = 412
- `RequestEntityTooLarge` = 413
- `RequestUriTooLong` = 414
- `UnsupportedMediaType` = 415
- `RequestedRangeNotSatisfiable` = 416
- `ExpectationFailed` = 417
- `MisdirectedRequest` = 421
- `UnprocessableEntity` = 422
- `Locked` = 423
- `FailedDependency` = 424
- `UpgradeRequired` = 426
- `PreconditionRequired` = 428
- `TooManyRequests` = 429
- `RequestHeaderFieldsTooLarge` = 431
- `UnavailableForLegalReasons` = 451
- `InternalServerError` = 500
- `NotImplemented` = 501
- `BadGateway` = 502
- `ServiceUnavailable` = 503
- `GatewayTimeout` = 504
- `HttpVersionNotSupported` = 505
- `VariantAlsoNegotiates` = 506
- `InsufficientStorage` = 507
- `LoopDetected` = 508
- `NotExtended` = 510
- `NetworkAuthenticationRequired` = 511

---

#### HttpTransportType

**Line:** 1583108

**Values:**

- `None` = 0
- `WebSockets` = 1
- `ServerSentEvents` = 2
- `LongPolling` = 4

---

#### HttpVerb

**Line:** 684772

**Values:**

- `Get` = 0
- `Post` = 1
- `Put` = 2
- `Delete` = 3

---

#### HubConnectionState

**Line:** 1415706

**Values:**

- `Disconnected` = 0
- `Connected` = 1
- `Connecting` = 2
- `Reconnecting` = 3

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

- `Auto` = 0
- `On` = 1
- `Off` = 2

---

#### IOControlCode

**Line:** 800323

**Values:**

- `AsyncIO` = 2147772029
- `NonBlockingIO` = 2147772030
- `DataToRead` = 1074030207
- `OobDataRead` = 1074033415
- `AssociateHandle` = 2281701377
- `EnableCircularQueuing` = 671088642
- `Flush` = 671088644
- `GetBroadcastAddress` = 1207959557
- `GetExtensionFunctionPointer` = 3355443206
- `GetQos` = 3355443207
- `GetGroupQos` = 3355443208
- `MultipointLoopback` = 2281701385
- `MulticastScope` = 2281701386
- `SetQos` = 2281701387
- `SetGroupQos` = 2281701388
- `TranslateHandle` = 3355443213
- `RoutingInterfaceQuery` = 3355443220
- `RoutingInterfaceChange` = 2281701397
- `AddressListQuery` = 1207959574
- `AddressListChange` = 671088663
- `QueryTargetPnpHandle` = 1207959576
- `NamespaceChange` = 2281701401
- `AddressListSort` = 3355443225
- `ReceiveAll` = 2550136833
- `ReceiveAllMulticast` = 2550136834
- `ReceiveAllIgmpMulticast` = 2550136835
- `KeepAliveValues` = 2550136836
- `AbsorbRouterAlert` = 2550136837
- `UnicastInterface` = 2550136838
- `LimitBroadcasts` = 2550136839
- `BindToInterface` = 2550136840
- `MulticastInterface` = 2550136841
- `AddMulticastGroupOnInterface` = 2550136842
- `DeleteMulticastGroupFromInterface` = 2550136843

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

- `ImageLeft` = 0
- `ImageAbove` = 1
- `ImageOnly` = 2
- `TextOnly` = 3

---

#### ImpactSfx

**Line:** 705764

**Values:**

- `None` = 0
- `Metal` = 1
- `Rock` = 2
- `Explosion` = 3
- `LightStab` = 4
- `HeavyStab` = 5
- `Glass` = 7

---

#### ImplicitUseKindFlags

**Line:** 869290

**Values:**

- `Default` = 7
- `Access` = 1
- `Assign` = 2
- `InstantiatedWithFixedConstructorSignature` = 4
- `InstantiatedNoFixedConstructorSignature` = 8

---

#### ImplicitUseTargetFlags

**Line:** 869303

**Values:**

- `Default` = 1
- `Itself` = 1
- `Members` = 2
- `WithMembers` = 3

---

#### Importance

**Line:** 1553122

**Values:**

- `None` = 0
- `Low` = 2
- `Default` = 3
- `High` = 4

---

#### InAppProductType

**Line:** 584115

**Values:**

- `Consumable` = 0
- `NonConsumable` = 1
- `Subscription` = 2

---

#### InAppPurchaseClientRefuseReason

**Line:** 584539

**Values:**

- `Unknown` = 0
- `CompletionActionFailed` = 1
- `UnityUserCancelled` = 2
- `UnityPurchasingUnavailable` = 3
- `UnityExistingPurchasePending` = 4
- `UnityProductUnavailable` = 5
- `UnitySignatureInvalid` = 6
- `UnityPaymentDeclined` = 7
- `UnityDuplicateTransaction` = 8

---

#### InAppPurchaseFlowKind

**Line:** 584393

**Values:**

- `ClientDriven` = 0
- `ServerDriven` = 1

---

#### InAppPurchasePaymentType

**Line:** 584556

**Values:**

- `Normal` = 0
- `Sandbox` = 1

---

#### InAppPurchaseStatus

**Line:** 584403

**Values:**

- `PendingValidation` = 0
- `Successful` = 1
- `Failed` = 2
- `ReceiptAlreadyUsed` = 3
- `_Reserved_4` = 4
- `_Reserved_5` = 5
- `_Reserved_6` = 6
- `Refunded` = 7
- `MissingContent` = 8
- `UserDeclined` = 9
- `Abandoned` = 10

---

#### IndexFormat

**Line:** 891630

**Values:**

- `UInt16` = 0
- `UInt32` = 1

---

#### IndirectBufferContext

**Line:** 1381322

---

#### InitResult

**Line:** 1492788

**Values:**

- `Success` = 0
- `FailedMissingDependency` = 1

---

#### InitializationFailureReason

**Line:** 1530606

**Values:**

- `PurchasingUnavailable` = 0
- `NoProductsAvailable` = 1
- `AppNotKnown` = 2

---

#### InjectPlayerLoopTimings

**Line:** 1099320

**Values:**

- `All` = 65535
- `Standard` = 30037
- `Minimum` = 8464
- `Initialization` = 1
- `LastInitialization` = 2
- `EarlyUpdate` = 4
- `LastEarlyUpdate` = 8
- `FixedUpdate` = 16
- `LastFixedUpdate` = 32
- `PreUpdate` = 64
- `LastPreUpdate` = 128
- `Update` = 256
- `LastUpdate` = 512
- `PreLateUpdate` = 1024
- `LastPreLateUpdate` = 2048
- `PostLateUpdate` = 4096
- `LastPostLateUpdate` = 8192
- `TimeUpdate` = 16384
- `LastTimeUpdate` = 32768

---

#### InputField

**Line:** 1353472

---

#### InspectorSort

**Line:** 883133

**Values:**

- `ByName` = 0
- `ByValue` = 1

---

#### InspectorSortDirection

**Line:** 883142

**Values:**

- `Ascending` = 0
- `Descending` = 1

---

#### InstantiationKind

**Line:** 1477856

**Values:**

- `Activator` = 0
- `PropertyBagOverride` = 1
- `NotInstantiatable` = 2

---

#### IntermediateTextureMode

**Line:** 908224

**Values:**

- `Auto` = 0
- `Always` = 1

---

#### IslamicEpoch

**Line:** 1167096

**Values:**

- `Astronomical` = 1
- `Civil` = 2

---

#### IslamicLeapYearPattern

**Line:** 1167105

**Values:**

- `Base15` = 1
- `Base16` = 2
- `Indian` = 3
- `HabashAlHasib` = 4

---

#### IsoDayOfWeek

**Line:** 1144355

**Values:**

- `None` = 0
- `Monday` = 1
- `Tuesday` = 2
- `Wednesday` = 3
- `Thursday` = 4
- `Friday` = 5
- `Saturday` = 6
- `Sunday` = 7

---

#### ItemType

**Line:** 1067865

**Values:**

- `Helmet` = 0
- `Armour` = 1
- `Gloves` = 2
- `Necklace` = 3
- `Ring` = 4
- `Weapon` = 5
- `Shoes` = 6
- `Belt` = 7

---

#### JTokenType

**Line:** 1046705

**Values:**

- `None` = 0
- `Object` = 1
- `Array` = 2
- `Constructor` = 3
- `Property` = 4
- `Comment` = 5
- `Integer` = 6
- `Float` = 7
- `String` = 8
- `Boolean` = 9
- `Null` = 10
- `Undefined` = 11
- `Date` = 12
- `Raw` = 13
- `Bytes` = 14
- `Guid` = 15
- `Uri` = 16
- `TimeSpan` = 17

---

#### JoinType

**Line:** 1361504

**Values:**

- `jtRound` = 0

---

#### JsonCommentHandling

**Line:** 991902

**Values:**

- `Disallow` = 0
- `Skip` = 1
- `Allow` = 2

---

#### JsonIgnoreCondition

**Line:** 1003212

**Values:**

- `Never` = 0
- `Always` = 1
- `WhenWritingDefault` = 2
- `WhenWritingNull` = 3

---

#### JsonKnownNamingPolicy

**Line:** 1003223

**Values:**

- `Unspecified` = 0
- `CamelCase` = 1
- `SnakeCaseLower` = 2
- `SnakeCaseUpper` = 3
- `KebabCaseLower` = 4
- `KebabCaseUpper` = 5

---

#### JsonNumberHandling

**Line:** 1003237

**Values:**

- `Strict` = 0
- `AllowReadingFromString` = 1
- `WriteAsString` = 2
- `AllowNamedFloatingPointLiterals` = 4

---

#### JsonObjectCreationHandling

**Line:** 1003248

**Values:**

- `Replace` = 0
- `Populate` = 1

---

#### JsonSchemaType

**Line:** 1042816

**Values:**

- `None` = 0
- `String` = 1
- `Float` = 2
- `Integer` = 4
- `Boolean` = 8
- `Object` = 16
- `Array` = 32
- `Null` = 64
- `Any` = 127

---

#### JsonSerializationMode

**Line:** 582798

**Values:**

- `Default` = 0
- `GdprExport` = 1
- `AnalyticsEvents` = 2
- `AdminApi` = 3

---

#### JsonSerializerDefaults

**Line:** 992346

**Values:**

- `General` = 0
- `Web` = 1

---

#### JsonSerializerTrackedObject

**Line:** 1329076

---

#### JsonSourceGenerationMode

**Line:** 1003306

**Values:**

- `Default` = 0
- `Metadata` = 1
- `Serialization` = 2

---

#### JsonToken

**Line:** 1030954

**Values:**

- `None` = 0
- `StartObject` = 1
- `StartArray` = 2
- `StartConstructor` = 3
- `PropertyName` = 4
- `Comment` = 5
- `Raw` = 6
- `Integer` = 7
- `Float` = 8
- `String` = 9
- `Boolean` = 10
- `Null` = 11
- `Undefined` = 12
- `EndObject` = 13
- `EndArray` = 14
- `EndConstructor` = 15
- `Date` = 16
- `Bytes` = 17

---

#### JsonTokenType

**Line:** 993577

**Values:**

- `None` = 0
- `StartObject` = 1
- `EndObject` = 2
- `StartArray` = 3
- `EndArray` = 4
- `PropertyName` = 5
- `Comment` = 6
- `String` = 7
- `Number` = 8
- `True` = 9
- `False` = 10
- `Null` = 11

---

#### JsonTypeInfoKind

**Line:** 1011784

**Values:**

- `None` = 0
- `Object` = 1
- `Enumerable` = 2
- `Dictionary` = 3

---

#### JsonUnknownDerivedTypeHandling

**Line:** 1004049

**Values:**

- `FailSerialization` = 0
- `FallBackToBaseType` = 1
- `FallBackToNearestAncestor` = 2

---

#### JsonUnknownTypeHandling

**Line:** 1003611

**Values:**

- `JsonElement` = 0
- `JsonNode` = 1

---

#### JsonValueKind

**Line:** 993416

**Values:**

- `Undefined` = 0
- `Object` = 1
- `Array` = 2
- `String` = 3
- `Number` = 4
- `True` = 5
- `False` = 6
- `Null` = 7

---

#### Justify

**Line:** 659904

**Values:**

- `FlexStart` = 0
- `Center` = 1
- `FlexEnd` = 2
- `SpaceBetween` = 3
- `SpaceAround` = 4
- `SpaceEvenly` = 5

---

#### KeyCode

**Line:** 878237

**Values:**

- `None` = 0
- `Backspace` = 8
- `Delete` = 127
- `Tab` = 9
- `Clear` = 12
- `Return` = 13
- `Pause` = 19
- `Escape` = 27
- `Space` = 32
- `Keypad0` = 256
- `Keypad1` = 257
- `Keypad2` = 258
- `Keypad3` = 259
- `Keypad4` = 260
- `Keypad5` = 261
- `Keypad6` = 262
- `Keypad7` = 263
- `Keypad8` = 264
- `Keypad9` = 265
- `KeypadPeriod` = 266
- `KeypadDivide` = 267
- `KeypadMultiply` = 268
- `KeypadMinus` = 269
- `KeypadPlus` = 270
- `KeypadEnter` = 271
- `KeypadEquals` = 272
- `UpArrow` = 273
- `DownArrow` = 274
- `RightArrow` = 275
- `LeftArrow` = 276
- `Insert` = 277
- `Home` = 278
- `End` = 279
- `PageUp` = 280
- `PageDown` = 281
- `F1` = 282
- `F2` = 283
- `F3` = 284
- `F4` = 285
- `F5` = 286
- `F6` = 287
- `F7` = 288
- `F8` = 289
- `F9` = 290
- `F10` = 291
- `F11` = 292
- `F12` = 293
- `F13` = 294
- `F14` = 295
- `F15` = 296
- `Alpha0` = 48
- `Alpha1` = 49
- `Alpha2` = 50
- `Alpha3` = 51
- `Alpha4` = 52
- `Alpha5` = 53
- `Alpha6` = 54
- `Alpha7` = 55
- `Alpha8` = 56
- `Alpha9` = 57
- `Exclaim` = 33
- `DoubleQuote` = 34
- `Hash` = 35
- `Dollar` = 36
- `Percent` = 37
- `Ampersand` = 38
- `Quote` = 39
- `LeftParen` = 40
- `RightParen` = 41
- `Asterisk` = 42
- `Plus` = 43
- `Comma` = 44
- `Minus` = 45
- `Period` = 46
- `Slash` = 47
- `Colon` = 58
- `Semicolon` = 59
- `Less` = 60
- `Equals` = 61
- `Greater` = 62
- `Question` = 63
- `At` = 64
- `LeftBracket` = 91
- `Backslash` = 92
- `RightBracket` = 93
- `Caret` = 94
- `Underscore` = 95
- `BackQuote` = 96
- `A` = 97
- `B` = 98
- `C` = 99
- `D` = 100
- `E` = 101
- `F` = 102
- `G` = 103
- `H` = 104

---

#### KeyEvent

**Line:** 1556064

---

#### KeyboardNavigationOperation

**Line:** 641267

**Values:**

- `None` = 0
- `SelectAll` = 1
- `Cancel` = 2
- `Submit` = 3
- `Previous` = 4
- `Next` = 5
- `MoveRight` = 6
- `MoveLeft` = 7
- `PageUp` = 8
- `PageDown` = 9
- `Begin` = 10
- `End` = 11

---

#### KnownColor

**Line:** 1548958

**Values:**

- `ActiveBorder` = 1
- `ActiveCaption` = 2
- `ActiveCaptionText` = 3
- `AppWorkspace` = 4
- `Control` = 5
- `ControlDark` = 6
- `ControlDarkDark` = 7
- `ControlLight` = 8
- `ControlLightLight` = 9
- `ControlText` = 10
- `Desktop` = 11
- `GrayText` = 12
- `Highlight` = 13
- `HighlightText` = 14
- `HotTrack` = 15
- `InactiveBorder` = 16
- `InactiveCaption` = 17
- `InactiveCaptionText` = 18
- `Info` = 19
- `InfoText` = 20
- `Menu` = 21
- `MenuText` = 22
- `ScrollBar` = 23
- `Window` = 24
- `WindowFrame` = 25
- `WindowText` = 26
- `Transparent` = 27
- `AliceBlue` = 28
- `AntiqueWhite` = 29
- `Aqua` = 30
- `Aquamarine` = 31
- `Azure` = 32
- `Beige` = 33
- `Bisque` = 34
- `Black` = 35
- `BlanchedAlmond` = 36
- `Blue` = 37
- `BlueViolet` = 38
- `Brown` = 39
- `BurlyWood` = 40
- `CadetBlue` = 41
- `Chartreuse` = 42
- `Chocolate` = 43
- `Coral` = 44
- `CornflowerBlue` = 45
- `Cornsilk` = 46
- `Crimson` = 47
- `Cyan` = 48
- `DarkBlue` = 49
- `DarkCyan` = 50
- `DarkGoldenrod` = 51
- `DarkGray` = 52
- `DarkGreen` = 53
- `DarkKhaki` = 54
- `DarkMagenta` = 55
- `DarkOliveGreen` = 56
- `DarkOrange` = 57
- `DarkOrchid` = 58
- `DarkRed` = 59
- `DarkSalmon` = 60
- `DarkSeaGreen` = 61
- `DarkSlateBlue` = 62
- `DarkSlateGray` = 63
- `DarkTurquoise` = 64
- `DarkViolet` = 65
- `DeepPink` = 66
- `DeepSkyBlue` = 67
- `DimGray` = 68
- `DodgerBlue` = 69
- `Firebrick` = 70
- `FloralWhite` = 71
- `ForestGreen` = 72
- `Fuchsia` = 73
- `Gainsboro` = 74
- `GhostWhite` = 75
- `Gold` = 76
- `Goldenrod` = 77
- `Gray` = 78
- `Green` = 79
- `GreenYellow` = 80
- `Honeydew` = 81
- `HotPink` = 82
- `IndianRed` = 83
- `Indigo` = 84
- `Ivory` = 85
- `Khaki` = 86
- `Lavender` = 87
- `LavenderBlush` = 88
- `LawnGreen` = 89
- `LemonChiffon` = 90
- `LightBlue` = 91
- `LightCoral` = 92
- `LightCyan` = 93
- `LightGoldenrodYellow` = 94
- `LightGray` = 95
- `LightGreen` = 96

---

#### LODCrossFadeDitheringType

**Line:** 900603

**Values:**

- `BayerMatrix` = 0
- `BlueNoise` = 1

---

#### LODFadeMode

**Line:** 875695

**Values:**

- `None` = 0
- `CrossFade` = 1
- `SpeedTree` = 2

---

#### Language

**Line:** 1564125

**Values:**

- `Arabic` = 0
- `Catalan` = 1
- `ChineseHongKong` = 2
- `ChineseSimplified` = 3
- `ChineseTraditional` = 4
- `Croatian` = 5
- `Czech` = 6
- `Danish` = 7
- `Dutch` = 8
- `EnglishAustralia` = 9
- `EnglishIndia` = 10
- `EnglishUnitedKingdom` = 11
- `Finnish` = 12
- `French` = 13
- `FrenchCanada` = 14
- `German` = 15
- `Greek` = 16
- `Hebrew` = 17
- `Hindi` = 18
- `Hungarian` = 19
- `Indonesian` = 20
- `Italian` = 21
- `Japanese` = 22
- `Korean` = 23
- `Malay` = 24
- `NorwegianBokmal` = 25
- `Polish` = 26
- `PortuguesePortugal` = 27
- `PortugueseBrazil` = 28
- `Romanian` = 29
- `Russian` = 30
- `Slovak` = 31
- `Spanish` = 32
- `SpanishLatinAmerica` = 33
- `Swedish` = 34
- `Thai` = 35
- `Turkish` = 36
- `Ukrainian` = 37
- `Vietnamese` = 38
- `Other` = 39

---

#### LanguageDirection

**Line:** 670866

**Values:**

- `Inherit` = 0
- `LTR` = 1
- `RTL` = 2

---

#### LanguageSelectionSource

**Line:** 533379

**Values:**

- `AccountCreationAutomatic` = 0
- `ServerSideAutomatic` = 1
- `UserDeviceAutomatic` = 2
- `UserSelected` = 3

---

#### LazyThreadSafetyMode

**Line:** 179021

**Values:**

- `None` = 0
- `PublicationOnly` = 1
- `ExecutionAndPublication` = 2

---

#### LeagueClientPhase

**Line:** 565346

**Values:**

- `NoSession` = 0
- `NoDivision` = 1
- `LoadingDivision` = 2
- `DivisionActive` = 3

---

#### LeagueJoinRefuseReason

**Line:** 565371

**Values:**

- `UnknownReason` = 0
- `LeagueNotEnabled` = 1
- `LeagueNotStarted` = 2
- `SeasonMigrationInProgress` = 3
- `RequirementsNotMet` = 4
- `AlreadyInLeague` = 5

---

#### LeaseState

**Line:** 222271

**Values:**

- `Null` = 0
- `Initial` = 1
- `Active` = 2
- `Renewing` = 3
- `Expired` = 4

---

#### LegalLinksSettings

**Line:** 1564359

**Values:**

- `Undefined` = 0
- `FirstLayerOnly` = 1
- `SecondLayerOnly` = 2
- `Both` = 3
- `Hidden` = 4

---

#### LengthUnit

**Line:** 656388

**Values:**

- `Pixel` = 0
- `Percent` = 1

---

#### LibraryVisibility

**Line:** 669283

**Values:**

- `Default` = 0
- `Visible` = 1
- `Hidden` = 2

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

- `GrayscaleLow` = 0
- `GrayscaleHigh` = 1
- `ColorLow` = 2
- `ColorHigh` = 3
- `ColorHDR` = 4

---

#### LightCookieResolution

**Line:** 900464

**Values:**

- `_256` = 256
- `_512` = 512
- `_1024` = 1024
- `_2048` = 2048
- `_4096` = 4096

---

#### LightLayerEnum

**Line:** 915352

**Values:**

- `Nothing` = 0
- `LightLayerDefault` = 1
- `LightLayer1` = 2
- `LightLayer2` = 4
- `LightLayer3` = 8
- `LightLayer4` = 16
- `LightLayer5` = 32
- `LightLayer6` = 64
- `LightLayer7` = 128
- `Everything` = 255

---

#### LightMode

**Line:** 898848

**Values:**

- `Realtime` = 0
- `Mixed` = 1
- `Baked` = 2
- `Unknown` = 3

---

#### LightProbeSystem

**Line:** 900612

**Values:**

- `LegacyLightProbes` = 0
- `ProbeVolumes` = 1

---

#### LightProbeUsage

**Line:** 892319

**Values:**

- `Off` = 0
- `BlendProbes` = 1
- `UseProxyVolume` = 2
- `CustomProvided` = 4

---

#### LightRenderingMode

**Line:** 900521

**Values:**

- `Disabled` = 0
- `PerVertex` = 2
- `PerPixel` = 1

---

#### LightShadowResolution

**Line:** 891899

**Values:**

- `Low` = 0
- `Medium` = 1
- `High` = 2
- `VeryHigh` = 3

---

#### LightShadows

**Line:** 875261

**Values:**

- `None` = 0
- `Hard` = 1
- `Soft` = 2

---

#### LightShape

**Line:** 875251

**Values:**

- `Cone` = 0
- `Pyramid` = 1
- `Box` = 2

---

#### LightType

**Line:** 898834

**Values:**

- `Directional` = 0
- `Point` = 1
- `Spot` = 2
- `Rectangle` = 3
- `Disc` = 4
- `SpotPyramidShape` = 5
- `SpotBoxShape` = 6

---

#### LightUnit

**Line:** 891912

**Values:**

- `Lumen` = 0
- `Candela` = 1
- `Lux` = 2
- `Nits` = 3
- `Ev100` = 4

---

#### LightmapBakeType

**Line:** 875272

**Values:**

- `Realtime` = 4
- `Baked` = 2
- `Mixed` = 1

---

#### LightmapsMode

**Line:** 875654

**Values:**

- `NonDirectional` = 0
- `CombinedDirectional` = 1

---

#### LineInfoHandling

**Line:** 1047126

**Values:**

- `Ignore` = 0
- `Load` = 1

---

#### LinkBehaviour

**Line:** 1425554

**Values:**

- `PauseOnDisable` = 0
- `PauseOnDisablePlayOnEnable` = 1
- `PauseOnDisableRestartOnEnable` = 2
- `PlayOnEnable` = 3
- `RestartOnEnable` = 4
- `KillOnDisable` = 5
- `KillOnDestroy` = 6
- `CompleteOnDisable` = 7
- `CompleteAndKillOnDisable` = 8
- `RewindOnDisable` = 9
- `RewindAndKillOnDisable` = 10

---

#### ListChangedType

**Line:** 782365

**Values:**

- `Reset` = 0
- `ItemAdded` = 1
- `ItemDeleted` = 2
- `ItemMoved` = 3
- `ItemChanged` = 4
- `PropertyDescriptorAdded` = 5
- `PropertyDescriptorDeleted` = 6
- `PropertyDescriptorChanged` = 7

---

#### ListSortDirection

**Line:** 782380

**Values:**

- `Ascending` = 0
- `Descending` = 1

---

#### ListViewReorderMode

**Line:** 613252

**Values:**

- `Simple` = 0
- `Animated` = 1

---

#### LoadHint

**Line:** 253386

**Values:**

- `Default` = 0
- `Always` = 1
- `Sometimes` = 2

---

#### LoadOptions

**Line:** 1561030

**Values:**

- `None` = 0
- `PreserveWhitespace` = 1
- `SetBaseUri` = 2
- `SetLineInfo` = 4

---

#### LoadSceneMode

**Line:** 888931

**Values:**

- `Single` = 0
- `Additive` = 1

---

#### LocalPhysicsMode

**Line:** 888941

**Values:**

- `None` = 0
- `Physics2D` = 1
- `Physics3D` = 2

---

#### LocalServerCodeReceiver

**Line:** 1372424

---

#### LockRecursionPolicy

**Line:** 1304460

**Values:**

- `NoRecursion` = 0
- `SupportsRecursion` = 1

---

#### LockScreenVisibility

**Line:** 1553133

**Values:**

- `Private` = 0
- `Public` = 1

---

#### LogBehaviour

**Line:** 1428385

**Values:**

- `Default` = 0
- `Verbose` = 1
- `ErrorsOnly` = 2

---

#### LogOption

**Line:** 870565

**Values:**

- `None` = 0
- `NoStacktrace` = 1

---

#### LogType

**Line:** 870553

**Values:**

- `Error` = 0
- `Assert` = 1
- `Warning` = 2
- `Log` = 3
- `Exception` = 4

---

#### LoginMethod

**Line:** 733857

**Values:**

- `Editor` = 0
- `Google` = 1
- `Apple` = 2
- `Facebook` = 3
- `Email` = 4

---

#### LoginOptions

**Line:** 1590231

**Values:**

- `None` = 0
- `IncludeFullName` = 1
- `IncludeEmail` = 2

---

#### LoopType

**Line:** 1425782

**Values:**

- `Restart` = 0
- `Yoyo` = 1
- `Incremental` = 2

---

#### MSAASamples

**Line:** 822171

**Values:**

- `None` = 1
- `MSAA2x` = 2
- `MSAA4x` = 4
- `MSAA8x` = 8

---

#### MainScreenType

**Line:** 721594

**Values:**

- `SkillTab` = 1
- `DungeonTab` = 2
- `ShopTab` = 3
- `ArenaTab` = 4
- `GuildTab` = 5

---

#### MaintenanceModeState

**Line:** 1308186

---

#### MappingType

**Line:** 1086984

**Values:**

- `Element` = 1
- `Attribute` = 2
- `SimpleContent` = 3
- `Hidden` = 4

---

#### MarkerFlags

**Line:** 837340

**Values:**

- `Default` = 0
- `Script` = 2
- `ScriptInvoke` = 32
- `ScriptDeepProfiler` = 64
- `AvailabilityEditor` = 4
- `AvailabilityNonDevelopment` = 8
- `Warning` = 16
- `Counter` = 128
- `SampleGPU` = 256

---

#### MaskingOffsetMode

**Line:** 1227085

**Values:**

- `Percentage` = 0
- `Pixel` = 1

---

#### MaskingTypes

**Line:** 1227050

**Values:**

- `MaskOff` = 0
- `MaskHard` = 1
- `MaskSoft` = 2

---

#### MatchCasing

**Line:** 469815

**Values:**

- `PlatformDefault` = 0
- `CaseSensitive` = 1
- `CaseInsensitive` = 2

---

#### MatchType

**Line:** 469825

**Values:**

- `Simple` = 0
- `Win32` = 1

---

#### MaterialQuality

**Line:** 825538

**Values:**

- `Low` = 1
- `Medium` = 2
- `High` = 4

---

#### MergeArrayHandling

**Line:** 1047135

**Values:**

- `Concat` = 0
- `Union` = 1
- `Replace` = 2
- `Merge` = 3

---

#### MergeNullValueHandling

**Line:** 1047147

**Values:**

- `Ignore` = 0
- `Merge` = 1

---

#### MeshTopology

**Line:** 875335

**Values:**

- `Triangles` = 0
- `Quads` = 2
- `Lines` = 3
- `LineStrip` = 4
- `Points` = 5

---

#### MeshUpdateFlags

**Line:** 891640

**Values:**

- `Default` = 0
- `DontValidateIndices` = 1
- `DontResetBoneBounds` = 2
- `DontNotifyMeshUsers` = 4
- `DontRecalculateBounds` = 8

---

#### MessageDirection

**Line:** 498969

**Values:**

- `Bidirectional` = 0
- `ClientToServer` = 1
- `ServerToClient` = 2
- `ServerInternal` = 3
- `ClientInternal` = 4

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

- `Utc` = 0
- `Local` = 1

---

#### MetaSerializableFlags

**Line:** 600717

**Values:**

- `None` = 0
- `ImplicitMembers` = 1
- `AutomaticConstructorDetection` = 2

---

#### MetaSerializationFlags

**Line:** 529385

**Values:**

- `IncludeAll` = 0
- `SendOverNetwork` = 1
- `ComputeChecksum` = 2
- `Persisted` = 4
- `EntityEventLog` = 16

---

#### MetadataPropertyHandling

**Line:** 1032308

**Values:**

- `Default` = 0
- `ReadAhead` = 1
- `Ignore` = 2

---

#### MetadataType

**Line:** 1327147

**Values:**

- `Locale` = 1
- `SharedTableData` = 2
- `StringTable` = 4
- `AssetTable` = 8
- `StringTableEntry` = 16
- `AssetTableEntry` = 32
- `SharedStringTableEntry` = 64
- `SharedAssetTableEntry` = 128
- `LocalizationSettings` = 256
- `AllTables` = 12
- `AllTableEntries` = 48
- `AllSharedTableEntries` = 192
- `All` = 511

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

- `MemberAccessMask` = 7
- `PrivateScope` = 0
- `Private` = 1
- `FamANDAssem` = 2
- `Assembly` = 3
- `Family` = 4
- `FamORAssem` = 5
- `Public` = 6
- `Static` = 16
- `Final` = 32
- `Virtual` = 64
- `HideBySig` = 128
- `CheckAccessOnOverride` = 512
- `VtableLayoutMask` = 256
- `ReuseSlot` = 0
- `NewSlot` = 256
- `Abstract` = 1024
- `SpecialName` = 2048
- `PinvokeImpl` = 8192
- `UnmanagedExport` = 8
- `RTSpecialName` = 4096
- `HasSecurity` = 16384
- `RequireSecObject` = 32768
- `ReservedMask` = 53248

---

#### MethodImplAttributes

**Line:** 265898

**Values:**

- `CodeTypeMask` = 3
- `IL` = 0
- `Native` = 1
- `OPTIL` = 2
- `Runtime` = 3
- `ManagedMask` = 4
- `Unmanaged` = 4
- `Managed` = 0
- `ForwardRef` = 16
- `PreserveSig` = 128
- `InternalCall` = 4096
- `Synchronized` = 32
- `NoInlining` = 8
- `AggressiveInlining` = 256
- `NoOptimization` = 64
- `MaxMethodImplVal` = 65535
- `SecurityMitigations` = 1024

---

#### MethodImplOptions

**Line:** 253494

**Values:**

- `Unmanaged` = 4
- `ForwardRef` = 16
- `PreserveSig` = 128
- `InternalCall` = 4096
- `Synchronized` = 32
- `NoInlining` = 8
- `AggressiveInlining` = 256
- `NoOptimization` = 64
- `SecurityMitigations` = 1024

---

#### MidpointRounding

**Line:** 26518

**Values:**

- `ToEven` = 0
- `AwayFromZero` = 1

---

#### MissingEntryAction

**Line:** 1317330

**Values:**

- `Nothing` = 0
- `AddEntriesToSharedData` = 1
- `RemoveEntriesFromTable` = 2

---

#### MissingSchemaAction

**Line:** 1087079

**Values:**

- `Add` = 1
- `Ignore` = 2
- `Error` = 3
- `AddWithKey` = 4

---

#### MissingTranslationBehavior

**Line:** 1318491

**Values:**

- `ShowMissingTranslationMessage` = 1
- `PrintWarning` = 2

---

#### MixedLightingMode

**Line:** 875282

**Values:**

- `IndirectOnly` = 0
- `Shadowmask` = 2
- `Subtractive` = 1

---

#### MixedLightingSetup

**Line:** 916918

**Values:**

- `None` = 0
- `ShadowMask` = 1
- `Subtractive` = 2

---

#### ModelActionExecuteFlags

**Line:** 601128

**Values:**

- `None` = 0
- `LeaderSynchronized` = 1
- `FollowerSynchronized` = 4
- `FollowerUnsynchronized` = 8

---

#### MonoSslPolicyErrors

**Line:** 1448938

**Values:**

- `None` = 0
- `RemoteCertificateNotAvailable` = 1
- `RemoteCertificateNameMismatch` = 2
- `RemoteCertificateChainErrors` = 4

---

#### MotionBlurMode

**Line:** 909487

**Values:**

- `CameraOnly` = 0
- `CameraAndObjects` = 1

---

#### MotionBlurQuality

**Line:** 909496

**Values:**

- `Low` = 0
- `Medium` = 1
- `High` = 2

---

#### MotionVectorGenerationMode

**Line:** 875668

**Values:**

- `Camera` = 0
- `Object` = 1
- `ForceNoMotion` = 2

---

#### MouseButton

**Line:** 641467

**Values:**

- `LeftMouse` = 0
- `RightMouse` = 1
- `MiddleMouse` = 2

---

#### MoveDirection

**Line:** 1360899

**Values:**

- `Left` = 0
- `Up` = 1
- `Right` = 2
- `Down` = 3
- `None` = 4

---

#### MsaaQuality

**Line:** 900499

**Values:**

- `Disabled` = 1
- `_2x` = 2
- `_4x` = 4
- `_8x` = 8

---

#### MultiplayerEntityClientPhase

**Line:** 551869

**Values:**

- `NoSession` = 0
- `NoEntity` = 1
- `LoadingEntity` = 2
- `EntityActive` = 3

---

#### MultiplayerEntityDirectConnectionProtocol

**Line:** 552867

---

#### MultiplierFormatType

**Line:** 736249

**Values:**

- `NoMultiplier` = 0
- `XMultiplier` = 1
- `MultiplierPercentage` = 2
- `Percentage` = 3
- `NegativePercentage` = 4

---

#### MusicType

**Line:** 705612

**Values:**

- `None` = 0
- `Battle` = 1
- `Menu` = 2

---

#### NPOTSupport

**Line:** 875449

**Values:**

- `None` = 0
- `Restricted` = 1
- `Full` = 2

---

#### NamespaceHandling

**Line:** 741442

**Values:**

- `Default` = 0
- `OmitDuplicates` = 1

---

#### NamespaceList

**Line:** 760478

---

#### NativeArrayOptions

**Line:** 838065

**Values:**

- `UninitializedMemory` = 0
- `ClearMemory` = 1

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

- `TryToPreserveSequence` = 0
- `KillWholeSequence` = 1

---

#### NetworkInterfaceComponent

**Line:** 798913

**Values:**

- `IPv4` = 0
- `IPv6` = 1

---

#### NetworkReachability

**Line:** 870386

**Values:**

- `NotReachable` = 0
- `ReachableViaCarrierDataNetwork` = 1
- `ReachableViaLocalAreaNetwork` = 2

---

#### NeutralRangeReductionMode

**Line:** 909721

**Values:**

- `Reinhard` = 1
- `BT2390` = 2

---

#### NewLineHandling

**Line:** 741451

**Values:**

- `Replace` = 0
- `Entitize` = 1
- `None` = 2

---

#### NftMetadataCorePropertyId

**Line:** 581833

**Values:**

- `Name` = 0
- `Description` = 1
- `ImageUrl` = 2

---

#### NftOwnerAddress

**Line:** 582026

---

#### NftPropertyType

**Line:** 581843

**Values:**

- `Enum` = 0
- `Text` = 1
- `Boolean` = 2
- `Number` = 3

---

#### NormalizationForm

**Line:** 215056

**Values:**

- `FormC` = 1
- `FormD` = 2
- `FormKC` = 5
- `FormKD` = 6

---

#### NotificationPresentation

**Line:** 1591167

**Values:**

- `Alert` = 1
- `Badge` = 2
- `Sound` = 4
- `Vibrate` = 8

---

#### NotificationRepeatInterval

**Line:** 1591350

**Values:**

- `OneTime` = 0
- `Daily` = 1

---

#### NotificationSettingsSection

**Line:** 1591178

**Values:**

- `Application` = 0
- `Category` = 1

---

#### NotificationStatus

**Line:** 1552614

**Values:**

- `Unknown` = 0
- `Scheduled` = 1
- `Delivered` = 2

---

#### NotificationStyle

**Line:** 1552246

**Values:**

- `None` = 0
- `BigPictureStyle` = 1
- `BigTextStyle` = 2

---

#### NotificationsPermissionStatus

**Line:** 1591448

**Values:**

- `RequestPending` = 0
- `Granted` = 1
- `Denied` = 2

---

#### NotifyCollectionChangedAction

**Line:** 785809

**Values:**

- `Add` = 0
- `Remove` = 1
- `Replace` = 2
- `Move` = 3
- `Reset` = 4

---

#### NtlmFlags

**Line:** 1448368

**Values:**

- `NegotiateUnicode` = 1
- `NegotiateOem` = 2
- `RequestTarget` = 4
- `NegotiateNtlm` = 512
- `NegotiateDomainSupplied` = 4096
- `NegotiateWorkstationSupplied` = 8192
- `NegotiateAlwaysSign` = 32768
- `NegotiateNtlm2Key` = 524288
- `Negotiate128` = 536870912

---

#### NullValueHandling

**Line:** 1032327

**Values:**

- `Include` = 0
- `Ignore` = 1

---

#### NumberStyles

**Line:** 272177

**Values:**

- `None` = 0
- `AllowLeadingWhite` = 1
- `AllowTrailingWhite` = 2
- `AllowLeadingSign` = 4
- `AllowTrailingSign` = 8
- `AllowParentheses` = 16
- `AllowDecimalPoint` = 32
- `AllowThousands` = 64
- `AllowExponent` = 128
- `AllowCurrencySymbol` = 256
- `AllowHexSpecifier` = 512
- `Integer` = 7
- `HexNumber` = 515
- `Number` = 111
- `Float` = 167
- `Currency` = 383
- `Any` = 511

---

#### OTL_FeatureTag

**Line:** 1346793

**Values:**

- `kern` = 1801810542
- `liga` = 1818847073
- `mark` = 1835102827
- `mkmk` = 1835756907

---

#### ObjectCreationHandling

**Line:** 1032336

**Values:**

- `Auto` = 0
- `Reuse` = 1
- `Replace` = 2

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

- `None` = 0
- `TestAll` = 1
- `TestCulled` = 2

---

#### OidGroup

**Line:** 778803

**Values:**

- `All` = 0
- `HashAlgorithm` = 1
- `EncryptionAlgorithm` = 2
- `PublicKeyAlgorithm` = 3
- `SignatureAlgorithm` = 4
- `Attribute` = 5
- `ExtensionOrAttribute` = 6
- `EnhancedKeyUsage` = 7
- `Policy` = 8
- `Template` = 9
- `KeyDerivationFunction` = 10

---

#### OidcTokenFormat

**Line:** 1372998

**Values:**

- `Standard` = 0
- `Full` = 1
- `FullWithLicences` = 2

---

#### OpaqueSortMode

**Line:** 891693

**Values:**

- `Default` = 0
- `FrontToBack` = 1
- `NoDistanceSort` = 2

---

#### OpenFlags

**Line:** 778903

**Values:**

- `ReadOnly` = 0
- `ReadWrite` = 1
- `MaxAllowed` = 2
- `OpenExistingOnly` = 4
- `IncludeArchived` = 8

---

#### OpenGLESVersion

**Line:** 892497

**Values:**

- `None` = 0
- `OpenGLES20` = 1
- `OpenGLES30` = 2
- `OpenGLES31` = 3
- `OpenGLES31AEP` = 4
- `OpenGLES32` = 5

---

#### OperationStatus

**Line:** 466068

**Values:**

- `Done` = 0
- `DestinationTooSmall` = 1
- `NeedMoreData` = 2
- `InvalidData` = 3

---

#### Operator

**Line:** 770249

---

#### OptimizeFor

**Line:** 1329674

**Values:**

- `Default` = 0
- `Performance` = 1
- `Size` = 2
- `FastCompilation` = 3
- `Balanced` = 4

---

#### OrientType

**Line:** 1429709

**Values:**

- `None` = 0
- `ToPath` = 1
- `LookAtTransform` = 2
- `LookAtPosition` = 3

---

#### Overflow

**Line:** 659842

**Values:**

- `Visible` = 0
- `Hidden` = 1

---

#### OverflowClipBox

**Line:** 659862

**Values:**

- `PaddingBox` = 0
- `ContentBox` = 1

---

#### PackingRules

**Line:** 821445

**Values:**

- `Exact` = 0
- `Aggressive` = 1

---

#### PaddingMode

**Line:** 217955

**Values:**

- `None` = 1
- `PKCS7` = 2
- `Zeros` = 3
- `ANSIX923` = 4
- `ISO10126` = 5

---

#### PanelScaleMode

**Line:** 640195

**Values:**

- `ConstantPixelSize` = 0
- `ConstantPhysicalSize` = 1
- `ScaleWithScreenSize` = 2

---

#### PanelScreenMatchMode

**Line:** 640205

**Values:**

- `MatchWidthOrHeight` = 0
- `Shrink` = 1
- `Expand` = 2

---

#### ParallelEtwProvider

**Line:** 191301

---

#### ParameterAttributes

**Line:** 266070

**Values:**

- `None` = 0
- `In` = 1
- `Out` = 2
- `Lcid` = 4
- `Retval` = 8
- `Optional` = 16
- `HasDefault` = 4096
- `HasFieldMarshal` = 8192
- `Reserved3` = 16384
- `Reserved4` = 32768
- `ReservedMask` = 61440

---

#### ParseError

**Line:** 1200788

**Values:**

- `None` = 0
- `Syntax` = 1
- `Overflow` = 2
- `Underflow` = 3

---

#### Parser

**Line:** 1322707

---

#### ParticleSystemAnimationMode

**Line:** 1577958

**Values:**

- `Grid` = 0
- `Sprites` = 1

---

#### ParticleSystemCurveMode

**Line:** 1577935

**Values:**

- `Constant` = 0
- `Curve` = 1
- `TwoCurves` = 2
- `TwoConstants` = 3

---

#### ParticleSystemGradientMode

**Line:** 1577946

**Values:**

- `Color` = 0
- `Gradient` = 1
- `TwoColors` = 2
- `TwoGradients` = 3
- `RandomColor` = 4

---

#### ParticleSystemRenderMode

**Line:** 1577922

**Values:**

- `Billboard` = 0
- `Stretch` = 1
- `HorizontalBillboard` = 2
- `VerticalBillboard` = 3
- `Mesh` = 4
- `None` = 5

---

#### ParticleSystemScalingMode

**Line:** 1577986

**Values:**

- `Hierarchy` = 0
- `Local` = 1
- `Shape` = 2

---

#### ParticleSystemSimulationSpace

**Line:** 1577967

**Values:**

- `Local` = 0
- `World` = 1
- `Custom` = 2

---

#### ParticleSystemStopBehavior

**Line:** 1577977

**Values:**

- `StopEmittingAndClear` = 0
- `StopEmitting` = 1

---

#### PathMode

**Line:** 1425572

**Values:**

- `Ignore` = 0
- `Full3D` = 1
- `TopDown2D` = 2
- `Sidescroller2D` = 3

---

#### PathType

**Line:** 1425583

**Values:**

- `Linear` = 0
- `CatmullRom` = 1
- `CubicBezier` = 2

---

#### PayoutType

**Line:** 1530747

**Values:**

- `Other` = 0
- `Currency` = 1
- `Item` = 2
- `Resource` = 3

---

#### PenEventType

**Line:** 1580382

**Values:**

- `NoContact` = 0
- `PenDown` = 1
- `PenUp` = 2

---

#### PenStatus

**Line:** 1580370

**Values:**

- `None` = 0
- `Contact` = 1
- `Barrel` = 2
- `Inverted` = 4
- `Eraser` = 8

---

#### PendingDynamicPurchaseContentStatus

**Line:** 583787

**Values:**

- `RequestedByClient` = 0
- `ConfirmedByServer` = 1

---

#### PendingPurchaseAnalyticsContextStatus

**Line:** 585885

**Values:**

- `RequestedByClient` = 0
- `ConfirmedByServer` = 1

---

#### PerObjectData

**Line:** 895792

**Values:**

- `None` = 0
- `LightProbe` = 1
- `ReflectionProbes` = 2
- `LightProbeProxyVolume` = 4
- `Lightmaps` = 8
- `LightData` = 16
- `MotionVectors` = 32
- `LightIndices` = 64
- `ReflectionProbeData` = 128
- `OcclusionProbe` = 256
- `OcclusionProbeProxyVolume` = 512
- `ShadowMask` = 1024

---

#### PeriodUnits

**Line:** 1146636

**Values:**

- `None` = 0
- `Years` = 1
- `Months` = 2
- `Weeks` = 4
- `Days` = 8
- `AllDateUnits` = 15
- `YearMonthDay` = 11
- `Hours` = 16
- `Minutes` = 32
- `Seconds` = 64
- `Milliseconds` = 128
- `Ticks` = 256
- `Nanoseconds` = 512
- `HourMinuteSecond` = 112
- `AllTimeUnits` = 1008
- `DateAndTime` = 1019
- `AllUnits` = 1023

---

#### PermissionState

**Line:** 217371

**Values:**

- `None` = 0
- `Unrestricted` = 1

---

#### PermissionStatus

**Line:** 1553459

**Values:**

- `NotRequested` = 0
- `Allowed` = 1
- `Denied` = 2
- `DeniedDontAskAgain` = 3
- `RequestPending` = 4
- `NotificationsBlockedForApp` = 5

---

#### PersistentListenerMode

**Line:** 886859

**Values:**

- `EventDefined` = 0
- `Void` = 1
- `Object` = 2
- `Int` = 3
- `Float` = 4
- `String` = 5
- `Bool` = 6

---

#### PersonNameFormatterStyle

**Line:** 1590241

**Values:**

- `Default` = 0
- `Short` = 1
- `Medium` = 2
- `Long` = 3
- `Abbreviated` = 4

---

#### PickingMode

**Line:** 670857

**Values:**

- `Position` = 0
- `Ignore` = 1

---

#### PinAlignment

**Line:** 1442549

**Values:**

- `TopLeft` = 0
- `TopRight` = 1
- `BottomLeft` = 2
- `BottomRight` = 3
- `CenterLeft` = 4
- `CenterRight` = 5
- `TopCenter` = 6
- `BottomCenter` = 7

---

#### PixelPerfectCamera

**Line:** 1363745

---

#### PixelValidationChannels

**Line:** 1594401

**Values:**

- `RGB` = 0
- `R` = 1
- `G` = 2
- `B` = 3
- `A` = 4

---

#### PlatformID

**Line:** 176590

**Values:**

- `Win32S` = 0
- `Win32Windows` = 1
- `Win32NT` = 2
- `WinCE` = 3
- `Unix` = 4
- `Xbox` = 5
- `MacOSX` = 6

---

#### PlayerDashboardActionAttribute

**Line:** 601174

---

#### PlayerDebugIncidentUploadMode

**Line:** 542603

**Values:**

- `Normal` = 0
- `SilentlyOmitUploads` = 1
- `RejectIncidents` = 2

---

#### PlayerDeletionSource

**Line:** 538169

**Values:**

- `Admin` = 0
- `User` = 1
- `System` = 2
- `Unknown` = 3

---

#### PlayerDeletionStatus

**Line:** 538181

**Values:**

- `None` = 0
- `DeletedByUnknownLegacy` = 2
- `ScheduledByAdmin` = 1
- `DeletedByAdmin` = 6
- `ScheduledByUser` = 5
- `DeletedByUser` = 14
- `ScheduledBySystem` = 9
- `DeletedBySystem` = 22
- `ScheduledByUnknown` = 25
- `DeletedByUnknown` = 30

---

#### PlayerEventExperimentAssignment

**Line:** 537035

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

- `None` = 0
- `Male` = 1
- `Female` = 2

---

#### PlayerHandleJoinResponse

**Line:** 1063742

---

#### PlayerLoopTiming

**Line:** 1099296

**Values:**

- `Initialization` = 0
- `LastInitialization` = 1
- `EarlyUpdate` = 2
- `LastEarlyUpdate` = 3
- `FixedUpdate` = 4
- `LastFixedUpdate` = 5
- `PreUpdate` = 6
- `LastPreUpdate` = 7
- `Update` = 8
- `LastUpdate` = 9
- `PreLateUpdate` = 10
- `LastPreLateUpdate` = 11
- `PostLateUpdate` = 12
- `LastPostLateUpdate` = 13
- `TimeUpdate` = 14
- `LastTimeUpdate` = 15

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

- `Mouse` = 0
- `Touch` = 1
- `Pen` = 2

---

#### PolicyEnforcement

**Line:** 778511

**Values:**

- `Never` = 0
- `WhenSupported` = 1
- `Always` = 2

---

#### PolyFillType

**Line:** 1361492

**Values:**

- `pftEvenOdd` = 0
- `pftNonZero` = 1
- `pftPositive` = 2
- `pftNegative` = 3

---

#### PolyType

**Line:** 1361482

**Values:**

- `ptSubject` = 0
- `ptClip` = 1

---

#### Position

**Line:** 659833

**Values:**

- `Relative` = 0
- `Absolute` = 1

---

#### PreloadAssetTableMetadata

**Line:** 1327554

---

#### PreloadBehavior

**Line:** 1319410

**Values:**

- `NoPreloading` = 0
- `PreloadSelectedLocale` = 1
- `PreloadSelectedLocaleAndFallbacks` = 2
- `PreloadAllLocales` = 3

---

#### PreserveReferencesHandling

**Line:** 1032347

**Values:**

- `None` = 0
- `Objects` = 1
- `Arrays` = 2
- `All` = 3

---

#### PrettyPrintFlag

**Line:** 499149

**Values:**

- `None` = 0
- `SizeOnly` = 1
- `Shorten` = 4
- `Hide` = 8
- `HideInDiff` = 16

---

#### Priority

**Line:** 837630

**Values:**

- `PriorityLow` = 0
- `PriorityHigh` = 1

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

- `MemoryBudgetLow` = 128
- `MemoryBudgetMedium` = 256
- `MemoryBudgetHigh` = 512

---

#### ProbeVolumeSHBands

**Line:** 818973

**Values:**

- `SphericalHarmonicsL1` = 1
- `SphericalHarmonicsL2` = 2

---

#### ProbeVolumeTextureMemoryBudget

**Line:** 818951

**Values:**

- `MemoryBudgetLow` = 512
- `MemoryBudgetMedium` = 1024
- `MemoryBudgetHigh` = 2048

---

#### ProcessWindowStyle

**Line:** 778316

**Values:**

- `Hidden` = 1
- `Maximized` = 3
- `Minimized` = 2
- `Normal` = 0

---

#### ProcessingState

**Line:** 837792

**Values:**

- `Unknown` = 0
- `InQueue` = 1
- `Reading` = 2
- `Completed` = 3
- `Failed` = 4
- `Canceled` = 5

---

#### ProcessorArchitecture

**Line:** 266196

**Values:**

- `None` = 0
- `MSIL` = 1
- `X86` = 2
- `IA64` = 3
- `Amd64` = 4
- `Arm` = 5

---

#### ProductCatalogPayout

**Line:** 1406922

---

#### ProductType

**Line:** 1531092

**Values:**

- `Consumable` = 0
- `NonConsumable` = 1
- `Subscription` = 2

---

#### ProfilerCategoryColor

**Line:** 837048

**Values:**

- `Render` = 0
- `Scripts` = 1
- `BurstJobs` = 2
- `Other` = 3
- `Physics` = 4
- `Animation` = 5
- `Audio` = 6
- `AudioJob` = 7
- `AudioUpdateJob` = 8
- `Lighting` = 9
- `GC` = 10
- `VSync` = 11
- `Memory` = 12
- `Internal` = 13
- `UI` = 14
- `Build` = 15
- `Input` = 16

---

#### ProfilerCounterOptions

**Line:** 837126

**Values:**

- `None` = 0
- `FlushOnEndOfFrame` = 2
- `ResetToZeroOnFlush` = 4

---

#### ProfilerGraphControl

**Line:** 1444692

---

#### ProfilerMarkerDataType

**Line:** 837356

**Values:**

- `InstanceId` = 1
- `Int32` = 2
- `UInt32` = 3
- `Int64` = 4
- `UInt64` = 5
- `Float` = 6
- `Double` = 7
- `String16` = 9
- `Blob8` = 11
- `GfxResourceId` = 12

---

#### ProfilerMarkerDataUnit

**Line:** 837112

**Values:**

- `Undefined` = 0
- `TimeNanoseconds` = 1
- `Bytes` = 2
- `Count` = 3
- `Percent` = 4
- `FrequencyHz` = 5

---

#### ProfilerRecorderOptions

**Line:** 837137

**Values:**

- `None` = 0
- `StartImmediately` = 1
- `KeepAliveDuringDomainReload` = 2
- `CollectOnlyOnCurrentThread` = 4
- `WrapAroundWhenCapacityReached` = 8
- `SumAllSamplesInFrame` = 16
- `GpuRecorder` = 64
- `Default` = 24

---

#### PropagationPhase

**Line:** 635056

**Values:**

- `None` = 0
- `TrickleDown` = 1
- `BubbleUp` = 3
- `AtTarget` = 2
- `DefaultAction` = 4
- `DefaultActionAtTarget` = 5

---

#### PropertyAttributes

**Line:** 266210

**Values:**

- `None` = 0
- `SpecialName` = 512
- `RTSpecialName` = 1024
- `HasDefault` = 4096
- `Reserved2` = 8192
- `Reserved3` = 16384
- `Reserved4` = 32768
- `ReservedMask` = 62464

---

#### PropertyPathPartKind

**Line:** 1461820

**Values:**

- `Name` = 0
- `Index` = 1
- `Key` = 2

---

#### ProtocolStatus

**Line:** 551655

**Values:**

- `Pending` = 0
- `InvalidGameMagic` = 1
- `WireProtocolVersionMismatch` = 2
- `ClusterRunning` = 3
- `ClusterStarting` = 4
- `ClusterShuttingDown` = 5
- `InMaintenance` = 6

---

#### ProtocolType

**Line:** 800402

**Values:**

- `IP` = 0
- `IPv6HopByHopOptions` = 0
- `Icmp` = 1
- `Igmp` = 2
- `Ggp` = 3
- `IPv4` = 4
- `Tcp` = 6
- `Pup` = 12
- `Udp` = 17
- `Idp` = 22
- `IPv6` = 41
- `IPv6RoutingHeader` = 43
- `IPv6FragmentHeader` = 44
- `IPSecEncapsulatingSecurityPayload` = 50
- `IPSecAuthenticationHeader` = 51
- `IcmpV6` = 58
- `IPv6NoNextHeader` = 59
- `IPv6DestinationOptions` = 60
- `ND` = 77
- `Raw` = 255
- `Unspecified` = 0
- `Ipx` = 1000
- `Spx` = 1256
- `SpxII` = 1257

---

#### ProviderBehaviourFlags

**Line:** 1437231

**Values:**

- `None` = 0
- `CanProvideWithFailedDependencies` = 1

---

#### PublishedAppPlatform

**Line:** 1564895

**Values:**

- `Android` = 0
- `Ios` = 1

---

#### PurchaseFailureReason

**Line:** 1531172

**Values:**

- `PurchasingUnavailable` = 0
- `ExistingPurchasePending` = 1
- `ProductUnavailable` = 2
- `SignatureInvalid` = 3
- `UserCancelled` = 4
- `PaymentDeclined` = 5
- `DuplicateTransaction` = 6
- `Unknown` = 7

---

#### PurchaseProcessingResult

**Line:** 1531187

**Values:**

- `Complete` = 0
- `Pending` = 1

---

#### QueryLastRespondedNotificationState

**Line:** 1591480

**Values:**

- `Pending` = 0
- `NoRespondedNotification` = 1
- `HaveRespondedNotification` = 2

---

#### QueryTriggerInteraction

**Line:** 1577063

**Values:**

- `UseGlobal` = 0
- `Ignore` = 1
- `Collide` = 2

---

#### RSASignaturePaddingMode

**Line:** 217846

**Values:**

- `Pkcs1` = 0
- `Pss` = 1

---

#### RTClearFlags

**Line:** 892460

**Values:**

- `None` = 0
- `Color` = 1
- `Depth` = 2
- `Stencil` = 4
- `All` = 7
- `DepthStencil` = 6
- `ColorDepth` = 3
- `ColorStencil` = 5

---

#### RayTracingAccelerationStructureBuildFlags

**Line:** 891619

**Values:**

- `None` = 0
- `PreferFastTrace` = 1
- `PreferFastBuild` = 2
- `MinimizeMemory` = 4

---

#### ReactionEntryUiView

**Line:** 708048

---

#### ReadState

**Line:** 741648

**Values:**

- `Initial` = 0
- `Interactive` = 1
- `Error` = 2
- `EndOfFile` = 3
- `Closed` = 4

---

#### ReadStatus

**Line:** 837617

**Values:**

- `Complete` = 0
- `InProgress` = 1
- `Failed` = 2
- `Truncated` = 4
- `Canceled` = 5

---

#### RealUserStatus

**Line:** 1590253

**Values:**

- `Unsupported` = 0
- `Unknown` = 1
- `LikelyReal` = 2

---

#### RectTransform

**Line:** 885982

---

#### RedDotReason

**Line:** 695439

**Values:**

- `IdleRewardClaimable` = 0
- `CanStartForgeUpgrade` = 10
- `ForgeUpgradeClaimable` = 11
- `ArenaRewardsTutorial` = 20
- `ArenaRewardsClaimable` = 21
- `CanUseArenaTickets` = 22
- `CanUseDungeonKeys` = 30
- `CanSummonSkills` = 40
- `CanUpgradeSkills` = 41
- `QuickEquipSkillsOptionAvailable` = 42
- `CanSummonMount` = 50
- `CanStartHatchingEggs` = 60
- `HatchedEggsClaimable` = 61
- `QuickEquipPetsOptionAvailable` = 62
- `TechNodeClaimable` = 70
- `GuildJoinRequests` = 80
- `WarEndRewardsClaimable` = 81
- `WarPassRewardsClaimable` = 82
- `CanUseWarTickets` = 83
- `MainProgressPassRewardsClaimable` = 90
- `SteppingStonesFreeResourcePack` = 100

---

#### ReferenceLoopHandling

**Line:** 1032358

**Values:**

- `Error` = 0
- `Ignore` = 1
- `Serialize` = 2

---

#### ReflectionProbe

**Line:** 871445

---

#### ReflectionProbeRefreshMode

**Line:** 892299

**Values:**

- `OnAwake` = 0
- `EveryFrame` = 1
- `ViaScripting` = 2

---

#### ReflectionProbeSortingCriteria

**Line:** 895842

**Values:**

- `None` = 0
- `Importance` = 1
- `Size` = 2
- `ImportanceThenSize` = 3

---

#### RefreshProperties

**Line:** 784773

**Values:**

- `None` = 0
- `All` = 1
- `Repaint` = 2

---

#### RegexOptions

**Line:** 776856

**Values:**

- `None` = 0
- `IgnoreCase` = 1
- `Multiline` = 2
- `ExplicitCapture` = 4
- `Compiled` = 8
- `Singleline` = 16
- `IgnorePatternWhitespace` = 32
- `RightToLeft` = 64
- `ECMAScript` = 256
- `CultureInvariant` = 512

---

#### ReloadAttribute

**Line:** 810965

---

#### RenderBufferLoadAction

**Line:** 891703

**Values:**

- `Load` = 0
- `Clear` = 1
- `DontCare` = 2

---

#### RenderBufferStoreAction

**Line:** 891713

**Values:**

- `Store` = 0
- `Resolve` = 1
- `StoreAndResolve` = 2
- `DontCare` = 3

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

- `ScreenSpaceOverlay` = 0
- `ScreenSpaceCamera` = 1
- `WorldSpace` = 2

---

#### RenderObjects

**Line:** 912479

---

#### RenderPassEvent

**Line:** 911760

**Values:**

- `BeforeRendering` = 0
- `BeforeRenderingShadows` = 50
- `AfterRenderingShadows` = 100
- `BeforeRenderingPrePasses` = 150
- `AfterRenderingPrePasses` = 200
- `BeforeRenderingGbuffer` = 210
- `AfterRenderingGbuffer` = 220
- `BeforeRenderingDeferredLights` = 230
- `AfterRenderingDeferredLights` = 240
- `BeforeRenderingOpaques` = 250
- `AfterRenderingOpaques` = 300
- `BeforeRenderingSkybox` = 350
- `AfterRenderingSkybox` = 400
- `BeforeRenderingTransparents` = 450
- `AfterRenderingTransparents` = 500
- `BeforeRenderingPostProcessing` = 550
- `AfterRenderingPostProcessing` = 600
- `AfterRendering` = 1000

---

#### RenderPathCompatibility

**Line:** 916205

**Values:**

- `Forward` = 1
- `Deferred` = 2
- `ForwardPlus` = 4
- `All` = 7

---

#### RenderQueueType

**Line:** 912470

**Values:**

- `Opaque` = 0
- `Transparent` = 1

---

#### RenderStateMask

**Line:** 896438

**Values:**

- `Nothing` = 0
- `Blend` = 1
- `Raster` = 2
- `Depth` = 4
- `Stencil` = 8
- `Everything` = 15

---

#### RenderTargetFlags

**Line:** 892243

**Values:**

- `None` = 0
- `ReadOnlyDepth` = 1
- `ReadOnlyStencil` = 2
- `ReadOnlyDepthStencil` = 3

---

#### RenderTextureCreationFlags

**Line:** 875601

**Values:**

- `MipMap` = 1
- `AutoGenerateMips` = 2
- `SRGB` = 4
- `EyeTexture` = 8
- `EnableRandomWrite` = 16
- `CreatedFromScript` = 32
- `AllowVerticalFlip` = 128
- `NoResolvedColorSurface` = 256
- `DynamicallyScalable` = 1024
- `BindMS` = 2048
- `DynamicallyScalableExplicit` = 131072

---

#### RenderTextureFormat

**Line:** 875554

**Values:**

- `ARGB32` = 0
- `Depth` = 1
- `ARGBHalf` = 2
- `Shadowmap` = 3
- `RGB565` = 4
- `ARGB4444` = 5
- `ARGB1555` = 6
- `Default` = 7
- `ARGB2101010` = 8
- `DefaultHDR` = 9
- `ARGB64` = 10
- `ARGBFloat` = 11
- `RGFloat` = 12
- `RGHalf` = 13
- `RFloat` = 14
- `RHalf` = 15
- `R8` = 16
- `ARGBInt` = 17
- `RGInt` = 18
- `RInt` = 19
- `BGRA32` = 20
- `RGB111110Float` = 22
- `RG32` = 23
- `RGBAUShort` = 24
- `RG16` = 25
- `BGRA10101010_XR` = 26
- `BGR101010_XR` = 27
- `R16` = 28

---

#### RenderTextureMemoryless

**Line:** 875630

**Values:**

- `None` = 0
- `Color` = 1
- `Depth` = 2
- `MSAA` = 4

---

#### RenderTextureReadWrite

**Line:** 875619

**Values:**

- `Default` = 0
- `Linear` = 1
- `sRGB` = 2

---

#### RenderTextureSubElement

**Line:** 892475

**Values:**

- `Color` = 0
- `Depth` = 1
- `Stencil` = 2
- `Default` = 3

---

#### RendererListStatus

**Line:** 896514

**Values:**

- `kRendererListEmpty` = 0
- `kRendererListPopulated` = 1

---

#### RendererOverrideOption

**Line:** 914932

**Values:**

- `Custom` = 0
- `UsePipelineSettings` = 1

---

#### RendererType

**Line:** 900541

**Values:**

- `Custom` = 0
- `UniversalRenderer` = 1
- `_2DRenderer` = 2

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

- `Forward` = 0
- `ForwardPlus` = 2
- `Deferred` = 1

---

#### RenderingPath

**Line:** 875176

**Values:**

- `VertexLit` = 0
- `Forward` = 1
- `DeferredLighting` = 2
- `DeferredShading` = 3

---

#### Repeat

**Line:** 659989

**Values:**

- `NoRepeat` = 0
- `Space` = 1
- `Round` = 2
- `Repeat` = 3

---

#### RequestError

**Line:** 1495693

---

#### RequestParameterType

**Line:** 1495180

**Values:**

- `Path` = 0
- `Query` = 1
- `UserDefinedQueries` = 2

---

#### Required

**Line:** 1032368

**Values:**

- `Default` = 0
- `AllowNull` = 1
- `Always` = 2
- `DisallowNull` = 3

---

#### ResourceLocation

**Line:** 266359

**Values:**

- `ContainedInAnotherAssembly` = 2
- `ContainedInManifestFile` = 4
- `Embedded` = 1

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

- `NotAllowed` = 0
- `RequireConsent` = 1
- `RequireLi` = 2

---

#### Result

**Line:** 1407725

**Values:**

- `True` = 0
- `False` = 1
- `Unsupported` = 2

---

#### RewindCallbackMode

**Line:** 1432790

**Values:**

- `FireIfPositionChanged` = 0
- `FireAlwaysWithRewind` = 1
- `FireAlways` = 2

---

#### RichTextTagParser

**Line:** 1346377

---

#### RigidbodyType2D

**Line:** 1578319

**Values:**

- `Dynamic` = 0
- `Kinematic` = 1
- `Static` = 2

---

#### RotateMode

**Line:** 1425593

**Values:**

- `Fast` = 0
- `FastBeyond360` = 1
- `WorldAxisAdd` = 2
- `LocalAxisAdd` = 3

---

#### Rule

**Line:** 1088466

**Values:**

- `None` = 0
- `Cascade` = 1
- `SetNull` = 2
- `SetDefault` = 3

---

#### RuntimeInitializeLoadType

**Line:** 883581

**Values:**

- `AfterSceneLoad` = 0
- `BeforeSceneLoad` = 1
- `AfterAssembliesLoaded` = 2
- `BeforeSplashScreen` = 3
- `SubsystemRegistration` = 4

---

#### RuntimePlatform

**Line:** 870418

**Values:**

- `OSXEditor` = 0
- `OSXPlayer` = 1
- `WindowsPlayer` = 2
- `OSXWebPlayer` = 3
- `OSXDashboardPlayer` = 4
- `WindowsWebPlayer` = 5
- `WindowsEditor` = 7
- `IPhonePlayer` = 8
- `XBOX360` = 10
- `PS3` = 9
- `Android` = 11
- `NaCl` = 12
- `FlashPlayer` = 15
- `LinuxPlayer` = 13
- `LinuxEditor` = 16
- `WebGLPlayer` = 17
- `MetroPlayerX86` = 18
- `WSAPlayerX86` = 18
- `MetroPlayerX64` = 19
- `WSAPlayerX64` = 19
- `MetroPlayerARM` = 20
- `WSAPlayerARM` = 20
- `WP8Player` = 21
- `BlackBerryPlayer` = 22
- `TizenPlayer` = 23
- `PSP2` = 24
- `PS4` = 25
- `PSM` = 26
- `XboxOne` = 27
- `SamsungTVPlayer` = 28
- `WiiU` = 30
- `tvOS` = 31
- `Switch` = 32
- `Lumin` = 33
- `Stadia` = 34
- `LinuxHeadlessSimulation` = 35
- `GameCoreXboxSeries` = 36
- `GameCoreXboxOne` = 37
- `PS5` = 38
- `EmbeddedLinuxArm64` = 39
- `EmbeddedLinuxArm32` = 40
- `EmbeddedLinuxX64` = 41
- `EmbeddedLinuxX86` = 42
- `LinuxServer` = 43
- `WindowsServer` = 44
- `OSXServer` = 45
- `QNXArm32` = 46
- `QNXArm64` = 47
- `QNXX64` = 48
- `QNXX86` = 49
- `VisionOS` = 50
- `Switch2` = 51
- `KeplerArm64` = 52
- `KeplerX64` = 53

---

#### SRMath

**Line:** 1504836

---

#### SRPLensFlareBlendMode

**Line:** 820820

**Values:**

- `Additive` = 0
- `Screen` = 1
- `Premultiply` = 2
- `Lerp` = 3

---

#### SRPLensFlareColorType

**Line:** 820858

**Values:**

- `Constant` = 0
- `RadialGradient` = 1
- `AngularGradient` = 2

---

#### SRPLensFlareDistribution

**Line:** 820832

**Values:**

- `Uniform` = 0
- `Curve` = 1
- `Random` = 2

---

#### SRPLensFlareType

**Line:** 820844

**Values:**

- `Image` = 0
- `Circle` = 1
- `Polygon` = 2
- `Ring` = 3
- `LensFlareDataSRP` = 4

---

#### SampleCount

**Line:** 913786

**Values:**

- `One` = 1
- `Two` = 2
- `Four` = 4

---

#### SaveOptions

**Line:** 1561042

**Values:**

- `None` = 0
- `DisableFormatting` = 1
- `OmitDuplicateNamespaces` = 2

---

#### ScaleMode

**Line:** 1451150

**Values:**

- `StretchToFill` = 0
- `ScaleAndCrop` = 1
- `ScaleToFit` = 2

---

#### SceneReleaseMode

**Line:** 1437342

**Values:**

- `ReleaseSceneWhenSceneUnloaded` = 0
- `OnlyReleaseSceneOnHandleRelease` = 1

---

#### ScheduleMode

**Line:** 836702

**Values:**

- `Run` = 0
- `Batched` = 1
- `Parallel` = 1
- `Single` = 2

---

#### SchemaNames

**Line:** 761945

---

#### SchemaSerializationMode

**Line:** 1088477

**Values:**

- `IncludeSchema` = 1
- `ExcludeSchema` = 2

---

#### ScrambleMode

**Line:** 1425604

**Values:**

- `None` = 0
- `All` = 1
- `Uppercase` = 2
- `Lowercase` = 3
- `Numerals` = 4
- `Custom` = 5

---

#### ScreenOrientation

**Line:** 875412

**Values:**

- `Portrait` = 1
- `PortraitUpsideDown` = 2
- `LandscapeLeft` = 3
- `LandscapeRight` = 4
- `AutoRotation` = 5
- `Unknown` = 0
- `Landscape` = 3

---

#### ScreenSpaceLensFlareResolution

**Line:** 909580

**Values:**

- `Half` = 2
- `Quarter` = 4
- `Eighth` = 8

---

#### ScriptableRenderPassInput

**Line:** 911748

**Values:**

- `None` = 0
- `Depth` = 1
- `Normal` = 2
- `Color` = 4
- `Motion` = 8

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

- `Vertical` = 0
- `Horizontal` = 1
- `VerticalAndHorizontal` = 2

---

#### Scrollbar

**Line:** 1355940

---

#### ScrollerVisibility

**Line:** 627310

**Values:**

- `Auto` = 0
- `AlwaysVisible` = 1
- `Hidden` = 2

---

#### SearchOption

**Line:** 469834

**Values:**

- `TopDirectoryOnly` = 0
- `AllDirectories` = 1

---

#### SearchType

**Line:** 892755

**Values:**

- `ProjectPath` = 0
- `BuiltinPath` = 1
- `BuiltinExtraPath` = 2
- `ShaderName` = 3

---

#### SecondaryStatType

**Line:** 1076395

**Values:**

- `CriticalChance` = 0
- `CriticalMulti` = 1
- `BlockChance` = 2
- `HealthRegen` = 3
- `LifeSteal` = 4
- `DoubleDamageChance` = 5
- `DamageMulti` = 6
- `MeleeDamageMulti` = 7
- `RangedDamageMulti` = 8
- `AttackSpeed` = 9
- `SkillDamageMulti` = 10
- `SkillCooldownMulti` = 11
- `HealthMulti` = 12

---

#### SectionAlignment

**Line:** 1565241

**Values:**

- `Undefined` = 0
- `Start` = 1
- `Center` = 2
- `End` = 3

---

#### SecurityAction

**Line:** 217383

**Values:**

- `Demand` = 2
- `Assert` = 3
- `Deny` = 4
- `PermitOnly` = 5
- `LinkDemand` = 6
- `InheritanceDemand` = 7
- `RequestMinimum` = 8
- `RequestOptional` = 9
- `RequestRefuse` = 10

---

#### SecurityProtocolType

**Line:** 791351

**Values:**

- `SystemDefault` = 0
- `Ssl3` = 48
- `Tls` = 192
- `Tls11` = 768
- `Tls12` = 3072
- `Tls13` = 12288

---

#### SeekOrigin

**Line:** 468159

**Values:**

- `Begin` = 0
- `Current` = 1
- `End` = 2

---

#### SelectMode

**Line:** 800434

**Values:**

- `SelectRead` = 0
- `SelectWrite` = 1
- `SelectError` = 2

---

#### Selectable

**Line:** 1356593

---

#### SelectionType

**Line:** 641257

**Values:**

- `None` = 0
- `Single` = 1
- `Multiple` = 2

---

#### SendEventOptions

**Line:** 891343

**Values:**

- `kAppendNone` = 0
- `kAppendBuildGuid` = 1
- `kAppendBuildTarget` = 2

---

#### SendMessageOptions

**Line:** 870409

**Values:**

- `RequireReceiver` = 0
- `DontRequireReceiver` = 1

---

#### SerializationFormat

**Line:** 1085006

**Values:**

- `Xml` = 0
- `Binary` = 1

---

#### ServiceLifetime

**Line:** 1543475

**Values:**

- `Singleton` = 0
- `Scoped` = 1
- `Transient` = 2

---

#### ServicesInitializationState

**Line:** 1589010

**Values:**

- `Uninitialized` = 0
- `Initializing` = 1
- `Initialized` = 2

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

- `Auto` = 0
- `PerVertex` = 1
- `Mixed` = 2
- `PerPixel` = 3

---

#### ShaderPathID

**Line:** 914105

**Values:**

- `Lit` = 0
- `SimpleLit` = 1
- `Unlit` = 2
- `TerrainLit` = 3
- `ParticlesLit` = 4
- `ParticlesSimpleLit` = 5
- `ParticlesUnlit` = 6
- `BakedLit` = 7
- `SpeedTree7` = 8
- `SpeedTree7Billboard` = 9
- `SpeedTree8` = 10
- `SpeedTree9` = 11
- `ComplexLit` = 12

---

#### ShaderPropertyFlags

**Line:** 898741

**Values:**

- `None` = 0
- `HideInInspector` = 1
- `PerRendererData` = 2
- `NoScaleOffset` = 4
- `Normal` = 8
- `HDR` = 16
- `Gamma` = 32
- `NonModifiableTextureData` = 64
- `MainTexture` = 128
- `MainColor` = 256

---

#### ShadowCascadesOption

**Line:** 905756

**Values:**

- `NoCascades` = 0
- `TwoCascades` = 1
- `FourCascades` = 2

---

#### ShadowCaster2D

**Line:** 1365044

---

#### ShadowCastingMode

**Line:** 891888

**Values:**

- `Off` = 0
- `On` = 1
- `TwoSided` = 2
- `ShadowsOnly` = 3

---

#### ShadowMesh2D

**Line:** 1365497

---

#### ShadowObjectsFilter

**Line:** 875301

**Values:**

- `AllObjects` = 0
- `DynamicOnly` = 1
- `StaticOnly` = 2

---

#### ShadowQuality

**Line:** 900429

**Values:**

- `Disabled` = 0
- `HardShadows` = 1
- `SoftShadows` = 2

---

#### ShadowResolution

**Line:** 900451

**Values:**

- `_256` = 256
- `_512` = 512
- `_1024` = 1024
- `_2048` = 2048
- `_4096` = 4096
- `_8192` = 8192

---

#### ShadowSamplingMode

**Line:** 892309

**Values:**

- `CompareDepths` = 0
- `RawDepth` = 1
- `None` = 2

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

- `Shadowmask` = 0
- `DistanceShadowmask` = 1

---

#### SheetsBaseServiceRequest

**Line:** 1383100

---

#### SinglePassStereoMode

**Line:** 892418

**Values:**

- `None` = 0
- `SideBySide` = 1
- `Instancing` = 2
- `Multiview` = 3

---

#### SingularUnityLogger

**Line:** 1571870

---

#### SliceType

**Line:** 660029

**Values:**

- `Sliced` = 0
- `Tiled` = 1

---

#### Slider

**Line:** 1356925

---

#### SliderDirection

**Line:** 613904

**Values:**

- `Horizontal` = 0
- `Vertical` = 1

---

#### SocialAuthenticateResult

**Line:** 543200

---

#### SocketAsyncOperation

**Line:** 800444

**Values:**

- `None` = 0
- `Accept` = 1
- `Connect` = 2
- `Disconnect` = 3
- `Receive` = 4
- `ReceiveFrom` = 5
- `ReceiveMessageFrom` = 6
- `Send` = 7
- `SendPackets` = 8
- `SendTo` = 9

---

#### SocketError

**Line:** 800461

**Values:**

- `Success` = 0
- `Interrupted` = 10004
- `AccessDenied` = 10013
- `Fault` = 10014
- `InvalidArgument` = 10022
- `TooManyOpenSockets` = 10024
- `WouldBlock` = 10035
- `InProgress` = 10036
- `AlreadyInProgress` = 10037
- `NotSocket` = 10038
- `DestinationAddressRequired` = 10039
- `MessageSize` = 10040
- `ProtocolType` = 10041
- `ProtocolOption` = 10042
- `ProtocolNotSupported` = 10043
- `SocketNotSupported` = 10044
- `OperationNotSupported` = 10045
- `ProtocolFamilyNotSupported` = 10046
- `AddressFamilyNotSupported` = 10047
- `AddressAlreadyInUse` = 10048
- `AddressNotAvailable` = 10049
- `NetworkDown` = 10050
- `NetworkUnreachable` = 10051
- `NetworkReset` = 10052
- `ConnectionAborted` = 10053
- `ConnectionReset` = 10054
- `NoBufferSpaceAvailable` = 10055
- `IsConnected` = 10056
- `NotConnected` = 10057
- `Shutdown` = 10058
- `TimedOut` = 10060
- `ConnectionRefused` = 10061
- `HostDown` = 10064
- `HostUnreachable` = 10065
- `ProcessLimit` = 10067
- `SystemNotReady` = 10091
- `VersionNotSupported` = 10092
- `NotInitialized` = 10093
- `Disconnecting` = 10101
- `TypeNotFound` = 10109
- `HostNotFound` = 11001
- `TryAgain` = 11002
- `NoRecovery` = 11003
- `NoData` = 11004
- `IOPending` = 997
- `OperationAborted` = 995

---

#### SocketFlags

**Line:** 800516

**Values:**

- `None` = 0
- `OutOfBand` = 1
- `Peek` = 2
- `DontRoute` = 4
- `MaxIOVectorLength` = 16
- `Truncated` = 256
- `ControlDataTruncated` = 512
- `Broadcast` = 1024
- `Multicast` = 2048
- `Partial` = 32768

---

#### SocketOptionName

**Line:** 800545

**Values:**

- `Debug` = 1
- `AcceptConnection` = 2
- `ReuseAddress` = 4
- `KeepAlive` = 8
- `DontRoute` = 16
- `Broadcast` = 32
- `UseLoopback` = 64
- `Linger` = 128
- `OutOfBandInline` = 256
- `SendBuffer` = 4097
- `ReceiveBuffer` = 4098
- `SendLowWater` = 4099
- `ReceiveLowWater` = 4100
- `SendTimeout` = 4101
- `ReceiveTimeout` = 4102
- `Error` = 4103
- `Type` = 4104
- `ReuseUnicastPort` = 12295
- `MaxConnections` = 2147483647
- `IPOptions` = 1
- `HeaderIncluded` = 2
- `TypeOfService` = 3
- `IpTimeToLive` = 4
- `MulticastInterface` = 9
- `MulticastTimeToLive` = 10
- `MulticastLoopback` = 11
- `AddMembership` = 12
- `DropMembership` = 13
- `DontFragment` = 14
- `AddSourceMembership` = 15
- `DropSourceMembership` = 16
- `BlockSource` = 17
- `UnblockSource` = 18
- `PacketInformation` = 19
- `HopLimit` = 21
- `IPProtectionLevel` = 23
- `IPv6Only` = 27
- `NoDelay` = 1
- `BsdUrgent` = 2
- `Expedited` = 2
- `NoChecksum` = 1
- `ChecksumCoverage` = 20
- `UpdateAcceptContext` = 28683
- `UpdateConnectContext` = 28688

---

#### SocketShutdown

**Line:** 800598

**Values:**

- `Receive` = 0
- `Send` = 1
- `Both` = 2

---

#### SocketType

**Line:** 800608

**Values:**

- `Stream` = 1
- `Dgram` = 2
- `Raw` = 3
- `Rdm` = 4
- `Seqpacket` = 5

---

#### SoftShadowQuality

**Line:** 900439

**Values:**

- `UsePipelineSettings` = 0
- `Low` = 1
- `Medium` = 2
- `High` = 3

---

#### SortDirection

**Line:** 626386

**Values:**

- `Ascending` = 0
- `Descending` = 1

---

#### SortingCriteria

**Line:** 896956

**Values:**

- `None` = 0
- `SortingLayer` = 1
- `RenderQueue` = 2
- `BackToFront` = 4
- `QuantizedFrontToBack` = 8
- `OptimizeStateChanges` = 16
- `CanvasOrder` = 32
- `RendererPriority` = 64
- `CommonOpaque` = 59
- `CommonTransparent` = 23

---

#### SpecialStartupMode

**Line:** 1432758

**Values:**

- `None` = 0
- `SetLookAt` = 1
- `SetShake` = 2
- `SetPunch` = 3
- `SetCameraShakePosition` = 4

---

#### SpreadsheetsResource

**Line:** 1384444

---

#### SpriteAssetImportFormats

**Line:** 1229940

**Values:**

- `None` = 0
- `TexturePackerJsonArray` = 1

---

#### SpriteDrawMode

**Line:** 869372

**Values:**

- `Simple` = 0
- `Sliced` = 1
- `Tiled` = 2

---

#### SpriteMeshType

**Line:** 869469

**Values:**

- `FullRect` = 0
- `Tight` = 1

---

#### SpritePackingRotation

**Line:** 869478

**Values:**

- `None` = 0
- `FlipHorizontal` = 1
- `FlipVertical` = 2
- `Rotate180` = 3
- `Any` = 15

---

#### SqlCompareOptions

**Line:** 1092083

**Values:**

- `None` = 0
- `IgnoreCase` = 1
- `IgnoreNonSpace` = 2
- `IgnoreKanaType` = 8
- `IgnoreWidth` = 16
- `BinarySort` = 32768
- `BinarySort2` = 16384

---

#### SslPolicyErrors

**Line:** 802803

**Values:**

- `None` = 0
- `RemoteCertificateNotAvailable` = 1
- `RemoteCertificateNameMismatch` = 2
- `RemoteCertificateChainErrors` = 4

---

#### SslProtocols

**Line:** 778450

**Values:**

- `None` = 0
- `Ssl2` = 12
- `Ssl3` = 48
- `Tls` = 192
- `Tls11` = 768
- `Tls12` = 3072
- `Tls13` = 12288
- `Default` = 240

---

#### StackTraceLogType

**Line:** 870376

**Values:**

- `None` = 0
- `ScriptOnly` = 1
- `Full` = 2

---

#### StandaloneInputModule

**Line:** 1360668

---

#### StatNature

**Line:** 1076694

**Values:**

- `Multiplier` = 0
- `Additive` = 1
- `Divisor` = 2
- `OneMinusMultiplier` = 3

---

#### StatType

**Line:** 1077360

**Values:**

- `Damage` = 0
- `Health` = 1
- `MaxLevel` = 2
- `Experience` = 3
- `Cost` = 4
- `TimerSpeed` = 5
- `SellPrice` = 6
- `MaxCount` = 7
- `Bonus` = 8
- `FreebieChance` = 10
- `CriticalChance` = 11
- `CriticalDamage` = 12
- `BlockChance` = 13
- `HealthRegen` = 14
- `LifeSteal` = 15
- `DoubleDamageChance` = 16
- `AttackSpeed` = 17
- `MoveSpeed` = 18

---

#### SteamClientHandlingStatus

**Line:** 587077

**Values:**

- `Unknown` = 0
- `Declined` = 1
- `Approved` = 2

---

#### SteamPeriod

**Line:** 584126

**Values:**

- `Day` = 0
- `Week` = 1
- `Month` = 2
- `Year` = 3

---

#### SteamPurchasingStatus

**Line:** 534130

**Values:**

- `Locked` = 0
- `Active` = 1
- `Trusted` = 2

---

#### StencilOp

**Line:** 891840

**Values:**

- `Keep` = 0
- `Zero` = 1
- `Replace` = 2
- `IncrementSaturate` = 3
- `DecrementSaturate` = 4
- `Invert` = 5
- `IncrementWrap` = 6
- `DecrementWrap` = 7

---

#### SteppingStoneEndReason

**Line:** 1079602

**Values:**

- `Fell` = 0
- `ReachedEnd` = 1

---

#### StoreActionsOptimization

**Line:** 900560

**Values:**

- `Auto` = 0
- `Discard` = 1
- `Store` = 2

---

#### StoreLocation

**Line:** 778915

**Values:**

- `CurrentUser` = 1
- `LocalMachine` = 2

---

#### StoreName

**Line:** 778924

**Values:**

- `AddressBook` = 1
- `AuthRoot` = 2
- `CertificateAuthority` = 3
- `Disallowed` = 4
- `My` = 5
- `Root` = 6
- `TrustedPeople` = 7
- `TrustedPublisher` = 8

---

#### StoreSpecificPurchaseErrorCode

**Line:** 1407494

**Values:**

- `SKErrorUnknown` = 0
- `SKErrorClientInvalid` = 1
- `SKErrorPaymentCancelled` = 2
- `SKErrorPaymentInvalid` = 3
- `SKErrorPaymentNotAllowed` = 4
- `SKErrorStoreProductNotAvailable` = 5
- `SKErrorCloudServicePermissionDenied` = 6
- `SKErrorCloudServiceNetworkConnectionFailed` = 7
- `SKErrorCloudServiceRevoked` = 8
- `BILLING_RESPONSE_RESULT_OK` = 9
- `BILLING_RESPONSE_RESULT_USER_CANCELED` = 10
- `BILLING_RESPONSE_RESULT_SERVICE_UNAVAILABLE` = 11
- `BILLING_RESPONSE_RESULT_BILLING_UNAVAILABLE` = 12
- `BILLING_RESPONSE_RESULT_ITEM_UNAVAILABLE` = 13
- `BILLING_RESPONSE_RESULT_DEVELOPER_ERROR` = 14
- `BILLING_RESPONSE_RESULT_ERROR` = 15
- `BILLING_RESPONSE_RESULT_ITEM_ALREADY_OWNED` = 16
- `BILLING_RESPONSE_RESULT_ITEM_NOT_OWNED` = 17
- `IABHELPER_ERROR_BASE` = 18
- `IABHELPER_REMOTE_EXCEPTION` = 19
- `IABHELPER_BAD_RESPONSE` = 20
- `IABHELPER_VERIFICATION_FAILED` = 21
- `IABHELPER_SEND_INTENT_FAILED` = 22
- `IABHELPER_USER_CANCELLED` = 23
- `IABHELPER_UNKNOWN_PURCHASE_RESPONSE` = 24
- `IABHELPER_MISSING_TOKEN` = 25
- `IABHELPER_UNKNOWN_ERROR` = 26
- `IABHELPER_SUBSCRIPTIONS_NOT_AVAILABLE` = 27
- `IABHELPER_INVALID_CONSUMPTION` = 28
- `Amazon_ALREADY_PURCHASED` = 29
- `Amazon_FAILED` = 30
- `Amazon_INVALID_SKU` = 31
- `Amazon_NOT_SUPPORTED` = 32
- `Unknown` = 33

---

#### StreamMessageTransport

**Line:** 547634

---

#### StreamingContextStates

**Line:** 226368

**Values:**

- `CrossProcess` = 1
- `CrossMachine` = 2
- `File` = 4
- `Persistence` = 8
- `Remoting` = 16
- `Other` = 32
- `Clone` = 64
- `CrossAppDomain` = 128
- `All` = 255

---

#### StringComparison

**Line:** 57733

**Values:**

- `CurrentCulture` = 0
- `CurrentCultureIgnoreCase` = 1
- `InvariantCulture` = 2
- `InvariantCultureIgnoreCase` = 3
- `Ordinal` = 4
- `OrdinalIgnoreCase` = 5

---

#### StringEscapeHandling

**Line:** 1032379

**Values:**

- `Default` = 0
- `EscapeNonAscii` = 1
- `EscapeHtml` = 2

---

#### StringSplitOptions

**Line:** 57747

**Values:**

- `None` = 0
- `RemoveEmptyEntries` = 1

---

#### StyleKeyword

**Line:** 658426

**Values:**

- `Undefined` = 0
- `Null` = 1
- `Auto` = 2
- `None` = 3
- `Initial` = 4

---

#### SubPassFlags

**Line:** 895046

**Values:**

- `None` = 0
- `ReadOnlyDepth` = 2
- `ReadOnlyStencil` = 4
- `ReadOnlyDepthStencil` = 6

---

#### SubStringFormatter

**Line:** 1322131

---

#### SubscriptionPeriodUnit

**Line:** 1407735

**Values:**

- `Day` = 0
- `Month` = 1
- `Week` = 2
- `Year` = 3
- `NotAvailable` = 4

---

#### SubscriptionRenewalStatus

**Line:** 586508

**Values:**

- `Unknown` = 0
- `NotExpectedToRenew` = 1
- `ExpectedToRenew` = 2

---

#### SubscriptionState

**Line:** 1511104

**Values:**

- `Unsubscribed` = 0
- `Synced` = 1
- `Unsynced` = 2
- `Error` = 3
- `Subscribing` = 4

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

- `VertexProcessing` = 0
- `PixelProcessing` = 1

---

#### SynchronisationStageFlags

**Line:** 892511

**Values:**

- `VertexProcessing` = 1
- `PixelProcessing` = 2
- `ComputeProcessing` = 4
- `AllGPUOperations` = 7

---

#### SystemInterfaceFlags

**Line:** 1590846

**Values:**

- `None` = 0
- `IInitializeSystem` = 2
- `IExecuteSystem` = 4
- `ICleanupSystem` = 8
- `ITearDownSystem` = 16
- `IReactiveSystem` = 32

---

#### SystemLanguage

**Line:** 870502

**Values:**

- `Afrikaans` = 0
- `Arabic` = 1
- `Basque` = 2
- `Belarusian` = 3
- `Bulgarian` = 4
- `Catalan` = 5
- `Chinese` = 6
- `Czech` = 7
- `Danish` = 8
- `Dutch` = 9
- `English` = 10
- `Estonian` = 11
- `Faroese` = 12
- `Finnish` = 13
- `French` = 14
- `German` = 15
- `Greek` = 16
- `Hebrew` = 17
- `Icelandic` = 19
- `Indonesian` = 20
- `Italian` = 21
- `Japanese` = 22
- `Korean` = 23
- `Latvian` = 24
- `Lithuanian` = 25
- `Norwegian` = 26
- `Polish` = 27
- `Portuguese` = 28
- `Romanian` = 29
- `Russian` = 30
- `SerboCroatian` = 31
- `Slovak` = 32
- `Slovenian` = 33
- `Spanish` = 34
- `Swedish` = 35
- `Thai` = 36
- `Turkish` = 37
- `Ukrainian` = 38
- `Vietnamese` = 39
- `ChineseSimplified` = 40
- `ChineseTraditional` = 41
- `Hindi` = 42
- `Unknown` = 43
- `Hungarian` = 18

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

- `Character` = 0
- `Sprite` = 1

---

#### TMP_VertexDataUpdateFlags

**Line:** 1221179

**Values:**

- `None` = 0
- `Vertices` = 1
- `Uv0` = 2
- `Uv2` = 4
- `Uv4` = 8
- `Colors32` = 16
- `All` = 255

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

- `Pixels` = 0
- `FontUnits` = 1
- `Percentage` = 2

---

#### TagValueType

**Line:** 1225709

**Values:**

- `None` = 0
- `NumericalValue` = 1
- `StringValue` = 2
- `ColorValue` = 4

---

#### TaskContinuationOptions

**Line:** 211699

**Values:**

- `None` = 0
- `PreferFairness` = 1
- `LongRunning` = 2
- `AttachedToParent` = 4
- `DenyChildAttach` = 8
- `HideScheduler` = 16
- `LazyCancellation` = 32
- `RunContinuationsAsynchronously` = 64
- `NotOnRanToCompletion` = 65536
- `NotOnFaulted` = 131072
- `NotOnCanceled` = 262144
- `OnlyOnRanToCompletion` = 393216
- `OnlyOnFaulted` = 327680
- `OnlyOnCanceled` = 196608
- `ExecuteSynchronously` = 524288

---

#### TaskCreationOptions

**Line:** 211669

**Values:**

- `None` = 0
- `PreferFairness` = 1
- `LongRunning` = 2
- `AttachedToParent` = 4
- `DenyChildAttach` = 8
- `HideScheduler` = 16
- `RunContinuationsAsynchronously` = 64

---

#### TaskStatus

**Line:** 209499

**Values:**

- `Created` = 0
- `WaitingForActivation` = 1
- `WaitingToRun` = 2
- `Running` = 3
- `WaitingForChildrenToComplete` = 4
- `RanToCompletion` = 5
- `Canceled` = 6
- `Faulted` = 7

---

#### TemporalAAQuality

**Line:** 914416

**Values:**

- `VeryLow` = 0
- `Low` = 1
- `Medium` = 2
- `High` = 3
- `VeryHigh` = 4

---

#### TextAlignmentOptions

**Line:** 1226962

**Values:**

- `TopLeft` = 257
- `Top` = 258
- `TopRight` = 260
- `TopJustified` = 264
- `TopFlush` = 272
- `TopGeoAligned` = 288
- `Left` = 513
- `Center` = 514
- `Right` = 516
- `Justified` = 520
- `Flush` = 528
- `CenterGeoAligned` = 544
- `BottomLeft` = 1025
- `Bottom` = 1026
- `BottomRight` = 1028
- `BottomJustified` = 1032
- `BottomFlush` = 1040
- `BottomGeoAligned` = 1056
- `BaselineLeft` = 2049
- `Baseline` = 2050
- `BaselineRight` = 2052
- `BaselineJustified` = 2056
- `BaselineFlush` = 2064
- `BaselineGeoAligned` = 2080
- `MidlineLeft` = 4097
- `Midline` = 4098
- `MidlineRight` = 4100
- `MidlineJustified` = 4104
- `MidlineFlush` = 4112
- `MidlineGeoAligned` = 4128
- `CaplineLeft` = 8193
- `Capline` = 8194
- `CaplineRight` = 8196
- `CaplineJustified` = 8200
- `CaplineFlush` = 8208
- `CaplineGeoAligned` = 8224
- `Converted` = 65535

---

#### TextAnchor

**Line:** 1580941

**Values:**

- `UpperLeft` = 0
- `UpperCenter` = 1
- `UpperRight` = 2
- `MiddleLeft` = 3
- `MiddleCenter` = 4
- `MiddleRight` = 5
- `LowerLeft` = 6
- `LowerCenter` = 7
- `LowerRight` = 8

---

#### TextClipping

**Line:** 1452103

**Values:**

- `Overflow` = 0
- `Clip` = 1
- `Ellipsis` = 2

---

#### TextContainerAnchors

**Line:** 1220142

**Values:**

- `TopLeft` = 0
- `Top` = 1
- `TopRight` = 2
- `Left` = 3
- `Middle` = 4
- `Right` = 5
- `BottomLeft` = 6
- `Bottom` = 7
- `BottomRight` = 8
- `Custom` = 9

---

#### TextEditor

**Line:** 1453124

---

#### TextElementType

**Line:** 1348710

**Values:**

- `Character` = 1
- `Sprite` = 2

---

#### TextFontWeight

**Line:** 1347142

**Values:**

- `Thin` = 100
- `ExtraLight` = 200
- `Light` = 300
- `Regular` = 400
- `Medium` = 500
- `SemiBold` = 600
- `Bold` = 700
- `Heavy` = 800
- `Black` = 900

---

#### TextGeneratorType

**Line:** 1580957

**Values:**

- `Standard` = 0
- `Advanced` = 1

---

#### TextOverflow

**Line:** 659927

**Values:**

- `Clip` = 0
- `Ellipsis` = 1

---

#### TextOverflowModes

**Line:** 1227060

**Values:**

- `Overflow` = 0
- `Ellipsis` = 1
- `Masking` = 2
- `Truncate` = 3
- `ScrollRect` = 4
- `Page` = 5
- `Linked` = 6

---

#### TextOverflowPosition

**Line:** 659917

**Values:**

- `End` = 0
- `Start` = 1
- `Middle` = 2

---

#### TextRenderFlags

**Line:** 1227032

**Values:**

- `DontRender` = 0
- `Render` = 255

---

#### TextWrappingModes

**Line:** 1227074

**Values:**

- `NoWrap` = 0
- `Normal` = 1
- `PreserveWhitespace` = 2
- `PreserveWhitespaceNoWrap` = 3

---

#### TextureCreationFlags

**Line:** 899343

**Values:**

- `None` = 0
- `MipChain` = 1
- `DontInitializePixels` = 4
- `Crunch` = 64
- `DontUploadUponCreate` = 1024
- `IgnoreMipmapLimit` = 2048

---

#### TextureDimension

**Line:** 892379

**Values:**

- `None` = 0
- `Any` = 1
- `Tex2D` = 2
- `Tex3D` = 3
- `Cube` = 4
- `Tex2DArray` = 5
- `CubeArray` = 6

---

#### TextureFormat

**Line:** 875460

**Values:**

- `Alpha8` = 1
- `ARGB4444` = 2
- `RGB24` = 3
- `RGBA32` = 4
- `ARGB32` = 5
- `RGB565` = 7
- `R16` = 9
- `DXT1` = 10
- `DXT5` = 12
- `RGBA4444` = 13
- `BGRA32` = 14
- `RHalf` = 15
- `RGHalf` = 16
- `RGBAHalf` = 17
- `RFloat` = 18
- `RGFloat` = 19
- `RGBAFloat` = 20
- `YUY2` = 21
- `RGB9e5Float` = 22
- `BC4` = 26
- `BC5` = 27
- `BC6H` = 24
- `BC7` = 25
- `DXT1Crunched` = 28
- `DXT5Crunched` = 29
- `PVRTC_RGB2` = 30
- `PVRTC_RGBA2` = 31
- `PVRTC_RGB4` = 32
- `PVRTC_RGBA4` = 33
- `ETC_RGB4` = 34
- `EAC_R` = 41
- `EAC_R_SIGNED` = 42
- `EAC_RG` = 43
- `EAC_RG_SIGNED` = 44
- `ETC2_RGB` = 45
- `ETC2_RGBA1` = 46
- `ETC2_RGBA8` = 47
- `ASTC_4x4` = 48
- `ASTC_5x5` = 49
- `ASTC_6x6` = 50
- `ASTC_8x8` = 51
- `ASTC_10x10` = 52
- `ASTC_12x12` = 53
- `RG16` = 62
- `R8` = 63
- `ETC_RGB4Crunched` = 64
- `ETC2_RGBA8Crunched` = 65
- `ASTC_HDR_4x4` = 66
- `ASTC_HDR_5x5` = 67
- `ASTC_HDR_6x6` = 68
- `ASTC_HDR_8x8` = 69
- `ASTC_HDR_10x10` = 70
- `ASTC_HDR_12x12` = 71
- `RG32` = 72
- `RGB48` = 73
- `RGBA64` = 74
- `R8_SIGNED` = 75
- `RG16_SIGNED` = 76
- `RGB24_SIGNED` = 77
- `RGBA32_SIGNED` = 78
- `R16_SIGNED` = 79
- `RG32_SIGNED` = 80
- `RGB48_SIGNED` = 81
- `RGBA64_SIGNED` = 82

---

#### TextureMappingOptions

**Line:** 1227094

**Values:**

- `Character` = 0
- `Line` = 1
- `Paragraph` = 2
- `MatchAspect` = 3

---

#### TextureSizeMode

**Line:** 831763

**Values:**

- `Explicit` = 0
- `Scale` = 1
- `Functor` = 2

---

#### TextureWrapMode

**Line:** 875438

**Values:**

- `Repeat` = 0
- `Clamp` = 1
- `Mirror` = 2
- `MirrorOnce` = 3

---

#### ThreadState

**Line:** 179122

**Values:**

- `Running` = 0
- `StopRequested` = 1
- `SuspendRequested` = 2
- `Background` = 4
- `Unstarted` = 8
- `Stopped` = 16
- `WaitSleepJoin` = 32
- `Suspended` = 64
- `AbortRequested` = 128
- `Aborted` = 256

---

#### TimeSpanFormatOptions

**Line:** 1321168

**Values:**

- `InheritDefaults` = 0
- `Abbreviate` = 1
- `AbbreviateOff` = 2
- `LessThan` = 4
- `LessThanOff` = 8
- `TruncateShortest` = 16
- `TruncateAuto` = 32
- `TruncateFill` = 64
- `TruncateFull` = 128
- `RangeMilliSeconds` = 256
- `RangeSeconds` = 512
- `RangeMinutes` = 1024
- `RangeHours` = 2048
- `RangeDays` = 4096
- `RangeWeeks` = 8192

---

#### TimeSpanStyles

**Line:** 272591

**Values:**

- `None` = 0
- `AssumeNegative` = 1

---

#### TimeUnit

**Line:** 659473

**Values:**

- `Second` = 0
- `Millisecond` = 1

---

#### TimelineSlot

**Line:** 603311

---

#### TimerState

**Line:** 696319

**Values:**

- `Idle` = 0
- `InProgress` = 1
- `Done` = 2

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

- `Zero` = 0
- `Tls10Client` = 128
- `Tls10Server` = 64
- `Tls10` = 192
- `Tls11Client` = 512
- `Tls11Server` = 256
- `Tls11` = 768
- `Tls12Client` = 2048
- `Tls12Server` = 1024
- `Tls12` = 3072
- `ClientMask` = 2688
- `ServerMask` = 1344

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

- `None` = 0
- `Neutral` = 1
- `ACES` = 2

---

#### TouchPhase

**Line:** 1580247

**Values:**

- `Began` = 0
- `Moved` = 1
- `Stationary` = 2
- `Ended` = 3
- `Canceled` = 4

---

#### TouchScreenKeyboard

**Line:** 885677

---

#### TouchScreenKeyboardType

**Line:** 885846

**Values:**

- `Default` = 0
- `ASCIICapable` = 1
- `NumbersAndPunctuation` = 2
- `URL` = 3
- `NumberPad` = 4
- `PhonePad` = 5
- `NamePhonePad` = 6
- `EmailAddress` = 7
- `NintendoNetworkAccount` = 8
- `Social` = 9
- `Search` = 10
- `DecimalPad` = 11
- `OneTimeCode` = 12

---

#### TouchType

**Line:** 1580269

**Values:**

- `Direct` = 0
- `Indirect` = 1
- `Stylus` = 2

---

#### TraceEventType

**Line:** 777545

**Values:**

- `Critical` = 1
- `Error` = 2
- `Warning` = 4
- `Information` = 8
- `Verbose` = 16
- `Start` = 256
- `Stop` = 512
- `Suspend` = 1024
- `Resume` = 2048
- `Transfer` = 4096

---

#### TraceOptions

**Line:** 777785

**Values:**

- `None` = 0
- `LogicalOperationStack` = 1
- `DateTime` = 2
- `Timestamp` = 4
- `ProcessId` = 8
- `ThreadId` = 16
- `Callstack` = 32

---

#### TransferFormat

**Line:** 1570716

**Values:**

- `Binary` = 1
- `Text` = 2

---

#### TransferFunction

**Line:** 875399

**Values:**

- `sRGB` = 0
- `BT1886` = 1
- `PQ` = 2
- `Linear` = 3
- `Gamma22` = 4

---

#### TransformOriginOffset

**Line:** 659936

**Values:**

- `Left` = 1
- `Right` = 2
- `Top` = 3
- `Bottom` = 4
- `Center` = 5

---

#### TransientError

**Line:** 1310253

---

#### TranslationLocale

**Line:** 1406793

**Values:**

- `zh_TW` = 0
- `cs_CZ` = 1
- `da_DK` = 2
- `nl_NL` = 3
- `en_US` = 4
- `fr_FR` = 5
- `fi_FI` = 6
- `de_DE` = 7
- `iw_IL` = 8
- `hi_IN` = 9
- `it_IT` = 10
- `ja_JP` = 11
- `ko_KR` = 12
- `no_NO` = 13
- `pl_PL` = 14
- `pt_PT` = 15
- `ru_RU` = 16
- `es_ES` = 17
- `sv_SE` = 18
- `zh_CN` = 19
- `en_AU` = 20
- `en_CA` = 21
- `en_GB` = 22
- `fr_CA` = 23
- `el_GR` = 24
- `id_ID` = 25
- `ms_MY` = 26
- `pt_BR` = 27
- `es_MX` = 28
- `th_TH` = 29
- `tr_TR` = 30
- `vi_VN` = 31

---

#### TransparencySortMode

**Line:** 875189

**Values:**

- `Default` = 0
- `Perspective` = 1
- `Orthographic` = 2
- `CustomAxis` = 3

---

#### TrickleDown

**Line:** 634871

**Values:**

- `NoTrickleDown` = 0
- `TrickleDown` = 1

---

#### TweenType

**Line:** 1429065

**Values:**

- `Tweener` = 0
- `Sequence` = 1
- `Callback` = 2

---

#### TwoPaneSplitViewOrientation

**Line:** 630083

**Values:**

- `Horizontal` = 0
- `Vertical` = 1

---

#### TypeAttributes

**Line:** 267040

**Values:**

- `VisibilityMask` = 7
- `NotPublic` = 0
- `Public` = 1
- `NestedPublic` = 2
- `NestedPrivate` = 3
- `NestedFamily` = 4
- `NestedAssembly` = 5
- `NestedFamANDAssem` = 6
- `NestedFamORAssem` = 7
- `LayoutMask` = 24
- `AutoLayout` = 0
- `SequentialLayout` = 8
- `ExplicitLayout` = 16
- `ClassSemanticsMask` = 32
- `Class` = 0
- `Interface` = 32
- `Abstract` = 128
- `Sealed` = 256
- `SpecialName` = 1024
- `Import` = 4096
- `Serializable` = 8192
- `WindowsRuntime` = 16384
- `StringFormatMask` = 196608
- `AnsiClass` = 0
- `UnicodeClass` = 65536
- `AutoClass` = 131072
- `CustomFormatClass` = 196608
- `CustomFormatMask` = 12582912
- `BeforeFieldInit` = 1048576
- `RTSpecialName` = 2048
- `HasSecurity` = 262144
- `ReservedMask` = 264192

---

#### TypeCode

**Line:** 59505

**Values:**

- `Empty` = 0
- `Object` = 1
- `DBNull` = 2
- `Boolean` = 3
- `Char` = 4
- `SByte` = 5
- `Byte` = 6
- `Int16` = 7
- `UInt16` = 8
- `Int32` = 9
- `UInt32` = 10
- `Int64` = 11
- `UInt64` = 12
- `Single` = 13
- `Double` = 14
- `Decimal` = 15
- `DateTime` = 16
- `String` = 18

---

#### TypeGenerationOptions

**Line:** 1458034

**Values:**

- `None` = 0
- `ValueType` = 2
- `ReferenceType` = 4
- `Default` = 6

---

#### TypeInferenceRules

**Line:** 834935

**Values:**

- `TypeReferencedByFirstArgument` = 0
- `TypeReferencedBySecondArgument` = 1
- `ArrayOfTypeReferencedByFirstArgument` = 2
- `TypeOfFirstArgument` = 3

---

#### TypeNameAssemblyFormatHandling

**Line:** 1032389

**Values:**

- `Simple` = 0
- `Full` = 1

---

#### TypeNameHandling

**Line:** 1032399

**Values:**

- `None` = 0
- `Objects` = 1
- `Arrays` = 2
- `All` = 3
- `Auto` = 4

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

- `UIToolkit_UGUI` = 1
- `LowLevel` = 2

---

#### UISystemProfilerApi

**Line:** 1576689

---

#### UVChannelFlags

**Line:** 1578072

**Values:**

- `UV0` = 1
- `UV1` = 2
- `UV2` = 4
- `UV3` = 8

---

#### UltimateResourceFallbackLocation

**Line:** 264340

**Values:**

- `MainAssembly` = 0
- `Satellite` = 1

---

#### UnauthorizedType

**Line:** 685279

**Values:**

- `Undefined` = 0
- `UserBanned` = 1
- `UserTimedOut` = 2
- `UserTokenInvalid` = 3
- `UserTokenMismatch` = 4
- `UserNotFound` = 5

---

#### UndefinedSchemaIdHandling

**Line:** 1042886

**Values:**

- `None` = 0
- `UseTypeName` = 1
- `UseAssemblyQualifiedName` = 2

---

#### UniTaskStatus

**Line:** 1097328

**Values:**

- `Pending` = 0
- `Succeeded` = 1
- `Faulted` = 2
- `Canceled` = 3

---

#### UnicodeCategory

**Line:** 272600

**Values:**

- `UppercaseLetter` = 0
- `LowercaseLetter` = 1
- `TitlecaseLetter` = 2
- `ModifierLetter` = 3
- `OtherLetter` = 4
- `NonSpacingMark` = 5
- `SpacingCombiningMark` = 6
- `EnclosingMark` = 7
- `DecimalDigitNumber` = 8
- `LetterNumber` = 9
- `OtherNumber` = 10
- `SpaceSeparator` = 11
- `LineSeparator` = 12
- `ParagraphSeparator` = 13
- `Control` = 14
- `Format` = 15
- `Surrogate` = 16
- `PrivateUse` = 17
- `ConnectorPunctuation` = 18
- `DashPunctuation` = 19
- `OpenPunctuation` = 20
- `ClosePunctuation` = 21
- `InitialQuotePunctuation` = 22
- `FinalQuotePunctuation` = 23
- `OtherPunctuation` = 24
- `MathSymbol` = 25
- `CurrencySymbol` = 26
- `ModifierSymbol` = 27
- `OtherSymbol` = 28
- `OtherNotAssigned` = 29

---

#### UnicodeDecodingConformance

**Line:** 799046

**Values:**

- `Auto` = 0
- `Strict` = 1
- `Compat` = 2
- `Loose` = 3

---

#### UnicodeEncodingConformance

**Line:** 799057

**Values:**

- `Auto` = 0
- `Strict` = 1
- `Compat` = 2

---

#### UnityEventCallState

**Line:** 887496

**Values:**

- `Off` = 0
- `EditorAndRuntime` = 1
- `RuntimeOnly` = 2

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

- `BackBufferColor` = 0
- `BackBufferDepth` = 1
- `CameraColor` = 2
- `CameraDepth` = 3
- `MainShadowsTexture` = 4
- `AdditionalShadowsTexture` = 5
- `GBuffer0` = 6
- `GBuffer1` = 7
- `GBuffer2` = 8
- `GBuffer3` = 9
- `GBuffer4` = 10
- `GBuffer5` = 11
- `GBuffer6` = 12
- `CameraOpaqueTexture` = 13
- `CameraDepthTexture` = 14
- `CameraNormalsTexture` = 15
- `MotionVectorColor` = 16
- `MotionVectorDepth` = 17
- `InternalColorLut` = 18
- `DebugScreenColor` = 19
- `DebugScreenDepth` = 20
- `AfterPostProcessColor` = 21
- `OverlayUITexture` = 22
- `RenderingLayersTexture` = 23
- `DBuffer0` = 24
- `DBuffer1` = 25
- `DBuffer2` = 26
- `DBufferDepth` = 27
- `SSAOTexture` = 28

---

#### UnloadSceneOptions

**Line:** 888968

**Values:**

- `None` = 0
- `UnloadAllEmbeddedSceneObjects` = 1

---

#### UnmanagedType

**Line:** 229138

**Values:**

- `Bool` = 2
- `I1` = 3
- `U1` = 4
- `I2` = 5
- `U2` = 6
- `I4` = 7
- `U4` = 8
- `I8` = 9
- `U8` = 10
- `R4` = 11
- `R8` = 12
- `Currency` = 15
- `BStr` = 19
- `LPStr` = 20
- `LPWStr` = 21
- `LPTStr` = 22
- `ByValTStr` = 23
- `IUnknown` = 25
- `IDispatch` = 26
- `Struct` = 27
- `Interface` = 28
- `SafeArray` = 29
- `ByValArray` = 30
- `SysInt` = 31
- `SysUInt` = 32
- `VBByRefStr` = 34
- `AnsiBStr` = 35
- `TBStr` = 36
- `VariantBool` = 37
- `FunctionPtr` = 38
- `AsAny` = 40
- `LPArray` = 42
- `LPStruct` = 43
- `CustomMarshaler` = 44
- `Error` = 45
- `IInspectable` = 46
- `HString` = 47
- `LPUTF8Str` = 48

---

#### UpdateAvailability

**Line:** 1579029

**Values:**

- `Unknown` = 0
- `UpdateNotAvailable` = 1
- `UpdateAvailable` = 2
- `DeveloperTriggeredUpdateInProgress` = 3

---

#### UpdateNotice

**Line:** 1432770

**Values:**

- `None` = 0
- `RewindStep` = 1

---

#### UpdateType

**Line:** 1429075

**Values:**

- `Normal` = 0
- `Late` = 1
- `Fixed` = 2
- `Manual` = 3

---

#### UploadStatus

**Line:** 1501496

**Values:**

- `NotStarted` = 0
- `Starting` = 1
- `Uploading` = 2
- `Completed` = 3
- `Failed` = 4

---

#### UpscalingFilterSelection

**Line:** 900583

**Values:**

- `Auto` = 0
- `Linear` = 1
- `Point` = 2
- `FSR` = 3
- `STP` = 4

---

#### UriComponents

**Line:** 774586

**Values:**

- `Scheme` = 1
- `UserInfo` = 2
- `Host` = 4
- `Port` = 8
- `Path` = 16
- `Query` = 32
- `Fragment` = 64
- `StrongPort` = 128
- `NormalizedHost` = 256
- `KeepDelimiter` = 1073741824
- `AbsoluteUri` = 127
- `HostAndPort` = 132
- `StrongAuthority` = 134
- `SchemeAndServer` = 13
- `HttpRequestUrl` = 61
- `PathAndQuery` = 48

---

#### UriFormat

**Line:** 774610

**Values:**

- `UriEscaped` = 1
- `Unescaped` = 2
- `SafeUnescaped` = 3

---

#### UriHostNameType

**Line:** 774714

**Values:**

- `Unknown` = 0
- `Basic` = 1
- `Dns` = 2
- `IPv4` = 3
- `IPv6` = 4

---

#### UriIdnScope

**Line:** 774620

**Values:**

- `None` = 0
- `AllExceptIntranet` = 1
- `All` = 2

---

#### UriKind

**Line:** 774575

**Values:**

- `RelativeOrAbsolute` = 0
- `Absolute` = 1
- `Relative` = 2

---

#### UsageHints

**Line:** 641886

**Values:**

- `None` = 0
- `DynamicTransform` = 1
- `GroupTransform` = 2
- `MaskContainer` = 4
- `DynamicColor` = 8

---

#### UsercentricsAnalyticsEventType

**Line:** 1564875

**Values:**

- `CmpShown` = 0
- `AcceptAllFirstLayer` = 1
- `DenyAllFirstLayer` = 2
- `SaveFirstLayer` = 3
- `AcceptAllSecondLayer` = 4
- `DenyAllSecondLayer` = 5
- `SaveSecondLayer` = 6
- `ImprintLink` = 7
- `MoreInformationLink` = 8
- `PrivacyPolicyLink` = 9
- `CcpaTogglesOn` = 10
- `CcpaTogglesOff` = 11

---

#### UsercentricsConsentType

**Line:** 1564510

**Values:**

- `Explicit` = 0
- `Implicit` = 1

---

#### UsercentricsLayout

**Line:** 1565153

**Values:**

- `Undefined` = 0
- `Full` = 1
- `Sheet` = 2
- `PopupBottom` = 3
- `PopupCenter` = 4

---

#### UsercentricsNetworkMode

**Line:** 1564443

**Values:**

- `World` = 0
- `EU` = 1

---

#### UsercentricsUserInteraction

**Line:** 1564535

**Values:**

- `AcceptAll` = 0
- `DenyAll` = 1
- `Granular` = 2
- `NoInteraction` = 3

---

#### UsercentricsVariant

**Line:** 1564905

**Values:**

- `Default` = 0
- `CCPA` = 1
- `TCF` = 2

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

- `None` = 0
- `Depth` = 1
- `Color` = 2
- `Normal` = 4

---

#### VRTextureUsage

**Line:** 875589

**Values:**

- `None` = 0
- `OneEye` = 1
- `TwoEyes` = 2
- `DeviceSpecific` = 3

---

#### ValidationType

**Line:** 741965

**Values:**

- `None` = 0
- `Auto` = 1
- `DTD` = 2
- `XDR` = 3
- `Schema` = 4

---

#### ValueTaskSourceOnCompletedFlags

**Line:** 213714

**Values:**

- `None` = 0
- `UseSchedulingContext` = 1
- `FlowExecutionContext` = 2

---

#### ValueTaskSourceStatus

**Line:** 213724

**Values:**

- `Pending` = 0
- `Succeeded` = 1
- `Faulted` = 2
- `Canceled` = 3

---

#### VarEnum

**Line:** 229085

**Values:**

- `VT_EMPTY` = 0
- `VT_NULL` = 1
- `VT_I2` = 2
- `VT_I4` = 3
- `VT_R4` = 4
- `VT_R8` = 5
- `VT_CY` = 6
- `VT_DATE` = 7
- `VT_BSTR` = 8
- `VT_DISPATCH` = 9
- `VT_ERROR` = 10
- `VT_BOOL` = 11
- `VT_VARIANT` = 12
- `VT_UNKNOWN` = 13
- `VT_DECIMAL` = 14
- `VT_I1` = 16
- `VT_UI1` = 17
- `VT_UI2` = 18
- `VT_UI4` = 19
- `VT_I8` = 20
- `VT_UI8` = 21
- `VT_INT` = 22
- `VT_UINT` = 23
- `VT_VOID` = 24
- `VT_HRESULT` = 25
- `VT_PTR` = 26
- `VT_SAFEARRAY` = 27
- `VT_CARRAY` = 28
- `VT_USERDEFINED` = 29
- `VT_LPSTR` = 30
- `VT_LPWSTR` = 31
- `VT_RECORD` = 36
- `VT_FILETIME` = 64
- `VT_BLOB` = 65
- `VT_STREAM` = 66
- `VT_STORAGE` = 67
- `VT_STREAMED_OBJECT` = 68
- `VT_STORED_OBJECT` = 69
- `VT_BLOB_OBJECT` = 70
- `VT_CF` = 71
- `VT_CLSID` = 72
- `VT_VECTOR` = 4096
- `VT_ARRAY` = 8192
- `VT_BYREF` = 16384

---

#### VarIntConst

**Line:** 566820

**Values:**

- `Zero` = 0
- `MinusOne` = 1
- `One` = 2
- `Sixteen` = 32

---

#### Variant

**Line:** 1493654

---

#### VersionChangeType

**Line:** 641857

**Values:**

- `Bindings` = 1
- `ViewData` = 2
- `Hierarchy` = 4
- `Layout` = 8
- `StyleSheet` = 16
- `Styles` = 32
- `Overflow` = 64
- `BorderRadius` = 128
- `BorderWidth` = 256
- `Transform` = 512
- `Size` = 1024
- `Repaint` = 2048
- `Opacity` = 4096
- `Color` = 8192
- `RenderHints` = 16384
- `TransitionProperty` = 32768
- `EventCallbackCategories` = 65536
- `DisableRendering` = 131072
- `BindingRegistration` = 262144
- `DataSource` = 524288
- `Picking` = 1048576

---

#### VertexAttribute

**Line:** 891672

**Values:**

- `Position` = 0
- `Normal` = 1
- `Tangent` = 2
- `Color` = 3
- `TexCoord0` = 4
- `TexCoord1` = 5
- `TexCoord2` = 6
- `TexCoord3` = 7
- `TexCoord4` = 8
- `TexCoord5` = 9
- `TexCoord6` = 10
- `TexCoord7` = 11
- `BlendWeight` = 12
- `BlendIndices` = 13

---

#### VertexAttributeFormat

**Line:** 891652

**Values:**

- `Float32` = 0
- `Float16` = 1
- `UNorm8` = 2
- `SNorm8` = 3
- `UNorm16` = 4
- `SNorm16` = 5
- `UInt8` = 6
- `SInt8` = 7
- `UInt16` = 8
- `SInt16` = 9
- `UInt32` = 10
- `SInt32` = 11

---

#### VertexSortingOrder

**Line:** 1225334

**Values:**

- `Normal` = 0
- `Reverse` = 1

---

#### VerticalAlignmentOptions

**Line:** 1227019

**Values:**

- `Top` = 256
- `Middle` = 512
- `Bottom` = 1024
- `Baseline` = 2048
- `Geometry` = 4096
- `Capline` = 8192

---

#### VerticalWrapMode

**Line:** 1580975

**Values:**

- `Truncate` = 0
- `Overflow` = 1

---

#### Visibility

**Line:** 659948

**Values:**

- `Visible` = 0
- `Hidden` = 1

---

#### VisitExceptionKind

**Line:** 1457327

**Values:**

- `None` = 0
- `Internal` = 1
- `Visitor` = 2
- `All` = 3

---

#### VisitReturnCode

**Line:** 1457983

**Values:**

- `Ok` = 0
- `NullContainer` = 1
- `InvalidContainerType` = 2
- `MissingPropertyBag` = 3
- `InvalidPath` = 4
- `InvalidCast` = 5
- `AccessViolation` = 6

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

- `EveryFrame` = 0
- `ViaScripting` = 1
- `UsePipelineSettings` = 2

---

#### WaitTimeoutMode

**Line:** 884694

**Values:**

- `Realtime` = 0
- `InGameTime` = 1

---

#### WebExceptionStatus

**Line:** 792117

**Values:**

- `Success` = 0
- `NameResolutionFailure` = 1
- `ConnectFailure` = 2
- `ReceiveFailure` = 3
- `SendFailure` = 4
- `PipelineFailure` = 5
- `RequestCanceled` = 6
- `ProtocolError` = 7
- `ConnectionClosed` = 8
- `TrustFailure` = 9
- `SecureChannelFailure` = 10
- `ServerProtocolViolation` = 11
- `KeepAliveFailure` = 12
- `Pending` = 13
- `Timeout` = 14
- `ProxyNameResolutionFailure` = 15
- `UnknownError` = 16
- `MessageLengthLimitExceeded` = 17
- `CacheEntryNotFound` = 18
- `RequestProhibitedByCachePolicy` = 19
- `RequestProhibitedByProxy` = 20

---

#### WebSocketCloseStatus

**Line:** 802424

**Values:**

- `NormalClosure` = 1000
- `EndpointUnavailable` = 1001
- `ProtocolError` = 1002
- `InvalidMessageType` = 1003
- `Empty` = 1005
- `InvalidPayloadData` = 1007
- `PolicyViolation` = 1008
- `MessageTooBig` = 1009
- `MandatoryExtension` = 1010
- `InternalServerError` = 1011

---

#### WebSocketError

**Line:** 802441

**Values:**

- `Success` = 0
- `InvalidMessageType` = 1
- `Faulted` = 2
- `NativeError` = 3
- `NotAWebSocket` = 4
- `UnsupportedVersion` = 5
- `UnsupportedProtocol` = 6
- `HeaderError` = 7
- `ConnectionClosedPrematurely` = 8
- `InvalidState` = 9

---

#### WebSocketMessageType

**Line:** 802513

**Values:**

- `Text` = 0
- `Binary` = 1
- `Close` = 2

---

#### WebSocketState

**Line:** 802564

**Values:**

- `None` = 0
- `Connecting` = 1
- `Open` = 2
- `CloseSent` = 3
- `CloseReceived` = 4
- `Closed` = 5
- `Aborted` = 6

---

#### WeightedMode

**Line:** 869715

**Values:**

- `None` = 0
- `In` = 1
- `Out` = 2
- `Both` = 3

---

#### WellKnownObjectMode

**Line:** 221866

**Values:**

- `Singleton` = 1
- `SingleCall` = 2

---

#### WhitePoint

**Line:** 875388

**Values:**

- `D65` = 0

---

#### WhiteSpace

**Line:** 659957

**Values:**

- `Normal` = 0
- `NoWrap` = 1
- `Pre` = 2
- `PreWrap` = 3

---

#### WhitespaceHandling

**Line:** 741979

**Values:**

- `All` = 0
- `Significant` = 1
- `None` = 2

---

#### WindowsAccountType

**Line:** 220382

**Values:**

- `Normal` = 0
- `Guest` = 1
- `System` = 2
- `Anonymous` = 3

---

#### WireDataType

**Line:** 532065

**Values:**

- `Invalid` = 0
- `Null` = 1
- `VarInt` = 2
- `VarInt128` = 3
- `F32` = 4
- `F32Vec2` = 5
- `F32Vec3` = 6
- `F64` = 7
- `F64Vec2` = 8
- `F64Vec3` = 9
- `Float32` = 10
- `Float64` = 11
- `String` = 12
- `Bytes` = 13
- `AbstractStruct` = 14
- `NullableStruct` = 15
- `Struct` = 16
- `EndStruct` = 17
- `ValueCollection` = 18
- `KeyValueCollection` = 19
- `ObjectTable` = 20
- `NullableVarInt` = 21
- `NullableVarInt128` = 22
- `NullableF32` = 23
- `NullableF32Vec2` = 24
- `NullableF32Vec3` = 25
- `NullableF64` = 26
- `NullableF64Vec2` = 27
- `NullableF64Vec3` = 28
- `NullableFloat32` = 29
- `NullableFloat64` = 30
- `MetaGuid` = 31
- `NullableMetaGuid` = 32

---

#### WireMessageWriteQueue

**Line:** 551472

---

#### WirePacketCompression

**Line:** 551611

**Values:**

- `None` = 0
- `Deflate` = 1

---

#### WirePacketType

**Line:** 551599

**Values:**

- `None` = 0
- `Message` = 1
- `Ping` = 2
- `PingResponse` = 3
- `HealthCheck` = 4

---

#### Wrap

**Line:** 659882

**Values:**

- `NoWrap` = 0
- `Wrap` = 1
- `WrapReverse` = 2

---

#### WrapMode

**Line:** 869799

**Values:**

- `Once` = 1
- `Loop` = 2
- `PingPong` = 4
- `Default` = 0
- `ClampForever` = 8
- `Clamp` = 1

---

#### WriteState

**Line:** 1032411

**Values:**

- `Error` = 0
- `Closed` = 1
- `Object` = 2
- `Array` = 3
- `Constructor` = 4
- `Property` = 5
- `Start` = 6

---

#### X500DistinguishedNameFlags

**Line:** 778940

**Values:**

- `None` = 0
- `Reversed` = 1
- `UseSemicolons` = 16
- `DoNotUsePlusSign` = 32
- `DoNotUseQuotes` = 64
- `UseCommas` = 128
- `UseNewLines` = 256
- `UseUTF8Encoding` = 4096
- `UseT61Encoding` = 8192
- `ForceUTF8Encoding` = 16384

---

#### X509ChainStatusFlags

**Line:** 1447967

**Values:**

- `InvalidBasicConstraints` = 1024
- `NoError` = 0
- `NotSignatureValid` = 8
- `NotTimeNested` = 2
- `NotTimeValid` = 1
- `PartialChain` = 65536
- `UntrustedRoot` = 32

---

#### X509ContentType

**Line:** 220005

**Values:**

- `Unknown` = 0
- `Cert` = 1
- `SerializedCert` = 2
- `Pfx` = 3
- `Pkcs12` = 3
- `SerializedStore` = 4
- `Pkcs7` = 5
- `Authenticode` = 6

---

#### X509FindType

**Line:** 778991

**Values:**

- `FindByThumbprint` = 0
- `FindBySubjectName` = 1
- `FindBySubjectDistinguishedName` = 2
- `FindByIssuerName` = 3
- `FindByIssuerDistinguishedName` = 4
- `FindBySerialNumber` = 5
- `FindByTimeValid` = 6
- `FindByTimeNotYetValid` = 7
- `FindByTimeExpired` = 8
- `FindByTemplateName` = 9
- `FindByApplicationPolicy` = 10
- `FindByCertificatePolicy` = 11
- `FindByExtension` = 12
- `FindByKeyUsage` = 13
- `FindBySubjectKeyIdentifier` = 14

---

#### X509KeyStorageFlags

**Line:** 220021

**Values:**

- `DefaultKeySet` = 0
- `UserKeySet` = 1
- `MachineKeySet` = 2
- `Exportable` = 4
- `UserProtected` = 8
- `PersistKeySet` = 16
- `EphemeralKeySet` = 32

---

#### X509KeyUsageFlags

**Line:** 779014

**Values:**

- `None` = 0
- `EncipherOnly` = 1
- `CrlSign` = 2
- `KeyCertSign` = 4
- `KeyAgreement` = 8
- `DataEncipherment` = 16
- `KeyEncipherment` = 32
- `NonRepudiation` = 64
- `DigitalSignature` = 128
- `DecipherOnly` = 32768

---

#### X509NameType

**Line:** 779031

**Values:**

- `SimpleName` = 0
- `EmailName` = 1
- `UpnName` = 2
- `DnsName` = 3
- `DnsFromAlternativeName` = 4
- `UrlName` = 5

---

#### X509RevocationFlag

**Line:** 779044

**Values:**

- `EndCertificateOnly` = 0
- `EntireChain` = 1
- `ExcludeRoot` = 2

---

#### X509RevocationMode

**Line:** 779054

**Values:**

- `NoCheck` = 0
- `Online` = 1
- `Offline` = 2

---

#### X509SubjectKeyIdentifierHashAlgorithm

**Line:** 779064

**Values:**

- `Sha1` = 0
- `ShortSha1` = 1
- `CapiSha1` = 2

---

#### X509VerificationFlags

**Line:** 779075

**Values:**

- `NoFlag` = 0
- `IgnoreNotTimeValid` = 1
- `IgnoreCtlNotTimeValid` = 2
- `IgnoreNotTimeNested` = 4
- `IgnoreInvalidBasicConstraints` = 8
- `AllowUnknownCertificateAuthority` = 16
- `IgnoreWrongUsage` = 32
- `IgnoreInvalidName` = 64
- `IgnoreInvalidPolicy` = 128
- `IgnoreEndRevocationUnknown` = 256
- `IgnoreCtlSignerRevocationUnknown` = 512
- `IgnoreCertificateAuthorityRevocationUnknown` = 1024
- `IgnoreRootRevocationUnknown` = 2048
- `AllFlags` = 4095

---

#### X86

**Line:** 1345491

---

#### XObjectChange

**Line:** 1561018

**Values:**

- `Add` = 0
- `Remove` = 1
- `Name` = 2
- `Value` = 3

---

#### XPathNamespaceScope

**Line:** 752792

**Values:**

- `All` = 0
- `ExcludeXml` = 1
- `Local` = 2

---

#### XPathNodeType

**Line:** 752937

**Values:**

- `Root` = 0
- `Element` = 1
- `Attribute` = 2
- `Namespace` = 3
- `Text` = 4
- `SignificantWhitespace` = 5
- `Whitespace` = 6
- `ProcessingInstruction` = 7
- `Comment` = 8
- `All` = 9

---

#### XPathResultType

**Line:** 752725

**Values:**

- `Number` = 0
- `String` = 1
- `Boolean` = 2
- `NodeSet` = 3
- `Navigator` = 1
- `Any` = 5
- `Error` = 6

---

#### XPathScanner

**Line:** 770491

---

#### XmlDateTimeSerializationMode

**Line:** 751443

**Values:**

- `Local` = 0
- `Utc` = 1
- `Unspecified` = 2
- `RoundtripKind` = 3

---

#### XmlNamespaceScope

**Line:** 752344

**Values:**

- `All` = 0
- `ExcludeXml` = 1
- `Local` = 2

---

#### XmlNodeChangedAction

**Line:** 749166

**Values:**

- `Insert` = 0
- `Remove` = 1
- `Change` = 2

---

#### XmlNodeType

**Line:** 752428

**Values:**

- `None` = 0
- `Element` = 1
- `Attribute` = 2
- `Text` = 3
- `CDATA` = 4
- `EntityReference` = 5
- `Entity` = 6
- `ProcessingInstruction` = 7
- `Comment` = 8
- `Document` = 9
- `DocumentType` = 10
- `DocumentFragment` = 11
- `Notation` = 12
- `Whitespace` = 13
- `SignificantWhitespace` = 14
- `EndElement` = 15
- `EndEntity` = 16
- `XmlDeclaration` = 17

---

#### XmlOutputMethod

**Line:** 747041

**Values:**

- `Xml` = 0
- `Html` = 1
- `Text` = 2
- `AutoDetect` = 3

---

#### XmlReadMode

**Line:** 1089660

**Values:**

- `Auto` = 0
- `ReadSchema` = 1
- `IgnoreSchema` = 2
- `InferSchema` = 3
- `DiffGram` = 4
- `Fragment` = 5
- `InferTypedSchema` = 6

---

#### XmlSchemaContentProcessing

**Line:** 764673

**Values:**

- `None` = 0
- `Skip` = 1
- `Lax` = 2
- `Strict` = 3

---

#### XmlSchemaContentType

**Line:** 764688

**Values:**

- `TextOnly` = 0
- `Empty` = 1
- `ElementOnly` = 2
- `Mixed` = 3

---

#### XmlSchemaDatatypeVariety

**Line:** 757580

**Values:**

- `Atomic` = 0
- `List` = 1
- `Union` = 2

---

#### XmlSchemaDerivationMethod

**Line:** 764809

**Values:**

- `Empty` = 0
- `Substitution` = 1
- `Extension` = 2
- `Restriction` = 4
- `List` = 8
- `Union` = 16
- `All` = 255
- `None` = 256

---

#### XmlSchemaForm

**Line:** 765442

**Values:**

- `None` = 0
- `Qualified` = 1
- `Unqualified` = 2

---

#### XmlSchemaInference

**Line:** 760315

---

#### XmlSchemaUse

**Line:** 767108

**Values:**

- `None` = 0
- `Optional` = 1
- `Prohibited` = 2
- `Required` = 3

---

#### XmlSchemaValidationFlags

**Line:** 767161

**Values:**

- `None` = 0
- `ProcessInlineSchema` = 1
- `ProcessSchemaLocation` = 2
- `ReportValidationWarnings` = 4
- `ProcessIdentityConstraints` = 8
- `AllowXmlAttributes` = 16

---

#### XmlSchemaValidity

**Line:** 767553

**Values:**

- `NotKnown` = 0
- `Valid` = 1
- `Invalid` = 2

---

#### XmlSeverityType

**Line:** 767563

**Values:**

- `Error` = 0
- `Warning` = 1

---

#### XmlSpace

**Line:** 743707

**Values:**

- `None` = 0
- `Default` = 1
- `Preserve` = 2

---

#### XmlTokenizedType

**Line:** 751258

**Values:**

- `CDATA` = 0
- `ID` = 1
- `IDREF` = 2
- `IDREFS` = 3
- `ENTITY` = 4
- `ENTITIES` = 5
- `NMTOKEN` = 6
- `NMTOKENS` = 7
- `NOTATION` = 8
- `ENUMERATION` = 9
- `QName` = 10
- `NCName` = 11
- `None` = 12

---

#### XmlTypeCode

**Line:** 767572

**Values:**

- `None` = 0
- `Item` = 1
- `Node` = 2
- `Document` = 3
- `Element` = 4
- `Attribute` = 5
- `Namespace` = 6
- `ProcessingInstruction` = 7
- `Comment` = 8
- `Text` = 9
- `AnyAtomicType` = 10
- `UntypedAtomic` = 11
- `String` = 12
- `Boolean` = 13
- `Decimal` = 14
- `Float` = 15
- `Double` = 16
- `Duration` = 17
- `DateTime` = 18
- `Time` = 19
- `Date` = 20
- `GYearMonth` = 21
- `GYear` = 22
- `GMonthDay` = 23
- `GDay` = 24
- `GMonth` = 25
- `HexBinary` = 26
- `Base64Binary` = 27
- `AnyUri` = 28
- `QName` = 29
- `Notation` = 30
- `NormalizedString` = 31
- `Token` = 32
- `Language` = 33
- `NmToken` = 34
- `Name` = 35
- `NCName` = 36
- `Id` = 37
- `Idref` = 38
- `Entity` = 39
- `Integer` = 40
- `NonPositiveInteger` = 41
- `NegativeInteger` = 42
- `Long` = 43
- `Int` = 44
- `Short` = 45
- `Byte` = 46
- `NonNegativeInteger` = 47
- `UnsignedLong` = 48
- `UnsignedInt` = 49
- `UnsignedShort` = 50
- `UnsignedByte` = 51
- `PositiveInteger` = 52
- `YearMonthDuration` = 53
- `DayTimeDuration` = 54

---

#### XmlWriteMode

**Line:** 1089804

**Values:**

- `WriteSchema` = 0
- `IgnoreSchema` = 1
- `DiffGram` = 2

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

## Pets & Mounts

### Classes (150)

#### AmountComponent

**Line:** 729427

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### AmountDisplayedComponent

**Line:** 711648

**Inherits:** IComponent

**Fields:**

- `Value`: long

---

#### AmountEventSystem

**Line:** 701012

**Inherits:** ReactiveSystem

---

#### AmountListenerComponent

**Line:** 699102

**Inherits:** IComponent

**Fields:**

- `value`: List<IAmountListener>

---

#### AnyAmountDisplayedEventSystem

**Line:** 701033

**Inherits:** ReactiveSystem

---

#### AnyAmountDisplayedListenerComponent

**Line:** 699115

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyAmountDisplayedListener>

---

#### AssignedEggComponent

**Line:** 725303

**Inherits:** IComponent

**Fields:**

- `Value`: GameEntityRef

---

#### AssignedEggEventSystem

**Line:** 701556

**Inherits:** ReactiveSystem

---

#### AssignedEggListenerComponent

**Line:** 699414

**Inherits:** IComponent

**Fields:**

- `value`: List<IAssignedEggListener>

---

#### AssignedEggRemovedEventSystem

**Line:** 701577

**Inherits:** ReactiveSystem

---

#### AssignedEggRemovedListenerComponent

**Line:** 699427

**Inherits:** IComponent

**Fields:**

- `value`: List<IAssignedEggRemovedListener>

---

#### AssociatedMetadataTypeTypeDescriptionProvider

**Line:** 1508653

**Inherits:** TypeDescriptionProvider

---

#### CanStartHatchingEggRedDotUiView

**Line:** 725614

**Inherits:** RedDotUiView

---

#### EggClaimableRedDotUiView

**Line:** 725632

**Inherits:** RedDotUiView

---

#### EggConfig

**Line:** 1071565

**Inherits:** IGameConfigData

---

#### EggDetailsUiView

**Line:** 725650

**Inherits:** UiUnityView

**Fields:**

- `EggRarityText`: TMP_Text
- `DescriptionText`: TMP_Text
- `SlotsFullTextGameObject`: GameObject
- `HatchButton`: BeveledUnityButton
- `_egg`: GameEntity

---

#### EggDungeonBattleLibrary

**Line:** 1061275

**Inherits:** DungeonBattleLibrary

---

#### EggEquippedToHatchSlotMessage

**Line:** 723575

**Inherits:** IMessage

---

#### EggFeature

**Line:** 725363

**Inherits:** Feature

---

#### EggHatchClaimSystem

**Line:** 725372

**Inherits:** ReactiveSystem

---

#### EggHatchClaimUiView

**Line:** 725681

**Inherits:** UiUnityView

**Fields:**

- `ClaimButton`: UnityButton
- `_node`: GameEntity

---

#### EggHatchDetailsOpenView

**Line:** 725709

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### EggHatchGemSkipSystem

**Line:** 725393

**Inherits:** ReactiveSystem

---

#### EggHatchPurchaseButtonUiView

**Line:** 725727

**Inherits:** UiUnityView

**Fields:**

- `PriceButtonView`: PriceButtonEntitasUiView

---

#### EggHatchPushNotificationSystem

**Line:** 725435

**Inherits:** ReactiveSystem

---

#### EggHatchSkipUiVIew

**Line:** 725745

**Inherits:** UiUnityView

**Fields:**

- `GemSkipButton`: PriceButtonEntitasUiView
- `_egg`: GameEntity

---

#### EggHatchSlotComponent

**Line:** 725326

**Inherits:** IComponent

---

#### EggHatchSlotPurchaseSystem

**Line:** 725456

**Inherits:** ReactiveSystem

---

#### EggHatchSlotPurchasedMessage

**Line:** 723602

**Inherits:** IMessage

---

#### EggHatchSlotUiComponent

**Line:** 725336

**Inherits:** IComponent

---

#### EggHatchSlotUiCreateSystem

**Line:** 725509

**Inherits:** ReactiveSystem

---

#### EggHatchSlotUiRemoveSystem

**Line:** 725530

**Inherits:** ReactiveSystem

---

#### EggHatchSlotUiUpdateOnHatchSystem

**Line:** 725551

**Inherits:** ReactiveSystem

---

#### EggHatchSlotUiUpdateOnPurchaseSlotSystem

**Line:** 725572

**Inherits:** ReactiveSystem

---

#### EggHatchSlotUiView

**Line:** 725770

**Inherits:** UiUnityView

**Fields:**

- `EggIcon`: Image
- `HatchText`: TMP_Text
- `Button`: UnityButton
- `LampCone`: Image
- `LampIcon`: Image
- `LampOn`: Sprite
- `LampOff`: Sprite
- `_egg`: GameEntityRef
- `EggClaimableRedDotUiView`: EggClaimableRedDotUiView
- `CanStartHatchingEggRedDotUiView`: CanStartHatchingEggRedDotUiView

---

#### EggHatchTimerUiView

**Line:** 725815

**Inherits:** UiUnityView

**Fields:**

- `TimerText`: TMP_Text
- `ProgressBar`: Image
- `_egg`: GameEntity
- `TimerParent`: GameObject

---

#### EggHideOnHatchingUiView

**Line:** 725845

**Inherits:** UiUnityView

**Fields:**

- `_egg`: GameEntity

---

#### EggIconUiView

**Line:** 725869

**Inherits:** UiUnityView

**Fields:**

- `EggIcon`: Image

---

#### EggReactiveModel

**Line:** 723750

**Inherits:** ReactiveModel

---

#### EggStatTarget

**Line:** 1077108

**Inherits:** StatTargetBase

---

#### EggUiSyncSystem

**Line:** 725593

**Inherits:** ReactiveSystem

---

#### HatchedPetInfo

**Line:** 1051840

---

#### InGamePetComponent

**Line:** 723409

**Inherits:** IComponent

---

#### LootAmounts

**Line:** 1057550

**Fields:**

- `Coins`: int
- `Hammers`: int

---

#### MaxAmountComponent

**Line:** 729440

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### MaxAmountEventSystem

**Line:** 702295

**Inherits:** ReactiveSystem

---

#### MaxAmountListenerComponent

**Line:** 699869

**Inherits:** IComponent

**Fields:**

- `value`: List<IMaxAmountListener>

---

#### MountCheatContainer

**Line:** 722128

**Inherits:** AbstractCheatContainer

---

#### MountCheatSystem

**Line:** 686625

**Inherits:** CheatSystem

---

#### MountCollectionEntryUiVisual

**Line:** 722276

**Inherits:** MonoBehaviour

**Fields:**

- `MountUiVisual`: MountUiVisual
- `MountEquippedVisual`: MountEquippedVisual
- `Button`: UnityButton

---

#### MountCollectionUiView

**Line:** 722353

**Inherits:** MonoBehaviour

**Fields:**

- `GridParent`: Transform
- `MountCollectionEntryUiPrefab`: MountCollectionEntryUiVisual
- `SummonLabel`: TMP_Text

---

#### MountCollectionVisualConfig

**Line:** 722175

**Inherits:** ScriptableObject

**Fields:**

- `SheetConnection`: GoogleSheetConnection
- `MountsLibrarySheetName`: string
- `MountAnimationView`: SummonEntryAnimationView

---

#### MountCollider

**Line:** 722833

**Inherits:** MonoBehaviour

**Fields:**

- `Radius`: float

---

#### MountDetailsUiView

**Line:** 722377

**Inherits:** UiUnityView

**Fields:**

- `MountUiVisual`: MountUiVisual
- `MountEquippedVisual`: MountEquippedVisual
- `MountName`: TMP_Text
- `MountDescription`: TMP_Text
- `EquipButtonText`: TMP_Text
- `EquipButton`: UnityButton
- `EquipButtonImage`: Image
- `UpgradeButton`: UnityButton
- `_mount`: PlayerMountModel

---

#### MountEquipAction

**Line:** 1070152

**Inherits:** PlayerAction

---

#### MountEquippedVisual

**Line:** 722412

**Inherits:** MonoBehaviour

**Fields:**

- `Equipped`: GameObject
- `CanvasGroup`: CanvasGroup

---

#### MountId

**Line:** 1070431

**Inherits:** IEquatable

---

#### MountInventorySlotUiView

**Line:** 722449

**Inherits:** UiUnityView

**Fields:**

- `Target`: GameObject
- `Icon`: Image
- `Background`: Image
- `LevelText`: TMP_Text
- `_lastMountCount`: int
- `_currentMount`: PlayerMountModel

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

- `MountUiVisual`: MountUiVisual
- `MountEquippedVisual`: MountEquippedVisual
- `Button`: UnityButton
- `SelectedMark`: GameObject
- `IconCanvasGroup`: CanvasGroup
- `Mount`: PlayerMountModel

---

#### MountMergeUiView

**Line:** 722606

**Inherits:** UiUnityView

**Fields:**

- `MountExperience`: TMP_Text
- `MountLevel`: TMP_Text
- `Title`: TMP_Text
- `Description`: TMP_Text
- `NumberOfMountsSelected`: TMP_Text
- `CurrentSlider`: Slider
- `TargetSlider`: Slider
- `MountMergeEntryUiPrefab`: MountMergeEntryUiVisual
- `MountParent`: Transform
- `Icon`: Image
- `Background`: Image
- `MergeButton`: UnityButton
- `MergeButtonImage`: Image
- `MountEquippedVisual`: MountEquippedVisual
- `_upgradeLibrary`: MountUpgradeLibrary
- `_maxLevel`: int
- `_currentTweenTotalXp`: int
- `_sequence`: Sequence
- `_mount`: PlayerMountModel

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

- `Icon`: Image
- `Level`: TMP_Text
- `Background`: Image

---

#### MountUnEquipAction

**Line:** 1070396

**Inherits:** PlayerAction

---

#### MountView

**Line:** 722848

**Inherits:** MonoBehaviour

**Fields:**

- `UnitAnchor`: Transform
- `Collider`: MountCollider

---

#### MountVisualConfig

**Line:** 722210

**Fields:**

- `Icon`: Sprite
- `Prefab`: MountView
- `MountName`: string

---

#### MountsRedDotLogic

**Line:** 722252

**Inherits:** IRedDotLogic

---

#### NativeSetClassTypeToNullOnScheduleAttribute

**Line:** 864266

**Inherits:** Attribute

---

#### OpenEggPanelOnEmptySlotButtonUiView

**Line:** 725905

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

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

#### PetCheatSystem

**Line:** 686640

**Inherits:** CheatSystem

---

#### PetCollectionReactiveModel

**Line:** 723887

**Inherits:** ReactiveModel

---

#### PetCollectionUiCreateSystem

**Line:** 724159

**Inherits:** ReactiveSystem

---

#### PetCollectionUiView

**Line:** 724724

**Inherits:** UiUnityView

**Fields:**

- `PetParent`: Transform

---

#### PetCollectionVisualConfig

**Line:** 723526

**Inherits:** ScriptableObject

**Fields:**

- `PetAnimationView`: SummonEntryAnimationView
- `EggAnimationView`: SummonEntryAnimationView

---

#### PetComponent

**Line:** 723429

**Inherits:** IComponent

---

#### PetConfig

**Line:** 1071746

**Inherits:** IGameConfigData

---

#### PetCreateOnEquipSystem

**Line:** 724180

**Inherits:** ReactiveSystem

---

#### PetCreateOnPlayerCreateSystem

**Line:** 724201

**Inherits:** ReactiveSystem

---

#### PetDestroyOnPlayerDestroySystem

**Line:** 724225

**Inherits:** ReactiveSystem

---

#### PetDestroyOnUnEquipSystem

**Line:** 724262

**Inherits:** ReactiveSystem

---

#### PetDetailsOpenButtonUiView

**Line:** 724739

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### PetDetailsUiView

**Line:** 724757

**Inherits:** UiUnityView

**Fields:**

- `Title`: TMP_Text
- `Description`: TMP_Text

---

#### PetDungeonKeysChangeMessage

**Line:** 712675

**Inherits:** DungeonKeysChangeMessage

---

#### PetEggCheatAction

**Line:** 1071090

**Inherits:** PlayerAction

---

#### PetEggComponent

**Line:** 725345

**Inherits:** IComponent

---

#### PetEggHatchClaimAction

**Line:** 1071252

**Inherits:** PlayerAction

---

#### PetEggHatchGemSkipAction

**Line:** 1071180

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

#### PetEquipButtonUiView

**Line:** 724773

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton
- `EquipText`: TMP_Text
- `ButtonImage`: Image
- `_pet`: GameEntity

---

#### PetEquipUiView

**Line:** 724806

**Inherits:** UiUnityView

**Fields:**

- `EquipIcon`: GameObject
- `IconCanvasGroup`: CanvasGroup
- `_pet`: GameEntity

---

#### PetEquippedMessage

**Line:** 723642

**Inherits:** IMessage

---

#### PetFeature

**Line:** 724009

**Inherits:** Feature

---

#### PetFeatureInitializeSystem

**Line:** 724283

**Inherits:** IInitializeSystem

---

#### PetHatchedMessage

**Line:** 723669

**Inherits:** IMessage

---

#### PetIconUiView

**Line:** 724835

**Inherits:** UiUnityView

**Fields:**

- `PetIcon`: Image
- `Background`: Image

---

#### PetId

**Line:** 1071788

**Inherits:** IEquatable

---

#### PetIdComponent

**Line:** 723438

**Inherits:** IComponent

**Fields:**

- `Value`: PetId

---

#### PetMergeAction

**Line:** 1071368

**Inherits:** PlayerAction

---

#### PetMergeButtonUiView

**Line:** 724913

**Inherits:** UiUnityView

**Fields:**

- `MergeButton`: BeveledUnityButton
- `_pet`: GameEntity

---

#### PetMergeEntriesCreateSystem

**Line:** 724352

**Inherits:** ReactiveSystem

---

#### PetMergeOpenUiView

**Line:** 724944

**Inherits:** UiUnityView

**Fields:**

- `OpenButton`: UnityButton

---

#### PetMergePossibleReactiveSystem

**Line:** 724373

**Inherits:** ReactiveSystem

---

#### PetMergeReactiveSystem

**Line:** 724395

**Inherits:** ReactiveSystem

---

#### PetMergeUiView

**Line:** 724982

**Inherits:** UiUnityView

**Fields:**

- `PetExperience`: TMP_Text
- `PetLevel`: TMP_Text
- `Title`: TMP_Text
- `Description`: TMP_Text
- `NumberOfPetsSelected`: TMP_Text
- `CurrentSlider`: Slider
- `TargetSlider`: Slider
- `PetParent`: Transform
- `_pet`: GameEntity
- `_upgradeLibrary`: PetUpgradeConfig
- `_maxLevel`: int
- `_currentTweenTotalXp`: int
- `_sequence`: Sequence

---

#### PetMovement

**Line:** 725233

**Inherits:** MonoBehaviour

**Fields:**

- `FollowAnchor`: Transform
- `Pet`: Transform
- `_timer`: float
- `_dist`: float
- `_targetPos`: Vector2
- `MinSpeed`: float
- `MaxSpeed`: float
- `MovementRadius`: float
- `_yOffset`: float

---

#### PetMovementBehaviour

**Line:** 725260

**Inherits:** MonoBehaviour

**Fields:**

- `Body`: Transform
- `MinSpeed`: float
- `MaxSpeed`: float
- `HopLenght`: float
- `HopHeight`: float
- `MaxAngle`: float
- `StretchAmount`: float
- `_timer`: float
- `_anchorPos`: Vector2
- `_targetPos`: Vector2
- `_position`: Vector2
- `_dist`: float
- `_moveMulti`: float

---

#### PetQuickEquipUiView

**Line:** 725062

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton

---

#### PetReactiveModel

**Line:** 723927

**Inherits:** ReactiveModel

---

#### PetReactiveModelComponent

**Line:** 723465

**Inherits:** IComponent

**Fields:**

- `Value`: PetCollectionReactiveModel

---

#### PetReactiveModelExecuteSystem

**Line:** 724416

**Inherits:** IExecuteSystem

---

#### PetReactiveModelInitializeSystem

**Line:** 724512

**Inherits:** IInitializeSystem

---

#### PetSelectUiView

**Line:** 725080

**Inherits:** UiUnityView

**Fields:**

- `Button`: UnityButton
- `_pet`: GameEntity
- `IconCanvasGroup`: CanvasGroup
- `CheckMark`: GameObject

---

#### PetSlotComponent

**Line:** 723477

**Inherits:** IComponent

---

#### PetSlotParentsUiView

**Line:** 725104

**Inherits:** UiUnityView

**Fields:**

- `EggHatchSlotParent`: Transform
- `PetSlotParent`: Transform

---

#### PetSlotUiComponent

**Line:** 723487

**Inherits:** IComponent

---

#### PetSlotUiCreateSystem

**Line:** 724571

**Inherits:** ReactiveSystem

---

#### PetSlotUiUpdateSystem

**Line:** 724611

**Inherits:** ReactiveSystem

---

#### PetSlotUiView

**Line:** 725120

**Inherits:** UiUnityView

**Fields:**

- `PetParent`: Transform
- `LockIcon`: GameObject
- `LockedButton`: UnityButton
- `_slot`: GameEntity

---

#### PetSlotUnlockUpdateSystem

**Line:** 724632

**Inherits:** ReactiveSystem

---

#### PetSortSystem

**Line:** 724682

**Inherits:** ReactiveSystem

---

#### PetStatTarget

**Line:** 1077306

**Inherits:** StatTargetBase

---

#### PetStats

**Line:** 1071933

---

#### PetUiSyncSystem

**Line:** 724703

**Inherits:** ReactiveSystem

---

#### PetUnEquipAction

**Line:** 1071425

**Inherits:** PlayerAction

---

#### PetUnequippedMessage

**Line:** 723689

**Inherits:** IMessage

---

#### PetUnselectSystem

**Line:** 724298

**Inherits:** ReactiveSystem

---

#### PetView

**Line:** 725183

**Inherits:** GameUnityView

**Fields:**

- `_visual`: PetVisual

---

#### PetVisual

**Line:** 725204

**Inherits:** MonoBehaviour

**Fields:**

- `_offset`: Vector2
- `PetMovement`: PetMovementBehaviour

---

#### PetVisualConfig

**Line:** 723557

**Fields:**

- `PetIcon`: Sprite
- `PetPrefab`: PetVisual
- `PetName`: string

---

#### PetsLocalizer

**Line:** 721280

**Inherits:** LocalizerBase

---

#### PetsQuickEquipRedDotUiView

**Line:** 725153

**Inherits:** RedDotUiView

---

#### PetsRedDotLogic

**Line:** 724063

**Inherits:** IRedDotLogic

**Fields:**

- `_stillLockedPetSlotsCount`: int
- `_alreadyMarkedClaimableHatchSlotsIds`: HashSet<int>

---

#### PetsTabRedDotUiView

**Line:** 725168

**Inherits:** RedDotUiView

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

#### PlayerPetModelComponent

**Line:** 723496

**Inherits:** IComponent

**Fields:**

- `Value`: PlayerPetModel

---

#### PurchaseEggHatchSlotComponent

**Line:** 725354

**Inherits:** IComponent

---

#### SecondaryStatPetUnlockLibrary

**Line:** 1071974

**Inherits:** IGameConfigData

---

#### UnitMountView

**Line:** 722883

**Inherits:** GameUnityView

**Fields:**

- `CharacterRig`: Transform
- `Shadow`: GameObject
- `UnitVisual`: UnitEquipmentVisual
- `UnitNameView`: UnitNameView
- `_currentMount`: MountId
- `_mount`: MountView
- `_sign`: int

---

### Enums (3)

#### PetBalancingType

**Line:** 1071661

**Values:**

- `Balanced` = 0
- `Damage` = 1
- `Health` = 2

---

#### PetMovement

**Line:** 725224

---

#### PhysicsShapeType2D

**Line:** 1578338

**Values:**

- `Circle` = 0
- `Capsule` = 1
- `Polygon` = 2
- `Edges` = 3

---

## Progression

### Classes (77)

#### AdTechProvider

**Line:** 1565002

**Fields:**

- `id`: int
- `name`: string
- `privacyPolicyUrl`: string
- `consent`: bool

---

#### CompositeChangeToken

**Line:** 1559257

**Inherits:** IChangeToken

**Fields:**

- `_cancellationTokenSource`: CancellationTokenSource
- `_disposables`: List<IDisposable>

---

#### CreateChatRoomRequest

**Line:** 1527451

**Inherits:** IEquatable

---

#### EntityConnectionCancelUpgradeRequest

**Line:** 554048

**Inherits:** MetaMessage

---

#### EntityConnectionCancelUpgradeResponse

**Line:** 554058

**Inherits:** MetaMessage

---

#### EntityConnectionUpgradeFlush

**Line:** 553981

**Inherits:** MetaMessage

---

#### EntityConnectionUpgradeRequest

**Line:** 553843

**Inherits:** MetaMessage

---

#### EntityConnectionUpgradeResponse

**Line:** 553896

**Inherits:** MetaMessage

---

#### ExperienceComponent

**Line:** 723397

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### ExperienceEventSystem

**Line:** 701936

**Inherits:** ReactiveSystem

---

#### ExperienceListenerComponent

**Line:** 699648

**Inherits:** IComponent

**Fields:**

- `value`: List<IExperienceListener>

---

#### GameConfigTopLevelDeduplicationStorage

**Line:** 596809

---

#### IapTechnicalClaimMessage

**Line:** 729788

**Inherits:** IMessage

---

#### ItemCreateCheatAction

**Line:** 1068692

**Inherits:** PlayerAction

---

#### ItemLevelBracketsConfig

**Line:** 1067703

**Inherits:** IGameConfigData

---

#### LevelComponent

**Line:** 713588

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### LevelEventSystem

**Line:** 702232

**Inherits:** ReactiveSystem

---

#### LevelListenerComponent

**Line:** 699830

**Inherits:** IComponent

**Fields:**

- `value`: List<ILevelListener>

---

#### LogLevelOverrideSpec

**Line:** 577101

**Fields:**

- `ChannelName`: string
- `LogLevel`: LogLevel

---

#### MaxLevelComponent

**Line:** 713600

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### MetaLogLevelSwitch

**Line:** 519903

**Fields:**

- `_minimumLevel`: LogLevel

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

#### PetLevelUiView

**Line:** 724851

**Inherits:** UiUnityView

**Fields:**

- `Level`: TMP_Text

---

#### PetMergeExperienceComponent

**Line:** 723451

**Inherits:** IComponent

**Fields:**

- `TargetLevel`: int
- `TargetExperience`: int

---

#### PetMergeExperienceEventSystem

**Line:** 702463

**Inherits:** ReactiveSystem

---

#### PetMergeExperienceListenerComponent

**Line:** 699973

**Inherits:** IComponent

**Fields:**

- `value`: List<IPetMergeExperienceListener>

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

#### PlayerTechTreeModel

**Line:** 1078033

---

#### ReactiveUpgradeTimer

**Line:** 695152

**Inherits:** IDisposable

---

#### SpriteCharacter

**Line:** 1348182

**Inherits:** TextElement

**Fields:**

- `m_Name`: string

---

#### SwitchLevelAttribute

**Line:** 777453

**Inherits:** Attribute

**Fields:**

- `type`: Type

---

#### TMP_SpriteCharacter

**Line:** 1226450

**Inherits:** TMP_TextElement

**Fields:**

- `m_Name`: string

---

#### TechNodeClaimableRedDotUiView

**Line:** 735421

**Inherits:** RedDotUiView

---

#### TechNodeUpgradeStartedMessage

**Line:** 735203

**Inherits:** IMessage

---

#### TechPotionsChangeMessage

**Line:** 711813

**Inherits:** CurrencyChangeMessage

---

#### TechTreeCategoryRedDotUiView

**Line:** 735439

**Inherits:** RedDotUiView

---

#### TechTreeCategoryUiView

**Line:** 735495

**Inherits:** MonoBehaviour

**Fields:**

- `CategoryIcon`: Image
- `CategoryName`: TMP_Text
- `Button`: UnityButton
- `CompletionText`: TMP_Text
- `TechTreeCategoryRedDotUiView`: TechTreeCategoryRedDotUiView
- `_techTreeType`: TechTreeType

---

#### TechTreeCategoryVisualConfig

**Line:** 735190

**Fields:**

- `Icon`: Sprite
- `TitleLocaKey`: string

---

#### TechTreeCheatContainer

**Line:** 686417

**Inherits:** AbstractCheatContainer

---

#### TechTreeCheatSystem

**Line:** 686706

**Inherits:** CheatSystem

---

#### TechTreeFeature

**Line:** 735330

**Inherits:** Feature

---

#### TechTreeFeatureInitializeSystem

**Line:** 735273

**Inherits:** IInitializeSystem

---

#### TechTreeLibrary

**Line:** 1077642

**Inherits:** IGameConfigData

---

#### TechTreeLocalizer

**Line:** 721407

**Inherits:** LocalizerBase

---

#### TechTreeMaxCheatAction

**Line:** 1077525

**Inherits:** PlayerAction

---

#### TechTreeNodeClaimedMessage

**Line:** 735238

**Inherits:** IMessage

---

#### TechTreeNodeDetailsView

**Line:** 735518

**Inherits:** MonoBehaviour

**Fields:**

- `Title`: TMP_Text
- `Description`: TMP_Text
- `Level`: TMP_Text
- `OtherResearchInProgressLabel`: TMP_Text
- `NodeBackground`: Image
- `NodeIcon`: Image
- `UpgradeTimerView`: UpgradeTimerView
- `ClaimButton`: UnityButton
- `UpgradeButton`: UnityButton
- `UpgradeCostLabel`: TMP_Text
- `UpgradeDurationLabel`: TMP_Text
- `UpgradeButtonImage`: Image
- `SkipButton`: UnityButton
- `_techTreeType`: TechTreeType
- `_nodeIndex`: int
- `_type`: TechTreeNodeType
- `_maxLevel`: int

---

#### TechTreeNodeInfo

**Line:** 1077822

---

#### TechTreeNodeModel

**Line:** 1078077

**Fields:**

- `Level`: int

---

#### TechTreeNodePushNotificationSystem

**Line:** 735309

**Inherits:** ReactiveSystem

---

#### TechTreeNodeUiView

**Line:** 735562

**Inherits:** MonoBehaviour

**Fields:**

- `NodeIcon`: Image
- `NodeBackground`: Image
- `Button`: UnityButton
- `TimerUiView`: TimerUiView
- `TechNodeClaimableRedDotUiView`: TechNodeClaimableRedDotUiView
- `Level`: TMP_Text
- `_maxLevel`: int
- `_techTreeType`: TechTreeType
- `_nodeIndex`: int

---

#### TechTreeNodeUpgradeClaimAction

**Line:** 1077538

**Inherits:** PlayerAction

---

#### TechTreeNodeUpgradeGemSkipAction

**Line:** 1077580

**Inherits:** PlayerAction

---

#### TechTreeNodeUpgradeStartAction

**Line:** 1077622

**Inherits:** PlayerAction

**Fields:**

- `TechTreeType`: TechTreeType
- `NodeId`: int

---

#### TechTreeNodeVisualConfig

**Line:** 735177

**Fields:**

- `Icon`: Sprite

---

#### TechTreePositionLibrary

**Line:** 1077780

**Inherits:** IGameConfigData

---

#### TechTreeRedDot

**Line:** 695257

**Inherits:** IRedDotEntryDatum

---

#### TechTreeRedDotLogic

**Line:** 735361

**Inherits:** IRedDotLogic

**Fields:**

- `_nodesInProgress`: bool

---

#### TechTreeStatContribution

**Line:** 1077696

**Inherits:** StatContribution

---

#### TechTreeStatTarget

**Line:** 1077347

**Inherits:** StatTargetBase

---

#### TechTreeTabRedDotUiView

**Line:** 735597

**Inherits:** RedDotUiView

---

#### TechTreeTabUiView

**Line:** 735612

**Inherits:** MonoBehaviour

**Fields:**

- `ContentParent`: RectTransform
- `TechTreeParent`: RectTransform

---

#### TechTreeUiView

**Line:** 735668

**Inherits:** PopupUiView

**Fields:**

- `ContentParent`: RectTransform
- `TitleText`: TMP_Text
- `TreeProgressText`: TMP_Text
- `ScrollRect`: ScrollRect
- `ScrollSpeed`: float
- `Parent`: RectTransform
- `ConnectionsParent`: RectTransform
- `ConnectorPrefab`: TreeConnector

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

- `Nodes`: SerializableDictionary<TechTreeNodeType, TechTreeNodeVisualConfig>
- `XSpacing`: float
- `YSpacing`: float
- `YTopPadding`: float
- `YBottomPadding`: float
- `Categories`: SerializableDictionary<TechTreeType, TechTreeCategoryVisualConfig>

---

#### UpdateChartSpecRequest

**Line:** 1400233

**Inherits:** IDirectResponseSchema

---

#### UpdateChatRoomSettingsRequest

**Line:** 1527538

**Inherits:** IEquatable

---

#### UpgradeTimerView

**Line:** 735751

**Inherits:** MonoBehaviour

**Fields:**

- `ClaimButton`: UnityButton
- `SkipButton`: UnityButton
- `SkipButtonImage`: Image
- `SkipCostLabel`: TMP_Text
- `TimerText`: TMP_Text
- `TimerParent`: GameObject
- `ProgressBar`: Image
- `_skipActionReference`: PlayerAction
- `_claimActionReference`: PlayerAction
- `_remainingSeconds`: int
- `_state`: TimerState

---

### Enums (21)

#### AlertLevel

**Line:** 1448518

**Values:**

- `Warning` = 1
- `Fatal` = 2

---

#### AuthenticationLevel

**Line:** 802758

**Values:**

- `None` = 0
- `MutualAuthRequested` = 1
- `MutualAuthRequired` = 2

---

#### BindingLogLevel

**Line:** 608859

**Values:**

- `None` = 0
- `Once` = 1
- `All` = 2

---

#### CompressionLevel

**Line:** 789375

**Values:**

- `Optimal` = 0
- `Fastest` = 1
- `NoCompression` = 2

---

#### ConformanceLevel

**Line:** 740774

**Values:**

- `Auto` = 0
- `Fragment` = 1
- `Document` = 2

---

#### DirectConnectionUpgradeRefuseReason

**Line:** 553883

**Values:**

- `Unknown` = 0
- `DisabledInEntitySettings` = 1
- `DisabledInServerSettings` = 2
- `NoPublicIpOnServer` = 3
- `ServerFailedToOpenPort` = 4

---

#### EventLevel

**Line:** 275506

**Values:**

- `LogAlways` = 0
- `Critical` = 1
- `Error` = 2
- `Warning` = 3
- `Informational` = 4
- `Verbose` = 5

---

#### GameConfigLogLevel

**Line:** 595222

**Values:**

- `NotSet` = 0
- `Verbose` = 1
- `Debug` = 2
- `Information` = 3
- `Warning` = 4
- `Error` = 5

---

#### IPProtectionLevel

**Line:** 800364

**Values:**

- `Unrestricted` = 10
- `EdgeRestricted` = 20
- `Restricted` = 30

---

#### LogLevel

**Line:** 1596433

**Values:**

- `On` = 0
- `Trace` = 1
- `Debug` = 2
- `Info` = 3
- `Warn` = 4
- `Error` = 5
- `Fatal` = 6
- `Off` = 7

---

#### NtlmAuthLevel

**Line:** 1448356

**Values:**

- `LM_and_NTLM` = 0
- `LM_and_NTLM_and_try_NTLMv2_Session` = 1
- `NTLM_only` = 2
- `NTLMv2_only` = 3

---

#### PipelineDebugLevel

**Line:** 900532

**Values:**

- `Disabled` = 0
- `Profiling` = 1

---

#### RequestCacheLevel

**Line:** 799177

**Values:**

- `Default` = 0
- `BypassCache` = 1
- `CacheOnly` = 2
- `CacheIfAvailable` = 3
- `Revalidate` = 4
- `Reload` = 5
- `NoCacheNoStore` = 6

---

#### ShaderVariantLogLevel

**Line:** 905767

**Values:**

- `Disabled` = 0
- `OnlyUniversalRPShaders` = 1
- `AllShaders` = 2

---

#### SocketOptionLevel

**Line:** 800533

**Values:**

- `Socket` = 65535
- `IP` = 0
- `IPv6` = 41
- `Tcp` = 6
- `Udp` = 17

---

#### TechTreeNodeType

**Line:** 1077725

**Values:**

- `WeaponBonus` = 0
- `HelmetBonus` = 1
- `BodyBonus` = 2
- `ShoeBonus` = 3
- `GloveBonus` = 4
- `BeltBonus` = 5
- `NecklaceBonus` = 6
- `RingBonus` = 7
- `WeaponLevelUp` = 8
- `HelmetLevelUp` = 9
- `BodyLevelUp` = 10
- `ShoeLevelUp` = 11
- `GloveLevelUp` = 12
- `BeltLevelUp` = 13
- `NecklaceLevelUp` = 14
- `RingLevelUp` = 15
- `MountDamage` = 16
- `MountHealth` = 17
- `ExtraMountChance` = 18
- `MountSummonCost` = 19
- `ForgeTimerSpeed` = 20
- `ForgeUpgradeCost` = 21
- `EquipmentSellPrice` = 22
- `AutoForge` = 23
- `HammerOfflineReward` = 24
- `CoinOfflineReward` = 25
- `MaxOfflineReward` = 26
- `FreeForgeChance` = 27
- `HammerThiefHammerReward` = 28
- `HammerThiefCoinReward` = 29
- `SkillDamage` = 30
- `SkillPassiveDamage` = 31
- `SkillPassiveHealth` = 32
- `GhostTownSkillBonus` = 33
- `SkillSummonCost` = 34
- `PetBonusDamage` = 35
- `PetBonusHealth` = 36
- `ExtraEggChance` = 37
- `CommonEggTimer` = 38
- `RareEggTimer` = 39
- `EpicEggTimer` = 40
- `LegendaryEggTimer` = 41
- `UltimateEggTimer` = 42
- `MythicEggTimer` = 43
- `ZombieRushTechPotions` = 44
- `TechNodeUpgradeCost` = 45
- `TechResearchTimer` = 46

---

#### TechTreeType

**Line:** 1077896

**Values:**

- `Forge` = 0
- `Power` = 1
- `SkillsPetTech` = 2

---

#### TokenImpersonationLevel

**Line:** 220353

**Values:**

- `None` = 0
- `Anonymous` = 1
- `Identification` = 2
- `Impersonation` = 3
- `Delegation` = 4

---

#### TraceLevel

**Line:** 777618

**Values:**

- `Off` = 0
- `Error` = 1
- `Warning` = 2
- `Info` = 3
- `Verbose` = 4

---

#### TypeFilterLevel

**Line:** 226403

**Values:**

- `Low` = 2
- `Full` = 3

---

#### UsercentricsLoggerLevel

**Line:** 1564431

**Values:**

- `None` = 0
- `Error` = 1
- `Warning` = 2
- `Debug` = 3

---

## PvE Content

### Classes (117)

#### AnyBattleLootEventSystem

**Line:** 701079

**Inherits:** ReactiveSystem

---

#### AnyBattleLootListenerComponent

**Line:** 699141

**Inherits:** IComponent

**Fields:**

- `value`: List<IAnyBattleLootListener>

---

#### BattleCheatContainer

**Line:** 685896

**Inherits:** AbstractCheatContainer

---

#### BattleCheatSystem

**Line:** 686518

**Inherits:** CheatSystem

---

#### BattleClientCheatSystem

**Line:** 686536

**Inherits:** CheatSystem

---

#### BattleId

**Line:** 1059348

**Inherits:** IEquatable

---

#### BattleIdxComponent

**Line:** 710021

**Inherits:** IComponent

**Fields:**

- `Value`: int

---

#### BattleLogUiView

**Line:** 719526

**Inherits:** MonoBehaviour

**Fields:**

- `LogContainer`: RectTransform
- `LogEntryPrefab`: LogEntryUiView
- `ScrollRect`: ScrollRect
- `ScrollSpeed`: float
- `_warManager`: GuildWarManager

---

#### BattleLootComponent

**Line:** 710034

**Inherits:** IComponent

---

#### BattleModeComponent

**Line:** 708471

**Inherits:** IComponent

**Fields:**

- `Value`: BattleMode

---

#### BattleModeFeature

**Line:** 708461

**Inherits:** Feature

---

#### BattleModeInitializeSystem

**Line:** 708881

**Inherits:** IInitializeSystem

---

#### BattleModeSyncSystem

**Line:** 708899

**Inherits:** IExecuteSystem

---

#### BattleNormalSpeedCheatAction

**Line:** 1056805

**Inherits:** PlayerAction

---

#### BattleSpeedUpCheatAction

**Line:** 1056791

**Inherits:** PlayerAction

---

#### BattleStartUiView

**Line:** 710255

**Inherits:** UiUnityView

**Fields:**

- `_battleLabel`: TMP_Text
- `_content`: Transform
- `_cg`: CanvasGroup
- `_sequence`: Sequence

---

#### BattleStateComponent

**Line:** 710044

**Inherits:** IComponent

**Fields:**

- `Value`: BattleState

---

#### BattleStateEventSystem

**Line:** 701663

**Inherits:** ReactiveSystem

---

#### BattleStateListenerComponent

**Line:** 699479

**Inherits:** IComponent

**Fields:**

- `value`: List<IBattleStateListener>

---

#### BattleUiParentView

**Line:** 721672

**Inherits:** UiUnityView

**Fields:**

- `Parent`: Transform

---

#### BattlesFeature

**Line:** 710000

**Inherits:** Feature

---

#### ChangeBattleCheatAction

**Line:** 1056342

**Inherits:** PlayerAction

---

#### CleanupAndReOpenDungeonTabSystem

**Line:** 713223

**Inherits:** ReactiveSystem

---

#### CleanupDungeonBattleAction

**Line:** 1060793

**Inherits:** PlayerAction

---

#### CurrentDungeonTypeComponent

**Line:** 712439

**Inherits:** IComponent

**Fields:**

- `Value`: DungeonType

---

#### DailyDungeonKeysPushNotesSystem

**Line:** 712753

**Inherits:** ReactiveSystem

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

#### DungeonBattleMapSystem

**Line:** 710383

**Inherits:** ReactiveSystem

---

#### DungeonBattleModelInitSystem

**Line:** 713260

**Inherits:** IInitializeSystem

---

#### DungeonBattleProgressUiView

**Line:** 713400

**Inherits:** UiUnityView

**Fields:**

- `RectTransform`: RectTransform
- `_mainBattleUiEntryPrefab`: MainBattleUiEntry
- `ProgressBar`: Image
- `Parent`: Transform
- `Spacing`: float
- `BattleLabel`: TextMeshProUGUI
- `_entries`: List<MainBattleUiEntry>
- `_sequence`: Sequence
- `_dungeonBattle`: GameEntity

---

#### DungeonBattleReactiveModel

**Line:** 713197

**Inherits:** ReactiveModel

---

#### DungeonBattleReactiveModelComponent

**Line:** 713176

**Inherits:** IComponent

**Fields:**

- `Value`: DungeonBattleReactiveModel

---

#### DungeonBattleStartUiView

**Line:** 713444

**Inherits:** UiUnityView

**Fields:**

- `_levelLabel`: TMP_Text
- `_cg`: CanvasGroup
- `_sequence`: Sequence

---

#### DungeonBattleSyncSystem

**Line:** 713275

**Inherits:** IExecuteSystem

---

#### DungeonBattleSystem

**Line:** 713290

**Inherits:** IExecuteSystem

**Fields:**

- `_timer`: float
- `_state`: BattleState

---

#### DungeonBattleUiReactiveSystem

**Line:** 713317

**Inherits:** ReactiveSystem

---

#### DungeonBattleUiView

**Line:** 713473

**Inherits:** UiUnityView

---

#### DungeonCheatContainer

**Line:** 712422

**Inherits:** AbstractCheatContainer

---

#### DungeonCheatSystem

**Line:** 686590

**Inherits:** CheatSystem

---

#### DungeonComponent

**Line:** 712451

**Inherits:** IComponent

**Fields:**

- `Value`: DungeonType

---

#### DungeonDetailsUiView

**Line:** 712865

**Inherits:** UiUnityView

**Fields:**

- `DungeonTitle`: TMP_Text
- `DungeonBackground`: Image

---

#### DungeonEndUiView

**Line:** 713485

**Inherits:** UiUnityView

**Fields:**

- `Title`: TMP_Text
- `Description`: TMP_Text
- `Button`: UnityButton
- `ButtonText`: TMP_Text
- `RewardText`: TMP_Text
- `_dungeonBattleModel`: IDungeonBattleModel

---

#### DungeonEnterButtonUiView

**Line:** 712881

**Inherits:** UiUnityView

**Fields:**

- `Button`: BeveledUnityButton
- `_dungeon`: GameEntity

---

#### DungeonEntryUiView

**Line:** 712909

**Inherits:** UiUnityView

**Fields:**

- `BackgroundImage`: Image
- `TitleText`: TMP_Text
- `OpenButton`: UnityButton

---

#### DungeonFeature

**Line:** 712553

**Inherits:** Feature

---

#### DungeonFeatureInitializeSystem

**Line:** 712780

**Inherits:** IInitializeSystem

---

#### DungeonInitializeSystem

**Line:** 712814

**Inherits:** IInitializeSystem

---

#### DungeonKeysChangeMessage

**Line:** 712630

**Inherits:** IMessage

---

#### DungeonLeaveButtonUiView

**Line:** 713508

**Inherits:** UiUnityView

**Fields:**

- `LeaveButton`: BeveledUnityButton
- `_leaveFeature`: GameEntity

---

#### DungeonLockUiView

**Line:** 712929

**Inherits:** UiUnityView

**Fields:**

- `UnlockedElements`: GameObject
- `LockedElements`: GameObject
- `UnlockText`: TMP_Text
- `_dungeonEntity`: GameEntity

---

#### DungeonReactiveModel

**Line:** 712704

**Inherits:** ReactiveModel

**Fields:**

- `DungeonModel`: PlayerDungeonModel

---

#### DungeonReactiveModelComponent

**Line:** 712464

**Inherits:** IComponent

**Fields:**

- `Value`: DungeonReactiveModel

---

#### DungeonRedDotLogic

**Line:** 712593

**Inherits:** IRedDotLogic

**Fields:**

- `_stillLockedDungeonsCount`: int

---

#### DungeonSpinnerUiView

**Line:** 713539

**Inherits:** UiUnityView

**Fields:**

- `_tween`: Tween
- `Target`: Transform
- `LoopDuration`: float

---

#### DungeonStatTarget

**Line:** 1077253

**Inherits:** StatTargetBase

---

#### DungeonSweepLastButtonUiView

**Line:** 713047

**Inherits:** UiUnityView

**Fields:**

- `Button`: BeveledUnityButton
- `_dungeon`: GameEntity

---

#### DungeonSyncSystem

**Line:** 712829

**Inherits:** IExecuteSystem

---

#### DungeonTabRedDotUiView

**Line:** 713075

**Inherits:** RedDotUiView

---

#### DungeonTabUiCreateSystem

**Line:** 712844

**Inherits:** ReactiveSystem

---

#### DungeonTabUiView

**Line:** 713090

**Inherits:** UiUnityView

**Fields:**

- `DungeonParent`: Transform
- `DungeonsHeaderLabel`: TMP_Text

---

#### DungeonVisualConfig

**Line:** 712487

**Inherits:** ScriptableObject

**Fields:**

- `Dungeons`: SerializableDictionary<DungeonType, DungeonVisualData>

---

#### DungeonVisualData

**Line:** 712500

**Fields:**

- `BackgroundImage`: Sprite
- `DungeonTitle`: string
- `KeyImage`: Sprite
- `MapElementViews`: List<MapElementView>
- `MapBackgroundColor`: Color

---

#### DungeonWinCheatAction

**Line:** 1060843

**Inherits:** PlayerAction

---

#### DungeonsDifficultyUiView

**Line:** 712959

**Inherits:** UiUnityView

**Fields:**

- `LeftButton`: UnityButton
- `RightButton`: UnityButton
- `DifficultyText`: TMP_Text
- `_dungeon`: GameEntity

---

#### DungeonsKeyUiView

**Line:** 712994

**Inherits:** UiUnityView

**Fields:**

- `KeysText`: TMP_Text
- `_dungeon`: GameEntity

---

#### DungeonsLocalizer

**Line:** 720934

**Inherits:** LocalizerBase

---

#### DungeonsMaxCheatAction

**Line:** 1060829

**Inherits:** PlayerAction

---

#### Enemy

**Line:** 1059439

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

#### HammerDungeonKeyChangeMessage

**Line:** 712665

**Inherits:** DungeonKeysChangeMessage

---

#### HammerThiefDungeonBattleLibrary

**Line:** 1061405

**Inherits:** IGameConfigData

---

#### HammerThiefDungeonBattleModel

**Line:** 1061471

**Inherits:** IDungeonBattleModel

---

#### InvasionDungeonEndReactiveSystem

**Line:** 713338

**Inherits:** ReactiveSystem

---

#### MainBattleBalancing

**Line:** 1056472

---

#### MainBattleConfig

**Line:** 1059256

**Inherits:** GameConfigKeyValue

---

#### MainBattleId

**Line:** 1050700

**Inherits:** IEquatable

---

#### MainBattleIdParser

**Line:** 1056498

**Inherits:** ConfigParserProvider

---

#### MainBattleIdProgressKey

**Line:** 1078488

**Inherits:** ProgressKeyBase

---

#### MainBattleLibrary

**Line:** 1059306

**Inherits:** IGameConfigData

---

#### MainBattleMapSystem

**Line:** 710428

**Inherits:** ReactiveSystem

---

#### MainBattleModel

**Line:** 1056551

---

#### MainBattleModelInitSystem

**Line:** 710177

**Inherits:** IInitializeSystem

---

#### MainBattlePauseExecuteSystem

**Line:** 710192

**Inherits:** IExecuteSystem

---

#### MainBattleProgressMessage

**Line:** 728392

**Inherits:** IMessage

---

#### MainBattleReactiveModel

**Line:** 710088

**Inherits:** ReactiveModel

---

#### MainBattleReactiveModelComponent

**Line:** 710056

**Inherits:** IComponent

**Fields:**

- `Value`: MainBattleReactiveModel

---

#### MainBattleStartedMessage

**Line:** 710068

**Inherits:** IMessage

---

#### MainBattleSyncSystem

**Line:** 710207

**Inherits:** IExecuteSystem

---

#### MainBattleSystem

**Line:** 710222

**Inherits:** IExecuteSystem

**Fields:**

- `_timer`: float
- `_state`: BattleState
- `_camPos`: Vector2

---

#### MainBattleUiCreateOnBattleModeSystem

**Line:** 721615

**Inherits:** ReactiveSystem

---

#### MainBattleUiDestroySystem

**Line:** 721636

**Inherits:** ReactiveSystem

---

#### MainBattleUiEntry

**Line:** 710290

**Inherits:** MonoBehaviour

**Fields:**

- `RectTransform`: RectTransform
- `Circle`: Image
- `BigScale`: Vector2
- `SmallScale`: Vector2

---

#### MainBattleUiFeature

**Line:** 721606

**Inherits:** Feature

---

#### MainBattleUiInitSystem

**Line:** 721657

**Inherits:** IInitializeSystem

---

#### MainBattleUiView

**Line:** 710328

**Inherits:** UiUnityView

**Fields:**

- `RectTransform`: RectTransform
- `_mainBattleUiEntryPrefab`: MainBattleUiEntry
- `ProgressBar`: Image
- `Parent`: Transform
- `Spacing`: float
- `BattleLabel`: TextMeshProUGUI
- `_entries`: List<MainBattleUiEntry>
- `_battleIdx`: int
- `_ageIdx`: int
- `_difficultyIdx`: int
- `_sequence`: Sequence

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

#### PotionDungeonKeysChangeMessage

**Line:** 712685

**Inherits:** DungeonKeysChangeMessage

---

#### SetupDungeonBattleAction

**Line:** 1061078

**Inherits:** PlayerAction

---

#### SetupMainBattleAction

**Line:** 1056718

**Inherits:** PlayerAction

---

#### StartMainBattleAfterDungeonSystem

**Line:** 713359

**Inherits:** ReactiveSystem

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

### Enums (3)

#### BattleMode

**Line:** 1056395

**Values:**

- `None` = 0
- `MainBattle` = 1
- `DungeonBattle` = 2
- `PvpBattle` = 3
- `GuildWarBattle` = 4

---

#### BattleState

**Line:** 1056514

**Values:**

- `None` = 0
- `ReadyToStartWave` = 1
- `WaveFinished` = 2
- `Running` = 3
- `Paused` = 4
- `Won` = 5
- `Lost` = 6

---

#### DungeonType

**Line:** 1061243

**Values:**

- `Hammer` = 0
- `Skill` = 1
- `Pet` = 2
- `Potion` = 3

---

## PvP

### Classes (90)

#### ArenaChallengeTicketsRedDotUiView

**Line:** 705034

**Inherits:** RedDotUiView

---

#### ArenaChallengeUiPlayerEntryView

**Line:** 705049

**Inherits:** MonoBehaviour

**Fields:**

- `ChallengeButton`: CostButtonUiView
- `ProfileButton`: UnityButton
- `StarsText`: TMP_Text
- `PowerText`: TMP_Text
- `PlayerNameText`: TMP_Text
- `PlayerIcon`: Image
- `_matchup`: ArenaMatchupOption

---

#### ArenaChallengeUiView

**Line:** 705079

**Inherits:** UiUnityView

**Fields:**

- `PlayerEntryPrefab`: ArenaChallengeUiPlayerEntryView
- `PlayerEntryParent`: Transform
- `HeaderLabel`: TMP_Text

---

#### ArenaFeature

**Line:** 704914

**Inherits:** Feature

---

#### ArenaFeatureInitializeSystem

**Line:** 705019

**Inherits:** IInitializeSystem

---

#### ArenaLeaderBoardUiManager

**Line:** 705171

**Inherits:** TickedUiView

**Fields:**

- `ArenaPlayerEntryPrefab`: ArenaPlayerEntryView
- `LeaderBoardParent`: Transform
- `ScrollRect`: ScrollRect
- `Promotion`: GameObject
- `Demotion`: GameObject
- `ScrollSpeed`: float
- `_leaderBoardEntries`: List<ArenaPlayerEntryView>
- `_freshOpened`: bool

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

#### ArenaPlayerEntryView

**Line:** 705212

**Inherits:** MonoBehaviour

**Fields:**

- `PlayerName`: TMP_Text
- `PlayerRank`: TMP_Text
- `StarsText`: TMP_Text
- `PowerText`: TMP_Text
- `PlayerRankIcon`: Image
- `PlayerIcon`: Image
- `Background`: UnityUiElement
- `PlayerWorldView`: PlayerWorldView
- `ProfileButton`: UnityButton
- `_targetPlayerId`: EntityId

---

#### ArenaPromotionDisplayedAction

**Line:** 1055814

**Inherits:** PlayerAction

---

#### ArenaPromotionManagerUiView

**Line:** 705245

**Inherits:** TickedUiView

**Fields:**

- `DebugFromLeague`: int
- `DebugToLeague`: int
- `Rank`: int

---

#### ArenaPromotionView

**Line:** 705295

**Inherits:** UiUnityView

**Fields:**

- `StartTransparency`: float
- `LeagueImageOverlay`: Image
- `LeagueImageMask`: Image
- `LeagueImage`: Image
- `LeagueToText`: TMP_Text
- `DescriptionText`: TMP_Text
- `BackGroundButton`: UnityButton
- `Promotion`: GameObject
- `Demotion`: GameObject
- `_isAnimating`: bool

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

#### ArenaResultStarsView

**Line:** 705325

**Inherits:** MonoBehaviour

**Fields:**

- `Stars`: TMP_Text

---

#### ArenaRewardEntryVisual

**Line:** 705340

**Inherits:** MonoBehaviour

**Fields:**

- `RewardText`: TMP_Text

---

#### ArenaRewardGridVisual

**Line:** 705352

**Inherits:** MonoBehaviour

**Fields:**

- `RewardGrid`: Transform
- `RewardPrefab`: ArenaRewardEntryVisual

---

#### ArenaRewardLibrary

**Line:** 1056132

**Inherits:** IGameConfigData

---

#### ArenaRewardRankEntryVisual

**Line:** 705371

**Inherits:** MonoBehaviour

**Fields:**

- `ArenaRewardGridVisual`: ArenaRewardGridVisual
- `RankText`: TMP_Text
- `RankIcon`: Image

---

#### ArenaRewardsRedDotUiView

**Line:** 705388

**Inherits:** RedDotUiView

---

#### ArenaRewardsUiView

**Line:** 705403

**Inherits:** TickedUiView

**Fields:**

- `ClaimedText`: GameObject
- `CollectButtonText`: TMP_Text
- `CurrentRankText`: TMP_Text
- `CollectButton`: UnityButton
- `CollectButtonImage`: Image
- `ArenaRewardGridVisual`: ArenaRewardGridVisual
- `RankEntryParent`: Transform
- `ArenaRewardRankEntryVisualPrefab`: ArenaRewardRankEntryVisual
- `CurrentLeagueBannerText`: TMP_Text

---

#### ArenaTabRedDotUiView

**Line:** 705444

**Inherits:** RedDotUiView

---

#### ArenaTutorialDisplayedAction

**Line:** 1055907

**Inherits:** PlayerAction

---

#### ArenaUiView

**Line:** 705492

**Inherits:** TickedUiView

**Fields:**

- `ChallengeButton`: UnityButton
- `ArenaEndedText`: TMP_Text
- `LeagueNameText`: TMP_Text
- `LeagueIcon`: Image
- `EnabledObjects`: List<GameObject>
- `DisabledObjects`: List<GameObject>
- `SeasonEndsInDisabledText`: TMP_Text
- `GiftText`: TMP_Text
- `ArenaPlayerEntryView`: ArenaPlayerEntryView
- `LoadingIcon`: GameObject

---

#### ArenaVisualConfig

**Line:** 704988

**Inherits:** ScriptableObject

---

#### ChatPvpResultShareUiView

**Line:** 727147

**Inherits:** MonoBehaviour

**Fields:**

- `ShareButton`: UnityButton
- `ShareSuccessTextGo`: GameObject
- `_mainChatUIModel`: MainChatUIModel

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

#### GuildWarPvpBattleStartAction

**Line:** 1062005

**Inherits:** PlayerAction

---

#### GuildWarPvpResultPointsUiView

**Line:** 719923

**Inherits:** PvpResultUiView

**Fields:**

- `Points`: TMP_Text

---

#### OperatingSystem

**Line:** 72424

**Inherits:** ISerializable

**Fields:**

- `_versionString`: string

---

#### PlayerPvpBattleModel

**Line:** 1074243

---

#### PlayerPvpCharacterEquipmentView

**Line:** 728160

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `Visual`: UnitEquipmentVisual
- `SkinsVisual`: SkinEquipmentVisual

---

#### PlayerPvpCharacterMountView

**Line:** 728179

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `CharacterRig`: Transform
- `Shadow`: GameObject

---

#### PlayerPvpCharacterMovementView

**Line:** 728198

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `Speed`: float
- `PlayerPvpCharacterPetParentView`: PlayerPvpCharacterPetParentView

---

#### PlayerPvpCharacterPetParentView

**Line:** 728220

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `PlayerUnitTransform`: Transform

---

#### PlayerPvpCharacterSerializerUi

**Line:** 728015

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `InputField`: TMP_InputField
- `SerializeButton`: UnityButton
- `LoadButton`: UnityButton
- `SaveButton`: UnityButton
- `SavePvpProfileViewPrefab`: SavePvpProfileView

---

#### PlayerPvpCharacterUnitView

**Line:** 728245

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `Animator`: Animator
- `_tween`: Tween

---

#### PlayerPvpCharacterView

**Line:** 728268

**Inherits:** MonoBehaviour

---

#### PlayerPvpInventoryManagerUiView

**Line:** 727247

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `Slots`: List<Transform>
- `SlotPrefab`: SlotVisual
- `ItemPrefab`: PvpInventoryItemVisual
- `SkinSlotPrefab`: SkinSlotUiView

---

#### PlayerPvpItemModel

**Line:** 1058122

---

#### PlayerPvpMountModel

**Line:** 1058175

---

#### PlayerPvpMountPopupUiView

**Line:** 727271

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `Level`: TMP_Text
- `Background`: Image
- `Name`: TMP_Text
- `Stats`: TMP_Text

---

#### PlayerPvpMountUiView

**Line:** 727290

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `MountParent`: GameObject
- `EmptyParent`: GameObject
- `Icon`: Image
- `Level`: TMP_Text
- `Background`: Image
- `Button`: UnityButton
- `_mount`: PlayerPvpMountModel
- `_stats`: Stats

---

#### PlayerPvpPetModel

**Line:** 1058228

---

#### PlayerPvpPetPopupUiView

**Line:** 727318

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `Level`: TMP_Text
- `Background`: Image
- `Name`: TMP_Text
- `Stats`: TMP_Text

---

#### PlayerPvpPetUiView

**Line:** 727337

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `Pets`: List<PvpProfilePetVisual>

---

#### PlayerPvpProfileCharacterScene

**Line:** 727355

**Inherits:** MonoBehaviour

**Fields:**

- `Views`: List<PlayerPvpCharacterView>
- `Camera`: Camera

---

#### PlayerPvpProfileEditorUiView

**Line:** 728046

**Inherits:** MonoBehaviour

**Fields:**

- `Views`: List<PlayerPvpCharacterView>

---

#### PlayerPvpProfileModel

**Line:** 1058294

---

#### PlayerPvpProfileQuickSaveStorage

**Line:** 727972

**Inherits:** ScriptableObject

**Fields:**

- `Profiles`: List<PvpProfileQuickSaveEntry>

---

#### PlayerPvpProfileStartBattleButtonUiView

**Line:** 727392

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `BattleButton`: UnityButton
- `BattleType`: PvpBattleType
- `_profileModel`: PlayerPvpProfileModel
- `_playerId`: EntityId

---

#### PlayerPvpProfileTextUiView

**Line:** 727436

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `_miniProfileView`: PlayerMiniProfileUiView
- `_progressText`: TMP_Text
- `HideGuildInfoButton`: bool
- `AllowGuildMembersProfileClick`: bool

---

#### PlayerPvpProfileUiView

**Line:** 727526

**Inherits:** MonoBehaviour

**Fields:**

- `LoadingParent`: GameObject
- `ActiveParent`: GameObject
- `SceneParent`: Transform
- `CharacterScenePrefab`: PlayerPvpProfileCharacterScene
- `CharacterTargetImage`: RawImage
- `_characterScene`: PlayerPvpProfileCharacterScene
- `Views`: List<PlayerPvpCharacterView>
- `BlockButton`: UnityButton
- `ReportButton`: UnityButton
- `BlockLabel`: TMP_Text
- `ReportLabel`: TMP_Text
- `_chatService`: IChatService
- `_cancellationTokenSource`: CancellationTokenSource
- `_messageId`: long
- `_channelId`: string

---

#### PlayerPvpSkinCollectionModel

**Line:** 1075968

---

#### PvpBaseConfig

**Line:** 1074008

**Inherits:** GameConfigKeyValue

---

#### PvpBattleMapSystem

**Line:** 710449

**Inherits:** ReactiveSystem

---

#### PvpBattleStartAction

**Line:** 1073893

**Inherits:** PlayerAction

---

#### PvpBattleStartedMessage

**Line:** 727138

**Inherits:** IMessage

---

#### PvpBattleSyncSystem

**Line:** 726958

**Inherits:** IExecuteSystem

**Fields:**

- `_state`: PvpBattleState

---

#### PvpBattleUi

**Line:** 726998

**Inherits:** UiUnityView

**Fields:**

- `Player1Name`: TMP_Text
- `Player2Name`: TMP_Text
- `Player1Power`: TMP_Text
- `Player2Power`: TMP_Text

---

#### PvpCheatContainer

**Line:** 686264

**Inherits:** AbstractCheatContainer

---

#### PvpCheatSystem

**Line:** 686655

**Inherits:** CheatSystem

---

#### PvpFeature

**Line:** 726949

**Inherits:** Feature

---

#### PvpInventoryItemPopupVisual

**Line:** 727601

**Inherits:** MonoBehaviour

**Fields:**

- `BaseItemVisual`: BaseItemVisual
- `Name`: TMP_Text
- `Stats`: TMP_Text

---

#### PvpInventoryItemVisual

**Line:** 727618

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `BaseItemVisual`: BaseItemVisual
- `_item`: PlayerPvpItemModel

---

#### PvpLeaveButtonUiView

**Line:** 727074

**Inherits:** UiUnityView

**Fields:**

- `LeaveButton`: BeveledUnityButton

---

#### PvpLeaveSystem

**Line:** 726974

**Inherits:** ReactiveSystem

---

#### PvpMapData

**Line:** 711508

**Fields:**

- `MapElementViews`: List<MapElementView>
- `MapBackgroundColor`: Color

---

#### PvpMatchInfo

**Line:** 1074508

**Fields:**

- `Player1`: PlayerPvpProfileModel
- `Player2`: PlayerPvpProfileModel
- `Result`: PvpBattleResult
- `BattleSeed`: ulong
- `PvpBattleType`: PvpBattleType
- `Player1Id`: EntityId
- `Player2Id`: EntityId

---

#### PvpProfilePetVisual

**Line:** 727656

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `Background`: Image
- `Level`: TMP_Text
- `Button`: UnityButton

---

#### PvpProfileQuickSaveEntry

**Line:** 727985

**Fields:**

- `Name`: string
- `Content`: string

---

#### PvpProfileSecondaryEffectsUiView

**Line:** 727701

**Inherits:** PlayerPvpCharacterView

**Fields:**

- `SecondariesText`: TMP_Text

---

#### PvpReplayBattleStartAction

**Line:** 1073946

**Inherits:** PlayerAction

---

#### PvpReplayButtonUiView

**Line:** 727756

**Inherits:** MonoBehaviour

**Fields:**

- `Button`: UnityButton
- `_matchInfo`: PvpMatchInfo

---

#### PvpResultEntryView

**Line:** 727775

**Inherits:** MonoBehaviour

**Fields:**

- `Icon`: Image
- `PlayerName`: TMP_Text
- `PlayerPower`: TMP_Text
- `Background`: Image
- `WinText`: GameObject
- `LoseText`: GameObject

---

#### PvpResultUiView

**Line:** 727795

**Inherits:** MonoBehaviour

**Fields:**

- `Player1`: PvpResultEntryView
- `Player2`: PvpResultEntryView
- `DrawText`: TMP_Text

---

#### PvpSpinnerUiView

**Line:** 727095

**Inherits:** UiUnityView

**Fields:**

- `_tween`: Tween
- `Target`: Transform
- `LoopDuration`: float

---

#### PvpTicketsChangeMessage

**Line:** 711793

**Inherits:** CurrencyChangeMessage

---

#### PvpTicketsUiView

**Line:** 705549

**Inherits:** UiUnityView

**Fields:**

- `CoinLabel`: TextMeshProUGUI
- `_gameListenerEntity`: GameEntityRef

---

#### PvpTimerUiView

**Line:** 727118

**Inherits:** UiUnityView

**Fields:**

- `TimerText`: TMP_Text
- `ProgressBar`: Image
- `ClockHandAnimation`: ClockHandAnimation

---

#### RunArenaPvpBattleAction

**Line:** 1055956

**Inherits:** PlayerSynchronizedServerActionCore

---

#### RunGuildWarPvpBattleAction

**Line:** 1062047

**Inherits:** PlayerSynchronizedServerActionCore

---

#### SavePvpProfileView

**Line:** 728139

**Inherits:** MonoBehaviour

**Fields:**

- `SaveButton`: UnityButton
- `NameInputField`: TMP_InputField
- `SavegameText`: TMP_Text
- `CloseButton`: UnityButton

---

#### ShareLastChatPvpAction

**Line:** 1073977

**Inherits:** PlayerAction

---

#### UpdateNextArenaTime

**Line:** 1056009

**Inherits:** PlayerSynchronizedServerActionCore

**Fields:**

- `NextDivisionTime`: MetaTime

---

### Enums (4)

#### OperatingSystemFamily

**Line:** 885041

**Values:**

- `Other` = 0
- `MacOSX` = 1
- `Windows` = 2
- `Linux` = 3

---

#### PvpBattleResult

**Line:** 1074354

**Values:**

- `NotFinished` = 0
- `Draw` = 1
- `Party1Win` = 2
- `Party2Win` = 3
- `Forfeit` = 4

---

#### PvpBattleState

**Line:** 1074342

**Values:**

- `None` = 0
- `Running` = 1
- `CombatFinished` = 2
- `Finished` = 3

---

#### PvpBattleType

**Line:** 1074230

**Values:**

- `Test` = 0
- `Chat` = 1
- `ChatReplay` = 2
- `Arena` = 3
- `GuildWar` = 4

---

## Summoning

### Classes (47)

#### AsyncDropTrigger

**Line:** 1134141

**Inherits:** AsyncTriggerBase

---

#### CryptoApiRandomGenerator

**Line:** 1518917

**Inherits:** IRandomGenerator

---

#### DigestRandomGenerator

**Line:** 1518953

**Inherits:** IRandomGenerator

**Fields:**

- `stateCounter`: long
- `seedCounter`: long
- `digest`: IDigest

---

#### DragAndDropData

**Line:** 631969

---

#### Dropdown

**Line:** 1352260

**Inherits:** Selectable

**Fields:**

- `m_Template`: RectTransform
- `m_CaptionText`: Text
- `m_CaptionImage`: Image
- `m_ItemText`: Text
- `m_ItemImage`: Image
- `m_Value`: int
- `m_AlphaFadeSpeed`: float
- `m_Dropdown`: GameObject
- `m_Blocker`: GameObject
- `m_Items`: List<Dropdown.DropdownItem>
- `m_AlphaTweenRunner`: TweenRunner<FloatTween>
- `validTemplate`: bool

---

#### DropdownField

**Line:** 617142

**Inherits:** PopupField

---

#### DropdownMenu

**Line:** 632770

**Fields:**

- `m_MenuItems`: List<DropdownMenuItem>
- `m_DropdownMenuEventInfo`: DropdownMenuEventInfo

---

#### DropdownMenuAction

**Line:** 632682

**Inherits:** DropdownMenuItem

---

#### DropdownMenuEventInfo

**Line:** 632613

---

#### DropdownMenuItem

**Line:** 632639

---

#### DropdownMenuSeparator

**Line:** 632648

**Inherits:** DropdownMenuItem

---

#### EggDropChanceDetailsUiView

**Line:** 713127

**Inherits:** UiUnityView

**Fields:**

- `Parent`: Transform
- `Prefab`: SummonUpgradeEntry
- `Label_Level`: TMP_Text
- `PreviousButton`: UnityButton
- `NextButton`: UnityButton
- `_summonUpgradeEntries`: List<SummonUpgradeEntry>
- `_level`: int
- `_dungeon`: GameEntity

---

#### EggDropDetailsOpenUiView

**Line:** 713158

**Inherits:** UiUnityView

**Fields:**

- `EggInfoButton`: UnityButton

---

#### EggsSummonedMessage

**Line:** 723622

**Inherits:** IMessage

---

#### EntitasSummonAnimationUiView

**Line:** 716073

**Inherits:** UiUnityView

**Fields:**

- `Parent`: Transform
- `BlackFadeCanvasGroup`: CanvasGroup
- `MainClickButton`: UnityButton
- `_itemDropSequence`: Sequence

---

#### GenericDropdownMenu

**Line:** 617563

**Inherits:** IGenericMenu

**Fields:**

- `m_Items`: List<GenericDropdownMenu.MenuItem>
- `m_MenuContainer`: VisualElement
- `m_OuterContainer`: VisualElement
- `m_ScrollView`: ScrollView
- `m_PanelRootVisualContainer`: VisualElement
- `m_TargetElement`: VisualElement
- `m_DesiredRect`: Rect
- `m_NavigationManipulator`: KeyboardNavigationManipulator
- `m_PositionTop`: float
- `m_PositionLeft`: float
- `m_ContentWidth`: float
- `m_FitContentWidth`: bool
- `m_ShownAboveTarget`: bool
- `m_MousePosition`: Vector2

---

#### IntDropdownAttribute

**Line:** 739391

**Inherits:** PropertyAttribute

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

#### MountSummonActionButtonUiView

**Line:** 722673

**Inherits:** ActionButtonUiView

---

#### MountSummonCheatAction

**Line:** 1070362

**Inherits:** PlayerAction

---

#### MountSummonConfig

**Line:** 1070591

**Inherits:** GameConfigKeyValue

---

#### MountSummonDetailsUiView

**Line:** 722721

**Inherits:** MonoBehaviour

**Fields:**

- `Parent`: Transform
- `Prefab`: SummonUpgradeEntry
- `LabelTitle`: TMP_Text
- `PreviousButton`: UnityButton
- `NextButton`: UnityButton
- `ProgressArea`: GameObject
- `_summonUpgradeEntries`: List<SummonUpgradeEntry>
- `_currentLevel`: int
- `_maxLevel`: int

---

#### MountSummonDropChanceConfig

**Line:** 1070629

**Inherits:** IGameConfigData

---

#### MountSummonUpgradeConfig

**Line:** 1070734

**Inherits:** IGameConfigData

---

#### MountSummonUpgradeStatusUiView

**Line:** 722774

**Inherits:** MonoBehaviour

**Fields:**

- `LabelProgress`: TMP_Text
- `LabelLevel`: TMP_Text
- `ProgressBar`: Image
- `_maxLevel`: int

---

#### MountsSummonedMessage

**Line:** 722228

**Inherits:** IMessage

---

#### PetRarityVisualConfig

**Line:** 723544

**Inherits:** ScriptableObject

---

#### PseudoRandom

**Line:** 1057806

**Fields:**

- `_offset`: int

---

#### Random

**Line:** 31081

**Fields:**

- `_inext`: int
- `_inextp`: int

---

#### RandomNumberGenerator

**Line:** 218557

**Inherits:** IDisposable

---

#### RandomPCG

**Line:** 523666

**Inherits:** IEquatable

**Fields:**

- `_state`: ulong

---

#### RandomValueStatContribution

**Line:** 1075806

---

#### RandomizeRangeRequest

**Line:** 1396393

**Inherits:** IDirectResponseSchema

---

#### RarityComponent

**Line:** 730406

**Inherits:** IComponent

**Fields:**

- `Value`: Rarity

---

#### SecureRandom

**Line:** 1518023

**Inherits:** Random

---

#### StringDropdownAttribute

**Line:** 739411

**Inherits:** PropertyAttribute

---

#### SummonAnimationData

**Line:** 716056

**Fields:**

- `Icon`: Sprite
- `AnimationView`: SummonEntryAnimationView
- `IsNew`: bool
- `Rarity`: Nullable<Rarity>
- `Text`: string

---

#### SummonAnimationDataComponent

**Line:** 716044

**Inherits:** IComponent

**Fields:**

- `Value`: List<SummonAnimationData>

---

#### SummonAnimationUiView

**Line:** 716100

**Inherits:** MonoBehaviour

**Fields:**

- `Parent`: RectTransform
- `BlackFadeCanvasGroup`: CanvasGroup
- `MainClickButton`: UnityButton
- `TextOnlyViewPrefab`: SummonEntryAnimationView
- `OnCloseAction`: Action
- `_itemDropSequence`: Sequence

---

#### SummonEntryAnimationView

**Line:** 716167

**Inherits:** MonoBehaviour

**Fields:**

- `ItemCanvasGroup`: CanvasGroup
- `SlotImage`: Image
- `Icon`: Image
- `NewTextObject`: GameObject
- `Label`: TMP_Text
- `_color`: Color

---

#### SummonMountRedDotUiView

**Line:** 722818

**Inherits:** RedDotUiView

---

#### SummonUpgradeEntry

**Line:** 729648

**Inherits:** MonoBehaviour

**Fields:**

- `RarityBackground`: Image
- `Label_Rarity`: TMP_Text
- `Label_NextProbability`: TMP_Text

---

#### TMP_Dropdown

**Line:** 1222363

**Inherits:** Selectable

**Fields:**

- `m_Template`: RectTransform
- `m_CaptionText`: TMP_Text
- `m_CaptionImage`: Image
- `m_Placeholder`: Graphic
- `m_ItemText`: TMP_Text
- `m_ItemImage`: Image
- `m_Value`: int
- `m_MultiSelect`: bool
- `m_AlphaFadeSpeed`: float
- `m_Dropdown`: GameObject
- `m_Blocker`: GameObject
- `m_Items`: List<TMP_Dropdown.DropdownItem>
- `m_AlphaTweenRunner`: TweenRunner<FloatTween>
- `validTemplate`: bool
- `m_Coroutine`: Coroutine

---

#### TrackedTmpDropdown

**Line:** 1329471

**Inherits:** JsonSerializerTrackedObject

---

#### TrackedUGuiDropdown

**Line:** 1329568

**Inherits:** JsonSerializerTrackedObject

---

### Enums (4)

#### DragAndDropPosition

**Line:** 632108

**Values:**

- `OverItem` = 0
- `BetweenItems` = 1
- `OutsideItems` = 2

---

#### DropdownMenuAction

**Line:** 632670

---

#### Rarity

**Line:** 1074976

**Values:**

- `Common` = 0
- `Rare` = 1
- `Epic` = 2
- `Legendary` = 3
- `Ultimate` = 4
- `Mythic` = 5

---

#### SummonEntryAnimationView

**Line:** 716132

---

