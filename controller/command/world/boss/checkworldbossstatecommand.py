local var_0_0 = class("CheckWorldBossStateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.bossId
	local var_1_2 = var_1_0.callback
	local var_1_3 = tonumber(var_1_0.time or 0)
	local var_1_4 = var_1_0.failedCallback

	local function var_1_5()
		local var_2_0 = getProxy(ChatProxy)
		local var_2_1 = var_2_0.GetMessagesByUniqueId(var_1_1 .. "_" .. var_1_3)

		for iter_2_0, iter_2_1 in ipairs(var_2_1):
			iter_2_1.args.isDeath = True

			var_2_0.UpdateMsg(iter_2_1)

		local var_2_2 = getProxy(GuildProxy)
		local var_2_3 = var_2_2.GetMessagesByUniqueId(var_1_1 .. "_" .. var_1_3)

		for iter_2_2, iter_2_3 in ipairs(var_2_3):
			iter_2_3.args.isDeath = True

			var_2_2.UpdateMsg(iter_2_3)

		if var_1_4:
			var_1_4()

	print("boss id", var_1_1, " time.", var_1_3)
	pg.ConnectionMgr.GetInstance().Send(34515, {
		boss_id = var_1_1,
		last_time = var_1_3
	}, 34516, function(arg_3_0)
		if arg_3_0.result == 0:
			if var_1_2:
				var_1_2()
		elif arg_3_0.result == 1:
			var_1_5()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_none"))
		elif arg_3_0.result == 3:
			var_1_5()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_none"))
		elif arg_3_0.result == 6:
			var_1_5()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_max_challenge_cnt"))
		elif arg_3_0.result == 20:
			var_1_5()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_none"))
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_3_0.result] .. arg_3_0.result))

return var_0_0
