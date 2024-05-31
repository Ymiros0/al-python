local var_0_0 = class("SpTemplatePage", import(".PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.buildBtn = arg_1_0.findTF("build_btn", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)

	local var_2_0 = arg_2_0.activity.getConfig("config_client").linkPoolActID

	if not var_2_0:
		pg.TipsMgr.GetInstance().ShowTips("未配置linkPoolActID！！！")
	else
		local var_2_1 = getProxy(ActivityProxy).getActivityById(var_2_0)

		if var_2_1 and not var_2_1.isEnd():
			setActive(arg_2_0.buildBtn, True)

			local var_2_2 = pg.activity_template[var_2_0].config_client.id
			local var_2_3 = var_2_2 and var_2_2 or BuildShipScene.PROJECTS.SPECIAL
			local var_2_4 = {
				BuildShipScene.PROJECTS.SPECIAL,
				BuildShipScene.PROJECTS.LIGHT,
				BuildShipScene.PROJECTS.HEAVY,
				BuildShipScene.PROJECTS.ACTIVITY
			}

			onButton(arg_2_0, arg_2_0.buildBtn, function()
				arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
					page = BuildShipScene.PAGE_BUILD,
					projectName = var_2_4[var_2_3]
				}), SFX_PANEL)
		else
			setActive(arg_2_0.buildBtn, False)

return var_0_0
