local var_0_0 = class("ChargeFailedCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.payId
	local var_1_2 = var_1_0.code

	if not var_1_1 then
		return
	end

	if not var_1_2 or type(var_1_2) ~= "number" then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(11510, {
		pay_id = tostring(var_1_1),
		code = math.abs(var_1_2)
	})
end

return var_0_0
