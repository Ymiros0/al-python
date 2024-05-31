local var_0_0 = class("RawData2ThemeConvertor")

local function var_0_1(arg_1_0, arg_1_1, arg_1_2)
	if arg_1_2:
		return arg_1_0
	elif pg.furniture_data_template[arg_1_0]:
		return BackyardThemeFurniture.GetUniqueId(arg_1_0, 0)
	else
		local var_1_0 = pg.furniture_data_template[arg_1_1].count
		local var_1_1

		if var_1_0 > arg_1_0 - arg_1_1:
			var_1_1 = arg_1_0 - arg_1_1
		elif arg_1_0 > 10000000:
			var_1_1 = arg_1_0 % 10

		return BackyardThemeFurniture.GetUniqueId(arg_1_1, var_1_1)

local function var_0_2(arg_2_0, arg_2_1)
	local var_2_0 = (arg_2_0.shipId or 0) == 1
	local var_2_1 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.child or {}):
		var_2_1[tonumber(iter_2_1.id)] = Vector2(iter_2_1.x, iter_2_1.y)

	return (BackyardThemeFurniture.New({
		id = tonumber(arg_2_0.id),
		position = Vector2(arg_2_0.x, arg_2_0.y),
		dir = arg_2_0.dir,
		child = var_2_1,
		parent = tonumber(arg_2_0.parent),
		floor = arg_2_1,
		isNewStyle = var_2_0
	}))

local function var_0_3(arg_3_0, arg_3_1, arg_3_2)
	assert(pg.furniture_data_template[arg_3_1], arg_3_1)

	local var_3_0 = (pg.furniture_data_template[arg_3_1] or {}).count or 0

	if arg_3_2:
		for iter_3_0 = 0, var_3_0 - 1:
			if arg_3_0 == BackyardThemeFurniture.GetUniqueId(arg_3_1, iter_3_0):
				return True
	elif var_3_0 > arg_3_0 - arg_3_1:
		for iter_3_1 = 0, var_3_0 - 1:
			if arg_3_1 + iter_3_1 == arg_3_0:
				return True
	elif arg_3_0 > 10000000:
		for iter_3_2 = 0, var_3_0 - 1:
			if arg_3_1 * 10000000 + iter_3_2 == arg_3_0:
				return True

	return False

local function var_0_4(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4)
	for iter_4_0, iter_4_1 in ipairs(arg_4_0):
		if var_0_3(iter_4_1.parent, arg_4_2, iter_4_1.isNewStyle) and iter_4_1.SameChildPosition(arg_4_3, arg_4_4) and var_0_3(arg_4_1, iter_4_1.configId, iter_4_1.isNewStyle):
			return iter_4_1

local function var_0_5(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)
	for iter_5_0, iter_5_1 in ipairs(arg_5_0):
		if var_0_3(iter_5_1.parent, arg_5_2, iter_5_1.isNewStyle) and iter_5_1.SameChildPosition(arg_5_3, arg_5_4) and var_0_3(arg_5_1, iter_5_1.configId, True):
			return iter_5_1

def var_0_0.GenFurnitures(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.floor
	local var_6_1 = arg_6_1.mapSize
	local var_6_2 = arg_6_1.skipCheck
	local var_6_3 = {}

	for iter_6_0, iter_6_1 in ipairs(arg_6_1.furniture_put_list):
		table.insert(var_6_3, var_0_2(iter_6_1, var_6_0))

	for iter_6_2, iter_6_3 in ipairs(var_6_3):
		if iter_6_3.AnyChild():
			local var_6_4 = {}

			for iter_6_4, iter_6_5 in pairs(iter_6_3.GetChildList()):
				local var_6_5 = var_0_4(var_6_3, iter_6_4, iter_6_3.configId, iter_6_3.GetPosition(), iter_6_5)

				if var_6_5:
					var_6_4[var_0_1(iter_6_4, var_6_5.configId, var_6_5.isNewStyle)] = iter_6_5

			iter_6_3.SetChildList(var_6_4)

	local function var_6_6(arg_7_0)
		local var_7_0 = {}

		for iter_7_0, iter_7_1 in pairs(arg_7_0.GetChildList()):
			local var_7_1 = var_0_5(var_6_3, iter_7_0, arg_7_0.configId, arg_7_0.GetPosition(), iter_7_1)

			if var_7_1:
				var_7_1.SetUniqueId(iter_7_0)
				table.insert(var_7_0, var_7_1)

		return var_7_0

	local var_6_7 = {}

	for iter_6_6, iter_6_7 in ipairs(var_6_3):
		if not iter_6_7.HasParent():
			table.insert(var_6_7, iter_6_7)

		if iter_6_7.AnyChild():
			for iter_6_8, iter_6_9 in ipairs(var_6_6(iter_6_7)):
				table.insert(var_6_7, iter_6_9)

	local var_6_8 = {}

	for iter_6_10, iter_6_11 in ipairs(var_6_7):
		if iter_6_11.HasParent():
			var_6_8[iter_6_11.id] = True

	for iter_6_12, iter_6_13 in ipairs(var_6_7):
		if not iter_6_13.HasParent():
			for iter_6_14, iter_6_15 in ipairs(iter_6_13.GetAllUniqueId()):
				if not var_6_8[iter_6_15]:
					iter_6_13.SetUniqueId(iter_6_15)

					var_6_8[iter_6_15] = True

					break

	local function var_6_9(arg_8_0, arg_8_1, arg_8_2)
		for iter_8_0, iter_8_1 in ipairs(arg_8_0):
			if iter_8_1.id == arg_8_1:
				iter_8_1.SetParent(arg_8_2)

				break

	for iter_6_16, iter_6_17 in ipairs(var_6_7):
		if iter_6_17.AnyChild():
			for iter_6_18, iter_6_19 in pairs(iter_6_17.GetChildList()):
				var_6_9(var_6_7, iter_6_18, iter_6_17.id)

	local var_6_10 = {}

	for iter_6_20, iter_6_21 in ipairs(var_6_7):
		var_6_10[iter_6_21.id] = iter_6_21

	if not var_6_2:
		arg_6_0.CheckFurnitures(var_6_10, var_6_1)

	return var_6_10

def var_0_0.CheckFurnitures(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = {}

	for iter_9_0, iter_9_1 in pairs(arg_9_1):
		local var_9_1, var_9_2 = CourtYardRawDataChecker.CheckFurniTrue(iter_9_1, arg_9_1, arg_9_2)

		if not var_9_1:
			arg_9_0.CollectionClearIdList(var_9_0, iter_9_1, arg_9_1)

	if #var_9_0 > 0:
		for iter_9_2, iter_9_3 in ipairs(var_9_0):
			if arg_9_1[iter_9_3]:
				arg_9_1[iter_9_3] = None

		arg_9_0.CheckFurnitures(arg_9_1, arg_9_2)

def var_0_0.CollectionClearIdList(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	if arg_10_2.AnyChild():
		for iter_10_0, iter_10_1 in ipairs(arg_10_2.GetChildIdList()):
			CollectionClearIdList(arg_10_1, arg_10_3[iter_10_1], arg_10_3)

	table.insert(arg_10_1, arg_10_2.id)

return var_0_0
