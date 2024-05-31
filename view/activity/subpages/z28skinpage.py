local var_0_0 = class("Z28SkinPage", import(".NewYearSnackPage"))

def var_0_0.OnDataSetting(arg_1_0):
	local var_1_0 = arg_1_0.activity.getConfig("config_id")
	local var_1_1 = getProxy(MiniGameProxy).GetHubByHubId(var_1_0)

	arg_1_0.needCount = var_1_1.getConfig("reward_need")
	arg_1_0.leftCount = var_1_1.count
	arg_1_0.playedCount = var_1_1.usedtime
	arg_1_0.isGotAward = var_1_1.ultimate > 0
	arg_1_0.curDay = arg_1_0.leftCount + arg_1_0.playedCount

def var_0_0.OnFirstFlush(arg_2_0):
	arg_2_0.progressUIItemList.make(function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_0 == UIItemList.EventUpdate:
			arg_3_1 = arg_3_1 + 1

			local var_3_0 = arg_2_0.findTF("Locked", arg_3_2)
			local var_3_1 = arg_2_0.findTF("Unlocked", arg_3_2)
			local var_3_2 = arg_2_0.findTF("Finished", arg_3_2)
			local var_3_3 = arg_2_0.findTF("FinalFinished", arg_3_2)

			setActive(var_3_0, arg_3_1 > arg_2_0.curDay)

			if arg_3_1 <= arg_2_0.curDay:
				setActive(var_3_1, arg_3_1 > arg_2_0.playedCount)
				setActive(var_3_2, arg_3_1 <= arg_2_0.playedCount and arg_3_1 != arg_2_0.needCount)
				setActive(var_3_3, arg_3_1 <= arg_2_0.playedCount and arg_3_1 == arg_2_0.needCount)
			else
				setActive(var_3_1, False)
				setActive(var_3_2, False)
				setActive(var_3_3, False))

	local var_2_0 = 36

	onButton(arg_2_0, arg_2_0.goBtn, function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, var_2_0, {
			def callback:()
				local var_5_0 = Context.New()

				SCENE.SetSceneInfo(var_5_0, SCENE.NEWYEAR_BACKHILL_2022)
				getProxy(ContextProxy).PushContext2Prev(var_5_0)
		}), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_xinnian2022_z28")
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_7_0):
	arg_7_0.progressUIItemList.align(arg_7_0.needCount)
	arg_7_0.tryGetFinalAward()

def var_0_0.OnDestroy(arg_8_0):
	return

def var_0_0.tryGetFinalAward(arg_9_0):
	local var_9_0 = arg_9_0.activity.getConfig("config_id")
	local var_9_1 = getProxy(MiniGameProxy).GetHubByHubId(var_9_0)
	local var_9_2 = var_9_1.usedtime
	local var_9_3 = var_9_1.getConfig("reward_need")
	local var_9_4 = var_9_1.ultimate > 0

	if var_9_3 <= var_9_2 and not var_9_4:
		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_9_1.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

return var_0_0
