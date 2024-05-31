local var_0_0 = class("AcademyCourse", import(".BaseVO"))

var_0_0.MaxStudyTime = 43200

def var_0_0.Ctor(arg_1_0):
	arg_1_0.proficiency = 0

def var_0_0.bindConfigTable(arg_2_0):
	return pg.class_upgrade_group

def var_0_0.getConfig(arg_3_0, arg_3_1):
	local var_3_0 = pg.TimeMgr.GetInstance().GetServerWeek()

	return arg_3_0.bindConfigTable()[var_3_0][arg_3_1]

def var_0_0.update(arg_4_0, arg_4_1):
	arg_4_0.proficiency = arg_4_1.proficiency

def var_0_0.GetProficiency(arg_5_0):
	return arg_5_0.proficiency

def var_0_0.getExtraRate(arg_6_0):
	return pg.TimeMgr.GetInstance().GetServerWeek() == 7 and 2 or 1

def var_0_0.SetProficiency(arg_7_0, arg_7_1):
	arg_7_0.proficiency = arg_7_1

return var_0_0
