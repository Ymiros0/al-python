local var_0_0 = class("Fushun3GameView", import("..BaseMiniGameView"))
local var_0_1 = "event./ui/ddldaoshu2"
local var_0_2 = "fushun_game3_tip"
local var_0_3 = "event./ui/taosheng"
local var_0_4 = "event./ui/tiji"
local var_0_5 = "event./ui/baozha1"
local var_0_6 = "event./ui/break_out_full"

def var_0_0.getUIName(arg_1_0):
	return "Fushun3GameView"

def var_0_0.didEnter(arg_2_0):
	arg_2_0.initEvent()
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.initGameUI()
	arg_2_0.initController()
	arg_2_0.updateMenuUI()
	arg_2_0.openMenuUI()

def var_0_0.initEvent(arg_3_0):
	arg_3_0.bind(Fushun3GameEvent.create_item_call, function(arg_4_0, arg_4_1, arg_4_2)
		if arg_3_0.itemController:
			arg_3_0.itemController.createItem(arg_4_1.name, arg_4_1.pos))
	arg_3_0.bind(Fushun3GameEvent.create_platform_item_call, function(arg_5_0, arg_5_1, arg_5_2)
		if arg_3_0.itemController:
			arg_3_0.itemController.createPlatformItem(arg_5_1.pos, arg_5_1.id))
	arg_3_0.bind(Fushun3GameEvent.item_follow_call, function(arg_6_0, arg_6_1, arg_6_2)
		if arg_3_0.itemController:
			arg_3_0.itemController.itemFollow(arg_6_1.anchoredPos))
	arg_3_0.bind(Fushun3GameEvent.create_monster_call, function(arg_7_0, arg_7_1, arg_7_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.createMonster(arg_7_1.pos))
	arg_3_0.bind(Fushun3GameEvent.player_attack_call, function(arg_8_0, arg_8_1, arg_8_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.checkMonsterDamage(arg_8_1.collider, arg_8_1.callback, Fushun3GameEvent.attack_damdage_monster_call))
	arg_3_0.bind(Fushun3GameEvent.char_damaged_call, function(arg_9_0, arg_9_1, arg_9_2)
		local var_9_0 = arg_3_0.charController.getHeart()

		arg_3_0.updateGameUI()

		if var_9_0 == 0:
			arg_3_0.onGameOver())
	arg_3_0.bind(Fushun3GameEvent.check_item_damage, function(arg_10_0, arg_10_1, arg_10_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.checkMonsterDamage(arg_10_1.collider, arg_10_1.callback, Fushun3GameEvent.shot_damage_monster_call))
	arg_3_0.bind(Fushun3GameEvent.check_player_damage, function(arg_11_0, arg_11_1, arg_11_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.checkPlayerDamage(arg_11_1.tf, arg_11_1.callback))
	arg_3_0.bind(Fushun3GameEvent.power_damage_monster_call, function(arg_12_0, arg_12_1, arg_12_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.damageMonster(arg_12_1.tf, Fushun3GameEvent.power_damage_monster_call))
	arg_3_0.bind(Fushun3GameEvent.shot_damage_monster_call, function(arg_13_0, arg_13_1, arg_13_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.damageMonster(arg_13_1.tf, Fushun3GameEvent.shot_damage_monster_call))
	arg_3_0.bind(Fushun3GameEvent.attack_damdage_monster_call, function(arg_14_0, arg_14_1, arg_14_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.damageMonster(arg_14_1.tf, Fushun3GameEvent.attack_damdage_monster_call))
	arg_3_0.bind(Fushun3GameEvent.kick_damage_monster_call, function(arg_15_0, arg_15_1, arg_15_2)
		if arg_3_0.monsterController:
			arg_3_0.monsterController.damageMonster(arg_15_1.tf, Fushun3GameEvent.kick_damage_monster_call, arg_15_1.callback))
	arg_3_0.bind(Fushun3GameEvent.add_anim_effect_call, function(arg_16_0, arg_16_1, arg_16_2)
		if arg_3_0.effectController and arg_16_1:
			arg_3_0.effectController.addEffectByAnim(arg_16_1.clipName, arg_16_1.targetTf))
	arg_3_0.bind(Fushun3GameEvent.add_effect_call, function(arg_17_0, arg_17_1, arg_17_2)
		if arg_3_0.effectController and arg_17_1:
			arg_3_0.effectController.addEffectByName(arg_17_1.effectName, arg_17_1.targetTf))
	arg_3_0.bind(Fushun3GameEvent.power_speed_call, function(arg_18_0, arg_18_1, arg_18_2)
		if arg_3_0.platformController:
			arg_3_0.platformController.onPlayerPower())
	arg_3_0.bind(Fushun3GameEvent.add_monster_score_call, function(arg_19_0, arg_19_1, arg_19_2)
		arg_3_0.charController.addPower(Fushun3GameConst.monster_score)
		arg_3_0.addScore(Fushun3GameConst.monster_score))
	arg_3_0.bind(Fushun3GameEvent.game_over_call, function(arg_20_0, arg_20_1, arg_20_2)
		arg_3_0.onGameOver())
	arg_3_0.bind(Fushun3GameEvent.day_night_change, function(arg_21_0, arg_21_1, arg_21_2)
		if arg_3_0.platformController:
			arg_3_0.platformController.updateDayNight())

def var_0_0.onEventHandle(arg_22_0, arg_22_1):
	return

def var_0_0.initData(arg_23_0):
	Fushun3GameVo.ChangeTimeType(math.random() < 0.5 and Fushun3GameConst.day_type or Fushun3GameConst.night_type)

	arg_23_0.dayTimeFlag = Fushun3GameVo.GetTimeFlag()

	local var_23_0 = Application.targetFrameRate or 60

	if var_23_0 > 60:
		var_23_0 = 60

	arg_23_0.timer = Timer.New(function()
		arg_23_0.onTimer(), 1 / var_23_0, -1)

def var_0_0.initController(arg_25_0):
	arg_25_0.charTf = findTF(arg_25_0._tf, "sceneContainer/scene/char")
	arg_25_0.rectCollider = RectCollider.New(arg_25_0.charTf, {}, arg_25_0)

	arg_25_0.rectCollider.addScript(FuShunMovementScript.New())
	arg_25_0.rectCollider.addScript(FuShunAttakeScript.New())
	arg_25_0.rectCollider.addScript(FuShunJumpScript.New())
	arg_25_0.rectCollider.addScript(FuShunPowerSpeedScript.New())
	arg_25_0.rectCollider.addScript(FuShunDamageScript.New())

	local var_25_0 = findTF(arg_25_0._tf, "tpls/platformTpls")
	local var_25_1 = findTF(arg_25_0.sceneTf, "platform/content")

	arg_25_0.platformController = Fushun3PlatformControll.New(arg_25_0.sceneTf, var_25_0, var_25_1, arg_25_0)
	arg_25_0.sceneController = Fushun3SceneController.New(arg_25_0.backSceneTf, arg_25_0.sceneTf, arg_25_0.charTf)

	local var_25_2 = arg_25_0.rectCollider.getCollisionInfo()

	arg_25_0.charController = Fushun3CharController.New(arg_25_0.rectCollider, arg_25_0.charTf, var_25_2, arg_25_0.powerProgressSlider, arg_25_0)

	local var_25_3 = findTF(arg_25_0._tf, "tpls/itemTpls")

	arg_25_0.itemController = Fushun3ItemController.New(arg_25_0.sceneTf, arg_25_0.charTf, var_25_3, arg_25_0)

	arg_25_0.itemController.setCallback(function(arg_26_0, arg_26_1)
		arg_25_0.onControllerCallback(arg_26_0, arg_26_1))

	local var_25_4 = findTF(arg_25_0._tf, "tpls/bgTpls")
	local var_25_5 = findTF(arg_25_0._tf, "tpls/fireTpls")
	local var_25_6 = findTF(arg_25_0._tf, "tpls/petalTpl")

	arg_25_0.bgController = Fushun3BgController.New(var_25_4, var_25_5, var_25_6, arg_25_0.backSceneTf, arg_25_0)

	local var_25_7 = findTF(arg_25_0._tf, "tpls/monsterTpls")
	local var_25_8 = findTF(arg_25_0.sceneTf, "monster")

	arg_25_0.monsterController = Fushun3MonsterController.New(var_25_7, var_25_8, arg_25_0.sceneTf, arg_25_0)

	local var_25_9 = findTF(arg_25_0._tf, "tpls/efTpls")
	local var_25_10 = findTF(arg_25_0.sceneTf, "effect")

	arg_25_0.effectController = Fushun3EffectController.New(var_25_9, var_25_10, arg_25_0)

def var_0_0.initUI(arg_27_0):
	arg_27_0.backSceneTf = findTF(arg_27_0._tf, "sceneContainer/scene_background")
	arg_27_0.frontSceneTf = findTF(arg_27_0._tf, "sceneContainer/scene_front")
	arg_27_0.sceneTf = findTF(arg_27_0._tf, "sceneContainer/scene")
	arg_27_0.clickMask = findTF(arg_27_0._tf, "clickMask")
	arg_27_0.countUI = findTF(arg_27_0._tf, "pop/CountUI")
	arg_27_0.countAnimator = GetComponent(findTF(arg_27_0.countUI, "count"), typeof(Animator))
	arg_27_0.countDft = GetOrAddComponent(findTF(arg_27_0.countUI, "count"), typeof(DftAniEvent))

	arg_27_0.countDft.SetTriggerEvent(function()
		return)
	arg_27_0.countDft.SetEndEvent(function()
		setActive(arg_27_0.countUI, False)
		arg_27_0.gameStart())
	SetActive(arg_27_0.countUI, False)

	arg_27_0.leaveUI = findTF(arg_27_0._tf, "pop/LeaveUI")

	onButton(arg_27_0, findTF(arg_27_0.leaveUI, "ad/btnOk"), function()
		arg_27_0.resumeGame()
		arg_27_0.onGameOver(), SFX_CANCEL)
	onButton(arg_27_0, findTF(arg_27_0.leaveUI, "ad/btnCancel"), function()
		arg_27_0.resumeGame(), SFX_CANCEL)
	SetActive(arg_27_0.leaveUI, False)

	arg_27_0.pauseUI = findTF(arg_27_0._tf, "pop/pauseUI")

	onButton(arg_27_0, findTF(arg_27_0.pauseUI, "ad/btnOk"), function()
		setActive(arg_27_0.pauseUI, False)
		arg_27_0.resumeGame(), SFX_CANCEL)
	SetActive(arg_27_0.pauseUI, False)

	arg_27_0.settlementUI = findTF(arg_27_0._tf, "pop/SettleMentUI")

	onButton(arg_27_0, findTF(arg_27_0.settlementUI, "ad/btnOver"), function()
		setActive(arg_27_0.settlementUI, False)
		arg_27_0.openMenuUI(), SFX_CANCEL)
	SetActive(arg_27_0.settlementUI, False)

	arg_27_0.menuUI = findTF(arg_27_0._tf, "pop/menuUI")
	arg_27_0.battleScrollRect = GetComponent(findTF(arg_27_0.menuUI, "battList"), typeof(ScrollRect))
	arg_27_0.totalTimes = arg_27_0.getGameTotalTime()

	local var_27_0 = arg_27_0.getGameUsedTimes() - 4 < 0 and 0 or arg_27_0.getGameUsedTimes() - 4

	scrollTo(arg_27_0.battleScrollRect, 0, 1 - var_27_0 / (arg_27_0.totalTimes - 4))
	onButton(arg_27_0, findTF(arg_27_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_34_0 = arg_27_0.battleScrollRect.normalizedPosition.y + 1 / (arg_27_0.totalTimes - 4)

		if var_34_0 > 1:
			var_34_0 = 1

		scrollTo(arg_27_0.battleScrollRect, 0, var_34_0), SFX_CANCEL)
	onButton(arg_27_0, findTF(arg_27_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_35_0 = arg_27_0.battleScrollRect.normalizedPosition.y - 1 / (arg_27_0.totalTimes - 4)

		if var_35_0 < 0:
			var_35_0 = 0

		scrollTo(arg_27_0.battleScrollRect, 0, var_35_0), SFX_CANCEL)
	onButton(arg_27_0, findTF(arg_27_0.menuUI, "btnBack"), function()
		arg_27_0.closeView(), SFX_CANCEL)
	onButton(arg_27_0, findTF(arg_27_0.menuUI, "btnRule"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_2].tip
		}), SFX_CANCEL)
	onButton(arg_27_0, findTF(arg_27_0.menuUI, "btnStart"), function()
		setActive(arg_27_0.menuUI, False)
		arg_27_0.readyStart(), SFX_CANCEL)

	local var_27_1 = findTF(arg_27_0.menuUI, "tplBattleItem")

	arg_27_0.battleItems = {}
	arg_27_0.dropItems = {}

	for iter_27_0 = 1, 7:
		local var_27_2 = tf(instantiate(var_27_1))

		var_27_2.name = "battleItem_" .. iter_27_0

		setParent(var_27_2, findTF(arg_27_0.menuUI, "battList/Viewport/Content"))

		local var_27_3 = iter_27_0

		GetSpriteFromAtlasAsync("ui/minigameui/fushun3gameui_atlas", "battleDesc" .. var_27_3, function(arg_39_0)
			setImageSprite(findTF(var_27_2, "state_open/buttomDesc"), arg_39_0, True)
			setImageSprite(findTF(var_27_2, "state_clear/buttomDesc"), arg_39_0, True)
			setImageSprite(findTF(var_27_2, "state_current/buttomDesc"), arg_39_0, True)
			setImageSprite(findTF(var_27_2, "state_closed/buttomDesc"), arg_39_0, True))
		setActive(var_27_2, True)
		table.insert(arg_27_0.battleItems, var_27_2)

	if not arg_27_0.handle:
		arg_27_0.handle = UpdateBeat.CreateListener(arg_27_0.Update, arg_27_0)

	UpdateBeat.AddListener(arg_27_0.handle)

def var_0_0.initGameUI(arg_40_0):
	arg_40_0.gameUI = findTF(arg_40_0._tf, "ui/gameUI")
	arg_40_0.powerProgress = findTF(arg_40_0.gameUI, "top/powerProgress")
	arg_40_0.powerProgressSlider = GetComponent(arg_40_0.powerProgress, typeof(Slider))

	onButton(arg_40_0, findTF(arg_40_0.gameUI, "topRight/btnStop"), function()
		arg_40_0.stopGame()
		setActive(arg_40_0.pauseUI, True))
	onButton(arg_40_0, findTF(arg_40_0.gameUI, "btnLeave"), function()
		arg_40_0.stopGame()
		setActive(arg_40_0.leaveUI, True))

	arg_40_0.gameTimeS = findTF(arg_40_0.gameUI, "top/time/s")
	arg_40_0.scoreTf = findTF(arg_40_0.gameUI, "top/score")
	arg_40_0.hearts = {}

	for iter_40_0 = 1, Fushun3GameConst.heart_num:
		table.insert(arg_40_0.hearts, findTF(arg_40_0.gameUI, "top/heart" .. iter_40_0 .. "/full"))

	arg_40_0.atkDelegate = GetOrAddComponent(findTF(arg_40_0.gameUI, "btnAtk"), "EventTriggerListener")
	arg_40_0.atkDelegate.enabled = True

	arg_40_0.atkDelegate.AddPointDownFunc(function(arg_43_0, arg_43_1)
		if arg_40_0.charController:
			arg_40_0.charController.attack())

	arg_40_0.jumpDelegate = GetOrAddComponent(findTF(arg_40_0.gameUI, "btnJump"), "EventTriggerListener")
	arg_40_0.jumpDelegate.enabled = True

	arg_40_0.jumpDelegate.AddPointDownFunc(function(arg_44_0, arg_44_1)
		if arg_40_0.charController:
			arg_40_0.charController.jump())
	setText(findTF(arg_40_0._tf, "pop/LeaveUI/ad/desc/n"), i18n(Fushun3GameConst.mini_game_leave))
	setText(findTF(arg_40_0._tf, "pop/pauseUI/ad/desc/n"), i18n(Fushun3GameConst.mini_game_pause))

def var_0_0.Update(arg_45_0):
	arg_45_0.AddDebugInput()

def var_0_0.AddDebugInput(arg_46_0):
	if arg_46_0.gameStop or arg_46_0.settlementFlag:
		return

	if Application.isEditor:
		-- block empty

def var_0_0.updateMenuUI(arg_47_0):
	local var_47_0 = arg_47_0.getGameUsedTimes()
	local var_47_1 = arg_47_0.getGameTimes()

	for iter_47_0 = 1, #arg_47_0.battleItems:
		setActive(findTF(arg_47_0.battleItems[iter_47_0], "bg/n"), not arg_47_0.dayTimeFlag)
		setActive(findTF(arg_47_0.battleItems[iter_47_0], "bg/d"), arg_47_0.dayTimeFlag)
		setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_open"), False)
		setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_closed"), False)
		setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_clear"), False)
		setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_current"), False)

		if iter_47_0 <= var_47_0:
			setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_clear"), True)
		elif iter_47_0 == var_47_0 + 1 and var_47_1 >= 1:
			setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_current"), True)
		elif var_47_0 < iter_47_0 and iter_47_0 <= var_47_0 + var_47_1:
			setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_open"), True)
		else
			setActive(findTF(arg_47_0.battleItems[iter_47_0], "state_closed"), True)

	arg_47_0.totalTimes = arg_47_0.getGameTotalTime()

	local var_47_2 = 1 - (arg_47_0.getGameUsedTimes() - 3 < 0 and 0 or arg_47_0.getGameUsedTimes() - 3) / (arg_47_0.totalTimes - 4)

	if var_47_2 > 1:
		var_47_2 = 1

	scrollTo(arg_47_0.battleScrollRect, 0, var_47_2)
	setActive(findTF(arg_47_0.menuUI, "btnStart/tip"), var_47_1 > 0)
	arg_47_0.CheckGet()
	arg_47_0.updateDayNightUI()

def var_0_0.CheckGet(arg_48_0):
	setActive(findTF(arg_48_0.menuUI, "got"), False)

	if arg_48_0.getUltimate() and arg_48_0.getUltimate() != 0:
		setActive(findTF(arg_48_0.menuUI, "got"), True)

	if arg_48_0.getUltimate() == 0:
		if arg_48_0.getGameTotalTime() > arg_48_0.getGameUsedTimes():
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_48_0.GetMGHubData().id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_48_0.menuUI, "got"), True)

def var_0_0.openMenuUI(arg_49_0):
	setActive(findTF(arg_49_0._tf, "sceneContainer/scene_front"), False)
	setActive(findTF(arg_49_0._tf, "sceneContainer/scene_background"), False)
	setActive(findTF(arg_49_0._tf, "sceneContainer/scene"), False)
	setActive(findTF(arg_49_0._tf, "bg"), True)
	setActive(arg_49_0.gameUI, False)
	setActive(arg_49_0.menuUI, True)
	arg_49_0.updateMenuUI()

def var_0_0.clearUI(arg_50_0):
	setActive(arg_50_0.sceneTf, False)
	setActive(arg_50_0.settlementUI, False)
	setActive(arg_50_0.countUI, False)
	setActive(arg_50_0.menuUI, False)
	setActive(arg_50_0.gameUI, False)

def var_0_0.readyStart(arg_51_0):
	setActive(arg_51_0.countUI, True)
	arg_51_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1)

def var_0_0.gameStart(arg_52_0):
	setActive(findTF(arg_52_0._tf, "sceneContainer/scene_front"), True)
	setActive(findTF(arg_52_0._tf, "sceneContainer/scene_background"), True)
	setActive(findTF(arg_52_0._tf, "sceneContainer/scene"), True)
	setActive(arg_52_0.gameUI, True)
	setActive(findTF(arg_52_0._tf, "bg"), False)

	arg_52_0.gameStartFlag = True
	arg_52_0.scoreNum = 0
	arg_52_0.playerPosIndex = 2
	arg_52_0.gameStepTime = 0
	arg_52_0.gameOverTime = 0
	arg_52_0.gameTime = Fushun3GameConst.game_time
	arg_52_0.gameLevelTime = Fushun3GameConst.level_time
	arg_52_0.rectCollider.getCollisionInfo().config.moveSpeed = Fushun3GameConst.move_speed

	arg_52_0.rectCollider.start()
	arg_52_0.platformController.start()
	arg_52_0.sceneController.start()
	arg_52_0.charController.start()
	arg_52_0.itemController.start()
	arg_52_0.bgController.start()
	arg_52_0.monsterController.start()
	arg_52_0.effectController.start()
	arg_52_0.updateGameUI()
	arg_52_0.timerStart()

def var_0_0.getGameTimes(arg_53_0):
	return arg_53_0.GetMGHubData().count

def var_0_0.getGameUsedTimes(arg_54_0):
	return arg_54_0.GetMGHubData().usedtime

def var_0_0.getUltimate(arg_55_0):
	return arg_55_0.GetMGHubData().ultimate

def var_0_0.getGameTotalTime(arg_56_0):
	return (arg_56_0.GetMGHubData().getConfig("reward_need"))

def var_0_0.updateDayNightUI(arg_57_0):
	arg_57_0.dayTimeFlag = Fushun3GameVo.GetTimeFlag()

	setActive(findTF(arg_57_0._tf, "bg/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0._tf, "bg/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "bg/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "bg/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "btnBack/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "btnBack/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "title/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "title/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "desc/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "desc/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "got/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "got/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "btnRule/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "btnRule/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "rightPanelBg/arrowUp/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "rightPanelBg/arrowUp/d"), arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "rightPanelBg/arrowDown/n"), not arg_57_0.dayTimeFlag)
	setActive(findTF(arg_57_0.menuUI, "rightPanelBg/arrowDown/d"), arg_57_0.dayTimeFlag)

	local var_57_0 = True

	setActive(findTF(arg_57_0.countUI, "bgCount/n"), not var_57_0)
	setActive(findTF(arg_57_0.countUI, "bgCount/d"), var_57_0)
	setActive(findTF(arg_57_0.leaveUI, "ad/img/n"), not var_57_0)
	setActive(findTF(arg_57_0.leaveUI, "ad/img/d"), var_57_0)
	setActive(findTF(arg_57_0.leaveUI, "ad/btnOk/n"), not var_57_0)
	setActive(findTF(arg_57_0.leaveUI, "ad/btnOk/d"), var_57_0)
	setActive(findTF(arg_57_0.leaveUI, "ad/desc/n"), not var_57_0)
	setActive(findTF(arg_57_0.leaveUI, "ad/desc/d"), var_57_0)
	setActive(findTF(arg_57_0.pauseUI, "ad/img/n"), not var_57_0)
	setActive(findTF(arg_57_0.pauseUI, "ad/img/d"), var_57_0)
	setActive(findTF(arg_57_0.pauseUI, "ad/btnOk/n"), not var_57_0)
	setActive(findTF(arg_57_0.pauseUI, "ad/btnOk/d"), var_57_0)
	setActive(findTF(arg_57_0.pauseUI, "ad/desc/n"), not var_57_0)
	setActive(findTF(arg_57_0.pauseUI, "ad/desc/d"), var_57_0)
	setActive(findTF(arg_57_0.settlementUI, "ad/bg/img/n"), not var_57_0)
	setActive(findTF(arg_57_0.settlementUI, "ad/bg/img/d"), var_57_0)
	setActive(findTF(arg_57_0.settlementUI, "ad/bg/imgScore/n"), not var_57_0)
	setActive(findTF(arg_57_0.settlementUI, "ad/bg/imgScore/d"), var_57_0)
	setActive(findTF(arg_57_0.settlementUI, "ad/bg/imgHigh/n"), not var_57_0)
	setActive(findTF(arg_57_0.settlementUI, "ad/bg/imgHigh/d"), var_57_0)

	local var_57_1 = var_57_0 and Color.New(1, 0.9686274509803922, 0.9215686274509803, 1) or Color.New(0.8549019607843137, 0.807843137254902, 1, 1)

	setTextColor(findTF(arg_57_0.settlementUI, "ad/currentText"), var_57_1)
	setTextColor(findTF(arg_57_0.settlementUI, "ad/highText"), var_57_1)
	setActive(findTF(arg_57_0.gameUI, "top/powerProgress/content/bg/n"), not var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/powerProgress/content/bg/d"), var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/powerProgress/full/n"), not var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/powerProgress/full/d"), var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/split/n"), not var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/split/d"), var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/scoreImg/n"), not var_57_0)
	setActive(findTF(arg_57_0.gameUI, "top/scoreImg/d"), var_57_0)

	local var_57_2 = var_57_0 and Color.New(0.9215686274509803, 0.8745098039215686, 0.7725490196078432, 1) or Color.New(0.8, 0.7372549019607844, 0.8392156862745098, 1)

	setTextColor(findTF(arg_57_0.gameUI, "top/score"), var_57_2)
	setActive(findTF(arg_57_0.gameUI, "topRight/btnStop/n"), not var_57_0)
	setActive(findTF(arg_57_0.gameUI, "topRight/btnStop/d"), var_57_0)
	setActive(findTF(arg_57_0.gameUI, "btnLeave/n"), not var_57_0)
	setActive(findTF(arg_57_0.gameUI, "btnLeave/d"), var_57_0)

	for iter_57_0 = 1, Fushun3GameConst.heart_num:
		local var_57_3 = findTF(arg_57_0.gameUI, "top/heart" .. iter_57_0 .. "")

		setActive(findTF(var_57_3, "img/n"), not var_57_0)
		setActive(findTF(var_57_3, "img/d"), var_57_0)
		setActive(findTF(var_57_3, "full/n"), not var_57_0)
		setActive(findTF(var_57_3, "full/d"), var_57_0)

def var_0_0.onTimer(arg_58_0):
	arg_58_0.gameStep()

def var_0_0.gameStep(arg_59_0):
	arg_59_0.gameOverTime = arg_59_0.gameOverTime + Time.deltaTime
	arg_59_0.gameTime = arg_59_0.gameTime - Time.deltaTime

	if arg_59_0.gameTime < 0:
		arg_59_0.gameTime = 0

	arg_59_0.gameStepTime = arg_59_0.gameStepTime + Time.deltaTime

	if arg_59_0.gameLevelTime > 0:
		arg_59_0.gameLevelTime = arg_59_0.gameLevelTime - Time.deltaTime

		if arg_59_0.gameLevelTime <= 0:
			arg_59_0.gameLevelTime = Fushun3GameConst.level_time

			arg_59_0.platformController.levelUp()

	arg_59_0.rectCollider.step()
	arg_59_0.platformController.step()
	arg_59_0.sceneController.step()
	arg_59_0.charController.step()
	arg_59_0.itemController.step()
	arg_59_0.bgController.step()
	arg_59_0.monsterController.step()
	arg_59_0.effectController.step()
	arg_59_0.updateGameUI()

	if arg_59_0.gameTime <= 0:
		arg_59_0.onGameOver()

		return

def var_0_0.timerStart(arg_60_0):
	if not arg_60_0.timer.running:
		arg_60_0.timer.Start()

def var_0_0.timerStop(arg_61_0):
	if arg_61_0.timer.running:
		arg_61_0.timer.Stop()

def var_0_0.updateGameUI(arg_62_0):
	local var_62_0 = arg_62_0.charController.getHeart()

	for iter_62_0 = 1, #arg_62_0.hearts:
		local var_62_1 = arg_62_0.hearts[iter_62_0]

		if iter_62_0 <= var_62_0:
			setActive(var_62_1, True)
		else
			setActive(var_62_1, False)

	setText(arg_62_0.scoreTf, arg_62_0.scoreNum)
	setText(arg_62_0.gameTimeS, math.ceil(arg_62_0.gameTime))

def var_0_0.addScore(arg_63_0, arg_63_1):
	arg_63_0.scoreNum = arg_63_0.scoreNum + arg_63_1

	if arg_63_0.scoreNum < 0:
		arg_63_0.scoreNum = 0

def var_0_0.onControllerCallback(arg_64_0, arg_64_1, arg_64_2):
	if arg_64_1 == Fushun3GameEvent.catch_item_call:
		local var_64_0 = arg_64_2.data

		if var_64_0.type == Fushun3GameConst.item_type_score:
			arg_64_0.addScore(var_64_0.score)
			arg_64_0.charController.addPower(var_64_0.score)
		else
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_6)
			arg_64_0.charController.setBuff(var_64_0)

def var_0_0.onGameOver(arg_65_0):
	if arg_65_0.settlementFlag:
		return

	arg_65_0.timerStop()

	arg_65_0.settlementFlag = True

	setActive(arg_65_0.clickMask, True)
	LeanTween.delayedCall(go(arg_65_0._tf), 1, System.Action(function()
		arg_65_0.settlementFlag = False
		arg_65_0.gameStartFlag = False

		setActive(arg_65_0.clickMask, False)
		arg_65_0.showSettlement()))
	pg.m02.sendNotification(GAME.MINI_GAME_TIME, {
		id = arg_65_0.GetMGData().id,
		time = math.ceil(arg_65_0.gameOverTime)
	})

def var_0_0.showSettlement(arg_67_0):
	setActive(arg_67_0.settlementUI, True)
	GetComponent(findTF(arg_67_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_67_0 = arg_67_0.GetMGData().GetRuntimeData("elements")
	local var_67_1 = arg_67_0.scoreNum
	local var_67_2 = var_67_0 and #var_67_0 > 0 and var_67_0[1] or 0

	setActive(findTF(arg_67_0.settlementUI, "ad/new"), var_67_2 < var_67_1)

	if var_67_2 <= var_67_1:
		var_67_2 = var_67_1

		arg_67_0.StoreDataToServer({
			var_67_2
		})

	local var_67_3 = findTF(arg_67_0.settlementUI, "ad/highText")
	local var_67_4 = findTF(arg_67_0.settlementUI, "ad/currentText")

	setText(var_67_3, var_67_2)
	setText(var_67_4, var_67_1)

	if arg_67_0.getGameTimes() and arg_67_0.getGameTimes() > 0:
		arg_67_0.sendSuccessFlag = True

		arg_67_0.SendSuccess(0)

def var_0_0.resumeGame(arg_68_0):
	arg_68_0.gameStop = False

	setActive(arg_68_0.leaveUI, False)
	arg_68_0.timerStart()

def var_0_0.stopGame(arg_69_0):
	arg_69_0.gameStop = True

	arg_69_0.timerStop()

def var_0_0.onBackPressed(arg_70_0):
	if not arg_70_0.gameStartFlag:
		arg_70_0.emit(var_0_0.ON_BACK_PRESSED)
	else
		if arg_70_0.settlementFlag:
			return

		if isActive(arg_70_0.pauseUI):
			setActive(arg_70_0.pauseUI, False)

		arg_70_0.stopGame()
		setActive(arg_70_0.leaveUI, True)

def var_0_0.willExit(arg_71_0):
	if arg_71_0.charController:
		arg_71_0.charController.dispose()

	if arg_71_0.handle:
		UpdateBeat.RemoveListener(arg_71_0.handle)

	if arg_71_0._tf and LeanTween.isTweening(go(arg_71_0._tf)):
		LeanTween.cancel(go(arg_71_0._tf))

	if arg_71_0.timer and arg_71_0.timer.running:
		arg_71_0.timer.Stop()

	if arg_71_0.atkDelegate:
		ClearEventTrigger(arg_71_0.atkDelegate)

	if arg_71_0.jumpDelegate:
		ClearEventTrigger(arg_71_0.jumpDelegate)

	Time.timeScale = 1
	arg_71_0.timer = None

	arg_71_0.rectCollider.clear()

return var_0_0
