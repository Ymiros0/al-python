﻿local var_0_0 = class("Dorm3dCollectionMediator", import("view.base.ContextMediator"))

var_0_0.DO_TALK = "Dorm3dCollectionMediator.DO_TALK"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.DO_TALK, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(Dorm3dSceneMediator.OTHER_DO_TALK, {
			talkId = arg_2_1,
			callback = arg_2_2
		})
		arg_1_0.viewComponent:closeView()
	end)
	arg_1_0.viewComponent:SetApartment(getProxy(ApartmentProxy):getApartment(arg_1_0.contextData.groupId))
end

function var_0_0.initNotificationHandleDic(arg_3_0)
	arg_3_0.handleDic = {}
end

function var_0_0.remove(arg_4_0)
	return
end

return var_0_0
