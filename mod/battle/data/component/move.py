ys = ys or {}

local var_0_0 = ys.Battle.BattleVariable
local var_0_1 = class("MoveComponent")

ys.Battle.MoveComponent = var_0_1

local var_0_2 = ys.Battle.BattleConst
local var_0_3 = ys.Battle.BattleFormulas

var_0_1._pos = Vector3.zero
var_0_1._isForceMove = False
var_0_1._staticState = False
var_0_1._speed = Vector3.zero
var_0_1._additiveSpeedList = {}
var_0_1._additiveSpeed = Vector3.zero
var_0_1._corpsLimitSpeed = 0
var_0_1._leftCorpsBound = 0
var_0_1._rightCorpsBound = 0
var_0_1._immuneAreaLimit = False
var_0_1._immuneMaxAreaLimit = False
var_0_1._leftBorder = 0
var_0_1._rightBorder = 0
var_0_1._upBorder = 0
var_0_1._downBorder = 0
var_0_1._IFF = 0

def var_0_1.Ctor(arg_1_0):
	return

def var_0_1.GetPos(arg_2_0):
	return arg_2_0._pos

def var_0_1.SetPos(arg_3_0, arg_3_1):
	arg_3_0._pos = arg_3_1

def var_0_1.Update(arg_4_0):
	arg_4_0._speed = arg_4_0.GetFinalSpeed()

def var_0_1.FixSpeed(arg_5_0, arg_5_1):
	assert(arg_5_1.FixSpeed != None and type(arg_5_1.FixSpeed) == "function", " MoveComponent.FixSpeed 速度修正出错")
	arg_5_1.FixSpeed(arg_5_0._speed)

def var_0_1.Move(arg_6_0, arg_6_1):
	arg_6_1 = arg_6_1 or 1
	arg_6_0._pos.x = arg_6_0._pos.x + arg_6_0._speed.x * arg_6_1
	arg_6_0._pos.y = arg_6_0._pos.y + arg_6_0._speed.y * arg_6_1
	arg_6_0._pos.z = arg_6_0._pos.z + arg_6_0._speed.z * arg_6_1

def var_0_1.GetSpeed(arg_7_0):
	return arg_7_0._speed

def var_0_1.SetCorpsArea(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0._leftCorpsBound = arg_8_1
	arg_8_0._rightCorpsBound = arg_8_2

def var_0_1.SetBorder(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	arg_9_0._leftBorder = arg_9_1
	arg_9_0._rightBorder = arg_9_2
	arg_9_0._upBorder = arg_9_3
	arg_9_0._downBorder = arg_9_4

def var_0_1.GetFinalSpeed(arg_10_0):
	local var_10_0 = arg_10_0.getInitialSpeed()

	if not arg_10_0._unstoppable:
		var_10_0 = arg_10_0.AdditiveForce(var_10_0)

	return (arg_10_0.BorderLimit(var_10_0))

def var_0_1.CorpsAreaLimit(arg_11_0, arg_11_1):
	if arg_11_0._immuneAreaLimit:
		return arg_11_1

	local var_11_0 = arg_11_0._pos.x
	local var_11_1 = arg_11_0._corpsLimitSpeed

	if var_11_0 < arg_11_0._leftCorpsBound:
		var_11_1 = math.max(var_11_1, 0.1)

		if arg_11_1.x < 0:
			var_11_1 = math.min(10, var_11_1 * 1.04)
	elif var_11_0 > arg_11_0._rightCorpsBound:
		var_11_1 = math.min(var_11_1, -0.1)

		if arg_11_1.x > 0:
			var_11_1 = math.max(-10, var_11_1 * 1.04)
	else
		var_11_1 = var_11_1 < 0.1 and var_11_1 > -0.1 and 0 or var_11_1 * 0.8

	arg_11_0._corpsLimitSpeed = var_11_1
	arg_11_1.x = arg_11_1.x + arg_11_0._corpsLimitSpeed

	return arg_11_1

def var_0_1.BorderLimit(arg_12_0, arg_12_1):
	if arg_12_0._immuneMaxAreaLimit:
		return arg_12_1

	local var_12_0 = arg_12_0._pos

	if arg_12_1.x < 0 and var_12_0.x <= arg_12_0._leftBorder or arg_12_1.x > 0 and var_12_0.x >= arg_12_0._rightBorder:
		arg_12_1.x = 0

	if arg_12_1.z < 0 and var_12_0.z <= arg_12_0._downBorder or arg_12_1.z > 0 and var_12_0.z >= arg_12_0._upBorder:
		arg_12_1.z = 0

	return arg_12_1

def var_0_1.ImmuneAreaLimit(arg_13_0, arg_13_1):
	arg_13_0._immuneAreaLimit = arg_13_1

def var_0_1.ImmuneMaxAreaLimit(arg_14_0, arg_14_1):
	arg_14_0._immuneMaxAreaLimit = arg_14_1

def var_0_1.getInitialSpeed(arg_15_0):
	if arg_15_0._isForceMove and not arg_15_0._unstoppable:
		local var_15_0 = arg_15_0._forceSpeed

		arg_15_0.UpdateForceMove()

		return var_15_0

	if arg_15_0._moveProcess:
		return arg_15_0._moveProcess()

	if arg_15_0._staticState:
		return Vector3.zero

	if arg_15_0._manuallyMove:
		return arg_15_0.CorpsAreaLimit(arg_15_0._manuallyMove())

	assert(arg_15_0._autoMoveAi != None, "角色缺少默认移动的ai")

	return arg_15_0._autoMoveAi()

def var_0_1.SetForceMove(arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4, arg_16_5):
	arg_16_0._isForceMove = True
	arg_16_1 = arg_16_1.normalized
	arg_16_0._forceSpeed = arg_16_1 * arg_16_2
	arg_16_0._forceReduce = arg_16_1 * arg_16_3
	arg_16_0._forceLastTime = arg_16_4
	arg_16_0._decayValve = arg_16_5 or 0

def var_0_1.UpdateForceMove(arg_17_0):
	local var_17_0 = arg_17_0._forceLastTime

	if var_17_0 <= 0:
		arg_17_0.ClearForceMove()

		return

	arg_17_0._forceLastTime = var_17_0 - 1

	if var_17_0 < arg_17_0._decayValve:
		arg_17_0._forceSpeed.Sub(arg_17_0._forceReduce)

def var_0_1.ClearForceMove(arg_18_0):
	arg_18_0._isForceMove = False
	arg_18_0._forceSpeed = None
	arg_18_0._forceReduce = None
	arg_18_0._forceLastTime = None

def var_0_1.SetMoveProcess(arg_19_0, arg_19_1):
	arg_19_0._moveProcess = arg_19_1

def var_0_1.SetStaticState(arg_20_0, arg_20_1):
	arg_20_0._staticState = arg_20_1

def var_0_1.SetAutoMoveAI(arg_21_0, arg_21_1, arg_21_2):
	function arg_21_0._autoMoveAi()
		return arg_21_1.GetDirection().Mul(arg_21_2.GetAttrByName("velocity"))

def var_0_1.SetFormationCtrlInfo(arg_23_0, arg_23_1):
	function arg_23_0._manuallyMove()
		return arg_23_0.UpdateFleetInfo(arg_23_1)

def var_0_1.CancelFormationCtrl(arg_25_0):
	arg_25_0._manuallyMove = None

def var_0_1.SetMotionVO(arg_26_0, arg_26_1):
	arg_26_0._fleetMotionVO = arg_26_1

def var_0_1.UpdateFleetInfo(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0._fleetMotionVO
	local var_27_1 = var_27_0.GetSpeed()

	if arg_27_1.EqualZero():
		return var_27_1

	local var_27_2 = var_27_0.GetPos()

	return (var_27_0.GetDirAngle() * arg_27_1).Add(var_27_2).Sub(arg_27_0._pos).Div(25).Add(var_27_1)

def var_0_1.AdditiveForce(arg_28_0, arg_28_1):
	arg_28_1.x = arg_28_1.x + arg_28_0._additiveSpeed.x
	arg_28_1.z = arg_28_1.z + arg_28_0._additiveSpeed.z

	return arg_28_1

def var_0_1.UpdateAdditiveSpeed(arg_29_0, arg_29_1):
	arg_29_0._additiveSpeed = arg_29_1

def var_0_1.RemoveAdditiveSpeed(arg_30_0):
	arg_30_0._additiveSpeed = Vector3.zero

def var_0_1.ActiveUnstoppable(arg_31_0, arg_31_1):
	arg_31_0._unstoppable = arg_31_1
