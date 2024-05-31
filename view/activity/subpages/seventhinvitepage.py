local var_0_0 = class("SeventhInvitePage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.rtMarks = arg_1_0._tf.Find("AD/progress")
	arg_1_0.rtFinish = arg_1_0._tf.Find("AD/award")
	arg_1_0.rtBtns = arg_1_0._tf.Find("AD/btn_list")

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.gameId = arg_2_0.activity.getConfig("config_client").mini_game_id
	arg_2_0.hubId = pg.mini_game[arg_2_0.gameId].hub_id
	arg_2_0.data = getProxy(MiniGameProxy).GetHubByHubId(arg_2_0.hubId)
	arg_2_0.ultimate = arg_2_0.data.ultimate
	arg_2_0.usedtime = arg_2_0.data.usedtime
	arg_2_0.maxtime = arg_2_0.data.getConfig("reward_need")

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.rtBtns.Find("go"), function()
		pg.m02.sendNotification(GAME.GO_MINI_GAME, arg_3_0.gameId), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.rtBtns.Find("get"), function()
		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_3_0.hubId,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		}), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_6_0):
	local var_6_0 = arg_6_0.maxtime
	local var_6_1 = arg_6_0.usedtime
	local var_6_2 = arg_6_0.rtMarks.childCount

	for iter_6_0 = 1, var_6_2:
		local var_6_3 = arg_6_0.rtMarks.GetChild(iter_6_0 - 1)

		setActive(var_6_3.Find("mark"), iter_6_0 <= var_6_1)
		setActive(var_6_3.Find("icon"), iter_6_0 == var_6_1 and arg_6_0.ultimate == 0)

	setActive(arg_6_0.rtFinish.Find("got"), arg_6_0.ultimate == 1)
	setActive(arg_6_0.rtBtns.Find("get"), arg_6_0.ultimate == 0 and var_6_1 == var_6_0)
	setActive(arg_6_0.rtBtns.Find("got"), arg_6_0.ultimate == 1)
	setActive(arg_6_0.rtBtns.Find("go"), var_6_1 < var_6_0)
	setActive(arg_6_0.rtBtns.Find("red"), var_6_1 <= var_6_0 and arg_6_0.ultimate != 1 and arg_6_0.data.count > 0)

return var_0_0
