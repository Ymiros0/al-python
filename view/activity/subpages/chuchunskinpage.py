local var_0_0 = class("ChuChunSkinPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	var_0_0.super.OnUpdateFlush(arg_1_0)
	setText(arg_1_0.dayTF, setColorStr(arg_1_0.nday, COLOR_GREEN) .. "/" .. #arg_1_0.taskGroup)

return var_0_0
