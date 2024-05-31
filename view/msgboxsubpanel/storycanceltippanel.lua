﻿local var_0_0 = class("StoryCancelTipPanel", import(".MsgboxSubPanel"))

function var_0_0.getUIName(arg_1_0)
	return "Msgbox4StoryCancelTip"
end

function var_0_0.OnInit(arg_2_0)
	setText(arg_2_0._tf:Find("Name"), i18n("autofight_story"))
end

function var_0_0.PreRefresh(arg_3_0, arg_3_1)
	arg_3_1.title = pg.MsgboxMgr.TITLE_INFORMATION

	var_0_0.super.PreRefresh(arg_3_0, arg_3_1)
end

function var_0_0.OnRefresh(arg_4_0, arg_4_1)
	arg_4_0:SetWindowSize(Vector2(1000, 640))

	local var_4_0 = arg_4_0._tf:Find("CircleProgress")
	local var_4_1 = arg_4_0._tf:Find("TimeText")
	local var_4_2 = 5

	LeanTween.value(go(var_4_0), var_4_2, 0, var_4_2):setOnUpdate(System.Action_float(function(arg_5_0)
		setFillAmount(var_4_0, arg_5_0 - math.floor(arg_5_0))
		setText(var_4_1, math.clamp(math.ceil(arg_5_0), 0, var_4_2))
	end)):setOnComplete(System.Action(function()
		existCall(arg_4_1.onYes)
		arg_4_0:closeView()
	end))
end

function var_0_0.OnHide(arg_7_0)
	return
end

function var_0_0.OnDestory(arg_8_0)
	LeanTween.cancel(arg_8_0._tf:Find("CircleProgress"))
end

return var_0_0
