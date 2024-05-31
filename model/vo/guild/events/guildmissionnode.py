local var_0_0 = class("GuildMissionNode", import("...BaseVO"))

var_0_0.STATE_DOING = 0
var_0_0.STATE_SUCCESS = 1
var_0_0.STATE_FAILED = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.node_id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.position = arg_1_1.position
	arg_1_0.status = arg_1_1.status

def var_0_0.bindConfigTable(arg_2_0):
	return pg.guild_event_node

def var_0_0.GetPosition(arg_3_0):
	return arg_3_0.position

def var_0_0.IsFinish(arg_4_0):
	return arg_4_0.status > 0

def var_0_0.IsSuccess(arg_5_0):
	return arg_5_0.status > var_0_0.STATE_SUCCESS

def var_0_0.GetIcon(arg_6_0):
	return arg_6_0.getConfig("icon")

def var_0_0.GetAwards(arg_7_0):
	if arg_7_0.status == var_0_0.STATE_SUCCESS:
		return arg_7_0.getConfig("success_award")
	elif arg_7_0.status == var_0_0.STATE_FAILED:
		return arg_7_0.getConfig("fail_award")

def var_0_0.GetLog(arg_8_0):
	if arg_8_0.status == var_0_0.STATE_SUCCESS or arg_8_0.status == var_0_0.STATE_FAILED:
		local var_8_0 = arg_8_0.GetAwards()
		local var_8_1 = getDropInfo(var_8_0)
		local var_8_2 = arg_8_0.getConfig("fail_describe")

		if arg_8_0.status == var_0_0.STATE_SUCCESS:
			var_8_2 = arg_8_0.getConfig("success_describe")

		return string.gsub(var_8_2, "$1", var_8_1)

def var_0_0.IsItemType(arg_9_0):
	return arg_9_0.getConfig("item") == "box"

def var_0_0.IsBattleType(arg_10_0):
	return arg_10_0.getConfig("item") == "sairendanchuan"

return var_0_0
