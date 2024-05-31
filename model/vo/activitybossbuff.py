local var_0_0 = class("ActivityBossBuff", import("model.vo.BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.worldboss_bufflist

def var_0_0.GetConfigID(arg_2_0):
	return arg_2_0.configId

def var_0_0.GetIcon(arg_3_0):
	return arg_3_0.getConfig("buff_icon")

def var_0_0.GetIconPath(arg_4_0):
	return "activitybossbuff/" .. arg_4_0.getConfig("buff_icon")

def var_0_0.GetName(arg_5_0):
	return arg_5_0.getConfig("name")

def var_0_0.GetDesc(arg_6_0):
	return arg_6_0.getConfig("desc")

def var_0_0.CastOnEnemy(arg_7_0):
	return arg_7_0.getConfig("buff_target") == 1

def var_0_0.GetBuffID(arg_8_0):
	return arg_8_0.getConfig("lua_id")

def var_0_0.GetBonus(arg_9_0):
	return tonumber(arg_9_0.getConfig("bonus"))

def var_0_0.GetBonusText(arg_10_0):
	return math.floor(arg_10_0.GetBonus() * 100) .. "%"

return var_0_0
