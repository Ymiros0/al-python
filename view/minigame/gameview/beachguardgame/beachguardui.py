local var_0_0 = class("BeachGuardUIlua")
local var_0_1 = "event./ui/ddldaoshu2"
local var_0_2 = "event./ui/break_out_full"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_3
	arg_1_0._gameData = arg_1_2

	arg_1_0.initCountUI()
	arg_1_0.initLeavelUI()
	arg_1_0.initPauseUI()
	arg_1_0.initSettlementUI()

def var_0_0.initCountUI(arg_2_0):
	arg_2_0.countUI = findTF(arg_2_0._tf, "pop/CountUI")
	arg_2_0.countAnimator = GetComponent(findTF(arg_2_0.countUI, "count"), typeof(Animator))
	arg_2_0.countDft = GetOrAddComponent(findTF(arg_2_0.countUI, "count"), typeof(DftAniEvent))

	arg_2_0.countDft.SetTriggerEvent(function()
		return)
	arg_2_0.countDft.SetEndEvent(function()
		arg_2_0._event.emit(BeachGuardGameView.COUNT_DOWN))

def var_0_0.initLeavelUI(arg_5_0):
	arg_5_0.leaveUI = findTF(arg_5_0._tf, "pop/LeaveUI")

	GetComponent(findTF(arg_5_0.leaveUI, "ad/desc"), typeof(Image)).SetNativeSize()
	setActive(arg_5_0.leaveUI, False)
	onButton(arg_5_0._event, findTF(arg_5_0.leaveUI, "ad/btnOk"), function()
		arg_5_0.resumeGame()
		arg_5_0._event.emit(BeachGuardGameView.LEVEL_GAME, True), SFX_CANCEL)
	onButton(arg_5_0._event, findTF(arg_5_0.leaveUI, "ad/btnCancel"), function()
		arg_5_0.resumeGame()
		arg_5_0._event.emit(BeachGuardGameView.LEVEL_GAME, False), SFX_CANCEL)

def var_0_0.initPauseUI(arg_8_0):
	arg_8_0.pauseUI = findTF(arg_8_0._tf, "pop/pauseUI")

	GetComponent(findTF(arg_8_0.pauseUI, "ad/desc"), typeof(Image)).SetNativeSize()
	setActive(arg_8_0.pauseUI, False)
	onButton(arg_8_0._event, findTF(arg_8_0.pauseUI, "ad/btnOk"), function()
		arg_8_0.resumeGame()
		arg_8_0._event.emit(BeachGuardGameView.PAUSE_GAME, False), SFX_CANCEL)

def var_0_0.initSettlementUI(arg_10_0):
	arg_10_0.settlementUI = findTF(arg_10_0._tf, "pop/SettleMentUI")

	setActive(arg_10_0.settlementUI, False)
	onButton(arg_10_0._event, findTF(arg_10_0.settlementUI, "ad/btnOver"), function()
		arg_10_0.clearUI()
		arg_10_0._event.emit(BeachGuardGameView.BACK_MENU), SFX_CANCEL)

def var_0_0.updateSettlementUI(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	GetComponent(findTF(arg_12_0.settlementUI, "ad"), typeof(Animator)).Play("settlement", -1, 0)

	local var_12_0 = arg_12_1.GetRuntimeData("elements")
	local var_12_1 = arg_12_3.scoreNum
	local var_12_2 = var_12_0 and #var_12_0 > 0 and var_12_0[1] or 0

	setActive(findTF(arg_12_0.settlementUI, "ad/new"), var_12_2 < var_12_1)

	if var_12_2 < var_12_1:
		var_12_2 = var_12_1

		arg_12_0._event.emit(BeachGuardGameView.STORE_SERVER, var_12_2)

	local var_12_3 = findTF(arg_12_0.settlementUI, "ad/highText")
	local var_12_4 = findTF(arg_12_0.settlementUI, "ad/currentText")

	setText(var_12_3, var_12_2)
	setText(var_12_4, var_12_1)

	local var_12_5 = arg_12_0.getGameTimes(arg_12_2)

	if var_12_5 and var_12_5 > 0 and not arg_12_0.sendSuccessFlag:
		arg_12_0._event.emit(BeachGuardGameView.SUBMIT_GAME_SUCCESS)

def var_0_0.backPressed(arg_13_0):
	if isActive(arg_13_0.pauseUI):
		arg_13_0.resumeGame()
		arg_13_0._event.emit(BeachGuardGameView.PAUSE_GAME, False)
	elif isActive(arg_13_0.leaveUI):
		arg_13_0.resumeGame()
		arg_13_0._event.emit(BeachGuardGameView.LEVEL_GAME, False)
	elif not isActive(arg_13_0.pauseUI) and not isActive(arg_13_0.pauseUI):
		arg_13_0.popPauseUI()
		arg_13_0._event.emit(BeachGuardGameView.PAUSE_GAME, True)
	else
		arg_13_0.resumeGame()

def var_0_0.resumeGame(arg_14_0):
	setActive(arg_14_0.leaveUI, False)
	setActive(arg_14_0.pauseUI, False)

def var_0_0.popLeaveUI(arg_15_0):
	if isActive(arg_15_0.pauseUI):
		setActive(arg_15_0.pauseUI, False)

	setActive(arg_15_0.leaveUI, True)

def var_0_0.popPauseUI(arg_16_0):
	if isActive(arg_16_0.leaveUI):
		setActive(arg_16_0.leaveUI, False)

	setActive(arg_16_0.pauseUI, True)

def var_0_0.updateGameUI(arg_17_0, arg_17_1):
	setText(arg_17_0.scoreTf, arg_17_1.scoreNum)
	setText(arg_17_0.gameTimeS, math.ceil(arg_17_1.gameTime))

def var_0_0.readyStart(arg_18_0):
	arg_18_0.popCountUI(True)
	arg_18_0.countAnimator.Play("count")
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_0_1)

def var_0_0.popCountUI(arg_19_0, arg_19_1):
	setActive(arg_19_0.countUI, arg_19_1)

def var_0_0.openSettlementUI(arg_20_0, arg_20_1):
	setActive(arg_20_0.settlementUI, arg_20_1)

def var_0_0.clearUI(arg_21_0):
	setActive(arg_21_0.settlementUI, False)
	setActive(arg_21_0.countUI, False)

def var_0_0.getGameTimes(arg_22_0, arg_22_1):
	return arg_22_1.count

return var_0_0
