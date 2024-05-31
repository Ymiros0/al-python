﻿local var_0_0 = class("NewYearSnackResultView", import(".SnackResultView"))

function var_0_0.getUIName(arg_1_0)
	return "NewYearSnackResult"
end

function var_0_0.updateView(arg_2_0)
	local var_2_0 = arg_2_0:calculateEXValue()

	if arg_2_0.contextData.countTime > 0 then
		setText(arg_2_0.timeText, arg_2_0.contextData.countTime .. "s   + " .. setColorStr(var_2_0 .. "s", "#3068E6FF"))
	else
		setText(arg_2_0.timeText, arg_2_0.contextData.countTime .. "s")
	end

	setText(arg_2_0.scoreText, arg_2_0.contextData.score .. "   + " .. setColorStr(var_2_0, "#3068E6FF"))
	arg_2_0.orderList:make(function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_0 == UIItemList.EventUpdate then
			local var_3_0 = arg_2_0.contextData.orderIDList[arg_3_1 + 1]
			local var_3_1 = arg_2_0:findTF("SnackImg", arg_3_2)

			setImageSprite(var_3_1, GetSpriteFromAtlas("ui/minigameui/newyearsnackui_atlas", "snack_" .. var_3_0))
		end
	end)
	arg_2_0.orderList:align(#arg_2_0.contextData.orderIDList)
	arg_2_0.selectedList:make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventUpdate then
			local var_4_0 = arg_2_0.contextData.selectedIDList[arg_4_1 + 1]
			local var_4_1 = arg_2_0:findTF("SnackImg", arg_4_2)

			setImageSprite(var_4_1, GetSpriteFromAtlas("ui/minigameui/newyearsnackui_atlas", "snack_" .. var_4_0))

			local var_4_2 = arg_2_0.contextData.orderIDList[arg_4_1 + 1]
			local var_4_3 = arg_2_0:findTF("ErrorImg", arg_4_2)
			local var_4_4 = arg_2_0:findTF("CorrectImg", arg_4_2)

			setActive(var_4_4, var_4_0 == var_4_2)
			setActive(var_4_3, var_4_0 ~= var_4_2)
		end
	end)
	arg_2_0.selectedList:align(#arg_2_0.contextData.selectedIDList)

	if arg_2_0.contextData.countTime == 0 then
		setActive(arg_2_0.continueBtn, false)
	end

	arg_2_0.contextData.countTime = arg_2_0.contextData.countTime + var_2_0
	arg_2_0.contextData.score = arg_2_0.contextData.score + var_2_0
end

return var_0_0
