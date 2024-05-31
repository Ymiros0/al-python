﻿local var_0_0 = class("LittleRenownPage", import(".TemplatePage.PtTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.heartTpl = arg_1_0:findTF("HeartTpl", arg_1_0.bg)
	arg_1_0.heartContainer = arg_1_0:findTF("HeartContainer", arg_1_0.bg)
	arg_1_0.heartUIItemList = UIItemList.New(arg_1_0.heartContainer, arg_1_0.heartTpl)

	arg_1_0.heartUIItemList:make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate then
			local var_2_0 = arg_2_1 + 1
			local var_2_1 = arg_1_0.ptData:GetLevelProgress()
			local var_2_2 = arg_1_0:findTF("Full", arg_2_2)

			setActive(var_2_2, not (var_2_1 < var_2_0))
		end
	end)
end

function var_0_0.OnUpdateFlush(arg_3_0)
	var_0_0.super.OnUpdateFlush(arg_3_0)

	local var_3_0, var_3_1 = arg_3_0.ptData:GetLevelProgress()

	arg_3_0.heartUIItemList:align(var_3_1)
end

return var_0_0
