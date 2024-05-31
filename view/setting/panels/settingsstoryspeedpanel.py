local var_0_0 = class("SettingsStorySpeedPanel", import(".SettingsBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsStorySpeed"

def var_0_0.GetTitle(arg_2_0):
	return i18n("story_setting_label")

def var_0_0.GetTitleEn(arg_3_0):
	return "  / AUTO SPEED"

def var_0_0.OnInit(arg_4_0):
	local var_4_0 = arg_4_0._tf.Find("speeds")

	arg_4_0.btns = {}

	for iter_4_0 = 1, var_4_0.childCount:
		local var_4_1 = var_4_0.GetChild(iter_4_0 - 1)

		onToggle(arg_4_0, var_4_1, function(arg_5_0)
			if arg_5_0:
				local var_5_0 = Story.STORY_AUTO_SPEED[iter_4_0]

				getProxy(SettingsProxy).SetStorySpeed(var_5_0), SFX_PANEL)
		setText(var_4_1.Find("Text"), i18n("setting_story_speed_" .. iter_4_0))

		arg_4_0.btns[iter_4_0] = var_4_1

def var_0_0.OnUpdate(arg_6_0):
	local var_6_0 = getProxy(SettingsProxy).GetStorySpeed()
	local var_6_1 = table.indexof(Story.STORY_AUTO_SPEED, var_6_0) or 2

	triggerToggle(arg_6_0.btns[var_6_1], True)

return var_0_0
