local var_0_0 = class("GuildTask", import("..BaseVO"))

var_0_0.STATE_EMPTY = 0
var_0_0.STATE_ONGOING = 2
var_0_0.STATE_FINISHED = 3
var_0_0.PRIVATE_TASK_TYPE_EVENT = {
	400
}
var_0_0.PRIVATE_TASK_TYPE_BATTLE = {
	20,
	11
}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id or 0
	arg_1_0.configId = arg_1_0.id
	arg_1_0.progress = arg_1_1.progress or 0

	local var_1_0 = arg_1_1.monday_0clock or 0

	arg_1_0.endTime = 0

	if var_1_0 > 0:
		arg_1_0.endTime = var_1_0 + 604800

def var_0_0.bindConfigTable(arg_2_0):
	return pg.guild_mission_template

def var_0_0.GetLivenessAddition(arg_3_0):
	return arg_3_0.getConfig("guild_active")

def var_0_0.isExpire(arg_4_0):
	return arg_4_0.endTime > 0 and arg_4_0.isEnd()

def var_0_0.getProgress(arg_5_0):
	return arg_5_0.progress

def var_0_0.updateProgress(arg_6_0, arg_6_1):
	arg_6_0.progress = arg_6_1

def var_0_0.isEnd(arg_7_0):
	return pg.TimeMgr.GetInstance().GetServerTime() >= arg_7_0.endTime

def var_0_0.getState(arg_8_0):
	if arg_8_0.id == 0 or arg_8_0.isEnd():
		return var_0_0.STATE_EMPTY
	elif arg_8_0.isFinished():
		return var_0_0.STATE_FINISHED
	else
		return var_0_0.STATE_ONGOING

def var_0_0.GetPresonTaskId(arg_9_0):
	return arg_9_0.getConfig("task_id")

def var_0_0.GetPrivateTaskName(arg_10_0):
	local var_10_0 = arg_10_0.GetPresonTaskId()

	return pg.task_data_template[var_10_0].desc

def var_0_0.IsSamePrivateTask(arg_11_0, arg_11_1):
	return arg_11_1 and arg_11_1.id == arg_11_0.GetPresonTaskId()

def var_0_0.isFinished(arg_12_0):
	return arg_12_0.progress >= arg_12_0.getMaxProgress()

def var_0_0.getMaxProgress(arg_13_0):
	return arg_13_0.getConfig("max_num")

def var_0_0.isRemind(arg_14_0, arg_14_1):
	return arg_14_0.getConfig("warning_time")[arg_14_1] >= pg.TimeMgr.GetInstance().GetServerWeek()

def var_0_0.GetScale(arg_15_0):
	return arg_15_0.getConfig("task_scale")

def var_0_0.GetDesc(arg_16_0):
	return arg_16_0.getConfig("name")

def var_0_0.GetPrivateAward(arg_17_0):
	return arg_17_0.getConfig("award_display")

def var_0_0.GetCaptailAward(arg_18_0):
	return arg_18_0.getConfig("award_capital_display") * arg_18_0.getMaxProgress()

def var_0_0.GetCurrCaptailAward(arg_19_0):
	return arg_19_0.progress * arg_19_0.getConfig("award_capital_display")

def var_0_0.PrivateBeFinished(arg_20_0):
	if var_0_0.STATE_ONGOING == arg_20_0.getState():
		local var_20_0 = arg_20_0.GetPresonTaskId()
		local var_20_1 = getProxy(TaskProxy)
		local var_20_2 = var_20_1.getTaskById(var_20_0) or var_20_1.getFinishTaskById(var_20_0)

		return var_20_2 and var_20_2.isFinish() and not var_20_2.isReceive()

	return False

def var_0_0.SamePrivateTaskType(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_0.GetPresonTaskId()
	local var_21_1 = pg.task_data_template[var_21_0].sub_type

	return _.any(arg_21_1, function(arg_22_0)
		return arg_22_0 == var_21_1)

return var_0_0
