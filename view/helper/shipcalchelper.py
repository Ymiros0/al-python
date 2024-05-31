local var_0_0 = class("ShipCalcHelper")

def var_0_0.CalcDestoryRes(arg_1_0):
	local var_1_0 = {}
	local var_1_1 = 0
	local var_1_2 = 0
	local var_1_3 = False

	for iter_1_0, iter_1_1 in ipairs(arg_1_0):
		local var_1_4, var_1_5, var_1_6 = iter_1_1.calReturnRes()

		var_1_1 = var_1_1 + var_1_4
		var_1_2 = var_1_2 + var_1_5
		var_1_0 = table.mergeArray(var_1_0, underscore.map(var_1_6, function(arg_2_0)
			return Drop.Create(arg_2_0)))

	local var_1_7 = PlayerConst.MergeSameDrops(var_1_0)

	for iter_1_2 = #var_1_7, 1, -1:
		local var_1_8 = var_1_7[iter_1_2]

		if var_1_8.type == DROP_TYPE_VITEM and var_1_8.getConfig("virtual_type") == 20:
			local var_1_9, var_1_10 = unpack(pg.gameset.urpt_chapter_max.description)
			local var_1_11 = math.min(var_1_8.count, var_1_10 - getProxy(BagProxy).GetLimitCntById(var_1_9))

			var_1_3 = var_1_11 < var_1_8.count

			if var_1_11 > 0:
				var_1_8.count = var_1_11
			else
				table.remove(var_1_7, iter_1_2)

	for iter_1_3, iter_1_4 in pairs(var_1_7):
		if iter_1_4.count > 0 and iter_1_4.type == DROP_TYPE_VITEM and Item.getConfigData(iter_1_4.id).virtual_type == 20:
			local var_1_12 = iter_1_4.count
			local var_1_13 = pg.gameset.urpt_chapter_max.description
			local var_1_14 = var_1_13[1]
			local var_1_15 = var_1_13[2]
			local var_1_16 = getProxy(BagProxy).GetLimitCntById(var_1_14)
			local var_1_17 = math.min(var_1_15 - var_1_16, var_1_12)

			var_1_3 = var_1_17 < var_1_12

			if var_1_17 <= 0:
				var_1_7[iter_1_3].count = 0
			else
				var_1_7[iter_1_3].count = var_1_17

	table.sort(var_1_7, CompareFuncs({
		function(arg_3_0)
			return arg_3_0.id
	}))

	return var_1_1, var_1_2, var_1_7, var_1_3

def var_0_0.GetEliteAndHightLevelShips(arg_4_0):
	local var_4_0 = {}
	local var_4_1 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0):
		if iter_4_1.getRarity() >= 4:
			table.insert(var_4_0, iter_4_1)
		elif iter_4_1.level > 1:
			table.insert(var_4_1, iter_4_1)

	return var_4_0, var_4_1

def var_0_0.GetEliteAndHightLevelAndResOverflow(arg_5_0, arg_5_1):
	local var_5_0 = _.map(arg_5_0, function(arg_6_0)
		assert(arg_5_1[arg_6_0], arg_6_0)

		return arg_5_1[arg_6_0])
	local var_5_1, var_5_2 = var_0_0.GetEliteAndHightLevelShips(var_5_0)
	local var_5_3, var_5_4, var_5_5, var_5_6 = var_0_0.CalcDestoryRes(var_5_0)

	return var_5_1, var_5_2, var_5_6

return var_0_0
