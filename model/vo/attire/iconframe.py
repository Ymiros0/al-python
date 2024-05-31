local var_0_0 = class("IconFrame", import(".AttireFrame"))

def var_0_0.GetIcon(arg_1_0):
	return "IconFrame/" .. arg_1_0

def var_0_0.bindConfigTable(arg_2_0):
	return pg.item_data_frame

def var_0_0.getType(arg_3_0):
	return AttireConst.TYPE_ICON_FRAME

def var_0_0.getDropType(arg_4_0):
	return DROP_TYPE_ICON_FRAME

def var_0_0.getPrefabName(arg_5_0):
	return arg_5_0.getConfig("id")

def var_0_0.getIcon(arg_6_0):
	return var_0_0.GetIcon(arg_6_0.getPrefabName())

return var_0_0
