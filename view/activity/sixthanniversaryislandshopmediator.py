local var_0_0 = class("SixthAnniversaryIslandShopMediator", import("..base.ContextMediator"))

var_0_0.OPEN_GOODS_WINDOW = "SixthAnniversaryIslandShopMediator.OPEN_GOODS_WINDOW"

def var_0_0.register(arg_1_0):
	arg_1_0.viewComponent.setShop(arg_1_0.contextData.shop)
	arg_1_0.viewComponent.setPlayer(getProxy(PlayerProxy).getData())
	arg_1_0.bind(var_0_0.OPEN_GOODS_WINDOW, function(arg_2_0, arg_2_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = SixthAnniversaryIslandShopWindowMediator,
			viewComponent = SixthAnniversaryIslandShopWindowLayer,
			data = {
				activityId = arg_1_0.contextData.shop.activityId,
				shop = arg_1_0.contextData.shop,
				goods = arg_2_1
			}
		})))

def var_0_0.initNotificationHandleDic(arg_3_0):
	arg_3_0.handleDic = {
		[GAME.ISLAND_SHOPPING_DONE] = function(arg_4_0, arg_4_1)
			local var_4_0 = arg_4_1.getBody()
			local var_4_1 = {}

			if #var_4_0.awards > 0:
				table.insert(var_4_1, function(arg_5_0)
					arg_4_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_4_0.awards, arg_5_0))

			seriesAsync(var_4_1, function()
				arg_4_0.viewComponent.refreshGoodsCard(var_4_0.goodsId)),
		[GAME.USE_ITEM_DONE] = function(arg_7_0, arg_7_1)
			local var_7_0 = arg_7_1.getBody()

			if #var_7_0 > 0:
				arg_7_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_7_0),
		[PlayerProxy.UPDATED] = function(arg_8_0, arg_8_1)
			local var_8_0 = arg_8_1.getBody()

			arg_8_0.viewComponent.setPlayer(var_8_0)
	}

return var_0_0
