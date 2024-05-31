local var_0_0 = class("ShopMultiWindow", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ShopsUIMsgbox"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.topItem = arg_2_0.findTF("item/panel_bg")
	arg_2_0.ownerTF = arg_2_0.topItem.Find("left/own")
	arg_2_0.detailTF = arg_2_0.topItem.Find("left/detail")
	arg_2_0.nameTF = arg_2_0.topItem.Find("display_panel/name_container/name/Text").GetComponent(typeof(Text))
	arg_2_0.descTF = arg_2_0.topItem.Find("display_panel/desc/Text").GetComponent(typeof(Text))
	arg_2_0.timeLimitTF = arg_2_0.topItem.Find("time_limit")
	arg_2_0.bottomItem = arg_2_0.findTF("got/panel_bg/list/item")
	arg_2_0.itemCountTF = arg_2_0.bottomItem.Find("icon_bg/count").GetComponent(typeof(Text))
	arg_2_0.maxBtn = arg_2_0.findTF("count/max")
	arg_2_0.leftBtn = arg_2_0.findTF("count/number_panel/left")
	arg_2_0.rightBtn = arg_2_0.findTF("count/number_panel/right")
	arg_2_0.countTF = arg_2_0.findTF("count/number_panel/value").GetComponent(typeof(Text))
	arg_2_0.cancelBtn = arg_2_0.findTF("actions/cancel_button")
	arg_2_0.confirmBtn = arg_2_0.findTF("actions/confirm_button")

	setText(arg_2_0.findTF("got/panel_bg/got_text"), i18n("shops_msgbox_output"))
	setText(arg_2_0.findTF("count/image_text"), i18n("shops_msgbox_exchange_count"))
	setText(arg_2_0.findTF("actions/cancel_button/label"), i18n("shop_word_cancel"))
	setText(arg_2_0.findTF("actions/confirm_button/label"), i18n("shop_word_exchange"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Close(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf.Find("bg"), function()
		arg_3_0.Close(), SFX_PANEL)

def var_0_0.Open(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.opening = True

	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)
	arg_6_0.InitWindow(arg_6_1, arg_6_2)
	arg_6_0.Show()

def var_0_0.InitWindow(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = {
		id = arg_7_1.getConfig("commodity_id"),
		type = arg_7_1.getConfig("commodity_type"),
		count = arg_7_1.getConfig("num")
	}

	if isa(arg_7_1, ActivityCommodity):
		local var_7_1, var_7_2, var_7_3 = arg_7_1.CheckTimeLimit()

		setActive(arg_7_0.timeLimitTF, var_7_1)

		if var_7_1 and var_7_2:
			local var_7_4 = getProxy(ActivityProxy).getActivityById(Item.getConfigData(var_7_0.id).link_id)

			setText(arg_7_0.findTF("Text", arg_7_0.timeLimitTF), i18n("eventshop_time_hint", var_7_4.GetEndTimeStrByConfig()))

	local var_7_5 = Drop.New({
		type = arg_7_1.getConfig("resource_category"),
		id = arg_7_1.getConfig("resource_type")
	}).getOwnedCount()
	local var_7_6 = math.max(math.floor(var_7_5 / arg_7_1.getConfig("resource_num")), 1)

	if arg_7_1.getConfig("num_limit") != 0 or isa(arg_7_1, QuotaCommodity):
		local var_7_7 = arg_7_1.GetPurchasableCnt()

		var_7_6 = math.min(var_7_6, math.max(0, var_7_7))

	local function var_7_8(arg_8_0)
		arg_8_0 = math.max(arg_8_0, 1)
		arg_8_0 = math.min(arg_8_0, var_7_6)
		arg_7_0.countTF.text = arg_8_0
		arg_7_0.curCount = arg_8_0
		arg_7_0.itemCountTF.text = arg_8_0 * arg_7_1.getConfig("num")

	var_7_8(1)
	updateDrop(arg_7_0.topItem.Find("left/IconTpl"), var_7_0)
	UpdateOwnDisplay(arg_7_0.ownerTF, var_7_0)
	RegisterDetailButton(arg_7_0, arg_7_0.detailTF, var_7_0)

	arg_7_0.nameTF.text = var_7_0.getConfig("name")
	arg_7_0.descTF.text = var_7_0.desc or var_7_0.getConfig("desc")

	updateDrop(arg_7_0.bottomItem, var_7_0)
	onButton(arg_7_0, arg_7_0.confirmBtn, function()
		if arg_7_2:
			arg_7_2(arg_7_1, arg_7_0.curCount, var_7_0.getConfig("name"))

		arg_7_0.Close(), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.leftBtn, function()
		var_7_8(arg_7_0.curCount - 1))
	onButton(arg_7_0, arg_7_0.rightBtn, function()
		var_7_8(arg_7_0.curCount + 1))
	onButton(arg_7_0, arg_7_0.maxBtn, function()
		var_7_8(var_7_6))

def var_0_0.Close(arg_13_0):
	if arg_13_0.opening:
		pg.UIMgr.GetInstance().UnblurPanel(arg_13_0._tf, arg_13_0._parentTf)
		arg_13_0.Hide()

		arg_13_0.opening = False

def var_0_0.OnDestroy(arg_14_0):
	if arg_14_0.opening:
		arg_14_0.Close()

return var_0_0
