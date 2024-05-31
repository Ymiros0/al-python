local var_0_0 = class("NewMeixiV4Scene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "NewMeixiV4UI"

def var_0_0.ResUISettings(arg_2_0):
	return True

def var_0_0.init(arg_3_0):
	arg_3_0.ani = arg_3_0.findTF("TV01")
	arg_3_0.progress = arg_3_0.findTF("progress/Text")
	arg_3_0.nodes = arg_3_0.findTF("nodes")
	arg_3_0.nodeInfo = arg_3_0.findTF("node_info")
	arg_3_0.titleTxt = arg_3_0.findTF("progress/title")
	arg_3_0.titleNum = arg_3_0.findTF("progress/cur")
	arg_3_0.helpBtn = arg_3_0.findTF("help_btn")
	arg_3_0.storyTip = arg_3_0.findTF("get_story")
	arg_3_0.taskProxy = getProxy(TaskProxy)

	local var_3_0 = pg.activity_template[ActivityConst.NEWMEIXIV4_SKIRMISH_ID]

	arg_3_0.storyGroup = var_3_0.config_client.storys
	arg_3_0.memoryGroup = var_3_0.config_client.memoryGroup

def var_0_0.didEnter(arg_4_0):
	onButton(arg_4_0, arg_4_0.findTF("top/back_btn"), function()
		arg_4_0.emit(var_0_0.ON_BACK), SOUND_BACK)
	onButton(arg_4_0, arg_4_0.findTF("top/option"), function()
		arg_4_0.emit(var_0_0.ON_HOME), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("MeixiV4_help")
		}), SFX_PANEL)
	setText(arg_4_0.findTF("bar/tip", arg_4_0.storyTip), i18n("world_collection_back"))
	arg_4_0.playAni()
	arg_4_0.updateNodes()

def var_0_0.setPlayer(arg_8_0, arg_8_1):
	arg_8_0.player = arg_8_1

	arg_8_0.onUpdateRes(arg_8_1)

def var_0_0.onUpdateRes(arg_9_0, arg_9_1):
	arg_9_0.player = arg_9_1

def var_0_0.playAni(arg_10_0):
	SetActive(arg_10_0.ani, True)
	arg_10_0.ani.GetComponent("DftAniEvent").SetEndEvent(function(arg_11_0)
		SetActive(arg_10_0.ani, False))
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_WARNING)

def var_0_0.setCurIndex(arg_12_0):
	arg_12_0.curIndex = 1
	arg_12_0.clearTaskNum = 0
	arg_12_0.clearTaskNum = (function()
		for iter_13_0, iter_13_1 in ipairs(arg_12_0.contextData.taskList):
			if arg_12_0.taskProxy.getTaskById(iter_13_1) or arg_12_0.taskProxy.getFinishTaskById(iter_13_1):
				return iter_13_0 - 1)()

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.contextData.taskList):
		local var_12_0 = arg_12_0.taskProxy.getTaskById(iter_12_1) or arg_12_0.taskProxy.getFinishTaskById(iter_12_1)
		local var_12_1 = arg_12_0.contextData.taskList[iter_12_0 + 1]
		local var_12_2 = arg_12_0.taskProxy.getTaskById(var_12_1) or arg_12_0.taskProxy.getFinishTaskById(var_12_1)

		if var_12_0 and var_12_0.getTaskStatus() == 2:
			arg_12_0.curIndex = arg_12_0.curIndex + 1

			if not var_12_1 or not var_12_2:
				arg_12_0.curIndex = arg_12_0.curIndex - 1

	arg_12_0.curIndex = arg_12_0.curIndex + arg_12_0.clearTaskNum

def var_0_0.updateNodes(arg_14_0):
	arg_14_0.setCurIndex()
	setText(arg_14_0.titleTxt, "POSITION " .. string.format("%02d", arg_14_0.curIndex))
	setText(arg_14_0.titleNum, string.format("%02d", arg_14_0.curIndex))
	eachChild(arg_14_0.nodes, function(arg_15_0)
		local var_15_0 = tonumber(arg_15_0.name)
		local var_15_1 = arg_14_0.contextData.taskList[var_15_0]

		if not arg_14_0.taskProxy.getTaskById(var_15_1):
			local var_15_2 = arg_14_0.taskProxy.getFinishTaskById(var_15_1)

		setActive(arg_15_0, var_15_0 <= arg_14_0.curIndex)
		onButton(arg_14_0, arg_15_0, function()
			arg_14_0.updateNodeInfo(var_15_0), SFX_PANEL))
	arg_14_0.updateNodeInfo(arg_14_0.curIndex)

def var_0_0.nodeInfoTween(arg_17_0, arg_17_1):
	local var_17_0 = tf(arg_17_0.findTF(tostring(arg_17_1), arg_17_0.nodes)).localPosition

	if arg_17_1 == 9:
		var_17_0.x = var_17_0.x - 80

	if arg_17_1 == 7:
		var_17_0.y = var_17_0.y - 20

	local function var_17_1()
		setLocalPosition(arg_17_0.nodeInfo, Vector3(var_17_0.x, var_17_0.y + 120, 0))
		setLocalScale(arg_17_0.nodeInfo, Vector3(0, 0, 0))
		LeanTween.scale(tf(arg_17_0.nodeInfo), Vector3.one, 0.1)

	local function var_17_2(arg_19_0)
		setLocalScale(arg_17_0.nodeInfo, Vector3(1, 1, 1))
		LeanTween.scale(tf(arg_17_0.nodeInfo), Vector3.zero, 0.1).setOnComplete(System.Action(function()
			if arg_19_0:
				arg_19_0()))

	if not isActive(arg_17_0.nodeInfo):
		setActive(arg_17_0.nodeInfo, True)
		var_17_1()
	else
		var_17_2(var_17_1)

def var_0_0.updateNodeInfo(arg_21_0, arg_21_1):
	local var_21_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.NEWMEIXIV4_SKIRMISH_ID)

	updateActivityTaskStatus(var_21_0)

	local var_21_1 = arg_21_0.contextData.taskList[arg_21_1]
	local var_21_2 = arg_21_0.taskProxy.getTaskById(var_21_1) or arg_21_0.taskProxy.getFinishTaskById(var_21_1)
	local var_21_3 = pg.task_data_template[var_21_1]
	local var_21_4 = var_21_2 and var_21_2.getProgress() or var_21_3.target_num
	local var_21_5 = var_21_2 and var_21_2.getConfig("target_num") or var_21_3.target_num
	local var_21_6 = var_21_2 and var_21_2.getTaskStatus() or 2
	local var_21_7 = var_21_2 and var_21_2.getConfig("desc") or var_21_3.desc

	setSlider(arg_21_0.findTF("progress", arg_21_0.nodeInfo), 0, var_21_5, var_21_4)
	setText(arg_21_0.findTF("step", arg_21_0.nodeInfo), var_21_4 .. "/" .. var_21_5)
	setText(arg_21_0.findTF("content", arg_21_0.nodeInfo), var_21_7)
	setText(arg_21_0.findTF("title", arg_21_0.nodeInfo), string.format("%02d", arg_21_1))

	local var_21_8 = arg_21_0.findTF("go_btn", arg_21_0.nodeInfo)
	local var_21_9 = arg_21_0.findTF("get_btn", arg_21_0.nodeInfo)
	local var_21_10 = arg_21_0.findTF("step/finish", arg_21_0.nodeInfo)

	setActive(var_21_8, var_21_6 == 0)
	setActive(var_21_9, var_21_6 == 1)
	setActive(var_21_10, var_21_6 == 2)
	onButton(arg_21_0, var_21_8, function()
		arg_21_0.emit(NewMeixiV4Mediator.ON_TASK_GO, var_21_2), SFX_PANEL)
	onButton(arg_21_0, var_21_9, function()
		arg_21_0.emit(NewMeixiV4Mediator.ON_TASK_SUBMIT, var_21_2), SFX_PANEL)
	eachChild(arg_21_0.nodes, function(arg_24_0)
		local var_24_0 = arg_21_0.findTF("arrow", arg_24_0)

		LeanTween.cancel(var_24_0.gameObject)
		setLocalPosition(var_24_0, Vector3(0, 27, 0))

		if tonumber(arg_24_0.name) == arg_21_1:
			setActive(var_24_0, True)
			LeanTween.moveY(var_24_0, 40, 0.5).setEase(LeanTweenType.easeInOutSine).setLoopPingPong()
		else
			setActive(var_24_0, False))
	arg_21_0.nodeInfoTween(arg_21_1)

def var_0_0.onUpdateTask(arg_25_0):
	local var_25_0 = arg_25_0.contextData.taskList[arg_25_0.curIndex]

	for iter_25_0, iter_25_1 in pairs(arg_25_0.storyGroup):
		if var_25_0 == iter_25_1[1]:
			arg_25_0.getStory(iter_25_1[2], iter_25_1[3])

	arg_25_0.updateNodes()

def var_0_0.getStory(arg_26_0, arg_26_1, arg_26_2):
	setActive(arg_26_0.storyTip, True)

	local var_26_0 = pg.memory_template[arg_26_1].title

	pg.NewStoryMgr.GetInstance().SetPlayedFlag(arg_26_2)
	setText(arg_26_0.findTF("bar/Anim/Frame/Mask/Name", arg_26_0.storyTip), var_26_0)
	removeOnButton(arg_26_0.storyTip)
	removeOnButton(arg_26_0.findTF("bar/Button", arg_26_0.storyTip))
	pg.UIMgr.GetInstance().BlurPanel(arg_26_0.storyTip)

	local var_26_1 = arg_26_0.findTF("bar", arg_26_0.storyTip).GetComponent(typeof(DftAniEvent))

	local function var_26_2()
		onButton(arg_26_0, arg_26_0.storyTip, function()
			pg.UIMgr.GetInstance().UnblurPanel(arg_26_0.storyTip)
			setActive(arg_26_0.storyTip, False))
		onButton(arg_26_0, arg_26_0.findTF("bar/Button", arg_26_0.storyTip), function()
			arg_26_0.emit(NewMeixiV4Mediator.GO_STORY, arg_26_0.memoryGroup)
			triggerButton(arg_26_0.storyTip), SFX_PANEL)

	var_26_1.SetEndEvent(var_26_2)

def var_0_0.willExit(arg_30_0):
	setActive(arg_30_0.storyTip, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_30_0.storyTip)

return var_0_0
