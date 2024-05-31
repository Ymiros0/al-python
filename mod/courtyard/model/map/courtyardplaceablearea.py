local var_0_0 = class("CourtYardPlaceableArea", import("...CourtYardDispatcher"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.sizeX = arg_1_2.x
	arg_1_0.sizeY = arg_1_2.y
	arg_1_0.minSizeX = arg_1_2.z
	arg_1_0.minSizeY = arg_1_2.w
	arg_1_0.map = {}
	arg_1_0.mats = {}
	arg_1_0.chars = {}

	for iter_1_0 = 0, arg_1_0.sizeX:
		arg_1_0.map[iter_1_0] = {}

		for iter_1_1 = 0, arg_1_0.sizeY:
			arg_1_0.map[iter_1_0][iter_1_1] = False

	arg_1_0.depthMap = CourtYardDepthMap.New(arg_1_0.sizeX + 1, arg_1_0.sizeY + 1)

def var_0_0.GetRange(arg_2_0):
	return Vector4(arg_2_0.sizeX, arg_2_0.sizeY, arg_2_0.minSizeX, arg_2_0.minSizeY)

def var_0_0.GetRangeWithoutWall(arg_3_0):
	return Vector4(arg_3_0.sizeX - 1, arg_3_0.sizeY - 1, arg_3_0.minSizeX, arg_3_0.minSizeY)

def var_0_0.UpdateMinRange(arg_4_0, arg_4_1):
	arg_4_0.minSizeX = arg_4_1.x
	arg_4_0.minSizeY = arg_4_1.y

def var_0_0.LockPosition(arg_5_0, arg_5_1):
	arg_5_0.map[arg_5_1.x][arg_5_1.y] = True

def var_0_0._ClearLockPosition(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.GetMarkPosition()

	if var_6_0:
		arg_6_0.ClearLockPosition(var_6_0)
		arg_6_1.ClearMarkPosition()

def var_0_0.ClearLockPosition(arg_7_0, arg_7_1):
	arg_7_0.map[arg_7_1.x][arg_7_1.y] = False

def var_0_0.AddItem(arg_8_0, arg_8_1):
	assert(isa(arg_8_1, CourtYardDepthItem))

	local var_8_0 = arg_8_1.GetDeathType()

	if var_8_0 == CourtYardConst.DEPTH_TYPE_MAT:
		table.insert(arg_8_0.mats, arg_8_1)
		arg_8_0.DispatchEvent(CourtYardEvent.ADD_MAT_ITEM, arg_8_1)

		return

	if var_8_0 == CourtYardConst.DEPTH_TYPE_SHIP:
		arg_8_0.depthMap.InsertChar(arg_8_1)
		table.insert(arg_8_0.chars, arg_8_1)
	else
		arg_8_0.depthMap.PlaceItem(arg_8_1)

	local var_8_1 = arg_8_1.GetArea()

	for iter_8_0, iter_8_1 in ipairs(var_8_1):
		if arg_8_0.map[iter_8_1.x]:
			arg_8_0.map[iter_8_1.x][iter_8_1.y] = True

	arg_8_0.DispatchEvent(CourtYardEvent.ADD_ITEM, arg_8_1)

def var_0_0.RemoveItem(arg_9_0, arg_9_1):
	assert(isa(arg_9_1, CourtYardDepthItem))

	local var_9_0 = arg_9_1.GetDeathType()

	if var_9_0 == CourtYardConst.DEPTH_TYPE_MAT:
		table.removebyvalue(arg_9_0.mats, arg_9_1)
		arg_9_0.DispatchEvent(CourtYardEvent.REMOVE_MAT_ITEM, arg_9_1)

		return

	local var_9_1 = 1

	if var_9_0 == CourtYardConst.DEPTH_TYPE_SHIP:
		arg_9_0.depthMap.RemoveChar(arg_9_1)

		var_9_1 = table.removebyvalue(arg_9_0.chars, arg_9_1)
	else
		arg_9_0.depthMap.RemoveItem(arg_9_1)

	if var_9_1 > 0:
		local var_9_2 = arg_9_1.GetArea()

		for iter_9_0, iter_9_1 in ipairs(var_9_2):
			if arg_9_0.map[iter_9_1.x]:
				arg_9_0.map[iter_9_1.x][iter_9_1.y] = False

		arg_9_0.DispatchEvent(CourtYardEvent.REMOVE_ITEM, arg_9_1)

def var_0_0.RemoveItemAndRefresh(arg_10_0, arg_10_1):
	local var_10_0 = _.map(arg_10_0.chars, function(arg_11_0)
		return arg_11_0)

	arg_10_0.RemoveItem(arg_10_1)
	_.each(var_10_0, function(arg_12_0)
		arg_10_0.RemoveItem(arg_12_0)
		arg_10_0.AddItem(arg_12_0))

def var_0_0.AddItemAndRefresh(arg_13_0, arg_13_1):
	local var_13_0 = _.map(arg_13_0.chars, function(arg_14_0)
		return arg_14_0)

	arg_13_0.AddItem(arg_13_1)
	_.each(var_13_0, function(arg_15_0)
		arg_13_0.RemoveItem(arg_15_0)
		arg_13_0.AddItem(arg_15_0))

def var_0_0.GetPositions(arg_16_0):
	local var_16_0 = {}

	for iter_16_0, iter_16_1 in pairs(arg_16_0.map):
		for iter_16_2, iter_16_3 in pairs(iter_16_1):
			table.insert(var_16_0, Vector2(iter_16_0, iter_16_2))

	return var_16_0

def var_0_0.IsEmptyPosition(arg_17_0, arg_17_1):
	if not arg_17_0.map[arg_17_1.x]:
		return False

	return arg_17_0.map[arg_17_1.x][arg_17_1.y] == False

def var_0_0.InSide(arg_18_0, arg_18_1):
	return arg_18_1.x >= arg_18_0.minSizeX and arg_18_1.y >= arg_18_0.minSizeY and arg_18_1.x <= arg_18_0.sizeX and arg_18_1.y <= arg_18_0.sizeY

def var_0_0.LegalPosition(arg_19_0, arg_19_1, arg_19_2):
	return arg_19_0.InSide(arg_19_1) and (arg_19_0.IsEmptyPosition(arg_19_1) or arg_19_2.GetDeathType() == CourtYardConst.DEPTH_TYPE_MAT)

def var_0_0.GetItems(arg_20_0):
	return arg_20_0.depthMap.sortedItems

def var_0_0.GetMatItems(arg_21_0):
	table.sort(arg_21_0.mats, function(arg_22_0, arg_22_1)
		local var_22_0 = arg_22_0.GetInitSizeCnt()
		local var_22_1 = arg_22_1.GetInitSizeCnt()

		if var_22_0 == var_22_1:
			local var_22_2 = arg_22_0.GetPosition()
			local var_22_3 = arg_22_1.GetPosition()

			return var_22_2.x + var_22_2.y > var_22_3.x + var_22_3.y
		else
			return var_22_1 < var_22_0)

	return arg_21_0.mats

def var_0_0.GetEmptyPositions(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_0.GetPositions()

	return (_.select(var_23_0, function(arg_24_0)
		return arg_23_0.LegalPosition(arg_24_0, arg_23_1)))

def var_0_0.GetRandomPosition(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.GetEmptyPositions(arg_25_1)

	if #var_25_0 > 0:
		return var_25_0[math.random(1, #var_25_0)]

	return None

def var_0_0.GetEmptyArea(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_1.GetInitSize()

	for iter_26_0, iter_26_1 in ipairs(var_26_0):
		local var_26_1 = arg_26_0._GetEmptyArea(arg_26_1, iter_26_1[1], iter_26_1[2])

		if var_26_1:
			return var_26_1

	return None

def var_0_0._GetEmptyArea(arg_27_0, arg_27_1, arg_27_2, arg_27_3):
	local function var_27_0(arg_28_0)
		local var_28_0 = {}

		for iter_28_0 = arg_28_0.x, arg_28_0.x + arg_27_2 - 1:
			for iter_28_1 = arg_28_0.y, arg_28_0.y + arg_27_3 - 1:
				table.insert(var_28_0, Vector2(iter_28_0, iter_28_1))

		return var_28_0

	for iter_27_0 = arg_27_0.sizeX, arg_27_0.minSizeX, -1:
		for iter_27_1 = arg_27_0.sizeY, arg_27_0.minSizeY, -1:
			local var_27_1 = var_27_0(Vector2(iter_27_0, iter_27_1))

			if _.all(var_27_1, function(arg_29_0)
				return arg_27_0.LegalPosition(arg_29_0, arg_27_1)):
				return Vector2(iter_27_0, iter_27_1)

	return None

def var_0_0._GetNextPositionForMove(arg_30_0, arg_30_1):
	local var_30_0 = arg_30_1.GetAroundPositions()
	local var_30_1 = _.select(var_30_0, function(arg_31_0)
		return arg_30_0.LegalPosition(arg_31_0, arg_30_1))

	if #var_30_1 > 0:
		return var_30_1[math.random(1, #var_30_1)]

	return None

def var_0_0.GetMapNotIncludeItem(arg_32_0, arg_32_1):
	local var_32_0 = arg_32_1.GetAreaByPosition(arg_32_1.GetPosition())
	local var_32_1 = {}

	for iter_32_0, iter_32_1 in pairs(arg_32_0.map):
		var_32_1[iter_32_0] = {}

		for iter_32_2, iter_32_3 in pairs(iter_32_1):
			if table.contains(var_32_0, Vector2(iter_32_0, iter_32_2)):
				var_32_1[iter_32_0][iter_32_2] = False
			else
				var_32_1[iter_32_0][iter_32_2] = iter_32_3

	return var_32_1

def var_0_0.__GetNextPositionForMove(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_0.GetMapNotIncludeItem(arg_33_1)

	local function var_33_1(arg_34_0)
		local var_34_0 = arg_33_1.IsDifferentDirection(arg_34_0)
		local var_34_1

		if var_34_0 and arg_33_0.CanRotateItem(arg_33_1):
			var_34_1 = arg_33_1._GetRotatePositions(arg_34_0)
		else
			var_34_1 = arg_33_1.GetAreaByPosition(arg_34_0)

		return _.all(var_34_1, function(arg_35_0)
			return var_33_0[arg_35_0.x] and var_33_0[arg_35_0.x][arg_35_0.y] == False and arg_33_0.InSide(arg_35_0) and arg_33_1.InActivityRange(arg_35_0))

	local var_33_2 = arg_33_1.GetAroundPositions()
	local var_33_3 = _.select(var_33_2, var_33_1)

	if #var_33_3 > 0:
		return var_33_3[math.random(1, #var_33_3)]

	return None

def var_0_0.GetNextPositionForMove(arg_36_0, arg_36_1):
	if arg_36_1.GetInitSizeCnt() == 1:
		return arg_36_0._GetNextPositionForMove(arg_36_1)
	else
		return arg_36_0.__GetNextPositionForMove(arg_36_1)

def var_0_0.AreaWithInfo(arg_37_0, arg_37_1, arg_37_2, arg_37_3, arg_37_4):
	return (_.map(arg_37_1.GetAreaByPosition(arg_37_2), function(arg_38_0)
		local var_38_0 = arg_37_4 or arg_37_0.LegalPosition(arg_38_0, arg_37_1)

		return {
			flag = var_38_0 and 1 or 2,
			position = arg_38_0,
			offset = arg_37_3
		}))

def var_0_0.CanRotateItem(arg_39_0, arg_39_1):
	if arg_39_1.HasParent():
		return arg_39_1.GetParent().CanRotateChild(arg_39_1)
	elif isa(arg_39_1, CourtYardCanPutFurniture) and arg_39_1.AnyNotRotateChilds():
		return False
	else
		local var_39_0 = arg_39_0.GetMapNotIncludeItem(arg_39_1)

		return _.all(arg_39_1.GetRotatePositions(), function(arg_40_0)
			return var_39_0[arg_40_0.x] and var_39_0[arg_40_0.x][arg_40_0.y] == False and arg_39_0.InSide(arg_40_0) and arg_39_1.InActivityRange(arg_40_0))

def var_0_0.GetAroundEmptyPosition(arg_41_0, arg_41_1):
	local var_41_0 = {}
	local var_41_1 = {}
	local var_41_2 = arg_41_1.GetPosition()

	table.insert(var_41_0, Vector2(var_41_2.x, var_41_2.y - 1))

	while #var_41_0 > 0:
		local var_41_3 = table.remove(var_41_0, 1)

		if arg_41_0.IsEmptyPosition(var_41_3):
			return var_41_3

		table.insert(var_41_1, var_41_3)

		for iter_41_0, iter_41_1 in ipairs({
			Vector2(var_41_3.x, var_41_3.y - 1),
			Vector2(var_41_3.x - 1, var_41_3.y),
			Vector2(var_41_3.x + 1, var_41_3.y),
			Vector2(var_41_3.x, var_41_3.y + 1)
		}):
			if not table.contains(var_41_1, iter_41_1) and arg_41_0.InSide(iter_41_1):
				table.insert(var_41_0, iter_41_1)

	assert(False)

def var_0_0.GetAroundEmptyArea(arg_42_0, arg_42_1, arg_42_2):
	local var_42_0 = arg_42_1.GetInitSize()
	local var_42_1 = var_42_0[1][1]
	local var_42_2 = var_42_0[1][2]
	local var_42_3 = arg_42_0.GetPositions()

	local function var_42_4(arg_43_0, arg_43_1)
		local var_43_0 = arg_43_0.x + arg_43_0.y - (arg_43_1.x + arg_43_1.y)

		return math.abs(var_43_0)

	local var_42_5 = _.map(var_42_3, function(arg_44_0)
		return {
			cost = var_42_4(arg_44_0, arg_42_2),
			value = arg_44_0
		})

	table.sort(var_42_5, function(arg_45_0, arg_45_1)
		return arg_45_0.cost < arg_45_1.cost)

	for iter_42_0, iter_42_1 in ipairs(var_42_5):
		local var_42_6 = iter_42_1.value
		local var_42_7 = arg_42_1.GetAreaByPosition(var_42_6)

		if _.all(var_42_7, function(arg_46_0)
			return arg_42_0.LegalPosition(arg_46_0, arg_42_1)):
			return var_42_6

	return None

def var_0_0.Dispose(arg_47_0):
	arg_47_0.ClearListeners()

return var_0_0
