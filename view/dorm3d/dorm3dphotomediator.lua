local var_0_0 = class("Dorm3dPhotoMediator", import("view.base.ContextMediator"))

function var_0_0.register(arg_1_0)
	local var_1_0 = pg.m02:retrieveMediator(Dorm3dSceneMediator.__cname):getViewComponent()

	arg_1_0.viewComponent:SetSceneRoot(var_1_0)

	local var_1_1 = var_1_0:GetApartment()

	arg_1_0.viewComponent:SetApartment(var_1_1)
	arg_1_0:bind(SnapshotScene.SHARE_PANEL, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:addSubLayers(Context.New({
			mediator = SnapshotShareMediator,
			viewComponent = SnapshotShareLayer,
			data = {
				photoTex = arg_2_1,
				photoData = arg_2_2
			}
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		ApartmentProxy.UPDATE_APARTMENT
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == ApartmentProxy.UPDATE_APARTMENT then
		-- block empty
	end
end

function var_0_0.remove(arg_5_0)
	return
end

return var_0_0
