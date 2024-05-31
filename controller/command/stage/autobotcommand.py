local var_0_0 = class("AutoBotCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.isActiveBot
	local var_1_2 = var_1_0.toggle
	local var_1_3 = var_1_0.system
	local var_1_4 = var_0_0.GetAutoBotMark(var_1_3)

	if var_0_0.autoBotSatisfied():
		if PlayerPrefs.GetInt("autoBotIsAcitve" .. var_1_4, 0) == not var_1_1:
			-- block empty
		else
			PlayerPrefs.SetInt("autoBotIsAcitve" .. var_1_4, not var_1_1 and 1 or 0)
			var_0_0.activeBotHelp(not var_1_1)
	elif not var_1_1:
		if var_1_2:
			onDelayTick(function()
				GetComponent(var_1_2, typeof(Toggle)).isOn = False, 0.1)

		pg.TipsMgr.GetInstance().ShowTips(i18n("auto_battle_limit_tip"))

	if var_1_1:
		arg_1_0.sendNotification(GAME.AUTO_SUB, {
			isActiveSub = True,
			system = var_1_3
		})

def var_0_0.autoBotSatisfied():
	local var_3_0 = getProxy(ChapterProxy)

	return var_3_0 and var_3_0.getChapterById(AUTO_ENABLE_CHAPTER).isClear()

def var_0_0.activeBotHelp(arg_4_0):
	local var_4_0 = getProxy(PlayerProxy)

	if not arg_4_0:
		if var_0_0.autoBotHelp:
			pg.MsgboxMgr.GetInstance().hide()

		return

	if var_4_0.botHelp:
		return

	var_0_0.autoBotHelp = True

	if getProxy(SettingsProxy).isTipAutoBattle():
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			showStopRemind = True,
			toggleStatus = True,
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_auto"),
			custom = {
				{
					text = "text_iknow",
					sound = SFX_CANCEL,
					def onCallback:()
						if pg.MsgboxMgr.GetInstance().stopRemindToggle.isOn:
							getProxy(SettingsProxy).setAutoBattleTip()
				}
			},
			def onClose:()
				var_0_0.autoBotHelp = False

				if pg.MsgboxMgr.GetInstance().stopRemindToggle.isOn:
					getProxy(SettingsProxy).setAutoBattleTip(),
			weight = LayerWeightConst.TOP_LAYER
		})

	var_4_0.botHelp = True

def var_0_0.GetAutoBotMark(arg_7_0):
	if arg_7_0 == SYSTEM_WORLD or arg_7_0 == SYSTEM_WORLD_BOSS:
		return "_" .. SYSTEM_WORLD
	elif arg_7_0 == SYSTEM_GUILD:
		return "_" .. SYSTEM_GUILD
	else
		return ""

return var_0_0
