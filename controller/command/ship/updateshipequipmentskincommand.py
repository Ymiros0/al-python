local var_0_0 = class("UpdateShipEquipmentSkinCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.pos
	local var_1_3 = var_1_0.equipmentSkinId
	local var_1_4 = getProxy(EquipmentProxy)

	if var_1_3 and var_1_3 != 0:
		local var_1_5 = var_1_4.getEquipmnentSkinById(var_1_3)

		assert(var_1_5, "不存在该外观" .. var_1_3)

		if not var_1_5 or var_1_5.count == 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_count_noenough"))

			return

	local var_1_6 = getProxy(BayProxy)
	local var_1_7 = var_1_6.getShipById(var_1_1)

	if not var_1_7:
		pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_no_new_ship"))

		return

	pg.ConnectionMgr.GetInstance().Send(12036, {
		ship_id = var_1_1,
		equip_skin_id = var_1_3,
		pos = var_1_2
	}, 12037, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_7.getEquipSkin(var_1_2)

			var_1_7.updateEquipmentSkin(var_1_2, var_1_3)
			var_1_6.updateShip(var_1_7)

			if var_1_3 and var_1_3 != 0:
				if var_2_0 and var_2_0 != 0:
					var_1_4.addEquipmentSkin(var_2_0, 1)

				var_1_4.useageEquipmnentSkin(var_1_3)
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_replace_done"))
			else
				var_1_4.addEquipmentSkin(var_2_0, 1)
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_unload"))

			arg_1_0.sendNotification(GAME.EQUIP_EQUIPMENTSKIN_TO_SHIP_DONE, {
				ship = var_1_7
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
