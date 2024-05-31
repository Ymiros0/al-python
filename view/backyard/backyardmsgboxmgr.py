local var_0_0 = class("BackyardMsgBoxMgr")

def var_0_0.Init(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.view = arg_1_1
	arg_1_0.loaded = False

	PoolMgr.GetInstance().GetUI("BackYardMsgBox", True, function(arg_2_0)
		if arg_1_0.exited:
			return

		setParent(arg_2_0, pg.UIMgr.GetInstance().UIMain)

		arg_1_0._go = arg_2_0
		arg_1_0._tf = arg_2_0.transform
		arg_1_0.frame = findTF(arg_1_0._tf, "msg")
		arg_1_0.closeBtn = findTF(arg_1_0._tf, "frame/close")
		arg_1_0.context = findTF(arg_1_0._tf, "msg/Text").GetComponent(typeof(Text))
		arg_1_0.cancelBtn = findTF(arg_1_0._tf, "msg/btns/btn2")
		arg_1_0.confirmBtn = findTF(arg_1_0._tf, "msg/btns/btn1")
		arg_1_0.helpPanel = findTF(arg_1_0._tf, "help_panel")
		arg_1_0._helpList = arg_1_0.helpPanel.Find("list")

		setText(arg_1_0._tf.Find("frame/title"), i18n("words_information"))
		setText(arg_1_0.cancelBtn.Find("Text"), i18n("word_cancel"))
		setText(arg_1_0.confirmBtn.Find("Text"), i18n("battle_result_confirm"))

		arg_1_0.loaded = True

		setActive(arg_1_0._tf, False)
		arg_1_2())
	pg.DelegateInfo.New(arg_1_0.view)

def var_0_0.Show(arg_3_0, arg_3_1):
	setActive(arg_3_0.frame, True)
	setActive(arg_3_0.helpPanel, False)

	if not arg_3_0.loaded:
		return

	arg_3_0.isShowMsg = True
	arg_3_0.context.text = arg_3_1.content
	arg_3_0.onYes = arg_3_1.onYes
	arg_3_0.onNo = arg_3_1.onNo

	arg_3_0.Common(arg_3_1)

def var_0_0.Common(arg_4_0, arg_4_1):
	onButton(arg_4_0.view, arg_4_0.confirmBtn, function()
		if arg_4_0.onYes:
			arg_4_0.onYes()

		arg_4_0.Hide(), arg_4_1.yesSound or SFX_PANEL)
	onButton(arg_4_0.view, arg_4_0._tf, function()
		arg_4_0.Hide(), SFX_PANEL)
	onButton(arg_4_0.view, arg_4_0.closeBtn, function()
		arg_4_0.Hide(), SFX_PANEL)
	onButton(arg_4_0.view, arg_4_0.cancelBtn, function()
		if arg_4_0.onNo:
			arg_4_0.onNo()

		arg_4_0.Hide(), SFX_PANEL)
	setActive(arg_4_0.cancelBtn, not arg_4_1.hideNo)
	setActive(arg_4_0._tf, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_4_0._tf, {
		weight = LayerWeightConst.TOP_LAYER
	})

def var_0_0.ShowHelp(arg_9_0, arg_9_1):
	setActive(arg_9_0.frame, False)
	setActive(arg_9_0.helpPanel, True)

	local var_9_0 = arg_9_1.helps

	for iter_9_0 = #var_9_0, arg_9_0._helpList.childCount - 1:
		Destroy(arg_9_0._helpList.GetChild(iter_9_0))

	for iter_9_1 = arg_9_0._helpList.childCount, #var_9_0 - 1:
		cloneTplTo(arg_9_0._helpTpl, arg_9_0._helpList)

	for iter_9_2, iter_9_3 in ipairs(var_9_0):
		local var_9_1 = arg_9_0._helpList.GetChild(iter_9_2 - 1)

		setActive(var_9_1, True)

		local var_9_2 = var_9_1.Find("icon")

		setActive(var_9_2, iter_9_3.icon)
		setActive(findTF(var_9_1, "line"), iter_9_3.line)

		local var_9_3 = var_9_1.Find("richText").GetComponent("RichText")

		setText(var_9_1, HXSet.hxLan(iter_9_3.info and SwitchSpecialChar(iter_9_3.info, True) or ""))

	arg_9_0.Common(arg_9_1)

def var_0_0.Hide(arg_10_0):
	arg_10_0.onYes = None
	arg_10_0.onNo = None
	arg_10_0.isShowMsg = False

	setActive(arg_10_0._tf, False)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_10_0._tf, pg.UIMgr.GetInstance().UIMain)

def var_0_0.Destroy(arg_11_0):
	arg_11_0.exited = True

	if arg_11_0.isShowMsg:
		arg_11_0.Hide()

	PoolMgr.GetInstance().ReturnUI("BackYardMsgBox", arg_11_0._go)

return var_0_0
