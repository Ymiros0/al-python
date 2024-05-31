local var_0_0 = class("ActivityBossConfig", import("model.vo.BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.activity_event_worldboss

def var_0_0.GetConfigID(arg_2_0):
	return arg_2_0.configId

def var_0_0.Ctor(arg_3_0, arg_3_1):
	var_0_0.super.Ctor(arg_3_0, arg_3_1)

	local var_3_0 = arg_3_0.getConfig("extrachallenge_id")

	if var_3_0 > 0:
		arg_3_0.spEnemy = ActivityBossSPEnemy.New({
			configId = var_3_0
		})

def var_0_0.GetTicketID(arg_4_0):
	return arg_4_0.getConfig("ticket")

def var_0_0.GetBattleTime(arg_5_0):
	return arg_5_0.getConfig("time")

def var_0_0.GetNormalStageIDs(arg_6_0):
	return arg_6_0.getConfig("normal_expedition")

def var_0_0.GetEXStageID(arg_7_0):
	return arg_7_0.getConfig("ex_expedition")

def var_0_0.GetOilLimits(arg_8_0):
	return arg_8_0.getConfig("use_oil_limit")

def var_0_0.GetBossID(arg_9_0):
	return arg_9_0.getConfig("boss_id")[1]

def var_0_0.GetMilestoneRewards(arg_10_0):
	local var_10_0 = arg_10_0.GetBossID()

	return AcessWithinNull(pg.extraenemy_template[var_10_0], "reward_display") or {}

def var_0_0.GetInitTicketPools(arg_11_0):
	return arg_11_0.getConfig("normal_expedition_drop_num")

def var_0_0.GetSPEnemy(arg_12_0):
	return arg_12_0.spEnemy

def var_0_0.GetSPStageID(arg_13_0):
	if not arg_13_0.spEnemy:
		return

	return arg_13_0.spEnemy.GetExtraStageId()

return var_0_0
