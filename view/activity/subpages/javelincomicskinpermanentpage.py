local var_0_0 = class("JavelinComicSkinPermanentPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	var_0_0.super.OnUpdateFlush(arg_1_0)

	if arg_1_0.nday < #arg_1_0.taskGroup:
		setText(arg_1_0.dayTF, "<color=#E75198><size=48>" .. arg_1_0.nday .. "</size></color><color=#00B8FF><size=28>     " .. #arg_1_0.taskGroup .. "</size></color>")
	else
		setText(arg_1_0.dayTF, "<color=#00FF00><size=48>" .. arg_1_0.nday .. "</size></color><color=#00B8FF><size=28>     " .. #arg_1_0.taskGroup .. "</size></color>")

return var_0_0
