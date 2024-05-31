local var_0_0 = class("Live2dDrag")
local var_0_1 = 4

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.live2dData = arg_1_2
	arg_1_0.frameRate = Application.targetFrameRate or 60
	arg_1_0.id = arg_1_1.id
	arg_1_0.drawAbleName = arg_1_1.draw_able_name or ""
	arg_1_0.parameterName = arg_1_1.parameter
	arg_1_0.mode = arg_1_1.mode
	arg_1_0.startValue = arg_1_1.start_value or 0
	arg_1_0.range = arg_1_1.range
	arg_1_0.offsetX = arg_1_1.offset_x

	if arg_1_0.offsetX == 0 then
		arg_1_0.offsetX = nil
	end

	arg_1_0.offsetY = arg_1_1.offset_y

	if arg_1_0.offsetY == 0 then
		arg_1_0.offsetY = nil
	end

	arg_1_0.smooth = arg_1_1.smooth / 1000
	arg_1_0.smoothRevert = arg_1_1.revert_smooth / 1000
	arg_1_0.revert = arg_1_1.revert
	arg_1_0.ignoreReact = arg_1_1.ignore_react == 1
	arg_1_0.gyro = arg_1_1.gyro == 1 or nil
	arg_1_0.gyroX = arg_1_1.gyro_x == 1
	arg_1_0.gyroY = arg_1_1.gyro_y == 1
	arg_1_0.gyroZ = arg_1_1.gyro_z == 1
	arg_1_0.ignoreAction = arg_1_1.ignore_action == 1
	arg_1_0.dragDirect = arg_1_1.drag_direct
	arg_1_0.rangeAbs = arg_1_1.range_abs == 1
	arg_1_0.partsData = arg_1_1.parts_data
	arg_1_0.actionTrigger = arg_1_1.action_trigger
	arg_1_0.reactX = arg_1_1.react_pos_x ~= 0 and arg_1_1.react_pos_x or nil
	arg_1_0.reactY = arg_1_1.react_pos_y ~= 0 and arg_1_1.react_pos_y or nil
	arg_1_0.actionTriggerActive = arg_1_1.action_trigger_active
	arg_1_0.relationParameter = arg_1_1.relation_parameter
	arg_1_0.limitTime = arg_1_1.limit_time > 0 and arg_1_1.limit_time or var_0_1
	arg_1_0.reactCondition = arg_1_1.react_condition and arg_1_1.react_condition ~= "" and arg_1_1.react_condition or {}
	arg_1_0.idleOn = arg_1_0.reactCondition.idle_on and arg_1_0.reactCondition.idle_on or {}
	arg_1_0.idleOff = arg_1_0.reactCondition.idleOff and arg_1_0.reactCondition.idleOff or {}
	arg_1_0.revertIdleIndex = arg_1_1.revert_idle_index == 1 and true or false
	arg_1_0.revertActionIndex = arg_1_1.revert_action_index == 1 and true or false
	arg_1_0.saveParameterFlag = true

	if arg_1_1.save_parameter == -1 then
		arg_1_0.saveParameterFlag = false
	end

	arg_1_0.randomAttitudeIndex = L2D_RANDOM_PARAM
	arg_1_0._active = false
	arg_1_0._parameterCom = nil
	arg_1_0.parameterValue = arg_1_0.startValue
	arg_1_0.parameterTargetValue = arg_1_0.startValue
	arg_1_0.parameterSmooth = 0
	arg_1_0.parameterSmoothTime = arg_1_0.smooth
	arg_1_0.mouseInputDown = Vector2(0, 0)
	arg_1_0.nextTriggerTime = 0
	arg_1_0.triggerActionTime = 0
	arg_1_0.sensitive = 4
	arg_1_0.l2dIdleIndex = 0
	arg_1_0.reactPos = Vector2(0, 0)
	arg_1_0.actionListIndex = 1
	arg_1_0._relationParameterList = {}
	arg_1_0.offsetDragX = arg_1_0.startValue
	arg_1_0.offsetDragY = arg_1_0.startValue
	arg_1_0.offsetDragTargetX = arg_1_0.startValue
	arg_1_0.offsetDragTargetY = arg_1_0.startValue
	arg_1_0.parameterComAdd = true
	arg_1_0.reactConditionFlag = false
end

function var_0_0.startDrag(arg_2_0)
	if arg_2_0.ignoreAction and arg_2_0.l2dIsPlaying then
		return
	end

	if not arg_2_0._active then
		arg_2_0._active = true
		arg_2_0.mouseInputDown = Input.mousePosition
		arg_2_0.mouseInputDownTime = Time.time
		arg_2_0.triggerActionTime = 0

		if arg_2_0.actionTrigger.type == Live2D.DRAG_DOWN_ACTION then
			arg_2_0.actionListIndex = 1
		end

		arg_2_0.parameterSmoothTime = arg_2_0.smooth
	end
end

function var_0_0.stopDrag(arg_3_0)
	if arg_3_0._active then
		arg_3_0._active = false

		if arg_3_0.revert > 0 then
			arg_3_0.parameterToStart = arg_3_0.revert / 1000
			arg_3_0.parameterSmoothTime = arg_3_0.smoothRevert
		end

		if arg_3_0.offsetDragX then
			arg_3_0.offsetDragTargetX = arg_3_0:fixParameterTargetValue(arg_3_0.offsetDragX, arg_3_0.range, arg_3_0.rangeAbs, arg_3_0.dragDirect)
		end

		if arg_3_0.offsetDragY then
			arg_3_0.offsetDragTargetY = arg_3_0:fixParameterTargetValue(arg_3_0.offsetDragY, arg_3_0.range, arg_3_0.rangeAbs, arg_3_0.dragDirect)
		end

		if type(arg_3_0.partsData) == "table" then
			local var_3_0 = arg_3_0.partsData.parts

			if arg_3_0.offsetX or arg_3_0.offsetY then
				local var_3_1 = arg_3_0.parameterTargetValue
				local var_3_2
				local var_3_3

				for iter_3_0 = 1, #var_3_0 do
					local var_3_4 = var_3_0[iter_3_0]
					local var_3_5 = math.abs(var_3_1 - var_3_4)

					if not var_3_2 or var_3_5 < var_3_2 then
						var_3_2 = var_3_5
						var_3_3 = iter_3_0
					end
				end

				if var_3_3 then
					arg_3_0:setTargetValue(var_3_0[var_3_3])
				end
			end
		end

		arg_3_0.mouseInputUp = Input.mousePosition
		arg_3_0.mouseInputUpTime = Time.time

		arg_3_0:saveData()
	end
end

function var_0_0.getIgnoreReact(arg_4_0)
	return arg_4_0.ignoreReact
end

function var_0_0.setParameterCom(arg_5_0, arg_5_1)
	if not arg_5_1 then
		print("live2dDrag id:" .. tostring(arg_5_0.id) .. "设置了null的组件(该打印非报错)")
	end

	arg_5_0._parameterCom = arg_5_1
end

function var_0_0.getParameterCom(arg_6_0)
	return arg_6_0._parameterCom
end

function var_0_0.addRelationComData(arg_7_0, arg_7_1, arg_7_2)
	table.insert(arg_7_0._relationParameterList, {
		com = arg_7_1,
		data = arg_7_2
	})
end

function var_0_0.getRelationParameterList(arg_8_0)
	return arg_8_0._relationParameterList
end

function var_0_0.getReactCondition(arg_9_0)
	return arg_9_0.reactConditionFlag
end

function var_0_0.getActive(arg_10_0)
	return arg_10_0._active
end

function var_0_0.getParameterUpdateFlag(arg_11_0)
	return arg_11_0._parameterUpdateFlag
end

function var_0_0.setEventCallback(arg_12_0, arg_12_1)
	arg_12_0._eventCallback = arg_12_1
end

function var_0_0.onEventCallback(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	if arg_13_1 == Live2D.EVENT_ACTION_APPLY then
		local var_13_0 = {}
		local var_13_1
		local var_13_2 = false
		local var_13_3
		local var_13_4
		local var_13_5

		if arg_13_0.actionTrigger.action then
			var_13_1 = arg_13_0:fillterAction(arg_13_0.actionTrigger.action)
			var_13_0 = arg_13_0.actionTriggerActive
			var_13_2 = arg_13_0.actionTrigger.focus or false
			var_13_3 = arg_13_0.actionTrigger.target or nil

			if (arg_13_0.actionTrigger.circle or nil) and var_13_3 and var_13_3 == arg_13_0.parameterTargetValue then
				var_13_3 = arg_13_0.startValue
			end

			var_13_4 = arg_13_0.actionTrigger.react or nil

			arg_13_0:triggerAction()
			arg_13_0:stopDrag()
		elseif arg_13_0.actionTrigger.action_list then
			local var_13_6 = arg_13_0.actionTrigger.action_list[arg_13_0.actionListIndex]

			var_13_1 = arg_13_0:fillterAction(var_13_6.action)

			if arg_13_0.actionTriggerActive.active_list and arg_13_0.actionListIndex <= #arg_13_0.actionTriggerActive.active_list then
				var_13_0 = arg_13_0.actionTriggerActive.active_list[arg_13_0.actionListIndex]
			end

			var_13_2 = var_13_6.focus or true
			var_13_3 = var_13_6.target or nil
			var_13_4 = var_13_6.react or nil

			if arg_13_0.actionListIndex == #arg_13_0.actionTrigger.action_list then
				arg_13_0:triggerAction()
				arg_13_0:stopDrag()

				arg_13_0.actionListIndex = 1
			else
				arg_13_0.actionListIndex = arg_13_0.actionListIndex + 1
			end

			print("id = " .. arg_13_0.id .. " action list index = " .. arg_13_0.actionListIndex)
		elseif not arg_13_0.actionTrigger.action then
			var_13_1 = arg_13_0:fillterAction(arg_13_0.actionTrigger.action)
			var_13_0 = arg_13_0.actionTriggerActive
			var_13_2 = arg_13_0.actionTrigger.focus or false
			var_13_3 = arg_13_0.actionTrigger.target or nil

			if (arg_13_0.actionTrigger.circle or nil) and var_13_3 and var_13_3 == arg_13_0.parameterTargetValue then
				var_13_3 = arg_13_0.startValue
			end

			var_13_4 = arg_13_0.actionTrigger.react or nil

			arg_13_0:triggerAction()
			arg_13_0:stopDrag()
		end

		if var_13_0.idle then
			if type(var_13_0.idle) == "number" then
				if var_13_0.idle == arg_13_0.l2dIdleIndex and not var_13_0.repeatFlag then
					return
				end
			elseif type(var_13_0.idle) == "table" and #var_13_0.idle == 1 and var_13_0.idle[1] == arg_13_0.l2dIdleIndex and not var_13_0.repeatFlag then
				return
			end
		end

		if var_13_3 then
			arg_13_0:setTargetValue(var_13_3)

			if not var_13_1 then
				arg_13_0.revertResetFlag = true
			end
		end

		arg_13_2 = {
			id = arg_13_0.id,
			action = var_13_1,
			activeData = var_13_0,
			focus = var_13_2,
			react = var_13_4,
			function()
				arg_13_0:actionApplyFinish()
			end
		}
	elseif arg_13_1 == Live2D.EVENT_ACTION_ABLE then
		-- block empty
	end

	arg_13_0._eventCallback(arg_13_1, arg_13_2, arg_13_3)
end

function var_0_0.fillterAction(arg_15_0, arg_15_1)
	if type(arg_15_1) == "table" then
		return arg_15_1[math.random(1, #arg_15_0.actionTrigger.action)]
	else
		return arg_15_1
	end
end

function var_0_0.setTargetValue(arg_16_0, arg_16_1)
	arg_16_0.parameterTargetValue = arg_16_1
end

function var_0_0.getParameter(arg_17_0)
	return arg_17_0.parameterValue
end

function var_0_0.getParameToTargetFlag(arg_18_0)
	if arg_18_0.parameterValue ~= arg_18_0.parameterTargetValue then
		return true
	end

	if arg_18_0.parameterToStart and arg_18_0.parameterToStart > 0 then
		return true
	end

	return false
end

function var_0_0.actionApplyFinish(arg_19_0)
	return
end

function var_0_0.stepParameter(arg_20_0)
	arg_20_0:updateState()
	arg_20_0:updateTrigger()
	arg_20_0:updateParameterUpdateFlag()
	arg_20_0:updateGyro()
	arg_20_0:updateDrag()
	arg_20_0:updateReactValue()
	arg_20_0:updateParameterValue()
	arg_20_0:updateRelationValue()
	arg_20_0:checkReset()
end

function var_0_0.updateParameterUpdateFlag(arg_21_0)
	if arg_21_0.actionTrigger.type == Live2D.DRAG_CLICK_ACTION then
		arg_21_0._parameterUpdateFlag = true
	elseif arg_21_0.actionTrigger.type == Live2D.DRAG_RELATION_IDLE then
		if not arg_21_0._parameterUpdateFlag then
			if not arg_21_0.l2dIsPlaying then
				arg_21_0._parameterUpdateFlag = true

				arg_21_0:changeParameComAble(true)
			elseif not table.contains(arg_21_0.actionTrigger.remove_com_list, arg_21_0.l2dPlayActionName) then
				arg_21_0._parameterUpdateFlag = true

				arg_21_0:changeParameComAble(true)
			end
		elseif arg_21_0._parameterUpdateFlag == true and arg_21_0.l2dIsPlaying and table.contains(arg_21_0.actionTrigger.remove_com_list, arg_21_0.l2dPlayActionName) then
			arg_21_0._parameterUpdateFlag = false

			arg_21_0:changeParameComAble(false)
		end
	else
		arg_21_0._parameterUpdateFlag = false
	end
end

function var_0_0.changeParameComAble(arg_22_0, arg_22_1)
	if arg_22_0.parameterComAdd == arg_22_1 then
		return
	end

	arg_22_0.parameterComAdd = arg_22_1

	if arg_22_1 then
		arg_22_0:onEventCallback(Live2D.EVENT_ADD_PARAMETER_COM, {
			com = arg_22_0._parameterCom,
			start = arg_22_0.startValue,
			mode = arg_22_0.mode
		})
	else
		arg_22_0:onEventCallback(Live2D.EVENT_REMOVE_PARAMETER_COM, {
			com = arg_22_0._parameterCom,
			mode = arg_22_0.mode
		})
	end
end

function var_0_0.updateDrag(arg_23_0)
	if not arg_23_0.offsetX and not arg_23_0.offsetY then
		return
	end

	local var_23_0

	if arg_23_0._active then
		local var_23_1 = Input.mousePosition

		if arg_23_0.offsetX and arg_23_0.offsetX ~= 0 then
			local var_23_2 = var_23_1.x - arg_23_0.mouseInputDown.x

			var_23_0 = arg_23_0.offsetDragTargetX + var_23_2 / arg_23_0.offsetX
			arg_23_0.offsetDragX = var_23_0
		end

		if arg_23_0.offsetY and arg_23_0.offsetY ~= 0 then
			local var_23_3 = var_23_1.y - arg_23_0.mouseInputDown.y

			var_23_0 = arg_23_0.offsetDragTargetY + var_23_3 / arg_23_0.offsetY
			arg_23_0.offsetDragY = var_23_0
		end

		if var_23_0 then
			arg_23_0:setTargetValue(arg_23_0:fixParameterTargetValue(var_23_0, arg_23_0.range, arg_23_0.rangeAbs, arg_23_0.dragDirect))
		end
	end

	arg_23_0._parameterUpdateFlag = true
end

function var_0_0.updateGyro(arg_24_0)
	if not arg_24_0.gyro then
		return
	end

	if not Input.gyro.enabled then
		arg_24_0:setTargetValue(0)

		arg_24_0._parameterUpdateFlag = true

		return
	end

	local var_24_0 = Input.gyro and Input.gyro.attitude or Vector3.zero
	local var_24_1 = 0

	if arg_24_0.gyroX and not math.isnan(var_24_0.y) then
		var_24_1 = Mathf.Clamp(var_24_0.y * arg_24_0.sensitive, -0.5, 0.5)
	elseif arg_24_0.gyroY and not math.isnan(var_24_0.x) then
		var_24_1 = Mathf.Clamp(var_24_0.x * arg_24_0.sensitive, -0.5, 0.5)
	elseif arg_24_0.gyroZ and not math.isnan(var_24_0.z) then
		var_24_1 = Mathf.Clamp(var_24_0.z * arg_24_0.sensitive, -0.5, 0.5)
	end

	if IsUnityEditor then
		if L2D_USE_RANDOM_ATTI then
			if arg_24_0.randomAttitudeIndex == 0 then
				var_24_1 = math.random() - 0.5

				local var_24_2 = (var_24_1 + 0.5) * (arg_24_0.range[2] - arg_24_0.range[1]) + arg_24_0.range[1]

				arg_24_0:setTargetValue(var_24_2)

				arg_24_0.randomAttitudeIndex = L2D_RANDOM_PARAM
			elseif arg_24_0.randomAttitudeIndex > 0 then
				arg_24_0.randomAttitudeIndex = arg_24_0.randomAttitudeIndex - 1
			end
		end
	else
		local var_24_3 = (var_24_1 + 0.5) * (arg_24_0.range[2] - arg_24_0.range[1]) + arg_24_0.range[1]

		arg_24_0:setTargetValue(var_24_3)
	end

	arg_24_0._parameterUpdateFlag = true
end

function var_0_0.updateReactValue(arg_25_0)
	if not arg_25_0.reactX and not arg_25_0.reactY then
		return
	end

	local var_25_0
	local var_25_1 = false

	if arg_25_0.l2dIgnoreReact then
		var_25_0 = arg_25_0.parameterTargetValue
	elseif arg_25_0.reactX then
		var_25_0 = arg_25_0.reactPos.x * arg_25_0.reactX
		var_25_1 = true
	else
		var_25_0 = arg_25_0.reactPos.y * arg_25_0.reactY
		var_25_1 = true
	end

	if var_25_1 then
		arg_25_0:setTargetValue(arg_25_0:fixParameterTargetValue(var_25_0, arg_25_0.range, arg_25_0.rangeAbs, arg_25_0.dragDirect))
	end

	arg_25_0._parameterUpdateFlag = true
end

function var_0_0.updateParameterValue(arg_26_0)
	if arg_26_0._parameterUpdateFlag and arg_26_0.parameterValue ~= arg_26_0.parameterTargetValue then
		if math.abs(arg_26_0.parameterValue - arg_26_0.parameterTargetValue) < 0.01 then
			arg_26_0:setParameterValue(arg_26_0.parameterTargetValue)
		elseif arg_26_0.parameterSmoothTime and arg_26_0.parameterSmoothTime > 0 then
			local var_26_0, var_26_1 = Mathf.SmoothDamp(arg_26_0.parameterValue, arg_26_0.parameterTargetValue, arg_26_0.parameterSmooth, arg_26_0.parameterSmoothTime)

			arg_26_0:setParameterValue(var_26_0, var_26_1)
		else
			arg_26_0:setParameterValue(arg_26_0.parameterTargetValue, 0)
		end
	end
end

function var_0_0.updateRelationValue(arg_27_0)
	for iter_27_0, iter_27_1 in ipairs(arg_27_0._relationParameterList) do
		local var_27_0 = iter_27_1.data
		local var_27_1 = var_27_0.type
		local var_27_2 = var_27_0.relation_value
		local var_27_3
		local var_27_4
		local var_27_5

		if var_27_1 == Live2D.relation_type_drag_x then
			var_27_3 = arg_27_0.offsetDragX or iter_27_1.start or arg_27_0.startValue or 0
			var_27_5 = true
		elseif var_27_1 == Live2D.relation_type_drag_y then
			var_27_3 = arg_27_0.offsetDragY or iter_27_1.start or arg_27_0.startValue or 0
			var_27_5 = true
		elseif var_27_1 == Live2D.relation_type_action_index then
			var_27_3 = var_27_2[arg_27_0.actionListIndex]
			var_27_3 = var_27_3 or 0
			var_27_5 = true
		else
			var_27_3 = arg_27_0.parameterTargetValue
			var_27_5 = false
		end

		local var_27_6 = iter_27_1.value or arg_27_0.startValue
		local var_27_7 = arg_27_0:fixRelationParameter(var_27_3, var_27_0)
		local var_27_8 = iter_27_1.parameterSmooth or 0
		local var_27_9 = 0.1
		local var_27_10, var_27_11 = Mathf.SmoothDamp(var_27_6, var_27_7, var_27_8, var_27_9)

		iter_27_1.value = var_27_10
		iter_27_1.parameterSmooth = var_27_11
		iter_27_1.enable = var_27_5
		iter_27_1.comId = arg_27_0.id
	end
end

function var_0_0.fixRelationParameter(arg_28_0, arg_28_1, arg_28_2)
	local var_28_0 = arg_28_2.range or arg_28_0.range
	local var_28_1 = arg_28_2.rangeAbs and arg_28_2.rangeAbs == 1 or arg_28_0.rangeAbs
	local var_28_2 = arg_28_2.dragDirect and arg_28_2.dragDirect or arg_28_0.dragDirect

	return arg_28_0:fixParameterTargetValue(arg_28_1, var_28_0, var_28_1, var_28_2)
end

function var_0_0.fixParameterTargetValue(arg_29_0, arg_29_1, arg_29_2, arg_29_3, arg_29_4)
	if arg_29_1 < 0 and arg_29_4 == 1 then
		arg_29_1 = 0
	elseif arg_29_1 > 0 and arg_29_4 == 2 then
		arg_29_1 = 0
	end

	arg_29_1 = arg_29_3 and math.abs(arg_29_1) or arg_29_1

	if arg_29_1 < arg_29_2[1] then
		arg_29_1 = arg_29_2[1]
	elseif arg_29_1 > arg_29_2[2] then
		arg_29_1 = arg_29_2[2]
	end

	return arg_29_1
end

function var_0_0.checkReset(arg_30_0)
	if not arg_30_0._active and arg_30_0.parameterToStart then
		if arg_30_0.parameterToStart > 0 then
			arg_30_0.parameterToStart = arg_30_0.parameterToStart - Time.deltaTime
		end

		if arg_30_0.parameterToStart <= 0 then
			arg_30_0:setTargetValue(arg_30_0.startValue)

			arg_30_0.parameterToStart = nil

			if arg_30_0.revertResetFlag then
				arg_30_0:setTriggerActionFlag(false)

				arg_30_0.revertResetFlag = false
			end

			if arg_30_0.offsetDragX then
				arg_30_0.offsetDragX = arg_30_0.startValue
				arg_30_0.offsetDragTargetX = arg_30_0.startValue
			end

			if arg_30_0.offsetDragY then
				arg_30_0.offsetDragY = arg_30_0.startValue
				arg_30_0.offsetDragTargetY = arg_30_0.startValue
			end
		end
	end
end

function var_0_0.changeReactValue(arg_31_0, arg_31_1)
	arg_31_0.reactPos = arg_31_1
end

function var_0_0.setParameterValue(arg_32_0, arg_32_1, arg_32_2)
	if arg_32_1 then
		arg_32_0.parameterValue = arg_32_1
	end

	if arg_32_2 then
		arg_32_0.parameterSmooth = arg_32_2
	end
end

function var_0_0.updateState(arg_33_0)
	if not arg_33_0.lastFrameActive and arg_33_0._active then
		arg_33_0.firstActive = true
	else
		arg_33_0.firstActive = false
	end

	if arg_33_0.lastFrameActive and not arg_33_0._active then
		arg_33_0.firstStop = true
	else
		arg_33_0.firstStop = false
	end

	arg_33_0.lastFrameActive = arg_33_0._active
end

function var_0_0.updateTrigger(arg_34_0)
	if not arg_34_0:isActionTriggerAble() then
		return
	end

	local var_34_0 = arg_34_0.actionTrigger.type
	local var_34_1 = arg_34_0.actionTrigger.action
	local var_34_2

	if arg_34_0.actionTrigger.time then
		var_34_2 = arg_34_0.actionTrigger.time
	elseif arg_34_0.actionTrigger.action_list and arg_34_0.actionListIndex > 0 then
		var_34_2 = arg_34_0.actionTrigger.action_list[arg_34_0.actionListIndex].time
	end

	local var_34_3

	if arg_34_0.actionTrigger.num then
		var_34_3 = arg_34_0.actionTrigger.num
	elseif arg_34_0.actionTrigger.action_list and arg_34_0.actionTrigger.action_list[arg_34_0.actionListIndex].num and arg_34_0.actionListIndex > 0 then
		var_34_3 = arg_34_0.actionTrigger.action_list[arg_34_0.actionListIndex].num
	end

	if var_34_0 == Live2D.DRAG_TIME_ACTION then
		if arg_34_0._active then
			if math.abs(arg_34_0.parameterValue - var_34_3) < math.abs(var_34_3) * 0.25 then
				arg_34_0.triggerActionTime = arg_34_0.triggerActionTime + Time.deltaTime

				if var_34_2 < arg_34_0.triggerActionTime and not arg_34_0.l2dIsPlaying then
					arg_34_0:onEventCallback(Live2D.EVENT_ACTION_APPLY)
				end
			else
				arg_34_0.triggerActionTime = arg_34_0.triggerActionTime + 0
			end
		end
	elseif var_34_0 == Live2D.DRAG_CLICK_ACTION then
		if arg_34_0:checkClickAction() then
			arg_34_0:onEventCallback(Live2D.EVENT_ACTION_APPLY)
		end
	elseif var_34_0 == Live2D.DRAG_DOWN_ACTION then
		if arg_34_0._active then
			if arg_34_0.firstActive then
				arg_34_0.ableFalg = true

				arg_34_0:onEventCallback(Live2D.EVENT_ACTION_ABLE, {
					ableFlag = true
				})
			end

			if var_34_2 <= Time.time - arg_34_0.mouseInputDownTime then
				arg_34_0:onEventCallback(Live2D.EVENT_ACTION_ABLE, {
					ableFlag = false
				})

				arg_34_0.ableFalg = false

				arg_34_0:onEventCallback(Live2D.EVENT_ACTION_APPLY)

				arg_34_0.mouseInputDownTime = Time.time
			end
		elseif arg_34_0.ableFalg then
			arg_34_0.ableFalg = false

			arg_34_0:onEventCallback(Live2D.EVENT_ACTION_ABLE, {
				ableFlag = false
			})
		end
	elseif var_34_0 == Live2D.DRAG_RELATION_XY then
		if arg_34_0._active then
			local var_34_4 = arg_34_0:fixParameterTargetValue(arg_34_0.offsetDragX, arg_34_0.range, arg_34_0.rangeAbs, arg_34_0.dragDirect)
			local var_34_5 = arg_34_0:fixParameterTargetValue(arg_34_0.offsetDragY, arg_34_0.range, arg_34_0.rangeAbs, arg_34_0.dragDirect)
			local var_34_6 = var_34_3[1]
			local var_34_7 = var_34_3[2]

			if math.abs(var_34_4 - var_34_6) < math.abs(var_34_6) * 0.25 and math.abs(var_34_5 - var_34_7) < math.abs(var_34_7) * 0.25 then
				arg_34_0.triggerActionTime = arg_34_0.triggerActionTime + Time.deltaTime

				if var_34_2 < arg_34_0.triggerActionTime and not arg_34_0.l2dIsPlaying then
					arg_34_0:onEventCallback(Live2D.EVENT_ACTION_APPLY)
				end
			else
				arg_34_0.triggerActionTime = arg_34_0.triggerActionTime + 0
			end
		end
	elseif var_34_0 == Live2D.DRAG_RELATION_IDLE then
		if arg_34_0.actionTrigger.const_fit then
			for iter_34_0 = 1, #arg_34_0.actionTrigger.const_fit do
				local var_34_8 = arg_34_0.actionTrigger.const_fit[iter_34_0]

				if arg_34_0.l2dIdleIndex == var_34_8.idle and not arg_34_0.l2dIsPlaying then
					arg_34_0:setTargetValue(var_34_8.target)
				end
			end
		end
	elseif var_34_0 == Live2D.DRAG_CLICK_MANY and arg_34_0:checkClickAction() then
		print("id = " .. arg_34_0.id .. "被按下了")
		arg_34_0:onEventCallback(Live2D.EVENT_ACTION_APPLY)
	end
end

function var_0_0.triggerAction(arg_35_0)
	arg_35_0.nextTriggerTime = arg_35_0.limitTime

	arg_35_0:setTriggerActionFlag(true)
end

function var_0_0.isActionTriggerAble(arg_36_0)
	if arg_36_0.actionTrigger.type == nil then
		return false
	end

	if not arg_36_0.actionTrigger or arg_36_0.actionTrigger == "" then
		return
	end

	if arg_36_0.nextTriggerTime - Time.deltaTime >= 0 then
		arg_36_0.nextTriggerTime = arg_36_0.nextTriggerTime - Time.deltaTime

		return false
	end

	if arg_36_0.isTriggerAtion then
		return false
	end

	return true
end

function var_0_0.updateStateData(arg_37_0, arg_37_1)
	if arg_37_0.revertIdleIndex and arg_37_0.l2dIdleIndex ~= arg_37_1.idleIndex then
		arg_37_0:setTargetValue(arg_37_0.startValue)
	end

	arg_37_0.lastActionIndex = arg_37_0.actionListIndex

	if arg_37_1.isPlaying and arg_37_0.actionTrigger.reset_index_action and arg_37_1.actionName and table.contains(arg_37_0.actionTrigger.reset_index_action, arg_37_1.actionName) then
		arg_37_0.actionListIndex = 1
	end

	if arg_37_0.revertActionIndex and arg_37_0.lastActionIndex ~= arg_37_0.actionListIndex then
		arg_37_0:setTargetValue(arg_37_0.startValue)
	end

	arg_37_0.l2dIdleIndex = arg_37_1.idleIndex
	arg_37_0.l2dIsPlaying = arg_37_1.isPlaying
	arg_37_0.l2dIgnoreReact = arg_37_1.ignoreReact
	arg_37_0.l2dPlayActionName = arg_37_1.actionName

	if not arg_37_0.l2dIsPlaying and arg_37_0.isTriggerAtion then
		arg_37_0:setTriggerActionFlag(false)
	end

	if arg_37_0.l2dIdleIndex and arg_37_0.idleOn and #arg_37_0.idleOn > 0 then
		arg_37_0.reactConditionFlag = table.contains(arg_37_0.idleOn, arg_37_0.l2dIdleIndex)
	end

	if arg_37_0.l2dIdleIndex and arg_37_0.idleOff and #arg_37_0.idleOff > 0 then
		arg_37_0.reactConditionFlag = not table.contains(arg_37_0.idleOff, arg_37_0.l2dIdleIndex)
	end
end

function var_0_0.checkClickAction(arg_38_0)
	if arg_38_0.firstActive then
		arg_38_0:onEventCallback(Live2D.EVENT_ACTION_ABLE, {
			ableFlag = true
		})
	elseif arg_38_0.firstStop then
		local var_38_0 = math.abs(arg_38_0.mouseInputUp.x - arg_38_0.mouseInputDown.x) < 30 and math.abs(arg_38_0.mouseInputUp.y - arg_38_0.mouseInputDown.y) < 30
		local var_38_1 = arg_38_0.mouseInputUpTime - arg_38_0.mouseInputDownTime < 0.5

		if var_38_0 and var_38_1 and not arg_38_0.l2dIsPlaying then
			arg_38_0.clickTriggerTime = 0.01
			arg_38_0.clickApplyFlag = true
		else
			arg_38_0:onEventCallback(Live2D.EVENT_ACTION_ABLE, {
				ableFlag = false
			})
		end
	elseif arg_38_0.clickTriggerTime and arg_38_0.clickTriggerTime > 0 then
		arg_38_0.clickTriggerTime = arg_38_0.clickTriggerTime - Time.deltaTime

		if arg_38_0.clickTriggerTime <= 0 then
			arg_38_0.clickTriggerTime = nil

			arg_38_0:onEventCallback(Live2D.EVENT_ACTION_ABLE, {
				ableFlag = false
			})

			if arg_38_0.clickApplyFlag then
				arg_38_0.clickApplyFlag = false

				return true
			end
		end
	end

	return false
end

function var_0_0.saveData(arg_39_0)
	if arg_39_0.revert == -1 and arg_39_0.saveParameterFlag then
		Live2dConst.SaveDragData(arg_39_0.id, arg_39_0.live2dData:GetShipSkinConfig().id, arg_39_0.live2dData.ship.id, arg_39_0.parameterTargetValue)
	end

	if arg_39_0.actionTrigger.type == Live2D.DRAG_CLICK_MANY then
		Live2dConst.SetDragActionIndex(arg_39_0.id, arg_39_0.live2dData:GetShipSkinConfig().id, arg_39_0.live2dData.ship.id, arg_39_0.actionListIndex)
	end
end

function var_0_0.loadData(arg_40_0)
	if arg_40_0.revert == -1 and arg_40_0.saveParameterFlag then
		local var_40_0 = Live2dConst.GetDragData(arg_40_0.id, arg_40_0.live2dData:GetShipSkinConfig().id, arg_40_0.live2dData.ship.id)

		if var_40_0 then
			arg_40_0:setParameterValue(var_40_0)
			arg_40_0:setTargetValue(var_40_0)
		end
	end

	if arg_40_0.actionTrigger.type == Live2D.DRAG_CLICK_MANY then
		arg_40_0.actionListIndex = Live2dConst.GetDragActionIndex(arg_40_0.id, arg_40_0.live2dData:GetShipSkinConfig().id, arg_40_0.live2dData.ship.id) or 1
	end
end

function var_0_0.clearData(arg_41_0)
	if arg_41_0.revert == -1 then
		arg_41_0:setParameterValue(arg_41_0.startValue)
		arg_41_0:setTargetValue(arg_41_0.startValue)
	end
end

function var_0_0.setTriggerActionFlag(arg_42_0, arg_42_1)
	arg_42_0.isTriggerAtion = arg_42_1
end

function var_0_0.dispose(arg_43_0)
	arg_43_0._active = false
	arg_43_0._parameterCom = nil
	arg_43_0.parameterValue = arg_43_0.startValue
	arg_43_0.parameterTargetValue = 0
	arg_43_0.parameterSmooth = 0
	arg_43_0.mouseInputDown = Vector2(0, 0)
	arg_43_0.live2dData = nil
end

return var_0_0
