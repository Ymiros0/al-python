local var_0_0 = class("FrameTemplatePage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("got_btn", arg_1_0.bg)
	arg_1_0.switchBtn = arg_1_0.findTF("AD/switch_btn")
	arg_1_0.phases = {
		arg_1_0.findTF("AD/switcher/phase1"),
		arg_1_0.findTF("AD/switcher/phase2")
	}
	arg_1_0.bar = arg_1_0.findTF("AD/switcher/phase2/Image/barContent/bar")
	arg_1_0.step = arg_1_0.findTF("AD/switcher/phase2/Image/step")
	arg_1_0.progress = arg_1_0.findTF("AD/switcher/phase2/Image/progress")

def var_0_0.OnDataSetting(arg_2_0):
	if arg_2_0.ptData:
		arg_2_0.ptData.Update(arg_2_0.activity)
	else
		arg_2_0.ptData = ActivityPtData.New(arg_2_0.activity)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK, {
			page = "activity"
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		local var_5_0 = {}
		local var_5_1 = arg_3_0.ptData.GetAward()
		local var_5_2 = getProxy(PlayerProxy).getData()

		if var_5_1.type == DROP_TYPE_RESOURCE and var_5_1.id == PlayerConst.ResGold and var_5_2.GoldMax(var_5_1.count):
			table.insert(var_5_0, function(arg_6_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("gold_max_tip_title") .. i18n("award_max_warning"),
					onYes = arg_6_0
				}))

		seriesAsync(var_5_0, function()
			local var_7_0, var_7_1 = arg_3_0.ptData.GetResProgress()

			arg_3_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_3_0.ptData.GetId(),
				arg1 = var_7_1
			})), SFX_PANEL)
	onToggle(arg_3_0, arg_3_0.switchBtn, function(arg_8_0)
		if arg_3_0.isSwitching:
			return

		arg_3_0.inPhase2 = arg_8_0

		arg_3_0.Switch(arg_8_0), SFX_PANEL)

	local var_3_0 = arg_3_0.activity.getConfig("config_client")
	local var_3_1 = pg.TimeMgr.GetInstance().inTime(var_3_0)

	setActive(arg_3_0.battleBtn, var_3_1)

	arg_3_0.inPhase2 = var_3_1

	if var_3_1:
		triggerToggle(arg_3_0.switchBtn, True)

def var_0_0.OnUpdateFlush(arg_9_0):
	local var_9_0 = arg_9_0.ptData.CanGetAward()
	local var_9_1 = arg_9_0.ptData.CanGetNextAward()

	setActive(arg_9_0.getBtn, var_9_0)
	setActive(arg_9_0.gotBtn, not var_9_1)

	local var_9_2, var_9_3, var_9_4 = arg_9_0.ptData.GetResProgress()

	setText(arg_9_0.step, var_9_4 >= 1 and setColorStr(var_9_2, COLOR_GREEN) or var_9_2)
	setText(arg_9_0.progress, "/" .. var_9_3)
	setFillAmount(arg_9_0.bar, var_9_2 / var_9_3)
	arg_9_0.UpdateAwardGot()

def var_0_0.Switch(arg_10_0, arg_10_1):
	arg_10_0.isSwitching = True

	local var_10_0 = GetOrAddComponent(arg_10_0.phases[1], typeof(CanvasGroup))
	local var_10_1 = arg_10_0.phases[1].localPosition
	local var_10_2 = arg_10_0.phases[2].localPosition

	arg_10_0.phases[2].SetAsLastSibling()
	setActive(arg_10_0.phases[1].Find("Image"), False)
	LeanTween.moveLocal(go(arg_10_0.phases[1]), var_10_2, 0.4).setOnComplete(System.Action(function()
		setActive(arg_10_0.phases[1].Find("label"), True)))
	LeanTween.value(go(arg_10_0.phases[1]), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_12_0)
		var_10_0.alpha = arg_12_0))
	setActive(arg_10_0.phases[2].Find("Image"), True)

	local var_10_3 = GetOrAddComponent(arg_10_0.phases[2], typeof(CanvasGroup))

	LeanTween.value(go(arg_10_0.phases[2]), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_13_0)
		var_10_3.alpha = arg_13_0))
	setActive(arg_10_0.phases[2].Find("label"), False)
	LeanTween.moveLocal(go(arg_10_0.phases[2]), var_10_1, 0.4).setOnComplete(System.Action(function()
		arg_10_0.isSwitching = None
		arg_10_0.phases[1], arg_10_0.phases[2] = arg_10_0.phases[2], arg_10_0.phases[1]))
	arg_10_0.UpdateAwardGot()

def var_0_0.UpdateAwardGot(arg_15_0):
	local var_15_0 = arg_15_0.findTF("switcher/phase2/got", arg_15_0.bg)
	local var_15_1 = not arg_15_0.ptData.CanGetNextAward() and arg_15_0.inPhase2

	setActive(var_15_0, var_15_1)

	if var_15_1:
		setActive(arg_15_0.battleBtn, False)

def var_0_0.OnDestroy(arg_16_0):
	return

return var_0_0
