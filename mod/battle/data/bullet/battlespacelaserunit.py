from luatable import pairs
import math
from Vector3 import Vector3
from mgr import TimeMgr

import BattleColumnAreaBulletUnit

class BattleSpaceLaserUnit(BattleColumnAreaBulletUnit):

	__name = "BattleSpaceLaserUnit"
	STATE_READY = "Ready"
	STATE_PRECAST = "Precast"
	STATE_ATTACK = "Attack"
	STATE_DESTROY = "Destroy"

	def Ctor(arg_1_0, *args):
		super().Ctor(arg_1_0, *args)

		arg_1_0._collidedTimes = {}

	def Dispose(arg_2_0):
		arg_2_0._lifeEndCb = None
		arg_2_0._collidedTimes = None

		super().Dispose(arg_2_0)

	def ExecuteLifeEndCallback(arg_3_0):
		if arg_3_0._lifeEndCb:
			arg_3_0._lifeEndCb()

	def AssertFields(arg_4_0, arg_4_1):
		assert(arg_4_0[arg_4_1], "Lack Field " + arg_4_1)

	def SetTemplateData(arg_5_0, arg_5_1):
		arg_5_0.AssertFields(arg_5_1.extra_param, "attack_time")
		arg_5_0.AssertFields(arg_5_1.hit_type, "interval")
		super().SetTemplateData(arg_5_0, arg_5_1)

		arg_5_0._hitInterval = arg_5_1.hit_type.interval

	def GetHitInterval(arg_6_0):
		return arg_6_0._hitInterval

	def DoTrack(arg_7_0):
		var_7_0 = arg_7_0
		var_7_1 = var_7_0.getTrackingTarget()

		if not var_7_1 or var_7_1 == -1:
			return
		elif not var_7_1.IsAlive():
			var_7_0.setTrackingTarget(-1)
			var_7_0._speed.SetNormalize().Mul(arg_7_0._convertedVelocity)

			return
		elif var_7_0.GetDistance(var_7_1) > var_7_0._trackRange:
			var_7_0.setTrackingTarget(-1)
			var_7_0._speed.SetNormalize().Mul(arg_7_0._convertedVelocity)

			return

		var_7_2 = var_7_1.GetPosition() - var_7_0.GetPosition()
		var_7_3 = var_7_2.Magnitude()

		if var_7_3 <= 1e-05:
			arg_7_0._speed.Set(0, 0, 0)

			return

		var_7_4 = arg_7_0._speedNormal

		var_7_2.SetNormalize()

		var_7_5 = var_7_2.x * var_7_4.x + var_7_2.z * var_7_4.z
		var_7_6 = var_7_2.z * var_7_4.x - var_7_2.x * var_7_4.z
		var_7_7 = var_7_0.GetSpeedRatio()
		var_7_8 = math.cos(var_7_0._cosAngularSpeed * var_7_7)
		var_7_9 = math.sin(var_7_0._sinAngularSpeed * var_7_7)
		var_7_10 = var_7_5
		var_7_11 = var_7_6

		if var_7_5 < var_7_8:
			var_7_10 = var_7_8
			var_7_11 = var_7_9 * (var_7_11 > 0 and 1 or -1)

		var_7_12 = var_7_4.x * var_7_10 - var_7_4.z * var_7_11
		var_7_13 = var_7_4.z * var_7_10 + var_7_4.x * var_7_11
		var_7_14 = math.min(arg_7_0._convertedVelocity, var_7_3)

		var_7_0._speed.Set(var_7_12, 0, var_7_13)
		var_7_0._speed.Mul(var_7_14)
		arg_7_0._speedNormal.Set(var_7_12, 0, var_7_13)
		arg_7_0._speedNormal.SetNormalize()

		arg_7_0._yAngle = math.rad2Deg * math.atan2(var_7_12, var_7_13)

	def InitSpeed(arg_8_0, *args):
		super().InitSpeed(arg_8_0, *args)

		if arg_8_0.IsTracker():
			var_8_0 = math.deg2Rad * arg_8_0._yAngle

			arg_8_0._speedNormal = Vector3(math.cos(var_8_0), 0, math.sin(var_8_0))
			arg_8_0.updateSpeed = arg_8_0.DoTrack
		elif arg_8_0.IsCircle() and arg_8_0.IsAlert():
			arg_8_0._centripetalSpeed = arg_8_0._centripetalSpeed * arg_8_0.alertSpeedRatio

	def SetLifeTime(arg_9_0, arg_9_1):
		arg_9_0._lifeTime = arg_9_1

	def SetAlert(arg_10_0, arg_10_1):
		arg_10_0._alertFlag = arg_10_1

		var_10_0 = arg_10_0.GetTemplate().extra_param

		if not var_10_0.alertSpeed:
			return

		arg_10_0.ResetVelocity(arg_10_0._velocity * var_10_0.alertSpeed)

		arg_10_0.alertSpeedRatio = var_10_0.alertSpeed

	def IsAlert(arg_11_0):
		return arg_11_0._alertFlag

	def Update(arg_12_0, arg_12_1):
		super().Update(arg_12_0, arg_12_1)

		arg_12_0._reachDestFlag = arg_12_1 > arg_12_0._timeStamp + arg_12_0._lifeTime

		var_12_0 = TimeMgr.GetInstance().GetCombatTime()

		for iter_12_0, iter_12_1 in pairs(arg_12_0._collidedTimes):
			if var_12_0 > iter_12_1 + arg_12_0._hitInterval:
				arg_12_0._collidedTimes[iter_12_0] = None
				arg_12_0._collidedList[iter_12_0] = None

	def GetCollidedList(arg_13_0):
		return arg_13_0._collidedList, arg_13_0._collidedTimes

	def RegisterLifeEndCB(arg_14_0, arg_14_1):
		arg_14_0._lifeEndCb = arg_14_1

	def UnRegisterLifeEndCB(arg_15_0):
		arg_15_0._lifeEndCb = None
