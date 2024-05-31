local var_0_0 = class("MainActFeastBtn", import(".MainBaseActivityBtn"))

def var_0_0.InShowTime(arg_1_0):
	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST)

	arg_1_0.config = {
		param = "0",
		name = "event_minigame",
		type = 0,
		text_pic = "text_event_minigame",
		id = 20,
		group_id = 5,
		pic = "event_minigame",
		order = 1,
		time = {
			"default"
		}
	}

	return var_1_0 and not var_1_0.isEnd()

def var_0_0.CustomOnClick(arg_2_0):
	arg_2_0.emit(NewMainMediator.GO_SCENE, SCENE.FEAST)

return var_0_0
