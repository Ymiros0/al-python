local var_0_0 = class("SettingsWorldPanle", import(".SettingsNotificationPanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsWorld"

def var_0_0.GetTitle(arg_2_0):
	return i18n("world_setting_title")

def var_0_0.GetTitleEn(arg_3_0):
	return "  / OPERATION SETTINGS"

def var_0_0.OnInit(arg_4_0):
	var_0_0.super.OnInit(arg_4_0)

	arg_4_0.worldbossProgressTip = findTF(arg_4_0._tf, "world_boss")

def var_0_0.OnItemSwitch(arg_5_0, arg_5_1, arg_5_2):
	getProxy(SettingsProxy).SetWorldFlag(arg_5_1.key, arg_5_2)

def var_0_0.GetDefaultValue(arg_6_0, arg_6_1):
	return getProxy(SettingsProxy).GetWorldFlag(arg_6_1.key)

def var_0_0.GetList(arg_7_0):
	return {
		{
			key = "story_tips",
			title = i18n("world_setting_quickmode"),
			desc = i18n("world_setting_quickmodetip")
		},
		{
			key = "consume_item",
			title = i18n("world_setting_submititem"),
			desc = i18n("world_setting_submititemtip")
		},
		{
			key = "auto_save_area",
			title = i18n("world_setting_mapauto"),
			desc = i18n("world_setting_mapautotip")
		}
	}

def var_0_0.DisplayWorldBossProgressTipSettings(arg_8_0):
	local var_8_0 = pg.NewStoryMgr.GetInstance().IsPlayed("WorldG190")

	setActive(arg_8_0.worldbossProgressTip, var_8_0)

	if var_8_0:
		arg_8_0.InitWorldBossProgressTipSettings()

def var_0_0.InitWorldBossProgressTipSettings(arg_9_0):
	local var_9_0 = arg_9_0.worldbossProgressTip
	local var_9_1 = arg_9_0.GetWorldBossProgressTipConfig()
	local var_9_2 = getProxy(SettingsProxy).GetWorldBossProgressTipFlag()

	local function var_9_3(arg_10_0, arg_10_1)
		local var_10_0 = tostring(var_9_1[arg_10_0])

		onToggle(arg_9_0, arg_10_1, function(arg_11_0)
			if arg_11_0:
				getProxy(SettingsProxy).WorldBossProgressTipFlag(var_10_0), SFX_PANEL)

		if var_10_0 == var_9_2:
			triggerToggle(arg_10_1, True)

	local var_9_4 = var_9_0.Find("notify_tpl")

	var_9_4.Find("mask/Text").GetComponent("ScrollText").SetText(i18n("world_boss_progress_tip_title"))

	for iter_9_0 = 1, #var_9_1:
		var_9_3(iter_9_0, var_9_4.Find(tostring(iter_9_0)))

	onButton(arg_9_0, var_9_4.Find("mask/Text"), function()
		pg.m02.sendNotification(NewSettingsMediator.SHOW_DESC, {
			desc = i18n("world_boss_progress_tip_desc")
		}), SFX_PANEL)

def var_0_0.GetWorldBossProgressTipConfig(arg_13_0):
	local var_13_0 = pg.gameset.joint_boss_ticket.description
	local var_13_1 = {}

	table.insert(var_13_1, "")

	local var_13_2 = var_13_0[1] + var_13_0[2]

	table.insert(var_13_1, var_13_0[1] .. "&" .. var_13_2)
	table.insert(var_13_1, var_13_2)

	return var_13_1

def var_0_0.OnUpdate(arg_14_0):
	var_0_0.super.OnUpdate(arg_14_0)
	arg_14_0.DisplayWorldBossProgressTipSettings()

return var_0_0
