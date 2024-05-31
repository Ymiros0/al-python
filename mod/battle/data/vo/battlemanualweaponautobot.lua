ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleManualWeaponAutoBot = class("BattleManualWeaponAutoBot")
var_0_0.Battle.BattleManualWeaponAutoBot.__name = "BattleManualWeaponAutoBot"

local var_0_3 = var_0_0.Battle.BattleManualWeaponAutoBot

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._fleetVO = arg_1_1

	arg_1_0:init(arg_1_1)
end

function var_0_3.init(arg_2_0)
	arg_2_0._active = false
	arg_2_0._isPlayFocus = true
	arg_2_0._chargeVO = arg_2_0._fleetVO:GetChargeWeaponVO()
	arg_2_0._torpedoVO = arg_2_0._fleetVO:GetTorpedoWeaponVO()
	arg_2_0._AAVO = arg_2_0._fleetVO:GetAirAssistVO()
	arg_2_0._totalTime = 0
	arg_2_0._lastActiveTimeStamp = nil
end

function var_0_3.Update(arg_3_0)
	if arg_3_0._active then
		if not arg_3_0._torpedoVO:IsOverLoad() then
			arg_3_0._fleetVO:QuickCastTorpedo()

			return
		end

		if not arg_3_0._AAVO:IsOverLoad() then
			arg_3_0._fleetVO:UnleashAllInStrike()

			return
		end

		if not arg_3_0._chargeVO:IsOverLoad() then
			arg_3_0._fleetVO:QuickTagChrageWeapon(arg_3_0._isPlayFocus)

			return
		end
	end
end

function var_0_3.IsActive(arg_4_0)
	return arg_4_0._active
end

function var_0_3.SetActive(arg_5_0, arg_5_1, arg_5_2)
	if arg_5_0._active ~= arg_5_1 and arg_5_1 == true then
		arg_5_0._lastActiveTimeStamp = pg.TimeMgr.GetInstance():GetCombatTime()
	elseif arg_5_0._active ~= arg_5_1 and arg_5_1 == false and arg_5_0._lastActiveTimeStamp ~= nil then
		local var_5_0 = pg.TimeMgr.GetInstance():GetCombatTime()

		arg_5_0._totalTime = arg_5_0._totalTime + (var_5_0 - arg_5_0._lastActiveTimeStamp)
		arg_5_0._lastActiveTimeStamp = nil
	end

	arg_5_0._fleetVO:AutoBotUpdated(arg_5_1)

	arg_5_0._active = arg_5_1
	arg_5_0._isPlayFocus = arg_5_2
end

function var_0_3.GetTotalActiveDuration(arg_6_0)
	if arg_6_0._lastActiveTimeStamp then
		local var_6_0 = pg.TimeMgr.GetInstance():GetCombatTime()

		arg_6_0._totalTime = arg_6_0._totalTime + (var_6_0 - arg_6_0._lastActiveTimeStamp)
		arg_6_0._lastActiveTimeStamp = nil
	end

	return arg_6_0._totalTime
end

function var_0_3.Dispose(arg_7_0)
	arg_7_0._chargeVO = nil
	arg_7_0._torpedoVO = nil
	arg_7_0._AAVO = nil
	arg_7_0._dataProxy = nil
	arg_7_0._uiMediator = nil

	var_0_0.EventListener.DetachEventListener(arg_7_0)
end
