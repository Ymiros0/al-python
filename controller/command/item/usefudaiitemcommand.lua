﻿local var_0_0 = class("UseFudaiItemCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = var_1_0.callback

	if var_1_2 == 0 then
		return
	end

	local var_1_4 = getProxy(BagProxy)
	local var_1_5 = var_1_4:getItemById(var_1_1)

	if var_1_2 > var_1_5.count then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(15002, {
		id = var_1_1,
		count = var_1_2
	}, 15003, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = {}

			var_1_4:removeItemById(var_1_1, var_1_2)
			assert(var_1_5:getConfig("usage") == ItemUsage.DROP or var_1_5:getConfig("usage") == ItemUsage.DROP_TEMPLATE, "未处理类型")
			existCall(var_1_3, PlayerConst.addTranDrop(arg_2_0.drop_list))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
			existCall(var_1_3)
		end
	end)
end

return var_0_0
