local var_0_0 = class("PipeGameVo")

var_0_0.game_id = None
var_0_0.hub_id = None
var_0_0.total_times = None
var_0_0.drop = None
var_0_0.menu_bgm = "story-richang-3"
var_0_0.game_bgm = "story-richang-3"
var_0_0.game_time = 2400000
var_0_0.rule_tip = "pipe_minigame_help"
var_0_0.rank_tip = "pipe_minigame_rank"
var_0_0.game_drag_time = 300
var_0_0.frameRate = Application.targetFrameRate or 60
var_0_0.ui_atlas = "ui/pipegameui_atlas"
var_0_0.game_ui = "PipeGameUI"
var_0_0.SFX_COUNT_DOWN = "event./ui/ddldaoshu2"
var_0_0.SFX_SOUND_FIRE = "event./ui/kaipao"
var_0_0.SFX_SOUND_BOOM = "event./ui/baozha3"
var_0_0.SFX_SOUND_SKILL = "event./ui/chongneng"
var_0_0.SFX_SOUND_ITEM = "event./ui/mini_shine"
var_0_0.use_direct_round = None
var_0_0.gameTime = 0
var_0_0.gameStepTime = 0
var_0_0.deltaTime = 0

def var_0_0.Init(arg_1_0, arg_1_1):
	var_0_0.game_id = arg_1_0
	var_0_0.hub_id = arg_1_1
	var_0_0.total_times = pg.mini_game_hub[var_0_0.hub_id]
	var_0_0.drop = pg.mini_game[var_0_0.game_id].simple_config_data.drop_ids
	var_0_0.total_times = pg.mini_game_hub[var_0_0.hub_id].reward_need

def var_0_0.GetGameTimes():
	return var_0_0.GetMiniGameHubData().count

def var_0_0.GetGameUseTimes():
	return var_0_0.GetMiniGameHubData().usedtime or 0

def var_0_0.GetGameRound():
	if var_0_0.use_direct_round != None:
		return var_0_0.use_direct_round

	if var_0_0.selectRound != None:
		return var_0_0.selectRound

	local var_4_0 = var_0_0.GetGameUseTimes()
	local var_4_1 = var_0_0.GetGameTimes()

	if var_4_1 and var_4_1 > 0:
		return var_4_0 + 1

	if var_4_0 and var_4_0 > 0:
		return var_4_0

	return 1

def var_0_0.GetMiniGameData():
	return getProxy(MiniGameProxy).GetMiniGameData(var_0_0.game_id)

def var_0_0.GetMiniGameHubData():
	return getProxy(MiniGameProxy).GetHubByHubId(var_0_0.hub_id)

var_0_0.scoreNum = 0
var_0_0.roundData = None
var_0_0.selectRound = None
var_0_0.tplItemPool = {}
var_0_0.draging = False
var_0_0.dragScreenPos = Vector2(0, 0)
var_0_0.dragItem = None
var_0_0.gameDragTime = None
var_0_0.startSettlement = False

def var_0_0.Prepare():
	var_0_0.gameTime = var_0_0.game_time
	var_0_0.gameDragTime = var_0_0.game_drag_time
	var_0_0.gameStepTime = 0
	var_0_0.scoreNum = 0
	var_0_0.draging = False
	var_0_0.dragScreenPos = Vector2(0, 0)
	var_0_0.dragItem = None
	var_0_0.roundData = PipeGameConst.game_round[var_0_0.GetGameRound()]
	var_0_0.sceneSpeed = Vector2(0, 0)
	var_0_0.startSettlement = False

def var_0_0.SetGameTpl(arg_8_0):
	var_0_0.tpl = arg_8_0

def var_0_0.GetTplItemFromPool(arg_9_0, arg_9_1):
	if not arg_9_1:
		return None

	if var_0_0.tplItemPool[arg_9_0] == None:
		var_0_0.tplItemPool[arg_9_0] = {}

	if #var_0_0.tplItemPool[arg_9_0] == 0:
		local var_9_0 = tf(instantiate(findTF(var_0_0.tpl, arg_9_0)))

		setParent(var_9_0, arg_9_1)

		return var_9_0
	else
		return table.remove(var_0_0.tplItemPool[arg_9_0], #var_0_0.tplItemPool[arg_9_0])

def var_0_0.RetTplItem(arg_10_0, arg_10_1):
	if var_0_0.tplItemPool[arg_10_0] == None:
		var_0_0.tplItemPool[arg_10_0] = {}

	table.insert(var_0_0.tplItemPool[arg_10_0], arg_10_1)

def var_0_0.GetSprite(arg_11_0):
	return GetSpriteFromAtlas(var_0_0.ui_atlas, arg_11_0)

def var_0_0.GetResultLevel():
	if not var_0_0.scoreNum or var_0_0.scoreNum == 0:
		return 1

	for iter_12_0 = #PipeGameConst.game_result_level, 1, -1:
		if var_0_0.scoreNum >= PipeGameConst.game_result_level[iter_12_0]:
			return iter_12_0

	return 1

def var_0_0.GetRoundData():
	return var_0_0.roundData

def var_0_0.Clear():
	var_0_0.tpl = None
	var_0_0.char = None

return var_0_0
