local var_0_0 = class("JiuJiuExpeditionPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.slider = arg_1_0.findTF("slider", arg_1_0.bg)
	arg_1_0.step = arg_1_0.findTF("step", arg_1_0.bg)
	arg_1_0.progress = arg_1_0.findTF("progress", arg_1_0.bg)
	arg_1_0.awardTF = arg_1_0.findTF("award", arg_1_0.bg)
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("got_btn", arg_1_0.bg)
	arg_1_0.help = arg_1_0.findTF("help", arg_1_0.bg)
	arg_1_0.book = arg_1_0.findTF("book", arg_1_0.bg)
	arg_1_0.startGame = arg_1_0.findTF("startGame", arg_1_0.bg)
	arg_1_0.desc = arg_1_0.findTF("desc", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	local var_2_0 = arg_2_0.activity.getConfig("config_data")

	arg_2_0.taskIDList = _.flatten(var_2_0)
	arg_2_0.dropList = {}
	arg_2_0.descs = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.taskIDList):
		local var_2_1 = pg.task_data_template[iter_2_1].award_display[1]

		table.insert(arg_2_0.dropList, Clone(var_2_1))

		local var_2_2 = pg.task_data_template[iter_2_1].desc

		table.insert(arg_2_0.descs, var_2_2)

	return updateActivityTaskStatus(arg_2_0.activity)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		if arg_3_0.curTaskVO:
			arg_3_0.emit(ActivityMediator.ON_TASK_GO, arg_3_0.curTaskVO), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		arg_3_0.emit(ActivityMediator.ON_TASK_SUBMIT, arg_3_0.curTaskVO), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.help, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.jiujiu_expedition_help.tip
		}), SFX_PANEL)

	if PLATFORM_CODE != PLATFORM_JP:
		setActive(arg_3_0.book, False)
	else
		local var_3_0, var_3_1, var_3_2, var_3_3 = JiuJiuExpeditionCollectionMediator.GetCollectionData()

		setActive(findTF(arg_3_0.book, "tip"), var_3_3 < var_3_2)
		onButton(arg_3_0, arg_3_0.book, function()
			arg_3_0.emit(ActivityMediator.OPEN_LAYER, Context.New({
				viewComponent = JiuJiuExpeditionCollectionLayer,
				mediator = JiuJiuExpeditionCollectionMediator
			})), SFX_PANEL)

	onButton(arg_3_0, arg_3_0.startGame, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.JIUJIU_EXPEDITION), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_9_0):
	local var_9_0, var_9_1 = getActivityTask(arg_9_0.activity)

	arg_9_0.curTaskVO = var_9_1

	setText(arg_9_0.desc, arg_9_0.curTaskVO.getConfig("desc"))

	local var_9_2 = var_9_1.getConfig("award_display")[1]
	local var_9_3 = {
		type = var_9_2[1],
		id = var_9_2[2],
		count = var_9_2[3]
	}

	updateDrop(arg_9_0.awardTF, var_9_3)
	onButton(arg_9_0, arg_9_0.awardTF, function()
		arg_9_0.emit(BaseUI.ON_DROP, var_9_3), SFX_PANEL)

	local var_9_4 = var_9_1.getProgress()
	local var_9_5 = var_9_1.getConfig("target_num")

	setText(arg_9_0.progress, (var_9_5 <= var_9_4 and setColorStr(var_9_4, COLOR_GREEN) or var_9_4) .. "/" .. var_9_5)
	setSlider(arg_9_0.slider, 0, var_9_5, var_9_4)

	local var_9_6 = table.indexof(arg_9_0.taskIDList, var_9_0, 1)

	setText(arg_9_0.step, var_9_6 .. "/" .. #arg_9_0.taskIDList)

	local var_9_7 = var_9_1.getTaskStatus()

	setActive(arg_9_0.battleBtn, var_9_7 == 0)
	setActive(arg_9_0.getBtn, var_9_7 == 1)
	setActive(arg_9_0.gotBtn, var_9_7 == 2)

	if var_9_7 == 2:
		arg_9_0.finishedIndex = var_9_6
	else
		arg_9_0.finishedIndex = var_9_6 - 1

def var_0_0.OnDestroy(arg_11_0):
	return

return var_0_0
