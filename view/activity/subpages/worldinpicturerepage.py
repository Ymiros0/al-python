local var_0_0 = class("WorldInPictureRePage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.item = arg_1_0.findTF("items/item", arg_1_0.bg)
	arg_1_0.items = arg_1_0.findTF("items", arg_1_0.bg)
	arg_1_0.uilist = UIItemList.New(arg_1_0.items, arg_1_0.item)
	arg_1_0.help = arg_1_0.findTF("AD/help")
	arg_1_0.start = arg_1_0.findTF("AD/start")
	arg_1_0.dayTF = arg_1_0.findTF("Text", arg_1_0.bg)
	arg_1_0.tip = arg_1_0.findTF("AD/tip")

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)
	onButton(arg_2_0, arg_2_0.help, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.worldinpicture_task_help.tip
		}), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.start, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.WORLDINPICTURE), SFX_PANEL)

	arg_2_0.miniGameAct = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)

def var_0_0.UpdateTask(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_1 + 1
	local var_5_1 = arg_5_0.findTF("item", arg_5_2)
	local var_5_2 = arg_5_0.taskGroup[arg_5_0.nday][var_5_0]
	local var_5_3 = arg_5_0.taskProxy.getTaskById(var_5_2) or arg_5_0.taskProxy.getFinishTaskById(var_5_2)

	assert(var_5_3, "without this task by id. " .. var_5_2)

	local var_5_4 = var_5_3.getConfig("award_display")[1]
	local var_5_5 = {
		type = var_5_4[1],
		id = var_5_4[2],
		count = var_5_4[3]
	}

	updateDrop(var_5_1, var_5_5)
	onButton(arg_5_0, var_5_1, function()
		arg_5_0.emit(BaseUI.ON_DROP, var_5_5), SFX_PANEL)

	local var_5_6 = var_5_3.getProgress()
	local var_5_7 = var_5_3.getConfig("target_num")

	setText(arg_5_0.findTF("description", arg_5_2), var_5_3.getConfig("desc"))
	setSlider(arg_5_0.findTF("progress", arg_5_2), 0, var_5_7, var_5_6)

	local var_5_8 = arg_5_0.findTF("go_btn", arg_5_2)
	local var_5_9 = arg_5_0.findTF("get_btn", arg_5_2)
	local var_5_10 = arg_5_0.findTF("got_btn", arg_5_2)
	local var_5_11 = var_5_3.getTaskStatus()

	setActive(var_5_8, var_5_11 == 0)
	setActive(var_5_9, var_5_11 == 1)
	setActive(var_5_10, var_5_11 == 2)
	onButton(arg_5_0, var_5_8, function()
		arg_5_0.emit(ActivityMediator.ON_TASK_GO, var_5_3), SFX_PANEL)
	onButton(arg_5_0, var_5_9, function()
		arg_5_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_5_3), SFX_PANEL)
	setText(arg_5_0.findTF("progressText", arg_5_2), "<color=#789143>" .. var_5_6 .. "</color><color=#a3876f>/" .. var_5_7 .. "</color>")

def var_0_0.OnUpdateFlush(arg_9_0):
	var_0_0.super.OnUpdateFlush(arg_9_0)

	local var_9_0 = arg_9_0.miniGameAct
	local var_9_1 = var_9_0 and not var_9_0.isEnd() and var_9_0.readyToAchieve()

	setActive(arg_9_0.tip, var_9_1)

return var_0_0
