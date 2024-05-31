ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleEvent
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = var_0_0.Battle.BattleConfig
local var_0_5 = var_0_0.Battle.BattleDataFunction
local var_0_6 = var_0_0.Battle.BattleAttr
local var_0_7 = var_0_0.Battle.BattleVariable
local var_0_8 = var_0_0.Battle.BattleTargetChoise
local var_0_9 = class("BattleIndieSonar")

var_0_0.Battle.BattleIndieSonar = var_0_9
var_0_9.__name = "BattleIndieSonar"

function var_0_9.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0._fleetVO = arg_1_1
	arg_1_0._range = 180
	arg_1_0._duration = arg_1_3
end

function var_0_9.SwitchHost(arg_2_0, arg_2_1)
	arg_2_0._host = arg_2_1
end

function var_0_9.Detect(arg_3_0)
	arg_3_0._snoarStartTime = pg.TimeMgr.GetInstance():GetCombatTime()

	local var_3_0 = arg_3_0:FilterTarget()

	for iter_3_0, iter_3_1 in ipairs(var_3_0) do
		iter_3_1:Detected(arg_3_0._duration)
	end

	arg_3_0._detectedList = var_3_0

	arg_3_0._fleetVO:DispatchSonarScan(true)
end

function var_0_9.Update(arg_4_0, arg_4_1)
	if arg_4_1 > arg_4_0._snoarStartTime + arg_4_0._duration then
		arg_4_0._detectedList = nil

		arg_4_0._fleetVO:RemoveIndieSonar(arg_4_0)
	end
end

function var_0_9.FilterTarget(arg_5_0)
	local var_5_0 = var_0_8.LegalTarget(arg_5_0._host)

	return (var_0_8.TargetDiveState(arg_5_0._host, {
		diveState = var_0_3.OXY_STATE.DIVE
	}, var_5_0))
end
