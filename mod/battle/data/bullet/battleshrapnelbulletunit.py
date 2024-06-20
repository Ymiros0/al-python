from luatable import table, Clone, ipairs
from Vector3 import Vector3
import math
import BattleBulletUnit

import BattleConfig
import BattleBulletEvent
import BattleDataFunction
import BattleFormulas

from Framework.event import Event
from support.utils import Tool
from mgr import TimeMgr

class BattleShrapnelBulletUnit(BattleBulletUnit):
	__name = "BattleShrapnelBulletUnit"

	STATE_NORMAL = "normal"
	STATE_SPLIT = "split"
	STATE_SPIN = "spin"
	STATE_FINAL_SPLIT = "final_split"
	STATE_EXPIRE = "expire"
	STATE_PRIORITY = table({
		STATE_EXPIRE: 5,
		STATE_FINAL_SPLIT: 4,
		STATE_SPLIT: 3,
		STATE_SPIN: 2,
		STATE_NORMAL: 1
	})

	def __init__(arg_1_0, arg_1_1, arg_1_2):
		super().__init__(arg_1_0, arg_1_1, arg_1_2)

		arg_1_0._splitCount = 0
		arg_1_0._cacheEmitter = {}

		arg_1_0.ChangeShrapnelState(arg_1_0.STATE_NORMAL)

	def Hit(arg_2_0, arg_2_1, arg_2_2):
		if arg_2_0.GetTemplate().extra_param.rangeAA:
			return

		super().Hit(arg_2_0, arg_2_1, arg_2_2)

		arg_2_0._pierceCount = arg_2_0._pierceCount - 1

	def SplitFinishCount(arg_3_0):
		arg_3_0._splitCount = arg_3_0._splitCount + 1

	def IsAllSplitFinish(arg_4_0):
		return arg_4_0._splitCount >= len(arg_4_0._tempData.extra_param.shrapnel)

	def Update(self, arg_5_1):
		if self._currentState == self.STATE_NORMAL:
			var_5_0 = self._verticalSpeed

			super().Update(self, arg_5_1)

			if var_5_0 != 0 and var_5_0 * self._verticalSpeed < 0:
				self.ChangeShrapnelState(self.STATE_SPLIT)
		elif self._currentState == self.STATE_SPIN and (not self._tempData.extra_param.lastTime or arg_5_1 - self._spinStartTime > self._tempData.extra_param.lastTime):
			self.ChangeShrapnelState(self.STATE_SPLIT)

	def ChangeShrapnelState(self, arg_6_1):
		var_6_0 = self.STATE_PRIORITY[self._currentState]

		if var_6_0 and var_6_0 >= self.STATE_PRIORITY[arg_6_1]:
			return

		self._currentState = arg_6_1

		if self._currentState == self.STATE_SPIN:
			self._spinStartTime = TimeMgr.GetInstance().GetCombatTime()
		elif self._currentState == self.STATE_SPLIT:
			self.DispatchEvent(Event.New(BattleBulletEvent.SPLIT, {}))

	def IsOutRange(self, arg_7_1):
		if self._currentState == self.STATE_NORMAL:
			return super().IsOutRange(self, arg_7_1)
		else:
			return False

	def SetSrcHost(self, arg_8_1):
		self._srcHost = arg_8_1

	def GetSrcHost(arg_9_0):
		return arg_9_0._srcHost

	def GetShrapnelParam(arg_10_0):
		return arg_10_0._tempData.extra_param

	def GetCurrentState(arg_11_0):
		return arg_11_0._currentState

	def SetSpawnPosition(arg_12_0, arg_12_1):
		super().SetSpawnPosition(arg_12_0, arg_12_1)

		var_12_0 = arg_12_0.GetTemplate().extra_param
		var_12_1 = Tool.FilterY(arg_12_0._spawnPos)
		var_12_2 = Vector3.Distance(var_12_1, Tool.FilterY(arg_12_0._explodePos))

		if var_12_0.flare:
			var_12_3 = var_12_0.shrapnel[1].bullet_ID
			var_12_4 = BattleDataFunction.GetBulletTmpDataFromID(var_12_3)
			var_12_5 = var_12_4.hit_type.time
			var_12_6 = 0.5 * abs(var_12_4.extra_param.gravity or -0.0005) * (var_12_5 * BattleConfig.calcFPS)^2 - arg_12_0._spawnPos.y

			arg_12_0._convertedVelocity = math.sqrt(-0.5 * arg_12_0._gravity * var_12_2 * var_12_2 / var_12_6)

			var_12_7 = var_12_2 / arg_12_0._convertedVelocity

			arg_12_0._verticalSpeed = var_12_6 / var_12_7 - 0.5 * arg_12_0._gravity * var_12_7
		elif var_12_0.rangeAA:
			var_12_8 = BattleConfig.AircraftHeight - arg_12_0._spawnPos.y
			var_12_9 = 0.5 * arg_12_0._gravity

			arg_12_0._velocity = math.sqrt(-var_12_9 * var_12_2 * var_12_2 / var_12_8)

			var_12_10 = var_12_2 / arg_12_0._velocity

			arg_12_0._verticalSpeed = var_12_8 / var_12_10 - var_12_9 * var_12_10
			arg_12_0._velocity = BattleFormulas.ConvertBulletDataSpeed(arg_12_0._velocity)
		elif arg_12_0._convertedVelocity != 0:
			var_12_11 = var_12_2 / arg_12_0._convertedVelocity
			var_12_12 = arg_12_0._explodePos.y - arg_12_0._spawnPos.y

			arg_12_0._verticalSpeed = var_12_0.launchVrtSpeed or var_12_12 / var_12_11 - 0.5 * arg_12_0._gravity * var_12_11

	def GetExplodePostion(arg_13_0):
		return arg_13_0._explodePos

	def SetExplodePosition(arg_14_0, arg_14_1):
		arg_14_0._explodePos = Clone(arg_14_1)
		arg_14_0._explodePos.y = BattleConfig.BombDetonateHeight

	def CacheChildEimtter(arg_15_0, arg_15_1):
		table.insert(arg_15_0._cacheEmitter, arg_15_1)

	def interruptChildEmitter(arg_16_0):
		for iter_16_0, iter_16_1 in ipairs(arg_16_0._cacheEmitter):
			iter_16_1.Destroy()

	def Dispose(arg_17_0):
		arg_17_0.interruptChildEmitter()

		arg_17_0._cacheEmitter = None

		super().Dispose(arg_17_0)
