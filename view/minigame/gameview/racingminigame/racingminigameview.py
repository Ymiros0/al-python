local var_0_0 = class("RacingMiniGameView", import("view.miniGame.MiniGameTemplateView"))

var_0_0.canSelectStage = False

def var_0_0.getUIName(arg_1_0):
	return "RacingMiniGameUI"

def var_0_0.getGameController(arg_2_0):
	return RacingMiniGameController

def var_0_0.getShowSide(arg_3_0):
	return False

def var_0_0.initPageUI(arg_4_0):
	arg_4_0.rtTitlePage = arg_4_0._tf.Find("TitlePage")

	arg_4_0.rtTitlePage.Find("countdown").Find("bg").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_4_0.openUI()
		arg_4_0.gameController.StartGame()
		pg.BgmMgr.GetInstance().ContinuePlay())

	local var_4_0 = arg_4_0.rtTitlePage.Find("pause")

	onButton(arg_4_0, var_4_0.Find("window/btn_confirm"), function()
		arg_4_0.openUI()
		arg_4_0.gameController.ResumeGame(), SFX_CONFIRM)

	local var_4_1 = arg_4_0.rtTitlePage.Find("exit")

	onButton(arg_4_0, var_4_1.Find("window/btn_cancel"), function()
		arg_4_0.openUI()
		arg_4_0.gameController.ResumeGame(), SFX_CANCEL)
	onButton(arg_4_0, var_4_1.Find("window/btn_confirm"), function()
		arg_4_0.openUI()
		arg_4_0.gameController.EndGame(), SFX_CONFIRM)

	local var_4_2 = arg_4_0.rtTitlePage.Find("result")

	onButton(arg_4_0, var_4_2.Find("window/btn_finish"), function()
		arg_4_0.closeView(), SFX_CONFIRM)

def var_0_0.didEnter(arg_10_0):
	arg_10_0.initPageUI()
	arg_10_0.initControllerUI()

	arg_10_0.gameController = arg_10_0.getGameController().New(arg_10_0, arg_10_0._tf)

	arg_10_0.gameController.ResetGame()
	arg_10_0.gameController.ReadyGame(getProxy(MiniGameProxy).GetRank(arg_10_0.GetMGData().id))
	pg.BgmMgr.GetInstance().StopPlay()
	arg_10_0.openUI("countdown")

def var_0_0.initOpenUISwich(arg_11_0):
	var_0_0.super.initOpenUISwich(arg_11_0)

	arg_11_0.openSwitchDic.main = None

	function arg_11_0.openSwitchDic.result()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3("ui-streamers")

		local var_12_0 = arg_11_0.GetMGData().id
		local var_12_1 = arg_11_0.gameController.point
		local var_12_2 = getProxy(MiniGameProxy).GetHighScore(var_12_0) / 100
		local var_12_3 = arg_11_0.rtTitlePage.Find("result")

		setActive(var_12_3.Find("window/now/new"), var_12_2 < var_12_1)

		if var_12_2 <= var_12_1:
			var_12_2 = var_12_1

			getProxy(MiniGameProxy).UpdataHighScore(var_12_0, math.floor(var_12_1 * 100))

		setText(var_12_3.Find("window/high/Text"), string.format("%.2fm", var_12_2))
		setText(var_12_3.Find("window/now/Text"), string.format("%.2fm", var_12_1))

		local var_12_4 = arg_11_0.GetMGHubData()

		arg_11_0.emit(BaseMiniGameMediator.GAME_FINISH_TRACKING, {
			game_id = var_12_0,
			hub_id = var_12_4.id,
			isComplete = arg_11_0.gameController.result
		})

		if (not arg_11_0.getShowSide() or arg_11_0.stageIndex == var_12_4.usedtime + 1) and var_12_4.count > 0:
			arg_11_0.SendSuccess(0)

	function arg_11_0.openSwitchDic.countdown()
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_STEP_PILE_COUNTDOWN)

def var_0_0.willExit(arg_14_0):
	arg_14_0.gameController.willExit()

return var_0_0
