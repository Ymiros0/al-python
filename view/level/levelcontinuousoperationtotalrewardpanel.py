local var_0_0 = class("LevelContinuousOperationTotalRewardPanel", import("view.level.LevelStageTotalRewardPanel"))

def var_0_0.getUIName(arg_1_0):
	return "LevelContinuousOperationTotalRewardPanel"

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

def var_0_0.didEnter(arg_3_0):
	var_0_0.super.didEnter(arg_3_0)

def var_0_0.UpdateView(arg_4_0):
	var_0_0.super.UpdateView(arg_4_0)
	setActive(arg_4_0.boxView, True)
	setActive(arg_4_0.emptyTip, False)

	local var_4_0 = arg_4_0.contextData.continuousData
	local var_4_1 = var_4_0.GetTotalBattleTime()
	local var_4_2 = arg_4_0.contextData.chapter.GetMaxBattleCount()
	local var_4_3 = math.min(var_4_1, var_4_2)
	local var_4_4 = var_4_3 > 0 and var_4_0.IsActive()

	onButton(arg_4_0, arg_4_0.window.Find("Fixed/ButtonGO"), function()
		if arg_4_0.contextData.spItemID and not (PlayerPrefs.GetInt("autoFight_firstUse_sp", 0) == 1):
			PlayerPrefs.SetInt("autoFight_firstUse_sp", 1)
			PlayerPrefs.Save()

			local function var_5_0()
				arg_4_0.contextData.spItemID = None

				arg_4_0.UpdateSPItem()

			arg_4_0.HandleShowMsgBox({
				hideNo = True,
				content = i18n("autofight_special_operation_tip"),
				onYes = var_5_0,
				onNo = var_5_0
			})

			return

		local var_5_1 = Chapter.GetSPOperationItemCacheKey(arg_4_0.contextData.chapter.id)

		PlayerPrefs.SetInt(var_5_1, arg_4_0.contextData.spItemID or 0)

		if var_4_4:
			getProxy(ChapterProxy).InitContinuousTime(SYSTEM_SCENARIO, var_4_3)

		local var_5_2 = True

		arg_4_0.emit(LevelMediator2.ON_RETRACKING, arg_4_0.contextData.chapter, var_5_2)
		arg_4_0.closeView(), SFX_CONFIRM)

	local var_4_5 = {}
	local var_4_6 = var_4_0.IsActive()

	if var_4_6:
		table.insert(var_4_5, i18n("multiple_sorties_finish"))
	else
		table.insert(var_4_5, i18n("multiple_sorties_stop"))

	setActive(arg_4_0.boxView.Find("Content/TextArea2/Title/Sucess"), var_4_6)
	setActive(arg_4_0.boxView.Find("Content/TextArea2/Title/Failure"), not var_4_6)
	table.insert(var_4_5, i18n("multiple_sorties_main_end", var_4_1, var_4_1 - var_4_0.GetRestBattleTime()))

	if #var_4_5 > 0:
		setText(arg_4_0.boxView.Find("Content/TextArea2/Title/Text"), var_4_5[1])
		setText(arg_4_0.boxView.Find("Content/TextArea2/Detail"), var_4_5[2])

	if var_4_4:
		local var_4_7 = arg_4_0.contextData.chapter.GetRestDailyBonus()

		setActive(arg_4_0.spList, go(arg_4_0.spList).activeSelf and var_4_7 < var_4_3)

	setActive(arg_4_0.window.Find("RetryTimes"), var_4_4)
	setText(arg_4_0.window.Find("RetryTimes/Text"), i18n("multiple_sorties_retry_desc", var_4_3))

def var_0_0.willExit(arg_7_0):
	var_0_0.super.willExit(arg_7_0)

return var_0_0
