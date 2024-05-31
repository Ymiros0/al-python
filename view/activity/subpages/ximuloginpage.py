local var_0_0 = class("XimuLoginPage", import(".TemplatePage.LoginTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.items2 = arg_1_0.findTF("items2", arg_1_0.bg)

def var_0_0.OnUpdateFlush(arg_2_0):
	var_0_0.super.OnUpdateFlush(arg_2_0)
	removeAllChildren(arg_2_0.items2)
	eachChild(arg_2_0.items, function(arg_3_0)
		local var_3_0 = arg_2_0.findTF("day/Text", arg_3_0)

		setText(var_3_0, setColorStr(getText(var_3_0), arg_3_0.GetSiblingIndex() < arg_2_0.nday and COLOR_GREY or COLOR_WHITE)))

	for iter_2_0 = arg_2_0.Day, 4, -1:
		local var_2_0 = arg_2_0.items.GetChild(iter_2_0 - 1)

		setParent(var_2_0, arg_2_0.items2, False)
		var_2_0.SetAsFirstSibling()

return var_0_0
