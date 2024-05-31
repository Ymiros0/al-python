ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst

var_0_0.Battle.EngageAntiSubState = class("EngageAntiSubState", var_0_0.Battle.IAntiSubState)
var_0_0.Battle.EngageAntiSubState.__name = "EngageAntiSubState"

local var_0_2 = var_0_0.Battle.EngageAntiSubState

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0)

def var_0_2.OnVigilantEngage(arg_2_0, arg_2_1):
	return

def var_0_2.OnMineExplode(arg_3_0, arg_3_1):
	return

def var_0_2.OnSubmarinFloat(arg_4_0, arg_4_1):
	return

def var_0_2.ToPreLevel(arg_5_0, arg_5_1):
	arg_5_1.OnVigilantState()

def var_0_2.OnHateChain(arg_6_0):
	return

def var_0_2.GetWeaponUseable(arg_7_0):
	return {
		var_0_1.OXY_STATE.FLOAT
	}

def var_0_2.CanDecay(arg_8_0):
	return True

def var_0_2.GetWarnMark(arg_9_0):
	return 3

def var_0_2.GetMeterSpeed(arg_10_0):
	return 5

def var_0_2.DecayDuration(arg_11_0):
	return 3
