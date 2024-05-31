local var_0_0 = class("GuildOfficeLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "GuildEmptyUI"

def var_0_0.setPlayer(arg_2_0, arg_2_1):
	arg_2_0.playerVO = arg_2_1

def var_0_0.SetGuild(arg_3_0, arg_3_1):
	arg_3_0.guild = arg_3_1
	arg_3_0.isAdmin = GuildMember.IsAdministrator(arg_3_1.getSelfDuty())

	if arg_3_0.taskPage and arg_3_0.taskPage.GetLoaded():
		arg_3_0.taskPage.OnUpdateGuild(arg_3_0.guild, arg_3_0.isAdmin)

def var_0_0.init(arg_4_0):
	arg_4_0.taskPage = GuildOfficeTaskPage.New(arg_4_0._tf, arg_4_0.event)
	arg_4_0.helpBtn = arg_4_0.findTF("frame/help")

def var_0_0.didEnter(arg_5_0):
	local var_5_0 = arg_5_0.guild.GetOfficePainting()

	pg.GuildPaintingMgr.GetInstance().Update(var_5_0, Vector3(-737, -171, 0))
	arg_5_0.taskPage.ExecuteAction("Update", arg_5_0.guild, arg_5_0.isAdmin)
	onButton(arg_5_0, arg_5_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.guild_office_tip.tip
		}), SFX_PANEL)

def var_0_0.UpdateContribution(arg_7_0):
	if arg_7_0.taskPage and arg_7_0.taskPage.GetLoaded():
		arg_7_0.taskPage.OnUpdateContribution()

def var_0_0.UpdateSupplyPanel(arg_8_0):
	if arg_8_0.taskPage and arg_8_0.taskPage.GetLoaded():
		arg_8_0.taskPage.OnUpdateSupplyPanel()

def var_0_0.UpdateTask(arg_9_0, arg_9_1):
	if arg_9_0.taskPage and arg_9_0.taskPage.GetLoaded():
		arg_9_0.taskPage.OnUpdateTask(arg_9_1)

def var_0_0.onBackPressed(arg_10_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
	arg_10_0.emit(var_0_0.ON_BACK)

def var_0_0.willExit(arg_11_0):
	arg_11_0.taskPage.Destroy()

	if isActive(pg.MsgboxMgr.GetInstance()._go):
		triggerButton(pg.MsgboxMgr.GetInstance()._closeBtn)

return var_0_0
