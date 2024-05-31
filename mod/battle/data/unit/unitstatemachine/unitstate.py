ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_1.ActionName

var_0_0.Battle.UnitState = class("UnitState")
var_0_0.Battle.UnitState.__name = "UnitState"
var_0_0.Battle.UnitState.STATE_IDLE = "STATE_IDLE"
var_0_0.Battle.UnitState.STATE_MOVE = "STATE_MOVE"
var_0_0.Battle.UnitState.STATE_ATTACK = "STATE_ATTACK"
var_0_0.Battle.UnitState.STATE_ATTACKLEFT = "STATE_ATTACKLEFT"
var_0_0.Battle.UnitState.STATE_DEAD = "STATE_DEAD"
var_0_0.Battle.UnitState.STATE_MOVELEFT = "STATE_MOVELEFT"
var_0_0.Battle.UnitState.STATE_SKILL = "STATE_SKILL"
var_0_0.Battle.UnitState.STATE_VICTORY = "STATE_VICTORY"
var_0_0.Battle.UnitState.STATE_STAND = "STATE_STAND"
var_0_0.Battle.UnitState.STATE_INTERRUPT = "STATE_INTERRUPT"
var_0_0.Battle.UnitState.STATE_SKILL_START = "STATE_SKILL_START"
var_0_0.Battle.UnitState.STATE_SKILL_END = "STATE_SKILL_END"
var_0_0.Battle.UnitState.STATE_DIVING = "STATE_DIVING"
var_0_0.Battle.UnitState.STATE_DIVE = "STATE_DIVE"
var_0_0.Battle.UnitState.STATE_DIVELEFT = "STATE_DIVELEFT"
var_0_0.Battle.UnitState.STATE_RAID = "STATE_RAID"
var_0_0.Battle.UnitState.STATE_RAIDLEFT = "STATE_RAIDLEFT"

def var_0_0.Battle.UnitState.Ctor(arg_1_0, arg_1_1):
	arg_1_0._target = arg_1_1
	arg_1_0._idleState = var_0_0.Battle.IdleState.New()
	arg_1_0._moveState = var_0_0.Battle.MoveState.New()
	arg_1_0._attackState = var_0_0.Battle.AttackState.New()
	arg_1_0._attackLeftState = var_0_0.Battle.AttackLeftState.New()
	arg_1_0._deadState = var_0_0.Battle.DeadState.New()
	arg_1_0._moveLeftState = var_0_0.Battle.MoveLeftState.New()
	arg_1_0._victoryState = var_0_0.Battle.VictoryState.New()
	arg_1_0._victorySwimState = var_0_0.Battle.VictorySwimState.New()
	arg_1_0._standState = var_0_0.Battle.StandState.New()
	arg_1_0._spellState = var_0_0.Battle.SpellState.New()
	arg_1_0._interruptState = var_0_0.Battle.InterruptState.New()
	arg_1_0._skillStartState = var_0_0.Battle.SkillStartState.New()
	arg_1_0._skillEndState = var_0_0.Battle.SkillEndState.New()
	arg_1_0._diveState = var_0_0.Battle.DiveState.New()
	arg_1_0._diveLeftState = var_0_0.Battle.DiveLeftState.New()
	arg_1_0._raidState = var_0_0.Battle.RaidState.New()
	arg_1_0._raidLeftState = var_0_0.Battle.RaidLeftState.New()

	arg_1_0.OnIdleState()

def var_0_0.Battle.UnitState.FreshActionKeyOffset(arg_2_0):
	local var_2_0 = arg_2_0.ActionKeyOffset()

	if var_2_0:
		if string.find(arg_2_0._currentAction, var_2_0) == None:
			arg_2_0.SendAction(arg_2_0._currentAction .. var_2_0)
	elif arg_2_0._offset != None:
		local var_2_1 = string.find(arg_2_0._currentAction, arg_2_0._offset)

		arg_2_0.SendAction(string.sub(arg_2_0._currentAction, 1, var_2_1 - 1))

	arg_2_0._offset = var_2_0

def var_0_0.Battle.UnitState.ChangeState(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_1 == arg_3_0.STATE_IDLE:
		arg_3_0._currentState.AddIdleState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_MOVE:
		arg_3_0._currentState.AddMoveState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_MOVE:
		arg_3_0._currentState.AddMoveState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_ATTACK:
		arg_3_0._currentState.AddAttackState(arg_3_0, arg_3_2)
	elif arg_3_1 == arg_3_0.STATE_DEAD:
		arg_3_0._currentState.AddDeadState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_MOVELEFT:
		arg_3_0._currentState.AddMoveLeftState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_VICTORY:
		local var_3_0 = arg_3_0.GetTarget().GetOxyState()

		if var_3_0 and var_3_0.GetCurrentDiveState() == var_0_1.OXY_STATE.DIVE:
			arg_3_0._currentState.AddVictorySwimState(arg_3_0)
		else
			arg_3_0._currentState.AddVictoryState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_INTERRUPT:
		arg_3_0._currentState.AddInterruptState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_STAND:
		arg_3_0._currentState.AddStandState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_DIVE:
		arg_3_0._currentState.AddDiveState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_DIVELEFT:
		arg_3_0._currentState.AddDiveLeftState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_SKILL_START:
		arg_3_0._currentState.AddSkillStartState(arg_3_0)
	elif arg_3_1 == arg_3_0.STATE_SKILL_END:
		arg_3_0._currentState.AddSkillEndState(arg_3_0)
	else
		assert(False, arg_3_0._target.__name .. "'s state machine, unexcepted state. " .. arg_3_1)

def var_0_0.Battle.UnitState.OnMoveState(arg_4_0):
	arg_4_0._currentState = arg_4_0._moveState

	local var_4_0 = arg_4_0._currentState.GetActionName(arg_4_0)

	arg_4_0.SendAction(var_4_0)

def var_0_0.Battle.UnitState.OnMoveLeftState(arg_5_0):
	arg_5_0._currentState = arg_5_0._moveLeftState

	local var_5_0 = arg_5_0._currentState.GetActionName(arg_5_0)

	arg_5_0.SendAction(var_5_0)

def var_0_0.Battle.UnitState.OnIdleState(arg_6_0):
	arg_6_0._currentState = arg_6_0._idleState

	local var_6_0 = arg_6_0._currentState.GetActionName(arg_6_0)

	arg_6_0.SendAction(var_6_0)

def var_0_0.Battle.UnitState.OnAttackState(arg_7_0, arg_7_1):
	arg_7_0._currentState = arg_7_0._attackState

	local var_7_0 = arg_7_0._currentState.GetActionName(arg_7_0, arg_7_1)

	arg_7_0.SendAction(var_7_0)

def var_0_0.Battle.UnitState.OnAttackLeftState(arg_8_0, arg_8_1):
	arg_8_0._currentState = arg_8_0._attackLeftState

	local var_8_0 = arg_8_0._currentState.GetActionName(arg_8_0, arg_8_1)

	arg_8_0.SendAction(var_8_0)

def var_0_0.Battle.UnitState.OnDiveState(arg_9_0):
	arg_9_0._currentState = arg_9_0._diveState

	local var_9_0 = arg_9_0._currentState.GetActionName(arg_9_0)

	arg_9_0.SendAction(var_9_0)

def var_0_0.Battle.UnitState.OnDiveLeftState(arg_10_0):
	arg_10_0._currentState = arg_10_0._diveLeftState

	local var_10_0 = arg_10_0._currentState.GetActionName(arg_10_0)

	arg_10_0.SendAction(var_10_0)

def var_0_0.Battle.UnitState.OnRaidState(arg_11_0, arg_11_1):
	arg_11_0._currentState = arg_11_0._raidState

	local var_11_0 = arg_11_0._currentState.GetActionName(arg_11_0)

	arg_11_0.SendAction(var_11_0)

def var_0_0.Battle.UnitState.OnRaidLeftState(arg_12_0, arg_12_1):
	arg_12_0._currentState = arg_12_0._raidLeftState

	local var_12_0 = arg_12_0._currentState.GetActionName(arg_12_0)

	arg_12_0.SendAction(var_12_0)

def var_0_0.Battle.UnitState.OnDeadState(arg_13_0):
	arg_13_0._currentState = arg_13_0._deadState

	local var_13_0 = arg_13_0._currentState.GetActionName(arg_13_0)

	arg_13_0.SendAction(var_13_0)

def var_0_0.Battle.UnitState.OnVictoryState(arg_14_0):
	arg_14_0._currentState = arg_14_0._victoryState

	local var_14_0 = arg_14_0._currentState.GetActionName(arg_14_0)

	arg_14_0.SendAction(var_14_0)

def var_0_0.Battle.UnitState.OnVictorySwimState(arg_15_0):
	arg_15_0._currentState = arg_15_0._victorySwimState

	local var_15_0 = arg_15_0._currentState.GetActionName(arg_15_0)

	arg_15_0.SendAction(var_15_0)

def var_0_0.Battle.UnitState.OnStandState(arg_16_0):
	arg_16_0._currentState = arg_16_0._standState

	local var_16_0 = arg_16_0._currentState.GetActionName(arg_16_0)

	arg_16_0.SendAction(var_16_0)

def var_0_0.Battle.UnitState.OnInterruptState(arg_17_0):
	arg_17_0._currentState = arg_17_0._interruptState

	local var_17_0 = arg_17_0._currentState.GetActionName(arg_17_0)

	arg_17_0.SendAction(var_17_0)

def var_0_0.Battle.UnitState.OnSkillStartState(arg_18_0):
	arg_18_0._currentState = arg_18_0._skillStartState

	local var_18_0 = arg_18_0._currentState.GetActionName(arg_18_0)

	arg_18_0.SendAction(var_18_0)

def var_0_0.Battle.UnitState.OnSkillEndState(arg_19_0):
	arg_19_0._currentState = arg_19_0._skillEndState

	local var_19_0 = arg_19_0._currentState.GetActionName(arg_19_0)

	arg_19_0.SendAction(var_19_0)

def var_0_0.Battle.UnitState.ChangeToMoveState(arg_20_0):
	local var_20_0 = arg_20_0.GetTarget().GetSpeed().x
	local var_20_1 = arg_20_0.GetTarget().GetOxyState()

	if var_20_1 and var_20_1.GetCurrentDiveState() == var_0_1.OXY_STATE.DIVE:
		if var_20_0 >= 0:
			arg_20_0.OnDiveState()
		else
			arg_20_0.OnDiveLeftState()
	elif var_20_0 >= 0:
		arg_20_0.OnMoveState()
	else
		arg_20_0.OnMoveLeftState()

def var_0_0.Battle.UnitState.SendAction(arg_21_0, arg_21_1):
	arg_21_0._currentAction = arg_21_1

	local var_21_0 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.CHANGE_ACTION, {
		actionType = arg_21_1
	})

	arg_21_0._target.DispatchEvent(var_21_0)

def var_0_0.Battle.UnitState.ChangeOxyState(arg_22_0, arg_22_1):
	arg_22_0._target.ChangeOxygenState(arg_22_1)

def var_0_0.Battle.UnitState.GetTarget(arg_23_0):
	return arg_23_0._target

def var_0_0.Battle.UnitState.ActionKeyOffset(arg_24_0):
	return arg_24_0._target.GetActionKeyOffset()

def var_0_0.Battle.UnitState.GetCurrentStateName(arg_25_0):
	return arg_25_0._currentState.__name

def var_0_0.Battle.UnitState.NeedWeaponCache(arg_26_0):
	return arg_26_0._currentState.CacheWeapon()

def var_0_0.Battle.UnitState.OnActionStart(arg_27_0):
	arg_27_0._currentState.OnStart(arg_27_0)

def var_0_0.Battle.UnitState.OnActionTrigger(arg_28_0):
	arg_28_0._currentState.OnTrigger(arg_28_0)

def var_0_0.Battle.UnitState.OnActionEnd(arg_29_0):
	arg_29_0._currentState.OnEnd(arg_29_0)
