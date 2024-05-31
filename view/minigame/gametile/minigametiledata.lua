local var_0_0 = class("MiniGameTileData")

local function var_0_1(arg_1_0)
	local var_1_0 = {}
	local var_1_1 = {}
	local var_1_2 = {}
	local var_1_3 = 1
	local var_1_4 = "{\n"

	while true do
		local var_1_5 = 0

		for iter_1_0, iter_1_1 in pairs(arg_1_0) do
			var_1_5 = var_1_5 + 1
		end

		local var_1_6 = 1

		for iter_1_2, iter_1_3 in pairs(arg_1_0) do
			if var_1_0[arg_1_0] == nil or var_1_6 >= var_1_0[arg_1_0] then
				if string.find(var_1_4, "}", var_1_4:len()) then
					var_1_4 = var_1_4 .. ",\n"
				elseif not string.find(var_1_4, "\n", var_1_4:len()) then
					var_1_4 = var_1_4 .. "\n"
				end

				table.insert(var_1_2, var_1_4)

				var_1_4 = ""

				local var_1_7

				if type(iter_1_2) == "number" or type(iter_1_2) == "boolean" then
					var_1_7 = "[" .. tostring(iter_1_2) .. "]"
				else
					var_1_7 = "['" .. tostring(iter_1_2) .. "']"
				end

				if type(iter_1_3) == "number" or type(iter_1_3) == "boolean" then
					var_1_4 = var_1_4 .. string.rep("\t", var_1_3) .. var_1_7 .. " = " .. tostring(iter_1_3)
				elseif type(iter_1_3) == "table" then
					var_1_4 = var_1_4 .. string.rep("\t", var_1_3) .. var_1_7 .. " = {\n"

					table.insert(var_1_1, arg_1_0)
					table.insert(var_1_1, iter_1_3)

					var_1_0[arg_1_0] = var_1_6 + 1

					break
				else
					var_1_4 = var_1_4 .. string.rep("\t", var_1_3) .. var_1_7 .. " = '" .. tostring(iter_1_3) .. "'"
				end

				if var_1_6 == var_1_5 then
					var_1_4 = var_1_4 .. "\n" .. string.rep("\t", var_1_3 - 1) .. "}"
				else
					var_1_4 = var_1_4 .. ","
				end
			elseif var_1_6 == var_1_5 then
				var_1_4 = var_1_4 .. "\n" .. string.rep("\t", var_1_3 - 1) .. "}"
			end

			var_1_6 = var_1_6 + 1
		end

		if var_1_5 == 0 then
			var_1_4 = var_1_4 .. "\n" .. string.rep("\t", var_1_3 - 1) .. "}"
		end

		if #var_1_1 > 0 then
			arg_1_0 = var_1_1[#var_1_1]
			var_1_1[#var_1_1] = nil
			var_1_3 = var_1_0[arg_1_0] == nil and var_1_3 + 1 or var_1_3 - 1
		else
			break
		end
	end

	table.insert(var_1_2, var_1_4)

	local var_1_8 = table.concat(var_1_2)

	print(var_1_8)
end

function var_0_0.Ctor(arg_2_0, arg_2_1)
	arg_2_0._data = arg_2_1
	arg_2_0._name = arg_2_1.name
	arg_2_0.tileMaps = arg_2_1.tile_map
	arg_2_0.tileDatas = arg_2_1.tile_data
	arg_2_0.tileMapDic = {}
	arg_2_0.tileDataDic = {}

	arg_2_0:initTile()
	arg_2_0:initData()
end

function var_0_0.loadTile(arg_3_0, arg_3_1, arg_3_2)
	local var_3_0 = "GameCfg.MiniGameTile." .. arg_3_1 .. "." .. arg_3_2
	local var_3_1, var_3_2 = pcall(function()
		return require(var_3_0)
	end)

	if not var_3_1 then
		errorMsg("不存在地图数据:" .. var_3_0)
	end

	return var_3_1 and var_3_2
end

function var_0_0.initTile(arg_5_0)
	for iter_5_0, iter_5_1 in ipairs(arg_5_0.tileMaps) do
		local var_5_0 = arg_5_0:loadTile(arg_5_0._name, iter_5_1)
		local var_5_1 = var_5_0.name
		local var_5_2 = var_5_0.tiles

		arg_5_0.tileMapDic[var_5_1] = arg_5_0:createTile(var_5_2)
	end
end

function var_0_0.getTileDataLayer(arg_6_0, arg_6_1)
	if arg_6_0.tileDataDic[arg_6_1] then
		return arg_6_0.tileDataDic[arg_6_1].layers
	end

	return nil
end

function var_0_0.dumpTileDataLayer(arg_7_0, arg_7_1, arg_7_2)
	if arg_7_0.tileDataDic[arg_7_1] then
		local var_7_0 = arg_7_0.tileDataDic[arg_7_1].layers

		for iter_7_0 = 1, #var_7_0 do
			local var_7_1 = var_7_0[iter_7_0]

			if not arg_7_2 or arg_7_2 == var_7_1.name then
				print(var_7_1.name .. " = ")
				var_0_1(var_7_1)
			end
		end
	end
end

function var_0_0.initData(arg_8_0)
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.tileDatas) do
		local var_8_0 = arg_8_0:loadTile(arg_8_0._name, iter_8_1)

		arg_8_0.tileDataDic[iter_8_1] = arg_8_0:createMapData(var_8_0, iter_8_1)
	end
end

function var_0_0.createTile(arg_9_0, arg_9_1)
	local var_9_0 = {}
	local var_9_1 = {}

	for iter_9_0 = 1, #arg_9_1 do
		local var_9_2 = arg_9_1[iter_9_0]
		local var_9_3 = var_9_2.id
		local var_9_4 = var_9_2.properties or {}
		local var_9_5 = var_9_2.image
		local var_9_6

		for iter_9_1 in string.gmatch(var_9_2.image, "[^/]+$") do
			var_9_6 = iter_9_1
		end

		local var_9_7 = string.gsub(var_9_6, ".png", "")
		local var_9_8 = string.gsub(var_9_7, ".jpg", "")

		table.insert(var_9_1, {
			id = var_9_3,
			name = var_9_8,
			properties = var_9_4
		})
	end

	var_9_0.maps = var_9_1

	return var_9_0
end

function var_0_0.createMapData(arg_10_0, arg_10_1, arg_10_2)
	if not arg_10_1 then
		return {
			layer = {},
			tilesets = {}
		}
	end

	local var_10_0 = arg_10_1.tilesets
	local var_10_1 = arg_10_1.layers
	local var_10_2 = arg_10_1.width
	local var_10_3 = arg_10_1.height
	local var_10_4 = {}

	for iter_10_0, iter_10_1 in ipairs(var_10_1) do
		local var_10_5 = iter_10_1.name
		local var_10_6 = iter_10_1.data
		local var_10_7 = arg_10_0:createLayerData(var_10_6, var_10_0, arg_10_2)

		table.insert(var_10_4, {
			name = var_10_5,
			layer = var_10_7,
			width = var_10_2,
			height = var_10_3
		})
	end

	return {
		layers = var_10_4,
		tilesets = var_10_0
	}
end

function var_0_0.createLayerData(arg_11_0, arg_11_1, arg_11_2, arg_11_3)
	local var_11_0 = {}

	for iter_11_0 = 1, #arg_11_1 do
		local var_11_1 = arg_11_1[iter_11_0]
		local var_11_2 = iter_11_0
		local var_11_3 = arg_11_0:relationTile(var_11_1, arg_11_2, arg_11_3, var_11_2)

		if var_11_3 and var_11_1 ~= 0 then
			table.insert(var_11_0, var_11_3)
		end
	end

	return var_11_0
end

function var_0_0.relationTile(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4)
	local var_12_0 = {}

	if arg_12_0._name == MiniGameTile.BOOM_GAME then
		-- block empty
	elseif arg_12_0._name == MiniGameTile.SPRING23_GAME then
		-- block empty
	else
		var_12_0.id = arg_12_1
	end

	var_12_0.item = nil
	var_12_0.drop = nil
	var_12_0.index = arg_12_4

	for iter_12_0 = 1, #arg_12_2 do
		local var_12_1 = arg_12_2[iter_12_0]
		local var_12_2 = var_12_1.firstgid
		local var_12_3 = var_12_1.name
		local var_12_4 = arg_12_0.tileMapDic[var_12_3]

		if var_12_4 then
			local var_12_5 = var_12_4.maps

			if var_12_2 <= arg_12_1 then
				for iter_12_1, iter_12_2 in ipairs(var_12_5) do
					if iter_12_2.id + var_12_2 == arg_12_1 then
						local var_12_6 = arg_12_1
						local var_12_7 = iter_12_2.name
						local var_12_8, var_12_9 = arg_12_0:createGridPropData(iter_12_2.properties, iter_12_2.name, arg_12_3)

						var_12_0.item = var_12_7 or nil
						var_12_0.prop = var_12_8 or nil

						return var_12_0
					end
				end
			end
		else
			print("警告 找不到" .. var_12_3 .. "的贴图数据")
		end
	end

	return var_12_0
end

function var_0_0.createGridPropData(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
	local var_13_0 = {}
	local var_13_1

	if arg_13_0._name == MiniGameTile.BOOM_GAME then
		local var_13_2 = arg_13_1.drop_id
		local var_13_3

		if var_13_2 and var_13_2 > 0 then
			var_13_0.drop = MiniGameTile.drops[var_13_2]
		else
			var_13_0.drop = nil
		end

		if arg_13_1.use_attr and arg_13_1.use_attr ~= nil then
			local var_13_4 = MiniGameTile.attrs[arg_13_3][arg_13_2]

			if var_13_4 then
				for iter_13_0, iter_13_1 in pairs(var_13_4) do
					var_13_0[iter_13_0] = iter_13_1
				end
			end
		end
	elseif arg_13_0._name == MiniGameTile.SPRING23_GAME then
		var_13_0 = nil
	end

	return var_13_0
end

function var_0_0.getName(arg_14_0)
	return arg_14_0._name
end

return var_0_0
