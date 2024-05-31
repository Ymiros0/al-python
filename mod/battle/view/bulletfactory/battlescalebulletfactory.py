ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.UnitType

var_0_0.Battle.BattleScaleBulletFactory = singletonClass("BattleScaleBulletFactory", var_0_0.Battle.BattleCannonBulletFactory)
var_0_0.Battle.BattleScaleBulletFactory.__name = "BattleScaleBulletFactory"

local var_0_2 = var_0_0.Battle.BattleScaleBulletFactory

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0)

def var_0_2.MakeBullet(arg_2_0):
	return var_0_0.Battle.BattleScaleBullet.New()
