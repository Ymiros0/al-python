local var_0_0 = class("ActivityBossSPEnemy", import("model.vo.BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.extraenemy_challenge_template

def var_0_0.GetConfigID(arg_2_0):
	return arg_2_0.configId

def var_0_0.GetScoreTargets(arg_3_0):
	return arg_3_0.getConfig("ex_challenge_target")

def var_0_0.GetRewards(arg_4_0):
	return arg_4_0.getConfig("ex_challenge_reward")

def var_0_0.GetSelectableBuffs(arg_5_0):
	return arg_5_0.getConfig("ex_challenge_buff")

def var_0_0.GetExtraStageId(arg_6_0):
	return arg_6_0.getConfig("ex_challenge_enemy")

return var_0_0
