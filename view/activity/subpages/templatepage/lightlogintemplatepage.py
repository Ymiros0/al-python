local var_0_0 = class("LightLoginTemplatePage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.bar = arg_1_0.findTF("bar", arg_1_0.bg)
	arg_1_0.item = arg_1_0.findTF("item", arg_1_0.bg)
	arg_1_0.items = arg_1_0.findTF("items", arg_1_0.bg)
	arg_1_0.itemList = UIItemList.New(arg_1_0.items, arg_1_0.item)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.config = pg.activity_7_day_sign[arg_2_0.activity.getConfig("config_id")]
	arg_2_0.Day = #arg_2_0.config.front_drops

def var_0_0.OnFirstFlush(arg_3_0):
	setActive(arg_3_0.item, False)
	arg_3_0.itemList.make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventInit:
			local var_4_0 = arg_3_0.findTF("item", arg_4_2)
			local var_4_1 = Drop.Create(arg_3_0.config.front_drops[arg_4_1 + 1])

			updateDrop(var_4_0, var_4_1)
			onButton(arg_3_0, arg_4_2, function()
				arg_3_0.emit(BaseUI.ON_DROP, var_4_1), SFX_PANEL)
			GetImageSpriteFromAtlasAsync("ui/share/light_login_atlas", "DAY" .. arg_4_1 + 1, arg_3_0.findTF("day", arg_4_2), True)
		elif arg_4_0 == UIItemList.EventUpdate:
			local var_4_2 = arg_4_1 < arg_3_0.nday

			setActive(arg_3_0.findTF("got", arg_4_2), var_4_2)
			setActive(arg_3_0.findTF("get", arg_4_2), var_4_2)
			setActive(arg_3_0.findTF("bg", arg_4_2), not var_4_2))

def var_0_0.OnUpdateFlush(arg_6_0):
	arg_6_0.nday = arg_6_0.activity.data1

	arg_6_0.itemList.align(arg_6_0.Day)
	setFillAmount(arg_6_0.bar, arg_6_0.nday / arg_6_0.Day)

def var_0_0.OnDestroy(arg_7_0):
	clearImageSprite(arg_7_0.bg)
	removeAllChildren(arg_7_0.items)

return var_0_0
