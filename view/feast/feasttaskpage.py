local var_0_0 = class("FeastTaskPage", import("view.base.BaseSubView"))

var_0_0.PAGE_PT = 1
var_0_0.PAGE_TASK = 2

def var_0_0.getUIName(arg_1_0):
	return "FeastTaskPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.getAllBtn = arg_2_0.findTF("main/getall")
	arg_2_0.getAllTip = arg_2_0.getAllBtn.Find("tip")
	arg_2_0.levelTxt = arg_2_0.findTF("main/level/Text").GetComponent(typeof(Text))
	arg_2_0.progressTxt = arg_2_0.findTF("main/level/value/Text").GetComponent(typeof(Text))
	arg_2_0.progress = arg_2_0.findTF("main/level/progress/bar")
	arg_2_0.lastAwardItem = arg_2_0.findTF("main/level/item")
	arg_2_0.lastAwardLvTxt = arg_2_0.lastAwardItem.Find("lock/Text").GetComponent(typeof(Text))

	setText(arg_2_0.lastAwardItem.Find("get"), i18n("feast_task_pt_get"))
	setText(arg_2_0.lastAwardItem.Find("got"), i18n("feast_task_pt_got"))
	setText(arg_2_0.findTF("main/tip"), i18n("feast_click_to_close"))
	setText(arg_2_0.findTF("main/level/value/label"), i18n("feast_task_pt_label"))

	arg_2_0.taskTip = arg_2_0.findTF("main/toggles/task/tip")
	arg_2_0.toggles = {
		arg_2_0.findTF("main/toggles/pt"),
		arg_2_0.findTF("main/toggles/task")
	}
	arg_2_0.scrollRects = {
		arg_2_0.findTF("main/pt/scrollrect").GetComponent("LScrollRect"),
		arg_2_0.findTF("main/task/scrollrect").GetComponent("LScrollRect")
	}
	arg_2_0.cardCls = {
		FeastPtCard,
		FeastTaskCard
	}
	arg_2_0.cards = {
		{},
		{}
	}
	arg_2_0.counts = {
		0,
		0
	}

	arg_2_0.AddListener()

def var_0_0.AddListener(arg_3_0):
	arg_3_0.bind(FeastScene.ON_TASK_UPDATE, function(arg_4_0)
		if arg_3_0.isShowing():
			arg_3_0.GenTaskData()
			arg_3_0.UpdateLevel()

			if arg_3_0.page == var_0_0.PAGE_TASK:
				arg_3_0.SwitchPage(arg_3_0.page))
	arg_3_0.bind(FeastScene.ON_ACT_UPDATE, function(arg_5_0)
		if arg_3_0.isShowing():
			arg_3_0.GenPtData()
			arg_3_0.UpdateLevel()

			if arg_3_0.page == var_0_0.PAGE_PT:
				arg_3_0.SwitchPage(arg_3_0.page))

def var_0_0.OnInit(arg_6_0):
	for iter_6_0, iter_6_1 in ipairs(arg_6_0.scrollRects):
		function iter_6_1.onInitItem(arg_7_0)
			arg_6_0.OnInitItem(iter_6_0, arg_7_0)

		function iter_6_1.onUpdateItem(arg_8_0, arg_8_1)
			arg_6_0.OnUpdateItem(iter_6_0, arg_8_0, arg_8_1)

	for iter_6_2, iter_6_3 in ipairs(arg_6_0.toggles):
		onToggle(arg_6_0, iter_6_3, function(arg_9_0)
			if arg_9_0:
				arg_6_0.SwitchPage(iter_6_2), SFX_PANEL)

	onButton(arg_6_0, arg_6_0._tf, function()
		arg_6_0.Hide(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.getAllBtn, function()
		if arg_6_0.page == var_0_0.PAGE_TASK:
			arg_6_0.GetAllForTask()
		elif arg_6_0.page == var_0_0.PAGE_PT:
			arg_6_0.GetAllForPt(), SFX_PANEL)

def var_0_0.UpdateGetAllTip(arg_12_0, arg_12_1):
	local var_12_0 = getProxy(FeastProxy)
	local var_12_1 = False

	if arg_12_1 == var_0_0.PAGE_PT:
		var_12_1 = var_12_0.ShouldTipPt()
	elif arg_12_1 == var_0_0.PAGE_TASK:
		var_12_1 = var_12_0.ShouldTipFeastTask()

	setActive(arg_12_0.getAllTip, var_12_1)
	setActive(arg_12_0.taskTip, var_12_0.ShouldTipFeastTask())

def var_0_0.GetAllForTask(arg_13_0):
	local var_13_0 = {}
	local var_13_1 = getProxy(TaskProxy)

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.taskList):
		local var_13_2 = var_13_1.getTaskById(iter_13_1)

		if var_13_2 and var_13_2.isFinish() and not var_13_2.isReceive():
			table.insert(var_13_0, var_13_2)

	if #var_13_0 <= 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("faest_nothing_to_get"))

		return

	arg_13_0.emit(FeastMediator.ON_SUBMIT_ONE_KEY, var_13_0)

def var_0_0.GetAllForPt(arg_14_0):
	if not arg_14_0.ptActData.CanGetAward():
		pg.TipsMgr.GetInstance().ShowTips(i18n("faest_nothing_to_get"))

		return

	local var_14_0 = arg_14_0.ptActData.GetCurrTarget()

	arg_14_0.emit(FeastMediator.EVENT_PT_OPERATION, {
		cmd = 4,
		activity_id = arg_14_0.ptActData.GetId(),
		arg1 = var_14_0
	})

def var_0_0.SwitchPage(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.counts[arg_15_1] or 0

	arg_15_0.scrollRects[arg_15_1].SetTotalCount(var_15_0)

	arg_15_0.page = arg_15_1

	arg_15_0.UpdateGetAllTip(arg_15_1)
	arg_15_0.UpdateLevel()

def var_0_0.UpdateLevel(arg_16_0):
	local var_16_0 = arg_16_0.ptActData.GetCurrLevel()

	arg_16_0.levelTxt.text = var_16_0

	local var_16_1 = 0
	local var_16_2 = 0

	if not arg_16_0.ptActData.IsMaxLevel():
		local var_16_3 = arg_16_0.ptActData.GetPtTarget(var_16_0)

		var_16_1, var_16_2 = arg_16_0.ptActData.count, arg_16_0.ptActData.GetNextLevelTarget()
		var_16_1 = var_16_1 - var_16_3
		var_16_2 = var_16_2 - var_16_3
		var_16_1 = math.min(var_16_1, var_16_2)
		arg_16_0.progressTxt.text = var_16_1 .. "/" .. var_16_2
	else
		var_16_1, var_16_2 = 1, 1
		arg_16_0.progressTxt.text = "MAX"

	setFillAmount(arg_16_0.progress, var_16_1 / var_16_2)

	local var_16_4 = arg_16_0.page == var_0_0.PAGE_PT

	setActive(arg_16_0.lastAwardItem, var_16_4)

	if var_16_4:
		arg_16_0.UpdateLastAward()

def var_0_0.UpdateLastAward(arg_17_0):
	local var_17_0 = arg_17_0.lastAwardItem.Find("award")
	local var_17_1 = arg_17_0.ptActData.GetLastAward()

	updateDrop(var_17_0, var_17_1)

	local var_17_2 = arg_17_0.ptActData.targets
	local var_17_3 = arg_17_0.ptActData.GetDroptItemState(#var_17_2)

	arg_17_0.lastAwardLvTxt.text = i18n("feast_task_pt_level", #var_17_2)

	setActive(arg_17_0.lastAwardItem.Find("lock"), var_17_3 == ActivityPtData.STATE_LOCK)
	setActive(arg_17_0.lastAwardItem.Find("get"), var_17_3 == ActivityPtData.STATE_CAN_GET)
	setActive(arg_17_0.lastAwardItem.Find("got"), var_17_3 == ActivityPtData.STATE_GOT)
	onButton(arg_17_0, var_17_0, function()
		if var_17_3 == ActivityPtData.STATE_CAN_GET:
			local var_18_0 = arg_17_0.ptActData.GetPtTarget(#var_17_2)

			arg_17_0.emit(FeastMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_17_0.ptActData.GetId(),
				arg1 = var_18_0
			})
		else
			arg_17_0.emit(BaseUI.ON_DROP, var_17_1), SFX_PANEL)

def var_0_0.Show(arg_19_0):
	var_0_0.super.Show(arg_19_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_19_0._tf)
	arg_19_0.GenPtData()
	arg_19_0.GenTaskData()
	triggerToggle(arg_19_0.toggles[var_0_0.PAGE_PT], True)

def var_0_0.GenPtData(arg_20_0):
	arg_20_0.ptActData = getProxy(FeastProxy).GetPtActData()
	arg_20_0.counts[var_0_0.PAGE_PT] = #arg_20_0.ptActData.targets

def var_0_0.GenTaskData(arg_21_0):
	arg_21_0.taskList = getProxy(FeastProxy).GetTaskList()

	local var_21_0 = getProxy(TaskProxy)

	table.sort(arg_21_0.taskList, function(arg_22_0, arg_22_1)
		local var_22_0 = var_21_0.getTaskById(arg_22_0) or var_21_0.getFinishTaskById(arg_22_0)
		local var_22_1 = var_21_0.getTaskById(arg_22_1) or var_21_0.getFinishTaskById(arg_22_1)
		local var_22_2 = var_22_0.isReceive() and 1 or 0
		local var_22_3 = var_22_1.isReceive() and 1 or 0

		if var_22_2 == var_22_3:
			local var_22_4 = var_22_0.IsActRoutineType() and 1 or 0
			local var_22_5 = var_22_1.IsActRoutineType() and 1 or 0

			if var_22_4 == var_22_5:
				return arg_22_0 < arg_22_1
			else
				return var_22_5 < var_22_4
		else
			return var_22_2 < var_22_3)

	arg_21_0.counts[var_0_0.PAGE_TASK] = #arg_21_0.taskList

def var_0_0.OnInitItem(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = arg_23_0.cardCls[arg_23_1].New(arg_23_2, arg_23_0)

	arg_23_0.cards[arg_23_1][arg_23_2] = var_23_0

def var_0_0.OnUpdateItem(arg_24_0, arg_24_1, arg_24_2, arg_24_3):
	local var_24_0 = arg_24_0.cards[arg_24_1][arg_24_3]

	if not var_24_0:
		arg_24_0.OnInitItem(arg_24_1, arg_24_3)

		var_24_0 = arg_24_0.cards[arg_24_1][arg_24_3]

	local var_24_1

	if arg_24_1 == var_0_0.PAGE_PT:
		var_24_1 = arg_24_0.ptActData
	elif arg_24_1 == var_0_0.PAGE_TASK:
		var_24_1 = arg_24_0.taskList[arg_24_2 + 1]

	var_24_0.Flush(var_24_1, arg_24_2 + 1)

def var_0_0.Hide(arg_25_0):
	var_0_0.super.Hide(arg_25_0)
	pg.UIMgr.GetInstance().UnblurPanel(arg_25_0._tf, arg_25_0._parentTf)

def var_0_0.OnDestroy(arg_26_0):
	if arg_26_0.isShowing():
		arg_26_0.Hide()

return var_0_0
