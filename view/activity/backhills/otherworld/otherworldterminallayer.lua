﻿local var_0_0 = class("OtherworldTerminalLayer", import("view.base.BaseUI"))

var_0_0.PAGE_PERSONAL = 1
var_0_0.PAGE_ADVENTURE = 2
var_0_0.PAGE_GUARDIAN = 3

local var_0_1 = var_0_0.PAGE_PERSONAL

function var_0_0.getUIName(arg_1_0)
	return "OtherworldTerminalUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
	arg_2_0:addListener()
end

function var_0_0.initData(arg_3_0)
	return
end

function var_0_0.findUI(arg_4_0)
	arg_4_0.windowTF = arg_4_0:findTF("window")
	arg_4_0.togglesTF = arg_4_0:findTF("toggles", arg_4_0.windowTF)
	arg_4_0.adventureTipTF = arg_4_0:findTF("2/tip", arg_4_0.togglesTF)

	setText(arg_4_0:findTF(var_0_0.PAGE_PERSONAL .. "/Text", arg_4_0.togglesTF), i18n("terminal_personal_title"))
	setText(arg_4_0:findTF(var_0_0.PAGE_ADVENTURE .. "/Text", arg_4_0.togglesTF), i18n("terminal_adventure_title"))
	setText(arg_4_0:findTF(var_0_0.PAGE_GUARDIAN .. "/Text", arg_4_0.togglesTF), i18n("terminal_guardian_title"))

	local var_4_0 = arg_4_0:findTF("pages", arg_4_0.windowTF)
	local var_4_1 = getProxy(ActivityProxy):getActivityById(ActivityConst.OTHER_WORLD_TERMINAL_EVENT_ID)

	if var_4_1 and not var_4_1:isEnd() then
		arg_4_0.personalPage = TerminalPersonalPage.New(var_4_0, arg_4_0, {
			upgrade = arg_4_0.contextData.upgrade
		})
	else
		arg_4_0.personalPage = nil
	end

	arg_4_0.adventurePage = TerminalAdventurePage.New(var_4_0, arg_4_0)
	arg_4_0.guardianPage = TerminalGuardianPage.New(var_4_0, arg_4_0)
	arg_4_0.pages = {
		[var_0_0.PAGE_PERSONAL] = arg_4_0.personalPage,
		[var_0_0.PAGE_ADVENTURE] = arg_4_0.adventurePage,
		[var_0_0.PAGE_GUARDIAN] = arg_4_0.guardianPage
	}
end

function var_0_0.addListener(arg_5_0)
	onButton(arg_5_0, arg_5_0:findTF("close_btn", arg_5_0.windowTF), function()
		arg_5_0:onBackPressed()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0:findTF("mask"), function()
		arg_5_0:onBackPressed()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0:findTF("help_btn", arg_5_0.windowTF), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.otherworld_terminal_help.tip
		})
	end, SFX_CANCEL)
	eachChild(arg_5_0.togglesTF, function(arg_9_0)
		onToggle(arg_5_0, arg_9_0, function(arg_10_0)
			if arg_10_0 then
				local var_10_0 = tonumber(arg_9_0.name)

				if arg_5_0.curPageIdx and arg_5_0.curPageIdx == var_10_0 then
					return
				end

				if var_10_0 == var_0_0.PAGE_PERSONAL and not arg_5_0.personalPage then
					pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

					return
				end

				arg_5_0.curPageIdx = var_10_0

				arg_5_0:SwitchPage()
			end
		end)
	end)
end

function var_0_0.didEnter(arg_11_0)
	local var_11_0 = arg_11_0.contextData.page or var_0_1

	if var_11_0 == var_0_0.PAGE_PERSONAL and not arg_11_0.personalPage then
		var_11_0 = var_0_0.PAGE_ADVENTURE
	end

	triggerToggle(arg_11_0:findTF(tostring(var_11_0), arg_11_0.togglesTF), true)
	arg_11_0:UpdateAdventureTip()
end

function var_0_0.SwitchPage(arg_12_0)
	for iter_12_0, iter_12_1 in pairs(arg_12_0.pages) do
		if iter_12_0 == arg_12_0.curPageIdx then
			iter_12_1:ExecuteAction("Show")

			arg_12_0.curPage = iter_12_1
		else
			iter_12_1:ExecuteAction("Hide")
		end
	end
end

function var_0_0.UpdateAdventurePtAct(arg_13_0, arg_13_1)
	arg_13_0.pages[var_0_0.PAGE_ADVENTURE]:ExecuteAction("UpdatePt", arg_13_1)
end

function var_0_0.UpdateAdventureTip(arg_14_0)
	local var_14_0 = TerminalAdventurePage.IsTip()

	setActive(arg_14_0.adventureTipTF, var_14_0)
end

function var_0_0.UpdateAdventureTaskAct(arg_15_0, arg_15_1)
	arg_15_0.pages[var_0_0.PAGE_ADVENTURE]:ExecuteAction("UpdateTask", arg_15_1)
end

function var_0_0.UpdateGuardianAct(arg_16_0, arg_16_1)
	arg_16_0.pages[var_0_0.PAGE_GUARDIAN]:ExecuteAction("UpdateView", arg_16_1)
end

function var_0_0.willExit(arg_17_0)
	for iter_17_0, iter_17_1 in pairs(arg_17_0.pages) do
		iter_17_1:Destroy()

		iter_17_1 = nil
	end

	if arg_17_0.contextData.onExit then
		arg_17_0.contextData.onExit()

		arg_17_0.contextData.onExit = nil
	end
end

return var_0_0
