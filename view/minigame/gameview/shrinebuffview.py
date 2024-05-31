local var_0_0 = class("ShrineBuffView", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ShrineBuff"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.Show()
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.updateView()

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0.contextData.onClose()

	arg_3_0.lockBackPress = False

def var_0_0.initData(arg_4_0):
	arg_4_0.lockBackPress = True

def var_0_0.initUI(arg_5_0):
	arg_5_0.bg = arg_5_0.findTF("BG")
	arg_5_0.backBtn = arg_5_0.findTF("BackBtn")
	arg_5_0.buffListTF = arg_5_0.findTF("Main/BuffList")

	for iter_5_0 = 1, 3:
		local var_5_0 = arg_5_0.buffListTF.GetChild(iter_5_0 - 1)

		onButton(arg_5_0, var_5_0, function()
			arg_5_0.contextData.onSelect(iter_5_0)
			arg_5_0.Destroy(), SFX_PANEL)

	onButton(arg_5_0, arg_5_0.backBtn, function()
		arg_5_0.Destroy(), SFX_CANCEL)

def var_0_0.updateView(arg_8_0):
	return

return var_0_0
