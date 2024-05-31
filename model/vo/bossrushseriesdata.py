local var_0_0 = class("BossRushSeriesData", import("model.vo.baseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.activity_series_enemy

var_0_0.ENERGY_WARN = 30
var_0_0.TYPE = {
	EXTRA = 3,
	NORMAL = 1,
	SP = 2
}
var_0_0.MODE = {
	SINGLE = 1,
	MULTIPLE = 2
}

def var_0_0.Ctor(arg_2_0, arg_2_1):
	var_0_0.super.Ctor(arg_2_0, arg_2_1)

	arg_2_0.configId = arg_2_0.id
	arg_2_0.stageLevel = 0
	arg_2_0.battleStatistics = {}

def var_0_0.PassStage(arg_3_0, arg_3_1):
	table.insert(arg_3_0.battleStatistics, arg_3_1)

	arg_3_0.stageLevel = arg_3_0.stageLevel + 1

def var_0_0.GetBattleStatistics(arg_4_0):
	return arg_4_0.battleStatistics

def var_0_0.GetStaegLevel(arg_5_0):
	return arg_5_0.stageLevel

def var_0_0.GetNextStage(arg_6_0):
	return {
		stageId = 1
	}

def var_0_0.GetMode(arg_7_0):
	assert(arg_7_0.mode)

	return arg_7_0.mode

def var_0_0.AddFinalResults(arg_8_0, arg_8_1):
	arg_8_0.battleResults = arg_8_1

def var_0_0.GetFinalResults(arg_9_0):
	return arg_9_0.battleResults

def var_0_0.AddEXScore(arg_10_0, arg_10_1):
	arg_10_0.exScores = arg_10_0.exScores or {}

	table.insert(arg_10_0.exScores, arg_10_1.score)

def var_0_0.GetEXScores(arg_11_0):
	return arg_11_0.exScores or {}

def var_0_0.GetFleets(arg_12_0):
	return (getProxy(FleetProxy).GetBossRushFleets(arg_12_0.actId, arg_12_0.GetFleetIds()))

def var_0_0.GetExpeditionIds(arg_13_0):
	return arg_13_0.getConfig("expedition_id")

def var_0_0.GetFleetIds(arg_14_0):
	if arg_14_0.fleetIds:
		return arg_14_0.fleetIds

	local var_14_0 = arg_14_0.GetExpeditionIds()

	arg_14_0.fleetIds = arg_14_0.StaticCalculateFleetIds(arg_14_0.id, #var_14_0)

	return arg_14_0.fleetIds

def var_0_0.GetType(arg_15_0):
	return arg_15_0.getConfig("type")

def var_0_0.GetPreSeriesId(arg_16_0):
	return arg_16_0.getConfig("pre_chapter")

def var_0_0.IsUnlock(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_0.GetPreSeriesId()

	return var_17_0 == 0 or arg_17_1.HasPassSeries(var_17_0)

def var_0_0.GetSeriesCode(arg_18_0):
	return arg_18_0.getConfig("chapter_name")

def var_0_0.GetName(arg_19_0):
	return arg_19_0.getConfig("name")

def var_0_0.GetLimitations(arg_20_0):
	return arg_20_0.getConfig("limitation")

def var_0_0.GetOilCost(arg_21_0):
	return arg_21_0.getConfig("oil")

def var_0_0.GetDescription(arg_22_0):
	return arg_22_0.getConfig("profiles")

def var_0_0.IsSingleFight(arg_23_0):
	return arg_23_0.getConfig("whether_singlefight") == 1

def var_0_0.GetBossIcons(arg_24_0):
	return arg_24_0.getConfig("boss_icon")

def var_0_0.GetPassAwards(arg_25_0):
	return arg_25_0.getConfig("pass_awards_display")

def var_0_0.GetAdditionalAwards(arg_26_0):
	return arg_26_0.getConfig("additional_awards_display")

def var_0_0.GetDefeatStories(arg_27_0):
	return arg_27_0.getConfig("defeat_story")

def var_0_0.GetDefeatStoriesCount(arg_28_0):
	return arg_28_0.getConfig("defeat_story_count")

def var_0_0.GetMaxBonusCount(arg_29_0):
	return arg_29_0.getConfig("count")

def var_0_0.GetOilLimit(arg_30_0):
	return arg_30_0.getConfig("use_oil_limit")

def var_0_0.GetEXParamater(arg_31_0):
	return arg_31_0.getConfig("ex_count")

def var_0_0.StaticCalculateFleetIds(arg_32_0, arg_32_1):
	assert(arg_32_1 <= 10, "expedition List Too long")

	return _.map(_.range(arg_32_1 + 1), function(arg_33_0)
		return arg_32_0 * 10 + arg_33_0 - 1)

return var_0_0
