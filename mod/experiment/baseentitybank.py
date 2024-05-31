local var_0_0 = class("BaseEntityBank", import(".BaseEntityPool"))

var_0_0.Fields = {
	marks = "table"
}

def var_0_0.Build(arg_1_0):
	var_0_0.super.Build(arg_1_0)

	arg_1_0.marks = {}

def var_0_0.Fetch(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0.Get(arg_2_1)

	arg_2_0.marks[arg_2_1] = arg_2_0.marks[arg_2_1] or {}

	table.insert(arg_2_0.marks[arg_2_1], var_2_0)

	return var_2_0

def var_0_0.Recycle(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.marks[arg_3_1]

	if var_3_0:
		for iter_3_0, iter_3_1 in ipairs(var_3_0):
			arg_3_0.Return(iter_3_1, arg_3_1)

		arg_3_0.marks[arg_3_1] = None

def var_0_0.RecycleAll(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(arg_4_0.marks):
		for iter_4_2, iter_4_3 in ipairs(iter_4_1):
			arg_4_0.Return(iter_4_3, iter_4_0)

	arg_4_0.marks = {}

return var_0_0
