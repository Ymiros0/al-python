from luatable import pairs, table
import math
from alsupport import tonumber


from Framework.tolua.unityengine.Time import Time
import TimeUtil
from Framework.tolua.event import UpdateBeat
import os
from Framework.tolua.system.Timer import Timer
from RunPaintingFilte import PLATFORM_CODE, PLATFORM_US
from support.helpers.LuaSupport import originalPrint
from support.helpers.M02 import NumberToChinese
from Framework import underscore


class TimeMgr: #singleton!

	_Timer = None
	_BattleTimer = None
	_sAnchorTime = 0
	_AnchorDelta = 0
	_serverUnitydelta = 0
	_isdstClient = False

	var_0_2 = 3600
	var_0_3 = 86400
	var_0_4 = 604800

	def Ctor(self):
		self._battleTimerList = table()

	def Init(self):
		print("initializing time manager+.")

		self._Timer = TimeUtil.NewUnityTimer()

		UpdateBeat.Add(self.Update, self)
		UpdateBeat.Add(self.BattleUpdate, self)

	def Update(self):
		self._Timer.Schedule()

	def BattleUpdate(self):
		if self._stopCombatTime > 0:
			self._cobTime = self._stopCombatTime - self._waitTime
		else:
			self._cobTime = Time.time - self._waitTime

	def AddTimer(self, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
		return self._Timer.SetTimer(arg_5_1, arg_5_2 * 1000, arg_5_3 * 1000, arg_5_4)

	def RemoveTimer(self, arg_6_1):
		if arg_6_1 == None or arg_6_1 == 0:
			return

		self._Timer.DeleteTimer(arg_6_1)

	_waitTime = 0
	_stopCombatTime = 0
	_cobTime = 0

	def GetCombatTime(self):
		return self._cobTime

	def ResetCombatTime(self):
		self._waitTime = 0
		self._cobTime = Time.time

	def GetCombatDeltaTime():
		return Time.fixedDeltaTime

	def PauseBattleTimer(self):
		self._stopCombatTime = Time.time

		for iter_10_0, iter_10_1 in pairs(self._battleTimerList):
			iter_10_0.Pause()

	def ResumeBattleTimer(self):
		self._waitTime = self._waitTime + Time.time - self._stopCombatTime
		self._stopCombatTime = 0

		for iter_11_0, iter_11_1 in pairs(self._battleTimerList):
			iter_11_0.Resume()

	def AddBattleTimer(self, arg_12_1, arg_12_2, arg_12_3, arg_12_4, arg_12_5, arg_12_6):
		arg_12_2 = arg_12_2 or -1
		arg_12_5 = arg_12_5 or False
		arg_12_6 = arg_12_6 or False

		var_12_0 = Timer.New(arg_12_4, arg_12_3, arg_12_2, arg_12_5)

		self._battleTimerList[var_12_0] = True

		if not arg_12_6:
			var_12_0.Start()

		if self._stopCombatTime != 0:
			var_12_0.Pause()

		return var_12_0

	def ScaleBattleTimer(self, arg_13_1):
		Time.timeScale = arg_13_1

	def RemoveBattleTimer(self, arg_14_1):
		if arg_14_1:
			self._battleTimerList[arg_14_1] = None

			arg_14_1.Stop()

	def RemoveAllBattleTimer(self):
		for iter_15_0, iter_15_1 in pairs(self._battleTimerList):
			iter_15_0.Stop()

		self._battleTimerList = table()

	def RealtimeSinceStartup(self):
		return math.ceil(Time.realtimeSinceStartup)

	def SetServerTime(self, arg_17_1, arg_17_2):
		self._SetServerTime_(arg_17_1, arg_17_2, self.RealtimeSinceStartup())

	def _SetServerTime_(self, arg_18_1, arg_18_2, arg_18_3):
		if PLATFORM_CODE == PLATFORM_US:
			self.SERVER_DAYLIGHT_SAVEING_TIME = False

		self._isdstClient = os.date("*t").isdst
		self._serverUnitydelta = arg_18_1 - arg_18_3
		self._sAnchorTime = arg_18_2 - (self.SERVER_DAYLIGHT_SAVEING_TIME and 3600 or 0)
		self._AnchorDelta = arg_18_2 - os.time(table(
			year = 2020,
			month = 11,
			hour = 0,
			min = 0,
			sec = 0,
			day = 23,
			isdst = False
		))

	def GetServerTime(self):
		return self.RealtimeSinceStartup() + self._serverUnitydelta

	def GetServerWeek(self):
		var_20_0 = self.GetServerTime()

		return self.GetServerTimestampWeek(var_20_0)

	def GetServerTimestampWeek(self, arg_21_1):
		var_21_0 = arg_21_1 - self._sAnchorTime

		return math.ceil((var_21_0 % self.var_0_4 + 1) / self.var_0_3)

	def GetServerHour(self):
		var_22_0 = self.GetServerTime() - self._sAnchorTime

		return math.floor(var_22_0 % self.var_0_3 / self.var_0_2)

	def Table2ServerTime(self, arg_23_1):
		arg_23_1.isdst = self._isdstClient

		if self._isdstClient != self.SERVER_DAYLIGHT_SAVEING_TIME:
			if self.SERVER_DAYLIGHT_SAVEING_TIME:
				return self._AnchorDelta + os.time(arg_23_1) - self.var_0_2
			else:
				return self._AnchorDelta + os.time(arg_23_1) + self.var_0_2
		else:
			return self._AnchorDelta + os.time(arg_23_1)

	def CTimeDescC(self, arg_24_1, arg_24_2):
		arg_24_2 = arg_24_2 or "%Y%m%d%H%M%S"

		return os.date(arg_24_2, arg_24_1)

	def STimeDescC(self, arg_25_1, arg_25_2, arg_25_3):
		originalPrint("Before . ", arg_25_1)

		arg_25_2 = arg_25_2 or "%Y/%m/%d %H.%M.%S"

		if arg_25_3:
			originalPrint("2after . ", os.date(arg_25_2, arg_25_1))

			return os.date(arg_25_2, arg_25_1 + os.time() - self.GetServerTime())
		else:
			originalPrint("1after . ", os.date(arg_25_2, arg_25_1))

			return os.date(arg_25_2, arg_25_1)

	def STimeDescS(self, arg_26_1, arg_26_2):
		arg_26_2 = arg_26_2 or "%Y/%m/%d %H.%M.%S"

		var_26_0 = 0

		if self._isdstClient != self.SERVER_DAYLIGHT_SAVEING_TIME:
			var_26_0 = self.SERVER_DAYLIGHT_SAVEING_TIME and 3600 or -3600

		return os.date(arg_26_2, arg_26_1 - self._AnchorDelta + var_26_0)

	def CurrentSTimeDesc(self, arg_27_1, arg_27_2):
		if arg_27_2:
			return self.STimeDescS(self.GetServerTime(), arg_27_1)
		else:
			return self.STimeDescC(self.GetServerTime(), arg_27_1)

	def ChieseDescTime(self, arg_28_1, arg_28_2):
		var_28_0 = "%Y/%m/%d"

		if arg_28_2:
			var_28_1 = os.date(var_28_0, arg_28_1)
		else:
			var_28_1 = os.date(var_28_0, arg_28_1 + os.time() - self.GetServerTime())

		var_28_2 = var_28_1.split("/")

		return NumberToChinese(var_28_2[1], False) + "年" + NumberToChinese(var_28_2[2], True) + "月" + NumberToChinese(var_28_2[3], True) + "日"

	def GetTimeToNextTime(self, arg_29_1, arg_29_2, arg_29_3):
		arg_29_1 = arg_29_1 or self.GetServerTime()
		arg_29_2 = arg_29_2 or self.var_0_3
		arg_29_3 = arg_29_3 or 0

		var_29_0 = arg_29_1 - (self._sAnchorTime + arg_29_3)

		return math.floor(var_29_0 / arg_29_2 + 1) * arg_29_2 + self._sAnchorTime + arg_29_3

	def GetNextTime(self, arg_30_1, arg_30_2, arg_30_3, arg_30_4):
		return self.GetTimeToNextTime(None, arg_30_4, arg_30_1 * self.var_0_2 + arg_30_2 * 60 + arg_30_3)

	def GetNextTimeByTimeStamp(self, arg_31_1):
		return self.GetTimeToNextTime(arg_31_1) - self.var_0_3

	def GetNextWeekTime(self, arg_32_1, arg_32_2, arg_32_3, arg_32_4):
		return self.GetNextTime((arg_32_1 - 1) * 24 + arg_32_2, arg_32_3, arg_32_4, self.var_0_4)

	def ParseTime(self, arg_33_1):
		var_33_0 = tonumber(arg_33_1)
		var_33_1 = var_33_0 % 100
		var_33_2 = var_33_0 / 100
		var_33_3 = var_33_2 % 100
		var_33_4 = var_33_2 / 100
		var_33_5 = var_33_4 % 100
		var_33_6 = var_33_4 / 100
		var_33_7 = var_33_6 % 100
		var_33_8 = var_33_6 / 100
		var_33_9 = var_33_8 % 100
		var_33_10 = var_33_8 / 100

		return self.Table2ServerTime(table(
			year = var_33_10,
			month = var_33_9,
			day = var_33_7,
			hour = var_33_5,
			min = var_33_3,
			sec = var_33_1
		))

	def ParseTimeEx(self, arg_34_1, arg_34_2):
		if arg_34_2 == None:
			arg_34_2 = "(%d+)%-(%d+)%-(%d+)%s(%d+)%.(%d+)%.(%d+)"

		var_34_0, var_34_1, var_34_2, var_34_3, var_34_4, var_34_5 = arg_34_1.match(arg_34_2)

		return self.Table2ServerTime(table(
			year = var_34_0,
			month = var_34_1,
			day = var_34_2,
			hour = var_34_3,
			min = var_34_4,
			sec = var_34_5
		))

	def parseTimeFromConfig(self, arg_35_1):
		return self.Table2ServerTime(table(
			year = arg_35_1[1][1],
			month = arg_35_1[1][2],
			day = arg_35_1[1][3],
			hour = arg_35_1[2][1],
			min = arg_35_1[2][2],
			sec = arg_35_1[2][3]
		))

	def DescDateFromConfig(self, arg_36_1, arg_36_2="%d.%02d.%02d"):

		return arg_36_2 % (arg_36_1[1][1], arg_36_1[1][2], arg_36_1[1][3])

	def DescCDTime(self, arg_37_1):
		var_37_0 = math.floor(arg_37_1 / 3600)

		arg_37_1 = arg_37_1 % 3600

		var_37_1 = math.floor(arg_37_1 / 60)

		arg_37_1 = arg_37_1 % 60

		return "%02d.%02d.%02d" % (var_37_0, var_37_1, arg_37_1)

	def DescCDTimeForMinute(self, arg_38_1):
		var_38_0 = math.floor(arg_38_1 / 3600)

		arg_38_1 = arg_38_1 % 3600

		var_38_1 = math.floor(arg_38_1 / 60)

		arg_38_1 = arg_38_1 % 60

		return "%02d.%02d" % (var_38_1, arg_38_1)

	def parseTimeFrom(self, arg_39_1):
		var_39_0 = math.floor(arg_39_1 / self.var_0_3)
		var_39_1 = math.fmod(math.floor(arg_39_1 / 3600), 24)
		var_39_2 = math.fmod(math.floor(arg_39_1 / 60), 60)
		var_39_3 = math.fmod(arg_39_1, 60)

		return var_39_0, var_39_1, var_39_2, var_39_3

	def DiffDay(self, arg_40_1, arg_40_2):
		return math.floor((arg_40_2 - self._sAnchorTime) / self.var_0_3) - math.floor((arg_40_1 - self._sAnchorTime) / self.var_0_3)

	def IsSameDay(self, arg_41_1, arg_41_2):
		return math.floor((arg_41_1 - self._sAnchorTime) / self.var_0_3) == math.floor((arg_41_2 - self._sAnchorTime) / self.var_0_3)

	def IsPassTimeByZero(self, arg_42_1, arg_42_2):
		return arg_42_2 < math.fmod(arg_42_1 - self._sAnchorTime, self.var_0_3)

	def CalcMonthDays(self, arg_43_1, arg_43_2):
		var_43_0 = 30

		if arg_43_2 == 2:
			var_43_0 = (arg_43_1 % 4 == 0 and arg_43_1 % 100 != 0 or arg_43_1 % 400 == 0) and 29 or 28
		elif underscore.include(table(
			1,
			3,
			5,
			7,
			8,
			10,
			12
		), arg_43_2):
			var_43_0 = 31

		return var_43_0

	def inTime(self, arg_44_1, arg_44_2):
		if not arg_44_1:
			return True

		if type(arg_44_1) == "string":
			return arg_44_1 == "always"

		if type(arg_44_1[1]) == "string":
			arg_44_1 = table(
				arg_44_1[2],
				arg_44_1[3]
			)

		def var_44_0(x):
			return table(
				year = x[1][1],
				month = x[1][2],
				day = x[1][3],
				hour = x[2][1],
				min = x[2][2],
				sec = x[2][3]
			)

		var_44_1 = None
		if len(arg_44_1) > 0:
			var_44_1 = var_44_0(arg_44_1[1] or table(
				table(
					2000,
					1,
					1
				),
				table(
					0,
					0,
					0
				)
			))

		var_44_2 = None
		if len(arg_44_1) > 1:
			var_44_2 = var_44_0(arg_44_1[2] or table(
				table(
					2000,
					1,
					1
				),
				table(
					0,
					0,
					0
				)
			))


		if var_44_1 and var_44_2:
			var_44_4 = arg_44_2 or self.GetServerTime()
			var_44_5 = self.Table2ServerTime(var_44_1)
			var_44_6 = self.Table2ServerTime(var_44_2)

			if var_44_4 < var_44_5:
				return False, var_44_1

			if var_44_6 < var_44_4:
				return False, None

			var_44_3 = var_44_2

		return True, var_44_3

	def passTime(self, arg_46_1):
		if not arg_46_1:
			return True

		def _func(x):
			var_47_0 = table()

			var_47_0.year, var_47_0.month, var_47_0.day = x[1]
			var_47_0.hour, var_47_0.min, var_47_0.sec = x[2]

			return var_47_0

		var_46_0 = _func(arg_46_1 or table(
			table(
				2000,
				1,
				1
			),
			table(
				0,
				0,
				0
			)
		))

		if var_46_0:
			return self.GetServerTime() > self.Table2ServerTime(var_46_0)

		return True
