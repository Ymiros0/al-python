ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleAirFighterUnit = class("BattleAirFighterUnit", var_0_0.Battle.BattleAircraftUnit)
var_0_0.Battle.BattleAirFighterUnit.__name = "BattleAirFighterUnit"

local var_0_3 = var_0_0.Battle.BattleAirFighterUnit

var_0_3.AIRFIGHTER_ENTER_POINT = Vector3(Screen.width * -0.5, Screen.height * 0.5, 15)
var_0_3.SPEED_FLY = Vector3(3, 0, 0)
var_0_3.BACK_X = 100
var_0_3.DOWN_X = 30
var_0_3.ATTACK_X = -23
var_0_3.UP_X = -70
var_0_3.FREE_X = -75
var_0_3.HEIGHT = var_0_0.Battle.BattleConfig.AirFighterHeight
var_0_3.STRIKE_STATE_FLY = 0
var_0_3.STRIKE_STATE_BACK = 1
var_0_3.STRIKE_STATE_DOWN = 2
var_0_3.STRIKE_STATE_ATTACK = 3
var_0_3.STRIKE_STATE_UP = 4
var_0_3.STRIKE_STATE_FREE = 5
var_0_3.STRIKE_STATE_BACKWARD = 6
var_0_3.STRIKE_STATE_RECYCLE = 7

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._dir = var_0_0.Battle.BattleConst.UnitDir.LEFT
	arg_1_0._type = var_0_0.Battle.BattleConst.UnitType.AIRFIGHTER_UNIT

	arg_1_0.changeState(var_0_3.STRIKE_STATE_FLY)
	arg_1_0.calcYShakeMin()
	arg_1_0.calcYShakeMax()

	arg_1_0._speedDir = Vector3(1, 0, 0)
	arg_1_0._backwardWeaponID = {}

def var_0_3.Update(arg_2_0, arg_2_1):
	arg_2_0.UpdateSpeed()
	arg_2_0.updateStrike()

def var_0_3.UpdateWeapon(arg_3_0):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0.GetWeapon()):
		local var_3_0 = iter_3_1.GetWeaponId()
		local var_3_1 = table.contains(arg_3_0._backwardWeaponID, var_3_0)
		local var_3_2 = iter_3_1.GetCurrentState()

		iter_3_1.Update()

		local var_3_3 = iter_3_1.GetCurrentState()

		if var_3_1 and var_3_2 == iter_3_1.STATE_READY and (var_3_3 == iter_3_1.STATE_ATTACK or var_3_3 == iter_3_1.STATE_OVER_HEAT):
			arg_3_0.changeState(var_0_3.STRIKE_STATE_BACKWARD)

def var_0_3.CreateWeapon(arg_4_0):
	local var_4_0 = {}

	if type(arg_4_0._weaponTemplateID) == "table":
		for iter_4_0, iter_4_1 in ipairs(arg_4_0._weaponTemplateID):
			var_4_0[iter_4_0] = var_0_0.Battle.BattleDataFunction.CreateAirFighterWeaponUnit(iter_4_1, arg_4_0, iter_4_0)
	else
		var_4_0[1] = var_0_0.Battle.BattleDataFunction.CreateAirFighterWeaponUnit(arg_4_0._weaponTemplateID, arg_4_0, 1)

	if arg_4_0._backwardWeaponID:
		for iter_4_2, iter_4_3 in ipairs(arg_4_0._backwardWeaponID):
			var_4_0[iter_4_2] = var_0_0.Battle.BattleDataFunction.CreateAirFighterWeaponUnit(iter_4_3, arg_4_0, iter_4_2)

	return var_4_0

def var_0_3.SetWeaponTemplateID(arg_5_0, arg_5_1):
	arg_5_0._weaponTemplateID = arg_5_1

def var_0_3.SetBackwardWeaponID(arg_6_0, arg_6_1):
	arg_6_0._backwardWeaponID = arg_6_1

def var_0_3.SetTemplate(arg_7_0, arg_7_1):
	arg_7_0.SetAttr(arg_7_1)
	var_0_3.super.SetTemplate(arg_7_0, arg_7_1)

def var_0_3.SetAttr(arg_8_0, arg_8_1):
	var_0_0.Battle.BattleAttr.SetAirFighterAttr(arg_8_0, arg_8_1)
	arg_8_0.SetIFF(-1)

def var_0_3.UpdateSpeed(arg_9_0):
	arg_9_0._speed.Copy(arg_9_0._speedDir)
	arg_9_0._speed.Mul(arg_9_0._velocity * arg_9_0.GetSpeedRatio())

def var_0_3.Free(arg_10_0):
	arg_10_0._undefeated = True

	arg_10_0.LiveCallBack()

	arg_10_0._aliveState = False

def var_0_3.recycle(arg_11_0):
	arg_11_0.LiveCallBack()

	arg_11_0._aliveState = False

def var_0_3.onDead(arg_12_0):
	arg_12_0._currentState = arg_12_0.STATE_DESTORY

	arg_12_0.DeadCallBack()

	arg_12_0._aliveState = False

def var_0_3.GetPosition(arg_13_0):
	return arg_13_0._viewPos

def var_0_3.SetFormationIndex(arg_14_0, arg_14_1):
	arg_14_0._formationIndex = arg_14_1
	arg_14_0._flyStateScale = 12 / (arg_14_1 + 3) + 1

	arg_14_0.DispatchStrikeStateChange()

def var_0_3.GetFormationIndex(arg_15_0):
	return arg_15_0._formationIndex

def var_0_3.SetFormationOffset(arg_16_0, arg_16_1):
	arg_16_0._formationOffset = Vector3(arg_16_1.x, arg_16_1.y, arg_16_1.z)
	arg_16_0._formationOffsetOppo = Vector3(arg_16_1.x * -1, arg_16_1.y, arg_16_1.z)

def var_0_3.SetDeadCallBack(arg_17_0, arg_17_1):
	arg_17_0._deadCallBack = arg_17_1

def var_0_3.DeadCallBack(arg_18_0):
	arg_18_0._deadCallBack()

def var_0_3.SetLiveCallBack(arg_19_0, arg_19_1):
	arg_19_0._liveCallBack = arg_19_1

def var_0_3.LiveCallBack(arg_20_0):
	arg_20_0._liveCallBack()

def var_0_3.getYShake(arg_21_0):
	local var_21_0 = arg_21_0._YShakeCurrent or 0

	arg_21_0._YShakeDir = arg_21_0._YShakeDir or 1

	local var_21_1 = var_21_0 + (0.04 * math.random() + 0.01) * arg_21_0._YShakeDir

	if var_21_1 > arg_21_0._YShakeMax:
		arg_21_0._YShakeDir = -1

		arg_21_0.calcYShakeMin()
	elif var_21_1 < arg_21_0._YShakeMin:
		arg_21_0._YShakeDir = 1

		arg_21_0.calcYShakeMax()

	arg_21_0._YShakeCurrent = var_21_1

	return var_21_1

def var_0_3.calcYShakeMin(arg_22_0):
	arg_22_0._YShakeMin = -0.5 - math.random()

def var_0_3.calcYShakeMax(arg_23_0):
	arg_23_0._YShakeMax = 0.5 + math.random()

def var_0_3.DispatchStrikeStateChange(arg_24_0):
	arg_24_0.DispatchEvent(var_0_0.Event.New(var_0_2.AIR_STRIKE_STATE_CHANGE, {}))

def var_0_3.GetStrikeState(arg_25_0):
	return arg_25_0._strikeState

def var_0_3.GetSize(arg_26_0):
	return arg_26_0._scale

def var_0_3.changeState(arg_27_0, arg_27_1):
	if arg_27_0._strikeState == arg_27_1:
		return

	arg_27_0._strikeState = arg_27_1

	if arg_27_1 == var_0_3.STRIKE_STATE_FLY:
		arg_27_0.changeToFlyState()

		arg_27_0.updateStrike = var_0_3._updatePosFly
	elif arg_27_1 == var_0_3.STRIKE_STATE_BACK:
		arg_27_0.updateStrike = var_0_3._updatePosBack

		arg_27_0.changeToBackState()
	elif arg_27_1 == var_0_3.STRIKE_STATE_DOWN:
		arg_27_0.updateStrike = var_0_3._updatePosDown

		arg_27_0.changeToDownState()
	elif arg_27_1 == var_0_3.STRIKE_STATE_ATTACK:
		arg_27_0.updateStrike = var_0_3._updatePosAttack

		arg_27_0.changeToAttackState()
	elif arg_27_1 == var_0_3.STRIKE_STATE_UP:
		arg_27_0.updateStrike = var_0_3._updatePosUp

		arg_27_0.changeToUpState()
	elif arg_27_1 == var_0_3.STRIKE_STATE_BACKWARD:
		arg_27_0.updateStrike = var_0_3._updateBackward

		arg_27_0.changeToBackwardState()
	elif arg_27_1 == var_0_3.STRIKE_STATE_FREE:
		arg_27_0.updateStrike = var_0_3._updateFree
	elif arg_27_1 == var_0_3.STRIKE_STATE_RECYCLE:
		arg_27_0.updateStrike = var_0_3._updateRecycle

	arg_27_0.DispatchStrikeStateChange()

def var_0_3.changeToFlyState(arg_28_0):
	arg_28_0._pos = var_0_0.Battle.BattleCameraUtil.GetInstance().GetS2WPoint(var_0_3.AIRFIGHTER_ENTER_POINT)
	arg_28_0._viewPos = arg_28_0._pos

	var_0_0.Battle.PlayBattleSFX("battle/plane")

def var_0_3._updatePosFly(arg_29_0):
	arg_29_0._pos.Add(var_0_3.SPEED_FLY)

	arg_29_0._viewPos = Vector3(arg_29_0._formationOffset.x * arg_29_0._flyStateScale, (arg_29_0._formationOffset.z / 1.7 + arg_29_0.getYShake()) * arg_29_0._flyStateScale, 0).Add(arg_29_0._pos)

	if arg_29_0._pos.x > var_0_3.BACK_X:
		arg_29_0.changeState(var_0_3.STRIKE_STATE_BACK)

def var_0_3.changeToBackState(arg_30_0):
	local var_30_0
	local var_30_1 = var_0_0.Battle.BattleDataProxy.GetInstance().GetFleetByIFF(var_0_1.FRIENDLY_CODE).GetMotion()

	if var_30_1:
		var_30_0 = var_30_1.GetPos().z
	else
		var_30_0 = 45

	arg_30_0._pos = Vector3(arg_30_0._pos.x, 15, var_30_0)

def var_0_3._updatePosBack(arg_31_0):
	arg_31_0._pos.Sub(arg_31_0._speed)
	arg_31_0._viewPos.Copy(arg_31_0._pos)
	arg_31_0._viewPos.Sub(arg_31_0._formationOffset)

	if arg_31_0._pos.x < var_0_3.DOWN_X:
		arg_31_0.changeState(var_0_3.STRIKE_STATE_DOWN)

def var_0_3.changeToDownState(arg_32_0):
	arg_32_0._ySpeed = 0.5

	arg_32_0.SetVisitable()

def var_0_3._updatePosDown(arg_33_0):
	arg_33_0._pos.Sub(arg_33_0._speed)

	arg_33_0._pos.y = math.max(var_0_3.HEIGHT, arg_33_0._pos.y - arg_33_0._ySpeed)
	arg_33_0._viewPos = arg_33_0._pos + arg_33_0._formationOffsetOppo
	arg_33_0._ySpeed = math.max(0.02, arg_33_0._ySpeed - 0.005)

	if arg_33_0._pos.x < var_0_3.ATTACK_X:
		arg_33_0.changeState(var_0_3.STRIKE_STATE_ATTACK)

def var_0_3.changeToAttackState(arg_34_0):
	var_0_0.Battle.PlayBattleSFX("battle/air-atk")

def var_0_3._updatePosAttack(arg_35_0):
	arg_35_0._pos.Sub(arg_35_0._speed)

	arg_35_0._pos.y = math.max(var_0_3.HEIGHT, arg_35_0._pos.y - 0.04)

	local var_35_0 = arg_35_0._formationOffsetOppo

	var_35_0.y = arg_35_0.getYShake()
	arg_35_0._viewPos = arg_35_0._pos + var_35_0

	arg_35_0.UpdateWeapon()

	if arg_35_0._pos.x < var_0_3.UP_X:
		arg_35_0.changeState(var_0_3.STRIKE_STATE_UP)

def var_0_3.changeToUpState(arg_36_0):
	arg_36_0._ySpeed = 0.1

def var_0_3._updatePosUp(arg_37_0):
	arg_37_0._pos.Sub(arg_37_0._speed)

	arg_37_0._pos.y = arg_37_0._pos.y + arg_37_0._ySpeed
	arg_37_0._ySpeed = math.min(0.7, arg_37_0._ySpeed + 0.02)
	arg_37_0._viewPos = arg_37_0._pos + arg_37_0._formationOffsetOppo

	if arg_37_0._pos.x < var_0_3.FREE_X:
		arg_37_0.changeState(var_0_3.STRIKE_STATE_FREE)

def var_0_3._updateFree(arg_38_0):
	arg_38_0.Free()

def var_0_3.changeToBackwardState(arg_39_0):
	return

def var_0_3._updateBackward(arg_40_0):
	arg_40_0._pos.Add(arg_40_0._speed)

	arg_40_0._pos.y = math.max(var_0_3.HEIGHT, arg_40_0._pos.y - 0.04)
	arg_40_0._viewPos = arg_40_0._pos + arg_40_0._formationOffsetOppo

	if arg_40_0._pos.x > var_0_3.DOWN_X:
		arg_40_0.changeState(var_0_3.STRIKE_STATE_RECYCLE)

def var_0_3._updateRecycle(arg_41_0):
	arg_41_0.recycle()
