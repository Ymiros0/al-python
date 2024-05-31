local var_0_0 = class("MailOverflowWindow", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "MailOverflowMsgboxUI"

def var_0_0.OnInit(arg_2_0):
	onButton(arg_2_0, arg_2_0._tf.Find("bg"), function()
		arg_2_0.Hide(), SFX_PANEL)

	arg_2_0.closeBtn = arg_2_0.findTF("adapt/window_overflow/top/btnBack")

	onButton(arg_2_0, arg_2_0.closeBtn, function()
		arg_2_0.Hide(), SFX_PANEL)

	arg_2_0._window_overflow = arg_2_0._tf.Find("adapt/window_overflow")
	arg_2_0.titleTips = arg_2_0._window_overflow.Find("top/bg/infomation/title")
	arg_2_0._itemConfireText = arg_2_0._window_overflow.Find("content")
	arg_2_0._confireLabel = arg_2_0._window_overflow.Find("desc/label1")
	arg_2_0._confireInput = arg_2_0._window_overflow.Find("desc/InputField")
	arg_2_0._overflowtitleTips = arg_2_0._window_overflow.Find("top/bg/infomation/title")
	arg_2_0.PlaceholderText = arg_2_0._confireInput.Find("Placeholder")
	arg_2_0._overflowcancelButton = arg_2_0._window_overflow.Find("button_container/btn_not")
	arg_2_0._overflowconfirmButton = arg_2_0._window_overflow.Find("button_container/btn_ok")
	arg_2_0.item = arg_2_0._window_overflow.Find("item")
	arg_2_0.items = arg_2_0._window_overflow.Find("items")
	arg_2_0.itemList = UIItemList.New(arg_2_0.items, arg_2_0.item)

	setText(arg_2_0._overflowcancelButton.Find("Text"), i18n("mail_box_cancel"))
	setText(arg_2_0._overflowconfirmButton.Find("Text"), i18n("mail_box_confirm"))
	setText(arg_2_0.titleTips, i18n("mail_boxtitle_information"))
	setText(arg_2_0.PlaceholderText, i18n("mail_search"))

def var_0_0.Updatelayout(arg_5_0):
	if not arg_5_0.key:
		arg_5_0.key = math.random(100000, 999999)

		setText(arg_5_0._confireLabel, i18n("mail_storeroom_max_2", arg_5_0.key))
	else
		setText(arg_5_0._confireLabel, "")

def var_0_0.showConformMsgBox(arg_6_0, arg_6_1):
	setText(arg_6_0._itemConfireText, arg_6_1.content)

	arg_6_0.key = None

	arg_6_0.Updatelayout()
	onButton(arg_6_0, arg_6_0._overflowcancelButton, function()
		arg_6_0.Hide(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0._overflowconfirmButton, function()
		if arg_6_0.key:
			local var_8_0 = getInputText(arg_6_0._confireInput)

			if arg_6_0.key != tonumber(var_8_0):
				pg.TipsMgr.GetInstance().ShowTips(i18n("mail_input_erro"))

				return

		arg_6_0.Hide()

		if arg_6_1.onYes:
			arg_6_1.onYes(), SFX_PANEL)
	setActive(arg_6_0.item, False)
	arg_6_0.itemList.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = arg_9_2.Find("IconTpl")
			local var_9_1 = arg_6_1.dropList[arg_9_1 + 1]
			local var_9_2 = {
				type = var_9_1.type,
				id = var_9_1.id,
				count = var_9_1.count
			}

			updateDrop(var_9_0, var_9_2))
	arg_6_0.itemList.align(#arg_6_1.dropList)

def var_0_0.Show(arg_10_0, arg_10_1):
	var_0_0.super.Show(arg_10_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_10_0._tf)
	arg_10_0.showConformMsgBox(arg_10_1)

def var_0_0.Hide(arg_11_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_11_0._tf, arg_11_0._parentTf)
	var_0_0.super.Hide(arg_11_0)
	setInputText(arg_11_0._confireInput, "")

def var_0_0.OnDestroy(arg_12_0):
	if arg_12_0.isShowing():
		arg_12_0.Hide()

return var_0_0
