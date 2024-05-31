local var_0_0 = class("VirtualBagActivity", import("model.vo.Activity"))

def var_0_0.getVitemNumber(arg_1_0, arg_1_1):
	return arg_1_0.data1KeyValueList[1][arg_1_1] or 0

def var_0_0.addVitemNumber(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.getVitemNumber(arg_2_1)

	arg_2_0.data1KeyValueList[1][arg_2_1] = var_2_0 + arg_2_2

def var_0_0.subVitemNumber(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_0.getVitemNumber(arg_3_1)

	arg_3_0.data1KeyValueList[1][arg_3_1] = math.max(0, var_3_0 - arg_3_2)

def var_0_0.GetAllVitems(arg_4_0):
	return arg_4_0.data1KeyValueList[1]

def var_0_0.GetDropCfgByType(arg_5_0):
	local var_5_0 = arg_5_0 and AcessWithinNull(pg.activity_drop_type[arg_5_0], "activity_id")
	local var_5_1 = var_5_0 and AcessWithinNull(pg.activity_template[var_5_0], "type")
	local var_5_2 = {
		[ActivityConst.ACTIVITY_TYPE_ATELIER_LINK] = AtelierMaterial,
		[ActivityConst.ACTIVITY_TYPE_WORKBENCH] = WorkBenchItem
	}
	local var_5_3

	var_5_3 = var_5_1 and var_5_2[var_5_1]

return var_0_0
