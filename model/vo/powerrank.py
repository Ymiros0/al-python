local var_0_0 = class("PowerRank", import(".PlayerAttire"))

var_0_0.TYPE_POWER = 1
var_0_0.TYPE_COLLECTION = 2
var_0_0.TYPE_PT = 3
var_0_0.TYPE_PLEDGE = 4
var_0_0.TYPE_CHALLENGE = 5
var_0_0.TYPE_EXTRA_CHAPTER = 6
var_0_0.TYPE_ACT_BOSS_BATTLE = 7
var_0_0.TYPE_GUILD_BATTLE = 8
var_0_0.TYPE_MILITARY_RANK = 9
var_0_0.TYPE_BOSSRUSH = 10
var_0_0.typeInfo = {
	{
		title_word = {
			5,
			8,
			7,
			1
		},
		score_icon = {
			"ui/billboardui_atlas",
			"power_icon"
		}
	},
	{
		title_word = {
			5,
			8,
			7,
			2
		}
	},
	{
		title_word = {
			5,
			8,
			7,
			2
		},
		score_icon = {
			"ui/commonui_atlas",
			"pt_icon"
		},
		act_type = ActivityConst.ACTIVITY_TYPE_PT_RANK
	},
	{
		title_word = {
			5,
			8,
			7,
			3
		}
	},
	{
		title_word = {
			5,
			8,
			7,
			4
		},
		act_type = ActivityConst.ACTIVITY_TYPE_CHALLENGE_RANK
	},
	{
		title_word = {
			5,
			8,
			7,
			4
		},
		act_type = ActivityConst.ACTIVITY_TYPE_EXTRA_CHAPTER_RANK
	},
	{
		title_word = {
			5,
			8,
			7,
			10
		},
		act_type = ActivityConst.ACTIVITY_TYPE_BOSS_RANK
	},
	[9] = {
		title_word = {
			5,
			8,
			6,
			9
		},
		score_icon = {
			"ui/billboardui_atlas",
			"rank_icon"
		}
	},
	[10] = {
		title_word = {
			5,
			8,
			7,
			4
		},
		act_type = ActivityConst.ACTIVITY_TYPE_EXTRA_BOSSRUSH_RANK
	}
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.id = arg_1_1.user_id or arg_1_1.id
	arg_1_0.lv = arg_1_1.lv or arg_1_1.level
	arg_1_0.name = arg_1_1.name
	arg_1_0.power = arg_1_1.point or arg_1_1.score or 0
	arg_1_0.rank = arg_1_1.rank or 0
	arg_1_0.arenaRank = math.min(math.max(arg_1_1.arena_rank or 0, 1), 14)

	assert(arg_1_2, "type can not be None")

	arg_1_0.type = arg_1_2

def var_0_0.getPainting(arg_2_0):
	local var_2_0 = pg.ship_skin_template[arg_2_0.skinId]

	return var_2_0 and var_2_0.painting or "unknown"

def var_0_0.setRank(arg_3_0, arg_3_1):
	arg_3_0.rank = arg_3_1

def var_0_0.setArenaRank(arg_4_0, arg_4_1):
	arg_4_0.arenaRank = arg_4_1

def var_0_0.getPowerTxt(arg_5_0):
	if arg_5_0.type == var_0_0.TYPE_POWER:
		return math.floor(arg_5_0.power^0.667)
	elif arg_5_0.type == var_0_0.TYPE_COLLECTION:
		local var_5_0 = getProxy(CollectionProxy).getCollectionTotal()

		return string.format("%0.01f", arg_5_0.power / var_5_0 * 100) .. "%"
	elif arg_5_0.type == var_0_0.TYPE_MILITARY_RANK:
		return arg_5_0.power + SeasonInfo.INIT_POINT
	else
		return arg_5_0.power

def var_0_0.getTitleWord(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = {}

	for iter_6_0 = 1, 4:
		table.insert(var_6_0, i18n("ranking_word_" .. var_0_0.typeInfo[arg_6_1].title_word[iter_6_0]))

	if arg_6_1 == var_0_0.TYPE_PT:
		local var_6_1 = id2ItemId(getProxy(ActivityProxy).getActivityById(arg_6_2).getConfig("config_id"))

		var_6_0[4] = Item.getConfigData(var_6_1).name

	return var_6_0

def var_0_0.getScoreIcon(arg_7_0, arg_7_1):
	return var_0_0.typeInfo[arg_7_1].score_icon

def var_0_0.getActivityByRankType(arg_8_0, arg_8_1):
	if not var_0_0.typeInfo[arg_8_1].act_type:
		return None

	return _.detect(getProxy(ActivityProxy).getActivitiesByType(var_0_0.typeInfo[arg_8_1].act_type), function(arg_9_0)
		return not arg_9_0.isEnd() and (arg_8_1 != var_0_0.TYPE_PT or tonumber(arg_9_0.getConfig("config_data")) > 0))

return var_0_0
