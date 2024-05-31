local var_0_0 = class("GetBackYardVisitorCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().callback

	pg.ConnectionMgr.GetInstance():Send(19024, {
		type = 0
	}, 19025, function(arg_2_0)
		if arg_2_0.visitor and arg_2_0.visitor.ship_template ~= 0 then
			local var_2_0 = Ship.New({
				id = 99999999,
				template_id = arg_2_0.visitor.ship_template,
				name = arg_2_0.visitor.name,
				skin_id = arg_2_0.visitor.ship_skin
			})

			getProxy(DormProxy):SetVisitorShip(var_2_0)
		end

		if var_1_0 then
			var_1_0()
		end

		arg_1_0:sendNotification(GAME.BACKYARD_GET_VISITOR_SHIP_DONE)
	end)
end

return var_0_0
