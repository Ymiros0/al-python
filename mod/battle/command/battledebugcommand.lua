ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = class("BattleDebugCommand", var_0_0.MVC.Command)

var_0_0.Battle.BattleDebugCommand = var_0_3
var_0_3.__name = "BattleDebugCommand"

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)
end

function var_0_3.Initialize(arg_2_0)
	arg_2_0:Init()
	var_0_3.super.Initialize(arg_2_0)

	arg_2_0._dataProxy = arg_2_0._state:GetProxyByName(var_0_0.Battle.BattleDataProxy.__name)
	arg_2_0._uiMediator = arg_2_0._state:GetMediatorByName(var_0_0.Battle.BattleUIMediator.__name)

	arg_2_0:AddEvent()
end

function var_0_3.DoPrologue(arg_3_0)
	(function()
		arg_3_0._uiMediator:OpeningEffect(function()
			arg_3_0._uiMediator:ShowAutoBtn()
			arg_3_0._uiMediator:ShowTimer()
			arg_3_0._state:ChangeState(var_0_0.Battle.BattleState.BATTLE_STATE_FIGHT)
		end, SYSTEM_DEBUG)
		arg_3_0._dataProxy:InitAllFleetUnitsWeaponCD()
		arg_3_0._dataProxy:TirggerBattleStartBuffs()
	end)()
end

function var_0_3.Init(arg_6_0)
	arg_6_0._unitDataList = {}
end

function var_0_3.Clear(arg_7_0)
	for iter_7_0, iter_7_1 in pairs(arg_7_0._unitDataList) do
		arg_7_0:UnregisterUnitEvent(iter_7_1)

		arg_7_0._unitDataList[iter_7_0] = nil
	end
end

function var_0_3.Reinitialize(arg_8_0)
	arg_8_0._state:Deactive()
	arg_8_0:Clear()
	arg_8_0:Init()
end

function var_0_3.Dispose(arg_9_0)
	var_0_0.Battle.BattleDataProxy.Update = var_0_0.Battle.BattleDebugConsole.ProxyUpdateNormal
	var_0_0.Battle.BattleDataProxy.UpdateAutoComponent = var_0_0.Battle.BattleDebugConsole.ProxyUpdateAutoComponentNormal

	arg_9_0:Clear()
	arg_9_0:RemoveEvent()
	var_0_3.super.Dispose(arg_9_0)
end

function var_0_3.AddEvent(arg_10_0)
	arg_10_0._dataProxy:RegisterEventListener(arg_10_0, var_0_2.STAGE_DATA_INIT_FINISH, arg_10_0.onInitBattle)
	arg_10_0._dataProxy:RegisterEventListener(arg_10_0, var_0_2.ADD_UNIT, arg_10_0.onAddUnit)
	arg_10_0._dataProxy:RegisterEventListener(arg_10_0, var_0_2.REMOVE_UNIT, arg_10_0.onRemoveUnit)
	arg_10_0._dataProxy:RegisterEventListener(arg_10_0, var_0_2.SHUT_DOWN_PLAYER, arg_10_0.onPlayerShutDown)
end

function var_0_3.RemoveEvent(arg_11_0)
	arg_11_0._dataProxy:UnregisterEventListener(arg_11_0, var_0_2.STAGE_DATA_INIT_FINISH)
	arg_11_0._dataProxy:UnregisterEventListener(arg_11_0, var_0_2.ADD_UNIT)
	arg_11_0._dataProxy:UnregisterEventListener(arg_11_0, var_0_2.REMOVE_UNIT)
	arg_11_0._dataProxy:UnregisterEventListener(arg_11_0, var_0_2.SHUT_DOWN_PLAYER)
end

function var_0_3.onInitBattle(arg_12_0)
	arg_12_0._userFleet = arg_12_0._dataProxy:GetFleetByIFF(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)
end

function var_0_3.onAddUnit(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1.Data.type
	local var_13_1 = arg_13_1.Data.unit

	arg_13_0:RegisterUnitEvent(var_13_1)

	arg_13_0._unitDataList[var_13_1:GetUniqueID()] = var_13_1

	if var_13_0 ~= var_0_0.Battle.BattleConst.UnitType.ENEMY_UNIT and var_13_0 ~= var_0_0.Battle.BattleConst.UnitType.BOSS_UNIT and var_13_0 ~= var_0_0.Battle.BattleConst.UnitType.MINION_UNIT and var_13_0 ~= var_0_0.Battle.BattleConst.UnitType.NPC_UNIT and var_13_0 == var_0_0.Battle.BattleConst.UnitType.BOSS_UNIT then
		-- block empty
	end
end

function var_0_3.RegisterUnitEvent(arg_14_0, arg_14_1)
	arg_14_1:RegisterEventListener(arg_14_0, var_0_1.WILL_DIE, arg_14_0.onWillDie)
	arg_14_1:RegisterEventListener(arg_14_0, var_0_1.DYING, arg_14_0.onUnitDying)

	if arg_14_1:GetUnitType() == var_0_0.Battle.BattleConst.UnitType.PLAYER_UNIT then
		arg_14_1:RegisterEventListener(arg_14_0, var_0_1.SHUT_DOWN_PLAYER, arg_14_0.onShutDownPlayer)
	end
end

function var_0_3.UnregisterUnitEvent(arg_15_0, arg_15_1)
	arg_15_1:UnregisterEventListener(arg_15_0, var_0_1.WILL_DIE)
	arg_15_1:UnregisterEventListener(arg_15_0, var_0_1.DYING)

	if arg_15_1:GetUnitType() == var_0_0.Battle.BattleConst.UnitType.PLAYER_UNIT then
		arg_15_1:UnregisterEventListener(arg_15_0, var_0_1.SHUT_DOWN_PLAYER)
	end
end

function var_0_3.onRemoveUnit(arg_16_0, arg_16_1)
	local var_16_0 = arg_16_1.Data.UID
	local var_16_1 = arg_16_0._unitDataList[var_16_0]

	if var_16_1 == nil then
		return
	end

	arg_16_0:UnregisterUnitEvent(var_16_1)

	arg_16_0._unitDataList[var_16_0] = nil
end

function var_0_3.onPlayerShutDown(arg_17_0, arg_17_1)
	if arg_17_1.Data.unit == arg_17_0._userFleet:GetMainList() == 0 then
		arg_17_0._dataProxy:KillAllAirStrike()
		arg_17_0._dataProxy:KillAllEnemy()
		arg_17_0._dataProxy:CLSBullet(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)
		arg_17_0._dataProxy:CLSBullet(var_0_0.Battle.BattleConfig.FOE_CODE)

		local var_17_0 = arg_17_0._dataProxy:GetInitData().MainUnitList

		for iter_17_0, iter_17_1 in ipairs(var_17_0) do
			arg_17_0._dataProxy:SpawnMain(iter_17_1, var_0_0.Battle.BattleConfig.FRIENDLY_CODE)
		end
	end

	if #arg_17_0._userFleet:GetScoutList() == 0 then
		arg_17_0._dataProxy:KillAllAirStrike()
		arg_17_0._dataProxy:KillAllEnemy()
		arg_17_0._dataProxy:CLSBullet(var_0_0.Battle.BattleConfig.FRIENDLY_CODE)
		arg_17_0._dataProxy:CLSBullet(var_0_0.Battle.BattleConfig.FOE_CODE)

		local var_17_1 = arg_17_0._dataProxy:GetInitData().VanguardUnitList

		for iter_17_2, iter_17_3 in ipairs(var_17_1) do
			arg_17_0._dataProxy:SpawnVanguard(iter_17_3, var_0_0.Battle.BattleConfig.FRIENDLY_CODE)
		end
	end
end

function var_0_3.onUnitDying(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_1.Dispatcher:GetUniqueID()

	arg_18_0._dataProxy:KillUnit(var_18_0)
end

function var_0_3.onWillDie(arg_19_0, arg_19_1)
	local var_19_0 = arg_19_1.Dispatcher

	arg_19_0._dataProxy:CalcBattleScoreWhenDead(var_19_0)

	local var_19_1 = arg_19_0._dataProxy:IsThereBoss()

	if var_19_0:IsBoss() and not var_19_1 then
		arg_19_0._dataProxy:KillAllEnemy()
	end
end

function var_0_3.onShutDownPlayer(arg_20_0, arg_20_1)
	local var_20_0 = arg_20_1.Dispatcher:GetUniqueID()

	arg_20_0._dataProxy:ShutdownPlayerUnit(var_20_0)
end
