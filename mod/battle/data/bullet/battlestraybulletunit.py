ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleStrayBulletUnit = class("BattleStrayBulletUnit", var_0_0.Battle.BattleBulletUnit)
var_0_0.Battle.BattleStrayBulletUnit.__name = "BattleStrayBulletUnit"

local var_0_1 = var_0_0.Battle.BattleStrayBulletUnit

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

def var_0_1.SetExplodePosition(arg_2_0, arg_2_1):
	arg_2_0._explodePos = arg_2_1

def var_0_1.GetExplodePostion(arg_3_0):
	return arg_3_0._explodePos
