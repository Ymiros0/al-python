local var_0_0 = class("BuildShipPool", import(".BaseVO"))

var_0_0.BUILD_POOL_MARK_SPECIAL = "special"
var_0_0.BUILD_POOL_MARK_LIGHT = "light"
var_0_0.BUILD_POOL_MARK_HEAVY = "heavy"
var_0_0.BUILD_POOL_MARK_NEW = "new"

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id

	assert(arg_1_1.mark)

	arg_1_0.mark = arg_1_1.mark

def var_0_0.bindConfigTable(arg_2_0):
	return pg.ship_data_create_material

def var_0_0.GetPoolId(arg_3_0):
	return arg_3_0.configId

def var_0_0.GetSortCode(arg_4_0):
	if arg_4_0.mark == var_0_0.BUILD_POOL_MARK_SPECIAL:
		return 4
	elif arg_4_0.mark == var_0_0.BUILD_POOL_MARK_LIGHT:
		return 2
	elif arg_4_0.mark == var_0_0.BUILD_POOL_MARK_HEAVY:
		return 3
	elif arg_4_0.mark == var_0_0.BUILD_POOL_MARK_NEW:
		return 1
	else
		return 5

def var_0_0.IsActivity(arg_5_0):
	return False

def var_0_0.GetMark(arg_6_0):
	return arg_6_0.mark

return var_0_0
