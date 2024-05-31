local var_0_0 = class("PlayerVitaeEducateBaseCard", import("view.base.BaseEventLogic"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_2)
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._tf = arg_1_1
	arg_1_0._go = arg_1_1.gameObject

def var_0_0.ShowOrHide(arg_2_0, arg_2_1):
	setActive(arg_2_0._tf, arg_2_1)

	if not arg_2_1:
		arg_2_0.Clear()

def var_0_0.Flush(arg_3_0):
	return

def var_0_0.Clear(arg_4_0):
	return

def var_0_0.Dispose(arg_5_0):
	pg.DelegateInfo.Dispose(arg_5_0)
	arg_5_0.Clear()

return var_0_0
