﻿local var_0_0 = class("PtAwardLayer", import("view.base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "ActivitybonusWindow_btnVariant"
end

function var_0_0.init(arg_2_0)
	arg_2_0.window = PtAwardWindow.New(arg_2_0._tf, arg_2_0)

	function arg_2_0.window.Hide()
		arg_2_0:Hide()
	end

	arg_2_0.btn_banned = arg_2_0._tf:Find("window/btn_banned")
	arg_2_0.btn_get = arg_2_0._tf:Find("window/btn_get")
	arg_2_0.btn_got = arg_2_0._tf:Find("window/btn_got")
end

function var_0_0.didEnter(arg_4_0)
	onButton(arg_4_0, arg_4_0.btn_get, function()
		local var_5_0 = arg_4_0.contextData.ptData
		local var_5_1, var_5_2 = var_5_0:GetResProgress()

		arg_4_0:emit(ActivityMediator.EVENT_PT_OPERATION, {
			cmd = 1,
			activity_id = var_5_0:GetId(),
			arg1 = var_5_2
		})
	end, SFX_PANEL)
	arg_4_0:UpdateView()
end

function var_0_0.UpdateView(arg_6_0)
	arg_6_0.window:Show(arg_6_0.contextData.ptData)

	local var_6_0 = arg_6_0.contextData.ptData:CanGetAward()

	setActive(arg_6_0.btn_get, var_6_0)
	setActive(arg_6_0.btn_banned, not var_6_0)
end

function var_0_0.Hide(arg_7_0)
	arg_7_0:closeView()
end

function var_0_0.willExit(arg_8_0)
	if arg_8_0.window then
		arg_8_0.window:Dispose()

		arg_8_0.window = nil
	end
end

return var_0_0
