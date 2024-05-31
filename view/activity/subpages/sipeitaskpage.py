local var_0_0 = class("SipeiTaskPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.slider = arg_1_0.findTF("slider", arg_1_0.bg).GetComponent(typeof(Slider))
	arg_1_0.step = arg_1_0.findTF("step", arg_1_0.bg).GetComponent(typeof(Text))
	arg_1_0.progress = arg_1_0.findTF("progress", arg_1_0.bg).GetComponent(typeof(Text))
	arg_1_0.desc = arg_1_0.findTF("desc", arg_1_0.bg).GetComponent(typeof(Text))
	arg_1_0.awardTF = arg_1_0.findTF("award", arg_1_0.bg)
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("got_btn", arg_1_0.bg)

def var_0_0.OnDataSetting(arg_2_0):
	local var_2_0 = getProxy(TaskProxy)

	arg_2_0.taskList = arg_2_0.taskList or arg_2_0.activity.getConfig("config_data")

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.taskList):
		arg_2_0.taskIndex = iter_2_0
		arg_2_0.taskVO = var_2_0.getTaskVO(iter_2_1)

		if not arg_2_0.taskVO.isReceive():
			break

	assert(arg_2_0.taskVO, "without any taskVO!!!")

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0.emit(ActivityMediator.BATTLE_OPERA), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		arg_3_0.emit(ActivityMediator.ON_TASK_SUBMIT, arg_3_0.taskVO), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_6_0):
	local var_6_0 = arg_6_0.taskVO.getConfig("award_display")[1]
	local var_6_1 = {
		type = var_6_0[1],
		id = var_6_0[2],
		count = var_6_0[3]
	}

	updateDrop(arg_6_0.awardTF, var_6_1)
	onButton(arg_6_0, arg_6_0.awardTF, function()
		arg_6_0.emit(BaseUI.ON_DROP, var_6_1), SFX_PANEL)

	if arg_6_0.step:
		setText(arg_6_0.step, arg_6_0.taskIndex .. "/" .. #arg_6_0.taskList)

	local var_6_2 = arg_6_0.taskVO.getProgress()
	local var_6_3 = arg_6_0.taskVO.getConfig("target_num")

	setText(arg_6_0.desc, arg_6_0.taskVO.getConfig("desc"))
	setText(arg_6_0.progress, var_6_2 .. "/" .. var_6_3)
	setSlider(arg_6_0.slider, 0, var_6_3, var_6_2)

	local var_6_4 = arg_6_0.taskVO.getTaskStatus()

	setActive(arg_6_0.battleBtn, var_6_4 == 0)
	setActive(arg_6_0.getBtn, var_6_4 == 1)
	setActive(arg_6_0.gotBtn, var_6_4 == 2)

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
