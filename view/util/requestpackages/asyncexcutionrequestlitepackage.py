local var_0_0 = class("AsyncExcutionRequestLitePackage", import(".RequestPackage"))

var_0_0.STATUS = {
	SUSPEND = 2,
	READY = 1,
	RUNNING = 3
}

def var_0_0.__call(arg_1_0, ...):
	if arg_1_0.stopped:
		return

	if not arg_1_0.funcs or #arg_1_0.funcs == 0:
		return

	arg_1_0.Excute()

def var_0_0.Resume(arg_2_0):
	arg_2_0.targetStatus = var_0_0.STATUS.READY

	if arg_2_0.status == var_0_0.STATUS.SUSPEND:
		arg_2_0.Excute()

def var_0_0.Suspend(arg_3_0):
	arg_3_0.targetStatus = var_0_0.STATUS.SUSPEND

def var_0_0.Ctor(arg_4_0, arg_4_1):
	arg_4_0.funcs = arg_4_1 or {}
	arg_4_0.status = var_0_0.STATUS.READY
	arg_4_0.targetStatus = var_0_0.STATUS.READY

def var_0_0.Insert(arg_5_0, arg_5_1):
	table.insert(arg_5_0.funcs, arg_5_1)

def var_0_0.Excute(arg_6_0):
	assert(arg_6_0.ready)

	if not arg_6_0.ready:
		return

	local var_6_0

	local function var_6_1(...)
		if arg_6_0.stopped:
			return

		if arg_6_0.suspended or not arg_6_0.funcs or not (#arg_6_0.funcs > 0):
			arg_6_0.ready = True

			return

		arg_6_0.ready = None

		table.remove(arg_6_0.funcs, 1)(var_6_1, ...)

	var_6_1()

return var_0_0
