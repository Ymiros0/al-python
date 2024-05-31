﻿local var_0_0 = class("Fushun3ItemController")
local var_0_1 = 3
local var_0_2 = 100

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	arg_1_0._sceneTf = arg_1_1
	arg_1_0._charTf = arg_1_2
	arg_1_0._itemTpls = arg_1_3
	arg_1_0._event = arg_1_4
	arg_1_0._charCollider = GetComponent(findTF(arg_1_0._charTf, "collider"), typeof(BoxCollider2D))
	arg_1_0._itemPos = findTF(arg_1_0._sceneTf, "item")
	arg_1_0.weightTotal = 0
	arg_1_0.weightItems = {}
	arg_1_0.items = {}
	arg_1_0.itemPools = {}

	for iter_1_0 = 1, #Fushun3GameConst.item_instance_data do
		local var_1_0 = Fushun3GameConst.item_instance_data[iter_1_0]

		arg_1_0.weightTotal = arg_1_0.weightTotal + var_1_0.weight

		local var_1_1 = arg_1_0.weightTotal
		local var_1_2 = var_1_0.id
		local var_1_3 = var_1_0.map
		local var_1_4 = {
			id = var_1_2,
			weight = var_1_1,
			map = var_1_3
		}

		table.insert(arg_1_0.weightItems, var_1_4)
	end
end

function var_0_0.setCallback(arg_2_0, arg_2_1)
	arg_2_0._callback = arg_2_1
end

function var_0_0.start(arg_3_0)
	for iter_3_0 = #arg_3_0.items, 1, -1 do
		local var_3_0 = table.remove(arg_3_0.items, iter_3_0)

		arg_3_0:returnItemToPool(var_3_0)
	end

	arg_3_0.createTime = math.random(Fushun3GameConst.create_time[1], Fushun3GameConst.create_time[2])
	arg_3_0.createPos = Vector2.zero
	arg_3_0.itemTime = var_0_1
end

function var_0_0.step(arg_4_0)
	arg_4_0:removeOutItems()

	local var_4_0 = arg_4_0._charCollider.bounds
	local var_4_1 = {}

	for iter_4_0 = #arg_4_0.items, 1, -1 do
		local var_4_2 = arg_4_0.items[iter_4_0]

		if var_4_2.collider and var_4_2.data.type ~= Fushun3GameConst.item_type_damage then
			local var_4_3 = var_4_2.collider.bounds

			if Fushun3GameConst.CheckBoxCollider(var_4_0.min, var_4_3.min, var_4_0.size, var_4_3.size) then
				local var_4_4 = table.remove(arg_4_0.items, iter_4_0)

				if var_4_4.data.effect then
					arg_4_0._event:emit(Fushun3GameEvent.add_effect_call, {
						effectName = var_4_4.data.effect,
						targetTf = var_4_4.tf
					})
				end

				if arg_4_0._callback then
					arg_4_0._callback(Fushun3GameEvent.catch_item_call, {
						data = var_4_4.data
					})
				end

				arg_4_0:returnItemToPool(var_4_4)
			end
		end

		if var_4_2.data.speed then
			local var_4_5 = var_4_2.tf.anchoredPosition

			var_4_5.x = var_4_5.x + var_4_2.data.speed * Time.deltaTime
			var_4_2.tf.anchoredPosition = var_4_5
		end

		if var_4_2.data.type == Fushun3GameConst.item_type_damage then
			table.insert(var_4_1, var_4_2)
		end
	end

	for iter_4_1 = #var_4_1, 1, -1 do
		local var_4_6 = var_4_1[iter_4_1]

		arg_4_0._event:emit(Fushun3GameEvent.check_item_damage, {
			collider = var_4_6.collider,
			callback = function(arg_5_0)
				if arg_5_0 then
					pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_BOOM)
					arg_4_0._event:emit(Fushun3GameEvent.add_effect_call, {
						effectName = "EF_fr_Hit_LA",
						targetTf = findTF(var_4_6.tf, "effectPos")
					})
					arg_4_0:removeItem(var_4_6)
				end
			end
		})
	end
end

function var_0_0.removeItem(arg_6_0, arg_6_1)
	for iter_6_0 = #arg_6_0.items, 1, -1 do
		if arg_6_1 == arg_6_0.items[iter_6_0] then
			local var_6_0 = table.remove(arg_6_0.items, iter_6_0)

			arg_6_0:returnItemToPool(var_6_0)

			return
		end
	end
end

function var_0_0.createPlatformItem(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0
	local var_7_1 = arg_7_0:getWeightItemsMap()

	if var_7_1 then
		var_7_0 = Fushun3GameConst.item_map[var_7_1]
	end

	if var_7_0 then
		local var_7_2 = var_7_0.list
		local var_7_3 = arg_7_0._itemPos:InverseTransformPoint(arg_7_1)
		local var_7_4 = 0
		local var_7_5 = 0

		for iter_7_0 = #var_7_2, 1, -1 do
			local var_7_6 = var_7_2[iter_7_0]

			for iter_7_1, iter_7_2 in ipairs(var_7_6) do
				if iter_7_2 and iter_7_2 > 0 then
					arg_7_0:createItemById(iter_7_2, Vector2(var_7_3.x + var_7_5, var_7_3.y + var_7_4))
				end

				var_7_5 = var_7_5 + Fushun3GameConst.item_h
			end

			var_7_5 = 0
			var_7_4 = var_7_4 + Fushun3GameConst.item_v
		end
	end
end

function var_0_0.createItemById(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0

	for iter_8_0 = 1, #Fushun3GameConst.item_data do
		if Fushun3GameConst.item_data[iter_8_0].id == arg_8_1 then
			var_8_0 = Fushun3GameConst.item_data[iter_8_0].name
		end
	end

	local var_8_1 = arg_8_0:getOrCreateItem(var_8_0)

	if var_8_1 then
		setActive(var_8_1.tf, true)

		var_8_1.tf.anchoredPosition = arg_8_2

		table.insert(arg_8_0.items, var_8_1)
	end
end

function var_0_0.createItem(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = arg_9_0:getOrCreateItem(arg_9_1)

	if var_9_0 then
		var_9_0.tf.position = arg_9_2

		setActive(var_9_0.tf, true)
		table.insert(arg_9_0.items, var_9_0)
	end
end

function var_0_0.itemFollow(arg_10_0, arg_10_1)
	for iter_10_0 = 1, #arg_10_0.items do
		local var_10_0 = arg_10_0.items[iter_10_0]

		if var_10_0.data.type == Fushun3GameConst.item_type_buff or var_10_0.data.type == Fushun3GameConst.item_type_score then
			local var_10_1 = var_10_0.tf.anchoredPosition

			if math.abs(arg_10_1.x - var_10_1.x) <= 600 and math.abs(arg_10_1.y - var_10_1.y) <= 700 then
				local var_10_2 = math.sign(arg_10_1.x - var_10_1.x)
				local var_10_3 = 2000 * Time.deltaTime * var_10_2
				local var_10_4 = 25 * math.sign(arg_10_1.y - var_10_1.y)

				if math.abs(arg_10_1.y - var_10_1.y) < 25 then
					var_10_4 = 0
				end

				var_10_1.x = var_10_1.x + var_10_3
				var_10_1.y = var_10_1.y + var_10_4
				var_10_0.tf.anchoredPosition = var_10_1
			end
		end
	end
end

function var_0_0.getOrCreateItem(arg_11_0, arg_11_1)
	for iter_11_0 = 1, #arg_11_0.itemPools do
		if arg_11_0.itemPools[iter_11_0].data.name == arg_11_1 then
			return table.remove(arg_11_0.itemPools, iter_11_0)
		end
	end

	for iter_11_1 = 1, #Fushun3GameConst.item_data do
		local var_11_0 = Clone(Fushun3GameConst.item_data[iter_11_1])

		if var_11_0.name == arg_11_1 then
			local var_11_1 = tf(instantiate(findTF(arg_11_0._itemTpls, arg_11_1)))

			var_11_1.localScale = Fushun3GameConst.game_scale_v3

			local var_11_2 = GetComponent(findTF(var_11_1, "collider"), typeof(BoxCollider2D))

			setParent(var_11_1, arg_11_0._itemPos)

			return {
				tf = var_11_1,
				data = var_11_0,
				collider = var_11_2
			}
		end
	end
end

function var_0_0.getWeightItemsMap(arg_12_0)
	if arg_12_0.itemTime > 0 then
		if math.random(1, arg_12_0.itemTime) == arg_12_0.itemTime then
			arg_12_0.itemTime = var_0_2

			if not arg_12_0.itemsMap then
				arg_12_0.itemsMap = {}

				for iter_12_0 = 1, #arg_12_0.weightItems do
					local var_12_0 = arg_12_0.weightItems[iter_12_0]

					if table.contains(Fushun3GameConst.item_map_ids, var_12_0.map) then
						table.insert(arg_12_0.itemsMap, var_12_0.map)
					end
				end
			end

			return arg_12_0.itemsMap[math.random(1, #arg_12_0.itemsMap)]
		else
			arg_12_0.itemTime = arg_12_0.itemTime - 1
		end
	end

	local var_12_1 = math.random(1, arg_12_0.weightTotal)

	for iter_12_1 = 1, #arg_12_0.weightItems do
		local var_12_2 = arg_12_0.weightItems[iter_12_1]

		if var_12_1 <= var_12_2.weight then
			return var_12_2.map
		end
	end

	return nil
end

function var_0_0.removeOutItems(arg_13_0)
	for iter_13_0 = #arg_13_0.items, 1, -1 do
		local var_13_0 = arg_13_0.items[iter_13_0].tf
		local var_13_1 = arg_13_0.items[iter_13_0].data

		if var_13_0.anchoredPosition.x < math.abs(arg_13_0._sceneTf.anchoredPosition.x) - 1500 then
			local var_13_2 = table.remove(arg_13_0.items, iter_13_0)

			arg_13_0:returnItemToPool(var_13_2)
		elseif var_13_1.type == Fushun3GameConst.item_type_damage and var_13_0.anchoredPosition.x >= math.abs(arg_13_0._sceneTf.anchoredPosition.x) + 2000 then
			local var_13_3 = table.remove(arg_13_0.items, iter_13_0)

			arg_13_0:returnItemToPool(var_13_3)
		elseif var_13_0.anchoredPosition.x >= math.abs(arg_13_0._sceneTf.anchoredPosition.x) + 5000 then
			local var_13_4 = table.remove(arg_13_0.items, iter_13_0)

			arg_13_0:returnItemToPool(var_13_4)
		end
	end
end

function var_0_0.returnItemToPool(arg_14_0, arg_14_1)
	setActive(arg_14_1.tf, false)
	table.insert(arg_14_0.itemPools, arg_14_1)
end

return var_0_0
