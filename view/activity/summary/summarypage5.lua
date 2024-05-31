local var_0_0 = class("SummaryPage5", import(".SummaryAnimationPage"))

function var_0_0.OnInit(arg_1_0)
	local var_1_0 = findTF(arg_1_0._go, "share")

	onButton(arg_1_0, var_1_0, function()
		if arg_1_0:inAnim() then
			return
		end

		pg.ShareMgr.GetInstance():Share(pg.ShareMgr.TypeSummary)
	end, SFX_PANEL)

	local var_1_1 = findTF(arg_1_0._go, "frame/name")
	local var_1_2 = findTF(var_1_1, "Text")

	setText(var_1_2, arg_1_0.summaryInfoVO.name)

	local var_1_3 = findTF(arg_1_0._go, "frame/texts")

	arg_1_0.textTFs = {}

	for iter_1_0 = 1, var_1_3.childCount do
		local var_1_4 = var_1_3:GetChild(iter_1_0 - 1)
		local var_1_5 = go(var_1_4).name

		if var_1_5 == "list" or var_1_5 == "list1" then
			for iter_1_1 = 1, var_1_4.childCount do
				local var_1_6 = var_1_4:GetChild(iter_1_1 - 1)
				local var_1_7 = go(var_1_6).name

				setActive(var_1_6, (var_1_7 ~= "guildName" or not not arg_1_0.summaryInfoVO:hasGuild()) and (var_1_7 ~= "medalCount" or not not arg_1_0.summaryInfoVO:hasMedal()))

				if go(var_1_6).name ~= "label" then
					if var_1_7 == "guildName" or var_1_7 == "chapterName" then
						setText(var_1_6:Find("image/Text"), "「" .. string.gsub(arg_1_0.summaryInfoVO[go(var_1_6).name] .. "」", "–", "-"))
					else
						setText(var_1_6:Find("image/Text"), arg_1_0.summaryInfoVO[go(var_1_6).name])
					end
				end
			end
		elseif var_1_5 ~= "label" then
			setText(var_1_4:Find("Text"), arg_1_0.summaryInfoVO[var_1_5])
		end

		table.insert(arg_1_0.textTFs, var_1_4)
	end

	setActive(arg_1_0._go, false)
end

function var_0_0.Clear(arg_3_0)
	return
end

return var_0_0
