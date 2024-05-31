local var_0_0 = class("FourthInvitePage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.icons = {
		arg_1_0.findTF("AD/bg/npc1"),
		arg_1_0.findTF("AD/bg/npc2"),
		arg_1_0.findTF("AD/bg/npc3"),
		arg_1_0.findTF("AD/bg/npc4"),
		arg_1_0.findTF("AD/bg/npc5"),
		arg_1_0.findTF("AD/bg/npc6"),
		arg_1_0.findTF("AD/bg/npc7")
	}
	arg_1_0.helpBtn = arg_1_0.findTF("AD/help")
	arg_1_0.goBtn = arg_1_0.findTF("AD/go")
	arg_1_0.gotBtn = arg_1_0.findTF("AD/got")

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.gameId = arg_2_0.activity.getConfig("config_client").mini_game_id
	arg_2_0.hubId = pg.mini_game[arg_2_0.gameId].hub_id
	arg_2_0.data = getProxy(MiniGameProxy).GetHubByHubId(arg_2_0.hubId)
	arg_2_0.ultimate = arg_2_0.data.ultimate
	arg_2_0.usedtime = arg_2_0.data.usedtime
	arg_2_0.maxtime = arg_2_0.data.getConfig("reward_need")

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.goBtn, function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, arg_3_0.gameId), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.catchteasure_help.tip
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_6_0):
	SetActive(arg_6_0.gotBtn, arg_6_0.ultimate == 1)
	arg_6_0.UpdateSigned()
	arg_6_0.CheckGet()

def var_0_0.UpdateSigned(arg_7_0):
	local var_7_0 = arg_7_0.maxtime
	local var_7_1 = arg_7_0.usedtime

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.icons):
		local var_7_2 = iter_7_0 <= var_7_1

		setActive(iter_7_1, var_7_2)

def var_0_0.CheckGet(arg_8_0):
	if arg_8_0.ultimate == 0:
		if arg_8_0.maxtime > arg_8_0.usedtime:
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_8_0.hubId,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

return var_0_0
