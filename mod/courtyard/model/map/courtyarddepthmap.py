local var_0_0 = class("CourtYardDepthMap")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.sizeX = arg_1_1
	arg_1_0.sizeY = arg_1_2
	arg_1_0.depths = {}
	arg_1_0.dependInfo = {}
	arg_1_0.allItems = {}
	arg_1_0.sortedFlag = False
	arg_1_0.sortedItems = {}

	arg_1_0.ResetDepth()

def var_0_0.SetAfterFunc(arg_2_0, arg_2_1):
	arg_2_0.afterSortFunc = arg_2_1

def var_0_0.GetDepth(arg_3_0, arg_3_1, arg_3_2):
	return arg_3_0.depths[arg_3_0.GetIndex(arg_3_1, arg_3_2)]

def var_0_0.InsertChar(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.GetDepth(arg_4_1.posX, arg_4_1.posY)

	arg_4_1.SetDepth(var_4_0)

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.sortedItems):
		if var_4_0 > iter_4_1.posZ:
			table.insert(arg_4_0.sortedItems, iter_4_0, arg_4_1)
			arg_4_0.CheckCharByIndex()

			return iter_4_0 - 1

	local var_4_1 = #arg_4_0.sortedItems

	table.insert(arg_4_0.sortedItems, var_4_1 + 1, arg_4_1)
	arg_4_0.CheckCharByIndex()

	return var_4_1

def var_0_0.CheckCharByIndex(arg_5_0):
	for iter_5_0 = 1, #arg_5_0.sortedItems:
		local var_5_0 = math.min(iter_5_0 + 1, #arg_5_0.sortedItems)

		assert(arg_5_0.sortedItems[iter_5_0].posZ >= arg_5_0.sortedItems[var_5_0].posZ, "舰娘插入队列位置错误")

def var_0_0.RemoveChar(arg_6_0, arg_6_1):
	table.removebyvalue(arg_6_0.sortedItems, arg_6_1)

def var_0_0.GetIndex(arg_7_0, arg_7_1, arg_7_2):
	return (arg_7_2 - 1) * arg_7_0.sizeX + arg_7_1

def var_0_0.ResetDepth(arg_8_0):
	local var_8_0 = arg_8_0.depths

	for iter_8_0 = 1, arg_8_0.sizeX:
		for iter_8_1 = 1, arg_8_0.sizeY:
			var_8_0[arg_8_0.GetIndex(iter_8_0, iter_8_1)] = iter_8_0 + iter_8_1 - 1

def var_0_0.AddDepth(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	local var_9_0 = arg_9_0.depths

	for iter_9_0 = 1, arg_9_1:
		for iter_9_1 = 1, arg_9_2:
			local var_9_1 = arg_9_0.GetIndex(iter_9_0, iter_9_1)

			var_9_0[var_9_1] = var_9_0[var_9_1] + arg_9_3

def var_0_0.ModifyDepth(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.depths
	local var_10_1 = arg_10_1.posX
	local var_10_2 = arg_10_1.posY
	local var_10_3 = arg_10_1.maxX
	local var_10_4 = arg_10_1.maxY
	local var_10_5 = var_10_0[arg_10_0.GetIndex(var_10_3, var_10_2)]
	local var_10_6 = var_10_0[arg_10_0.GetIndex(var_10_1, var_10_4)]

	if var_10_5 == var_10_6:
		arg_10_1.SetDepth(var_10_5)

		return

	if var_10_5 < var_10_6:
		if var_10_1 > 1:
			local var_10_7 = var_10_5 - 1 - var_10_0[arg_10_0.GetIndex(var_10_1 - 1, var_10_4)]

			if var_10_7 < 0:
				arg_10_0.AddDepth(var_10_1 - 1, var_10_4, var_10_7)

		arg_10_1.SetDepth(var_10_5)

		return
	else
		if var_10_2 > 1:
			local var_10_8 = var_10_6 - 1 - var_10_0[arg_10_0.GetIndex(var_10_3, var_10_2 - 1)]

			if var_10_8 < 0:
				arg_10_0.AddDepth(var_10_3, var_10_2 - 1, var_10_8)

		arg_10_1.SetDepth(var_10_6)

		return

def var_0_0.PlaceItem(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.maxX
	local var_11_1 = arg_11_1.maxY
	local var_11_2 = arg_11_1.posX
	local var_11_3 = arg_11_1.posY
	local var_11_4 = {}

	arg_11_0.dependInfo[arg_11_1] = var_11_4

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.allItems):
		if var_11_2 <= iter_11_1.maxX and var_11_3 <= iter_11_1.maxY:
			var_11_4[#var_11_4 + 1] = iter_11_1
		elif var_11_0 >= iter_11_1.posX and var_11_1 >= iter_11_1.posY:
			table.insert(arg_11_0.dependInfo[iter_11_1], arg_11_1)

	table.insert(arg_11_0.allItems, arg_11_1)

	arg_11_1.sortedFlag = arg_11_0.sortedFlag

	arg_11_0.SortAndCalcDepth()

	local var_11_5 = arg_11_0.afterSortFunc

	if var_11_5:
		var_11_5(arg_11_0.sortedItems)

def var_0_0.sortItemByDepth(arg_12_0, arg_12_1):
	return arg_12_0.posZ > arg_12_1.posZ

def var_0_0.SortAndCalcDepth(arg_13_0):
	local var_13_0 = {}

	arg_13_0.sortedItems = var_13_0
	arg_13_0.sortedFlag = not arg_13_0.sortedFlag

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.allItems):
		arg_13_0.AddItemAndDepend(iter_13_1)

	arg_13_0.ResetDepth()

	for iter_13_2, iter_13_3 in ipairs(var_13_0):
		arg_13_0.ModifyDepth(iter_13_3)

	table.sort(var_13_0, var_0_0.sortItemByDepth)

def var_0_0.AddItemAndDepend(arg_14_0, arg_14_1):
	if arg_14_1.sortedFlag == arg_14_0.sortedFlag:
		return

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.dependInfo[arg_14_1]):
		arg_14_0.AddItemAndDepend(iter_14_1)

	table.insert(arg_14_0.sortedItems, arg_14_1)
	assert(arg_14_1.sortedFlag != sortedFlag, "依赖关系产生了循环！")

	arg_14_1.sortedFlag = arg_14_0.sortedFlag

def var_0_0.RemoveItem(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_1.posX
	local var_15_1 = arg_15_1.posY
	local var_15_2 = arg_15_1.maxX
	local var_15_3 = arg_15_1.maxY

	table.removebyvalue(arg_15_0.allItems, arg_15_1)

	local var_15_4 = arg_15_0.dependInfo

	var_15_4[arg_15_1] = None

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.allItems):
		if var_15_2 >= iter_15_1.posX and var_15_3 >= iter_15_1.posY:
			table.removebyvalue(var_15_4[iter_15_1], arg_15_1)

	arg_15_0.SortAndCalcDepth()
	table.removebyvalue(arg_15_0.sortedItems, arg_15_1)

return var_0_0
