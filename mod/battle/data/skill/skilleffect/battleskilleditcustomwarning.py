ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillEditCustomWarning", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillEditCustomWarning = var_0_1
var_0_1.__name = "BattleSkillEditCustomWarning"
var_0_1.OP_ADD = 1
var_0_1.OP_REMOVE = 0
var_0_1.OP_REMOVE_PERMANENT = -1
var_0_1.OP_REMOVE_TEMPLATE = -2

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._labelData = {
		op = arg_1_0._tempData.arg_list.op,
		key = arg_1_0._tempData.arg_list.key,
		x = arg_1_0._tempData.arg_list.x,
		y = arg_1_0._tempData.arg_list.y,
		dialogue = arg_1_0._tempData.arg_list.dialogue,
		duration = arg_1_0._tempData.arg_list.duration
	}

def var_0_1.DoDataEffect(arg_2_0):
	arg_2_0.doEditWarning()

def var_0_1.DoDataEffectWithoutTarget(arg_3_0):
	arg_3_0.doEditWarning()

def var_0_1.doEditWarning(arg_4_0):
	var_0_0.Battle.BattleDataProxy.GetInstance().DispatchCustomWarning(arg_4_0._labelData)
