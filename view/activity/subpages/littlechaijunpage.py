local var_0_0 = class("LittleChaijunPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.helpBtn = arg_1_0.findTF("help_btn", arg_1_0.bg)

	onButton(arg_1_0, arg_1_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.littleChaijun_npc.tip
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_3_0):
	var_0_0.super.OnUpdateFlush(arg_3_0)

	local var_3_0, var_3_1, var_3_2 = arg_3_0.ptData.GetLevelProgress()
	local var_3_3, var_3_4, var_3_5 = arg_3_0.ptData.GetResProgress()

	setText(arg_3_0.step, setColorStr(var_3_0, "ebced8") .. " / " .. var_3_1)
	setText(arg_3_0.progress, (var_3_5 >= 1 and setColorStr(var_3_3, COLOR_GREEN) or setColorStr(var_3_3, "ebced8")) .. "/" .. var_3_4)

	if arg_3_0.firstSliderInit:
		if LeanTween.isTweening(go(arg_3_0.slider)):
			LeanTween.cancel(go(arg_3_0.slider))

		local var_3_6 = GetComponent(arg_3_0.slider, typeof(Slider)).value
		local var_3_7 = arg_3_0.l1 != var_3_0 and 0 or arg_3_0.sliderValue

		LeanTween.value(go(arg_3_0.slider), var_3_7, var_3_5, 1).setOnUpdate(System.Action_float(function(arg_4_0)
			setSlider(arg_3_0.slider, 0, 1, arg_4_0)

			arg_3_0.sliderValue = arg_4_0))
	else
		setSlider(arg_3_0.slider, 0, 1, var_3_5)

		arg_3_0.firstSliderInit = True
		arg_3_0.sliderValue = var_3_5

	arg_3_0.l1 = var_3_0

	arg_3_0.updataTask()
	arg_3_0.sortTaskGroups()
	arg_3_0.updateTaskUI()

def var_0_0.updataTask(arg_5_0):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0.taskGroups):
		for iter_5_2, iter_5_3 in ipairs(iter_5_1.tasks):
			local var_5_0 = arg_5_0.taskProxy.getFinishTaskById(iter_5_3.id) and 1 or 0
			local var_5_1 = arg_5_0.taskProxy.getTaskById(iter_5_3.id)
			local var_5_2 = 0

			if var_5_1:
				var_5_2 = var_5_1.getProgress()
				iter_5_1.progress = var_5_2 == 0 and iter_5_1.progress or var_5_2
			else
				var_5_2 = iter_5_1.progress

			iter_5_3.progress = var_5_2

			if iter_5_3.finish != var_5_0:
				setActive(iter_5_3.tf, False)
				table.insert(arg_5_0.taskTplPool, iter_5_3.tf)

				iter_5_3.tf = None

			iter_5_3.finish = var_5_0

def var_0_0.OnFirstFlush(arg_6_0):
	var_0_0.super.OnFirstFlush(arg_6_0)
	onButton(arg_6_0, arg_6_0.displayBtn, function()
		arg_6_0.emit(ActivityMediator.SHOW_AWARD_WINDOW, PtAwardWindow, {
			type = 5,
			dropList = arg_6_0.ptData.dropList,
			targets = arg_6_0.ptData.targets,
			level = arg_6_0.ptData.level,
			count = arg_6_0.ptData.count,
			resId = arg_6_0.ptData.resId
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.battleBtn, function()
		arg_6_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.LEVEL), SFX_PANEL)
	arg_6_0.initTask()
	arg_6_0.sortTaskGroups()
	arg_6_0.updateTaskUI()

def var_0_0.initTask(arg_9_0):
	arg_9_0.missionTpl = findTF(arg_9_0.bg, "missionTpl")

	setActive(arg_9_0.missionTpl, False)

	arg_9_0.missionContainer = findTF(arg_9_0.bg, "mission/content")

	local var_9_0 = arg_9_0.activity.getConfig("config_client").task_act_id
	local var_9_1 = pg.activity_template[var_9_0].config_data

	arg_9_0.taskProxy = getProxy(TaskProxy)
	arg_9_0.taskTplPool = {}
	arg_9_0.taskScroll = GetComponent(findTF(arg_9_0.bg, "mission"), typeof(ScrollRect))
	arg_9_0.taskGroups = {}

	for iter_9_0 = 1, #var_9_1:
		local var_9_2 = var_9_1[iter_9_0]
		local var_9_3 = pg.task_data_template[var_9_2]
		local var_9_4 = var_9_3.type
		local var_9_5 = var_9_3.sub_type

		if var_9_4 == 26:
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
		setText(findTF(var_11_8, "pahase"), setColorStr(var_11_1, "#b35845") .. "/" .. var_11_0)
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
	else
		setActive(findTF(var_11_8, "go"), True)
		onButton(arg_11_0, findTF(var_11_8, "go"), function()
			local var_14_0 = arg_11_0.taskProxy.getTaskById(arg_11_3.id)

			if var_14_0:
				arg_11_0.emit(ActivityMediator.ON_TASK_GO, var_14_0), SFX_CONFIRM)

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

def var_0_0.changeGroupOpening(arg_16_0, arg_16_1):
	arg_16_1.opening = not arg_16_1.opening

	for iter_16_0 = 1, #arg_16_1.tasks:
		local var_16_0 = arg_16_1.tasks[iter_16_0]

		if iter_16_0 == 1:
			var_16_0.show = True
		else
			var_16_0.show = arg_16_1.opening

		if not var_16_0.show and var_16_0.tf:
			setActive(var_16_0.tf, False)
			table.insert(arg_16_0.taskTplPool, var_16_0.tf)

			var_16_0.tf = None

	arg_16_0.scrollToGroup = arg_16_1

	arg_16_0.updateTaskUI()

def var_0_0.getTaskTfFromPool(arg_17_0):
	if #arg_17_0.taskTplPool > 0:
		return table.remove(arg_17_0.taskTplPool, 1)

	local var_17_0 = tf(Instantiate(arg_17_0.missionTpl))

	SetParent(var_17_0, arg_17_0.missionContainer)

	return var_17_0

def var_0_0.getTaskGroup(arg_18_0, arg_18_1, arg_18_2):
	for iter_18_0 = 1, #arg_18_0.taskGroups:
		local var_18_0 = arg_18_0.taskGroups[iter_18_0]

		if var_18_0.type == arg_18_1 and var_18_0.subType == arg_18_2:
			return var_18_0

	local var_18_1 = {
		opening = False,
		progress = 0,
		type = arg_18_1,
		subType = arg_18_2,
		tasks = {}
	}

	table.insert(arg_18_0.taskGroups, var_18_1)

	return var_18_1

def var_0_0.insertTaskToGroup(arg_19_0, arg_19_1, arg_19_2, arg_19_3):
	local var_19_0 = arg_19_3.tasks

	for iter_19_0 = 1, #var_19_0:
		if var_19_0[iter_19_0].id == arg_19_1:
			return

	local var_19_1 = arg_19_2.target_num
	local var_19_2 = arg_19_2.desc
	local var_19_3 = {
		type = arg_19_2.award_display[1][1],
		id = arg_19_2.award_display[1][2],
		count = arg_19_2.award_display[1][3]
	}
	local var_19_4 = False

	if #arg_19_3.tasks == 0:
		var_19_4 = True

	local var_19_5 = arg_19_0.taskProxy.getFinishTaskById(arg_19_1) and 1 or 0
	local var_19_6 = arg_19_0.taskProxy.getTaskById(arg_19_1)
	local var_19_7 = 0

	if var_19_6:
		var_19_7 = var_19_6.getProgress()
		arg_19_3.progress = var_19_7 == 0 and arg_19_3.progress or var_19_7
	else
		var_19_7 = arg_19_3.progress

	table.insert(arg_19_3.tasks, {
		id = arg_19_1,
		targetNum = var_19_1,
		show = var_19_4,
		finish = var_19_5,
		progress = var_19_7,
		desc = var_19_2,
		drop = var_19_3
	})

def var_0_0.sortTaskGroups(arg_20_0):
	for iter_20_0, iter_20_1 in ipairs(arg_20_0.taskGroups):
		table.sort(iter_20_1.tasks, function(arg_21_0, arg_21_1)
			if arg_21_0.finish != arg_21_1.finish:
				return arg_21_0.finish < arg_21_1.finish

			return arg_21_0.targetNum < arg_21_1.targetNum)

	table.sort(arg_20_0.taskGroups, function(arg_22_0, arg_22_1)
		local var_22_0 = arg_22_0.tasks
		local var_22_1 = arg_22_1.tasks
		local var_22_2 = 0
		local var_22_3 = arg_22_0.tasks[1].id
		local var_22_4 = 0
		local var_22_5 = 0
		local var_22_6 = 0
		local var_22_7 = arg_22_1.tasks[1].id
		local var_22_8 = 0
		local var_22_9 = 0

		for iter_22_0, iter_22_1 in ipairs(var_22_0):
			if var_22_2 == 0 and iter_22_1.finish == 0 and iter_22_1.progress >= iter_22_1.targetNum:
				var_22_2 = 1
				var_22_3 = iter_22_1.id

			var_22_4 = iter_22_1.finish == 1 and var_22_4 + 1 or var_22_4

		local var_22_10 = var_22_4 == #var_22_0 and 1 or 0

		for iter_22_2, iter_22_3 in ipairs(var_22_1):
			if var_22_6 == 0 and iter_22_3.finish == 0 and iter_22_3.progress >= iter_22_3.targetNum:
				var_22_6 = 1
				var_22_7 = iter_22_3.id

			var_22_8 = iter_22_3.finish == 1 and var_22_8 + 1 or var_22_8

		local var_22_11 = var_22_8 == #var_22_1 and 1 or 0

		if var_22_2 != var_22_6:
			return var_22_6 < var_22_2
		elif var_22_10 != var_22_11:
			return var_22_10 < var_22_11
		else
			return var_22_3 < var_22_7)

	for iter_20_2, iter_20_3 in ipairs(arg_20_0.taskGroups):
		local var_20_0 = iter_20_3.opening
		local var_20_1 = iter_20_3.tasks

		for iter_20_4 = 1, #var_20_1:
			local var_20_2 = var_20_1[iter_20_4]

			if iter_20_4 == 1:
				var_20_2.show = True
			elif var_20_0:
				var_20_2.show = True
			else
				var_20_2.show = False

def var_0_0.OnDestroy(arg_23_0):
	if LeanTween.isTweening(go(arg_23_0.slider)):
		LeanTween.cancel(go(arg_23_0.slider))

return var_0_0
