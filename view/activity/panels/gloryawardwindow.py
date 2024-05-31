local var_0_0 = class("GloryAwardWindow", import(".PtAwardWindow"))

local function var_0_1(arg_1_0)
	local var_1_0 = arg_1_0.taskList
	local var_1_1 = getProxy(TaskProxy)

	arg_1_0.UIlist.make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate:
			local var_2_0 = var_1_0[arg_2_1 + 1]
			local var_2_1 = var_1_1.getTaskVO(var_2_0)

			setText(arg_2_2.Find("title/Text"), "PHASE " .. arg_2_1 + 1)
			setText(arg_2_2.Find("target/title"), var_2_1.getConfig("desc"))
			setText(arg_2_2.Find("target/Text"), "")

			local var_2_2 = var_2_1.getConfig("award_display")[1]
			local var_2_3 = {
				type = var_2_2[1],
				id = var_2_2[2],
				count = var_2_2[3]
			}

			updateDrop(arg_2_2.Find("award"), var_2_3)
			onButton(arg_1_0.binder, arg_2_2.Find("award"), function()
				arg_1_0.binder.emit(BaseUI.ON_DROP, var_2_3), SFX_PANEL)
			setActive(arg_2_2.Find("award/mask"), var_2_1.isReceive()))
	arg_1_0.UIlist.align(#var_1_0)

def var_0_0.Show(arg_4_0, arg_4_1):
	arg_4_0.taskList = arg_4_1.taskList
	arg_4_0.taskVO = arg_4_1.taskVO

	var_0_1(arg_4_0)

	arg_4_0.totalTxt.text = arg_4_0.taskVO.getProgress()
	arg_4_0.totalTitleTxt.text = i18n("pt_total_count", i18n("pass_times"))

	setActive(arg_4_0._tf, True)

return var_0_0
