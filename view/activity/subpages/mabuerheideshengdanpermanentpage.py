local var_0_0 = class("MabuerheideshengdanPermanentPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	onButton(arg_1_0, arg_1_0.battleBtn, function()
		arg_1_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA), SFX_PANEL)

return var_0_0
