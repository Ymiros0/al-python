﻿local var_0_0 = class("RyzaMainPage", import(".TemplatePage.PreviewTemplatePage"))

function var_0_0.OnFirstFlush(arg_1_0)
	var_0_0.super.OnFirstFlush(arg_1_0)

	arg_1_0.mountainBtn = arg_1_0:findTF("mountain", arg_1_0.btnList)

	onButton(arg_1_0, arg_1_0.mountainBtn, function()
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.RYZA_URBAN_AREA)
	end, SFX_PANEL)
end

return var_0_0
