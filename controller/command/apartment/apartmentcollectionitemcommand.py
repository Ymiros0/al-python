local var_0_0 = class("ApartmentCollectionItemCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.itemId
	local var_1_3 = getProxy(ApartmentProxy)
	local var_1_4 = var_1_3.getApartment(var_1_1)

	if var_1_4.collectItemDic[var_1_2]:
		return

	warning(var_1_1, var_1_2)
	pg.ConnectionMgr.GetInstance().Send(28011, {
		ship_group = var_1_1,
		collection_id = var_1_2
	}, 28012, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_4.collectItemDic[var_1_2] = True

			var_1_3.updateApartment(var_1_4)

			local var_2_0 = pg.dorm3d_collection_template[var_1_2].award

			var_1_4 = var_1_3.getApartment(var_1_1)

			local var_2_1 = var_1_4.addFavor(var_2_0)

			var_1_3.updateApartment(var_1_4)
			arg_1_0.sendNotification(GAME.APARTMENT_COLLECTION_ITEM_DONE, {
				itemId = var_1_2
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
