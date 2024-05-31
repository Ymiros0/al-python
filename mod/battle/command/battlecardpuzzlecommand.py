ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = class("BattleCardPuzzleCommand", var_0_0.MVC.Command)

var_0_0.Battle.BattleCardPuzzleCommand = var_0_3
var_0_3.__name = "BattleCardPuzzleCommand"

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.Initialize(arg_2_0):
	arg_2_0.Init()
	var_0_3.super.Initialize(arg_2_0)

	arg_2_0._dataProxy = arg_2_0._state.GetProxyByName(var_0_0.Battle.BattleDataProxy.__name)
	arg_2_0._uiMediator = arg_2_0._state.GetMediatorByName(var_0_0.Battle.BattleUIMediator.__name)

	arg_2_0.AddEvent()

def var_0_3.DoPrologue(arg_3_0):
	pg.UIMgr.GetInstance().Marching()

	local function var_3_0()
		arg_3_0._uiMediator.OpeningEffect(function()
			arg_3_0._dataProxy.SetupCalculateDamage(var_0_0.Battle.BattleCardPuzzleFormulas.CreateContextCalculateDamage)
			arg_3_0._state.ChangeState(var_0_0.Battle.BattleState.BATTLE_STATE_FIGHT)
			arg_3_0._waveUpdater.Start(), SYSTEM_CARDPUZZLE)
		arg_3_0._dataProxy.InitAllFleetUnitsWeaponCD()
		arg_3_0._dataProxy.TirggerBattleStartBuffs()
		arg_3_0._dataProxy.StartCardPuzzle()

		local var_4_0 = arg_3_0._dataProxy.GetFleetByIFF(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)

		arg_3_0._joystickBot = var_0_0.Battle.CardPuzzleJoyStickAutoBot.New(arg_3_0._dataProxy, var_4_0)

		arg_3_0._joystickBot.SetActive(True)
		arg_3_0._state.EnableJoystick(False)

	arg_3_0._uiMediator.SeaSurfaceShift(45, 0, None, var_3_0)

def var_0_3.Init(arg_6_0):
	arg_6_0._unitDataList = {}

	arg_6_0.initWaveModule()

def var_0_3.initWaveModule(arg_7_0):
	local function var_7_0(arg_8_0, arg_8_1, arg_8_2)
		arg_7_0._dataProxy.SpawnMonster(arg_8_0, arg_8_1, arg_8_2, var_0_0.Battle.BattleConfig.FOE_CODE)

	local function var_7_1(arg_9_0)
		arg_7_0._dataProxy.SpawnAirFighter(arg_9_0)

	local function var_7_2()
		if arg_7_0._vertifyFail:
			pg.m02.sendNotification(GAME.CHEATER_MARK, {
				reason = arg_7_0._vertifyFail
			})

			return

		arg_7_0.CalcStatistic()
		arg_7_0._state.BattleEnd()

	local function var_7_3(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4)
		arg_7_0._dataProxy.SpawnCubeArea(var_0_0.Battle.BattleConst.AOEField.SURFACE, -1, arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4)

	arg_7_0._waveUpdater = var_0_0.Battle.BattleWaveUpdater.New(var_7_0, var_7_1, var_7_2, var_7_3)

def var_0_3.Clear(arg_12_0):
	for iter_12_0, iter_12_1 in pairs(arg_12_0._unitDataList):
		arg_12_0.UnregisterUnitEvent(iter_12_1)

		arg_12_0._unitDataList[iter_12_0] = None

	arg_12_0._waveUpdater.Clear()

def var_0_3.Reinitialize(arg_13_0):
	arg_13_0._state.Deactive()
	arg_13_0.Clear()
	arg_13_0.Init()

def var_0_3.Dispose(arg_14_0):
	var_0_0.Battle.BattleDataProxy.Update = var_0_0.Battle.BattleDebugConsole.ProxyUpdateNormal
	var_0_0.Battle.BattleDataProxy.UpdateAutoComponent = var_0_0.Battle.BattleDebugConsole.ProxyUpdateAutoComponentNormal

	arg_14_0._joystickBot.Dispose()
	arg_14_0.Clear()
	arg_14_0.RemoveEvent()
	var_0_3.super.Dispose(arg_14_0)

def var_0_3.AddEvent(arg_15_0):
	arg_15_0._dataProxy.RegisterEventListener(arg_15_0, var_0_2.STAGE_DATA_INIT_FINISH, arg_15_0.onInitBattle)
	arg_15_0._dataProxy.RegisterEventListener(arg_15_0, var_0_2.ADD_UNIT, arg_15_0.onAddUnit)
	arg_15_0._dataProxy.RegisterEventListener(arg_15_0, var_0_2.REMOVE_UNIT, arg_15_0.onRemoveUnit)
	arg_15_0._dataProxy.RegisterEventListener(arg_15_0, var_0_2.SHUT_DOWN_PLAYER, arg_15_0.onPlayerShutDown)

def var_0_3.RemoveEvent(arg_16_0):
	arg_16_0._dataProxy.UnregisterEventListener(arg_16_0, var_0_2.STAGE_DATA_INIT_FINISH)
	arg_16_0._dataProxy.UnregisterEventListener(arg_16_0, var_0_2.ADD_UNIT)
	arg_16_0._dataProxy.UnregisterEventListener(arg_16_0, var_0_2.REMOVE_UNIT)
	arg_16_0._dataProxy.UnregisterEventListener(arg_16_0, var_0_2.SHUT_DOWN_PLAYER)

def var_0_3.onInitBattle(arg_17_0):
	arg_17_0._userFleet = arg_17_0._dataProxy.GetFleetByIFF(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)

	arg_17_0._waveUpdater.SetWavesData(arg_17_0._dataProxy.GetStageInfo())

def var_0_3.onAddUnit(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_1.Data.type
	local var_18_1 = arg_18_1.Data.unit

	arg_18_0.RegisterUnitEvent(var_18_1)

	arg_18_0._unitDataList[var_18_1.GetUniqueID()] = var_18_1

	if var_18_0 == var_0_0.Battle.BattleConst.UnitType.ENEMY_UNIT or var_18_0 == var_0_0.Battle.BattleConst.UnitType.BOSS_UNIT:
		arg_18_0._waveUpdater.AddMonster(var_18_1)

def var_0_3.RegisterUnitEvent(arg_19_0, arg_19_1):
	arg_19_1.RegisterEventListener(arg_19_0, var_0_1.WILL_DIE, arg_19_0.onWillDie)
	arg_19_1.RegisterEventListener(arg_19_0, var_0_1.DYING, arg_19_0.onUnitDying)

	if arg_19_1.GetUnitType() == var_0_0.Battle.BattleConst.UnitType.PLAYER_UNIT:
		arg_19_1.RegisterEventListener(arg_19_0, var_0_1.SHUT_DOWN_PLAYER, arg_19_0.onShutDownPlayer)

def var_0_3.UnregisterUnitEvent(arg_20_0, arg_20_1):
	arg_20_1.UnregisterEventListener(arg_20_0, var_0_1.WILL_DIE)
	arg_20_1.UnregisterEventListener(arg_20_0, var_0_1.DYING)

	if arg_20_1.GetUnitType() == var_0_0.Battle.BattleConst.UnitType.PLAYER_UNIT:
		arg_20_1.UnregisterEventListener(arg_20_0, var_0_1.SHUT_DOWN_PLAYER)

def var_0_3.onRemoveUnit(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_1.Data.UID

	arg_21_0._waveUpdater.RemoveMonster(var_21_0)

	local var_21_1 = arg_21_0._unitDataList[var_21_0]

	if var_21_1 == None:
		return

	arg_21_0.UnregisterUnitEvent(var_21_1)

	arg_21_0._unitDataList[var_21_0] = None

def var_0_3.onPlayerShutDown(arg_22_0, arg_22_1):
	arg_22_0.CalcStatistic()
	arg_22_0._state.BattleEnd()

def var_0_3.onUnitDying(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_1.Dispatcher.GetUniqueID()

	arg_23_0._dataProxy.KillUnit(var_23_0)

def var_0_3.onWillDie(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_1.Dispatcher

	arg_24_0._dataProxy.CalcBattleScoreWhenDead(var_24_0)

	local var_24_1 = arg_24_0._dataProxy.IsThereBoss()

	if var_24_0.IsBoss() and not var_24_1:
		arg_24_0._dataProxy.KillAllEnemy()

def var_0_3.onShutDownPlayer(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_1.Dispatcher.GetUniqueID()

	arg_25_0._dataProxy.ShutdownPlayerUnit(var_25_0)

def var_0_3.CalcStatistic(arg_26_0):
	arg_26_0._dataProxy.CalcCardPuzzleScoreAtEnd(arg_26_0._userFleet)
