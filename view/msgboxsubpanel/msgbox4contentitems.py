local var_0_0 = class("Msgbox4ContentItems", import(".MsgboxSubPanel"))

def var_0_0.getUIName(arg_1_0):
	return "Msgbox4ContentItems"

def var_0_0.OnRefresh(arg_2_0, arg_2_1):
	rtf(arg_2_0.viewParent._window).sizeDelta = Vector2.New(1000, 638)

	setText(arg_2_0._tf.Find("content"), arg_2_1.content)

	local var_2_0 = arg_2_0._tf.Find("list")
	local var_2_1 = UIItemList.New(var_2_0, var_2_0.GetChild(0))

	var_2_1.make(function(arg_3_0, arg_3_1, arg_3_2)
		arg_3_1 = arg_3_1 + 1

		if arg_3_0 == UIItemList.EventUpdate:
			updateDrop(arg_3_2, arg_2_1.items[arg_3_1])
			setActive(arg_3_2.Find("name"), False)
			setActive(arg_3_2.Find("name_mask"), False)
			setScrollText(arg_3_2.Find("name_mask/name"), getText(arg_3_2.Find("name"))))
	var_2_1.align(#arg_2_1.items)

return var_0_0
