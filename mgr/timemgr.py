pg = pg or {}

local var_0_0 = pg

var_0_0.TimeMgr = singletonClass("TimeMgr")

local var_0_1 = var_0_0.TimeMgr

var_0_1._Timer = None
var_0_1._BattleTimer = None
var_0_1._sAnchorTime = 0
var_0_1._AnchorDelta = 0
var_0_1._serverUnitydelta = 0
var_0_1._isdstClient = False

local var_0_2 = 3600
local var_0_3 = 86400
local var_0_4 = 604800

def var_0_1.Ctor(arg_1_0):
	arg_1_0._battleTimerList = {}

def var_0_1.Init(arg_2_0):
	print("initializing time manager...")

	arg_2_0._Timer = TimeUtil.NewUnityTimer()

	UpdateBeat.Add(arg_2_0.Update, arg_2_0)
	UpdateBeat.Add(arg_2_0.BattleUpdate, arg_2_0)

def var_0_1.Update(arg_3_0):
	arg_3_0._Timer.Schedule()

def var_0_1.BattleUpdate(arg_4_0):
	if arg_4_0._stopCombatTime > 0:
		arg_4_0._cobTime = arg_4_0._stopCombatTime - arg_4_0._waitTime
	else
		arg_4_0._cobTime = Time.time - arg_4_0._waitTime

def var_0_1.AddTimer(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	return arg_5_0._Timer.SetTimer(arg_5_1, arg_5_2 * 1000, arg_5_3 * 1000, arg_5_4)

def var_0_1.RemoveTimer(arg_6_0, arg_6_1):
	if arg_6_1 == None or arg_6_1 == 0:
		return

	arg_6_0._Timer.DeleteTimer(arg_6_1)

var_0_1._waitTime = 0
var_0_1._stopCombatTime = 0
var_0_1._cobTime = 0

def var_0_1.GetCombatTime(arg_7_0):
	return arg_7_0._cobTime

def var_0_1.ResetCombatTime(arg_8_0):
	arg_8_0._waitTime = 0
	arg_8_0._cobTime = Time.time

def var_0_1.GetCombatDeltaTime():
	return Time.fixedDeltaTime

def var_0_1.PauseBattleTimer(arg_10_0):
	arg_10_0._stopCombatTime = Time.time

	for iter_10_0, iter_10_1 in pairs(arg_10_0._battleTimerList):
		iter_10_0.Pause()

def var_0_1.ResumeBattleTimer(arg_11_0):
	arg_11_0._waitTime = arg_11_0._waitTime + Time.time - arg_11_0._stopCombatTime
	arg_11_0._stopCombatTime = 0

	for iter_11_0, iter_11_1 in pairs(arg_11_0._battleTimerList):
		iter_11_0.Resume()

def var_0_1.AddBattleTimer(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4, arg_12_5, arg_12_6):
	arg_12_2 = arg_12_2 or -1
	arg_12_5 = arg_12_5 or False
	arg_12_6 = arg_12_6 or False

	local var_12_0 = Timer.New(arg_12_4, arg_12_3, arg_12_2, arg_12_5)

	arg_12_0._battleTimerList[var_12_0] = True

	if not arg_12_6:
		var_12_0.Start()

	if arg_12_0._stopCombatTime != 0:
		var_12_0.Pause()

	return var_12_0

def var_0_1.ScaleBattleTimer(arg_13_0, arg_13_1):
	Time.timeScale = arg_13_1

def var_0_1.RemoveBattleTimer(arg_14_0, arg_14_1):
	if arg_14_1:
		arg_14_0._battleTimerList[arg_14_1] = None

		arg_14_1.Stop()

def var_0_1.RemoveAllBattleTimer(arg_15_0):
	for iter_15_0, iter_15_1 in pairs(arg_15_0._battleTimerList):
		iter_15_0.Stop()

	arg_15_0._battleTimerList = {}

def var_0_1.RealtimeSinceStartup(arg_16_0):
	return math.ceil(Time.realtimeSinceStartup)

def var_0_1.SetServerTime(arg_17_0, arg_17_1, arg_17_2):
	arg_17_0._SetServerTime_(arg_17_1, arg_17_2, arg_17_0.RealtimeSinceStartup())

def var_0_1._SetServerTime_(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	if PLATFORM_CODE == PLATFORM_US:
		SERVER_DAYLIGHT_SAVEING_TIME = False

	arg_18_0._isdstClient = os.date("*t").isdst
	arg_18_0._serverUnitydelta = arg_18_1 - arg_18_3
	arg_18_0._sAnchorTime = arg_18_2 - (SERVER_DAYLIGHT_SAVEING_TIME and 3600 or 0)
	arg_18_0._AnchorDelta = arg_18_2 - os.time({
		year = 2020,
		month = 11,
		hour = 0,
		min = 0,
		sec = 0,
		day = 23,
		isdst = False
	})

def var_0_1.GetServerTime(arg_19_0):
	return arg_19_0.RealtimeSinceStartup() + arg_19_0._serverUnitydelta

def var_0_1.GetServerWeek(arg_20_0):
	local var_20_0 = arg_20_0.GetServerTime()

	return arg_20_0.GetServerTimestampWeek(var_20_0)

def var_0_1.GetServerTimestampWeek(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_1 - arg_21_0._sAnchorTime

	return math.ceil((var_21_0 % var_0_4 + 1) / var_0_3)

def var_0_1.GetServerHour(arg_22_0):
	local var_22_0 = arg_22_0.GetServerTime() - arg_22_0._sAnchorTime

	return math.floor(var_22_0 % var_0_3 / var_0_2)

def var_0_1.Table2ServerTime(arg_23_0, arg_23_1):
	arg_23_1.isdst = arg_23_0._isdstClient

	if arg_23_0._isdstClient != SERVER_DAYLIGHT_SAVEING_TIME:
		if SERVER_DAYLIGHT_SAVEING_TIME:
			return arg_23_0._AnchorDelta + os.time(arg_23_1) - var_0_2
		else
			return arg_23_0._AnchorDelta + os.time(arg_23_1) + var_0_2
	else
		return arg_23_0._AnchorDelta + os.time(arg_23_1)

def var_0_1.CTimeDescC(arg_24_0, arg_24_1, arg_24_2):
	arg_24_2 = arg_24_2 or "%Y%m%d%H%M%S"

	return os.date(arg_24_2, arg_24_1)

def var_0_1.STimeDescC(arg_25_0, arg_25_1, arg_25_2, arg_25_3):
	originalPrint("Before . ", arg_25_1)

	arg_25_2 = arg_25_2 or "%Y/%m/%d %H.%M.%S"

	if arg_25_3:
		originalPrint("2after . ", os.date(arg_25_2, arg_25_1))

		return os.date(arg_25_2, arg_25_1 + os.time() - arg_25_0.GetServerTime())
	else
		originalPrint("1after . ", os.date(arg_25_2, arg_25_1))

		return os.date(arg_25_2, arg_25_1)

def var_0_1.STimeDescS(arg_26_0, arg_26_1, arg_26_2):
	arg_26_2 = arg_26_2 or "%Y/%m/%d %H.%M.%S"

	local var_26_0 = 0

	if arg_26_0._isdstClient != SERVER_DAYLIGHT_SAVEING_TIME:
		var_26_0 = SERVER_DAYLIGHT_SAVEING_TIME and 3600 or -3600

	return os.date(arg_26_2, arg_26_1 - arg_26_0._AnchorDelta + var_26_0)

def var_0_1.CurrentSTimeDesc(arg_27_0, arg_27_1, arg_27_2):
	if arg_27_2:
		return arg_27_0.STimeDescS(arg_27_0.GetServerTime(), arg_27_1)
	else
		return arg_27_0.STimeDescC(arg_27_0.GetServerTime(), arg_27_1)

def var_0_1.ChieseDescTime(arg_28_0, arg_28_1, arg_28_2):
	local var_28_0 = "%Y/%m/%d"
	local var_28_1

	if arg_28_2:
		var_28_1 = os.date(var_28_0, arg_28_1)
	else
		var_28_1 = os.date(var_28_0, arg_28_1 + os.time() - arg_28_0.GetServerTime())

	local var_28_2 = split(var_28_1, "/")

	return NumberToChinese(var_28_2[1], False) .. "年" .. NumberToChinese(var_28_2[2], True) .. "月" .. NumberToChinese(var_28_2[3], True) .. "日"

def var_0_1.GetTimeToNextTime(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	arg_29_1 = arg_29_1 or arg_29_0.GetServerTime()
	arg_29_2 = arg_29_2 or var_0_3
	arg_29_3 = arg_29_3 or 0

	local var_29_0 = arg_29_1 - (arg_29_0._sAnchorTime + arg_29_3)

	return math.floor(var_29_0 / arg_29_2 + 1) * arg_29_2 + arg_29_0._sAnchorTime + arg_29_3

def var_0_1.GetNextTime(arg_30_0, arg_30_1, arg_30_2, arg_30_3, arg_30_4):
	return arg_30_0.GetTimeToNextTime(None, arg_30_4, arg_30_1 * var_0_2 + arg_30_2 * 60 + arg_30_3)

def var_0_1.GetNextTimeByTimeStamp(arg_31_0, arg_31_1):
	return arg_31_0.GetTimeToNextTime(arg_31_1) - var_0_3

def var_0_1.GetNextWeekTime(arg_32_0, arg_32_1, arg_32_2, arg_32_3, arg_32_4):
	return arg_32_0.GetNextTime((arg_32_1 - 1) * 24 + arg_32_2, arg_32_3, arg_32_4, var_0_4)

def var_0_1.ParseTime(arg_33_0, arg_33_1):
	local var_33_0 = tonumber(arg_33_1)
	local var_33_1 = var_33_0 % 100
	local var_33_2 = var_33_0 / 100
	local var_33_3 = var_33_2 % 100
	local var_33_4 = var_33_2 / 100
	local var_33_5 = var_33_4 % 100
	local var_33_6 = var_33_4 / 100
	local var_33_7 = var_33_6 % 100
	local var_33_8 = var_33_6 / 100
	local var_33_9 = var_33_8 % 100
	local var_33_10 = var_33_8 / 100

	return arg_33_0.Table2ServerTime({
		year = var_33_10,
		month = var_33_9,
		day = var_33_7,
		hour = var_33_5,
		min = var_33_3,
		sec = var_33_1
	})

def var_0_1.ParseTimeEx(arg_34_0, arg_34_1, arg_34_2):
	if arg_34_2 == None:
		arg_34_2 = "(%d+)%-(%d+)%-(%d+)%s(%d+)%.(%d+)%.(%d+)"

	local var_34_0, var_34_1, var_34_2, var_34_3, var_34_4, var_34_5 = arg_34_1.match(arg_34_2)

	return arg_34_0.Table2ServerTime({
		year = var_34_0,
		month = var_34_1,
		day = var_34_2,
		hour = var_34_3,
		min = var_34_4,
		sec = var_34_5
	})

def var_0_1.parseTimeFromConfig(arg_35_0, arg_35_1):
	return arg_35_0.Table2ServerTime({
		year = arg_35_1[1][1],
		month = arg_35_1[1][2],
		day = arg_35_1[1][3],
		hour = arg_35_1[2][1],
		min = arg_35_1[2][2],
		sec = arg_35_1[2][3]
	})

def var_0_1.DescDateFromConfig(arg_36_0, arg_36_1, arg_36_2):
	arg_36_2 = arg_36_2 or "%d.%02d.%02d"

	return string.format(arg_36_2, arg_36_1[1][1], arg_36_1[1][2], arg_36_1[1][3])

def var_0_1.DescCDTime(arg_37_0, arg_37_1):
	local var_37_0 = math.floor(arg_37_1 / 3600)

	arg_37_1 = arg_37_1 % 3600

	local var_37_1 = math.floor(arg_37_1 / 60)

	arg_37_1 = arg_37_1 % 60

	return string.format("%02d.%02d.%02d", var_37_0, var_37_1, arg_37_1)

def var_0_1.DescCDTimeForMinute(arg_38_0, arg_38_1):
	local var_38_0 = math.floor(arg_38_1 / 3600)

	arg_38_1 = arg_38_1 % 3600

	local var_38_1 = math.floor(arg_38_1 / 60)

	arg_38_1 = arg_38_1 % 60

	return string.format("%02d.%02d", var_38_1, arg_38_1)

def var_0_1.parseTimeFrom(arg_39_0, arg_39_1):
	local var_39_0 = math.floor(arg_39_1 / var_0_3)
	local var_39_1 = math.fmod(math.floor(arg_39_1 / 3600), 24)
	local var_39_2 = math.fmod(math.floor(arg_39_1 / 60), 60)
	local var_39_3 = math.fmod(arg_39_1, 60)

	return var_39_0, var_39_1, var_39_2, var_39_3

def var_0_1.DiffDay(arg_40_0, arg_40_1, arg_40_2):
	return math.floor((arg_40_2 - arg_40_0._sAnchorTime) / var_0_3) - math.floor((arg_40_1 - arg_40_0._sAnchorTime) / var_0_3)

def var_0_1.IsSameDay(arg_41_0, arg_41_1, arg_41_2):
	return math.floor((arg_41_1 - arg_41_0._sAnchorTime) / var_0_3) == math.floor((arg_41_2 - arg_41_0._sAnchorTime) / var_0_3)

def var_0_1.IsPassTimeByZero(arg_42_0, arg_42_1, arg_42_2):
	return arg_42_2 < math.fmod(arg_42_1 - arg_42_0._sAnchorTime, var_0_3)

def var_0_1.CalcMonthDays(arg_43_0, arg_43_1, arg_43_2):
	local var_43_0 = 30

	if arg_43_2 == 2:
		var_43_0 = (arg_43_1 % 4 == 0 and arg_43_1 % 100 != 0 or arg_43_1 % 400 == 0) and 29 or 28
	elif _.include({
		1,
		3,
		5,
		7,
		8,
		10,
		12
	}, arg_43_2):
		var_43_0 = 31

	return var_43_0

def var_0_1.inTime(arg_44_0, arg_44_1, arg_44_2):
	if not arg_44_1:
		return True

	if type(arg_44_1) == "string":
		return arg_44_1 == "always"

	if type(arg_44_1[1]) == "string":
		arg_44_1 = {
			arg_44_1[2],
			arg_44_1[3]
		}

	local function var_44_0(arg_45_0)
		return {
			year = arg_45_0[1][1],
			month = arg_45_0[1][2],
			day = arg_45_0[1][3],
			hour = arg_45_0[2][1],
			min = arg_45_0[2][2],
			sec = arg_45_0[2][3]
		}

	local var_44_1

	if #arg_44_1 > 0:
		var_44_1 = var_44_0(arg_44_1[1] or {
			{
				2000,
				1,
				1
			},
			{
				0,
				0,
				0
			}
		})

	local var_44_2

	if #arg_44_1 > 1:
		var_44_2 = var_44_0(arg_44_1[2] or {
			{
				2000,
				1,
				1
			},
			{
				0,
				0,
				0
			}
		})

	local var_44_3

	if var_44_1 and var_44_2:
		local var_44_4 = arg_44_2 or arg_44_0.GetServerTime()
		local var_44_5 = arg_44_0.Table2ServerTime(var_44_1)
		local var_44_6 = arg_44_0.Table2ServerTime(var_44_2)

		if var_44_4 < var_44_5:
			return False, var_44_1

		if var_44_6 < var_44_4:
			return False, None

		var_44_3 = var_44_2

	return True, var_44_3

def var_0_1.passTime(arg_46_0, arg_46_1):
	if not arg_46_1:
		return True

	local var_46_0 = (function(arg_47_0)
		local var_47_0 = {}

		var_47_0.year, var_47_0.month, var_47_0.day = unpack(arg_47_0[1])
		var_47_0.hour, var_47_0.min, var_47_0.sec = unpack(arg_47_0[2])

		return var_47_0)(arg_46_1 or {
		{
			2000,
			1,
			1
		},
		{
			0,
			0,
			0
		}
	})

	if var_46_0:
		return arg_46_0.GetServerTime() > arg_46_0.Table2ServerTime(var_46_0)

	return True
