local var_0_0 = class("Match3Page", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.item = arg_1_0.findTF("item", arg_1_0.bg)
	arg_1_0.items = arg_1_0.findTF("items", arg_1_0.bg)
	arg_1_0.goBtn = arg_1_0.findTF("go", arg_1_0.bg)
	arg_1_0.itemList = UIItemList.New(arg_1_0.items, arg_1_0.item)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.drop = arg_2_0.activity.getConfig("config_client").drop
	arg_2_0.id = arg_2_0.activity.getConfig("config_client").gameId
	arg_2_0.day = #arg_2_0.drop

def var_0_0.OnFirstFlush(arg_3_0):
	setActive(arg_3_0.item, False)

	local var_3_0 = getProxy(MiniGameProxy).GetHubByHubId(arg_3_0.activity.getConfig("config_id"))

	setActive(arg_3_0.item, False)
	arg_3_0.itemList.make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventInit:
			local var_4_0 = arg_3_0.findTF("item", arg_4_2)
			local var_4_1 = arg_3_0.drop[arg_4_1 + 1]
			local var_4_2 = {
				type = var_4_1[1],
				id = var_4_1[2],
				count = var_4_1[3]
			}

			updateDrop(var_4_0, var_4_2)
			onButton(arg_3_0, arg_4_2, function()
				arg_3_0.emit(BaseUI.ON_DROP, var_4_2), SFX_PANEL)
		elif arg_4_0 == UIItemList.EventUpdate:
			local var_4_3 = arg_3_0.findTF("got", arg_4_2)
			local var_4_4 = arg_3_0.findTF("mask", arg_4_2)

			setActive(var_4_3, arg_4_1 < var_3_0.usedtime)
			setActive(var_4_4, arg_4_1 >= var_3_0.usedtime + var_3_0.count))
	arg_3_0.itemList.align(arg_3_0.day)
	onButton(arg_3_0, arg_3_0.goBtn, function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, arg_3_0.id))

def var_0_0.OnUpdateFlush(arg_7_0):
	arg_7_0.itemList.align(arg_7_0.day)

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
