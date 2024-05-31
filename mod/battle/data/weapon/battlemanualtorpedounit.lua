ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = class("BattleManualTorpedoUnit", var_0_0.Battle.BattleTorpedoUnit)

var_0_0.Battle.BattleManualTorpedoUnit = var_0_2
var_0_2.__name = "BattleManualTorpedoUnit"

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
end

function var_0_2.createMajorEmitter(arg_2_0, arg_2_1, arg_2_2)
	local function var_2_0(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		local var_3_0 = arg_2_0._emitBulletIDList[arg_2_2]
		local var_3_1 = arg_2_0:Spawn(var_3_0, nil, var_0_2.INTERNAL)

		var_3_1:SetOffsetPriority(arg_3_3)
		var_3_1:SetShiftInfo(arg_3_0, arg_3_1)
		var_3_1:SetRotateInfo(nil, arg_2_0._botAutoAimAngle, arg_3_2)
		arg_2_0:DispatchBulletEvent(var_3_1)

		return var_3_1
	end

	local function var_2_1()
		return
	end

	var_0_2.super.createMajorEmitter(arg_2_0, arg_2_1, arg_2_2, nil, var_2_0, var_2_1)
end

function var_0_2.Update(arg_5_0)
	arg_5_0:UpdateReload()
end

function var_0_2.SetPlayerTorpedoWeaponVO(arg_6_0, arg_6_1)
	arg_6_0._playerTorpedoVO = arg_6_1
end

function var_0_2.TriggerBuffOnReady(arg_7_0)
	arg_7_0._host:TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_MANUAL_TORPEDO_READY, {})
end

function var_0_2.Fire(arg_8_0, arg_8_1)
	if arg_8_1 then
		arg_8_0:updateMovementInfo()

		local var_8_0 = var_0_0.Battle.BattleTargetChoise.TargetHarmRandomByWeight(arg_8_0._host, nil, arg_8_0:GetFilteredList())[1]

		if var_8_0 then
			local var_8_1 = var_8_0:GetPosition()
			local var_8_2 = arg_8_0._host:GetPosition()

			arg_8_0._botAutoAimAngle = math.rad2Deg * math.atan2(var_8_1.z - var_8_2.z, var_8_1.x - var_8_2.x)
		else
			arg_8_0._botAutoAimAngle = arg_8_0:GetBaseAngle()
		end
	else
		arg_8_0._botAutoAimAngle = arg_8_0:GetBaseAngle()
	end

	var_0_2.super.Fire(arg_8_0)

	return true
end

function var_0_2.DoAttack(arg_9_0)
	arg_9_0:DispatchEvent(var_0_0.Event.New(var_0_1.TORPEDO_WEAPON_FIRE, {}))
	var_0_2.super.DoAttack(arg_9_0)
	arg_9_0:DispatchEvent(var_0_0.Event.New(var_0_1.MANUAL_WEAPON_FIRE, {}))
end

function var_0_2.InitialCD(arg_10_0)
	var_0_2.super.InitialCD(arg_10_0)
	arg_10_0._playerTorpedoVO:InitialDeduct(arg_10_0)
	arg_10_0._playerTorpedoVO:Charge(arg_10_0)
end

function var_0_2.EnterCoolDown(arg_11_0)
	var_0_2.super.EnterCoolDown(arg_11_0)
	arg_11_0._playerTorpedoVO:Charge(arg_11_0)
end

function var_0_2.OverHeat(arg_12_0)
	var_0_2.super.OverHeat(arg_12_0)
	arg_12_0._playerTorpedoVO:Deduct(arg_12_0)
end

function var_0_2.Cease(arg_13_0)
	if arg_13_0._currentState == var_0_2.STATE_OVER_HEAT then
		arg_13_0:interruptAllEmitter()
	end
end

function var_0_2.handleCoolDown(arg_14_0)
	arg_14_0._currentState = arg_14_0.STATE_READY

	arg_14_0._playerTorpedoVO:Plus(arg_14_0)
	arg_14_0:DispatchEvent(var_0_0.Event.New(var_0_1.TORPEDO_WEAPON_READY, {}))
	arg_14_0:DispatchEvent(var_0_0.Event.New(var_0_1.MANUAL_WEAPON_READY, {}))
	arg_14_0:TriggerBuffOnReady()

	arg_14_0._CDstartTime = nil
	arg_14_0._reloadBoostList = {}
end

function var_0_2.FlushReloadMax(arg_15_0, arg_15_1)
	if var_0_2.super.FlushReloadMax(arg_15_0, arg_15_1) then
		return true
	end

	arg_15_0._playerTorpedoVO:RefreshReloadingBar()
end

function var_0_2.FlushReloadRequire(arg_16_0)
	if var_0_2.super.FlushReloadRequire(arg_16_0) then
		return true
	end

	arg_16_0._playerTorpedoVO:RefreshReloadingBar()
end

function var_0_2.QuickCoolDown(arg_17_0)
	if arg_17_0._currentState == arg_17_0.STATE_OVER_HEAT then
		arg_17_0._currentState = arg_17_0.STATE_READY

		arg_17_0._playerTorpedoVO:InstantCoolDown(arg_17_0)
		arg_17_0:DispatchEvent(var_0_0.Event.New(var_0_1.MANUAL_WEAPON_INSTANT_READY, {}))

		arg_17_0._CDstartTime = nil
		arg_17_0._reloadBoostList = {}
	end
end

function var_0_2.Prepar(arg_18_0)
	arg_18_0._currentState = arg_18_0.STATE_PRECAST

	local var_18_0 = {}
	local var_18_1 = var_0_0.Event.New(var_0_1.TORPEDO_WEAPON_PREPAR, var_18_0)

	arg_18_0:DispatchEvent(var_18_1)
end

function var_0_2.Cancel(arg_19_0)
	arg_19_0._currentState = arg_19_0.STATE_READY

	local var_19_0 = var_0_0.Event.New(var_0_1.TORPEDO_WEAPON_CANCEL, {})

	arg_19_0:DispatchEvent(var_19_0)
end

function var_0_2.ReloadBoost(arg_20_0, arg_20_1)
	local var_20_0 = 0

	for iter_20_0, iter_20_1 in ipairs(arg_20_0._reloadBoostList) do
		var_20_0 = var_20_0 + iter_20_1
	end

	local var_20_1 = var_20_0 + arg_20_1
	local var_20_2 = pg.TimeMgr.GetInstance():GetCombatTime() - arg_20_0._jammingTime - arg_20_0._CDstartTime
	local var_20_3

	if var_20_1 < 0 then
		var_20_3 = math.max(var_20_1, (arg_20_0._reloadRequire - var_20_2) * -1)
	else
		var_20_3 = math.min(var_20_1, var_20_2)
	end

	fixValue = var_20_3 - var_20_1 + arg_20_1

	table.insert(arg_20_0._reloadBoostList, fixValue)
end

function var_0_2.AppendReloadBoost(arg_21_0, arg_21_1)
	if arg_21_0._currentState == arg_21_0.STATE_OVER_HEAT then
		arg_21_0._playerTorpedoVO:ReloadBoost(arg_21_0, arg_21_1)
	end
end
