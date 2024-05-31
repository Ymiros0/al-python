ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleLabelWave = class("BattleLabelWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleLabelWave.__name = "BattleLabelWave"

local var_0_1 = var_0_0.Battle.BattleLabelWave

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.SetWaveData(arg_2_0, arg_2_1):
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._labelData = {
		op = arg_2_0._param.op,
		key = arg_2_0._param.key,
		x = arg_2_0._param.x,
		y = arg_2_0._param.y,
		dialogue = arg_2_0._param.dialogue,
		duration = arg_2_0._param.duration
	}

def var_0_1.DoWave(arg_3_0):
	var_0_1.super.DoWave(arg_3_0)
	var_0_0.Battle.BattleState.GetInstance().GetProxyByName(var_0_0.Battle.BattleDataProxy.__name).DispatchCustomWarning(arg_3_0._labelData)
	arg_3_0.doPass()
