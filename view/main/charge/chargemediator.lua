local var_0_0 = class("ChargeMediator", import("...base.ContextMediator"))

var_0_0.SWITCH_TO_SHOP = "ChargeMediator:SWITCH_TO_SHOP"
var_0_0.CHARGE = "ChargeMediator:CHARGE"
var_0_0.BUY_ITEM = "ChargeMediator:BUY_ITEM"
var_0_0.CLICK_MING_SHI = "ChargeMediator:CLICK_MING_SHI"
var_0_0.GET_CHARGE_LIST = "ChargeMediator:GET_CHARGE_LIST"
var_0_0.ON_SKIN_SHOP = "ChargeMediator:ON_SKIN_SHOP"
var_0_0.OPEN_CHARGE_ITEM_PANEL = "ChargeMediator:OPEN_CHARGE_ITEM_PANEL"
var_0_0.OPEN_CHARGE_ITEM_BOX = "ChargeMediator:OPEN_CHARGE_ITEM_BOX"
var_0_0.OPEN_CHARGE_BIRTHDAY = "ChargeMediator:OPEN_CHARGE_BIRTHDAY"
var_0_0.OPEN_USER_AGREE = "ChargeMediator:OPEN_USER_AGREE"
var_0_0.VIEW_SKIN_PROBABILITY = "ChargeMediator:VIEW_SKIN_PROBABILITY"
var_0_0.OPEN_TEC_SHIP_GIFT_SELL_LAYER = "ChargeMediator:OPEN_TEC_SHIP_GIFT_SELL_LAYER"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(PlayerProxy):getData()

	arg_1_0.viewComponent:setPlayer(var_1_0)
	arg_1_0.viewComponent:checkFreeGiftTag()
	arg_1_0:bind(var_0_0.VIEW_SKIN_PROBABILITY, function(arg_2_0, arg_2_1)
		arg_1_0.contextData.wrap = ChargeScene.TYPE_GIFT

		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.PROBABILITY_SKINSHOP, {
			commodityId = arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.GET_CHARGE_LIST, function(arg_3_0)
		arg_1_0:sendNotification(GAME.GET_CHARGE_LIST)
	end)
	arg_1_0:bind(var_0_0.ON_SKIN_SHOP, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SKINSHOP)
	end)
	arg_1_0:bind(var_0_0.SWITCH_TO_SHOP, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHOP, arg_5_1)
	end)
	arg_1_0:bind(var_0_0.CHARGE, function(arg_6_0, arg_6_1)
		arg_1_0:sendNotification(GAME.CHARGE_OPERATION, {
			shopId = arg_6_1
		})
	end)
	arg_1_0:bind(var_0_0.BUY_ITEM, function(arg_7_0, arg_7_1, arg_7_2)
		arg_1_0:sendNotification(GAME.SHOPPING, {
			id = arg_7_1,
			count = arg_7_2
		})
	end)
	arg_1_0:bind(var_0_0.CLICK_MING_SHI, function(arg_8_0)
		arg_1_0:sendNotification(GAME.CLICK_MING_SHI)
	end)
	arg_1_0:bind(var_0_0.OPEN_CHARGE_ITEM_PANEL, function(arg_9_0, arg_9_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = ChargeItemPanelMediator,
			viewComponent = ChargeItemPanelLayer,
			data = {
				panelConfig = arg_9_1
			}
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_CHARGE_ITEM_BOX, function(arg_10_0, arg_10_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = ChargeItemBoxMediator,
			viewComponent = ChargeItemBoxLayer,
			data = {
				panelConfig = arg_10_1
			}
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_CHARGE_BIRTHDAY, function(arg_11_0, arg_11_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = ChargeBirthdayMediator,
			viewComponent = ChargeBirthdayLayer,
			data = {}
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_USER_AGREE, function(arg_12_0, arg_12_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = ChargeJPUserAgreeMediator,
			viewComponent = ChargeJPUserAgreeLayer,
			data = {
				contentStr = arg_12_1
			}
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_TEC_SHIP_GIFT_SELL_LAYER, function(arg_13_0, arg_13_1, arg_13_2)
		arg_1_0:addSubLayers(Context.New({
			mediator = ChargeTecShipGiftSellMediator,
			viewComponent = ChargeTecShipGiftSellLayer,
			data = {
				showGoodVO = arg_13_1,
				chargedList = arg_13_2
			}
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_14_0)
	return {
		PlayerProxy.UPDATED,
		ShopsProxy.FIRST_CHARGE_IDS_UPDATED,
		ShopsProxy.CHARGED_LIST_UPDATED,
		GAME.CHARGE_CONFIRM_FAILED,
		GAME.GET_CHARGE_LIST_DONE,
		GAME.SHOPPING_DONE,
		GAME.USE_ITEM_DONE,
		GAME.CLICK_MING_SHI_SUCCESS,
		GAME.REMOVE_LAYERS,
		PlayerResUI.GO_MALL,
		GAME.CHARGE_SUCCESS
	}
end

function var_0_0.handleNotification(arg_15_0, arg_15_1)
	local var_15_0 = arg_15_1:getName()
	local var_15_1 = arg_15_1:getBody()

	if var_15_0 == PlayerProxy.UPDATED then
		arg_15_0.viewComponent:setPlayer(var_15_1)
		arg_15_0.viewComponent:updateNoRes()
	elseif var_15_0 == ShopsProxy.FIRST_CHARGE_IDS_UPDATED then
		arg_15_0.viewComponent:setFirstChargeIds(var_15_1)
		arg_15_0.viewComponent:updateCurSubView()
	elseif var_15_0 == ShopsProxy.CHARGED_LIST_UPDATED then
		arg_15_0.viewComponent:setChargedList(var_15_1)
		arg_15_0.viewComponent:updateCurSubView()
	elseif var_15_0 == GAME.CHARGE_CONFIRM_FAILED then
		getProxy(ShopsProxy):chargeFailed(var_15_1.payId, var_15_1.bsId)
	elseif var_15_0 == GAME.SHOPPING_DONE then
		if var_15_1.awards and #var_15_1.awards > 0 then
			arg_15_0.viewComponent:unBlurView()
			arg_15_0.viewComponent:emit(BaseUI.ON_AWARD, {
				items = var_15_1.awards
			})
		end

		local var_15_2 = var_15_1.normalList
		local var_15_3 = var_15_1.normalGroupList

		if var_15_2 then
			arg_15_0.viewComponent:setNormalList(var_15_2)
		end

		if var_15_3 then
			arg_15_0.viewComponent:setNormalGroupList(var_15_3)
		end

		local var_15_4 = pg.shop_template[var_15_1.id]

		arg_15_0.viewComponent:checkBuyDone(var_15_1.id)
		arg_15_0.viewComponent:updateCurSubView()
		arg_15_0.viewComponent:checkFreeGiftTag()
	elseif var_15_0 == GAME.USE_ITEM_DONE then
		if table.getCount(var_15_1) ~= 0 then
			arg_15_0.viewComponent:emit(BaseUI.ON_AWARD, {
				items = var_15_1
			})
		end
	elseif var_15_0 == GAME.GET_CHARGE_LIST_DONE then
		local var_15_5 = var_15_1.firstChargeIds
		local var_15_6 = var_15_1.chargedList
		local var_15_7 = var_15_1.normalList
		local var_15_8 = var_15_1.normalGroupList

		if var_15_5 then
			arg_15_0.viewComponent:setFirstChargeIds(var_15_5)
		end

		if var_15_6 then
			arg_15_0.viewComponent:setChargedList(var_15_6)
		end

		if var_15_7 then
			arg_15_0.viewComponent:setNormalList(var_15_7)
		end

		if var_15_8 then
			arg_15_0.viewComponent:setNormalGroupList(var_15_8)
		end

		if var_15_5 or var_15_6 or var_15_7 or var_15_8 then
			arg_15_0.viewComponent:updateCurSubView()
		end

		arg_15_0.viewComponent:checkFreeGiftTag()
	elseif var_15_0 == GAME.CLICK_MING_SHI_SUCCESS then
		arg_15_0.viewComponent:playHeartEffect()
	elseif var_15_0 == PlayerResUI.GO_MALL then
		local var_15_9 = ChargeScene.TYPE_DIAMOND

		if var_15_1 then
			var_15_9 = var_15_1.type or ChargeScene.TYPE_DIAMOND
		end

		arg_15_0.viewComponent:switchSubViewByTogger(var_15_9)
		arg_15_0.viewComponent:updateNoRes(var_15_1 and var_15_1.noRes or nil)
	elseif var_15_0 == GAME.CHARGE_SUCCESS then
		arg_15_0.viewComponent:checkBuyDone("damonds")

		local var_15_10 = Goods.Create({
			shop_id = var_15_1.shopId
		}, Goods.TYPE_CHARGE)

		arg_15_0.viewComponent:OnChargeSuccess(var_15_10)
	end
end

return var_0_0
