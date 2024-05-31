local var_0_0 = class("MetaCharacterBreakout", import("..BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.ship_meta_breakout

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.configId = arg_2_0.id
	arg_2_0.needLevel = arg_2_0.getConfig("level")
	arg_2_0.needRepairRate = arg_2_0.getConfig("repair")
	arg_2_0.needItems = {}

	table.insert(arg_2_0.needItems, {
		itemId = arg_2_0.getConfig("item1"),
		count = arg_2_0.getConfig("item1_num")
	})

	arg_2_0.needGold = arg_2_0.getConfig("gold")
	arg_2_0.weaponIds = arg_2_0.getConfig("weapon_ids")
	arg_2_0.breakoutView = arg_2_0.getConfig("breakout_view")

	local var_2_0 = arg_2_0.getConfig("breakout_id")

	if var_2_0 != 0:
		arg_2_0.nextBreakInfo = MetaCharacterBreakout.New({
			id = var_2_0
		})

def var_0_0.getConsume(arg_3_0):
	return arg_3_0.needGold, arg_3_0.needItems

def var_0_0.getLimited(arg_4_0):
	return arg_4_0.needLevel, arg_4_0.needRepairRate

def var_0_0.hasNextInfo(arg_5_0):
	return arg_5_0.nextBreakInfo != None

def var_0_0.getNextInfo(arg_6_0):
	return arg_6_0.nextBreakInfo

def var_0_0.getWeaponIds(arg_7_0):
	return arg_7_0.weaponIds

return var_0_0
