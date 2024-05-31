local var_0_0 = class("DexiV3framePage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	setActive(arg_1_0.displayBtn, False)
	setActive(arg_1_0.awardTF, False)
	onButton(arg_1_0, arg_1_0.battleBtn, function()
		arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK, {
			page = "activity"
		}), SFX_PANEL)

	arg_1_0.step = arg_1_0.findTF("AD/switcher/phase2/Image/step")
	arg_1_0.progress = arg_1_0.findTF("AD/switcher/phase2/Image/progress")
	arg_1_0.switchBtn = arg_1_0.findTF("AD/switch_btn")
	arg_1_0.bar = arg_1_0.findTF("AD/switcher/phase2/Image/barContent/bar")
	arg_1_0.phases = {
		arg_1_0.findTF("AD/switcher/phase1"),
		arg_1_0.findTF("AD/switcher/phase2")
	}
	arg_1_0.inPhase2 = False

	onToggle(arg_1_0, arg_1_0.switchBtn, function(arg_3_0)
		if arg_1_0.isSwitching:
			return

		arg_1_0.inPhase2 = arg_3_0

		arg_1_0.Switch(arg_3_0), SFX_PANEL)

	local var_1_0 = arg_1_0.activity.getConfig("config_client")

	if pg.TimeMgr.GetInstance().inTime(var_1_0):
		triggerToggle(arg_1_0.switchBtn, True)

def var_0_0.Switch(arg_4_0, arg_4_1):
	arg_4_0.isSwitching = True

	local var_4_0 = GetOrAddComponent(arg_4_0.phases[1], typeof(CanvasGroup))
	local var_4_1 = arg_4_0.phases[1].localPosition
	local var_4_2 = arg_4_0.phases[2].localPosition

	arg_4_0.phases[2].SetAsLastSibling()
	setActive(arg_4_0.phases[1].Find("Image"), False)
	LeanTween.moveLocal(go(arg_4_0.phases[1]), var_4_2, 0.4).setOnComplete(System.Action(function()
		setActive(arg_4_0.phases[1].Find("label"), True)))
	LeanTween.value(go(arg_4_0.phases[1]), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_6_0)
		var_4_0.alpha = arg_6_0))
	setActive(arg_4_0.phases[2].Find("Image"), True)

	local var_4_3 = GetOrAddComponent(arg_4_0.phases[2], typeof(CanvasGroup))

	LeanTween.value(go(arg_4_0.phases[2]), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_7_0)
		var_4_3.alpha = arg_7_0))
	setActive(arg_4_0.phases[2].Find("label"), False)
	LeanTween.moveLocal(go(arg_4_0.phases[2]), var_4_1, 0.4).setOnComplete(System.Action(function()
		arg_4_0.isSwitching = None
		arg_4_0.phases[1], arg_4_0.phases[2] = arg_4_0.phases[2], arg_4_0.phases[1]))
	arg_4_0.UpdateAwardGot()

def var_0_0.UpdateAwardGot(arg_9_0):
	local var_9_0 = arg_9_0.findTF("switcher/phase2/got", arg_9_0.bg)
	local var_9_1 = not arg_9_0.ptData.CanGetNextAward() and arg_9_0.inPhase2

	setActive(var_9_0, var_9_1)

def var_0_0.OnUpdateFlush(arg_10_0):
	var_0_0.super.OnUpdateFlush(arg_10_0)

	local var_10_0 = arg_10_0.activity.getConfig("config_client")
	local var_10_1 = pg.TimeMgr.GetInstance().inTime(var_10_0)

	setActive(arg_10_0.battleBtn, isActive(arg_10_0.battleBtn) and var_10_1)
	arg_10_0.UpdateAwardGot()

	local var_10_2, var_10_3, var_10_4 = arg_10_0.ptData.GetResProgress()

	setText(arg_10_0.step, var_10_4 >= 1 and setColorStr(var_10_2, "#FFA76CFF") or var_10_2)
	setText(arg_10_0.progress, "/" .. var_10_3)
	setFillAmount(arg_10_0.bar, var_10_2 / var_10_3)

return var_0_0
