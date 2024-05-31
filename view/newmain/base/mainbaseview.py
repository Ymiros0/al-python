local var_0_0 = class("MainBaseView", import("view.base.BaseEventLogic"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_2)
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._tf = arg_1_1
	arg_1_0._go = arg_1_1.gameObject
	arg_1_0.foldableHelper = MainFoldableHelper.New(arg_1_1, arg_1_0.GetDirection())

def var_0_0.Init(arg_2_0):
	return

def var_0_0.Fold(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.foldableHelper.Fold(arg_3_1, arg_3_2)

def var_0_0.Refresh(arg_4_0):
	return

def var_0_0.Disable(arg_5_0):
	return

def var_0_0.GetDirection(arg_6_0):
	return Vector2.zero

def var_0_0.Dispose(arg_7_0):
	arg_7_0.exited = True

	arg_7_0.disposeEvent()

	if arg_7_0.foldableHelper:
		pg.DelegateInfo.Dispose(arg_7_0)
		arg_7_0.foldableHelper.Dispose()

		arg_7_0.foldableHelper = None

return var_0_0
