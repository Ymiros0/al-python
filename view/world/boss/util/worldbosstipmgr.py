pg = pg or {}
pg.WorldBossTipMgr = singletonClass("WorldBossTipMgr")

local var_0_0 = pg.WorldBossTipMgr
local var_0_1 = True
local var_0_2 = False
local var_0_3 = {
	"LevelMediator2",
	"WorldMediator",
	"WorldBossMediator"
}

def var_0_0.Init(arg_1_0, arg_1_1):
	arg_1_0.isInit = True
	arg_1_0.list = {}

	PoolMgr.GetInstance().GetUI("WorldBossTipUI", True, function(arg_2_0)
		arg_1_0._go = arg_2_0
		arg_1_0._tf = tf(arg_2_0)

		setActive(arg_1_0._go, True)

		arg_1_0.tipTF = arg_1_0._tf.Find("BG")
		arg_1_0.tipTFCG = arg_1_0.tipTF.GetComponent(typeof(CanvasGroup))
		arg_1_0.scrollText = arg_1_0.tipTF.Find("Text").GetComponent("ScrollText")

		setParent(arg_1_0._tf, GameObject.Find("OverlayCamera/Overlay/UIOverlay").transform)

		arg_1_0.richText = arg_1_0.tipTF.Find("Text").GetComponent("RichText")

		setActive(arg_1_0.tipTF, False)

		if arg_1_1:
			arg_1_1())

def var_0_0.Show(arg_3_0, arg_3_1):
	if var_0_2:
		local function var_3_0()
			if arg_3_0.IsEnable(arg_3_1.GetType()):
				table.insert(arg_3_0.list, arg_3_1)

				if #arg_3_0.list == 1:
					arg_3_0.Start()
			else
				print("Message intercepted")

		if not arg_3_0.isInit:
			arg_3_0.Init(var_3_0)
		else
			var_3_0()

	if var_0_1 and arg_3_0.IsEnableNotify(arg_3_1.GetType()):
		local var_3_1 = arg_3_1.GetRoleName()
		local var_3_2 = arg_3_1.GetType()
		local var_3_3
		local var_3_4

		if WorldBoss.SUPPORT_TYPE_FRIEND == var_3_2:
			var_3_3 = ChatConst.ChannelFriend
			var_3_4 = i18n("world_word_friend")
		elif WorldBoss.SUPPORT_TYPE_GUILD == var_3_2:
			var_3_3 = ChatConst.ChannelGuild
			var_3_4 = i18n("world_word_guild_member")
		else
			var_3_3 = ChatConst.ChannelWorldBoss
			var_3_4 = i18n("world_word_guild_player")

		assert(var_3_3)

		local var_3_5 = arg_3_1.GetPlayer()
		local var_3_6 = getProxy(PlayerProxy).getData()

		print(var_3_3, var_3_4)

		local var_3_7 = {
			id = 4,
			timestamp = pg.TimeMgr.GetInstance().GetServerTime(),
			args = {
				isDeath = False,
				supportType = var_3_4,
				playerName = var_3_1,
				bossName = arg_3_1.config.name,
				level = arg_3_1.level,
				wordBossId = arg_3_1.id,
				lastTime = arg_3_1.lastTime,
				wordBossConfigId = arg_3_1.configId
			},
			player = var_3_5 or var_3_6,
			uniqueId = arg_3_1.id .. "_" .. arg_3_1.lastTime
		}

		if var_3_3 == ChatConst.ChannelGuild:
			arg_3_0.AddGuildMsg(var_3_3, var_3_7)
		else
			getProxy(ChatProxy).addNewMsg(ChatMsg.New(var_3_3, var_3_7))

def var_0_0.AddGuildMsg(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = getProxy(GuildProxy).getRawData()

	if not var_5_0:
		return

	local var_5_1 = var_5_0.getMemberById(arg_5_2.player.id)

	if not var_5_1:
		return

	arg_5_2.player = var_5_1

	getProxy(GuildProxy).AddNewMsg(ChatMsg.New(arg_5_1, arg_5_2))

def var_0_0.IsEnableNotify(arg_6_0, arg_6_1):
	return True

def var_0_0.IsEnable(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.IsEnableNotify(arg_7_1)
	local var_7_1 = (function()
		local var_8_0 = getProxy(ContextProxy).getCurrentContext()

		return _.any(var_0_3, function(arg_9_0)
			return var_8_0.mediator.__cname == arg_9_0))()

	return var_7_0 and var_7_1

def var_0_0.Start(arg_10_0):
	if #arg_10_0.list > 0:
		arg_10_0.AddTimer()

def var_0_0.BuildClickableTxt(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.BuildTipText()

	return string.format("<material=underline c=#FFFFFF h=1 event=onClick args=" .. arg_11_1.id .. ">%s</material>", var_11_0)

def var_0_0.AddTimer(arg_12_0):
	local var_12_0 = arg_12_0.list[1]

	arg_12_0.RemoveTimer()
	setActive(arg_12_0.tipTF, True)
	arg_12_0.scrollText.SetText(arg_12_0.BuildClickableTxt(var_12_0))
	LeanTween.value(go(arg_12_0.tipTF), 1, 0, 1).setOnUpdate(System.Action_float(function(arg_13_0)
		arg_12_0.tipTFCG.alpha = arg_13_0)).setOnComplete(System.Action(function()
		setActive(arg_12_0.tipTF, False)
		arg_12_0.scrollText.SetText("")

		arg_12_0.tipTFCG.alpha = 1

		table.remove(arg_12_0.list, 1)
		arg_12_0.Start())).setDelay(4)

local function var_0_4(arg_15_0, arg_15_1)
	if not arg_15_0 or #arg_15_0 == 0:
		return

	local var_15_0 = _.detect(arg_15_0, function(arg_16_0)
		return arg_16_0.id == tonumber(arg_15_1))

	if not var_15_0 or var_15_0.isDeath():
		return

	return True

def var_0_0.OnClick(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4):
	local var_17_0 = nowWorld()

	if not var_17_0 or not var_17_0.IsActivate():
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_unactivated"))

		return

	local var_17_1 = var_17_0.GetBossProxy()

	if not var_17_1:
		return

	local function var_17_2(arg_18_0)
		local var_18_0 = getProxy(ContextProxy)
		local var_18_1 = var_18_0.getCurrentContext()

		local function var_18_2()
			local function var_19_0()
				var_18_1 = var_18_0.getCurrentContext()

				if var_18_1.getContextByMediator(CombatLoadMediator):
					return

				if var_18_1.mediator.__cname == "WorldBossMediator":
					return

				pg.m02.sendNotification(GAME.GO_WORLD_BOSS_SCENE)
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.WORLDBOSS, {
					worldBossId = tonumber(arg_17_2)
				})

			pg.m02.sendNotification(GAME.CHECK_WORLD_BOSS_STATE, {
				bossId = tonumber(arg_17_2),
				time = arg_17_3,
				callback = var_19_0,
				failedCallback = arg_17_4
			})

		if var_18_1.mediator.__cname == "BattleMediator":
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("world_joint_exit_battle_tip"),
				def onYes:()
					pg.m02.sendNotification(GAME.QUIT_BATTLE)
					var_18_2()
			})
		else
			var_18_2()

	if var_17_1.isSetup:
		local var_17_3 = var_17_1.GetBossById(tonumber(arg_17_2))

		if not var_17_3 or var_17_3.isDeath():
			local var_17_4 = getProxy(ChatProxy)
			local var_17_5 = var_17_3 and var_17_3.lastTime or "0"
			local var_17_6 = var_17_4.GetMessagesByUniqueId(tonumber(arg_17_2) .. "_" .. var_17_5)

			for iter_17_0, iter_17_1 in ipairs(var_17_6):
				iter_17_1.args.isDeath = True

				var_17_4.UpdateMsg(iter_17_1)

			local var_17_7 = getProxy(GuildProxy)
			local var_17_8 = var_17_7.GetMessagesByUniqueId(tonumber(arg_17_2) .. "_" .. var_17_5)

			for iter_17_2, iter_17_3 in ipairs(var_17_8):
				iter_17_3.args.isDeath = True

				var_17_7.UpdateMsg(iter_17_3)

			arg_17_4()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_none"))

			return

		var_17_2()

def var_0_0.RemoveTimer(arg_22_0):
	if LeanTween.isTweening(go(arg_22_0.tipTF)):
		LeanTween.cancel(go(arg_22_0.tipTF))
