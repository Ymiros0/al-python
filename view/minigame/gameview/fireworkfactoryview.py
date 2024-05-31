local var_0_0 = class("FireworkFactoryView", import("..BaseMiniGameView"))
local var_0_1 = Mathf

def var_0_0.getUIName(arg_1_0):
	return "FireworkFactoryUI"

local var_0_2 = 50
local var_0_3 = {
	{
		color = "FFD26FFF",
		name = "na"
	},
	{
		color = "DE89ECFF",
		name = "k"
	},
	{
		color = "8F77DFFF",
		name = "rb"
	},
	{
		color = "70ad9f",
		name = "zn"
	},
	{
		color = "FF7069FF",
		name = "ca"
	},
	{
		color = "7faf6e",
		name = "cu"
	}
}
local var_0_4 = {
	"s",
	"a",
	"b",
	"c"
}

def var_0_0.TransformColor(arg_2_0):
	local var_2_0 = tonumber(string.sub(arg_2_0, 1, 2), 16)
	local var_2_1 = tonumber(string.sub(arg_2_0, 3, 4), 16)
	local var_2_2 = tonumber(string.sub(arg_2_0, 5, 6), 16)

	return Color.New(var_2_0 / 255, var_2_1 / 255, var_2_2 / 255)

def var_0_0.init(arg_3_0):
	arg_3_0.top = arg_3_0.findTF("top")
	arg_3_0.plate = arg_3_0.findTF("plate")
	arg_3_0.storage = arg_3_0.findTF("storage")
	arg_3_0.dispenseView = arg_3_0.findTF("top/dispenseView")

	setActive(arg_3_0.dispenseView, False)

	arg_3_0.resultWindow = arg_3_0.findTF("top/resultwindow")

	setActive(arg_3_0.resultWindow, False)

	arg_3_0.btn_back = arg_3_0.top.Find("noAdaptPanel/back")
	arg_3_0.btn_help = arg_3_0.top.Find("noAdaptPanel/title/help")
	arg_3_0.timesText = arg_3_0.top.Find("times/text")
	arg_3_0.ballPlate = arg_3_0.plate.Find("ball_plate")
	arg_3_0.plateRings = {}

	for iter_3_0 = 1, 3:
		table.insert(arg_3_0.plateRings, arg_3_0.ballPlate.GetChild(iter_3_0))

	arg_3_0.btn_load = arg_3_0.plate.Find("btn_load")
	arg_3_0.ballSelectPanel = arg_3_0.plate.Find("panel/layout")
	arg_3_0.ballSelects = CustomIndexLayer.Clone2Full(arg_3_0.ballSelectPanel, 3)
	arg_3_0.ballSelectStatus = {
		0,
		0,
		0
	}
	arg_3_0.lastSelectedBall = None
	arg_3_0.ballStoragePanel = arg_3_0.storage.Find("house/layout")
	arg_3_0.ballStorages = CustomIndexLayer.Clone2Full(arg_3_0.ballStoragePanel, 6)
	arg_3_0.screen_mask = arg_3_0.findTF("mask")
	arg_3_0.btn_next = arg_3_0.findTF("Button")
	arg_3_0.btn_next_text = arg_3_0.btn_next.Find("Image")
	arg_3_0.desc_dispense = arg_3_0.dispenseView.Find("intro/Scroll View/Viewport/text")

	setText(arg_3_0.desc_dispense, i18n("help_firework_produce"))

	arg_3_0.btn_dispenseBG = arg_3_0.dispenseView.Find("bg")
	arg_3_0.btn_hammer = arg_3_0.dispenseView.Find("container/Button")
	arg_3_0.btn_hammer_text = arg_3_0.btn_hammer.Find("text")
	arg_3_0.slider_powder = arg_3_0.dispenseView.Find("container/Slider/Fill Area").GetComponent("Slider")
	arg_3_0.slider_progress = arg_3_0.dispenseView.Find("progress/Slider").GetComponent("Slider")
	arg_3_0.slider_progress_bg = arg_3_0.dispenseView.Find("progress/Slider/Background/progressdi")
	arg_3_0.slider_bubble = arg_3_0.dispenseView.Find("container/Slider/Fill Area/Fill/handler/bubble")
	arg_3_0.slider_bubble_text = arg_3_0.slider_bubble.Find("text")
	arg_3_0.progress_width = arg_3_0.dispenseView.Find("progress/Slider/Handle Slide Area").rect.width
	arg_3_0.progress_sub_mark_1 = arg_3_0.dispenseView.Find("progress/Slider/Handle Slide Area/submark1")
	arg_3_0.progress_sub_mark_2 = arg_3_0.dispenseView.Find("progress/Slider/Handle Slide Area/submark2")
	arg_3_0.progress_dis = {}

	for iter_3_1 = 0, arg_3_0.slider_progress_bg.childCount - 1:
		table.insert(arg_3_0.progress_dis, arg_3_0.slider_progress_bg.GetChild(iter_3_1))

	arg_3_0.result_digits = {}

	pg.PoolMgr.GetInstance().GetPrefab("ui/light01", "", True, function(arg_4_0)
		tf(arg_4_0).SetParent(arg_3_0.dispenseView, False)
		arg_4_0.SetActive(False)

		arg_3_0.effect_light = arg_4_0)

	arg_3_0.result_bg = arg_3_0.resultWindow.Find("bg")
	arg_3_0.result_desc = arg_3_0.resultWindow.Find("window/Text")

	setText(arg_3_0.result_desc, i18n("result_firework_produce"))

	arg_3_0.btn_result_confirm = arg_3_0.resultWindow.Find("window/button")
	arg_3_0.result_pingjia = arg_3_0.resultWindow.Find("window/pingjia").GetComponent("Image")
	arg_3_0.flagStart = False
	arg_3_0.flagDispense = False
	arg_3_0.progressDispense = 0

def var_0_0.SetSprite(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_1.GetComponent("Image")

	arg_5_0.SetImageSprite(var_5_0, arg_5_2)

def var_0_0.SetImageSprite(arg_6_0, arg_6_1, arg_6_2):
	pg.PoolMgr.GetInstance().GetSprite("ui/fireworkfactoryui_atlas", arg_6_2, False, function(arg_7_0)
		arg_6_1.sprite = arg_7_0)

def var_0_0.didEnter(arg_8_0):
	onButton(arg_8_0, arg_8_0.btn_back, function()
		if arg_8_0.flagDispense:
			arg_8_0.ExitDispenseView()
		elif arg_8_0.CheckpowderDispensed() and arg_8_0.flagStart:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("tips_firework_exit"),
				def onYes:()
					arg_8_0.emit(var_0_0.ON_BACK_PRESSED)
			})
		else
			arg_8_0.emit(var_0_0.ON_BACK))
	onButton(arg_8_0, arg_8_0.btn_dispenseBG, function()
		arg_8_0.ExitDispenseView())
	onButton(arg_8_0, arg_8_0.btn_help, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_xinnian2022_firework.tip
		}))
	onButton(arg_8_0, arg_8_0.btn_next, function()
		if not arg_8_0.flagStart:
			arg_8_0.flagStart = True

			arg_8_0.UpdateNextBtn()
		elif arg_8_0.CheckballLoaded():
			arg_8_0.EnterDispenseView())
	onButton(arg_8_0, arg_8_0.btn_hammer, function()
		local var_14_0 = arg_8_0.progressDispense

		if var_14_0 == 0:
			arg_8_0.ResetHammerAnim()
			arg_8_0.FindNextPowderProgress()
			arg_8_0.UpdateContainer()
		elif var_14_0 == 1:
			arg_8_0.result_digits[1] = arg_8_0.slider_powder.value * 100

			arg_8_0.FindandStopProgress()
			arg_8_0.UpdateContainer()
		elif var_14_0 == 2:
			arg_8_0.result_digits[2] = arg_8_0.slider_powder.value * 100

			arg_8_0.FindandStopProgress()
			arg_8_0.UpdateContainer()
		elif var_14_0 == 3:
			arg_8_0.result_digits[3] = arg_8_0.slider_powder.value * 100

			arg_8_0.FindandStopProgress()
			arg_8_0.UpdateContainer())
	onButton(arg_8_0, arg_8_0.btn_result_confirm, function()
		arg_8_0.ShowResult())
	onButton(arg_8_0, arg_8_0.result_bg, function()
		arg_8_0.ShowResult())

	for iter_8_0 = 1, #arg_8_0.ballStorages:
		local var_8_0 = arg_8_0.ballStorages[iter_8_0]

		arg_8_0.UpdateBall(var_8_0, iter_8_0)
		onButton(arg_8_0, var_8_0.Find("mask"), function()
			if not arg_8_0.lastSelectedBall or arg_8_0.lastSelectedBall <= 0:
				return

			arg_8_0.ballSelectStatus[arg_8_0.lastSelectedBall] = iter_8_0

			arg_8_0.UpdateRing(arg_8_0.lastSelectedBall, iter_8_0)
			arg_8_0.UpdateBall(arg_8_0.ballSelects[arg_8_0.lastSelectedBall].Find("ball"), iter_8_0)
			arg_8_0.UdpateSelectedBall(arg_8_0.lastSelectedBall + 1)
			arg_8_0.UpdateNextBtn())

	for iter_8_1 = 1, #arg_8_0.ballSelects:
		local var_8_1 = arg_8_0.ballSelects[iter_8_1]

		arg_8_0.UpdateBall(var_8_1.Find("ball"), 0)
		arg_8_0.UpdateRing(iter_8_1, 0)
		onButton(arg_8_0, var_8_1.Find("mask"), function()
			arg_8_0.ballSelectStatus[iter_8_1] = 0

			arg_8_0.UpdateBall(arg_8_0.ballSelects[iter_8_1].Find("ball"), 0)
			arg_8_0.UpdateRing(iter_8_1, 0)
			arg_8_0.UdpateSelectedBall(iter_8_1)
			arg_8_0.UpdateNextBtn())

	arg_8_0.ResetView()
	pg.UIMgr.GetInstance().OverlayPanel(arg_8_0.top, {
		groupName = LayerWeightConst.GROUP_FIREWORK_PRODUCE
	})

	local var_8_2 = arg_8_0.GetMGData().GetSimpleValue("score_reference")
	local var_8_3 = {}

	var_8_3[1] = 0

	for iter_8_2, iter_8_3 in ipairs(var_8_2):
		var_8_3[#var_8_2 - iter_8_2 + 2] = iter_8_3[1]
		var_8_3[#var_8_2 + iter_8_2 + 1] = iter_8_3[2]

	var_8_3[#var_8_3] = 300

	for iter_8_4 = 1, #var_8_3 - 1:
		local var_8_4 = var_8_3[iter_8_4] / 300
		local var_8_5 = var_8_3[iter_8_4 + 1] / 300

		arg_8_0.progress_dis[iter_8_4].anchorMin = Vector2(var_8_4, 0)
		arg_8_0.progress_dis[iter_8_4].anchorMax = Vector2(var_8_5, 1)
		arg_8_0.progress_dis[iter_8_4].sizeDelta = Vector2.zero

def var_0_0.UpdateNextBtn(arg_19_0):
	if not arg_19_0.flagStart:
		local var_19_0 = "dispense_ready"
		local var_19_1 = arg_19_0.GetMGData().GetRuntimeData("elements")

		if var_19_1 and #var_19_1 > 3 and var_19_1[4] == SummerFeastScene.GetCurrentDay():
			var_19_0 = "dispense_retry"

		arg_19_0.SetSprite(arg_19_0.btn_next_text, var_19_0)
	else
		arg_19_0.SetSprite(arg_19_0.btn_next_text, "dispense_confirm")

	setActive(arg_19_0.screen_mask, not arg_19_0.flagStart)

	local var_19_2 = not arg_19_0.flagStart or arg_19_0.CheckballLoaded()

	setButtonEnabled(arg_19_0.btn_next, var_19_2)

def var_0_0.UpdateDispenseBtn(arg_20_0):
	local var_20_0 = arg_20_0.CheckpowderDispensed()

	arg_20_0.SetImageSprite(arg_20_0.btn_load_img, var_20_0 and "btn_loadcompleted" or "btn_load")
	arg_20_0.SetSprite(arg_20_0.btn_load_text, var_20_0 and "load_completed" or "load_ready")
	setButtonEnabled(arg_20_0.btn_load, not var_20_0)

local var_0_5 = {
	"start",
	"first_time",
	"second_time",
	"third_time",
	"finish_time"
}

def var_0_0.FindandStopProgress(arg_21_0):
	arg_21_0.StopHammerAnim()
	setButtonEnabled(arg_21_0.btn_hammer, False)
	setButtonEnabled(arg_21_0.btn_dispenseBG, False)
	setText(arg_21_0.slider_bubble_text, math.ceil(arg_21_0.result_digits[#arg_21_0.result_digits]) .. "%")
	setActive(arg_21_0.slider_bubble, True)
	setActive(arg_21_0.effect_light, True)

	arg_21_0.progressDispense = #arg_21_0.result_digits >= 3 and 4 or 0

	local var_21_0 = 0

	for iter_21_0 = 1, 3:
		local var_21_1 = arg_21_0.result_digits[iter_21_0]

		if var_21_1:
			var_21_0 = var_21_0 + var_21_1

	local var_21_2 = 0

	for iter_21_1 = 1, #arg_21_0.result_digits - 1:
		local var_21_3 = arg_21_0.result_digits[iter_21_1]

		if var_21_3:
			var_21_2 = var_21_2 + var_21_3

			if iter_21_1 == 1:
				setActive(arg_21_0.progress_sub_mark_1, True)

				local var_21_4 = Vector2(arg_21_0.progress_width * var_21_2 / 300, 27)

				arg_21_0.progress_sub_mark_1.anchoredPosition = var_21_4
			elif iter_21_1 == 2:
				setActive(arg_21_0.progress_sub_mark_2, True)

				local var_21_5 = Vector2(arg_21_0.progress_width * var_21_2 / 300, 27)

				arg_21_0.progress_sub_mark_2.anchoredPosition = var_21_5

	local var_21_6 = arg_21_0.slider_bubble.transform.position
	local var_21_7 = arg_21_0.slider_progress.transform.position
	local var_21_8 = arg_21_0.slider_progress.value

	arg_21_0.progressAnim = LeanTween.value(arg_21_0.slider_progress.gameObject, 0, 1, 1.5).setEase(LeanTweenType.linear).setOnUpdate(System.Action_float(function(arg_22_0)
		arg_21_0.slider_progress.value = var_0_1.Lerp(var_21_8, var_21_0 / 300, arg_22_0)

		if arg_21_0.effect_light:
			arg_21_0.effect_light.transform.position = Vector3.Lerp(var_21_6, var_21_7, arg_22_0 * 3) - Vector3(0, 0, 2)

			if arg_22_0 * 3 > 1:
				setActive(arg_21_0.effect_light, False))).setOnComplete(System.Action(function()
		setButtonEnabled(arg_21_0.btn_hammer, True)
		setButtonEnabled(arg_21_0.btn_dispenseBG, True)

		if arg_21_0.progressDispense > 3:
			arg_21_0.FindNextPowderProgress()))

def var_0_0.FindNextPowderProgress(arg_24_0):
	arg_24_0.progressDispense = #arg_24_0.result_digits + 1

	if arg_24_0.progressDispense > 3:
		arg_24_0.StopHammerAnim()
		setButtonEnabled(arg_24_0.btn_hammer, False)
		arg_24_0.ShowResultWindow()

def var_0_0.ShowResultWindow(arg_25_0):
	if #arg_25_0.result_digits < 3:
		return

	setActive(arg_25_0.resultWindow, True)

	local var_25_0 = arg_25_0.GetMGData().GetSimpleValue("score_reference")
	local var_25_1 = 0

	for iter_25_0 = 1, 3:
		var_25_1 = var_25_1 + arg_25_0.result_digits[iter_25_0]

	local var_25_2 = 4

	for iter_25_1, iter_25_2 in ipairs(var_25_0):
		if var_25_1 >= iter_25_2[1] and var_25_1 <= iter_25_2[2]:
			var_25_2 = iter_25_1

			break

	if var_25_2 <= 0:
		return

	arg_25_0.SetImageSprite(arg_25_0.result_pingjia, var_0_4[var_25_2])

def var_0_0.ShowResult(arg_26_0):
	if arg_26_0.GetMGHubData().count <= 0:
		arg_26_0.AfterResult()
	else
		arg_26_0.GetReward()

	setActive(arg_26_0.resultWindow, False)

def var_0_0.OnGetAwardDone(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0.GetMGHubData()
	local var_27_1 = var_27_0.ultimate == 0 and var_27_0.usedtime >= var_27_0.getConfig("reward_need")

	if arg_27_1.cmd == MiniGameOPCommand.CMD_COMPLETE and var_27_1:
		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_27_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
	elif arg_27_1.cmd == MiniGameOPCommand.CMD_ULTIMATE:
		arg_27_0.AfterResult()
	else
		arg_27_0.AfterResult()

def var_0_0.AfterResult(arg_28_0):
	local var_28_0 = SummerFeastScene.GetCurrentDay()
	local var_28_1 = Clone(arg_28_0.ballSelectStatus)

	table.insert(var_28_1, var_28_0)
	arg_28_0.StoreDataToServer(var_28_1)
	onNextTick(function()
		arg_28_0.emit(var_0_0.ON_BACK))

def var_0_0.reset(arg_30_0):
	arg_30_0.ExitDispenseView()

	arg_30_0.flagStart = False
	arg_30_0.flagDispense = False
	arg_30_0.progressDispense = 0
	arg_30_0.result_digits = {}

	arg_30_0.ResetView()
	arg_30_0.UpdateNextBtn()

def var_0_0.GetReward(arg_31_0):
	if #arg_31_0.result_digits < 3:
		return

	local var_31_0 = arg_31_0.GetMGData().GetSimpleValue("score_reference")
	local var_31_1 = 0

	for iter_31_0 = 1, 3:
		var_31_1 = var_31_1 + arg_31_0.result_digits[iter_31_0]

	local var_31_2 = 4

	for iter_31_1, iter_31_2 in ipairs(var_31_0):
		if var_31_1 >= iter_31_2[1] and var_31_1 <= iter_31_2[2]:
			var_31_2 = iter_31_1

			break

	if var_31_2 <= 0:
		return

	arg_31_0.SendSuccess(var_31_2)

def var_0_0.ResetHammerAnim(arg_32_0):
	if arg_32_0.hammerAnim:
		arg_32_0.StopHammerAnim()

	setActive(arg_32_0.slider_bubble, False)

	local var_32_0 = (arg_32_0.GetMGData().GetSimpleValue("roundTime") or var_0_2) / 100

	arg_32_0.hammerAnim = LeanTween.value(arg_32_0.slider_powder.gameObject, 0, 1, var_32_0 * 2).setEase(LeanTweenType.linear).setLoopPingPong().setOnUpdate(System.Action_float(function(arg_33_0)
		arg_32_0.slider_powder.value = arg_33_0))

def var_0_0.StopHammerAnim(arg_34_0):
	if not arg_34_0.hammerAnim:
		return

	LeanTween.cancel(arg_34_0.hammerAnim.uniqueId)

	arg_34_0.hammerAnim = None

def var_0_0.UpdateContainer(arg_35_0):
	arg_35_0.SetSprite(arg_35_0.btn_hammer_text, var_0_5[arg_35_0.progressDispense + 1])

	local var_35_0 = 0
	local var_35_1 = True

	for iter_35_0 = 1, 3:
		local var_35_2 = arg_35_0.result_digits[iter_35_0]

		var_35_1 = var_35_1 and var_35_2 != None

		if var_35_2:
			var_35_0 = var_35_0 + var_35_2

	arg_35_0.slider_progress.value = var_35_0 / 300

def var_0_0.StopProgressAnim(arg_36_0):
	if not arg_36_0.progressAnim:
		return

	LeanTween.cancel(arg_36_0.progressAnim.uniqueId)

	arg_36_0.progressAnim = None

def var_0_0.CheckballLoaded(arg_37_0):
	return _.all(arg_37_0.ballSelectStatus, function(arg_38_0)
		return arg_38_0 > 0)

def var_0_0.CheckpowderDispensed(arg_39_0):
	return #arg_39_0.result_digits >= 3

def var_0_0.UpdateBall(arg_40_0, arg_40_1, arg_40_2):
	setActive(arg_40_1, arg_40_2 > 0)

	if arg_40_2 <= 0:
		return

	arg_40_1.GetComponent("Image").color = arg_40_0.TransformColor(var_0_3[arg_40_2].color)

	arg_40_0.SetSprite(arg_40_1.Find("symbol"), var_0_3[arg_40_2].name)

def var_0_0.UpdateRing(arg_41_0, arg_41_1, arg_41_2):
	if arg_41_1 <= 0 or arg_41_1 > 3:
		return

	local var_41_0 = arg_41_0.plateRings[arg_41_1]

	setActive(var_41_0, arg_41_2 > 0)

	if arg_41_2 <= 0:
		return

	var_41_0.GetComponent("Image").color = arg_41_0.TransformColor(var_0_3[arg_41_2].color)

def var_0_0.ResetView(arg_42_0):
	_.each(arg_42_0.plateRings, function(arg_43_0)
		setActive(arg_43_0, False))
	_.each(arg_42_0.ballSelects, function(arg_44_0)
		setActive(arg_44_0.Find("ball"), False)
		setActive(arg_44_0.Find("selected"), False))

	local var_42_0 = arg_42_0.GetMGHubData()

	setText(arg_42_0.timesText, var_42_0.count)

	local var_42_1 = arg_42_0.GetMGData().GetRuntimeData("elements")

	if var_42_1 and #var_42_1 > 3 and var_42_1[4] == SummerFeastScene.GetCurrentDay():
		for iter_42_0 = 1, 3:
			local var_42_2 = var_42_1[iter_42_0]

			arg_42_0.ballSelectStatus[iter_42_0] = var_42_2

			if var_42_2 > 0:
				arg_42_0.UpdateRing(iter_42_0, var_42_2)

				local var_42_3 = arg_42_0.ballSelects[iter_42_0].Find("ball")

				arg_42_0.UpdateBall(var_42_3, var_42_2)

	arg_42_0.UdpateSelectedBall(1)
	arg_42_0.UpdateNextBtn()
	setActive(arg_42_0.slider_bubble, False)
	setActive(arg_42_0.progress_sub_mark_1, False)
	setActive(arg_42_0.progress_sub_mark_2, False)

def var_0_0.UdpateSelectedBall(arg_45_0, arg_45_1):
	if arg_45_1 <= 0 or arg_45_1 > 3:
		return

	if arg_45_0.lastSelectedBall:
		if arg_45_0.lastSelectedBall == arg_45_1:
			return

		setActive(arg_45_0.ballSelects[arg_45_0.lastSelectedBall].Find("selected"), False)

	setActive(arg_45_0.ballSelects[arg_45_1].Find("selected"), True)

	arg_45_0.lastSelectedBall = arg_45_1

def var_0_0.EnterDispenseView(arg_46_0):
	setActive(arg_46_0.dispenseView, True)

	arg_46_0.flagDispense = True
	arg_46_0.progressDispense = #arg_46_0.result_digits >= 3 and 4 or 0

	arg_46_0.UpdateContainer()

	arg_46_0.slider_powder.value = 0

def var_0_0.ExitDispenseView(arg_47_0):
	if not arg_47_0.flagDispense:
		return

	arg_47_0.UpdateNextBtn()
	arg_47_0.StopHammerAnim()
	arg_47_0.StopProgressAnim()

	arg_47_0.progressDispense = 0

	setActive(arg_47_0.dispenseView, False)
	setButtonEnabled(arg_47_0.btn_hammer, True)

	local var_47_0 = arg_47_0.GetMGHubData()

	setText(arg_47_0.timesText, var_47_0.count)
	setActive(arg_47_0.slider_bubble, False)

	if arg_47_0.effect_light:
		setActive(arg_47_0.effect_light, False)

	arg_47_0.flagDispense = False

def var_0_0.willExit(arg_48_0):
	arg_48_0.ExitDispenseView()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_48_0.top, arg_48_0._tf)

	if arg_48_0.effect_light:
		pg.PoolMgr.GetInstance().ReturnPrefab("ui/light01", "", arg_48_0.effect_light)

	pg.PoolMgr.GetInstance().DestroyPrefab("ui/light01", "")
	pg.PoolMgr.GetInstance().DestroySprite("ui/fireworkfactoryui_atlas")

	if arg_48_0.OPTimer:
		arg_48_0.OPTimer.Stop()

		arg_48_0.OPTimer = None

return var_0_0
