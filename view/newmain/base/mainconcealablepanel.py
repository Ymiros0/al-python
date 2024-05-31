local var_0_0 = class("MainConcealablePanel", import(".MainBasePanel"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)

	arg_1_0.initPosition = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0.btns):
		if not iter_1_1.IsFixed():
			table.insert(arg_1_0.initPosition, iter_1_1._tf.localPosition)

	arg_1_0.isChanged = False

def var_0_0.Init(arg_2_0):
	var_0_0.super.Init(arg_2_0)
	arg_2_0.CalcLayout()

def var_0_0.Refresh(arg_3_0):
	var_0_0.super.Refresh(arg_3_0)
	arg_3_0.CalcLayout()

def var_0_0.CalcLayout(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.btns):
		if not iter_4_1.IsFixed() and isActive(iter_4_1._tf):
			table.insert(var_4_0, iter_4_1._tf)

	local var_4_1 = #var_4_0 >= #arg_4_0.initPosition

	if var_4_1 and not arg_4_0.isChanged:
		return

	arg_4_0.FillEmptySlot(var_4_0)

	arg_4_0.isChanged = not var_4_1

def var_0_0.FillEmptySlot(arg_5_0, arg_5_1):
	local var_5_0 = #arg_5_0.initPosition

	for iter_5_0 = #arg_5_1, 1, -1:
		arg_5_1[iter_5_0].localPosition = arg_5_0.initPosition[var_5_0]
		var_5_0 = var_5_0 - 1

return var_0_0
