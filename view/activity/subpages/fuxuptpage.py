local var_0_0 = class("FuxuPtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	onButton(arg_1_0, arg_1_0.findTF("build_btn", arg_1_0.bg), function()
		arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
			projectName = BuildShipScene.PROJECTS.HEAVY
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_3_0):
	var_0_0.super.OnUpdateFlush(arg_3_0)

	local var_3_0, var_3_1, var_3_2 = arg_3_0.ptData.GetLevelProgress()
	local var_3_3, var_3_4, var_3_5 = arg_3_0.ptData.GetResProgress()

	setText(arg_3_0.step, var_3_0)
	setText(arg_3_0.progress, (var_3_5 >= 1 and setColorStr(var_3_3, "#df9e38") or var_3_3) .. "/" .. var_3_4)

	local var_3_6
	local var_3_7

	if arg_3_0.activity.getConfig("config_client") != "":
		var_3_6 = arg_3_0.activity.getConfig("config_client").linkActID

		if var_3_6:
			var_3_7 = getProxy(ActivityProxy).getActivityById(var_3_6)

	if var_3_6 and not var_3_7 or var_3_7 and var_3_7.isEnd():
		setActive(arg_3_0.battleBtn, False)
		setActive(arg_3_0.findTF("build_btn", arg_3_0.bg), False)

return var_0_0
