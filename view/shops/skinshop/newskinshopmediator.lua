local var_0_0 = class("NewSkinShopMediator", import("view.base.ContextMediator"))

var_0_0.ON_ATLAS = "NewSkinShopMediator:ON_ATLAS"
var_0_0.ON_INDEX = "NewSkinShopMediator:ON_INDEX"
var_0_0.ON_BACKYARD_SHOP = "NewSkinShopMediator:ON_BACKYARD_SHOP"
var_0_0.GO_SHOPS_LAYER = "NewSkinShopMediator:GO_SHOPS_LAYER"
var_0_0.OPEN_SCENE = "NewSkinShopMediator:OPEN_SCENE"
var_0_0.OPEN_ACTIVITY = "NewSkinShopMediator:OPEN_ACTIVITY"
var_0_0.ON_SHOPPING_BY_ACT = "NewSkinShopMediator:ON_SHOPPING_BY_ACT"
var_0_0.ON_SHOPPING = "NewSkinShopMediator:ON_SHOPPING"
var_0_0.ON_RECORD_ANIM_PREVIEW_BTN = "NewSkinShopMediator:ON_RECORD_ANIM_PREVIEW_BTN"
var_0_0.ON_ITEM_PURCHASE = "NewSkinShopMediator:ON_ITEM_PURCHASE"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_ITEM_PURCHASE, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.USE_ITEM, {
			count = 1,
			id = arg_2_1,
			arg = {
				arg_2_2
			}
		})
	end)
	arg_1_0:bind(var_0_0.ON_RECORD_ANIM_PREVIEW_BTN, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(GAME.RECORD_SKIN_ANIM_PREVIEW, {
			isOpen = arg_3_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_SHOPPING, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0:sendNotification(GAME.SKIN_SHOPPIGN, {
			id = arg_4_1,
			count = arg_4_2
		})
	end)
	arg_1_0:bind(var_0_0.ON_SHOPPING_BY_ACT, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0:sendNotification(GAME.SKIN_COUPON_SHOPPING, {
			shopId = arg_5_1,
			cnt = arg_5_2
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_ACTIVITY, function(arg_6_0, arg_6_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = arg_6_1
		})
	end)
	arg_1_0:bind(var_0_0.GO_SHOPS_LAYER, function(arg_7_0, arg_7_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
			warp = NewShopsScene.TYPE_ACTIVITY,
			actId = arg_7_1
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_SCENE, function(arg_8_0, arg_8_1)
		arg_1_0:sendNotification(GAME.GO_SCENE, arg_8_1[1], arg_8_1[2])
	end)
	arg_1_0:bind(var_0_0.ON_BACKYARD_SHOP, function(arg_9_0)
		arg_1_0:addSubLayers(Context.New({
			mediator = NewBackYardShopMediator,
			viewComponent = NewBackYardShopLayer,
			data = {
				topLayer = true,
				page = 5
			}
		}))
	end)
	arg_1_0:bind(var_0_0.ON_ATLAS, function(arg_10_0)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SKINATALAS)
	end)
	arg_1_0:bind(var_0_0.ON_INDEX, function(arg_11_0, arg_11_1)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = SkinIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_11_1
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_12_0)
	return {
		GAME.SKIN_SHOPPIGN_DONE,
		GAME.SKIN_COUPON_SHOPPING_DONE,
		GAME.BUY_FURNITURE_DONE,
		GAME.LOAD_LAYERS,
		GAME.REMOVE_LAYERS
	}
end

function var_0_0.handleNotification(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1:getName()
	local var_13_1 = arg_13_1:getBody()
	local var_13_2 = arg_13_1:getType()

	if var_13_0 == GAME.SKIN_SHOPPIGN_DONE or var_13_0 == GAME.SKIN_COUPON_SHOPPING_DONE then
		local var_13_3 = pg.shop_template[var_13_1.id]

		if var_13_3 and (var_13_3.genre == ShopArgs.SkinShop or var_13_3.genre == ShopArgs.SkinShopTimeLimit) then
			arg_13_0:addSubLayers(Context.New({
				mediator = NewSkinMediator,
				viewComponent = NewSkinLayer,
				data = {
					skinId = var_13_3.effect_args[1],
					timeLimit = var_13_3.genre == ShopArgs.SkinShopTimeLimit
				}
			}))
			arg_13_0.viewComponent:OnShopping(var_13_1.id)
		end
	elseif var_13_0 == GAME.BUY_FURNITURE_DONE then
		arg_13_0.viewComponent:OnFurnitureUpdate(var_13_2[1])
	elseif var_13_0 == GAME.LOAD_LAYERS then
		if var_13_1.context.mediator == NewBackYardShopMediator then
			arg_13_0:sendNotification(PlayerResUI.HIDE)
		end
	elseif var_13_0 == GAME.REMOVE_LAYERS and var_13_1.context.mediator == NewBackYardShopMediator then
		arg_13_0:sendNotification(PlayerResUI.SHOW)
	end
end

return var_0_0
