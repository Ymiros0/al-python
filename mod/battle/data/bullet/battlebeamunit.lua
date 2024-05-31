ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleVariable
local var_0_3 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleBeamUnit = class("BattleBeamUnit")
var_0_0.Battle.BattleBeamUnit.__name = "BattleBeamUnit"

local var_0_4 = var_0_0.Battle.BattleBeamUnit

var_0_4.BEAM_STATE_READY = "ready"
var_0_4.BEAM_STATE_ATTACK = "attack"
var_0_4.BEAM_STATE_FINISH = "finish"

function var_0_4.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._bulletID = arg_1_1
	arg_1_0._beamInfoID = arg_1_2
	arg_1_0._cldList = {}
	arg_1_0._beamState = var_0_4.BEAM_STATE_READY
end

function var_0_4.IsBeamActive(arg_2_0)
	return arg_2_0._aoe:GetActiveFlag()
end

function var_0_4.ClearBeam(arg_3_0)
	arg_3_0._beamState = var_0_4.BEAM_STATE_FINISH
	arg_3_0._aoe = nil
	arg_3_0._cldList = {}
	arg_3_0._nextDamageTime = nil
end

function var_0_4.SetAoeData(arg_4_0, arg_4_1)
	arg_4_0._aoe = arg_4_1
	arg_4_0._beamTemp = var_0_1.GetBarrageTmpDataFromID(arg_4_0._beamInfoID)
	arg_4_0._bulletTemp = var_0_1.GetBulletTmpDataFromID(arg_4_0._bulletID)
	arg_4_0._angle = arg_4_0._beamTemp.angle

	arg_4_0._aoe:SetAngle(arg_4_0._angle + arg_4_0._aimAngle)

	local var_4_0 = arg_4_0._bulletTemp.extra_param.diveFilter

	if var_4_0 then
		arg_4_0._aoe:SetDiveFilter(var_4_0)
	end
end

function var_0_4.SetAimAngle(arg_5_0, arg_5_1)
	arg_5_0._aimAngle = arg_5_1 or 0
end

function var_0_4.SetAimPosition(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	if arg_6_3 == var_0_3.FOE_CODE then
		arg_6_0._aimAngle = math.rad2Deg * math.atan2(arg_6_2.z - arg_6_1.z, arg_6_2.x - arg_6_1.x)
	elseif arg_6_3 == var_0_3.FRIENDLY_CODE then
		arg_6_0._aimAngle = math.rad2Deg * math.atan2(arg_6_1.z - arg_6_2.z, arg_6_1.x - arg_6_2.x)
	end
end

function var_0_4.getAngleRatio(arg_7_0)
	return var_0_2.GetSpeedRatio(arg_7_0._aoe:GetTimeRationExemptKey(), arg_7_0._aoe:GetIFF())
end

function var_0_4.GetAoeData(arg_8_0)
	return arg_8_0._aoe
end

function var_0_4.UpdateBeamPos(arg_9_0, arg_9_1)
	arg_9_0._aoe:SetPosition(Vector3(arg_9_1.x + arg_9_0._beamTemp.offset_x, 0, arg_9_1.z + arg_9_0._beamTemp.offset_z))
end

function var_0_4.UpdateBeamAngle(arg_10_0)
	arg_10_0._angle = arg_10_0._angle + arg_10_0._beamTemp.delta_angle * arg_10_0:getAngleRatio()

	arg_10_0._aoe:SetAngle(arg_10_0._angle + arg_10_0._aimAngle)
end

function var_0_4.AddCldUnit(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_1:GetUniqueID()

	arg_11_0._cldList[var_11_0] = arg_11_1
end

function var_0_4.RemoveCldUnit(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_1:GetUniqueID()

	arg_12_0._cldList[var_12_0] = nil
end

function var_0_4.ChangeBeamState(arg_13_0, arg_13_1)
	arg_13_0._beamState = arg_13_1
end

function var_0_4.GetBeamState(arg_14_0)
	return arg_14_0._beamState
end

function var_0_4.GetCldUnitList(arg_15_0)
	return arg_15_0._cldList
end

function var_0_4.BeginFocus(arg_16_0)
	arg_16_0._nextDamageTime = pg.TimeMgr.GetInstance():GetCombatTime() + arg_16_0._beamTemp.senior_delay
end

function var_0_4.DealDamage(arg_17_0)
	arg_17_0._nextDamageTime = pg.TimeMgr.GetInstance():GetCombatTime() + arg_17_0._beamTemp.delta_delay
end

function var_0_4.CanDealDamage(arg_18_0)
	return arg_18_0._nextDamageTime < pg.TimeMgr.GetInstance():GetCombatTime()
end

function var_0_4.GetFXID(arg_19_0)
	return arg_19_0._bulletTemp.hit_fx
end

function var_0_4.GetSFXID(arg_20_0)
	return arg_20_0._bulletTemp.hit_sfx
end

function var_0_4.GetBulletID(arg_21_0)
	return arg_21_0._bulletID
end

function var_0_4.GetBeamInfoID(arg_22_0)
	return arg_22_0._beamInfoID
end

function var_0_4.GetBeamExtraParam(arg_23_0)
	return arg_23_0._bulletTemp.extra_param
end
