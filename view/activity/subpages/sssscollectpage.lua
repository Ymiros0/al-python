﻿local var_0_0 = class("SSSSCollectPage", import(".TemplatePage.LinkCollectTemplatePage"))
local var_0_1 = 0.45
local var_0_2 = 0.2
local var_0_3 = 1.2
local var_0_4 = "event:/ui/kaiji"

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.effectBlankScreen = arg_1_0:findTF("blank_screen_effect", arg_1_0.bg)
	arg_1_0.effectOpen = arg_1_0:findTF("open_effect", arg_1_0.bg)
	arg_1_0.effectBlink = arg_1_0:findTF("blink_effect", arg_1_0.bg)
	arg_1_0.effectClick = arg_1_0:findTF("click_effect", arg_1_0.bg)
end

function var_0_0.OnFirstFlush(arg_2_0)
	var_0_0.super.OnFirstFlush(arg_2_0)

	local var_2_0 = arg_2_0.activity:getConfig("config_client")

	if arg_2_0.furnitureThemeBtn and var_2_0.furniture_theme_link then
		removeOnButton(arg_2_0.furnitureThemeBtn)
		onButton(arg_2_0, arg_2_0.furnitureThemeBtn, function()
			arg_2_0:PlayClickEffect(arg_2_0.furnitureThemeBtn, function()
				arg_2_0:DoSkip(var_2_0.furniture_theme_link[1], var_2_0.furniture_theme_link[2])
			end)
		end, SFX_PANEL)
	end

	if arg_2_0.medalBtn and var_2_0.medal_link then
		removeOnButton(arg_2_0.medalBtn)
		onButton(arg_2_0, arg_2_0.medalBtn, function()
			arg_2_0:PlayClickEffect(arg_2_0.furnitureThemeBtn, function()
				arg_2_0:DoSkip(var_2_0.medal_link[1], var_2_0.medal_link[2])
			end)
		end, SFX_PANEL)
	end

	arg_2_0:PlayOpenEffect()
end

function var_0_0.PlayOpenEffect(arg_7_0)
	setActive(arg_7_0.effectBlankScreen, true)
	setActive(arg_7_0.effectOpen, false)
	arg_7_0:managedTween(LeanTween.delayedCall, function()
		setActive(arg_7_0.effectOpen, true)
		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_4)
	end, var_0_2, nil)
	arg_7_0:managedTween(LeanTween.delayedCall, function()
		setActive(arg_7_0.effectBlankScreen, false)
	end, var_0_1, nil)
	arg_7_0:managedTween(LeanTween.delayedCall, function()
		setActive(arg_7_0.effectOpen, false)
		setActive(arg_7_0.effectBlink, true)
	end, var_0_2 + var_0_3, nil)
end

function var_0_0.PlayClickEffect(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = pg.UIMgr.GetInstance().OverlayEffect:GetChild(0)
	local var_11_1 = Vector3(192, 60, 0)
	local var_11_2 = var_11_0 and var_11_0.localPosition:Sub(var_11_1) or arg_11_1.localPosition

	setLocalPosition(arg_11_0.effectClick, var_11_2)
	setActive(arg_11_0.effectClick, true)
	arg_11_0:managedTween(LeanTween.delayedCall, function()
		setActive(arg_11_0.effectClick, false)

		if arg_11_2 then
			arg_11_2()
		end
	end, 0.3, nil)
end

function var_0_0.OnDestroy(arg_13_0)
	arg_13_0:cleanManagedTween()
end

return var_0_0
