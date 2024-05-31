local var_0_0 = class("EducateRequestShopDataCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0 and var_1_0.callback

	pg.ConnectionMgr.GetInstance().Send(27043, {
		shop_id = var_1_0.shopId,
		goods = var_1_0.goods
	}, 27044, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = EducateShop.New(arg_2_0.shop_data.shop_id, arg_2_0.shop_data.goods)

			getProxy(EducateProxy).GetShopProxy().UpdateShop(var_2_0)
			arg_1_0.sendNotification(GAME.EDUCATE_REQUEST_SHOP_DATA_DONE)

			if var_1_1:
				var_1_1()
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("educate request shop data error. ", arg_2_0.result)))

return var_0_0
