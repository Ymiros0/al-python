local var_0_0 = class("SummaryPage4", import(".SummaryAnimationPage"))

def var_0_0.OnInit(arg_1_0):
	local var_1_0 = findTF(arg_1_0._go, "content")
	local var_1_1 = arg_1_0.summaryInfoVO.furnitures
	local var_1_2 = {}

	for iter_1_0 = 1, var_1_0.childCount:
		local var_1_3 = var_1_0.GetChild(iter_1_0 - 1)
		local var_1_4 = findTF(var_1_3, "info")
		local var_1_5 = tonumber(go(var_1_3).name)
		local var_1_6 = var_1_1[var_1_5]

		triggerToggle(var_1_4, var_1_6)

		if var_1_6:
			setText(var_1_4.Find("from/Text"), var_1_6.getConfig("gain_by"))
		else
			local var_1_7 = pg.furniture_data_template[var_1_5]

			setText(var_1_4.Find("from/Text"), var_1_7 and var_1_7.gain_by or "--：--.--")

		setText(var_1_4.Find("date/Text"), var_1_6 and var_1_6.getDate() or i18n("summary_page_un_rearch"))
		table.insert(var_1_2, var_1_4)

	setActive(arg_1_0._go, False)

def var_0_0.Clear(arg_2_0):
	return

return var_0_0
