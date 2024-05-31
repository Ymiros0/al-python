local var_0_0 = class("GuildShopPurchasePanel", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "GuildShopPurchaseMsgUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.list = UIItemList.New(arg_2_0.findTF("got/bottom/scroll/list"), arg_2_0.findTF("got/bottom/scroll/list/tpl"))
	arg_2_0.confirmBtn = arg_2_0.findTF("confirm")
	arg_2_0.descTxt = arg_2_0.findTF("got/top/desc").GetComponent(typeof(Text))
	arg_2_0.exchagneCnt = arg_2_0.findTF("got/top/exchange/Text").GetComponent(typeof(Text))
	arg_2_0.consumeCnt = arg_2_0.findTF("confirm/consume/Text").GetComponent(typeof(Text))
	arg_2_0.title = arg_2_0.findTF("got/top/title")

	setText(arg_2_0.findTF("got/top/exchange/label"), i18n("guild_shop_label_2"))
	setText(arg_2_0.findTF("confirm/Text"), i18n("guild_shop_label_3"))
	setText(arg_2_0.findTF("confirm/consume/label"), i18n("guild_shop_label_4"))

	arg_2_0.resIcon = arg_2_0.findTF("confirm/consume/icon")

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if #arg_3_0.selectedList == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_shop_must_select_goods"))

			return

		arg_3_0.OnConfirm()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.OnConfirm(arg_6_0):
	arg_6_0.emit(NewShopsMediator.ON_GUILD_SHOPPING, arg_6_0.data.id, arg_6_0.selectedList)

def var_0_0.Show(arg_7_0, arg_7_1):
	var_0_0.super.Show(arg_7_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf)

	arg_7_0.data = arg_7_1
	arg_7_0.maxCnt = arg_7_1.count
	arg_7_0.selectedList = {}

	arg_7_0.InitList()
	arg_7_0.UpdateValue()

	if arg_7_1.type == 4:
		setText(arg_7_0.title, i18n("guild_shop_label_5"))
	else
		setText(arg_7_0.title, i18n("guild_shop_label_1"))

	arg_7_0.descTxt.text = ""

def var_0_0.UpdateValue(arg_8_0):
	local var_8_0 = arg_8_0.maxCnt - #arg_8_0.selectedList
	local var_8_1 = var_8_0 > 0 and "<color=#92FC63FF>" .. var_8_0 .. "</color>/" or "<color=#FF5C5CFF>" .. var_8_0 .. "</color>/"

	arg_8_0.exchagneCnt.text = var_8_1 .. arg_8_0.maxCnt
	arg_8_0.consumeCnt.text = arg_8_0.data.price * #arg_8_0.selectedList

def var_0_0.InitList(arg_9_0):
	local var_9_0 = arg_9_0.data

	arg_9_0.displays = var_9_0.displays

	arg_9_0.list.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate:
			local var_10_0 = arg_9_0.displays[arg_10_1 + 1]

			arg_9_0.UpdateItem(var_9_0, var_10_0, arg_10_2))
	arg_9_0.list.align(#arg_9_0.displays)

def var_0_0.UpdateItem(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0 = arg_11_1.type

	updateDrop(arg_11_3.Find("item/bg"), {
		type = var_11_0,
		id = arg_11_2,
		count = arg_11_1.num
	})

	local var_11_1 = Drop.New({
		type = var_11_0,
		id = arg_11_2
	})
	local var_11_2 = arg_11_3.Find("name_bg/Text").GetComponent("ScrollText")
	local var_11_3 = var_11_1.getConfig("name")

	var_11_2.SetText(var_11_3)

	local var_11_4 = arg_11_3.Find("cnt/Text").GetComponent(typeof(Text))

	local function var_11_5()
		local var_12_0 = 0

		for iter_12_0, iter_12_1 in ipairs(arg_11_0.selectedList):
			if iter_12_1 == arg_11_2:
				var_12_0 = var_12_0 + 1

		var_11_4.text = var_12_0

	onButton(arg_11_0, arg_11_3, function()
		arg_11_0.ClickItem(arg_11_3, arg_11_2), SFX_PANEL)
	pressPersistTrigger(arg_11_3.Find("cnt/minus"), 0.5, function()
		arg_11_0.PressMinusBtn(arg_11_3, arg_11_2)
		var_11_5(), None, True, True, 0.1, SFX_PANEL)
	pressPersistTrigger(arg_11_3.Find("cnt/add"), 0.5, function()
		arg_11_0.PressAddBtn(arg_11_3, arg_11_2)
		var_11_5(), None, True, True, 0.1, SFX_PANEL)

	local var_11_6 = arg_11_3.Find("mask")

	setActive(var_11_6, False)
	var_11_5()

def var_0_0.ClearZeroItem(arg_16_0, arg_16_1):
	arg_16_0.list.each(function(arg_17_0, arg_17_1)
		local var_17_0 = arg_16_0.displays[arg_17_0 + 1]

		if arg_16_1 != arg_17_1 and not table.contains(arg_16_0.selectedList, var_17_0):
			setActive(arg_17_1.Find("cnt"), False)
			setActive(arg_17_1.Find("selected"), False))

def var_0_0.ClickItem(arg_18_0, arg_18_1, arg_18_2):
	arg_18_0.ClearZeroItem(arg_18_1)
	setActive(arg_18_1.Find("cnt"), True)
	setActive(arg_18_1.Find("selected"), True)

def var_0_0.PressMinusBtn(arg_19_0, arg_19_1, arg_19_2):
	if #arg_19_0.selectedList == 0:
		return

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.selectedList):
		if iter_19_1 == arg_19_2:
			table.remove(arg_19_0.selectedList, iter_19_0)

			break

	arg_19_0.UpdateValue()

def var_0_0.PressAddBtn(arg_20_0, arg_20_1, arg_20_2):
	if #arg_20_0.selectedList == arg_20_0.maxCnt:
		return

	table.insert(arg_20_0.selectedList, arg_20_2)
	arg_20_0.UpdateValue()

def var_0_0.Hide(arg_21_0):
	if arg_21_0.isShowing():
		pg.UIMgr.GetInstance().UnblurPanel(arg_21_0._tf, arg_21_0._parentTf)

	arg_21_0.list.each(function(arg_22_0, arg_22_1)
		setActive(arg_22_1.Find("cnt"), False)
		setActive(arg_22_1.Find("selected"), False))
	var_0_0.super.Hide(arg_21_0)

def var_0_0.OnDestroy(arg_23_0):
	arg_23_0.Hide()

return var_0_0
