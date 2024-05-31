local var_0_0 = class("UIItemList")

var_0_0.EventInit = 1
var_0_0.EventUpdate = 2
var_0_0.EventExcess = 3

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	assert(not IsNil(arg_1_1))
	assert(not IsNil(arg_1_2))

	arg_1_0.container = arg_1_1
	arg_1_0.item = arg_1_2
	arg_1_0.currentCount = 0

def var_0_0.make(arg_2_0, arg_2_1):
	assert(arg_2_1 == None or type(arg_2_1) == "function")

	arg_2_0.callback = arg_2_1

def var_0_0.align(arg_3_0, arg_3_1):
	assert(arg_3_1 >= 0)

	local var_3_0 = arg_3_0.container
	local var_3_1 = var_3_0.childCount

	for iter_3_0 = arg_3_1, var_3_1 - 1:
		local var_3_2 = var_3_0.GetChild(iter_3_0)

		setActive(var_3_2, False)

	for iter_3_1 = var_3_1, arg_3_1 - 1:
		local var_3_3 = cloneTplTo(arg_3_0.item, var_3_0)

	if arg_3_0.callback:
		for iter_3_2 = arg_3_0.currentCount, arg_3_1 - 1:
			local var_3_4 = var_3_0.GetChild(iter_3_2)

			arg_3_0.callback(var_0_0.EventInit, iter_3_2, var_3_4)

		for iter_3_3 = arg_3_1, arg_3_0.currentCount - 1:
			local var_3_5 = var_3_0.GetChild(iter_3_3)

			arg_3_0.callback(var_0_0.EventExcess, iter_3_3, var_3_5)

		arg_3_0.currentCount = arg_3_1

	for iter_3_4 = 0, arg_3_1 - 1:
		local var_3_6 = var_3_0.GetChild(iter_3_4)

		setActive(var_3_6, True)

		if arg_3_0.callback:
			arg_3_0.callback(var_0_0.EventUpdate, iter_3_4, var_3_6)

def var_0_0.each(arg_4_0, arg_4_1):
	for iter_4_0 = arg_4_0.container.childCount - 1, 0, -1:
		local var_4_0 = arg_4_0.container.GetChild(iter_4_0)

		arg_4_1(iter_4_0, var_4_0)

def var_0_0.eachActive(arg_5_0, arg_5_1):
	for iter_5_0 = 0, arg_5_0.container.childCount - 1:
		local var_5_0 = arg_5_0.container.GetChild(iter_5_0)

		if isActive(var_5_0):
			arg_5_1(iter_5_0, var_5_0)

def var_0_0.StaticAlign(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	local var_6_0 = UIItemList.New(arg_6_0, arg_6_1)

	var_6_0.make(arg_6_3)
	var_6_0.align(arg_6_2)

return var_0_0
