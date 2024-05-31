ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleClearWave = class("BattleClearWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleClearWave.__name = "BattleClearWave"

local var_0_1 = var_0_0.Battle.BattleClearWave

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.DoWave(arg_2_0)
	var_0_1.super.DoWave(arg_2_0)

	local var_2_0 = var_0_0.Battle.BattleState.GetInstance()
	local var_2_1 = var_2_0:GetProxyByName(var_0_0.Battle.BattleDataProxy.__name)
	local var_2_2 = var_2_0:GetMediatorByName(var_0_0.Battle.BattleSceneMediator.__name)

	var_2_1:KillAllAircraft()
	var_2_1:KillSubmarineByIFF(var_0_0.Battle.BattleConfig.FOE_CODE)
	var_2_2:AllBulletNeutralize()
	arg_2_0:doPass()
end
