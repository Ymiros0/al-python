local var_0_0 = class("SecondSummaryPage6", import(".SummaryAnimationPage"))

function var_0_0.OnInit(arg_1_0)
	local var_1_0 = arg_1_0.summaryInfoVO.skinId > 0

	setActive(arg_1_0._tf:Find("skin_panel"), var_1_0)
	setActive(arg_1_0._tf:Find("un_panel"), not var_1_0)

	if var_1_0 then
		local var_1_1 = pg.ship_skin_template[arg_1_0.summaryInfoVO.skinId].painting
		local var_1_2 = arg_1_0._tf:Find("skin_panel")

		setPaintingPrefabAsync(var_1_2:Find("paint_panel/painting"), var_1_1, "chuanwu")
		setText(var_1_2:Find("window_7/count/Text"), arg_1_0.summaryInfoVO.skinNum)
		setText(var_1_2:Find("window_7/ship/Text"), arg_1_0.summaryInfoVO.skinShipNum)
	end
end

function var_0_0.Show(arg_2_0, arg_2_1)
	var_0_0.super.Show(arg_2_0, arg_2_1, arg_2_0._tf:Find(arg_2_0.summaryInfoVO.skinId > 0 and "skin_panel" or "un_panel"))
end

return var_0_0
