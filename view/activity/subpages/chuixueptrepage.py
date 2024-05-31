local var_0_0 = class("ChuixuePTRePage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)

	var_0_0.scrolltext = arg_1_0.findTF("name", arg_1_0.awardTF)

	onButton(arg_1_0, arg_1_0.battleBtn, function()
		arg_1_0.emit(ActivityMediator.GO_SHOPS_LAYER_STEEET, {
			warp = NewShopsScene.TYPE_SHOP_STREET
		}))

def var_0_0.OnUpdateFlush(arg_3_0):
	var_0_0.super.OnUpdateFlush(arg_3_0)
	arg_3_0.SetAwardName()

	local var_3_0, var_3_1, var_3_2 = arg_3_0.ptData.GetResProgress()

	setText(arg_3_0.progress, (var_3_2 >= 1 and setColorStr(var_3_0, "#A2A2A2FF") or var_3_0) .. "/" .. var_3_1)

def var_0_0.SetAwardName(arg_4_0):
	local var_4_0 = arg_4_0.ptData.GetAward()

	if Item.getConfigData(var_4_0.id):
		changeToScrollText(var_0_0.scrolltext, var_4_0.getName())
	else
		setActive(arg_4_0.findTF("name", arg_4_0.awardTF), False)

return var_0_0
