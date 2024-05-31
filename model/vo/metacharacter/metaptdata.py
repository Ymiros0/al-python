local var_0_0 = class("MetaPTData")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.group_id

	arg_1_0.groupID = var_1_0

	local var_1_1 = pg.ship_strengthen_meta[var_1_0]

	assert(var_1_1 != None, "Null MetaShip Strengthen Data, ID." .. var_1_0)

	arg_1_0.targets = var_1_1.target
	arg_1_0.dropList = var_1_1.award_display
	arg_1_0.resId = var_1_1.itemid
	arg_1_0.count = 0
	arg_1_0.level = 0
	arg_1_0.curLevel = arg_1_0.level + 1

def var_0_0.initFromServerData(arg_2_0, arg_2_1):
	arg_2_0.count = arg_2_1.pt or 0

	local var_2_0 = arg_2_1.fetch_list

	if #var_2_0 > 0:
		local var_2_1 = {}

		for iter_2_0, iter_2_1 in ipairs(var_2_0):
			table.insert(var_2_1, iter_2_1)

		table.sort(var_2_1)

		for iter_2_2, iter_2_3 in ipairs(var_2_1):
			if iter_2_3 == arg_2_0.targets[iter_2_2]:
				arg_2_0.level = iter_2_2
			else
				break

	arg_2_0.curLevel = math.min(arg_2_0.level + 1, #arg_2_0.targets)

def var_0_0.update(arg_3_0, arg_3_1):
	arg_3_0.count = arg_3_1.pt or arg_3_0.count
	arg_3_0.level = arg_3_1.level or arg_3_0.level
	arg_3_0.curLevel = arg_3_0.level + 1

def var_0_0.updateLevel(arg_4_0, arg_4_1):
	arg_4_0.level = arg_4_1
	arg_4_0.curLevel = math.min(arg_4_0.level + 1, #arg_4_0.targets)

def var_0_0.addPT(arg_5_0, arg_5_1):
	arg_5_0.count = arg_5_0.count + arg_5_1

def var_0_0.GetResProgress(arg_6_0):
	local var_6_0 = arg_6_0.count
	local var_6_1 = arg_6_0.targets[arg_6_0.curLevel]
	local var_6_2 = var_6_0 / var_6_1

	return var_6_0, var_6_1, var_6_2

def var_0_0.GetLevelProgress(arg_7_0):
	local var_7_0 = arg_7_0.curLevel
	local var_7_1 = #arg_7_0.targets
	local var_7_2 = var_7_0 / var_7_1

	return var_7_0, var_7_1, var_7_2

def var_0_0.CanGetAward(arg_8_0):
	local var_8_0, var_8_1, var_8_2 = arg_8_0.GetResProgress()

	return arg_8_0.CanGetNextAward() and var_8_2 >= 1

def var_0_0.CanGetNextAward(arg_9_0):
	return arg_9_0.level < #arg_9_0.targets

def var_0_0.GetTotalResRequire(arg_10_0):
	return arg_10_0.targets[#arg_10_0.targets]

def var_0_0.IsMaxPt(arg_11_0):
	return arg_11_0.count >= arg_11_0.GetTotalResRequire()

return var_0_0
