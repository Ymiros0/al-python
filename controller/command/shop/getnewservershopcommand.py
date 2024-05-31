local var_0_0 = class("GetNewServerShopCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().callback
	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_SHOP)

	if not var_1_1 or var_1_1.isEnd():
		var_1_0()

		return

	pg.ConnectionMgr.GetInstance().Send(26041, {
		act_id = var_1_1.id
	}, 26042, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = NewServerShop.New({
				start_time = arg_2_0.start_time,
				stop_time = arg_2_0.stop_time,
				goods = arg_2_0.goods,
				id = var_1_1.id
			})

			getProxy(ShopsProxy).SetNewServerShop(var_2_0)
			var_1_0(var_2_0)
			arg_1_0.sendNotification(GAME.GET_NEW_SERVER_SHOP_DONE)
		else
			var_1_0()
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
