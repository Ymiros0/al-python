local var_0_0 = class("GatewayNoticeProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.data = {}
end

function var_0_0.getGatewayNotices(arg_2_0, arg_2_1)
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.data) do
		if not arg_2_1 or not iter_2_1.isRead then
			table.insert(var_2_0, iter_2_1)
		end
	end

	return var_2_0
end

function var_0_0.setGatewayNotices(arg_3_0, arg_3_1)
	arg_3_0.data = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_1) do
		table.insert(arg_3_0.data, GatewayNotice.New(iter_3_1))
	end
end

return var_0_0
