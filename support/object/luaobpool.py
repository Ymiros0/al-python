pg = pg or {}

local var_0_0 = pg
local var_0_1 = require("Mgr/Pool/PoolUtil")
local var_0_2 = class("LuaObPool")

var_0_0.LuaObPool = var_0_2

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	assert(arg_1_1.Init, "template should have func Init")
	assert(arg_1_1.Recycle, "template should have func Recycle")
	assert(arg_1_1.Dispose, "template should have func Dispose")

	arg_1_0.baseClass = arg_1_1
	arg_1_0.info = arg_1_2
	arg_1_0.list = {}
	arg_1_0.ob2index = {}

	for iter_1_0 = 1, arg_1_3:
		arg_1_0.list[iter_1_0] = arg_1_1.New(arg_1_0, arg_1_2)

	arg_1_0.usedEnd = 0

def var_0_2.GetObject(arg_2_0):
	local var_2_0 = arg_2_0.list
	local var_2_1 = arg_2_0.usedEnd
	local var_2_2

	if var_2_1 >= #var_2_0:
		var_2_0[#var_2_0 + 1] = arg_2_0.baseClass.New(arg_2_0, arg_2_0.info)

	local var_2_3 = var_2_1 + 1
	local var_2_4 = var_2_0[var_2_3]

	arg_2_0.ob2index[var_2_4] = var_2_3
	arg_2_0.usedEnd = var_2_3

	var_2_4.Init()

	return var_2_4

def var_0_2.Recycle(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.ob2index[arg_3_1]
	local var_3_1 = arg_3_0.usedEnd
	local var_3_2 = arg_3_0.list

	arg_3_1.Recycle()

	if var_3_1 != var_3_0:
		local var_3_3 = var_3_2[var_3_1]

		arg_3_0.ob2index[var_3_3] = var_3_0
		var_3_2[var_3_1], var_3_2[var_3_0] = arg_3_1, var_3_3

	arg_3_0.ob2index[arg_3_1] = None
	arg_3_0.usedEnd = var_3_1 - 1

def var_0_2.UpdateInfo(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.info[arg_4_1] = arg_4_2

def var_0_2.Dispose(arg_5_0):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0.list):
		iter_5_1.Dispose()

	arg_5_0.ob2index = None
