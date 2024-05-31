local var_0_0 = class("ItemShowPanel", import(".MsgboxSubPanel"))

var_0_0.ConfigData = {
	equipID = 908601,
	isOpen = True,
	title = "equipment_info_change_tip",
	icon_new = "equips/50860",
	icon_old = "equips/50860",
	name_new = "equipment_info_change_name_b",
	tip_old = "equipment_info_change_text_before",
	tip_new = "equipment_info_change_text_after",
	name_old = "equipment_info_change_name_a"
}

def var_0_0.getUIName(arg_1_0):
	return "ItemChangeNoticeBox"

def var_0_0.UpdateView(arg_2_0, arg_2_1):
	arg_2_0.PreRefresh(arg_2_1)

	rtf(arg_2_0.viewParent._window).sizeDelta = Vector2.New(1000, 638)

	local var_2_0 = arg_2_0.findTF("title", arg_2_0._tf)
	local var_2_1 = arg_2_0.findTF("icon_origin", arg_2_0._tf)
	local var_2_2 = arg_2_0.findTF("icon_now", arg_2_0._tf)
	local var_2_3 = arg_2_0.findTF("name_origin", arg_2_0._tf)
	local var_2_4 = arg_2_0.findTF("name_now", arg_2_0._tf)
	local var_2_5 = arg_2_0.findTF("before/Text", arg_2_0._tf)
	local var_2_6 = arg_2_0.findTF("after/Text", arg_2_0._tf)

	setText(var_2_0, i18n(var_0_0.ConfigData.title))
	setText(var_2_3, i18n(var_0_0.ConfigData.name_old))
	setText(var_2_4, i18n(var_0_0.ConfigData.name_new))
	setText(var_2_5, i18n(var_0_0.ConfigData.tip_old))
	setText(var_2_6, i18n(var_0_0.ConfigData.tip_new))
	setImageSprite(var_2_1, LoadSprite(var_0_0.ConfigData.icon_old))
	setImageSprite(var_2_2, LoadSprite(var_0_0.ConfigData.icon_new))
	arg_2_0.PostRefresh(arg_2_1)

return var_0_0
