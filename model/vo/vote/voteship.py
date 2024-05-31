local var_0_0 = class("VoteShip", import("..BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.voteId = arg_1_2
	arg_1_0.group = arg_1_1.key
	arg_1_0.totalVotes = arg_1_1.value1
	arg_1_0.votes = arg_1_1.value2
	arg_1_0.netVotes = arg_1_1.value3
	arg_1_0.configId = arg_1_0.GenConfigId(arg_1_0.group)

	assert(arg_1_0.configId)

def var_0_0.GenConfigId(arg_2_0, arg_2_1):
	for iter_2_0 = 4, 1, -1:
		local var_2_0 = tonumber(arg_2_1 .. iter_2_0)

		if pg.ship_data_statistics[var_2_0]:
			return var_2_0

def var_0_0.bindConfigTable(arg_3_0):
	return pg.ship_data_statistics

def var_0_0.getRarity(arg_4_0):
	return arg_4_0.getConfig("rarity")

def var_0_0.getShipName(arg_5_0):
	if arg_5_0.group == 30507:
		local var_5_0, var_5_1 = i18n("name_zhanliejahe")

		return var_5_0

	return arg_5_0.getConfig("name")

def var_0_0.getEnName(arg_6_0):
	return arg_6_0.getConfig("english_name")

def var_0_0.getTeamType(arg_7_0):
	return TeamType.GetTeamFromShipType(arg_7_0.getShipType())

def var_0_0.getPainting(arg_8_0):
	local var_8_0 = arg_8_0.getConfig("skin_id")

	return pg.ship_skin_template[var_8_0].painting

def var_0_0.GetDesc(arg_9_0):
	local var_9_0 = arg_9_0.getConfig("skin_id")

	return ShipWordHelper.RawGetWord(var_9_0, ShipWordHelper.WORD_TYPE_PROFILE)

def var_0_0.getShipType(arg_10_0):
	if arg_10_0.IsFunRace():
		return ""
	else
		return (arg_10_0.getConfig("type"))

def var_0_0.getShipTypeName(arg_11_0):
	if arg_11_0.IsFunRace():
		return ""
	else
		local var_11_0 = arg_11_0.getConfig("type")

		return pg.ship_data_by_type[var_11_0].type_name

def var_0_0.IsFunRace(arg_12_0):
	return pg.activity_vote[arg_12_0.voteId].type == VoteConst.RACE_TYPE_FUN

def var_0_0.getNationality(arg_13_0):
	if arg_13_0.IsFunRace():
		return None
	else
		return arg_13_0.getConfig("nationality")

def var_0_0.getNation(arg_14_0):
	return arg_14_0.getNationality()

def var_0_0.IsMatchSearchKey(arg_15_0, arg_15_1):
	if not arg_15_1 or arg_15_1 == "":
		return True

	arg_15_1 = string.lower(string.gsub(arg_15_1, "%.", "%%."))

	return string.find(string.lower(arg_15_0.getShipName()), arg_15_1)

def var_0_0.UpdateVoteCnt(arg_16_0, arg_16_1):
	arg_16_0.votes = arg_16_0.votes + arg_16_1

def var_0_0.getScore(arg_17_0):
	return arg_17_0.votes

def var_0_0.GetTotalScore(arg_18_0):
	return arg_18_0.totalVotes

def var_0_0.isSamaGroup(arg_19_0, arg_19_1):
	return arg_19_0.group == arg_19_1

def var_0_0.GetGameVotes(arg_20_0):
	if arg_20_0.votes >= 100000:
		return math.floor(arg_20_0.votes / 1000) .. "K"
	else
		return arg_20_0.votes

def var_0_0.getTotalVotes(arg_21_0):
	if arg_21_0.totalVotes >= 100000:
		return math.floor(arg_21_0.totalVotes / 1000) .. "K"
	else
		return arg_21_0.totalVotes

return var_0_0
