local var_0_0 = class("WorldMapPort", import("...BaseEntity"))

var_0_0.Fields = {
	config = "table",
	zeroHourTime = "number",
	goods = "table",
	taskIds = "table",
	id = "number",
	expiredTime = "number"
}
var_0_0.EventUpdateTaskIds = "WorldMapPort.UpdateTaskIds"
var_0_0.EventUpdateGoods = "WorldMapPort.EventUpdateGoods"

def var_0_0.Build(arg_1_0):
	arg_1_0.taskIds = {}
	arg_1_0.goods = {}

def var_0_0.Setup(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1
	arg_2_0.config = pg.world_port_data[arg_2_0.id]

	assert(arg_2_0.config, "world_port_data not exist. " .. arg_2_0.id)

def var_0_0.Dispose(arg_3_0):
	arg_3_0.ClearGoods()
	arg_3_0.Clear()

def var_0_0.IsValid(arg_4_0):
	local var_4_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return arg_4_0.expiredTime and var_4_0 <= arg_4_0.expiredTime and arg_4_0.zeroHourTime and var_4_0 <= arg_4_0.zeroHourTime

def var_0_0.UpdateExpiredTime(arg_5_0, arg_5_1):
	arg_5_0.expiredTime = arg_5_1
	arg_5_0.zeroHourTime = pg.TimeMgr.GetInstance().GetNextTime(0, 0, 0)

def var_0_0.UpdateTaskIds(arg_6_0, arg_6_1):
	if arg_6_0.taskIds != arg_6_1:
		arg_6_0.taskIds = arg_6_1

		arg_6_0.DispatchEvent(var_0_0.EventUpdateTaskIds)

def var_0_0.UpdateGoods(arg_7_0, arg_7_1):
	if arg_7_0.goods != arg_7_1:
		arg_7_0.goods = arg_7_1

		local var_7_0 = underscore.filter(arg_7_0.goods, function(arg_8_0)
			return arg_8_0.count > 0)

		nowWorld().GetAtlas().UpdatePortMark(arg_7_0.id, #var_7_0 > 0)
		arg_7_0.DispatchEvent(var_0_0.EventUpdateGoods)

def var_0_0.ClearGoods(arg_9_0):
	WPool.ReturnArray(arg_9_0.goods)

	arg_9_0.goods = {}

def var_0_0.GetRealm(arg_10_0):
	return arg_10_0.config.port_camp

def var_0_0.IsOpen(arg_11_0, arg_11_1, arg_11_2):
	for iter_11_0, iter_11_1 in ipairs(arg_11_0.config.open_condition):
		if iter_11_1[1] == arg_11_1 and arg_11_2 >= iter_11_1[2]:
			return True

	return False

def var_0_0.IsTempPort(arg_12_0):
	return arg_12_0.config.port_camp == 0

return var_0_0
