from luatable import table, pairs, ipairs
import ys
import pg

import BattleDataProxy
import BattleEvent
import BattleFormulas
import BattleConst
import BattleConfig
import BattleDataFunction
import BattleAttr
import BattleVariable
from model.const import ShipType, TeamType

def SetupCalculateDamage(arg_1_0, arg_1_1):
	arg_1_0._calculateDamage = arg_1_1 or BattleFormulas.CreateContextCalculateDamage()
BattleDataProxy.SetupCalculateDamage = SetupCalculateDamage

def SetupDamageKamikazeAir(arg_2_0, arg_2_1):
	arg_2_0._calculateDamageKamikazeAir = arg_2_1 or BattleFormulas.CalculateDamageFromAircraftToMainShip
BattleDataProxy.SetupDamageKamikazeAir = SetupDamageKamikazeAir

def SetupDamageKamikazeShip(arg_3_0, arg_3_1):
	arg_3_0._calculateDamageKamikazeShip = arg_3_1 or BattleFormulas.CalculateDamageFromShipToMainShip
BattleDataProxy.SetupDamageKamikazeShip = SetupDamageKamikazeShip

def SetupDamageCrush(arg_4_0, arg_4_1):
	arg_4_0._calculateDamageCrush = arg_4_1 or BattleFormulas.CalculateCrashDamage
BattleDataProxy.SetupDamageCrush = SetupDamageCrush

def ClearFormulas(arg_5_0):
	arg_5_0._calculateDamage = None
	arg_5_0._calculateDamageKamikazeAir = None
	arg_5_0._calculateDamageKamikazeShip = None
	arg_5_0._calculateDamageCrush = None
BattleDataProxy.ClearFormulas = ClearFormulas

def HandleBulletHit(arg_6_0, arg_6_1, arg_6_2):
	if not arg_6_2:
		assert(False, "HandleBulletHit, but no vehicleData")

		return False
	elif not arg_6_1:
		assert(False, "HandleBulletHit, but no bulletData")

		return False

	if BattleAttr.IsSpirit(arg_6_2):
		return False

	if arg_6_1.IsCollided(arg_6_2.GetUniqueID()) == True:
		return

	arg_6_1.Hit(arg_6_2.GetUniqueID(), arg_6_2.GetUnitType())

	var_6_0 = table(
		_bullet = arg_6_1,
		equipIndex = arg_6_1.GetWeapon().GetEquipmentIndex(),
		bulletTag = arg_6_1.GetExtraTag()
	)

	arg_6_1.BuffTrigger(ys.Battle.BattleConst.BuffEffectType.ON_BULLET_COLLIDE, var_6_0)

	if arg_6_2.GetUnitType() == BattleConst.UnitType.PLAYER_UNIT and arg_6_2.GetIFF() == BattleConfig.FRIENDLY_CODE:
		ys.Battle.BattleCameraUtil.GetInstance().StartShake(pg.shake_template[BattleConst.ShakeType.HIT])

	return True
BattleDataProxy.HandleBulletHit = HandleBulletHit

def HandleDamage(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4):
	if arg_7_2.GetIFF() == BattleConfig.FOE_CODE and arg_7_2.IsShowHPBar():
		arg_7_0.DispatchEvent(ys.Event.New(BattleEvent.HIT_ENEMY, arg_7_2))

	var_7_0 = arg_7_1.GetWeapon()
	var_7_1 = arg_7_1.GetWeaponHostAttr()
	var_7_2 = arg_7_1.GetExtraTag()
	var_7_3 = var_7_0.GetTemplateData()
	var_7_4 = table(
		weaponType = var_7_3.attack_attribute,
		bulletType = arg_7_1.GetType(),
		bulletTag = var_7_2
	)

	arg_7_2.TriggerBuff(BattleConst.BuffEffectType.ON_BULLET_HIT_BEFORE, var_7_4)

	if BattleAttr.IsInvincible(arg_7_2):
		return

	var_7_5, var_7_6, var_7_7 = arg_7_0._calculateDamage(arg_7_1, arg_7_2, arg_7_3, arg_7_4)
	var_7_8 = var_7_6.isMiss
	var_7_9 = var_7_6.isCri
	var_7_10 = var_7_6.damageAttr

	arg_7_1.AppendDamageUnit(arg_7_2.GetUniqueID())

	var_7_11 = var_7_3.type
	var_7_12 = var_7_0.GetEquipmentIndex()
	var_7_13 = table(
		target = arg_7_2,
		damage = var_7_5,
		weaponType = var_7_11,
		equipIndex = var_7_12,
		bulletTag = var_7_2
	)
	var_7_14 = table(
		isHeal = False,
		isMiss = var_7_8,
		isCri = var_7_9,
		attr = var_7_10,
		font = var_7_7,
		cldPos = arg_7_1.GetPosition(),
		srcID = var_7_1.battleUID
	)

	arg_7_1.GetWeapon().WeaponStatistics(var_7_5, var_7_9, var_7_8)

	var_7_15 = arg_7_2.UpdateHP(var_7_5 * -1, var_7_14)

	arg_7_0.DamageStatistics(var_7_1.id, arg_7_2.GetAttrByName("id"), -var_7_15)

	if not var_7_8 and arg_7_1.GetWeaponTempData().type != BattleConst.EquipmentType.ANTI_AIR:
		arg_7_1.BuffTrigger(ys.Battle.BattleConst.BuffEffectType.ON_BULLET_HIT, var_7_13)

		var_7_16 = arg_7_1.GetHost()

		if var_7_16 and var_7_16.IsAlive() and var_7_16.GetUnitType() != ys.Battle.BattleConst.UnitType.AIRFIGHTER_UNIT:
			if table.contains(BattleConst.AircraftUnitType, var_7_16.GetUnitType()):
				var_7_16 = var_7_16.GetMotherUnit()

			var_7_17 = var_7_16.GetIFF()

			for iter_7_0, iter_7_1 in pairs(arg_7_0._unitList):
				if iter_7_1.GetIFF() == var_7_17 and iter_7_1 != var_7_16:
					iter_7_1.TriggerBuff(ys.Battle.BattleConst.BuffEffectType.ON_TEAMMATE_BULLET_HIT, var_7_13)

	var_7_18 = arg_7_2.GetUnitType()
	var_7_19 = True

	if var_7_18 != BattleConst.UnitType.AIRCRAFT_UNIT and var_7_18 != BattleConst.UnitType.AIRFIGHTER_UNIT and var_7_18 != BattleConst.UnitType.FUNNEL_UNIT and var_7_18 != BattleConst.UnitType.UAV_UNIT:
		var_7_19 = False

	if arg_7_2.IsAlive():
		if not var_7_19:
			for iter_7_2, iter_7_3 in ipairs(arg_7_1.GetAttachBuff()):
				if iter_7_3.hit_ignore or not var_7_8:
					BattleDataProxy.HandleBuffPlacer(iter_7_3, arg_7_1, arg_7_2)

		if not var_7_8:
			arg_7_2.TriggerBuff(BattleConst.BuffEffectType.ON_BE_HIT, var_7_4)
	else:
		arg_7_1.BuffTrigger(ys.Battle.BattleConst.BuffEffectType.ON_BULLET_KILL, table(
			unit = arg_7_2,
			killer = arg_7_1
		))
		arg_7_0.obituary(arg_7_2, var_7_19, arg_7_1)
		arg_7_0.KillCountStatistics(var_7_1.id, arg_7_2.GetAttrByName("id"))

	return var_7_8, var_7_9
BattleDataProxy.HandleDamage = HandleDamage

def HandleMeteoDamage(arg_8_0, arg_8_1, arg_8_2):
	var_8_0 = BattleFormulas.GetMeteoDamageRatio(len(arg_8_2))

	for iter_8_0, iter_8_1 in ipairs(arg_8_2):
		arg_8_0.HandleDamage(arg_8_1, iter_8_1, None, var_8_0[iter_8_0])
BattleDataProxy.HandleMeteoDamage = HandleMeteoDamage

def HandleDirectDamage(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	var_9_0

	if arg_9_3:
		var_9_0 = arg_9_3.GetAttrByName("id")

	var_9_1 = table(
		isMiss = False,
		isCri = False,
		isHeal = False,
		damageReason = arg_9_4,
		srcID = var_9_0
	)
	var_9_2 = arg_9_1.GetAttrByName("id")
	var_9_3 = arg_9_1.UpdateHP(arg_9_2 * -1, var_9_1)
	var_9_4 = arg_9_1.IsAlive()

	if arg_9_3:
		arg_9_0.DamageStatistics(var_9_0, var_9_2, -var_9_3)

		if not var_9_4:
			arg_9_0.KillCountStatistics(var_9_0, var_9_2)

	if not var_9_4:
		var_9_5 = arg_9_1.GetUnitType()
		var_9_6 = True

		if var_9_5 != BattleConst.UnitType.AIRCRAFT_UNIT and var_9_5 != BattleConst.UnitType.AIRFIGHTER_UNIT and var_9_5 != BattleConst.UnitType.FUNNEL_UNIT and var_9_5 != BattleConst.UnitType.UAV_UNIT:
			var_9_6 = False

		arg_9_0.obituary(arg_9_1, var_9_6, arg_9_3)
BattleDataProxy.HandleDirectDamage = HandleDirectDamage

def obituary(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	for iter_10_0, iter_10_1 in pairs(arg_10_0._unitList):
		if iter_10_1 != arg_10_1:
			if iter_10_1.GetIFF() == arg_10_1.GetIFF():
				if arg_10_2:
					iter_10_1.TriggerBuff(BattleConst.BuffEffectType.ON_FRIENDLY_AIRCRAFT_DYING, table(
						unit = arg_10_1,
						killer = arg_10_3
					))
				elif not arg_10_1.GetWorldDeathMark():
					iter_10_1.TriggerBuff(BattleConst.BuffEffectType.ON_FRIENDLY_SHIP_DYING, table(
						unit = arg_10_1,
						killer = arg_10_3
					))
			elif arg_10_2:
				iter_10_1.TriggerBuff(BattleConst.BuffEffectType.ON_FOE_AIRCRAFT_DYING, table(
					unit = arg_10_1,
					killer = arg_10_3
				))
			else:
				iter_10_1.TriggerBuff(BattleConst.BuffEffectType.ON_FOE_DYING, table(
					unit = arg_10_1,
					killer = arg_10_3
				))
BattleDataProxy.obituary = obituary

def HandleAircraftMissDamage(arg_11_0, arg_11_1, arg_11_2):
	if arg_11_2 == None:
		return

	var_11_0 = arg_11_2.GetCloakList()

	for iter_11_0, iter_11_1 in ipairs(var_11_0):
		iter_11_1.CloakExpose(arg_11_0._airExpose)

	var_11_1 = arg_11_1.GetPosition()
	var_11_2 = arg_11_2.NearestUnitByType(var_11_1, ShipType.CloakShipTypeList)

	if var_11_2:
		var_11_2.CloakExpose(arg_11_0._airExposeEX)

	var_11_3 = arg_11_2.RandomMainVictim(table(
		"immuneDirectHit"
	))

	if var_11_3:
		var_11_4 = arg_11_0._calculateDamageKamikazeAir(arg_11_1, var_11_3)

		var_11_3.TriggerBuff(BattleConst.BuffEffectType.ON_BE_HIT, table())
		arg_11_0.HandleDirectDamage(var_11_3, var_11_4, arg_11_1)
BattleDataProxy.HandleAircraftMissDamage = HandleAircraftMissDamage

def HandleShipMissDamage(arg_12_0, arg_12_1, arg_12_2):
	if arg_12_2 == None:
		return

	var_12_0 = arg_12_2.GetCloakList()

	for iter_12_0, iter_12_1 in ipairs(var_12_0):
		iter_12_1.CloakExpose(arg_12_0._shipExpose)

	var_12_1 = arg_12_1.GetPosition()
	var_12_2 = arg_12_2.NearestUnitByType(var_12_1, ShipType.CloakShipTypeList)

	if var_12_2:
		var_12_2.CloakExpose(arg_12_0._shipExposeEX)

	var_12_3 = arg_12_2.RandomMainVictim(table(
		"immuneDirectHit"
	))

	if var_12_3:
		var_12_4 = arg_12_1.GetTemplate().type

		if table.contains(TeamType.SubShipType, var_12_4):
			var_12_5 = BattleFormulas.CalculateDamageFromSubmarinToMainShip(arg_12_1, var_12_3)

			var_12_3.TriggerBuff(BattleConst.BuffEffectType.ON_BE_HIT, table())
			arg_12_0.HandleDirectDamage(var_12_3, var_12_5, arg_12_1)

			if var_12_3.IsAlive() and BattleFormulas.RollSubmarineDualDice(arg_12_1):
				var_12_6 = BattleFormulas.CalculateDamageFromSubmarinToMainShip(arg_12_1, var_12_3)

				var_12_3.TriggerBuff(BattleConst.BuffEffectType.ON_BE_HIT, table())
				arg_12_0.HandleDirectDamage(var_12_3, var_12_6, arg_12_1)
		else:
			var_12_7 = arg_12_0._calculateDamageKamikazeShip(arg_12_1, var_12_3)

			var_12_3.TriggerBuff(BattleConst.BuffEffectType.ON_BE_HIT, table())
			arg_12_0.HandleDirectDamage(var_12_3, var_12_7, arg_12_1)
BattleDataProxy.HandleShipMissDamage = HandleShipMissDamage

def HandleCrashDamage(arg_13_0, arg_13_1, arg_13_2):
	var_13_0, var_13_1 = arg_13_0._calculateDamageCrush(arg_13_1, arg_13_2)

	arg_13_0.HandleDirectDamage(arg_13_1, var_13_0, arg_13_2, BattleConst.UnitDeathReason.CRUSH)
	arg_13_0.HandleDirectDamage(arg_13_2, var_13_1, arg_13_1, BattleConst.UnitDeathReason.CRUSH)
BattleDataProxy.HandleCrashDamage = HandleCrashDamage

def HandleBuffPlacer(arg_14_0, arg_14_1, arg_14_2):
	var_14_0 = BattleDataFunction.GetBuffTemplate(arg_14_0.buff_id).effect_list
	var_14_1 = False

	if var_14_0[1].type == "BattleBuffDOT":
		if BattleFormulas.CaclulateDOTPlace(arg_14_0.rant, var_14_0[1], arg_14_1, arg_14_2):
			var_14_1 = True
	elif BattleFormulas.IsHappen(arg_14_0.rant or 10000):
		var_14_1 = True

	if var_14_1:
		var_14_2 = ys.Battle.BattleBuffUnit.New(arg_14_0.buff_id, arg_14_0.level, arg_14_1)

		var_14_2.SetOrb(arg_14_1, arg_14_0.level)
		arg_14_2.AddBuff(var_14_2)
BattleDataProxy.HandleBuffPlacer = HandleBuffPlacer

def HandleDOTPlace(arg_15_0, arg_15_1, arg_15_2):
	var_15_0 = arg_15_0.arg_list
	var_15_1 = BattleConfig.DOT_CONFIG[var_15_0.dotType]
	var_15_2 = arg_15_1.GetAttrByName(var_15_1.hit)

	if BattleFormulas.IsHappen(var_15_0.ACC + arg_15_1.GetAttrByName(var_15_1.hit) - arg_15_2.GetAttrByName(var_15_1.resist)):
		return True

	return False
BattleDataProxy.HandleDOTPlace = HandleDOTPlace

def HandleShipCrashDamageList(arg_16_0, arg_16_1, arg_16_2):
	var_16_0 = arg_16_1.GetHostileCldList()

	for iter_16_0, iter_16_1 in pairs(var_16_0):
		if not table.contains(arg_16_2, iter_16_0):
			arg_16_1.RemoveHostileCld(iter_16_0)

	for iter_16_2, iter_16_3 in ipairs(arg_16_2):
		if var_16_0[iter_16_3] == None:
			def var_16_2():
				arg_16_0.HandleCrashDamage(arg_16_0._unitList[iter_16_3], arg_16_1)

			var_16_3 = pg.TimeMgr.GetInstance().AddBattleTimer("shipCld", None, BattleConfig.SHIP_CLD_INTERVAL, var_16_2, True)

			arg_16_1.AppendHostileCld(iter_16_3, var_16_3)
			var_16_2()

			if not arg_16_1.IsAlive():
				break
BattleDataProxy.HandleShipCrashDamageList = HandleShipCrashDamageList

def HandleShipCrashDecelerate(arg_18_0, arg_18_1, arg_18_2):
	if arg_18_2 == 0 and arg_18_1.IsCrash():
		arg_18_1.SetCrash(False)
	elif arg_18_2 > 0 and not arg_18_1.IsCrash():
		arg_18_1.SetCrash(True)
BattleDataProxy.HandleShipCrashDecelerate = HandleShipCrashDecelerate

def HandleWallHitByBullet(arg_19_0, arg_19_1, arg_19_2):
	return (arg_19_1.GetCldFunc()(arg_19_2))
BattleDataProxy.HandleWallHitByBullet = HandleWallHitByBullet

def HandleWallHitByShip(arg_20_0, arg_20_1, arg_20_2):
	arg_20_1.GetCldFunc()(arg_20_2)
BattleDataProxy.HandleWallHitByShip = HandleWallHitByShip

def HandleWallDamage(arg_21_0, arg_21_1, arg_21_2):
	if arg_21_2.GetIFF() == BattleConfig.FOE_CODE and arg_21_2.IsShowHPBar():
		arg_21_0.DispatchEvent(ys.Event.New(BattleEvent.HIT_ENEMY, arg_21_2))

	var_21_0 = BattleAttr.GetCurrent(arg_21_1, "id")

	if BattleAttr.IsInvincible(arg_21_2):
		return

	var_21_1, var_21_2, var_21_3 = arg_21_0._calculateDamage(arg_21_1, arg_21_2)
	var_21_4 = var_21_2.isMiss
	var_21_5 = var_21_2.isCri
	var_21_6 = var_21_2.damageAttr
	var_21_7 = table(
		isHeal = False,
		isMiss = var_21_4,
		isCri = var_21_5,
		attr = var_21_6,
		font = var_21_3,
		cldPos = arg_21_1.GetPosition(),
		srcID = var_21_0
	)
	var_21_8 = arg_21_2.UpdateHP(var_21_1 * -1, var_21_7)

	arg_21_0.DamageStatistics(var_21_0, arg_21_2.GetAttrByName("id"), -var_21_8)

	if arg_21_2.IsAlive():
		if not var_21_4:
			arg_21_2.TriggerBuff(BattleConst.BuffEffectType.ON_BE_HIT, table())
	else:
		arg_21_0.obituary(arg_21_2, False, arg_21_1)
		arg_21_0.KillCountStatistics(var_21_0, arg_21_2.GetAttrByName("id"))

	return var_21_4, var_21_5
BattleDataProxy.HandleWallDamage = HandleWallDamage