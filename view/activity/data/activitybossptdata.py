local var_0_0 = class("ActivityBossPtData", import(".ActivityPtData"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	local var_1_0 = arg_1_1.getDataConfig("link_id")
	local var_1_1 = getProxy(ActivityProxy).getActivityById(var_1_0).getConfig("config_id")
	local var_1_2 = pg.activity_event_worldboss[var_1_1]

	assert(var_1_2, "miss activity_event_worldboss config, ID. " .. var_1_1)

	arg_1_0.linkID = var_1_0
	arg_1_0.progress_target = var_1_2.reward_pt

def var_0_0.GetBossProgress(arg_2_0):
	local var_2_0 = arg_2_0.getTargetLevel()
	local var_2_1 = getProxy(ActivityProxy).getActivityById(arg_2_0.linkID)
	local var_2_2 = 0

	if var_2_1 and not var_2_1.isEnd():
		var_2_2 = var_2_1.GetBossHP() or 0

	return var_2_2, arg_2_0.progress_target[var_2_0]

def var_0_0.CanGetAward(arg_3_0):
	local function var_3_0()
		local var_4_0, var_4_1, var_4_2 = arg_3_0.GetResProgress()

		return var_4_2 >= 1

	local var_3_1, var_3_2 = arg_3_0.GetBossProgress()

	return arg_3_0.CanGetNextAward() and var_3_0() and var_3_1 <= var_3_2

return var_0_0
