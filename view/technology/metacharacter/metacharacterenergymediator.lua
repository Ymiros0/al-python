local var_0_0 = class("MetaCharacterEnergyMediator", import("...base.ContextMediator"))

var_0_0.ON_ACTIVATION = "MetaCharacterEnergyMediator:ON_ACTIVATION"
var_0_0.ON_PREVIEW = "MetaCharacterEnergyMediator:ON_PREVIEW"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_ACTIVATION, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.ENERGY_META_ACTIVATION, {
			shipId = arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_PREVIEW, function(arg_3_0, arg_3_1, arg_3_2)
		local var_3_0 = {
			equipSkinId = 0,
			shipVO = arg_3_1,
			weaponIds = arg_3_2
		}

		arg_1_0:addSubLayers(Context.New({
			viewComponent = ShipPreviewLayer,
			mediator = ShipPreviewMediator,
			data = var_3_0
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_4_0)
	return {
		GAME.ENERGY_META_ACTIVATION_DONE,
		BayProxy.SHIP_UPDATED,
		BagProxy.ITEM_UPDATED
	}
end

function var_0_0.handleNotification(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1:getName()
	local var_5_1 = arg_5_1:getBody()

	if var_5_0 == GAME.ENERGY_META_ACTIVATION_DONE then
		arg_5_0:addSubLayers(Context.New({
			viewComponent = ShipBreakResultLayer,
			mediator = ShipBreakResultMediator,
			data = {
				newShip = var_5_1.newShip,
				oldShip = var_5_1.oldShip
			}
		}))
		arg_5_0.viewComponent:updateData()
		arg_5_0.viewComponent:updateNamePanel()
		arg_5_0.viewComponent:updateAttrPanel()
		arg_5_0.viewComponent:updateMaterialPanel()
		arg_5_0.viewComponent:initPreviewPanel()
	end
end

return var_0_0
