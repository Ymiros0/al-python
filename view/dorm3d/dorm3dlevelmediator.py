local var_0_0 = class("Dorm3dLevelMediator", import("view.base.ContextMediator"))

var_0_0.CHANGE_SKIN = "Dorm3dLevelMediator.CHANGE_SKIN"
var_0_0.CHAMGE_TIME = "Dorm3dLevelMediator.CHAMGE_TIME"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.CHANGE_SKIN, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.APARTMENT_CHANGE_SKIN, {
			groupId = arg_2_1,
			skinId = arg_2_2
		})
		arg_1_0.viewComponent.closeView())
	arg_1_0.bind(var_0_0.CHAMGE_TIME, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(Dorm3dSceneMediator.CHAMGE_TIME_RELOAD_SCENE, {
			timeIndex = arg_3_1
		})
		arg_1_0.viewComponent.closeView())
	arg_1_0.viewComponent.SetApartment(getProxy(ApartmentProxy).getApartment(arg_1_0.contextData.groupId))

def var_0_0.initNotificationHandleDic(arg_4_0):
	arg_4_0.handleDic = {}

def var_0_0.remove(arg_5_0):
	return

return var_0_0
