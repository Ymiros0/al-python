ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleDelayWave = class("BattleDelayWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleDelayWave.__name = "BattleDelayWave"

local var_0_1 = var_0_0.Battle.BattleDelayWave

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.SetWaveData(arg_2_0, arg_2_1):
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._duration = arg_2_0._param.timeout

def var_0_1.DoWave(arg_3_0):
	var_0_1.super.DoWave(arg_3_0)

	local var_3_0

	local function var_3_1()
		arg_3_0.doPass()
		pg.TimeMgr.GetInstance().RemoveBattleTimer(var_3_0)

	var_3_0 = pg.TimeMgr.GetInstance().AddBattleTimer("delayWave", 1, arg_3_0._duration, var_3_1, True)
