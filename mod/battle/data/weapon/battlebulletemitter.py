ys = ys or {}

local var_0_0 = ys
local var_0_1 = pg
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleDataFunction
local var_0_4 = math
local var_0_5 = class("BattleBulletEmitter")

var_0_0.Battle.BattleBulletEmitter = var_0_5
var_0_5.__name = "BattleBulletEmitter"
var_0_5.STATE_ACTIVE = "ACTIVE"
var_0_5.STATE_STOP = "STOP"

def var_0_5.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._spawnFunc = arg_1_1
	arg_1_0._stopFunc = arg_1_2
	arg_1_0._barrageID = arg_1_3
	arg_1_0._barrageTemp = var_0_3.GetBarrageTmpDataFromID(arg_1_3)
	arg_1_0._offsetPriority = arg_1_0._barrageTemp.offset_prioritise
	arg_1_0._isRandomAngle = arg_1_0._barrageTemp.random_angle
	arg_1_0._timerList = {}

	if arg_1_0._barrageTemp.delta_delay != 0:
		arg_1_0.PrimalIteration = arg_1_0._advancePrimalIteration
	elif arg_1_0._barrageTemp.delay != 0:
		arg_1_0.PrimalIteration = arg_1_0._averagePrimalIteration
	else
		arg_1_0.PrimalIteration = arg_1_0._nonDelayPrimalIteration

	arg_1_0._primalMax = arg_1_0._barrageTemp.primal_repeat + 1

	function arg_1_0.timerCb(arg_2_0)
		arg_1_0._timerList[arg_2_0](arg_1_0, arg_2_0)

def var_0_5.Ready(arg_3_0):
	arg_3_0._state = arg_3_0.STATE_ACTIVE
	arg_3_0._seniorCounter = -1

	arg_3_0.ClearAllTimer()

def var_0_5.Fire(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0._target = arg_4_1
	arg_4_0._dir = arg_4_2 or var_0_2.UnitDir.RIGHT

	if not arg_4_0._convertedDirBarrage:
		arg_4_0._convertedDirBarrage = var_0_3.GetConvertedBarrageTableFromID(arg_4_0._barrageID, arg_4_0._dir)[arg_4_0._dir]

	arg_4_0.SeniorIteration()

def var_0_5.Stop(arg_5_0):
	arg_5_0._state = arg_5_0.STATE_STOP
	arg_5_0._target = None

	arg_5_0.ClearAllTimer()
	arg_5_0._stopFunc(arg_5_0)

def var_0_5.Interrupt(arg_6_0):
	arg_6_0._state = arg_6_0.STATE_STOP
	arg_6_0._target = None

	arg_6_0.ClearAllTimer()

def var_0_5.Destroy(arg_7_0):
	arg_7_0._spawnFunc = None
	arg_7_0._stopFunc = None
	arg_7_0._convertedDirBarrage = None

	if arg_7_0._timerList:
		arg_7_0.ClearAllTimer()

def var_0_5.GetState(arg_8_0):
	return arg_8_0._state

def var_0_5.ClearAllTimer(arg_9_0):
	for iter_9_0, iter_9_1 in pairs(arg_9_0._timerList):
		var_0_1.TimeMgr.GetInstance().RemoveBattleTimer(iter_9_0)

	arg_9_0._timerList = {}

def var_0_5.GenerateBullet(arg_10_0):
	local var_10_0 = arg_10_0._convertedDirBarrage[arg_10_0._primalCounter]
	local var_10_1 = var_10_0.OffsetX

	arg_10_0._delay = var_10_0.Delay

	local var_10_2

	if arg_10_0._isRandomAngle:
		var_10_2 = (var_0_4.random() - 0.5) * var_10_0.Angle
	else
		var_10_2 = var_10_0.Angle

	local var_10_3 = arg_10_0._spawnFunc(var_10_1, var_10_0.OffsetZ, var_10_2, arg_10_0._offsetPriority, arg_10_0._target, arg_10_0._primalCounter)

	if var_10_3:
		local var_10_4 = var_0_3.GenerateTransBarrage(arg_10_0._barrageID, arg_10_0._dir, arg_10_0._primalCounter)

		var_10_3.SetBarrageTransformTempate(var_10_4)

	arg_10_0.Interation()

def var_0_5.DelaySeniorFunc(arg_11_0, arg_11_1):
	var_0_1.TimeMgr.GetInstance().RemoveBattleTimer(arg_11_1)

	arg_11_0._timerList[arg_11_1] = None

	arg_11_0.PrimalIteration()

def var_0_5.SeniorIteration(arg_12_0):
	if arg_12_0._state != arg_12_0.STATE_ACTIVE:
		return

	arg_12_0._seniorCounter = arg_12_0._seniorCounter + 1

	if arg_12_0._seniorCounter > arg_12_0._barrageTemp.senior_repeat:
		arg_12_0.Stop()
	else
		arg_12_0.InitParam()

		local var_12_0

		if arg_12_0._seniorCounter == 0:
			var_12_0 = arg_12_0._barrageTemp.first_delay
		else
			var_12_0 = arg_12_0._barrageTemp.senior_delay

		if var_12_0 > 0:
			local var_12_1 = var_0_1.TimeMgr.GetInstance().AddBattleTimer("spawnBullet", -1, var_12_0, arg_12_0.timerCb, True)

			arg_12_0._timerList[var_12_1] = arg_12_0.DelaySeniorFunc
		else
			arg_12_0.PrimalIteration()

def var_0_5.InitParam(arg_13_0):
	arg_13_0._delay = arg_13_0._barrageTemp.delay
	arg_13_0._primalCounter = 1

def var_0_5.Interation(arg_14_0):
	arg_14_0._primalCounter = arg_14_0._primalCounter + 1

def var_0_5.SetTimeScale(arg_15_0, arg_15_1):
	if arg_15_0._timerList:
		for iter_15_0, iter_15_1 in pairs(arg_15_0._timerList):
			iter_15_0.SetScale(arg_15_1)

def var_0_5.DelayPrimalConst(arg_16_0, arg_16_1):
	arg_16_0.GenerateBullet()

	if arg_16_0._primalCounter > arg_16_0._primalMax:
		var_0_1.TimeMgr.GetInstance().RemoveBattleTimer(arg_16_1)

		arg_16_0._timerList[arg_16_1] = None

		arg_16_0.SeniorIteration()

def var_0_5._averagePrimalIteration(arg_17_0):
	if arg_17_0._state != arg_17_0.STATE_ACTIVE:
		return

	local var_17_0 = var_0_1.TimeMgr.GetInstance().AddBattleTimer("spawnBullet", -1, arg_17_0._delay, arg_17_0.timerCb, True)

	arg_17_0._timerList[var_17_0] = arg_17_0.DelayPrimalConst

def var_0_5.DelayPrimalAdvance(arg_18_0, arg_18_1):
	var_0_1.TimeMgr.GetInstance().RemoveBattleTimer(arg_18_1)

	arg_18_0._timerList[arg_18_1] = None

	arg_18_0.GenerateBullet()

	if arg_18_0._primalCounter > arg_18_0._primalMax:
		arg_18_0.SeniorIteration()
	else
		arg_18_0.PrimalIteration()

def var_0_5._advancePrimalIteration(arg_19_0):
	if arg_19_0._state != arg_19_0.STATE_ACTIVE:
		return

	if arg_19_0._delay == 0:
		arg_19_0.GenerateBullet()

		if arg_19_0._primalCounter > arg_19_0._primalMax:
			arg_19_0.SeniorIteration()
		else
			arg_19_0.PrimalIteration()
	else
		local var_19_0 = var_0_1.TimeMgr.GetInstance().AddBattleTimer("spawnBullet", -1, arg_19_0._delay, arg_19_0.timerCb, True)

		arg_19_0._timerList[var_19_0] = arg_19_0.DelayPrimalAdvance

def var_0_5._nonDelayPrimalIteration(arg_20_0):
	if arg_20_0._state != arg_20_0.STATE_ACTIVE:
		return

	arg_20_0.GenerateBullet()

	if arg_20_0._primalCounter > arg_20_0._primalMax:
		arg_20_0.SeniorIteration()
	else
		arg_20_0.PrimalIteration()