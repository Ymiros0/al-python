local var_0_0 = class("DockyardQuickSelectSettingPage", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "DockyardQuickSelectSettingUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitUI()

def var_0_0.InitUI(arg_3_0):
	setText(findTF(arg_3_0._tf, "window/top/bg/obtain/title"), i18n("retire_title"))

	local var_3_0 = {
		findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_1"),
		findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_2"),
		findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_3")
	}
	local var_3_1 = {
		sr = 4,
		n = 2,
		empty = 0,
		r = 3
	}
	local var_3_2 = {}

	for iter_3_0 = 1, #var_3_0:
		var_3_2[iter_3_0] = {}

		for iter_3_1, iter_3_2 in pairs(var_3_1):
			var_3_2[iter_3_0][iter_3_1] = findTF(var_3_0[iter_3_0], iter_3_1)

	for iter_3_3 = 1, #var_3_0:
		for iter_3_4, iter_3_5 in pairs(var_3_1):
			onToggle(arg_3_0, var_3_2[iter_3_3][iter_3_4], function(arg_4_0)
				local var_4_0 = var_3_2[iter_3_3][iter_3_4].GetComponent(typeof(Toggle))

				if arg_4_0:
					arg_3_0.settingChanged = True

					PlayerPrefs.SetInt("QuickSelectRarity" .. iter_3_3, iter_3_5)
				elif not var_4_0.group.AnyTogglesOn():
					triggerToggle(var_3_2[iter_3_3].empty, True))

	local var_3_3 = findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_4")

	onToggle(arg_3_0, findTF(var_3_3, "keep_all"), function(arg_5_0)
		if arg_5_0:
			arg_3_0.settingChanged = True

			PlayerPrefs.SetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepAll"))
	onToggle(arg_3_0, findTF(var_3_3, "keep_one"), function(arg_6_0)
		if arg_6_0:
			arg_3_0.settingChanged = True

			PlayerPrefs.SetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepOne"))
	onToggle(arg_3_0, findTF(var_3_3, "keep_none"), function(arg_7_0)
		if arg_7_0:
			arg_3_0.settingChanged = True

			PlayerPrefs.SetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepNone"))

	local var_3_4 = findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_5")

	onToggle(arg_3_0, findTF(var_3_4, "keep_all"), function(arg_8_0)
		if arg_8_0:
			arg_3_0.settingChanged = True

			PlayerPrefs.SetString("QuickSelectWithoutMaxstar", "KeepAll"))
	onToggle(arg_3_0, findTF(var_3_4, "keep_needed"), function(arg_9_0)
		if arg_9_0:
			arg_3_0.settingChanged = True

			PlayerPrefs.SetString("QuickSelectWithoutMaxstar", "KeepNeeded"))
	onToggle(arg_3_0, findTF(var_3_4, "keep_none"), function(arg_10_0)
		if arg_10_0:
			arg_3_0.settingChanged = True

			PlayerPrefs.SetString("QuickSelectWithoutMaxstar", "KeepNone"))
	onButton(arg_3_0, findTF(arg_3_0._tf, "window/top/btnBack"), function()
		arg_3_0.Hide(), SFX_CANCEL)
	onButton(arg_3_0, findTF(arg_3_0._tf, "window/top/bg/obtain/title/title_en/info"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("retire_setting_help")
		}), SFX_CONFIRM)

	local var_3_5 = PlayerPrefs.GetString("QuickSelectWhenHasAtLeastOneMaxstar", "KeepNone")
	local var_3_6 = PlayerPrefs.GetString("QuickSelectWithoutMaxstar", "KeepAll")

	if var_3_5 == "KeepAll":
		triggerToggle(findTF(var_3_3, "keep_all"), True)
	elif var_3_5 == "KeepOne":
		triggerToggle(findTF(var_3_3, "keep_one"), True)
	elif var_3_5 == "KeepNone":
		triggerToggle(findTF(var_3_3, "keep_none"), True)

	if var_3_6 == "KeepAll":
		triggerToggle(findTF(var_3_4, "keep_all"), True)
	elif var_3_6 == "KeepNeeded":
		triggerToggle(findTF(var_3_4, "keep_needed"), True)
	elif var_3_6 == "KeepNone":
		triggerToggle(findTF(var_3_4, "keep_none"), True)

	setText(findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_4/Text"), i18n("retire_1"))
	setText(findTF(arg_3_0._tf, "window/notifications/options/notify_tpl_5/Text"), i18n("retire_2"))

	local var_3_7 = {
		PlayerPrefs.GetInt("QuickSelectRarity1", 3),
		PlayerPrefs.GetInt("QuickSelectRarity2", 4),
		PlayerPrefs.GetInt("QuickSelectRarity3", 2)
	}

	for iter_3_6 = 1, #var_3_0:
		setText(findTF(var_3_0[iter_3_6], "Text"), i18n("retire_rarity", iter_3_6))

		for iter_3_7, iter_3_8 in pairs(var_3_1):
			if iter_3_8 == var_3_7[iter_3_6]:
				triggerToggle(var_3_2[iter_3_6][iter_3_7], True)

def var_0_0.Show(arg_13_0):
	setActive(arg_13_0._tf, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_13_0._tf)

def var_0_0.Hide(arg_14_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_14_0._tf, arg_14_0._parentTf)
	setActive(arg_14_0._tf, False)

	if arg_14_0.settingChangedCB:
		arg_14_0.settingChangedCB()

def var_0_0.OnDestroy(arg_15_0):
	arg_15_0.settingChangedCB = None

def var_0_0.OnSettingChanged(arg_16_0, arg_16_1):
	arg_16_0.settingChangedCB = arg_16_1

return var_0_0
