local var_0_0 = class("DecodeGameModel")

def var_0_0.SetData(arg_1_0, arg_1_1):
	arg_1_0.data = arg_1_1
	arg_1_0.mapId = arg_1_1.mapId
	arg_1_0.unlocks = arg_1_1.unlocks
	arg_1_0.canUseCnt = arg_1_1.canUseCnt
	arg_1_0.passwords = arg_1_1.passwords
	arg_1_0.isFinished = arg_1_1.isFinished
	arg_1_0.mapIndexs = {}

	if arg_1_0.isFinished:
		arg_1_0.BuildMapIndexs()
	else
		for iter_1_0 = 1, #DecodeGameConst.PASSWORD:
			table.insert(arg_1_0.mapIndexs, False)

	arg_1_0.maps = {}

	for iter_1_1 = 1, DecodeGameConst.MAX_MAP_COUNT:
		table.insert(arg_1_0.maps, arg_1_0.InitMap(iter_1_1))

	arg_1_0.SwitchMap(arg_1_1.mapId)

def var_0_0.BuildMapIndexs(arg_2_0):
	local var_2_0 = DecodeGameConst.PASSWORD

	local function var_2_1(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(DecodeGameConst.MAPS_PASSWORD):
			if _.any(iter_3_1, function(arg_4_0)
				return arg_4_0[1] == arg_3_0[1] and arg_4_0[2] == arg_3_0[2]):
				return iter_3_0

	for iter_2_0 = 1, #var_2_0:
		local var_2_2 = var_2_0[iter_2_0]
		local var_2_3 = var_2_1(var_2_2)
		local var_2_4 = DecodeGameConst.Vect2Index(var_2_2[1], var_2_2[2]) + (var_2_3 - 1) * (DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN)

		table.insert(arg_2_0.mapIndexs, var_2_4)

def var_0_0.InitMap(arg_5_0, arg_5_1):
	local function var_5_0(arg_6_0, arg_6_1, arg_6_2)
		local var_6_0 = DecodeGameConst.START_POS[1] + (arg_6_1 - 1) * DecodeGameConst.BLOCK_SIZE[1]
		local var_6_1 = DecodeGameConst.START_POS[2] - (arg_6_0 - 1) * DecodeGameConst.BLOCK_SIZE[2]
		local var_6_2 = table.contains(arg_5_0.unlocks, arg_6_2)

		return {
			isUsed = False,
			index = arg_6_2,
			i = arg_6_0,
			j = arg_6_1,
			position = Vector3(var_6_0, var_6_1, 0),
			isUnlock = var_6_2
		}

	local var_5_1 = {}
	local var_5_2 = (arg_5_1 - 1) * (DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN)
	local var_5_3 = var_5_2

	for iter_5_0 = 1, DecodeGameConst.MAP_ROW:
		for iter_5_1 = 1, DecodeGameConst.MAP_COLUMN:
			var_5_2 = var_5_2 + 1

			local var_5_4 = var_5_0(iter_5_0, iter_5_1, var_5_2)

			table.insert(var_5_1, var_5_4)

	local var_5_5 = arg_5_0.IsUnlockMap(arg_5_1)
	local var_5_6 = arg_5_0.passwords[arg_5_1]
	local var_5_7 = {}

	for iter_5_2 = 1, #var_5_6:
		local var_5_8 = var_5_6[iter_5_2]
		local var_5_9 = var_5_3 + DecodeGameConst.Vect2Index(var_5_8[1], var_5_8[2])

		table.insert(var_5_7, var_5_9)

	return {
		id = arg_5_1,
		items = var_5_1,
		isUnlock = var_5_5,
		password = var_5_6,
		passwordIndexs = var_5_7
	}

def var_0_0.SwitchMap(arg_7_0, arg_7_1):
	arg_7_0.map = arg_7_0.maps[arg_7_1]

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.map.items):
		iter_7_1.isUsed = arg_7_0.IsUsedMapKey(iter_7_1.index)

def var_0_0.ExitMap(arg_8_0):
	arg_8_0.map = None

def var_0_0.UnlockMapItem(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.map

	for iter_9_0, iter_9_1 in ipairs(var_9_0.items):
		if iter_9_1.index == arg_9_1:
			iter_9_1.isUnlock = True

			break

	if not table.contains(arg_9_0.unlocks, arg_9_1):
		table.insert(arg_9_0.unlocks, arg_9_1)

	arg_9_0.canUseCnt = arg_9_0.canUseCnt - 1

def var_0_0.OnRepairMap(arg_10_0):
	arg_10_0.map.isUnlock = True

def var_0_0.IsUnlock(arg_11_0, arg_11_1):
	return _.any(arg_11_0.map.items, function(arg_12_0)
		return arg_12_0.index == arg_11_1 and arg_12_0.isUnlock)

def var_0_0.GetUnlockedCnt(arg_13_0):
	return #arg_13_0.unlocks

def var_0_0.IsUnlockMap(arg_14_0, arg_14_1):
	local var_14_0 = DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN
	local var_14_1 = (arg_14_1 - 1) * var_14_0 + 1
	local var_14_2 = var_14_1 + var_14_0 - 1

	return _.all(_.range(var_14_1, var_14_2), function(arg_15_0)
		return table.contains(arg_14_0.unlocks, arg_15_0))

def var_0_0.GetUnlockMapCnt(arg_16_0):
	local var_16_0 = 0

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.maps):
		if iter_16_1.isUnlock:
			var_16_0 = var_16_0 + 1

	return var_16_0

def var_0_0.CheckIndex(arg_17_0, arg_17_1):
	local var_17_0 = #DecodeGameConst.MAPS_PASSWORD[1]
	local var_17_1 = arg_17_0.GetCurrMapKeyIndex(arg_17_1)
	local var_17_2 = (math.ceil(var_17_1 / var_17_0) - 1) * var_17_0 + 1
	local var_17_3 = var_17_2 + (var_17_0 - 1)

	if var_17_1 == var_17_2:
		return True

	if var_17_2 < var_17_1:
		local var_17_4 = var_17_1 - 1

		if arg_17_0.mapIndexs[var_17_4] != False:
			return True

	return False

def var_0_0.IsUsedMapKey(arg_18_0, arg_18_1):
	return table.contains(arg_18_0.mapIndexs, arg_18_1)

def var_0_0.IsMapKey(arg_19_0, arg_19_1):
	return _.any(arg_19_0.map.passwordIndexs, function(arg_20_0)
		return arg_20_0 == arg_19_1)

def var_0_0.InsertMapKey(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_0.GetCurrMapKeyIndex(arg_21_1)

	arg_21_0.mapIndexs[var_21_0] = arg_21_1

def var_0_0.GetMapKeyStr(arg_22_0, arg_22_1):
	arg_22_1 = arg_22_1 - (arg_22_0.map.id - 1) * (DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN)

	return DecodeGameConst.PASSWORDS[arg_22_1]

def var_0_0.ClearMapKeys(arg_23_0):
	if arg_23_0.isFinished:
		return

	arg_23_0.mapIndexs = _.map(arg_23_0.mapIndexs, function(arg_24_0)
		return False)

def var_0_0.GetCurrMapKeyIndex(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_1 % (DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN)
	local var_25_1, var_25_2 = DecodeGameConst.Index2Vect(var_25_0)
	local var_25_3

	for iter_25_0, iter_25_1 in ipairs(DecodeGameConst.PASSWORD):
		if iter_25_1[1] == var_25_1 and iter_25_1[2] == var_25_2:
			var_25_3 = iter_25_0

			break

	assert(var_25_3)

	return var_25_3

def var_0_0.IsSuccess(arg_26_0):
	return _.all(arg_26_0.mapIndexs, function(arg_27_0)
		return arg_27_0 != False)

def var_0_0.GetMapKeyStrs(arg_28_0):
	return _.map(arg_28_0.mapIndexs, function(arg_29_0)
		if arg_29_0 == False:
			return False

		local var_29_0 = arg_29_0 % (DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN)

		return DecodeGameConst.PASSWORDS[var_29_0])

def var_0_0.GetPassWordProgress(arg_30_0):
	local var_30_0 = 1
	local var_30_1 = {}
	local var_30_2 = 0

	for iter_30_0 = 1, #DecodeGameConst.PASSWORD, DecodeGameConst.MAX_MAP_COUNT:
		local var_30_3 = _.all(_.slice(arg_30_0.mapIndexs, iter_30_0, 3), function(arg_31_0)
			return arg_31_0 != False)

		if var_30_3 == True:
			var_30_2 = var_30_2 + 1

		table.insert(var_30_1, var_30_3)

	return var_30_1, var_30_2

def var_0_0.Finish(arg_32_0):
	arg_32_0.isFinished = True

def var_0_0.CanUnlockAward(arg_33_0):
	local var_33_0 = DecodeGameConst.MAX_MAP_COUNT * DecodeGameConst.MAP_ROW * DecodeGameConst.MAP_COLUMN

	return not arg_33_0.isFinished and var_33_0 <= arg_33_0.GetUnlockedCnt()

def var_0_0.Dispose(arg_34_0):
	return

return var_0_0
