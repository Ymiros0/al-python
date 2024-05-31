local var_0_0 = class("ShopSingleWindow", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ShopsUISinglebox"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.itemTF = arg_2_0.findTF("window/item")
	arg_2_0.nameTF = arg_2_0.itemTF.Find("display_panel/name_container/name/Text").GetComponent(typeof(Text))
	arg_2_0.descTF = arg_2_0.itemTF.Find("display_panel/desc/Text").GetComponent(typeof(Text))
	arg_2_0.itemOwnTF = arg_2_0.itemTF.Find("left/own")
	arg_2_0.itemDetailTF = arg_2_0.itemTF.Find("left/detail")
	arg_2_0.confirmBtn = arg_2_0.findTF("window/actions/confirm_btn")

	setText(arg_2_0.findTF("window/actions/cancel_btn/pic"), i18n("shop_word_cancel"))
	setText(arg_2_0.findTF("window/actions/confirm_btn/pic"), i18n("shop_word_exchange"))
	setText(arg_2_0.itemTF.Find("ship_group/locked/Text"), i18n("tag_ship_locked"))
	setText(arg_2_0.itemTF.Find("ship_group/unlocked/Text"), i18n("tag_ship_unlocked"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("window/actions/cancel_btn"), function()
		arg_3_0.Close(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf.Find("bg"), function()
		arg_3_0.Close(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("window/top/btnBack"), function()
		arg_3_0.Close(), SFX_CANCEL)

def var_0_0.Open(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0.opening = True

	arg_7_0.Show()
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf)
	arg_7_0.InitWindow(arg_7_1, arg_7_2)

def var_0_0.InitWindow(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = {
		id = arg_8_1.getConfig("commodity_id"),
		type = arg_8_1.getConfig("commodity_type"),
		count = arg_8_1.getConfig("num")
	}

	onButton(arg_8_0, arg_8_0.confirmBtn, function()
		if arg_8_2:
			arg_8_2(arg_8_1, 1, var_8_0.getConfig("name"))

		arg_8_0.Close(), SFX_CANCEL)
	updateDrop(arg_8_0.itemTF.Find("left/IconTpl"), var_8_0)
	UpdateOwnDisplay(arg_8_0.itemOwnTF, var_8_0)
	RegisterDetailButton(arg_8_0, arg_8_0.itemDetailTF, var_8_0)

	local var_8_1 = var_8_0.type == DROP_TYPE_SHIP
	local var_8_2 = arg_8_0.itemTF.Find("ship_group")

	SetActive(var_8_2, var_8_1)

	if var_8_1:
		local var_8_3 = tobool(getProxy(CollectionProxy).getShipGroup(pg.ship_data_template[var_8_0.id].group_type))

		SetActive(var_8_2.Find("unlocked"), var_8_3)
		SetActive(var_8_2.Find("locked"), not var_8_3)

	arg_8_0.descTF.text = var_8_0.desc or var_8_0.getConfig("desc")
	arg_8_0.nameTF.text = var_8_0.getConfig("name")

def var_0_0.Close(arg_10_0):
	if arg_10_0.opening:
		arg_10_0.opening = False

		pg.UIMgr.GetInstance().UnblurPanel(arg_10_0._tf, arg_10_0._parentTf)
		arg_10_0.Hide()

def var_0_0.OnDestroy(arg_11_0):
	if arg_11_0.opening:
		arg_11_0.Close()

return var_0_0
