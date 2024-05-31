local var_0_0 = class("GetCacheBossHpCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().callback
	local var_1_1 = nowWorld().GetBossProxy()
	local var_1_2 = var_1_1.GetCacheBossList()

	if not var_1_2 or #var_1_2 == 0:
		if var_1_0:
			var_1_0()

		return

	local var_1_3 = _.map(var_1_2, function(arg_2_0)
		return arg_2_0.id)

	pg.ConnectionMgr.GetInstance().Send(34517, {
		boss_id = var_1_3
	}, 34518, function(arg_3_0)
		for iter_3_0, iter_3_1 in pairs(arg_3_0.list):
			local var_3_0 = var_1_1.GetCacheBoss(iter_3_1.id)

			if var_3_0:
				var_3_0.UpdateHp(iter_3_1.hp)
				var_3_0.SetRankCnt(iter_3_1.rank_count)

		if var_1_0:
			var_1_0())

return var_0_0
