local var_0_0 = class("EskiPtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.progresses = arg_1_0.findTF("progresses", arg_1_0.bg)
	arg_1_0.progress_r = arg_1_0.findTF("progress_r", arg_1_0.progresses)
	arg_1_0.progress_l = arg_1_0.findTF("progress_l", arg_1_0.progresses)
	arg_1_0.buildBtn = arg_1_0.findTF("build_btn", arg_1_0.bg)

def var_0_0.OnUpdateFlush(arg_2_0):
	local var_2_0 = arg_2_0.ptData.getTargetLevel()
	local var_2_1 = arg_2_0.activity.getConfig("config_client").story

	if checkExist(var_2_1, {
		var_2_0
	}, {
		1
	}):
		pg.NewStoryMgr.GetInstance().Play(var_2_1[var_2_0][1])

	local var_2_2, var_2_3, var_2_4 = arg_2_0.ptData.GetLevelProgress()
	local var_2_5, var_2_6, var_2_7 = arg_2_0.ptData.GetResProgress()

	setText(arg_2_0.step, var_2_2 .. "/" .. var_2_3)

	local var_2_8 = var_2_7 >= 1 and setColorStr(var_2_5, COLOR_GREEN) or var_2_5

	setText(arg_2_0.progress_r, var_2_8 .. "/" .. var_2_6)
	setSlider(arg_2_0.slider, 0, 1, var_2_7)

	local var_2_9 = arg_2_0.ptData.CanGetAward()
	local var_2_10 = arg_2_0.ptData.CanGetNextAward()
	local var_2_11 = arg_2_0.ptData.CanGetMorePt()

	setActive(arg_2_0.battleBtn, var_2_11 and not var_2_9 and var_2_10)
	setActive(arg_2_0.getBtn, var_2_9)
	setActive(arg_2_0.gotBtn, not var_2_10)

	local var_2_12 = arg_2_0.ptData.GetAward()

	updateDrop(arg_2_0.awardTF, var_2_12)
	onButton(arg_2_0, arg_2_0.awardTF, function()
		arg_2_0.emit(BaseUI.ON_DROP, var_2_12), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.buildBtn, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
			projectName = BuildShipScene.PROJECTS.LIGHT
		}), SFX_PANEL)

return var_0_0
