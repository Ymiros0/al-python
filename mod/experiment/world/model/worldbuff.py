local var_0_0 = class("WorldBuff", import("...BaseEntity"))

var_0_0.Fields = {
	config = "table",
	floor = "number",
	time = "number",
	id = "number",
	round = "number",
	step = "number"
}
var_0_0.TrapCompassInterference = 1
var_0_0.TrapVortex = 2
var_0_0.TrapFire = 3
var_0_0.TrapDisturbance = 4
var_0_0.TrapCripple = 5
var_0_0.TrapFrozen = 6

def var_0_0.GetTemplate(arg_1_0):
	assert(pg.world_SLGbuff_data[arg_1_0], "without this buff " .. arg_1_0)

	return pg.world_SLGbuff_data[arg_1_0]

def var_0_0.Setup(arg_2_0, arg_2_1):
	arg_2_0.id = arg_2_1.id
	arg_2_0.config = var_0_0.GetTemplate(arg_2_0.id)

	assert(arg_2_0.config, "world_SLGbuff_data not exist. " .. arg_2_0.id)

	arg_2_0.floor = math.min(arg_2_1.floor, arg_2_0.GetMaxFloor())
	arg_2_0.time = arg_2_1.time != 0 and arg_2_1.time or None
	arg_2_0.round = arg_2_1.round != 0 and arg_2_1.round or None
	arg_2_0.step = arg_2_1.step != 0 and arg_2_1.step or None

def var_0_0.IsValid(arg_3_0):
	return not arg_3_0.time or arg_3_0.time > pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.CheckValid(arg_4_0):
	if not arg_4_0.IsValid():
		arg_4_0.floor = 0

def var_0_0.GetMaxFloor(arg_5_0):
	return arg_5_0.config.buff_maxfloor

def var_0_0.GetTrapType(arg_6_0):
	return arg_6_0.config.trap_type

def var_0_0.GetTrapParams(arg_7_0):
	return arg_7_0.config.trap_parameter

def var_0_0.GetLost(arg_8_0):
	if arg_8_0.step and arg_8_0.round:
		return math.min(arg_8_0.step, arg_8_0.round)
	else
		return arg_8_0.step or arg_8_0.round

def var_0_0.AddFloor(arg_9_0, arg_9_1):
	arg_9_0.CheckValid()

	arg_9_0.floor = math.clamp(arg_9_0.floor + arg_9_1, 0, 999)

def var_0_0.GetFloor(arg_10_0):
	arg_10_0.CheckValid()

	return math.min(arg_10_0.floor, arg_10_0.GetMaxFloor())

return var_0_0
