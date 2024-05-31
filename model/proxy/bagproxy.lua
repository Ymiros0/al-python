local var_0_0 = class("BagProxy", import(".NetProxy"))

var_0_0.ITEM_UPDATED = "item updated"

function var_0_0.register(arg_1_0)
	arg_1_0:on(15001, function(arg_2_0)
		arg_1_0.data = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.item_list) do
			local var_2_0 = Item.New({
				id = iter_2_1.id,
				count = iter_2_1.count
			})

			var_2_0:display("loaded")

			arg_1_0.data[var_2_0.id] = var_2_0
		end

		arg_1_0.limitList = {}

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.limit_list) do
			arg_1_0.limitList[iter_2_3.id] = iter_2_3.count
		end

		arg_1_0.extraItemData = {}

		for iter_2_4, iter_2_5 in ipairs(arg_2_0.item_misc_list) do
			arg_1_0.extraItemData[iter_2_5.id] = arg_1_0.extraItemData[iter_2_5.id] or {}

			table.insert(arg_1_0.extraItemData[iter_2_5.id], iter_2_5.data)
		end
	end)
end

function var_0_0.addExtraData(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0.extraItemData[arg_3_1] = arg_3_0.extraItemData[arg_3_1] or {}

	table.insert(arg_3_0.extraItemData[arg_3_1], arg_3_2)
end

function var_0_0.removeExtraData(arg_4_0, arg_4_1, arg_4_2)
	table.removebyvalue(arg_4_0.extraItemData[arg_4_1] or {}, arg_4_2)
end

function var_0_0.addItemById(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	assert(arg_5_2 > 0, "count should greater than zero")

	if arg_5_1 == ITEM_ID_CUBE then
		pg.TrackerMgr.GetInstance():Tracking(TRACKING_CUBE_ADD, arg_5_2)
	end

	arg_5_0:updateItem(arg_5_1, arg_5_2, arg_5_3)
end

function var_0_0.removeItemById(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	assert(arg_6_2 > 0, "count should greater than zero")

	if arg_6_1 == ITEM_ID_CUBE then
		pg.TrackerMgr.GetInstance():Tracking(TRACKING_CUBE_CONSUME, arg_6_2)
	end

	arg_6_0:updateItem(arg_6_1, -arg_6_2, arg_6_3)
end

function var_0_0.getItemsByExclude(arg_7_0)
	local var_7_0 = {}

	for iter_7_0, iter_7_1 in pairs(arg_7_0.data) do
		local var_7_1 = iter_7_1:getConfig("type")

		if not Item.INVISIBLE_TYPE[var_7_1] and iter_7_1.count > 0 then
			if arg_7_0.extraItemData[iter_7_0] then
				local var_7_2 = iter_7_1.count

				for iter_7_2, iter_7_3 in ipairs(arg_7_0.extraItemData[iter_7_0]) do
					table.insert(var_7_0, Item.New({
						count = 1,
						id = iter_7_0,
						extra = iter_7_3
					}))

					var_7_2 = var_7_2 - 1
				end

				if var_7_2 > 0 then
					table.insert(var_7_0, Item.New({
						id = iter_7_0,
						count = var_7_2
					}))
				end
			else
				table.insert(var_7_0, iter_7_1)
			end
		end
	end

	return var_7_0
end

function var_0_0.getItemsByType(arg_8_0, arg_8_1)
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in pairs(arg_8_0.data) do
		if iter_8_1:getConfig("type") == arg_8_1 and iter_8_1.count ~= 0 then
			table.insert(var_8_0, iter_8_1)
		end
	end

	return Clone(var_8_0)
end

function var_0_0.ExitTypeItems(arg_9_0, arg_9_1)
	for iter_9_0, iter_9_1 in pairs(arg_9_0.data) do
		if iter_9_1:getConfig("type") == arg_9_1 and iter_9_1.count > 0 then
			return true
		end
	end

	return false
end

function var_0_0.GetItemsByCondition(arg_10_0, arg_10_1)
	local var_10_0 = {}

	for iter_10_0, iter_10_1 in pairs(arg_10_0.data) do
		local var_10_1 = true

		if arg_10_1 then
			for iter_10_2, iter_10_3 in pairs(arg_10_1) do
				if iter_10_1:getConfig(iter_10_2) ~= iter_10_3 then
					var_10_1 = false

					break
				end
			end
		end

		if var_10_1 then
			table.insert(var_10_0, iter_10_1)
		end
	end

	return var_10_0
end

function var_0_0.getItemById(arg_11_0, arg_11_1)
	if arg_11_0.data[arg_11_1] ~= nil then
		return arg_11_0.data[arg_11_1]:clone()
	end

	return nil
end

function var_0_0.RawGetItemById(arg_12_0, arg_12_1)
	if arg_12_0.data[arg_12_1] ~= nil then
		return arg_12_0.data[arg_12_1]
	end

	return nil
end

function var_0_0.getItemCountById(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_0.data[arg_13_1] and arg_13_0.data[arg_13_1].count or 0

	if arg_13_0.extraItemData[arg_13_1] and #arg_13_0.extraItemData[arg_13_1] > 0 then
		var_13_0 = math.max(var_13_0, 1)
	end

	return var_13_0
end

function var_0_0.getBoxCount(arg_14_0)
	local var_14_0 = arg_14_0:getItemsByType(Item.EQUIPMENT_BOX_TYPE_5)

	return table.getCount(var_14_0)
end

function var_0_0.getCanComposeCount(arg_15_0)
	local var_15_0 = 0
	local var_15_1 = pg.compose_data_template

	for iter_15_0, iter_15_1 in pairs(var_15_1.all) do
		local var_15_2 = var_15_1[iter_15_1].material_id
		local var_15_3 = var_15_1[iter_15_1].material_num
		local var_15_4 = arg_15_0:getItemById(var_15_2)

		if var_15_4 and var_15_3 <= var_15_4.count then
			var_15_0 = var_15_0 + 1
		end
	end

	return var_15_0
end

function var_0_0.updateItem(arg_16_0, arg_16_1, arg_16_2, arg_16_3)
	local var_16_0 = arg_16_0.data[arg_16_1] or Item.New({
		count = 0,
		id = arg_16_1
	})

	var_16_0.count = var_16_0.count + arg_16_2

	assert(var_16_0.count >= 0, "item count error: " .. var_16_0.id)

	if arg_16_3 then
		arg_16_0.extraItemData[arg_16_1] = arg_16_0.extraItemData[arg_16_1] or {}

		for iter_16_0 = -1, arg_16_2, -1 do
			local var_16_1 = table.removebyvalue(arg_16_0.extraItemData[arg_16_1], arg_16_3)

			assert(var_16_1 > 0)
		end

		for iter_16_1 = 1, arg_16_2 do
			table.insert(arg_16_0.extraItemData[arg_16_1], arg_16_3)
		end
	end

	arg_16_0.data[var_16_0.id] = var_16_0

	arg_16_0.data[var_16_0.id]:display("updated")
	arg_16_0.facade:sendNotification(var_0_0.ITEM_UPDATED, var_16_0:clone())
end

function var_0_0.canUpgradeFlagShipEquip(arg_17_0)
	local var_17_0 = getProxy(BayProxy):getEquipment2ByflagShip()

	if var_17_0 then
		for iter_17_0, iter_17_1 in pairs(var_17_0:getConfig("trans_use_item")) do
			local var_17_1 = arg_17_0:getItemById(iter_17_1[1])

			if not var_17_1 or var_17_1.count < iter_17_1[2] then
				return false
			end
		end

		return true
	end
end

function var_0_0.AddLimitCnt(arg_18_0, arg_18_1, arg_18_2)
	arg_18_0.limitList[arg_18_1] = (arg_18_0.limitList[arg_18_1] or 0) + arg_18_2
end

function var_0_0.GetLimitCntById(arg_19_0, arg_19_1)
	return arg_19_0.limitList[arg_19_1] or 0
end

function var_0_0.ClearLimitCnt(arg_20_0, arg_20_1)
	arg_20_0.limitList[arg_20_1] = 0
end

function var_0_0.GetSkinShopDiscountItemList(arg_21_0)
	local var_21_0 = {}

	for iter_21_0, iter_21_1 in pairs(arg_21_0.data) do
		if iter_21_1.count > 0 and iter_21_1:IsSkinShopDiscountType() then
			table.insert(var_21_0, iter_21_1)
		end
	end

	return var_21_0
end

return var_0_0
