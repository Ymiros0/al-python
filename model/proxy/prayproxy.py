local var_0_0 = class("Prayproxy", import(".NetProxy"))

var_0_0.STATE_HOME = 1
var_0_0.STATE_SELECT_POOL = 2
var_0_0.STAGE_SELECT_SHIP = 3
var_0_0.STAGE_BUILD_SUCCESS = 4

def var_0_0.register(arg_1_0):
	arg_1_0.selectedPoolType = None
	arg_1_0.selectedShipCount = 0
	arg_1_0.needSelectShipCount = None
	arg_1_0.selectedShipIDList = {}
	arg_1_0.pageState = var_0_0.STATE_HOME
	arg_1_0.tagConstructed = False

def var_0_0.setSelectedPoolNum(arg_2_0, arg_2_1):
	arg_2_0.selectedPoolType = arg_2_1

def var_0_0.setSelectedShipList(arg_3_0, arg_3_1):
	arg_3_0.selectedShipIDList = arg_3_1

def var_0_0.updateSelectedPool(arg_4_0, arg_4_1):
	arg_4_0.selectedPoolType = arg_4_1
	arg_4_0.needSelectShipCount = pg.activity_ship_create[arg_4_1].pickup_num
	arg_4_0.selectedShipCount = 0
	arg_4_0.selectedShipIDList = {}

def var_0_0.updatePageState(arg_5_0, arg_5_1):
	if arg_5_1 != var_0_0.STATE_HOME and arg_5_1 != var_0_0.STATE_SELECT_POOL and arg_5_1 != var_0_0.STAGE_SELECT_SHIP and arg_5_1 != var_0_0.STAGE_BUILD_SUCCESS:
		assert(False, "没有定义的pageState参数" .. arg_5_1)

	arg_5_0.pageState = arg_5_1

def var_0_0.insertSelectedShipIDList(arg_6_0, arg_6_1):
	if arg_6_0.selectedShipCount == arg_6_0.needSelectShipCount:
		assert(False, "已选舰娘已经达到上限,不允许插入")

	arg_6_0.selectedShipIDList[#arg_6_0.selectedShipIDList + 1] = arg_6_1
	arg_6_0.selectedShipCount = arg_6_0.selectedShipCount + 1

def var_0_0.removeSelectedShipIDList(arg_7_0, arg_7_1):
	if arg_7_0.selectedShipCount == 0:
		assert(False, "没有已选舰娘,不允许删除")

	local var_7_0

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.selectedShipIDList):
		if iter_7_1 == arg_7_1:
			var_7_0 = iter_7_0

			table.remove(arg_7_0.selectedShipIDList, iter_7_0)

			arg_7_0.selectedShipCount = arg_7_0.selectedShipCount - 1

	if not var_7_0:
		assert(False, "已选列表不存在该ID的舰娘")

def var_0_0.getPageState(arg_8_0):
	return arg_8_0.pageState

def var_0_0.getSelectedPoolType(arg_9_0):
	return arg_9_0.selectedPoolType

def var_0_0.getSelectedShipIDList(arg_10_0):
	return arg_10_0.selectedShipIDList

def var_0_0.getSelectedShipCount(arg_11_0):
	return arg_11_0.selectedShipCount

return var_0_0
