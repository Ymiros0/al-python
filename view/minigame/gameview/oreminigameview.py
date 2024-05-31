local var_0_0 = class("OreMiniGameView", import("view.miniGame.MiniGameTemplateView"))

def var_0_0.getUIName(arg_1_0):
	return "OreMiniGameUI"

def var_0_0.getGameController(arg_2_0):
	return OreMiniGameController

def var_0_0.getShowSide(arg_3_0):
	return False

def var_0_0.initPageUI(arg_4_0):
	var_0_0.super.initPageUI(arg_4_0)
	onButton(arg_4_0, arg_4_0.rtTitlePage.Find("main/btn_help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.ore_minigame_help.tip
		}), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.rtTitlePage.Find("result/window/btn_finish"), function()
		arg_4_0.openUI("main")
		arg_4_0.gameController.ResetGame(), SFX_CONFIRM)

	local var_4_0 = arg_4_0.rtTitlePage.Find("main/res_bar")
	local var_4_1 = pg.activity_template[ActivityConst.ISLAND_GAME_ID].config_client.item_id

	LoadImageSpriteAsync(Item.getConfigData(var_4_1).icon, var_4_0.Find("icon"), True)
	setText(var_4_0.Find("num"), arg_4_0.GetMGHubData().count)
	onButton(arg_4_0, var_4_0, function()
		arg_4_0.emit(BaseMiniGameMediator.OPEN_SUB_LAYER, {
			mediator = IslandGameLimitMediator,
			viewComponent = IslandGameLimitLayer
		}), SFX_CANCEL)

def var_0_0.updateMainUI(arg_8_0):
	var_0_0.super.updateMainUI(arg_8_0)

	local var_8_0 = arg_8_0.rtTitlePage.Find("main/res_bar")
	local var_8_1 = pg.activity_template[ActivityConst.ISLAND_GAME_ID].config_client.item_id

	setText(var_8_0.Find("num"), arg_8_0.GetMGHubData().count)

def var_0_0.willExit(arg_9_0):
	arg_9_0.gameController.willExit()

return var_0_0
