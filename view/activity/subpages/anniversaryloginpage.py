local var_0_0 = class("AnniversaryLoginPage", import(".TemplatePage.LoginTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.item = arg_1_0.findTF("item", arg_1_0.bg)
	arg_1_0.items = arg_1_0.findTF("mask/items", arg_1_0.bg)
	arg_1_0.itemList = UIItemList.New(arg_1_0.items, arg_1_0.item)

def var_0_0.OnUpdateFlush(arg_2_0):
	var_0_0.super.OnUpdateFlush(arg_2_0)
	eachChild(arg_2_0.items, function(arg_3_0)
		local var_3_0 = arg_2_0.findTF("day/Text", arg_3_0)

		setText(var_3_0, arg_3_0.GetSiblingIndex() + 1))

return var_0_0
