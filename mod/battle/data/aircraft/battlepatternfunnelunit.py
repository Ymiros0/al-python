ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleTargetChoise
local var_0_3 = var_0_0.Battle.BattleDataFunction
local var_0_4 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattlePatternFunnelUnit = class("BattlePatternFunnelUnit", var_0_0.Battle.BattleAircraftUnit)
var_0_0.Battle.BattlePatternFunnelUnit.__name = "BattlePatternFunnelUnit"

local var_0_5 = var_0_0.Battle.BattlePatternFunnelUnit

var_0_5.STOP_STATE = "STOP_STATE"
var_0_5.MOVE_STATE = "MOVE_STATE"
var_0_5.CRASH_STATE = "CRASH_STATE"

def var_0_5.Ctor(arg_1_0, arg_1_1):
	var_0_5.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._untDir = var_0_0.Battle.BattleConst.UnitDir.LEFT
	arg_1_0._type = var_0_0.Battle.BattleConst.UnitType.FUNNEL_UNIT
	arg_1_0._move = var_0_0.Battle.MoveComponent.New()

def var_0_5.Update(arg_2_0, arg_2_1):
	arg_2_0.updatePatrol(arg_2_1)
	arg_2_0.UpdateWeapon()
	arg_2_0.updatePosition()

def var_0_5.OnMotherDead(arg_3_0):
	arg_3_0.onDead()

def var_0_5.updateExist(arg_4_0):
	if not arg_4_0._existStartTime:
		return

	if arg_4_0._existStartTime + arg_4_0._existDuration < pg.TimeMgr.GetInstance().GetCombatTime():
		arg_4_0.changePartolState(var_0_5.CRASH_STATE)

def var_0_5.UpdateWeapon(arg_5_0):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0.GetWeapon()):
		iter_5_1.Update()

def var_0_5.SetMotherUnit(arg_6_0, arg_6_1):
	var_0_5.super.SetMotherUnit(arg_6_0, arg_6_1)

	local var_6_0 = arg_6_0.GetIFF() * -1

	arg_6_0._upperBound, arg_6_0._lowerBound, arg_6_0._leftBound, arg_6_0._rightBound = var_0_0.Battle.BattleDataProxy.GetInstance().GetFleetBoundByIFF(var_6_0)

def var_0_5.SetTemplate(arg_7_0, arg_7_1):
	var_0_5.super.SetTemplate(arg_7_0, arg_7_1)

	arg_7_0._existDuration = arg_7_1.funnel_behavior.exist

def var_0_5.changePartolState(arg_8_0, arg_8_1):
	if arg_8_1 == var_0_5.MOVE_STATE:
		arg_8_0.changeToMoveState()

	arg_8_0._portalState = arg_8_1

def var_0_5.AddCreateTimer(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0._currentState = arg_9_0.STATE_CREATE
	arg_9_0._speedDir = arg_9_1
	arg_9_0._velocity = var_0_0.Battle.BattleFormulas.ConvertAircraftSpeed(30)

	local function var_9_0()
		arg_9_0._existStartTime = pg.TimeMgr.GetInstance().GetCombatTime()
		arg_9_0._velocity = var_0_0.Battle.BattleFormulas.ConvertAircraftSpeed(arg_9_0._tmpData.speed)

		arg_9_0.changePartolState(var_0_5.MOVE_STATE)
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_9_0._createTimer)

		arg_9_0._createTimer = None

	arg_9_0.updatePatrol = arg_9_0._updateCreate
	arg_9_0._createTimer = pg.TimeMgr.GetInstance().AddBattleTimer("AddCreateTimer", 0, 0.5, var_9_0)

def var_0_5.updatePosition(arg_11_0):
	arg_11_0._pos = arg_11_0._pos + arg_11_0._speed

def var_0_5._updateCreate(arg_12_0):
	arg_12_0.UpdateSpeed()
	arg_12_0.updatePosition()

def var_0_5.changeToMoveState(arg_13_0):
	arg_13_0._currentState = var_0_5.MOVE_STATE

	local var_13_0 = var_0_3.GetAITmpDataFromID(arg_13_0._tmpData.funnel_behavior.AI)
	local var_13_1 = var_0_0.Battle.AutoPilot.New(arg_13_0, var_13_0)

	arg_13_0._move.ImmuneMaxAreaLimit(True)
	arg_13_0._move.CancelFormationCtrl()

	arg_13_0._autoPilotAI = var_13_1

	arg_13_0._autoPilotAI.SetHiveUnit(arg_13_0._motherUnit)

	arg_13_0.updatePatrol = arg_13_0._updateMove

def var_0_5._updateMove(arg_14_0, arg_14_1):
	arg_14_0._move.Update()
	arg_14_0._speed.Copy(arg_14_0._move.GetSpeed())
	arg_14_0._speed.Mul(arg_14_0._velocity * arg_14_0.GetSpeedRatio())
	arg_14_0.updatePosition()
