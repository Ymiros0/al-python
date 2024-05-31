﻿local var_0_0 = class("BgStoryPlayer", import(".DialogueStoryPlayer"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.subImage = arg_1_0:findTF("sub", arg_1_0.bgPanel):GetComponent(typeof(Image))
	arg_1_0.bgRecord = nil
end

function var_0_0.Reset(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	var_0_0.super.super.Reset(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	setActive(arg_2_0.bgPanel, true)
	setActive(arg_2_0.subImage.gameObject, false)
	setActive(arg_2_0.actorPanel, false)
	arg_2_0:RecyclePainting({
		"actorLeft",
		"actorMiddle",
		"actorRgiht"
	})
end

function var_0_0.OnBgUpdate(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:GetBgName()

	if arg_3_0.bgRecord ~= var_3_0 then
		arg_3_0.bgRecord = var_3_0

		local var_3_1 = arg_3_1:GetFadeSpeed()

		arg_3_0:TweenValueForcanvasGroup(arg_3_0.bgPanelCg, 0, 1, var_3_1, 0, nil)
	end
end

function var_0_0.UpdateBg(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:GetSubBg()

	if var_4_0 then
		setActive(arg_4_0.subImage.gameObject, true)

		arg_4_0.subImage.sprite = arg_4_0:GetBg(var_4_0)
	end

	if not arg_4_1:GetBgName() then
		return
	end

	var_0_0.super.UpdateBg(arg_4_0, arg_4_1)
end

function var_0_0.OnInit(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	if arg_5_1:ShouldBlackScreen() then
		setActive(arg_5_0.curtain, true)
		arg_5_0.curtain:SetAsLastSibling()
		arg_5_3()
	else
		var_0_0.super.OnInit(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	end
end

function var_0_0.OnEnter(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	if arg_6_1:ShouldBlackScreen() then
		arg_6_0:DelayCall(arg_6_1:ShouldBlackScreen(), function()
			setActive(arg_6_0.curtain, true)
			arg_6_0.curtain:SetAsFirstSibling()
			assert(not arg_6_1:ExistOption())
			arg_6_3()
			triggerButton(arg_6_0._go)
		end)
	else
		local var_6_0 = arg_6_1:GetUnscaleDelay()

		if arg_6_0.autoNext then
			var_6_0 = var_6_0 - arg_6_0.script:GetTriggerDelayTime()
		end

		arg_6_0:UnscaleDelayCall(var_6_0, function()
			var_0_0.super.OnEnter(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
		end)
	end
end

function var_0_0.GetSideTF(arg_9_0, arg_9_1)
	local var_9_0
	local var_9_1
	local var_9_2
	local var_9_3

	if DialogueStep.SIDE_LEFT == arg_9_1 then
		var_9_0, var_9_1, var_9_2, var_9_3 = nil, arg_9_0.nameLeft, arg_9_0.nameLeftTxt
	elseif DialogueStep.SIDE_RIGHT == arg_9_1 then
		var_9_0, var_9_1, var_9_2, var_9_3 = nil, arg_9_0.nameRight, arg_9_0.nameRightTxt
	elseif DialogueStep.SIDE_MIDDLE == arg_9_1 then
		var_9_0, var_9_1, var_9_2, var_9_3 = nil, arg_9_0.nameLeft, arg_9_0.nameLeftTxt
	end

	return var_9_0, var_9_1, var_9_2, var_9_3
end

function var_0_0.Clear(arg_10_0, arg_10_1)
	arg_10_0.bgs = {}
	arg_10_0.goCG.alpha = 1
	arg_10_0.callback = nil
	arg_10_0.autoNext = nil
	arg_10_0.script = nil
	arg_10_0.subImage.sprite = nil

	arg_10_0:OnClear()

	if arg_10_1 then
		arg_10_1()
	end

	pg.DelegateInfo.New(arg_10_0)
end

function var_0_0.StoryEnd(arg_11_0)
	var_0_0.super.StoryEnd(arg_11_0)

	arg_11_0.bgRecord = nil
	arg_11_0.bgImage.sprite = nil
end

return var_0_0
