local var_0_0 = class("JamaicaSkinPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.slider = arg_1_0.findTF("slider", arg_1_0.bg)
	arg_1_0.step = arg_1_0.findTF("step", arg_1_0.bg)
	arg_1_0.progress = arg_1_0.findTF("progress", arg_1_0.bg)
	arg_1_0.awardTF = arg_1_0.findTF("award", arg_1_0.bg)
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("got_btn", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	local var_2_0 = arg_2_0.activity.getConfig("config_data")

	arg_2_0.taskIDList = _.flatten(var_2_0)
	arg_2_0.dropList = {}
	arg_2_0.descs = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.taskIDList):
		local var_2_1 = pg.task_data_template[iter_2_1].award_display[1]

		table.insert(arg_2_0.dropList, Clone(var_2_1))

		local var_2_2 = pg.task_data_template[iter_2_1].desc

		table.insert(arg_2_0.descs, var_2_2)

	return updateActivityTaskStatus(arg_2_0.activity)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		arg_3_0.emit(ActivityMediator.ON_TASK_SUBMIT, arg_3_0.curTaskVO), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_6_0):
	local var_6_0, var_6_1 = getActivityTask(arg_6_0.activity)

	arg_6_0.curTaskVO = var_6_1

	local var_6_2 = var_6_1.getConfig("award_display")[1]
	local var_6_3 = {
		type = var_6_2[1],
		id = var_6_2[2],
		count = var_6_2[3]
	}

	updateDrop(arg_6_0.awardTF, var_6_3)
	onButton(arg_6_0, arg_6_0.awardTF, function()
		arg_6_0.emit(BaseUI.ON_DROP, var_6_3), SFX_PANEL)

	local var_6_4 = var_6_1.getProgress()
	local var_6_5 = var_6_1.getConfig("target_num")

	setText(arg_6_0.progress, (var_6_5 <= var_6_4 and setColorStr(var_6_4, COLOR_GREEN) or var_6_4) .. "/" .. var_6_5)
	setSlider(arg_6_0.slider, 0, var_6_5, var_6_4)

	local var_6_6 = table.indexof(arg_6_0.taskIDList, var_6_0, 1)

	setText(arg_6_0.step, var_6_6 .. "/" .. #arg_6_0.taskIDList)

	local var_6_7 = var_6_1.getTaskStatus()

	setActive(arg_6_0.battleBtn, var_6_7 == 0)
	setActive(arg_6_0.getBtn, var_6_7 == 1)
	setActive(arg_6_0.gotBtn, var_6_7 == 2)

	if var_6_7 == 2:
		arg_6_0.finishedIndex = var_6_6
	else
		arg_6_0.finishedIndex = var_6_6 - 1

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
