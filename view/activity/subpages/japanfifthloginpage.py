local var_0_0 = class("JapanFifthLoginPage", import(".TemplatePage.LoginTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	setActive(arg_1_0.item, False)
	arg_1_0.itemList.make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate:
			local var_2_0 = arg_1_0.findTF("item", arg_2_2)
			local var_2_1 = arg_1_0.config.front_drops[arg_2_1 + 1]
			local var_2_2 = {
				type = var_2_1[1],
				id = var_2_1[2],
				count = var_2_1[3]
			}

			updateDrop(var_2_0, var_2_2)
			onButton(arg_1_0, arg_2_2, function()
				arg_1_0.emit(BaseUI.ON_DROP, var_2_2), SFX_PANEL)

			local var_2_3 = arg_1_0.findTF("got", arg_2_2)

			setActive(var_2_3, arg_2_1 < arg_1_0.nday))

def var_0_0.OnUpdateFlush(arg_4_0):
	var_0_0.super.OnUpdateFlush(arg_4_0)
	setText(arg_4_0.bg.Find("Text"), arg_4_0.nday .. "/" .. arg_4_0.Day)

return var_0_0
