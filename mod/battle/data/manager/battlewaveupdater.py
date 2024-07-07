from packages.luatable import ipairs

from mod.battle.data import BattleConst

WaveTriggerType = BattleConst.WaveTriggerType
class BattleWaveUpdater:
	__name = "BattleWaveUpdater"
	PREWAVES_CONDITION_AND = 0
	PREWAVES_CONDITION_OR = 1

	def Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
		EventListener.AttachEventListener(arg_1_0)

		arg_1_0._spawnFunc = arg_1_1
		arg_1_0._airFighterFunc = arg_1_2
		arg_1_0._clearFunc = arg_1_3
		arg_1_0._spawnAreaFunc = arg_1_4

		arg_1_0.Init()

	def Init(arg_2_0):
		arg_2_0._monsterList = {}
		arg_2_0._spawnList = {}
		arg_2_0._airFighter = {}
		arg_2_0._waveInfos = {}
		arg_2_0._timerList = {}
		arg_2_0._waveUnitAliveList = {}
		arg_2_0._keyList = {}
		arg_2_0._waveInfoList = {}

	def SetWavesData(arg_3_0, arg_3_1):
		arg_3_0._waveTmpData = arg_3_1

		for iter_3_0, iter_3_1 in ipairs(arg_3_1.waves):
			var_3_0 = iter_3_1.triggerType
			var_3_1

			if var_3_0 == WaveTriggerType.NORMAL:
				var_3_1 = BattleSpawnWave.New()

				var_3_1.SetCallback(arg_3_0._spawnFunc, arg_3_0._airFighterFunc)
			elif var_3_0 == WaveTriggerType.TIMER:
				var_3_1 = BattleDelayWave.New()
			elif var_3_0 == WaveTriggerType.RANGE:
				var_3_1 = BattleRangeWave.New()

				var_3_1.SetCallback(arg_3_0._spawnAreaFunc)
			elif var_3_0 == WaveTriggerType.STORY:
				var_3_1 = BattleStoryWave.New()
			elif var_3_0 == WaveTriggerType.AID:
				var_3_1 = BattleAidWave.New()
			elif var_3_0 == WaveTriggerType.BGM:
				var_3_1 = BattleSwitchBGMWave.New()
			elif var_3_0 == WaveTriggerType.GUIDE:
				var_3_1 = BattleGuideWave.New()
			elif var_3_0 == WaveTriggerType.CAMERA:
				var_3_1 = BattleCameraWave.New()
			elif var_3_0 == WaveTriggerType.CLEAR:
				var_3_1 = BattleClearWave.New()
			elif var_3_0 == WaveTriggerType.JAMMING:
				var_3_1 = BattleJammingWave.New()
			elif var_3_0 == WaveTriggerType.ENVIRONMENT:
				var_3_1 = BattleEnvironmentWave.New()
			elif var_3_0 == WaveTriggerType.LABEL:
				var_3_1 = BattleLabelWave.New()
			elif var_3_0 == WaveTriggerType.CARD_PUZZLE:
				var_3_1 = BattleCardPuzzleWave.New()

			var_3_1.SetWaveData(iter_3_1)
			var_3_1.RegisterEventListener(arg_3_0, BattleEvent.WAVE_FINISH, arg_3_0.onWaveFinish)

			arg_3_0._waveInfoList[var_3_1.GetIndex()] = var_3_1

			if var_3_1.IsKeyWave():
				arg_3_0._keyList[#arg_3_0._keyList + 1] = var_3_1

		for iter_3_2, iter_3_3 in pairs(arg_3_0._waveInfoList):
			for iter_3_4, iter_3_5 in ipairs(iter_3_3.GetPreWaveIDs()):
				var_3_2 = arg_3_0._waveInfoList[iter_3_5]

				if var_3_2:
					iter_3_3.AppendPreWave(var_3_2)
					var_3_2.AppendPostWave(iter_3_3)

			for iter_3_6, iter_3_7 in pairs(iter_3_3.GetBranchWaveIDs()):
				var_3_3 = arg_3_0._waveInfoList[iter_3_6]

				if var_3_3:
					iter_3_3.AppendBranchWave(var_3_3)

	def Start(arg_4_0):
		arg_4_0._active = True

		for iter_4_0, iter_4_1 in pairs(arg_4_0._waveInfoList):
			if iter_4_1.IsReady():
				iter_4_1.DoBranch()

	def AddMonster(arg_5_0, arg_5_1):
		for iter_5_0, iter_5_1 in pairs(arg_5_0._waveInfoList):
			iter_5_1.AddMonster(arg_5_1)

	def RemoveMonster(arg_6_0, arg_6_1):
		for iter_6_0, iter_6_1 in pairs(arg_6_0._waveInfoList):
			iter_6_1.RemoveMonster(arg_6_1)

	def onWaveFinish(arg_7_0, arg_7_1):
		if not arg_7_0._active:
			return

		if arg_7_0.CheckAllKeyWave():
			arg_7_0._active = False

			arg_7_0._clearFunc()

		var_7_0 = arg_7_1.Dispatcher.GetPostWaves()

		for iter_7_0, iter_7_1 in ipairs(var_7_0):
			if iter_7_1.IsReady() and iter_7_1.GetState() == iter_7_1.STATE_DEACTIVE:
				iter_7_1.DoBranch()

	def GetAllBossWave(arg_8_0):
		var_8_0 = {}

		for iter_8_0, iter_8_1 in pairs(arg_8_0._waveInfoList):
			if iter_8_1.GetType() == WaveTriggerType.NORMAL and iter_8_1.IsBossWave():
				table.insert(var_8_0, iter_8_1)

		return var_8_0

	def CheckAllKeyWave(arg_9_0):
		for iter_9_0, iter_9_1 in ipairs(arg_9_0._keyList):
			if not iter_9_1.IsFinish():
				return False

		return True

	def Clear(arg_10_0):
		for iter_10_0, iter_10_1 in pairs(arg_10_0._timerList):
			arg_10_0.RemoveTimer(iter_10_0)

		for iter_10_2, iter_10_3 in pairs(arg_10_0._waveInfoList):
			iter_10_3.UnregisterEventListener(arg_10_0, BattleEvent.WAVE_FINISH)
			iter_10_3.Dispose()

		arg_10_0._waveInfoList = None
		arg_10_0._keyList = None

		arg_10_0.Init()
		EventListener.DetachEventListener(arg_10_0)

	def GetUnfinishedWaveCount(arg_11_0):
		var_11_0 = 0

		for iter_11_0, iter_11_1 in pairs(arg_11_0._waveInfoList):
			if not iter_11_1.IsFinish():
				var_11_0 = var_11_0 + 1

		return var_11_0
