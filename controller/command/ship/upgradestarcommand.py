local var_0_0 = class("UpgradeStarCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.shipIds
	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = var_1_3.getShipById(var_1_1)
	local var_1_5 = pg.ship_data_breakout[var_1_4.configId].breakout_id

	if var_1_5 == 0:
		return

	local var_1_6 = Clone(var_1_4)

	var_1_6.configId = var_1_5

	for iter_1_0, iter_1_1 in pairs(var_1_4.equipments):
		if iter_1_1 and var_1_6.isForbiddenAtPos(iter_1_1, iter_1_0):
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("ship_upgrade_unequip_tip", var_1_6.getConfig("name"), "#fad545"),
				def onYes:()
					arg_1_0.sendNotification(GAME.UNEQUIP_FROM_SHIP, {
						shipId = var_1_4.id,
						pos = iter_1_0
					})
			})

			return

	local var_1_7 = Clone(var_1_4)
	local var_1_8 = {}

	for iter_1_2, iter_1_3 in ipairs(var_1_2):
		local var_1_9 = var_1_3.getShipById(iter_1_3)

		if not var_1_9:
			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_error_noShip", iter_1_3))

			return

		table.insert(var_1_8, var_1_9)

	local var_1_10 = getProxy(CollectionProxy).getShipGroup(var_1_7.groupId)

	pg.ConnectionMgr.GetInstance().Send(12027, {
		ship_id = var_1_1,
		material_id_list = var_1_2
	}, 12028, function(arg_3_0)
		if arg_3_0.result == 0:
			local var_3_0 = getProxy(EquipmentProxy)

			for iter_3_0, iter_3_1 in ipairs(var_1_8):
				for iter_3_2, iter_3_3 in ipairs(iter_3_1.equipments):
					if iter_3_3:
						var_3_0.addEquipment(iter_3_3)

					if iter_3_1.getEquipSkin(iter_3_2) != 0:
						var_3_0.addEquipmentSkin(iter_3_1.getEquipSkin(iter_3_2), 1)
						iter_3_1.updateEquipmentSkin(iter_3_2, 0)
						pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_unload"))

				local var_3_1 = iter_3_1.GetSpWeapon()

				if var_3_1:
					iter_3_1.UpdateSpWeapon(None)
					var_3_0.AddSpWeapon(var_3_1)

				var_1_3.removeShip(iter_3_1)

			local var_3_2 = pg.ship_data_breakout[var_1_4.configId]

			if var_3_2.breakout_id != 0:
				var_1_4.configId = var_3_2.breakout_id

				local var_3_3 = pg.ship_data_template[var_1_4.configId]

				for iter_3_4, iter_3_5 in ipairs(var_3_3.buff_list):
					if not var_1_4.skills[iter_3_5]:
						var_1_4.skills[iter_3_5] = {
							exp = 0,
							level = 1,
							id = iter_3_5
						}

				var_1_4.updateMaxLevel(var_3_3.max_level)

				local var_3_4 = pg.ship_data_template[var_1_7.configId].buff_list

				for iter_3_6, iter_3_7 in ipairs(var_3_4):
					if not table.contains(var_3_3.buff_list, iter_3_7):
						var_1_4.skills[iter_3_7] = None

				var_1_3.updateShip(var_1_4)

			local var_3_5 = getProxy(BagProxy)

			for iter_3_8, iter_3_9 in ipairs(var_3_2.use_item):
				var_3_5.removeItemById(iter_3_9[1], iter_3_9[2])

			local var_3_6 = getProxy(PlayerProxy)
			local var_3_7 = var_3_6.getData()

			var_3_7.consume({
				gold = var_3_2.use_gold
			})
			var_3_6.updatePlayer(var_3_7)
			arg_1_0.sendNotification(GAME.UPGRADE_STAR_DONE, {
				newShip = var_1_4,
				oldShip = var_1_7
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_upgradeStar_error", arg_3_0.result)))

return var_0_0
