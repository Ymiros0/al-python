import math
from Vector3 import Vector3
from luatable import table
import BattleConfig
import BattleConst
import BattleBulletEvent
import BattleFormulas
import BattleBulletUnit
from Framework.event import Event
from support.utils import Tool

class BattleMissileUnit(BattleBulletUnit):

	__name = "BattleMissileUnit"
	STATE_LAUNCH = "Launch"
	STATE_ATTACK = "Attack"
	TYPE_COORD = 1
	TYPE_RANGE = 2
	TYPE_TARGET = 3

	def __init__(self, *args):
		super().__init__(self, *args)

		self._state = self.STATE_LAUNCH

	def SetTemplateData(self, arg_2_1):
		super().SetTemplateData(self, arg_2_1)
		self.ResetVelocity(0)

		var_2_0 = self.GetTemplate().extra_param

		self._gravity = var_2_0.gravity or BattleConfig.GRAVITY
		self._targetType = var_2_0.aimType or self.TYPE_TARGET

	def GetPierceCount(self):
		return 1

	def RegisterOnTheAir(self, arg_4_1):
		self._onTheHighest = arg_4_1

	def SetExplodePosition(self, arg_5_1):
		self._explodePos = arg_5_1.Clone()
		self._explodePos.y = BattleConfig.BombDetonateHeight

	def GetExplodePostion(self):
		return self._explodePos

	viewInterval = 1 / BattleConfig.viewFPS

	def SetSpawnPosition(self, arg_7_1):
		super.SetSpawnPosition(self, arg_7_1)

		self._verticalSpeed = self.GetTemplate().extra_param.launchVrtSpeed

	def Update(self, arg_8_1):
		super().Update(self, arg_8_1)

		if self._state == self.STATE_LAUNCH and arg_8_1 > self.GetTemplate().extra_param.launchRiseTime + self._timeStamp:
			self.CompleteRise()

	def CompleteRise(self):
		self._state = self.STATE_ATTACK
		self._gravity = 0

		if self._onTheHighest:
			self._onTheHighest()

		var_9_0 = self.GetTemplate().extra_param.fallTime

		self._targetPos = self._explodePos
		self._yAngle = math.rad2Deg * math.atan2(self._explodePos.z - self._spawnPos.z, self._explodePos.x - self._spawnPos.x)
		self._verticalSpeed = -(self._position.y / var_9_0) * self.viewInterval

		var_9_1 = Tool.FilterY(self._explodePos - self._position).Magnitude()

		self.ResetVelocity(BattleFormulas.ConvertBulletDataSpeed(var_9_1 / var_9_0 * self.viewInterval))
		self.calcSpeed()

	def IsOutRange(self):
		return self._state == self.STATE_ATTACK and self._position.y <= BattleConfig.BombDetonateHeight

	def OutRange(self, arg_11_1):
		var_11_0 = table(
			UID = arg_11_1
		)

		self.DispatchEvent(Event.New(BattleBulletEvent.EXPLODE, var_11_0))
		super.OutRange(self)

	def GetMissileTargetPosition(self):
		if self._targetType == self.TYPE_RANGE:
			return self.aimRange()
		elif self._targetType == self.TYPE_COORD:
			return self.aimCoord()
		elif self._targetType == self.TYPE_TARGET:
			return self.aimTarget()

	def aimRange(self):
		var_13_0 = self._range
		var_13_1 = self._range * self.GetIFF()

		return (Vector3(self._spawnPos.x + var_13_1, 0, 0))

	def aimCoord(self):
		var_14_0 = self.GetTemplate().extra_param
		var_14_1 = var_14_0.missileX
		var_14_2 = var_14_0.missileZ

		if not var_14_1 or not var_14_2:
			return self.aimRange()

		return (Vector3(var_14_1, 0, var_14_2))

	def aimTarget(self):
		var_15_0 = self.GetWeapon()
		var_15_1 = var_15_0.GetHost()

		if not var_15_1 or not var_15_1.IsAlive():
			return self.aimCoord()

		var_15_2 = var_15_0.Tracking()

		return var_15_0.GetTemplateData().aim_type == BattleConst.WeaponAimType.AIM and var_15_2 and var_15_0.CalculateRandTargetPosition(self, var_15_2) or var_15_0.CalculateFixedExplodePosition(self)
