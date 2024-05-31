local var_0_0 = class("VedioStoryPlayer", import(".StoryPlayer"))

def var_0_0.OnReset(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_3()

local function var_0_1(arg_2_0)
	return PathMgr.getAssetBundle("originsource/cpk/" .. arg_2_0 .. ".cpk")

def var_0_0.RegisterTrigger(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = arg_3_2.GetVedioPath()

	arg_3_0.CheckAndPlay(arg_3_2, var_3_0, arg_3_3)

def var_0_0.CheckAndPlay(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	if not PathMgr.FileExists(var_0_1(arg_4_2)):
		arg_4_3()

		return

	arg_4_0.PlayVedio(arg_4_1, arg_4_2, arg_4_3)

def var_0_0.PlayVedio(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	ResourceMgr.Inst.getAssetAsync("Story/" .. arg_5_2, arg_5_2, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_6_0)
		if arg_5_0.stop:
			return

		local var_6_0 = Object.Instantiate(arg_6_0, arg_5_0.frontTr)
		local var_6_1 = var_6_0.transform.Find("cpk").GetComponent(typeof(CriManaCpkUI))
		local var_6_2 = var_6_0.transform.Find("skip_button")

		onButton(arg_5_0, var_6_2, function()
			arg_5_0.ClearVedio()
			arg_5_3(), SFX_PANEL)
		var_6_1.SetPlayEndHandler(System.Action(function()
			triggerButton(var_6_2)))
		setActive(var_6_2, arg_5_1.GetSkipFlag())

		arg_5_0._vedioGo = var_6_0), True, True)

def var_0_0.ClearVedio(arg_9_0):
	if arg_9_0._vedioGo:
		Object.Destroy(arg_9_0._vedioGo)

		arg_9_0._vedioGo = None

def var_0_0.OnClear(arg_10_0):
	arg_10_0.ClearVedio()

def var_0_0.OnEnd(arg_11_0):
	arg_11_0.ClearVedio()

return var_0_0
