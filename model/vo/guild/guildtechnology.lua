local var_0_0 = class("GuildTechnology", import("..BaseVO"))

var_0_0.UPGRADE_TYPE_SELF = 1
var_0_0.UPGRADE_TYPE_PUBLIC = 2

function var_0_0.Ctor(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_0:bindConfigTable().get_id_list_by_group[arg_1_1.id][1]

	arg_1_0:Update(var_1_0, arg_1_1)
end

function var_0_0.Update(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.group = arg_2_2

	if arg_2_0.group:GuildMemberCntType() then
		arg_2_0.id = arg_2_0.group.pid
	else
		arg_2_0.id = arg_2_1
	end

	arg_2_0.configId = arg_2_0.id
	arg_2_0.level = arg_2_0:getConfig("level")
end

function var_0_0.GetShipAttrAddition(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = arg_3_0:getConfig("effect_args")
	local var_3_1 = var_3_0[1]
	local var_3_2 = var_3_0[2]

	if var_3_1 == arg_3_1 and table.contains(var_3_2, arg_3_2) then
		return arg_3_0:getConfig("num")
	else
		return 0
	end
end

function var_0_0.GetTargetLivness(arg_4_0)
	local var_4_0 = arg_4_0:GetNextLevelId()

	if var_4_0 == 0 then
		return 0
	else
		return pg.guild_technology_template[var_4_0].need_guild_active
	end
end

function var_0_0.ReachTargetLiveness(arg_5_0, arg_5_1)
	return arg_5_1:GetLiveness() >= arg_5_0:GetTargetLivness()
end

function var_0_0._ReachTargetLiveness_(arg_6_0)
	local var_6_0 = getProxy(PlayerProxy):getRawData().id
	local var_6_1 = getProxy(GuildProxy):getRawData():getMemberById(var_6_0)

	return arg_6_0:ReachTargetLiveness(var_6_1)
end

function var_0_0.levelUp(arg_7_0)
	local var_7_0 = arg_7_0:GetNextLevelId()

	if var_7_0 ~= 0 then
		arg_7_0:Update(var_7_0, arg_7_0.group)
	end
end

function var_0_0.GetNextLevelId(arg_8_0)
	return arg_8_0:getConfig("next_tech")
end

function var_0_0.GetLevel(arg_9_0)
	return arg_9_0.level
end

function var_0_0.isMaxLevel(arg_10_0)
	return arg_10_0:GetLevel() >= arg_10_0:GetMaxLevel()
end

function var_0_0.CanUpgradeBySelf(arg_11_0)
	local var_11_0 = arg_11_0:_ReachTargetLiveness_()
	local var_11_1 = arg_11_0:GetLevel() < arg_11_0:GetMaxLevel()

	return var_11_0 and var_11_1, var_11_0, var_11_1
end

function var_0_0.GetLivenessOffset(arg_12_0)
	local var_12_0 = getProxy(PlayerProxy):getRawData().id
	local var_12_1 = getProxy(GuildProxy):getRawData():getMemberById(var_12_0)

	return arg_12_0:GetTargetLivness() - var_12_1:GetLiveness()
end

function var_0_0.GetUpgradeType(arg_13_0)
	if arg_13_0:CanUpgradeBySelf() then
		return var_0_0.UPGRADE_TYPE_SELF
	else
		local var_13_0 = arg_13_0.group:GetFakeLevel()
		local var_13_1 = arg_13_0:GetMaxLevel()

		if var_13_0 > arg_13_0:GetLevel() then
			return var_0_0.UPGRADE_TYPE_PUBLIC
		end
	end

	return false
end

function var_0_0.CanUpgrade(arg_14_0)
	return arg_14_0:GetUpgradeType() ~= false
end

function var_0_0.GetMaxLevel(arg_15_0)
	return arg_15_0.group:GetLevel()
end

function var_0_0.bindConfigTable(arg_16_0)
	return pg.guild_technology_template
end

function var_0_0.GetDesc(arg_17_0)
	local var_17_0 = arg_17_0:getConfig("effect_args")
	local var_17_1 = arg_17_0:getConfig("num")

	return GuildConst.GET_TECHNOLOGY_DESC(var_17_0, var_17_1)
end

function var_0_0.getAddition(arg_18_0)
	if arg_18_0:GetLevel() > 0 then
		return arg_18_0:getConfig("num")
	else
		return 0
	end
end

function var_0_0.GetConsume(arg_19_0)
	local var_19_0 = arg_19_0:getConfig("contribution_consume")
	local var_19_1 = arg_19_0:getConfig("gold_consume")

	if arg_19_0:IsRiseInPrice() then
		local var_19_2 = arg_19_0:getConfig("contribution_multiple")

		return var_19_0 * var_19_2, var_19_1 * var_19_2
	else
		return var_19_0, var_19_1
	end
end

function var_0_0.IsRiseInPrice(arg_20_0)
	return arg_20_0:GetUpgradeType() == var_0_0.UPGRADE_TYPE_PUBLIC
end

function var_0_0.IsGuildMember(arg_21_0)
	return arg_21_0:getConfig("group") == 1
end

return var_0_0
