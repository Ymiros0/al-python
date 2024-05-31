local var_0_0 = class("USSkirmishRePage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.initUI()
	arg_1_0.initData()
	arg_1_0.addListener()

def var_0_0.OnFirstFlush(arg_2_0):
	return

def var_0_0.OnUpdateFlush(arg_3_0):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0.taskVOList):
		local var_3_0 = iter_3_1.state
		local var_3_1 = arg_3_0.progress.GetChild(iter_3_0 - 1)
		local var_3_2 = arg_3_0.findTF("Empty", var_3_1)
		local var_3_3 = arg_3_0.findTF("Full", var_3_1)

		if var_3_0 < SkirmishVO.StateClear:
			setActive(var_3_2, True)
			setActive(var_3_3, False)
		else
			setActive(var_3_2, False)
			setActive(var_3_3, True)

def var_0_0.initUI(arg_4_0):
	arg_4_0.bg = arg_4_0.findTF("AD")
	arg_4_0.progress = arg_4_0.findTF("Progress")
	arg_4_0.helpBtn = arg_4_0.findTF("HelpBtn")
	arg_4_0.battleBtn = arg_4_0.findTF("BattleBtn")

def var_0_0.initData(arg_5_0):
	arg_5_0.taskGroup = Clone(pg.activity_template[ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE].config_data)
	arg_5_0.taskCount = #arg_5_0.taskGroup
	arg_5_0.skirmishProxy = getProxy(SkirmishProxy)

	arg_5_0.skirmishProxy.UpdateSkirmishProgress()

	arg_5_0.taskVOList = Clone(arg_5_0.skirmishProxy.data)

def var_0_0.addListener(arg_6_0):
	onButton(arg_6_0, arg_6_0.helpBtn, function()
		if pg.gametip.help_tempesteve:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = pg.gametip.help_tempesteve.tip,
				weight = LayerWeightConst.TOP_LAYER
			}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.battleBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
			mapIdx = SkirmishProxy.SkirmishMap
		}), SFX_PANEL)

return var_0_0
