﻿local var_0_0 = class("EducateCharDockScene", import("view.base.BaseUI"))

var_0_0.ON_CLOSE_VIEW = "EducateCharDockScene.ON_CLOSE_VIEW"
var_0_0.ON_SELECT = "EducateCharDockScene.ON_SELECT"
var_0_0.ON_CONFIRM = "EducateCharDockScene.ON_CONFIRM"
var_0_0.MSG_CLEAR_TIP = "EducateCharDockScene.MSG_CLEAR_TIP"

function var_0_0.getUIName(arg_1_0)
	return "EducateCharDockUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.backBtn = arg_2_0:findTF("adapt/top/back")
	arg_2_0.homeBtn = arg_2_0:findTF("adapt/top/home")
	arg_2_0.selectPage = EducateCharSelectPage.New(arg_2_0._tf:Find("adapt/pages"), arg_2_0.event)
	arg_2_0.groupPage = EducateCharGroupPage.New(arg_2_0._tf:Find("adapt/pages/groupPage"), arg_2_0.event, arg_2_0.contextData)
end

function var_0_0.didEnter(arg_3_0)
	arg_3_0.groupPage:Update()
	onButton(arg_3_0, arg_3_0.backBtn, function()
		if arg_3_0.selectPage and arg_3_0.selectPage:GetLoaded() and arg_3_0.selectPage:isShowing() then
			arg_3_0.selectPage:Back(function()
				arg_3_0.groupPage:Show()
				arg_3_0.selectPage:Hide()
			end)

			return
		end

		arg_3_0:closeView()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.homeBtn, function()
		arg_3_0:emit(var_0_0.ON_HOME)
	end, SFX_PANEL)
	arg_3_0:bind(var_0_0.ON_CLOSE_VIEW, function()
		arg_3_0:closeView()
	end)
	arg_3_0:bind(var_0_0.ON_SELECT, function(arg_8_0, arg_8_1, arg_8_2)
		arg_3_0.groupPage:Hide()
		arg_3_0.selectPage:ExecuteAction("Update", arg_8_1, arg_8_2)
	end)
	arg_3_0:bind(var_0_0.ON_CONFIRM, function(arg_9_0, arg_9_1)
		arg_3_0.groupPage:Show()
		arg_3_0.selectPage:Hide()
		arg_3_0.groupPage:FlushList(arg_9_1)
		arg_3_0:emit(EducateCharDockMediator.ON_SELECTED, arg_9_1)
	end)
end

function var_0_0.onBackPressed(arg_10_0)
	if arg_10_0.selectPage and arg_10_0.selectPage:GetLoaded() and arg_10_0.selectPage:isShowing() then
		triggerButton(arg_10_0.backBtn)

		return
	end

	var_0_0.super.onBackPressed(arg_10_0)
end

function var_0_0.willExit(arg_11_0)
	if arg_11_0.selectPage then
		arg_11_0.selectPage:Destroy()

		arg_11_0.selectPage = nil
	end

	if arg_11_0.groupPage then
		arg_11_0.groupPage:Destroy()

		arg_11_0.groupPage = nil
	end
end

return var_0_0
