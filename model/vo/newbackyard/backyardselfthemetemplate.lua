local var_0_0 = class("BackYardSelfThemeTemplate", import(".BackYardBaseThemeTemplate"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.floor = arg_1_2 or 1
end

function var_0_0.GetAllFurniture(arg_2_0)
	if not arg_2_0.furnitruesByIds then
		local var_2_0 = arg_2_0:GetRawPutList()

		arg_2_0.furnitruesByIds = arg_2_0:InitFurnitures({
			mapSize = arg_2_0:GetMapSize(),
			floor = arg_2_0.floor,
			furniture_put_list = var_2_0
		})
	end

	return arg_2_0.furnitruesByIds
end

function var_0_0.AddFurniture(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = arg_3_0:GetAllFurniture()
	local var_3_1 = {}

	for iter_3_0, iter_3_1 in pairs(arg_3_1.child) do
		var_3_1[iter_3_0] = iter_3_1
	end

	local var_3_2 = BackyardThemeFurniture.New({
		isNewStyle = true,
		id = arg_3_1.id,
		configId = arg_3_1.configId,
		position = Vector2(arg_3_1.x, arg_3_1.y),
		dir = arg_3_1.dir,
		child = var_3_1,
		parent = arg_3_1.parent,
		floor = arg_3_2
	})

	var_3_0[arg_3_1.id] = var_3_2

	return var_3_2
end

function var_0_0.DeleteFurniture(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0:GetAllFurniture()

	if var_4_0[arg_4_1] then
		var_4_0[arg_4_1] = nil
	end
end

function var_0_0.GetFurniture(arg_5_0, arg_5_1)
	return arg_5_0:GetAllFurniture()[arg_5_1]
end

function var_0_0.GetType(arg_6_0)
	return BackYardConst.THEME_TEMPLATE_USAGE_TYPE_SELF
end

function var_0_0.IsSystem(arg_7_0)
	return false
end

function var_0_0.IsCollected(arg_8_0)
	return true
end

function var_0_0.IsLiked(arg_9_0)
	return true
end

function var_0_0.UnLoad(arg_10_0)
	arg_10_0.time = 0
end

function var_0_0.Upload(arg_11_0)
	arg_11_0.time = pg.TimeMgr.GetInstance():GetServerTime()
end

function var_0_0.CanDispaly(arg_12_0)
	local var_12_0 = arg_12_0:IsPushed()

	return var_12_0 or not var_12_0 and arg_12_0:ExistLocalImage()
end

function var_0_0.IsUsing(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_0:GetWarpFurnitures()
	local var_13_1 = table.getCount(arg_13_1)
	local var_13_2 = table.getCount(var_13_0)

	if var_13_1 ~= var_13_2 then
		return false, Vector2(var_13_1, var_13_2)
	end

	local var_13_3 = {}

	for iter_13_0, iter_13_1 in pairs(arg_13_1) do
		if arg_13_0:IsSystem() and iter_13_1:getConfig("themeId") ~= arg_13_0.id then
			return false, 0
		end

		local var_13_4 = iter_13_1:getConfig("id")

		if not var_13_3[var_13_4] then
			var_13_3[var_13_4] = {}
		end

		table.insert(var_13_3[var_13_4], iter_13_1)
	end

	for iter_13_2, iter_13_3 in pairs(var_13_0) do
		local var_13_5 = arg_13_1[iter_13_3.id]

		if not var_13_5 then
			return false, 1
		end

		if not var_13_5:isPaper() then
			if not var_13_5.position then
				return false, 2
			end

			local var_13_6 = var_13_3[iter_13_3.id] or {}
			local var_13_7 = false

			for iter_13_4, iter_13_5 in ipairs(var_13_6) do
				if iter_13_5:isSame(iter_13_3) then
					var_13_7 = true

					break
				end
			end

			if not var_13_7 then
				return false, 3
			end
		end
	end

	return true
end

function var_0_0.GetMissFurnitures(arg_14_0, arg_14_1)
	local var_14_0 = arg_14_0:GetWarpFurnitures()

	if #arg_14_1 == #var_14_0 then
		return
	end

	local var_14_1 = {}

	local function var_14_2(arg_15_0, arg_15_1)
		for iter_15_0, iter_15_1 in ipairs(arg_15_0) do
			if not arg_15_1[iter_15_1.id] then
				arg_15_1[iter_15_1.id] = 0
			else
				arg_15_1[iter_15_1.id] = arg_15_1[iter_15_1.id] + 1
			end
		end
	end

	local var_14_3 = {}
	local var_14_4 = {}

	var_14_2(var_14_0, var_14_3)
	var_14_2(arg_14_1, var_14_4)

	local function var_14_5(arg_16_0)
		local var_16_0 = pg.furniture_data_template[arg_16_0]

		return {
			count = 1,
			name = var_16_0.name
		}
	end

	for iter_14_0, iter_14_1 in pairs(var_14_3) do
		if not var_14_4[iter_14_0] then
			var_14_1[iter_14_0] = var_14_5(iter_14_0)
		elseif var_14_4[iter_14_0] and iter_14_1 > var_14_4[iter_14_0] then
			if not var_14_1[iter_14_0] then
				var_14_1[iter_14_0] = var_14_5(iter_14_0)
			end

			var_14_1[iter_14_0].count = iter_14_1 - var_14_4[iter_14_0]
		end
	end

	return var_14_1
end

function var_0_0.getName(arg_17_0)
	return arg_17_0:GetName()
end

function var_0_0.getIcon(arg_18_0)
	return "themeicon"
end

return var_0_0
