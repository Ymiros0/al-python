﻿local var_0_0 = class("ArchivesWorldBossMsgboxPage", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "ArchivesWorldBossMsgboxUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.yesBtn = arg_2_0:findTF("Box/ConfirmBtn")
	arg_2_0.cancelBtn = arg_2_0:findTF("Box/CancelBtn")
	arg_2_0.contentTxt = arg_2_0:findTF("Box/Text"):GetComponent(typeof(Text))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.yesBtn, function()
		if arg_3_0.onYes then
			arg_3_0.onYes()
		end

		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.Show(arg_7_0, arg_7_1)
	var_0_0.super.Show(arg_7_0)

	arg_7_0.contentTxt.text = arg_7_1.content
	arg_7_0.onYes = arg_7_1.onYes
end

function var_0_0.Hide(arg_8_0)
	var_0_0.super.Hide(arg_8_0)

	if arg_8_0.onYes then
		arg_8_0.onYes = nil
	end
end

function var_0_0.OnDestroy(arg_9_0)
	if arg_9_0:isShowing() then
		arg_9_0:Hide()
	end
end

return var_0_0
