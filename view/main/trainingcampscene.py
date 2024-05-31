local var_0_0 = class("TrainingCampScene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "TrainingCampUI"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.initData()
	arg_2_0.addListener()

	if var_0_0.isNormalActOn():
		arg_2_0.initNormalPanel()

	if var_0_0.isTecActOn():
		arg_2_0.initTecPanel()

	arg_2_0.closeMsgBox()

def var_0_0.findUI(arg_3_0):
	arg_3_0.adaptPanel = arg_3_0.findTF("blur_panel/adapt")
	arg_3_0.panelContainer = arg_3_0.findTF("PanelContainer")
	arg_3_0.normalPanel = arg_3_0.findTF("NormalPanel", arg_3_0.panelContainer)
	arg_3_0.tecPanel = arg_3_0.findTF("TecPanel", arg_3_0.panelContainer)
	arg_3_0.switchToNormalBtn = arg_3_0.findTF("SwitchToNormal")
	arg_3_0.switchToTecBtn = arg_3_0.findTF("SwitchToTec")
	arg_3_0.switchToNormalLight = GetOrAddComponent(arg_3_0.findTF("Light", arg_3_0.switchToNormalBtn), "Animator")
	arg_3_0.switchToTecLight = GetOrAddComponent(arg_3_0.findTF("Light", arg_3_0.switchToTecBtn), "Animator")
	arg_3_0.awardMsg = arg_3_0.findTF("ChooseAwardPanel")
	arg_3_0.helpBtn = arg_3_0.findTF("HelpBtn")
	arg_3_0.titleTf = arg_3_0.findTF("blur_panel/adapt/top/title")

	GetComponent(findTF(arg_3_0.titleTf, "img"), typeof(Image)).SetNativeSize()

def var_0_0.initData(arg_4_0):
	arg_4_0.taskProxy = getProxy(TaskProxy)
	arg_4_0.activityProxy = getProxy(ActivityProxy)
	arg_4_0.normalTaskactivity = arg_4_0.activityProxy.getActivityByType(ActivityConst.ACTIVITY_TYPE_GUIDE_TASKS)
	arg_4_0.tecTaskActivity = arg_4_0.activityProxy.getActivityByType(ActivityConst.ACTIVITY_TYPE_FRESH_TEC_CATCHUP)
	arg_4_0.phaseId = None
	arg_4_0.cachePageID = None
	arg_4_0.activity = None

def var_0_0.addListener(arg_5_0):
	onButton(arg_5_0, arg_5_0.findTF("top/back_button", arg_5_0.adaptPanel), function()
		arg_5_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.switchToNormalBtn, function()
		if not arg_5_0.isOnSwitchAni and var_0_0.isNormalActOn():
			arg_5_0.switchPanel(arg_5_0.normalTaskactivity, True)
			setActive(arg_5_0.switchToNormalBtn, False)
			setActive(arg_5_0.switchToTecBtn, True)
			arg_5_0.resetSwitchBtnsLight(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.switchToTecBtn, function()
		if not arg_5_0.isOnSwitchAni and var_0_0.isTecActOn():
			arg_5_0.switchPanel(arg_5_0.tecTaskActivity, True)
			setActive(arg_5_0.switchToNormalBtn, True)
			setActive(arg_5_0.switchToTecBtn, False)
			arg_5_0.resetSwitchBtnsLight(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("newplayer_help_tip")
		}), SFX_PANEL)

def var_0_0.didEnter(arg_10_0):
	arg_10_0.updateSwitchBtns()
	arg_10_0.updateSwitchBtnsTag()
	arg_10_0.autoSelectPanel()

def var_0_0.willExit(arg_11_0):
	LeanTween.cancel(go(arg_11_0.normalPanel))
	LeanTween.cancel(go(arg_11_0.tecPanel))

def var_0_0.updateSwitchBtns(arg_12_0):
	local var_12_0, var_12_1 = TrainingCampScene.isNormalActOn()
	local var_12_2, var_12_3 = TrainingCampScene.isTecActOn()

	if not var_12_0 or not var_12_2:
		setActive(arg_12_0.switchToNormalBtn, False)
		setActive(arg_12_0.switchToTecBtn, False)
	elif var_12_0 and var_12_2:
		setActive(arg_12_0.switchToNormalBtn, True)
		setActive(arg_12_0.switchToTecBtn, True)

	local var_12_4 = arg_12_0.findTF("Tag", arg_12_0.switchToNormalBtn)
	local var_12_5 = arg_12_0.findTF("Tag", arg_12_0.switchToTecBtn)

	setActive(var_12_4, var_12_1)
	setActive(var_12_5, var_12_3)

def var_0_0.updateSwitchBtnsTag(arg_13_0):
	local var_13_0, var_13_1 = TrainingCampScene.isNormalActOn()
	local var_13_2, var_13_3 = TrainingCampScene.isTecActOn()
	local var_13_4 = arg_13_0.findTF("Tag", arg_13_0.switchToNormalBtn)
	local var_13_5 = arg_13_0.findTF("Tag", arg_13_0.switchToTecBtn)

	setActive(var_13_4, var_13_1)
	setActive(var_13_5, var_13_3)

	local var_13_6 = PlayerPrefs.GetInt("TrainCamp_Tec_Catchup_First_Tag", 0)

	arg_13_0.switchToNormalLight.enabled = var_13_6 == 0
	arg_13_0.switchToTecLight.enabled = var_13_6 == 0

	if var_13_6 == 0:
		PlayerPrefs.SetInt("TrainCamp_Tec_Catchup_First_Tag", 1)

def var_0_0.resetSwitchBtnsLight(arg_14_0):
	arg_14_0.switchToNormalLight.enabled = False
	arg_14_0.switchToTecLight.enabled = False

def var_0_0.autoSelectPanel(arg_15_0):
	local var_15_0, var_15_1 = TrainingCampScene.isNormalActOn()
	local var_15_2, var_15_3 = TrainingCampScene.isTecActOn()

	if var_15_0 and var_15_2:
		arg_15_0.switchPanel(arg_15_0.normalTaskactivity)
		setActive(arg_15_0.switchToNormalBtn, False)
		setActive(arg_15_0.switchToTecBtn, True)
	elif var_15_0:
		arg_15_0.switchPanel(arg_15_0.normalTaskactivity)
	elif var_15_2:
		arg_15_0.switchPanel(arg_15_0.tecTaskActivity)

def var_0_0.initNormalPanel(arg_16_0):
	local var_16_0 = arg_16_0.findTF("ToggleList", arg_16_0.normalPanel)

	arg_16_0.normalToggles = {
		arg_16_0.findTF("Phase1", var_16_0),
		arg_16_0.findTF("Phase2", var_16_0),
		arg_16_0.findTF("Phase3", var_16_0)
	}
	arg_16_0.normalTaskUIItemList = UIItemList.New(arg_16_0.findTF("ScrollRect/Content", arg_16_0.normalPanel), arg_16_0.findTF("ScrollRect/TaskTpl", arg_16_0.normalPanel))
	arg_16_0.normalProgressPanel = arg_16_0.findTF("ProgressPanel", arg_16_0.normalPanel)

	for iter_16_0, iter_16_1 in pairs(arg_16_0.normalToggles):
		onToggle(arg_16_0, iter_16_1, function(arg_17_0)
			if arg_17_0:
				if arg_16_0.phaseId < iter_16_0:
					pg.TipsMgr.GetInstance().ShowTips(i18n("newplayer_notice_7"))
					triggerToggle(arg_16_0.normalToggles[arg_16_0.cachePageID], True)
				else
					arg_16_0.updateNormalPanel(iter_16_0), SFX_PANEL)

def var_0_0.updateNormalPanel(arg_18_0, arg_18_1):
	arg_18_0.cachePageID = arg_18_1

	local var_18_0 = arg_18_0.normalTaskactivity.getConfig("config_data")[3]
	local var_18_1 = var_18_0[arg_18_1][1]
	local var_18_2 = var_18_0[arg_18_1][2]

	arg_18_0.sortTaskIDList(var_18_1)
	arg_18_0.updateTaskUIItemList(arg_18_0.normalTaskUIItemList, var_18_1, arg_18_1)
	arg_18_0.updateNormalProgressPanel(arg_18_1, var_18_2, var_18_1)

def var_0_0.updateNormalProgressPanel(arg_19_0, arg_19_1, arg_19_2, arg_19_3):
	local var_19_0 = arg_19_0.getTask(arg_19_1, arg_19_2)

	if arg_19_1 == arg_19_0.phaseId and arg_19_0.isMissTask(arg_19_3):
		arg_19_0.emit(TrainingCampMediator.ON_TRIGGER, {
			cmd = 1,
			activity_id = arg_19_0.activity.id
		})

	if var_19_0 and var_19_0.isClientTrigger() and not var_19_0.isFinish():
		arg_19_0.emit(TrainingCampMediator.ON_UPDATE, var_19_0)

	local var_19_1 = arg_19_0.normalProgressPanel.Find("Get")
	local var_19_2 = arg_19_0.normalProgressPanel.Find("Lock")
	local var_19_3 = arg_19_0.normalProgressPanel.Find("Go")
	local var_19_4 = arg_19_0.normalProgressPanel.Find("Pass")

	setActive(var_19_1, var_19_0 and var_19_0.isFinish() and not var_19_0.isReceive())
	setActive(var_19_2, not var_19_0)
	setActive(var_19_3, var_19_0 and not var_19_0.isFinish())
	setActive(var_19_4, var_19_0 and var_19_0.isReceive())

	local var_19_5 = arg_19_0.normalProgressPanel.Find("Slider/LabelText")
	local var_19_6 = arg_19_0.normalProgressPanel.Find("Slider/ProgressText")

	if not var_19_0:
		var_19_0 = Task.New({
			id = arg_19_2
		})

		if arg_19_0.isFinishedAll(arg_19_3):
			arg_19_0.emit(TrainingCampMediator.ON_TRIGGER, {
				cmd = 2,
				activity_id = arg_19_0.activity.id
			})

		setText(var_19_5, i18n("newplayer_notice_" .. arg_19_1))

		local var_19_7 = 0

		_.each(arg_19_3, function(arg_20_0)
			if arg_19_0.taskProxy.getFinishTaskById(arg_20_0) != None:
				var_19_7 = var_19_7 + 1)
		setText(var_19_6, var_19_7 .. "/" .. #arg_19_3)
	else
		setText(var_19_5, var_19_0.getConfig("desc"))
		setText(var_19_6, math.min(var_19_0.progress, var_19_0.getConfig("target_num")) .. "/" .. var_19_0.getConfig("target_num"))

	arg_19_0.normalProgressPanel.Find("Slider").GetComponent(typeof(Slider)).value = var_19_0.progress / var_19_0.getConfig("target_num")
	arg_19_0.normalProgressPanel.Find("Icon").GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/trainingcampui_atlas", "panel_phase_award_" .. arg_19_1)

	setText(arg_19_0.normalProgressPanel.Find("TipText"), i18n("newplayer_notice_" .. 3 + arg_19_1))
	onButton(arg_19_0, var_19_1, function()
		if var_19_0.isSelectable():
			arg_19_0.openMsgbox(function(arg_22_0)
				arg_19_0.emit(TrainingCampMediator.ON_SELECTABLE_GET, var_19_0, arg_22_0))
		else
			arg_19_0.emit(TrainingCampMediator.ON_GET, var_19_0), SFX_PANEL)
	onButton(arg_19_0, var_19_3, function()
		arg_19_0.emit(TrainingCampMediator.ON_GO, var_19_0), SFX_PANEL)

def var_0_0.initTecPanel(arg_24_0):
	local var_24_0 = #arg_24_0.tecTaskActivity.getConfig("config_data")[3]
	local var_24_1 = arg_24_0.findTF("ToggleList", arg_24_0.tecPanel)

	arg_24_0.tecToggles = {
		arg_24_0.findTF("Phase1", var_24_1)
	}

	for iter_24_0 = #arg_24_0.tecToggles + 1, var_24_0:
		local var_24_2 = cloneTplTo(arg_24_0.tecToggles[1], var_24_1)

		table.insert(arg_24_0.tecToggles, var_24_2)

		var_24_2.name = "Phase" .. iter_24_0

	for iter_24_1 = 1, var_24_0:
		local var_24_3 = var_24_1.GetChild(iter_24_1 - 1)
		local var_24_4 = arg_24_0.findTF("TextImg", var_24_3)

		setText(var_24_4, i18n("tec_catchup_" .. iter_24_1))

		local var_24_5 = arg_24_0.findTF("Selected/TextImage", var_24_3)

		setText(var_24_5, i18n("tec_catchup_" .. iter_24_1))

	arg_24_0.tecTaskUIItemList = UIItemList.New(arg_24_0.findTF("ScrollRect/Content", arg_24_0.tecPanel), arg_24_0.findTF("ScrollRect/TaskTpl", arg_24_0.tecPanel))
	arg_24_0.tecProgressPanel = arg_24_0.findTF("ProgressPanel", arg_24_0.tecPanel)

	for iter_24_2, iter_24_3 in pairs(arg_24_0.tecToggles):
		onToggle(arg_24_0, iter_24_3, function(arg_25_0)
			if arg_25_0:
				if arg_24_0.phaseId < iter_24_2:
					pg.TipsMgr.GetInstance().ShowTips(i18n("tec_notice_not_open_tip"))
					triggerToggle(arg_24_0.tecToggles[arg_24_0.cachePageID], True)
				else
					arg_24_0.updateTecPanel(iter_24_2), SFX_PANEL)

def var_0_0.updateTecPanel(arg_26_0, arg_26_1):
	arg_26_0.cachePageID = arg_26_1

	local var_26_0 = arg_26_0.tecTaskActivity.getConfig("config_data")[3]
	local var_26_1 = var_26_0[arg_26_1][1]
	local var_26_2 = var_26_0[arg_26_1][2]

	arg_26_0.sortTaskIDList(var_26_1)
	arg_26_0.updateTaskUIItemList(arg_26_0.tecTaskUIItemList, var_26_1, arg_26_1)
	arg_26_0.updateTecProgressPanel(arg_26_1, var_26_2, var_26_1)

def var_0_0.updateTecProgressPanel(arg_27_0, arg_27_1, arg_27_2, arg_27_3):
	local var_27_0 = arg_27_0.isFinishedAll(arg_27_3)
	local var_27_1

	if not var_27_0:
		var_27_1 = True

	local var_27_2 = arg_27_0.getTask(arg_27_1, arg_27_2, var_27_1)

	if arg_27_1 == arg_27_0.phaseId and arg_27_0.isMissTask(arg_27_3):
		arg_27_0.emit(TrainingCampMediator.ON_TRIGGER, {
			cmd = 1,
			activity_id = arg_27_0.activity.id
		})

	if var_27_2 and var_27_2.isClientTrigger() and not var_27_2.isFinish():
		arg_27_0.emit(TrainingCampMediator.ON_UPDATE, var_27_2)

	local var_27_3 = arg_27_0.tecProgressPanel.Find("Get")
	local var_27_4 = arg_27_0.tecProgressPanel.Find("Lock")
	local var_27_5 = arg_27_0.tecProgressPanel.Find("Go")
	local var_27_6 = arg_27_0.tecProgressPanel.Find("Pass")

	setActive(var_27_3, var_27_2 and var_27_2.isFinish() and not var_27_2.isReceive())
	setActive(var_27_4, not var_27_2)
	setActive(var_27_5, var_27_2 and not var_27_2.isFinish())
	setActive(var_27_6, var_27_2 and var_27_2.isReceive())

	local var_27_7 = arg_27_0.tecProgressPanel.Find("Slider/LabelText")
	local var_27_8 = arg_27_0.tecProgressPanel.Find("Slider/ProgressText")

	if not var_27_2:
		var_27_2 = Task.New({
			id = arg_27_2
		})

		if arg_27_0.isFinishedAll(arg_27_3):
			arg_27_0.emit(TrainingCampMediator.ON_TRIGGER, {
				cmd = 2,
				activity_id = arg_27_0.activity.id
			})

		setText(var_27_7, i18n("tec_notice", i18n("tec_catchup_" .. arg_27_1)))

		local var_27_9 = 0

		_.each(arg_27_3, function(arg_28_0)
			local var_28_0 = arg_27_0.taskProxy.getTaskVO(arg_28_0)

			if var_28_0 and var_28_0.isReceive():
				var_27_9 = var_27_9 + 1)
		setText(var_27_8, var_27_9 .. "/" .. #arg_27_3)
	else
		setText(var_27_7, var_27_2.getConfig("desc"))
		setText(var_27_8, math.min(var_27_2.progress, var_27_2.getConfig("target_num")) .. "/" .. var_27_2.getConfig("target_num"))

	arg_27_0.tecProgressPanel.Find("Slider").GetComponent(typeof(Slider)).value = var_27_2.progress / var_27_2.getConfig("target_num")

	local var_27_10 = arg_27_0.tecProgressPanel.Find("Icon/Item")
	local var_27_11 = var_27_2.getConfig("award_display")[1]
	local var_27_12 = {
		type = var_27_11[1],
		id = var_27_11[2],
		count = var_27_11[3]
	}

	updateDrop(var_27_10, var_27_12)
	onButton(arg_27_0, var_27_10, function()
		arg_27_0.emit(BaseUI.ON_DROP, var_27_12), SFX_PANEL)
	setActive(arg_27_0.tecProgressPanel.Find("TipText"), False)
	onButton(arg_27_0, var_27_3, function()
		if var_27_2.isSelectable():
			arg_27_0.openMsgbox(function(arg_31_0)
				arg_27_0.emit(TrainingCampMediator.ON_SELECTABLE_GET, var_27_2, arg_31_0))
		else
			arg_27_0.emit(TrainingCampMediator.ON_GET, var_27_2)

			if arg_27_0.phaseId == 1:
				arg_27_0.isSubmitTecFirstTaskTag = True

				arg_27_0.emit(TrainingCampMediator.ON_TRIGGER, {
					cmd = 1,
					activity_id = arg_27_0.activity.id
				}), SFX_PANEL)
	onButton(arg_27_0, var_27_5, function()
		arg_27_0.emit(TrainingCampMediator.ON_GO, var_27_2), SFX_PANEL)

def var_0_0.updateToggleDisable(arg_33_0, arg_33_1):
	for iter_33_0, iter_33_1 in ipairs(arg_33_1):
		setActive(iter_33_1.Find("Disable"), iter_33_0 > arg_33_0.phaseId)

def var_0_0.updateTaskUIItemList(arg_34_0, arg_34_1, arg_34_2, arg_34_3):
	arg_34_1.make(function(arg_35_0, arg_35_1, arg_35_2)
		if arg_35_0 == UIItemList.EventUpdate:
			arg_35_1 = arg_35_1 + 1

			arg_34_0.updateTask(arg_34_2[arg_35_1], arg_35_2, arg_34_3))
	arg_34_1.align(#arg_34_2)

def var_0_0.updateTask(arg_36_0, arg_36_1, arg_36_2, arg_36_3):
	local var_36_0 = arg_36_2.Find("Get")
	local var_36_1 = arg_36_2.Find("Got")
	local var_36_2 = arg_36_2.Find("Go")
	local var_36_3 = arg_36_0.getTask(arg_36_3, arg_36_1)

	setActive(var_36_0, var_36_3 and var_36_3.isFinish() and not var_36_3.isReceive())
	setActive(var_36_1, var_36_3 and var_36_3.isReceive())
	setActive(var_36_2, not var_36_3 or var_36_3 and not var_36_3.isFinish())

	if var_36_3 and var_36_3.isClientTrigger() and not var_36_3.isFinish():
		arg_36_0.emit(TrainingCampMediator.ON_UPDATE, var_36_3)

	var_36_3 = var_36_3 or Task.New({
		id = arg_36_1
	})

	setText(arg_36_2.Find("TitleText"), var_36_3.getConfig("desc"))

	local var_36_4 = var_36_3.getConfig("award_display")[1]
	local var_36_5 = arg_36_2.Find("Item")
	local var_36_6 = {
		type = var_36_4[1],
		id = var_36_4[2],
		count = var_36_4[3]
	}

	updateDrop(var_36_5, var_36_6)
	onButton(arg_36_0, var_36_5, function()
		arg_36_0.emit(BaseUI.ON_DROP, var_36_6), SFX_PANEL)
	setText(arg_36_2.Find("ProgressText"), math.min(var_36_3.progress, var_36_3.getConfig("target_num")) .. "/" .. var_36_3.getConfig("target_num"))
	onButton(arg_36_0, var_36_0, function()
		arg_36_0.emit(TrainingCampMediator.ON_GET, var_36_3), SFX_PANEL)
	onButton(arg_36_0, var_36_2, function()
		arg_36_0.emit(TrainingCampMediator.ON_GO, var_36_3), SFX_PANEL)

def var_0_0.getTask(arg_40_0, arg_40_1, arg_40_2, arg_40_3):
	local var_40_0

	if arg_40_1 >= arg_40_0.phaseId:
		if arg_40_3 == True:
			return None

		var_40_0 = arg_40_0.taskProxy.getTaskById(arg_40_2) or arg_40_0.taskProxy.getFinishTaskById(arg_40_2)
	else
		var_40_0 = Task.New({
			id = arg_40_2
		})
		var_40_0.progress = var_40_0.getConfig("target_num")
		var_40_0.submitTime = 1

	return var_40_0

def var_0_0.getTaskState(arg_41_0, arg_41_1):
	if arg_41_1.isReceive():
		return 0
	elif arg_41_1.isFinish():
		return 2
	elif not arg_41_1.isFinish():
		return 1

	return -1

def var_0_0.sortTaskIDList(arg_42_0, arg_42_1):
	table.sort(arg_42_1, function(arg_43_0, arg_43_1)
		local var_43_0 = arg_42_0.taskProxy.getTaskVO(arg_43_0) or Task.New({
			id = arg_43_0
		})
		local var_43_1 = arg_42_0.taskProxy.getTaskVO(arg_43_1) or Task.New({
			id = arg_43_1
		})
		local var_43_2 = arg_42_0.getTaskState(var_43_0)
		local var_43_3 = arg_42_0.getTaskState(var_43_1)

		if var_43_2 == var_43_3:
			return var_43_0.id < var_43_1.id
		else
			return var_43_3 < var_43_2)

	return arg_42_1

def var_0_0.isFinishedAll(arg_44_0, arg_44_1):
	return _.all(arg_44_1, function(arg_45_0)
		local var_45_0 = arg_44_0.taskProxy.getTaskVO(arg_45_0)

		return var_45_0 and var_45_0.isReceive() or False)

def var_0_0.isMissTask(arg_46_0, arg_46_1):
	return _.any(arg_46_1, function(arg_47_0)
		return arg_46_0.taskProxy.getTaskVO(arg_47_0) == None)

def var_0_0.setPhrase(arg_48_0):
	if arg_48_0.lockFirst == True:
		arg_48_0.phaseId = 1

		return

	local var_48_0 = 1
	local var_48_1 = arg_48_0.activity.getConfig("config_data")[3]
	local var_48_2 = #var_48_1

	local function var_48_3(arg_49_0)
		if arg_49_0 > 1:
			local var_49_0 = var_48_1[arg_49_0 - 1][2]

			return arg_48_0.taskProxy.getFinishTaskById(var_49_0) != None

	for iter_48_0 = var_48_2, 1, -1:
		local var_48_4 = var_48_1[iter_48_0][1]

		if _.all(var_48_4, function(arg_50_0)
			return arg_48_0.taskProxy.getTaskVO(arg_50_0) != None) or var_48_3(iter_48_0):
			var_48_0 = iter_48_0

			break

	arg_48_0.phaseId = var_48_0

def var_0_0.isNormalActOn():
	local var_51_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_GUIDE_TASKS)
	local var_51_1 = var_51_0 and not var_51_0.isEnd()
	local var_51_2 = False
	local var_51_3 = False

	if var_51_1:
		local var_51_4 = var_51_0.getConfig("config_data")[1]
		local var_51_5 = getProxy(ChapterProxy).getChapterById(var_51_4)

		var_51_2 = var_51_5 and var_51_5.isClear()

		local var_51_6 = _.flatten(var_51_0.getConfig("config_data")[3])
		local var_51_7 = getProxy(TaskProxy)

		var_51_3 = _.any(var_51_6, function(arg_52_0)
			local var_52_0 = var_51_7.getTaskById(arg_52_0)

			return var_52_0 and var_52_0.isFinish() and not var_52_0.isReceive())

	return var_51_1 and var_51_2, var_51_3

def var_0_0.isTecActOn():
	local var_53_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FRESH_TEC_CATCHUP)
	local var_53_1 = var_53_0 and not var_53_0.isEnd()
	local var_53_2 = getProxy(PlayerProxy).getRawData()
	local var_53_3 = pg.SystemOpenMgr.GetInstance().isOpenSystem(var_53_2.level, "ShipBluePrintMediator")
	local var_53_4 = False
	local var_53_5 = False

	if var_53_1:
		local var_53_6 = var_53_0.getConfig("config_data")[1]
		local var_53_7 = getProxy(ChapterProxy).getChapterById(var_53_6)

		var_53_4 = var_53_7 and var_53_7.isClear()

		local var_53_8 = _.flatten(var_53_0.getConfig("config_data")[3])
		local var_53_9 = getProxy(TaskProxy)

		var_53_5 = _.any(var_53_8, function(arg_54_0)
			local var_54_0 = var_53_9.getTaskById(arg_54_0)

			return var_54_0 and var_54_0.isFinish() and not var_54_0.isReceive())

	return var_53_1 and var_53_4 and var_53_3, var_53_5

def var_0_0.switchPanel(arg_55_0, arg_55_1, arg_55_2):
	arg_55_0.activity = arg_55_1

	if arg_55_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_GUIDE_TASKS:
		arg_55_0.setPhrase()

		if arg_55_2:
			arg_55_0.aniOnSwitch(arg_55_0.normalPanel, arg_55_0.tecPanel)
		else
			setActive(arg_55_0.normalPanel, True)
			setActive(arg_55_0.tecPanel, False)

		arg_55_0.updateToggleDisable(arg_55_0.normalToggles)
		triggerToggle(arg_55_0.normalToggles[arg_55_0.phaseId], True)
	elif arg_55_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_FRESH_TEC_CATCHUP:
		arg_55_0.setPhrase()

		if arg_55_2:
			arg_55_0.aniOnSwitch(arg_55_0.tecPanel, arg_55_0.normalPanel)
		else
			setActive(arg_55_0.normalPanel, False)
			setActive(arg_55_0.tecPanel, True)

		arg_55_0.updateToggleDisable(arg_55_0.tecToggles)
		triggerToggle(arg_55_0.tecToggles[arg_55_0.phaseId], True)

def var_0_0.switchPageByMediator(arg_56_0):
	if arg_56_0.activity.getConfig("type") == ActivityConst.ACTIVITY_TYPE_GUIDE_TASKS:
		arg_56_0.switchPanel(arg_56_0.normalTaskactivity)
	elif arg_56_0.activity.getConfig("type") == ActivityConst.ACTIVITY_TYPE_FRESH_TEC_CATCHUP:
		arg_56_0.switchPanel(arg_56_0.tecTaskActivity)

def var_0_0.aniOnSwitch(arg_57_0, arg_57_1, arg_57_2):
	arg_57_0.isOnSwitchAni = True

	arg_57_1.SetAsLastSibling()
	setActive(arg_57_1, True)
	GetOrAddComponent(arg_57_1, "DftAniEvent").SetEndEvent(function()
		arg_57_0.isOnSwitchAni = False

		setActive(arg_57_2, False))

def var_0_0.openMsgbox(arg_59_0, arg_59_1):
	setActive(arg_59_0.switchToNormalBtn, False)
	setActive(arg_59_0.switchToTecBtn, False)
	setActive(arg_59_0.awardMsg, True)
	setActive(arg_59_0.normalPanel, False)

	local var_59_0
	local var_59_1 = arg_59_0.awardMsg.Find("photos")

	for iter_59_0 = 1, var_59_1.childCount:
		local var_59_2 = var_59_1.GetChild(iter_59_0 - 1)

		onToggle(arg_59_0, var_59_2, function(arg_60_0)
			if arg_60_0:
				var_59_0 = iter_59_0, SFX_PANEL)

	onButton(arg_59_0, arg_59_0.awardMsg.Find("confirm_btn"), function()
		if var_59_0:
			if arg_59_1:
				arg_59_1(var_59_0)

			arg_59_0.closeMsgBox(), SFX_PANEL)

def var_0_0.closeMsgBox(arg_62_0):
	setActive(arg_62_0.awardMsg, False)
	setActive(arg_62_0.normalPanel, True)
	arg_62_0.updateSwitchBtns()

def var_0_0.tryShowTecFixTip(arg_63_0):
	if arg_63_0.isSubmitTecFirstTaskTag == True:
		arg_63_0.isSubmitTecFirstTaskTag = False

		local var_63_0 = arg_63_0.tecTaskActivity.getConfig("config_data")[3][1][1]

		if _.all(var_63_0, function(arg_64_0)
			return arg_63_0.taskProxy.getTaskById(arg_64_0) != None):
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				modal = True,
				hideNo = True,
				hideClose = True,
				content = i18n("tec_catchup_errorfix"),
				weight = LayerWeightConst.TOP_LAYER,
				def onClose:()
					arg_63_0.lockFirst = True

					arg_63_0.switchPanel(arg_63_0.tecTaskActivity),
				def onYes:()
					arg_63_0.lockFirst = True

					arg_63_0.switchPanel(arg_63_0.tecTaskActivity)
			})

return var_0_0
