﻿local var_0_0 = class("ActivityBossSurugaScene", import(".ActivityBossSceneTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "ActivityBossUI"
end

function var_0_0.preload(arg_2_0, arg_2_1)
	local var_2_0 = PoolMgr.GetInstance()

	var_2_0:GetPrefab("ui/cysx_fk", "cysx_fk", true, function(arg_3_0)
		var_2_0:ReturnPrefab("ui/cysx_fk", "cysx_fk", arg_3_0)
		arg_2_1()
	end)
end

function var_0_0.init(arg_4_0)
	var_0_0.super.init(arg_4_0)
	setText(arg_4_0.rankTF:Find("title/Text"), i18n("word_billboard"))

	arg_4_0.loader = AutoLoader.New()
end

function var_0_0.didEnter(arg_5_0)
	var_0_0.super.didEnter(arg_5_0)
	arg_5_0.loader:GetPrefab("ui/cysx_fk", "cysx_fk", function(arg_6_0)
		setParent(arg_6_0, arg_5_0.left)
		setAnchoredPosition(arg_6_0, Vector2(69, 295))
		arg_6_0.transform:SetAsFirstSibling()
	end)
end

function var_0_0.UpdateRank(arg_7_0, arg_7_1)
	arg_7_1 = arg_7_1 or {}

	for iter_7_0 = 1, #arg_7_0.rankList do
		local var_7_0 = arg_7_0.rankList[iter_7_0]

		setActive(var_7_0, iter_7_0 <= #arg_7_1)

		if iter_7_0 <= #arg_7_1 then
			local var_7_1 = var_7_0:Find("name/Text")

			setText(var_7_1, tostring(arg_7_1[iter_7_0].name))
			setText(var_7_0:Find("num/Text"), "NO." .. iter_7_0)
		end
	end
end

function var_0_0.UpdateDropItems(arg_8_0)
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.contextData.DisplayItems or {}) do
		local var_8_0 = arg_8_0:findTF("milestone/item", arg_8_0.barList[iter_8_0])
		local var_8_1 = {
			type = arg_8_0.contextData.DisplayItems[5 - iter_8_0][1],
			id = arg_8_0.contextData.DisplayItems[5 - iter_8_0][2],
			count = arg_8_0.contextData.DisplayItems[5 - iter_8_0][3]
		}

		updateDrop(var_8_0, var_8_1)
		onButton(arg_8_0, var_8_0, function()
			arg_8_0:emit(var_0_0.ON_DROP, var_8_1)
		end, SFX_PANEL)
	end
end

function var_0_0.willExit(arg_10_0)
	var_0_0.super.willExit(arg_10_0)
	arg_10_0.loader:Clear()
end

return var_0_0
