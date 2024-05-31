﻿local var_0_0 = class("Fushun3PlatformControll")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	arg_1_0._tplTf = arg_1_2
	arg_1_0._content = arg_1_3
	arg_1_0._event = arg_1_4
	arg_1_0._platformPool = {}
	arg_1_0._platforms = {}
	arg_1_0._sceneTf = arg_1_1
	arg_1_0._weightTotal = 0
	arg_1_0.createDatas = nil
end

function var_0_0.start(arg_2_0)
	arg_2_0.moveDistance = 0
	arg_2_0.fillDistance = 0
	arg_2_0.level = 0

	for iter_2_0 = #arg_2_0._platforms, 1, -1 do
		local var_2_0 = table.remove(arg_2_0._platforms, iter_2_0)

		setActive(var_2_0.tf, false)
		table.insert(arg_2_0._platformPool, var_2_0)
	end

	arg_2_0.createDatas = {}
	arg_2_0._weightTotal = 0

	for iter_2_1 = 1, #Fushun3GameConst.platform_data do
		local var_2_1 = Clone(Fushun3GameConst.platform_data[iter_2_1])

		arg_2_0._weightTotal = arg_2_0._weightTotal + var_2_1.weight

		table.insert(arg_2_0.createDatas, {
			config = var_2_1,
			weight = arg_2_0._weightTotal
		})
	end

	arg_2_0.initTimes = false

	arg_2_0:fillPlatform()

	arg_2_0.initTimes = true
	arg_2_0.timeFlag = Fushun3GameVo.GetTimeFlag()

	arg_2_0:changePlatformShow(false)
end

function var_0_0.updateCreateData(arg_3_0)
	arg_3_0.createDatas = {}
	arg_3_0._weightTotal = 0

	for iter_3_0 = 1, #Fushun3GameConst.platform_data do
		local var_3_0 = Clone(Fushun3GameConst.platform_data[iter_3_0])

		arg_3_0._weightTotal = arg_3_0._weightTotal + var_3_0.weight + var_3_0.diff * arg_3_0.level

		table.insert(arg_3_0.createDatas, {
			config = var_3_0,
			weight = arg_3_0._weightTotal
		})
	end
end

function var_0_0.fillPlatform(arg_4_0)
	if arg_4_0.fillDistance < arg_4_0.moveDistance + Fushun3GameConst.platform_distance then
		local var_4_0 = arg_4_0:getPlatform()

		if var_4_0.high then
			setActive(findTF(var_4_0.tf, "high_roof"), true)
		end

		table.insert(arg_4_0._platforms, var_4_0)

		var_4_0.anchoredX = arg_4_0.fillDistance
		var_4_0.tf.anchoredPosition = Vector2(arg_4_0.fillDistance, 0)

		setActive(var_4_0.tf, true)

		local var_4_1 = GetComponent(var_4_0.tf, typeof(Animator))
		local var_4_2 = Fushun3GameVo.GetTimeFlag() and "day_no_fade" or "night_no_fade"

		var_4_1:SetTrigger(var_4_2)

		if var_4_0.monster then
			local var_4_3 = findTF(var_4_0.tf, "monster")

			arg_4_0._event:emit(Fushun3GameEvent.create_monster_call, {
				pos = var_4_3.position
			})
		end

		if var_4_0.item then
			local var_4_4 = findTF(var_4_0.tf, "item")
			local var_4_5 = 0

			arg_4_0._event:emit(Fushun3GameEvent.create_platform_item_call, {
				pos = var_4_4.position,
				id = var_4_5
			})
		end

		arg_4_0.fillDistance = arg_4_0.fillDistance + var_4_0.distance

		arg_4_0:fillPlatform()
	end
end

function var_0_0.getPlatform(arg_5_0)
	local var_5_0

	if arg_5_0.powerNum and arg_5_0.powerNum > 0 then
		arg_5_0.powerNum = arg_5_0.powerNum - 1

		if arg_5_0.powerNum <= 15 then
			var_5_0 = arg_5_0:getPowerPlatform()
		else
			var_5_0 = arg_5_0:getRandomPlatform()
		end
	else
		var_5_0 = arg_5_0:getRandomPlatform()
	end

	local var_5_1 = var_5_0.name
	local var_5_2 = var_5_0.distance
	local var_5_3 = var_5_0.monster
	local var_5_4 = var_5_0.high
	local var_5_5 = var_5_0.item
	local var_5_6 = arg_5_0:getPlatformFromPool(var_5_1)

	if not var_5_6 then
		local var_5_7 = tf(instantiate(findTF(arg_5_0._tplTf, var_5_1)))

		var_5_7.localScale = Fushun3GameConst.game_scale_v3

		setParent(var_5_7, arg_5_0._content)

		var_5_6 = {
			name = var_5_1,
			tf = var_5_7,
			distance = var_5_2 * Fushun3GameConst.game_scale,
			monster = var_5_3,
			high = var_5_4,
			item = var_5_5
		}
	end

	return var_5_6
end

function var_0_0.getPowerPlatform(arg_6_0)
	for iter_6_0 = 1, 10 do
		local var_6_0 = arg_6_0.initTimes and math.random(1, arg_6_0._weightTotal) or 1

		for iter_6_1, iter_6_2 in ipairs(arg_6_0.createDatas) do
			if var_6_0 <= iter_6_2.weight and iter_6_2.config.power then
				return iter_6_2.config
			end
		end
	end

	return arg_6_0:getRandomPlatform()
end

function var_0_0.getRandomPlatform(arg_7_0)
	local var_7_0 = arg_7_0.initTimes and math.random(1, arg_7_0._weightTotal) or 1

	for iter_7_0 = 1, #arg_7_0.createDatas do
		local var_7_1 = arg_7_0.createDatas[iter_7_0]

		if var_7_0 <= var_7_1.weight then
			return var_7_1.config
		end
	end
end

function var_0_0.getPlatformFromPool(arg_8_0, arg_8_1)
	for iter_8_0 = 1, #arg_8_0._platformPool do
		if arg_8_0._platformPool[iter_8_0].name == arg_8_1 then
			return table.remove(arg_8_0._platformPool, iter_8_0)
		end
	end

	return nil
end

function var_0_0.removePlatform(arg_9_0)
	for iter_9_0 = #arg_9_0._platforms, 1, -1 do
		local var_9_0 = arg_9_0._platforms[iter_9_0]

		if var_9_0.anchoredX < arg_9_0.moveDistance - Fushun3GameConst.platform_remove then
			setActive(var_9_0.tf, false)
			table.insert(arg_9_0._platformPool, table.remove(arg_9_0._platforms, iter_9_0))
		end
	end
end

function var_0_0.step(arg_10_0)
	arg_10_0.moveDistance = math.abs(arg_10_0._sceneTf.anchoredPosition.x)

	arg_10_0:fillPlatform()
	arg_10_0:removePlatform()
end

function var_0_0.levelUp(arg_11_0)
	arg_11_0.level = arg_11_0.level + 1

	arg_11_0:updateCreateData()
end

function var_0_0.updateDayNight(arg_12_0)
	if arg_12_0.timeFlag ~= Fushun3GameVo.GetTimeFlag() then
		arg_12_0.timeFlag = Fushun3GameVo.GetTimeFlag()

		arg_12_0:changePlatformShow(true)
	end
end

function var_0_0.changePlatformShow(arg_13_0, arg_13_1)
	for iter_13_0 = #arg_13_0._platforms, 1, -1 do
		local var_13_0 = arg_13_0._platforms[iter_13_0].tf

		if arg_13_1 then
			local var_13_1 = GetComponent(var_13_0, typeof(Animator))
			local var_13_2 = Fushun3GameVo.GetTimeFlag() and "day" or "night"

			var_13_1:SetTrigger(var_13_2)
		else
			GetComponent(findTF(var_13_0, "day"), typeof(CanvasGroup)).alpha = Fushun3GameVo.GetTimeFlag() and 1 or 0
			GetComponent(findTF(var_13_0, "night"), typeof(CanvasGroup)).alpha = Fushun3GameVo.GetTimeFlag() and 0 or 1
		end
	end
end

function var_0_0.onPlayerPower(arg_14_0)
	arg_14_0.powerNum = 20
end

function var_0_0.dipose(arg_15_0)
	return
end

return var_0_0
