ys = ys or {}

local var_0_0 = ys
local var_0_1 = Vector3.up
local var_0_2 = var_0_0.Battle.BattleTargetChoise
local var_0_3 = class("BattleTrackingAAMissileUnit", var_0_0.Battle.BattleBulletUnit)

var_0_3.__name = "BattleTrackingAAMissileUnit"
var_0_0.Battle.BattleTrackingAAMissileUnit = var_0_3

def var_0_3.doAccelerate(arg_1_0, arg_1_1):
	local var_1_0, var_1_1 = arg_1_0.GetAcceleration(arg_1_1)

	if var_1_0 == 0 and var_1_1 == 0:
		return

	if var_1_0 < 0 and arg_1_0._speedLength + var_1_0 < 0:
		arg_1_0.reverseAcceleration()

	arg_1_0._speed.Set(arg_1_0._speed.x + arg_1_0._speedNormal.x * var_1_0 + arg_1_0._speedCross.x * var_1_1, arg_1_0._speed.y + arg_1_0._speedNormal.y * var_1_0 + arg_1_0._speedCross.y * var_1_1, arg_1_0._speed.z + arg_1_0._speedNormal.z * var_1_0 + arg_1_0._speedCross.z * var_1_1)

	arg_1_0._speedLength = arg_1_0._speed.Magnitude()

	if arg_1_0._speedLength != 0:
		arg_1_0._speedNormal.Copy(arg_1_0._speed)
		arg_1_0._speedNormal.Div(arg_1_0._speedLength)

	arg_1_0._speedCross.Copy(arg_1_0._speedNormal)
	arg_1_0._speedCross.Cross2(var_0_1)

def var_0_3.doTrack(arg_2_0):
	if arg_2_0.getTrackingTarget() == None:
		local var_2_0 = arg_2_0.GetFilteredList()
		local var_2_1 = var_0_2.TargetWeightiest(arg_2_0, None, var_2_0)[1]

		if var_2_1 != None:
			arg_2_0.setTrackingTarget(var_2_1)

	local var_2_2 = arg_2_0.getTrackingTarget()

	if var_2_2 == None or var_2_2 == -1:
		return
	elif not var_2_2.IsAlive():
		arg_2_0.CleanAimMark()
		arg_2_0.setTrackingTarget(-1)

		return

	local var_2_3 = var_2_2.GetBeenAimedPosition()

	if not var_2_3:
		return

	local var_2_4 = var_2_3 - arg_2_0.GetPosition()

	var_2_4.SetNormalize()

	local var_2_5 = Vector3.Normalize(arg_2_0._speed)
	local var_2_6 = Vector3.Dot(var_2_5, var_2_4)
	local var_2_7 = var_2_5.z * var_2_4.x - var_2_5.x * var_2_4.z
	local var_2_8 = arg_2_0.GetSpeedRatio()
	local var_2_9 = var_2_6
	local var_2_10 = var_2_7
	local var_2_11 = arg_2_0._speed.x * var_2_9 + arg_2_0._speed.z * var_2_10
	local var_2_12 = arg_2_0._speed.z * var_2_9 - arg_2_0._speed.x * var_2_10

	arg_2_0._speed.Set(var_2_11, 0, var_2_12)

def var_0_3.doNothing(arg_3_0):
	if arg_3_0._gravity != 0:
		arg_3_0._verticalSpeed = arg_3_0._verticalSpeed + arg_3_0._gravity * arg_3_0.GetSpeedRatio()

def var_0_3.GetFilteredList(arg_4_0):
	local var_4_0 = var_0_2.TargetAllHarm(arg_4_0)
	local var_4_1 = arg_4_0.FilterRange(var_4_0)

	return (arg_4_0.FilterAngle(var_4_1))

def var_0_3.FilterRange(arg_5_0, arg_5_1):
	if not arg_5_0._trackDist:
		return arg_5_1

	for iter_5_0 = #arg_5_1, 1, -1:
		if arg_5_0.IsOutOfRange(arg_5_1[iter_5_0]):
			table.remove(arg_5_1, iter_5_0)

	return arg_5_1

def var_0_3.IsOutOfRange(arg_6_0, arg_6_1):
	if not arg_6_0._trackDist:
		return True

	return arg_6_0.GetDistance(arg_6_1) > arg_6_0._trackDist

def var_0_3.FilterAngle(arg_7_0, arg_7_1):
	if not arg_7_0._trackAngle or arg_7_0._trackAngle >= 360:
		return arg_7_1

	for iter_7_0 = #arg_7_1, 1, -1:
		if arg_7_0.IsOutOfAngle(arg_7_1[iter_7_0]):
			table.remove(arg_7_1, iter_7_0)

	return arg_7_1

def var_0_3.IsOutOfAngle(arg_8_0, arg_8_1):
	if not arg_8_0._trackAngle or arg_8_0._trackAngle >= 360:
		return False

	local var_8_0 = arg_8_0.GetPosition()
	local var_8_1 = arg_8_1.GetPosition() - var_8_0
	local var_8_2 = arg_8_0._speedNormal
	local var_8_3 = Vector3.Dot(var_8_1, var_8_2) / var_8_1.Magnitude()
	local var_8_4 = math.acos(var_8_3)

	return var_8_4 > arg_8_0._trackRadian or var_8_4 < -arg_8_0._trackRadian

def var_0_3.SetTrackingFXData(arg_9_0, arg_9_1):
	arg_9_0._trackingFXData = arg_9_1

def var_0_3.InitSpeed(arg_10_0, arg_10_1):
	if arg_10_0._yAngle == None:
		if arg_10_0._targetPos != None:
			arg_10_0._yAngle = arg_10_1 + arg_10_0._barrageAngle
		else
			arg_10_0._yAngle = arg_10_0._baseAngle + arg_10_0._barrageAngle

	arg_10_0.calcSpeed()

	local var_10_0 = {}

	local function var_10_1(arg_11_0, arg_11_1)
		for iter_11_0, iter_11_1 in ipairs(var_10_0):
			iter_11_1(arg_11_0, arg_11_1)

		local var_11_0 = arg_10_0.getTrackingTarget()

		if var_11_0 and var_11_0 != -1 and not arg_10_0._trackingFXData.aimingFX and arg_10_0._trackingFXData.fxName and arg_10_0._trackingFXData.fxName != "":
			local var_11_1 = var_0_0.Battle.BattleState.GetInstance().GetSceneMediator().GetCharacter(var_11_0.GetUniqueID())

			arg_10_0._trackingFXData.aimingFX = var_11_1.AddFX(arg_10_0._trackingFXData.fxName)

	if arg_10_0.IsTracker():
		local var_10_2 = arg_10_0._accTable.tracker

		arg_10_0._trackAngle = var_10_2.angular
		arg_10_0._trackDist = var_10_2.range

		if var_10_2.angular:
			arg_10_0._trackRadian = math.deg2Rad * arg_10_0._trackAngle * 0.5

		table.insert(var_10_0, arg_10_0.doTrack)

	if arg_10_0.HasAcceleration():
		arg_10_0._speedLength = arg_10_0._speed.Magnitude()
		arg_10_0._speedNormal = arg_10_0._speed / arg_10_0._speedLength
		arg_10_0._speedCross = Vector3.Cross(arg_10_0._speedNormal, var_0_1)

		table.insert(var_10_0, function(arg_12_0, ...)
			arg_10_0._speedLength = arg_10_0._speed.Magnitude()
			arg_10_0._speedNormal = arg_10_0._speed / arg_10_0._speedLength
			arg_10_0._speedCross = Vector3.Cross(arg_10_0._speedNormal, var_0_1)

			arg_10_0.doAccelerate(arg_12_0, ...))

	if #var_10_0 == 0:
		table.insert(var_10_0, arg_10_0.doNothing)

	arg_10_0.updateSpeed = var_10_1

def var_0_3.CleanAimMark(arg_13_0):
	local var_13_0 = arg_13_0.getTrackingTarget()

	if var_13_0 and var_13_0 != -1 and arg_13_0._trackingFXData.aimingFX:
		local var_13_1 = var_0_0.Battle.BattleState.GetInstance().GetSceneMediator().GetCharacter(var_13_0.GetUniqueID())

		if var_13_1:
			var_13_1.RemoveFX(arg_13_0._trackingFXData.aimingFX)

		arg_13_0._trackingFXData.aimingFX = None

def var_0_3.OutRange(arg_14_0, ...):
	arg_14_0.CleanAimMark()
	var_0_3.super.OutRange(arg_14_0, ...)
