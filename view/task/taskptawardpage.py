local var_0_0 = class("TaskPtAwardPage", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ActivitybonusWindow"

def var_0_0.Display(arg_2_0, arg_2_1):
	if not arg_2_0.window:
		arg_2_0.window = TaskPtAwardWindow.New(arg_2_0._tf, arg_2_0)

	arg_2_0.window.Show(arg_2_1)
	arg_2_0.Show()

def var_0_0.OnDestroy(arg_3_0):
	if arg_3_0.window:
		arg_3_0.window.Dispose()

		arg_3_0.window = None

return var_0_0
