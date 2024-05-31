local var_0_0 = class("SelectDorm3DMediator", import("view.base.ContextMediator"))

var_0_0.ON_DORM = "SelectDorm3DMediator.ON_DORM"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_DORM, function(arg_2_0, arg_2_1)
		pg.SceneAnimMgr.GetInstance().Dorm3DSceneChange(function(arg_3_0)
			arg_1_0.sendNotification(GAME.CHANGE_SCENE, SCENE.DORM3D, {
				showLoading = False,
				groupId = arg_2_1,
				resumeCallback = arg_3_0
			})))

def var_0_0.listNotificationInterests(arg_4_0):
	return {}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == None:
		-- block empty

return var_0_0
