local var_0_0 = class("EquipCommanderToFleetCommande", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.commanderId
	local var_1_2 = var_1_0.pos
	local var_1_3 = var_1_0.fleetId
	local var_1_4 = var_1_0.callback
	local var_1_5

	if var_1_1 ~= 0 then
		var_1_5 = getProxy(CommanderProxy):getCommanderById(var_1_1)

		if not var_1_5 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("commander_not_exist"))

			return
		end
	end

	local var_1_6 = getProxy(FleetProxy)
	local var_1_7 = var_1_6:getFleetById(var_1_3)

	if not var_1_7 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("commander_fleet_not_exist"))

		return
	end

	if var_1_1 == 0 and not var_1_7:getCommanderByPos(var_1_2) then
		if var_1_4 then
			var_1_4()
		end

		return
	end

	pg.ConnectionMgr.GetInstance():Send(25006, {
		groupid = var_1_3,
		pos = var_1_2,
		commanderid = var_1_1
	}, 25007, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_7:updateCommanderByPos(var_1_2, var_1_5)
			var_1_6:updateFleet(var_1_7)

			if var_1_4 then
				var_1_4(var_1_7)
			end

			arg_1_0:sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("commander_equip_to_fleet_erro", arg_2_0.result))
		end
	end)
end

return var_0_0
