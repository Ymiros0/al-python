local var_0_0 = class("LevelStrategyView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "LevelStrategyView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitUI()
	setActive(arg_2_0._tf, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf)

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0.onConfirm = None
	arg_3_0.onCancel = None

	pg.UIMgr.GetInstance().UnblurPanel(arg_3_0._tf, arg_3_0._parentTf)

def var_0_0.setCBFunc(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.onConfirm = arg_4_1
	arg_4_0.onCancel = arg_4_2

def var_0_0.InitUI(arg_5_0):
	arg_5_0.icon = arg_5_0.findTF("window/panel/item/icon_bg/icon")
	arg_5_0.count = arg_5_0.findTF("window/panel/item/icon_bg/count")
	arg_5_0.name = arg_5_0.findTF("window/panel/item/name")
	arg_5_0.desc = arg_5_0.findTF("window/panel/item/desc")
	arg_5_0.btnCancel = arg_5_0.findTF("window/panel/actions/cancel_button")
	arg_5_0.btnUse = arg_5_0.findTF("window/panel/actions/use_button")
	arg_5_0.btnBack = arg_5_0.findTF("top/btnBack")
	arg_5_0.tips = arg_5_0.findTF("window/panel/tips")
	arg_5_0.txSwitch = findTF(arg_5_0.btnUse, "switch")
	arg_5_0.txUse = findTF(arg_5_0.btnUse, "use")

def var_0_0.set(arg_6_0, arg_6_1):
	arg_6_0.strategy = arg_6_1

	local var_6_0 = pg.strategy_data_template[arg_6_1.id]

	GetImageSpriteFromAtlasAsync("strategyicon/" .. var_6_0.icon, "", arg_6_0.icon)

	if var_6_0.type == 1:
		setText(arg_6_0.count, "")
		setActive(arg_6_0.tips, True)
		setActive(arg_6_0.txSwitch, True)
		setActive(arg_6_0.txUse, False)
	else
		setText(arg_6_0.count, arg_6_1.count)
		setActive(arg_6_0.tips, False)
		setActive(arg_6_0.txSwitch, False)
		setActive(arg_6_0.txUse, True)

	setText(arg_6_0.name, var_6_0.name)
	setText(arg_6_0.desc, var_6_0.desc)
	onButton(arg_6_0, arg_6_0.btnBack, function()
		if arg_6_0.onCancel:
			arg_6_0.onCancel(), SFX_CANCEL)
	onButton(arg_6_0, arg_6_0.btnCancel, function()
		if arg_6_0.onCancel:
			arg_6_0.onCancel(), SFX_CANCEL)
	onButton(arg_6_0, arg_6_0.btnUse, function()
		if arg_6_0.onConfirm:
			arg_6_0.onConfirm(), SFX_CONFIRM)

return var_0_0
