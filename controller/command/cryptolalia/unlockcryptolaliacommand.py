local var_0_0 = class("UnlockCryptolaliaCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.costType
	local var_1_3 = getProxy(PlayerProxy).getRawData()
	local var_1_4 = var_1_3.GetCryptolaliaList()
	local var_1_5

	for iter_1_0, iter_1_1 in ipairs(var_1_4):
		if iter_1_1.id == var_1_1:
			var_1_5 = iter_1_1

			break

	if not var_1_5 or not var_1_5.IsLock():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	if not var_1_5.InTime():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	local var_1_6 = var_1_5.GetCost(var_1_2)

	if var_1_3.getResById(var_1_6.id) < var_1_6.count:
		if var_1_2 == Cryptolalia.COST_TYPE_TICKET:
			pg.TipsMgr.GetInstance().ShowTips(i18n("cryptolalia_no_ticket"))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	pg.ConnectionMgr.GetInstance().Send(16205, {
		id = var_1_1,
		cost_type = var_1_2
	}, 16206, function(arg_2_0)
		if arg_2_0.ret == 0:
			var_1_3.UnlockCryptolalia(var_1_1)
			var_1_3.consume({
				[id2res(var_1_6.id)] = var_1_6.count
			})
			getProxy(PlayerProxy).updatePlayer(var_1_3)
			pg.TipsMgr.GetInstance().ShowTips(i18n("cryptolalia_exchange_success"))
			arg_1_0.sendNotification(GAME.UNLOCK_CRYPTOLALIA_DONE, {
				id = var_1_1
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.ret] .. arg_2_0.ret))

return var_0_0
