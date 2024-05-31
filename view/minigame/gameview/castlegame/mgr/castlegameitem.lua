﻿local var_0_0 = class("CastleGameItem")
local var_0_1 = 70
local var_0_2 = 300
local var_0_3 = 166
local var_0_4 = {
	2,
	6
}
local var_0_5 = 125
local var_0_6 = "bubble_broken"
local var_0_7 = "bubble_wait"
local var_0_8 = "bubble_hold"
local var_0_9 = 130
local var_0_10 = 130

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._bubbleTpl = findTF(arg_1_1, "bubbleTpl")
	arg_1_0._carriageTpl = findTF(arg_1_1, "carriageTpl")
	arg_1_0._stoneTpl = findTF(arg_1_1, "stoneTpl")
	arg_1_0._boomTpl = findTF(arg_1_1, "boomTpl")
	arg_1_0._event = arg_1_2
	arg_1_0.carriagePool = {}
	arg_1_0.bubblePool = {}
	arg_1_0.carriages = {}
	arg_1_0.bubbles = {}
	arg_1_0.stonePool = {}
	arg_1_0.stones = {}
	arg_1_0.boomPool = {}
	arg_1_0.booms = {}
end

function var_0_0.setContent(arg_2_0, arg_2_1)
	if not arg_2_1 then
		print("容器不能为nil")

		return
	end

	arg_2_0._content = arg_2_1
end

function var_0_0.start(arg_3_0)
	local var_3_0 = CastleGameVo.roundData.stone

	arg_3_0.stoneDatas = {}

	for iter_3_0 = 1, #var_3_0 do
		local var_3_1 = math.random() * (var_3_0[iter_3_0].time[2] - var_3_0[iter_3_0].time[1]) + var_3_0[iter_3_0].time[1]
		local var_3_2 = var_3_0[iter_3_0].index

		table.insert(arg_3_0.stoneDatas, {
			time = var_3_1,
			indexs = var_3_2
		})
	end

	for iter_3_1 = #arg_3_0.stones, 1, -1 do
		local var_3_3 = table.remove(arg_3_0.stones, iter_3_1)

		setActive(var_3_3.tf, false)
		arg_3_0:returnItem(var_3_3, arg_3_0.stonePool)
	end

	for iter_3_2 = #arg_3_0.carriages, 1, -1 do
		local var_3_4 = table.remove(arg_3_0.carriages, iter_3_2)

		var_3_4.ready = 0

		setActive(var_3_4.tf, false)
		arg_3_0:returnItem(var_3_4, arg_3_0.carriagePool)
	end

	for iter_3_3 = #arg_3_0.bubbles, 1, -1 do
		local var_3_5 = table.remove(arg_3_0.bubbles, iter_3_3)

		var_3_5.ready = 0
		var_3_5.broken = true
		var_3_5.brokenTime = 0
		var_3_5.hit = false

		setActive(var_3_5.tf, false)
		arg_3_0:returnItem(var_3_5, arg_3_0.bubblePool)
	end

	for iter_3_4 = #arg_3_0.booms, 1, -1 do
		local var_3_6 = table.remove(arg_3_0.booms, iter_3_4)

		var_3_6.ready = 0
		var_3_6.broken = true
		var_3_6.brokenTime = 0

		setActive(var_3_6.tf, false)
		arg_3_0:returnItem(var_3_6, arg_3_0.boomPool)
	end

	arg_3_0.floorIndexs = {}
	arg_3_0.carriageTime = CastleGameVo.roundData.carriage
	arg_3_0.bubbleTime = CastleGameVo.roundData.bubble_time
	arg_3_0.boomTimes = {}

	for iter_3_5 = 1, #CastleGameVo.roundData.boom do
		local var_3_7 = CastleGameVo.roundData.boom[iter_3_5].time
		local var_3_8 = var_3_7[math.random(1, #var_3_7)]

		table.insert(arg_3_0.boomTimes, {
			time = var_3_8
		})
	end
end

function var_0_0.step(arg_4_0)
	for iter_4_0 = #arg_4_0.carriageTime, 1, -1 do
		if CastleGameVo.gameStepTime > arg_4_0.carriageTime[iter_4_0] then
			table.remove(arg_4_0.carriageTime, iter_4_0)
			arg_4_0:appearCarriage()
		end
	end

	for iter_4_1 = #arg_4_0.bubbleTime, 1, -1 do
		if CastleGameVo.gameStepTime > arg_4_0.bubbleTime[iter_4_1].time then
			local var_4_0 = table.remove(arg_4_0.bubbleTime, iter_4_1)

			arg_4_0:appearBubble(var_4_0.num)
		end
	end

	for iter_4_2 = #arg_4_0.boomTimes, 1, -1 do
		local var_4_1 = arg_4_0.boomTimes[iter_4_2]

		if CastleGameVo.gameStepTime > var_4_1.time then
			table.remove(arg_4_0.boomTimes, iter_4_2)
			arg_4_0:appearBoom()
		end
	end

	for iter_4_3 = #arg_4_0.carriages, 1, -1 do
		local var_4_2 = arg_4_0.carriages[iter_4_3]

		if var_4_2.ready and var_4_2.ready > 0 then
			var_4_2.ready = var_4_2.ready - CastleGameVo.deltaTime

			if var_4_2.ready <= 0 then
				var_4_2.ready = 0

				if arg_4_0.itemRemindCallback then
					-- block empty
				end
			end
		else
			local var_4_3 = var_4_2.tf
			local var_4_4 = var_4_2.target
			local var_4_5 = var_4_3.anchoredPosition
			local var_4_6 = Vector2(var_4_5.x + var_4_2.speed.x * CastleGameVo.deltaTime * var_0_2, var_4_5.y + var_4_2.speed.y * CastleGameVo.deltaTime * var_0_2)

			var_4_3.anchoredPosition = var_4_6

			if var_4_5.x < var_4_4.x and var_4_6.x > var_4_4.x then
				table.remove(arg_4_0.carriages, iter_4_3)
				setActive(var_4_2.tf, false)
				arg_4_0:returnItem(var_4_2, arg_4_0.carriagePool)
			elseif var_4_5.x > var_4_4.x and var_4_6.x < var_4_4.x then
				table.remove(arg_4_0.carriages, iter_4_3)
				setActive(var_4_2.tf, false)
				arg_4_0:returnItem(var_4_2, arg_4_0.carriagePool)
			end
		end
	end

	for iter_4_4 = #arg_4_0.bubbles, 1, -1 do
		local var_4_7 = arg_4_0.bubbles[iter_4_4]

		if var_4_7.ready and var_4_7.ready > 0 then
			var_4_7.ready = var_4_7.ready - CastleGameVo.deltaTime

			if var_4_7.ready <= 0 then
				var_4_7.ready = 0

				setActive(var_4_7.tf, true)
			end
		elseif var_4_7.brokenTime and var_4_7.brokenTime > 0 then
			var_4_7.brokenTime = var_4_7.brokenTime - CastleGameVo.deltaTime

			if not var_4_7.hit and CastleGameVo.bubble_broken_time - var_4_7.brokenTime > 1 then
				var_4_7.hit = true
			end

			if var_4_7.brokenTime < 0 then
				var_4_7.broken = true
				var_4_7.brokenTime = 0
				var_4_7.hit = false

				if arg_4_0.bubbleBrokenCallback then
					arg_4_0.bubbleBrokenCallback(var_4_7)
				end

				arg_4_0:changeAnimAction(var_4_7.anims, var_0_6, 1, var_0_7, function()
					setActive(var_4_7.tf, false)
				end)
				arg_4_0:returnItem(var_4_7, arg_4_0.bubblePool)
				table.remove(arg_4_0.bubbles, iter_4_4)
			end
		end
	end

	for iter_4_5 = #arg_4_0.stoneDatas, 1, -1 do
		if CastleGameVo.gameStepTime > arg_4_0.stoneDatas[iter_4_5].time then
			local var_4_8 = table.remove(arg_4_0.stoneDatas, iter_4_5).indexs

			arg_4_0:appearStone(var_4_8)
		end
	end

	for iter_4_6 = #arg_4_0.stones, 1, -1 do
		local var_4_9 = arg_4_0.stones[iter_4_6]

		if var_4_9.ready and var_4_9.ready > 0 then
			var_4_9.ready = var_4_9.ready - CastleGameVo.deltaTime

			if var_4_9.ready <= 0 then
				var_4_9.ready = 0

				setActive(var_4_9.tf, true)

				if arg_4_0.floorBrokenCallback then
					arg_4_0.floorBrokenCallback(var_4_9.useIndex, 0.5)
				end
			end
		elseif var_4_9.brokenTime and var_4_9.brokenTime > 0 then
			var_4_9.brokenTime = var_4_9.brokenTime - CastleGameVo.deltaTime

			if var_4_9.brokenTime <= 0 then
				var_4_9.broken = true
				var_4_9.brokenTime = nil

				table.remove(arg_4_0.stones, iter_4_6)
				setActive(var_4_9.tf, false)
				arg_4_0:returnItem(var_4_9, arg_4_0.stonePool)
			end
		end
	end

	for iter_4_7 = #arg_4_0.booms, 1, -1 do
		local var_4_10 = arg_4_0.booms[iter_4_7]
		local var_4_11 = arg_4_0.booms[iter_4_7].tf.anchoredPosition
		local var_4_12 = var_4_10.bound.points
		local var_4_13 = {}

		for iter_4_8 = 0, var_4_12.Length - 1 do
			local var_4_14 = var_4_12[iter_4_8]

			findTF(var_4_10.tf, "zPos/" .. iter_4_8 + 1).anchoredPosition = Vector2(var_4_14.x, var_4_14.y)

			local var_4_15 = Vector2(var_4_11.x + var_4_14.x, var_4_11.y + var_4_14.y)

			table.insert(var_4_13, var_4_15)
		end

		var_4_10.boundPoints = var_4_13

		if var_4_10.ready and var_4_10.ready > 0 then
			var_4_10.ready = var_4_10.ready - CastleGameVo.deltaTime

			if var_4_10.ready <= 0 then
				var_4_10.ready = 0

				setActive(var_4_10.tf, true)

				if arg_4_0.floorBrokenCallback then
					arg_4_0.floorBrokenCallback(var_4_10.useIndex, 0.5)
				end
			end
		elseif var_4_10.brokenTime and var_4_10.brokenTime > 0 then
			var_4_10.brokenTime = var_4_10.brokenTime - CastleGameVo.deltaTime

			if var_4_10.brokenTime < 0 then
				var_4_10.broken = true
				var_4_10.brokenTime = 0

				setActive(var_4_10.tf, false)

				local var_4_16 = table.remove(arg_4_0.booms, iter_4_7)

				arg_4_0:returnItem(var_4_16, arg_4_0.boomPool)
			end
		end
	end
end

function var_0_0.appearStone(arg_6_0, arg_6_1)
	local var_6_0
	local var_6_1 = {}
	local var_6_2 = arg_6_0:getItemActiveIndex()

	for iter_6_0 = 1, #var_6_2 do
		if not table.contains(arg_6_1, var_6_2[iter_6_0]) then
			table.insert(var_6_1, var_6_2[iter_6_0])
		end
	end

	if #var_6_1 == 0 then
		return
	end

	if #arg_6_0.stonePool > 0 then
		var_6_0 = table.remove(arg_6_0.stonePool, 1)
	else
		local var_6_3 = tf(instantiate(arg_6_0._stoneTpl))

		setParent(var_6_3, arg_6_0._content)

		local var_6_4 = GetComponent(findTF(var_6_3, "zPos/anim/collider"), typeof(BoxCollider2D))

		var_6_0 = {
			tf = var_6_3,
			bound = var_6_4
		}
	end

	local var_6_5 = findTF(var_6_0.tf, "zPos/anim/img")
	local var_6_6 = var_6_5.childCount
	local var_6_7 = math.random(1, var_6_6) - 1

	for iter_6_1 = 0, var_6_6 - 1 do
		setActive(var_6_5:GetChild(iter_6_1), iter_6_1 == var_6_7)
	end

	var_6_0.ready = CastleGameVo.item_ready_time
	var_6_0.brokenTime = CastleGameVo.stone_broken_time

	local var_6_8 = var_6_1[math.random(1, #var_6_1)]
	local var_6_9 = var_6_8 % CastleGameVo.w_count
	local var_6_10 = math.floor(var_6_8 / CastleGameVo.w_count)

	var_6_0.tf.anchoredPosition = CastleGameVo.GetRotationPosByWH(var_6_9, var_6_10)

	setActive(var_6_0.tf, false)

	var_6_0.index = var_6_8
	var_6_0.useIndex = {
		var_6_8
	}

	if arg_6_0.itemRemindCallback then
		arg_6_0.itemRemindCallback({
			{
				w = var_6_9,
				h = var_6_10,
				type = CastleGameRemind.remind_type_1
			}
		})
	end

	table.insert(arg_6_0.stones, var_6_0)
end

function var_0_0.returnItem(arg_7_0, arg_7_1, arg_7_2)
	if arg_7_0.itemChangeCallback then
		arg_7_0.itemChangeCallback(arg_7_1, false)
	end

	table.insert(arg_7_2, arg_7_1)
end

function var_0_0.appearBubble(arg_8_0, arg_8_1)
	for iter_8_0 = 1, arg_8_1 do
		local var_8_0
		local var_8_1 = arg_8_0:getItemActiveIndex()

		if #var_8_1 == 0 then
			return
		end

		if #arg_8_0.bubblePool > 0 then
			var_8_0 = table.remove(arg_8_0.bubblePool, 1)
		else
			local var_8_2 = tf(instantiate(arg_8_0._bubbleTpl))
			local var_8_3 = findTF(var_8_2, "zPos/pos")
			local var_8_4 = GetComponent(findTF(var_8_2, "zPos/spine1"), typeof(SpineAnimUI))
			local var_8_5 = GetComponent(findTF(var_8_2, "zPos/spine2"), typeof(SpineAnimUI))
			local var_8_6 = GetComponent(findTF(var_8_2, "zPos/collider"), typeof(BoxCollider2D))
			local var_8_7 = var_8_2:InverseTransformPoint(var_8_6.bounds.min)
			local var_8_8 = var_8_2:InverseTransformPoint(var_8_6.bounds.max)

			setParent(var_8_2, arg_8_0._content)

			var_8_0 = {
				tf = var_8_2,
				anims = {
					var_8_4,
					var_8_5
				},
				bound = var_8_6,
				pos = var_8_3,
				bmin = var_8_7,
				bmax = var_8_8
			}
		end

		local var_8_9 = var_8_1[math.random(1, #var_8_1)]
		local var_8_10 = var_8_9 % CastleGameVo.w_count
		local var_8_11 = math.floor(var_8_9 / CastleGameVo.w_count)

		var_8_0.start = CastleGameVo.GetRotationPosByWH(var_8_10, var_8_11)
		var_8_0.start.y = var_8_0.start.y + var_0_5
		var_8_0.tf.anchoredPosition = var_8_0.start

		setActive(var_8_0.tf, false)

		var_8_0.ready = CastleGameVo.bubble_ready_time
		var_8_0.broken = false
		var_8_0.brokenTime = CastleGameVo.bubble_broken_time
		var_8_0.useIndex = {
			var_8_9
		}
		var_8_0.index = var_8_9

		if arg_8_0.itemChangeCallback then
			arg_8_0.itemChangeCallback(var_8_0, true)
		end

		setActive(var_8_0.tf, false)
		table.insert(arg_8_0.bubbles, var_8_0)
		arg_8_0:changeAnimAction(var_8_0.anims, var_0_8, -1)
	end
end

function var_0_0.appearBoom(arg_9_0)
	local var_9_0 = {}
	local var_9_1 = arg_9_0:getItemActiveIndex()

	for iter_9_0 = 1, #var_9_1 do
		local var_9_2 = var_9_1[iter_9_0]

		if var_9_2 % CastleGameVo.w_count ~= CastleGameVo.w_count - 1 then
			local var_9_3 = var_9_2 + 1
			local var_9_4 = var_9_2 + CastleGameVo.w_count
			local var_9_5 = var_9_2 + 1 + CastleGameVo.w_count

			if table.contains(var_9_1, var_9_3) and table.contains(var_9_1, var_9_4) and table.contains(var_9_1, var_9_5) then
				table.insert(var_9_0, var_9_2)
			end
		end
	end

	local var_9_6 = var_9_0[math.random(1, #var_9_0)]

	if #var_9_0 == 0 then
		return
	end

	local var_9_7

	if #arg_9_0.boomPool > 0 then
		var_9_7 = table.remove(arg_9_0.boomPool, 1)
	else
		local var_9_8 = tf(instantiate(arg_9_0._boomTpl))
		local var_9_9 = GetComponent(findTF(var_9_8, "zPos/collider"), typeof("UnityEngine.PolygonCollider2D"))

		setParent(var_9_8, arg_9_0._content)

		var_9_7 = {
			tf = var_9_8,
			bound = var_9_9
		}
	end

	local var_9_10 = var_9_6 % CastleGameVo.w_count
	local var_9_11 = math.floor(var_9_6 / CastleGameVo.w_count)
	local var_9_12 = CastleGameVo.GetRotationPosByWH(var_9_10, var_9_11)

	var_9_12.x = var_9_12.x + var_0_9
	var_9_12.y = var_9_12.y + var_0_10
	var_9_7.tf.anchoredPosition = var_9_12
	var_9_7.ready = CastleGameVo.item_ready_time
	var_9_7.broken = false

	setActive(var_9_7.tf, false)

	var_9_7.index = var_9_6
	var_9_7.useIndex = {
		var_9_6,
		var_9_6 + 1,
		var_9_6 + CastleGameVo.w_count,
		var_9_6 + CastleGameVo.w_count + 1
	}
	var_9_7.brokenTime = 1.5

	if arg_9_0.itemChangeCallback then
		arg_9_0.itemChangeCallback(var_9_7, true)
	end

	if arg_9_0.itemRemindCallback then
		arg_9_0.itemRemindCallback({
			{
				w = var_9_10,
				h = var_9_11,
				type = CastleGameRemind.remind_type_2
			}
		})
	end

	table.insert(arg_9_0.booms, var_9_7)
end

function var_0_0.setFloorBroken(arg_10_0, arg_10_1)
	arg_10_0.floorBrokenCallback = arg_10_1
end

function var_0_0.setBubbleBroken(arg_11_0, arg_11_1)
	arg_11_0.bubbleBrokenCallback = arg_11_1
end

function var_0_0.setItemChange(arg_12_0, arg_12_1)
	arg_12_0.itemChangeCallback = arg_12_1
end

function var_0_0.setFloorIndexs(arg_13_0, arg_13_1)
	arg_13_0.floorIndexs = arg_13_1
end

function var_0_0.getItemActiveIndex(arg_14_0)
	local var_14_0 = {}
	local var_14_1 = {}

	for iter_14_0 = 1, #arg_14_0.bubbles do
		for iter_14_1, iter_14_2 in ipairs(arg_14_0.bubbles[iter_14_0].useIndex) do
			table.insert(var_14_1, iter_14_2)
		end
	end

	for iter_14_3 = 1, #arg_14_0.booms do
		for iter_14_4, iter_14_5 in ipairs(arg_14_0.booms[iter_14_3].useIndex) do
			table.insert(var_14_1, iter_14_5)
		end
	end

	for iter_14_6 = 1, #arg_14_0.stones do
		for iter_14_7, iter_14_8 in ipairs(arg_14_0.stones[iter_14_6].useIndex) do
			table.insert(var_14_1, iter_14_8)
		end
	end

	for iter_14_9 = 1, #arg_14_0.floorIndexs do
		local var_14_2 = arg_14_0.floorIndexs[iter_14_9]

		if not table.contains(var_14_1, var_14_2) then
			table.insert(var_14_0, var_14_2)
		end
	end

	return var_14_0
end

function var_0_0.appearCarriage(arg_15_0)
	local var_15_0

	if #arg_15_0.carriagePool > 0 then
		var_15_0 = table.remove(arg_15_0.carriagePool, 1)
	else
		local var_15_1 = tf(instantiate(arg_15_0._carriageTpl))
		local var_15_2 = GetComponent(findTF(var_15_1, "zPos/spine"), typeof(SpineAnimUI))
		local var_15_3 = GetComponent(findTF(var_15_1, "zPos/collider"), typeof(BoxCollider2D))
		local var_15_4 = var_15_1:InverseTransformPoint(var_15_3.bounds.min)
		local var_15_5 = var_15_1:InverseTransformPoint(var_15_3.bounds.max)

		setParent(var_15_1, arg_15_0._content)

		var_15_0 = {
			tf = var_15_1,
			bound = var_15_3,
			anims = {
				var_15_2
			},
			bmin = var_15_4,
			bmax = var_15_5
		}
	end

	local var_15_6 = arg_15_0:getCarriageRoadlist()

	if #var_15_6 > 0 then
		local var_15_7 = var_15_6[math.random(1, #var_15_6)]
		local var_15_8 = var_15_7.w
		local var_15_9 = var_15_7.h
		local var_15_10 = var_15_7.target_w
		local var_15_11 = var_15_7.target_h
		local var_15_12 = var_15_7.scale

		var_15_0.w = var_15_8
		var_15_0.h = var_15_9
		var_15_0.target_w = var_15_10
		var_15_0.target_h = var_15_11
		findTF(var_15_0.tf, "zPos").localScale = var_15_12
		var_15_0.start = CastleGameVo.GetRotationPosByWH(var_15_0.w, var_15_0.h)
		var_15_0.start.y = var_15_0.start.y + var_0_1
		var_15_0.target = CastleGameVo.GetRotationPosByWH(var_15_0.target_w, var_15_0.target_h)
		var_15_0.target.y = var_15_0.target.y + var_0_1
		var_15_0.tf.anchoredPosition = var_15_0.start
		var_15_0.ready = CastleGameVo.item_ready_time

		setActive(var_15_0.tf, false)
		setActive(var_15_0.tf, true)

		local var_15_13, var_15_14 = arg_15_0:countSpeed(var_15_0.start, var_15_0.target)

		var_15_0.speed = var_15_13
		var_15_0.direct = var_15_14

		if arg_15_0.itemChangeCallback then
			arg_15_0.itemChangeCallback(var_15_0, true)
		end

		table.insert(arg_15_0.carriages, var_15_0)
	else
		print("当前不存在可以出现马车的位置")
	end
end

function var_0_0.getCarriageRoadlist(arg_16_0)
	local var_16_0 = {}

	for iter_16_0 = 0, CastleGameVo.w_count - 1 do
		local var_16_1 = true

		for iter_16_1 = 0, CastleGameVo.h_count - 1 do
			local var_16_2 = iter_16_0 + iter_16_1 * CastleGameVo.w_count

			if var_16_1 and not table.contains(arg_16_0.floorIndexs, var_16_2) then
				var_16_1 = false
			end
		end

		if var_16_1 then
			table.insert(var_16_0, {
				h = -1,
				w = iter_16_0,
				target_w = iter_16_0,
				target_h = CastleGameVo.h_count,
				scale = Vector3(-1, 1, 1)
			})
		end
	end

	for iter_16_2 = 0, CastleGameVo.h_count - 1 do
		local var_16_3 = true

		for iter_16_3 = 0, CastleGameVo.w_count - 1 do
			local var_16_4 = iter_16_3 + iter_16_2 * CastleGameVo.w_count

			if var_16_3 and not table.contains(arg_16_0.floorIndexs, var_16_4) then
				var_16_3 = false
			end
		end

		if var_16_3 then
			table.insert(var_16_0, {
				w = -1,
				h = iter_16_2,
				target_w = CastleGameVo.w_count,
				target_h = iter_16_2,
				scale = Vector3(1, 1, 1)
			})
		end
	end

	return var_16_0
end

function var_0_0.setItemRemindCallback(arg_17_0, arg_17_1)
	arg_17_0.itemRemindCallback = arg_17_1
end

function var_0_0.countSpeed(arg_18_0, arg_18_1, arg_18_2)
	local var_18_0 = math.atan(math.abs(arg_18_2.y - arg_18_1.y) / math.abs(arg_18_2.x - arg_18_1.x))
	local var_18_1 = arg_18_2.x > arg_18_1.x and 1 or -1
	local var_18_2 = arg_18_2.y > arg_18_1.y and 1 or -1
	local var_18_3 = math.cos(var_18_0) * var_18_1
	local var_18_4 = math.sin(var_18_0) * var_18_2

	return Vector2(var_18_3, var_18_4), Vector2(var_18_1, var_18_2)
end

function var_0_0.changeAnimAction(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5)
	local var_19_0 = 0

	for iter_19_0 = 1, #arg_19_1 do
		local var_19_1 = arg_19_1[iter_19_0]

		var_19_1:SetActionCallBack(nil)
		var_19_1:SetAction(arg_19_2, 0)
		var_19_1:SetActionCallBack(function(arg_20_0)
			if arg_20_0 == "finish" then
				if arg_19_3 == 1 then
					var_19_1:SetActionCallBack(nil)
					var_19_1:SetAction(arg_19_4, 0)
				end

				if arg_19_5 and var_19_0 == 0 then
					var_19_0 = 1

					arg_19_5()
				end
			end
		end)

		if arg_19_3 ~= 1 and arg_19_5 and var_19_0 == 0 then
			var_19_0 = 1

			arg_19_5()
		end
	end
end

function var_0_0.playerInBubble(arg_21_0, arg_21_1, arg_21_2)
	arg_21_1.char = arg_21_2
end

function var_0_0.getBooms(arg_22_0)
	return arg_22_0.booms
end

function var_0_0.getBubbles(arg_23_0)
	return arg_23_0.bubbles
end

function var_0_0.getCarriages(arg_24_0)
	return arg_24_0.carriages
end

function var_0_0.clear(arg_25_0)
	return
end

return var_0_0
