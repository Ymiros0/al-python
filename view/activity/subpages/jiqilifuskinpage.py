local var_0_0 = class("JiqilifuSkinPage", import(".DachaolifuSkinPage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.step_txt = arg_1_0.findTF("step_text", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	arg_2_0.uilist.make(function(arg_3_0, arg_3_1, arg_3_2)
		if arg_3_0 == UIItemList.EventUpdate:
			local var_3_0 = arg_3_1 + 1
			local var_3_1 = arg_2_0.findTF("item", arg_3_2)
			local var_3_2 = arg_2_0.taskGroup[arg_2_0.nday][var_3_0]
			local var_3_3 = arg_2_0.taskProxy.getTaskById(var_3_2) or arg_2_0.taskProxy.getFinishTaskById(var_3_2)

			assert(var_3_3, "without this task by id. " .. var_3_2)

			local var_3_4 = var_3_3.getConfig("award_display")[1]
			local var_3_5 = {
				type = var_3_4[1],
				id = var_3_4[2],
				count = var_3_4[3]
			}

			updateDrop(var_3_1, var_3_5)
			onButton(arg_2_0, var_3_1, function()
				arg_2_0.emit(BaseUI.ON_DROP, var_3_5), SFX_PANEL)

			local var_3_6 = var_3_3.getProgress()
			local var_3_7 = var_3_3.getConfig("target_num")

			setText(arg_2_0.findTF("description", arg_3_2), var_3_3.getConfig("desc"))
			setText(arg_2_0.findTF("progressText", arg_3_2), var_3_6 .. "/" .. var_3_7)
			setSlider(arg_2_0.findTF("progress", arg_3_2), 0, var_3_7, var_3_6)

			local var_3_8 = arg_2_0.findTF("go_btn", arg_3_2)
			local var_3_9 = arg_2_0.findTF("get_btn", arg_3_2)
			local var_3_10 = arg_2_0.findTF("got_btn", arg_3_2)
			local var_3_11 = var_3_3.getTaskStatus()

			setActive(var_3_8, var_3_11 == 0)
			setActive(var_3_9, var_3_11 == 1)
			setActive(var_3_10, var_3_11 == 2)
			onButton(arg_2_0, var_3_8, function()
				arg_2_0.emit(ActivityMediator.ON_TASK_GO, var_3_3), SFX_PANEL)
			onButton(arg_2_0, var_3_9, function()
				arg_2_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_3_3), SFX_PANEL))

def var_0_0.OnUpdateFlush(arg_7_0):
	var_0_0.super.OnUpdateFlush(arg_7_0)
	setText(arg_7_0.step_txt, setColorStr(arg_7_0.nday, "#6CF7C1FF") .. "/" .. #arg_7_0.taskGroup)

return var_0_0
