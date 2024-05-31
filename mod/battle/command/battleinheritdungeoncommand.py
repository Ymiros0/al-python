ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = class("BattleInheritDungeonCommand", var_0_0.Battle.BattleSingleDungeonCommand)

var_0_0.Battle.BattleInheritDungeonCommand = var_0_3
var_0_3.__name = "BattleInheritDungeonCommand"

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.initWaveModule(arg_2_0):
	local function var_2_0(arg_3_0, arg_3_1, arg_3_2)
		arg_2_0._dataProxy.SpawnMonster(arg_3_0, arg_3_1, arg_3_2, var_0_0.Battle.BattleConfig.FOE_CODE)

	local function var_2_1(arg_4_0)
		arg_2_0._dataProxy.SpawnAirFighter(arg_4_0)

	local function var_2_2()
		if arg_2_0._vertifyFail:
			pg.m02.sendNotification(GAME.CHEATER_MARK, {
				reason = arg_2_0._vertifyFail
			})

			return

		arg_2_0.CalcStatistic()
		arg_2_0.calcDamageData()
		arg_2_0._state.BattleEnd()

	local function var_2_3(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4)
		arg_2_0._dataProxy.SpawnCubeArea(var_0_0.Battle.BattleConst.AOEField.SURFACE, -1, arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4)

	arg_2_0._waveUpdater = var_0_0.Battle.BattleWaveUpdater.New(var_2_0, var_2_1, var_2_2, var_2_3)

def var_0_3.onInitBattle(arg_7_0):
	var_0_3.super.onInitBattle(arg_7_0)

	local var_7_0 = arg_7_0._dataProxy.GetInitData()

	arg_7_0._specificEnemyList = var_0_0.Battle.BattleDataFunction.GetSpecificEnemyList(var_7_0.ActID, var_7_0.StageTmpId)

def var_0_3.onAddUnit(arg_8_0, arg_8_1):
	var_0_3.super.onAddUnit(arg_8_0, arg_8_1)

	local var_8_0 = arg_8_1.Data.unit

	if table.contains(arg_8_0._specificEnemyList, var_8_0.GetTemplateID()):
		arg_8_0._dataProxy.InitSpecificEnemyStatistics(var_8_0)

def var_0_3.onPlayerShutDown(arg_9_0, arg_9_1):
	if arg_9_0._state.GetState() != arg_9_0._state.BATTLE_STATE_FIGHT:
		return

	if arg_9_1.Data.unit == arg_9_0._userFleet.GetFlagShip() and arg_9_0._dataProxy.GetInitData().battleType != SYSTEM_PROLOGUE and arg_9_0._dataProxy.GetInitData().battleType != SYSTEM_PERFORM:
		arg_9_0.CalcStatistic()
		arg_9_0.calcDamageData()
		arg_9_0._state.BattleEnd()

		return

	if #arg_9_0._userFleet.GetScoutList() == 0:
		arg_9_0.CalcStatistic()
		arg_9_0.calcDamageData()
		arg_9_0._state.BattleEnd()

def var_0_3.onUpdateCountDown(arg_10_0, arg_10_1):
	if arg_10_0._dataProxy.GetCountDown() <= 0:
		arg_10_0._dataProxy.EnemyEscape()
		arg_10_0.CalcStatistic()
		arg_10_0.calcDamageData()
		arg_10_0._state.BattleTimeUp()

def var_0_3.calcDamageData(arg_11_0):
	local var_11_0 = arg_11_0._dataProxy.GetInitData()

	arg_11_0._dataProxy.CalcActBossDamageInfo(var_11_0.ActID)
