from Vector3 import Vector3
import math
from luatable import table, ipairs

import BattleBulletUnit
import BattleState

up = Vector3.up
import BattleTargetChoise
class BattleTrackingAAMissileUnit(BattleBulletUnit):

	__name = "BattleTrackingAAMissileUnit"
	
	def doAccelerate(self, arg_1_1):
		var_1_0, var_1_1 = self.GetAcceleration(arg_1_1)

		if var_1_0 == 0 and var_1_1 == 0:
			return

		if var_1_0 < 0 and self._speedLength + var_1_0 < 0:
			self.reverseAcceleration()

		self._speed.Set(self._speed.x + self._speedNormal.x * var_1_0 + self._speedCross.x * var_1_1, self._speed.y + self._speedNormal.y * var_1_0 + self._speedCross.y * var_1_1, self._speed.z + self._speedNormal.z * var_1_0 + self._speedCross.z * var_1_1)

		self._speedLength = self._speed.Magnitude()

		if self._speedLength != 0:
			self._speedNormal.Copy(self._speed)
			self._speedNormal.Div(self._speedLength)

		self._speedCross.Copy(self._speedNormal)
		self._speedCross.Cross2(up)

	def doTrack(self):
		if self.getTrackingTarget() == None:
			var_2_0 = self.GetFilteredList()
			var_2_1 = BattleTargetChoise.TargetWeightiest(self, None, var_2_0)[1]

			if var_2_1 != None:
				self.setTrackingTarget(var_2_1)

		var_2_2 = self.getTrackingTarget()

		if var_2_2 == None or var_2_2 == -1:
			return
		elif not var_2_2.IsAlive():
			self.CleanAimMark()
			self.setTrackingTarget(-1)

			return

		var_2_3 = var_2_2.GetBeenAimedPosition()

		if not var_2_3:
			return

		var_2_4 = var_2_3 - self.GetPosition()

		var_2_4.SetNormalize()

		var_2_5 = Vector3.Normalize(self._speed)
		var_2_6 = Vector3.Dot(var_2_5, var_2_4)
		var_2_7 = var_2_5.z * var_2_4.x - var_2_5.x * var_2_4.z
		var_2_8 = self.GetSpeedRatio()
		var_2_9 = var_2_6
		var_2_10 = var_2_7
		var_2_11 = self._speed.x * var_2_9 + self._speed.z * var_2_10
		var_2_12 = self._speed.z * var_2_9 - self._speed.x * var_2_10

		self._speed.Set(var_2_11, 0, var_2_12)

	def doNothing(self):
		if self._gravity != 0:
			self._verticalSpeed = self._verticalSpeed + self._gravity * self.GetSpeedRatio()

	def GetFilteredList(self):
		var_4_0 = BattleTargetChoise.TargetAllHarm(self)
		var_4_1 = self.FilterRange(var_4_0)

		return (self.FilterAngle(var_4_1))

	def FilterRange(self, arg_5_1):
		if not self._trackDist:
			return arg_5_1

		for iter_5_0 in range(len(arg_5_1), 1, -1):
			if self.IsOutOfRange(arg_5_1[iter_5_0]):
				table.remove(arg_5_1, iter_5_0)

		return arg_5_1

	def IsOutOfRange(self, arg_6_1):
		if not self._trackDist:
			return True

		return self.GetDistance(arg_6_1) > self._trackDist

	def FilterAngle(self, arg_7_1):
		if not self._trackAngle or self._trackAngle >= 360:
			return arg_7_1

		for iter_7_0 in range(len(arg_7_1), 1, -1):
			if self.IsOutOfAngle(arg_7_1[iter_7_0]):
				table.remove(arg_7_1, iter_7_0)

		return arg_7_1

	def IsOutOfAngle(self, arg_8_1):
		if not self._trackAngle or self._trackAngle >= 360:
			return False

		var_8_0 = self.GetPosition()
		var_8_1 = arg_8_1.GetPosition() - var_8_0
		var_8_2 = self._speedNormal
		var_8_3 = Vector3.Dot(var_8_1, var_8_2) / var_8_1.Magnitude()
		var_8_4 = math.acos(var_8_3)

		return var_8_4 > self._trackRadian or var_8_4 < -self._trackRadian

	def SetTrackingFXData(self, arg_9_1):
		self._trackingFXData = arg_9_1

	def InitSpeed(arg_10_0, arg_10_1):
		if arg_10_0._yAngle == None:
			if arg_10_0._targetPos != None:
				arg_10_0._yAngle = arg_10_1 + arg_10_0._barrageAngle
			else:
				arg_10_0._yAngle = arg_10_0._baseAngle + arg_10_0._barrageAngle

		arg_10_0.calcSpeed()

		var_10_0 = {}

		def var_10_1(arg_11_0, arg_11_1):
			for iter_11_0, iter_11_1 in ipairs(var_10_0):
				iter_11_1(arg_11_0, arg_11_1)

			var_11_0 = arg_10_0.getTrackingTarget()

			if var_11_0 and var_11_0 != -1 and not arg_10_0._trackingFXData.aimingFX and arg_10_0._trackingFXData.fxName and arg_10_0._trackingFXData.fxName != "":
				var_11_1 = BattleState.GetInstance().GetSceneMediator().GetCharacter(var_11_0.GetUniqueID())

				arg_10_0._trackingFXData.aimingFX = var_11_1.AddFX(arg_10_0._trackingFXData.fxName)

		if arg_10_0.IsTracker():
			var_10_2 = arg_10_0._accTable.tracker

			arg_10_0._trackAngle = var_10_2.angular
			arg_10_0._trackDist = var_10_2.range

			if var_10_2.angular:
				arg_10_0._trackRadian = math.deg2Rad * arg_10_0._trackAngle * 0.5

			table.insert(var_10_0, arg_10_0.doTrack)

		if arg_10_0.HasAcceleration():
			arg_10_0._speedLength = arg_10_0._speed.Magnitude()
			arg_10_0._speedNormal = arg_10_0._speed / arg_10_0._speedLength
			arg_10_0._speedCross = Vector3.Cross(arg_10_0._speedNormal, up)

			def _func(arg_12_0, *args):
				arg_10_0._speedLength = arg_10_0._speed.Magnitude()
				arg_10_0._speedNormal = arg_10_0._speed / arg_10_0._speedLength
				arg_10_0._speedCross = Vector3.Cross(arg_10_0._speedNormal, up)

				arg_10_0.doAccelerate(arg_12_0, *args)

			table.insert(var_10_0, _func)

		if len(var_10_0) == 0:
			table.insert(var_10_0, arg_10_0.doNothing)

		arg_10_0.updateSpeed = var_10_1

	def CleanAimMark(arg_13_0):
		var_13_0 = arg_13_0.getTrackingTarget()

		if var_13_0 and var_13_0 != -1 and arg_13_0._trackingFXData.aimingFX:
			var_13_1 = BattleState.GetInstance().GetSceneMediator().GetCharacter(var_13_0.GetUniqueID())

			if var_13_1:
				var_13_1.RemoveFX(arg_13_0._trackingFXData.aimingFX)

			arg_13_0._trackingFXData.aimingFX = None

	def OutRange(arg_14_0, *args):
		arg_14_0.CleanAimMark()
		super.OutRange(arg_14_0, *args)
