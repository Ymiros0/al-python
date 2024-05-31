ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleJammingWave = class("BattleJammingWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleJammingWave.__name = "BattleJammingWave"

local var_0_1 = var_0_0.Battle.BattleJammingWave

var_0_1.JAMMING_ENGAGE = 1
var_0_1.JAMMING_DODGE = 2

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.DoWave(arg_2_0):
	var_0_1.super.DoWave(arg_2_0)

	local var_2_0 = var_0_0.Battle.BattleDataProxy.GetInstance()
	local var_2_1 = var_2_0.GetInitData().KizunaJamming

	if var_2_1 and table.contains(var_2_1, var_0_1.JAMMING_ENGAGE):
		var_2_0.KizunaJamming()

	arg_2_0.doFinish()
