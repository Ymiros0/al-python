local var_0_0 = class("BuildShipImmediatelyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.type or 1
	local var_1_2 = var_1_0.pos_list
	local var_1_3 = getProxy(BuildShipProxy)
	local var_1_4 = underscore.filter(var_1_2, function(arg_2_0)
		return var_1_3:getBuildShip(arg_2_0).state ~= BuildShip.FINISH
	end)

	if #var_1_4 == 0 then
		existCall(var_1_0.callback)

		return
	end

	local var_1_5 = getProxy(BagProxy)
	local var_1_6 = var_1_5:getItemCountById(ITEM_ID_EQUIP_QUICK_FINISH)

	if var_1_6 == 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

		return
	else
		var_1_4 = underscore.slice(var_1_4, 1, var_1_6)
	end

	pg.ConnectionMgr.GetInstance():Send(12008, {
		type = var_1_1,
		pos_list = var_1_4
	}, 12009, function(arg_3_0)
		local var_3_0 = {}

		for iter_3_0, iter_3_1 in ipairs(arg_3_0.pos_list) do
			var_1_5:removeItemById(ITEM_ID_EQUIP_QUICK_FINISH, 1)
			var_1_3:getBuildShip(iter_3_1):finish()
			var_1_3:finishBuildShip(iter_3_1)
		end

		if arg_3_0.result == 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("word_speedUp") .. i18n("word_succeed"))
			arg_1_0:sendNotification(GAME.BUILD_SHIP_IMMEDIATELY_DONE)
			existCall(var_1_0.callback)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("ship_buildShipImmediately", arg_3_0.result))
		end
	end)
end

return var_0_0
