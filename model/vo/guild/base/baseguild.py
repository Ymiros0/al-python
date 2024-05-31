local var_0_0 = class("BaseGuild", import("...BaseVO"))

def var_0_0.GetTechnologys(arg_1_0):
	assert(False)

def var_0_0.getAddition(arg_2_0, arg_2_1):
	local var_2_0 = 0
	local var_2_1 = GuildConst.TYPE_TO_GROUP[arg_2_1]

	return var_2_0 + arg_2_0.GetTechnologys()[var_2_1].getAddition()

def var_0_0.getMaxOilAddition(arg_3_0):
	return arg_3_0.getAddition(GuildConst.TYPE_OIL_MAX)

def var_0_0.getMaxGoldAddition(arg_4_0):
	return arg_4_0.getAddition(GuildConst.TYPE_GOLD_MAX)

def var_0_0.getCatBoxGoldAddition(arg_5_0):
	return arg_5_0.getAddition(GuildConst.TYPE_CATBOX_GOLD_COST)

def var_0_0.getEquipmentBagAddition(arg_6_0):
	return arg_6_0.getAddition(GuildConst.TYPE_EQUIPMENT_BAG)

def var_0_0.getShipBagAddition(arg_7_0):
	return arg_7_0.getAddition(GuildConst.TYPE_SHIP_BAG)

def var_0_0.getShipAddition(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = 0
	local var_8_1 = arg_8_0.GetTechnologys()

	for iter_8_0, iter_8_1 in pairs(var_8_1):
		var_8_0 = var_8_0 + iter_8_1.GetShipAttrAddition(arg_8_1, arg_8_2)

	return var_8_0

def var_0_0.GetGuildMemberCntAddition(arg_9_0):
	return arg_9_0.getAddition(GuildConst.TYPE_GUILD_MEMBER_CNT)

return var_0_0
