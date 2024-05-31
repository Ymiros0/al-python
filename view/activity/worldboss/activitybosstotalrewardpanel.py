local var_0_0 = class("ActivityBossTotalRewardPanel", import("view.level.BaseTotalRewardPanel"))

def var_0_0.getUIName(arg_1_0):
	return "ActivityBossTotalRewardPanel"

local var_0_1 = 0.15

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.itemList = arg_2_0.boxView.Find("Content/ItemGrid2")

	setText(arg_2_0.window.Find("Fixed/top/bg/obtain/title"), i18n("autofight_rewards"))

def var_0_0.didEnter(arg_3_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf, None, {
		lockGlobalBlur = True,
		weight = LayerWeightConst.THIRD_LAYER
	})
	arg_3_0.UpdateView()

	local var_3_0 = arg_3_0.contextData.isAutoFight
	local var_3_1 = PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0) > 0

	if var_3_0 and var_3_1:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_AUTO_BATTLE)
		LuaHelper.Vibrate()

def var_0_0.willExit(arg_4_0):
	arg_4_0.SkipAnim()
	pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf)

def var_0_0.UpdateView(arg_5_0):
	local var_5_0 = arg_5_0.contextData

	onButton(arg_5_0, arg_5_0._tf.Find("BG"), function()
		if arg_5_0.isRewardAnimating:
			arg_5_0.SkipAnim()

			return

		existCall(var_5_0.onClose)
		arg_5_0.closeView())
	onButton(arg_5_0, arg_5_0.window.Find("Fixed/ButtonGO"), function()
		existCall(var_5_0.onClose)
		arg_5_0.closeView(), SFX_CONFIRM)

	local var_5_1 = var_5_0.rewards
	local var_5_2 = {}
	local var_5_3 = var_5_1 and #var_5_1 > 0
	local var_5_4 = CustomIndexLayer.Clone2Full(arg_5_0.itemList, #var_5_1)

	for iter_5_0, iter_5_1 in ipairs(var_5_4):
		local var_5_5 = var_5_1[iter_5_0]
		local var_5_6 = var_5_4[iter_5_0]

		updateDrop(var_5_6.Find("Icon"), var_5_5)
		onButton(arg_5_0, var_5_6.Find("Icon"), function()
			arg_5_0.emit(BaseUI.ON_DROP, var_5_5), SFX_PANEL)

	if var_5_3:
		arg_5_0.isRewardAnimating = True

		for iter_5_2 = 1, #var_5_1:
			local var_5_7 = var_5_4[iter_5_2]

			setActive(var_5_7, False)
			table.insert(var_5_2, function(arg_9_0)
				if arg_5_0.exited:
					return

				setActive(var_5_7, True)
				scrollTo(arg_5_0.boxView.Find("Content"), {
					y = 0
				})

				arg_5_0.LTid = LeanTween.delayedCall(var_0_1, System.Action(arg_9_0)).uniqueId)

	local var_5_8 = {}
	local var_5_9 = arg_5_0.contextData.stopReason

	if not var_5_9:
		if arg_5_0.contextData.isAutoFight:
			table.insert(var_5_8, i18n("multiple_sorties_finish"))
		else
			table.insert(var_5_8, i18n("multiple_sorties_stop"))
	else
		table.insert(var_5_8, var_5_9 .. i18n("multiple_sorties_stop_tip_end"))

	table.insert(var_5_8, i18n("multiple_sorties_end_status", arg_5_0.contextData.totalBattleTimes, arg_5_0.contextData.totalBattleTimes - arg_5_0.contextData.continuousBattleTimes))

	if #var_5_8 > 0:
		setText(arg_5_0.boxView.Find("Content/TextArea2/Text"), table.concat(var_5_8, "\n"))

	seriesAsync(var_5_2, function()
		arg_5_0.SkipAnim())

def var_0_0.SkipAnim(arg_11_0):
	if not arg_11_0.isRewardAnimating:
		return

	arg_11_0.isRewardAnimating = None

	if arg_11_0.LTid:
		LeanTween.cancel(arg_11_0.LTid)

		arg_11_0.LTid = None

	eachChild(arg_11_0.itemList, function(arg_12_0)
		setActive(arg_12_0, True))

def var_0_0.onBackPressed(arg_13_0):
	existCall(arg_13_0.contextData.onClose)
	arg_13_0.closeView()

return var_0_0
