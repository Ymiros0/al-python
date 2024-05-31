local var_0_0 = class("CollectionGetAwardCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.index
	local var_1_3 = False
	local var_1_4 = 0
	local var_1_5 = getProxy(PlayerProxy).getData()
	local var_1_6 = pg.storeup_data_template[var_1_1].award_display[var_1_2]

	if var_1_6 and var_1_6[1] == DROP_TYPE_RESOURCE:
		var_1_4 = var_1_6[2]
		var_1_3 = True

	if var_1_3 and var_1_4 == 1 and var_1_5.GoldMax(1):
		pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_collect"))

		return

	if var_1_3 and var_1_4 == 2 and var_1_5.OilMax(1):
		pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_collect"))

		return

	pg.ConnectionMgr.GetInstance().Send(17005, {
		id = var_1_1,
		award_index = var_1_2
	}, 17006, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(CollectionProxy).updateAward(var_1_1, var_1_2)

			local var_2_0 = pg.storeup_data_template[var_1_1].award_display[var_1_2]

			if var_2_0[1] == DROP_TYPE_RESOURCE:
				local var_2_1 = getProxy(PlayerProxy)
				local var_2_2 = var_2_1.getData()

				var_2_2.addResources({
					[id2res(var_2_0[2])] = var_2_0[3]
				})
				var_2_1.updatePlayer(var_2_2)
			elif var_2_0[1] == DROP_TYPE_ITEM:
				getProxy(BagProxy).addItemById(var_2_0[2], var_2_0[3])
			elif var_2_0[1] == DROP_TYPE_EQUIP:
				getProxy(EquipmentProxy).addEquipmentById(var_2_0[2], var_2_0[3])
			elif var_2_0[1] == DROP_TYPE_SHIP:
				pg.TipsMgr.GetInstance().ShowTips(i18n("collection_award_ship", pg.ship_data_statistics[var_2_0[2]].name))
			elif var_2_0[1] == DROP_TYPE_FURNITURE:
				local var_2_3 = getProxy(DormProxy)
				local var_2_4 = Furniture.New({
					count = 1,
					id = var_2_0[2]
				})

				var_2_3.AddFurniture(var_2_4)

			local var_2_5 = {}

			table.insert(var_2_5, Drop.Create(var_2_0))
			arg_1_0.sendNotification(GAME.COLLECT_GET_AWARD_DONE, {
				id = var_1_1,
				items = var_2_5
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("word_takeOk"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("collection_getResource_error", arg_2_0.result)))

return var_0_0
