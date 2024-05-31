﻿local var_0_0 = class("CryptolaliaScrollRectItem")
local var_0_1 = Vector3(490, -35, 0)
local var_0_2 = Vector3(297, 297, 0)

local function var_0_3(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_0.midIndex - arg_1_1
	local var_1_1 = var_0_2 * var_1_0

	return var_0_1 + var_1_1
end

function var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	arg_2_0._go = arg_2_1
	arg_2_0._tf = arg_2_1.transform
	arg_2_0.initIndex = arg_2_3
	arg_2_0.midIndex = arg_2_2
	arg_2_0.img = arg_2_0._go:GetComponent(typeof(Image))
	arg_2_0.text = arg_2_0._tf:Find("Text")
	arg_2_0.index = arg_2_3

	local var_2_0 = var_0_3(arg_2_0, arg_2_3)

	arg_2_0:SetPosition(var_2_0)
end

function var_0_0.Interactable(arg_3_0, arg_3_1)
	arg_3_0.img.raycastTarget = arg_3_1

	setActive(arg_3_0.text, not arg_3_1)
end

function var_0_0.CanInteractable(arg_4_0)
	return arg_4_0.img.raycastTarget
end

function var_0_0.UpdateIndexWithAnim(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	local var_5_0 = math.abs(arg_5_1 - arg_5_0.index) > 1

	local function var_5_1(arg_6_0, arg_6_1)
		LeanTween.moveLocal(arg_5_0._go, arg_6_0, 0.594):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(arg_6_1))
	end

	if var_5_0 then
		local var_5_2 = var_0_3(arg_5_0, arg_5_2)

		var_5_1(var_5_2, function()
			arg_5_0:UpdateIndex(arg_5_1)
			arg_5_3()
		end)
	else
		local var_5_3 = var_0_3(arg_5_0, arg_5_1)

		var_5_1(var_5_3, function()
			arg_5_0:UpdateIndex(arg_5_1)
		end)
	end
end

function var_0_0.UpdateIndex(arg_9_0, arg_9_1)
	arg_9_0.index = arg_9_1
	arg_9_0._go.name = arg_9_1

	local var_9_0 = var_0_3(arg_9_0, arg_9_1)

	arg_9_0:SetPosition(var_9_0)
end

function var_0_0.UpdateIndexSilence(arg_10_0, arg_10_1)
	arg_10_0.index = arg_10_1
	arg_10_0._go.name = arg_10_1
end

function var_0_0.Refresh(arg_11_0)
	local var_11_0 = arg_11_0:GetIndex()

	arg_11_0:UpdateIndex(var_11_0)
end

function var_0_0.ClearAnimation(arg_12_0)
	if LeanTween.isTweening(arg_12_0._go) then
		LeanTween.cancel(arg_12_0._go)
	end

	arg_12_0:SetPosition(var_0_3(arg_12_0, arg_12_0.index))
end

function var_0_0.GetIndex(arg_13_0)
	return arg_13_0.index
end

function var_0_0.GetInitIndex(arg_14_0)
	return arg_14_0.initIndex
end

function var_0_0.IsMidIndex(arg_15_0)
	return arg_15_0:GetIndex() == arg_15_0.midIndex
end

function var_0_0.UpdateSprite(arg_16_0, arg_16_1)
	arg_16_0.img.sprite = arg_16_1

	arg_16_0.img:SetNativeSize()
end

function var_0_0.SetPosition(arg_17_0, arg_17_1)
	arg_17_0._tf.localPosition = arg_17_1
end

function var_0_0.GetPosition(arg_18_0)
	return arg_18_0._tf.localPosition
end

function var_0_0.Dispose(arg_19_0)
	arg_19_0:ClearAnimation()
end

return var_0_0
