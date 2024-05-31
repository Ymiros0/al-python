local var_0_0 = class("MedalShopCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.goodsId
	local var_1_2 = var_1_0.selectedId
	local var_1_3 = #var_1_2
	local var_1_4 = getProxy(BagProxy)
	local var_1_5 = var_1_4.getItemCountById(ITEM_ID_SILVER_HOOK)
	local var_1_6 = getProxy(ShopsProxy)
	local var_1_7 = var_1_6.GetMedalShop()
	local var_1_8 = var_1_7.getGoodsById(var_1_1)
	local var_1_9 = var_1_8.GetPrice()

	if var_1_5 < var_1_9 * var_1_3:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	if not var_1_8.CanPurchaseCnt(var_1_3):
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_shop_cnt_no_enough"))

		return

	local var_1_10 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_2):
		if not var_1_10[iter_1_1]:
			var_1_10[iter_1_1] = {
				count = 1,
				id = iter_1_1
			}
		else
			var_1_10[iter_1_1].count = var_1_10[iter_1_1].count + 1

	pg.ConnectionMgr.GetInstance().Send(16108, {
		flash_time = var_1_7.nextTime,
		shopid = var_1_8.configId,
		selected = _.values(var_1_10)
	}, 16109, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)
			local var_2_1 = var_1_6.GetMedalShop()

			var_2_1.UpdateGoodsCnt(var_1_1, var_1_3)
			var_1_6.UpdateMedalShop(var_2_1)
			var_1_4.removeItemById(ITEM_ID_SILVER_HOOK, var_1_9 * var_1_3)
			arg_1_0.sendNotification(GAME.ON_MEDAL_SHOP_PURCHASE_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
