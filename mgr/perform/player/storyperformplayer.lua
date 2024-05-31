﻿local var_0_0 = class("StoryPerformPlayer", import(".BasePerformPlayer"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.noDrawGraphicCom = arg_1_0._tf.parent:GetComponent("NoDrawingGraphic")
end

function var_0_0.Play(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0:Show()

	arg_2_0.noDrawGraphicCom.enabled = false

	pg.NewStoryMgr.GetInstance():Play(arg_2_1.param or "", function()
		arg_2_0.noDrawGraphicCom.enabled = true

		if arg_2_2 then
			arg_2_2()
		end
	end, true)
end

function var_0_0.Clear(arg_4_0)
	arg_4_0:Hide()
end

return var_0_0
