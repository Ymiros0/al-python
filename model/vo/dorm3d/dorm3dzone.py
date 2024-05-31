local var_0_0 = class("Dorm3dZone", import("model.vo.BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.dorm3d_zone_template

def var_0_0.GetName(arg_2_0):
	return arg_2_0.getConfig("name")

def var_0_0.GetShipGroupId(arg_3_0):
	return arg_3_0.getConfig("char_id")

def var_0_0.IsGlobal(arg_4_0):
	return arg_4_0.getConfig("is_global") == 1

def var_0_0.GetWatchCameraName(arg_5_0):
	return arg_5_0.getConfig("watch_camera")

def var_0_0.GetSlotIDList(arg_6_0):
	return pg.dorm3d_furniture_slot_template.get_id_list_by_zone_id[arg_6_0.configId] or {}

def var_0_0.SetSlots(arg_7_0, arg_7_1):
	arg_7_0.slots = arg_7_1

def var_0_0.GetSlots(arg_8_0):
	return arg_8_0.slots or {}

def var_0_0.GetTypePriorities(arg_9_0):
	local var_9_0 = arg_9_0.getConfig("type_prioritys")

	if var_9_0 == None or var_9_0 == "":
		return {}

	return var_9_0

def var_0_0.SortTypes(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.GetTypePriorities()

	table.sort(arg_10_1, CompareFuncs({
		function(arg_11_0)
			return table.indexof(var_10_0, arg_11_0) or 99,
		function(arg_12_0)
			return -arg_12_0
	}))

return var_0_0
