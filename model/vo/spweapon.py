

from const import DROP_TYPE_SPWEAPON
from Framework import underscore
from lib import pg
from model.proxy.BayProxy import BayProxy
from BaseVO import BaseVO
from Item import Item
from packages.luatable import Clone, ipairs, table
from support.helpers.M02 import getProxy, getSkillConfig


class SpWeapon(BaseVO):

	type = DROP_TYPE_SPWEAPON
	CONFIRM_OP_DISCARD = 0
	CONFIRM_OP_EXCHANGE = 1

	def __init__(arg_1_0, arg_1_1):
		super().__init__(arg_1_0, arg_1_1)

		arg_1_0.configId = arg_1_1.id

	def CreateByNet(arg_2_0):
		if arg_2_0.template_id == 0:
			return

		var_2_0 = table(
			uid = arg_2_0.id,
			id = arg_2_0.template_id,
			attr1 = arg_2_0.attr_1,
			attr2 = arg_2_0.attr_2,
			attrTemp1 = arg_2_0.attr_temp_1,
			attrTemp2 = arg_2_0.attr_temp_2,
			pt = arg_2_0.pt
		)

		return SpWeapon(var_2_0)

	def bindConfigTable(arg_3_0):
		return pg.spweapon_data_statistics

	def GetUID(arg_4_0):
		return arg_4_0.uid

	def IsReal(arg_5_0):
		return bool(arg_5_0.GetUID())

	def GetConfigID(arg_6_0):
		return arg_6_0.configId

	def GetOriginID(arg_7_0):
		return arg_7_0.getConfig("base") or arg_7_0.GetConfigID()

	def IsImportant(arg_8_0):
		return arg_8_0.getConfig("important") == 2

	def IsUnique(arg_9_0):
		return arg_9_0.getConfig("unique") != 0

	def GetUniqueGroup(arg_10_0):
		return arg_10_0.getConfig("unique")

	def GetType(arg_11_0):
		return arg_11_0.getConfig("type")

	def GetName(arg_12_0):
		return arg_12_0.getConfig("name")

	def GetLevel(arg_13_0):
		return arg_13_0.getConfig("level")

	def GetTechTier(arg_14_0):
		return arg_14_0.getConfig("tech")

	def GetIconPath(arg_15_0):
		return f"SpWeapon/{arg_15_0.getConfig("icon")}"

	def GetRarity(arg_16_0):
		return arg_16_0.getConfig("rarity")

	def GetPt(arg_17_0):
		return arg_17_0.IsReal() and arg_17_0.pt or 0

	def SetPt(arg_18_0, arg_18_1):
		assert(arg_18_1)

		arg_18_0.pt = arg_18_1 or 0

	def GetEffect(arg_19_0):
		return arg_19_0.getConfig("effect_id")

	def GetDisplayEffect(arg_20_0):
		return arg_20_0.getConfig("effect_id_display")

	def GetUpgradableSkillIds(arg_21_0):
		return arg_21_0.getConfig("skill_upgrade")

	def GetNextUpgradeID(arg_22_0):
		return arg_22_0.getConfig("next")

	def GetPrevUpgradeID(arg_23_0):
		return arg_23_0.getConfig("prev")

	def MigrateTo(arg_24_0, arg_24_1):
		var_24_0 = Clone(arg_24_0)

		var_24_0.id = arg_24_1
		var_24_0.configId = arg_24_1
		var_24_0.pt = 0

		return var_24_0

	def GetLabel(arg_25_0):
		return arg_25_0.getConfig("label")

	def SetShipId(arg_26_0, arg_26_1):
		arg_26_0.shipId = arg_26_1

	def GetShipId(arg_27_0):
		return arg_27_0.shipId

	def GetSkill(arg_28_0):
		var_28_0 = arg_28_0.GetEffect()

		return var_28_0 > 0 and getSkillConfig(var_28_0) or None

	def GetSkillInfo(arg_29_0):
		var_29_0 = table(
			lv = 1,
			skillId = arg_29_0.GetDisplayEffect()
		)

		var_29_0.unlock = var_29_0.skillId == arg_29_0.GetEffect()

		return var_29_0

	def GetUpgradableSkillInfo(arg_30_0):
		var_30_0 = 0
		var_30_1 = 1
		var_30_2 = False
		var_30_3 = arg_30_0.GetShipId()

		if var_30_3:
			var_30_4 = getProxy(BayProxy).getShipById(var_30_3)
			var_30_5, var_30_6 = arg_30_0.GetActiveUpgradableSkill(var_30_4)

			if var_30_5:
				var_30_0 = var_30_5

				var_30_7 = var_30_4 and var_30_4.skills[var_30_6]

				var_30_1 = var_30_7 and var_30_7.level or var_30_1
				var_30_2 = True

		if var_30_0 == 0:
			var_30_8 = arg_30_0.GetUpgradableSkillIds()[1]

			if var_30_8 and var_30_8[2]:
				var_30_0 = var_30_8[2]
				var_30_2 = var_30_8[1] != 0

		return table(
			skillId = var_30_0,
			lv = var_30_1,
			unlock = var_30_2
		)

	def GetActiveUpgradableSkill(arg_31_0, arg_31_1):
		for iter_31_0, iter_31_1 in ipairs(arg_31_1.getSkillList()):
			var_31_0, var_31_1 = arg_31_0.RemapSkillId(iter_31_1)

			if var_31_1:
				return var_31_0, iter_31_1

	def RemapSkillId(arg_32_0, arg_32_1):
		for iter_32_0, iter_32_1 in ipairs(arg_32_0.GetUpgradableSkillIds()):
			if iter_32_1[1] == arg_32_1:
				return iter_32_1[2], True

		return arg_32_1, False

	def GetSkillGroup(arg_33_0):
		return table(
			arg_33_0.GetSkillInfo(),
			(arg_33_0.GetUpgradableSkillInfo())
		)

	def GetConfigAttributes(arg_34_0):
		return table(
			arg_34_0.getConfig("value_1"),
			arg_34_0.getConfig("value_2")
		)

	def GetAttributesRange(arg_35_0):
		return table(
			arg_35_0.getConfig("value_1_random"),
			arg_35_0.getConfig("value_2_random")
		)

	def GetAttributes(arg_36_0):
		var_36_0 = arg_36_0.GetConfigAttributes()

		if arg_36_0.IsReal():
			var_36_0[1] = var_36_0[1] + arg_36_0.attr1
			var_36_0[2] = var_36_0[2] + arg_36_0.attr2

		return var_36_0

	def GetBaseAttributes(arg_37_0):
		return table(
			arg_37_0.attr1 or 0,
			arg_37_0.attr2 or 0
		)

	def SetBaseAttributes(arg_38_0, arg_38_1):
		arg_38_0.attr1 = arg_38_1[1]
		arg_38_0.attr2 = arg_38_1[2]

	def GetAttributeOptions(arg_39_0):
		return table(
			arg_39_0.attrTemp1 or 0,
			arg_39_0.attrTemp2 or 0
		)

	def SetAttributeOptions(arg_40_0, arg_40_1):
		arg_40_0.attrTemp1 = arg_40_1[1]
		arg_40_0.attrTemp2 = arg_40_1[2]

	def GetPropertiesInfo(arg_41_0):
		var_41_0 = table(
			attrs = table()
		)
		var_41_1 = arg_41_0.GetAttributes()

		table.insert(var_41_0.attrs, table(
			type = arg_41_0.getConfig("attribute_1"),
			value = var_41_1[1]
		))
		table.insert(var_41_0.attrs, table(
			type = arg_41_0.getConfig("attribute_2"),
			value = var_41_1[2]
		))

		var_41_0.weapon = table(
			sub = table()
		)
		var_41_0.equipInfo = table(
			sub = table()
		)

		var_41_2 = arg_41_0.GetWearableShipTypes()

		var_41_0.part = table(
			var_41_2,
			var_41_2
		)

		return var_41_0

	def GetWearableShipTypes(arg_42_0):
		var_42_0 = arg_42_0.getConfig("usability")

		if var_42_0 and len(var_42_0) > 0:
			return var_42_0

		return pg.spweapon_type[arg_42_0.GetType()].ship_type

	def IsCraftable(arg_43_0):
		return not arg_43_0.IsUnCraftable() and arg_43_0.GetUpgradeConfig().create_use_gold > 0

	def GetUpgradeConfig(arg_44_0):
		var_44_0 = arg_44_0.getConfig("upgrade_id")

		return pg.spweapon_upgrade[var_44_0]

	def IsUnCraftable(arg_45_0):
		return arg_45_0.getConfig("uncraftable") == 1

	def CalculateHistoryPt(arg_46_0, arg_46_1):
		var_46_0 = underscore.reduce(arg_46_0, 0, lambda arg_47_0, arg_47_1: arg_47_0 + Item.getConfigData(arg_47_1.id).usage_arg[1] * arg_47_1.count)

		return (underscore.reduce(arg_46_1, var_46_0, lambda arg_48_0, arg_48_1: arg_48_0 + (0 + arg_48_1.GetUpgradeConfig().upgrade_supply_pt)))