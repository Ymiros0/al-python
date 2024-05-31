local var_0_0 = class("PublicGuildTechnology", import("..GuildTechnology"))

function var_0_0.GetConsume(arg_1_0)
	local var_1_0 = arg_1_0:getConfig("contribution_consume")
	local var_1_1 = arg_1_0:getConfig("gold_consume")
	local var_1_2 = arg_1_0:getConfig("contribution_multiple")

	return var_1_0 * var_1_2, var_1_1 * var_1_2
end

return var_0_0
