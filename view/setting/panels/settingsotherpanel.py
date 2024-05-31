local var_0_0 = class("SettingsOtherPanel", import(".SettingsNotificationPanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsOther"

def var_0_0.GetTitle(arg_2_0):
	return i18n("Settings_title_Other")

def var_0_0.GetTitleEn(arg_3_0):
	return "  / OTHER SETTINGS"

def var_0_0.OnInit(arg_4_0, ...):
	var_0_0.super.OnInit(arg_4_0, ...)

	local var_4_0 = PlayerPrefs.GetInt("AUTOFIGHT_BATTERY_SAVEMODE", 0) > 0
	local var_4_1 = pg.BrightnessMgr.GetInstance().IsPermissionGranted()

	if var_4_0 and not var_4_1:
		PlayerPrefs.SetInt("AUTOFIGHT_BATTERY_SAVEMODE", 0)
		PlayerPrefs.Save()

def var_0_0.OnItemSwitch(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_1.id == 1:
		pg.PushNotificationMgr.GetInstance().setSwitchShipName(arg_5_2)
	elif arg_5_1.id == 5:
		arg_5_0.OnClickEffectItemSwitch(arg_5_1, arg_5_2)
	elif arg_5_1.id == 9:
		arg_5_0.OnAutoFightBatterySaveModeItemSwitch(arg_5_1, arg_5_2)
	elif arg_5_1.id == 10:
		arg_5_0.OnAutoFightDownFrameItemSwitch(arg_5_1, arg_5_2)
	elif arg_5_1.type == 0:
		arg_5_0.OnCommonLocalItemSwitch(arg_5_1, arg_5_2)
	elif arg_5_1.type == 1:
		arg_5_0.OnCommonServerItemSwitch(arg_5_1, arg_5_2)

def var_0_0.OnClickEffectItemSwitch(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = pg.UIMgr.GetInstance().OverlayEffect

	if var_6_0:
		setActive(var_6_0, arg_6_2)

	arg_6_0.OnCommonLocalItemSwitch(arg_6_1, arg_6_2)

def var_0_0.OnCommonServerItemSwitch(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = _G[arg_7_1.name]
	local var_7_1 = getProxy(PlayerProxy).getRawData().GetCommonFlag(var_7_0)
	local var_7_2 = not arg_7_2

	if arg_7_1.default == 1:
		var_7_2 = arg_7_2

	if var_7_2:
		pg.m02.sendNotification(GAME.CANCEL_COMMON_FLAG, {
			flagID = var_7_0
		})
	else
		pg.m02.sendNotification(GAME.COMMON_FLAG, {
			flagID = var_7_0
		})

def var_0_0.OnAutoFightBatterySaveModeItemSwitch(arg_8_0, arg_8_1, arg_8_2):
	local function var_8_0()
		local var_9_0 = arg_8_0.uilist.container.GetChild(arg_8_1.id - 1)

		triggerToggle(var_9_0.Find("off"), True)

	local var_8_1 = pg.BrightnessMgr.GetInstance()

	seriesAsync({
		function(arg_10_0)
			if not arg_8_2 or var_8_1.IsPermissionGranted():
				return arg_10_0()

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("words_autoFight_right"),
				def onYes:()
					var_8_1.RequestPremission(function(arg_12_0)
						if arg_12_0:
							arg_10_0()
						else
							var_8_0()),
				onNo = var_8_0
			}),
		function(arg_13_0)
			local var_13_0 = _G[arg_8_1.name]

			PlayerPrefs.SetInt(var_13_0, arg_8_2 and 1 or 0)
			PlayerPrefs.Save()

			local var_13_1 = arg_8_0.uilist.container.GetChild(arg_8_1.id)

			triggerToggle(var_13_1.Find(arg_8_2 and "on" or "off"), True)
			var_0_0.SetGrayOption(var_13_1, arg_8_2)
	})

def var_0_0.OnAutoFightDownFrameItemSwitch(arg_14_0, arg_14_1, arg_14_2):
	if not arg_14_0.GetDefaultValue(arg_14_0.list[9]) and arg_14_2:
		pg.TipsMgr.GetInstance().ShowTips(i18n("words_autoFight_tips"))

		local var_14_0 = arg_14_0.uilist.container.GetChild(arg_14_1.id - 1)

		triggerToggle(var_14_0.Find("off"), True)

		return

	local var_14_1 = _G[arg_14_1.name]

	PlayerPrefs.SetInt(var_14_1, arg_14_2 and 1 or 0)
	PlayerPrefs.Save()

def var_0_0.SetGrayOption(arg_15_0, arg_15_1):
	setGray(arg_15_0.Find("on"), not arg_15_1)
	setGray(arg_15_0.Find("off"), not arg_15_1)

def var_0_0.OnCommonLocalItemSwitch(arg_16_0, arg_16_1, arg_16_2):
	local var_16_0 = _G[arg_16_1.name]

	PlayerPrefs.SetInt(var_16_0, arg_16_2 and 1 or 0)
	PlayerPrefs.Save()

def var_0_0.OnUpdateItem(arg_17_0, arg_17_1):
	if arg_17_1.id == 10:
		local var_17_0 = arg_17_0.uilist.container.GetChild(arg_17_1.id - 1)

		var_0_0.SetGrayOption(var_17_0, arg_17_0.GetDefaultValue(arg_17_0.list[9]))

def var_0_0.OnUpdateItemWithTr(arg_18_0, arg_18_1, arg_18_2):
	local var_18_0 = findTF(arg_18_2, "mask/tip")

	setActive(var_18_0, False)

	if arg_18_1.id == 18:
		onButton(arg_18_0, var_18_0, function()
			pg.m02.sendNotification(NewSettingsMediator.SHOW_DESC, arg_18_1), SFX_PANEL)
		setActive(var_18_0, True)

def var_0_0.GetDefaultValue(arg_20_0, arg_20_1):
	if arg_20_1.id == 1:
		return pg.PushNotificationMgr.GetInstance().isEnableShipName()
	elif arg_20_1.id == 17:
		return getProxy(SettingsProxy).IsDisplayResultPainting()
	elif arg_20_1.type == 0:
		return PlayerPrefs.GetInt(_G[arg_20_1.name], arg_20_1.default or 0) > 0
	elif arg_20_1.type == 1:
		local var_20_0 = getProxy(PlayerProxy).getRawData().GetCommonFlag(_G[arg_20_1.name])

		if arg_20_1.default == 1:
			return not var_20_0
		else
			return var_20_0

def var_0_0.GetList(arg_21_0):
	local var_21_0 = {}

	for iter_21_0, iter_21_1 in ipairs(pg.settings_other_template.all):
		if LOCK_BATTERY_SAVEMODE and (iter_21_1 == 9 or iter_21_1 == 10):
			-- block empty
		elif LOCK_L2D_GYRO and iter_21_1 == 15:
			-- block empty
		else
			table.insert(var_21_0, pg.settings_other_template[iter_21_1])

	return var_21_0

return var_0_0
