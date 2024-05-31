local var_0_0 = class("FriendDorm", import(".Dorm"))

function var_0_0.GetName(arg_1_0)
	if getProxy(PlayerProxy):getRawData():ShouldCheckCustomName() then
		return i18n("nodisplay_player_home_name")
	else
		return var_0_0.super.GetName(arg_1_0)
	end
end

function var_0_0.GetShips(arg_2_0)
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.shipIds) do
		local var_2_1 = Ship.New({
			energy = 100,
			id = iter_2_1.id,
			configId = iter_2_1.tid,
			skin_id = iter_2_1.skin_id
		})

		var_2_1.state = iter_2_1.state

		var_2_1:updateStateInfo34(0, 0)

		var_2_0[var_2_1.id] = var_2_1
	end

	return var_2_0
end

return var_0_0
