local var_0_0 = class("SkinTemplatePage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.dayTF = arg_1_0.findTF("day", arg_1_0.bg)
	arg_1_0.item = arg_1_0.findTF("item", arg_1_0.bg)
	arg_1_0.items = arg_1_0.findTF("items", arg_1_0.bg)
	arg_1_0.uilist = UIItemList.New(arg_1_0.items, arg_1_0.item)

	setActive(arg_1_0.item, False)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.nday = 0
	arg_2_0.taskProxy = getProxy(TaskProxy)
	arg_2_0.taskGroup = arg_2_0.activity.getConfig("config_data")

	return updateActivityTaskStatus(arg_2_0.activity)

def var_0_0.OnFirstFlush(arg_3_0):
	arg_3_0.uilist.make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventUpdate:
			arg_3_0.UpdateTask(arg_4_1, arg_4_2))

def var_0_0.UpdateTask(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_1 + 1
	local var_5_1 = arg_5_0.findTF("item", arg_5_2)
	local var_5_2 = arg_5_0.taskGroup[arg_5_0.nday][var_5_0]
	local var_5_3 = arg_5_0.taskProxy.getTaskById(var_5_2) or arg_5_0.taskProxy.getFinishTaskById(var_5_2)

	assert(var_5_3, "without this task by id. " .. var_5_2)

	local var_5_4 = Drop.Create(var_5_3.getConfig("award_display")[1])

	updateDrop(var_5_1, var_5_4)
	onButton(arg_5_0, var_5_1, function()
		arg_5_0.emit(BaseUI.ON_DROP, var_5_4), SFX_PANEL)

	local var_5_5 = var_5_3.getProgress()
	local var_5_6 = var_5_3.getConfig("target_num")

	setText(arg_5_0.findTF("description", arg_5_2), var_5_3.getConfig("desc"))

	local var_5_7, var_5_8 = arg_5_0.GetProgressColor()
	local var_5_9

	var_5_9 = var_5_7 and setColorStr(var_5_5, var_5_7) or var_5_5

	local var_5_10

	var_5_10 = var_5_8 and setColorStr("/" .. var_5_6, var_5_8) or "/" .. var_5_6

	setText(arg_5_0.findTF("progressText", arg_5_2), var_5_9 .. var_5_10)
	setSlider(arg_5_0.findTF("progress", arg_5_2), 0, var_5_6, var_5_5)

	local var_5_11 = arg_5_0.findTF("go_btn", arg_5_2)
	local var_5_12 = arg_5_0.findTF("get_btn", arg_5_2)
	local var_5_13 = arg_5_0.findTF("got_btn", arg_5_2)
	local var_5_14 = var_5_3.getTaskStatus()

	setActive(var_5_11, var_5_14 == 0)
	setActive(var_5_12, var_5_14 == 1)
	setActive(var_5_13, var_5_14 == 2)
	onButton(arg_5_0, var_5_11, function()
		arg_5_0.emit(ActivityMediator.ON_TASK_GO, var_5_3), SFX_PANEL)
	onButton(arg_5_0, var_5_12, function()
		arg_5_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_5_3), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_9_0):
	arg_9_0.nday = arg_9_0.activity.data3

	arg_9_0.PlayStory()

	if arg_9_0.dayTF:
		setText(arg_9_0.dayTF, tostring(arg_9_0.nday))

	arg_9_0.uilist.align(#arg_9_0.taskGroup[arg_9_0.nday])

def var_0_0.PlayStory(arg_10_0):
	local var_10_0 = arg_10_0.activity.getConfig("config_client").story

	if checkExist(var_10_0, {
		arg_10_0.nday
	}, {
		1
	}):
		pg.NewStoryMgr.GetInstance().Play(var_10_0[arg_10_0.nday][1])

def var_0_0.OnDestroy(arg_11_0):
	eachChild(arg_11_0.items, function(arg_12_0)
		Destroy(arg_12_0))

def var_0_0.GetProgressColor(arg_13_0):
	return None

return var_0_0
