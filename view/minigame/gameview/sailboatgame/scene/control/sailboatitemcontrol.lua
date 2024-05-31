local var_0_0 = class("SailBoatItemControl")
local var_0_1

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._items = {}
	arg_1_0._itemsPool = {}
	arg_1_0._content = findTF(arg_1_0._tf, "scene/content")
end

function var_0_0.start(arg_2_0)
	arg_2_0:clear()

	arg_2_0._rules = {}

	local var_2_0 = var_0_1.GetRoundData().item_rule

	for iter_2_0 = 1, #var_2_0 do
		local var_2_1 = SailBoatGameConst.item_rule[var_2_0[iter_2_0]]

		table.insert(arg_2_0._rules, {
			time = 0,
			data = var_2_1
		})
	end

	var_0_1.SetGameItems(arg_2_0._items)
end

function var_0_0.step(arg_3_0, arg_3_1)
	local var_3_0 = var_0_1.gameTime

	for iter_3_0 = 1, #arg_3_0._rules do
		local var_3_1 = arg_3_0._rules[iter_3_0]
		local var_3_2 = var_3_1.data.create_time

		if var_3_0 > var_3_2[1] and var_3_0 < var_3_2[2] and var_3_1.time and var_3_1.time >= 0 then
			var_3_1.time = var_3_1.time - arg_3_1

			if var_3_1.time <= 0 then
				var_3_1.time = math.random(var_3_1.data.time[1], var_3_1.data.time[2])

				arg_3_0:applyRule(var_3_1)
			end
		end
	end

	for iter_3_1 = #arg_3_0._items, 1, -1 do
		local var_3_3 = arg_3_0._items[iter_3_1]

		var_3_3:step(arg_3_1)

		if var_3_3:getRemoveFlag() then
			table.remove(arg_3_0._items, iter_3_1)
			arg_3_0:returnItem(var_3_3)
		end
	end

	for iter_3_2 = #arg_3_0._rules, 1, -1 do
		local var_3_4 = arg_3_0._rules[iter_3_2].data

		if var_0_1.gameTime <= var_3_4.create_time[1] then
			table.remove(arg_3_0._rules, iter_3_2)
		end
	end
end

function var_0_0.dispose(arg_4_0)
	return
end

function var_0_0.applyRule(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_1.data
	local var_5_1 = var_5_0.items
	local var_5_2 = var_5_0.screen_pos_x
	local var_5_3 = var_5_0.screen_pos_y
	local var_5_4 = var_5_1[math.random(1, #var_5_1)]
	local var_5_5 = var_0_1.GetRangePos(var_5_2, var_5_3)

	if var_5_5 then
		local var_5_6 = arg_5_0:getOrCreateItem(var_5_4, var_5_5)

		table.insert(arg_5_0._items, var_5_6)
	end
end

function var_0_0.getOrCreateItem(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0

	if #arg_6_0._itemsPool > 0 then
		for iter_6_0 = 1, #arg_6_0._itemsPool do
			if arg_6_0._itemsPool[iter_6_0]:getId() == arg_6_1 then
				var_6_0 = table.remove(arg_6_0._itemsPool, 1)

				break
			end
		end
	end

	if not var_6_0 then
		local var_6_1 = SailBoatGameConst.game_item[arg_6_1]
		local var_6_2 = var_0_1.GetGameItemTf(var_6_1.tpl)

		var_6_0 = SailBoatItem.New(var_6_2, arg_6_0._event)

		var_6_0:setData(var_6_1)
		var_6_0:setContent(arg_6_0._content)
	end

	var_6_0:start()

	if arg_6_2 then
		var_6_0:setPosition(arg_6_2)
	end

	return var_6_0
end

function var_0_0.returnItem(arg_7_0, arg_7_1)
	arg_7_1:clear()
	table.insert(arg_7_0._itemsPool, arg_7_1)
end

function var_0_0.clear(arg_8_0)
	for iter_8_0 = #arg_8_0._items, 1, -1 do
		local var_8_0 = table.remove(arg_8_0._items, iter_8_0)

		var_8_0:clear()
		table.insert(arg_8_0._itemsPool, var_8_0)
	end

	arg_8_0._rules = {}
end

return var_0_0
