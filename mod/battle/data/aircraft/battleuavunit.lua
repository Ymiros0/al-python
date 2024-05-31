ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleTargetChoise
local var_0_3 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattelUAVUnit = class("BattelUAVUnit", var_0_0.Battle.BattleAircraftUnit)
var_0_0.Battle.BattelUAVUnit.__name = "BattelUAVUnit"

local var_0_4 = var_0_0.Battle.BattelUAVUnit

var_0_4.MOVE_STATE = "MOVE_STATE"
var_0_4.HOVER_STATE = "HOVER_STATE"

function var_0_4.Ctor(arg_1_0, arg_1_1)
	var_0_4.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._dir = var_0_0.Battle.BattleConst.UnitDir.LEFT
	arg_1_0._type = var_0_0.Battle.BattleConst.UnitType.UAV_UNIT
end

function var_0_4.Update(arg_2_0, arg_2_1)
	arg_2_0:updatePatrol(arg_2_1)
end

function var_0_4.SetTemplate(arg_3_0, arg_3_1)
	var_0_4.super.SetTemplate(arg_3_0, arg_3_1)

	local var_3_0 = arg_3_1.funnel_behavior.offsetX * arg_3_0:GetIFF()
	local var_3_1 = arg_3_1.funnel_behavior.offsetZ
	local var_3_2 = var_0_0.Battle.BattleDataProxy.GetInstance():GetVanguardBornCoordinate(arg_3_0:GetIFF())

	arg_3_0._centerPos = BuildVector3(var_3_2) + Vector3(var_3_0, 0, var_3_1)
	arg_3_0._range = arg_3_1.funnel_behavior.hover_range
end

function var_0_4.changePartolState(arg_4_0, arg_4_1)
	if arg_4_1 == var_0_4.MOVE_STATE then
		arg_4_0:changeToMoveState()
	elseif arg_4_1 == var_0_4.HOVER_STATE then
		arg_4_0:changeToHoverState()
	end

	arg_4_0._portalState = arg_4_1
end

function var_0_4.AddCreateTimer(arg_5_0, arg_5_1, arg_5_2)
	arg_5_0._currentState = arg_5_0.STATE_CREATE
	arg_5_0._speedDir = arg_5_1
	arg_5_0._velocity = var_0_0.Battle.BattleFormulas.ConvertAircraftSpeed(20)
	arg_5_2 = arg_5_2 or 1.5

	local function var_5_0()
		arg_5_0._existStartTime = pg.TimeMgr.GetInstance():GetCombatTime()
		arg_5_0._velocity = var_0_0.Battle.BattleFormulas.ConvertAircraftSpeed(arg_5_0._tmpData.speed)

		arg_5_0:changePartolState(var_0_4.MOVE_STATE)
		pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_5_0._createTimer)

		arg_5_0._createTimer = nil
	end

	arg_5_0.updatePatrol = arg_5_0._updateCreate
	arg_5_0._createTimer = pg.TimeMgr.GetInstance():AddBattleTimer("AddCreateTimer", 0, arg_5_2, var_5_0)
end

function var_0_4._updateCreate(arg_7_0)
	arg_7_0:UpdateSpeed()

	arg_7_0._pos = arg_7_0._pos + arg_7_0._speed
end

function var_0_4.changeToMoveState(arg_8_0)
	arg_8_0._cruiseLimit = arg_8_0._centerPos.x
	arg_8_0.updatePatrol = arg_8_0._updateMove
end

function var_0_4._updateMove(arg_9_0, arg_9_1)
	arg_9_0:UpdateSpeed()

	arg_9_0._pos = arg_9_0._pos + arg_9_0._speed

	if arg_9_0._IFF == var_0_1.FRIENDLY_CODE then
		if arg_9_0._pos.x > arg_9_0._cruiseLimit then
			arg_9_0:changePartolState(var_0_4.HOVER_STATE)
		end
	elseif arg_9_0._IFF == var_0_1.FOE_CODE and arg_9_0._pos.x < arg_9_0._cruiseLimit then
		arg_9_0:changePartolState(var_0_4.HOVER_STATE)
	end
end

function var_0_4.changeToHoverState(arg_10_0)
	arg_10_0._hoverStartTime = pg.TimeMgr.GetInstance():GetCombatTime()
	arg_10_0.updatePatrol = arg_10_0._updateHover
end

function var_0_4._updateHover(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_1 - arg_11_0._hoverStartTime

	arg_11_0._pos = Vector3(math.sin(var_11_0) * arg_11_0._range, 15, math.cos(var_11_0) * arg_11_0._range):Add(arg_11_0._centerPos)
end

function var_0_4.GetSize(arg_12_0)
	if arg_12_0._portalState == var_0_4.HOVER_STATE then
		local var_12_0 = pg.TimeMgr.GetInstance():GetCombatTime() - arg_12_0._hoverStartTime
		local var_12_1 = math.cos(var_12_0)

		if var_12_1 > 0 and var_12_1 < 0.2 then
			var_12_1 = 0.2
		elseif var_12_1 <= 0 and var_12_1 > -0.2 then
			var_12_1 = -0.2
		end

		return var_12_1
	else
		var_0_4.super.GetSize(arg_12_0)
	end
end
