local var_0_0 = class("EducateEvent", import("model.vo.BaseVO"))

var_0_0.TYPE_PLAN = 1
var_0_0.TYPE_OPTION = 2
var_0_0.TYPE_BUBBLE = 3

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id

def var_0_0.bindConfigTable(arg_2_0):
	return pg.child_event

def var_0_0.GetPerformance(arg_3_0):
	return arg_3_0.getConfig("performance")

return var_0_0
