local var_0_0 = class("RefluxScene", import("..base.BaseUI"))

var_0_0.Sign = 1
var_0_0.Task = 2
var_0_0.PT = 3
var_0_0.Shop = 4

def var_0_0.getUIName(arg_1_0):
	return "RefluxUI"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.initData()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updateRedPotList()

	if not getProxy(RefluxProxy).isInRefluxTime():
		arg_3_0.closeView()

		return

	if not arg_3_0.tryOpenLetterView():
		arg_3_0.tryAutoOpenLastView()

	arg_3_0.updateDay()

def var_0_0.willExit(arg_4_0):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.viewList):
		if iter_4_1 and iter_4_1.GetLoaded():
			iter_4_1.Destroy()

	if arg_4_0.signView and arg_4_0.signView.GetLoaded():
		arg_4_0.signView.Destroy()

	if arg_4_0.taskView and arg_4_0.taskView.GetLoaded():
		arg_4_0.taskView.Destroy()

	if arg_4_0.ptView and arg_4_0.ptView.GetLoaded():
		arg_4_0.ptView.Destroy()

	if arg_4_0.shopView and arg_4_0.shopView.GetLoaded():
		arg_4_0.shopView.Destroy()

def var_0_0.onBackPressed(arg_5_0):
	if arg_5_0.letterView and arg_5_0.letterView.isShowing():
		arg_5_0.letterView.OnBackPress()

		return

	arg_5_0.closeView()

def var_0_0.findUI(arg_6_0):
	arg_6_0.letterContainer = arg_6_0.findTF("PanelLetter")
	arg_6_0.panelContainer = arg_6_0.findTF("PanelContainer")

	local var_6_0 = arg_6_0.findTF("left/left_bar")

	arg_6_0.letterBtn = arg_6_0.findTF("letter", var_6_0)
	arg_6_0.signToggle = arg_6_0.findTF("tabs/sign", var_6_0)
	arg_6_0.taskToggle = arg_6_0.findTF("tabs/task", var_6_0)
	arg_6_0.ptToggle = arg_6_0.findTF("tabs/pt", var_6_0)
	arg_6_0.shopToggle = arg_6_0.findTF("tabs/shop", var_6_0)
	arg_6_0.toggleList = {
		[var_0_0.Sign] = arg_6_0.signToggle,
		[var_0_0.Task] = arg_6_0.taskToggle,
		[var_0_0.PT] = arg_6_0.ptToggle,
		[var_0_0.Shop] = arg_6_0.shopToggle
	}
	arg_6_0.redPotList = {
		[var_0_0.Sign] = arg_6_0.findTF("Red", arg_6_0.signToggle),
		[var_0_0.Task] = arg_6_0.findTF("Red", arg_6_0.taskToggle),
		[var_0_0.PT] = arg_6_0.findTF("Red", arg_6_0.ptToggle),
		[var_0_0.Shop] = arg_6_0.findTF("Red", arg_6_0.shopToggle)
	}
	arg_6_0.backBtn = arg_6_0.findTF("back", var_6_0)
	arg_6_0.dayText = arg_6_0.findTF("time/text")

	local var_6_1 = arg_6_0.findTF("time/icon")

	setText(var_6_1, i18n("reflux_word_1"))

	local var_6_2 = arg_6_0.findTF("time/icon1")

	setText(var_6_2, i18n("word_date"))

def var_0_0.initData(arg_7_0):
	arg_7_0.curViewIndex = 0
	arg_7_0.letterView = RefluxLetterView.New(arg_7_0.letterContainer, arg_7_0.event, arg_7_0.contextData)
	arg_7_0.signView = RefluxSignView.New(arg_7_0.panelContainer, arg_7_0.event, arg_7_0.contextData)
	arg_7_0.taskView = RefluxTaskView.New(arg_7_0.panelContainer, arg_7_0.event, arg_7_0.contextData)
	arg_7_0.ptView = RefluxPTView.New(arg_7_0.panelContainer, arg_7_0.event, arg_7_0.contextData)
	arg_7_0.shopView = RefluxShopView.New(arg_7_0.panelContainer, arg_7_0.event, arg_7_0.contextData)
	arg_7_0.viewList = {
		[var_0_0.Sign] = arg_7_0.signView,
		[var_0_0.Task] = arg_7_0.taskView,
		[var_0_0.PT] = arg_7_0.ptView,
		[var_0_0.Shop] = arg_7_0.shopView
	}

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.backBtn, function()
		arg_8_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.letterBtn, function()
		arg_8_0.switchLetter(), SFX_PANEL)
	onToggle(arg_8_0, arg_8_0.signToggle, function(arg_11_0)
		if arg_11_0 == True:
			arg_8_0.switchPage(var_0_0.Sign), SFX_PANEL)
	onToggle(arg_8_0, arg_8_0.taskToggle, function(arg_12_0)
		if arg_12_0 == True:
			arg_8_0.switchPage(var_0_0.Task), SFX_PANEL)
	onToggle(arg_8_0, arg_8_0.ptToggle, function(arg_13_0)
		if arg_13_0 == True:
			arg_8_0.switchPage(var_0_0.PT), SFX_PANEL)
	onToggle(arg_8_0, arg_8_0.shopToggle, function(arg_14_0)
		if arg_14_0 == True:
			arg_8_0.switchPage(var_0_0.Shop)
			arg_8_0.updateRedPotList(), SFX_PANEL)

def var_0_0.tryOpenLetterView(arg_15_0):
	local var_15_0 = getProxy(RefluxProxy).returnTimestamp
	local var_15_1 = getProxy(PlayerProxy).getRawData().id .. "_" .. var_15_0

	if PlayerPrefs.GetInt(var_15_1, 0) != 1:
		PlayerPrefs.SetInt(var_15_1, 1)
		PlayerPrefs.Save()
		arg_15_0.letterView.ActionInvoke("setCloseFunc", function()
			triggerToggle(arg_15_0.toggleList[var_0_0.Sign], True))
		arg_15_0.switchLetter()

		return True
	else
		return False

def var_0_0.switchPage(arg_17_0, arg_17_1):
	if arg_17_0.curViewIndex != arg_17_1:
		local var_17_0 = arg_17_0.viewList[arg_17_1]

		var_17_0.Load()
		var_17_0.ActionInvoke("Show")
		var_17_0.ActionInvoke("updateOutline")

		if arg_17_0.curViewIndex > 0:
			arg_17_0.viewList[arg_17_0.curViewIndex].Hide()

		arg_17_0.curViewIndex = arg_17_1
		arg_17_0.contextData.lastViewIndex = arg_17_1

def var_0_0.tryAutoOpenLastView(arg_18_0):
	if arg_18_0.contextData.lastViewIndex:
		triggerToggle(arg_18_0.toggleList[arg_18_0.contextData.lastViewIndex], True)
	else
		triggerToggle(arg_18_0.toggleList[var_0_0.Sign], True)

def var_0_0.switchLetter(arg_19_0):
	arg_19_0.letterView.Load()
	arg_19_0.letterView.ActionInvoke("Show")

def var_0_0.updateRedPotList(arg_20_0):
	local var_20_0 = RefluxTaskView.isAnyTaskCanGetAward()
	local var_20_1 = RefluxPTView.isAnyPTCanGetAward()
	local var_20_2 = RefluxShopView.isShowRedPot()

	setActive(arg_20_0.redPotList[var_0_0.Sign], False)
	setActive(arg_20_0.redPotList[var_0_0.Task], var_20_0)
	setActive(arg_20_0.redPotList[var_0_0.PT], var_20_1)
	setActive(arg_20_0.redPotList[var_0_0.Shop], var_20_2)

def var_0_0.updateDay(arg_21_0):
	local var_21_0 = getProxy(RefluxProxy)
	local var_21_1 = pg.TimeMgr.GetInstance()
	local var_21_2 = #pg.return_sign_template.all
	local var_21_3 = math.clamp(var_21_1.DiffDay(var_21_0.returnTimestamp, var_21_1.GetServerTime()), 0, var_21_2 - 1)

	setText(arg_21_0.dayText, var_21_2 - var_21_3)

return var_0_0
