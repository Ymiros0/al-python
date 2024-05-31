local var_0_0 = class("BossRushTotalRewardPanel", import("view.activity.worldboss.ActivityBossTotalRewardPanel"))

def var_0_0.getUIName(arg_1_0):
	return "BossRushTotalRewardPanel"

local var_0_1 = 0.15

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

def var_0_0.didEnter(arg_3_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, None, {
		lockGlobalBlur = True,
		weight = LayerWeightConst.SECOND_LAYER
	})
	arg_3_0.UpdateView()

def var_0_0.UpdateView(arg_4_0):
	local var_4_0 = arg_4_0.contextData

	onButton(arg_4_0, arg_4_0._tf.Find("BG"), function()
		if arg_4_0.isRewardAnimating:
			arg_4_0.SkipAnim()

			return

		existCall(var_4_0.onClose)
		arg_4_0.closeView())
	setText(arg_4_0.window.Find("Fixed/ButtonGO/pic"), i18n("text_confirm"))
	onButton(arg_4_0, arg_4_0.window.Find("Fixed/ButtonGO"), function()
		existCall(var_4_0.onClose)
		arg_4_0.closeView(), SFX_CONFIRM)
	setText(arg_4_0.window.Find("Fixed/ButtonExit/pic"), i18n("autofight_leave"))
	onButton(arg_4_0, arg_4_0.window.Find("Fixed/ButtonExit"), function()
		existCall(var_4_0.onClose)
		arg_4_0.closeView(), SFX_CANCEL)

	local var_4_1 = var_4_0.rewards
	local var_4_2 = {}
	local var_4_3 = var_4_1 and #var_4_1 > 0

	arg_4_0.itemList = arg_4_0.boxView.Find("Content/ItemGrid")

	setActive(arg_4_0.boxView.Find("Content/TextArea2"), False)
	setActive(arg_4_0.boxView.Find("Content/ItemGrid2"), False)
	setActive(arg_4_0.boxView.Find("Content/Title"), False)
	setActive(arg_4_0.itemList, False)

	if var_4_3:
		arg_4_0.hasRewards = True

		table.insert(var_4_2, function(arg_8_0)
			setActive(arg_4_0.boxView.Find("Content/Title"), True)
			setActive(arg_4_0.itemList, True)
			arg_8_0())

		local var_4_4 = CustomIndexLayer.Clone2Full(arg_4_0.itemList, #var_4_1)

		for iter_4_0, iter_4_1 in ipairs(var_4_4):
			local var_4_5 = var_4_1[iter_4_0]
			local var_4_6 = var_4_4[iter_4_0]

			updateDrop(var_4_6.Find("Shell/Icon"), var_4_5)
			onButton(arg_4_0, var_4_6.Find("Shell/Icon"), function()
				arg_4_0.emit(BaseUI.ON_DROP, var_4_5), SFX_PANEL)

		arg_4_0.isRewardAnimating = True

		local var_4_7 = {}

		for iter_4_2 = 1, #var_4_1:
			local var_4_8 = var_4_4[iter_4_2]

			setActive(var_4_8, False)
			table.insert(var_4_2, function(arg_10_0)
				if arg_4_0.exited:
					return

				setActive(var_4_8, True)
				scrollTo(arg_4_0.boxView.Find("Content"), {
					y = 0
				})

				arg_4_0.LTid = LeanTween.delayedCall(var_0_1, System.Action(arg_10_0)).uniqueId)

	local var_4_9 = {}
	local var_4_10 = arg_4_0.contextData.stopReason

	if not var_4_10:
		if arg_4_0.contextData.isAutoFight:
			table.insert(var_4_9, i18n("multiple_sorties_finish"))
		else
			table.insert(var_4_9, i18n("multiple_sorties_stop"))
	else
		table.insert(var_4_9, var_4_10 .. i18n("multiple_sorties_stop_tip_end"))

	if arg_4_0.contextData.totalBattleTimes:
		table.insert(var_4_9, i18n("multiple_sorties_end_status", arg_4_0.contextData.totalBattleTimes, arg_4_0.contextData.totalBattleTimes - arg_4_0.contextData.continuousBattleTimes))

		if #var_4_9 > 0:
			setText(arg_4_0.boxView.Find("Content/TextArea2/Text"), table.concat(var_4_9, "\n"))

	seriesAsync(var_4_2, function()
		arg_4_0.SkipAnim())

def var_0_0.willExit(arg_12_0):
	pg.m02.sendNotification(BossRushTotalRewardPanelMediator.ON_WILL_EXIT)

return var_0_0
