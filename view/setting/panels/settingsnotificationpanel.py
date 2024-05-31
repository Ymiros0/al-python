local var_0_0 = class("SettingsNotificationPanel", import(".SettingsBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "SettingsNotifications"

def var_0_0.GetTitle(arg_2_0):
	return i18n("Settings_title_Notification")

def var_0_0.GetTitleEn(arg_3_0):
	return "  / ENABLE NOTIFICATIONS"

def var_0_0.OnInit(arg_4_0):
	arg_4_0.uilist = UIItemList.New(arg_4_0._tf.Find("options"), arg_4_0._tf.Find("options/notify_tpl"))

	arg_4_0.uilist.make(function(arg_5_0, arg_5_1, arg_5_2)
		if arg_5_0 == UIItemList.EventUpdate:
			arg_4_0.UpdateItem(arg_5_1 + 1, arg_5_2))

def var_0_0.UpdateItem(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.list[arg_6_1]

	arg_6_2.Find("mask/Text").GetComponent("ScrollText").SetText(var_6_0.title)
	onButton(arg_6_0, arg_6_2.Find("mask/Text"), function()
		pg.m02.sendNotification(NewSettingsMediator.SHOW_DESC, var_6_0), SFX_PANEL)
	removeOnToggle(arg_6_2.Find("on"))

	if arg_6_0.GetDefaultValue(var_6_0):
		triggerToggle(arg_6_2.Find("on"), True)
	else
		triggerToggle(arg_6_2.Find("off"), True)

	onToggle(arg_6_0, arg_6_2.Find("on"), function(arg_8_0)
		arg_6_0.OnItemSwitch(var_6_0, arg_8_0), SFX_UI_TAG, SFX_UI_CANCEL)
	arg_6_0.OnUpdateItem(var_6_0)
	arg_6_0.OnUpdateItemWithTr(var_6_0, arg_6_2)

def var_0_0.OnUpdateItem(arg_9_0, arg_9_1):
	return

def var_0_0.OnUpdateItemWithTr(arg_10_0, arg_10_1, arg_10_2):
	return

def var_0_0.OnItemSwitch(arg_11_0, arg_11_1, arg_11_2):
	pg.PushNotificationMgr.GetInstance().setSwitch(arg_11_1.id, arg_11_2)

def var_0_0.GetDefaultValue(arg_12_0, arg_12_1):
	return pg.PushNotificationMgr.GetInstance().isEnabled(arg_12_1.id)

def var_0_0.GetList(arg_13_0):
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in ipairs(pg.push_data_template.all):
		table.insert(var_13_0, pg.push_data_template[iter_13_1])

	return var_13_0

def var_0_0.OnUpdate(arg_14_0):
	arg_14_0.list = arg_14_0.GetList()

	arg_14_0.uilist.align(#arg_14_0.list)

return var_0_0
