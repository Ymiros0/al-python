local var_0_0 = class("CurlingGamePage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.progressTpl = arg_1_0.findTF("ProgressTpl")
	arg_1_0.progressTplContainer = arg_1_0.findTF("ProgressList")
	arg_1_0.progressUIItemList = UIItemList.New(arg_1_0.progressTplContainer, arg_1_0.progressTpl)
	arg_1_0.goBtn = arg_1_0.findTF("GoBtn")

def var_0_0.OnDataSetting(arg_2_0):
	local var_2_0 = arg_2_0.activity.getConfig("config_id")
	local var_2_1 = getProxy(MiniGameProxy).GetHubByHubId(var_2_0)

	arg_2_0.needCount = var_2_1.getConfig("reward_need")
	arg_2_0.leftCount = var_2_1.count
	arg_2_0.playedCount = var_2_1.usedtime
	arg_2_0.isGotAward = var_2_1.ultimate > 0
	arg_2_0.curDay = arg_2_0.leftCount + arg_2_0.playedCount

def var_0_0.OnFirstFlush(arg_3_0):
	arg_3_0.progressUIItemList.make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventUpdate:
			arg_4_1 = arg_4_1 + 1

			local var_4_0 = arg_3_0.findTF("Unlocked", arg_4_2)
			local var_4_1 = arg_3_0.findTF("Finished", arg_4_2)
			local var_4_2 = arg_3_0.findTF("Current", arg_4_2)

			setActive(var_4_2, arg_4_1 == arg_3_0.playedCount)

			if arg_4_1 <= arg_3_0.curDay:
				setActive(var_4_0, arg_4_1 > arg_3_0.playedCount)
				setActive(var_4_1, arg_4_1 <= arg_3_0.playedCount and arg_4_1 != arg_3_0.needCount)
			else
				setActive(var_4_0, False)
				setActive(var_4_1, False))
	arg_3_0.progressUIItemList.align(arg_3_0.needCount)
	onButton(arg_3_0, arg_3_0.goBtn, function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, 33), SFX_PANEL)
	arg_3_0.tryGetFinalAward()

def var_0_0.OnUpdateFlush(arg_6_0):
	return

def var_0_0.OnDestroy(arg_7_0):
	return

def var_0_0.tryGetFinalAward(arg_8_0):
	local var_8_0 = arg_8_0.activity.getConfig("config_id")
	local var_8_1 = getProxy(MiniGameProxy).GetHubByHubId(var_8_0)
	local var_8_2 = var_8_1.usedtime
	local var_8_3 = var_8_1.getConfig("reward_need")
	local var_8_4 = var_8_1.ultimate > 0

	if var_8_3 <= var_8_2 and not var_8_4:
		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_8_1.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

return var_0_0
