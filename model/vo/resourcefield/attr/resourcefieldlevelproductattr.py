local var_0_0 = class("ResourceFieldLevelProductAttr", import(".ResourceFieldProductAttr"))

def var_0_0.ReCalcValue(arg_1_0):
	arg_1_0.multiple = arg_1_0.config[arg_1_0.level].hour_time

	var_0_0.super.ReCalcValue(arg_1_0)

return var_0_0
