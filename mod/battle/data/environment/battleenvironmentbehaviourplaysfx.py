ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviourPlaySFX", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourPlaySFX = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviourPlaySFX"

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.SetTemplate(arg_2_0, arg_2_1):
	var_0_3.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._sfx = arg_2_0._tmpData.SFX_ID

def var_0_3.doBehaviour(arg_3_0):
	var_0_0.Battle.PlayBattleSFX(arg_3_0._sfx)
	var_0_3.super.doBehaviour(arg_3_0)
