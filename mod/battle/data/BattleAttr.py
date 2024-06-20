import math
from luatable import table, setmetatable
def clamp(a,b,c):
	return b if b < a else c if c > a else a

var_0_0 = table()



import BattleConst
import BattleConfig
import BattleFormulas
import BattleDataProxy
import BattleDataFunction
from model.const import AttributeType
from const import *

class BattleAttr:
	AttrListInheritance = table(
		"level",
		"formulaLevel",
		"repressReduce",
		"cannonPower",
		"torpedoPower",
		"antiAirPower",
		"airPower",
		"antiSubPower",
		"fleetGS",
		"loadSpeed",
		"attackRating",
		"dodgeRate",
		"velocity",
		"luck",
		"cri",
		"criDamage",
		"criDamageResist",
		"hiveExtraHP",
		"GCT",
		"bulletSpeedRatio",
		"torpedoSpeedExtra",
		"damageRatioBullet",
		"damageEnhanceProjectile",
		"healingEnhancement",
		"injureRatio",
		"injureRatioByCannon",
		"injureRatioByBulletTorpedo",
		"injureRatioByAir",
		"damageRatioByCannon",
		"damageRatioByBulletTorpedo",
		"damageRatioByAir",
		"damagePreventRantTorpedo",
		"accuracyRateExtra",
		"dodgeRateExtra",
		"perfectDodge",
		"immuneDirectHit",
		"chargeBulletAccuracy",
		"dropBombAccuracy",
		"aircraftBooster",
		"manualEnhancement",
		"initialEnhancement",
		"worldBuffResistance",
		"airResistPierceActive",
		"airResistPierce"
	)

	@staticmethod
	def InsertInheritedAttr(arg_1_0):
		for i in arg_1_0.values():
			BattleAttr.AttrListInheritance.append(i)

	InsertInheritedAttr(BattleConfig.AMMO_DAMAGE_ENHANCE)
	InsertInheritedAttr(BattleConfig.AMMO_DAMAGE_REDUCE)
	InsertInheritedAttr(BattleConfig.DAMAGE_AMMO_TO_ARMOR_RATE_ENHANCE)
	InsertInheritedAttr(BattleConfig.DAMAGE_TO_ARMOR_RATE_ENHANCE)
	InsertInheritedAttr(BattleConfig.SHIP_TYPE_ACCURACY_ENHANCE)

	TAG_EHC_KEY = "DMG_TAG_EHC_"
	FROM_TAG_EHC_KEY = "DMG_FROM_TAG_"
	TAG_CRI_EHC_KEY = "CRI_TAG_EHC_"
	TAG_CRIDMG_EHC_KEY = "CRIDMG_TAG_EHC_"
	ATTACK_ATTR_TYPE = table({
		BattleConst.WeaponDamageAttr.CANNON: "cannonPower",
		BattleConst.WeaponDamageAttr.TORPEDO: "torpedoPower",
		BattleConst.WeaponDamageAttr.ANTI_AIR: "antiAirPower",
		BattleConst.WeaponDamageAttr.AIR: "airPower",
		BattleConst.WeaponDamageAttr.ANIT_SUB: "antiSubPower"
	})

	@staticmethod
	def GetAtkAttrByType(arg_2_0, arg_2_1):
		var_2_0 = BattleAttr.ATTACK_ATTR_TYPE[arg_2_1]

		return max(arg_2_0[var_2_0], 0)

	@staticmethod
	def SetAttr(arg_3_0, arg_3_1):
		arg_3_0._attr = setmetatable(table(), table(
			__index = arg_3_1
		))

	@staticmethod
	def GetAttr(arg_4_0):
		return arg_4_0._attr

	@staticmethod
	def SetBaseAttr(arg_5_0):
		arg_5_0._baseAttr = table.Clone(arg_5_0._attr)

	@staticmethod
	def IsInvincible(arg_6_0):
		var_6_0 = arg_6_0._attr.isInvincible

		return var_6_0 and var_6_0 > 0

	@staticmethod
	def AppendInvincible(arg_7_0):
		var_7_0 = arg_7_0._attr.isInvincible or 0

		arg_7_0._attr.isInvincible = var_7_0 + 1

	@staticmethod
	def AddImmuneAreaLimit(arg_8_0, arg_8_1):
		var_8_0 = (arg_8_0._attr.immuneAreaLimit or 0) + arg_8_1

		arg_8_0._attr.immuneAreaLimit = var_8_0

		arg_8_0._move.ImmuneAreaLimit(var_8_0 > 0)

	@staticmethod
	def AddImmuneMaxAreaLimit(arg_9_0, arg_9_1):
		var_9_0 = (arg_9_0._attr.immuneMaxAreaLimit or 0) + arg_9_1

		arg_9_0._attr.immuneMaxAreaLimit = var_9_0

		arg_9_0._move.ImmuneMaxAreaLimit(var_9_0 > 0)

	@staticmethod
	def IsImmuneAreaLimit(arg_10_0):
		var_10_0 = arg_10_0._attr.immuneAreaLimit

		return var_10_0 and var_10_0 > 0

	@staticmethod
	def IsImmuneMaxAreaLimit(arg_11_0):
		var_11_0 = arg_11_0._attr.immuneMaxAreaLimit

		return var_11_0 and var_11_0 > 0

	@staticmethod
	def IsVisitable(arg_12_0):
		var_12_0 = arg_12_0._attr.isUnVisitable

		return not var_12_0 or var_12_0 <= 0

	@staticmethod
	def UnVisitable(arg_13_0):
		var_13_0 = arg_13_0._attr.isUnVisitable or 0

		arg_13_0._attr.isUnVisitable = var_13_0 + 1

	@staticmethod
	def Visitable(arg_14_0):
		var_14_0 = arg_14_0._attr.isUnVisitable or 0

		arg_14_0._attr.isUnVisitable = var_14_0 - 1

	@staticmethod
	def IsSpirit(arg_15_0):
		var_15_0 = arg_15_0._attr.isSpirit

		return var_15_0 and var_15_0 > 0

	@staticmethod
	def Spirit(arg_16_0):
		var_16_0 = arg_16_0._attr.isSpirit or 0

		arg_16_0._attr.isSpirit = var_16_0 + 1

	@staticmethod
	def Entity(arg_17_0):
		var_17_0 = arg_17_0._attr.isSpirit or 0

		arg_17_0._attr.isSpirit = var_17_0 - 1

	@staticmethod
	def IsStun(arg_18_0):
		var_18_0 = arg_18_0._attr.isStun

		return var_18_0 and var_18_0 > 0

	@staticmethod
	def Stun(arg_19_0):
		var_19_0 = arg_19_0._attr.isStun or 0

		arg_19_0._attr.isStun = var_19_0 + 1

	@staticmethod
	def CancelStun(arg_20_0):
		var_20_0 = arg_20_0._attr.isStun or 0

		arg_20_0._attr.isStun = var_20_0 - 1

	@staticmethod
	def IsCloak(arg_21_0):
		return (arg_21_0._attr.isCloak or 0) == 1

	@staticmethod
	def Cloak(arg_22_0):
		arg_22_0._attr.isCloak = 1
		arg_22_0._attr.airResistPierceActive = 1

	@staticmethod
	def Uncloak(arg_23_0):
		arg_23_0._attr.isCloak = 0
		arg_23_0._attr.airResistPierceActive = 0

	@staticmethod
	def IsLockAimBias(arg_24_0):
		return (arg_24_0._attr.lockAimBias or 0) >= 1

	@staticmethod
	def IsUnitCldImmune(arg_25_0):
		return (arg_25_0._attr.unitCldImmune or 0) >= 1

	@staticmethod
	def UnitCldImmune(arg_26_0):
		var_26_0 = arg_26_0._attr.unitCldImmune or 0

		arg_26_0._attr.unitCldImmune = var_26_0 + 1

	@staticmethod
	def UnitCldEnable(arg_27_0):
		var_27_0 = arg_27_0._attr.unitCldImmune or 0

		arg_27_0._attr.unitCldImmune = var_27_0 - 1

	@staticmethod
	def GetCurrentTargetSelect(arg_28_0):
		var_28_0
		var_28_1 = BattleAttr.GetCurrent(arg_28_0, "TargetChoise")
		var_28_2 = BattleConfig.TARGET_SELECT_PRIORITY

		for iter_28_0, iter_28_1 in var_28_1.ivalues():
			if not var_28_0 or var_28_2[iter_28_1] > var_28_2[var_28_0]:
				var_28_0 = iter_28_1

		return var_28_0

	@staticmethod
	def AddTargetSelect(arg_29_0, arg_29_1):
		table.insert(BattleAttr.GetCurrent(arg_29_0, "TargetChoise"), arg_29_1)

	@staticmethod
	def RemoveTargetSelect(arg_30_0, arg_30_1):
		var_30_0 = BattleAttr.GetCurrent(arg_30_0, "TargetChoise")

		for iter_30_0, iter_30_1 in table.ipairs(var_30_0):
			if iter_30_1 == arg_30_1:
				table.remove(var_30_0, iter_30_0)

				break

	@staticmethod
	def GetCurrentGuardianID(arg_31_0):
		var_31_0 = BattleAttr.GetCurrent(arg_31_0, "guardian")
		var_31_1 = len(var_31_0)

		if var_31_1 == 0:
			return None
		else:
			return var_31_0[var_31_1]

	@staticmethod
	def AddGuardianID(arg_32_0, arg_32_1):
		var_32_0 = BattleAttr.GetCurrent(arg_32_0, "guardian")

		if not table.contains(var_32_0, arg_32_1):
			table.insert(var_32_0, arg_32_1)

	@staticmethod
	def RemoveGuardianID(arg_33_0, arg_33_1):
		var_33_0 = BattleAttr.GetCurrent(arg_33_0, "guardian")

		for iter_33_0, iter_33_1 in table.ipairs(var_33_0):
			if iter_33_1 == arg_33_1:
				table.remove(var_33_0, iter_33_0)

				return

	@staticmethod
	def SetPlayerAttrFromOutBattle(arg_34_0, arg_34_1, arg_34_2):
		var_34_0 = arg_34_0._attr or {}

		arg_34_0._attr = var_34_0
		var_34_0.id = arg_34_1.id
		var_34_0.battleUID = arg_34_0.GetUniqueID()
		var_34_0.level = arg_34_1.level
		var_34_0.formulaLevel = arg_34_1.level
		var_34_0.maxHP = arg_34_1.durability
		var_34_0.HPRate = 1
		var_34_0.DMGRate = 0
		var_34_0.cannonPower = arg_34_1.cannon
		var_34_0.torpedoPower = arg_34_1.torpedo
		var_34_0.antiAirPower = arg_34_1.antiaircraft
		var_34_0.antiSubPower = arg_34_1.antisub or 0
		var_34_0.baseAntiSubPower = arg_34_2 and arg_34_2.antisub or arg_34_1.antisub
		var_34_0.airPower = arg_34_1.air
		var_34_0.loadSpeed = arg_34_1.reload
		var_34_0.armorType = arg_34_1.armorType
		var_34_0.attackRating = arg_34_1.hit
		var_34_0.dodgeRate = arg_34_1.dodge
		var_34_0.velocity = BattleFormulas.ConvertShipSpeed(arg_34_1.speed)
		var_34_0.baseVelocity = var_34_0.velocity
		var_34_0.luck = arg_34_1.luck
		var_34_0.repressReduce = arg_34_1.repressReduce or 1
		var_34_0.oxyMax = arg_34_1.oxy_max
		var_34_0.oxyCost = arg_34_1.oxy_cost
		var_34_0.oxyRecovery = arg_34_1.oxy_recovery
		var_34_0.oxyRecoverySurface = arg_34_1.oxy_recovery_surface
		var_34_0.oxyRecoveryBench = arg_34_1.oxy_recovery_bench
		var_34_0.oxyAtkDuration = arg_34_1.attack_duration
		var_34_0.raidDist = arg_34_1.raid_distance
		var_34_0.sonarRange = arg_34_1.sonarRange or 0
		var_34_0.cloakExposeBase = arg_34_2 and arg_34_2.dodge + BattleConfig.CLOAK_EXPOSE_CONST or 0
		var_34_0.cloakExposeExtra = 0
		var_34_0.cloakRestore = var_34_0.cloakExposeBase + var_34_0.cloakExposeExtra + BattleConfig.CLOAK_BASE_RESTORE_DELTA
		var_34_0.cloakRecovery = BattleConfig.CLOAK_RECOVERY
		var_34_0.cloakStrikeAdditive = BattleConfig.CLOAK_STRIKE_ADDITIVE
		var_34_0.cloakBombardAdditive = BattleConfig.CLOAK_STRIKE_ADDITIVE
		var_34_0.airResistPierce = BattleConfig.BASE_ARP
		var_34_0.aimBias = 0
		var_34_0.aimBiasDecaySpeed = 0
		var_34_0.aimBiasDecaySpeedRatio = 0
		var_34_0.aimBiasExtraACC = 0
		var_34_0.healingRate = 1
		var_34_0.DMG_TAG_EHC_N_99 = arg_34_1[AttributeType.AntiSiren] or 0
		var_34_0.comboTag = f"combo_{var_34_0.battleUID}"
		var_34_0.labelTag = {}
		var_34_0.barrageCounterMod = 1
		var_34_0.TargetChoise = {}
		var_34_0.guardian = {}

		BattleAttr.SetBaseAttr(arg_34_0)

	@staticmethod
	def AttrFixer(arg_35_0, arg_35_1):
		if arg_35_0 == SYSTEM_SCENARIO:
			arg_35_1.repressReduce = BattleDataProxy().GetRepressReduce()
		elif arg_35_0 == SYSTEM_DUEL or arg_35_0 == SYSTEM_SHAM:
			var_35_0 = arg_35_1.level
			var_35_1 = arg_35_1.durability
			var_35_2, var_35_3 = BattleDataFunction.GetPlayerUnitDurabilityExtraAddition(arg_35_0, var_35_0)

			arg_35_1.durability = var_35_1 * var_35_2 + var_35_3

	@staticmethod
	def InitDOTAttr(arg_36_0, arg_36_1):
		var_36_0 = BattleConfig.DOT_CONFIG_DEFAULT
		var_36_1 = BattleConfig.DOT_CONFIG

		for iter_36_1 in var_36_1.ivalues():
			for iter_36_2, iter_36_3 in table.pairs(iter_36_1):
				if iter_36_2 == "hit":
					arg_36_0[iter_36_3] = arg_36_1[iter_36_3] or var_36_0[iter_36_2]
				else:
					arg_36_0[iter_36_3] = var_36_0[iter_36_2]

	@staticmethod
	def SetEnemyAttr(arg_37_0, arg_37_1):
		var_37_0 = arg_37_0._tmpData
		var_37_1 = arg_37_0.GetLevel()
		var_37_2 = arg_37_0._attr or {}

		arg_37_0._attr = var_37_2
		var_37_2.battleUID = arg_37_0.GetUniqueID()
		var_37_2.level = var_37_1
		var_37_2.formulaLevel = var_37_1

		var_37_3 = (var_37_1 - 1) / 1000

		var_37_2.maxHP = math.ceil(var_37_0.durability + var_37_0.durability_growth * var_37_3)
		var_37_2.HPRate = 1
		var_37_2.DMGRate = 0
		var_37_2.cannonPower = var_37_0.cannon + var_37_0.cannon_growth * var_37_3
		var_37_2.torpedoPower = var_37_0.torpedo + var_37_0.torpedo_growth * var_37_3
		var_37_2.antiAirPower = var_37_0.antiaircraft + var_37_0.antiaircraft_growth * var_37_3
		var_37_2.airPower = var_37_0.air + var_37_0.air_growth * var_37_3
		var_37_2.antiSubPower = var_37_0.antisub + var_37_0.antisub_growth * var_37_3
		var_37_2.loadSpeed = var_37_0.reload + var_37_0.reload_growth * var_37_3
		var_37_2.armorType = var_37_0.armor_type
		var_37_2.attackRating = var_37_0.hit + var_37_0.hit_growth * var_37_3
		var_37_2.dodgeRate = var_37_0.dodge + var_37_0.dodge_growth * var_37_3
		var_37_2.velocity = BattleFormulas.ConvertShipSpeed(var_37_0.speed + var_37_0.speed_growth * var_37_3)
		var_37_2.baseVelocity = var_37_2.velocity
		var_37_2.luck = var_37_0.luck + var_37_0.luck_growth * var_37_3
		var_37_2.bulletSpeedRatio = 0
		var_37_2.id = f"enemy_{str(var_37_0.id)}"
		var_37_2.repressReduce = 1
		var_37_2.healingRate = 1
		var_37_2.comboTag = f"combo_{var_37_2.battleUID}"
		var_37_2.labelTag = {}
		var_37_2.TargetChoise = {}
		var_37_2.guardian = {}

		BattleAttr.SetBaseAttr(arg_37_0)

	@staticmethod
	def SetEnemyWorldEnhance(arg_38_0):
		var_38_0 = arg_38_0._tmpData
		var_38_1 = arg_38_0._attr
		var_38_2 = var_38_1.level
		var_38_3 = BattleDataProxy()
		var_38_4 = var_38_0.world_enhancement
		var_38_5 = BattleFormulas

		var_38_1.maxHP = var_38_1.maxHP * var_38_5.WorldEnemyAttrEnhance(var_38_4[1], var_38_2)
		var_38_1.cannonPower = var_38_1.cannonPower * var_38_5.WorldEnemyAttrEnhance(var_38_4[2], var_38_2)
		var_38_1.torpedoPower = var_38_1.torpedoPower * var_38_5.WorldEnemyAttrEnhance(var_38_4[3], var_38_2)
		var_38_1.antiAirPower = var_38_1.antiAirPower * var_38_5.WorldEnemyAttrEnhance(var_38_4[4], var_38_2)
		var_38_1.airPower = var_38_1.airPower * var_38_5.WorldEnemyAttrEnhance(var_38_4[5], var_38_2)
		var_38_1.attackRating = var_38_1.attackRating * var_38_5.WorldEnemyAttrEnhance(var_38_4[6], var_38_2)
		var_38_1.dodgeRate = var_38_1.dodgeRate * var_38_5.WorldEnemyAttrEnhance(var_38_4[7], var_38_2)

		var_38_6 = var_38_3.GetInitData()
		var_38_7, var_38_8, var_38_9 = var_38_5.WorldMapRewardAttrEnhance(var_38_6.EnemyMapRewards, var_38_6.FleetMapRewards)

		var_38_1.cannonPower = var_38_1.cannonPower * (1 + var_38_7)
		var_38_1.torpedoPower = var_38_1.torpedoPower * (1 + var_38_7)
		var_38_1.airPower = var_38_1.airPower * (1 + var_38_7)
		var_38_1.antiAirPower = var_38_1.antiAirPower * (1 + var_38_7)
		var_38_1.antiSubPower = var_38_1.antiSubPower * (1 + var_38_7)
		var_38_1.maxHP = math.ceil(var_38_1.maxHP * (1 + var_38_8))
		var_38_1.worldBuffResistance = var_38_9

		BattleAttr.SetBaseAttr(arg_38_0)

	@staticmethod
	def SetMinionAttr(arg_39_0, arg_39_1):
		var_39_0 = arg_39_0.GetMaster()
		var_39_1 = BattleAttr.GetAttr(var_39_0)
		var_39_2 = arg_39_0._tmpData
		var_39_3 = var_39_1.level
		var_39_4 = arg_39_0._attr or {}

		arg_39_0._attr = var_39_4
		var_39_4.battleUID = arg_39_0.GetUniqueID()

		for iter_39_0, iter_39_1 in BattleAttr.AttrListInheritance.ivalues():
			var_39_4[iter_39_1] = var_39_1[iter_39_1]

		for iter_39_2, iter_39_3 in table.pairs(var_39_1):
			if BattleAttr.TAG_EHC_KEY in iter_39_2:
				var_39_4[iter_39_2] = iter_39_3

		for iter_39_4, iter_39_5 in table.pairs(var_39_1):
			if BattleAttr.TAG_CRI_EHC_KEY in iter_39_4:
				var_39_4[iter_39_4] = iter_39_5

		var_39_4.id = var_39_1.id
		var_39_4.level = var_39_3
		var_39_4.formulaLevel = var_39_3

		def var_39_5(arg_40_0, arg_40_1):
			var_40_0 = var_39_2[arg_40_0 + "_growth"]

			if var_40_0 != 0:
				var_39_4[arg_40_1] = var_39_1[arg_40_1] * var_40_0 * 0.0001
			else:
				var_39_4[arg_40_1] = var_39_2[arg_40_0]

		var_39_4.HPRate = 1
		var_39_4.DMGRate = 0

		var_39_5("durability", "maxHP")
		var_39_5("cannon", "cannonPower")
		var_39_5("torpedo", "torpedoPower")
		var_39_5("antiaircraft", "antiAirPower")
		var_39_5("air", "airPower")
		var_39_5("antisub", "antiSubPower")
		var_39_5("reload", "loadSpeed")
		var_39_5("hit", "attackRating")
		var_39_5("dodge", "dodgeRate")
		var_39_5("luck", "luck")

		var_39_4.armorType = var_39_2.armor_type

		var_39_5("speed", "velocity")

		var_39_4.velocity = BattleFormulas.ConvertShipSpeed(var_39_4.velocity)
		var_39_4.baseVelocity = var_39_4.velocity
		var_39_4.bulletSpeedRatio = 0
		var_39_4.repressReduce = 1
		var_39_4.healingRate = 1
		var_39_4.comboTag = f"combo_{var_39_4.battleUID}"
		var_39_4.labelTag = {}
		var_39_4.TargetChoise = {}
		var_39_4.guardian = {}

		BattleAttr.SetBaseAttr(arg_39_0)

	@staticmethod
	def IsWorldMapRewardAttrWarning(arg_41_0, arg_41_1):
		for iter_41_0 in range(1, 3):
			#Use api
			if arg_41_1[iter_41_0] / (arg_41_0[iter_41_0] != 0 and arg_41_0[iter_41_0] or 1) < gameset.world_mapbuff_tips.key_value / 10000:
				return True

		return False

	@staticmethod
	def MonsterAttrFixer(arg_42_0, arg_42_1):
		if arg_42_0 == SYSTEM_SCENARIO:
			var_42_0 = BattleDataProxy()
			var_42_1 = var_42_0.IsCompletelyRepress() and var_42_0.GetRepressLevel() or 0
			var_42_2 = BattleAttr.GetCurrent(arg_42_1, "level")

			BattleAttr.SetCurrent(arg_42_1, "formulaLevel", math.max(1, var_42_2 - var_42_1))
		elif arg_42_0 == SYSTEM_WORLD:
			BattleAttr.SetEnemyWorldEnhance(arg_42_1)

	@staticmethod
	def SetAircraftAttFromMother(arg_43_0, arg_43_1):
		var_43_0 = arg_43_0._attr or {}

		arg_43_0._attr = var_43_0
		var_43_0.battleUID = arg_43_0.GetUniqueID()
		var_43_0.hostUID = arg_43_1.GetUniqueID()

		if not type(arg_43_1._attr.id) == str or not "enemy_" in arg_43_1._attr.id:
			var_43_0.id = arg_43_1._attr.id

		var_43_1 = BattleAttr.GetAttr(arg_43_1)

		for iter_43_1 in BattleAttr.AttrListInheritance.ivalues():
			var_43_0[iter_43_1] = var_43_1[iter_43_1]

		for iter_43_2, iter_43_3 in table.pairs(var_43_1):
			if BattleAttr.TAG_EHC_KEY in iter_43_2:
				var_43_0[iter_43_2] = iter_43_3

		for iter_43_4, iter_43_5 in table.pairs(var_43_1):
			if BattleAttr.TAG_CRI_EHC_KEY in iter_43_4:
				var_43_0[iter_43_4] = iter_43_5

		var_43_0.armorType = 0
		var_43_0.velocity = BattleAttr.GetCurrent(arg_43_1, "baseVelocity")
		var_43_0.labelTag = {}
		var_43_0.TargetChoise = {}
		var_43_0.guardian = {}
		var_43_0.comboTag = f"combo_{var_43_0.hostUID}"

	@staticmethod
	def SetAircraftAttFromTemp(arg_44_0):
		arg_44_0._attr = arg_44_0._attr or {}

		var_44_0 = BattleAttr.GetCurrent(arg_44_0, "hiveExtraHP")

		arg_44_0._attr.velocity = arg_44_0._attr.velocity or BattleFormulas.ConvertAircraftSpeed(arg_44_0._tmpData.speed)

		var_44_1 = arg_44_0._attr.level or 1

		arg_44_0._attr.maxHP = arg_44_0._attr.maxHP or arg_44_0._tmpData.max_hp + arg_44_0._tmpData.hp_growth / 1000 * (var_44_1 - 1) + var_44_0
		arg_44_0._attr.crashDMG = arg_44_0._tmpData.crash_DMG
		arg_44_0._attr.dodge = arg_44_0._tmpData.dodge
		arg_44_0._attr.dodgeLimit = arg_44_0._tmpData.dodge_limit

	@staticmethod
	def SetAirFighterAttr(arg_45_0, arg_45_1):
		var_45_0 = arg_45_0._attr or {}

		arg_45_0._attr = var_45_0

		var_45_1 = BattleDataProxy()
		var_45_2 = var_45_1.GetDungeonLevel()

		var_45_0.battleUID = arg_45_0.GetUniqueID()
		var_45_0.hostUID = 0
		var_45_0.id = 0
		var_45_0.level = var_45_2
		var_45_0.formulaLevel = var_45_2

		if var_45_1.IsCompletelyRepress():
			var_45_0.formulaLevel = max(var_45_0.formulaLevel - 10, 1)

		var_45_3 = (var_45_2 - 1) / 1000

		var_45_0.maxHP = math.floor(arg_45_1.max_hp + arg_45_1.hp_growth * var_45_3)
		var_45_0.attackRating = arg_45_1.accuracy + arg_45_1.ACC_growth * var_45_3

		var_45_4 = arg_45_1.attack_power + arg_45_1.AP_growth * var_45_3

		var_45_0.dodge = arg_45_1.dodge
		var_45_0.dodgeLimit = arg_45_1.dodge_limit
		var_45_0.cannonPower = var_45_4
		var_45_0.torpedoPower = var_45_4
		var_45_0.antiAirPower = var_45_4
		var_45_0.antiSubPower = var_45_4
		var_45_0.airPower = var_45_4
		var_45_0.loadSpeed = 0
		var_45_0.armorType = 1
		var_45_0.dodgeRate = 0
		var_45_0.luck = 50
		var_45_0.velocity = BattleFormulas.ConvertAircraftSpeed(arg_45_1.speed)
		var_45_0.repressReduce = 1
		var_45_0.TargetChoise = {}
		var_45_0.guardian = {}
		var_45_0.crashDMG = arg_45_1.crash_DMG

	@staticmethod
	def SetFusionAttrFromElement(arg_46_0, arg_46_1, arg_46_2, arg_46_3):
		var_46_0 = BattleAttr.GetAttr(arg_46_1)
		var_46_1 = var_46_0.level
		var_46_2 = arg_46_0._attr or {}

		arg_46_0._attr = var_46_2
		var_46_2.id = var_46_0.id
		var_46_2.level = var_46_1
		var_46_2.formulaLevel = var_46_1
		var_46_2.battleUID = arg_46_0.GetUniqueID()

		for iter_46_1 in table.ivalues(BattleAttr.AttrListInheritance):
			var_46_2[iter_46_1] = var_46_0[iter_46_1]

		for iter_46_2, iter_46_3 in table.pairs(var_46_0):
			if BattleAttr.TAG_EHC_KEY in iter_46_2:
				var_46_2[iter_46_2] = iter_46_3

		for iter_46_4, iter_46_5 in table.pairs(var_46_0):
			if BattleAttr.TAG_CRI_EHC_KEY in iter_46_4:
				var_46_2[iter_46_4] = iter_46_5

		var_46_3 = arg_46_1.GetHP()

		for iter_46_6, iter_46_7 in table.ipairs(arg_46_2):
			var_46_3 = var_46_3 + iter_46_7.GetHP()

		var_46_2.maxHP = var_46_3
		var_46_2.hpProvideRate = {}
		var_46_2.hpProvideRate[BattleAttr.GetCurrent(arg_46_1, "id")] = arg_46_1.GetHP() / var_46_3

		for iter_46_9 in arg_46_2.ivalues():
			var_46_2.hpProvideRate[BattleAttr.GetCurrent(iter_46_9, "id")] = iter_46_9.GetHP() / var_46_3

		def var_46_4(arg_47_0):
			var_47_0 = arg_46_3[arg_47_0] or 1

			var_46_2[arg_47_0] = BattleAttr.GetCurrent(arg_46_1, arg_47_0) * var_47_0

		var_46_4("cannonPower")
		var_46_4("torpedoPower")
		var_46_4("antiAirPower")
		var_46_4("antiSubPower")
		var_46_4("baseAntiSubPower")
		var_46_4("airPower")
		var_46_4("loadSpeed")
		var_46_4("attackRating")
		var_46_4("dodgeRate")
		var_46_4("luck")
		var_46_4("velocity")
		var_46_4("baseVelocity")

		var_46_2.armorType = BattleAttr.GetCurrent(arg_46_1, "armorType")
		var_46_2.aimBias = 0
		var_46_2.aimBiasDecaySpeed = 0
		var_46_2.aimBiasDecaySpeedRatio = 0
		var_46_2.aimBiasExtraACC = 0
		var_46_2.healingRate = 1
		var_46_2.comboTag = f"combo_{var_46_2.battleUID}"
		var_46_2.labelTag = {}
		var_46_2.barrageCounterMod = 1
		var_46_2.TargetChoise = {}
		var_46_2.guardian = {}

		BattleAttr.SetBaseAttr(arg_46_0)

	@staticmethod
	def FlashByBuff(arg_48_0, arg_48_1, arg_48_2):
		arg_48_0._attr[arg_48_1] = arg_48_2 + (arg_48_0._baseAttr[arg_48_1] or 0)

		if BattleAttr.FROM_TAG_EHC_KEY in arg_48_1:
			var_48_0 = 0

			for iter_48_0, iter_48_1 in table.pairs(arg_48_0._attr):
				if BattleAttr.FROM_TAG_EHC_KEY in iter_48_0 and iter_48_1 != 0:
					var_48_0 = 1

					break

			BattleAttr.SetCurrent(arg_48_0, BattleAttr.FROM_TAG_EHC_KEY, var_48_0)

	@staticmethod
	def FlashVelocity(arg_49_0, arg_49_1, arg_49_2):
		var_49_0 = BattleAttr.GetBase(arg_49_0, "velocity") * 1.8
		var_49_1 = BattleAttr.GetBase(arg_49_0, "velocity") * 0.2
		var_49_2 = arg_49_0._baseAttr.velocity * arg_49_1 + arg_49_2
		var_49_3 = clamp(var_49_2, var_49_1, var_49_0)

		BattleAttr.SetCurrent(arg_49_0, "velocity", var_49_3)

	@staticmethod
	def HasSonar(arg_50_0):
		var_50_0 = arg_50_0.GetTemplate().type

		return BattleConfig.VAN_SONAR_PROPERTY[var_50_0] != None

	@staticmethod
	def SetCurrent(arg_51_0, arg_51_1, arg_51_2):
		arg_51_0._attr[arg_51_1] = arg_51_2

	@staticmethod
	def GetCurrent(arg_52_0, arg_52_1) -> int:
		var_52_0 = BattleAttr.AttributeType.IsPrimalBattleAttr(arg_52_1) or False

		return BattleAttr._attrFunc[var_52_0](arg_52_0, arg_52_1)

	@staticmethod
	def _getPrimalAttr(arg_53_0, arg_53_1):
		return max(arg_53_0._attr[arg_53_1], 0)

	@staticmethod
	def _getSecondaryAttr(arg_54_0, arg_54_1):
		return arg_54_0._attr[arg_54_1] or 0

	_attrFunc = table({
		True: _getPrimalAttr,
		False: _getSecondaryAttr
	})

	@staticmethod
	def GetBase(arg_55_0, arg_55_1):
		return arg_55_0._baseAttr[arg_55_1] or 0

	@staticmethod
	def GetCurrentTags(arg_56_0):
		return arg_56_0._attr.labelTag or {}

	@staticmethod
	def Increase(arg_57_0, arg_57_1, arg_57_2):
		if arg_57_2:
			arg_57_0._attr[arg_57_1] = (arg_57_0._attr[arg_57_1] or 0) + arg_57_2

	@staticmethod
	def RatioIncrease(arg_58_0, arg_58_1, arg_58_2):
		if arg_58_2:
			arg_58_0._attr[arg_58_1] = arg_58_0._attr[arg_58_1] + arg_58_0._baseAttr[arg_58_1] * arg_58_2 / 10000

	@staticmethod
	def GetTagAttr(arg_59_0, arg_59_1, arg_59_2):
		var_59_0 = arg_59_1.GetLabelTag()
		var_59_1 = {}

		for iter_59_0, iter_59_1 in var_59_0.ivalues():
			var_59_1[BattleAttr.TAG_EHC_KEY + iter_59_1] = True

		var_59_2 = 1

		for iter_59_2 in var_59_1.keys():
			var_59_3 = BattleAttr.GetCurrent(arg_59_0, iter_59_2)

			if var_59_3 != 0:
				if arg_59_2:
					var_59_3 = BattleDataFunction.GetLimitAttributeRange(iter_59_2, var_59_3)

				var_59_2 = var_59_2 * (1 + var_59_3)

		if BattleAttr.GetCurrent(arg_59_1, BattleAttr.FROM_TAG_EHC_KEY) > 0:
			var_59_4 = arg_59_0.GetWeaponTempData().attack_attribute
			var_59_5 = BattleAttr.FROM_TAG_EHC_KEY + var_59_4 + "_"
			var_59_6 = BattleAttr.GetCurrentTags(arg_59_0)

			for iter_59_4, iter_59_5 in table.pairs(var_59_6):
				if iter_59_5 > 0:
					var_59_7 = var_59_5 + iter_59_4
					var_59_8 = BattleAttr.GetCurrent(arg_59_1, var_59_7)

					if var_59_8 != 0:
						var_59_2 = var_59_2 * (1 + var_59_8)

		return var_59_2

	@staticmethod
	def GetTagAttrCri(arg_60_0, arg_60_1):
		var_60_0 = arg_60_1.GetLabelTag()
		var_60_1 = {}

		for iter_60_1 in var_60_0.ivalues():
			var_60_1[BattleAttr.TAG_CRI_EHC_KEY + iter_60_1] = True

		var_60_2 = 0

		for iter_60_2 in var_60_1.keys():
			var_60_3 = BattleAttr.GetCurrent(arg_60_0, iter_60_2)

			if var_60_3 != 0:
				var_60_2 = var_60_2 + var_60_3

		return var_60_2

	@staticmethod
	def GetTagAttrCriDmg(arg_61_0, arg_61_1):
		var_61_0 = arg_61_1.GetLabelTag()
		var_61_1 = {}

		for iter_61_1 in var_61_0.ivalues():
			var_61_1[BattleAttr.TAG_CRIDMG_EHC_KEY + iter_61_1] = True

		var_61_2 = 0

		for iter_61_2 in var_61_1.keys():
			var_61_3 = BattleAttr.GetCurrent(arg_61_0, iter_61_2)

			if var_61_3 != 0:
				var_61_2 = var_61_2 + var_61_3

		return var_61_2
