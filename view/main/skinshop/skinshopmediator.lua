local var_0_0 = class("SkinShopMediator", import("...base.ContextMediator"))

var_0_0.ON_SHOPPING = "SkinShopMediator:ON_SHOPPING"
var_0_0.GO_SHOPS_LAYER = "SkinShopMediator:GO_SHOPS_LAYER"
var_0_0.OPEN_SCENE = "SkinShopMediator:OPEN_SCENE"
var_0_0.OPEN_ACTIVITY = "SkinShopMediator:OPEN_ACTIVITY"
var_0_0.ON_SHOPPING_BY_ACT = "SkinShopMediator:ON_SHOPPING_BY_ACT"
var_0_0.ON_BACKYARD_SHOP = "SkinShopMediator:ON_BACKYARD_SHOP"
var_0_0.ON_ATLAS = "SkinShopMediator:ON_ATLAS"
var_0_0.ON_INDEX = "SkinShopMediator:ON_INDEX"
var_0_0.ON_RECORD_ANIM_PREVIEW_BTN = "SkinShopMediator:ON_RECORD_ANIM_PREVIEW_BTN"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_RECORD_ANIM_PREVIEW_BTN, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.RECORD_SKIN_ANIM_PREVIEW, {
			isOpen = arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_INDEX, function(arg_3_0, arg_3_1)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = SkinIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_3_1
		}))
	end)
	arg_1_0:bind(var_0_0.ON_ATLAS, function(arg_4_0)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SKINATALAS)
	end)
	arg_1_0:bind(var_0_0.ON_BACKYARD_SHOP, function(arg_5_0)
		if not pg.SystemOpenMgr.GetInstance():isOpenSystem(getProxy(PlayerProxy):getRawData().level, "BackYardMediator") then
			local var_5_0 = pg.open_systems_limited[1]

			pg.TipsMgr.GetInstance():ShowTips(i18n("no_open_system_tip", var_5_0.name, var_5_0.level))

			return
		end

		arg_1_0:addSubLayers(Context.New({
			mediator = NewBackYardShopMediator,
			viewComponent = NewBackYardShopLayer,
			data = {
				page = 5
			}
		}))
	end)
	arg_1_0:bind(var_0_0.ON_SHOPPING_BY_ACT, function(arg_6_0, arg_6_1, arg_6_2)
		arg_1_0:sendNotification(GAME.SKIN_COUPON_SHOPPING, {
			shopId = arg_6_1,
			cnt = arg_6_2
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_ACTIVITY, function(arg_7_0, arg_7_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = arg_7_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_SHOPPING, function(arg_8_0, arg_8_1, arg_8_2)
		arg_1_0:sendNotification(GAME.SKIN_SHOPPIGN, {
			id = arg_8_1,
			count = arg_8_2
		})
	end)
	arg_1_0:bind(var_0_0.GO_SHOPS_LAYER, function(arg_9_0, arg_9_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
			warp = NewShopsScene.TYPE_ACTIVITY,
			actId = arg_9_1
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_SCENE, function(arg_10_0, arg_10_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, arg_10_1[1], arg_10_1[2])
	end)

	local var_1_0 = getProxy(ShipSkinProxy):getSkinList()

	arg_1_0.viewComponent:setSkins(var_1_0)

	local var_1_1 = getProxy(PlayerProxy)

	arg_1_0.viewComponent:setPlayer(var_1_1:getData())

	if arg_1_0.contextData.type == SkinShopScene.SHOP_TYPE_TIMELIMIT then
		getProxy(SettingsProxy):SetNextTipTimeLimitSkinShop()
	end

	arg_1_0.viewComponent:SetEncoreSkins(getProxy(ShipSkinProxy):GetEncoreSkins())
end

function var_0_0.listNotificationInterests(arg_11_0)
	return {
		GAME.SKIN_SHOPPIGN_DONE,
		PlayerProxy.UPDATED,
		GAME.SKIN_COUPON_SHOPPING_DONE,
		GAME.BUY_FURNITURE_DONE
	}
end

function var_0_0.handleNotification(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_1:getName()
	local var_12_1 = arg_12_1:getBody()
	local var_12_2 = arg_12_1:getType()

	if var_12_0 == GAME.SKIN_SHOPPIGN_DONE or var_12_0 == GAME.SKIN_COUPON_SHOPPING_DONE then
		local var_12_3 = getProxy(ShipSkinProxy):getSkinList()

		arg_12_0.viewComponent:setSkins(var_12_3)
		arg_12_0.viewComponent:onBuyDone(var_12_1.id)
		arg_12_0.viewComponent:updateShipRect()

		local var_12_4 = pg.shop_template[var_12_1.id]

		if var_12_4 and var_12_4.genre == ShopArgs.SkinShop or var_12_4.genre == ShopArgs.SkinShopTimeLimit then
			arg_12_0:addSubLayers(Context.New({
				mediator = NewSkinMediator,
				viewComponent = NewSkinLayer,
				data = {
					skinId = var_12_4.effect_args[1],
					timeLimit = var_12_4.genre == ShopArgs.SkinShopTimeLimit
				}
			}))
		end
	elseif var_12_0 == PlayerProxy.UPDATED then
		arg_12_0.viewComponent:setPlayer(var_12_1)
	elseif var_12_0 == GAME.BUY_FURNITURE_DONE then
		arg_12_0.viewComponent:OnFurnitureUpdate(var_12_2[1])
	end
end

return var_0_0
