local var_0_0 = class("HMSHardyTaskPage", import(".TemplatePage.PassChaptersTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.notGetBtn = arg_1_0.findTF("not_get_btn", arg_1_0.bg)
	arg_1_0.goHuntBtn = arg_1_0.findTF("gohunt_btn", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)
	onButton(arg_2_0, arg_2_0.goHuntBtn, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, pg.activity_const.HMS_Hunter_PT_ID.act_id), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.battleBtn, function()
		arg_2_0.emit(ActivityMediator.BATTLE_OPERA), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.notGetBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.TASK), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.buildBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.GETBOAT, {
			page = BuildShipScene.PAGE_BUILD,
			projectName = BuildShipScene.PROJECTS.LIGHT
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_7_0):
	local var_7_0 = arg_7_0.taskVO.getConfig("award_display")[1]
	local var_7_1 = {
		type = var_7_0[1],
		id = var_7_0[2],
		count = var_7_0[3]
	}

	updateDrop(arg_7_0.awardTF, var_7_1)
	onButton(arg_7_0, arg_7_0.awardTF, function()
		arg_7_0.emit(BaseUI.ON_DROP, var_7_1), SFX_PANEL)

	if arg_7_0.step:
		setText(arg_7_0.step, arg_7_0.taskIndex)

	local var_7_2 = arg_7_0.taskVO.getProgress()
	local var_7_3 = arg_7_0.taskVO.getConfig("target_num")

	setText(arg_7_0.desc, arg_7_0.taskVO.getConfig("desc"))
	setText(arg_7_0.progress, var_7_2 .. "/" .. var_7_3)
	setSlider(arg_7_0.slider, 0, var_7_3, var_7_2)

	local var_7_4 = arg_7_0.taskVO.getTaskStatus()

	setActive(arg_7_0.notGetBtn, var_7_4 == 0)
	setActive(arg_7_0.getBtn, var_7_4 == 1)
	setActive(arg_7_0.gotBtn, var_7_4 == 2)

return var_0_0
