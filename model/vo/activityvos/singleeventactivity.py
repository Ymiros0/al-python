local var_0_0 = class("SingleEventActivity", import("model.vo.Activity"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.eventData = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0.GetAllEventIds()):
		local var_1_0 = SingleEvent.New({
			id = iter_1_1
		})

		if var_1_0.IsMain():
			arg_1_0.eventData[iter_1_1] = var_1_0

	for iter_1_2, iter_1_3 in ipairs(arg_1_0.GetDailyEventIds()):
		local var_1_1 = SingleEvent.New({
			id = iter_1_3
		})

		if var_1_1.IsDaily():
			arg_1_0.eventData[iter_1_3] = var_1_1

def var_0_0.GetEventById(arg_2_0, arg_2_1):
	return arg_2_0.eventData[arg_2_1]

def var_0_0.GetAllEventIds(arg_3_0):
	return arg_3_0.getConfig("config_data")

def var_0_0.GetFinishMainIds(arg_4_0):
	return arg_4_0.data1_list

def var_0_0.AddFinishMainId(arg_5_0, arg_5_1):
	if not table.contains(arg_5_0.GetFinishMainIds(), arg_5_1):
		table.insert(arg_5_0.GetFinishMainIds(), arg_5_1)

def var_0_0.IsFinish(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.GetEventById(arg_6_1)

	if var_6_0.IsMain():
		return table.contains(arg_6_0.GetFinishMainIds(), arg_6_1)

	if var_6_0.IsDaily():
		return table.contains(arg_6_0.GetDailyEventIds(), arg_6_1) and not table.contains(arg_6_0.GetUnFinishDailyIds(), arg_6_1)

	return False

def var_0_0.IsFinishAllMain(arg_7_0):
	for iter_7_0, iter_7_1 in pairs(arg_7_0.eventData):
		if iter_7_1.IsMain() and not arg_7_0.IsFinish(iter_7_1.id):
			return False

	return True

def var_0_0.CheckDailyEventRequest(arg_8_0):
	return #arg_8_0.GetDailyEventIds() == 0

def var_0_0.SetDailyEventIds(arg_9_0, arg_9_1):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.eventData):
		if iter_9_1.IsDaily():
			arg_9_0.eventData[iter_9_0] = None

	arg_9_0.data2_list = {}
	arg_9_0.data3_list = {}

	for iter_9_2, iter_9_3 in ipairs(arg_9_1):
		table.insert(arg_9_0.data2_list, iter_9_3)
		table.insert(arg_9_0.data3_list, iter_9_3)

		local var_9_0 = SingleEvent.New({
			id = iter_9_3
		})

		if var_9_0.IsDaily():
			arg_9_0.eventData[iter_9_3] = var_9_0

def var_0_0.GetDailyEventIds(arg_10_0):
	return arg_10_0.data2_list

def var_0_0.GetUnFinishDailyIds(arg_11_0):
	return arg_11_0.data3_list

def var_0_0.RemoveFinishDailyId(arg_12_0, arg_12_1):
	if table.contains(arg_12_0.GetUnFinishDailyIds(), arg_12_1):
		table.removebyvalue(arg_12_0.GetUnFinishDailyIds(), arg_12_1)

def var_0_0.CheckTrigger(arg_13_0, arg_13_1):
	if not arg_13_0.eventData[arg_13_1]:
		return False

	if arg_13_0.IsFinish(arg_13_1):
		return False

	local var_13_0 = arg_13_0.eventData[arg_13_1].GetPreEventId()

	return var_13_0 == 0 or arg_13_0.IsFinish(var_13_0)

def var_0_0.AddFinishEvent(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0.GetEventById(arg_14_1)

	if var_14_0.IsMain():
		arg_14_0.AddFinishMainId(arg_14_1)

	if var_14_0.IsDaily():
		arg_14_0.RemoveFinishDailyId(arg_14_1)

def var_0_0.GetUnlockMapAreas(arg_15_0):
	local var_15_0 = {}

	underscore.each(arg_15_0.GetFinishMainIds(), function(arg_16_0)
		local var_16_0 = pg.activity_single_event[arg_16_0].map_options

		if var_16_0 == "":
			return

		local var_16_1 = tonumber(var_16_0)

		if not table.contains(var_15_0, var_16_1):
			table.insert(var_15_0, var_16_1))

	return var_15_0

def var_0_0.GetLastShowConfig(arg_17_0):
	local var_17_0 = arg_17_0.GetFinishMainIds()

	if #var_17_0 == 0:
		return {}

	table.sort(var_17_0)

	for iter_17_0 = #var_17_0 - 1, 1, -1:
		local var_17_1 = pg.activity_single_event[var_17_0[iter_17_0]].options

		if #var_17_1 > 0:
			return var_17_1

	return pg.activity_single_event[var_17_0[1]].options

def var_0_0.GetShowConfig(arg_18_0):
	local var_18_0 = arg_18_0.GetFinishMainIds()

	if #var_18_0 == 0:
		return {}

	table.sort(var_18_0)

	for iter_18_0 = #var_18_0, 1, -1:
		local var_18_1 = pg.activity_single_event[var_18_0[iter_18_0]].options

		if #var_18_1 > 0:
			return var_18_1

	return pg.activity_single_event[var_18_0[1]].options

def var_0_0.IsShowMapAnim(arg_19_0, arg_19_1):
	if not arg_19_0.GetEventById(arg_19_1).IsMain():
		return False

	local var_19_0 = arg_19_0.GetFinishMainIds()
	local var_19_1 = arg_19_0.GetUnlockMapAreas()
	local var_19_2 = {}
	local var_19_3 = {}

	for iter_19_0 = 1, #var_19_0 - 1:
		table.insert(var_19_2, var_19_0[iter_19_0])

	underscore.each(var_19_2, function(arg_20_0)
		local var_20_0 = pg.activity_single_event[arg_20_0].map_options

		if var_20_0 == "":
			return

		local var_20_1 = tonumber(var_20_0)

		if not table.contains(var_19_3, var_20_1):
			table.insert(var_19_3, var_20_1))

	return #var_19_1 != #var_19_3

return var_0_0
