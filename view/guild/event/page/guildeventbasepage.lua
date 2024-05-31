﻿local var_0_0 = class("GuildEventBasePage", import("....base.BaseSubView"))

function var_0_0.Show(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0:UpdateData(arg_1_1, arg_1_2, arg_1_3)
	var_0_0.super.Show(arg_1_0)
	assert(arg_1_0._tf)
	pg.UIMgr:GetInstance():BlurPanel(arg_1_0._tf)
	arg_1_0:OnShow()

	arg_1_0.inAnim = true

	arg_1_0:EnterAnim(function()
		arg_1_0.inAnim = false
	end)
end

function var_0_0.SetHideCallBack(arg_3_0, arg_3_1)
	arg_3_0.exitCallback = arg_3_1
end

function var_0_0.UpdateData(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_0.guild = arg_4_1
	arg_4_0.player = arg_4_2
	arg_4_0.extraData = arg_4_3
end

function var_0_0.Hide(arg_5_0, arg_5_1)
	local function var_5_0()
		arg_5_0.inAnim = false

		var_0_0.super.Hide(arg_5_0)
		assert(arg_5_0._tf)
		assert(arg_5_0._parentTf)
		pg.UIMgr:GetInstance():UnblurPanel(arg_5_0._tf, arg_5_0._parentTf)

		if not arg_5_1 and arg_5_0.exitCallback then
			arg_5_0.exitCallback()
		end
	end

	if not arg_5_1 then
		arg_5_0.inAnim = true

		arg_5_0:ExistAnim(var_5_0)
	else
		var_5_0()
	end
end

function var_0_0.OnDestroy(arg_7_0)
	arg_7_0:Hide(true)
end

function var_0_0.emit(arg_8_0, ...)
	if arg_8_0.inAnim then
		return
	end

	var_0_0.super.emit(arg_8_0, ...)
end

function var_0_0.EnterAnim(arg_9_0, arg_9_1)
	arg_9_1()
end

function var_0_0.ExistAnim(arg_10_0, arg_10_1)
	arg_10_1()
end

function var_0_0.OnShow(arg_11_0)
	return
end

return var_0_0
