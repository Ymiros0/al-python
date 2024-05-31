local var_0_0 = class("DOAPPMiniGameView", import("view.miniGame.MiniGameTemplateView"))

var_0_0.canSelectStage = False

def var_0_0.getUIName(arg_1_0):
	return "DOAPPMiniGameUI"

def var_0_0.getGameController(arg_2_0):
	return DOAPPMiniGameController

def var_0_0.initPageUI(arg_3_0):
	var_0_0.super.initPageUI(arg_3_0)
	onButton(arg_3_0, arg_3_0.rtTitlePage.Find("main/btn_help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.doa_minigame_help.tip
		}), SFX_PANEL)

	local var_3_0 = arg_3_0.GetMGData().GetSimpleValue("story")

	onButton(arg_3_0, arg_3_0.rtTitlePage.Find("main/btn_start"), function()
		local var_5_0 = {}
		local var_5_1 = checkExist(var_3_0, {
			arg_3_0.stageIndex
		}, {
			1
		})

		if var_5_1:
			table.insert(var_5_0, function(arg_6_0)
				pg.NewStoryMgr.GetInstance().Play(var_5_1, arg_6_0))

		seriesAsync(var_5_0, function()
			arg_3_0.openUI("select")), SFX_PANEL)

	local var_3_1 = arg_3_0.rtTitlePage.Find("select")

	onButton(arg_3_0, var_3_1.Find("btn_back"), function()
		arg_3_0.openUI("main"), SFX_CANCEL)
	onButton(arg_3_0, var_3_1.Find("btn/confirm"), function()
		if not arg_3_0.character:
			pg.TipsMgr.GetInstance().ShowTips("without selected character")

			return

		arg_3_0.gameController.ResetGame()
		arg_3_0.gameController.ReadyGame({
			name = arg_3_0.character
		})
		arg_3_0.openUI("countdown"), SFX_CONFIRM)
	eachChild(var_3_1.Find("content"), function(arg_10_0)
		setText(arg_10_0.Find("name/Text"), i18n("doa_minigame_" .. arg_10_0.name))
		onToggle(arg_3_0, arg_10_0, function(arg_11_0)
			if arg_11_0:
				arg_3_0.character = arg_10_0.name

				setAnchoredPosition(arg_10_0.Find(arg_10_0.name), {
					x = 70
				})
				quickPlayAnimator(arg_10_0.Find(arg_10_0.name .. "/Image"), "Win")
			else
				if arg_3_0.character == arg_10_0.name:
					arg_3_0.character = None

				setAnchoredPosition(arg_10_0.Find(arg_10_0.name), {
					x = 110
				})
				quickPlayAnimator(arg_10_0.Find(arg_10_0.name .. "/Image"), "Idle"), SFX_PANEL))

local function var_0_1(arg_12_0, arg_12_1, arg_12_2, arg_12_3)
	eachChild(arg_12_0.Find("mask"), function(arg_13_0)
		setActive(arg_13_0, arg_13_0.name == arg_12_1))
	setText(arg_12_0.Find("name/Text"), i18n("doa_minigame_" .. arg_12_1))
	eachChild(arg_12_0.Find("name/Text"), function(arg_14_0)
		setActive(arg_14_0, arg_14_0.name == arg_12_1))
	setActive(arg_12_0.Find("result/lose"), arg_12_3 < 0)
	setActive(arg_12_0.Find("result/win"), arg_12_3 > 0)
	eachChild(arg_12_0.Find("point"), function(arg_15_0)
		setActive(arg_15_0, tonumber(arg_15_0.name) <= arg_12_2))

def var_0_0.initOpenUISwich(arg_16_0):
	var_0_0.super.initOpenUISwich(arg_16_0)

	function arg_16_0.openSwitchDic.result()
		var_0_1(arg_16_0.rtTitlePage.Find("result/window/self"), arg_16_0.gameController.GetResultInfo(False))
		var_0_1(arg_16_0.rtTitlePage.Find("result/window/other"), arg_16_0.gameController.GetResultInfo(True))

		local var_17_0 = arg_16_0.GetMGHubData()

		if arg_16_0.stageIndex == var_17_0.usedtime + 1 and var_17_0.count > 0:
			arg_16_0.SendSuccess(0)

	function arg_16_0.openSwitchDic.select()
		triggerToggle(arg_16_0.rtTitlePage.Find("select/content/Marie"), True)

def var_0_0.initBackPressSwitch(arg_19_0):
	var_0_0.super.initBackPressSwitch(arg_19_0)

	function arg_19_0.backPressSwitchDic.select()
		arg_19_0.openUI("main")

def var_0_0.willExit(arg_21_0):
	arg_21_0.gameController.willExit()

return var_0_0
