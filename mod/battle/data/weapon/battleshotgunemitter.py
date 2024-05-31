ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = math
local var_0_3 = class("BattleShotgunEmitter", var_0_0.Battle.BattleBulletEmitter)

var_0_0.Battle.BattleShotgunEmitter = var_0_3
var_0_3.__name = "BattleShotgunEmitter"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.Battle.BattleShotgunEmitter.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)

	arg_1_0.PrimalIteration = arg_1_0._nonDelayPrimalIteration

def var_0_3.Fire(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0._angleRange = arg_2_3

	var_0_0.Battle.BattleShotgunEmitter.super.Fire(arg_2_0, arg_2_1, arg_2_2)

def var_0_3.GenerateBullet(arg_3_0):
	local var_3_0 = arg_3_0._convertedDirBarrage[arg_3_0._primalCounter]
	local var_3_1 = var_3_0.OffsetX

	arg_3_0._delay = var_3_0.Delay

	local var_3_2

	if arg_3_0._isRandomAngle:
		var_3_2 = (var_0_2.random() - 0.5) * var_0_2.random(arg_3_0._angleRange) - arg_3_0._angleRange / 2
	else
		var_3_2 = var_0_2.random(arg_3_0._angleRange) - arg_3_0._angleRange / 2

	arg_3_0._spawnFunc(var_3_1, var_3_0.OffsetZ, var_3_2, arg_3_0._offsetPriority, arg_3_0._target, arg_3_0._primalCounter)
	arg_3_0.Interation()
