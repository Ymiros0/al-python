local var_0_0 = class("MainActBackHillBtn", import(".MainBaseActivityBtn"))

def var_0_0.GetEventName(arg_1_0):
	return "event_minigame"

def var_0_0.OnInit(arg_2_0):
	local var_2_0 = arg_2_0.IsShowTip()

	setActive(arg_2_0.tipTr.gameObject, var_2_0)

def var_0_0.GetActivityID(arg_3_0):
	local var_3_0 = checkExist(arg_3_0.config, {
		"time"
	})

	if not var_3_0:
		return None

	return var_3_0[1] == "default" and var_3_0[2] or None

def var_0_0.CustomOnClick(arg_4_0):
	local var_4_0 = arg_4_0.GetActivityID()
	local var_4_1 = getProxy(ActivityProxy).getActivityById(var_4_0)

	if var_4_1:
		local var_4_2 = var_4_1.getConfig("config_client").scene

		if var_4_2:
			arg_4_0.emit(NewMainMediator.GO_SCENE, var_4_2)

			return

	errorMsg("not bind backhill Activity id.", var_4_0 or "NIL")
	arg_4_0.OnClick()

def var_0_0.IsShowTip(arg_5_0):
	local var_5_0 = arg_5_0.GetActivityID()
	local var_5_1 = getProxy(ActivityProxy).getActivityById(var_5_0)

	if var_5_1:
		local var_5_2 = var_5_1.getConfig("config_client").scene

		if var_5_2:
			local var_5_3 = Context.New()

			if IsUnityEditor:
				assert(table.Find(SCENE, function(arg_6_0, arg_6_1)
					return arg_6_1 == var_5_2), "not Find name in scene.lua . " .. var_5_2)

			SCENE.SetSceneInfo(var_5_3, var_5_2)

			local var_5_4 = var_5_3.viewComponent.IsShowMainTip

			if var_5_4:
				return var_5_4(var_5_1)

			errorMsg("scene has not function IsShowMainTip Tip Activity id.", var_5_0 or "NIL")

return var_0_0
