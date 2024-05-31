local var_0_0 = class("SummaryPage1", import(".SummaryAnimationPage"))

function var_0_0.OnInit(arg_1_0)
	local var_1_0 = findTF(arg_1_0._go, "name")
	local var_1_1 = findTF(var_1_0, "Text")
	local var_1_2 = findTF(arg_1_0._go, "painting")
	local var_1_3 = findTF(var_1_2, "mask/painting")

	setText(var_1_1, arg_1_0.summaryInfoVO.name)

	local var_1_4 = findTF(arg_1_0._go, "time_line")
	local var_1_5 = {}

	for iter_1_0 = 1, var_1_4.childCount do
		local var_1_6 = var_1_4:GetChild(iter_1_0 - 1)
		local var_1_7 = var_1_6:Find("texts")

		for iter_1_1 = 1, var_1_7.childCount do
			local var_1_8 = var_1_7:GetChild(iter_1_1 - 1)
			local var_1_9 = go(var_1_8).name

			if var_1_9 == "guildName" then
				local var_1_10 = arg_1_0.summaryInfoVO.guildName
				local var_1_11 = not var_1_10 or var_1_10 == ""

				if not var_1_11 then
					setText(var_1_8:Find("text/Text"), "「" .. var_1_10 .. "」")
				end

				setActive(var_1_8:Find("image"), var_1_11)
				setActive(var_1_8:Find("text"), not var_1_11)
			elseif var_1_9 == "days" or var_1_9 == "furnitureCount" or var_1_9 == "furnitureWorth" then
				setText(var_1_8:Find("Text"), arg_1_0.summaryInfoVO[var_1_9])
			elseif var_1_9 ~= "label" then
				setText(var_1_8:Find("Text"), "「" .. string.gsub(arg_1_0.summaryInfoVO[var_1_9], "–", "-") .. "」")
			end
		end

		table.insert(var_1_5, var_1_6)
	end

	local var_1_12 = Ship.New({
		configId = arg_1_0.summaryInfoVO.flagShipId
	}):getPainting()

	setPaintingPrefabAsync(var_1_3, var_1_12, "chuanwu")
	setActive(arg_1_0._go, false)
end

return var_0_0
