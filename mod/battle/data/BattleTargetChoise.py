from luatable import pairs, table, ipairs
from alsupport import math, Mathf

import ys

import BattleConfig
import BattleAttr
import BattleFormulas
from model.const import TeamType


def TargetNil():
	return None

def TargetNull():
	return table()

def TargetAll():
	return ys.Battle.BattleDataProxy.GetInstance().GetUnitList()

def TargetEntityUnit():
	var_4_0 = table()
	var_4_1 = ys.Battle.BattleDataProxy.GetInstance().GetUnitList()

	for iter_4_0, iter_4_1 in pairs(var_4_1):
		if not iter_4_1.IsSpectre():
			var_4_0.append(iter_4_1)

	return var_4_0

def TargetSpectreUnit(arg_5_0, arg_5_1, arg_5_2):
	var_5_0 = table()
	var_5_1 = ys.Battle.BattleDataProxy.GetInstance().GetSpectreShipList()

	for iter_5_0, iter_5_1 in pairs(var_5_1):
		var_5_0.append(iter_5_1)

	return var_5_0

def TargetTemplate(arg_6_0, arg_6_1, arg_6_2):
	var_6_0 = arg_6_1.targetTemplateIDList or table(
		arg_6_1.targetTemplateID
	)
	var_6_1 = arg_6_2 or TargetEntityUnit()
	var_6_2 = table()
	var_6_3 = arg_6_0.GetIFF()

	for iter_6_0, iter_6_1 in pairs(var_6_1):
		var_6_4 = iter_6_1.GetTemplateID()
		var_6_5 = iter_6_1.GetIFF()

		if table.contains(var_6_0, var_6_4) and var_6_3 == var_6_5:
			var_6_2.append(iter_6_1)

	return var_6_2

def TargetNationality(arg_7_0, arg_7_1, arg_7_2):
	if not arg_7_1.targetTemplateIDList:
		(table())[1] = arg_7_1.targetTemplateID #???

	var_7_0 = arg_7_2 or ys.Battle.BattleDataProxy.GetInstance().GetUnitList()
	var_7_1 = table()
	var_7_2 = arg_7_1.nationality
	var_7_3 = type(var_7_2)

	for iter_7_0, iter_7_1 in pairs(var_7_0):
		if var_7_3 in (float, int):
			if iter_7_1.GetTemplate().nationality == var_7_2:
				var_7_1.append(iter_7_1)
		elif var_7_3 == table and table.contains(var_7_2, iter_7_1.GetTemplate().nationality):
			var_7_1.append(iter_7_1)

	return var_7_1

def TargetShipType(arg_8_0, arg_8_1, arg_8_2):
	var_8_0 = arg_8_2 or TargetEntityUnit()
	var_8_1 = table()
	var_8_2 = arg_8_1.ship_type_list

	for iter_8_0, iter_8_1 in pairs(var_8_0):
		var_8_3 = iter_8_1.GetTemplate().type

		if table.contains(var_8_2, var_8_3):
			var_8_1.append(iter_8_1)

	return var_8_1

def TargetShipTag(arg_9_0, arg_9_1, arg_9_2):
	var_9_0 = arg_9_2 or TargetEntityUnit()
	var_9_1 = table()
	var_9_2 = arg_9_1.ship_tag_list

	for iter_9_0, iter_9_1 in pairs(var_9_0):
		if iter_9_1.ContainsLabelTag(var_9_2):
			var_9_1.append(iter_9_1)

	return var_9_1

def TargetShipArmor(arg_10_0, arg_10_1, arg_10_2):
	var_10_0 = arg_10_2 or TargetEntityUnit()
	var_10_1 = table()
	var_10_2 = arg_10_1.armor_type

	for iter_10_0, iter_10_1 in ipairs(var_10_0):
		if iter_10_1.GetAttrByName("armorType") == var_10_2:
			var_10_1.append(iter_10_1)

	return var_10_1

def getShipListByIFF(arg_11_0):
	var_11_0 = ys.Battle.BattleDataProxy.GetInstance()
	var_11_1

	if arg_11_0 == BattleConfig.FRIENDLY_CODE:
		var_11_1 = var_11_0.GetFriendlyShipList()
	elif arg_11_0 == BattleConfig.FOE_CODE:
		var_11_1 = var_11_0.GetFoeShipList()

	return var_11_1

def TargetAllHelp(arg_12_0, arg_12_1, arg_12_2):
	var_12_0 = table()

	if arg_12_0:
		arg_12_1 = arg_12_1 or table()

		var_12_1 = arg_12_1.exceptCaster
		var_12_2 = arg_12_0.GetUniqueID()
		var_12_3 = arg_12_0.GetIFF()
		var_12_4 = arg_12_2 or getShipListByIFF(var_12_3)

		for iter_12_0, iter_12_1 in pairs(var_12_4):
			var_12_5 = iter_12_1.GetUniqueID()

			if iter_12_1.IsAlive() and iter_12_1.GetIFF() == var_12_3 and (not var_12_1 or var_12_5 != var_12_2):
				var_12_0.append(iter_12_1)

	return var_12_0

def TargetHelpLeastHP(arg_13_0, arg_13_1, arg_13_2):
	arg_13_1 = arg_13_1 or table()

	var_13_0
	var_13_1 = arg_13_1.targetMaxHPRatio

	if arg_13_0:
		var_13_2 = arg_13_2 or getShipListByIFF(arg_13_0.GetIFF())
		var_13_3 = 9999999999

		for iter_13_0, iter_13_1 in pairs(var_13_2):
			if iter_13_1.IsAlive() and var_13_3 > iter_13_1.GetCurrentHP() and (not var_13_1 or var_13_1 >= iter_13_1.GetHPRate()):
				var_13_0 = iter_13_1
				var_13_3 = iter_13_1.GetCurrentHP()

	return table(
		var_13_0
	)

def TargetHelpLeastHPRatio(arg_14_0, arg_14_1, arg_14_2):
	arg_14_1 = arg_14_1 or table()

	var_14_0

	if arg_14_0:
		var_14_1 = 100
		var_14_2 = arg_14_2 or getShipListByIFF(arg_14_0.GetIFF())

		for iter_14_0, iter_14_1 in pairs(var_14_2):
			if iter_14_1.IsAlive() and var_14_1 > iter_14_1.GetHPRate():
				var_14_0 = iter_14_1
				var_14_1 = iter_14_1.GetHPRate()

	return table(
		var_14_0
	)

def TargetHighestHP(arg_15_0, arg_15_1, arg_15_2):
	arg_15_1 = arg_15_1 or table()

	var_15_0

	if arg_15_0:
		var_15_1 = arg_15_2 or TargetEntityUnit()
		var_15_2 = 1

		for iter_15_0, iter_15_1 in pairs(var_15_1):
			if iter_15_1.IsAlive() and var_15_2 < iter_15_1.GetCurrentHP():
				var_15_0 = iter_15_1
				var_15_2 = iter_15_1.GetCurrentHP()

	return table(
		var_15_0
	)

def TargetLowestHPRatio(arg_16_0, arg_16_1, arg_16_2):
	arg_16_1 = arg_16_1 or table()

	var_16_0
	var_16_1 = arg_16_2 or TargetEntityUnit()
	var_16_2 = 1

	for iter_16_0, iter_16_1 in pairs(var_16_1):
		var_16_3 = iter_16_1.GetHPRate()

		if iter_16_1.IsAlive() and var_16_3 < var_16_2 and var_16_3 > 0:
			var_16_0 = iter_16_1
			var_16_2 = var_16_3

	return table(
		var_16_0
	)

def TargetLowestHP(arg_17_0, arg_17_1, arg_17_2):
	arg_17_1 = arg_17_1 or table()

	var_17_0
	var_17_1 = arg_17_2 or TargetEntityUnit()
	var_17_2 = 9999999999

	for iter_17_0, iter_17_1 in pairs(var_17_1):
		var_17_3 = iter_17_1.GetCurrentHP()

		if iter_17_1.IsAlive() and var_17_3 < var_17_2 and var_17_3 > 0:
			var_17_0 = iter_17_1
			var_17_2 = var_17_3

	return table(
		var_17_0
	)

def TargetHighestHPRatio(arg_18_0, arg_18_1, arg_18_2):
	arg_18_1 = arg_18_1 or table()

	var_18_0
	var_18_1 = arg_18_2 or TargetEntityUnit()
	var_18_2 = 0

	for iter_18_0, iter_18_1 in pairs(var_18_1):
		if iter_18_1.IsAlive() and var_18_2 < iter_18_1.GetHPRate():
			var_18_0 = iter_18_1
			var_18_2 = iter_18_1.GetHPRate()

	return table(
		var_18_0
	)

def TargetAttrCompare(arg_19_0, arg_19_1, arg_19_2):
	var_19_0 = table()
	var_19_1 = arg_19_2 or TargetEntityUnit()

	for iter_19_0, iter_19_1 in pairs(var_19_1):
		if iter_19_1.IsAlive() and BattleFormulas.parseCompareUnitAttr(arg_19_1.attrCompare, iter_19_1, arg_19_0):
			table.insert(var_19_0, iter_19_1)

	return var_19_0

def TargetTempCompare(arg_20_0, arg_20_1, arg_20_2):
	var_20_0 = table()
	var_20_1 = arg_20_2 or TargetEntityUnit()

	for iter_20_0, iter_20_1 in pairs(var_20_1):
		if iter_20_1.IsAlive() and BattleFormulas.parseCompareUnitTemplate(arg_20_1.tempCompare, iter_20_1, arg_20_0):
			table.insert(var_20_0, iter_20_1)

	return var_20_0

def TargetHPCompare(arg_21_0, arg_21_1, arg_21_2):
	var_21_0 = table()
	var_21_1 = arg_21_2 or TargetEntityUnit()

	if arg_21_0:
		var_21_2 = arg_21_0.GetHP()

		for iter_21_0, iter_21_1 in ipairs(var_21_1):
			if var_21_2 > iter_21_1.GetHP():
				var_21_0.append(iter_21_1)

	return var_21_0

def TargetHPRatioLowerThan(arg_22_0, arg_22_1, arg_22_2):
	var_22_0 = table()
	var_22_1 = arg_22_1.hpRatioList[1]
	var_22_2 = arg_22_2 or TargetEntityUnit()

	for iter_22_0, iter_22_1 in ipairs(var_22_2):
		if var_22_1 > iter_22_1.GetHP():
			var_22_0.append(iter_22_1)

	return var_22_0

def TargetNationalityFriendly(arg_23_0, arg_23_1, arg_23_2):
	var_23_0 = table()

	if arg_23_0:
		var_23_1 = arg_23_1.nationality
		var_23_2 = arg_23_2 or TargetAllHelp(arg_23_0, arg_23_1)

		for iter_23_0, iter_23_1 in pairs(var_23_2):
			if iter_23_1.GetTemplate().nationality == var_23_1:
				var_23_0.append(iter_23_1)

	return var_23_0

def TargetNationalityFoe(arg_24_0, arg_24_1, arg_24_2):
	var_24_0 = table()

	if arg_24_0:
		var_24_1 = arg_24_1.nationality
		var_24_2 = arg_24_2 or TargetAllHarm(arg_24_0, arg_24_1)

		for iter_24_0, iter_24_1 in pairs(var_24_2):
			if iter_24_1.GetTemplate().nationality == var_24_1:
				var_24_0.append(iter_24_1)

	return var_24_0

def TargetShipTypeFriendly(arg_25_0, arg_25_1, arg_25_2):
	var_25_0 = table()

	if arg_25_0:
		var_25_1 = arg_25_1.ship_type_list
		var_25_2 = arg_25_2 or TargetAllHelp(arg_25_0, arg_25_1)

		for iter_25_0, iter_25_1 in pairs(var_25_2):
			var_25_3 = iter_25_1.GetTemplate().type

			if table.contains(var_25_1, var_25_3):
				var_25_0.append(iter_25_1)

	return var_25_0

def TargetSelf(arg_26_0):
	return table(
		arg_26_0
	)

def TargetAllHarm(arg_27_0, arg_27_1, arg_27_2):
	var_27_0 = table()
	var_27_1
	var_27_2 = ys.Battle.BattleDataProxy.GetInstance()

	if arg_27_2:
		var_27_1 = arg_27_2
	else:
		var_27_3 = arg_27_0.GetIFF()

		if var_27_3 == BattleConfig.FRIENDLY_CODE:
			var_27_1 = var_27_2.GetFoeShipList()
		elif var_27_3 == BattleConfig.FOE_CODE:
			var_27_1 = var_27_2.GetFriendlyShipList()

	var_27_4, var_27_5, var_27_6, var_27_7 = var_27_2.GetFieldBound()

	if var_27_1:
		for iter_27_0, iter_27_1 in pairs(var_27_1):
			if iter_27_1.IsAlive() and var_27_7 > iter_27_1.GetPosition().x and iter_27_1.GetCurrentOxyState() != ys.Battle.BattleConst.OXY_STATE.DIVE:
				var_27_0.append(iter_27_1)

	return var_27_0

def TargetAllFoe(arg_28_0, arg_28_1, arg_28_2):
	var_28_0 = table()
	var_28_1
	var_28_2 = ys.Battle.BattleDataProxy.GetInstance()

	if arg_28_2:
		var_28_1 = arg_28_2
	else:
		var_28_3 = arg_28_0.GetIFF()

		if var_28_3 == BattleConfig.FRIENDLY_CODE:
			var_28_1 = var_28_2.GetFoeShipList()
		elif var_28_3 == BattleConfig.FOE_CODE:
			var_28_1 = var_28_2.GetFriendlyShipList()

	var_28_4, var_28_5, var_28_6, var_28_7 = var_28_2.GetFieldBound()

	if var_28_1:
		for iter_28_0, iter_28_1 in pairs(var_28_1):
			if iter_28_1.IsAlive() and var_28_7 > iter_28_1.GetPosition().x:
				var_28_0.append(iter_28_1)

	return var_28_0

def TargetFoeUncloak(arg_29_0, arg_29_1, arg_29_2):
	var_29_0 = table()
	var_29_1
	var_29_2 = ys.Battle.BattleDataProxy.GetInstance()

	if arg_29_2:
		var_29_1 = arg_29_2
	else:
		var_29_3 = arg_29_0.GetIFF()

		if var_29_3 == BattleConfig.FRIENDLY_CODE:
			var_29_1 = var_29_2.GetFoeShipList()
		elif var_29_3 == BattleConfig.FOE_CODE:
			var_29_1 = var_29_2.GetFriendlyShipList()

	var_29_4, var_29_5, var_29_6, var_29_7 = var_29_2.GetFieldBound()

	if var_29_1:
		for iter_29_0, iter_29_1 in pairs(var_29_1):
			if iter_29_1.IsAlive() and var_29_7 > iter_29_1.GetPosition().x and not BattleAttr.IsCloak(iter_29_1) and iter_29_1.GetCurrentOxyState() != ys.Battle.BattleConst.OXY_STATE.DIVE:
				var_29_0.append(iter_29_1)

	return var_29_0

def TargetCloakState(arg_30_0, arg_30_1, arg_30_2):
	var_30_0 = table()
	var_30_1 = arg_30_1.cloak or 1
	var_30_2 = arg_30_2 or TargetEntityUnit()

	for iter_30_0, iter_30_1 in ipairs(var_30_2):
		if BattleAttr.GetCurrent(iter_30_1, "isCloak") == var_30_1:
			var_30_0.append(iter_30_1)

	return var_30_0

def TargetFaintState(arg_31_0, arg_31_1, arg_31_2):
	var_31_0 = table()
	var_31_1 = arg_31_1.faint or 1
	var_31_2 = arg_31_2 or TargetEntityUnit()

	for iter_31_0, iter_31_1 in ipairs(var_31_2):
		var_31_3 = iter_31_1.GetAimBias()

		if var_31_1 == 1:
			if var_31_3 and var_31_3.IsFaint():
				var_31_0.append(iter_31_1)
		elif var_31_1 == 0 and (not var_31_3 or not var_31_3.IsFaint()):
			var_31_0.append(iter_31_1)

	return var_31_0

def TargetHarmNearest(arg_32_0, arg_32_1, arg_32_2):
	arg_32_1 = arg_32_1 or table()

	var_32_0 = arg_32_1.range or 9999999999
	var_32_1
	var_32_2 = arg_32_2 or TargetFoeUncloak(arg_32_0)

	for iter_32_0, iter_32_1 in ipairs(var_32_2):
		var_32_3 = arg_32_0.GetDistance(iter_32_1)

		if var_32_3 < var_32_0:
			var_32_0 = var_32_3
			var_32_1 = iter_32_1

	return table(
		var_32_1
	)

def TargetHarmFarthest(arg_33_0, arg_33_1, arg_33_2):
	var_33_0 = 0
	var_33_1
	var_33_2 = arg_33_2 or TargetFoeUncloak(arg_33_0)

	for iter_33_0, iter_33_1 in ipairs(var_33_2):
		var_33_3 = arg_33_0.GetDistance(iter_33_1)

		if var_33_0 < var_33_3:
			var_33_0 = var_33_3
			var_33_1 = iter_33_1

	return table(
		var_33_1
	)

def TargetHarmRandom(arg_34_0, arg_34_1, arg_34_2):
	var_34_0 = arg_34_2 or TargetFoeUncloak(arg_34_0)

	if len(var_34_0) > 0:
		var_34_1 = math.random(len(var_34_0))

		return table(
			var_34_0[var_34_1]
		)
	else:
		return table()

def TargetHarmRandomByWeight(arg_35_0, arg_35_1, arg_35_2):
	var_35_0 = arg_35_2 or TargetFoeUncloak(arg_35_0)
	var_35_1 = table()
	var_35_2 = -9999

	for iter_35_0, iter_35_1 in ipairs(var_35_0):
		var_35_3 = iter_35_1.GetTargetedPriority() or 0

		if var_35_3 == var_35_2:
			var_35_1.append(iter_35_1)
		elif var_35_2 < var_35_3:
			var_35_1 = table(
				iter_35_1
			)
			var_35_2 = var_35_3

	if len(var_35_1) > 0:
		var_35_4 = math.random(len(var_35_1))

		return table(
			var_35_1[var_35_4]
		)
	else:
		return table()

def TargetWeightiest(arg_36_0, arg_36_1, arg_36_2):
	var_36_0 = arg_36_2 or TargetEntityUnit()
	var_36_1 = table()
	var_36_2 = -9999

	for iter_36_0, iter_36_1 in ipairs(var_36_0):
		var_36_3 = iter_36_1.GetTargetedPriority() or 0

		if var_36_3 == var_36_2:
			var_36_1.append(iter_36_1)
		elif var_36_2 < var_36_3:
			var_36_1 = table(
				iter_36_1
			)
			var_36_2 = var_36_3

	return var_36_1

def TargetRandom(arg_37_0, arg_37_1, arg_37_2):
	var_37_0 = arg_37_2 or TargetEntityUnit()
	var_37_1 = arg_37_1.randomCount or 1

	return (Mathf.MultiRandom(var_37_0, var_37_1))

def TargetInsideArea(arg_38_0, arg_38_1, arg_38_2):
	var_38_0 = arg_38_2 or TargetAllHarm(arg_38_0)
	var_38_1 = arg_38_1.dir or ys.Battle.BattleConst.UnitDir.RIGHT
	var_38_2 = arg_38_1.lineX
	var_38_3 = table()

	if var_38_1 == ys.Battle.BattleConst.UnitDir.RIGHT:
		for iter_38_0, iter_38_1 in ipairs(var_38_0):
			if var_38_2 <= iter_38_1.GetPosition().x:
				table.insert(var_38_3, iter_38_1)
	elif var_38_1 == ys.Battle.BattleConst.UnitDir.LEFT:
		for iter_38_2, iter_38_3 in ipairs(var_38_0):
			if var_38_2 >= iter_38_3.GetPosition().x:
				table.insert(var_38_3, iter_38_3)

	return var_38_3

def TargetAircraftHelp(arg_39_0):
	var_39_0 = ys.Battle.BattleDataProxy.GetInstance()
	var_39_1 = table()
	var_39_2 = arg_39_0.GetIFF()

	for iter_39_0, iter_39_1 in pairs(var_39_0.GetAircraftList()):
		if var_39_2 == iter_39_1.GetIFF():
			var_39_1.append(iter_39_1)

	return var_39_1

def TargetAircraftHarm(arg_40_0):
	var_40_0 = ys.Battle.BattleDataProxy.GetInstance()
	var_40_1 = table()
	var_40_2 = arg_40_0.GetIFF()

	for iter_40_0, iter_40_1 in pairs(var_40_0.GetAircraftList()):
		if var_40_2 != iter_40_1.GetIFF() and iter_40_1.IsVisitable():
			var_40_1.append(iter_40_1)

	return var_40_1

def TargetAircraftGB(arg_41_0):
	var_41_0 = ys.Battle.BattleDataProxy.GetInstance()
	var_41_1 = table()
	var_41_2 = arg_41_0.GetIFF()

	for iter_41_0, iter_41_1 in pairs(var_41_0.GetAircraftList()):
		if var_41_2 != iter_41_1.GetIFF() and iter_41_1.IsVisitable() and iter_41_1.GetMotherUnit() == None:
			var_41_1.append(iter_41_1)

	return var_41_1

def TargetDiveState(arg_42_0, arg_42_1, arg_42_2):
	var_42_0 = arg_42_1 and arg_42_1.diveState or ys.Battle.BattleConst.OXY_STATE.DIVE
	var_42_1 = arg_42_2 or TargetEntityUnit()
	var_42_2 = table()

	for iter_42_0, iter_42_1 in pairs(var_42_1):
		if var_42_0 == iter_42_1.GetCurrentOxyState():
			var_42_2.append(iter_42_1)

	return var_42_2

def TargetDetectedUnit(arg_43_0, arg_43_1, arg_43_2):
	var_43_0 = arg_43_2 or TargetEntityUnit()
	var_43_1 = table()

	for iter_43_0, iter_43_1 in pairs(var_43_0):
		if iter_43_1.GetDiveDetected():
			var_43_1.append(iter_43_1)

	return var_43_1

def TargetAllHarmBullet(arg_44_0):
	var_44_0 = ys.Battle.BattleDataProxy.GetInstance()
	var_44_1 = table()
	var_44_2 = arg_44_0.GetIFF()

	for iter_44_0, iter_44_1 in pairs(var_44_0.GetBulletList()):
		if var_44_2 != iter_44_1.GetIFF():
			var_44_1.append(iter_44_1)

	return var_44_1

def TargetAllHarmBulletByType(arg_45_0, arg_45_1):
	var_45_0 = ys.Battle.BattleDataProxy.GetInstance()
	var_45_1 = table()
	var_45_2 = arg_45_0.GetIFF()

	for iter_45_0, iter_45_1 in pairs(var_45_0.GetBulletList()):
		if var_45_2 != iter_45_1.GetIFF() and iter_45_1.GetType() == arg_45_1:
			var_45_1.append(iter_45_1)

	return var_45_1

def TargetAllHarmTorpedoBullet(arg_46_0):
	return TargetAllHarmBulletByType(arg_46_0, ys.Battle.BattleConst.BulletType.TORPEDO)

def TargetFleetIndex(arg_47_0, arg_47_1):
	var_47_0

	if arg_47_0:
		var_47_0 = arg_47_0.GetIFF()
	else:
		var_47_0 = BattleConfig.FRIENDLY_CODE

	var_47_1 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(var_47_0)
	var_47_2 = TeamType.TeamPos
	var_47_3 = arg_47_1.fleetPos
	var_47_4 = table()
	var_47_5 = var_47_1.GetUnitList()
	var_47_6 = var_47_1.GetScoutList()
	var_47_7 = arg_47_1.exceptCaster

	if var_47_7:
		var_47_8 = arg_47_0.GetUniqueID()

	for iter_47_0, iter_47_1 in ipairs(var_47_5):
		var_47_9 = iter_47_1.GetUniqueID()

		if var_47_7 and var_47_9 == casterID: #???
			pass #block empty
		elif iter_47_1 == var_47_1.GetFlagShip():
			if var_47_3 == var_47_2.FLAG_SHIP:
				table.insert(var_47_4, iter_47_1)
		elif iter_47_1 == var_47_6[1]:
			if var_47_3 == var_47_2.LEADER:
				table.insert(var_47_4, iter_47_1)
		elif len(var_47_6) == 3 and iter_47_1 == var_47_6[2]:
			if var_47_3 == var_47_2.CENTER:
				table.insert(var_47_4, iter_47_1)
		elif iter_47_1 == var_47_6[len(var_47_6)]:
			if var_47_3 == var_47_2.REAR:
				table.insert(var_47_4, iter_47_1)
		elif iter_47_1.IsMainFleetUnit() and iter_47_1.GetMainUnitIndex() == 2:
			if var_47_3 == var_47_2.UPPER_CONSORT:
				table.insert(var_47_4, iter_47_1)
		elif iter_47_1.IsMainFleetUnit() and iter_47_1.GetMainUnitIndex() == 3 and var_47_3 == var_47_2.LOWER_CONSORT:
			table.insert(var_47_4, iter_47_1)

	var_47_10 = var_47_1.GetSubList()

	for iter_47_2, iter_47_3 in ipairs(var_47_5):
		if iter_47_2 == 1:
			if var_47_3 == var_47_2.SUB_LEADER:
				table.insert(var_47_4, iter_47_3)
		elif var_47_3 == var_47_2.SUB_CONSORT:
			table.insert(var_47_4, iter_47_3)

	return var_47_4

def TargetPlayerVanguardFleet(arg_48_0, arg_48_1, arg_48_2):
	var_48_0 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(arg_48_0.GetIFF()).GetScoutList()

	if not arg_48_2:
		return var_48_0
	else:
		var_48_1 = len(arg_48_2)

		while var_48_1 > 0:
			if not table.contains(var_48_0, arg_48_2[var_48_1]):
				table.remove(arg_48_2, var_48_1)

			var_48_1 = var_48_1 - 1

		return arg_48_2

def TargetPlayerMainFleet(arg_49_0, arg_49_1, arg_49_2):
	var_49_0 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(arg_49_0.GetIFF()).GetMainList()

	if not arg_49_2:
		return var_49_0
	else:
		var_49_1 = len(arg_49_2)

		while var_49_1 > 0:
			if not table.contains(var_49_0, arg_49_2[var_49_1]):
				table.remove(arg_49_2, var_49_1)

			var_49_1 = var_49_1 - 1

		return arg_49_2

def TargetPlayerFlagShip(arg_50_0, arg_50_1, arg_50_2):
	var_50_0 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(arg_50_0.GetIFF())

	return table(
		var_50_0.GetFlagShip()
	)

def TargetPlayerLeaderShip(arg_51_0, arg_51_1, arg_51_2):
	var_51_0 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(arg_51_0.GetIFF())

	return table(
		var_51_0.GetLeaderShip()
	)

def TargetPlayerByType(arg_52_0, arg_52_1):
	var_52_0 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(arg_52_0.GetIFF()).GetUnitList()
	var_52_1 = table()
	var_52_2 = arg_52_1.shipType

	for iter_52_0, iter_52_1 in ipairs(var_52_0):
		if iter_52_1.GetTemplate().type == var_52_2:
			var_52_1.append(iter_52_1)

	return var_52_1

def TargetPlayerAidUnit(arg_53_0, arg_53_1):
	var_53_0 = ys.Battle.BattleDataProxy.GetInstance().GetAidUnit()
	var_53_1 = table()

	for iter_53_0, iter_53_1 in pairs(var_53_0):
		table.insert(var_53_1, iter_53_1)

	return var_53_1

def TargetDamageSource(arg_54_0, arg_54_1, arg_54_2):
	var_54_0 = arg_54_2 or TargetAllFoe(arg_54_0)
	var_54_1 = table()

	for iter_54_0, iter_54_1 in pairs(var_54_0):
		if iter_54_1.GetUniqueID() == arg_54_1.damageSourceID:
			table.insert(var_54_1, iter_54_1)

			break

	return var_54_1

def TargetRarity(arg_55_0, arg_55_1, arg_55_2):
	var_55_0 = arg_55_2 or TargetAllHelp(arg_55_0)
	var_55_1 = table()

	for iter_55_0, iter_55_1 in ipairs(var_55_0):
		if iter_55_1.GetRarity() == arg_55_1.rarity:
			table.insert(var_55_1, iter_55_1)

	return var_55_1

def TargetIllustrator(arg_56_0, arg_56_1, arg_56_2):
	var_56_0 = arg_56_2 or TargetAllHelp(arg_56_0)
	var_56_1 = table()

	for iter_56_0, iter_56_1 in ipairs(var_56_0):
		if ys.Battle.BattleDataFunction.GetPlayerShipSkinDataFromID(iter_56_1.GetSkinID()).illustrator == arg_56_1.illustrator:
			table.insert(var_56_1, iter_56_1)

	return var_56_1

def TargetTeam(arg_57_0, arg_57_1, arg_57_2):
	var_57_0 = ys.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(arg_57_0.GetIFF())
	var_57_1 = table()
	var_57_2 = TeamType.TeamTypeIndex[arg_57_1.teamIndex]

	if var_57_2 == TeamType.Vanguard:
		var_57_1 = var_57_0.GetScoutList()
	elif var_57_2 == TeamType.Main:
		var_57_1 = var_57_0.GetMainList()
	elif var_57_2 == TeamType.Submarine:
		var_57_1 = var_57_0.GetSubList()

	var_57_3 = table()

	for iter_57_0, iter_57_1 in ipairs(var_57_1):
		if not arg_57_2 or table.contains(arg_57_2, iter_57_1):
			table.insert(var_57_3, iter_57_1)

	return var_57_3

def TargetGroup(arg_58_0, arg_58_1, arg_58_2):
	var_58_0 = arg_58_1.groupIDList
	var_58_1 = arg_58_2 or TargetAllHelp(arg_58_0)
	var_58_2 = table()
	var_58_3 = arg_58_0.GetIFF()

	for iter_58_0, iter_58_1 in ipairs(var_58_1):
		var_58_4 = iter_58_1.GetTemplateID()
		var_58_5 = ys.Battle.BattleDataFunction.GetPlayerShipModelFromID(var_58_4).group_type
		var_58_6 = iter_58_1.GetIFF()

		if table.contains(var_58_0, var_58_5) and var_58_3 == var_58_6:
			var_58_2.append(iter_58_1)

	return var_58_2

def LegalTarget(arg_59_0):
	var_59_0 = table()
	var_59_2 = ys.Battle.BattleDataProxy.GetInstance()
	var_59_3, var_59_4, var_59_5, var_59_6 = var_59_2.GetFieldBound()
	var_59_7 = var_59_2.GetUnitList()
	var_59_8 = arg_59_0.GetIFF()

	for iter_59_0, iter_59_1 in pairs(var_59_7):
		if iter_59_1.IsAlive() and iter_59_1.GetIFF() != var_59_8 and var_59_6 > iter_59_1.GetPosition().x and not iter_59_1.IsSpectre():
			var_59_0.append(iter_59_1)

	return var_59_0

def LegalWeaponTarget(arg_60_0):
	var_60_0 = table()
	var_60_2 = ys.Battle.BattleDataProxy.GetInstance().GetUnitList()
	var_60_3 = arg_60_0.GetIFF()

	for iter_60_0, iter_60_1 in pairs(var_60_2):
		if iter_60_1.GetIFF() != var_60_3 and not iter_60_1.IsSpectre():
			var_60_0.append(iter_60_1)

	return var_60_0
