ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = class("BattleDodgemCommand", var_0_0.Battle.BattleSingleDungeonCommand)

var_0_0.Battle.BattleDodgemCommand = var_0_3
var_0_3.__name = "BattleDodgemCommand"

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.Initialize(arg_2_0):
	var_0_3.super.Initialize(arg_2_0)
	arg_2_0._dataProxy.DodgemCountInit()

def var_0_3.DoPrologue(arg_3_0):
	pg.UIMgr.GetInstance().Marching()

	local function var_3_0()
		arg_3_0._uiMediator.OpeningEffect(function()
			arg_3_0._dataProxy.SetupDamageKamikazeShip(var_0_0.Battle.BattleFormulas.CalcDamageLockS2M)
			arg_3_0._dataProxy.SetupDamageCrush(var_0_0.Battle.BattleFormulas.UNoneateralCrush)
			arg_3_0._uiMediator.ShowTimer()
			arg_3_0._state.ChangeState(var_0_0.Battle.BattleState.BATTLE_STATE_FIGHT)
			arg_3_0._waveUpdater.Start())
		arg_3_0._dataProxy.GetFleetByIFF(var_0_0.Battle.BattleConfig.FRIENDLY_CODE).FleetWarcry()

	arg_3_0._uiMediator.SeaSurfaceShift(45, 0, None, var_3_0)
	arg_3_0._uiMediator.ShowDodgemScoreBar()

def var_0_3.initWaveModule(arg_6_0):
	local function var_6_0(arg_7_0, arg_7_1, arg_7_2)
		arg_6_0._dataProxy.SpawnMonster(arg_7_0, arg_7_1, arg_7_2, var_0_0.Battle.BattleConfig.FOE_CODE)

	local function var_6_1()
		if arg_6_0._vertifyFail:
			pg.m02.sendNotification(GAME.CHEATER_MARK, {
				reason = arg_6_0._vertifyFail
			})

			return

		arg_6_0._dataProxy.CalcDodgemScore()
		arg_6_0._state.BattleEnd()

	arg_6_0._waveUpdater = var_0_0.Battle.BattleWaveUpdater.New(var_6_0, None, var_6_1, None)

def var_0_3.onWillDie(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.Dispatcher

	arg_9_0._dataProxy.CalcDodgemCount(var_9_0)

	local var_9_1 = var_9_0.GetDeathReason()

	if var_9_0.GetTemplate().type == ShipType.JinBi and var_9_1 == var_0_0.Battle.BattleConst.UnitDeathReason.CRUSH:
		local var_9_2 = arg_9_0._dataProxy.GetScorePoint()

		var_9_0.DispatchScorePoint(var_9_2)
