local var_0_0 = class("GetRefundInfoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	pg.ConnectionMgr.GetInstance().Send(11023, {
		type = 1
	}, 11024, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(PlayerProxy).setRefundInfo(arg_2_0.shop_info)
			pg.m02.sendNotification(GAME.REFUND_INFO_UPDATE)

			if arg_1_1 and arg_1_1.getBody() and arg_1_1.getBody().callback:
				arg_1_1.getBody().callback())

return var_0_0
