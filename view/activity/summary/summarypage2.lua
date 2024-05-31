local var_0_0 = class("SummaryPage2", import(".SummaryAnimationPage"))

function var_0_0.OnInit(arg_1_0)
	local var_1_0 = findTF(arg_1_0._go, "name/Text")

	setText(var_1_0, arg_1_0.summaryInfoVO.firstProposeName)

	local var_1_1 = findTF(arg_1_0._go, "texts")

	arg_1_0.textTFs = {}

	for iter_1_0 = 1, var_1_1.childCount do
		local var_1_2 = var_1_1:GetChild(iter_1_0 - 1)
		local var_1_3 = go(var_1_2).name

		if var_1_3 ~= "label" then
			setText(var_1_2:Find("Text"), arg_1_0.summaryInfoVO[var_1_3])
		end

		table.insert(arg_1_0.textTFs, var_1_2)
	end

	local var_1_4 = findTF(arg_1_0._go, "name/date")

	setText(var_1_4, arg_1_0.summaryInfoVO.firstLadyTime)

	local var_1_5 = findTF(arg_1_0._go, "painting"):Find("mask/painting")
	local var_1_6 = Ship.New({
		configId = arg_1_0.summaryInfoVO.firstLadyId
	}):getPainting()

	setPaintingPrefabAsync(var_1_5, var_1_6, "chuanwu")
	setActive(arg_1_0._go, false)
end

function var_0_0.Clear(arg_2_0)
	return
end

return var_0_0
