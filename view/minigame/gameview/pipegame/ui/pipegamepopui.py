local var_0_0 = class("PipeGamePopUI")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	var_0_1 = PipeGameVo

	arg_1_0.initCountUI()
	arg_1_0.initLeavelUI()
	arg_1_0.initPauseUI()
	arg_1_0.initSettlementUI()
	arg_1_0.initRankUI()

def var_0_0.initCountUI(arg_2_0):
	arg_2_0.countUI = findTF(arg_2_0._tf, "pop/CountUI")
	arg_2_0.countAnimator = GetComponent(findTF(arg_2_0.countUI, "count"), typeof(Animator))
	arg_2_0.countDft = GetOrAddComponent(findTF(arg_2_0.countUI, "count"), typeof(DftAniEvent))

	arg_2_0.countDft.SetTriggerEvent(function()
		return)
	arg_2_0.countDft.SetEndEvent(function()
		arg_2_0._event.emit(PipeGameEvent.COUNT_DOWN))

def var_0_0.initLeavelUI(arg_5_0):
	arg_5_0.leaveUI = findTF(arg_5_0._tf, "pop/LeaveUI")

	GetComponent(findTF(arg_5_0.leaveUI, "ad/desc"), typeof(Image)).SetNativeSize()
	setActive(arg_5_0.leaveUI, False)
	onButton(arg_5_0._event, findTF(arg_5_0.leaveUI, "ad/btnOk"), function()
		arg_5_0.resumeGame()
		arg_5_0._event.emit(PipeGameEvent.LEVEL_GAME, True), SFX_CANCEL)
	onButton(arg_5_0._event, findTF(arg_5_0.leaveUI, "ad/btnCancel"), function()
		arg_5_0.resumeGame()
		arg_5_0._event.emit(PipeGameEvent.LEVEL_GAME, False), SFX_CANCEL)

def var_0_0.initPauseUI(arg_8_0):
	arg_8_0.pauseUI = findTF(arg_8_0._tf, "pop/pauseUI")

	setActive(arg_8_0.pauseUI, False)
	GetComponent(findTF(arg_8_0.pauseUI, "ad/desc"), typeof(Image)).SetNativeSize()
	onButton(arg_8_0._event, findTF(arg_8_0.pauseUI, "ad/btnOk"), function()
		arg_8_0.resumeGame()
		arg_8_0._event.emit(PipeGameEvent.PAUSE_GAME, False), SFX_CANCEL)

def var_0_0.initSettlementUI(arg_10_0):
	arg_10_0.settlementUI = findTF(arg_10_0._tf, "pop/SettleMentUI")

	GetComponent(findTF(arg_10_0.settlementUI, "ad/HighImg"), typeof(Image)).SetNativeSize()
	GetComponent(findTF(arg_10_0.settlementUI, "ad/CurImg"), typeof(Image)).SetNativeSize()
	setActive(arg_10_0.settlementUI, False)
	onButton(arg_10_0._event, findTF(arg_10_0.settlementUI, "ad/btnOver"), function()
		arg_10_0.clearUI()
		arg_10_0._event.emit(PipeGameEvent.BACK_MENU), SFX_CANCEL)

def var_0_0.initRankUI(arg_12_0):
	arg_12_0.rankUI = findTF(arg_12_0._tf, "pop/RankUI")

	arg_12_0.showRank(False)
	GetComponent(findTF(arg_12_0.rankUI, "ad/img/score"), typeof(Image)).SetNativeSize()
	GetComponent(findTF(arg_12_0.rankUI, "ad/img/time"), typeof(Image)).SetNativeSize()

	arg_12_0._rankImg = findTF(arg_12_0.rankUI, "ad/img")
	arg_12_0._rankBtnClose = findTF(arg_12_0.rankUI, "ad/btnClose")
	arg_12_0._rankContent = findTF(arg_12_0.rankUI, "ad/list/content")
	arg_12_0._rankItemTpl = findTF(arg_12_0.rankUI, "ad/list/content/itemTpl")
	arg_12_0._rankEmpty = findTF(arg_12_0.rankUI, "ad/empty")
	arg_12_0._rankDesc = findTF(arg_12_0.rankUI, "ad/desc")
	arg_12_0._rankItems = {}

	setActive(arg_12_0._rankItemTpl, False)
	onButton(arg_12_0._event, findTF(arg_12_0.rankUI, "ad/close"), function()
		arg_12_0.showRank(False), SFX_CANCEL)
	onButton(arg_12_0._event, arg_12_0._rankBtnClose, function()
		arg_12_0.showRank(False), SFX_CANCEL)
	setText(arg_12_0._rankDesc, i18n(var_0_1.rank_tip))
	arg_12_0.getRankData()

def var_0_0.getRankData(arg_15_0):
	pg.m02.sendNotification(GAME.MINI_GAME_FRIEND_RANK, {
		id = var_0_1.game_id,
		def callback:(arg_16_0)
			local var_16_0 = {}

			for iter_16_0 = 1, #arg_16_0:
				local var_16_1 = {}

				for iter_16_1, iter_16_2 in pairs(arg_16_0[iter_16_0]):
					var_16_1[iter_16_1] = iter_16_2

				table.insert(var_16_0, var_16_1)

			table.sort(var_16_0, function(arg_17_0, arg_17_1)
				if arg_17_0.score != arg_17_1.score:
					return arg_17_0.score > arg_17_1.score
				elif arg_17_0.time_data != arg_17_1.time_data:
					return arg_17_0.time_data > arg_17_1.time_data
				else
					return arg_17_0.player_id < arg_17_1.player_id)
			arg_15_0.updateRankData(var_16_0)
	})

def var_0_0.updateRankData(arg_18_0, arg_18_1):
	for iter_18_0 = 1, #arg_18_1:
		local var_18_0

		if iter_18_0 > #arg_18_0._rankItems:
			local var_18_1 = tf(instantiate(arg_18_0._rankItemTpl))

			setActive(var_18_1, False)
			setParent(var_18_1, arg_18_0._rankContent)
			table.insert(arg_18_0._rankItems, var_18_1)

		local var_18_2 = arg_18_0._rankItems[iter_18_0]

		arg_18_0.setRankItemData(var_18_2, arg_18_1[iter_18_0], iter_18_0)
		setActive(var_18_2, True)

	for iter_18_1 = #arg_18_1 + 1, #arg_18_0._rankItems:
		setActive(arg_18_0._rankItems, False)

	setActive(arg_18_0._rankEmpty, #arg_18_1 == 0)
	setActive(arg_18_0._rankImg, #arg_18_1 > 0)

def var_0_0.setRankItemData(arg_19_0, arg_19_1, arg_19_2, arg_19_3):
	local var_19_0 = arg_19_2.name
	local var_19_1 = arg_19_2.player_id
	local var_19_2 = arg_19_2.position
	local var_19_3 = arg_19_2.score
	local var_19_4 = arg_19_2.time_data
	local var_19_5 = getProxy(PlayerProxy).isSelf(var_19_1)

	setText(findTF(arg_19_1, "nameText"), var_19_0)
	arg_19_0.setChildVisible(findTF(arg_19_1, "bg"), False)
	arg_19_0.setChildVisible(findTF(arg_19_1, "rank"), False)

	if arg_19_3 <= 3:
		setActive(findTF(arg_19_1, "bg/" .. arg_19_3), True)
		setActive(findTF(arg_19_1, "rank/" .. arg_19_3), True)
	elif var_19_5:
		setActive(findTF(arg_19_1, "bg/me"), True)
		setActive(findTF(arg_19_1, "rank/count"), True)
	else
		setActive(findTF(arg_19_1, "bg/other"), True)
		setActive(findTF(arg_19_1, "rank/count"), True)

	setText(findTF(arg_19_1, "rank/count"), tostring(arg_19_3))
	setText(findTF(arg_19_1, "score"), tostring(var_19_3))
	setText(findTF(arg_19_1, "time"), tostring(var_19_4))
	setActive(findTF(arg_19_1, "imgMy"), var_19_5)

def var_0_0.setChildVisible(arg_20_0, arg_20_1, arg_20_2):
	for iter_20_0 = 1, arg_20_1.childCount:
		local var_20_0 = arg_20_1.GetChild(iter_20_0 - 1)

		setActive(var_20_0, arg_20_2)

def var_0_0.showRank(arg_21_0, arg_21_1):
	if arg_21_1:
		arg_21_0.getRankData()

	setActive(arg_21_0.rankUI, arg_21_1)

def var_0_0.updateSettlementUI(arg_22_0):
	GetComponent(findTF(arg_22_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_22_0 = var_0_1.scoreNum
	local var_22_1 = math.floor(var_0_1.gameDragTime)
	local var_22_2 = getProxy(MiniGameProxy).GetHighScore(var_0_1.game_id)
	local var_22_3 = var_22_2 and #var_22_2 > 0 and var_22_2[1] or 0
	local var_22_4 = var_22_2 and #var_22_2 > 1 and var_22_2[2] or 0

	setActive(findTF(arg_22_0.settlementUI, "ad/new"), var_22_3 < var_22_0)

	if var_22_0 > 0 and var_22_3 < var_22_0:
		arg_22_0._event.emit(PipeGameEvent.STORE_SERVER, {
			var_22_0,
			var_22_1
		})
	elif var_22_0 > 0 and var_22_0 == var_22_3 and var_22_4 < var_22_1:
		arg_22_0._event.emit(PipeGameEvent.STORE_SERVER, {
			var_22_0,
			var_22_1
		})

	local var_22_5 = findTF(arg_22_0.settlementUI, "ad/highText")
	local var_22_6 = findTF(arg_22_0.settlementUI, "ad/currentText")

	setText(var_22_6, var_22_0)
	setText(var_22_5, var_22_1)
	arg_22_0._event.emit(PipeGameEvent.SUBMIT_GAME_SUCCESS)

def var_0_0.backPressed(arg_23_0):
	if isActive(arg_23_0.pauseUI):
		arg_23_0.resumeGame()
		arg_23_0._event.emit(PipeGameEvent.PAUSE_GAME, False)
	elif isActive(arg_23_0.leaveUI):
		arg_23_0.resumeGame()
		arg_23_0._event.emit(PipeGameEvent.LEVEL_GAME, False)
	elif not isActive(arg_23_0.pauseUI) and not isActive(arg_23_0.pauseUI):
		if not var_0_1.startSettlement:
			arg_23_0.popPauseUI()
			arg_23_0._event.emit(PipeGameEvent.PAUSE_GAME, True)
	else
		arg_23_0.resumeGame()

def var_0_0.resumeGame(arg_24_0):
	setActive(arg_24_0.leaveUI, False)
	setActive(arg_24_0.pauseUI, False)

def var_0_0.popLeaveUI(arg_25_0):
	if isActive(arg_25_0.pauseUI):
		setActive(arg_25_0.pauseUI, False)

	setActive(arg_25_0.leaveUI, True)

def var_0_0.popPauseUI(arg_26_0):
	if isActive(arg_26_0.leaveUI):
		setActive(arg_26_0.leaveUI, False)

	setActive(arg_26_0.pauseUI, True)

def var_0_0.updateGameUI(arg_27_0, arg_27_1):
	setText(arg_27_0.scoreTf, arg_27_1.scoreNum)
	setText(arg_27_0.gameTimeS, math.ceil(arg_27_1.gameTime))

def var_0_0.readyStart(arg_28_0):
	arg_28_0.popCountUI(True)
	arg_28_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1.SFX_COUNT_DOWN)

def var_0_0.popCountUI(arg_29_0, arg_29_1):
	setActive(arg_29_0.countUI, arg_29_1)

def var_0_0.popSettlementUI(arg_30_0, arg_30_1):
	setActive(arg_30_0.settlementUI, arg_30_1)

def var_0_0.clearUI(arg_31_0):
	setActive(arg_31_0.settlementUI, False)
	setActive(arg_31_0.countUI, False)

return var_0_0
