local var_0_0 = class("TaskWeekPage", import(".TaskCommonPage"))

var_0_0.WEEK_TASK_TYPE_COMMON = 1
var_0_0.WEEK_TASK_TYPE_PT = 2

def var_0_0.getUIName(arg_1_0):
	return "TaskListForWeekPage"

def var_0_0.RefreshWeekProgress(arg_2_0):
	arg_2_0.UpdateWeekProgress(arg_2_0.contextData.weekTaskProgressInfo)

def var_0_0.OnLoaded(arg_3_0):
	var_0_0.super.OnLoaded(arg_3_0)

	local var_3_0 = arg_3_0.findTF("right_panel/task_progress")

	setActive(var_3_0, True)
	setText(var_3_0.Find("title"), i18n("week_task_title_label"))

	arg_3_0.awardPreviewBtn = var_3_0.Find("award_preview")

	setText(arg_3_0.awardPreviewBtn.Find("Text"), i18n("week_task_award_preview_label"))

	arg_3_0.phaseTxt = var_3_0.Find("phase/Text").GetComponent(typeof(Text))
	arg_3_0.progressSlider = var_3_0.Find("slider").GetComponent(typeof(Slider))
	arg_3_0.progressTxt = var_3_0.Find("slider/Text").GetComponent(typeof(Text))
	arg_3_0.awardList = UIItemList.New(var_3_0.Find("awards"), var_3_0.Find("awards/itemtpl"))
	arg_3_0.getBtn = var_3_0.Find("get_btn")
	arg_3_0.getBtnEnableTF = arg_3_0.getBtn.Find("enable")
	arg_3_0.getBtnDisableTF = arg_3_0.getBtn.Find("disable")
	arg_3_0.tip = var_3_0.Find("tip")

	onButton(arg_3_0, arg_3_0.awardPreviewBtn, function()
		local var_4_0 = arg_3_0.contextData.weekTaskProgressInfo

		arg_3_0.contextData.ptAwardWindow.ExecuteAction("Display", var_4_0.GetAllPhaseDrops()), SFX_PANEL)

	arg_3_0.topTF = arg_3_0._scrllPanel.parent
	arg_3_0.topPosy = arg_3_0._scrllPanel.localPosition.y + arg_3_0._scrllPanel.rect.height * 0.5

	arg_3_0._scrollView.onValueChanged.AddListener(function(arg_5_0)
		arg_3_0.UpdateCardTip())

def var_0_0.UpdateCardTip(arg_6_0):
	for iter_6_0, iter_6_1 in pairs(arg_6_0.taskCards):
		local var_6_0 = arg_6_0.topTF.InverseTransformPoint(iter_6_1._tf.position).y + iter_6_1.height * 0.5

		iter_6_1.tip.anchoredPosition3D = math.abs(var_6_0 - arg_6_0.topPosy) < iter_6_1.tip.rect.height * 0.5 and Vector3(-5, -25) or Vector3(-5, 0)

def var_0_0.onUpdateTask(arg_7_0, arg_7_1, arg_7_2):
	var_0_0.super.onUpdateTask(arg_7_0, arg_7_1, arg_7_2)

	if arg_7_1 == 0:
		arg_7_0.taskCards[arg_7_2].tip.anchoredPosition3D = Vector3(-5, -25)

def var_0_0.Update(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	if arg_8_0.contextData.weekTaskProgressInfo.ReachMaxPt() and arg_8_0.isShowing():
		pg.UIMgr.GetInstance().LoadingOn(False)
		arg_8_0.DoDisablePtTaskAnim(function()
			pg.UIMgr.GetInstance().LoadingOff()
			arg_8_0.Flush(arg_8_2)

			if arg_8_3:
				arg_8_3(arg_8_0.taskVOs or {}))
	elif TaskScene.IsPassScenario():
		arg_8_0.Flush(arg_8_2)

		if arg_8_3:
			arg_8_3(arg_8_0.taskVOs or {})
	else
		setActive(arg_8_0._tf, False)

		if arg_8_3:
			arg_8_3({})

def var_0_0.DoDisablePtTaskAnim(arg_10_0, arg_10_1):
	local function var_10_0(arg_11_0, arg_11_1)
		arg_11_0.DoSubmitAnim(function()
			setActive(arg_11_0._go, False)
			arg_11_1())

	arg_10_0._scrollView.enabled = False

	local var_10_1 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.taskVOs or {}):
		if iter_10_1.isWeekTask:
			local var_10_2 = arg_10_0.GetCard(iter_10_1.id)

			if var_10_2:
				table.insert(var_10_1, function(arg_13_0)
					var_10_0(var_10_2, arg_13_0))

	seriesAsync(var_10_1, function()
		arg_10_0._scrollView.enabled = True

		arg_10_1())

def var_0_0.GetCard(arg_15_0, arg_15_1):
	for iter_15_0, iter_15_1 in pairs(arg_15_0.taskCards):
		if iter_15_1.taskVO.id == arg_15_1:
			return iter_15_1

	return None

def var_0_0.Flush(arg_16_0, arg_16_1):
	arg_16_0.taskVOs = {}

	local var_16_0 = arg_16_0.contextData.weekTaskProgressInfo

	arg_16_0.UpdateWeekProgress(var_16_0)

	if not var_16_0.ReachMaxPt():
		local var_16_1 = var_16_0.GetSubTasks()

		for iter_16_0, iter_16_1 in pairs(var_16_1):
			table.insert(arg_16_0.taskVOs, iter_16_1)

	local var_16_2 = arg_16_0.contextData.taskVOsById

	for iter_16_2, iter_16_3 in pairs(var_16_2):
		if iter_16_3.ShowOnTaskScene() and arg_16_1[iter_16_3.GetRealType()]:
			table.insert(arg_16_0.taskVOs, iter_16_3)

	table.sort(arg_16_0.taskVOs, function(arg_17_0, arg_17_1)
		local var_17_0 = arg_17_0.getTaskStatus(arg_17_0)
		local var_17_1 = arg_17_1.getTaskStatus(arg_17_1)

		if var_17_0 == var_17_1:
			return (arg_17_0.isWeekTask and 0 or 1) > (arg_17_1.isWeekTask and 0 or 1)
		else
			return var_17_1 < var_17_0)
	arg_16_0.Show()
	arg_16_0._scrollView.SetTotalCount(#arg_16_0.taskVOs, -1)

def var_0_0.UpdateWeekProgress(arg_18_0, arg_18_1):
	arg_18_0.UpdateWeekProgressGetBtn(arg_18_1)

	arg_18_0.phaseTxt.text = arg_18_1.GetPhase() .. "/" .. arg_18_1.GetTotalPhase()

	local var_18_0 = arg_18_1.GetProgress()
	local var_18_1 = arg_18_1.GetTarget()

	arg_18_0.progressSlider.value = var_18_0 / var_18_1
	arg_18_0.progressTxt.text = var_18_0 .. "/" .. var_18_1

	local var_18_2 = arg_18_1.GetDropList()

	arg_18_0.awardList.make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventUpdate:
			local var_19_0 = var_18_2[arg_19_1 + 1]
			local var_19_1 = {
				type = var_19_0[1],
				id = var_19_0[2],
				count = var_19_0[3]
			}

			updateDrop(arg_19_2, var_19_1)
			onButton(arg_18_0, arg_19_2, function()
				arg_18_0.emit(TaskMediator.ON_DROP, var_19_1), SFX_PANEL))
	arg_18_0.awardList.align(#var_18_2)

def var_0_0.UpdateWeekProgressGetBtn(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_1.CanUpgrade()

	setGray(arg_21_0.getBtn, not var_21_0, False)
	setActive(arg_21_0.getBtnEnableTF, var_21_0)
	setActive(arg_21_0.getBtnDisableTF, not var_21_0)
	setActive(arg_21_0.tip, var_21_0)
	onButton(arg_21_0, arg_21_0.getBtn, function()
		if var_21_0:
			arg_21_0.JudgeOverflow(arg_21_1, function()
				arg_21_0.emit(TaskMediator.ON_SUBMIT_WEEK_PROGREE)), SFX_PANEL)

def var_0_0.JudgeOverflow(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = getProxy(PlayerProxy).getRawData()
	local var_24_1 = pg.gameset.urpt_chapter_max.description[1]
	local var_24_2 = LOCK_UR_SHIP and 0 or getProxy(BagProxy).GetLimitCntById(var_24_1)
	local var_24_3 = arg_24_1.GetDropList()
	local var_24_4, var_24_5 = Task.StaticJudgeOverflow(var_24_0.gold, var_24_0.oil, var_24_2, True, True, var_24_3)

	if var_24_4:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_ITEM_BOX,
			content = i18n("award_max_warning"),
			items = var_24_5,
			onYes = arg_24_2
		})
	else
		arg_24_2()

def var_0_0.OnDestroy(arg_25_0):
	arg_25_0._scrollView.onValueChanged.RemoveAllListeners()

def var_0_0.RefreshWeekTaskPageBefore(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_0.GetCard(arg_26_1)

	if var_26_0:
		setActive(var_26_0._go, False)

return var_0_0
