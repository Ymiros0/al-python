local var_0_0 = class("MetaCharacterTacticsInfoRequestCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().idList
	local var_1_1 = ""

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		var_1_1 = var_1_1 .. iter_1_1 .. ", "

	print("63317 request tactics exp detail info.", var_1_1)
	pg.ConnectionMgr.GetInstance().Send(63317, {
		ship_id_list = var_1_0
	}, 63318, function(arg_2_0)
		print("63318 requset success")

		local var_2_0 = getProxy(MetaCharacterProxy)
		local var_2_1 = arg_2_0.info_list

		if var_2_1:
			for iter_2_0, iter_2_1 in ipairs(var_2_1):
				var_2_0.setMetaTacticsInfo(iter_2_1)
		else
			errorMsg("63318 error, data.info_list is null!"))

return var_0_0
