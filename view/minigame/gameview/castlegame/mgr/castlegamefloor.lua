local var_0_0 = class("CastleGameFloor")
local var_0_1 = 999999

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._tpl = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.floors = {}
	arg_1_0.colliders = {}
	arg_1_0.floorTfs = {}
	arg_1_0.bounds = {}

	local var_1_0 = CastleGameVo.h_count * CastleGameVo.w_count

	for iter_1_0 = 0, var_1_0 - 1 do
		local var_1_1 = tf(instantiate(arg_1_0._tpl))

		var_1_1.name = tostring(iter_1_0 + 1)

		setActive(var_1_1, true)

		local var_1_2 = findTF(var_1_1, "zPos")
		local var_1_3 = findTF(var_1_1, "zPos/floor/img")

		setImageSprite(var_1_3, CastleGameVo.getFloorImage(iter_1_0 + 1), true)

		local var_1_4 = var_1_1.anchoredPosition
		local var_1_5 = findTF(var_1_1, "zPos/collider")
		local var_1_6 = GetComponent(var_1_5, typeof("UnityEngine.PolygonCollider2D"))
		local var_1_7 = GetComponent(findTF(var_1_1, "zPos/floor"), typeof(Animator))
		local var_1_8 = iter_1_0 % CastleGameVo.h_count
		local var_1_9 = math.floor(iter_1_0 / CastleGameVo.w_count)

		table.insert(arg_1_0.colliders, var_1_6)
		table.insert(arg_1_0.floorTfs, var_1_1)
		table.insert(arg_1_0.floors, {
			fall = false,
			tf = var_1_1,
			zPos = var_1_2,
			anim = var_1_7,
			index = iter_1_0,
			collider = var_1_6,
			w = var_1_8,
			h = var_1_9
		})
	end

	arg_1_0:updateFloorPos()
	arg_1_0:updateBounds()
end

function var_0_0.getTfs(arg_2_0)
	return arg_2_0.floorTfs
end

function var_0_0.getFloors(arg_3_0)
	return arg_3_0.floors
end

function var_0_0.getActiveIndexs(arg_4_0)
	return arg_4_0.activeIndexs
end

function var_0_0.updateBounds(arg_5_0)
	for iter_5_0 = 1, #arg_5_0.floors do
		local var_5_0 = arg_5_0.floors[iter_5_0].collider.points
		local var_5_1 = arg_5_0.floors[iter_5_0].tf.anchoredPosition
		local var_5_2 = {}

		for iter_5_1 = 0, var_5_0.Length - 1 do
			local var_5_3 = Vector2(var_5_1.x + var_5_0[iter_5_1].x, var_5_1.y + var_5_0[iter_5_1].y)

			table.insert(var_5_2, var_5_3)
		end

		arg_5_0.floors[iter_5_0].bound = var_5_2

		table.insert(arg_5_0.bounds, var_5_2)
	end
end

function var_0_0.getBounds(arg_6_0)
	return arg_6_0.bounds
end

function var_0_0.setContent(arg_7_0, arg_7_1)
	if not arg_7_1 then
		print("地板的容器不能为nil")

		return
	end

	arg_7_0._content = arg_7_1

	for iter_7_0 = 1, #arg_7_0.floorTfs do
		SetParent(arg_7_0.floorTfs[iter_7_0], arg_7_1)
	end
end

function var_0_0.start(arg_8_0)
	arg_8_0.fallDatas = arg_8_0:getFallDatas()
	arg_8_0.floorFallStep = var_0_1
	arg_8_0.activeIndexs = {}

	for iter_8_0 = 1, #arg_8_0.floors do
		arg_8_0.floors[iter_8_0].fall = false
		arg_8_0.floors[iter_8_0].removeTime = nil
		arg_8_0.floors[iter_8_0].revertTime = nil

		setActive(arg_8_0.floors[iter_8_0].tf, false)
		setActive(arg_8_0.floors[iter_8_0].tf, true)
		table.insert(arg_8_0.activeIndexs, arg_8_0.floors[iter_8_0].index)
	end

	arg_8_0:updateFloorPos()
end

function var_0_0.step(arg_9_0)
	if arg_9_0.floorFallStep and arg_9_0.floorFallStep > 0 then
		arg_9_0.floorFallStep = arg_9_0.floorFallStep - CastleGameVo.deltaTime

		if arg_9_0.floorFallStep <= 0 then
			-- block empty
		end
	end

	for iter_9_0 = #arg_9_0.floors, 1, -1 do
		local var_9_0 = arg_9_0.floors[iter_9_0]

		if var_9_0.removeTime and var_9_0.removeTime > 0 then
			var_9_0.removeTime = var_9_0.removeTime - CastleGameVo.deltaTime

			if var_9_0.removeTime <= 0 then
				var_9_0.removeTime = nil

				arg_9_0:applyFloorFall(var_9_0)
			end
		end
	end

	for iter_9_1 = #arg_9_0.floors, 1, -1 do
		local var_9_1 = arg_9_0.floors[iter_9_1]

		if var_9_1.revertTime and var_9_1.revertTime > 0 then
			var_9_1.revertTime = var_9_1.revertTime - CastleGameVo.deltaTime

			if var_9_1.revertTime <= 0 then
				var_9_1.revertTime = nil

				arg_9_0:revertFloorFall(var_9_1)
				arg_9_0:revertActiveFloor(var_9_1)
			end
		end
	end

	for iter_9_2 = #arg_9_0.fallDatas, 1, -1 do
		if CastleGameVo.gameStepTime >= arg_9_0.fallDatas[iter_9_2].time then
			local var_9_2 = table.remove(arg_9_0.fallDatas, iter_9_2)

			arg_9_0:removeFloorByFallData(var_9_2)

			break
		end
	end
end

function var_0_0.setBroken(arg_10_0, arg_10_1, arg_10_2)
	local var_10_0 = arg_10_0:getFloorByIndex(arg_10_1)

	arg_10_0:setFloorFallTime(var_10_0, false, arg_10_2)
end

function var_0_0.removeFloorByFallData(arg_11_0, arg_11_1)
	local var_11_0 = table.remove(arg_11_1.rule_id, math.random(1, #arg_11_1.rule_id))
	local var_11_1 = CastleGameVo.floor_rule[var_11_0]

	for iter_11_0 = 1, #var_11_1 do
		local var_11_2 = arg_11_0:getFloorByIndex(var_11_1[iter_11_0])

		arg_11_0:setFloorFallTime(var_11_2, true, nil)
	end
end

function var_0_0.clear(arg_12_0)
	return
end

function var_0_0.setFloorFallCallback(arg_13_0, arg_13_1)
	arg_13_0.floorFallCallback = arg_13_1
end

function var_0_0.getFallDatas(arg_14_0)
	return CastleGameVo.roundData.floors
end

function var_0_0.applyFloorFall(arg_15_0, arg_15_1)
	local var_15_0 = arg_15_1.zPos
	local var_15_1 = arg_15_1.anim

	arg_15_1.fall = true
	arg_15_1.revertTime = CastleGameVo.floor_revert_time

	var_15_1:Play("hide")
end

function var_0_0.revertFloorFall(arg_16_0, arg_16_1)
	local var_16_0 = arg_16_1.anim

	arg_16_1.fall = false

	var_16_0:Play("revert")
end

function var_0_0.revertActiveFloor(arg_17_0, arg_17_1)
	if not table.contains(arg_17_0.activeIndexs, arg_17_1.index) then
		table.insert(arg_17_0.activeIndexs, arg_17_1.index)
	end
end

function var_0_0.removeActiveFloor(arg_18_0, arg_18_1)
	for iter_18_0 = #arg_18_0.activeIndexs, 1, -1 do
		if arg_18_0.activeIndexs[iter_18_0] == arg_18_1.index then
			table.remove(arg_18_0.activeIndexs, iter_18_0)
		end
	end
end

function var_0_0.setFloorFallTime(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	for iter_19_0 = 1, #arg_19_1 do
		if arg_19_2 then
			arg_19_1[iter_19_0].anim:Play("shake")
		end

		if not arg_19_1[iter_19_0].fall then
			arg_19_1[iter_19_0].removeTime = arg_19_3 and arg_19_3 or CastleGameVo.floor_remove_time
			arg_19_1[iter_19_0].revertTime = nil

			arg_19_0:removeActiveFloor(arg_19_1[iter_19_0])
		else
			print(arg_19_1[iter_19_0].index .. "已经被移除，无法设置掉落")
		end
	end
end

function var_0_0.getFloorByIndex(arg_20_0, arg_20_1, arg_20_2)
	for iter_20_0 = 1, #arg_20_0.floors do
		if arg_20_0.floors[iter_20_0].index == arg_20_1 then
			return {
				arg_20_0.floors[iter_20_0]
			}
		end
	end

	print("找不到index = " .. arg_20_1 .. "的地板")

	return {}
end

function var_0_0.updateFloorPos(arg_21_0)
	for iter_21_0 = 1, #arg_21_0.floors do
		local var_21_0 = arg_21_0.floors[iter_21_0].index
		local var_21_1 = var_21_0 % CastleGameVo.w_count
		local var_21_2 = math.floor(var_21_0 / CastleGameVo.h_count)

		arg_21_0.floors[iter_21_0].tf.anchoredPosition = CastleGameVo.GetRotationPosByWH(var_21_1, var_21_2)
	end
end

function var_0_0.getOutLandPoint(arg_22_0)
	local var_22_0 = arg_22_0.floors[1].bound[1]
	local var_22_1 = arg_22_0.floors[(CastleGameVo.h_count - 1) * CastleGameVo.w_count + 1].bound[2]
	local var_22_2 = arg_22_0.floors[CastleGameVo.w_count].bound[4]
	local var_22_3 = arg_22_0.floors[CastleGameVo.h_count * CastleGameVo.w_count].bound[3]

	return {
		lb = var_22_0,
		lt = var_22_1,
		rt = var_22_3,
		rb = var_22_2
	}
end

function var_0_0.press(arg_23_0, arg_23_1)
	return
end

return var_0_0
