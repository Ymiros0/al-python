﻿local var_0_0 = class("BulvxieerSPSkinPage", import(".TemplatePage.SkinTemplatePage"))

function var_0_0.OnUpdateFlush(arg_1_0)
	var_0_0.super.OnUpdateFlush(arg_1_0)
	setText(arg_1_0.dayTF, setColorStr(arg_1_0.nday, "#FFCBAE") .. "/" .. #arg_1_0.taskGroup)
end

function var_0_0.GetProgressColor(arg_2_0)
	return "#FFCBAE"
end

return var_0_0