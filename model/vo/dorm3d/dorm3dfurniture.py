local var_0_0 = class("Dorm3dFurniture", import("model.vo.BaseVO"))

var_0_0.TYPE = {
	DECORATION = 3,
	FLOOR = 2,
	COUCH = 5,
	BED = 4,
	WALLPAPER = 1,
	TABLE = 6
}
var_0_0.TYPE2NAME = {
	"dorm3d_furniTrue_type_wallpaper",
	"dorm3d_furniTrue_type_floor",
	"dorm3d_furniTrue_type_decoration",
	"dorm3d_furniTrue_type_bed",
	"dorm3d_furniTrue_type_couch",
	"dorm3d_furniTrue_type_table"
}

def var_0_0.bindConfigTable(arg_1_0):
	return pg.dorm3d_furniture_template

def var_0_0.Ctor(arg_2_0, arg_2_1):
	var_0_0.super.Ctor(arg_2_0, arg_2_1)

	arg_2_0.slotId = arg_2_0.slotId or 0

def var_0_0.GetSlotID(arg_3_0):
	return arg_3_0.slotId

def var_0_0.SetSlotID(arg_4_0, arg_4_1):
	arg_4_0.slotId = arg_4_1

def var_0_0.GetName(arg_5_0):
	return arg_5_0.getConfig("name")

def var_0_0.GetType(arg_6_0):
	return arg_6_0.getConfig("type")

def var_0_0.GetRarity(arg_7_0):
	return arg_7_0.getConfig("rarity")

def var_0_0.GetTargetSlots(arg_8_0):
	return arg_8_0.getConfig("target_slots")

def var_0_0.GetShipGroupId(arg_9_0):
	return arg_9_0.getConfig("char_id")

def var_0_0.GetIcon(arg_10_0):
	return arg_10_0.getConfig("icon")

def var_0_0.GetModel(arg_11_0):
	return arg_11_0.getConfig("model")

def var_0_0.GetAcesses(arg_12_0):
	local var_12_0 = arg_12_0.getConfig("acesses")

	if var_12_0 == None or var_12_0 == "":
		return {}

	return var_12_0

return var_0_0
