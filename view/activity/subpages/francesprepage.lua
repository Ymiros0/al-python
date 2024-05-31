﻿local var_0_0 = class("FranceSpRePage", import("...base.BaseActivityPage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.slider = arg_1_0:findTF("slider", arg_1_0.bg):GetComponent(typeof(Slider))
	arg_1_0.step = arg_1_0:findTF("step", arg_1_0.bg):GetComponent(typeof(Text))
	arg_1_0.progress = arg_1_0:findTF("progress", arg_1_0.bg):GetComponent(typeof(Text))
	arg_1_0.desc = arg_1_0:findTF("desc", arg_1_0.bg):GetComponent(typeof(Text))
	arg_1_0.awardTF = arg_1_0:findTF("award", arg_1_0.bg)
	arg_1_0.battleBtn = arg_1_0:findTF("battle_btn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0:findTF("get_btn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0:findTF("got_btn", arg_1_0.bg)
	arg_1_0.buildBtn = arg_1_0:findTF("build_btn", arg_1_0.bg)
end

function var_0_0.OnDataSetting(arg_2_0)
	local var_2_0 = getProxy(TaskProxy)

	arg_2_0.taskList = arg_2_0.taskList or arg_2_0.activity:getConfig("config_data")

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.taskList) do
		arg_2_0.taskIndex = iter_2_0
		arg_2_0.taskVO = var_2_0:getTaskVO(iter_2_1)

		if not arg_2_0.taskVO:isReceive() then
			break
		end
	end

	assert(arg_2_0.taskVO, "without any taskVO!!!")
end

function var_0_0.OnFirstFlush(arg_3_0)
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0:emit(ActivityMediator.BATTLE_OPERA)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		arg_3_0:emit(ActivityMediator.ON_TASK_SUBMIT, arg_3_0.taskVO)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.buildBtn, function()
		arg_3_0:emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
			projectName = BuildShipScene.PROJECTS.LIGHT
		})
	end, SFX_PANEL)
end

function var_0_0.OnUpdateFlush(arg_7_0)
	local var_7_0 = arg_7_0.taskVO:getConfig("award_display")[1]
	local var_7_1 = {
		type = var_7_0[1],
		id = var_7_0[2],
		count = var_7_0[3]
	}

	updateDrop(arg_7_0.awardTF, var_7_1)
	onButton(arg_7_0, arg_7_0.awardTF, function()
		arg_7_0:emit(BaseUI.ON_DROP, var_7_1)
	end, SFX_PANEL)

	if arg_7_0.step then
		setText(arg_7_0.step, arg_7_0.taskIndex .. "/" .. #arg_7_0.taskList)
	end

	local var_7_2 = arg_7_0.taskVO:getProgress()
	local var_7_3 = arg_7_0.taskVO:getConfig("target_num")

	setText(arg_7_0.desc, arg_7_0.taskVO:getConfig("desc"))
	setText(arg_7_0.progress, var_7_2 .. "/" .. var_7_3)
	setSlider(arg_7_0.slider, 0, var_7_3, var_7_2)

	local var_7_4 = arg_7_0.taskVO:getTaskStatus()

	setActive(arg_7_0.battleBtn, var_7_4 == 0)
	setActive(arg_7_0.getBtn, var_7_4 == 1)
	setActive(arg_7_0.gotBtn, var_7_4 == 2)
end

function var_0_0.OnDestroy(arg_9_0)
	return
end

return var_0_0
