ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CardPuzzleMoveState = class("CardPuzzleMoveState")

local var_0_3 = var_0_0.Battle.CardPuzzleMoveState

var_0_3.__name = "CardPuzzleMoveState"
var_0_3.STATE_MOVE = "STATE_MOVE"
var_0_3.STATE_STAY = "STATE_STAY"
var_0_3.STATE_RANDOM = "STATE_RANDOM"

function var_0_3.Ctor(arg_1_0, arg_1_1)
	arg_1_0._fleet = arg_1_1
	arg_1_0._fleetMotion = arg_1_1:GetMotion()
	arg_1_0._moveToState = var_0_0.Battle.CardPuzzleMoveToState.New()
	arg_1_0._stayState = var_0_0.Battle.CardPuzzleStayState.New()
	arg_1_0._RandomState = var_0_0.Battle.CardPuzzleRandomState.New()

	arg_1_0:OnStayState()
end

function var_0_3.SetReferencePoint(arg_2_0, arg_2_1)
	arg_2_0._currentReferencePoint = arg_2_1
end

function var_0_3.ChangeState(arg_3_0, arg_3_1)
	local var_3_0 = var_0_0.Battle.CardPuzzleIMoveState.ADD_STATE_TABLE[arg_3_1]

	arg_3_0._currentState[var_3_0](arg_3_0._currentState, arg_3_0)
end

function var_0_3.Update(arg_4_0)
	arg_4_0._currentState:Update()

	if arg_4_0._currentState:IsFinish(arg_4_0) then
		if arg_4_0._currentState == arg_4_0._moveToState then
			arg_4_0._callback()

			arg_4_0._callback = nil
		end

		local var_4_0 = arg_4_0._currentState:NextState()

		arg_4_0:ChangeState(var_4_0)
	end
end

function var_0_3.FinishCallback(arg_5_0, arg_5_1)
	arg_5_0._callback = arg_5_1
end

function var_0_3.GetFleetPosition(arg_6_0)
	return arg_6_0._fleetMotion:GetPos()
end

function var_0_3.GetDistance(arg_7_0)
	return arg_7_0._currentReferencePoint - arg_7_0:GetFleetPosition()
end

function var_0_3.GetDirection(arg_8_0)
	local var_8_0, var_8_1 = arg_8_0._currentState:GetOutput(arg_8_0)

	return var_8_0, var_8_1
end

function var_0_3.GetStateChangeTimeStamp(arg_9_0)
	return arg_9_0._stateChangeTimeStamp
end

function var_0_3.OnMoveToState(arg_10_0)
	arg_10_0._currentState = arg_10_0._moveToState

	arg_10_0:HandleStateChange()
end

function var_0_3.OnRandomState(arg_11_0)
	arg_11_0._currentState = arg_11_0._RandomState

	arg_11_0:HandleStateChange()
end

function var_0_3.OnStayState(arg_12_0)
	arg_12_0._currentState = arg_12_0._stayState

	arg_12_0:HandleStateChange()
end

function var_0_3.HandleStateChange(arg_13_0)
	arg_13_0._stateChangeTimeStamp = pg.TimeMgr.GetInstance():GetCombatTime()

	arg_13_0._currentState:IntputReferencePoint(arg_13_0._currentReferencePoint or arg_13_0:GetFleetPosition())
end
