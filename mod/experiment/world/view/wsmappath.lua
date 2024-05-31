local var_0_0 = class("WSMapPath", import("...BaseEntity"))

var_0_0.Fields = {
	wsObject = "table",
	startPos = "table",
	upOffset = "number",
	theme = "table",
	moveAction = "string",
	path = "table",
	twId = "number",
	paused = "boolean",
	dirType = "number",
	step = "number"
}
var_0_0.EventStartTrip = "WSMapPath.EventStartTrip"
var_0_0.EventArrivedStep = "WSMapPath.EventArrivedStep"
var_0_0.EventArrived = "WSMapPath.EventArrived"

function var_0_0.Setup(arg_1_0, arg_1_1)
	arg_1_0.theme = arg_1_1
end

function var_0_0.Dispose(arg_2_0)
	if arg_2_0.twId then
		LeanTween.cancel(arg_2_0.twId)
	end

	arg_2_0:Clear()
end

function var_0_0.UpdateObject(arg_3_0, arg_3_1)
	assert(arg_3_1.GetModelAngles and arg_3_1.UpdateModelAngles and arg_3_1.UpdateModelAction)

	arg_3_0.wsObject = arg_3_1
end

function var_0_0.UpdateAction(arg_4_0, arg_4_1)
	arg_4_0.moveAction = arg_4_1
end

function var_0_0.UpdateDirType(arg_5_0, arg_5_1)
	arg_5_0.dirType = arg_5_1
end

function var_0_0.StartMove(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	arg_6_0.startPos = arg_6_1
	arg_6_0.path = arg_6_2
	arg_6_0.upOffset = arg_6_3 or 0
	arg_6_0.step = 0
	arg_6_0.wsObject.isMoving = true

	arg_6_0.wsObject:UpdateModelAction(arg_6_0.moveAction)
	arg_6_0:DispatchEvent(var_0_0.EventStartTrip)
	arg_6_0:MoveStep()
end

function var_0_0.MoveStep(arg_7_0)
	local var_7_0 = arg_7_0.wsObject
	local var_7_1 = arg_7_0.path
	local var_7_2 = arg_7_0.step > 0 and var_7_1[arg_7_0.step] or arg_7_0.startPos
	local var_7_3 = var_7_1[arg_7_0.step + 1]
	local var_7_4 = var_7_1[#var_7_1]
	local var_7_5 = var_7_0:GetModelAngles()

	if arg_7_0.dirType == WorldConst.DirType4 then
		if var_7_3.column < var_7_2.column then
			var_7_5.z = 180
		elseif var_7_3.column > var_7_2.column then
			var_7_5.z = 0
		elseif var_7_3.row < var_7_2.row then
			var_7_5.z = 90
		elseif var_7_3.row > var_7_2.row then
			var_7_5.z = 270
		end

		var_7_0:UpdateModelAngles(var_7_5)
	elseif arg_7_0.dirType == WorldConst.DirType2 then
		if var_7_3.column < var_7_2.column or var_7_3.column == var_7_2.column and var_7_4.column < var_7_2.column then
			var_7_5.y = 180
		elseif var_7_3.column ~= var_7_2.column or var_7_4.column ~= var_7_2.column then
			var_7_5.y = 0
		end

		var_7_0:UpdateModelAngles(var_7_5)
	end

	local var_7_6 = arg_7_0.theme:GetLinePosition(var_7_2.row, var_7_2.column)
	local var_7_7 = arg_7_0.theme:GetLinePosition(var_7_3.row, var_7_3.column)

	assert(var_7_3.duration, "without move duration")

	arg_7_0.twId = LeanTween.value(var_7_0.transform.gameObject, 0, 1, var_7_3.duration):setOnUpdate(System.Action_float(function(arg_8_0)
		local var_8_0 = Vector3.Lerp(var_7_6, var_7_7, arg_8_0)
		local var_8_1, var_8_2 = arg_7_0:CalcUpOffset(arg_7_0.step, arg_8_0)

		var_7_0.transform.localPosition = var_8_0 + var_8_1

		if var_7_0.rtShadow then
			var_7_0.rtShadow.localPosition = Vector3(0, -var_8_2, 0)
		end
	end)):setOnComplete(System.Action(function()
		arg_7_0.step = arg_7_0.step + 1

		if arg_7_0.step >= #var_7_1 then
			arg_7_0.twId = nil

			var_7_0:UpdateModelAction(WorldConst.ActionIdle)

			var_7_0.isMoving = false

			arg_7_0:DispatchEvent(var_0_0.EventArrived)
		else
			arg_7_0:DispatchEvent(var_0_0.EventArrivedStep, var_7_3)
			onDelayTick(function()
				arg_7_0:MoveStep()
			end, 0.015)
		end
	end)).uniqueId

	arg_7_0:FlushPaused()
end

function var_0_0.UpdatePaused(arg_11_0, arg_11_1)
	if arg_11_0.paused ~= arg_11_1 then
		arg_11_0.paused = arg_11_1

		arg_11_0:FlushPaused()
	end
end

function var_0_0.FlushPaused(arg_12_0)
	if arg_12_0.paused then
		LeanTween.pause(arg_12_0.twId)
		arg_12_0.wsObject:UpdateModelAction(WorldConst.ActionIdle)
	else
		LeanTween.resume(arg_12_0.twId)
		arg_12_0.wsObject:UpdateModelAction(arg_12_0.moveAction)
	end
end

function var_0_0.CalcUpOffset(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0 = math.sin((arg_13_1 + arg_13_2) / #arg_13_0.path * math.pi)
	local var_13_1 = math.clamp(var_13_0, 0, 1) * arg_13_0.upOffset

	return Vector3(0, arg_13_0.theme.cosAngle * var_13_1, -arg_13_0.theme.sinAngle * var_13_1), var_13_1
end

function var_0_0.IsMoving(arg_14_0)
	return arg_14_0.twId ~= nil
end

return var_0_0
