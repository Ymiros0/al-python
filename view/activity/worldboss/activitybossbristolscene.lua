﻿local var_0_0 = class("ActivityBossBristolScene", import(".ActivityBossSceneTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "ActivityBossBristolUI"
end

function var_0_0.init(arg_2_0)
	var_0_0.super.init(arg_2_0)
	setText(arg_2_0:findTF("ticket/Desc", arg_2_0.top), i18n("word_special_challenge_ticket"))
end

function var_0_0.UpdateDropItems(arg_3_0)
	for iter_3_0, iter_3_1 in ipairs(arg_3_0.contextData.DisplayItems or {}) do
		local var_3_0 = arg_3_0:findTF("milestone/item/IconTpl", arg_3_0.barList[iter_3_0])
		local var_3_1 = {
			type = arg_3_0.contextData.DisplayItems[5 - iter_3_0][1],
			id = arg_3_0.contextData.DisplayItems[5 - iter_3_0][2],
			count = arg_3_0.contextData.DisplayItems[5 - iter_3_0][3]
		}

		updateDrop(var_3_0, var_3_1)
		onButton(arg_3_0, var_3_0, function()
			arg_3_0:emit(var_0_0.ON_DROP, var_3_1)
		end, SFX_PANEL)
	end
end

return var_0_0
