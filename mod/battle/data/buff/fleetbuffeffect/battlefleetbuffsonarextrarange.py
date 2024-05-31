ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleFleetBuffSonarExtraRange = class("BattleFleetBuffSonarExtraRange", var_0_0.Battle.BattleFleetBuffEffect)
var_0_0.Battle.BattleFleetBuffSonarExtraRange.__name = "BattleFleetBuffSonarExtraRange"

local var_0_1 = var_0_0.Battle.BattleFleetBuffSonarExtraRange

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._extraRange = arg_2_0._tempData.arg_list.range

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.appendRange(arg_3_1)

def var_0_1.onStack(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.appendRange(arg_4_1)

def var_0_1.appendRange(arg_5_0, arg_5_1):
	arg_5_1.GetFleetSonar().AppendExtraSkillRange(arg_5_0._extraRange)
