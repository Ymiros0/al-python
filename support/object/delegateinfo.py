pg = pg or {}

local var_0_0 = pg
local var_0_1 = class("DelegateInfo")

var_0_0.DelegateInfo = var_0_1
var_0_1.ClientsInfo = {}

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.ClientsInfo[arg_1_1] = arg_1_0
	arg_1_0.events = {}

def var_0_1.Add(arg_2_0, arg_2_1):
	if arg_2_0 == None:
		return

	local var_2_0 = var_0_1.ClientsInfo[arg_2_0]

	assert(var_2_0, "没有初始化委托处理" .. arg_2_0.__cname)

	if var_2_0:
		var_2_0.AddEventOb(arg_2_1)

def var_0_1.AddEventOb(arg_3_0, arg_3_1):
	arg_3_0.events[arg_3_1] = True

def var_0_1.Dispose(arg_4_0):
	local var_4_0 = var_0_1.ClientsInfo[arg_4_0]

	assert(var_4_0, "没有初始化委托处理" .. arg_4_0.__cname)

	if var_4_0:
		var_4_0.Clear()

	var_0_1.ClientsInfo[arg_4_0] = None

def var_0_1.Clear(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0.events):
		iter_5_0.RemoveAllListeners()

	arg_5_0.events = None
