﻿local var_0_0 = class("CourtYardMoveableFurniture", import(".CourtYardFurniture"))
local var_0_1 = 0
local var_0_2 = 1
local var_0_3 = 2
local var_0_4 = 3

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.moveState = var_0_1
end

function var_0_0.IsCar(arg_2_0)
	if arg_2_0.config.spine then
		local var_2_0 = arg_2_0.config.spine[1]

		return var_2_0 and var_2_0[4] ~= nil
	end

	return false
end

function var_0_0.GetAroundPositions(arg_3_0)
	local var_3_0 = var_0_0.super.GetAroundPositions(arg_3_0)

	if not arg_3_0:IsCar() then
		return var_3_0
	end

	local var_3_1 = arg_3_0.config.spine[1][4]

	if type(var_3_1) == "table" then
		local var_3_2 = {}

		for iter_3_0, iter_3_1 in ipairs(var_3_0) do
			if table.contains(var_3_1, iter_3_0) then
				table.insert(var_3_2, iter_3_1)
			end
		end

		return var_3_2
	else
		return var_3_0
	end
end

function var_0_0.ChangeState(arg_4_0, arg_4_1)
	var_0_0.super.ChangeState(arg_4_0, arg_4_1)

	if arg_4_0:IsTouchState() then
		arg_4_0:ChangeMoveState(var_0_2)
	elseif arg_4_0:IsMoving() then
		arg_4_0:Idle()
	end
end

function var_0_0.IsMoveableSlot(arg_5_0, arg_5_1)
	return arg_5_1.id == 1
end

function var_0_0.IsReadyMove(arg_6_0)
	return arg_6_0.moveState == var_0_2
end

function var_0_0.IsMoving(arg_7_0)
	return arg_7_0.moveState == var_0_3
end

function var_0_0.IsStop(arg_8_0)
	return arg_8_0.moveState == var_0_4
end

function var_0_0.SetPosition(arg_9_0, arg_9_1)
	if arg_9_0.moveState == var_0_3 then
		var_0_0.super.super.SetPosition(arg_9_0, arg_9_1)
	else
		var_0_0.super.SetPosition(arg_9_0, arg_9_1)
	end
end

function var_0_0.GetSpeed(arg_10_0)
	local var_10_0 = 1

	if arg_10_0.config.spine and arg_10_0.config.spine[7] then
		var_10_0 = arg_10_0.config.spine[7]
	end

	return var_10_0
end

function var_0_0.GetMoveTime(arg_11_0)
	return 1 / arg_11_0:GetSpeed()
end

function var_0_0.Move(arg_12_0, arg_12_1)
	arg_12_0:RemoveTimer()
	arg_12_0:ChangeMoveState(var_0_3)

	local var_12_0 = arg_12_0:GetMoveTime()

	arg_12_0.moveTimer = Timer.New(function()
		arg_12_0:ChangeMoveState(var_0_2)
	end, var_12_0, 1)

	arg_12_0.moveTimer:Start()
	arg_12_0:DispatchEvent(CourtYardEvent.FURNITURE_MOVE, arg_12_1)
end

function var_0_0.Rest(arg_14_0)
	arg_14_0:RemoveTimer()
	arg_14_0:ChangeMoveState(var_0_1)

	local var_14_0 = math.random(1)

	arg_14_0.moveTimer = Timer.New(function()
		arg_14_0:ChangeMoveState(var_0_2)
	end, math.random(10, 20), 1)

	arg_14_0.moveTimer:Start()
end

function var_0_0.Idle(arg_16_0)
	arg_16_0:RemoveTimer()
	arg_16_0:ChangeMoveState(var_0_1)
	arg_16_0:SetPosition(arg_16_0:GetPosition())
	arg_16_0:DispatchEvent(CourtYardEvent.FURNITURE_STOP_MOVE)
end

function var_0_0.Stop(arg_17_0)
	arg_17_0:RemoveTimer()
	arg_17_0:ChangeMoveState(var_0_4)
	arg_17_0:SetPosition(arg_17_0:GetPosition())
	arg_17_0:DispatchEvent(CourtYardEvent.FURNITURE_STOP_MOVE)
end

function var_0_0.ReStart(arg_18_0)
	arg_18_0:ChangeMoveState(var_0_2)
end

function var_0_0.ChangeMoveState(arg_19_0, arg_19_1)
	arg_19_0.moveState = arg_19_1
end

function var_0_0.StartInteraction(arg_20_0, arg_20_1)
	var_0_0.super.StartInteraction(arg_20_0, arg_20_1)

	if arg_20_0:IsMoveableSlot(arg_20_1) then
		arg_20_0:ChangeMoveState(var_0_2)
	end
end

function var_0_0.ClearInteraction(arg_21_0, arg_21_1)
	var_0_0.super.ClearInteraction(arg_21_0, arg_21_1)

	if arg_21_0:IsMoveableSlot(arg_21_1) then
		arg_21_0:Idle()
	end
end

function var_0_0.RemoveTimer(arg_22_0)
	if arg_22_0.moveTimer then
		arg_22_0.moveTimer:Stop()

		arg_22_0.moveTimer = nil
	end
end

function var_0_0.IsDifferentDirectionForCard(arg_23_0, arg_23_1)
	local var_23_0 = arg_23_0:GetPosition()
	local var_23_1 = arg_23_0.config.dir == 1 and {
		1,
		2
	} or {
		2,
		1
	}
	local var_23_2

	if arg_23_1.x > var_23_0.x then
		var_23_2 = var_23_1[1]
	elseif arg_23_1.y > var_23_0.y then
		var_23_2 = var_23_1[2]
	else
		var_23_2 = (arg_23_1.x < var_23_0.x and arg_23_1.y == var_23_0.y or arg_23_1.y > var_23_0.y and arg_23_1.x == var_23_0.x) and var_23_1[1] or var_23_1[2]
	end

	return arg_23_0.dir ~= var_23_2
end

function var_0_0.IsDifferentDirection(arg_24_0, arg_24_1)
	if arg_24_0:IsCar() then
		return arg_24_0:IsDifferentDirectionForCard(arg_24_1)
	else
		return var_0_0.super.IsDifferentDirection(arg_24_0, arg_24_1)
	end
end

function var_0_0.Dispose(arg_25_0)
	var_0_0.super.Dispose(arg_25_0)
	arg_25_0:RemoveTimer()
end

return var_0_0