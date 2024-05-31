local var_0_0 = class("SandiegoReformPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.progress = arg_1_0.findTF("progress/left", arg_1_0.bg)
	arg_1_0.gameBtn = arg_1_0.findTF("start", arg_1_0.bg)
	arg_1_0.helpBtn = arg_1_0.findTF("mic", arg_1_0.bg)
	arg_1_0.getSign = arg_1_0.findTF("get", arg_1_0.bg)
	arg_1_0.days = arg_1_0.findTF("days", arg_1_0.bg)
	arg_1_0.nums = arg_1_0.findTF("count", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	local var_2_0 = arg_2_0.activity.getConfig("config_client")[1][1]

	if var_2_0 != None:
		pg.NewStoryMgr.GetInstance().Play(var_2_0)

def var_0_0.OnFirstFlush(arg_3_0):
	local var_3_0 = arg_3_0.activity
	local var_3_1 = var_3_0.getConfig("config_client")[3]

	setText(arg_3_0.nums, _.reduce(_.slice(var_3_1, 1, var_3_0.data2), 0, function(arg_4_0, arg_4_1)
		return arg_4_0 + arg_4_1))
	setActive(arg_3_0.getSign, var_3_0.data1 == 1)

	local var_3_2 = var_3_0.getConfig("config_data")[4]

	arg_3_0.progress.sizeDelta = Vector2.New(10 + 90 * math.max(var_3_0.data2 - 1, 0), arg_3_0.progress.sizeDelta.y)

	local var_3_3 = Color.New(1, 0.83, 0.15)
	local var_3_4 = Color.New(0.59, 0.62, 0.69)

	for iter_3_0 = 1, 7:
		local var_3_5 = arg_3_0.days.Find(iter_3_0)

		setTextColor(var_3_5, iter_3_0 <= var_3_0.data2 and var_3_3 or var_3_4)

	onButton(arg_3_0, arg_3_0.gameBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.LINK_LINK), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("link_link_help_tip")
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_7_0):
	return

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
