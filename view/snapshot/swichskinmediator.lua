﻿local var_0_0 = class("SwichSkinMediator", import("..base.ContextMediator"))

var_0_0.CHANGE_SKIN = "SwichSkinMediator:CHANGE_SKIN"
var_0_0.BUY_ITEM = "SwichSkinMediator:BUY_ITEM"
var_0_0.UPDATE_SKINCONFIG = "SwichSkinMediator:UPDATE_SKINCONFIG"
var_0_0.BUY_ITEM_BY_ACT = "SwichSkinMediator:BUY_ITEM_BY_ACT"

function var_0_0.register(arg_1_0)
	arg_1_0.shipVO = arg_1_0.contextData.shipVO

	if arg_1_0.shipVO then
		arg_1_0.viewComponent:setShip(arg_1_0.shipVO)

		local var_1_0 = getProxy(ShipSkinProxy):getSkinList()

		arg_1_0.viewComponent:setSkinList(var_1_0)
	end

	arg_1_0:bind(var_0_0.BUY_ITEM_BY_ACT, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.SKIN_COUPON_SHOPPING, {
			shopId = arg_2_1,
			cnt = arg_2_2
		})
	end)
	arg_1_0:bind(var_0_0.CHANGE_SKIN, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(GAME.SET_SHIP_SKIN, {
			shipId = arg_3_1,
			skinId = arg_3_2
		})
	end)
	arg_1_0:bind(var_0_0.BUY_ITEM, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0:sendNotification(GAME.SKIN_SHOPPIGN, {
			id = arg_4_1,
			count = arg_4_2
		})
	end)
	arg_1_0:bind(var_0_0.UPDATE_SKINCONFIG, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.UPDATE_SKINCONFIG, {
			skinId = arg_5_1
		})
	end)
end

function var_0_0.listNotificationInterests(arg_6_0)
	return {
		ShipSkinProxy.SHIP_SKINS_UPDATE,
		GAME.SKIN_SHOPPIGN_DONE,
		GAME.SKIN_COUPON_SHOPPING_DONE,
		BayProxy.SHIP_UPDATED
	}
end

function var_0_0.handleNotification(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_1:getName()
	local var_7_1 = arg_7_1:getBody()

	if var_7_0 == GAME.SKIN_SHOPPIGN_DONE or var_7_0 == GAME.SKIN_COUPON_SHOPPING_DONE then
		local var_7_2 = pg.shop_template[var_7_1.id]

		if var_7_2 and var_7_2.genre == ShopArgs.SkinShop then
			arg_7_0:addSubLayers(Context.New({
				mediator = NewSkinMediator,
				viewComponent = NewSkinLayer,
				data = {
					skinId = var_7_2.effect_args[1]
				}
			}))
		end
	elseif var_7_0 == ShipSkinProxy.SHIP_SKINS_UPDATE then
		local var_7_3 = getProxy(ShipSkinProxy):getSkinList()

		arg_7_0.viewComponent:setSkinList(var_7_3)
		arg_7_0.viewComponent:openSelectSkinPanel()
	elseif var_7_0 == BayProxy.SHIP_UPDATED and var_7_1.id == arg_7_0.shipVO.id then
		arg_7_0.viewComponent:setShip(var_7_1)

		local var_7_4 = getProxy(ShipSkinProxy):getSkinList()

		arg_7_0.viewComponent:setSkinList(var_7_4)
		arg_7_0.viewComponent:openSelectSkinPanel()
	end
end

return var_0_0
