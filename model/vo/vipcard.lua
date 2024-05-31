local var_0_0 = class("VipCard", import(".BaseVO"))

var_0_0.MONTH = 1

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.id = arg_1_1.type
	arg_1_0.type = arg_1_1.type
	arg_1_0.leftDate = arg_1_1.left_date
	arg_1_0.data = arg_1_1.data
end

function var_0_0.getLeftDate(arg_2_0)
	if arg_2_0.type == var_0_0.MONTH then
		return arg_2_0.leftDate + 86400
	end
end

function var_0_0.GetLeftDay(arg_3_0)
	local var_3_0 = arg_3_0:getLeftDate()
	local var_3_1 = pg.TimeMgr.GetInstance():GetServerTime()

	return (math.floor((var_3_0 - var_3_1) / 86400))
end

function var_0_0.isExpire(arg_4_0)
	if arg_4_0.type == var_0_0.MONTH then
		return arg_4_0:getLeftDate() <= pg.TimeMgr.GetInstance():GetServerTime()
	end
end

return var_0_0
