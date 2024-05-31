local var_0_0 = class("WorldBossSupportCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().type

	assert(var_1_0)

	local var_1_1 = nowWorld().worldBossProxy
	local var_1_2 = var_1_1.GetSelfBoss()

	if not var_1_2:
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_not_found"))

		return

	if var_1_2.isDeath():
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_is_death"))

		return

	if var_1_0 == WorldBoss.SUPPORT_TYPE_GUILD:
		if not getProxy(GuildProxy).getRawData():
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_whitout_guild"))

			return
	elif var_1_0 == WorldBoss.SUPPORT_TYPE_FRIEND:
		local var_1_3 = getProxy(FriendProxy).getRawData()

		if table.getCount(var_1_3) <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_whitout_friend"))

			return

	local function var_1_4(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_0 == WorldBoss.SUPPORT_TYPE_FRIEND:
				var_1_1.UpdateFriendSupported()
			elif var_1_0 == WorldBoss.SUPPORT_TYPE_GUILD:
				var_1_1.UpdateGuildSupported()
			elif var_1_0 == WorldBoss.SUPPORT_TYPE_WORLD:
				var_1_1.UpdateWorldSupported()

			var_1_1.UpdateSelfBoss(var_1_2)
			arg_1_0.sendNotification(GAME.WORLD_BOSS_SUPPORT_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_call_support_failed") .. arg_2_0.result)

	pg.ConnectionMgr.GetInstance().Send(34509, {
		type = var_1_0
	}, 34510, var_1_4)

return var_0_0
