local var_0_0 = class("Stage", import(".BaseVO"))

var_0_0.SubmarinStage = 15

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.configId = arg_1_1.id
	arg_1_0.id = arg_1_0.configId
	arg_1_0.score = arg_1_1.score
	arg_1_0.out_time = arg_1_1.out_time or 0

def var_0_0.bindConfigTable(arg_2_0):
	return pg.expedition_data_template

def var_0_0.isFinish(arg_3_0):
	return arg_3_0.score and arg_3_0.score > 1

return var_0_0
