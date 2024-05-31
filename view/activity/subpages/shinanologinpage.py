local var_0_0 = class("ShinanoLoginPage", import(".TemplatePage.LoginTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.bar = arg_1_0.findTF("bar", arg_1_0.bg)

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
			GetImageSpriteFromAtlasAsync("ui/share/light_login_atlas", "DAY" .. arg_3_1 + 1, arg_2_0.findTF("day", arg_3_2), True)
		elif arg_3_0 == UIItemList.EventUpdate:
			local var_3_3 = arg_3_1 < arg_2_0.nday

			setActive(arg_2_0.findTF("got", arg_3_2), var_3_3)
			setActive(arg_2_0.findTF("get", arg_3_2), var_3_3)
			setActive(arg_2_0.findTF("bg", arg_3_2), not var_3_3))

def var_0_0.OnUpdateFlush(arg_5_0):
	var_0_0.super.OnUpdateFlush(arg_5_0)
	setFillAmount(arg_5_0.bar, arg_5_0.nday / arg_5_0.Day)

def var_0_0.OnDestroy(arg_6_0):
	return

return var_0_0
