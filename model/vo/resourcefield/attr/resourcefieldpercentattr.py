local var_0_0 = class("ResourceFieldPercentAttr", import(".ResourceFieldProductAttr"))

def var_0_0.GetProgressDesc(arg_1_0):
	return arg_1_0.value .. "%" .. "/" .. arg_1_0.maxValue .. "%"

def var_0_0.GetAdditionDesc(arg_2_0):
	return arg_2_0.addition .. "%"

return var_0_0
