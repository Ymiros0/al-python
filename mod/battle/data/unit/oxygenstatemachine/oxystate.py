ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleConst

var_0_0.Battle.OxyState = class("OxyState")
var_0_0.Battle.OxyState.__name = "OxyState"

local var_0_3 = var_0_0.Battle.OxyState

var_0_3.STATE_IDLE = "STATE_IDLE"
var_0_3.STATE_DIVE = "STATE_DIVE"
var_0_3.STATE_FLOAT = "STATE_FLOAT"
var_0_3.STATE_RAID = "STATE_RAID"
var_0_3.STATE_RETREAT = "STATE_RETREAT"
var_0_3.STATE_FREE_DIVE = "STATE_FREE_DIVE"
var_0_3.STATE_FREE_FLOAT = "STATE_FREE_FLOAT"
var_0_3.STATE_FREE_BENCH = "STATE_FREE_BENCH"
var_0_3.STATE_DEEP_MINE = "STATE_DEEP_MINE"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._target = arg_1_1
	arg_1_0._idleState = var_0_0.Battle.IdleOxyState.New()
	arg_1_0._diveState = var_0_0.Battle.DiveOxyState.New()
	arg_1_0._floatState = var_0_0.Battle.FloatOxyState.New()
	arg_1_0._raidState = var_0_0.Battle.RaidOxyState.New()
	arg_1_0._retreatState = var_0_0.Battle.RetreatOxyState.New()
	arg_1_0._freeDiveState = var_0_0.Battle.FreeDiveOxyState.New()
	arg_1_0._freeFloatState = var_0_0.Battle.FreeFloatOxyState.New()
	arg_1_0._freeBenchState = var_0_0.Battle.FreeBenchOxyState.New()
	arg_1_0._deepMineState = var_0_0.Battle.DeepMineOxyState.New()

	local var_1_0 = var_0_0.Battle.BattleBuffUnit.New(8520)

	arg_1_0._target.AddBuff(var_1_0)
	arg_1_0.OnIdleState()

def var_0_3.SetRecycle(arg_2_0, arg_2_1):
	arg_2_0._recycle = arg_2_1

def var_0_3.SetBubbleTemplate(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0._bubbleInitial = arg_3_1 or 0
	arg_3_0._bubbleInterval = arg_3_2 or 0
	arg_3_0._bubbleTimpStamp = None

def var_0_3.UpdateOxygen(arg_4_0):
	arg_4_0._currentState.DoUpdateOxy(arg_4_0)

def var_0_3.GetNextBubbleStamp(arg_5_0):
	if arg_5_0._currentState.GetBubbleFlag():
		if arg_5_0._target.GetPosition().x < arg_5_0._bubbleInitial and arg_5_0._bubbleTimpStamp == None:
			arg_5_0._bubbleTimpStamp = 0

		return arg_5_0._bubbleTimpStamp
	else
		return None

def var_0_3.SetForceExpose(arg_6_0, arg_6_1):
	arg_6_0._forceExpose = arg_6_1

	arg_6_0._target.SetForceVisible()

def var_0_3.GetForceExpose(arg_7_0):
	return arg_7_0._forceExpose

def var_0_3.FlashBubbleStamp(arg_8_0, arg_8_1):
	arg_8_0._bubbleTimpStamp = arg_8_1 + arg_8_0._bubbleInterval

def var_0_3.ChangeState(arg_9_0, arg_9_1, arg_9_2):
	if arg_9_1 == var_0_3.STATE_IDLE:
		arg_9_0.OnIdleState()
	elif arg_9_1 == var_0_3.STATE_DIVE:
		arg_9_0.OnDiveState()
	elif arg_9_1 == var_0_3.STATE_FLOAT:
		arg_9_0.OnFloatState()
	elif arg_9_1 == var_0_3.STATE_RAID:
		arg_9_0.OnRaidState()
	elif arg_9_1 == var_0_3.STATE_RETREAT:
		arg_9_0.OnRetreatState()
	elif arg_9_1 == var_0_3.STATE_FREE_DIVE:
		arg_9_0.OnFreeDiveState()
	elif arg_9_1 == var_0_3.STATE_FREE_FLOAT:
		arg_9_0.OnFreeFloatState()
	elif arg_9_1 == var_0_3.STATE_FREE_BENCH:
		arg_9_0.OnFreeBenchState()
	elif arg_9_1 == var_0_3.STATE_DEEP_MINE:
		arg_9_0.OnDeepMineState()
	else
		assert(False, arg_9_0._target.__name .. "'s oxygen state machine, unexcepted state. " .. arg_9_1)

	arg_9_0._target.GetCldData().Surface = arg_9_0._currentState.GetDiveState()

def var_0_3.OxyConsume(arg_10_0):
	arg_10_0._target.OxyConsume()

def var_0_3.OxyRecover(arg_11_0, arg_11_1):
	arg_11_0._target.OxyRecover(arg_11_1)

def var_0_3.OnIdleState(arg_12_0):
	arg_12_0._currentState = arg_12_0._idleState

def var_0_3.OnDiveState(arg_13_0):
	local var_13_0 = arg_13_0._currentState.UpdateDive()
	local var_13_1 = arg_13_0._currentState

	arg_13_0._currentState = arg_13_0._diveState

	arg_13_0._currentState.UpdateCldData(arg_13_0._target, var_13_1)
	arg_13_0._target.ChangeWeaponDiveState()
	arg_13_0._target.SetCrash(False)
	arg_13_0._target.SetAI(var_0_1.SUB_DEFAULT_ENGAGE_AI)

	if var_13_0:
		arg_13_0._target.SetDiveInvisible(True)

	arg_13_0._target.StateChange(var_0_0.Battle.UnitState.STATE_DIVE)
	arg_13_0._target.TriggerBuff(var_0_2.BuffEffectType.ON_SUBMARINE_DIVE, {})
	arg_13_0._target.RemoveBuff(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF)
	arg_13_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF))

def var_0_3.OnFloatState(arg_14_0):
	local var_14_0 = arg_14_0._currentState

	arg_14_0._currentState = arg_14_0._floatState

	arg_14_0._currentState.UpdateCldData(arg_14_0._target, var_14_0)
	arg_14_0._target.ChangeWeaponDiveState()
	arg_14_0._target.SetDiveInvisible(False)
	arg_14_0._target.StateChange(var_0_0.Battle.UnitState.STATE_MOVE)
	arg_14_0._target.RemoveSonarExpose()
	arg_14_0._target.PlayFX("qianting_chushui", False)
	arg_14_0._target.TriggerBuff(var_0_2.BuffEffectType.ON_SUBMARINE_FLOAT, {})
	arg_14_0._target.RemoveBuff(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF)
	arg_14_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF))

def var_0_3.OnRaidState(arg_15_0):
	local var_15_0 = arg_15_0._currentState.UpdateDive()
	local var_15_1 = arg_15_0._currentState

	arg_15_0._currentState = arg_15_0._raidState

	arg_15_0._currentState.UpdateCldData(arg_15_0._target, var_15_1)
	arg_15_0._target.ChangeWeaponDiveState()

	if var_15_0:
		arg_15_0._target.SetDiveInvisible(True)

	arg_15_0._target.SetAI(var_0_1.SUB_DEFAULT_STAY_AI)
	arg_15_0._target.TriggerBuff(var_0_2.BuffEffectType.ON_SUBMARINE_RAID, {})
	arg_15_0._target.RemoveBuff(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF)
	arg_15_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF))

def var_0_3.OnRetreatState(arg_16_0):
	local var_16_0 = arg_16_0._currentState

	arg_16_0._currentState = arg_16_0._retreatState

	arg_16_0._currentState.UpdateCldData(arg_16_0._target, var_16_0)
	arg_16_0._target.ChangeWeaponDiveState()
	arg_16_0._target.SetDiveInvisible(False)
	arg_16_0._target.SetAI(var_0_1.SUB_DEFAULT_RETREAT_AI)
	arg_16_0._target.TriggerBuff(var_0_2.BuffEffectType.ON_SUBMARINE_RETREAT, {})
	arg_16_0._target.RemoveBuff(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF)
	arg_16_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF))

def var_0_3.OnFreeDiveState(arg_17_0):
	local var_17_0 = arg_17_0._currentState

	arg_17_0._currentState = arg_17_0._freeDiveState

	arg_17_0._currentState.UpdateCldData(arg_17_0._target, var_17_0)
	arg_17_0._target.ChangeWeaponDiveState()
	arg_17_0._target.SetCrash(False)
	arg_17_0._target.SetDiveInvisible(True)
	arg_17_0._target.StateChange(var_0_0.Battle.UnitState.STATE_DIVE)
	arg_17_0._target.PlayFX("qianting_rushui", False)
	arg_17_0._target.TriggerBuff(var_0_2.BuffEffectType.ON_SUBMARINE_DIVE, {})
	arg_17_0._target.RemoveBuff(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF)
	arg_17_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF))

def var_0_3.OnFreeFloatState(arg_18_0):
	local var_18_0 = arg_18_0._currentState

	arg_18_0._currentState = arg_18_0._freeFloatState

	arg_18_0._currentState.UpdateCldData(arg_18_0._target, var_18_0)
	arg_18_0._target.ChangeWeaponDiveState()
	arg_18_0._target.SetDiveInvisible(False)
	arg_18_0._target.StateChange(var_0_0.Battle.UnitState.STATE_MOVE)
	arg_18_0._target.PlayFX("qianting_chushui", False)
	arg_18_0._target.TriggerBuff(var_0_2.BuffEffectType.ON_SUBMARINE_FLOAT, {})
	arg_18_0._target.RemoveBuff(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF)
	arg_18_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF))

def var_0_3.OnFreeBenchState(arg_19_0):
	local var_19_0 = arg_19_0._currentState

	arg_19_0._currentState = arg_19_0._freeBenchState

	arg_19_0._currentState.UpdateCldData(arg_19_0._target, var_19_0)
	arg_19_0._target.ChangeWeaponDiveState()
	arg_19_0._target.SetDiveInvisible(False)
	arg_19_0._target.StateChange(var_0_0.Battle.UnitState.STATE_MOVE)
	arg_19_0._target.PlayFX("qianting_chushui", False)
	arg_19_0._target.RemoveBuff(var_0_1.SUB_DIVE_IMMUNE_IGNITE_BUFF)
	arg_19_0._target.AddBuff(var_0_0.Battle.BattleBuffUnit.New(var_0_1.SUB_FLOAT_DISIMMUNE_IGNITE_BUFF))

def var_0_3.OnDeepMineState(arg_20_0):
	local var_20_0 = arg_20_0._currentState

	arg_20_0._currentState = arg_20_0._deepMineState

	arg_20_0._currentState.UpdateCldData(arg_20_0._target, var_20_0)
	arg_20_0._target.SetDiveInvisible(False)
	arg_20_0._target.ChangeWeaponDiveState()
	arg_20_0._target.SetAI(20005)

def var_0_3.GetRecycle(arg_21_0):
	return False

def var_0_3.GetTarget(arg_22_0):
	return arg_22_0._target

def var_0_3.GetCurrentState(arg_23_0):
	return arg_23_0._currentState

def var_0_3.GetCurrentStateName(arg_24_0):
	return arg_24_0._currentState.__name

def var_0_3.GetWeaponType(arg_25_0):
	return arg_25_0._currentState.GetWeaponUseableList()

def var_0_3.GetBarVisible(arg_26_0):
	return arg_26_0._currentState.GetBarVisible()

def var_0_3.GetRundMode(arg_27_0):
	return arg_27_0._currentState.RunMode()

def var_0_3.GetCurrentDiveState(arg_28_0):
	return arg_28_0._currentState.GetDiveState()
