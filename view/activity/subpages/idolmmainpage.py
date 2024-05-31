local var_0_0 = class("IDOLMMainPage", import(".TemplatePage.PreviewTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)

	arg_1_0.mountainBtn = arg_1_0.findTF("mountain", arg_1_0.btnList)

	onButton(arg_1_0, arg_1_0.mountainBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.IMAS_STAGE), SFX_PANEL)

return var_0_0
