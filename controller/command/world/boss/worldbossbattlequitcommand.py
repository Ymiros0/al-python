local var_0_0 = class("WorldBossBattleQuitCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id

	if not var_1_0:
		return

	local var_1_1 = nowWorld().GetBossProxy()
	local var_1_2 = var_1_1.GetBossById(var_1_0)

	if var_1_2 and not var_1_1.IsSelfBoss(var_1_2):
		var_1_1.RemoveCacheBoss(var_1_0)

		local var_1_3 = getProxy(ChatProxy)
		local var_1_4 = var_1_3.GetMessagesByUniqueId(var_1_0 .. "_" .. var_1_2.lastTime)

		for iter_1_0, iter_1_1 in ipairs(var_1_4):
			iter_1_1.args.isDeath = True

			var_1_3.UpdateMsg(iter_1_1)

		local var_1_5 = getProxy(GuildProxy)
		local var_1_6 = var_1_5.GetMessagesByUniqueId(var_1_0 .. "_" .. var_1_2.lastTime)

		for iter_1_2, iter_1_3 in ipairs(var_1_6):
			iter_1_3.args.isDeath = True

			var_1_5.UpdateMsg(iter_1_3)

return var_0_0
