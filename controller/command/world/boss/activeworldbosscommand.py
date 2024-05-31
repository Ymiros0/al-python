local var_0_0 = class("ActiveWorldBossCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.type

	pg.ConnectionMgr.GetInstance().Send(34521, {
		template_id = var_1_1
	}, 34522, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = nowWorld().GetBossProxy()

			var_2_0.RemoveSelfBoss()

			local var_2_1 = WorldBoss.New()

			var_2_1.Setup(arg_2_0.boss, getProxy(PlayerProxy).getData())
			var_2_1.UpdateBossType(WorldBoss.BOSS_TYPE_SELF)
			var_2_1.SetJoinTime(pg.TimeMgr.GetInstance().GetServerTime())

			if var_2_0.isSetup:
				var_2_0.ClearRank(var_2_1.id)
				var_2_0.UpdateCacheBoss(var_2_1)

				if var_1_2 == WorldBossConst.BOSS_TYPE_CURR:
					local var_2_2 = WorldBossConst.GetCurrBossConsume()

					var_2_0.ConsumeSummonPt(var_2_2)
				elif var_1_2 == WorldBossConst.BOSS_TYPE_ARCHIVES:
					local var_2_3 = WorldBossConst.GetAchieveBossConsume()

					var_2_0.ConsumeSummonPtOld(var_2_3)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
