local var_0_0 = class("Notification")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.name = arg_1_1
	arg_1_0.body = arg_1_2
	arg_1_0.type = arg_1_3

def var_0_0.getName(arg_2_0):
	return arg_2_0.name

def var_0_0.setBody(arg_3_0, arg_3_1):
	arg_3_0.body = arg_3_1

def var_0_0.getBody(arg_4_0):
	return arg_4_0.body

def var_0_0.setType(arg_5_0, arg_5_1):
	arg_5_0.type = arg_5_1

def var_0_0.getType(arg_6_0):
	return arg_6_0.type

def var_0_0.toString(arg_7_0):
	return (("Notification Name. " .. arg_7_0.getName()) .. "\nBody. " .. tostring(arg_7_0.getBody())) .. "\nType. " .. arg_7_0.getType()

return var_0_0
