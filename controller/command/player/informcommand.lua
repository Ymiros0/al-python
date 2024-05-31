local var_0_0 = class("InformCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.playerId
	local var_1_2 = var_1_0.info
	local var_1_3 = var_1_0.content

	if not var_1_1 or not var_1_2 or not var_1_3 then
		return
	end

	if getProxy(PlayerProxy):getRawData().level < 20 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("inform_level_limit"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(50111, {
		id = var_1_1,
		info = var_1_2,
		content = var_1_3
	}, 50112, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(ChatProxy)

			table.insert(var_2_0.informs, var_1_1 .. var_1_3)
			pg.TipsMgr.GetInstance():ShowTips(i18n("inform_sueecss"))
			arg_1_0:sendNotification(GAME.INFORM_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("inform_failed"))
		end
	end)
end

return var_0_0
