local var_0_0 = class("BackYardShipAddExpCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(DormProxy):getBackYardShips()
	local var_1_2 = getProxy(BayProxy)
	local var_1_3 = {}
	local var_1_4 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_1) do
		if iter_1_1.state == Ship.STATE_TRAIN then
			local var_1_5 = var_1_2:getShipById(iter_1_1.id)
			local var_1_6 = Clone(var_1_5)

			if var_1_5.level ~= var_1_5:getMaxLevel() then
				var_1_5:addExp(var_1_0)
				var_1_2:updateShip(var_1_5)
				arg_1_0:sendNotification(GAME.BACKYARD_SHIP_EXP_ADDED, {
					id = var_1_5.id,
					exp = var_1_0
				})
			end

			var_1_3[var_1_5.id] = var_1_5
			var_1_4[var_1_5.id] = var_1_6
		end
	end

	arg_1_0:sendNotification(DormProxy.SHIPS_EXP_ADDED, {
		oldShips = var_1_4,
		newShips = var_1_3
	})
end

return var_0_0
