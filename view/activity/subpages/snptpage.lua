﻿local var_0_0 = class("SNPTPage", import(".TemplatePage.PtTemplatePage"))

function var_0_0.OnUpdateFlush(arg_1_0)
	var_0_0.super.OnUpdateFlush(arg_1_0)

	local var_1_0, var_1_1, var_1_2 = arg_1_0.ptData:GetResProgress()

	setText(arg_1_0.progress, (var_1_2 >= 1 and setColorStr(var_1_0, "#0A79FFFF") or var_1_0) .. "/" .. var_1_1)
end

return var_0_0
