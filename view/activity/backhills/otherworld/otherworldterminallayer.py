local var_0_0 = class("OtherworldTerminalLayer", import("view.base.BaseUI"))

var_0_0.PAGE_PERSONAL = 1
var_0_0.PAGE_ADVENTURE = 2
var_0_0.PAGE_GUARDIAN = 3

local var_0_1 = var_0_0.PAGE_PERSONAL

def var_0_0.getUIName(arg_1_0):
	return "OtherworldTerminalUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.initData(arg_3_0):
	return

def var_0_0.findUI(arg_4_0):
	arg_4_0.windowTF = arg_4_0.findTF("window")
	arg_4_0.togglesTF = arg_4_0.findTF("toggles", arg_4_0.windowTF)
	arg_4_0.adventureTipTF = arg_4_0.findTF("2/tip", arg_4_0.togglesTF)

	setText(arg_4_0.findTF(var_0_0.PAGE_PERSONAL .. "/Text", arg_4_0.togglesTF), i18n("terminal_personal_title"))
	setText(arg_4_0.findTF(var_0_0.PAGE_ADVENTURE .. "/Text", arg_4_0.togglesTF), i18n("terminal_adventure_title"))
	setText(arg_4_0.findTF(var_0_0.PAGE_GUARDIAN .. "/Text", arg_4_0.togglesTF), i18n("terminal_guardian_title"))

	local var_4_0 = arg_4_0.findTF("pages", arg_4_0.windowTF)
	local var_4_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.OTHER_WORLD_TERMINAL_EVENT_ID)

	if var_4_1 and not var_4_1.isEnd():
		arg_4_0.personalPage = TerminalPersonalPage.New(var_4_0, arg_4_0, {
			upgrade = arg_4_0.contextData.upgrade
		})
	else
		arg_4_0.personalPage = None

	arg_4_0.adventurePage = TerminalAdventurePage.New(var_4_0, arg_4_0)
	arg_4_0.guardianPage = TerminalGuardianPage.New(var_4_0, arg_4_0)
	arg_4_0.pages = {
		[var_0_0.PAGE_PERSONAL] = arg_4_0.personalPage,
		[var_0_0.PAGE_ADVENTURE] = arg_4_0.adventurePage,
		[var_0_0.PAGE_GUARDIAN] = arg_4_0.guardianPage
	}

def var_0_0.addListener(arg_5_0):
	onButton(arg_5_0, arg_5_0.findTF("close_btn", arg_5_0.windowTF), function()
		arg_5_0.onBackPressed(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("mask"), function()
		arg_5_0.onBackPressed(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("help_btn", arg_5_0.windowTF), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.otherworld_terminal_help.tip
		}), SFX_CANCEL)
	eachChild(arg_5_0.togglesTF, function(arg_9_0)
		onToggle(arg_5_0, arg_9_0, function(arg_10_0)
			if arg_10_0:
				local var_10_0 = tonumber(arg_9_0.name)

				if arg_5_0.curPageIdx and arg_5_0.curPageIdx == var_10_0:
					return

				if var_10_0 == var_0_0.PAGE_PERSONAL and not arg_5_0.personalPage:
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

					return

				arg_5_0.curPageIdx = var_10_0

				arg_5_0.SwitchPage()))

def var_0_0.didEnter(arg_11_0):
	local var_11_0 = arg_11_0.contextData.page or var_0_1

	if var_11_0 == var_0_0.PAGE_PERSONAL and not arg_11_0.personalPage:
		var_11_0 = var_0_0.PAGE_ADVENTURE

	triggerToggle(arg_11_0.findTF(tostring(var_11_0), arg_11_0.togglesTF), True)
	arg_11_0.UpdateAdventureTip()

def var_0_0.SwitchPage(arg_12_0):
	for iter_12_0, iter_12_1 in pairs(arg_12_0.pages):
		if iter_12_0 == arg_12_0.curPageIdx:
			iter_12_1.ExecuteAction("Show")

			arg_12_0.curPage = iter_12_1
		else
			iter_12_1.ExecuteAction("Hide")

def var_0_0.UpdateAdventurePtAct(arg_13_0, arg_13_1):
	arg_13_0.pages[var_0_0.PAGE_ADVENTURE].ExecuteAction("UpdatePt", arg_13_1)

def var_0_0.UpdateAdventureTip(arg_14_0):
	local var_14_0 = TerminalAdventurePage.IsTip()

	setActive(arg_14_0.adventureTipTF, var_14_0)

def var_0_0.UpdateAdventureTaskAct(arg_15_0, arg_15_1):
	arg_15_0.pages[var_0_0.PAGE_ADVENTURE].ExecuteAction("UpdateTask", arg_15_1)

def var_0_0.UpdateGuardianAct(arg_16_0, arg_16_1):
	arg_16_0.pages[var_0_0.PAGE_GUARDIAN].ExecuteAction("UpdateView", arg_16_1)

def var_0_0.willExit(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0.pages):
		iter_17_1.Destroy()

		iter_17_1 = None

	if arg_17_0.contextData.onExit:
		arg_17_0.contextData.onExit()

		arg_17_0.contextData.onExit = None

return var_0_0
