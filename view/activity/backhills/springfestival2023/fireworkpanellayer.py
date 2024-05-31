local var_0_0 = class("FireworkPanelLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "FireworkPanelUI"

def var_0_0.init(arg_2_0):
	arg_2_0.leftPanel = arg_2_0.findTF("main/left_panel")
	arg_2_0.rightPanel = arg_2_0.findTF("main/right_panel")
	arg_2_0.fireBtn = arg_2_0.findTF("fire_btn", arg_2_0.rightPanel)

	setText(arg_2_0.findTF("tip", arg_2_0.rightPanel), i18n("activity_yanhua_tip7"))

	arg_2_0.leftItem = arg_2_0.findTF("scrollrect/content/item_tpl", arg_2_0.leftPanel)
	arg_2_0.leftItems = arg_2_0.findTF("scrollrect/content", arg_2_0.leftPanel)
	arg_2_0.leftUIList = UIItemList.New(arg_2_0.leftItems, arg_2_0.leftItem)
	arg_2_0.rightItem = arg_2_0.findTF("content/item_tpl", arg_2_0.rightPanel)
	arg_2_0.rightItems = arg_2_0.findTF("content", arg_2_0.rightPanel)
	arg_2_0.rightUIList = UIItemList.New(arg_2_0.rightItems, arg_2_0.rightItem)
	arg_2_0.arrowsTF = arg_2_0.findTF("arrows", arg_2_0.rightPanel)

	arg_2_0.initData()

def var_0_0.initData(arg_3_0):
	local var_3_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FIREWORK)

	assert(var_3_0 and not var_3_0.isEnd(), "烟花活动(type92)已结束")

	arg_3_0.unlockCount = var_3_0.getData1()
	arg_3_0.unlockIds = var_3_0.getData1List()
	arg_3_0.allIds = pg.activity_template[var_3_0.id].config_data[3]
	arg_3_0.playerId = getProxy(PlayerProxy).getData().id
	arg_3_0.orderIds = arg_3_0.getLocalData()

def var_0_0.getLocalData(arg_4_0):
	local var_4_0 = {}

	for iter_4_0 = 1, #arg_4_0.allIds:
		local var_4_1 = PlayerPrefs.GetInt("fireworks_" .. arg_4_0.playerId .. "_pos_" .. iter_4_0)

		if var_4_1 != 0:
			table.insert(var_4_0, var_4_1)

	return var_4_0

def var_0_0.setLocalData(arg_5_0):
	for iter_5_0 = 1, #arg_5_0.allIds:
		local var_5_0 = arg_5_0.orderIds[iter_5_0] or 0

		PlayerPrefs.SetInt("fireworks_" .. arg_5_0.playerId .. "_pos_" .. iter_5_0, var_5_0)

def var_0_0.didEnter(arg_6_0):
	onButton(arg_6_0, arg_6_0.findTF("main/mask"), function()
		arg_6_0.emit(var_0_0.ON_CLOSE))
	onButton(arg_6_0, arg_6_0.findTF("close_btn", arg_6_0.rightPanel), function()
		arg_6_0.emit(var_0_0.ON_CLOSE))
	onButton(arg_6_0, arg_6_0.fireBtn, function()
		if #arg_6_0.orderIds > 0:
			arg_6_0.emit(FireworkPanelMediator.LET_OFF_FIREWORKS, arg_6_0.orderIds))
	arg_6_0.initLeft()
	arg_6_0.initRight()
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)

def var_0_0.initLeft(arg_10_0):
	setActive(arg_10_0.findTF("empty", arg_10_0.leftPanel), #arg_10_0.unlockIds == 0)
	setActive(arg_10_0.findTF("scrollrect", arg_10_0.leftPanel), #arg_10_0.unlockIds > 0)
	arg_10_0.leftUIList.make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate:
			local var_11_0 = arg_11_1 + 1
			local var_11_1 = "lock"

			if var_11_0 <= #arg_10_0.unlockIds:
				var_11_1 = tostring(arg_10_0.unlockIds[var_11_0])

			arg_11_2.name = var_11_1

			if var_11_1 == "lock":
				setActive(arg_10_0.findTF("firework", arg_11_2), False)
			else
				local var_11_2 = tonumber(arg_11_2.name)
				local var_11_3 = arg_10_0.findTF("firework/icon", arg_11_2)
				local var_11_4 = arg_10_0.findTF("firework/selected", arg_11_2)

				setActive(arg_10_0.findTF("firework", arg_11_2), True)

				local var_11_5 = table.contains(arg_10_0.orderIds, var_11_2)

				setActive(var_11_4, var_11_5)
				GetImageSpriteFromAtlasAsync(Item.getConfigData(var_11_2).icon, "", var_11_3)
				onButton(arg_10_0, arg_11_2, function()
					arg_10_0.onLeftClick(var_11_2, var_11_5), SFX_PANEL))
	arg_10_0.leftUIList.align(#arg_10_0.allIds)

def var_0_0.initRight(arg_13_0):
	for iter_13_0 = 1, #arg_13_0.allIds - 2:
		cloneTplTo(arg_13_0.findTF("tpl", arg_13_0.arrowsTF), arg_13_0.arrowsTF)

	arg_13_0.rightUIList.make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate:
			local var_14_0 = arg_14_1 + 1
			local var_14_1 = "null"

			if var_14_0 <= #arg_13_0.orderIds:
				var_14_1 = tostring(arg_13_0.orderIds[var_14_0])

			arg_14_2.name = var_14_1

			local var_14_2 = arg_13_0.findTF("icon", arg_14_2)

			setActive(arg_13_0.findTF("add", arg_14_2), var_14_1 == "null")

			if var_14_1 == "null":
				setActive(var_14_2, False)
			else
				local var_14_3 = tonumber(arg_14_2.name)

				setActive(var_14_2, True)
				GetImageSpriteFromAtlasAsync(Item.getConfigData(var_14_3).icon, "", var_14_2)
				onButton(arg_13_0, var_14_2, function()
					arg_13_0.onRightClick(var_14_3), SFX_PANEL))
	arg_13_0.rightUIList.align(#arg_13_0.allIds)

def var_0_0.onLeftClick(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_2:
		table.removebyvalue(arg_16_0.orderIds, arg_16_1)
	else
		table.insert(arg_16_0.orderIds, arg_16_1)

	arg_16_0.setLocalData()
	arg_16_0.leftUIList.align(#arg_16_0.allIds)
	arg_16_0.rightUIList.align(#arg_16_0.allIds)

def var_0_0.onRightClick(arg_17_0, arg_17_1):
	table.removebyvalue(arg_17_0.orderIds, arg_17_1)
	arg_17_0.setLocalData()
	arg_17_0.leftUIList.align(#arg_17_0.allIds)
	arg_17_0.rightUIList.align(#arg_17_0.allIds)

def var_0_0.willExit(arg_18_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_18_0._tf)

return var_0_0
