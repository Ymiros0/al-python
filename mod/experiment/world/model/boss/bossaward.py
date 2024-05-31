local var_0_0 = class("BossAward", import("....BaseEntity"))

var_0_0.Fields = {
	bossId = "number",
	config = "table",
	rank = "number",
	level = "number",
	acceptTime = "number",
	duetime = "number"
}

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.bossId = arg_1_1.bossId
	arg_1_0.config = pg.world_joint_boss_template[arg_1_0.bossId]
	arg_1_0.level = arg_1_1.level
	arg_1_0.rank = arg_1_1.rank
	arg_1_0.duetime = arg_1_1.duetime
	arg_1_0.acceptTime = arg_1_1.accept_time or 0

def var_0_0.IsReceived(arg_2_0):
	return arg_2_0.acceptTime > 0

def var_0_0.GetAwards(arg_3_0):
	return arg_3_0.config.drop_show

def var_0_0.IsExpired(arg_4_0):
	return pg.TimeMgr.GetInstance().GetServerTime() >= arg_4_0.duetime

def var_0_0.GetExpiredTime(arg_5_0, ...):
	return arg_5_0.duetime

def var_0_0.GetBossName(arg_6_0):
	return arg_6_0.config.name

def var_0_0.GetRank(arg_7_0):
	return arg_7_0.rank

return var_0_0
