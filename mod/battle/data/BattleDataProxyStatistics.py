from luatable import pairs, table, ipairs
from alsupport import Mathf, math

import ys
import BattleDataProxy
import BattleConst
import BattleConfig
import BattleDataFunction
from .. import BattleEvent
from model.const import TeamType, ShipType

def StatisticsInit(arg_1_0, arg_1_1):
	arg_1_0._statistics = table()
	arg_1_0._statistics._battleScore = BattleConst.BattleScore.D
	arg_1_0._statistics.kill_id_list = table()
	arg_1_0._statistics._totalTime = 0
	arg_1_0._statistics._deadCount = 0
	arg_1_0._statistics._boss_destruct = 0
	arg_1_0._statistics._botPercentage = 0
	arg_1_0._statistics._maxBossHP = 0
	arg_1_0._statistics._enemyInfoList = table()

	for iter_1_0, iter_1_1 in ipairs(arg_1_1):
		var_1_0 = table(
			id = iter_1_1.GetAttrByName("id")
		)

		var_1_0.damage = 0
		var_1_0.output = 0
		var_1_0.kill_count = 0
		var_1_0.bp = 0
		var_1_0.max_hp = iter_1_1.GetAttrByName("maxHP")
		var_1_0.maxDamageOnce = 0
		var_1_0.gearScore = iter_1_1.GetGearScore()
		arg_1_0._statistics[var_1_0.id] = var_1_0
BattleDataProxy.StatisticsInit = StatisticsInit

def InitAidUnitStatistics(arg_2_0, arg_2_1):
	var_2_0 = table(
		id = arg_2_1.GetAttrByName("id")
	)

	var_2_0.damage = 0
	var_2_0.output = 0
	var_2_0.kill_count = 0
	var_2_0.bp = 0
	var_2_0.max_hp = arg_2_1.GetAttrByName("maxHP")
	var_2_0.maxDamageOnce = 0
	var_2_0.gearScore = arg_2_1.GetGearScore()
	arg_2_0._statistics[var_2_0.id] = var_2_0
	arg_2_0._statistics.submarineAid = True
BattleDataProxy.InitAidUnitStatistics = InitAidUnitStatistics

def InitSpecificEnemyStatistics(arg_3_0, arg_3_1):
	var_3_0 = table(
		id = arg_3_1.GetAttrByName("id")
	)

	var_3_0.damage = 0
	var_3_0.output = 0
	var_3_0.kill_count = 0
	var_3_0.bp = 0
	var_3_0.max_hp = arg_3_1.GetAttrByName("maxHP")
	var_3_0.init_hp = arg_3_1.GetCurrentHP()
	var_3_0.maxDamageOnce = 0
	var_3_0.gearScore = arg_3_1.GetGearScore()
	arg_3_0._statistics[var_3_0.id] = var_3_0
BattleDataProxy.InitSpecificEnemyStatistics = InitSpecificEnemyStatistics

def RivalInit(arg_4_0, arg_4_1):
	arg_4_0._statistics._rivalInfo = table()

	for iter_4_0, iter_4_1 in ipairs(arg_4_1):
		var_4_0 = iter_4_1.GetAttrByName("id")

		arg_4_0._statistics._rivalInfo[var_4_0] = table()
		arg_4_0._statistics._rivalInfo[var_4_0].id = var_4_0
BattleDataProxy.RivalInit = RivalInit

def DodgemCountInit(arg_5_0):
	arg_5_0._dodgemStatistics = table()
	arg_5_0._dodgemStatistics.kill = 0
	arg_5_0._dodgemStatistics.combo = 0
	arg_5_0._dodgemStatistics.miss = 0
	arg_5_0._dodgemStatistics.fail = 0
	arg_5_0._dodgemStatistics.score = 0
	arg_5_0._dodgemStatistics.maxCombo = 0
BattleDataProxy.DodgemCountInit = DodgemCountInit

def SubmarineRunInit(arg_6_0):
	arg_6_0._subRunStatistics = table()
	arg_6_0._subRunStatistics.score = 0
BattleDataProxy.SubmarineRunInit = SubmarineRunInit

def SetFlagShipID(arg_7_0, arg_7_1):
	if arg_7_1:
		arg_7_0._statistics._flagShipID = arg_7_1.GetAttrByName("id")
BattleDataProxy.SetFlagShipID = SetFlagShipID

def DamageStatistics(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	if arg_8_0._statistics[arg_8_1]:
		arg_8_0._statistics[arg_8_1].output = arg_8_0._statistics[arg_8_1].output + arg_8_3
		arg_8_0._statistics[arg_8_1].maxDamageOnce = max(arg_8_0._statistics[arg_8_1].maxDamageOnce, arg_8_3)

	if arg_8_0._statistics[arg_8_2]:
		arg_8_0._statistics[arg_8_2].damage = arg_8_0._statistics[arg_8_2].damage + arg_8_3
BattleDataProxy.DamageStatistics = DamageStatistics

def KillCountStatistics(arg_9_0, arg_9_1, arg_9_2):
	if arg_9_0._statistics[arg_9_1]:
		arg_9_0._statistics[arg_9_1].kill_count = arg_9_0._statistics[arg_9_1].kill_count + 1
BattleDataProxy.KillCountStatistics = KillCountStatistics

def HPRatioStatistics(arg_10_0):
	for iter_10_0, iter_10_1 in pairs(arg_10_0._fleetList):
		iter_10_1.UndoFusion()

	var_10_0 = arg_10_0._fleetList[1].GetUnitList()

	for iter_10_2, iter_10_3 in ipairs(var_10_0):
		arg_10_0._statistics[iter_10_3.GetAttrByName("id")].bp = math.ceil(iter_10_3.GetHPRate() * 10000)
BattleDataProxy.HPRatioStatistics = HPRatioStatistics

def BotPercentage(arg_11_0, arg_11_1):
	var_11_0 = arg_11_0._currentStageData.timeCount - arg_11_0._countDown

	arg_11_0._statistics._botPercentage = Mathf.Clamp(math.floor(arg_11_1 / var_11_0 * 100), 0, 100)
BattleDataProxy.BotPercentage = BotPercentage

def CalcBattleScoreWhenDead(arg_12_0, arg_12_1):
	var_12_0 = arg_12_1.GetIFF()

	if var_12_0 == BattleConfig.FRIENDLY_CODE:
		if not table.contains(TeamType.SubShipType, arg_12_1.GetTemplate().type):
			arg_12_0.DelScoreWhenPlayerDead(arg_12_1)
	elif var_12_0 == BattleConfig.FOE_CODE:
		arg_12_0.AddScoreWhenEnemyDead(arg_12_1)
BattleDataProxy.CalcBattleScoreWhenDead = CalcBattleScoreWhenDead

def AddScoreWhenBossDestruct(arg_13_0):
	arg_13_0._statistics._boss_destruct = arg_13_0._statistics._boss_destruct + 1
BattleDataProxy.AddScoreWhenBossDestruct = AddScoreWhenBossDestruct

def AddScoreWhenEnemyDead(arg_14_0, arg_14_1):
	if arg_14_1.GetDeathReason() == BattleConst.UnitDeathReason.KILLED:
		arg_14_0._statistics.kill_id_list.append(arg_14_1.GetTemplateID())
BattleDataProxy.AddScoreWhenEnemyDead = AddScoreWhenEnemyDead

def DelScoreWhenPlayerDead(arg_15_0, arg_15_1):
	arg_15_0._statistics._deadCount = arg_15_0._statistics._deadCount + 1
BattleDataProxy.DelScoreWhenPlayerDead = DelScoreWhenPlayerDead

def CalcBPWhenPlayerLeave(arg_16_0, arg_16_1):
	arg_16_0._statistics[arg_16_1.GetAttrByName("id")].bp = math.ceil(arg_16_1.GetHPRate() * 10000)
BattleDataProxy.CalcBPWhenPlayerLeave = CalcBPWhenPlayerLeave

def isTimeOut(arg_17_0):
	return arg_17_0._currentStageData.timeCount - arg_17_0._countDown >= 180
BattleDataProxy.isTimeOut = isTimeOut

def CalcCardPuzzleScoreAtEnd(arg_18_0, arg_18_1):
	arg_18_0._statistics._deadUnit = True
	arg_18_0._statistics._badTime = True

	var_18_0 = arg_18_1.GetCardPuzzleComponent().GetCurrentCommonHP()

	arg_18_0._statistics._battleScore = var_18_0 > 0 and BattleConst.BattleScore.S or BattleConst.BattleScore.D
	arg_18_0._statistics._cardPuzzleStatistics = table()
	arg_18_0._statistics._cardPuzzleStatistics.common_hp_rest = var_18_0

	var_18_1 = arg_18_0._currentStageData.timeCount - arg_18_0._countDown

	arg_18_0._statistics._totalTime = var_18_1

	arg_18_0.AirFightInit()
BattleDataProxy.CalcCardPuzzleScoreAtEnd = CalcCardPuzzleScoreAtEnd

def CalcSingleDungeonScoreAtEnd(arg_19_0, arg_19_1):
	arg_19_0._statistics._deadUnit = True
	arg_19_0._statistics._badTime = True

	var_19_0 = arg_19_0._currentStageData.timeCount - arg_19_0._countDown

	arg_19_0._statistics._totalTime = var_19_0

	var_19_1 = arg_19_0._expeditionTmp.limit_type
	var_19_2 = arg_19_0._expeditionTmp.sink_limit
	var_19_3 = arg_19_0._expeditionTmp.time_limit

	if var_19_2 > arg_19_0._statistics._deadCount:
		arg_19_0._statistics._deadUnit = False

	var_19_4 = arg_19_1.GetFlagShip()
	var_19_5 = arg_19_1.GetScoutList()

	if var_19_1 == 2:
		if not var_19_4.IsAlive() or len(var_19_5) <= 0:
			arg_19_0._statistics._battleScore = BattleConst.BattleScore.D
			arg_19_0._statistics._boss_destruct = 1
		else:
			arg_19_0._statistics._battleScore = BattleConst.BattleScore.S
	elif arg_19_0._countDown <= 0:
		arg_19_0._statistics._battleScore = BattleConst.BattleScore.C
		arg_19_0._statistics._boss_destruct = 1
	elif var_19_4 and not var_19_4.IsAlive():
		arg_19_0._statistics._battleScore = BattleConst.BattleScore.D
		arg_19_0._statistics._boss_destruct = 1
		arg_19_0._statistics._scoreMark = BattleConst.DEAD_FLAG
	elif len(var_19_5) <= 0:
		arg_19_0._statistics._battleScore = BattleConst.BattleScore.D
		arg_19_0._statistics._boss_destruct = 1
	else:
		var_19_6 = 0

		if arg_19_0._statistics._deadUnit:
			var_19_6 = var_19_6 + 1

		if var_19_3 < var_19_0:
			var_19_6 = var_19_6 + 1
		else:
			arg_19_0._statistics._badTime = False

		if arg_19_0._statistics._boss_destruct > 0:
			var_19_6 = var_19_6 + 1

		if var_19_6 >= 2:
			arg_19_0._statistics._battleScore = BattleConst.BattleScore.B
		elif var_19_6 == 1:
			arg_19_0._statistics._battleScore = BattleConst.BattleScore.A
		elif var_19_6 == 0:
			arg_19_0._statistics._battleScore = BattleConst.BattleScore.S

	arg_19_0._statistics._timeout = arg_19_0.isTimeOut()

	if arg_19_0._battleInitData.CMDArgs:
		arg_19_0.CalcSpecificEnemyInfo(table(
			arg_19_0._battleInitData.CMDArgs
		))
BattleDataProxy.CalcSingleDungeonScoreAtEnd = CalcSingleDungeonScoreAtEnd

def CalcMaxRestHPRateBossRate(arg_20_0, arg_20_1):
	arg_20_0._statistics._maxBossHP = arg_20_1
BattleDataProxy.CalcMaxRestHPRateBossRate = CalcMaxRestHPRateBossRate

def CalcDuelScoreAtTimesUp(arg_21_0, arg_21_1, arg_21_2, arg_21_3, arg_21_4):
	arg_21_0._statistics._deadUnit = True
	arg_21_0._statistics._badTime = True
	arg_21_0._statistics._timeout = False

	var_21_0 = arg_21_0._currentStageData.timeCount - arg_21_0._countDown

	arg_21_0._statistics._totalTime = var_21_0

	if arg_21_0._expeditionTmp.sink_limit > arg_21_0._statistics._deadCount:
		arg_21_0._statistics._deadUnit = False

	if arg_21_2 < arg_21_1:
		arg_21_0._statistics._battleScore = BattleConst.BattleScore.S
	elif arg_21_1 < arg_21_2:
		arg_21_0._statistics._battleScore = BattleConst.BattleScore.D
	elif arg_21_4 <= arg_21_3:
		arg_21_0._statistics._battleScore = BattleConst.BattleScore.S
	elif arg_21_3 < arg_21_4:
		arg_21_0._statistics._battleScore = BattleConst.BattleScore.D
BattleDataProxy.CalcDuelScoreAtTimesUp = CalcDuelScoreAtTimesUp

def CalcDuelScoreAtEnd(arg_22_0, arg_22_1, arg_22_2):
	arg_22_0._statistics._deadUnit = True
	arg_22_0._statistics._badTime = True

	var_22_0 = arg_22_0._currentStageData.timeCount - arg_22_0._countDown

	arg_22_0._statistics._totalTime = var_22_0

	var_22_1 = len(arg_22_1.GetUnitList())
	var_22_2 = len(arg_22_2.GetUnitList())
	var_22_3 = arg_22_0._expeditionTmp.sink_limit
	var_22_4 = arg_22_0._expeditionTmp.time_limit

	if var_22_3 > arg_22_0._statistics._deadCount:
		arg_22_0._statistics._deadUnit = False

	if var_22_1 == 0:
		arg_22_0._statistics._battleScore = BattleConst.BattleScore.D
	elif var_22_2 == 0:
		arg_22_0._statistics._battleScore = BattleConst.BattleScore.S

	arg_22_0._statistics._timeout = arg_22_0.isTimeOut()
BattleDataProxy.CalcDuelScoreAtEnd = CalcDuelScoreAtEnd

def CalcSimulationScoreAtEnd(arg_23_0, arg_23_1, arg_23_2):
	arg_23_0._statistics._deadUnit = True
	arg_23_0._statistics._badTime = True

	var_23_0 = arg_23_0._currentStageData.timeCount - arg_23_0._countDown

	arg_23_0._statistics._totalTime = var_23_0

	var_23_1 = len(arg_23_1.GetUnitList())
	var_23_2 = arg_23_1.GetMaxCount()
	var_23_3 = len(arg_23_1.GetScoutList())
	var_23_4 = len(arg_23_2.GetUnitList())
	var_23_5 = arg_23_0._expeditionTmp.sink_limit
	var_23_6 = arg_23_0._expeditionTmp.time_limit

	if arg_23_0._statistics._deadCount <= 0:
		arg_23_0._statistics._deadUnit = False

	if not arg_23_1.GetFlagShip().IsAlive():
		arg_23_0._statistics._battleScore = BattleConst.BattleScore.D
		arg_23_0._statistics._scoreMark = BattleConst.DEAD_FLAG
	elif var_23_3 == 0:
		arg_23_0._statistics._battleScore = BattleConst.BattleScore.D
	elif var_23_4 == 0:
		arg_23_0._statistics._battleScore = BattleConst.BattleScore.S

	arg_23_0._statistics._timeout = arg_23_0.isTimeOut()

	arg_23_0.overwriteRivalStatistics(arg_23_2)
BattleDataProxy.CalcSimulationScoreAtEnd = CalcSimulationScoreAtEnd

def CalcSimulationScoreAtTimesUp(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4, arg_24_5):
	arg_24_0._statistics._deadUnit = True
	arg_24_0._statistics._badTime = True
	arg_24_0._statistics._timeout = False

	var_24_0 = arg_24_0._currentStageData.timeCount - arg_24_0._countDown

	arg_24_0._statistics._totalTime = var_24_0

	if arg_24_0._statistics._deadCount <= 0:
		arg_24_0._statistics._deadUnit = False

	arg_24_0._statistics._battleScore = BattleConst.BattleScore.D

	arg_24_0.overwriteRivalStatistics(arg_24_5)
BattleDataProxy.CalcSimulationScoreAtTimesUp = CalcSimulationScoreAtTimesUp

def overwriteRivalStatistics(arg_25_0, arg_25_1):
	for iter_25_0, iter_25_1 in pairs(arg_25_0._statistics._rivalInfo):
		var_25_0 = False

		for iter_25_2, iter_25_3 in ipairs(arg_25_1.GetUnitList()):
			if iter_25_3.GetAttrByName("id") == iter_25_0:
				iter_25_1.bp = math.ceil(iter_25_3.GetHPRate() * 10000)
				var_25_0 = True

				break

		if not var_25_0:
			iter_25_1.bp = 0
BattleDataProxy.overwriteRivalStatistics = overwriteRivalStatistics

def CalcChallengeScore(arg_26_0, arg_26_1):
	if arg_26_1:
		arg_26_0._statistics._battleScore = BattleConst.BattleScore.S
	else:
		arg_26_0._statistics._battleScore = BattleConst.BattleScore.D

	arg_26_0._statistics._totalTime = arg_26_0._totalTime
BattleDataProxy.CalcChallengeScore = CalcChallengeScore

def CalcDodgemCount(arg_27_0, arg_27_1):
	var_27_0 = arg_27_1.GetDeathReason()
	var_27_1 = arg_27_1.GetTemplate().type

	if var_27_0 == ys.Battle.BattleConst.UnitDeathReason.CRUSH:
		arg_27_0._dodgemStatistics.kill = arg_27_0._dodgemStatistics.kill + 1

		if var_27_1 == ShipType.JinBi:
			arg_27_0._dodgemStatistics.combo = arg_27_0._dodgemStatistics.combo + 1
			arg_27_0._dodgemStatistics.maxCombo = math.max(arg_27_0._dodgemStatistics.maxCombo, arg_27_0._dodgemStatistics.combo)

			var_27_2 = arg_27_0._dodgemStatistics.score + arg_27_0.GetScorePoint()

			arg_27_0._dodgemStatistics.score = var_27_2

			arg_27_0.DispatchEvent(ys.Event.New(BattleEvent.UPDATE_DODGEM_SCORE, table(
				totalScore = var_27_2
			)))
		elif var_27_1 == ShipType.ZiBao:
			arg_27_0._dodgemStatistics.fail = arg_27_0._dodgemStatistics.fail + 1
			arg_27_0._dodgemStatistics.combo = 0

		arg_27_0.DispatchEvent(ys.Event.New(BattleEvent.UPDATE_DODGEM_COMBO, table(
			combo = arg_27_0._dodgemStatistics.combo
		)))
	elif var_27_1 == ShipType.JinBi:
		arg_27_0._dodgemStatistics.miss = arg_27_0._dodgemStatistics.miss + 1
BattleDataProxy.CalcDodgemCount = CalcDodgemCount

def GetScorePoint(arg_28_0):
	var_28_0

	if arg_28_0._dodgemStatistics.combo == 1:
		var_28_0 = 1
	elif arg_28_0._dodgemStatistics.combo == 2:
		var_28_0 = 2
	elif arg_28_0._dodgemStatistics.combo > 2:
		var_28_0 = 3

	return var_28_0
BattleDataProxy.GetScorePoint = GetScorePoint

def CalcDodgemScore(arg_29_0):
	if arg_29_0._dodgemStatistics.score >= BattleConfig.BATTLE_DODGEM_PASS_SCORE:
		arg_29_0._statistics._battleScore = BattleConst.BattleScore.S
	else:
		arg_29_0._statistics._battleScore = BattleConst.BattleScore.B

	arg_29_0._statistics.dodgemResult = arg_29_0._dodgemStatistics
BattleDataProxy.CalcDodgemScore = CalcDodgemScore

def CalcActBossDamageInfo(arg_30_0, arg_30_1):
	var_30_0 = BattleDataFunction.GetSpecificEnemyList(arg_30_1, arg_30_0._expeditionID)

	arg_30_0.CalcSpecificEnemyInfo(var_30_0)
BattleDataProxy.CalcActBossDamageInfo = CalcActBossDamageInfo

def CalcWorldBossDamageInfo(arg_31_0, arg_31_1, arg_31_2, arg_31_3):
	var_31_0 = BattleDataFunction.GetSpecificWorldJointEnemyList(arg_31_1, arg_31_2, arg_31_3)

	arg_31_0.CalcSpecificEnemyInfo(var_31_0)
BattleDataProxy.CalcWorldBossDamageInfo = CalcWorldBossDamageInfo

def CalcGuildBossEnemyInfo(arg_32_0, arg_32_1):
	var_32_0 = BattleDataFunction.GetSpecificGuildBossEnemyList(arg_32_1, arg_32_0._expeditionID)

	arg_32_0.CalcSpecificEnemyInfo(var_32_0)
BattleDataProxy.CalcGuildBossEnemyInfo = CalcGuildBossEnemyInfo

def CalcSpecificEnemyInfo(arg_33_0, arg_33_1):
	arg_33_0._statistics.specificDamage = 0

	for iter_33_0, iter_33_1 in ipairs(arg_33_1):
		if arg_33_0._statistics["enemy_" + iter_33_1]:
			var_33_0 = arg_33_0._statistics["enemy_" + iter_33_1].damage

			if table.contains(arg_33_0._statistics.kill_id_list, iter_33_1):
				var_33_0 = arg_33_0._statistics["enemy_" + iter_33_1].init_hp

			arg_33_0._statistics.specificDamage = arg_33_0._statistics.specificDamage + var_33_0

			var_33_1 = table(
				id = iter_33_1,
				damage = var_33_0,
				totalHp = arg_33_0._statistics["enemy_" + iter_33_1].max_hp
			)

			table.insert(arg_33_0._statistics._enemyInfoList, var_33_1)
BattleDataProxy.CalcSpecificEnemyInfo = CalcSpecificEnemyInfo

def CalcKillingSupplyShip(arg_34_0):
	arg_34_0._subRunStatistics.score = arg_34_0._subRunStatistics.score + 1
BattleDataProxy.CalcKillingSupplyShip = CalcKillingSupplyShip

def CalcSubRunTimeUp(arg_35_0):
	arg_35_0._statistics._battleScore = BattleConst.BattleScore.B
	arg_35_0._statistics.subRunResult = arg_35_0._subRunStatistics
BattleDataProxy.CalcSubRunTimeUp = CalcSubRunTimeUp

def CalcSubRunScore(arg_36_0):
	arg_36_0._statistics._battleScore = BattleConst.BattleScore.S
	arg_36_0._statistics.subRunResult = arg_36_0._subRunStatistics
BattleDataProxy.CalcSubRunScore = CalcSubRunScore

def CalcSubRunDead(arg_37_0):
	arg_37_0._statistics._battleScore = BattleConst.BattleScore.D
	arg_37_0._statistics.subRunResult = arg_37_0._subRunStatistics
BattleDataProxy.CalcSubRunDead = CalcSubRunDead

def CalcKillingSupplyShip(arg_38_0):
	arg_38_0._subRunStatistics.score = arg_38_0._subRunStatistics.score + 1
BattleDataProxy.CalcKillingSupplyShip = CalcKillingSupplyShip

def CalcSubRountineTimeUp(arg_39_0):
	arg_39_0._statistics._badTime = True

	arg_39_0.CalcSubRoutineScore()

	arg_39_0._statistics._battleScore = BattleConst.BattleScore.C
BattleDataProxy.CalcSubRountineTimeUp = CalcSubRountineTimeUp

def CalcSubRountineElimate(arg_40_0):
	arg_40_0._statistics._elimated = True

	arg_40_0.CalcSubRoutineScore()

	arg_40_0._statistics._battleScore = BattleConst.BattleScore.D
BattleDataProxy.CalcSubRountineElimate = CalcSubRountineElimate

def CalcSubRoutineScore(arg_41_0):
	var_41_0 = arg_41_0._statistics._deadCount * BattleConfig.SR_CONFIG.DEAD_POINT
	var_41_1 = arg_41_0._subRunStatistics.score * BattleConfig.SR_CONFIG.POINT
	var_41_2 = (arg_41_0._statistics._badTime or arg_41_0._statistics._elimated) and 0 or BattleConfig.SR_CONFIG.BASE_POINT
	var_41_3 = var_41_2 + var_41_1 - var_41_0

	if var_41_3 >= BattleConfig.SR_CONFIG.BASE_POINT + BattleConfig.SR_CONFIG.M * BattleConfig.SR_CONFIG.POINT:
		arg_41_0._statistics._battleScore = BattleConst.BattleScore.S
	elif var_41_3 >= BattleConfig.SR_CONFIG.BASE_POINT:
		arg_41_0._statistics._battleScore = BattleConst.BattleScore.A
	elif var_41_3 >= BattleConfig.SR_CONFIG.BASE_POINT - 2 * BattleConfig.SR_CONFIG.DEAD_POINT:
		arg_41_0._statistics._battleScore = BattleConst.BattleScore.B
	else:
		arg_41_0._statistics._battleScore = BattleConst.BattleScore.D

	arg_41_0._subRunStatistics.basePoint = var_41_2
	arg_41_0._subRunStatistics.deadCount = arg_41_0._statistics._deadCount
	arg_41_0._subRunStatistics.losePoint = var_41_0
	arg_41_0._subRunStatistics.point = var_41_1
	arg_41_0._subRunStatistics.total = var_41_3
	arg_41_0._statistics.subRunResult = arg_41_0._subRunStatistics
BattleDataProxy.CalcSubRoutineScore = CalcSubRoutineScore

def AirFightInit(arg_42_0):
	arg_42_0._statistics._airFightStatistics = table()
	arg_42_0._statistics._airFightStatistics.kill = 0
	arg_42_0._statistics._airFightStatistics.score = 0
	arg_42_0._statistics._airFightStatistics.hit = 0
	arg_42_0._statistics._airFightStatistics.lose = 0
	arg_42_0._statistics._airFightStatistics.total = 0
BattleDataProxy.AirFightInit = AirFightInit

def AddAirFightScore(arg_43_0, arg_43_1):
	arg_43_0._statistics._airFightStatistics.score = arg_43_0._statistics._airFightStatistics.score + arg_43_1
	arg_43_0._statistics._airFightStatistics.kill = arg_43_0._statistics._airFightStatistics.kill + 1
	arg_43_0._statistics._airFightStatistics.total = math.max(arg_43_0._statistics._airFightStatistics.score - arg_43_0._statistics._airFightStatistics.lose, 0)

	arg_43_0.DispatchEvent(ys.Event.New(BattleEvent.UPDATE_DODGEM_SCORE, table(
		totalScore = arg_43_0._statistics._airFightStatistics.total
	)))
BattleDataProxy.AddAirFightScore = AddAirFightScore

def DecreaseAirFightScore(arg_44_0, arg_44_1):
	arg_44_0._statistics._airFightStatistics.lose = arg_44_0._statistics._airFightStatistics.lose + arg_44_1
	arg_44_0._statistics._airFightStatistics.hit = arg_44_0._statistics._airFightStatistics.hit + 1
	arg_44_0._statistics._airFightStatistics.total = math.max(arg_44_0._statistics._airFightStatistics.score - arg_44_0._statistics._airFightStatistics.lose, 0)

	arg_44_0.DispatchEvent(ys.Event.New(BattleEvent.UPDATE_DODGEM_SCORE, table(
		totalScore = arg_44_0._statistics._airFightStatistics.total
	)))
BattleDataProxy.DecreaseAirFightScore = DecreaseAirFightScore

def CalcAirFightScore(arg_45_0):
	arg_45_0._statistics._battleScore = BattleConst.BattleScore.S
BattleDataProxy.CalcAirFightScore = BattleConst.BattleScore.S