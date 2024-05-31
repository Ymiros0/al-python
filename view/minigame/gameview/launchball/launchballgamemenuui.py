local var_0_0 = class("LaunchBallGameMenuUI")

var_0_0.player_item = {
	{
		skill_1_desc = "launch_ball_hatsuduki_skill_1_desc",
		name = "Hatsuduki",
		skill_1 = "launch_ball_hatsuduki_skill_1",
		skill_2 = "launch_ball_hatsuduki_skill_2",
		id = 1,
		skill_2_desc = "launch_ball_hatsuduki_skill_2_desc"
	},
	{
		skill_1_desc = "launch_ball_shinano_skill_1_desc",
		name = "Shinano",
		skill_1 = "launch_ball_shinano_skill_1",
		skill_2 = "launch_ball_shinano_skill_2",
		id = 2,
		skill_2_desc = "launch_ball_shinano_skill_2_desc"
	},
	{
		skill_1_desc = "launch_ball_yura_skill_1_desc",
		name = "Yura",
		skill_1 = "launch_ball_yura_skill_1",
		skill_2 = "launch_ball_yura_skill_2",
		id = 3,
		skill_2_desc = "launch_ball_yura_skill_2_desc"
	},
	{
		skill_1_desc = "launch_ball_shimakaze_skill_1_desc",
		name = "Shimakaze",
		skill_1 = "launch_ball_shimakaze_skill_1",
		skill_2 = "launch_ball_shimakaze_skill_2",
		id = 4,
		skill_2_desc = "launch_ball_shimakaze_skill_2_desc"
	}
}
var_0_0.skill_detail_desc = "launch_ball_skill_desc"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.menuUI = findTF(arg_1_0._tf, "ui/menuUI")
	arg_1_0.battleScrollRect = GetComponent(findTF(arg_1_0.menuUI, "battList"), typeof(ScrollRect))
	arg_1_0.totalTimes = LaunchBallGameVo.total_times
	arg_1_0.battleItems = {}
	arg_1_0.dropItems = {}

	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_2_0 = arg_1_0.battleScrollRect.normalizedPosition.y + 1 / (arg_1_0.totalTimes - 4)

		if var_2_0 > 1:
			var_2_0 = 1

		scrollTo(arg_1_0.battleScrollRect, 0, var_2_0), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_3_0 = arg_1_0.battleScrollRect.normalizedPosition.y - 1 / (arg_1_0.totalTimes - 4)

		if var_3_0 < 0:
			var_3_0 = 0

		scrollTo(arg_1_0.battleScrollRect, 0, var_3_0), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnBack"), function()
		arg_1_0._event.emit(BeachGuardGameView.CLOSE_GAME), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnRule"), function()
		arg_1_0._event.emit(BeachGuardGameView.SHOW_RULE), SFX_CANCEL)

	arg_1_0.btnStart = findTF(arg_1_0.menuUI, "btnStart")

	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnStart"), function()
		if arg_1_0.playerId == None:
			return

		arg_1_0._event.emit(BeachGuardGameView.READY_START), SFX_CANCEL)

	local var_1_0 = findTF(arg_1_0.menuUI, "tplBattleItem")

	for iter_1_0 = 1, 7:
		local var_1_1 = tf(instantiate(var_1_0))

		var_1_1.name = "battleItem_" .. iter_1_0

		setParent(var_1_1, findTF(arg_1_0.menuUI, "battList/Viewport/Content"))

		local var_1_2 = iter_1_0
		local var_1_3 = findTF(var_1_1, "icon")

		onButton(arg_1_0._event, var_1_3, function()
			return, SFX_PANEL)
		table.insert(arg_1_0.dropItems, var_1_3)
		setActive(var_1_1, True)
		table.insert(arg_1_0.battleItems, var_1_1)

	arg_1_0.players = {}

	for iter_1_1 = 1, #var_0_0.player_item:
		local var_1_4 = var_0_0.player_item[iter_1_1]
		local var_1_5 = findTF(arg_1_0.menuUI, "player/" .. var_1_4.name)
		local var_1_6 = LaunchBallActivityMgr.GetPlayerZhuanshuIndex(var_1_4.id)
		local var_1_7 = False

		if var_1_6:
			var_1_7 = LaunchBallActivityMgr.CheckZhuanShuAble(ActivityConst.MINIGAME_ZUMA, var_1_6)
		else
			var_1_7 = True

		setActive(findTF(var_1_5, "ad/mask"), not var_1_7)
		setScrollText(findTF(var_1_5, "ad/skillPanel/skill1/text"), i18n(var_1_4.skill_1))
		setScrollText(findTF(var_1_5, "ad/skillPanel/skill2/text"), i18n(var_1_4.skill_2))
		setText(findTF(var_1_5, "ad/skillPanel/detail/img"), i18n(var_0_0.skill_detail_desc))

		local var_1_8 = GetComponent(findTF(var_1_5, "ad/icon"), typeof(Animator))

		onButton(arg_1_0._event, findTF(var_1_5, "ad/click"), function()
			if not var_1_7:
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.ZUMA_PT_SHOP)

				return

			if arg_1_0.playerId == var_1_4.id:
				arg_1_0.selectPlayer(None)
			else
				arg_1_0.selectPlayer(var_1_4.id), SFX_CONFIRM)
		onButton(arg_1_0._event, findTF(var_1_5, "ad/skillPanel"), function()
			arg_1_0.showSkillPanel(var_1_4)
			setActive(arg_1_0.skillDetailPanel, True), SFX_CONFIRM)
		table.insert(arg_1_0.players, {
			tf = var_1_5,
			data = var_1_4,
			anim = var_1_8
		})

	arg_1_0.skillDetailPanel = findTF(arg_1_0.menuUI, "skillDetail")

	setActive(arg_1_0.skillDetailPanel, False)
	onButton(arg_1_0._event, findTF(arg_1_0.skillDetailPanel, "ad"), function()
		setActive(arg_1_0.skillDetailPanel, False), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.skillDetailPanel, "ad/btnOk"), function()
		setActive(arg_1_0.skillDetailPanel, False), SFX_CANCEL)

	arg_1_0.selectMask = findTF(arg_1_0.menuUI, "selectMask")

	setText(findTF(arg_1_0.menuUI, "select"), i18n(LaunchBallGameVo.launchball_minigame_select))
	setText(findTF(arg_1_0.menuUI, "selectMask/unSelect"), i18n(LaunchBallGameVo.launchball_minigame_un_select))
	arg_1_0.selectPlayer(None)

def var_0_0.selectPlayer(arg_12_0, arg_12_1):
	for iter_12_0 = 1, #arg_12_0.players:
		if arg_12_0.players[iter_12_0].data.id == arg_12_1:
			setActive(findTF(arg_12_0.players[iter_12_0].tf, "ad/select"), True)
			arg_12_0.players[iter_12_0].anim.Play("Attack")
		else
			setActive(findTF(arg_12_0.players[iter_12_0].tf, "ad/select"), False)
			arg_12_0.players[iter_12_0].anim.Play("Idle")

	arg_12_0.playerId = arg_12_1

	LaunchBallGameVo.SetPlayer(arg_12_0.playerId)

	if arg_12_0.playerId == None:
		setActive(arg_12_0.btnStart, False)
		setActive(arg_12_0.selectMask, False)
		setActive(findTF(arg_12_0.menuUI, "select"), True)
	else
		setActive(arg_12_0.btnStart, True)
		setActive(arg_12_0.selectMask, True)
		setActive(findTF(arg_12_0.menuUI, "select"), False)

def var_0_0.showSkillPanel(arg_13_0, arg_13_1):
	local var_13_0 = i18n(arg_13_1.skill_1)
	local var_13_1 = i18n(arg_13_1.skill_1_desc)
	local var_13_2 = i18n(arg_13_1.skill_2)
	local var_13_3 = i18n(arg_13_1.skill_2_desc)

	if var_13_0:
		setText(findTF(arg_13_0.skillDetailPanel, "ad/skill1Bg/skill1Name"), var_13_0)
		setText(findTF(arg_13_0.skillDetailPanel, "ad/skill1Desc"), var_13_1)
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill1Desc"), True)
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill1Bg"), True)
	else
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill1Desc"), False)
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill1Bg"), False)

	if var_13_2:
		setText(findTF(arg_13_0.skillDetailPanel, "ad/skill2Bg/skill2Name"), var_13_2)
		setText(findTF(arg_13_0.skillDetailPanel, "ad/skill2Desc"), var_13_3)
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill2Desc"), True)
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill2Bg"), True)
	else
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill2Desc"), False)
		setActive(findTF(arg_13_0.skillDetailPanel, "ad/skill2Bg"), False)

def var_0_0.show(arg_14_0, arg_14_1):
	setActive(arg_14_0.menuUI, arg_14_1)

def var_0_0.update(arg_15_0, arg_15_1):
	arg_15_0.mgHubData = arg_15_1

	local var_15_0 = arg_15_0.getGameUsedTimes(arg_15_1)
	local var_15_1 = arg_15_0.getGameTimes(arg_15_1)

	for iter_15_0 = 1, #arg_15_0.battleItems:
		setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_open"), False)
		setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_closed"), False)
		setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_clear"), False)
		setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_current"), False)

		if iter_15_0 <= var_15_0:
			SetParent(arg_15_0.dropItems[iter_15_0], findTF(arg_15_0.battleItems[iter_15_0], "state_clear/icon"))
			setActive(arg_15_0.dropItems[iter_15_0], True)
			setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_clear"), True)
		elif iter_15_0 == var_15_0 + 1 and var_15_1 >= 1:
			setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_current"), True)
			SetParent(arg_15_0.dropItems[iter_15_0], findTF(arg_15_0.battleItems[iter_15_0], "state_current/icon"))
			setActive(arg_15_0.dropItems[iter_15_0], True)
		elif var_15_0 < iter_15_0 and iter_15_0 <= var_15_0 + var_15_1:
			setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_open"), True)
			SetParent(arg_15_0.dropItems[iter_15_0], findTF(arg_15_0.battleItems[iter_15_0], "state_open/icon"))
			setActive(arg_15_0.dropItems[iter_15_0], True)
		else
			setActive(findTF(arg_15_0.battleItems[iter_15_0], "state_closed"), True)
			SetParent(arg_15_0.dropItems[iter_15_0], findTF(arg_15_0.battleItems[iter_15_0], "state_closed/icon"))
			setActive(arg_15_0.dropItems[iter_15_0], True)

	local var_15_2 = 1 - (var_15_0 - 3 < 0 and 0 or var_15_0 - 3) / (arg_15_0.totalTimes - 4)

	if var_15_2 > 1:
		var_15_2 = 1

	scrollTo(arg_15_0.battleScrollRect, 0, var_15_2)
	setActive(findTF(arg_15_0.menuUI, "btnStart/tip"), var_15_1 > 0)

def var_0_0.CheckGet(arg_16_0):
	local var_16_0 = arg_16_0.mgHubData

	setActive(findTF(arg_16_0.menuUI, "got"), False)

	local var_16_1 = arg_16_0.getUltimate(var_16_0)

	if var_16_1 and var_16_1 != 0:
		setActive(findTF(arg_16_0.menuUI, "got"), True)

	if var_16_1 == 0:
		if LaunchBallGameVo.total_times > arg_16_0.getGameUsedTimes(var_16_0):
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_16_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_16_0.menuUI, "got"), True)

def var_0_0.getGameTimes(arg_17_0, arg_17_1):
	return arg_17_1.count

def var_0_0.getGameUsedTimes(arg_18_0, arg_18_1):
	return arg_18_1.usedtime

def var_0_0.getUltimate(arg_19_0, arg_19_1):
	return arg_19_1.ultimate

return var_0_0
