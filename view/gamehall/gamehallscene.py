local var_0_0 = class("GameHallScene", import("..base.BaseUI"))

var_0_0.open_with_list = False

def var_0_0.getUIName(arg_1_0):
	return "GameHallUI"

def var_0_0.init(arg_2_0):
	return

def var_0_0.didEnter(arg_3_0):
	arg_3_0.initTopUI()
	arg_3_0.initHomeUI()

	local var_3_0 = findTF(arg_3_0._tf, "ad/container")

	arg_3_0.charController = GameHallContainerUI.New(var_3_0)
	arg_3_0.freeCoinTf = findTF(var_3_0, "content/top/free")

	onButton(arg_3_0, arg_3_0.freeCoinTf, function()
		local var_4_0 = getProxy(GameRoomProxy).getCoin()
		local var_4_1 = pg.gameset.game_coin_max.key_value - var_4_0
		local var_4_2 = pg.gameset.game_coin_initial.key_value

		if var_4_1 == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("game_icon_max_full"))
		elif var_4_1 < var_4_2:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("game_icon_max"),
				def onYes:()
					arg_3_0.emit(GameHallMediator.GET_WEEKLY_COIN),
				def onNo:()
					return
			})
		else
			arg_3_0.emit(GameHallMediator.GET_WEEKLY_COIN), SFX_CONFIRM)

	arg_3_0.listPanelTf = findTF(arg_3_0._tf, "ad/listPanel")
	arg_3_0.listPanel = GameHallListPanel.New(arg_3_0.listPanelTf, arg_3_0)

	arg_3_0.listPanel.setVisible(GameHallScene.open_with_list)

	GameHallScene.open_with_list = False
	arg_3_0.exchangePanelTf = findTF(arg_3_0._tf, "ad/exchangePanel")
	arg_3_0.parentTf = findTF(arg_3_0._tf, "ad")
	arg_3_0.exchangePanel = GameHallExchangePanel.New(arg_3_0.exchangePanelTf, arg_3_0.parentTf, arg_3_0)

	arg_3_0.openExchangePanel(False)
	arg_3_0.changeTitle(False)

	local var_3_1 = Application.targetFrameRate or 60

	if var_3_1 > 60:
		var_3_1 = 60

	arg_3_0.timer = Timer.New(function()
		arg_3_0.onTimer(), 1 / var_3_1, -1)

	arg_3_0.timer.Start()
	arg_3_0.updateUI()

def var_0_0.initTopUI(arg_8_0):
	arg_8_0.btnBack = findTF(arg_8_0._tf, "ad/topPanel/btnBack")
	arg_8_0.btnHome = findTF(arg_8_0._tf, "ad/topPanel/btnHome")
	arg_8_0.btnHelp = findTF(arg_8_0._tf, "ad/topPanel/btnHelp")
	arg_8_0.btnCoin = findTF(arg_8_0._tf, "ad/topPanel/coin")
	arg_8_0.textCoin = findTF(arg_8_0._tf, "ad/topPanel/coin/text")
	arg_8_0.coinMax = pg.gameset.game_coin_max.key_value
	arg_8_0.textCoinMaxTF = findTF(arg_8_0._tf, "ad/topPanel/coin/max")

	setText(arg_8_0.textCoinMaxTF, "MAX." .. arg_8_0.coinMax)
	onButton(arg_8_0, arg_8_0.btnCoin, function()
		arg_8_0.openExchangePanel(True))
	onButton(arg_8_0, arg_8_0.btnBack, function()
		if arg_8_0.listPanel.getVisible():
			arg_8_0.listPanel.setVisible(False)
			arg_8_0.changeTitle(False)
			pg.SystemGuideMgr.GetInstance().Play(arg_8_0)

			return

		arg_8_0.closeView(), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.btnHome, function()
		arg_8_0.quickExitFunc(), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.game_room_help.tip
		}), SFX_CANCEL)

def var_0_0.openExchangePanel(arg_13_0, arg_13_1):
	arg_13_0.exchangePanel.setVisible(arg_13_1)

def var_0_0.ResUISettings(arg_14_0):
	return {
		showType = bit.bor(PlayerResUI.TYPE_OIL, PlayerResUI.TYPE_GOLD)
	}

def var_0_0.initHomeUI(arg_15_0):
	arg_15_0.btnShop = findTF(arg_15_0._tf, "ad/btnShop")
	arg_15_0.btnPlay = findTF(arg_15_0._tf, "ad/btnPlay")

	onButton(arg_15_0, arg_15_0.btnPlay, function()
		arg_15_0.listPanel.setVisible(True)
		arg_15_0.changeTitle(True), SFX_CANCEL)
	onButton(arg_15_0, arg_15_0.btnShop, function()
		arg_15_0.emit(GameHallMediator.OPEN_GAME_SHOP), SFX_CANCEL)

	arg_15_0.topShop = findTF(arg_15_0._tf, "ad/container/content/top/btnShop")
	arg_15_0.topGame = findTF(arg_15_0._tf, "ad/container/content/top/btnGameList")

	onButton(arg_15_0, arg_15_0.topGame, function()
		arg_15_0.listPanel.setVisible(True)
		arg_15_0.changeTitle(True), SFX_CANCEL)
	onButton(arg_15_0, arg_15_0.topShop, function()
		arg_15_0.emit(GameHallMediator.OPEN_GAME_SHOP), SFX_CANCEL)

def var_0_0.updateUI(arg_20_0):
	local var_20_0 = getProxy(GameRoomProxy).getWeekly()

	setActive(arg_20_0.freeCoinTf, var_20_0)

	local var_20_1 = getProxy(GameRoomProxy).getCoin()

	setText(arg_20_0.textCoin, var_20_1)

def var_0_0.onTimer(arg_21_0):
	arg_21_0.charController.step()

def var_0_0.changeTitle(arg_22_0, arg_22_1):
	setActive(findTF(arg_22_0._tf, "ad/topPanel/title_list"), arg_22_1)
	setActive(findTF(arg_22_0._tf, "ad/topPanel/title_main"), not arg_22_1)

def var_0_0.onBackPressed(arg_23_0):
	if arg_23_0.listPanel.getVisible():
		arg_23_0.listPanel.setVisible(False)
		arg_23_0.changeTitle(False)

		return

	if arg_23_0.exchangePanel.getVisible():
		arg_23_0.exchangePanel.setVisible(False)

		return

	arg_23_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.willExit(arg_24_0):
	if arg_24_0.timer:
		arg_24_0.timer.Stop()

		arg_24_0.timer = None

	if arg_24_0.listPanel.getVisible():
		GameHallScene.open_with_list = True

	arg_24_0.exchangePanel.dispose()
	arg_24_0.listPanel.dispose()

return var_0_0
