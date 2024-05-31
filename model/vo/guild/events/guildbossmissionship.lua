local var_0_0 = class("GuildBossMissionShip")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.super = arg_1_1

	setmetatable(arg_1_0, {
		__index = function(arg_2_0, arg_2_1)
			local var_2_0 = rawget(arg_2_0, "class")

			return var_2_0[arg_2_1] and var_2_0[arg_2_1] or arg_1_1[arg_2_1]
		end
	})
end

function var_0_0.IsOwner(arg_3_0)
	return tonumber(GuildAssaultFleet.GetUserId(arg_3_0.id)) == getProxy(PlayerProxy):getRawData().id
end

function var_0_0.GetUniqueId(arg_4_0)
	return GuildAssaultFleet.GetRealId(arg_4_0.id)
end

function var_0_0.getProperties(arg_5_0, arg_5_1, arg_5_2)
	local var_5_0 = getProxy(GuildProxy):getRawData()
	local var_5_1 = {}
	local var_5_2 = arg_5_0.super:getProperties(arg_5_1, arg_5_2)

	for iter_5_0, iter_5_1 in pairs(var_5_2) do
		local var_5_3 = var_5_0:getShipAddition(iter_5_0, arg_5_0:getShipType())

		var_5_1[iter_5_0] = (var_5_2[iter_5_0] or 0) + var_5_3
	end

	return var_5_1
end

return var_0_0
