local var_0_0 = class("MainLanternFestivalBtn", import(".MainBaseActivityBtn"))

var_0_0.LANTERNFESTIVAL_MINIGAME_ID = 64

def var_0_0.GetEventName(arg_1_0):
	return "event_LanternFestival"

def var_0_0.GetActivityID(arg_2_0):
	local var_2_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.LANTERNFESTIVAL)

	return var_2_0 and var_2_0.id

def var_0_0.OnInit(arg_3_0):
	local var_3_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.LANTERNFESTIVAL)
	local var_3_1 = False

	if var_3_0 and not var_3_0.isEnd():
		local var_3_2 = getProxy(MiniGameProxy).GetHubByHubId(var_3_0.getConfig("config_id"))

		var_3_1 = var_3_2.count > 0 and var_3_2.usedtime < 7

	setActive(arg_3_0._tf.Find("Tip"), var_3_1)

def var_0_0.CustomOnClick(arg_4_0):
	if getProxy(ActivityProxy).getActivityById(ActivityConst.LANTERNFESTIVAL):
		pg.m02.sendNotification(GAME.GO_MINI_GAME, var_0_0.LANTERNFESTIVAL_MINIGAME_ID)

return var_0_0
