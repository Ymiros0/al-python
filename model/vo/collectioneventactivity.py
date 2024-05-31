local var_0_0 = class("CollectionEventActivity", import(".Activity"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.collections = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.collection_list):
		local var_1_0 = EventInfo.New(iter_1_1)

		var_1_0.SetActivityId(arg_1_0.id)
		table.insert(arg_1_0.collections, var_1_0)

	local var_1_1 = arg_1_0.getConfig("config_data")
	local var_1_2 = arg_1_0.getDayIndex()

	print("collection==============================", var_1_2)

	if #arg_1_0.collections == 0 and var_1_2 > 0 and var_1_2 <= #var_1_1:
		local var_1_3 = var_1_1[var_1_2]

		if not table.contains(arg_1_0.data1_list, var_1_3):
			table.insert(arg_1_0.collections, EventInfo.New({
				finish_time = 0,
				over_time = 0,
				id = var_1_3,
				ship_id_list = {},
				activity_id = arg_1_0.id
			}))

def var_0_0.getDayIndex(arg_2_0):
	local var_2_0 = arg_2_0.data1
	local var_2_1 = pg.TimeMgr.GetInstance()
	local var_2_2 = var_2_1.GetServerTime()

	return var_2_1.DiffDay(var_2_0, var_2_2) + 1

def var_0_0.GetCollectionList(arg_3_0):
	return arg_3_0.collections

return var_0_0
