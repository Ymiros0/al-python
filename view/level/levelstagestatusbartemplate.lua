﻿local var_0_0 = class("LevelStageStatusBarTemplate", BaseSubPanel)

function var_0_0.OnInit(arg_1_0)
	arg_1_0.anim = arg_1_0._go:GetComponent(typeof(Animator))
	arg_1_0.animEvent = arg_1_0._go:GetComponent(typeof(DftAniEvent))
end

function var_0_0.OnShow(arg_2_0)
	pg.UIMgr.GetInstance():OverlayPanel(arg_2_0._tf, {
		weight = LayerWeightConst.THIRD_LAYER,
		groupName = LayerWeightConst.GROUP_LEVELUI
	})
	arg_2_0.animEvent:SetEndEvent(function()
		arg_2_0:Hide()
	end)
end

function var_0_0.OnHide(arg_4_0)
	arg_4_0.animEvent:SetEndEvent(nil)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_4_0._tf)
end

function var_0_0.PlayAnim(arg_5_0)
	arg_5_0:Hide()
	arg_5_0:Show()
end

return var_0_0
