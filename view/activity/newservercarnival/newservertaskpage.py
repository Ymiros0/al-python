local var_0_0 = class("NewServerTaskPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "NewServerTaskPage"

var_0_0.TYPE_ALL = 1
var_0_0.TYPE_DAILY = 2
var_0_0.TYPE_TARGET = 3
var_0_0.TXT_DESC = 1
var_0_0.TXT_CURRENT_NUM = 2
var_0_0.TXT_TARGET_NUM = 3

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.addListener()
	arg_2_0.onUpdateTask()

def var_0_0.initData(arg_3_0):
	arg_3_0.activity = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_TASK)
	arg_3_0.taskGroupList = arg_3_0.activity.getConfig("config_data")
	arg_3_0.taskProxy = getProxy(TaskProxy)
	arg_3_0.page = var_0_0.TYPE_ALL

def var_0_0.initUI(arg_4_0):
	arg_4_0.getAllBtn = arg_4_0.findTF("get_all")
	arg_4_0.extendTpl = arg_4_0.findTF("extend_tpl")
	arg_4_0.typeToggles = {
		arg_4_0.findTF("types/all"),
		arg_4_0.findTF("types/daily"),
		arg_4_0.findTF("types/target")
	}
	arg_4_0.content = arg_4_0.findTF("view/content")
	arg_4_0.taskGroupItemList = UIItemList.New(arg_4_0.content, arg_4_0.findTF("tpl", arg_4_0.content))

def var_0_0.addListener(arg_5_0):
	onButton(arg_5_0, arg_5_0.getAllBtn, function()
		arg_5_0.emit(NewServerCarnivalMediator.TASK_SUBMIT_ONESTEP, arg_5_0.finishVOList), SFX_PANEL)
	arg_5_0.taskGroupItemList.make(function(arg_7_0, arg_7_1, arg_7_2)
		arg_7_1 = arg_7_1 + 1

		if arg_7_0 == UIItemList.EventUpdate:
			arg_5_0.updateTaskGroup(arg_7_2, arg_7_1))

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.typeToggles):
		onToggle(arg_5_0, iter_5_1, function(arg_8_0)
			if arg_8_0:
				if iter_5_0 == var_0_0.TYPE_ALL:
					arg_5_0.filterAll()
				elif iter_5_0 == var_0_0.TYPE_DAILY:
					arg_5_0.filterDaily()
				elif iter_5_0 == var_0_0.TYPE_TARGET:
					arg_5_0.filterTarget()

				arg_5_0.page = iter_5_0

			arg_5_0.updataTaskList())

def var_0_0.updateTaskGroup(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = arg_9_0.showVOGroup[arg_9_2]
	local var_9_1 = arg_9_1.Find("info")
	local var_9_2 = {}

	for iter_9_0, iter_9_1 in ipairs(var_9_0):
		if not iter_9_1.isReceive():
			table.insert(var_9_2, iter_9_1)

	triggerToggle(var_9_1, False)

	local var_9_3 = #var_9_2 > 0 and table.remove(var_9_2, 1) or var_9_0[#var_9_0]

	SetCompomentEnabled(var_9_1, typeof(Toggle), #var_9_2 > 0)
	arg_9_0.updateTaskDisplay(var_9_1, var_9_3)
	setActive(var_9_1.Find("toggle_mark"), #var_9_2 > 0)

	local var_9_4 = var_9_3.getTaskStatus()

	GetOrAddComponent(arg_9_1, typeof(CanvasGroup)).alpha = var_9_4 == 2 and 0.5 or 1

	setActive(var_9_1.Find("mask"), var_9_4 == 2)
	setActive(var_9_1.Find("bg/receive"), var_9_4 == 1)
	setActive(var_9_1.Find("tag/tag_daily"), var_9_3.getConfig("type") == Task.TYPE_ACTIVITY_ROUTINE)
	setActive(var_9_1.Find("tag/tag_target"), var_9_3.getConfig("type") != Task.TYPE_ACTIVITY_ROUTINE)
	onToggle(arg_9_0, var_9_1, function(arg_10_0)
		if arg_10_0:
			local var_10_0 = arg_9_1.Find("content")
			local var_10_1 = UIItemList.New(var_10_0, arg_9_0.extendTpl)

			var_10_1.make(function(arg_11_0, arg_11_1, arg_11_2)
				arg_11_1 = arg_11_1 + 1

				if arg_11_0 == UIItemList.EventUpdate:
					arg_9_0.updateTaskDisplay(arg_11_2, var_9_2[arg_11_1]))
			var_10_1.align(#var_9_2)
			scrollTo(arg_9_0.content, 0, 1 - (arg_9_2 - 1) / (#arg_9_0.showVOGroup + #var_9_2 - 4))
		else
			removeAllChildren(arg_9_1.Find("content")))

def var_0_0.updateTaskDisplay(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = arg_12_2.getProgress()
	local var_12_1 = arg_12_2.getConfig("target_num")

	setSlider(arg_12_1.Find("Slider"), 0, var_12_1, var_12_0)

	local var_12_2 = arg_12_2.getConfig("award_display")[1]
	local var_12_3 = {
		type = var_12_2[1],
		id = var_12_2[2],
		count = var_12_2[3]
	}

	updateDrop(arg_12_1.Find("IconTpl"), var_12_3)
	onButton(arg_12_0, arg_12_1.Find("IconTpl"), function()
		arg_12_0.emit(BaseUI.ON_DROP, var_12_3), SFX_PANEL)

	local var_12_4 = arg_12_2.getTaskStatus()

	setActive(arg_12_1.Find("go"), var_12_4 == 0)
	setActive(arg_12_1.Find("get"), var_12_4 == 1)
	setActive(arg_12_1.Find("got"), var_12_4 == 2)
	setText(arg_12_1.Find("desc"), setColorStr(arg_12_2.getConfig("desc"), arg_12_0.getColor(var_0_0.TXT_DESC, var_12_4)))
	setText(arg_12_1.Find("Slider/Text"), setColorStr(var_12_0, arg_12_0.getColor(var_0_0.TXT_CURRENT_NUM, var_12_4)) .. setColorStr("/" .. var_12_1, arg_12_0.getColor(var_0_0.TXT_TARGET_NUM, var_12_4)))
	onButton(arg_12_0, arg_12_1.Find("go"), function()
		arg_12_0.emit(NewServerCarnivalMediator.TASK_GO, arg_12_2), SFX_PANEL)
	onButton(arg_12_0, arg_12_1.Find("get"), function()
		arg_12_0.emit(NewServerCarnivalMediator.TASK_SUBMIT, arg_12_2), SFX_CONFIRM)

def var_0_0.getColor(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_1 == var_0_0.TXT_DESC:
		return arg_16_2 == 1 and "#63573c" or "#a1976e"
	elif arg_16_1 == var_0_0.TXT_CURRENT_NUM:
		return arg_16_2 == 1 and "#219215" or "#65D559"
	elif arg_16_1 == var_0_0.TXT_TARGET_NUM:
		return arg_16_2 == 1 and "#5c4212" or "#ae9363"

def var_0_0.filterAll(arg_17_0):
	arg_17_0.taskVOGroup = underscore.map(arg_17_0.taskGroupList, function(arg_18_0)
		return underscore.map(arg_18_0, function(arg_19_0)
			assert(arg_17_0.taskProxy.getTaskVO(arg_19_0), "without this task." .. arg_19_0)

			return arg_17_0.taskProxy.getTaskVO(arg_19_0)))
	arg_17_0.showVOGroup = arg_17_0.taskVOGroup

def var_0_0.filterDaily(arg_20_0):
	arg_20_0.taskVOGroup = underscore.map(arg_20_0.taskGroupList, function(arg_21_0)
		return underscore.map(arg_21_0, function(arg_22_0)
			assert(arg_20_0.taskProxy.getTaskVO(arg_22_0), "without this task." .. arg_22_0)

			return arg_20_0.taskProxy.getTaskVO(arg_22_0)))
	arg_20_0.showVOGroup = {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.taskVOGroup):
		if iter_20_1[1].getConfig("type") == Task.TYPE_ACTIVITY_ROUTINE:
			table.insert(arg_20_0.showVOGroup, iter_20_1)

def var_0_0.filterTarget(arg_23_0):
	arg_23_0.taskVOGroup = underscore.map(arg_23_0.taskGroupList, function(arg_24_0)
		return underscore.map(arg_24_0, function(arg_25_0)
			assert(arg_23_0.taskProxy.getTaskVO(arg_25_0), "without this task." .. arg_25_0)

			return arg_23_0.taskProxy.getTaskVO(arg_25_0)))
	arg_23_0.showVOGroup = {}

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.taskVOGroup):
		if iter_23_1[1].getConfig("type") != Task.TYPE_ACTIVITY_ROUTINE:
			table.insert(arg_23_0.showVOGroup, iter_23_1)

def var_0_0.updataTaskList(arg_26_0):
	table.sort(arg_26_0.showVOGroup, CompareFuncs({
		function(arg_27_0)
			for iter_27_0, iter_27_1 in ipairs(arg_27_0):
				if iter_27_1.getTaskStatus() == 1:
					return 0

			return underscore.all(arg_27_0, function(arg_28_0)
				return arg_28_0.isReceive()) and 2 or 1,
		function(arg_29_0)
			return arg_29_0[1].getConfig("type") != Task.TYPE_ACTIVITY_ROUTINE and 1 or 0,
		function(arg_30_0)
			return arg_30_0[1].id
	}))
	arg_26_0.taskGroupItemList.align(#arg_26_0.showVOGroup)

def var_0_0.onUpdateTask(arg_31_0):
	triggerToggle(arg_31_0.typeToggles[arg_31_0.page], True)
	arg_31_0.updataGetAllBtn()

def var_0_0.updataGetAllBtn(arg_32_0):
	arg_32_0.finishVOList = {}

	for iter_32_0, iter_32_1 in ipairs(arg_32_0.taskVOGroup):
		for iter_32_2, iter_32_3 in ipairs(iter_32_1):
			if iter_32_3.getTaskStatus() == 1:
				table.insert(arg_32_0.finishVOList, iter_32_3)

	setActive(arg_32_0.getAllBtn, #arg_32_0.finishVOList > 0)

def var_0_0.isTip(arg_33_0):
	if arg_33_0.finishVOList:
		return #arg_33_0.finishVOList > 0
	else
		local var_33_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_NEWSERVER_TASK)

		if var_33_0 and not var_33_0.isEnd():
			local var_33_1 = getProxy(TaskProxy)
			local var_33_2 = var_33_0.getConfig("config_data")

			for iter_33_0, iter_33_1 in ipairs(var_33_2):
				for iter_33_2, iter_33_3 in ipairs(iter_33_1):
					assert(var_33_1.getTaskVO(iter_33_3), "without this task." .. iter_33_3)

					if var_33_1.getTaskVO(iter_33_3).getTaskStatus() == 1:
						return True

		return False

def var_0_0.OnDestroy(arg_34_0):
	return

return var_0_0
