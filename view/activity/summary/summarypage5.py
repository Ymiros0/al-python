local var_0_0 = class("SummaryPage5", import(".SummaryAnimationPage"))

def var_0_0.OnInit(arg_1_0):
	local var_1_0 = findTF(arg_1_0._go, "share")

	onButton(arg_1_0, var_1_0, function()
		if arg_1_0.inAnim():
			return

		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeSummary), SFX_PANEL)

	local var_1_1 = findTF(arg_1_0._go, "frame/name")
	local var_1_2 = findTF(var_1_1, "Text")

	setText(var_1_2, arg_1_0.summaryInfoVO.name)

	local var_1_3 = findTF(arg_1_0._go, "frame/texts")

	arg_1_0.textTFs = {}

	for iter_1_0 = 1, var_1_3.childCount:
		local var_1_4 = var_1_3.GetChild(iter_1_0 - 1)
		local var_1_5 = go(var_1_4).name

		if var_1_5 == "list" or var_1_5 == "list1":
			for iter_1_1 = 1, var_1_4.childCount:
				local var_1_6 = var_1_4.GetChild(iter_1_1 - 1)
				local var_1_7 = go(var_1_6).name

				setActive(var_1_6, (var_1_7 != "guildName" or not not arg_1_0.summaryInfoVO.hasGuild()) and (var_1_7 != "medalCount" or not not arg_1_0.summaryInfoVO.hasMedal()))

				if go(var_1_6).name != "label":
					if var_1_7 == "guildName" or var_1_7 == "chapterName":
						setText(var_1_6.Find("image/Text"), "「" .. string.gsub(arg_1_0.summaryInfoVO[go(var_1_6).name] .. "」", "–", "-"))
					else
						setText(var_1_6.Find("image/Text"), arg_1_0.summaryInfoVO[go(var_1_6).name])
		elif var_1_5 != "label":
			setText(var_1_4.Find("Text"), arg_1_0.summaryInfoVO[var_1_5])

		table.insert(arg_1_0.textTFs, var_1_4)

	setActive(arg_1_0._go, False)

def var_0_0.Clear(arg_3_0):
	return

return var_0_0
