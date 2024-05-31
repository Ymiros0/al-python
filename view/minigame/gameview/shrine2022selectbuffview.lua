﻿local var_0_0 = class("Shrine2022SelectBuffView", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "Shrine2022SelectBuffUI"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:initData()
	arg_2_0:initUI()
	pg.UIMgr.GetInstance():BlurPanel(arg_2_0._tf)
	arg_2_0:Show()
	arg_2_0:playEnterAni(true)
end

function var_0_0.OnDestroy(arg_3_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_3_0._tf)
	arg_3_0:cleanManagedTween()
end

function var_0_0.initData(arg_4_0)
	arg_4_0.onSelectFunc = arg_4_0.contextData.onSelect
end

function var_0_0.initUI(arg_5_0)
	arg_5_0.bg = arg_5_0:findTF("BG")
	arg_5_0.cloud1 = arg_5_0:findTF("Cloud1")
	arg_5_0.cloud2 = arg_5_0:findTF("Cloud2")
	arg_5_0.buffListTF = arg_5_0:findTF("BuffContainer")
	arg_5_0.buffListCG = GetComponent(arg_5_0.buffListTF, "CanvasGroup")

	for iter_5_0 = 1, 3 do
		local var_5_0 = arg_5_0.buffListTF:GetChild(iter_5_0 - 1)

		onButton(arg_5_0, var_5_0, function()
			if arg_5_0.onSelectFunc then
				arg_5_0.onSelectFunc(iter_5_0)
			end

			arg_5_0:closeMySelf()
		end, SFX_PANEL)
	end

	onButton(arg_5_0, arg_5_0.bg, function()
		arg_5_0:closeMySelf()
	end, SFX_CANCEL)
end

function var_0_0.playEnterAni(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = arg_8_1 and 1000 or 0
	local var_8_1 = arg_8_1 and 0 or 1000
	local var_8_2 = {
		x = var_8_0,
		y = rtf(arg_8_0.cloud1).anchoredPosition.y
	}
	local var_8_3 = arg_8_1 and -1000 or 0
	local var_8_4 = arg_8_1 and 0 or -1000
	local var_8_5 = {
		x = var_8_3,
		y = rtf(arg_8_0.cloud2).anchoredPosition.y
	}
	local var_8_6 = arg_8_1 and 0 or 1
	local var_8_7 = arg_8_1 and 1 or 0
	local var_8_8 = 0.3

	arg_8_0.isPlaying = true

	arg_8_0:managedTween(LeanTween.value, nil, go(arg_8_0.cloud1), 0, 1, var_8_8):setOnUpdate(System.Action_float(function(arg_9_0)
		local var_9_0 = var_8_0 + (var_8_1 - var_8_0) * arg_9_0
		local var_9_1 = var_8_3 + (var_8_4 - var_8_3) * arg_9_0
		local var_9_2 = var_8_6 + (var_8_7 - var_8_6) * arg_9_0

		var_8_2.x = var_9_0

		setAnchoredPosition(arg_8_0.cloud1, var_8_2)

		var_8_5.x = var_9_1

		setAnchoredPosition(arg_8_0.cloud2, var_8_5)

		arg_8_0.buffListCG.alpha = var_9_2
	end)):setOnComplete(System.Action(function()
		arg_8_0.isPlaying = false

		if arg_8_2 then
			arg_8_2()
		end
	end))
end

function var_0_0.closeMySelf(arg_11_0)
	if arg_11_0.isPlaying then
		return
	end

	arg_11_0:playEnterAni(false, function()
		arg_11_0:Destroy()
	end)
end

return var_0_0
