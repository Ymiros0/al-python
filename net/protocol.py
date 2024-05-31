pg = pg or {}

local var_0_0 = pg

var_0_0.Protocol = class("Protocol")

def var_0_0.Protocol.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	assert(arg_1_1 != None and arg_1_2 != None and arg_1_3 != None, "pg.Protocol.Ctor invalid argument")

	arg_1_0._id = arg_1_1
	arg_1_0._name = arg_1_2
	arg_1_0._object = arg_1_3

def var_0_0.Protocol.GetMessage(arg_2_0):
	assert(arg_2_0._name != None and arg_2_0._object != None, "pg.Protocol.GetMessage object and name must not be None")

	return arg_2_0._object[arg_2_0._name]()

def var_0_0.Protocol.GetId(arg_3_0):
	return arg_3_0._id

def var_0_0.Protocol.GetName(arg_4_0):
	return arg_4_0._name
