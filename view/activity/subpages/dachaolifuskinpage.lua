﻿local var_0_0 = class("DachaolifuSkinPage", import(".TemplatePage.SkinTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.step_txt = arg_1_0:findTF("step_text", arg_1_0.bg)
end

function var_0_0.OnUpdateFlush(arg_2_0)
	var_0_0.super.OnUpdateFlush(arg_2_0)
	setText(arg_2_0.step_txt, setColorStr(arg_2_0.nday, "#89FF59FF") .. "/" .. #arg_2_0.taskGroup)
end

return var_0_0
