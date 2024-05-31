local var_0_0 = class("PrayPoolHomeView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "PrayPoolHomeView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.Show()

def var_0_0.OnDestroy(arg_3_0):
	return

def var_0_0.OnBackPress(arg_4_0):
	return

def var_0_0.initData(arg_5_0):
	arg_5_0.prayProxy = getProxy(PrayProxy)

def var_0_0.initUI(arg_6_0):
	arg_6_0.startBtn = arg_6_0.findTF("StartBtn")

	onButton(arg_6_0, arg_6_0.startBtn, function()
		arg_6_0.prayProxy.updatePageState(PrayProxy.STATE_SELECT_POOL)
		arg_6_0.emit(PrayPoolConst.SWITCH_TO_SELECT_POOL_PAGE, PrayProxy.STATE_SELECT_POOL), SFX_PANEL)

return var_0_0
