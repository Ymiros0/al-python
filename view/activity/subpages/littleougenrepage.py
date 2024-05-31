local var_0_0 = class("LittleOuGenRePage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.heartTpl = arg_1_0.findTF("HeartTpl", arg_1_0.bg)
	arg_1_0.heartContainer = arg_1_0.findTF("HeartContainer", arg_1_0.bg)
	arg_1_0.heartUIItemList = UIItemList.New(arg_1_0.heartContainer, arg_1_0.heartTpl)

	arg_1_0.heartUIItemList.make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate:
			local var_2_0 = arg_2_1 + 1
			local var_2_1 = arg_1_0.ptData.GetLevelProgress()
			local var_2_2 = arg_1_0.findTF("Full", arg_2_2)

			setActive(var_2_2, not (var_2_1 < var_2_0)))

	arg_1_0.helpBtn = arg_1_0.findTF("help_btn", arg_1_0.bg)

	onButton(arg_1_0, arg_1_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.littleEugen_npc.tip
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_4_0):
	var_0_0.super.OnUpdateFlush(arg_4_0)

	local var_4_0, var_4_1 = arg_4_0.ptData.GetLevelProgress()

	arg_4_0.heartUIItemList.align(var_4_1)

	local var_4_2, var_4_3, var_4_4 = arg_4_0.ptData.GetLevelProgress()
	local var_4_5, var_4_6, var_4_7 = arg_4_0.ptData.GetResProgress()

	setText(arg_4_0.step, setColorStr(var_4_2, "#f8e6e2") .. " / " .. setColorStr(var_4_3, "#4e2c2b"))
	setText(arg_4_0.progress, (var_4_7 >= 1 and setColorStr(var_4_5, COLOR_GREEN) or setColorStr(var_4_5, "COLOR_GREEN")) .. "/" .. setColorStr(var_4_6, "#4e2c2b"))

	if arg_4_0.firstSliderInit:
		if LeanTween.isTweening(go(arg_4_0.slider)):
			LeanTween.cancel(go(arg_4_0.slider))

		local var_4_8 = GetComponent(arg_4_0.slider, typeof(Slider)).value
		local var_4_9 = arg_4_0.l1 != var_4_2 and 0 or arg_4_0.sliderValue

		LeanTween.value(go(arg_4_0.slider), var_4_9, var_4_7, 1).setOnUpdate(System.Action_float(function(arg_5_0)
			setSlider(arg_4_0.slider, 0, 1, arg_5_0)

			arg_4_0.sliderValue = arg_5_0))
	else
		setSlider(arg_4_0.slider, 0, 1, var_4_7)

		arg_4_0.firstSliderInit = True
		arg_4_0.sliderValue = var_4_7

	arg_4_0.l1 = var_4_2

	arg_4_0.updataTask()
	arg_4_0.sortTaskGroups()
	arg_4_0.updateTaskUI()

def var_0_0.updataTask(arg_6_0):
	for iter_6_0, iter_6_1 in ipairs(arg_6_0.taskGroups):
		for iter_6_2, iter_6_3 in ipairs(iter_6_1.tasks):
			local var_6_0 = arg_6_0.taskProxy.getFinishTaskById(iter_6_3.id) and 1 or 0
			local var_6_1 = arg_6_0.taskProxy.getTaskById(iter_6_3.id)
			local var_6_2 = 0

			if var_6_1:
				var_6_2 = var_6_1.getProgress()
				iter_6_1.progress = var_6_2 == 0 and iter_6_1.progress or var_6_2
			else
				var_6_2 = iter_6_1.progress

			iter_6_3.progress = var_6_2

			if iter_6_3.finish != var_6_0:
				setActive(iter_6_3.tf, False)
				table.insert(arg_6_0.taskTplPool, iter_6_3.tf)

				iter_6_3.tf = None

			iter_6_3.finish = var_6_0

def var_0_0.OnFirstFlush(arg_7_0):
	var_0_0.super.OnFirstFlush(arg_7_0)
	onButton(arg_7_0, arg_7_0.battleBtn, function()
		arg_7_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.LEVEL), SFX_PANEL)
	arg_7_0.initTask()
	arg_7_0.sortTaskGroups()
	arg_7_0.updateTaskUI()

def var_0_0.initTask(arg_9_0):
	arg_9_0.missionTpl = findTF(arg_9_0.bg, "missionTpl")

	setActive(arg_9_0.missionTpl, False)

	arg_9_0.missionContainer = findTF(arg_9_0.bg, "mission/content")

	local var_9_0 = arg_9_0.activity.getConfig("config_client").task_act_id
	local var_9_1 = pg.activity_template[var_9_0].config_data[1]

	arg_9_0.taskProxy = getProxy(TaskProxy)
	arg_9_0.taskTplPool = {}
	arg_9_0.taskScroll = GetComponent(findTF(arg_9_0.bg, "mission"), typeof(ScrollRect))
	arg_9_0.taskGroups = {}

	for iter_9_0 = 1, #var_9_1:
		local var_9_2 = var_9_1[iter_9_0]
		local var_9_3 = pg.task_data_template[var_9_2]

		if not var_9_3:
			print("task_data_template 不存在任务id . " .. tostring(var_9_2))

		local var_9_4 = var_9_3.type
		local var_9_5 = var_9_3.sub_type

		if var_9_4 == Task.TYPE_ACTIVITY or var_9_4 == Task.TYPE_ACTIVITY_BRANCH:
			local var_9_6 = arg_9_0.getTaskGroup(var_9_4, var_9_5)

			arg_9_0.insertTaskToGroup(var_9_2, var_9_3, var_9_6)

def var_0_0.updateTaskUI(arg_10_0):
	local var_10_0 = 0

	for iter_10_0 = 1, #arg_10_0.taskGroups:
		local var_10_1 = arg_10_0.taskGroups[iter_10_0]
		local var_10_2 = var_10_1.tasks

		for iter_10_1, iter_10_2 in ipairs(var_10_2):
			arg_10_0.updateTaskList(iter_10_1, var_10_0, iter_10_2, var_10_1)

			var_10_0 = var_10_0 + 1

	local var_10_3 = 0
	local var_10_4 = 0

	if arg_10_0.scrollToGroup:
		for iter_10_3, iter_10_4 in ipairs(arg_10_0.taskGroups):
			if iter_10_4 == arg_10_0.scrollToGroup:
				var_10_4 = var_10_3

			if iter_10_4.opening:
				var_10_3 = var_10_3 + #iter_10_4.tasks
			else
				var_10_3 = var_10_3 + 1

		arg_10_0.scrollToGroup = None

	if var_10_4 != 0 and var_10_3 != 0:
		scrollTo(arg_10_0.taskScroll, 0, 1 - var_10_4 / var_10_3)
	else
		scrollTo(arg_10_0.taskScroll, 0, 1)

def var_0_0.updateTaskList(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4):
	if not arg_11_3.show:
		return

	local var_11_0 = arg_11_3.targetNum
	local var_11_1 = arg_11_3.progress
	local var_11_2 = arg_11_3.finish == 1
	local var_11_3 = arg_11_1 == 1
	local var_11_4 = arg_11_3.desc
	local var_11_5 = arg_11_3.drop
	local var_11_6 = arg_11_4.opening
	local var_11_7 = #arg_11_4.tasks == 1

	if not arg_11_3.tf:
		arg_11_3.tf = arg_11_0.getTaskTfFromPool()

	local var_11_8 = findTF(arg_11_3.tf, "AD")

	arg_11_3.tf.sizeDelta = Vector2(778, var_11_3 and 120 or 110)

	setActive(findTF(var_11_8, "bg1"), var_11_3)
	setActive(findTF(var_11_8, "bg2"), not var_11_3)

	if var_11_3:
		setActive(findTF(var_11_8, "mask1"), var_11_2)
	else
		setActive(findTF(var_11_8, "mask2"), var_11_2)

	if var_11_2:
		setActive(findTF(var_11_8, "pahase"), False)
		setSlider(findTF(var_11_8, "slider"), 0, 1, 1)
	else
		setActive(findTF(var_11_8, "pahase"), True)
		setSlider(findTF(var_11_8, "slider"), 0, 1, var_11_1 / var_11_0)

	setText(findTF(var_11_8, "desc"), var_11_4)

	if arg_11_4.subType != 33:
		setText(findTF(var_11_8, "pahase"), setColorStr(var_11_1, "#95b345") .. "/" .. setColorStr(var_11_0, "#e9c9bd"))
	else
		setText(findTF(var_11_8, "pahase"), "")

	updateDrop(findTF(var_11_8, "award"), var_11_5)
	onButton(arg_11_0, findTF(var_11_8, "award"), function()
		arg_11_0.emit(BaseUI.ON_DROP, var_11_5), SFX_PANEL)
	setActive(findTF(var_11_8, "got"), False)
	setActive(findTF(var_11_8, "get"), False)
	setActive(findTF(var_11_8, "go"), False)

	if not var_11_3:
		setActive(findTF(var_11_8, "go"), not var_11_2)
		setActive(findTF(var_11_8, "got"), var_11_2)
	elif var_11_2:
		setActive(findTF(var_11_8, "got"), True)
	elif var_11_0 <= var_11_1:
		setActive(findTF(var_11_8, "get"), True)
		onButton(arg_11_0, findTF(var_11_8, "get"), function()
			local var_13_0 = arg_11_0.taskProxy.getTaskById(arg_11_3.id)

			if var_13_0:
				arg_11_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_13_0), SFX_CONFIRM)

		if not arg_11_0.nextTickFlag:
			onNextTick(function()
				triggerButton(findTF(var_11_8, "get"))

				arg_11_0.nextTickFlag = False)

			arg_11_0.nextTickFlag = True
	else
		setActive(findTF(var_11_8, "go"), True)
		onButton(arg_11_0, findTF(var_11_8, "go"), function()
			local var_15_0 = arg_11_0.taskProxy.getTaskById(arg_11_3.id)

			if var_15_0:
				arg_11_0.emit(ActivityMediator.ON_TASK_GO, var_15_0), SFX_CONFIRM)

	if var_11_7 or not var_11_3 or var_11_2 and var_11_3:
		setActive(findTF(var_11_8, "show"), False)
	else
		setActive(findTF(var_11_8, "show"), True)
		setActive(findTF(var_11_8, "show/on"), var_11_6)
		setActive(findTF(var_11_8, "show/off"), not var_11_6)

	if var_11_3:
		onButton(arg_11_0, findTF(var_11_8, "show"), function()
			arg_11_0.changeGroupOpening(arg_11_4), SFX_CONFIRM)

	setActive(arg_11_3.tf, True)
	arg_11_3.tf.SetSiblingIndex(arg_11_2)

def var_0_0.changeGroupOpening(arg_17_0, arg_17_1):
	arg_17_1.opening = not arg_17_1.opening

	for iter_17_0 = 1, #arg_17_1.tasks:
		local var_17_0 = arg_17_1.tasks[iter_17_0]

		if iter_17_0 == 1:
			var_17_0.show = True
		else
			var_17_0.show = arg_17_1.opening

		if not var_17_0.show and var_17_0.tf:
			setActive(var_17_0.tf, False)
			table.insert(arg_17_0.taskTplPool, var_17_0.tf)

			var_17_0.tf = None

	arg_17_0.scrollToGroup = arg_17_1

	arg_17_0.updateTaskUI()

def var_0_0.getTaskTfFromPool(arg_18_0):
	if #arg_18_0.taskTplPool > 0:
		return table.remove(arg_18_0.taskTplPool, 1)

	local var_18_0 = tf(Instantiate(arg_18_0.missionTpl))

	SetParent(var_18_0, arg_18_0.missionContainer)

	return var_18_0

def var_0_0.getTaskGroup(arg_19_0, arg_19_1, arg_19_2):
	for iter_19_0 = 1, #arg_19_0.taskGroups:
		local var_19_0 = arg_19_0.taskGroups[iter_19_0]

		if var_19_0.type == arg_19_1 and var_19_0.subType == arg_19_2:
			return var_19_0

	local var_19_1 = {
		opening = False,
		progress = 0,
		type = arg_19_1,
		subType = arg_19_2,
		tasks = {}
	}

	table.insert(arg_19_0.taskGroups, var_19_1)

	return var_19_1

def var_0_0.insertTaskToGroup(arg_20_0, arg_20_1, arg_20_2, arg_20_3):
	local var_20_0 = arg_20_3.tasks

	for iter_20_0 = 1, #var_20_0:
		if var_20_0[iter_20_0].id == arg_20_1:
			return

	local var_20_1 = arg_20_2.target_num
	local var_20_2 = arg_20_2.desc
	local var_20_3 = {
		type = arg_20_2.award_display[1][1],
		id = arg_20_2.award_display[1][2],
		count = arg_20_2.award_display[1][3]
	}
	local var_20_4 = False

	if #arg_20_3.tasks == 0:
		var_20_4 = True

	local var_20_5 = arg_20_0.taskProxy.getFinishTaskById(arg_20_1) and 1 or 0
	local var_20_6 = arg_20_0.taskProxy.getTaskById(arg_20_1)
	local var_20_7 = 0

	if var_20_6:
		var_20_7 = var_20_6.getProgress()
		arg_20_3.progress = var_20_7 == 0 and arg_20_3.progress or var_20_7
	else
		var_20_7 = arg_20_3.progress

	table.insert(arg_20_3.tasks, {
		id = arg_20_1,
		targetNum = var_20_1,
		show = var_20_4,
		finish = var_20_5,
		progress = var_20_7,
		desc = var_20_2,
		drop = var_20_3
	})

def var_0_0.sortTaskGroups(arg_21_0):
	for iter_21_0, iter_21_1 in ipairs(arg_21_0.taskGroups):
		table.sort(iter_21_1.tasks, function(arg_22_0, arg_22_1)
			if arg_22_0.finish != arg_22_1.finish:
				return arg_22_0.finish < arg_22_1.finish

			return arg_22_0.targetNum < arg_22_1.targetNum)

	table.sort(arg_21_0.taskGroups, function(arg_23_0, arg_23_1)
		local var_23_0 = arg_23_0.tasks
		local var_23_1 = arg_23_1.tasks
		local var_23_2 = 0
		local var_23_3 = arg_23_0.tasks[1].id
		local var_23_4 = 0
		local var_23_5 = 0
		local var_23_6 = 0
		local var_23_7 = arg_23_1.tasks[1].id
		local var_23_8 = 0
		local var_23_9 = 0

		for iter_23_0, iter_23_1 in ipairs(var_23_0):
			if var_23_2 == 0 and iter_23_1.finish == 0 and iter_23_1.progress >= iter_23_1.targetNum:
				var_23_2 = 1
				var_23_3 = iter_23_1.id

			var_23_4 = iter_23_1.finish == 1 and var_23_4 + 1 or var_23_4

		local var_23_10 = var_23_4 == #var_23_0 and 1 or 0

		for iter_23_2, iter_23_3 in ipairs(var_23_1):
			if var_23_6 == 0 and iter_23_3.finish == 0 and iter_23_3.progress >= iter_23_3.targetNum:
				var_23_6 = 1
				var_23_7 = iter_23_3.id

			var_23_8 = iter_23_3.finish == 1 and var_23_8 + 1 or var_23_8

		local var_23_11 = var_23_8 == #var_23_1 and 1 or 0

		if var_23_2 != var_23_6:
			return var_23_6 < var_23_2
		elif var_23_10 != var_23_11:
			return var_23_10 < var_23_11
		else
			return var_23_3 < var_23_7)

	for iter_21_2, iter_21_3 in ipairs(arg_21_0.taskGroups):
		local var_21_0 = iter_21_3.opening
		local var_21_1 = iter_21_3.tasks

		for iter_21_4 = 1, #var_21_1:
			local var_21_2 = var_21_1[iter_21_4]

			if iter_21_4 == 1:
				var_21_2.show = True
			elif var_21_0:
				var_21_2.show = True
			else
				var_21_2.show = False

def var_0_0.OnDestroy(arg_24_0):
	if LeanTween.isTweening(go(arg_24_0.slider)):
		LeanTween.cancel(go(arg_24_0.slider))

return var_0_0
