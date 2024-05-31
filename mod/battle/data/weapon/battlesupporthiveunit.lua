ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleSupportHiveUnit = class("BattleSupportHiveUnit", var_0_0.Battle.BattleWeaponUnit)
var_0_0.Battle.BattleSupportHiveUnit.__name = "BattleSupportHiveUnit"

local var_0_3 = var_0_0.Battle.BattleSupportHiveUnit

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)
end

function var_0_3.Update(arg_2_0)
	arg_2_0:UpdateReload()
	arg_2_0:updateMovementInfo()

	if arg_2_0._currentState == arg_2_0.STATE_READY then
		if arg_2_0._host:GetUnitType() ~= var_0_1.UnitType.PLAYER_UNIT then
			if arg_2_0._preCastInfo.time == nil then
				arg_2_0._currentState = arg_2_0.STATE_PRECAST_FINISH
			else
				arg_2_0:PreCast()
			end
		elseif #var_0_0.Battle.BattleTargetChoise.TargetAircraftGB(arg_2_0._host) > 0 then
			arg_2_0._currentState = arg_2_0.STATE_PRECAST_FINISH
		end
	end

	if arg_2_0._currentState == arg_2_0.STATE_PRECAST_FINISH then
		arg_2_0:updateMovementInfo()
		arg_2_0:Fire()
	end
end

function var_0_3.Fire(arg_3_0)
	arg_3_0:DispatchGCD()

	arg_3_0._currentState = arg_3_0.STATE_ATTACK

	arg_3_0:DoAttack()

	return true
end

function var_0_3.createMajorEmitter(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5)
	local function var_4_0(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)
		local var_5_0, var_5_1 = arg_4_0:SpwanAircraft(arg_5_2)

		var_5_0:AddCreateTimer(var_5_1, 1.5)

		if arg_4_0._debugRecordDEFAircraft then
			table.insert(arg_4_0._debugRecordDEFAircraft, var_5_0)
		end
	end

	var_0_3.super.createMajorEmitter(arg_4_0, arg_4_1, arg_4_2, nil, var_4_0, nil)
end

function var_0_3.SpwanAircraft(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0._dataProxy:CreateAircraft(arg_6_0._host, arg_6_0._tmpData.id, arg_6_0:GetPotential(), arg_6_0._skinID)
	local var_6_1 = arg_6_0:GetBaseAngle() + arg_6_1
	local var_6_2 = math.deg2Rad * var_6_1
	local var_6_3 = Vector3(math.cos(var_6_2), 0, math.sin(var_6_2))

	return var_6_0, var_6_3
end

function var_0_3.GetATKAircraftList(arg_7_0)
	arg_7_0._debugRecordATKAircraft = arg_7_0._debugRecordATKAircraft or {}

	return arg_7_0._debugRecordATKAircraft
end

function var_0_3.GetDEFAircraftList(arg_8_0)
	arg_8_0._debugRecordDEFAircraft = arg_8_0._debugRecordDEFAircraft or {}

	return arg_8_0._debugRecordDEFAircraft
end

function var_0_3.GetDamageSUM(arg_9_0)
	local var_9_0 = 0
	local var_9_1 = arg_9_0:GetDEFAircraftList()

	for iter_9_0, iter_9_1 in ipairs(var_9_1) do
		local var_9_2 = iter_9_1:GetWeapon()

		for iter_9_2, iter_9_3 in ipairs(var_9_2) do
			var_9_0 = var_9_0 + iter_9_3:GetDamageSUM()
		end
	end

	return var_9_0
end
