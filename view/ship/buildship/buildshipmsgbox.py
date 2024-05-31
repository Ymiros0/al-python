local var_0_0 = class("BuildShipMsgBox", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "BuildShipMsgBoxUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.cancenlBtn = findTF(arg_2_0._go, "window/btns/cancel_btn")
	arg_2_0.confirmBtn = findTF(arg_2_0._go, "window/btns/confirm_btn")
	arg_2_0.closeBtn = findTF(arg_2_0._go, "window/close_btn")
	arg_2_0.count = 1
	arg_2_0.minusBtn = findTF(arg_2_0._go, "window/content/calc_panel/minus")
	arg_2_0.addBtn = findTF(arg_2_0._go, "window/content/calc_panel/add")
	arg_2_0.maxBtn = findTF(arg_2_0._go, "window/content/max")
	arg_2_0.valueTxt = findTF(arg_2_0._go, "window/content/calc_panel/Text").GetComponent(typeof(Text))
	arg_2_0.text = findTF(arg_2_0._go, "window/content/Text").GetComponent(typeof(Text))

	setText(arg_2_0.findTF("window/btns/cancel_btn/Image/Image (1)"), i18n("text_cancel"))
	setText(arg_2_0.findTF("window/btns/confirm_btn/Image/Image (1)"), i18n("text_confirm"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancenlBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.onConfirm:
			arg_3_0.onConfirm(arg_3_0.count)

		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.minusBtn, function()
		arg_3_0.count = math.max(arg_3_0.count - 1, 1)

		arg_3_0.updateTxt(arg_3_0.count), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.addBtn, function()
		if arg_3_0.buildType == "ticket" and arg_3_0.count >= arg_3_0.itemVO.count:
			pg.TipsMgr.GetInstance().ShowTips(i18n("tip_build_ticket_not_enough", arg_3_0.itemVO.getConfig("name")))

			return

		arg_3_0.count = math.clamp(arg_3_0.count + 1, 1, MAX_BUILD_WORK_COUNT)

		arg_3_0.updateTxt(arg_3_0.count), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.maxBtn, function()
		arg_3_0.count = MAX_BUILD_WORK_COUNT

		if arg_3_0.buildType == "ticket":
			arg_3_0.count = math.clamp(arg_3_0.itemVO.count, 1, MAX_BUILD_WORK_COUNT)

		arg_3_0.updateTxt(arg_3_0.count), SFX_PANEL)

def var_0_0.updateTxt(arg_11_0, arg_11_1):
	arg_11_0.valueTxt.text = arg_11_1

	local var_11_0 = arg_11_0.GetDesc(arg_11_1)

	arg_11_0.text.text = var_11_0

def var_0_0.GetDesc(arg_12_0, arg_12_1):
	local var_12_0 = ""

	switch(arg_12_0.buildType, {
		def base:()
			local var_13_0 = arg_12_0.buildPool

			if arg_12_1 <= arg_12_0.max and arg_12_0.player.gold >= arg_12_1 * var_13_0.use_gold and arg_12_0.itemVO.count >= arg_12_1 * var_13_0.number_1:
				var_12_0 = i18n("build_ship_tip", arg_12_1, var_13_0.name, arg_12_1 * var_13_0.use_gold, arg_12_1 * var_13_0.number_1, COLOR_GREEN)
			else
				var_12_0 = i18n("build_ship_tip", arg_12_1, var_13_0.name, arg_12_1 * var_13_0.use_gold, arg_12_1 * var_13_0.number_1, COLOR_RED),
		def ticket:()
			if arg_12_1 <= arg_12_0.max and arg_12_0.itemVO.count >= arg_12_1:
				var_12_0 = i18n("build_ship_tip_use_ticket", arg_12_1, arg_12_0.buildPool.name, arg_12_1, arg_12_0.itemVO.getConfig("name"), COLOR_GREEN)
			else
				var_12_0 = i18n("build_ship_tip_use_ticket", arg_12_1, arg_12_0.buildPool.name, arg_12_1, arg_12_0.itemVO.getConfig("name"), COLOR_RED),
		def medal:()
			if arg_12_1 <= arg_12_0.max and arg_12_0.itemVO.count >= arg_12_1 * arg_12_0.cost:
				var_12_0 = i18n("honor_medal_support_tips_confirm", arg_12_1, arg_12_1 * arg_12_0.cost, COLOR_GREEN)
			else
				var_12_0 = i18n("honor_medal_support_tips_confirm", arg_12_1, arg_12_1 * arg_12_0.cost, COLOR_RED)
	})

	return var_12_0

def var_0_0.Show(arg_16_0, arg_16_1):
	arg_16_0.showing = True

	for iter_16_0, iter_16_1 in pairs(arg_16_1):
		arg_16_0[iter_16_0] = iter_16_1

	arg_16_0.count = 1

	arg_16_0.updateTxt(arg_16_0.count)
	setText(arg_16_0._tf.Find("window/content/title"), i18n(arg_16_0.buildType == "medal" and "support_times_tip" or "build_times_tip"))
	setActiveViaLayer(arg_16_0._go, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_16_0._tf)

def var_0_0.Hide(arg_17_0):
	arg_17_0.showing = False

	if arg_17_0._go:
		arg_17_0.onConfirm = None
		arg_17_0.count = 1
		arg_17_0.max = 1

		setActiveViaLayer(arg_17_0._go, False)

	pg.UIMgr.GetInstance().UnblurPanel(arg_17_0._tf, arg_17_0._parentTf)

def var_0_0.isShowing(arg_18_0):
	return arg_18_0.showing

def var_0_0.OnDestroy(arg_19_0):
	arg_19_0.Hide()

return var_0_0
