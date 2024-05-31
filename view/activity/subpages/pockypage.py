local var_0_0 = class("PockyPage", import(".TemplatePage.LoginTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.title = arg_1_0.findTF("day", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	setActive(arg_2_0.item, False)
	arg_2_0.itemList.make(function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_0 == UIItemList.EventInit:
			local var_3_0 = arg_2_0.findTF("item", arg_3_2)
			local var_3_1 = arg_2_0.config.front_drops[arg_3_1 + 1]
			local var_3_2 = {
				type = var_3_1[1],
				id = var_3_1[2],
				count = var_3_1[3]
			}

			updateDrop(var_3_0, var_3_2)
			onButton(arg_2_0, arg_3_2, function()
				arg_2_0.emit(BaseUI.ON_DROP, var_3_2), SFX_PANEL)
		elif arg_3_0 == UIItemList.EventUpdate:
			local var_3_3 = arg_2_0.findTF("got", arg_3_2)

			setActive(var_3_3, arg_3_1 < arg_2_0.nday))

def var_0_0.OnUpdateFlush(arg_5_0):
	arg_5_0.nday = arg_5_0.activity.data1

	setText(arg_5_0.title, arg_5_0.nday)
	arg_5_0.itemList.align(arg_5_0.Day)

return var_0_0
