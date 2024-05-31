local var_0_0 = class("ChangeEducateCharacterCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().id
	local var_1_1 = getProxy(PlayerProxy):getRawData():GetEducateCharacter()

	pg.ConnectionMgr.GetInstance():Send(27041, {
		ending_id = var_1_0
	}, 27042, function(arg_2_0)
		if arg_2_0.result == 0 then
			if var_1_0 > 0 and var_1_1 and pg.secretary_special_ship[var_1_1] then
				local var_2_0 = pg.secretary_special_ship[var_1_1].group

				if var_2_0 == pg.secretary_special_ship[var_1_0].group and var_2_0 == 1000 then
					getProxy(PlayerProxy):setFlag("change_tb", true)
				end
			end

			local var_2_1 = getProxy(PlayerProxy)
			local var_2_2 = var_2_1:getData()

			var_2_2:SetEducateCharacter(var_1_0)
			var_2_1:updatePlayer(var_2_2)
			arg_1_0:sendNotification(GAME.CHANGE_EDUCATE_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
