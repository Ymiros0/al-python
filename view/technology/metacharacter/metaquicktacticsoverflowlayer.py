local var_0_0 = class("MetaQuickTacticsOverflowLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MetaQuickTacticsOverflowUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.addListener()
	arg_2_0.overlayPanel(True)

def var_0_0.didEnter(arg_3_0):
	return

def var_0_0.willExit(arg_4_0):
	arg_4_0.overlayPanel(False)

def var_0_0.onBackPressed(arg_5_0):
	arg_5_0.closeView()

def var_0_0.overlayPanel(arg_6_0, arg_6_1):
	if arg_6_1 and arg_6_0._tf:
		pg.UIMgr.GetInstance().OverlayPanel(arg_6_0._tf, {
			groupName = LayerWeightConst.GROUP_META,
			weight = LayerWeightConst.BASE_LAYER
		})
	elif arg_6_0._tf:
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_6_0._tf)

def var_0_0.initData(arg_7_0):
	arg_7_0.shipID = arg_7_0.contextData.shipID
	arg_7_0.skillID = arg_7_0.contextData.skillID
	arg_7_0.useCountDict = arg_7_0.contextData.useCountDict
	arg_7_0.overExp = arg_7_0.contextData.overExp

def var_0_0.initUI(arg_8_0):
	arg_8_0.bg = arg_8_0.findTF("BG")
	arg_8_0.text = arg_8_0.findTF("Content/Context/Text")
	arg_8_0.cancelBtn = arg_8_0.findTF("Content/CancelBtn")
	arg_8_0.confirmBtn = arg_8_0.findTF("Content/ConfirmBtn")

	setText(arg_8_0.text, i18n("metaskill_overflow_tip", arg_8_0.overExp))

def var_0_0.addListener(arg_9_0):
	local function var_9_0()
		arg_9_0.closeView()

	onButton(arg_9_0, arg_9_0.bg, var_9_0, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.cancelBtn, var_9_0, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.confirmBtn, function()
		arg_9_0.emit(MetaQuickTacticsOverflowMediator.USE_TACTICS_BOOK, arg_9_0.shipID, arg_9_0.skillID, arg_9_0.useCountDict)
		arg_9_0.closeView(), SFX_PANEL)

return var_0_0
