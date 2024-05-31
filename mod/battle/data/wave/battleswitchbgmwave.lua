ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSwitchBGMWave = class("BattleSwitchBGMWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleSwitchBGMWave.__name = "BattleSwitchBGMWave"

local var_0_1 = var_0_0.Battle.BattleSwitchBGMWave

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.SetWaveData(arg_2_0, arg_2_1)
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._bgmName = arg_2_0._param.bgm
end

function var_0_1.DoWave(arg_3_0)
	var_0_1.super.DoWave(arg_3_0)
	pg.BgmMgr.GetInstance():Push(BattleScene.__cname, arg_3_0._bgmName)
	arg_3_0:doPass()
end
