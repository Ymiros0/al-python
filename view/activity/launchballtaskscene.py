local var_0_0 = class("LaunchBallTaskScene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "LaunchBallTaskUI"

def var_0_0.getBGM(arg_2_0):
	return "cw-story"

def var_0_0.init(arg_3_0):
	arg_3_0.taskDatas = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_ZUMA_TASK).getConfig("config_client")
	arg_3_0.iconTpl = findTF(arg_3_0._tf, "ad/players/Viewport/Content/iconTpl")

	setActive(arg_3_0.iconTpl, False)

	arg_3_0.iconContent = findTF(arg_3_0._tf, "ad/players/Viewport/Content")
	arg_3_0.icons = {}

	for iter_3_0 = 1, #arg_3_0.taskDatas:
		local var_3_0 = tf(instantiate(arg_3_0.iconTpl))
		local var_3_1 = iter_3_0
		local var_3_2 = arg_3_0.taskDatas[iter_3_0].player
		local var_3_3 = LaunchBallActivityMgr.GetPlayerZhuanshuIndex(var_3_2)
		local var_3_4

		if var_3_3:
			var_3_4 = LaunchBallActivityMgr.CheckZhuanShuAble(ActivityConst.MINIGAME_ZUMA, var_3_3)
		else
			var_3_4 = True

		setActive(findTF(var_3_0, "lock"), not var_3_4)
		GetSpriteFromAtlasAsync("ui/launchballtaskui_atlas", "playerIcon" .. arg_3_0.taskDatas[iter_3_0].player, function(arg_4_0)
			if arg_4_0:
				setImageSprite(findTF(var_3_0, "img"), arg_4_0, True))
		setParent(var_3_0, arg_3_0.iconContent)
		setActive(var_3_0, True)
		onButton(arg_3_0, var_3_0, function()
			if var_3_4:
				arg_3_0.selectPlayer(var_3_2)
			else
				local var_5_0

				if var_3_2 == 2:
					var_5_0 = i18n("launchball_lock_Shinano")
				elif var_3_2 == 3:
					var_5_0 = i18n("launchball_lock_Yura")
				elif var_3_2 == 4:
					var_5_0 = i18n("launchball_lock_Shimakaze")

				pg.TipsMgr.GetInstance().ShowTips(var_5_0))
		table.insert(arg_3_0.icons, {
			tf = var_3_0,
			player = var_3_2
		})

	arg_3_0.taskTpl = findTF(arg_3_0._tf, "ad/tasks/Viewport/Content/taskTpl")
	arg_3_0.taskContent = findTF(arg_3_0._tf, "ad/tasks/Viewport/Content")

	setActive(arg_3_0.taskTpl, False)

	arg_3_0.tasks = {}

	onButton(arg_3_0, findTF(arg_3_0._tf, "ad/getAll"), function()
		if #arg_3_0.submitTasks > 1:
			arg_3_0.emit(LaunchBallTaskMediator.SUBMIT_ALL, arg_3_0.submitTasks))

	arg_3_0.helpWindow = findTF(arg_3_0._tf, "helpWindow")

	setActive(arg_3_0.helpWindow, False)
	onButton(arg_3_0, findTF(arg_3_0.helpWindow, "ad"), function()
		setActive(arg_3_0.helpWindow, False))
	onButton(arg_3_0, findTF(arg_3_0.helpWindow, "ad/btnOk"), function()
		setActive(arg_3_0.helpWindow, False))
	onButton(arg_3_0, findTF(arg_3_0._tf, "ad/back"), function()
		arg_3_0.closeView())
	arg_3_0.selectPlayer(1)

def var_0_0.selectPlayer(arg_10_0, arg_10_1):
	for iter_10_0 = 1, #arg_10_0.icons:
		local var_10_0 = arg_10_0.icons[iter_10_0].tf

		setActive(findTF(var_10_0, "selected"), arg_10_0.icons[iter_10_0].player == arg_10_1)

	local var_10_1 = arg_10_0.getTaskByPlayer(arg_10_1)

	arg_10_0.updateTaskList(var_10_1)

	arg_10_0.selectPlayerId = arg_10_1

def var_0_0.updateTaskList(arg_11_0, arg_11_1):
	arg_11_0.submitTasks = {}

	for iter_11_0 = 1, #arg_11_0.tasks:
		setActive(arg_11_0.tasks[iter_11_0].tf, False)

	local var_11_0 = {}

	for iter_11_1 = 1, #arg_11_1:
		local var_11_1 = arg_11_1[iter_11_1][2]
		local var_11_2 = arg_11_1[iter_11_1][1]
		local var_11_3 = getProxy(TaskProxy).getTaskById(var_11_1)
		local var_11_4 = getProxy(TaskProxy).getFinishTaskById(var_11_1)

		if var_11_3:
			table.insert(var_11_0, {
				data = var_11_3,
				type = var_11_2
			})
		elif var_11_4:
			table.insert(var_11_0, {
				data = var_11_4,
				type = var_11_2
			})

	table.sort(var_11_0, function(arg_12_0, arg_12_1)
		local var_12_0 = arg_12_0.data
		local var_12_1 = arg_12_1.data

		if var_12_0.getTaskStatus() == 1 and var_12_1.getTaskStatus() != 1:
			return True
		elif var_12_0.getTaskStatus() != 1 and var_12_1.getTaskStatus() == 1:
			return False
		elif var_12_0.getTaskStatus() == 2 and var_12_1.getTaskStatus() != 2:
			return False
		elif var_12_0.getTaskStatus() != 2 and var_12_1.getTaskStatus() == 2:
			return True
		else
			return var_12_0.id < var_12_1.id)

	for iter_11_2 = 1, #var_11_0:
		local var_11_5

		if iter_11_2 > #arg_11_0.tasks:
			var_11_5 = tf(instantiate(arg_11_0.taskTpl))

			setParent(var_11_5, arg_11_0.taskContent)
			setActive(var_11_5, True)
			table.insert(arg_11_0.tasks, {
				tf = var_11_5
			})
		else
			var_11_5 = arg_11_0.tasks[iter_11_2].tf

		local var_11_6 = var_11_0[iter_11_2].data
		local var_11_7 = var_11_0[iter_11_2].type
		local var_11_8 = var_11_6.id
		local var_11_9
		local var_11_10
		local var_11_11
		local var_11_12
		local var_11_13 = var_11_6.getProgress()
		local var_11_14 = var_11_6.getTargetNumber()
		local var_11_15 = var_11_6.getConfig("desc")
		local var_11_16 = var_11_6.getConfig("award_display")[1]

		setSlider(findTF(var_11_5, "Slider"), 0, 1, var_11_13 / var_11_14)

		local var_11_17 = {
			type = var_11_16[1],
			id = var_11_16[2],
			count = var_11_16[3]
		}

		updateDrop(findTF(var_11_5, "icon"), var_11_17)
		setActive(findTF(var_11_5, "icon"), True)
		setText(findTF(var_11_5, "desc"), var_11_15)
		setText(findTF(var_11_5, "progress"), var_11_13 .. "/" .. var_11_14)

		local var_11_18

		if var_11_7 == LaunchBallTaskMgr.type_series_split:
			var_11_18 = i18n("launchball_spilt_series")
		elif var_11_7 == LaunchBallTaskMgr.type_close_split:
			var_11_18 = i18n("launchball_spilt_mix")
		elif var_11_7 == LaunchBallTaskMgr.type_over_split:
			var_11_18 = i18n("launchball_spilt_over")
		elif var_11_7 == LaunchBallTaskMgr.type_many_split:
			var_11_18 = i18n("launchball_spilt_many")

		if var_11_18:
			setActive(findTF(var_11_5, "tip"), True)
		else
			setActive(findTF(var_11_5, "tip"), False)

		onButton(arg_11_0, findTF(var_11_5, "tip"), function()
			setText(findTF(arg_11_0.helpWindow, "ad/desc"), var_11_18)
			setActive(arg_11_0.helpWindow, True))
		setActive(findTF(var_11_5, "go"), var_11_6.getTaskStatus() == 0)
		setActive(findTF(var_11_5, "got"), var_11_6.getTaskStatus() == 2)
		setActive(findTF(var_11_5, "get"), var_11_6.getTaskStatus() == 1)
		onButton(arg_11_0, findTF(var_11_5, "go"), function()
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SIXTH_ANNIVERSARY_JP_DARK))
		onButton(arg_11_0, findTF(var_11_5, "get"), function()
			pg.m02.sendNotification(GAME.SUBMIT_TASK, var_11_8))
		setActive(var_11_5, True)

		if var_11_6.getTaskStatus() == 1:
			table.insert(arg_11_0.submitTasks, var_11_6)

	setActive(findTF(arg_11_0._tf, "ad/getAll"), #arg_11_0.submitTasks > 1)

def var_0_0.updateTasks(arg_16_0):
	arg_16_0.selectPlayer(arg_16_0.selectPlayerId)

def var_0_0.getTaskByPlayer(arg_17_0, arg_17_1):
	for iter_17_0 = 1, #arg_17_0.taskDatas:
		if arg_17_0.taskDatas[iter_17_0].player == arg_17_1:
			return arg_17_0.taskDatas[iter_17_0].task

def var_0_0.willExit(arg_18_0):
	return

return var_0_0
