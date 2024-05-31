local var_0_0 = class("ActivityExtraCommodity", import(".ActivityCommodity"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.activity_shop_extra

def var_0_0.ShowMaintenanceTime(arg_2_0):
	return arg_2_0.getConfig("end_by_maintenance") == 1

def var_0_0.GetMaintenanceMonthAndDay(arg_3_0):
	local var_3_0 = arg_3_0.getConfig("time")
	local var_3_1 = var_3_0[2][1][2]
	local var_3_2 = var_3_0[2][1][3]

	return var_3_1, var_3_2

return var_0_0
