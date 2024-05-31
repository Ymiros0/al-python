ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviourBuff", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourBuff = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviourBuff"

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.SetTemplate(arg_2_0, arg_2_1):
	var_0_3.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._buffID = arg_2_0._tmpData.buff_id
	arg_2_0._buffLevel = arg_2_0._tmpData.level or 1

def var_0_3.doBehaviour(arg_3_0):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0._cldUnitList):
		if iter_3_1.IsAlive():
			local var_3_0 = var_0_0.Battle.BattleBuffUnit.New(arg_3_0._buffID, arg_3_0._buffLevel)

			iter_3_1.AddBuff(var_3_0)

	var_0_3.super.doBehaviour(arg_3_0)
