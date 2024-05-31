local var_0_0 = class("TaskScene", import("..base.BaseUI"))

var_0_0.PAGE_TYPE_SCENARIO = "scenario"
var_0_0.PAGE_TYPE_BRANCH = "branch"
var_0_0.PAGE_TYPE_ROUTINE = "routine"
var_0_0.PAGE_TYPE_WEEKLY = "weekly"
var_0_0.PAGE_TYPE_ALL = "all"
var_0_0.PAGE_TYPE_ACT = "activity"

local var_0_1 = {
	[var_0_0.PAGE_TYPE_SCENARIO] = {
		[1] = True
	},
	[var_0_0.PAGE_TYPE_BRANCH] = {
		None,
		True,
		None,
		None,
		True,
		True
	},
	[var_0_0.PAGE_TYPE_ROUTINE] = {
		[3] = True,
		[36] = True
	},
	[var_0_0.PAGE_TYPE_WEEKLY] = {
		[4] = True,
		[13] = True
	},
	[var_0_0.PAGE_TYPE_ALL] = {
		True,
		True,
		True,
		True,
		True,
		True,
		None,
		None,
		None,
		None,
		None,
		None,
		True,
		[36] = True,
		[26] = True
	},
	[var_0_0.PAGE_TYPE_ACT] = {
		[36] = True,
		[6] = True,
		[26] = True
	}
}

def var_0_0.getUIName(arg_1_0):
	return "TaskScene"

def var_0_0.setTaskVOs(arg_2_0, arg_2_1):
	arg_2_0.contextData.taskVOsById = arg_2_1

def var_0_0.SetWeekTaskProgressInfo(arg_3_0, arg_3_1):
	arg_3_0.contextData.weekTaskProgressInfo = arg_3_1

def var_0_0.init(arg_4_0):
	arg_4_0._topPanel = arg_4_0.findTF("blur_panel/adapt/top")
	arg_4_0._backBtn = arg_4_0._topPanel.Find("back_btn")
	arg_4_0._leftLength = arg_4_0.findTF("blur_panel/adapt/left_length")
	arg_4_0._tagRoot = arg_4_0.findTF("blur_panel/adapt/left_length/frame/tagRoot")
	arg_4_0.taskIconTpl = arg_4_0.findTF("taskTagOb/task_icon_default")
	arg_4_0.weekTip = arg_4_0.findTF("weekly/tip", arg_4_0._tagRoot)
	arg_4_0.oneStepBtn = arg_4_0.findTF("blur_panel/adapt/top/GetAllButton")
	arg_4_0.contextData.viewComponent = arg_4_0
	arg_4_0.pageTF = arg_4_0.findTF("pages")

def var_0_0.IsNewStyleTime():
	return pg.TimeMgr.GetInstance().parseTimeFromConfig({
		{
			2021,
			6,
			14
		},
		{
			0,
			0,
			0
		}
	}) <= pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.IsPassScenario():
	local var_6_0 = pg.gameset.task_first_daily_pre_id.key_value
	local var_6_1 = getProxy(TaskProxy).getData()
	local var_6_2 = _.select(_.values(var_6_1), function(arg_7_0)
		return arg_7_0.getConfig("type") == 1)

	if #var_6_2 > 0:
		table.sort(var_6_2, function(arg_8_0, arg_8_1)
			return arg_8_0.id < arg_8_1.id)

		return var_6_0 < var_6_2[1].id
	else
		return True

def var_0_0.didEnter(arg_9_0):
	local var_9_0 = TaskCommonPage.New(arg_9_0.pageTF, arg_9_0.event, arg_9_0.contextData)
	local var_9_1 = var_0_0.IsNewStyleTime() and not arg_9_0.contextData.weekTaskProgressInfo.IsMaximum() and TaskWeekPage.New(arg_9_0.pageTF, arg_9_0.event, arg_9_0.contextData) or var_9_0

	arg_9_0.emptyPage = TaskEmptyListPage.New(arg_9_0._tf, arg_9_0.event)
	arg_9_0.pages = {
		[var_0_0.PAGE_TYPE_SCENARIO] = var_9_0,
		[var_0_0.PAGE_TYPE_BRANCH] = var_9_0,
		[var_0_0.PAGE_TYPE_ROUTINE] = var_9_0,
		[var_0_0.PAGE_TYPE_WEEKLY] = var_9_1,
		[var_0_0.PAGE_TYPE_ALL] = var_9_0,
		[var_0_0.PAGE_TYPE_ACT] = var_9_0
	}
	arg_9_0.contextData.ptAwardWindow = TaskPtAwardPage.New(arg_9_0._tf, arg_9_0.event, arg_9_0.contextData)

	onButton(arg_9_0, arg_9_0._backBtn, function()
		arg_9_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	setActive(arg_9_0.findTF("stamp"), getProxy(TaskProxy).mingshiTouchFlagEnabled())

	if LOCK_CLICK_MINGSHI:
		setActive(arg_9_0.findTF("stamp"), False)

	onButton(arg_9_0, arg_9_0.findTF("stamp"), function()
		getProxy(TaskProxy).dealMingshiTouchFlag(5), SFX_CONFIRM)

	arg_9_0.toggles = {}

	for iter_9_0, iter_9_1 in pairs(var_0_1):
		local var_9_2 = arg_9_0.findTF(iter_9_0, arg_9_0._tagRoot)

		onToggle(arg_9_0, var_9_2, function(arg_12_0)
			if arg_12_0:
				arg_9_0.UpdatePage(iter_9_0), SFX_PANEL)

		arg_9_0.toggles[iter_9_0] = var_9_2

	local var_9_3 = arg_9_0.toggles[arg_9_0.contextData.page or var_0_0.PAGE_TYPE_ALL]

	if arg_9_0.toggles and var_9_3:
		triggerToggle(var_9_3, True)

	arg_9_0.UpdateWeekTip()

def var_0_0.refreshPage(arg_13_0):
	arg_13_0.UpdatePage(arg_13_0._currentToggleType)

def var_0_0.UpdatePage(arg_14_0, arg_14_1):
	local var_14_0 = var_0_1[arg_14_1]

	local function var_14_1(arg_15_0, arg_15_1)
		if #arg_15_1 <= 0:
			arg_14_0.emptyPage.ExecuteAction("ShowOrHide", True)
		elif #arg_15_1 > 0 and arg_14_0.emptyPage.GetLoaded():
			arg_14_0.emptyPage.ExecuteAction("ShowOrHide", False)

		arg_14_0.updateOneStepBtn(arg_15_0)

	if arg_14_0._currentToggleType and arg_14_0._currentToggleType != arg_14_1:
		arg_14_0.pages[arg_14_0._currentToggleType].ExecuteAction("Hide")

	local var_14_2 = arg_14_0.pages[arg_14_1]

	var_14_2.ExecuteAction("Update", arg_14_1, var_14_0, function(arg_16_0)
		var_14_1(var_14_2, arg_16_0))

	arg_14_0._currentToggleType = arg_14_1
	arg_14_0.contextData.page = arg_14_1

def var_0_0.addTask(arg_17_0, arg_17_1):
	print("add task " .. arg_17_1.id)

	arg_17_0.contextData.taskVOsById[arg_17_1.id] = arg_17_1

	arg_17_0.UpdatePage(arg_17_0._currentToggleType)

def var_0_0.removeTask(arg_18_0, arg_18_1):
	print("revemo task " .. arg_18_1.id)

	arg_18_0.contextData.taskVOsById[arg_18_1.id] = None

	arg_18_0.UpdatePage(arg_18_0._currentToggleType)

def var_0_0.updateTask(arg_19_0, arg_19_1):
	arg_19_0.addTask(arg_19_1)

def var_0_0.ResetWeekTaskPage(arg_20_0):
	local var_20_0 = arg_20_0.pages[var_0_0.PAGE_TYPE_WEEKLY]

	if var_0_0.IsNewStyleTime() and isa(var_20_0, TaskCommonPage):
		if var_20_0.GetLoaded() and var_20_0.isShowing():
			var_20_0.Hide()

		local var_20_1 = TaskWeekPage.New(arg_20_0.pageTF, arg_20_0.event, arg_20_0.contextData)

		arg_20_0.pages[var_0_0.PAGE_TYPE_WEEKLY] = var_20_1

	arg_20_0.RefreshWeekTaskPage()

	if arg_20_0._currentToggleType != var_0_0.PAGE_TYPE_WEEKLY:
		arg_20_0.UpdatePage(arg_20_0._currentToggleType)

def var_0_0.RefreshWeekTaskPage(arg_21_0):
	if arg_21_0._currentToggleType == var_0_0.PAGE_TYPE_WEEKLY:
		arg_21_0.UpdatePage(arg_21_0._currentToggleType)
		arg_21_0.UpdateWeekTip()

def var_0_0.RefreshWeekTaskPageBefore(arg_22_0, arg_22_1):
	if arg_22_0._currentToggleType == var_0_0.PAGE_TYPE_WEEKLY:
		arg_22_0.pages[arg_22_0._currentToggleType].RefreshWeekTaskPageBefore(arg_22_1)

def var_0_0.RefreshWeekTaskProgress(arg_23_0):
	local var_23_0 = arg_23_0.pages[arg_23_0._currentToggleType]

	if isa(var_23_0, TaskWeekPage) and arg_23_0.contextData.weekTaskProgressInfo.IsMaximum():
		var_23_0.Destroy()

		arg_23_0.pages[var_0_0.PAGE_TYPE_WEEKLY] = arg_23_0.pages[var_0_0.PAGE_TYPE_SCENARIO]

		arg_23_0.UpdatePage(var_0_0.PAGE_TYPE_WEEKLY)
	elif arg_23_0._currentToggleType == var_0_0.PAGE_TYPE_WEEKLY and isa(var_23_0, TaskWeekPage):
		var_23_0.ExecuteAction("RefreshWeekProgress")
		arg_23_0.UpdateWeekTip()

def var_0_0.UpdateWeekTip(arg_24_0):
	local var_24_0 = False

	if var_0_0.IsPassScenario() and var_0_0.IsNewStyleTime():
		for iter_24_0, iter_24_1 in pairs(arg_24_0.contextData.taskVOsById):
			if (iter_24_1.getConfig("type") == 4 or iter_24_1.getConfig("type") == 13) and iter_24_1.isFinish() and not iter_24_1.isReceive() and iter_24_1.ShowOnTaskScene():
				var_24_0 = True

				break

		if not var_24_0:
			local var_24_1 = arg_24_0.contextData.weekTaskProgressInfo

			if var_24_1.CanUpgrade() or var_24_1.AnySubTaskCanSubmit():
				var_24_0 = True

	setActive(arg_24_0.weekTip, var_24_0)

def var_0_0.GoToFilter(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.findTF(arg_25_1, arg_25_0._tagRoot)

	triggerToggle(var_25_0, True)

def var_0_0.onSubmit(arg_26_0, arg_26_1):
	if arg_26_0.onShowAwards:
		return

	arg_26_0.emit(TaskMediator.ON_TASK_SUBMIT, arg_26_1)

def var_0_0.onSubmitForWeek(arg_27_0, arg_27_1):
	if arg_27_0.onShowAwards:
		return

	arg_27_0.emit(TaskMediator.ON_SUBMIT_WEEK_TASK, arg_27_1)

def var_0_0.onSubmitForAvatar(arg_28_0, arg_28_1):
	if arg_28_0.onShowAwards:
		return

	arg_28_0.emit(TaskMediator.ON_SUBMIT_AVATAR_TASK, arg_28_1)

def var_0_0.onGo(arg_29_0, arg_29_1):
	if arg_29_0.onShowAwards:
		return

	if isa(arg_29_1, AvatarFrameTask) and arg_29_1.IsActEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	arg_29_0.emit(TaskMediator.ON_TASK_GO, arg_29_1)

def var_0_0.willExit(arg_30_0):
	for iter_30_0, iter_30_1 in pairs(arg_30_0.pages):
		iter_30_1.Destroy()

	if arg_30_0.emptyPage:
		arg_30_0.emptyPage.Destroy()

		arg_30_0.emptyPage = None

	arg_30_0.pages = None

	arg_30_0.contextData.ptAwardWindow.Destroy()

	arg_30_0.contextData.ptAwardWindow = None
	arg_30_0.contextData.taskVOsById = None
	arg_30_0.contextData.weekTaskProgressInfo = None
	arg_30_0.contextData.viewComponent = None

def var_0_0.updateOneStepBtn(arg_31_0, arg_31_1):
	arg_31_1 = arg_31_1 or arg_31_0.pages[arg_31_0._currentToggleType]

	local var_31_0 = #arg_31_1.GetWaitToCheckList() >= 2

	if var_31_0:
		onButton(arg_31_0, arg_31_0.oneStepBtn, function()
			arg_31_1.ExecuteOneStepSubmit(), SFX_PANEL)
	else
		removeOnButton(arg_31_0.oneStepBtn)

	setActive(arg_31_0.oneStepBtn, var_31_0)

return var_0_0
