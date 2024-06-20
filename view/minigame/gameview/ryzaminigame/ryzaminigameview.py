local var_0_0 = class("RyzaMiniGameView", import("view.miniGame.BaseMiniGameView"))

var_0_0.EVENT_CREATE = "RyzaMiniGameView.EVENT_CREATE"
var_0_0.EVENT_DESTROY = "RyzaMiniGameView.EVENT_DESTROY"
var_0_0.EVENT_FINISH = "RyzaMiniGameView.EVENT_FINISH"
var_0_0.EVENT_WINDOW_FOCUS = "RyzaMiniGameView.EVENT_WINDOW_FOCUS"
var_0_0.EVENT_STATUS_SYNC = "RyzaMiniGameView.EVENT_STATUS_SYNC"
var_0_0.EVENT_UPDATE_HIDE = "RyzaMiniGameView.EVENT_UPDATE_HIDE"

def var_0_0.getUIName(arg_1_0):
	return "RyzaMiniGameUI"

def var_0_0.didEnter(arg_2_0):
	arg_2_0.initTimer()
	arg_2_0.initUI()
	arg_2_0.initGameUI()
	onNextTick(function()
		arg_2_0.openUI("main"))

local function var_0_1(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0.GetComponentsInChildren(typeof(Animator), True)

	for iter_4_0 = 0, var_4_0.Length - 1:
		var_4_0[iter_4_0].speed = arg_4_1

def var_0_0.openUI(arg_5_0, arg_5_1):
	if arg_5_0.status:
		setActive(arg_5_0.rtTitlePage.Find(arg_5_0.status), False)

	if arg_5_1:
		setActive(arg_5_0.rtTitlePage.Find(arg_5_1), True)

	arg_5_0.status = arg_5_1

	switch(arg_5_1, {
		def main:()
			arg_5_0.updateMainUI(),
		def pause:()
			arg_5_0.pauseGame(),
		def exit:()
			arg_5_0.pauseGame(),
		def result:()
			local var_9_0 = arg_5_0.GetMGData().GetRuntimeData("elements")
			local var_9_1 = arg_5_0.scoreNum
			local var_9_2 = var_9_0 and #var_9_0 > 0 and var_9_0[1] or 0
			local var_9_3 = arg_5_0.rtTitlePage.Find("result")

			setActive(var_9_3.Find("window/now/new"), var_9_2 < var_9_1)

			if var_9_2 <= var_9_1:
				var_9_2 = var_9_1

				arg_5_0.StoreDataToServer({
					var_9_2
				})

			setText(var_9_3.Find("window/high/Text"), var_9_2)
			setText(var_9_3.Find("window/now/Text"), var_9_1)

			local var_9_4 = arg_5_0.GetMGHubData()

			if arg_5_0.stageIndex == var_9_4.usedtime + 1 and var_9_4.count > 0:
				arg_5_0.SendSuccess(0)
	})

def var_0_0.updateMainUI(arg_10_0):
	local var_10_0 = arg_10_0.GetMGHubData()
	local var_10_1 = var_10_0.getConfig("reward_need")
	local var_10_2 = var_10_0.usedtime
	local var_10_3 = var_10_2 + var_10_0.count
	local var_10_4 = var_10_2 == var_10_1 and 8 or math.min(var_10_0.usedtime + 1, var_10_3)
	local var_10_5 = arg_10_0.itemList.container
	local var_10_6 = var_10_5.childCount

	for iter_10_0 = 1, var_10_6:
		local var_10_7 = {}

		if iter_10_0 <= var_10_2:
			var_10_7.finish = True
		elif iter_10_0 <= var_10_3:
			-- block empty
		elif var_10_2 == var_10_1:
			var_10_7.finish = False
			var_10_7.lock = False
		else
			var_10_7.lock = True

		local var_10_8 = var_10_5.GetChild(iter_10_0 - 1)

		setActive(var_10_8.Find("finish"), var_10_7.finish)
		setActive(var_10_8.Find("lock"), var_10_7.lock)
		setToggleEnabled(var_10_8, iter_10_0 <= var_10_4)
		triggerToggle(var_10_8, iter_10_0 == var_10_4)

	local var_10_9 = var_10_5.GetChild(0).anchoredPosition.y - var_10_5.GetChild(var_10_4 - 1).anchoredPosition.y
	local var_10_10 = var_10_5.rect.height
	local var_10_11 = var_10_5.GetComponent(typeof(ScrollRect)).viewport.rect.height
	local var_10_12 = math.clamp(var_10_9, 0, var_10_10 - var_10_11) / (var_10_10 - var_10_11)

	scrollTo(var_10_5, None, 1 - var_10_12)
	setActive(arg_10_0.rtTitlePage.Find("main/tip/Image"), var_10_2 == var_10_1)
	arg_10_0.checkGet()

	if var_10_2 == 1 and var_10_4 == 2:
		scrollTo(var_10_5, None, 1)
		pg.NewGuideMgr.GetInstance().Play("Ryza_MiniGame")
	elif PlayerPrefs.GetInt("ryza_minigame_help", 0) == 0:
		triggerButton(arg_10_0.rtTitlePage.Find("main/btn_rule"))

def var_0_0.checkGet(arg_11_0):
	local var_11_0 = arg_11_0.GetMGHubData()

	if var_11_0.ultimate == 0:
		if var_11_0.usedtime < var_11_0.getConfig("reward_need"):
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_11_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})

def var_0_0.initUI(arg_12_0):
	arg_12_0.rtTitlePage = arg_12_0._tf.Find("TitlePage")

	local var_12_0 = arg_12_0.rtTitlePage.Find("main")

	onButton(arg_12_0, var_12_0.Find("btn_back"), function()
		arg_12_0.closeView(), SFX_CANCEL)
	onButton(arg_12_0, var_12_0.Find("btn_rule"), function()
		PlayerPrefs.SetInt("ryza_minigame_help", 1)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.ryza_mini_game.tip
		}), SFX_PANEL)

	local var_12_1 = arg_12_0.GetMGData().GetSimpleValue("story")

	onButton(arg_12_0, var_12_0.Find("btn_start"), function()
		local var_15_0 = {}
		local var_15_1 = checkExist(var_12_1, {
			arg_12_0.stageIndex
		}, {
			1
		})

		if var_15_1:
			table.insert(var_15_0, function(arg_16_0)
				pg.NewStoryMgr.GetInstance().Play(var_15_1, arg_16_0))

		seriesAsync(var_15_0, function()
			arg_12_0.readyStart()), SFX_CONFIRM)

	arg_12_0.stageIndex = 0

	local var_12_2 = pg.mini_game[arg_12_0.GetMGData().id].simple_config_data.drop_ids
	local var_12_3 = var_12_0.Find("side_panel/award/content")

	arg_12_0.itemList = UIItemList.New(var_12_3, var_12_3.GetChild(0))

	arg_12_0.itemList.make(function(arg_18_0, arg_18_1, arg_18_2)
		arg_18_1 = arg_18_1 + 1

		if arg_18_0 == UIItemList.EventUpdate:
			local var_18_0 = arg_18_2.Find("IconTpl")
			local var_18_1 = {}

			var_18_1.type, var_18_1.id, var_18_1.count = unpack(var_12_2[arg_18_1])

			updateDrop(var_18_0, var_18_1)
			onButton(arg_12_0, var_18_0, function()
				arg_12_0.emit(var_0_0.ON_DROP, var_18_1), SFX_PANEL)
			onToggle(arg_12_0, arg_18_2, function(arg_20_0)
				if arg_20_0:
					arg_12_0.stageIndex = arg_18_1))
	arg_12_0.itemList.align(#var_12_2)

	local var_12_4 = arg_12_0.GetMGHubData().getConfig("reward_need")

	setActive(var_12_3.GetChild(var_12_4), True)
	onToggle(arg_12_0, var_12_3.GetChild(var_12_4), function(arg_21_0)
		if arg_21_0:
			arg_12_0.stageIndex = 0)
	arg_12_0.rtTitlePage.Find("countdown").Find("bg/Image").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_12_0.openUI()
		arg_12_0.startGame())

	local var_12_5 = arg_12_0.rtTitlePage.Find("pause")

	onButton(arg_12_0, var_12_5.Find("window/btn_confirm"), function()
		arg_12_0.openUI()
		arg_12_0.resumeGame(), SFX_CONFIRM)

	local var_12_6 = arg_12_0.rtTitlePage.Find("exit")

	onButton(arg_12_0, var_12_6.Find("window/btn_cancel"), function()
		arg_12_0.openUI()
		arg_12_0.resumeGame(), SFX_CANCEL)
	onButton(arg_12_0, var_12_6.Find("window/btn_confirm"), function()
		arg_12_0.openUI()
		arg_12_0.resumeGame()
		arg_12_0.endGame(), SFX_CONFIRM)

	local var_12_7 = arg_12_0.rtTitlePage.Find("result")

	onButton(arg_12_0, var_12_7.Find("window/btn_finish"), function()
		setActive(arg_12_0._tf.Find("Viewport"), False)
		arg_12_0.openUI("main")
		pg.CriMgr.GetInstance().PlayBGM("ryza-5"), SFX_CONFIRM)

def var_0_0.initGameUI(arg_27_0):
	arg_27_0.uiMgr = pg.UIMgr.GetInstance()
	arg_27_0.rtResource = arg_27_0._tf.Find("Resource")
	arg_27_0.rtMain = arg_27_0._tf.Find("Viewport/MainContent")
	arg_27_0.rtPlane = arg_27_0.rtMain.Find("plane")
	arg_27_0.sprites = {}

	eachChild(arg_27_0.rtPlane, function(arg_28_0)
		arg_27_0.sprites[arg_28_0.name] = getImageSprite(arg_28_0))

	arg_27_0.rtController = arg_27_0._tf.Find("Controller")
	arg_27_0.rtJoyStick = arg_27_0.rtController.Find("bottom/handle_stick")

	onButton(arg_27_0, arg_27_0.rtController.Find("bottom/btn_bomb"), function()
		arg_27_0.responder.RyzaBomb())

	arg_27_0.rtScore = arg_27_0.rtController.Find("top/title/SCORE/Text")
	arg_27_0.rtTime = arg_27_0.rtController.Find("top/title/TIME/Text")

	onButton(arg_27_0, arg_27_0.rtController.Find("top/btn_back"), function()
		arg_27_0.openUI("exit"), SFX_PANEL)
	onButton(arg_27_0, arg_27_0.rtController.Find("top/btn_pause"), function()
		arg_27_0.openUI("pause"), SFX_PANEL)

	arg_27_0.rtStatus = arg_27_0.rtController.Find("bottom/status")
	arg_27_0.rtRyzaHP = arg_27_0.rtController.Find("top/title/HP/heart")
	arg_27_0.rtControllerUI = arg_27_0.rtController.Find("UI")

	eachChild(arg_27_0.rtControllerUI, function(arg_32_0)
		arg_27_0["tplUI" .. arg_32_0.name] = arg_32_0

		setActive(arg_32_0, False))

	arg_27_0.responder = Responder.New(arg_27_0)

	arg_27_0.bind(var_0_0.EVENT_CREATE, function(arg_33_0, ...)
		arg_27_0.CreateReactor(...))
	arg_27_0.bind(var_0_0.EVENT_DESTROY, function(arg_34_0, ...)
		arg_27_0.DestroyReactor(...))
	arg_27_0.bind(var_0_0.EVENT_FINISH, function(arg_35_0, arg_35_1)
		arg_27_0.endGame(arg_35_1))
	arg_27_0.bind(var_0_0.EVENT_WINDOW_FOCUS, function(arg_36_0, arg_36_1)
		setAnchoredPosition(arg_27_0.rtMain, {
			x = math.clamp(-arg_36_1.x, -arg_27_0.buffer.x, arg_27_0.buffer.x),
			y = math.clamp(-arg_36_1.y, -arg_27_0.buffer.y - 48, arg_27_0.buffer.y - 48)
		}))
	arg_27_0.bind(var_0_0.EVENT_STATUS_SYNC, function(arg_37_0, ...)
		arg_27_0.updateControllerStatus(...)
		arg_27_0.popRyzaUI(...))
	arg_27_0.bind(var_0_0.EVENT_UPDATE_HIDE, function(arg_38_0, arg_38_1, arg_38_2)
		if isa(arg_38_1, MoveEnemy):
			GetOrAddComponent(arg_27_0.reactorUIs[arg_38_1], typeof(CanvasGroup)).alpha = arg_38_2 and 0 or 1)

def var_0_0.initTimer(arg_39_0):
	arg_39_0.timer = Timer.New(function()
		arg_39_0.onTimer(), RyzaMiniGameConfig.TIME_INTERVAL, -1)

def var_0_0.readyStart(arg_41_0):
	arg_41_0.resetGame()
	setActive(arg_41_0._tf.Find("Viewport"), True)
	var_0_1(arg_41_0.rtMain, 1)
	arg_41_0.initConfig()
	arg_41_0.buildMap()
	arg_41_0.initController()
	arg_41_0.openUI("countdown")

def var_0_0.startGame(arg_42_0):
	pg.CriMgr.GetInstance().PlayBGM("ryza-az-battle")

	arg_42_0.gameStartFlag = True

	arg_42_0.startTimer()

def var_0_0.endGame(arg_43_0, arg_43_1):
	if arg_43_1:
		arg_43_0.scoreNum = arg_43_0.scoreNum + RyzaMiniGameConfig.GetPassGamePoint(arg_43_0.countTime)

		setText(arg_43_0.rtScore, arg_43_0.scoreNum)

	arg_43_0.gameEndFlag = True

	arg_43_0.stopTimer()
	arg_43_0.openUI("result")

def var_0_0.pauseGame(arg_44_0):
	arg_44_0.gamePause = True

	arg_44_0.stopTimer()
	arg_44_0.pauseManagedTween()

def var_0_0.resumeGame(arg_45_0):
	arg_45_0.gamePause = False

	arg_45_0.startTimer()
	arg_45_0.resumeManagedTween()

def var_0_0.resetGame(arg_46_0):
	arg_46_0.gameStartFlag = False
	arg_46_0.gamePause = False
	arg_46_0.gameEndFlag = False
	arg_46_0.scoreNum = 0
	arg_46_0.countTime = 0

	arg_46_0.responder.reset()

	if arg_46_0.reactorUIs:
		for iter_46_0, iter_46_1 in pairs(arg_46_0.reactorUIs):
			Destroy(iter_46_1)

	arg_46_0.reactorUIs = {}

def var_0_0.initConfig(arg_47_0):
	local var_47_0 = arg_47_0.stageIndex == 0 and math.random(7) or arg_47_0.stageIndex
	local var_47_1 = 0
	local var_47_2 = underscore.rest(RyzaMiniGameConfig.ENEMY_TYPE_LIST, 1)
	local var_47_3 = {}
	local var_47_4 = pg.MiniGameTileMgr.GetInstance().getDataLayers("BoomGame", "BoomLevel_" .. var_47_0)

	arg_47_0.config = {}
	arg_47_0.config.mapSize = NewPos(var_47_4[1].width, var_47_4[1].height)
	arg_47_0.config.reactorList = {}

	for iter_47_0, iter_47_1 in ipairs(var_47_4):
		for iter_47_2, iter_47_3 in ipairs(iter_47_1.layer):
			if iter_47_3.item:
				local var_47_5 = {
					name = iter_47_3.item
				}

				if arg_47_0.stageIndex == 0 and isa(RyzaMiniGameConfig.CreateInfo(var_47_5.name), TargetMove):
					if var_47_5.name == "Ryza":
						-- block empty
					else
						local var_47_6 = math.random(#var_47_2)

						if string.find(var_47_2[var_47_6], "BOSS_"):
							var_47_5.name = table.remove(var_47_2, var_47_6)
							var_47_1 = var_47_1 + 1

							if var_47_1 == RyzaMiniGameConfig.FREE_MAP_BOSS_LIMIT[var_47_0]:
								while string.find(var_47_2[#var_47_2], "BOSS_"):
									table.remove(var_47_2)
						else
							var_47_5.name = var_47_2[var_47_6]

						table.insert(var_47_3, #arg_47_0.config.reactorList + 1)
				elif iter_47_3.prop:
					for iter_47_4, iter_47_5 in pairs(iter_47_3.prop):
						var_47_5[iter_47_4] = iter_47_5

				var_47_5.pos = {
					(iter_47_3.index - 1) % arg_47_0.config.mapSize.x,
					math.floor((iter_47_3.index - 1) / arg_47_0.config.mapSize.x)
				}

				table.insert(arg_47_0.config.reactorList, var_47_5)

	if arg_47_0.stageIndex == 0 and var_47_1 == 0:
		local var_47_7 = math.random(#var_47_3)
		local var_47_8 = arg_47_0.config.reactorList[var_47_7]

		arg_47_0.config.reactorList[var_47_7] = {
			name = "BOSS_" .. var_47_8.name,
			pos = var_47_8.pos
		}

def var_0_0.buildMap(arg_48_0):
	setSizeDelta(arg_48_0.rtMain, arg_48_0.config.mapSize * 32)
	eachChild(arg_48_0.rtMain.Find("bg/NW"), function(arg_49_0)
		setActive(arg_49_0, arg_49_0.name == tostring(math.floor((arg_48_0.stageIndex - 1) % 8 / 2) + 1)))

	local var_48_0 = arg_48_0._tf.Find("Viewport").rect
	local var_48_1 = arg_48_0.rtMain.rect

	arg_48_0.buffer = NewPos(math.max(var_48_1.width + 256 - var_48_0.width, 0), math.max(var_48_1.height + 160 - var_48_0.height, 0)) * 0.5

	local var_48_2 = Time.realtimeSinceStartup
	local var_48_3 = arg_48_0.config.mapSize.x
	local var_48_4 = arg_48_0.config.mapSize.y
	local var_48_5 = UIItemList.New(arg_48_0.rtPlane, arg_48_0.rtPlane.GetChild(0))

	var_48_5.make(function(arg_50_0, arg_50_1, arg_50_2)
		if arg_50_0 == UIItemList.EventUpdate:
			local var_50_0 = arg_50_1 % var_48_4
			local var_50_1 = math.floor(arg_50_1 / var_48_4)

			arg_50_2.name = var_50_0 .. "_" .. var_50_1

			if math.random() < RyzaMiniGameConfig.GRASS_CHAGNE_RATE:
				setImageAlpha(arg_50_2, 1)

				local var_50_2 = "Grass_" .. 3 + math.random(3)

				setImageSprite(arg_50_2, arg_48_0.sprites[var_50_2])
			else
				setImageAlpha(arg_50_2, 0))
	var_48_5.align(var_48_3 * var_48_4)
	arg_48_0.soilMapPartition(Vector2.zero, arg_48_0.config.mapSize)

	for iter_48_0, iter_48_1 in ipairs(arg_48_0.config.reactorList):
		arg_48_0.CreateReactor(iter_48_1)

def var_0_0.initController(arg_51_0):
	setText(arg_51_0.rtScore, arg_51_0.scoreNum)
	setText(arg_51_0.rtTime, string.format("%02d.%02d", math.floor(arg_51_0.countTime / 60), math.floor(arg_51_0.countTime % 60)))

	local var_51_0 = arg_51_0.responder.reactorRyza

	arg_51_0.updateControllerStatus(var_51_0, "hp", {
		num = var_51_0.hp
	})
	arg_51_0.updateControllerStatus(var_51_0, "bomb", {
		num = var_51_0.bomb
	})
	arg_51_0.updateControllerStatus(var_51_0, "power", {
		num = var_51_0.power
	})
	arg_51_0.updateControllerStatus(var_51_0, "speed", {
		num = var_51_0.speed
	})

def var_0_0.updateControllerStatus(arg_52_0, arg_52_1, arg_52_2, arg_52_3):
	local var_52_0 = arg_52_0.reactorUIs[arg_52_1]

	if isa(arg_52_1, MoveRyza):
		if arg_52_2 == "hp":
			eachChild(arg_52_0.rtRyzaHP, function(arg_53_0)
				setActive(arg_53_0.Find("active"), tonumber(arg_53_0.name) <= arg_52_3.num))
		else
			eachChild(arg_52_0.rtStatus.Find(string.upper(arg_52_2) .. "/bit"), function(arg_54_0)
				setActive(arg_54_0, tonumber(arg_54_0.name) <= arg_52_3.num))
	elif isa(arg_52_1, MoveEnemy):
		setSlider(var_52_0.Find("hp"), 0, arg_52_3.max, arg_52_3.num)

def var_0_0.popRyzaUI(arg_55_0, arg_55_1, arg_55_2, arg_55_3):
	if isa(arg_55_1, MoveRyza):
		local var_55_0 = arg_55_0.reactorUIs[arg_55_1]

		if arg_55_2 == "hp":
			local var_55_1 = var_55_0.Find("pop/hp_" .. (arg_55_3.delta > 0 and "up" or "down"))

			for iter_55_0 = 1, 2:
				setActive(var_55_1.Find(iter_55_0), iter_55_0 * iter_55_0 == arg_55_3.delta * arg_55_3.delta)

			setActive(var_55_1, False)
			setActive(var_55_1, True)
		else
			local var_55_2 = var_55_0.Find("pop/" .. arg_55_2 .. "_up")

			setActive(var_55_2, False)
			setActive(var_55_2, True)

def var_0_0.CreateReactor(arg_56_0, arg_56_1):
	local var_56_0, var_56_1, var_56_2 = RyzaMiniGameConfig.CreateInfo(arg_56_1.name)

	if not var_56_0:
		warning(arg_56_1.name)

		return

	local var_56_3 = var_56_0.New(arg_56_1, cloneTplTo(arg_56_0.rtResource.Find(var_56_1), arg_56_0.rtMain.Find(var_56_2)), arg_56_0.responder)

	if isa(var_56_3, MoveRyza):
		arg_56_0.reactorUIs[var_56_3] = cloneTplTo(arg_56_0.tplUIRyza, arg_56_0.rtControllerUI)

		eachChild(arg_56_0.reactorUIs[var_56_3].Find("pop"), function(arg_57_0)
			arg_57_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
				setActive(arg_57_0, False)))

		arg_56_0.reactorUIs[var_56_3].position = var_56_3._tf.position
	elif isa(var_56_3, MoveEnemy):
		arg_56_0.reactorUIs[var_56_3] = cloneTplTo(arg_56_0.tplUIEnemy, arg_56_0.rtControllerUI)

		setAnchoredPosition(arg_56_0.reactorUIs[var_56_3].Find("hp"), {
			y = var_56_3.GetUIHeight()
		})

		arg_56_0.reactorUIs[var_56_3].position = var_56_3._tf.position

def var_0_0.DestroyReactor(arg_59_0, arg_59_1, arg_59_2):
	if arg_59_0.reactorUIs[arg_59_1]:
		Destroy(arg_59_0.reactorUIs[arg_59_1])

		arg_59_0.reactorUIs[arg_59_1] = None

	arg_59_0.scoreNum = arg_59_0.scoreNum + arg_59_2

	setText(arg_59_0.rtScore, arg_59_0.scoreNum)

def var_0_0.soilMapPartition(arg_60_0, arg_60_1, arg_60_2):
	local var_60_0 = RyzaMiniGameConfig.SOIL_RANDOM_CONFIG
	local var_60_1 = math.floor(math.min(arg_60_2.x, arg_60_2.y) * (var_60_0.size_rate[1] + math.random() * (var_60_0.size_rate[2] - var_60_0.size_rate[1])))

	if var_60_1 < 2:
		return

	local var_60_2 = math.random(4) % 4

	arg_60_0.dealSoilMap(NewPos(arg_60_1.x + (var_60_2 % 2 > 0 and arg_60_2.x - var_60_1 or 0), arg_60_1.y + (var_60_2 > 1 and arg_60_2.y - var_60_1 or 0)), var_60_1)

	local var_60_3 = var_60_1 + math.ceil((arg_60_2.x - var_60_1) * var_60_0.spacer_rate)
	local var_60_4 = var_60_1 + math.ceil((arg_60_2.y - var_60_1) * var_60_0.spacer_rate)

	if arg_60_2.x > arg_60_2.y:
		arg_60_0.soilMapPartition(NewPos(arg_60_1.x + (var_60_2 % 2 > 0 and 0 or var_60_3), arg_60_1.y), NewPos(arg_60_2.x - var_60_3, arg_60_2.y))
		arg_60_0.soilMapPartition(NewPos(arg_60_1.x + (var_60_2 % 2 > 0 and arg_60_2.x - var_60_1 or 0), arg_60_1.y + (var_60_2 > 1 and 0 or var_60_4)), NewPos(var_60_1, arg_60_2.y - var_60_4))
	else
		arg_60_0.soilMapPartition(NewPos(arg_60_1.x + (var_60_2 % 2 > 0 and 0 or var_60_3), arg_60_1.y + (var_60_2 > 1 and arg_60_2.y - var_60_1 or 0)), NewPos(arg_60_2.x - var_60_3, var_60_1))
		arg_60_0.soilMapPartition(NewPos(arg_60_1.x, arg_60_1.y + (var_60_2 > 1 and 0 or var_60_4)), NewPos(arg_60_2.x, arg_60_2.y - var_60_4))

local var_0_2 = {
	{
		0,
		1
	},
	{
		1,
		0
	},
	{
		0,
		-1
	},
	{
		-1,
		0
	}
}
local var_0_3 = {
	{
		0,
		1
	},
	{
		1,
		0
	},
	{
		0,
		-1
	},
	{
		-1,
		0
	},
	{
		1,
		1
	},
	{
		1,
		-1
	},
	{
		-1,
		-1
	},
	{
		-1,
		1
	}
}

def var_0_0.dealSoilMap(arg_61_0, arg_61_1, arg_61_2):
	local var_61_0 = {}

	for iter_61_0 = 0, 3:
		table.insert(var_61_0, arg_61_1 + NewPos(iter_61_0 % 2 > 0 and arg_61_2 - 1 or 0, iter_61_0 > 1 and arg_61_2 - 1 or 0))

	local function var_61_1(arg_62_0)
		if arg_62_0.x < arg_61_1.x or arg_62_0.y < arg_61_1.y or arg_62_0.x >= arg_61_1.x + arg_61_2 or arg_62_0.y >= arg_61_1.y + arg_61_2:
			return False
		else
			return True

	local var_61_2 = {}

	local function var_61_3(arg_63_0)
		local var_63_0 = 0
		local var_63_1 = 1

		for iter_63_0, iter_63_1 in ipairs(var_0_3):
			local var_63_2 = arg_63_0 + NewPos(unpack(iter_63_1))

			if var_61_1(var_63_2) and defaultValue(var_61_2[var_63_2.x .. "_" .. var_63_2.y], True):
				var_63_0 = var_63_0 + var_63_1

			var_63_1 = var_63_1 + var_63_1

		return var_63_0

	local function var_61_4(arg_64_0)
		for iter_64_0, iter_64_1 in ipairs(var_0_3):
			local var_64_0 = arg_64_0 + NewPos(unpack(iter_64_1))

			if var_61_1(var_64_0) and defaultValue(var_61_2[var_64_0.x .. "_" .. var_64_0.y], True) and not RyzaMiniGameConfig.SOIL_SPRITES_DIC[var_61_3(var_64_0)]:
				return False

		return True

	local var_61_5 = 0
	local var_61_6 = RyzaMiniGameConfig.SOIL_RANDOM_CONFIG.cancel_rate
	local var_61_7
	local var_61_8 = 0

	while var_61_8 < #var_61_0:
		var_61_8 = var_61_8 + 1

		local var_61_9 = var_61_0[var_61_8]

		var_61_2[var_61_9.x .. "_" .. var_61_9.y] = False

		if math.random() < var_61_6[1] + var_61_6[2] * (1 - var_61_5 / arg_61_2 / arg_61_2) * (1 - var_61_5 / arg_61_2 / arg_61_2) and var_61_4(var_61_9):
			var_61_5 = var_61_5 + 1
		else
			var_61_2[var_61_9.x .. "_" .. var_61_9.y] = True

		for iter_61_1, iter_61_2 in ipairs(var_0_2):
			local var_61_10 = var_61_9 + NewPos(unpack(iter_61_2))

			if var_61_1(var_61_10) and var_61_2[var_61_10.x .. "_" .. var_61_10.y] == None:
				table.insert(var_61_0, var_61_10)

	local var_61_11 = arg_61_0.config.mapSize.x
	local var_61_12 = arg_61_0.config.mapSize.y

	for iter_61_3 = arg_61_1.x, arg_61_1.x + arg_61_2 - 1:
		for iter_61_4 = arg_61_1.y, arg_61_1.y + arg_61_2 - 1:
			if defaultValue(var_61_2[iter_61_3 .. "_" .. iter_61_4], True):
				local var_61_13 = RyzaMiniGameConfig.SOIL_SPRITES_DIC[var_61_3(NewPos(iter_61_3, iter_61_4))]

				assert(var_61_13)

				local var_61_14 = arg_61_0.rtPlane.GetChild(iter_61_4 * var_61_11 + iter_61_3)

				setImageAlpha(var_61_14, 1)
				setImageSprite(var_61_14, arg_61_0.sprites[var_61_13])

def var_0_0.startTimer(arg_65_0):
	if not arg_65_0.timer.running:
		arg_65_0.timer.Start()

	arg_65_0.uiMgr.AttachStickOb(arg_65_0.rtJoyStick)
	var_0_1(arg_65_0.rtMain, 1)

def var_0_0.stopTimer(arg_66_0):
	if arg_66_0.timer.running:
		arg_66_0.timer.Stop()

	arg_66_0.uiMgr.ClearStick()
	var_0_1(arg_66_0.rtMain, 0)

def var_0_0.onTimer(arg_67_0):
	arg_67_0.countTime = arg_67_0.countTime + RyzaMiniGameConfig.TIME_INTERVAL

	setText(arg_67_0.rtTime, string.format("%02d.%02d", math.floor(arg_67_0.countTime / 60), math.floor(arg_67_0.countTime % 60)))
	arg_67_0.responder.TimeFlow(RyzaMiniGameConfig.TIME_INTERVAL)

	for iter_67_0, iter_67_1 in pairs(arg_67_0.reactorUIs):
		iter_67_1.position = iter_67_0._tf.position

	local var_67_0 = arg_67_0.responder.GetJoyStick()

	if var_67_0.x != 0 or var_67_0.y != 0:
		local var_67_1 = arg_67_0.reactorUIs[arg_67_0.responder.reactorRyza].Find("dir")

		if var_67_0.x == 0:
			setLocalEulerAngles(var_67_1, {
				z = var_67_0.y > 0 and 270 or 90
			})
		else
			setLocalEulerAngles(var_67_1, {
				z = math.atan2(-var_67_0.y, var_67_0.x) / math.pi * 180
			})

def var_0_0.OnApplicationPaused(arg_68_0, arg_68_1):
	if arg_68_1:
		-- block empty

def var_0_0.onBackPressed(arg_69_0):
	switch(arg_69_0.status, {
		def main:()
			var_0_0.super.onBackPressed(arg_69_0),
		def countdown:()
			return,
		def pause:()
			arg_69_0.openUI()
			arg_69_0.resumeGame(),
		def exit:()
			arg_69_0.openUI()
			arg_69_0.resumeGame(),
		def result:()
			return
	}, function()
		assert(arg_69_0.gameStartFlag)
		arg_69_0.openUI("pause"))

def var_0_0.willExit(arg_76_0):
	return

return var_0_0