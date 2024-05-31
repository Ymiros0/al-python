ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSpawnWave = class("BattleSpawnWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleSpawnWave.__name = "BattleSpawnWave"

local var_0_1 = var_0_0.Battle.BattleSpawnWave

var_0_1.ASYNC_TIME_GAP = 0.03

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0._spawnUnitList = {}
	arg_1_0._monsterList = {}
	arg_1_0._reinforceKillCount = 0
	arg_1_0._reinforceTotalKillCount = 0
	arg_1_0._airStrikeTimerList = {}
	arg_1_0._spawnTimerList = {}
	arg_1_0._reinforceSpawnTimerList = {}

def var_0_1.SetWaveData(arg_2_0, arg_2_1):
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._sapwnData = arg_2_1.spawn or {}
	arg_2_0._airStrike = arg_2_1.airFighter or {}
	arg_2_0._reinforce = arg_2_1.reinforcement or {}
	arg_2_0._reinforceCount = #arg_2_0._reinforce
	arg_2_0._spawnCount = #arg_2_0._sapwnData
	arg_2_0._reinforceDuration = arg_2_0._reinforce.reinforceDuration or 0
	arg_2_0._reinforeceExpire = False
	arg_2_0._round = arg_2_0._param.round

def var_0_1.IsBossWave(arg_3_0):
	local var_3_0 = False
	local var_3_1 = arg_3_0._sapwnData

	for iter_3_0, iter_3_1 in ipairs(var_3_1):
		if iter_3_1.bossData:
			var_3_0 = True

	return var_3_0

def var_0_1.DoWave(arg_4_0):
	var_0_1.super.DoWave(arg_4_0)

	if arg_4_0._round:
		local var_4_0 = False
		local var_4_1 = var_0_0.Battle.BattleDataProxy.GetInstance()

		if var_4_1.GetInitData().ChallengeInfo:
			local var_4_2 = var_4_1.GetInitData().ChallengeInfo.getRound()

			if arg_4_0._round.less and var_4_2 < arg_4_0._round.less:
				var_4_0 = True

			if arg_4_0._round.more and var_4_2 > arg_4_0._round.more:
				var_4_0 = True

			if arg_4_0._round.equal and table.contains(arg_4_0._round.equal, var_4_2):
				var_4_0 = True

		if not var_4_0:
			arg_4_0.doPass()

			return

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._airStrike):
		local var_4_3 = iter_4_1.delay + iter_4_0 * var_0_1.ASYNC_TIME_GAP

		if var_4_3 <= 0:
			arg_4_0.doAirStrike(iter_4_1)
		else
			arg_4_0.airStrikeTimer(iter_4_1, var_4_3)

	local var_4_4 = 0

	for iter_4_2, iter_4_3 in ipairs(arg_4_0._sapwnData):
		if iter_4_3.bossData:
			var_4_4 = var_4_4 + 1

	local var_4_5 = 0
	local var_4_6 = 0

	for iter_4_4, iter_4_5 in ipairs(arg_4_0._sapwnData):
		if (iter_4_5.chance or 1) >= math.random():
			if iter_4_5.bossData and var_4_4 > 1:
				var_4_5 = var_4_5 + 1
				iter_4_5.bossData.bossCount = var_4_5

			local var_4_7 = iter_4_5.delay + var_4_6

			if var_4_7 <= 0:
				arg_4_0.doSpawn(iter_4_5)
			else
				arg_4_0.spawnTimer(iter_4_5, var_4_7, arg_4_0._spawnTimerList)
		else
			arg_4_0._spawnCount = arg_4_0._spawnCount - 1

		var_4_6 = var_4_6 + var_0_1.ASYNC_TIME_GAP

	if arg_4_0._reinforce:
		arg_4_0.doReinforce(var_4_6)

	if arg_4_0._spawnCount == 0 and arg_4_0._reinforceDuration == 0:
		arg_4_0.doPass()

	if arg_4_0._reinforceDuration != 0:
		arg_4_0.reinforceDurationTimer(arg_4_0._reinforceDuration)

	var_0_0.Battle.BattleState.GenerateVertifyData(1)

	local var_4_8, var_4_9 = var_0_0.Battle.BattleState.Vertify()

	if not var_4_8:
		local var_4_10 = 100 + var_4_9

		var_0_0.Battle.BattleState.GetInstance().GetCommandByName(var_0_0.Battle.BattleSingleDungeonCommand.__name).SetVertifyFail(var_4_10)

def var_0_1.AddMonster(arg_5_0, arg_5_1):
	if arg_5_1.GetWaveIndex() != arg_5_0._index:
		return

	arg_5_0._monsterList[arg_5_1.GetUniqueID()] = arg_5_1

def var_0_1.RemoveMonster(arg_6_0, arg_6_1):
	arg_6_0.onWaveUnitDie(arg_6_1)

def var_0_1.doSpawn(arg_7_0, arg_7_1):
	local var_7_0 = var_0_0.Battle.BattleConst.UnitType.ENEMY_UNIT

	if arg_7_1.bossData:
		var_7_0 = var_0_0.Battle.BattleConst.UnitType.BOSS_UNIT

	arg_7_0._spawnFunc(arg_7_1, arg_7_0._index, var_7_0)

def var_0_1.spawnTimer(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0

	local function var_8_1()
		arg_8_3[var_8_0] = None

		arg_8_0.doSpawn(arg_8_1)
		pg.TimeMgr.GetInstance().RemoveBattleTimer(var_8_0)

	var_8_0 = pg.TimeMgr.GetInstance().AddBattleTimer("", 1, arg_8_2, var_8_1, True)
	arg_8_3[var_8_0] = True

def var_0_1.doAirStrike(arg_10_0, arg_10_1):
	arg_10_0._airFunc(arg_10_1)

def var_0_1.airStrikeTimer(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0

	local function var_11_1()
		arg_11_0._airStrikeTimerList[var_11_0] = None

		arg_11_0.doAirStrike(arg_11_1)
		pg.TimeMgr.GetInstance().RemoveBattleTimer(var_11_0)

	var_11_0 = pg.TimeMgr.GetInstance().AddBattleTimer("", 1, arg_11_2, var_11_1, True)
	arg_11_0._airStrikeTimerList[var_11_0] = True

def var_0_1.doReinforce(arg_13_0, arg_13_1):
	arg_13_0._reinforceKillCount = 0

	if arg_13_0._reinforeceExpire:
		return

	arg_13_1 = arg_13_1 or 0

	for iter_13_0, iter_13_1 in ipairs(arg_13_0._reinforce):
		iter_13_1.reinforce = True

		local var_13_0 = iter_13_1.delay + arg_13_1

		if var_13_0 <= 0:
			arg_13_0.doSpawn(iter_13_1)
		else
			arg_13_0.spawnTimer(iter_13_1, var_13_0, arg_13_0._reinforceSpawnTimerList)

		arg_13_1 = arg_13_1 + var_0_1.ASYNC_TIME_GAP

def var_0_1.reinforceTimer(arg_14_0, arg_14_1):
	arg_14_0.clearReinforceTimer()

	local function var_14_0()
		arg_14_0.doReinforce()
		arg_14_0.clearReinforceTimer()

	arg_14_0._reinforceTimer = pg.TimeMgr.GetInstance().AddBattleTimer("", 1, arg_14_1, var_14_0, True)

def var_0_1.clearReinforceTimer(arg_16_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_16_0._reinforceTimer)

	arg_16_0._reinforceTimer = None

def var_0_1.reinforceDurationTimer(arg_17_0, arg_17_1):
	local function var_17_0()
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_17_0._reinforceDurationTimer)

		arg_17_0._reinforeceExpire = True
		arg_17_0._reinforceDuration = None

		arg_17_0.clearReinforceTimer()
		arg_17_0.clearTimerList(arg_17_0._reinforceSpawnTimerList)

		if arg_17_0._spawnCount == 0:
			arg_17_0.doPass()

	arg_17_0._reinforceDurationTimer = pg.TimeMgr.GetInstance().AddBattleTimer("", 1, arg_17_1, var_17_0, True)

def var_0_1.clearReinforceDurationTimer(arg_19_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_19_0._reinforceDurationTimer)

	arg_19_0._reinforceDurationTimer = None

def var_0_1.onWaveUnitDie(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_0._monsterList[arg_20_1]

	if var_20_0 == None:
		return

	local var_20_1

	if var_20_0.IsReinforcement():
		arg_20_0._reinforceKillCount = arg_20_0._reinforceKillCount + 1
		arg_20_0._reinforceTotalKillCount = arg_20_0._reinforceTotalKillCount + 1

		if arg_20_0._reinforceCount != 0 and arg_20_0._reinforceCount == arg_20_0._reinforceKillCount:
			var_20_1 = True

	local function var_20_2(arg_21_0)
		if var_20_1 and arg_21_0:
			if arg_21_0 == 0:
				arg_20_0.doReinforce()
			else
				arg_20_0.reinforceTimer(arg_21_0)

			var_20_1 = False

	local var_20_3 = 0
	local var_20_4 = 0

	for iter_20_0, iter_20_1 in pairs(arg_20_0._monsterList):
		if iter_20_1.IsAlive() == False:
			if not iter_20_1.IsReinforcement():
				var_20_3 = var_20_3 + 1
		else
			var_20_4 = var_20_4 + 1

			var_20_2(iter_20_1.GetReinforceCastTime())

	if arg_20_0._reinforceDuration != 0 and not arg_20_0._reinforeceExpire:
		var_20_2(0)

	if var_20_4 == 0 and var_20_3 >= arg_20_0._spawnCount and arg_20_0._reinforceTotalKillCount >= arg_20_0._reinforceCount and (arg_20_0._reinforceDuration == 0 or arg_20_0._reinforeceExpire):
		arg_20_0.doPass()

def var_0_1.doPass(arg_22_0):
	arg_22_0.clearTimerList(arg_22_0._spawnTimerList)
	arg_22_0.clearTimerList(arg_22_0._reinforceSpawnTimerList)
	arg_22_0.clearReinforceTimer()
	arg_22_0.clearReinforceDurationTimer()
	var_0_0.Battle.BattleDataProxy.GetInstance().KillWaveSummonMonster(arg_22_0._index)
	var_0_1.super.doPass(arg_22_0)

def var_0_1.clearTimerList(arg_23_0):
	for iter_23_0, iter_23_1 in pairs(arg_23_0):
		pg.TimeMgr.GetInstance().RemoveBattleTimer(iter_23_0)

def var_0_1.Dispose(arg_24_0):
	arg_24_0.clearTimerList(arg_24_0._airStrikeTimerList)

	arg_24_0._airStrikeTimerList = None

	arg_24_0.clearTimerList(arg_24_0._spawnTimerList)

	arg_24_0._spawnTimerList = None

	arg_24_0.clearTimerList(arg_24_0._reinforceSpawnTimerList)

	arg_24_0._reinforceSpawnTimerList = None

	arg_24_0.clearReinforceTimer()
	arg_24_0.clearReinforceDurationTimer()
	var_0_1.super.Dispose(arg_24_0)
