local var_0_0 = class("RectCollisionHorizontal")

var_0_0.directUp = Vector3(0, 1, 0)
var_0_0.directDown = Vector3(0, -1, 0)
var_0_0.directRight = Vector3(1, 0, 0)
var_0_0.directLeft = Vector3(-1, 0, 0)

function var_0_0.HorizontalCollisions(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_0.x ~= 0 and Mathf.Sign(arg_1_0.x) or arg_1_1.MoveDir
	local var_1_1 = var_1_0 == 1 and var_0_0.directRight or var_0_0.directLeft
	local var_1_2 = var_1_0 == -1 and arg_1_2.bottomLeft or arg_1_2.bottomRight
	local var_1_3 = Mathf.Abs(arg_1_0.x) + arg_1_2.skinWidth

	if Mathf.Abs(arg_1_0.x) < arg_1_2.skinWidth then
		var_1_3 = 2 * arg_1_2.skinWidth
	end

	local var_1_4 = false
	local var_1_5 = Vector3.zero

	for iter_1_0 = 1, arg_1_2.horizontalRayCount do
		var_1_5.x = var_1_2.x
		var_1_5.y = var_1_2.y + arg_1_2.horizontalRaySpacing * (iter_1_0 - 1)
		var_1_5.z = var_1_2.z

		local var_1_6, var_1_7 = Physics.Raycast(var_1_5, var_1_1, nil, var_1_3, arg_1_1.layerMask)
		local var_1_8 = false

		if var_1_7 then
			local var_1_9 = var_1_7.transform.parent

			if table.contains(arg_1_1.ignoreLayerMask, go(var_1_9).layer) then
				var_1_8 = true
			end

			if var_1_0 == 1 and not arg_1_1.horizontalRightTfs[var_1_9] then
				arg_1_1.horizontalRightTfs[var_1_9] = var_1_9
			elseif var_1_0 == -1 and not arg_1_1.horizontalLeftTfs[var_1_9] then
				arg_1_1.horizontalLeftTfs[var_1_9] = var_1_9
			end
		end

		if not var_1_8 and var_1_6 and var_1_7.distance ~= 0 then
			local var_1_10 = Vector3.Angle(var_1_7.normal, var_0_0.directUp)

			if iter_1_0 == 1 and var_1_10 <= arg_1_1.config.maxSlopeAngle then
				if arg_1_1.descendingSlope then
					arg_1_1.descendingSlope = false
					arg_1_0 = arg_1_1.moveAmountOld
				end

				local var_1_11 = 0

				if var_1_10 ~= arg_1_1.slopeAngleOld then
					var_1_11 = var_1_7.distance - arg_1_2.skinWidth
					arg_1_0.x = arg_1_0.x - var_1_11 * var_1_0
				end

				RectCollisionHorizontal.ClimbSlope(arg_1_0, arg_1_1, var_1_10, var_1_7.normal)

				arg_1_0.x = arg_1_0.x + var_1_11 * var_1_0
			end

			if not arg_1_1.climbingSlope or var_1_10 > arg_1_1.config.maxSlopeAngle then
				arg_1_0.x = (var_1_7.distance - arg_1_2.skinWidth) * var_1_0
				var_1_3 = var_1_7.distance

				if arg_1_1.climbingSlope then
					arg_1_0.y = Mathf.Tan(arg_1_1.slopeAngle * Mathf.Deg2Rad) * Mathf.Abs(arg_1_0.x)
				end

				if iter_1_0 == 1 then
					var_1_4 = true
				end

				arg_1_1.left = var_1_0 == -1
				arg_1_1.right = var_1_0 == 1
			end
		end
	end

	if var_1_4 then
		local var_1_12 = 2 * arg_1_2.skinWidth

		var_1_5.x = var_1_2.x
		var_1_5.y = var_1_2.y + arg_1_2.horizontalRaySpacing * (arg_1_2.horizontalRayCount - 1)
		var_1_5.z = var_1_2.z

		local var_1_13, var_1_14 = Physics.Raycast(var_1_5, var_1_1, nil, var_1_12, arg_1_1.layerMask)

		if var_1_13 and Vector3.Angle(var_1_14.normal, var_0_0.directUp) > arg_1_1.config.maxSlopeAngle then
			arg_1_1.fullSliding = true
		end
	end
end

function var_0_0.ClimbSlope(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = Mathf.Abs(arg_2_0.x)
	local var_2_1 = Mathf.Sin(arg_2_2 * Mathf.Deg2Rad) * var_2_0

	if var_2_1 >= arg_2_0.y then
		arg_2_0.y = var_2_1
		arg_2_0.x = Mathf.Cos(arg_2_2 * Mathf.Deg2Rad) * var_2_0 * Mathf.Sign(arg_2_0.x)
		arg_2_1.below = true
		arg_2_1.climbingSlope = true
		arg_2_1.slopeAngle = arg_2_2
		arg_2_1.slopeNormal = arg_2_3
	end
end

return var_0_0
