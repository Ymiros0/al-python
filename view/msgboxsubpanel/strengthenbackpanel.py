local var_0_0 = class("StrengthenBackPanel", import(".MsgboxSubPanel"))

var_0_0.ConfigData = {
	equipID = 96000,
	btnTxt = "text_forward",
	isOpen = True,
	icon = "equips/56000",
	content = "equipment_info_change_strengthen"
}

def var_0_0.getUIName(arg_1_0):
	return "StrengthenBackBox"

def var_0_0.UpdateView(arg_2_0, arg_2_1):
	arg_2_0.PreRefresh(arg_2_1)

	rtf(arg_2_0.viewParent._window).sizeDelta = Vector2.New(1000, 638)

	local var_2_0 = arg_2_0.findTF("info_view/Viewport/Content/Text", arg_2_0._tf)
	local var_2_1 = Equipment.getConfigData(var_0_0.ConfigData.equipID).name

	setText(var_2_0, i18n(var_0_0.ConfigData.content, var_2_1))

	local var_2_2 = arg_2_0.findTF("button_container/custom_button_1(Clone)/pic", arg_2_0._tf.parent)

	setText(var_2_2, i18n(var_0_0.ConfigData.btnTxt))

	local var_2_3 = arg_2_0.findTF("icon_bg/icon", arg_2_0._tf)

	setImageSprite(var_2_3, LoadSprite(var_0_0.ConfigData.icon))

	if arg_2_1.windowSize:
		arg_2_0._tf.parent.sizeDelta = Vector2(arg_2_1.windowSize.x, arg_2_1.windowSize.y)

	arg_2_0.PostRefresh(arg_2_1)

return var_0_0
