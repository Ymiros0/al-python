local var_0_0 = class("EquipToShipCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.equipmentId
	local var_1_2 = var_1_0.shipId
	local var_1_3 = var_1_0.pos
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(BayProxy)
	local var_1_6 = var_1_5.getShipById(var_1_2)

	if var_1_6 == None:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_error_noShip", var_1_2))

		if var_1_4:
			var_1_4(100)

		return

	local var_1_7 = getProxy(EquipmentProxy)
	local var_1_8 = var_1_7.getEquipmentById(var_1_1)
	local var_1_9, var_1_10 = var_1_6.canEquipAtPos(var_1_8, var_1_3)

	if not var_1_9:
		pg.TipsMgr.GetInstance().ShowTips(var_1_10)

		return

	if not var_1_8 or var_1_8.count == 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_equipToShip_error_noEquip"))

		if var_1_4:
			var_1_4(101)

		return

	pg.ConnectionMgr.GetInstance().Send(12006, {
		type = 0,
		equip_id = var_1_1,
		ship_id = var_1_2,
		pos = var_1_3
	}, 12007, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = var_1_6.getEquip(var_1_3)
			local var_2_1 = var_1_7.getEquipmentById(var_1_1)

			assert(var_2_1 and var_2_1.count > 0)

			var_2_1.count = 1

			if var_2_0:
				var_1_7.addEquipment(var_2_0)

			var_1_6.updateEquip(var_1_3, var_2_1)
			var_1_5.updateShip(var_1_6)
			var_1_7.removeEquipmentById(var_1_1, 1)
			arg_1_0.sendNotification(GAME.EQUIP_TO_SHIP_DONE, var_1_6)
			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_equipToShip_ok", var_2_1.getConfig("name")), "green")
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_DOCKYARD_EQUIPON)

			if var_1_4:
				var_1_4()
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_equipToShip", arg_2_0.result))

			if var_1_4:
				var_1_4())

return var_0_0
