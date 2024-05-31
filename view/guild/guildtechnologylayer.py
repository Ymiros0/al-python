local var_0_0 = class("GuildTechnologyLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "GuildEmptyUI"

def var_0_0.setGuild(arg_2_0, arg_2_1):
	arg_2_0.guildVO = arg_2_1

def var_0_0.init(arg_3_0):
	arg_3_0.technologyPage = GuildTechnologyPage.New(arg_3_0._tf, arg_3_0.event)
	arg_3_0.helpBtn = arg_3_0.findTF("frame/help")

def var_0_0.didEnter(arg_4_0):
	arg_4_0.UpdatePainting()
	arg_4_0.technologyPage.ExecuteAction("SetUp", arg_4_0.guildVO)
	onButton(arg_4_0, arg_4_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.guild_tech_tip.tip
		}), SFX_PANEL)

def var_0_0.UpdatePainting(arg_6_0):
	local var_6_0 = arg_6_0.guildVO.GetOfficePainting()

	pg.GuildPaintingMgr.GetInstance().Update(var_6_0, Vector3(-737, -171, 0))

def var_0_0.UpdateUpgradeList(arg_7_0):
	if arg_7_0.technologyPage.GetLoaded():
		arg_7_0.technologyPage.UpdateUpgradeList()

def var_0_0.UpdateBreakOutList(arg_8_0):
	if arg_8_0.technologyPage.GetLoaded():
		arg_8_0.technologyPage.UpdateBreakOutList()

def var_0_0.UpdateGuild(arg_9_0, arg_9_1):
	arg_9_0.setGuild(arg_9_1)

	if arg_9_0.technologyPage and arg_9_0.technologyPage.GetLoaded():
		arg_9_0.technologyPage.Update(arg_9_0.guildVO)

def var_0_0.UpdateAll(arg_10_0):
	if arg_10_0.technologyPage.GetLoaded():
		arg_10_0.technologyPage.Flush()

def var_0_0.onBackPressed(arg_11_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
	arg_11_0.emit(var_0_0.ON_BACK)

def var_0_0.willExit(arg_12_0):
	arg_12_0.technologyPage.Destroy()

	if isActive(pg.MsgboxMgr.GetInstance()._go):
		triggerButton(pg.MsgboxMgr.GetInstance()._closeBtn)

return var_0_0
