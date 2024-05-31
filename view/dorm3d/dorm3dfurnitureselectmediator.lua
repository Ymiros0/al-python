local var_0_0 = class("Dorm3dFurnitureSelectMediator", import("view.base.ContextMediator"))

var_0_0.SHOW_CONFIRM_WINDOW = "SHOW_CONFIRM_WINDOW"
var_0_0.SHOW_FURNITURE_ACESSES = "SHOW_FURNITURE_ACESSES"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(GAME.APARTMENT_REPLACE_FURNITURE, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.APARTMENT_REPLACE_FURNITURE, arg_2_1)
	end)
	arg_1_0:bind(var_0_0.SHOW_CONFIRM_WINDOW, function(arg_3_0, arg_3_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = Dorm3dFurnitureConfirmWindowMediator,
			viewComponent = Dorm3dFurnitureConfirmWindow,
			data = arg_3_1
		}))
	end)
	arg_1_0:bind(var_0_0.SHOW_FURNITURE_ACESSES, function(arg_4_0, arg_4_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = Dorm3dFurnitureAcessesWindowMediator,
			viewComponent = Dorm3dFurnitureAcessesWindow,
			data = arg_4_1
		}))
	end)

	local var_1_0 = pg.m02:retrieveMediator(Dorm3dSceneMediator.__cname):getViewComponent()

	arg_1_0.viewComponent:SetSceneRoot(var_1_0)

	local var_1_1 = var_1_0:GetApartment()

	arg_1_0.viewComponent:SetApartment(var_1_1)
end

function var_0_0.listNotificationInterests(arg_5_0)
	return {
		Dorm3dSceneMediator.ON_CLICK_FURNITURE_SLOT,
		GAME.APARTMENT_REPLACE_FURNITURE_DONE,
		GAME.APARTMENT_REPLACE_FURNITURE_ERROR
	}
end

function var_0_0.handleNotification(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1:getName()
	local var_6_1 = arg_6_1:getBody()

	if var_6_0 == ApartmentProxy.UPDATE_APARTMENT then
		-- block empty
	elseif var_6_0 == Dorm3dSceneMediator.ON_CLICK_FURNITURE_SLOT then
		arg_6_0.viewComponent:OnClickFurnitureSlot(var_6_1)
	elseif var_6_0 == GAME.APARTMENT_REPLACE_FURNITURE_DONE then
		arg_6_0.viewComponent:OnReplaceFurnitureDone()
	elseif var_6_0 == GAME.APARTMENT_REPLACE_FURNITURE_ERROR then
		arg_6_0.viewComponent:OnReplaceFurnitureError()
	end
end

function var_0_0.remove(arg_7_0)
	return
end

return var_0_0
