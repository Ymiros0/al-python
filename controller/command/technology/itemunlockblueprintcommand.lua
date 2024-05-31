local var_0_0 = class("ItemUnlockBluePrintCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.itemId
	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3:getBluePrintById(var_1_1)
	local var_1_5 = getProxy(BagProxy)

	if not var_1_4 or not var_1_5:getItemCountById(var_1_2) then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(63214, {
		group = var_1_1,
		itemid = var_1_2
	}, 63215, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = Ship.New(arg_2_0.ship)

			getProxy(BayProxy):addShip(var_2_0)
			var_1_4:unlock(var_2_0.id)
			var_1_3:updateBluePrint(var_1_4)
			var_1_5:removeItemById(var_1_2, 1)
			arg_1_0:sendNotification(GAME.ITEM_LOCK_SHIP_BLUPRINT_DONE, {
				ship = var_2_0
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("printblue_build_erro") .. arg_2_0.result)
		end
	end)
end

return var_0_0
