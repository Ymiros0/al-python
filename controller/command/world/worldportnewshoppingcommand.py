local var_0_0 = class("WorldPortNewShoppingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.goods
	local var_1_2 = var_1_0.count

	if not var_1_1.canPurchase():
		pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit"))

		return

	local var_1_3 = var_1_1.GetPriceInfo()

	var_1_3.count = var_1_3.count * var_1_2

	if var_1_3.getOwnedCount() < var_1_3.count:
		pg.TipsMgr.GetInstance().ShowTips(i18n("buyProp_noResource_error", var_1_3.getName()))

		return

	pg.ConnectionMgr.GetInstance().Send(33403, {
		shop_type = 2,
		shop_id = var_1_1.id,
		count = var_1_2
	}, 33404, function(arg_2_0)
		if arg_2_0.result == 0:
			reducePlayerOwn(var_1_3)
			nowWorld().GetAtlas().UpdateNShopGoodsCount(var_1_1.id, var_1_2)

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)

			arg_1_0.sendNotification(GAME.WORLD_PORT_NEW_SHOPPING_DONE, {
				drops = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("world_port_shopping_error_", arg_2_0.result)))

return var_0_0
