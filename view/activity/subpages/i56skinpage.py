local var_0_0 = class("I56SkinPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	arg_1_0.uilist.make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate:
			local var_2_0 = arg_2_1 + 1
			local var_2_1 = arg_1_0.findTF("item", arg_2_2)
			local var_2_2 = arg_1_0.taskGroup[arg_1_0.nday][var_2_0]
			local var_2_3 = arg_1_0.taskProxy.getTaskById(var_2_2) or arg_1_0.taskProxy.getFinishTaskById(var_2_2)

			assert(var_2_3, "without this task by id. " .. var_2_2)

			local var_2_4 = var_2_3.getConfig("award_display")[1]
			local var_2_5 = {
				type = var_2_4[1],
				id = var_2_4[2],
				count = var_2_4[3]
			}

			updateDrop(var_2_1, var_2_5)
			onButton(arg_1_0, var_2_1, function()
				arg_1_0.emit(BaseUI.ON_DROP, var_2_5), SFX_PANEL)

			local var_2_6 = var_2_3.getProgress()
			local var_2_7 = var_2_3.getConfig("target_num")
			local var_2_8 = var_2_3.getConfig("desc")
			local var_2_9 = "(" .. var_2_6 .. "/" .. var_2_7 .. ")"

			setText(arg_1_0.findTF("description", arg_2_2), var_2_8 .. " " .. var_2_9)
			setSlider(arg_1_0.findTF("progress", arg_2_2), 0, var_2_7, var_2_6)

			local var_2_10 = arg_1_0.findTF("go_btn", arg_2_2)
			local var_2_11 = arg_1_0.findTF("get_btn", arg_2_2)
			local var_2_12 = arg_1_0.findTF("got_btn", arg_2_2)
			local var_2_13 = var_2_3.getTaskStatus()

			setActive(var_2_10, var_2_13 == 0)
			setActive(var_2_11, var_2_13 == 1)
			setActive(var_2_12, var_2_13 == 2)
			onButton(arg_1_0, var_2_10, function()
				arg_1_0.emit(ActivityMediator.ON_TASK_GO, var_2_3), SFX_PANEL)
			onButton(arg_1_0, var_2_11, function()
				arg_1_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_2_3), SFX_PANEL))

def var_0_0.OnUpdateFlush(arg_6_0):
	var_0_0.super.OnUpdateFlush(arg_6_0)
	setText(arg_6_0.dayTF, arg_6_0.nday .. " " .. #arg_6_0.taskGroup)
	eachChild(arg_6_0.items, function(arg_7_0)
		local var_7_0 = arg_6_0.findTF("get_btn", arg_7_0)
		local var_7_1 = arg_6_0.findTF("got_btn", arg_7_0)
		local var_7_2 = isActive(var_7_1)

		setButtonEnabled(var_7_1, False)
		setButtonEnabled(var_7_0, not var_7_2)

		if var_7_2:
			setActive(var_7_0, True))

return var_0_0