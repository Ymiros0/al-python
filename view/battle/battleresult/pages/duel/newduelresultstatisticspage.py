local var_0_0 = class("NewDuelResultStatisticsPage", import("..NewBattleResultStatisticsPage"))

def var_0_0.UpdatePlayer(arg_1_0):
	local var_1_0 = getProxy(PlayerProxy).getRawData()

	arg_1_0.playerName.text = var_1_0.GetName()

	local var_1_1 = getProxy(MilitaryExerciseProxy).getSeasonInfo()
	local var_1_2 = SeasonInfo.getMilitaryRank(var_1_1.score, var_1_1.rank)
	local var_1_3, var_1_4 = SeasonInfo.getNextMilitaryRank(var_1_1.score, var_1_1.rank)

	arg_1_0.playerLv.text = var_1_2.name
	arg_1_0.playerExpLabel.text = i18n("word_rankScore")

	local function var_1_5()
		arg_1_0.playerExp.text = "+" .. NewBattleResultUtil.GetSeasonScoreOffset(arg_1_0.contextData.oldRank, var_1_1)
		arg_1_0.playerExpBar.fillAmount = var_1_1.score / var_1_4

	if not arg_1_0.contextData.autoSkipFlag:
		arg_1_0.duelAniamtion = NewBattleResultDuelAniamtion.New(arg_1_0.playerExp, arg_1_0.playerExpBar, var_1_4, arg_1_0.contextData.oldRank, var_1_1)

		arg_1_0.duelAniamtion.SetUp(var_1_5)
	else
		var_1_5()

def var_0_0.UpdateChapterName(arg_3_0):
	local var_3_0 = arg_3_0.contextData
	local var_3_1 = getProxy(MilitaryExerciseProxy).getPreRivalById(var_3_0.rivalId or 0)
	local var_3_2 = var_3_1 and var_3_1.name or ""

	arg_3_0.chapterName.text = var_3_2

	setActive(arg_3_0.opBonus, False)

def var_0_0.OnDestroy(arg_4_0):
	var_0_0.super.OnDestroy(arg_4_0)

	if arg_4_0.duelAniamtion:
		arg_4_0.duelAniamtion.Dispose()

		arg_4_0.duelAniamtion = None

return var_0_0
