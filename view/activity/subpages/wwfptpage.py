local var_0_0 = class("WWFPtPage", import(".TemplatePage.PtTemplatePage"))
local var_0_1 = 6000

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.helpBtn = arg_1_0.findTF("help_btn", arg_1_0.bg)
	arg_1_0.collectBtn = arg_1_0.findTF("collect_btn", arg_1_0.bg)
	arg_1_0.taskRedDot = arg_1_0.findTF("red_dot", arg_1_0.collectBtn)
	arg_1_0.resNumTF = arg_1_0.findTF("res_num", arg_1_0.collectBtn)
	arg_1_0.title = arg_1_0.findTF("title", arg_1_0.bg)
	arg_1_0.tags = arg_1_0.findTF("tags", arg_1_0.bg)
	arg_1_0.convertBtn = arg_1_0.findTF("convert_btn", arg_1_0.bg)
	arg_1_0.switchBtn = arg_1_0.findTF("switch_btn", arg_1_0.bg)
	arg_1_0.switchRedDot = arg_1_0.findTF("red_dot", arg_1_0.switchBtn)
	arg_1_0.paintings = {
		arg_1_0.findTF("paintings/ninghai", arg_1_0.bg),
		arg_1_0.findTF("paintings/pinghai", arg_1_0.bg)
	}
	arg_1_0.anim = arg_1_0.findTF("anim", arg_1_0.bg)
	arg_1_0.ninghaiTF = arg_1_0.findTF("anim/panda_anim/ninghai", arg_1_0.bg)
	arg_1_0.pinghaiTF = arg_1_0.findTF("anim/panda_anim/pinghai", arg_1_0.bg)
	arg_1_0.heartImages = arg_1_0.findTF("hearts", arg_1_0.bg)
	arg_1_0.step2 = arg_1_0.findTF("step2", arg_1_0.bg)
	arg_1_0.taskWindow = arg_1_0.findTF("TaskWindow")
	arg_1_0.closeBtn = arg_1_0.findTF("panel/close_btn", arg_1_0.taskWindow)
	arg_1_0.maskBtn = arg_1_0.findTF("mask", arg_1_0.taskWindow)
	arg_1_0.item = arg_1_0.findTF("panel/scrollview/item", arg_1_0.taskWindow)
	arg_1_0.items = arg_1_0.findTF("panel/scrollview/items", arg_1_0.taskWindow)
	arg_1_0.uilist = UIItemList.New(arg_1_0.items, arg_1_0.item)
	arg_1_0.typeImages = arg_1_0.findTF("panel/tags", arg_1_0.taskWindow)
	arg_1_0.barImages = arg_1_0.findTF("panel/bars", arg_1_0.taskWindow)
	arg_1_0.guide = arg_1_0.findTF("Guide")
	arg_1_0.guideTarget = arg_1_0.findTF("target", arg_1_0.guide)
	arg_1_0.guideContent = arg_1_0.findTF("dialogBox/content", arg_1_0.guide)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.titleTxts = {
		i18n("wwf_bamboo_tip1"),
		i18n("wwf_bamboo_tip2")
	}
	arg_2_0.resID = arg_2_0.activity.getConfig("config_client").convertRes
	arg_2_0.subActivities = arg_2_0.activity.getConfig("config_client").ptActID
	arg_2_0.taskList = arg_2_0.activity.getConfig("config_data")

	arg_2_0.initPtData()
	arg_2_0.initTaskData()
	arg_2_0.initLocalData()

def var_0_0.initPtData(arg_3_0):
	arg_3_0.subPtDate = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.subActivities):
		local var_3_0 = getProxy(ActivityProxy).getActivityById(iter_3_1)

		if arg_3_0.subPtDate[iter_3_1]:
			arg_3_0.subPtDate[iter_3_1].Update(var_3_0)
		else
			arg_3_0.subPtDate[iter_3_1] = ActivityPtData.New(var_3_0)

	arg_3_0.resNum = getProxy(PlayerProxy).getRawData().getResource(arg_3_0.resID)

def var_0_0.setPtActIndex(arg_4_0):
	arg_4_0.curActIndex = arg_4_0.lastSelectIndex
	arg_4_0.curSubActID = arg_4_0.subActivities[arg_4_0.curActIndex]

	local var_4_0 = arg_4_0.curActIndex == 1 and 2 or 1
	local var_4_1 = arg_4_0.subPtDate[arg_4_0.curSubActID].CanGetMorePt()
	local var_4_2 = arg_4_0.subPtDate[arg_4_0.subActivities[var_4_0]].CanGetAward()

	if not var_4_1 or var_4_2:
		arg_4_0.curActIndex = var_4_0
		arg_4_0.curSubActID = arg_4_0.subActivities[arg_4_0.curActIndex]

		PlayerPrefs.SetInt("wwf_select_index_" .. arg_4_0.playerId, arg_4_0.lastSelectIndex)
		PlayerPrefs.Save()

def var_0_0.setStep2Progress(arg_5_0):
	local var_5_0 = arg_5_0.subPtDate[arg_5_0.curSubActID].count

	setImageSprite(arg_5_0.step2, arg_5_0.heartImages.Find(tostring(arg_5_0.curActIndex)).GetComponent(typeof(Image)).sprite)

	arg_5_0.step2.GetComponent(typeof(Image)).fillAmount = var_5_0 / var_0_1

def var_0_0.initTaskData(arg_6_0):
	arg_6_0.taskProxy = getProxy(TaskProxy)
	arg_6_0.curTask = {}
	arg_6_0.todoTaskNum = 0

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.taskList):
		local var_6_0 = arg_6_0.taskProxy.getTaskById(iter_6_1) or arg_6_0.taskProxy.getFinishTaskById(iter_6_1)

		if var_6_0:
			table.insert(arg_6_0.curTask, var_6_0.id)

			if var_6_0.getTaskStatus() == 0:
				arg_6_0.todoTaskNum = arg_6_0.todoTaskNum + 1

def var_0_0.initLocalData(arg_7_0):
	arg_7_0.playerId = getProxy(PlayerProxy).getData().id
	arg_7_0.isFirst = PlayerPrefs.GetInt("wwf_first_" .. arg_7_0.playerId)

	if PlayerPrefs.GetInt("wwf_select_index_" .. arg_7_0.playerId) == 0:
		arg_7_0.lastSelectIndex = 1
	else
		arg_7_0.lastSelectIndex = PlayerPrefs.GetInt("wwf_select_index_" .. arg_7_0.playerId)

	arg_7_0.showTaskRedDot = False

	local var_7_0 = PlayerPrefs.GetInt("wwf_todo_task_num_" .. arg_7_0.playerId)

	if (var_7_0 == 0 and not arg_7_0.todoTaskNum == 0 or var_7_0 < arg_7_0.todoTaskNum) and not arg_7_0.isFinishAllAct():
		arg_7_0.showTaskRedDot = True

	arg_7_0.hasClickTask = False

	PlayerPrefs.SetInt("wwf_todo_task_num_" .. arg_7_0.playerId, arg_7_0.todoTaskNum)
	PlayerPrefs.Save()

def var_0_0.OnFirstFlush(arg_8_0):
	onButton(arg_8_0, arg_8_0.awardTF, function()
		arg_8_0.emit(ActivityMediator.SHOW_AWARD_WINDOW, PtAwardWindow, {
			type = arg_8_0.subPtDate[arg_8_0.curSubActID].type,
			dropList = arg_8_0.subPtDate[arg_8_0.curSubActID].dropList,
			targets = arg_8_0.subPtDate[arg_8_0.curSubActID].targets,
			level = arg_8_0.subPtDate[arg_8_0.curSubActID].level,
			count = arg_8_0.subPtDate[arg_8_0.curSubActID].count,
			resId = arg_8_0.subPtDate[arg_8_0.curSubActID].resId
		}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.getBtn, function()
		local var_10_0 = {}
		local var_10_1 = arg_8_0.subPtDate[arg_8_0.curSubActID].GetAward()
		local var_10_2 = getProxy(PlayerProxy).getData()

		if var_10_1.type == DROP_TYPE_RESOURCE and var_10_1.id == PlayerConst.ResGold and var_10_2.GoldMax(var_10_1.count):
			table.insert(var_10_0, function(arg_11_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("gold_max_tip_title") .. i18n("award_max_warning"),
					onYes = arg_11_0
				}))

		local function var_10_3()
			if not arg_8_0.subPtDate[arg_8_0.curSubActID].CanGetNextAward():
				triggerButton(arg_8_0.switchBtn)

		seriesAsync(var_10_0, function()
			local var_13_0, var_13_1 = arg_8_0.subPtDate[arg_8_0.curSubActID].GetResProgress()

			arg_8_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_8_0.subPtDate[arg_8_0.curSubActID].GetId(),
				arg1 = var_13_1,
				callback = var_10_3
			})), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("wwf_bamboo_help")
		}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.convertBtn, function()
		if arg_8_0.resNum <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("wwf_bamboo_tip3"))
			arg_8_0.openTask()
		else
			arg_8_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 5,
				activity_id = arg_8_0.curSubActID,
				arg1 = arg_8_0.resID
			})
			arg_8_0.playSpineAni(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.switchBtn, function()
		if arg_8_0.isSwitching:
			return

		arg_8_0.curActIndex = arg_8_0.curActIndex == 1 and 2 or 1
		arg_8_0.lastSelectIndex = arg_8_0.curActIndex

		PlayerPrefs.SetInt("wwf_select_index_" .. arg_8_0.playerId, arg_8_0.lastSelectIndex)
		PlayerPrefs.Save()

		arg_8_0.curSubActID = arg_8_0.subActivities[arg_8_0.curActIndex]

		arg_8_0.OnUpdatePtAct()
		arg_8_0.playPaintingAni()
		arg_8_0.setStep2Progress(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.collectBtn, function()
		arg_8_0.openTask(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.closeBtn, function()
		arg_8_0.closeTask(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.maskBtn, function()
		arg_8_0.closeTask(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.guideTarget, function()
		setActive(arg_8_0.guide, False)
		arg_8_0.openTask()
		PlayerPrefs.SetInt("wwf_first_" .. arg_8_0.playerId, 1)
		PlayerPrefs.Save()

		if #arg_8_0.finishItemList > 0:
			arg_8_0.autoFinishTask(), SFX_PANEL)

	local var_8_0 = "ninghai_7"
	local var_8_1 = "pinghai_7"

	if not arg_8_0.model1:
		pg.UIMgr.GetInstance().LoadingOn()
		PoolMgr.GetInstance().GetSpineChar(var_8_0, True, function(arg_21_0)
			pg.UIMgr.GetInstance().LoadingOff()

			arg_8_0.prefab1 = var_8_0
			arg_8_0.model1 = arg_21_0
			tf(arg_21_0).localScale = Vector3(1, 1, 1)

			setParent(arg_21_0, arg_8_0.ninghaiTF)
			setActive(arg_21_0, False))

	if not arg_8_0.model2:
		pg.UIMgr.GetInstance().LoadingOn()
		PoolMgr.GetInstance().GetSpineChar(var_8_1, True, function(arg_22_0)
			pg.UIMgr.GetInstance().LoadingOff()

			arg_8_0.prefab2 = var_8_1
			arg_8_0.model2 = arg_22_0
			tf(arg_22_0).localScale = Vector3(1, 1, 1)

			setParent(arg_22_0, arg_8_0.pinghaiTF)
			setActive(arg_22_0, False))

	arg_8_0.setPtActIndex()
	arg_8_0.setStep2Progress()
	arg_8_0.initTaskWindow()

	if arg_8_0.isFirst == 0:
		setActive(arg_8_0.guide, True)
		setText(arg_8_0.guideContent, i18n("wwf_guide_tip"))
	elif #arg_8_0.finishItemList > 0:
		arg_8_0.openTask()
		arg_8_0.autoFinishTask()

def var_0_0.OnUpdateFlush(arg_23_0):
	for iter_23_0, iter_23_1 in ipairs(arg_23_0.subActivities):
		local var_23_0 = getProxy(ActivityProxy).getActivityById(iter_23_1)

		if arg_23_0.subPtDate[iter_23_1]:
			arg_23_0.subPtDate[iter_23_1].Update(var_23_0)
		else
			arg_23_0.subPtDate[iter_23_1] = ActivityPtData.New(var_23_0)

	arg_23_0.resNum = getProxy(PlayerProxy).getRawData().getResource(arg_23_0.resID)

	setText(arg_23_0.resNumTF, arg_23_0.resNum)
	arg_23_0.OnUpdatePtAct()

	local var_23_1 = arg_23_0.curActIndex == 1 and 2 or 1

	GetOrAddComponent(arg_23_0.paintings[arg_23_0.curActIndex], typeof(CanvasGroup)).alpha = 1
	GetOrAddComponent(arg_23_0.paintings[var_23_1], typeof(CanvasGroup)).alpha = 0

def var_0_0.OnUpdatePtAct(arg_24_0):
	setText(arg_24_0.title, arg_24_0.titleTxts[arg_24_0.curActIndex])
	eachChild(arg_24_0.tags, function(arg_25_0)
		setActive(arg_25_0, tonumber(arg_25_0.name) == arg_24_0.curActIndex))

	local var_24_0, var_24_1, var_24_2 = arg_24_0.subPtDate[arg_24_0.curSubActID].GetLevelProgress()
	local var_24_3, var_24_4, var_24_5 = arg_24_0.subPtDate[arg_24_0.curSubActID].GetResProgress()

	eachChild(arg_24_0.step, function(arg_26_0)
		setActive(arg_26_0, tonumber(arg_26_0.name) < var_24_0 and True or False))
	setText(arg_24_0.progress, (var_24_5 >= 1 and setColorStr(var_24_3, "#94D979") or var_24_3) .. "/" .. var_24_4)

	local var_24_6 = arg_24_0.subPtDate[arg_24_0.curSubActID].GetAward()

	updateDrop(arg_24_0.awardTF, var_24_6)

	local var_24_7 = arg_24_0.subPtDate[arg_24_0.curSubActID].CanGetAward()
	local var_24_8 = arg_24_0.subPtDate[arg_24_0.curSubActID].CanGetNextAward()
	local var_24_9 = arg_24_0.subPtDate[arg_24_0.curSubActID].CanGetMorePt()

	setActive(arg_24_0.convertBtn, not var_24_7)
	setActive(arg_24_0.getBtn, var_24_7)
	setActive(arg_24_0.gotBtn, not var_24_8)
	setActive(arg_24_0.findTF("10", arg_24_0.step), not var_24_8)
	setActive(arg_24_0.switchRedDot, not var_24_8 and not arg_24_0.isFinishAllAct())
	setActive(arg_24_0.taskRedDot, arg_24_0.showTaskRedDot and not arg_24_0.hasClickTask)

def var_0_0.playPaintingAni(arg_27_0):
	arg_27_0.isSwitching = True

	local var_27_0 = arg_27_0.curActIndex
	local var_27_1 = arg_27_0.curActIndex == 1 and 2 or 1
	local var_27_2 = arg_27_0.paintings[var_27_0]
	local var_27_3 = arg_27_0.paintings[var_27_1]
	local var_27_4 = GetOrAddComponent(var_27_2, typeof(CanvasGroup))
	local var_27_5 = GetOrAddComponent(var_27_3, typeof(CanvasGroup))

	LeanTween.value(go(var_27_3), 1, 0, 0.4).setOnUpdate(System.Action_float(function(arg_28_0)
		var_27_5.alpha = arg_28_0)).setOnComplete(System.Action(function()
		LeanTween.value(go(var_27_2), 0, 1, 0.4).setOnUpdate(System.Action_float(function(arg_30_0)
			var_27_4.alpha = arg_30_0)).setOnComplete(System.Action(function()
			arg_27_0.isSwitching = False))))

def var_0_0.playSpineAni(arg_32_0):
	setActive(arg_32_0.anim, True)

	local var_32_0 = 0.4
	local var_32_1 = arg_32_0.findTF("panda_anim", arg_32_0.anim)
	local var_32_2 = arg_32_0.findTF("heart_anim", arg_32_0.anim)
	local var_32_3 = GetOrAddComponent(var_32_1, typeof(CanvasGroup))

	setActive(var_32_1, True)

	var_32_3.alpha = 1

	LeanTween.value(go(var_32_1), 0, 1, var_32_0).setOnUpdate(System.Action_float(function(arg_33_0)
		var_32_3.alpha = arg_33_0))

	local function var_32_4()
		LeanTween.value(go(var_32_1), 1, 0, var_32_0).setOnUpdate(System.Action_float(function(arg_35_0)
			var_32_3.alpha = arg_35_0))
		LeanTween.scale(var_32_1, Vector3(1, 0, 1), var_32_0).setFrom(Vector3(1, 1, 1)).setOnComplete(System.Action(function()
			setActive(var_32_1, False)))
		setActive(var_32_2, True)
		LeanTween.delayedCall(2, System.Action(function()
			setActive(var_32_2, False)

			local var_37_0 = arg_32_0.step2.GetComponent(typeof(Image)).fillAmount
			local var_37_1 = arg_32_0.subPtDate[arg_32_0.curSubActID].count

			LeanTween.value(go(arg_32_0.step2), var_37_0, var_37_1 / var_0_1, 1).setOnUpdate(System.Action_float(function(arg_38_0)
				arg_32_0.step2.GetComponent(typeof(Image)).fillAmount = arg_38_0)).setOnComplete(System.Action(function()
				setActive(arg_32_0.anim, False)

				arg_32_0.heartAni = False))))

	local var_32_5 = arg_32_0.curActIndex == 1 and arg_32_0.model1 or arg_32_0.model2

	LeanTween.scale(var_32_1, Vector3(1, 1, 1), var_32_0).setFrom(Vector3(1, 0, 1)).setOnComplete(System.Action(function()
		setActive(var_32_5, True)
		var_32_5.GetComponent("SpineAnimUI").SetActionCallBack(function(arg_41_0)
			if arg_41_0 == "finish":
				var_32_5.GetComponent("SpineAnimUI").SetActionCallBack(None)
				setActive(var_32_5, False)
				var_32_4())
		var_32_5.GetComponent("SpineAnimUI").SetAction("event", 0)))

	arg_32_0.heartAni = False

	onButton(arg_32_0, arg_32_0.anim, function()
		if arg_32_0.heartAni:
			return

		var_32_5.GetComponent("SpineAnimUI").SetActionCallBack(None)
		setActive(var_32_5, False)

		arg_32_0.heartAni = True

		var_32_4(), SFX_PANEL)

def var_0_0.initTaskWindow(arg_43_0):
	arg_43_0.finishItemList = {}
	arg_43_0.finishTaskVOList = {}

	arg_43_0.uilist.make(function(arg_44_0, arg_44_1, arg_44_2)
		if arg_44_0 == UIItemList.EventUpdate:
			local var_44_0 = arg_44_1 + 1
			local var_44_1 = arg_43_0.findTF("item", arg_44_2)
			local var_44_2 = arg_43_0.curTask[var_44_0]
			local var_44_3 = arg_43_0.taskProxy.getTaskById(var_44_2) or arg_43_0.taskProxy.getFinishTaskById(var_44_2)

			assert(var_44_3, "without this task by id. " .. var_44_2)

			local var_44_4 = var_44_3.getConfig("award_display")[1]
			local var_44_5 = {
				type = var_44_4[1],
				id = var_44_4[2],
				count = var_44_4[3]
			}

			updateDrop(var_44_1, var_44_5)
			onButton(arg_43_0, var_44_1, function()
				arg_43_0.emit(BaseUI.ON_DROP, var_44_5), SFX_PANEL)

			local var_44_6 = var_44_3.getProgress()
			local var_44_7 = var_44_3.getConfig("target_num")

			setText(arg_43_0.findTF("description", arg_44_2), var_44_3.getConfig("desc"))
			setText(arg_43_0.findTF("progressText", arg_44_2), var_44_6 .. "/" .. var_44_7)
			setSlider(arg_43_0.findTF("progress", arg_44_2), 0, var_44_7, var_44_6)

			local var_44_8 = arg_43_0.findTF("go_btn", arg_44_2)
			local var_44_9 = var_44_3.getTaskStatus()

			if var_44_9 == 1:
				table.insert(arg_43_0.finishItemList, arg_44_2)
				table.insert(arg_43_0.finishTaskVOList, var_44_3)

			setActive(arg_43_0.findTF("finnal", arg_44_2), var_44_9 == 2)
			onButton(arg_43_0, var_44_8, function()
				arg_43_0.emit(ActivityMediator.ON_TASK_GO, var_44_3), SFX_PANEL)

			local var_44_10 = var_44_3.getConfig("type")

			setImageSprite(arg_43_0.findTF("type", arg_44_2), arg_43_0.typeImages.Find(tostring(var_44_10)).GetComponent(typeof(Image)).sprite, True)
			setImageSprite(arg_43_0.findTF("progress/slider", arg_44_2), arg_43_0.barImages.Find(tostring(var_44_10)).GetComponent(typeof(Image)).sprite))
	arg_43_0.uilist.align(#arg_43_0.curTask)
	setActive(arg_43_0.taskWindow, False)

def var_0_0.closeTask(arg_47_0):
	setActive(arg_47_0.taskWindow, False)

def var_0_0.openTask(arg_48_0):
	if not arg_48_0.curSubActID:
		arg_48_0.setPtActIndex()
		arg_48_0.setStep2Progress()

	setActive(arg_48_0.taskWindow, True)

	if arg_48_0.showTaskRedDot:
		setActive(arg_48_0.taskRedDot, False)
		getProxy(ActivityProxy).updateActivity(arg_48_0.activity)

	arg_48_0.hasClickTask = True

	eachChild(arg_48_0.items, function(arg_49_0)
		if isActive(arg_48_0.findTF("finnal", arg_49_0)):
			arg_49_0.SetAsLastSibling())

def var_0_0.autoFinishTask(arg_50_0):
	local var_50_0 = 0.01
	local var_50_1 = 0.5

	for iter_50_0, iter_50_1 in ipairs(arg_50_0.finishItemList):
		local var_50_2 = GetOrAddComponent(iter_50_1, typeof(CanvasGroup))

		arg_50_0.managedTween(LeanTween.delayedCall, function()
			iter_50_1.SetAsFirstSibling()
			LeanTween.value(go(iter_50_1), 1, 0, var_50_1).setOnUpdate(System.Action_float(function(arg_52_0)
				var_50_2.alpha = arg_52_0)).setOnComplete(System.Action(function()
				var_50_2.alpha = 1

				setActive(arg_50_0.findTF("finnal", iter_50_1), True)
				iter_50_1.SetAsLastSibling())), var_50_0, None)

		var_50_0 = var_50_0 + var_50_1 + 0.1

	arg_50_0.managedTween(LeanTween.delayedCall, function()
		pg.m02.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
			resultList = arg_50_0.finishTaskVOList
		}), var_50_0, None)

def var_0_0.canFinishTask(arg_55_0, arg_55_1):
	local var_55_0 = False

	for iter_55_0, iter_55_1 in pairs(arg_55_0):
		if (arg_55_1.getTaskById(iter_55_1) or arg_55_1.getFinishTaskById(iter_55_1)).getTaskStatus() == 1:
			var_55_0 = True

			break

	return var_55_0

def var_0_0.canAddProgress(arg_56_0, arg_56_1):
	local var_56_0 = False

	for iter_56_0, iter_56_1 in pairs(arg_56_1):
		local var_56_1, var_56_2, var_56_3 = iter_56_1.GetResProgress()

		if arg_56_0 >= var_56_2 - var_56_1 and iter_56_1.CanGetNextAward():
			var_56_0 = True

			break

	return var_56_0

def var_0_0.canGetPtAward(arg_57_0):
	local var_57_0 = False

	for iter_57_0, iter_57_1 in pairs(arg_57_0):
		if iter_57_1.CanGetAward():
			var_57_0 = True

			break

	return var_57_0

def var_0_0.isFinishAllAct(arg_58_0):
	local var_58_0 = True

	for iter_58_0, iter_58_1 in pairs(arg_58_0.subPtDate):
		if iter_58_1.CanGetNextAward():
			var_58_0 = False

			break

	return var_58_0

def var_0_0.isNewTask(arg_59_0):
	local var_59_0 = getProxy(PlayerProxy).getData().id
	local var_59_1 = PlayerPrefs.GetInt("wwf_todo_task_num_" .. var_59_0)

	if var_59_1 == 0 and not arg_59_0 == 0 or var_59_1 < arg_59_0:
		return True
	else
		return False

def var_0_0.IsShowRed():
	local var_60_0 = pg.activity_template[ActivityConst.WWF_TASK_ID]
	local var_60_1 = var_60_0.config_client.convertRes
	local var_60_2 = var_60_0.config_client.ptActID
	local var_60_3 = var_60_0.config_data
	local var_60_4 = {}

	for iter_60_0, iter_60_1 in ipairs(var_60_2):
		local var_60_5 = getProxy(ActivityProxy).getActivityById(iter_60_1)

		if var_60_4[iter_60_1]:
			var_60_4[iter_60_1].Update(var_60_5)
		else
			var_60_4[iter_60_1] = ActivityPtData.New(var_60_5)

	local var_60_6 = getProxy(PlayerProxy).getRawData().getResource(var_60_1)
	local var_60_7 = getProxy(TaskProxy)
	local var_60_8 = {}
	local var_60_9 = 0

	for iter_60_2, iter_60_3 in ipairs(var_60_3):
		local var_60_10 = var_60_7.getTaskById(iter_60_3) or var_60_7.getFinishTaskById(iter_60_3)

		if var_60_10:
			table.insert(var_60_8, var_60_10.id)

			if var_60_10.getTaskStatus() == 0:
				var_60_9 = var_60_9 + 1

	if (function()
		local var_61_0 = True

		for iter_61_0, iter_61_1 in pairs(var_60_4):
			if iter_61_1.CanGetNextAward():
				var_61_0 = False

				break

		return var_61_0)():
		return False
	else
		return var_0_0.canFinishTask(var_60_8, var_60_7) or var_0_0.canGetPtAward(var_60_4) or var_0_0.canAddProgress(var_60_6, var_60_4) or var_0_0.isNewTask(var_60_9)

	return False

def var_0_0.OnDestroy(arg_62_0):
	if arg_62_0.prefab1 and arg_62_0.model1:
		PoolMgr.GetInstance().ReturnSpineChar(arg_62_0.prefab1, arg_62_0.model1)

		arg_62_0.prefab1 = None
		arg_62_0.model1 = None

	if arg_62_0.prefab2 and arg_62_0.model2:
		PoolMgr.GetInstance().ReturnSpineChar(arg_62_0.prefab2, arg_62_0.model2)

		arg_62_0.prefab2 = None
		arg_62_0.model2 = None

	arg_62_0.cleanManagedTween()

return var_0_0
