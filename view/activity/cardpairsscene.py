local var_0_0 = class("CardPairsScene", import("..base.BaseUI"))

var_0_0.CARD_NUM = 18
var_0_0.GAME_STATE_BEGIN = 0
var_0_0.GAME_STATE_GAMING = 1
var_0_0.GAME_STATE_END = 2
var_0_0.config_init = False

def var_0_0.getUIName(arg_1_0):
	return "CardPairsUI"

def var_0_0.setPlayerData(arg_2_0, arg_2_1):
	arg_2_0.playerData = arg_2_1

def var_0_0.setActivityData(arg_3_0, arg_3_1):
	arg_3_0.activityData = arg_3_1

	if not arg_3_0.config_init:
		local var_3_0 = arg_3_0.activityData.getConfig("config_client")[2]

		if var_3_0:
			arg_3_0.firstShowingTime = var_3_0.firstShowingTime
			arg_3_0.showingTime = var_3_0.showingTime
			arg_3_0.aniTime = var_3_0.aniTime
			arg_3_0.cardEffectTimesMax = arg_3_0.activityData.getConfig("config_data")[4]
		else
			arg_3_0.firstShowingTime = 2
			arg_3_0.showingTime = 0.3
			arg_3_0.aniTime = 0.2
			arg_3_0.cardEffectTimesMax = 7

		CardPairsCard.ANI_TIME = arg_3_0.aniTime
		arg_3_0.config_init = True

	arg_3_0.updateTimes()

	if arg_3_0.activityData.data4 <= 0:
		setText(arg_3_0.bestTxt, "--'--'--")
	else
		setText(arg_3_0.bestTxt, arg_3_0.getTimeFormat(arg_3_0.activityData.data4))

def var_0_0.checkActivityEnd(arg_4_0):
	return

def var_0_0.init(arg_5_0):
	arg_5_0.backBtn = arg_5_0.findTF("top/back", arg_5_0._tf)
	arg_5_0.cardTpl = arg_5_0.findTF("res/card", arg_5_0._tf)
	arg_5_0.cardCon = arg_5_0.findTF("card_con/layout", arg_5_0._tf)
	arg_5_0.pics = arg_5_0.findTF("res/pics", arg_5_0._tf)
	arg_5_0.helpBtn = arg_5_0.findTF("top/help_btn", arg_5_0._tf)
	arg_5_0.timesTxt = arg_5_0.findTF("num_txt", arg_5_0._tf)
	arg_5_0.timeTxt = arg_5_0.findTF("time_txt", arg_5_0._tf)
	arg_5_0.bestTxt = arg_5_0.findTF("best_txt", arg_5_0._tf)
	arg_5_0.maskBtn = arg_5_0.findTF("mask_btn", arg_5_0._tf)
	arg_5_0.endTips = arg_5_0.findTF("end_tips", arg_5_0._tf)

	arg_5_0.hideChild(arg_5_0.findTF("res", arg_5_0._tf))

def var_0_0.didEnter(arg_6_0):
	onButton(arg_6_0, arg_6_0.backBtn, function()
		arg_6_0.emit(var_0_0.ON_BACK), SOUND_BACK)
	onButton(arg_6_0, arg_6_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("card_pairs_help_tip")
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.maskBtn, function()
		if arg_6_0.lastTimes > 0:
			arg_6_0.gameInit()
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("card_pairs_tips"),
				def onYes:()
					arg_6_0.gameInit()
			}), SFX_PANEL)

	arg_6_0.updateTimer = Timer.New(function()
		arg_6_0.updateTimes(), 10, -1)

	arg_6_0.updateTimer.Start()

	arg_6_0.showCards = {}
	arg_6_0.showingCards = {}
	arg_6_0.cardList = {}
	arg_6_0.cardUIList = UIItemList.New(arg_6_0.cardCon, arg_6_0.cardTpl)

	arg_6_0.cardUIList.make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate:
			local var_12_0 = arg_6_0.cardList[arg_12_1 + 1]

			if var_12_0 != None:
				var_12_0.initCard(arg_6_0.cardIndexList[arg_12_1 + 1][1])
			else
				table.insert(arg_6_0.cardList, arg_12_1 + 1, CardPairsCard.New(arg_12_2, arg_6_0.pics, arg_6_0.cardIndexList[arg_12_1 + 1][1], function(arg_13_0)
					if arg_6_0.gameState == arg_6_0.GAME_STATE_GAMING:
						if arg_6_0.isFrist:
							arg_6_0.isFrist = False
							arg_6_0.beginTime = Time.realtimeSinceStartup
							arg_6_0.countTimer = Timer.New(function()
								local var_14_0 = math.floor((Time.realtimeSinceStartup - arg_6_0.beginTime) * 1000)

								arg_6_0.setTimeTxt(var_14_0), 0.12, -1)

							arg_6_0.countTimer.Start()

						if arg_13_0.canClick and arg_13_0.enable and #arg_6_0.showCards < 2:
							arg_13_0.aniShowBack(arg_13_0.cardState == CardPairsCard.CARD_STATE_BACK), function(arg_15_0, arg_15_1)
					if arg_6_0.gameState == arg_6_0.GAME_STATE_GAMING:
						arg_15_0.setEnable(False)

						if arg_15_1:
							table.insert(arg_6_0.showCards, #arg_6_0.showCards + 1, arg_15_0)

							if #arg_6_0.showCards == 2:
								arg_6_0.setAllCardEnale(False), function(arg_16_0, arg_16_1)
					if arg_6_0.gameState == arg_6_0.GAME_STATE_GAMING:
						if arg_16_1:
							arg_16_0.setOutline(True)
							table.insert(arg_6_0.showingCards, #arg_6_0.showingCards + 1, arg_16_0)

							if #arg_6_0.showingCards % 2 == 0:
								local var_16_0 = #arg_6_0.showingCards
								local var_16_1 = #arg_6_0.showingCards - 1
								local var_16_2 = arg_6_0.showingCards[var_16_1]
								local var_16_3 = arg_6_0.showingCards[var_16_0]

								table.remove(arg_6_0.showingCards, var_16_0)
								table.remove(arg_6_0.showingCards, var_16_1)

								if var_16_2.getCardIndex() == var_16_3.getCardIndex():
									var_16_2.setClear(True)
									var_16_3.setClear(True)

									arg_6_0.curValue = arg_6_0.curValue + 2

									if arg_6_0.curValue >= arg_6_0.CARD_NUM:
										arg_6_0.gameEndHandler()
									else
										for iter_16_0 = #arg_6_0.showCards, 0, -1:
											table.remove(arg_6_0.showCards, iter_16_0)

										arg_6_0.setAllCardEnale(True)
								else
									var_16_2.aniShowBack(False, False, arg_6_0.showingTime)
									var_16_3.aniShowBack(False, False, arg_6_0.showingTime)
						else
							table.remove(arg_6_0.showCards, #arg_6_0.showCards)
							arg_6_0.setAllCardEnale(#arg_6_0.showingCards == 0))))

	if not arg_6_0.tryFirstPlayStory():
		triggerButton(arg_6_0.maskBtn)

def var_0_0.setAllCardEnale(arg_17_0, arg_17_1):
	for iter_17_0, iter_17_1 in pairs(arg_17_0.cardList):
		iter_17_1.setEnable(arg_17_1)

def var_0_0.setTimeTxt(arg_18_0, arg_18_1):
	setText(arg_18_0.timeTxt, arg_18_0.getTimeFormat(arg_18_1))

def var_0_0.getTimeFormat(arg_19_0, arg_19_1):
	local var_19_0 = math.floor(arg_19_1 / 60000)

	var_19_0 = var_19_0 >= 10 and var_19_0 or "0" .. var_19_0

	local var_19_1 = math.floor(arg_19_1 % 60000 / 1000)

	var_19_1 = var_19_1 >= 10 and var_19_1 or "0" .. var_19_1

	local var_19_2 = math.floor(arg_19_1 % 1000 / 10)

	var_19_2 = var_19_2 >= 10 and var_19_2 or "0" .. var_19_2

	return var_19_0 .. "'" .. var_19_1 .. "'" .. var_19_2

def var_0_0.updateTimes(arg_20_0):
	local var_20_0 = os.difftime(pg.TimeMgr.GetInstance().GetServerTime(), arg_20_0.activityData.data3)
	local var_20_1 = math.ceil(var_20_0 / 86400)

	var_20_1 = var_20_1 < 0 and 0 or var_20_1
	var_20_1 = var_20_1 > arg_20_0.cardEffectTimesMax and arg_20_0.cardEffectTimesMax or var_20_1
	arg_20_0.lastTimes = var_20_1 - arg_20_0.activityData.data2

	setText(arg_20_0.timesTxt, arg_20_0.lastTimes >= 0 and arg_20_0.lastTimes or 0)

def var_0_0.gameInit(arg_21_0):
	setActive(arg_21_0.maskBtn, False)
	setActive(arg_21_0.endTips, False)

	arg_21_0.isFrist = True
	arg_21_0.curValue = 0
	arg_21_0.showCards = {}
	arg_21_0.showingCards = {}
	arg_21_0.cardIndexList = {}

	for iter_21_0 = 1, arg_21_0.CARD_NUM / 2:
		table.insert(arg_21_0.cardIndexList, #arg_21_0.cardIndexList + 1, {
			iter_21_0,
			math.random(0, 100)
		})
		table.insert(arg_21_0.cardIndexList, #arg_21_0.cardIndexList + 1, {
			iter_21_0,
			math.random(0, 100)
		})

	table.sort(arg_21_0.cardIndexList, function(arg_22_0, arg_22_1)
		if arg_22_0[2] > arg_22_1[2]:
			return True

		return False)
	arg_21_0.setTimeTxt(0)
	arg_21_0.clearCountTimer()
	arg_21_0.clearAllCard()
	arg_21_0.cardUIList.align(arg_21_0.CARD_NUM)

	arg_21_0.gameState = arg_21_0.GAME_STATE_BEGIN

	arg_21_0.checkGameState()

def var_0_0.checkGameState(arg_23_0):
	if arg_23_0.gameState == arg_23_0.GAME_STATE_BEGIN:
		arg_23_0.showAllCard()
	elif arg_23_0.gameState == arg_23_0.GAME_STATE_GAMING:
		-- block empty
	elif arg_23_0.gameState == arg_23_0.GAME_STATE_END:
		arg_23_0.clearCountTimer()

def var_0_0.gameEndHandler(arg_24_0):
	arg_24_0.gameState = arg_24_0.GAME_STATE_END

	arg_24_0.checkGameState()
	setActive(arg_24_0.maskBtn, True)

	local var_24_0 = math.floor((Time.realtimeSinceStartup - arg_24_0.beginTime) * 1000)

	var_24_0 = var_24_0 < 0 and 9 * arg_24_0.aniTime or var_24_0

	arg_24_0.setTimeTxt(var_24_0)

	local var_24_1 = arg_24_0.lastTimes > 0 and arg_24_0.activityData.data2 + 1 or arg_24_0.activityData.data2

	var_24_1 = var_24_1 > arg_24_0.cardEffectTimesMax and arg_24_0.cardEffectTimesMax or var_24_1

	if arg_24_0.lastTimes > 0 or var_24_0 < arg_24_0.activityData.data4:
		arg_24_0.emit(CardPairsMediator.EVENT_OPERATION, {
			cmd = 1,
			activity_id = arg_24_0.activityData.id,
			arg1 = var_24_1,
			arg2 = var_24_0
		})

	setActive(arg_24_0.endTips, True)

def var_0_0.showAllCard(arg_25_0):
	arg_25_0.setAllCardEnale(False)

	arg_25_0.timer = Timer.New(function()
		for iter_26_0, iter_26_1 in pairs(arg_25_0.cardList):
			iter_26_1.aniShowBack(True)

		arg_25_0.timer = Timer.New(function()
			for iter_27_0, iter_27_1 in pairs(arg_25_0.cardList):
				iter_27_1.aniShowBack()

			arg_25_0.timer = Timer.New(function()
				arg_25_0.gameState = arg_25_0.GAME_STATE_GAMING

				arg_25_0.checkGameState()
				arg_25_0.setAllCardEnale(True), arg_25_0.aniTime, 1)

			arg_25_0.timer.Start(), arg_25_0.firstShowingTime, 1)

		arg_25_0.timer.Start(), 0.5, 1)

	arg_25_0.timer.Start()

def var_0_0.clearAllCard(arg_29_0, arg_29_1):
	if arg_29_0.timer != None:
		arg_29_0.timer.Stop()

		arg_29_0.timer = None

	if arg_29_1:
		for iter_29_0, iter_29_1 in pairs(arg_29_0.cardList):
			iter_29_1.destroy()

		arg_29_0.cardList = {}
	else
		for iter_29_2, iter_29_3 in pairs(arg_29_0.cardList):
			iter_29_3.clear()

def var_0_0.hideChild(arg_30_0, arg_30_1):
	local var_30_0 = arg_30_1.childCount

	for iter_30_0 = 0, var_30_0 - 1:
		local var_30_1 = arg_30_1.GetChild(iter_30_0)

		setActive(var_30_1, False)

def var_0_0.tryFirstPlayStory(arg_31_0):
	if arg_31_0.activityData.getConfig("config_client")[1]:
		local var_31_0 = arg_31_0.activityData.getConfig("config_client")[1][1]

		if var_31_0 != None and not pg.NewStoryMgr.GetInstance().IsPlayed(var_31_0):
			pg.NewStoryMgr.GetInstance().Play(var_31_0, function()
				triggerButton(arg_31_0.maskBtn))

			return True

		return False
	else
		return False

def var_0_0.clearCountTimer(arg_33_0):
	if arg_33_0.countTimer != None:
		arg_33_0.countTimer.Stop()

		arg_33_0.countTimer = None

def var_0_0.willExit(arg_34_0):
	arg_34_0.clearAllCard(True)
	arg_34_0.clearCountTimer()

	if arg_34_0.updateTimer != None:
		arg_34_0.updateTimer.Stop()

		arg_34_0.updateTimer = None

return var_0_0
