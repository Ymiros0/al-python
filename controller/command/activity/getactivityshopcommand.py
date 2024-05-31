local var_0_0 = class("GetActivityShopCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0 and var_1_0.callback
	local var_1_2 = ActivityConst.ACTIVITY_TYPE_SHOP
	local var_1_3 = getProxy(ActivityProxy).getActivitiesByType(var_1_2)
	local var_1_4 = getProxy(ShopsProxy)
	local var_1_5 = {}

	_.each(var_1_3, function(arg_2_0)
		if arg_2_0 and not arg_2_0.isEnd() and arg_2_0.getConfig("config_id") == 0:
			local var_2_0 = ActivityShop.New(arg_2_0)

			var_1_5[arg_2_0.id] = var_2_0

			var_1_4.addActivityShops(var_1_5))
	arg_1_0.sendNotification(GAME.GET_ACTIVITY_SHOP_DONE)

	if var_1_1:
		var_1_1(var_1_5)

return var_0_0
