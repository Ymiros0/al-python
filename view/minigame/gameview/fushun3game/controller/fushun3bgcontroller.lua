local var_0_0 = class("Fushun3BgController")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5)
	arg_1_0._bgTpl = arg_1_1
	arg_1_0._fireTpl = arg_1_2
	arg_1_0._backSceneTf = arg_1_4
	arg_1_0._petalTpl = arg_1_3
	arg_1_0._event = arg_1_5
	arg_1_0._backBgBottomTf = findTF(arg_1_0._backSceneTf, "bgBottom")
	arg_1_0._backBgMidTf = findTF(arg_1_0._backSceneTf, "bgMid")
	arg_1_0._backBgTopTf = findTF(arg_1_0._backSceneTf, "bgTop")
	arg_1_0._backBgPetalTf = findTF(arg_1_0._backSceneTf, "bgPetal")
	arg_1_0.bgItems = {}
	arg_1_0.bgsPool = {}
	arg_1_0.bgLoops = {}

	for iter_1_0 = 1, #Fushun3GameConst.loop_bg do
		local var_1_0 = arg_1_0:getBgData(Fushun3GameConst.loop_bg[iter_1_0])

		if var_1_0 then
			table.insert(arg_1_0.bgLoops, {
				data = var_1_0,
				pos = Vector2(0, 0)
			})
		end
	end

	arg_1_0._bgAnimTf = findTF(arg_1_0._backSceneTf, "bg/anim")
	arg_1_0.bgAnimator = GetComponent(findTF(arg_1_0._backSceneTf, "bg/anim"), typeof(Animator))
end

function var_0_0.start(arg_2_0)
	arg_2_0:clearBg()

	arg_2_0.fireTime = math.random() * (Fushun3GameConst.fire_time[2] - Fushun3GameConst.fire_time[1]) + Fushun3GameConst.fire_time[1]

	for iter_2_0 = 1, #arg_2_0.bgLoops do
		arg_2_0.bgLoops[iter_2_0].pos = Vector2(0, 0)
	end

	arg_2_0.midBgPosX = 0

	arg_2_0:createMidBg()

	arg_2_0.topBgIds = Clone(Fushun3GameConst.top_bg)
	arg_2_0.topBgIdx = math.random(1, #arg_2_0.topBgIds)
	arg_2_0.topBgPosX = 0
	arg_2_0.petalCount = 0

	for iter_2_1 = arg_2_0.topBgIdx, #arg_2_0.topBgIds do
		arg_2_0:createTopBg(arg_2_0.topBgIds[iter_2_1])
	end

	arg_2_0:changeDayNight(false)
end

function var_0_0.step(arg_3_0)
	if arg_3_0.fireTime > 0 then
		arg_3_0.fireTime = arg_3_0.fireTime - Time.deltaTime

		if arg_3_0.fireTime <= 0 then
			if not Fushun3GameVo.GetTimeFlag() then
				arg_3_0:createFire()
			end

			arg_3_0.fireTime = math.random() * (Fushun3GameConst.fire_time[2] - Fushun3GameConst.fire_time[1]) + Fushun3GameConst.fire_time[1]
		end
	end

	if Fushun3GameVo.GetTimeFlag() and arg_3_0.petalCount < Fushun3GameConst.petal_count_max then
		arg_3_0:createPetal()
	end

	for iter_3_0 = 1, #arg_3_0.bgLoops do
		local var_3_0 = arg_3_0._backBgBottomTf.anchoredPosition
		local var_3_1 = arg_3_0.bgLoops[iter_3_0].data
		local var_3_2 = arg_3_0.bgLoops[iter_3_0].pos
		local var_3_3 = var_3_1.bound.x * Fushun3GameConst.game_scale

		if math.abs(var_3_0.x) + var_3_3 * Fushun3GameConst.loop_nums >= var_3_2.x then
			local var_3_4 = arg_3_0:getBgFromPool(var_3_1.id)

			var_3_4.tf.anchoredPosition = Vector2(var_3_2.x, var_3_1.pos.y)

			setActive(var_3_4.tf, true)
			table.insert(arg_3_0.bgItems, var_3_4)

			var_3_2.x = var_3_2.x + var_3_3
			arg_3_0.bgLoops[iter_3_0].pos = var_3_2
		end
	end

	if arg_3_0.topBgPosX < math.abs(arg_3_0._backBgTopTf.anchoredPosition.x) + Fushun3GameConst.top_bg_inst_posX then
		local var_3_5 = arg_3_0.topBgIds[arg_3_0.topBgIdx]

		arg_3_0:createTopBg(var_3_5)

		if arg_3_0.topBgIdx >= #arg_3_0.topBgIds then
			arg_3_0.topBgIdx = 1
		else
			arg_3_0.topBgIdx = arg_3_0.topBgIdx + 1
		end
	end

	if arg_3_0.midBgPosX < math.abs(arg_3_0._backBgMidTf.anchoredPosition.x) + Fushun3GameConst.mid_bg_inst_posX then
		arg_3_0:createMidBg()
	end

	if arg_3_0.dayTimeCount and arg_3_0.dayTimeCount > 0 then
		arg_3_0.dayTimeCount = arg_3_0.dayTimeCount - Time.deltaTime

		if arg_3_0.dayTimeCount <= 0 then
			Fushun3GameVo.ChangeTimeType(arg_3_0.timeTypeData.next)
			print("切换白天黑夜下一个阶段 = " .. tostring(arg_3_0.timeTypeData.next))
			arg_3_0:changeDayNight(true)
			arg_3_0._event:emit(Fushun3GameEvent.day_night_change)
		end
	end

	for iter_3_1 = 1, #arg_3_0.bgItems do
		local var_3_6 = arg_3_0.bgItems[iter_3_1]

		if var_3_6.data.type == Fushun3GameConst.BG_TYPE_PETAL then
			local var_3_7 = var_3_6.tf.anchoredPosition

			var_3_7.x = var_3_7.x + var_3_6.speed.x * Time.deltaTime
			var_3_7.y = var_3_7.y + var_3_6.speed.y * Time.deltaTime
			var_3_6.tf.anchoredPosition = var_3_7

			if var_3_7.y < Fushun3GameConst.petal_remove_y then
				var_3_6.removeTime = 0
			end
		end
	end

	arg_3_0:removeBg()
end

function var_0_0.changeDayNight(arg_4_0, arg_4_1)
	arg_4_0.timeTypeData = Fushun3GameVo.GetTimeTypeData()
	arg_4_0.dayTimeCount = arg_4_0.timeTypeData.time

	arg_4_0:changeBg(arg_4_1)
	arg_4_0:changeBgItems(arg_4_1)
end

function var_0_0.changeBgItems(arg_5_0, arg_5_1)
	if arg_5_1 and arg_5_0.currentItemTimeFlag == Fushun3GameVo.GetTimeFlag() then
		return
	end

	arg_5_0.currentItemTimeFlag = Fushun3GameVo.GetTimeFlag()

	for iter_5_0 = 1, #arg_5_0.bgItems do
		local var_5_0 = arg_5_0.bgItems[iter_5_0].tf
		local var_5_1 = arg_5_0.bgItems[iter_5_0].data

		if var_5_1.type == Fushun3GameConst.BG_TYPE_FIRE then
			if arg_5_0.bgItems[iter_5_0].removeTime and arg_5_0.currentItemTimeFlag then
				arg_5_0.bgItems[iter_5_0].removeTime = 0
			end
		elseif var_5_1.type == Fushun3GameConst.BG_TYPE_PETAL then
			if arg_5_0.bgItems[iter_5_0].removeTime and not arg_5_0.currentItemTimeFlag then
				arg_5_0.bgItems[iter_5_0].removeTime = 0
			end
		else
			local var_5_2 = GetComponent(var_5_0, typeof(Animator))

			if arg_5_1 then
				local var_5_3 = arg_5_0.currentItemTimeFlag and findTF(var_5_0, "day") or findTF(var_5_0, "night")

				setActive(var_5_3, false)
				setActive(var_5_3, true)

				local var_5_4 = Fushun3GameVo.GetTimeFlag() and "day" or "night"

				var_5_2:SetTrigger(var_5_4)
			else
				local var_5_5 = Fushun3GameVo.GetTimeFlag() and "day_no_fade" or "night_no_fade"

				var_5_2:SetTrigger(var_5_5)
			end
		end
	end
end

function var_0_0.changeBg(arg_6_0, arg_6_1)
	if arg_6_1 then
		arg_6_0.bgAnimator:SetTrigger(arg_6_0.timeTypeData.change_anim)
	else
		setActive(arg_6_0._bgAnimTf, false)
		setActive(arg_6_0._bgAnimTf, true)

		local var_6_0 = arg_6_0._bgAnimTf.childCount

		for iter_6_0 = 0, var_6_0 - 1 do
			local var_6_1 = arg_6_0._bgAnimTf:GetChild(iter_6_0)

			setActive(var_6_1, var_6_1.name == arg_6_0.timeTypeData.tf)
		end

		arg_6_0.bgAnimator:SetTrigger(arg_6_0.timeTypeData.anim)
	end

	print("当前状态" .. tostring(arg_6_0.timeTypeData.name))
end

function var_0_0.createTopBg(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0:getBgData(arg_7_1)

	if var_7_0 then
		local var_7_1 = arg_7_0:getBgFromPool(var_7_0.id)

		var_7_1.tf.anchoredPosition = Vector2(arg_7_0.topBgPosX, var_7_1.data.pos.y)
		arg_7_0.topBgPosX = arg_7_0.topBgPosX + var_7_1.data.bound.x * Fushun3GameConst.game_scale

		setActive(var_7_1.tf, true)
		table.insert(arg_7_0.bgItems, var_7_1)
	end
end

function var_0_0.createMidBg(arg_8_0)
	local var_8_0 = 0

	for iter_8_0 = 1, #Fushun3GameConst.mid_bg do
		local var_8_1 = Fushun3GameConst.mid_bg[iter_8_0]
		local var_8_2 = var_8_1.num
		local var_8_3 = var_8_1.mid_random
		local var_8_4 = Clone(var_8_1.ids)

		for iter_8_1 = 1, var_8_2 do
			local var_8_5 = table.remove(var_8_4, math.random(1, #var_8_4))
			local var_8_6 = arg_8_0:getBgFromPool(var_8_5)

			if var_8_6 then
				if var_8_3 then
					var_8_6.tf.anchoredPosition = Vector2(math.random(900, 1000) + arg_8_0.midBgPosX, var_8_6.data.pos.y)
				else
					var_8_6.tf.anchoredPosition = Vector2(var_8_0 + arg_8_0.midBgPosX, var_8_6.data.pos.y)
					var_8_0 = var_8_0 + var_8_6.data.bound.x * Fushun3GameConst.game_scale
				end

				setActive(var_8_6.tf, true)
				table.insert(arg_8_0.bgItems, var_8_6)
			end
		end
	end

	arg_8_0.midBgPosX = arg_8_0.midBgPosX + Fushun3GameConst.mid_bg_inst_posX
end

function var_0_0.createPetal(arg_9_0)
	local var_9_0 = Fushun3GameConst.petal_ids[math.random(1, #Fushun3GameConst.petal_ids)]
	local var_9_1 = Vector2(math.random(100, 1920), math.random(540, 1080))
	local var_9_2 = arg_9_0:getBgFromPool(var_9_0)

	if var_9_2 then
		var_9_1.x = var_9_1.x + math.abs(var_9_2.parentTf.anchoredPosition.x)
		var_9_1.y = var_9_1.y
		var_9_2.tf.anchoredPosition = var_9_1
		var_9_2.removeTime = math.random(Fushun3GameConst.peta_remove_time[1], Fushun3GameConst.peta_remove_time[2])
		var_9_1.x = var_9_1.x + var_9_2.data.bound.x
		var_9_2.speed = Vector2(Fushun3GameConst.petal_speed[1] + math.random(1, Fushun3GameConst.petal_speed_offset), Fushun3GameConst.petal_speed[2] + math.random(1, Fushun3GameConst.petal_speed_offset))

		setActive(var_9_2.tf, true)
		table.insert(arg_9_0.bgItems, var_9_2)

		arg_9_0.petalCount = arg_9_0.petalCount + 1
	end
end

function var_0_0.createFire(arg_10_0)
	local var_10_0 = Fushun3GameConst.fire_group[math.random(1, #Fushun3GameConst.fire_group)]
	local var_10_1 = Vector2(math.random(100, 1920), 0)

	for iter_10_0 = 1, #var_10_0 do
		local var_10_2 = var_10_0[iter_10_0]
		local var_10_3 = arg_10_0:getBgFromPool(var_10_2)

		if var_10_3 then
			var_10_1.x = var_10_1.x + math.abs(var_10_3.parentTf.anchoredPosition.x)
			var_10_1.y = var_10_3.data.pos.y
			var_10_3.tf.anchoredPosition = var_10_1
			var_10_3.removeTime = Fushun3GameConst.fire_remove
			var_10_1.x = var_10_1.x + var_10_3.data.bound.x

			setActive(var_10_3.tf, true)
			table.insert(arg_10_0.bgItems, var_10_3)
		end
	end
end

function var_0_0.getBgData(arg_11_0, arg_11_1)
	for iter_11_0 = 1, #Fushun3GameConst.bg_data do
		if Fushun3GameConst.bg_data[iter_11_0].id == arg_11_1 then
			return Fushun3GameConst.bg_data[iter_11_0]
		end
	end
end

function var_0_0.getBgFromPool(arg_12_0, arg_12_1)
	for iter_12_0 = 1, #arg_12_0.bgsPool do
		if arg_12_0.bgsPool[iter_12_0].data.id == arg_12_1 then
			return table.remove(arg_12_0.bgsPool, iter_12_0)
		end
	end

	local var_12_0

	for iter_12_1 = 1, #Fushun3GameConst.bg_data do
		local var_12_1 = Fushun3GameConst.bg_data[iter_12_1]

		if var_12_1.id == arg_12_1 then
			var_12_0 = var_12_1
		end
	end

	if var_12_0 then
		local var_12_2
		local var_12_3

		if var_12_0.type == Fushun3GameConst.BG_TYPE_FIRE then
			var_12_2 = tf(instantiate(findTF(arg_12_0._fireTpl, var_12_0.name)))
			var_12_3 = findTF(arg_12_0._backSceneTf, "bgFire")
		elseif var_12_0.type == Fushun3GameConst.BG_TYPE_TOP then
			var_12_2 = tf(instantiate(findTF(arg_12_0._bgTpl, var_12_0.name)))
			var_12_3 = findTF(arg_12_0._backSceneTf, "bgTop")
		elseif var_12_0.type == Fushun3GameConst.BG_TYPE_MID then
			var_12_2 = tf(instantiate(findTF(arg_12_0._bgTpl, var_12_0.name)))
			var_12_3 = findTF(arg_12_0._backSceneTf, "bgMid")
		elseif var_12_0.type == Fushun3GameConst.BG_TYPE_LOOP then
			var_12_2 = tf(instantiate(findTF(arg_12_0._bgTpl, var_12_0.name)))
			var_12_3 = findTF(arg_12_0._backSceneTf, "bgBottom")
		elseif var_12_0.type == Fushun3GameConst.BG_TYPE_PETAL then
			var_12_2 = tf(instantiate(findTF(arg_12_0._petalTpl, var_12_0.name)))
			var_12_3 = findTF(arg_12_0._backSceneTf, "bgPetal")
		end

		if var_12_2 and var_12_3 then
			SetParent(var_12_2, var_12_3)
		end

		return {
			tf = var_12_2,
			data = var_12_0,
			parentTf = var_12_3
		}
	end

	return nil
end

function var_0_0.clearBg(arg_13_0)
	for iter_13_0 = #arg_13_0.bgItems, 1, -1 do
		setActive(arg_13_0.bgItems[iter_13_0].tf, false)
		table.insert(arg_13_0.bgsPool, table.remove(arg_13_0.bgItems, iter_13_0))
	end
end

function var_0_0.removeBg(arg_14_0)
	local var_14_0 = {}

	for iter_14_0 = #arg_14_0.bgItems, 1, -1 do
		local var_14_1 = arg_14_0.bgItems[iter_14_0]

		if var_14_0[var_14_1.parentTf] == nil then
			var_14_0[var_14_1.parentTf] = math.abs(var_14_1.parentTf.anchoredPosition.x) + Fushun3GameConst.bg_remove_posX - var_14_1.data.bound.x * Fushun3GameConst.game_scale
		end

		if var_14_1.removeTime and var_14_1.removeTime > 0 then
			var_14_1.removeTime = var_14_1.removeTime - Time.deltaTime
		end

		if var_14_1.tf.anchoredPosition.x <= var_14_0[var_14_1.parentTf] then
			setActive(var_14_1.tf, false)
			table.insert(arg_14_0.bgsPool, table.remove(arg_14_0.bgItems, iter_14_0))
		elseif var_14_1.removeTime and var_14_1.removeTime <= 0 then
			if var_14_1.data.type == Fushun3GameConst.BG_TYPE_PETAL then
				arg_14_0.petalCount = arg_14_0.petalCount - 1
			end

			setActive(var_14_1.tf, false)
			table.insert(arg_14_0.bgsPool, table.remove(arg_14_0.bgItems, iter_14_0))
		end
	end
end

return var_0_0
