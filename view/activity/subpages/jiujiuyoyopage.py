local var_0_0 = class("JiujiuYoyoPage", import("...base.BaseActivityPage"))
local var_0_1 = PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_CHT

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.helpBtn = arg_1_0.findTF("help_btn", arg_1_0.bg)
	arg_1_0.taskBtn = arg_1_0.findTF("task_btn", arg_1_0.bg)
	arg_1_0.taskRedDot = arg_1_0.findTF("red_dot", arg_1_0.taskBtn)
	arg_1_0.ticketNumTF = arg_1_0.findTF("ticket_num", arg_1_0.bg)
	arg_1_0.rollingCountTF = arg_1_0.findTF("rolling_count", arg_1_0.bg)
	arg_1_0.rollingBlink = arg_1_0.findTF("blink", arg_1_0.bg)

	if var_0_1:
		arg_1_0.awardTpl = arg_1_0.findTF("item_jp", arg_1_0.bg)
		arg_1_0.awardContainter = arg_1_0.findTF("award_list_jp", arg_1_0.bg)
	else
		arg_1_0.awardTpl = arg_1_0.findTF("item", arg_1_0.bg)
		arg_1_0.awardContainter = arg_1_0.findTF("award_list", arg_1_0.bg)

	arg_1_0.awardUIList = UIItemList.New(arg_1_0.awardContainter, arg_1_0.awardTpl)
	arg_1_0.finalGot = arg_1_0.findTF("final_got_jp", arg_1_0.bg)
	arg_1_0.rollingAni = arg_1_0.findTF("rolling_mask", arg_1_0.bg)
	arg_1_0.rollingSpine = arg_1_0.findTF("rolling", arg_1_0.rollingAni).GetComponent("SpineAnimUI")
	arg_1_0.rollingGraphic = arg_1_0.findTF("rolling", arg_1_0.rollingAni).GetComponent("SkeletonGraphic")
	arg_1_0.forbidMask = arg_1_0.findTF("forbid_mask", arg_1_0.bg)
	arg_1_0.taskWindow = arg_1_0.findTF("TaskWindow")
	arg_1_0.closeBtn = arg_1_0.findTF("panel/close_btn", arg_1_0.taskWindow)
	arg_1_0.taskTpl = arg_1_0.findTF("panel/scrollview/item", arg_1_0.taskWindow)
	arg_1_0.taskContainter = arg_1_0.findTF("panel/scrollview/items", arg_1_0.taskWindow)
	arg_1_0.taskUIList = UIItemList.New(arg_1_0.taskContainter, arg_1_0.taskTpl)

	arg_1_0.register()

def var_0_0.register(arg_2_0):
	arg_2_0.bind(ActivityMediator.ON_SHAKE_BEADS_RESULT, function(arg_3_0, arg_3_1)
		arg_2_0.displayResult(arg_3_1.awards, arg_3_1.number, function()
			arg_3_1.callback()))

def var_0_0.OnDataSetting(arg_5_0):
	arg_5_0.taskProxy = getProxy(TaskProxy)

	local var_5_0 = arg_5_0.activity.getConfig("config_client").taskActID

	arg_5_0.taskList = pg.activity_template[var_5_0].config_data
	arg_5_0.startTime = arg_5_0.activity.getStartTime()
	arg_5_0.totalNumList = {}
	arg_5_0.remainNumList = {}
	arg_5_0.remainTotalNum = 0
	arg_5_0.awardList = {}
	arg_5_0.finalAward = arg_5_0.activity.getConfig("config_client").finalAward
	arg_5_0.awardConifg = arg_5_0.activity.getConfig("config_client").award
	arg_5_0.beadsConfig = arg_5_0.activity.getConfig("config_data")[1]

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.beadsConfig):
		local var_5_1 = iter_5_1[1]

		arg_5_0.awardList[var_5_1] = arg_5_0.awardConifg[var_5_1]
		arg_5_0.totalNumList[var_5_1] = iter_5_1[2]

def var_0_0.OnFirstFlush(arg_6_0):
	onButton(arg_6_0, arg_6_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("tips_shakebeads")
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.taskBtn, function()
		arg_6_0.openTask(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.closeBtn, function()
		arg_6_0.closeTask(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.findTF("mask", arg_6_0.taskWindow), function()
		arg_6_0.closeTask(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.rollingBlink, function()
		if arg_6_0.ticketNum <= 0:
			return

		arg_6_0.emit(ActivityMediator.EVENT_OPERATION, {
			cmd = 1,
			activity_id = arg_6_0.activity.id
		}), SFX_PANEL)
	setActive(arg_6_0.taskRedDot, False)

	if LeanTween.isTweening(arg_6_0.rollingBlink):
		LeanTween.cancel(arg_6_0.rollingBlink)

	setImageAlpha(arg_6_0.rollingBlink, 1)
	blinkAni(arg_6_0.rollingBlink, 0.5)

def var_0_0.OnUpdateFlush(arg_12_0):
	arg_12_0.curDay = pg.TimeMgr.GetInstance().DiffDay(arg_12_0.startTime, pg.TimeMgr.GetInstance().GetServerTime()) + 1
	arg_12_0.ticketNum = arg_12_0.activity.data1
	arg_12_0.hasNumList = arg_12_0.activity.data1KeyValueList[1]
	arg_12_0.remainTotalNum = 0

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.beadsConfig):
		local var_12_0 = iter_12_1[1]

		if not arg_12_0.hasNumList[var_12_0]:
			arg_12_0.hasNumList[var_12_0] = 0

		arg_12_0.remainNumList[var_12_0] = arg_12_0.totalNumList[var_12_0] - arg_12_0.hasNumList[var_12_0]
		arg_12_0.remainTotalNum = arg_12_0.remainTotalNum + arg_12_0.remainNumList[var_12_0]

	setText(arg_12_0.ticketNumTF, arg_12_0.ticketNum)
	setText(arg_12_0.rollingCountTF, arg_12_0.remainTotalNum)
	setActive(arg_12_0.rollingBlink, arg_12_0.ticketNum > 0)
	arg_12_0.initAwardList()
	arg_12_0.initTaskWindow()

	arg_12_0.isFirst = PlayerPrefs.GetInt("jiujiuyoyo_first_" .. getProxy(PlayerProxy).getData().id)

	if arg_12_0.isFirst == 0:
		setActive(arg_12_0.taskRedDot, True)

	if #arg_12_0.finishItemList > 0:
		arg_12_0.openTask()

	setActive(arg_12_0.finalGot, var_0_1 and arg_12_0.activity.data2 == 1)
	arg_12_0.CheckFinalAward()

def var_0_0.initAwardList(arg_13_0):
	arg_13_0.awardUIList.make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate:
			local var_14_0 = arg_14_1 + 1
			local var_14_1 = arg_13_0.totalNumList[var_14_0]
			local var_14_2 = arg_13_0.remainNumList[var_14_0]

			if var_14_2 == 0:
				setTextColor(arg_13_0.findTF("num", arg_14_2), Color.New(0.55, 0.55, 0.55, 1))
				setOutlineColor(arg_13_0.findTF("num", arg_14_2), Color.New(0.26, 0.26, 0.26, 1))

			setText(arg_13_0.findTF("num", arg_14_2), var_14_2 .. "/" .. var_14_1)
			setActive(arg_13_0.findTF("got", arg_14_2), var_14_2 == 0)

			local var_14_3 = arg_13_0.findTF("award_mask/award", arg_14_2)
			local var_14_4 = arg_13_0.awardList[var_14_0]
			local var_14_5 = {
				type = var_14_4[1],
				id = var_14_4[2],
				count = var_14_4[3] * var_14_2
			}

			updateDrop(var_14_3, var_14_5)
			onButton(arg_13_0, var_14_3, function()
				arg_13_0.emit(BaseUI.ON_DROP, var_14_5), SFX_PANEL))
	arg_13_0.awardUIList.align(#arg_13_0.awardList)

def var_0_0.initTaskWindow(arg_16_0):
	arg_16_0.finishItemList = {}
	arg_16_0.finishTaskVOList = {}

	arg_16_0.taskUIList.make(function(arg_17_0, arg_17_1, arg_17_2)
		if arg_17_0 == UIItemList.EventUpdate:
			local var_17_0 = arg_17_1 + 1
			local var_17_1 = arg_16_0.findTF("award/award", arg_17_2)
			local var_17_2 = arg_16_0.taskList[var_17_0]
			local var_17_3 = arg_16_0.taskProxy.getTaskById(var_17_2) or arg_16_0.taskProxy.getFinishTaskById(var_17_2)

			assert(var_17_3, "without this task by id. " .. var_17_2)

			local var_17_4 = var_17_3.getProgress()
			local var_17_5 = var_17_3.getConfig("target_num")
			local var_17_6 = var_17_3.getTaskStatus()
			local var_17_7 = var_17_3.getConfig("desc")
			local var_17_8 = var_17_3.getConfig("award_display")[1]
			local var_17_9 = var_17_0 > arg_16_0.curDay

			setText(arg_16_0.findTF("description", arg_17_2), var_17_7)
			setText(arg_16_0.findTF("progress/progressText", arg_17_2), var_17_4 .. "/" .. var_17_5)
			setSlider(arg_16_0.findTF("progress", arg_17_2), 0, var_17_5, var_17_4)

			local var_17_10 = {
				type = var_17_8[1],
				id = var_17_8[2],
				count = var_17_8[3]
			}

			updateDrop(var_17_1, var_17_10)
			onButton(arg_16_0, arg_16_0.findTF("award/Image", arg_17_2), function()
				arg_16_0.emit(BaseUI.ON_DROP, var_17_10), SFX_PANEL)

			local var_17_11 = arg_16_0.findTF("go_btn", arg_17_2)
			local var_17_12 = arg_16_0.findTF("get_btn", arg_17_2)

			setActive(var_17_11, var_17_6 == 0)
			setActive(var_17_12, var_17_6 == 1)
			onButton(arg_16_0, var_17_11, function()
				arg_16_0.emit(ActivityMediator.ON_TASK_GO, var_17_3), SFX_PANEL)
			onButton(arg_16_0, var_17_12, function()
				arg_16_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_17_3), SFX_PANEL)
			setActive(arg_16_0.findTF("finnal", arg_17_2), var_17_6 == 2 and not var_17_9)
			setText(arg_16_0.findTF("lock/tip", arg_17_2), i18n("unlock_tips", var_17_0))
			setActive(arg_16_0.findTF("lock", arg_17_2), var_17_9)

			if var_17_6 == 1 and not var_17_9:
				table.insert(arg_16_0.finishItemList, arg_17_2)
				table.insert(arg_16_0.finishTaskVOList, var_17_3))
	arg_16_0.taskUIList.align(#arg_16_0.taskList)

def var_0_0.closeTask(arg_21_0):
	setActive(arg_21_0.taskWindow, False)

def var_0_0.openTask(arg_22_0):
	setActive(arg_22_0.taskWindow, True)

	if arg_22_0.isFirst == 0:
		PlayerPrefs.SetInt("jiujiuyoyo_first_" .. getProxy(PlayerProxy).getData().id, 1)
		setActive(arg_22_0.taskRedDot, False)

	arg_22_0.hasClickTask = True

	eachChild(arg_22_0.taskContainter, function(arg_23_0)
		if isActive(arg_22_0.findTF("finnal", arg_23_0)):
			arg_23_0.SetAsLastSibling())

	if #arg_22_0.finishItemList > 0:
		arg_22_0.autoFinishTask()

def var_0_0.autoFinishTask(arg_24_0):
	local var_24_0 = 0.01
	local var_24_1 = 0.5

	for iter_24_0, iter_24_1 in ipairs(arg_24_0.finishItemList):
		local var_24_2 = GetOrAddComponent(iter_24_1, typeof(CanvasGroup))

		arg_24_0.managedTween(LeanTween.delayedCall, function()
			iter_24_1.SetAsFirstSibling()
			LeanTween.value(go(iter_24_1), 1, 0, var_24_1).setOnUpdate(System.Action_float(function(arg_26_0)
				var_24_2.alpha = arg_26_0)).setOnComplete(System.Action(function()
				var_24_2.alpha = 1

				setActive(arg_24_0.findTF("finnal", iter_24_1), True)
				iter_24_1.SetAsLastSibling())), var_24_0, None)

		var_24_0 = var_24_0 + var_24_1 + 0.1

	arg_24_0.managedTween(LeanTween.delayedCall, function()
		pg.m02.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
			resultList = arg_24_0.finishTaskVOList
		}), var_24_0, None)

def var_0_0.CheckFinalAward(arg_29_0):
	if var_0_1 and arg_29_0.activity.data2 == 0 and arg_29_0.remainTotalNum == 0:
		arg_29_0.emit(ActivityMediator.EVENT_OPERATION, {
			cmd = 2,
			activity_id = arg_29_0.activity.id
		})

def var_0_0.displayResult(arg_30_0, arg_30_1, arg_30_2, arg_30_3):
	arg_30_0.setForbidMaskStatus(True)
	setActive(arg_30_0.rollingAni, True)

	function arg_30_0.aniCallback()
		arg_30_3()

	arg_30_0.rollingSpine.SetActionCallBack(function(arg_32_0)
		if arg_32_0 == "finish":
			setActive(arg_30_0.rollingAni, False)
			arg_30_3()

			arg_30_0.aniCallback = None

			arg_30_0.setForbidMaskStatus(False))
	arg_30_0.rollingSpine.SetAction(tostring(arg_30_2), 0)
	pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/zhuanzhu")
	arg_30_0.managedTween(LeanTween.delayedCall, function()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("event./ui/zhengque"), 4, None)

def var_0_0.setForbidMaskStatus(arg_34_0, arg_34_1):
	if arg_34_1:
		setActive(arg_34_0.forbidMask, True)
		pg.UIMgr.GetInstance().OverlayPanel(arg_34_0.forbidMask)
	else
		setActive(arg_34_0.forbidMask, False)
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_34_0.forbidMask, arg_34_0.bg)

def var_0_0.canFinishTask():
	local var_35_0 = pg.activity_template[ActivityConst.JIUJIU_YOYO_ID]
	local var_35_1 = var_35_0.config_client.taskActID
	local var_35_2 = pg.activity_template[var_35_1].config_data
	local var_35_3 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_35_0.time[2])
	local var_35_4 = pg.TimeMgr.GetInstance().DiffDay(var_35_3, pg.TimeMgr.GetInstance().GetServerTime()) + 1
	local var_35_5 = False
	local var_35_6 = getProxy(TaskProxy)

	for iter_35_0, iter_35_1 in pairs(var_35_2):
		local var_35_7 = var_35_4 < iter_35_0
		local var_35_8 = var_35_6.getTaskById(iter_35_1) or var_35_6.getFinishTaskById(iter_35_1)

		assert(var_35_8, "without this task by id. " .. iter_35_1)

		if var_35_8.getTaskStatus() == 1 and not var_35_7:
			var_35_5 = True

			break

	return var_35_5

def var_0_0.IsShowRed():
	return getProxy(ActivityProxy).getActivityById(ActivityConst.JIUJIU_YOYO_ID).data1 > 0 or var_0_0.canFinishTask()

return var_0_0
