local var_0_0 = class("GetWBOtherBossCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().type
	local var_1_1 = {}

	if var_1_0 == WorldBoss.OTHER_BOSS_TYPE_FRIEND:
		local var_1_2 = getProxy(FriendProxy).getRawData()

		for iter_1_0, iter_1_1 in pairs(var_1_2):
			table.insert(var_1_1, iter_1_1.id)
	elif var_1_0 == WorldBoss.OTHER_BOSS_TYPE_GUILD:
		local var_1_3 = getProxy(GuildProxy).getRawData()

		for iter_1_2, iter_1_3 in pairs(var_1_3.member):
			table.insert(var_1_1, iter_1_3.id)

	if #var_1_1 == 0:
		return

	pg.ConnectionMgr.GetInstance().Send(33503, {
		user_id_list = var_1_1
	}, 33504, function(arg_2_0)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.boss_list):
			local var_2_1 = WorldBoss.New()

			var_2_1.Setup(iter_2_1)
			table.insert(var_2_0, var_2_1)

		nowWorld().GetBossProxy().UpdateOtheroBosses(var_2_0)
		arg_1_0.sendNotification(GAME.WORLD_BOSS_GET_OTHER_BOSS_DONE))

return var_0_0
