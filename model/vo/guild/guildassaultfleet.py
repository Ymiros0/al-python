local var_0_0 = class("GuildAssaultFleet", import("..BaseVO"))

def var_0_0.GetRealId(arg_1_0):
	return tonumber(string.split(tostring(arg_1_0), "_")[1])

def var_0_0.GetUserId(arg_2_0):
	return tonumber(string.split(tostring(arg_2_0), "_")[2])

def var_0_0.GetVirtualId(arg_3_0, arg_3_1):
	return arg_3_1 .. "_" .. arg_3_0

def var_0_0.IsSameUserId(arg_4_0, arg_4_1):
	return var_0_0.GetUserId(arg_4_0) == var_0_0.GetUserId(arg_4_1)

def var_0_0.Ctor(arg_5_0, arg_5_1):
	local var_5_0 = {}

	for iter_5_0, iter_5_1 in ipairs(arg_5_1.ships or {}):
		var_5_0[iter_5_0] = GuildAssaultShip.New(iter_5_1)

	arg_5_0.InitShips(arg_5_1.user_id, var_5_0)

def var_0_0.InitShips(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.ships = {}
	arg_6_0.userId = arg_6_1

	for iter_6_0, iter_6_1 in pairs(arg_6_2):
		iter_6_1.id = var_0_0.GetVirtualId(arg_6_0.userId, iter_6_1.id)
		arg_6_0.ships[iter_6_0] = iter_6_1

def var_0_0.ClearAllRecommandShip(arg_7_0):
	for iter_7_0, iter_7_1 in ipairs(arg_7_0.ships):
		arg_7_0.MarkShipBeRecommanded(iter_7_1, False)

def var_0_0.SetRecommendList(arg_8_0, arg_8_1):
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.ships):
		local var_8_0 = var_0_0.GetRealId(iter_8_1.id)

		if _.any(arg_8_1, function(arg_9_0)
			return arg_9_0 == var_8_0):
			arg_8_0.MarkShipBeRecommanded(iter_8_1, True)

def var_0_0.MarkShipBeRecommanded(arg_10_0, arg_10_1, arg_10_2):
	arg_10_1.guildRecommand = arg_10_2

def var_0_0.SetShipBeRecommanded(arg_11_0, arg_11_1, arg_11_2):
	for iter_11_0, iter_11_1 in ipairs(arg_11_0.ships):
		if arg_11_1 == var_0_0.GetRealId(iter_11_1.id):
			arg_11_0.MarkShipBeRecommanded(iter_11_1, arg_11_2)

			break

def var_0_0.GetStrongestShip(arg_12_0, arg_12_1):
	local var_12_0 = {}

	for iter_12_0, iter_12_1 in pairs(arg_12_0.ships):
		if iter_12_1.getTeamType() == arg_12_1:
			table.insert(var_12_0, iter_12_1)

	table.sort(var_12_0, function(arg_13_0, arg_13_1)
		return arg_13_0.level > arg_13_1.level)

	return var_12_0[1]

def var_0_0.GetShipList(arg_14_0):
	return arg_14_0.ships

def var_0_0.IsEmpty(arg_15_0):
	return table.getCount(arg_15_0.ships) == 0

def var_0_0.ExistShip(arg_16_0, arg_16_1):
	for iter_16_0, iter_16_1 in pairs(arg_16_0.ships):
		if arg_16_1 == iter_16_1.id:
			return True

	return False

def var_0_0.GetShipIds(arg_17_0):
	local var_17_0 = {}

	for iter_17_0, iter_17_1 in pairs(arg_17_0.ships):
		table.insert(var_17_0, iter_17_1.id)

	return var_17_0

def var_0_0.GetShipById(arg_18_0, arg_18_1):
	for iter_18_0, iter_18_1 in pairs(arg_18_0.ships):
		if iter_18_1.id == arg_18_1:
			return iter_18_1

def var_0_0.GetShipByRealId(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = var_0_0.GetVirtualId(arg_19_1, arg_19_2)

	for iter_19_0, iter_19_1 in pairs(arg_19_0.ships):
		if iter_19_1.id == var_19_0:
			return iter_19_1

def var_0_0.GetShipByPos(arg_20_0, arg_20_1):
	return arg_20_0.ships[arg_20_1]

def var_0_0.InsertBayShip(arg_21_0, arg_21_1, arg_21_2):
	arg_21_2.id = var_0_0.GetVirtualId(arg_21_0.userId, arg_21_2.id)
	arg_21_0.ships[arg_21_1] = arg_21_2

def var_0_0.AnyShipChanged(arg_22_0, arg_22_1):
	for iter_22_0 = 1, 2:
		if arg_22_0.PositionIsChanged(arg_22_1, iter_22_0):
			return True

	return False

def var_0_0.PositionIsChanged(arg_23_0, arg_23_1, arg_23_2):
	local function var_23_0(arg_24_0, arg_24_1)
		if arg_24_0 and arg_24_1 and arg_24_0.id == arg_24_1.id:
			for iter_24_0, iter_24_1 in ipairs(arg_24_0.equipments):
				local var_24_0 = arg_24_1.equipments[iter_24_0]
				local var_24_1 = iter_24_1 and 1 or 0
				local var_24_2 = var_24_0 and 1 or 0

				if var_24_1 != var_24_2 or var_24_1 == var_24_2 and var_24_1 == 1 and iter_24_1.id != var_24_0.id:
					return True

		return False

	local var_23_1 = arg_23_1.GetShipByPos(arg_23_2)
	local var_23_2 = arg_23_0.GetShipByPos(arg_23_2)

	if (var_23_1 and var_23_1.id or 0) != (var_23_2 and var_23_2.id or 0) or var_23_0(var_23_1, var_23_2):
		return True

	return False

return var_0_0
