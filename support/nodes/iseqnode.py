ys = ys or {}

local var_0_0 = class("ISeqNode")

ys.ISeqNode = var_0_0
var_0_0.Finish = False
var_0_0._init = False
var_0_0._data = None
var_0_0._cfg = None

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._data = arg_1_1
	arg_1_0._cfg = arg_1_2

def var_0_0.UpdateNode(arg_2_0):
	if arg_2_0.Finish:
		return

	if not arg_2_0._init:
		arg_2_0._init = True

		arg_2_0.Init()

	if arg_2_0.Finish:
		return

	arg_2_0.Update()

def var_0_0.Init(arg_3_0):
	return

def var_0_0.Update(arg_4_0):
	return

def var_0_0.Dispose(arg_5_0):
	arg_5_0.Finish = True

	arg_5_0.Clear()

def var_0_0.Clear(arg_6_0):
	return
