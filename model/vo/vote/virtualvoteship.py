local var_0_0 = class("VirtualVoteShip", import(".VoteShip"))

def var_0_0.GenConfigId(arg_1_0, arg_1_1):
	return arg_1_1

def var_0_0.bindConfigTable(arg_2_0):
	return pg.activity_vote_virtual_ship_data

def var_0_0.getRarity(arg_3_0):
	return arg_3_0.getConfig("rarity")

def var_0_0.getShipName(arg_4_0):
	return arg_4_0.getConfig("name")

def var_0_0.getEnName(arg_5_0):
	return arg_5_0.getConfig("english_name")

def var_0_0.getTeamType(arg_6_0):
	return TeamType.GetTeamFromShipType(arg_6_0.getShipType())

def var_0_0.getPainting(arg_7_0):
	return arg_7_0.getConfig("painting")

def var_0_0.GetDesc(arg_8_0):
	return arg_8_0.getConfig("desc")

def var_0_0.getShipType(arg_9_0):
	return ""

def var_0_0.getNationality(arg_10_0):
	return None

return var_0_0
