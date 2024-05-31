ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.ActionName

var_0_0.Battle.MoveLeftState = class("MoveLeftState", var_0_0.Battle.IUnitState)
var_0_0.Battle.MoveLeftState.__name = "MoveLeftState"

local var_0_2 = var_0_0.Battle.MoveLeftState

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor()

def var_0_2.AddIdleState(arg_2_0, arg_2_1, arg_2_2):
	arg_2_1.OnIdleState()

def var_0_2.AddMoveState(arg_3_0, arg_3_1, arg_3_2):
	arg_3_1.OnMoveState()

def var_0_2.AddMoveLeftState(arg_4_0, arg_4_1, arg_4_2):
	return

def var_0_2.AddAttackState(arg_5_0, arg_5_1, arg_5_2):
	arg_5_1.OnAttackLeftState(arg_5_2)

def var_0_2.AddDeadState(arg_6_0, arg_6_1, arg_6_2):
	arg_6_1.OnDeadState()

def var_0_2.AddSkillState(arg_7_0, arg_7_1, arg_7_2):
	return

def var_0_2.AddSpellState(arg_8_0, arg_8_1, arg_8_2):
	arg_8_1.OnSpellState()

def var_0_2.AddVictoryState(arg_9_0, arg_9_1, arg_9_2):
	arg_9_1.OnVictoryState()

def var_0_2.AddVictorySwimState(arg_10_0, arg_10_1, arg_10_2):
	arg_10_1.OnVictorySwimState()

def var_0_2.AddStandState(arg_11_0, arg_11_1, arg_11_2):
	return

def var_0_2.AddDiveState(arg_12_0, arg_12_1, arg_12_2):
	arg_12_1.OnDiveState()

def var_0_2.AddDiveLeftState(arg_13_0, arg_13_1, arg_13_2):
	arg_13_1.OnDiveLeftState()

def var_0_2.AddInterruptState(arg_14_0, arg_14_1, arg_14_2):
	arg_14_1.OnInterruptState()

def var_0_2.AddDivingState(arg_15_0, arg_15_1, arg_15_2):
	arg_15_1.OnDivingState()

def var_0_2.AddSkillStartState(arg_16_0, arg_16_1, arg_16_2):
	arg_16_1.OnSkillStartState()

def var_0_2.AddSkillEndState(arg_17_0, arg_17_1, arg_17_2):
	return

def var_0_2.OnTrigger(arg_18_0, arg_18_1):
	return

def var_0_2.OnStart(arg_19_0, arg_19_1):
	return

def var_0_2.OnEnd(arg_20_0, arg_20_1):
	return

def var_0_2.CacheWeapon(arg_21_0):
	return True

def var_0_2.FreshActionKeyOffset(arg_22_0):
	return True

def var_0_2.GetActionName(arg_23_0, arg_23_1):
	local var_23_0 = var_0_1.MOVELEFT
	local var_23_1 = arg_23_1.ActionKeyOffset()

	if var_23_1:
		var_23_0 = var_23_0 .. var_23_1

	return var_23_0
