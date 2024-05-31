local var_0_0 = class("EquipFromShipCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.equipmentId
	local var_1_2 = var_1_0.shipId
	local var_1_3 = var_1_0.pos
	local var_1_4 = var_1_0.oldShipId
	local var_1_5 = var_1_0.oldPos
	local var_1_6 = getProxy(BayProxy)
	local var_1_7 = getProxy(EquipmentProxy)
	local var_1_8 = var_1_6.getShipById(var_1_2)

	if not var_1_8:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_error_noShip", var_1_2))

		return

	if var_1_8.getEquip(var_1_3):
		local var_1_9 = getProxy(PlayerProxy).getData()

		if var_1_7.getCapacity() >= var_1_9.getMaxEquipmentBag():
			NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)

			return

	local var_1_10 = var_1_6.getShipById(var_1_4)

	if not var_1_10:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_error_noShip", var_1_4))

		return

	local var_1_11 = var_1_10.getEquip(var_1_5)

	if not var_1_11:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_equipToShip_error_noEquip"))

		return

	local var_1_12, var_1_13 = var_1_8.canEquipAtPos(var_1_11, var_1_3)

	if not var_1_12:
		pg.TipsMgr.GetInstance().ShowTips(var_1_13)

		return

	local var_1_14 = {}

	table.insert(var_1_14, function(arg_2_0)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("ship_equip_exchange_tip", var_1_10.getName(), var_1_11.getConfig("name"), var_1_8.getName()),
			onYes = arg_2_0
		}))
	table.insert(var_1_14, function(arg_3_0)
		pg.ConnectionMgr.GetInstance().Send(12006, {
			equip_id = 0,
			type = 0,
			ship_id = var_1_4,
			pos = var_1_5
		}, 12007, function(arg_4_0)
			if arg_4_0.result == 0:
				local var_4_0 = var_1_10.getEquip(var_1_5)

				var_1_10.updateEquip(var_1_5, None)
				var_1_6.updateShip(var_1_10)

				if var_1_8.id == var_1_10.id:
					var_1_8 = var_1_10

				var_1_7.addEquipment(var_4_0)
				arg_3_0(var_1_8, var_1_1, var_1_2, var_1_3)
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_unequipFromShip", arg_4_0.result))))
	seriesAsync(var_1_14, function(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
		local var_5_0 = var_1_7.getEquipmentById(arg_5_1)

		var_5_0.count = 1

		assert(var_5_0 and var_5_0.count > 0)
		pg.ConnectionMgr.GetInstance().Send(12006, {
			type = 0,
			equip_id = arg_5_1,
			ship_id = arg_5_2,
			pos = arg_5_3
		}, 12007, function(arg_6_0)
			if arg_6_0.result == 0:
				local var_6_0 = arg_5_0.getEquip(arg_5_3)
				local var_6_1 = pg.equip_skin_template

				if var_6_0:
					var_1_7.addEquipment(var_6_0)

				arg_5_0.updateEquip(arg_5_3, var_5_0)
				var_1_6.updateShip(arg_5_0)
				var_1_7.removeEquipmentById(arg_5_1, 1)
				arg_1_0.sendNotification(GAME.EQUIP_TO_SHIP_DONE, arg_5_0)
				pg.TipsMgr.GetInstance().ShowTips(i18n("ship_equipToShip_ok", Equipment.getConfigData(arg_5_1).name), "green")
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_equipToShip", arg_6_0.result))))

return var_0_0
