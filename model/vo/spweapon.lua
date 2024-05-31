local var_0_0 = class("SpWeapon", import(".BaseVO"))

var_0_0.type = DROP_TYPE_SPWEAPON
var_0_0.CONFIRM_OP_DISCARD = 0
var_0_0.CONFIRM_OP_EXCHANGE = 1

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.configId = arg_1_1.id
end

function var_0_0.CreateByNet(arg_2_0)
	if arg_2_0.template_id == 0 then
		return
	end

	local var_2_0 = {
		uid = arg_2_0.id,
		id = arg_2_0.template_id,
		attr1 = arg_2_0.attr_1,
		attr2 = arg_2_0.attr_2,
		attrTemp1 = arg_2_0.attr_temp_1,
		attrTemp2 = arg_2_0.attr_temp_2,
		pt = arg_2_0.pt
	}

	return var_0_0.New(var_2_0)
end

function var_0_0.bindConfigTable(arg_3_0)
	return pg.spweapon_data_statistics
end

function var_0_0.GetUID(arg_4_0)
	return arg_4_0.uid
end

function var_0_0.IsReal(arg_5_0)
	return tobool(arg_5_0:GetUID())
end

function var_0_0.GetConfigID(arg_6_0)
	return arg_6_0.configId
end

function var_0_0.GetOriginID(arg_7_0)
	return arg_7_0:getConfig("base") or arg_7_0:GetConfigID()
end

function var_0_0.IsImportant(arg_8_0)
	return arg_8_0:getConfig("important") == 2
end

function var_0_0.IsUnique(arg_9_0)
	return arg_9_0:getConfig("unique") ~= 0
end

function var_0_0.GetUniqueGroup(arg_10_0)
	return arg_10_0:getConfig("unique")
end

function var_0_0.GetType(arg_11_0)
	return arg_11_0:getConfig("type")
end

function var_0_0.GetName(arg_12_0)
	return arg_12_0:getConfig("name")
end

function var_0_0.GetLevel(arg_13_0)
	return arg_13_0:getConfig("level")
end

function var_0_0.GetTechTier(arg_14_0)
	return arg_14_0:getConfig("tech")
end

function var_0_0.GetIconPath(arg_15_0)
	return "SpWeapon/" .. arg_15_0:getConfig("icon")
end

function var_0_0.GetRarity(arg_16_0)
	return arg_16_0:getConfig("rarity")
end

function var_0_0.GetPt(arg_17_0)
	return arg_17_0:IsReal() and arg_17_0.pt or 0
end

function var_0_0.SetPt(arg_18_0, arg_18_1)
	assert(arg_18_1)

	arg_18_0.pt = arg_18_1 or 0
end

function var_0_0.GetEffect(arg_19_0)
	return arg_19_0:getConfig("effect_id")
end

function var_0_0.GetDisplayEffect(arg_20_0)
	return arg_20_0:getConfig("effect_id_display")
end

function var_0_0.GetUpgradableSkillIds(arg_21_0)
	return arg_21_0:getConfig("skill_upgrade")
end

function var_0_0.GetNextUpgradeID(arg_22_0)
	return arg_22_0:getConfig("next")
end

function var_0_0.GetPrevUpgradeID(arg_23_0)
	return arg_23_0:getConfig("prev")
end

function var_0_0.MigrateTo(arg_24_0, arg_24_1)
	local var_24_0 = Clone(arg_24_0)

	var_24_0.id = arg_24_1
	var_24_0.configId = arg_24_1
	var_24_0.pt = 0

	return var_24_0
end

function var_0_0.GetLabel(arg_25_0)
	return arg_25_0:getConfig("label")
end

function var_0_0.SetShipId(arg_26_0, arg_26_1)
	arg_26_0.shipId = arg_26_1
end

function var_0_0.GetShipId(arg_27_0)
	return arg_27_0.shipId
end

function var_0_0.GetSkill(arg_28_0)
	local var_28_0 = arg_28_0:GetEffect()

	return var_28_0 > 0 and getSkillConfig(var_28_0) or nil
end

function var_0_0.GetSkillInfo(arg_29_0)
	local var_29_0 = {
		lv = 1,
		skillId = arg_29_0:GetDisplayEffect()
	}

	var_29_0.unlock = var_29_0.skillId == arg_29_0:GetEffect()

	return var_29_0
end

function var_0_0.GetUpgradableSkillInfo(arg_30_0)
	local var_30_0 = 0
	local var_30_1 = 1
	local var_30_2 = false
	local var_30_3 = arg_30_0:GetShipId()

	if var_30_3 then
		local var_30_4 = getProxy(BayProxy):getShipById(var_30_3)
		local var_30_5, var_30_6 = arg_30_0:GetActiveUpgradableSkill(var_30_4)

		if var_30_5 then
			var_30_0 = var_30_5

			local var_30_7 = var_30_4 and var_30_4.skills[var_30_6]

			var_30_1 = var_30_7 and var_30_7.level or var_30_1
			var_30_2 = true
		end
	end

	if var_30_0 == 0 then
		local var_30_8 = arg_30_0:GetUpgradableSkillIds()[1]

		if var_30_8 and var_30_8[2] then
			var_30_0 = var_30_8[2]
			var_30_2 = var_30_8[1] ~= 0
		end
	end

	return {
		skillId = var_30_0,
		lv = var_30_1,
		unlock = var_30_2
	}
end

function var_0_0.GetActiveUpgradableSkill(arg_31_0, arg_31_1)
	for iter_31_0, iter_31_1 in ipairs(arg_31_1:getSkillList()) do
		local var_31_0, var_31_1 = arg_31_0:RemapSkillId(iter_31_1)

		if var_31_1 then
			return var_31_0, iter_31_1
		end
	end
end

function var_0_0.RemapSkillId(arg_32_0, arg_32_1)
	for iter_32_0, iter_32_1 in ipairs(arg_32_0:GetUpgradableSkillIds()) do
		if iter_32_1[1] == arg_32_1 then
			return iter_32_1[2], true
		end
	end

	return arg_32_1, false
end

function var_0_0.GetSkillGroup(arg_33_0)
	return {
		arg_33_0:GetSkillInfo(),
		(arg_33_0:GetUpgradableSkillInfo())
	}
end

function var_0_0.GetConfigAttributes(arg_34_0)
	return {
		arg_34_0:getConfig("value_1"),
		arg_34_0:getConfig("value_2")
	}
end

function var_0_0.GetAttributesRange(arg_35_0)
	return {
		arg_35_0:getConfig("value_1_random"),
		arg_35_0:getConfig("value_2_random")
	}
end

function var_0_0.GetAttributes(arg_36_0)
	local var_36_0 = arg_36_0:GetConfigAttributes()

	if arg_36_0:IsReal() then
		var_36_0[1] = var_36_0[1] + arg_36_0.attr1
		var_36_0[2] = var_36_0[2] + arg_36_0.attr2
	end

	return var_36_0
end

function var_0_0.GetBaseAttributes(arg_37_0)
	return {
		arg_37_0.attr1 or 0,
		arg_37_0.attr2 or 0
	}
end

function var_0_0.SetBaseAttributes(arg_38_0, arg_38_1)
	arg_38_0.attr1 = arg_38_1[1]
	arg_38_0.attr2 = arg_38_1[2]
end

function var_0_0.GetAttributeOptions(arg_39_0)
	return {
		arg_39_0.attrTemp1 or 0,
		arg_39_0.attrTemp2 or 0
	}
end

function var_0_0.SetAttributeOptions(arg_40_0, arg_40_1)
	arg_40_0.attrTemp1 = arg_40_1[1]
	arg_40_0.attrTemp2 = arg_40_1[2]
end

function var_0_0.GetPropertiesInfo(arg_41_0)
	local var_41_0 = {
		attrs = {}
	}
	local var_41_1 = arg_41_0:GetAttributes()

	table.insert(var_41_0.attrs, {
		type = arg_41_0:getConfig("attribute_1"),
		value = var_41_1[1]
	})
	table.insert(var_41_0.attrs, {
		type = arg_41_0:getConfig("attribute_2"),
		value = var_41_1[2]
	})

	var_41_0.weapon = {
		sub = {}
	}
	var_41_0.equipInfo = {
		sub = {}
	}

	local var_41_2 = arg_41_0:GetWearableShipTypes()

	var_41_0.part = {
		var_41_2,
		var_41_2
	}

	return var_41_0
end

function var_0_0.GetWearableShipTypes(arg_42_0)
	local var_42_0 = arg_42_0:getConfig("usability")

	if var_42_0 and #var_42_0 > 0 then
		return var_42_0
	end

	return pg.spweapon_type[arg_42_0:GetType()].ship_type
end

function var_0_0.IsCraftable(arg_43_0)
	return not arg_43_0:IsUnCraftable() and arg_43_0:GetUpgradeConfig().create_use_gold > 0
end

function var_0_0.GetUpgradeConfig(arg_44_0)
	local var_44_0 = arg_44_0:getConfig("upgrade_id")

	return pg.spweapon_upgrade[var_44_0]
end

function var_0_0.IsUnCraftable(arg_45_0)
	return arg_45_0:getConfig("uncraftable") == 1
end

function var_0_0.CalculateHistoryPt(arg_46_0, arg_46_1)
	local var_46_0 = _.reduce(arg_46_0, 0, function(arg_47_0, arg_47_1)
		return arg_47_0 + Item.getConfigData(arg_47_1.id).usage_arg[1] * arg_47_1.count
	end)

	return (_.reduce(arg_46_1, var_46_0, function(arg_48_0, arg_48_1)
		return arg_48_0 + (0 + arg_48_1:GetUpgradeConfig().upgrade_supply_pt)
	end))
end

return var_0_0
