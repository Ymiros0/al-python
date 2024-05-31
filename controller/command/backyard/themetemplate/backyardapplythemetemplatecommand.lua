local var_0_0 = class("BackYardApplyThemeTemplateCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.template
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(DormProxy)

	local function var_1_4(arg_2_0, arg_2_1)
		if #arg_2_0 == 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_theme_template_list_is_empty"))

			return
		end

		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0) do
			var_2_0[iter_2_1.id] = iter_2_1
		end

		local var_2_1 = {}

		for iter_2_2, iter_2_3 in pairs(var_2_0) do
			var_2_1[iter_2_3.id] = iter_2_3:ToSaveData()
		end

		pg.m02:sendNotification(GAME.PUT_FURNITURE, {
			furnsPos = var_2_1,
			floor = arg_2_1,
			callback = function(arg_3_0, arg_3_1)
				if arg_3_0 then
					arg_1_0:sendNotification(GAME.BACKYARD_APPLY_THEME_TEMPLATE_DONE)
				else
					pg.TipsMgr.GetInstance():ShowTips(i18n("backyard_apply_theme_template_erro"))
					print(arg_3_1)
				end
			end
		})
	end

	local var_1_5 = 1
	local var_1_6 = var_0_0.GetAllFloorFurnitures()
	local var_1_7 = var_1_1:IsOccupyed(var_1_6, 1)
	local var_1_8 = {}

	if var_1_7 then
		var_1_8 = var_1_1:GetUsableFurnituresForFloor(var_1_6, var_1_5)
	else
		local var_1_9 = var_1_1:GetAllFurniture()

		for iter_1_0, iter_1_1 in pairs(var_1_9) do
			table.insert(var_1_8, iter_1_1)
		end
	end

	var_0_0.WarpList(var_1_8)
	var_1_4(var_1_8, var_1_5)

	if var_1_2 then
		var_1_2(not var_1_7, var_1_8)
	end
end

function var_0_0.GetAllFloorFurnitures()
	local function var_4_0(arg_5_0, arg_5_1)
		local var_5_0 = getProxy(DormProxy):getRawData():GetTheme(arg_5_0)
		local var_5_1 = {}

		if var_5_0 then
			var_5_1 = var_5_0:GetAllFurniture()
		end

		for iter_5_0, iter_5_1 in pairs(var_5_1) do
			arg_5_1[iter_5_1.id] = iter_5_1
		end
	end

	local var_4_1 = {}

	var_4_0(1, var_4_1)
	var_4_0(2, var_4_1)

	return var_4_1
end

function var_0_0.WarpList(arg_6_0)
	local var_6_0 = getProxy(DormProxy):getRawData()
	local var_6_1 = var_6_0:GetMapSize()
	local var_6_2 = var_6_1.x
	local var_6_3 = var_6_1.y
	local var_6_4 = var_6_1.z
	local var_6_5 = var_6_1.w

	local function var_6_6(arg_7_0)
		assert(arg_7_0.position, arg_7_0.id)

		return not arg_7_0:isPaper() and (arg_7_0.position.x < var_6_2 or arg_7_0.position.y < var_6_3)
	end

	local var_6_7 = var_6_0.level
	local var_6_8 = var_6_0:GetPurchasedFurnitures()

	for iter_6_0 = #arg_6_0, 1, -1 do
		local var_6_9 = arg_6_0[iter_6_0]

		if not var_6_9.position or not var_6_8[var_6_9.configId] or var_6_6(var_6_9) then
			table.remove(arg_6_0, iter_6_0)
		end
	end

	table.sort(arg_6_0, function(arg_8_0, arg_8_1)
		if #arg_8_0.child == #arg_8_1.child then
			return arg_8_0.parent > arg_8_1.parent
		else
			return #arg_8_0.child > #arg_8_1.child
		end
	end)

	local var_6_10 = {}

	for iter_6_1, iter_6_2 in ipairs(arg_6_0) do
		var_6_10[iter_6_2.id] = iter_6_2
	end

	local var_6_11 = {}
	local var_6_12 = {}
	local var_6_13 = var_6_0:GetMapSize()

	for iter_6_3, iter_6_4 in ipairs(arg_6_0) do
		local var_6_14, var_6_15 = CourtYardRawDataChecker.CheckFurnitrue(iter_6_4, var_6_10, var_6_13)

		if not var_6_14 and not table.contains(var_6_11, iter_6_4.id) then
			for iter_6_5, iter_6_6 in pairs(iter_6_4.child or {}) do
				table.insert(var_6_11, iter_6_5)
			end

			if iter_6_4.parent ~= 0 then
				if not var_6_12[iter_6_4.parent] then
					var_6_12[iter_6_4.parent] = {}
				end

				table.insert(var_6_12[iter_6_4.parent], iter_6_4.id)
			end

			table.insert(var_6_11, iter_6_4.id)
		end
	end

	for iter_6_7 = #arg_6_0, 1, -1 do
		local var_6_16 = arg_6_0[iter_6_7]

		if table.contains(var_6_11, var_6_16.id) then
			table.remove(arg_6_0, iter_6_7)
		else
			local var_6_17 = var_6_12[var_6_16.id]

			if var_6_17 then
				for iter_6_8, iter_6_9 in pairs(var_6_16.child or {}) do
					if table.contains(var_6_17, iter_6_8) then
						var_6_16.child[iter_6_8] = nil
					end
				end
			end
		end
	end

	GetCanBePutFurnituresForThemeCommand.SortListForPut(arg_6_0)
end

return var_0_0
