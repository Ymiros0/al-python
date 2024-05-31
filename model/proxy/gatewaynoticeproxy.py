local var_0_0 = class("GatewayNoticeProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}

def var_0_0.getGatewayNotices(arg_2_0, arg_2_1):
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.data):
		if not arg_2_1 or not iter_2_1.isRead:
			table.insert(var_2_0, iter_2_1)

	return var_2_0

def var_0_0.setGatewayNotices(arg_3_0, arg_3_1):
	arg_3_0.data = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_1):
		table.insert(arg_3_0.data, GatewayNotice.New(iter_3_1))

return var_0_0
