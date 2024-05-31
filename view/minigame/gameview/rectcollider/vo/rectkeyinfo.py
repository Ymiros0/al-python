local var_0_0 = class("RectKeyInfo")

def var_0_0.Ctor(arg_1_0):
	arg_1_0._inPutKeyDic = {}

def var_0_0.setKeyPress(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.getKeyData(arg_2_1).status = arg_2_2

	arg_2_0.setKeyData(arg_2_1, arg_2_2)

	if arg_2_0._triggerCallback:
		arg_2_0._triggerCallback(arg_2_1, arg_2_2)

def var_0_0.setTriggerCallback(arg_3_0, arg_3_1):
	arg_3_0._triggerCallback = arg_3_1

def var_0_0.setKeyData(arg_4_0, arg_4_1, arg_4_2):
	for iter_4_0 = 1, #arg_4_0._inPutKeyDic:
		local var_4_0 = arg_4_0._inPutKeyDic[iter_4_0]

		if var_4_0.code == arg_4_1:
			var_4_0.status = arg_4_2

def var_0_0.getKeyData(arg_5_0, arg_5_1):
	if not arg_5_1:
		return

	local var_5_0

	for iter_5_0 = 1, #arg_5_0._inPutKeyDic:
		local var_5_1 = arg_5_0._inPutKeyDic[iter_5_0]

		if var_5_1.code == arg_5_1:
			var_5_0 = var_5_1

	if not var_5_0:
		var_5_0 = {
			status = False,
			code = arg_5_1
		}

		table.insert(arg_5_0._inPutKeyDic, var_5_0)

	return var_5_0

def var_0_0.getKeyCode(arg_6_0, arg_6_1):
	if not arg_6_1:
		return None

	local var_6_0

	for iter_6_0 = 1, #arg_6_0._inPutKeyDic:
		local var_6_1 = arg_6_0._inPutKeyDic[iter_6_0]

		if var_6_1.code == arg_6_1:
			var_6_0 = var_6_1

	if not var_6_0:
		var_6_0 = {
			status = False,
			code = arg_6_1
		}

		table.insert(arg_6_0._inPutKeyDic, var_6_0)

	return var_6_0.status

return var_0_0
