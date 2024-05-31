local var_0_0 = class("GetCanBePutFurnituresForThemeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.theme
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(DormProxy).floor
	local var_1_4 = var_0_0.GetAllFloorFurnitures()

	if var_1_1.IsOccupyed(var_1_4, var_1_3):
		local var_1_5 = var_1_1.GetUsableFurnituresForFloor(var_1_4, var_1_3)

		var_0_0.SortListForPut(var_1_5)

		if var_1_2:
			var_1_2(False, var_1_5)
	else
		local var_1_6 = var_1_1.GetAllFurniture()
		local var_1_7 = {}

		for iter_1_0, iter_1_1 in pairs(Clone(var_1_6)):
			table.insert(var_1_7, iter_1_1)

		var_0_0.SortListForPut(var_1_7)

		if var_1_2:
			var_1_2(True, var_1_7)

def var_0_0.GetAllFloorFurnitures():
	local var_2_0 = {}

	var_0_0.GetCurrFloorHouse(var_2_0)
	var_0_0.GetOtherFloorHouse(var_2_0)

	return var_2_0

def var_0_0.GetCurrFloorHouse(arg_3_0):
	local var_3_0 = _courtyard.GetController().GetStoreyData()

	for iter_3_0, iter_3_1 in pairs(var_3_0):
		arg_3_0[iter_3_1.id] = var_0_0.StoreyFurniture2ThemeFurniture(iter_3_1)

def var_0_0.StoreyFurniture2ThemeFurniture(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in pairs(arg_4_0.child):
		var_4_0[tonumber(iter_4_0)] = {
			x = iter_4_1.x,
			y = iter_4_1.y
		}

	return BackyardThemeFurniture.New({
		id = tonumber(arg_4_0.id),
		configId = arg_4_0.configId or tonumber(arg_4_0.id),
		position = arg_4_0.position,
		dir = arg_4_0.dir,
		child = var_4_0,
		parent = tonumber(arg_4_0.parent) or 0,
		floor = arg_4_0.floor
	})

def var_0_0.GetOtherFloorHouse(arg_5_0):
	local var_5_0 = var_0_0.GetFurnitureInOtherFloor(getProxy(DormProxy).floor)

	for iter_5_0, iter_5_1 in pairs(var_5_0):
		arg_5_0[iter_5_1.id] = iter_5_1

def var_0_0.GetFurnitureInOtherFloor(arg_6_0):
	local var_6_0 = getProxy(DormProxy).getRawData()
	local var_6_1 = {}

	for iter_6_0, iter_6_1 in pairs(var_6_0.GetThemeList()):
		if arg_6_0 != iter_6_0:
			for iter_6_2, iter_6_3 in pairs(iter_6_1.GetAllFurniture()):
				var_6_1[iter_6_2] = iter_6_3

	return var_6_1

def var_0_0.IsUsing(arg_7_0):
	local var_7_0 = {}
	local var_7_1 = {}

	var_0_0.GetCurrFloorHouse(var_7_0)
	var_0_0.GetOtherFloorHouse(var_7_1)

	return arg_7_0.id != "" and (arg_7_0.IsUsing(var_7_0) or arg_7_0.IsUsing(var_7_1))

def var_0_0.SortListForPut(arg_8_0):
	local var_8_0 = pg.furniture_data_template

	table.sort(arg_8_0, function(arg_9_0, arg_9_1)
		if (arg_9_0.parent != 0 and 1 or 0) == (arg_9_1.parent != 0 and 1 or 0):
			local var_9_0 = var_8_0[arg_9_0.id] and var_8_0[arg_9_0.id].type == Furniture.TYPE_STAGE and 1 or 0
			local var_9_1 = var_8_0[arg_9_1.id] and var_8_0[arg_9_1.id].type == Furniture.TYPE_STAGE and 1 or 0

			if var_9_0 == var_9_1:
				local var_9_2 = table.getCount(arg_9_0.child or {})
				local var_9_3 = table.getCount(arg_9_1.child or {})

				if var_9_2 == var_9_3:
					return arg_9_0.id < arg_9_0.id
				else
					return var_9_3 < var_9_2
			else
				return var_9_1 < var_9_0
		else
			return arg_9_0.parent < arg_9_1.parent)

return var_0_0
