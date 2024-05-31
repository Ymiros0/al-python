﻿local var_0_0 = class("TrophyView")

var_0_0.GRAY_COLOR = Color(0.764, 0.764, 0.764, 0.784)

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._trophyNamePic = findTF(arg_1_0._tf, "frame/trophyName/Text")
	arg_1_0._trophyNameBG = findTF(arg_1_0._tf, "frame/trophyName")
	arg_1_0._trophyIcon = findTF(arg_1_0._tf, "frame/trophyIcon")
	arg_1_0._trophyDescUpper = findTF(arg_1_0._tf, "frame/trophyDesc/Text_upper"):GetComponent(typeof(Text))
	arg_1_0._trophyDescLower = findTF(arg_1_0._tf, "frame/trophyDesc/Text_lower"):GetComponent(typeof(Text))
	arg_1_0._trophyCountBG = findTF(arg_1_0._tf, "frame/trophyCount")
	arg_1_0._trophyCount = findTF(arg_1_0._tf, "frame/trophyCount/Text"):GetComponent(typeof(Text))
	arg_1_0._progressBar = findTF(arg_1_0._tf, "frame/trophy_progress/Fill"):GetComponent(typeof(Slider))
end

function var_0_0.UpdateTrophyGroup(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_1:getDisplayTrophy()
	local var_2_1 = arg_2_1:getProgressTrophy()

	arg_2_0:updateInfoView(var_2_0)
	arg_2_0:updateProgressView(var_2_1)
end

function var_0_0.ProgressingForm(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:getProgressTrophy()

	arg_3_0:updateInfoView(var_3_0)
	arg_3_0:updateProgressView(var_3_0)
end

function var_0_0.ClaimForm(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getMaxClaimedTrophy()

	if var_4_0 then
		arg_4_0:updateInfoView(var_4_0)
		arg_4_0:updateProgressView(var_4_0)
	end
end

function var_0_0.updateInfoView(arg_5_0, arg_5_1)
	arg_5_0._trophy = arg_5_1
	arg_5_0._trophyCount.text = arg_5_1:getConfig("rank")

	if not arg_5_1:isClaimed() and not arg_5_1:canClaimed() then
		setActive(arg_5_0._trophyCount, false)
	end

	LoadImageSpriteAsync("medal/" .. arg_5_1:getConfig("icon"), arg_5_0._trophyIcon, true)
	LoadImageSpriteAsync("medal/" .. arg_5_1:getConfig("label"), arg_5_0._trophyNamePic, true)
	arg_5_0:setGray(arg_5_0._trophyIcon, not arg_5_1:isClaimed())
	arg_5_0:setGray(arg_5_0._trophyNamePic, not arg_5_1:isClaimed())
	arg_5_0:setGray(arg_5_0._trophyNameBG, not arg_5_1:isClaimed())
	arg_5_0:setGray(arg_5_0._trophyCountBG, not arg_5_1:isClaimed())

	arg_5_0._trophyDescUpper.text = arg_5_1:getConfig("explain1")
	arg_5_0._trophyDescLower.text = arg_5_1:getConfig("explain2")
end

function var_0_0.setGray(arg_6_0, arg_6_1, arg_6_2)
	setGray(arg_6_1, arg_6_2, true)

	if arg_6_2 then
		arg_6_1:GetComponent(typeof(Image)).color = var_0_0.GRAY_COLOR
	else
		arg_6_1:GetComponent(typeof(Image)).color = Color.white
	end
end

function var_0_0.updateProgressView(arg_7_0, arg_7_1)
	arg_7_0._progressTrophy = arg_7_1
	arg_7_0._progressBar.value = arg_7_1:getProgressRate()
end

function var_0_0.GetTrophyClaimTipsID(arg_8_0)
	return "reminder_" .. math.floor(arg_8_0._trophy:getConfig("icon") / 10)
end

function var_0_0.SetTrophyReminder(arg_9_0, arg_9_1)
	arg_9_0._reminder = tf(arg_9_1)

	arg_9_0._reminder:SetParent(findTF(arg_9_0._tf, "frame"), false)

	arg_9_0._reminder.localPosition = arg_9_0._trophyIcon.localPosition

	setActive(arg_9_0._reminder, arg_9_0._progressTrophy:canClaimed() and not arg_9_0._progressTrophy:isClaimed())
end

function var_0_0.PlayClaimAnima(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	arg_10_0._isPlaying = true

	setActive(arg_10_0._reminder, false)

	local var_10_0 = arg_10_0._tf:GetComponent(typeof(Animator))

	var_10_0.enabled = true

	arg_10_0._tf:GetComponent(typeof(DftAniEvent)):SetEndEvent(function(arg_11_0)
		arg_10_3()
		setActive(arg_10_0._reminder, arg_10_0._progressTrophy:canClaimed() and not arg_10_0._progressTrophy:isClaimed())
	end)
	var_10_0:Play("trophy_upper", -1, 0)
	setActive(arg_10_2, true)

	local var_10_1 = tf(arg_10_2)

	var_10_1:SetParent(findTF(arg_10_0._tf, "frame"), false)

	var_10_1.localScale = Vector3(1, 1, 0)

	LuaHelper.SetParticleEndEvent(arg_10_2, function()
		arg_10_0._isPlaying = false

		Object.Destroy(arg_10_2)
	end)
end

function var_0_0.IsPlaying(arg_13_0)
	return arg_13_0._isPlaying
end

return var_0_0
