local var_0_0 = class("LevelOpenActPage", import("view.base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	local var_1_0 = arg_1_0._tf.Find("AD/task_list/content")

	arg_1_0.uiList = UIItemList.New(var_1_0, var_1_0.Find("tpl"))

	arg_1_0.uiList.make(function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_0 == UIItemList.EventUpdate:
			arg_1_0.UpdateTask(arg_2_2, arg_1_0.taskVOs[arg_2_1 + 1]))

def var_0_0.OnDataSetting(arg_3_0):
	local var_3_0 = arg_3_0.activity
	local var_3_1 = var_3_0.getConfig("config_data")[1][1]

	if not getProxy(TaskProxy).getTaskVO(var_3_1):
		pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = var_3_0.id
		})

		return True
	else
		return False

def var_0_0.OnUpdateFlush(arg_4_0):
	local var_4_0 = getProxy(TaskProxy)

	arg_4_0.taskVOs = underscore.map(arg_4_0.activity.getConfig("config_data")[1], function(arg_5_0)
		return var_4_0.getTaskVO(arg_5_0))

	table.sort(arg_4_0.taskVOs, CompareFuncs({
		function(arg_6_0)
			if arg_6_0.isReceive():
				return 2
			elif arg_6_0.isFinish():
				return 0
			else
				return 1
	}))
	arg_4_0.uiList.align(#arg_4_0.taskVOs)

def var_0_0.UpdateTask(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = arg_7_2.getTaskStatus()

	setImageAlpha(arg_7_1.Find("bg"), var_7_0 == 2 and 0.5 or 1)
	eachChild(arg_7_1.Find("status"), function(arg_8_0)
		setActive(arg_8_0, arg_8_0.GetSiblingIndex() == var_7_0))

	local var_7_1 = arg_7_1.Find("canvas")

	setCanvasGroupAlpha(var_7_1, var_7_0 == 2 and 0.2 or 1)

	local var_7_2 = arg_7_2.getConfig("desc")

	if var_7_0 == 2:
		setSlider(var_7_1.Find("progress"), 0, 1, 1)
	else
		local var_7_3 = arg_7_2.getProgress()
		local var_7_4 = arg_7_2.getConfig("target_num")

		var_7_2 = var_7_2 .. " " .. setColorStr("(" .. var_7_3 .. "/" .. var_7_4 .. ")", COLOR_RED)

		setSlider(var_7_1.Find("progress"), 0, var_7_4, var_7_3)

	setText(arg_7_1.Find("canvas/Text"), var_7_2)

	local var_7_5 = underscore.rest(arg_7_2.getConfig("award_display"), 1)

	while #var_7_5 > 3:
		table.remove(var_7_5)

	local var_7_6 = UIItemList.New(var_7_1.Find("items"), var_7_1.Find("items/IconTpl"))

	var_7_6.make(function(arg_9_0, arg_9_1, arg_9_2)
		arg_9_1 = arg_9_1 + 1

		if arg_9_0 == UIItemList.EventUpdate:
			local var_9_0 = var_7_5[arg_9_1]
			local var_9_1 = {
				type = var_9_0[1],
				id = var_9_0[2],
				count = var_9_0[3]
			}

			updateDrop(arg_9_2, var_9_1)
			onButton(arg_7_0, arg_9_2, function()
				arg_7_0.emit(BaseUI.ON_DROP, var_9_1), SFX_PANEL))
	var_7_6.align(#var_7_5)

	if var_7_0 == 2:
		removeOnButton(arg_7_1)
	elif var_7_0 == 1:
		onButton(arg_7_0, arg_7_1, function()
			arg_7_0.emit(ActivityMediator.ON_TASK_SUBMIT, arg_7_2), SFX_PANEL)
	elif var_7_0 == 0:
		onButton(arg_7_0, arg_7_1, function()
			arg_7_0.emit(ActivityMediator.ON_TASK_GO, arg_7_2), SFX_PANEL)
	else
		assert(False, "task status error." .. arg_7_2.id)

return var_0_0
