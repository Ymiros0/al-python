local var_0_0 = class("SanDiegoPtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	onButton(arg_1_0, arg_1_0.battleBtn, function()
		arg_1_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA), SFX_PANEL)
	onButton(arg_1_0, arg_1_0.findTF("help_btn", arg_1_0.bg), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("littleSanDiego_npc")
		}), SFX_PANEL)

return var_0_0
