﻿local var_0_0 = class("SecondSummaryPage2", import(".SummaryAnimationPage"))

function var_0_0.OnInit(arg_1_0)
	local var_1_0 = Ship.New({
		configId = arg_1_0.summaryInfoVO.flagShipId
	}):getPainting()

	setPaintingPrefabAsync(arg_1_0._tf:Find("paint_panel/painting"), var_1_0, "chuanwu")
	setText(arg_1_0._tf:Find("window_1/name"), arg_1_0.summaryInfoVO.name)
	setText(arg_1_0._tf:Find("window_1/time/Text"), "「" .. arg_1_0.summaryInfoVO.registerTime .. "」")
	setText(arg_1_0._tf:Find("window_1/server/Text"), "「" .. arg_1_0.summaryInfoVO.serverName .. "」")
	setText(arg_1_0._tf:Find("window_1/day/Text"), arg_1_0.summaryInfoVO.days)

	local var_1_1 = arg_1_0.summaryInfoVO:hasGuild()

	setActive(arg_1_0._tf:Find("window_2/has_guild"), var_1_1)
	setActive(arg_1_0._tf:Find("window_2/without"), not var_1_1)

	local var_1_2 = arg_1_0._tf:Find("window_2/" .. (var_1_1 and "has_guild" or "without"))

	if var_1_1 then
		setText(var_1_2:Find("guild_name/Text"), "「" .. arg_1_0.summaryInfoVO.guildName .. "」")
	end

	setText(var_1_2:Find("chapter_name/Text"), "「" .. arg_1_0.summaryInfoVO.chapterName .. "」")

	if arg_1_0.summaryInfoVO.worldProgressTask > 0 then
		local var_1_3 = pg.world_task_data[arg_1_0.summaryInfoVO.worldProgressTask].name

		setText(var_1_2:Find("world_name/Text"), "「" .. var_1_3 .. "」")
	else
		setText(var_1_2:Find("world_name/Text"), i18n("five_shujuhuigu"))
	end

	setText(arg_1_0._tf:Find("window_3/count/Text"), arg_1_0.summaryInfoVO.furnitureCount)
	setText(arg_1_0._tf:Find("window_3/coin/Text"), arg_1_0.summaryInfoVO.furnitureWorth)
	setText(arg_1_0._tf:Find("window_4/collection/Text"), arg_1_0.summaryInfoVO.collectionNum)
	setText(arg_1_0._tf:Find("window_4/power/Text"), arg_1_0.summaryInfoVO.powerRaw)
	setText(arg_1_0._tf:Find("window_4/ship/Text"), arg_1_0.summaryInfoVO.totalShipNum)
	setText(arg_1_0._tf:Find("window_4/top_ship/Text"), arg_1_0.summaryInfoVO.topShipNum)
	setText(arg_1_0._tf:Find("window_4/best_ship/Text"), arg_1_0.summaryInfoVO.bestShipNum)
end

return var_0_0
