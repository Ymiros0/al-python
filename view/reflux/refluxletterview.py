local var_0_0 = class("RefluxLetterView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "RefluxLetterUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.updateUI()

def var_0_0.OnDestroy(arg_3_0):
	return

def var_0_0.OnBackPress(arg_4_0):
	arg_4_0.Hide()

	if arg_4_0.closeCB:
		arg_4_0.closeCB()

def var_0_0.initData(arg_5_0):
	arg_5_0.refluxProxy = getProxy(RefluxProxy)

def var_0_0.initUI(arg_6_0):
	local var_6_0 = arg_6_0.findTF("billboard")

	arg_6_0.billboardTF = var_6_0
	arg_6_0.yearText = arg_6_0.findTF("year", var_6_0)
	arg_6_0.monthText = arg_6_0.findTF("month", var_6_0)
	arg_6_0.dateText = arg_6_0.findTF("date", var_6_0)
	arg_6_0.daysText = arg_6_0.findTF("days", var_6_0)
	arg_6_0.countText = arg_6_0.findTF("count", var_6_0)
	arg_6_0.shareBtn = arg_6_0.findTF("btn_share", var_6_0)

	setActive(arg_6_0.shareBtn, False)
	onButton(arg_6_0, arg_6_0.billboardTF, function()
		arg_6_0.OnBackPress(), SFX_PANEL)

def var_0_0.updateUI(arg_8_0):
	local var_8_0 = pg.TimeMgr.GetInstance()
	local var_8_1 = arg_8_0.refluxProxy.returnLastTimestamp
	local var_8_2 = arg_8_0.refluxProxy.returnTimestamp
	local var_8_3 = var_8_0.STimeDescS(var_8_1, "*t")

	setText(arg_8_0.yearText, var_8_3.year % 100)
	setText(arg_8_0.monthText, var_8_3.month)
	setText(arg_8_0.dateText, var_8_3.day)
	setText(arg_8_0.daysText, var_8_0.DiffDay(var_8_1, var_8_2))
	setText(arg_8_0.countText, arg_8_0.refluxProxy.returnShipNum)

def var_0_0.setCloseFunc(arg_9_0, arg_9_1):
	arg_9_0.closeCB = arg_9_1

return var_0_0
