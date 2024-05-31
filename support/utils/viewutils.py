pg = pg or {}

local var_0_0 = pg
local var_0_1 = class("ViewUtils")

var_0_0.ViewUtils = var_0_1

def var_0_1.SetLayer(arg_1_0, arg_1_1):
	if IsNil(go(arg_1_0)):
		return

	go(arg_1_0).layer = arg_1_1

	local var_1_0 = arg_1_0.childCount

	for iter_1_0 = 0, var_1_0 - 1:
		var_0_1.SetLayer(arg_1_0.GetChild(iter_1_0), arg_1_1)

def var_0_1.SetSortingOrder(arg_2_0, arg_2_1):
	arg_2_0 = tf(arg_2_0)

	local var_2_0 = arg_2_0.GetComponents(typeof(Renderer))

	for iter_2_0 = 0, var_2_0.Length - 1:
		var_2_0[iter_2_0].sortingOrder = arg_2_1

	local var_2_1 = arg_2_0.GetComponent(typeof(Canvas))

	if var_2_1:
		var_2_1.sortingOrder = arg_2_1

	for iter_2_1 = 0, arg_2_0.childCount - 1:
		var_0_1.SetSortingOrder(arg_2_0.GetChild(iter_2_1), arg_2_1)

def var_0_1.AddSortingOrder(arg_3_0, arg_3_1):
	arg_3_0 = tf(arg_3_0)

	local var_3_0 = arg_3_0.GetComponents(typeof(Renderer))

	for iter_3_0 = 0, var_3_0.Length - 1:
		var_3_0[iter_3_0].sortingOrder = var_3_0[iter_3_0].sortingOrder + arg_3_1

	local var_3_1 = arg_3_0.GetComponent(typeof(Canvas))

	if var_3_1:
		var_3_1.sortingOrder = var_3_1.sortingOrder + arg_3_1

	for iter_3_1 = 0, arg_3_0.childCount - 1:
		var_0_1.AddSortingOrder(arg_3_0.GetChild(iter_3_1), arg_3_1)
