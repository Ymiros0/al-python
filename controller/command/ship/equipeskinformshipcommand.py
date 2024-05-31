local var_0_0 = class("EquipESkinFormShipCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.oldShipId
	local var_1_2 = var_1_0.oldShipPos
	local var_1_3 = var_1_0.newShipId
	local var_1_4 = var_1_0.newShipPos
	local var_1_5 = getProxy(EquipmentProxy)
	local var_1_6 = getProxy(BayProxy)
	local var_1_7 = var_1_6.getShipById(var_1_1)

	if not var_1_7:
		pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_no_old_ship"))

		return

	local var_1_8 = var_1_7.getEquipSkin(var_1_2)

	if var_1_8 == 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_no_old_skinorequipment"))

		return

	local var_1_9 = var_1_6.getShipById(var_1_3)

	if not var_1_9:
		pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_no_new_ship"))

		return

	local function var_1_10()
		local var_2_0 = var_1_5.getEquipmnentSkinById(var_1_8)

		if not var_2_0 or var_2_0.count == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_count_noenough"))

			return

		pg.ConnectionMgr.GetInstance().Send(12036, {
			ship_id = var_1_3,
			equip_skin_id = var_1_8,
			pos = var_1_4
		}, 12037, function(arg_3_0)
			if arg_3_0.result == 0:
				local var_3_0 = var_1_9.getEquipSkin(var_1_4)

				if var_3_0 != 0:
					var_1_5.addEquipmentSkin(var_3_0, 1)
					pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_unload"))

				var_1_9.updateEquipmentSkin(var_1_4, var_1_8)
				var_1_6.updateShip(var_1_9)
				var_1_5.useageEquipmnentSkin(var_1_8)
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_replace_done"))
				arg_1_0.sendNotification(GAME.EQUIP_EQUIPMENTSKIN_FROM_SHIP_DONE)
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_unload_failed" .. arg_3_0.result)))

	pg.ConnectionMgr.GetInstance().Send(12036, {
		equip_skin_id = 0,
		ship_id = var_1_1,
		pos = var_1_2
	}, 12037, function(arg_4_0)
		if arg_4_0.result == 0:
			var_1_7.updateEquipmentSkin(var_1_2, 0)
			var_1_6.updateShip(var_1_7)
			var_1_5.addEquipmentSkin(var_1_8, 1)
			var_1_10()
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_unload_failed" .. arg_4_0.result)))

return var_0_0
