ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.WaveTriggerType
local var_0_2 = class("BattleWaveUpdater")

var_0_0.Battle.BattleWaveUpdater = var_0_2
var_0_2.__name = "BattleWaveUpdater"
var_0_2.PREWAVES_CONDITION_AND = 0
var_0_2.PREWAVES_CONDITION_OR = 1

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._spawnFunc = arg_1_1
	arg_1_0._airFighterFunc = arg_1_2
	arg_1_0._clearFunc = arg_1_3
	arg_1_0._spawnAreaFunc = arg_1_4

	arg_1_0.Init()

def var_0_2.Init(arg_2_0):
	arg_2_0._monsterList = {}
	arg_2_0._spawnList = {}
	arg_2_0._airFighter = {}
	arg_2_0._waveInfos = {}
	arg_2_0._timerList = {}
	arg_2_0._waveUnitAliveList = {}
	arg_2_0._keyList = {}
	arg_2_0._waveInfoList = {}

def var_0_2.SetWavesData(arg_3_0, arg_3_1):
	arg_3_0._waveTmpData = arg_3_1

	for iter_3_0, iter_3_1 in ipairs(arg_3_1.waves):
		local var_3_0 = iter_3_1.triggerType
		local var_3_1

		if var_3_0 == var_0_1.NORMAL:
			var_3_1 = var_0_0.Battle.BattleSpawnWave.New()

			var_3_1.SetCallback(arg_3_0._spawnFunc, arg_3_0._airFighterFunc)
		elif var_3_0 == var_0_1.TIMER:
			var_3_1 = var_0_0.Battle.BattleDelayWave.New()
		elif var_3_0 == var_0_1.RANGE:
			var_3_1 = var_0_0.Battle.BattleRangeWave.New()

			var_3_1.SetCallback(arg_3_0._spawnAreaFunc)
		elif var_3_0 == var_0_1.STORY:
			var_3_1 = var_0_0.Battle.BattleStoryWave.New()
		elif var_3_0 == var_0_1.AID:
			var_3_1 = var_0_0.Battle.BattleAidWave.New()
		elif var_3_0 == var_0_1.BGM:
			var_3_1 = var_0_0.Battle.BattleSwitchBGMWave.New()
		elif var_3_0 == var_0_1.GUIDE:
			var_3_1 = var_0_0.Battle.BattleGuideWave.New()
		elif var_3_0 == var_0_1.CAMERA:
			var_3_1 = var_0_0.Battle.BattleCameraWave.New()
		elif var_3_0 == var_0_1.CLEAR:
			var_3_1 = var_0_0.Battle.BattleClearWave.New()
		elif var_3_0 == var_0_1.JAMMING:
			var_3_1 = var_0_0.Battle.BattleJammingWave.New()
		elif var_3_0 == var_0_1.ENVIRONMENT:
			var_3_1 = var_0_0.Battle.BattleEnvironmentWave.New()
		elif var_3_0 == var_0_1.LABEL:
			var_3_1 = var_0_0.Battle.BattleLabelWave.New()
		elif var_3_0 == var_0_1.CARD_PUZZLE:
			var_3_1 = var_0_0.Battle.BattleCardPuzzleWave.New()

		var_3_1.SetWaveData(iter_3_1)
		var_3_1.RegisterEventListener(arg_3_0, var_0_0.Battle.BattleEvent.WAVE_FINISH, arg_3_0.onWaveFinish)

		arg_3_0._waveInfoList[var_3_1.GetIndex()] = var_3_1

		if var_3_1.IsKeyWave():
			arg_3_0._keyList[#arg_3_0._keyList + 1] = var_3_1

	for iter_3_2, iter_3_3 in pairs(arg_3_0._waveInfoList):
		for iter_3_4, iter_3_5 in ipairs(iter_3_3.GetPreWaveIDs()):
			local var_3_2 = arg_3_0._waveInfoList[iter_3_5]

			if var_3_2:
				iter_3_3.AppendPreWave(var_3_2)
				var_3_2.AppendPostWave(iter_3_3)

		for iter_3_6, iter_3_7 in pairs(iter_3_3.GetBranchWaveIDs()):
			local var_3_3 = arg_3_0._waveInfoList[iter_3_6]

			if var_3_3:
				iter_3_3.AppendBranchWave(var_3_3)

def var_0_2.Start(arg_4_0):
	arg_4_0._active = True

	for iter_4_0, iter_4_1 in pairs(arg_4_0._waveInfoList):
		if iter_4_1.IsReady():
			iter_4_1.DoBranch()

def var_0_2.AddMonster(arg_5_0, arg_5_1):
	for iter_5_0, iter_5_1 in pairs(arg_5_0._waveInfoList):
		iter_5_1.AddMonster(arg_5_1)

def var_0_2.RemoveMonster(arg_6_0, arg_6_1):
	for iter_6_0, iter_6_1 in pairs(arg_6_0._waveInfoList):
		iter_6_1.RemoveMonster(arg_6_1)

def var_0_2.onWaveFinish(arg_7_0, arg_7_1):
	if not arg_7_0._active:
		return

	if arg_7_0.CheckAllKeyWave():
		arg_7_0._active = False

		arg_7_0._clearFunc()

	local var_7_0 = arg_7_1.Dispatcher.GetPostWaves()

	for iter_7_0, iter_7_1 in ipairs(var_7_0):
		if iter_7_1.IsReady() and iter_7_1.GetState() == iter_7_1.STATE_DEACTIVE:
			iter_7_1.DoBranch()

def var_0_2.GetAllBossWave(arg_8_0):
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in pairs(arg_8_0._waveInfoList):
		if iter_8_1.GetType() == var_0_1.NORMAL and iter_8_1.IsBossWave():
			table.insert(var_8_0, iter_8_1)

	return var_8_0

def var_0_2.CheckAllKeyWave(arg_9_0):
	for iter_9_0, iter_9_1 in ipairs(arg_9_0._keyList):
		if not iter_9_1.IsFinish():
			return False

	return True

def var_0_2.Clear(arg_10_0):
	for iter_10_0, iter_10_1 in pairs(arg_10_0._timerList):
		arg_10_0.RemoveTimer(iter_10_0)

	for iter_10_2, iter_10_3 in pairs(arg_10_0._waveInfoList):
		iter_10_3.UnregisterEventListener(arg_10_0, var_0_0.Battle.BattleEvent.WAVE_FINISH)
		iter_10_3.Dispose()

	arg_10_0._waveInfoList = None
	arg_10_0._keyList = None

	arg_10_0.Init()
	var_0_0.EventListener.DetachEventListener(arg_10_0)

def var_0_2.GetUnfinishedWaveCount(arg_11_0):
	local var_11_0 = 0

	for iter_11_0, iter_11_1 in pairs(arg_11_0._waveInfoList):
		if not iter_11_1.IsFinish():
			var_11_0 = var_11_0 + 1

	return var_11_0
