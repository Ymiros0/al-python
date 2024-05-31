ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = class("BattleAirFightCommand", var_0_0.Battle.BattleSingleDungeonCommand)

var_0_0.Battle.BattleAirFightCommand = var_0_3
var_0_3.__name = "BattleAirFightCommand"

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)
end

function var_0_3.AddEvent(arg_2_0, ...)
	var_0_3.super.AddEvent(arg_2_0, ...)
	arg_2_0._dataProxy:RegisterEventListener(arg_2_0, var_0_2.COMMON_DATA_INIT_FINISH, arg_2_0.onBattleDataInitFinished)
end

function var_0_3.RemoveEvent(arg_3_0, ...)
	arg_3_0._dataProxy:UnregisterEventListener(arg_3_0, var_0_2.COMMON_DATA_INIT_FINISH)
	var_0_3.super.RemoveEvent(arg_3_0, ...)
end

function var_0_3.DoPrologue(arg_4_0)
	pg.UIMgr.GetInstance():Marching()

	local function var_4_0()
		arg_4_0._uiMediator:OpeningEffect(function()
			arg_4_0._dataProxy:SetupCalculateDamage(var_0_0.Battle.BattleFormulas.FriendInvincibleDamage)
			arg_4_0._dataProxy:SetupDamageKamikazeShip(var_0_0.Battle.BattleFormulas.CalcDamageLockS2M)
			arg_4_0._dataProxy:SetupDamageCrush(var_0_0.Battle.BattleFormulas.FriendInvincibleCrashDamage)
			arg_4_0._uiMediator:ShowTimer()
			arg_4_0._state:ChangeState(var_0_0.Battle.BattleState.BATTLE_STATE_FIGHT)
			arg_4_0._waveUpdater:Start()
		end, SYSTEM_AIRFIGHT)
		arg_4_0._dataProxy:InitAllFleetUnitsWeaponCD()
	end

	arg_4_0._uiMediator:SeaSurfaceShift(1, 15, nil, var_4_0)

	local var_4_1 = arg_4_0._state:GetSceneMediator()

	var_4_1:InitPopScorePool()
	var_4_1:EnablePopContainer(var_0_0.Battle.BattlePopNumManager.CONTAINER_HP, false)
	var_4_1:EnablePopContainer(var_0_0.Battle.BattlePopNumManager.CONTAINER_SCORE, false)
	var_4_1:EnablePopContainer(var_0_0.Battle.BattleHPBarManager.ROOT_NAME, false)
	arg_4_0._uiMediator:ShowAirFightScoreBar()
end

function var_0_3.initWaveModule(arg_7_0)
	local function var_7_0(arg_8_0, arg_8_1, arg_8_2)
		arg_7_0._dataProxy:SpawnMonster(arg_8_0, arg_8_1, arg_8_2, var_0_0.Battle.BattleConfig.FOE_CODE)
	end

	local function var_7_1()
		if arg_7_0._vertifyFail then
			pg.m02:sendNotification(GAME.CHEATER_MARK, {
				reason = arg_7_0._vertifyFail
			})

			return
		end

		arg_7_0._dataProxy:CalcAirFightScore()
		arg_7_0._state:BattleEnd()
	end

	arg_7_0._waveUpdater = var_0_0.Battle.BattleWaveUpdater.New(var_7_0, nil, var_7_1, nil)
end

function var_0_3.onBattleDataInitFinished(arg_10_0)
	arg_10_0._dataProxy:AirFightInit()

	local var_10_0 = arg_10_0._userFleet:GetScoutList()

	for iter_10_0, iter_10_1 in ipairs(var_10_0) do
		iter_10_1:HideWaveFx()
	end
end

function var_0_3.RegisterUnitEvent(arg_11_0, arg_11_1, ...)
	var_0_3.super.RegisterUnitEvent(arg_11_0, arg_11_1, ...)

	if arg_11_1:GetUnitType() == var_0_0.Battle.BattleConst.UnitType.PLAYER_UNIT then
		arg_11_1:RegisterEventListener(arg_11_0, var_0_1.UPDATE_HP, arg_11_0.onPlayerHPUpdate)
	end
end

function var_0_3.UnregisterUnitEvent(arg_12_0, arg_12_1, ...)
	if arg_12_1:GetUnitType() == var_0_0.Battle.BattleConst.UnitType.PLAYER_UNIT then
		arg_12_1:UnregisterEventListener(arg_12_0, var_0_1.UPDATE_HP)
	end

	var_0_3.super.UnregisterUnitEvent(arg_12_0, arg_12_1, ...)
end

var_0_3.ShipType2Point = {
	[ShipType.YuLeiTing] = 200,
	[ShipType.JinBi] = 300,
	[ShipType.ZiBao] = 3000
}
var_0_3.BeenHitDecreasePoint = 10

function var_0_3.onWillDie(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1.Dispatcher
	local var_13_1 = var_13_0:GetDeathReason()
	local var_13_2 = var_13_0:GetTemplate().type

	if var_13_1 == var_0_0.Battle.BattleConst.UnitDeathReason.CRUSH or var_13_1 == var_0_0.Battle.BattleConst.UnitDeathReason.KILLED then
		local var_13_3 = var_0_3.ShipType2Point[var_13_2]

		if var_13_3 and var_13_3 > 0 then
			arg_13_0._dataProxy:AddAirFightScore(var_13_3)
		end
	end
end

function var_0_3.onPlayerHPUpdate(arg_14_0, arg_14_1)
	if arg_14_1.Data.dHP <= 0 then
		arg_14_0._dataProxy:DecreaseAirFightScore(var_0_3.BeenHitDecreasePoint * -arg_14_1.Data.dHP)
	end
end
