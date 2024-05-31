local var_0_0 = class("MainBasePanel", import(".MainBaseView"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.contextData = arg_1_3
	arg_1_0.btns = arg_1_0.GetBtns()

	arg_1_0.Register()

def var_0_0.Init(arg_2_0):
	for iter_2_0, iter_2_1 in ipairs(arg_2_0.btns):
		onButton(arg_2_0, iter_2_1.GetTarget(), function()
			iter_2_1.OnClick(), SFX_PANEL)
		iter_2_1.Flush(True)

def var_0_0.Register(arg_4_0):
	arg_4_0.bind(PlayerProxy.UPDATED, function(arg_5_0)
		arg_4_0.Refresh())

def var_0_0.Refresh(arg_6_0):
	for iter_6_0, iter_6_1 in ipairs(arg_6_0.btns):
		iter_6_1.Flush(False)

def var_0_0.Dispose(arg_7_0):
	var_0_0.super.Dispose(arg_7_0)

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.btns):
		iter_7_1.Dispose()

	arg_7_0.btns = {}

	arg_7_0.OnDispose()

def var_0_0.GetBtns(arg_8_0):
	return {}

def var_0_0.OnDispose(arg_9_0):
	return

return var_0_0
