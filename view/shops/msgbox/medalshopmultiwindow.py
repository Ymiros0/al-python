local var_0_0 = class("MedalShopMultiWindow", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ShopsUIMsgbox"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.topItem = arg_2_0.findTF("item/panel_bg")
	arg_2_0.ownerTF = arg_2_0.topItem.Find("left/own")
	arg_2_0.detailTF = arg_2_0.topItem.Find("left/detail")
	arg_2_0.nameTF = arg_2_0.topItem.Find("display_panel/name_container/name/Text").GetComponent(typeof(Text))
	arg_2_0.descTF = arg_2_0.topItem.Find("display_panel/desc/Text").GetComponent(typeof(Text))
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
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf.Find("bg"), function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.InitWindow(arg_6_1, arg_6_2)
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)
	var_0_0.super.Show(arg_6_0)

def var_0_0.Hide(arg_7_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_7_0._tf, arg_7_0._parentTf)
	var_0_0.super.Hide(arg_7_0)

def var_0_0.InitWindow(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = arg_8_1.GetDropInfo()
	local var_8_1 = getProxy(BagProxy).getItemCountById(ITEM_ID_SILVER_HOOK)
	local var_8_2 = math.max(math.floor(var_8_1 / arg_8_1.getConfig("price")), 1)

	if arg_8_1.GetLimit() != 0:
		var_8_2 = math.min(var_8_2, arg_8_1.GetMaxCnt())

	local function var_8_3(arg_9_0)
		arg_9_0 = math.max(arg_9_0, 1)
		arg_9_0 = math.min(arg_9_0, var_8_2)
		arg_8_0.countTF.text = arg_9_0
		arg_8_0.curCount = arg_9_0
		arg_8_0.itemCountTF.text = arg_9_0 * arg_8_1.getConfig("num")

	var_8_3(1)
	updateDrop(arg_8_0.topItem.Find("left/IconTpl"), var_8_0)
	UpdateOwnDisplay(arg_8_0.ownerTF, var_8_0)
	RegisterDetailButton(arg_8_0, arg_8_0.detailTF, var_8_0)

	arg_8_0.nameTF.text = var_8_0.getConfig("name")
	arg_8_0.descTF.text = var_8_0.desc or var_8_0.getConfig("desc")

	updateDrop(arg_8_0.bottomItem, var_8_0)
	onButton(arg_8_0, arg_8_0.confirmBtn, function()
		if arg_8_2:
			arg_8_2(arg_8_0.curCount)

		arg_8_0.Hide(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.leftBtn, function()
		var_8_3(arg_8_0.curCount - 1))
	onButton(arg_8_0, arg_8_0.rightBtn, function()
		var_8_3(arg_8_0.curCount + 1))
	onButton(arg_8_0, arg_8_0.maxBtn, function()
		var_8_3(var_8_2))

def var_0_0.OnDestroy(arg_14_0):
	if arg_14_0.isShowing():
		arg_14_0.Hide()

return var_0_0
