local var_0_0 = class("ShinanoframeRePage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.goBtn = arg_1_0.findTF("GoBtn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("GetBtn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("GotBtn", arg_1_0.bg)
	arg_1_0.gotTag = arg_1_0.findTF("got", arg_1_0.bg)
	arg_1_0.cur = arg_1_0.findTF("cur", arg_1_0.bg)
	arg_1_0.max = arg_1_0.findTF("max", arg_1_0.bg)
	arg_1_0.progressBar = arg_1_0.findTF("progress", arg_1_0.bg)

	setActive(arg_1_0.goBtn, False)
	setActive(arg_1_0.getBtn, False)
	setActive(arg_1_0.gotBtn, False)
	setActive(arg_1_0.gotTag, False)

def var_0_0.OnDataSetting(arg_2_0):
	return

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.goBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK, {}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_OPERATION, {
			cmd = 1,
			activity_id = arg_3_0.activity.id
		}), SFX_PANEL)

	local var_3_0 = pg.activity_event_avatarframe[arg_3_0.activity.getConfig("config_id")].icon_frame
	local var_3_1 = LoadAndInstantiateSync("IconFrame", var_3_0)

	setParent(var_3_1, findTF(arg_3_0.bg, "icon"), False)

def var_0_0.OnUpdateFlush(arg_6_0):
	local var_6_0 = arg_6_0.activity.data1
	local var_6_1 = pg.activity_event_avatarframe[arg_6_0.activity.getConfig("config_id")].target

	if var_6_1 < var_6_0:
		var_6_0 = var_6_1

	local var_6_2 = var_6_0 / var_6_1

	setText(arg_6_0.cur, var_6_0)
	setText(arg_6_0.max, "/" .. var_6_1)
	setSlider(arg_6_0.progressBar, 0, 1, var_6_2)
	setActive(arg_6_0.progressBar, True)

	local var_6_3 = var_6_1 <= var_6_0
	local var_6_4 = arg_6_0.activity.data2 >= 1

	setActive(arg_6_0.goBtn, not var_6_3)
	setActive(arg_6_0.getBtn, not var_6_4 and var_6_3)
	setActive(arg_6_0.gotBtn, var_6_4)
	setActive(arg_6_0.gotTag, var_6_4)

def var_0_0.OnDestroy(arg_7_0):
	return

return var_0_0
