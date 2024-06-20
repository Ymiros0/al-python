import re
from luatable import table, ipairs, pairs, setmetatable
from alsupport import math, Mathf, getCompareFuncByPunctuation, getArithmeticFuncByOperator, tonumber, time
from Vector3 import Vector3



import BattleConst
gameset = pg.gameset #Use api
import BattleAttr
import BattleConfig
import BattleDataFunction
import BattleTargetChoise
from mgr.TimeMgr import TimeMgr
from const import *
AARepeatConf = BattleConfig.AnitAirRepeaterConfig
from BattleState import bfConsts
bulletSpeedCoef = bfConsts.SECONDs / BattleConfig.viewFPS * BattleConfig.BulletSpeedConvertConst
shipSpeedCoef = bfConsts.SECONDs / BattleConfig.calcFPS * BattleConfig.ShipSpeedConvertConst
planeSpeedCoef = bfConsts.SECONDs / BattleConfig.viewFPS * BattleConfig.AircraftSpeedConvertConst
AirstrikeReloadConst = BattleConfig.AIR_ASSIST_RELOAD_RATIO * bfConsts.PERCENT
DamageEnhanceFromShipType = BattleConfig.DAMAGE_ENHANCE_FROM_SHIP_TYPE
AmmoDamageEnhance = BattleConfig.AMMO_DAMAGE_ENHANCE
AmmoDamageReduce = BattleConfig.AMMO_DAMAGE_REDUCE
ShipTypeAccuracyEnhance = BattleConfig.SHIP_TYPE_ACCURACY_ENHANCE


def GetFleetTotalHP(arg_1_0):
	var_1_0 = arg_1_0.GetFlagShip()
	var_1_1 = arg_1_0.GetUnitList()
	var_1_2 = bfConsts.NUM0

	for iter_1_0, iter_1_1 in ipairs(var_1_1):
		if iter_1_1 == var_1_0:
			var_1_2 = var_1_2 + BattleAttr.GetCurrent(iter_1_1, "maxHP") * bfConsts.HP_CONST
		else:
			var_1_2 = var_1_2 + BattleAttr.GetCurrent(iter_1_1, "maxHP")

	return var_1_2

def GetFleetVelocity(arg_2_0):
	var_2_0 = arg_2_0[1]

	if var_2_0:
		var_2_1 = BattleAttr.GetCurrent(var_2_0, "fleetVelocity")

		if var_2_1 > bfConsts.NUM0:
			return var_2_1 * bfConsts.PERCENT

	var_2_2 = bfConsts.NUM0
	var_2_3 = len(arg_2_0)

	for iter_2_0, iter_2_1 in ipairs(arg_2_0):
		var_2_2 = var_2_2 + iter_2_1.GetAttrByName("velocity")

	var_2_4 = bfConsts.NUM1 - bfConsts.SPEED_CONST * (var_2_3 - bfConsts.NUM1)

	return var_2_2 / var_2_3 * var_2_4

def GetFleetReload(arg_3_0):
	var_3_0 = bfConsts.NUM0

	for iter_3_0, iter_3_1 in ipairs(arg_3_0):
		var_3_0 = var_3_0 + iter_3_1.GetReload()

	return var_3_0

def GetFleetTorpedoPower(arg_4_0):
	var_4_0 = bfConsts.NUM0

	for iter_4_0, iter_4_1 in ipairs(arg_4_0):
		var_4_0 = var_4_0 + iter_4_1.GetTorpedoPower()

	return var_4_0

def AttrFixer(arg_5_0, arg_5_1):
	if arg_5_0 == SYSTEM_DUEL:
		var_5_0 = arg_5_1.level
		var_5_1 = arg_5_1.durability
		var_5_2, var_5_3 = BattleDataFunction.GetPlayerUnitDurabilityExtraAddition(arg_5_0, var_5_0)

		arg_5_1.durability = var_5_1 * var_5_2 + var_5_3

def HealFixer(arg_6_0, arg_6_1):
	var_6_0 = 1

	if arg_6_0 == SYSTEM_DUEL:
		var_6_1 = arg_6_1.level

		var_6_0 = BattleDataFunction.GetPlayerUnitDurabilityExtraAddition(arg_6_0, var_6_1)

	return var_6_0

def ConvertShipSpeed(arg_7_0):
	return arg_7_0 * shipSpeedCoef

def ConvertAircraftSpeed(arg_8_0):
	if arg_8_0:
		return arg_8_0 * planeSpeedCoef
	else:
		return None

def ConvertBulletSpeed(arg_9_0):
	return arg_9_0 * bulletSpeedCoef

def ConvertBulletDataSpeed(arg_10_0):
	return arg_10_0 / bulletSpeedCoef

def CreateContextCalculateDamage(is_OpSi):
	def func(bullet, target, decay_factor, dmg_fraction):
		one = bfConsts.NUM1
		zero = bfConsts.NUM0
		tenk = bfConsts.NUM10000
		DRATE = bfConsts.DRATE
		ACC = bfConsts.ACCURACY
		HostAttr = bullet.GetWeaponHostAttr()
		weapon = bullet.GetWeapon()
		weapon_tmp = bullet.GetWeaponTempData()
		atk_attr = weapon_tmp.attack_attribute
		atk_attr_conv = weapon.GetConvertedAtkAttr()
		bullet_tmp = bullet.GetTemplate()
		dmg_type = bullet_tmp.damage_type
		dmg_random = bullet_tmp.random_damage_rate
		target_attr = target._attr
		attr_coef = dmg_fraction or one

		decay_factor = decay_factor or zero

		target_armour = target_attr.armorType
		lvl_adv = HostAttr.formulaLevel - target_attr.formulaLevel
		crit_dmg = one
		crit = False
		eff_wp_dmg = bullet.GetCorrectedDMG() #With coef
		dmg = (one + bullet.GetWeaponAtkAttr() * atk_attr_conv) * eff_wp_dmg

		if atk_attr == BattleConst.WeaponDamageAttr.CANNON:
			attr_coef = one + BattleAttr.GetCurrent(target, "injureRatioByCannon") + BattleAttr.GetCurrent(bullet, "damageRatioByCannon")
		elif atk_attr == BattleConst.WeaponDamageAttr.TORPEDO:
			attr_coef = one + BattleAttr.GetCurrent(target, "injureRatioByBulletTorpedo") + BattleAttr.GetCurrent(bullet, "damageRatioByBulletTorpedo")
		elif atk_attr == BattleConst.WeaponDamageAttr.AIR:
			aa_pierce = BattleAttr.GetCurrent(bullet, "airResistPierceActive") == 1 and BattleAttr.GetCurrent(bullet, "airResistPierce") or 0

			attr_coef = attr_coef * min(DRATE[7] / (target_attr.antiAirPower + DRATE[7]) + aa_pierce, 1) * (one + BattleAttr.GetCurrent(target, "injureRatioByAir") + BattleAttr.GetCurrent(bullet, "damageRatioByAir"))
		elif atk_attr == BattleConst.WeaponDamageAttr.ANTI_AIR:
			pass #block empty
		elif atk_attr == BattleConst.WeaponDamageAttr.ANIT_SUB:
			pass #block empty

		luck_adv = HostAttr.luck - target_attr.luck
		immu = BattleAttr.GetCurrent(target, "perfectDodge")
		host_acc = max(HostAttr.attackRating, 0)

		if immu == 1:
			missed = True
		else:
			base_hit_rate = ACC[1] + host_acc / (host_acc + target_attr.dodgeRate + ACC[2]) + (luck_adv + lvl_adv) * bfConsts.PERCENT1
			target_extra_hit_rate = BattleAttr.GetCurrent(target, "accuracyRateExtra")
			hit_rate_by_target_type = BattleAttr.GetCurrent(bullet, ShipTypeAccuracyEnhance[target.GetTemplate().type])
			target_extra_eva_rate = BattleAttr.GetCurrent(target, "dodgeRateExtra")
			final_hit_rate = max(DRATE[5], min(one, base_hit_rate + target_extra_hit_rate + hit_rate_by_target_type - target_extra_eva_rate))

			missed = not IsHappen(final_hit_rate * tenk)

		if not missed:
			crit_rate = BattleAttr.GetCurrent(bullet, "GCT") == 1 and 1 or bfConsts.DFT_CRIT_RATE + host_acc / (host_acc + target_attr.dodgeRate + DRATE[4]) + (luck_adv + lvl_adv) * DRATE[3] + BattleAttr.GetCurrent(bullet, "cri") + BattleAttr.GetTagAttrCri(bullet, target)

			dmg += math.random(BattleConfig.RANDOM_DAMAGE_MIN, BattleConfig.RANDOM_DAMAGE_MAX)

			if IsHappen(crit_rate * tenk):
				crit = True

				crit_dmg = bfConsts.DFT_CRIT_EFFECT + BattleAttr.GetTagAttrCriDmg(bullet, target) + BattleAttr.GetCurrent(bullet, "criDamage") - BattleAttr.GetCurrent(target, "criDamageResist")

				crit_dmg = math.max(1, crit_dmg)
			else:
				crit = False
		else:
			dmg = zero

			event = table(
				isMiss = True,
				isDamagePrevent = False,
				isCri = crit
			)

			return dmg, event

		one_2 = bfConsts.NUM1
		dRB = BattleAttr.GetCurrent(bullet, "damageRatioBullet")
		hunter_coef = BattleAttr.GetTagAttr(bullet, target, is_OpSi)
		target_iR = BattleAttr.GetCurrent(target, "injureRatio")
		armour_mod = (weapon.GetFixAmmo() or dmg_type[target_armour] or one_2) + BattleAttr.GetCurrent(bullet, BattleConfig.DAMAGE_AMMO_TO_ARMOR_RATE_ENHANCE[target_armour])
		armour_coef = BattleAttr.GetCurrent(bullet, BattleConfig.DAMAGE_TO_ARMOR_RATE_ENHANCE[target_armour])
		ammo_rate = BattleAttr.GetCurrent(bullet, AmmoDamageEnhance[bullet_tmp.ammo_type])
		target_ammo_red = BattleAttr.GetCurrent(target, AmmoDamageReduce[bullet_tmp.ammo_type])
		comboTag = BattleAttr.GetCurrent(bullet, "comboTag")
		combo = BattleAttr.GetCurrent(target, comboTag)
		dmg = math.max(one_2, math.floor(dmg * attr_coef * (one_2 - decay_factor) * armour_mod * (one_2 + armour_coef) * crit_dmg * (one_2 + dRB) * hunter_coef * (one_2 + target_iR) * (one_2 + ammo_rate - target_ammo_red) * (one_2 + combo) * (one_2 + math.min(DRATE[1], math.max(-DRATE[1], lvl_adv)) * DRATE[2])))

		if target.GetCurrentOxyState() == BattleConst.OXY_STATE.DIVE:
			dmg = math.floor(dmg * bullet_tmp.antisub_enhancement)

		event = table(
			isMiss = missed,
			isCri = crit,
			damageAttr = atk_attr
		)
		var_12_50 = bullet.GetDamageEnhance()

		if var_12_50 != 1:
			dmg = math.floor(dmg * var_12_50)

		dmg *= target_attr.repressReduce

		if dmg_random != 0:
			dmg *= (Mathf.RandomFloat(dmg_random) + 1)

		dmg_enh_proj = BattleAttr.GetCurrent(bullet, "damageEnhanceProjectile")
		dmg = math.max(0, dmg + dmg_enh_proj)

		if is_OpSi:
			dmg *= (bfConsts.NUM1 + BattleAttr.GetCurrent(bullet, "worldBuffResistance"))

		dmg = math.floor(dmg)
		font = bullet_tmp.DMG_font[target_armour]

		if dmg_enh_proj < 0:
			font = BattleConfig.BULLET_DECREASE_DMG_FONT

		return dmg, event, font
	return func

def CalculateIgniteDamage(arg_13_0, arg_13_1, arg_13_2):
	var_13_0 = arg_13_0._attr

	return arg_13_0.GetWeapon().GetCorrectedDMG() * (1 + var_13_0[arg_13_1] * bfConsts.PERCENT) * arg_13_2

def WeaponDamagePreCorrection(arg_14_0, arg_14_1):
	var_14_0 = arg_14_0.GetTemplateData()
	var_14_1 = arg_14_1 or var_14_0.damage
	var_14_2 = var_14_0.corrected

	return var_14_1 * arg_14_0.GetPotential() * var_14_2 * bfConsts.PERCENT

def WeaponAtkAttrPreRatio(arg_15_0):
	return arg_15_0.GetTemplateData().attack_attribute_ratio * bfConsts.PERCENT2

def GetMeteoDamageRatio(arg_16_0):
	var_16_0 = table()
	var_16_1 = bfConsts.METEO_RATE
	var_16_2 = var_16_1[1]

	if arg_16_0 >= var_16_1[2]:
		for iter_16_0 in range(len(arg_16_0)):
			var_16_0[iter_16_0] = var_16_2

		return var_16_0
	else:
		var_16_3 = 1 - var_16_2 * arg_16_0

		for iter_16_1 in range(arg_16_0):
			var_16_4 = math.random() * var_16_3 * (var_16_1[3] + var_16_1[4] * (iter_16_1 - 1) / arg_16_0)

			var_16_0[iter_16_1] = var_16_4 + var_16_2
			var_16_3 = math.max(0, var_16_3 - var_16_4)

		var_16_0[arg_16_0 + 1] = var_16_3

		return var_16_0

def CalculateFleetAntiAirTotalDamage(arg_17_0):
	var_17_0 = arg_17_0.GetCrewUnitList()
	var_17_1 = 0

	for iter_17_0, iter_17_1 in pairs(var_17_0):
		var_17_2 = BattleAttr.GetCurrent(iter_17_0, "antiAirPower")

		for iter_17_2, iter_17_3 in ipairs(iter_17_1):
			var_17_3 = iter_17_3.GetConvertedAtkAttr()
			var_17_4 = iter_17_3.GetCorrectedDMG()

			var_17_1 = var_17_1 + math.max(1, (var_17_2 * var_17_3 + 1) * var_17_4)

	return var_17_1

def CalculateRepaterAnitiAirTotalDamage(arg_18_0):
	var_18_0 = arg_18_0.GetHost()
	var_18_1 = arg_18_0.GetConvertedAtkAttr()
	var_18_2 = arg_18_0.GetCorrectedDMG()
	var_18_3 = BattleAttr.GetCurrent(var_18_0, "antiAirPower")

	return (math.max(1, (var_18_3 * var_18_1 + 1) * var_18_2))

def RollRepeaterHitDice(arg_19_0, arg_19_1):
	var_19_0 = arg_19_0.GetHost()
	var_19_1 = BattleAttr.GetCurrent(var_19_0, "antiAirPower")
	var_19_2 = math.max(BattleAttr.GetCurrent(var_19_0, "attackRating"), 0)
	var_19_3 = BattleAttr.GetCurrent(arg_19_1, "airPower")
	var_19_4 = BattleAttr.GetCurrent(arg_19_1, "dodgeLimit")
	var_19_5 = BattleAttr.GetCurrent(arg_19_1, "immu")
	var_19_6 = var_19_3 / AARepeatConf.const_A + AARepeatConf.const_B
	var_19_7 = var_19_6 / (var_19_1 * var_19_5 + var_19_6 + AARepeatConf.const_C)
	var_19_8 = math.min(var_19_4, var_19_7)

	return IsHappen(var_19_8 * bfConsts.NUM10000)

def AntiAirPowerWeight(arg_20_0):
	return arg_20_0 * arg_20_0

def CalculateDamageFromAircraftToMainShip(arg_21_0, arg_21_1):
	var_21_0 = BattleAttr.GetCurrent(arg_21_0, "airPower")
	var_21_1 = BattleAttr.GetCurrent(arg_21_1, "antiAirPower")
	var_21_2 = BattleAttr.GetCurrent(arg_21_0, "crashDMG")
	var_21_3 = arg_21_0.GetHPRate()
	var_21_4 = BattleAttr.GetCurrent(arg_21_0, "formulaLevel")
	var_21_5 = BattleAttr.GetCurrent(arg_21_1, "formulaLevel")
	var_21_6 = BattleAttr.GetCurrent(arg_21_1, "injureRatio")
	var_21_7 = BattleAttr.GetCurrent(arg_21_1, "injureRatioByAir")
	var_21_8 = bfConsts.PLANE_LEAK_RATE
	var_21_9 = math.max(var_21_8[1], math.floor((var_21_2 * (var_21_8[2] + var_21_0 * var_21_8[3]) + var_21_4 * var_21_8[4]) * (var_21_3 * var_21_8[5] + var_21_8[6]) * (var_21_8[7] + (var_21_4 - var_21_5) * var_21_8[8]) * (var_21_8[9] / (var_21_1 + var_21_8[10])) * (var_21_8[11] + var_21_6) * (var_21_8[12] + var_21_7)))

	return (math.floor(var_21_9 * BattleAttr.GetCurrent(arg_21_1, "repressReduce")))

def CalculateDamageFromShipToMainShip(arg_22_0, arg_22_1):
	var_22_0 = BattleAttr.GetCurrent(arg_22_0, "cannonPower")
	var_22_1 = BattleAttr.GetCurrent(arg_22_0, "torpedoPower")
	var_22_2 = arg_22_0.GetHPRate()
	var_22_3 = BattleAttr.GetCurrent(arg_22_0, "formulaLevel")
	var_22_4 = BattleAttr.GetCurrent(arg_22_1, "formulaLevel")
	var_22_5 = BattleAttr.GetCurrent(arg_22_1, "injureRatio")
	var_22_6 = bfConsts.LEAK_RATE
	var_22_7 = math.max(var_22_6[1], math.floor(((var_22_0 + var_22_1) * var_22_6[2] + var_22_3 * var_22_6[7]) * (var_22_6[5] + var_22_5) * (var_22_2 * var_22_6[3] + var_22_6[4]) * (var_22_6[5] + (var_22_3 - var_22_4) * var_22_6[6])))

	return (math.floor(var_22_7 * BattleAttr.GetCurrent(arg_22_1, "repressReduce")))

def CalculateDamageFromSubmarinToMainShip(arg_23_0, arg_23_1):
	var_23_0 = BattleAttr.GetCurrent(arg_23_0, "torpedoPower")
	var_23_1 = arg_23_0.GetHPRate()
	var_23_2 = BattleAttr.GetCurrent(arg_23_0, "formulaLevel")
	var_23_3 = BattleAttr.GetCurrent(arg_23_1, "formulaLevel")
	var_23_4 = BattleAttr.GetCurrent(arg_23_1, "injureRatio")
	var_23_5 = bfConsts.SUBMARINE_KAMIKAZE

	return (math.max(var_23_5[1], math.floor((var_23_0 * var_23_5[2] + var_23_2 * var_23_5[3]) * (var_23_5[4] + var_23_4) * (var_23_1 * var_23_5[5] + var_23_5[6]) * (var_23_5[7] + (var_23_2 - var_23_3) * var_23_5[8]))))

def RollSubmarineDualDice(arg_24_0):
	var_24_0 = BattleAttr.GetCurrent(arg_24_0, "dodgeRate")
	var_24_1 = var_24_0 / (var_24_0 + BattleConfig.MONSTER_SUB_KAMIKAZE_DUAL_K) * BattleConfig.MONSTER_SUB_KAMIKAZE_DUAL_P

	return IsHappen(var_24_1 * bfConsts.NUM10000)

def CalculateCrashDamage(arg_25_0, arg_25_1):
	var_25_0 = BattleAttr.GetCurrent(arg_25_0, "maxHP")
	var_25_1 = BattleAttr.GetCurrent(arg_25_1, "maxHP")
	var_25_2 = var_25_0 * bfConsts.CRASH_RATE[1]
	var_25_3 = var_25_1 * bfConsts.CRASH_RATE[1]
	var_25_4 = BattleAttr.GetCurrent(arg_25_0, "hammerDamageRatio")
	var_25_5 = BattleAttr.GetCurrent(arg_25_1, "hammerDamageRatio")
	var_25_6 = BattleAttr.GetCurrent(arg_25_0, "hammerDamagePrevent")
	var_25_7 = BattleAttr.GetCurrent(arg_25_1, "hammerDamagePrevent")
	var_25_8 = math.min(var_25_6, BattleConfig.HammerCFG.PreventUpperBound)
	var_25_9 = math.min(var_25_7, BattleConfig.HammerCFG.PreventUpperBound)
	var_25_10 = math.sqrt(var_25_0 * var_25_1) * bfConsts.CRASH_RATE[2]
	var_25_11 = math.min(var_25_2, var_25_10)
	var_25_12 = math.min(var_25_3, var_25_10)
	var_25_13 = math.floor(var_25_11 * (1 + var_25_5) * (1 - var_25_8))
	var_25_14 = math.floor(var_25_13 * BattleAttr.GetCurrent(arg_25_0, "repressReduce"))
	var_25_15 = math.floor(var_25_12 * (1 + var_25_4) * (1 - var_25_9))
	var_25_16 = math.floor(var_25_15 * BattleAttr.GetCurrent(arg_25_1, "repressReduce"))

	return var_25_14, var_25_16

def CalculateFleetDamage(arg_26_0):
	return arg_26_0 * bfConsts.SCORE_RATE[1]

def CalculateFleetOverDamage(arg_27_0, arg_27_1):
	if arg_27_1 == arg_27_0.GetFlagShip():
		return BattleAttr.GetCurrent(arg_27_1, "maxHP") * bfConsts.SCORE_RATE[2]
	else:
		return BattleAttr.GetCurrent(arg_27_1, "maxHP") * bfConsts.SCORE_RATE[3]

def CalculateReloadTime(arg_28_0, arg_28_1):
	return arg_28_0 / BattleConfig.K1 / math.sqrt((arg_28_1 + BattleConfig.K2) * BattleConfig.K3)

def CaclulateReloaded(arg_29_0, arg_29_1):
	return math.sqrt((arg_29_1 + BattleConfig.K2) * BattleConfig.K3) * arg_29_0 * BattleConfig.K1

def CaclulateReloadAttr(arg_30_0, arg_30_1):
	var_30_0 = arg_30_0 / BattleConfig.K1 / arg_30_1

	return math.max(var_30_0 * var_30_0 / BattleConfig.K3 - BattleConfig.K2, 0)

def CaclulateAirAssistReloadMax(arg_31_0):
	var_31_0 = 0

	for iter_31_0, iter_31_1 in ipairs(arg_31_0):
		var_31_0 = var_31_0 + iter_31_1.GetTemplateData().reload_max

	return var_31_0 / len(arg_31_0) * AirstrikeReloadConst

def CaclulateDOTPlace(arg_32_0, arg_32_1, arg_32_2, arg_32_3):
	var_32_0 = arg_32_1.arg_list

	if var_32_0.tagOnly and not arg_32_3.ContainsLabelTag(var_32_0.tagOnly):
		return False

	var_32_1 = BattleConfig.DOT_CONFIG[var_32_0.dotType]
	var_32_2 = arg_32_2 and arg_32_2.GetAttrByName(var_32_1.hit) or bfConsts.NUM0
	var_32_3 = arg_32_3 and arg_32_3.GetAttrByName(var_32_1.resist) or bfConsts.NUM0

	return IsHappen(arg_32_0 * (bfConsts.NUM1 + var_32_2) * (bfConsts.NUM1 - var_32_3))

def CaclulateDOTDuration(arg_33_0, arg_33_1, arg_33_2):
	var_33_0 = arg_33_0.arg_list
	var_33_1 = BattleConfig.DOT_CONFIG[var_33_0.dotType]

	return (arg_33_1 and arg_33_1.GetAttrByName(var_33_1.prolong) or bfConsts.NUM0) - (arg_33_2 and arg_33_2.GetAttrByName(var_33_1.shorten) or bfConsts.NUM0)

def CaclulateDOTDamageEnhanceRate(arg_34_0, arg_34_1, arg_34_2):
	var_34_0 = arg_34_0.arg_list
	var_34_1 = BattleConfig.DOT_CONFIG[var_34_0.dotType]

	return ((arg_34_1 and arg_34_1.GetAttrByName(var_34_1.enhance) or bfConsts.NUM0) - (arg_34_2 and arg_34_2.GetAttrByName(var_34_1.reduce) or bfConsts.NUM0)) * bfConsts.PERCENT2

def CaclulateMetaDotaDamage(arg_35_0, arg_35_1):
	var_35_0 = BattleDataFunction.GetMetaBossTemplate(arg_35_0)

	if type(var_35_0.state) == str:
		return 0

	var_35_1 = var_35_0.state
	var_35_2 = time(table(
		year = var_35_1[1][1][1],
		month = var_35_1[1][1][2],
		day = var_35_1[1][1][3],
		hour = var_35_1[1][2][1],
		minute = var_35_1[1][2][2],
		second = var_35_1[1][2][3]
	))
	var_35_3 = time(table(
		year = var_35_1[2][1][1],
		month = var_35_1[2][1][2],
		day = var_35_1[2][1][3],
		hour = var_35_1[2][2][1],
		minute = var_35_1[2][2][2],
		second = var_35_1[2][2][3]
	))
	var_35_4 = var_35_3 - var_35_2
	var_35_5 = math.floor(var_35_4 / 86400)
	var_35_6 = math.floor((TimeMgr().GetServerTime() - var_35_2) / 86400)
	var_35_7 = gameset.world_metaboss_supportattack.description
	var_35_8 = var_35_7[1]
	var_35_9 = var_35_5 - var_35_7[2]
	var_35_10 = var_35_7[3]
	var_35_11 = var_35_7[4]
	var_35_12 = var_35_7[5]
	var_35_13 = BattleDataFunction.GetMetaBossLevelTemplate(arg_35_0, arg_35_1).hp
	var_35_14 = math.floor(var_35_13 * var_35_10 / var_35_12 / (1 + 0.5 * var_35_11) / (var_35_9 - var_35_8) * math.min(var_35_6 - var_35_8 + 1, var_35_9 - var_35_8))

	return var_35_14 + math.random(math.floor(var_35_11 * var_35_14))

def CalculateMaxAimBiasRange(arg_36_0):
	var_36_0 = BattleConfig.AIM_BIAS_FLEET_RANGE_MOD
	var_36_1

	if len(arg_36_0) == 1:
		var_36_2 = arg_36_0[1]

		var_36_1 = BattleAttr.GetCurrent(arg_36_0[1], "dodgeRate") * var_36_0
	else:
		var_36_3 = table()

		for iter_36_0, iter_36_1 in ipairs(arg_36_0):
			table.insert(var_36_3, BattleAttr.GetCurrent(iter_36_1, "dodgeRate"))

		table.sort(var_36_3, lambda a,b: b-a)

		var_36_1 = (var_36_3[1] + var_36_3[2] * 0.6 + (var_36_3[3] or 0) * 0.3) / len(var_36_3) * var_36_0

	return (math.min(var_36_1, BattleConfig.AIM_BIAS_MAX_RANGE_SCOUT))

def CalculateMaxAimBiasRangeSub(arg_38_0):
	var_38_0 = BattleAttr.GetCurrent(arg_38_0[1], "dodgeRate") * BattleConfig.AIM_BIAS_SUB_RANGE_MOD

	return (math.min(var_38_0, BattleConfig.AIM_BIAS_MAX_RANGE_SUB))

def CalculateMaxAimBiasRangeMonster(arg_39_0):
	var_39_0 = BattleAttr.GetCurrent(arg_39_0[1], "dodgeRate") * BattleConfig.AIM_BIAS_MONSTER_RANGE_MOD

	return (math.min(var_39_0, BattleConfig.AIM_BIAS_MAX_RANGE_MONSTER))

def CalculateBiasDecay(arg_40_0):
	var_40_0 = arg_40_0 * BattleConfig.AIM_BIAS_DECAY_MOD_MONSTER

	return (math.min(var_40_0, BattleConfig.AIM_BIAS_DECAY_SPEED_MAX_SCOUT))

def CalculateBiasDecayMonster(arg_41_0):
	var_41_0 = arg_41_0 * BattleConfig.AIM_BIAS_DECAY_MOD

	return (math.min(var_41_0, BattleConfig.AIM_BIAS_DECAY_SPEED_MAX_MONSTER))

def CalculateBiasDecayMonsterInSmoke(arg_42_0):
	var_42_0 = arg_42_0 * BattleConfig.AIM_BIAS_DECAY_MOD * BattleConfig.AIM_BIAS_DECAY_SMOKE

	return (math.min(var_42_0, BattleConfig.AIM_BIAS_DECAY_SPEED_MAX_MONSTER))

def CalculateBiasDecayDiving(arg_43_0):
	var_43_0 = math.max(0, arg_43_0 - BattleConfig.AIM_BIAS_DECAY_SUB_CONST) * BattleConfig.AIM_BIAS_DECAY_MOD

	return (math.min(var_43_0, BattleConfig.AIM_BIAS_DECAY_SPEED_MAX_SUB))

def WorldEnemyAttrEnhance(arg_44_0, arg_44_1):
	return 1 + arg_44_0 / (1 + BattleConfig.WORLD_ENEMY_ENHANCEMENT_CONST_C^(BattleConfig.WORLD_ENEMY_ENHANCEMENT_CONST_B - arg_44_1))


var_0_15 = setmetatable(table(), table(
	__index = lambda a,b: 0
))

def WorldMapRewardAttrEnhance(arg_46_0, arg_46_1):
	arg_46_0 = arg_46_0 or var_0_15
	arg_46_1 = arg_46_1 or var_0_15

	var_46_3 = table(
		table(
			gameset.attr_world_value_X1.key_value / 10000,
			gameset.attr_world_value_X2.key_value / 10000
		),
		table(
			gameset.attr_world_value_Y1.key_value / 10000,
			gameset.attr_world_value_Y2.key_value / 10000
		),
		table(
			gameset.attr_world_value_Z1.key_value / 10000,
			gameset.attr_world_value_Z2.key_value / 10000
		)
	)
	var_46_4 = gameset.attr_world_damage_fix.key_value / 10000
	var_46_5

	if arg_46_0[1] == 0:
		var_46_5 = var_46_3[1][2]
	else:
		var_46_5 = arg_46_1[1] / arg_46_0[1]

	var_46_6 = 1 - math.clamp(var_46_5, var_46_3[1][1], var_46_3[1][2])

	if arg_46_0[2] == 0:
		var_46_5 = var_46_3[2][2]
	else:
		var_46_5 = arg_46_1[2] / arg_46_0[2]

	var_46_7 = 1 - math.clamp(var_46_5, var_46_3[2][1], var_46_3[2][2])

	if arg_46_0[3] == 0:
		var_46_5 = var_46_3[3][2]
	else:
		var_46_5 = arg_46_1[3] / arg_46_0[3]

	var_46_8 = math.max(1 - math.clamp(var_46_5, var_46_3[3][1], var_46_3[3][2]), -var_46_4)

	return var_46_6, var_46_7, var_46_8

def WorldMapRewardHealingRate(arg_47_0, arg_47_1):
	var_47_0 = table(
		gameset.attr_world_value_H1.key_value / 10000,
		gameset.attr_world_value_H2.key_value / 10000
	)

	arg_47_0 = arg_47_0 or var_0_15
	arg_47_1 = arg_47_1 or var_0_15

	var_47_1

	if arg_47_0[3] == 0:
		var_47_1 = var_47_0[2]
	else:
		var_47_1 = arg_47_1[3] / arg_47_0[3]

	return math.clamp(var_47_1, var_47_0[1], var_47_0[2])

def CalcDamageLock():
	return 0, table(
		False,
		True,
		False
	)

def CalcDamageLockA2M():
	return 0

def CalcDamageLockS2M():
	return 0

def CalcDamageLockCrush():
	return 0, 0

def UNoneateralCrush():
	return 0, 100000

def FriendInvincibleDamage(arg_53_0, arg_53_1, *args):
	var_53_0 = arg_53_1.GetIFF()

	if var_53_0 == BattleConfig.FRIENDLY_CODE:
		return 1, table(
			isMiss = False,
			isCri = False,
			isDamagePrevent = False
		)
	elif var_53_0 == BattleConfig.FOE_CODE:
		raise UnboundLocalError('CalculateDamage called but never defined')
		return CalculateDamage(arg_53_0, arg_53_1, *args) #????? Does this function even work in the game

def FriendInvincibleCrashDamage(arg_54_0, arg_54_1):
	var_54_0, var_54_1 = CalculateCrashDamage(arg_54_0, arg_54_1)
	var_54_2 = 1

	var_54_1 = arg_54_1.GetIFF() == BattleConfig.FRIENDLY_CODE and 1 or var_54_1

	return var_54_2, var_54_1

def ChapterRepressReduce(arg_55_0):
	return 1 - arg_55_0 * 0.01

def IsHappen(arg_56_0):
	if arg_56_0 <= 0:
		return False
	elif arg_56_0 >= 10000:
		return True
	else:
		return arg_56_0 >= math.random(10000)

def WeightRandom(arg_57_0):
	var_57_0, var_57_1 = GenerateWeightList(arg_57_0)

	return (WeightListRandom(var_57_0, var_57_1))

def WeightListRandom(arg_58_0, arg_58_1):
	var_58_0 = math.random(0, arg_58_1)

	for iter_58_0, iter_58_1 in pairs(arg_58_0):
		var_58_1 = iter_58_0.min
		var_58_2 = iter_58_0.max

		if var_58_1 <= var_58_0 and var_58_0 <= var_58_2:
			return iter_58_1

def GenerateWeightList(arg_59_0):
	var_59_0 = table()
	var_59_1 = -1

	for iter_59_0, iter_59_1 in ipairs(arg_59_0):
		var_59_2 = iter_59_1.weight
		var_59_3 = iter_59_1.rst
		var_59_4 = var_59_1 + 1

		var_59_1 = var_59_1 + var_59_2

		var_59_6 = var_59_1

		var_59_0[table(
			min = var_59_4,
			max = var_59_6
		)] = var_59_3

	return var_59_0, var_59_1

def IsListHappen(arg_60_0):
	for iter_60_0, iter_60_1 in ipairs(arg_60_0):
		if IsHappen(iter_60_1[1]):
			return True, iter_60_1[2]

	return False, None

def BulletYAngle(arg_61_0, arg_61_1):
	return math.rad2Deg * math.atan2(arg_61_1.z - arg_61_0.z, arg_61_1.x - arg_61_0.x)

def RandomPosNull(arg_62_0, arg_62_1):
	arg_62_1 = arg_62_1 or 10

	var_62_0 = arg_62_0.distance or 10
	var_62_1 = var_62_0 * var_62_0
	var_62_2 = BattleTargetChoise.TargetAll()

	for iter_62_0 in range(1, arg_62_1):
		var_62_5 = True
		var_62_6 = RandomPos(arg_62_0)

		for iter_62_1, iter_62_2 in pairs(var_62_2):
			var_62_7 = iter_62_2.GetPosition()

			if var_62_1 > Vector3.SqrDistance(var_62_6, var_62_7):
				var_62_5 = False

				break

		if var_62_5:
			return var_62_6

	return None

def RandomPos(arg_63_0):
	var_63_0 = arg_63_0[1] or 0
	var_63_1 = arg_63_0[2] or 0
	var_63_2 = arg_63_0[3] or 0

	if arg_63_0.rangeX or arg_63_0.rangeY or arg_63_0.rangeZ:
		var_63_3 = RandomDelta(arg_63_0.rangeX)
		var_63_4 = RandomDelta(arg_63_0.rangeY)
		var_63_5 = RandomDelta(arg_63_0.rangeZ)

		return Vector3(var_63_0 + var_63_3, var_63_1 + var_63_4, var_63_2 + var_63_5)
	else:
		var_63_6 = RandomPosXYZ(arg_63_0, "X1", "X2")
		var_63_7 = RandomPosXYZ(arg_63_0, "Y1", "Y2")
		var_63_8 = RandomPosXYZ(arg_63_0, "Z1", "Z2")

		return Vector3(var_63_0 + var_63_6, var_63_1 + var_63_7, var_63_2 + var_63_8)

def RandomPosXYZ(arg_64_0, arg_64_1, arg_64_2):
	arg_64_1 = arg_64_0[arg_64_1]
	arg_64_2 = arg_64_0[arg_64_2]

	if arg_64_1 and arg_64_2:
		return math.random(arg_64_1, arg_64_2)
	else:
		return 0

def RandomPosCenterRange(arg_65_0):
	var_65_0 = RandomDelta(arg_65_0.rangeX)
	var_65_1 = RandomDelta(arg_65_0.rangeY)
	var_65_2 = RandomDelta(arg_65_0.rangeZ)

	return Vector3(var_65_0, var_65_1, var_65_2)

def RandomDelta(arg_66_0):
	if arg_66_0 and arg_66_0 > 0:
		return math.random(arg_66_0 + arg_66_0) - arg_66_0
	else:
		return 0

def simpleCompare(arg_67_0, arg_67_1):
	var_67_2, var_67_3 = re.search(r'([^\w\s]+)(.*)',arg_67_0).groups()
	var_67_4 = getCompareFuncByPunctuation(var_67_2)
	var_67_5 = tonumber(var_67_3)

	return var_67_4(arg_67_1, var_67_5)

def parseCompareUnitAttr(arg_68_0, arg_68_1, arg_68_2):
	var_68_3, var_68_2, var_68_4 = re.search(r'([\w\s]+)([^\w\s]+)(.*)',arg_68_0).groups()
	var_68_5 = getCompareFuncByPunctuation(var_68_2)
	var_68_6 = tonumber(var_68_3) or arg_68_1.GetAttrByName(var_68_3)
	var_68_7 = tonumber(var_68_4) or arg_68_2.GetAttrByName(var_68_4)

	return var_68_5(var_68_6, var_68_7)

def parseCompareUnitTemplate(arg_69_0, arg_69_1, arg_69_2):
	var_69_3, var_69_2, var_69_4 = re.search(r'([\w\s]+)([^\w\s]+)(.*)',arg_69_0).groups()
	var_69_5 = getCompareFuncByPunctuation(var_69_2)
	var_69_6 = tonumber(var_69_3) or arg_69_1.GetTemplateValue(var_69_3)
	var_69_7 = tonumber(var_69_4) or arg_69_2.GetTemplateValue(var_69_4)

	return var_69_5(var_69_6, var_69_7)

def parseCompareBuffAttachData(arg_70_0, arg_70_1):
	var_70_3, var_70_2, var_70_4 = re.search(r'(.*)([^\w\s]+(.*))',arg_70_0).groups()

	if arg_70_1.__name != var_70_3:
		return True

	var_70_5 = arg_70_1.GetEffectAttachData()

	return getCompareFuncByPunctuation(var_70_2)(var_70_5, var_70_4)

def parseCompare(arg_71_0, arg_71_1):
	var_71_3, var_71_2, var_71_4 = re.search(r'(.*)([^\w\s]+(.*))',arg_71_0).groups()
	var_71_5 = getCompareFuncByPunctuation(var_71_2)
	var_71_6 = tonumber(var_71_3) or arg_71_1.GetCurrent(var_71_3)
	var_71_7 = tonumber(var_71_4) or arg_71_1.GetCurrent(var_71_4)

	return var_71_5(var_71_6, var_71_7)

def parseFormula(arg_72_0, arg_72_1):
	var_72_0 = table()
	var_72_1 = table()

	for iter_72_0 in re.findall(r'\w+\.?\w*', arg_72_0):
		table.insert(var_72_0, iter_72_0)

	for iter_72_1 in re.findall(r'[^\w.]', arg_72_0):
		table.insert(var_72_1, iter_72_1)

	var_72_2 = table()
	var_72_3 = table()
	var_72_4 = 1
	var_72_5 = var_72_0[1]

	var_72_5 = tonumber(var_72_5) or arg_72_1.GetCurrent(var_72_5)

	for iter_72_2, iter_72_3 in ipairs(var_72_1):
		var_72_4 = var_72_4 + 1

		var_72_6 = tonumber(var_72_0[var_72_4]) or arg_72_1.GetCurrent(var_72_0[var_72_4])

		if iter_72_3 == "+" or iter_72_3 == "-":
			table.insert(var_72_3, var_72_5)

			var_72_5 = var_72_6

			table.insert(var_72_2, iter_72_3)
		elif iter_72_3 == "*" or iter_72_3 == "/":
			var_72_5 = getArithmeticFuncByOperator(iter_72_3)(var_72_5, var_72_6)

	table.insert(var_72_3, var_72_5)

	var_72_7 = 1
	var_72_8 = var_72_3[var_72_7]

	while var_72_7 < len(var_72_3) :
		var_72_9 = getArithmeticFuncByOperator(var_72_2[var_72_7])

		var_72_7 = var_72_7 + 1
		var_72_8 = var_72_9(var_72_8, var_72_3[var_72_7])

	return var_72_8
