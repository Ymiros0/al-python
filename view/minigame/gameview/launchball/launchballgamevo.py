local var_0_0 = class("LaunchBallGameVo")

var_0_0.game_id = None
var_0_0.hub_id = None
var_0_0.total_times = None
var_0_0.drop = None
var_0_0.game_bgm = "cw-story"
var_0_0.game_time = 60000
var_0_0.rule_tip = "launchball_minigame_help"
var_0_0.frameRate = Application.targetFrameRate or 60
var_0_0.ui_atlas = "ui/minigameui/launchballgameui_atlas"
var_0_0.game_ui = "LaunchBallGameUI"
var_0_0.SFX_COUNT_DOWN = "event./ui/ddldaoshu2"
var_0_0.launchball_minigame_select = "launchball_minigame_select"
var_0_0.launchball_minigame_un_select = "launchball_minigame_un_select"
var_0_0.SFX_PRESS_SKILL = "ui-maoudamashii"
var_0_0.SFX_FIRE = "ui-mini_throw"
var_0_0.SFX_ENEMY_REMOVE = "ui-mini_pigu"
var_0_0.enemyToEndRate = None
var_0_0.gameTime = 0
var_0_0.gameStepTime = 0
var_0_0.deltaTime = 0

def var_0_0.Init(arg_1_0, arg_1_1):
	var_0_0.game_id = arg_1_0
	var_0_0.hub_id = arg_1_1
	var_0_0.total_times = pg.mini_game_hub[var_0_0.hub_id]
	var_0_0.drop = pg.mini_game[var_0_0.game_id].simple_config_data.drop_ids
	var_0_0.total_times = pg.mini_game_hub[var_0_0.hub_id].reward_need

def var_0_0.initRoundData(arg_2_0, arg_2_1):
	local var_2_0 = LaunchBallGameConst.game_round

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		if iter_2_1.type == arg_2_0 and iter_2_1.type_index == arg_2_1:
			var_0_0.gameRoundData = iter_2_1

			if iter_2_1.player_id:
				var_0_0.SetPlayer(iter_2_1.player_id)

def var_0_0.SetPlayer(arg_3_0):
	var_0_0.selectPlayer = arg_3_0

def var_0_0.GetGameTimes():
	return var_0_0.GetMiniGameHubData().count

def var_0_0.GetGameUseTimes():
	return var_0_0.GetMiniGameHubData().usedtime or 0

def var_0_0.GetGameRound():
	local var_6_0 = var_0_0.GetGameUseTimes()
	local var_6_1 = var_0_0.GetGameTimes()

	if var_6_1 and var_6_1 > 0:
		return var_6_0 + 1
	else
		return var_6_0

def var_0_0.GetMiniGameData():
	return getProxy(MiniGameProxy).GetMiniGameData(var_0_0.game_id)

def var_0_0.GetMiniGameHubData():
	return getProxy(MiniGameProxy).GetHubByHubId(var_0_0.hub_id)

var_0_0.scoreNum = 0
var_0_0.joyStickData = None
var_0_0.amulet = None
var_0_0.gameRoundData = None
var_0_0.selectPlayer = None
var_0_0.pressSkill = None
var_0_0.buffs = None
var_0_0.base_score = 10
var_0_0.series_score = 10
var_0_0.enemyColors = {}
var_0_0.enemyStopTime = None

def var_0_0.Prepare():
	var_0_0.gameTime = var_0_0.game_time
	var_0_0.gameStepTime = 0
	var_0_0.scoreNum = 0
	var_0_0.enemyStopTime = None
	var_0_0.gameResultData = {
		mix_count = 0,
		skill_count = 0,
		use_pass_skill = 0,
		pass_skill_count = 0,
		double_pass_skill_time = 0,
		many_count = 0,
		round = 0,
		player = 0,
		double_skill_time = 0,
		use_skill = 0,
		series_count = 0,
		split_count = 0,
		over_count = 0
	}

var_0_0.result_split_count = "split_count"
var_0_0.result_round = "round"
var_0_0.result_player = "player"
var_0_0.result_series_count = "series_count"
var_0_0.result_over_count = "over_count"
var_0_0.result_many_count = "many_count"
var_0_0.result_mix_count = "mix_count"
var_0_0.result_use_skill = "use_skill"
var_0_0.result_use_pass_skill = "use_pass_skill"
var_0_0.result_skill_count = "skill_count"
var_0_0.result_pass_skill_count = "pass_skill_count"
var_0_0.reuslt_double_skill_time = "double_skill_time"
var_0_0.reuslt_double_pass_skill_time = "double_pass_skill_time"

def var_0_0.UpdateGameResultData(arg_10_0, arg_10_1):
	print(arg_10_0 .. "  update count  = " .. arg_10_1)

	if arg_10_0 == var_0_0.reuslt_double_skill_time:
		arg_10_1 = math.floor(arg_10_1)

		if var_0_0.gameResultData[arg_10_0] != 0:
			if arg_10_1 < var_0_0.gameResultData[arg_10_0]:
				var_0_0.gameResultData[arg_10_0] = arg_10_1
		else
			var_0_0.gameResultData[arg_10_0] = arg_10_1
	elif arg_10_0 == var_0_0.result_skill_count:
		if var_0_0.gameResultData[arg_10_0] and arg_10_1 > var_0_0.gameResultData[arg_10_0]:
			var_0_0.gameResultData[arg_10_0] = arg_10_1
	else
		var_0_0.gameResultData[arg_10_0] = arg_10_1

def var_0_0.AddGameResultData(arg_11_0, arg_11_1):
	var_0_0.gameResultData[arg_11_0] = var_0_0.gameResultData[arg_11_0] + arg_11_1

def var_0_0.GetBuff(arg_12_0):
	if var_0_0.buffs and #var_0_0.buffs > 0:
		for iter_12_0, iter_12_1 in ipairs(var_0_0.buffs):
			if iter_12_1.data.type == arg_12_0:
				return iter_12_1

	return None

def var_0_0.GetScore(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0 = 0
	local var_13_1 = arg_13_0 * var_0_0.base_score

	if arg_13_3 and arg_13_3 > 0:
		var_13_1 = var_13_1 + arg_13_3 * var_0_0.base_score

	if arg_13_2:
		var_13_1 = var_13_1 + var_0_0.base_score

	if arg_13_0 > 3:
		var_13_1 = var_13_1 + (arg_13_0 - 3) * 10

	if arg_13_1 > 1:
		var_13_1 = var_13_1 + (arg_13_1 - 1) * var_0_0.series_score

	return var_13_1

def var_0_0.Sign(arg_14_0, arg_14_1, arg_14_2):
	return (arg_14_0.x - arg_14_2.x) * (arg_14_1.y - arg_14_2.y) - (arg_14_1.x - arg_14_2.x) * (arg_14_0.y - arg_14_2.y)

def var_0_0.PointInRect(arg_15_0, arg_15_1, arg_15_2, arg_15_3, arg_15_4):
	local var_15_0
	local var_15_1
	local var_15_2
	local var_15_3
	local var_15_4
	local var_15_5
	local var_15_6 = var_0_0.Sign(arg_15_0, arg_15_1, arg_15_2)
	local var_15_7 = var_0_0.Sign(arg_15_0, arg_15_2, arg_15_3)
	local var_15_8 = var_0_0.Sign(arg_15_0, arg_15_3, arg_15_4)
	local var_15_9 = var_0_0.Sign(arg_15_0, arg_15_4, arg_15_1)
	local var_15_10 = var_15_6 < 0 or var_15_7 < 0 or var_15_8 < 0 or var_15_9 < 0
	local var_15_11 = var_15_6 > 0 or var_15_7 > 0 or var_15_8 > 0 or var_15_9 > 0

	return not var_15_10 or not var_15_11

return var_0_0
