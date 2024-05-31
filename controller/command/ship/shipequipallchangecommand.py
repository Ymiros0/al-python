local var_0_0 = class("ShipEquipAllChangeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(BayProxy)
	local var_1_2 = getProxy(EquipmentProxy)

	local function var_1_3(arg_2_0, arg_2_1, arg_2_2)
		return function(arg_3_0)
			pg.ConnectionMgr.GetInstance().Send(12006, {
				type = 0,
				ship_id = arg_2_0,
				equip_id = arg_2_1,
				pos = arg_2_2
			}, 12007, function(arg_4_0)
				if arg_4_0.result == 0:
					local var_4_0 = var_1_1.getShipById(arg_2_0)
					local var_4_1 = var_4_0.getEquip(arg_2_2)

					if var_4_1:
						var_1_2.addEquipment(var_4_1)

					local var_4_2 = arg_2_1 > 0 and var_1_2.getEquipmentById(arg_2_1) or None

					if var_4_2:
						var_4_2.count = 1

						var_1_2.removeEquipmentById(arg_2_1, 1)

					var_4_0.updateEquip(arg_2_2, var_4_2)
					var_1_1.updateShip(var_4_0)
					existCall(arg_3_0)
				else
					pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_equipToShip", arg_4_0.result)))

	local function var_1_4(arg_5_0, arg_5_1)
		return function(arg_6_0)
			pg.ConnectionMgr.GetInstance().Send(14201, {
				spweapon_id = arg_5_1,
				ship_id = arg_5_0
			}, 14202, function(arg_7_0)
				if arg_7_0.result == 0:
					local var_7_0 = var_1_1.getShipById(arg_5_0)
					local var_7_1 = var_7_0.GetSpWeapon()

					if var_7_1:
						var_1_2.AddSpWeapon(var_7_1)

					local var_7_2 = arg_5_1 > 0 and var_1_2.GetSpWeaponByUid(arg_5_1) or None

					if var_7_2:
						var_1_2.RemoveSpWeapon(var_7_2)

					var_7_0.UpdateSpWeapon(var_7_2)
					var_1_1.updateShip(var_7_0)
					existCall(arg_6_0)
				else
					pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_equipToShip", arg_7_0.result)))

	local var_1_5 = var_1_0.shipId
	local var_1_6 = var_1_1.getShipById(var_1_5)

	if not var_1_6:
		pg.TipsMgr.GetInstance().ShowTips(i18n("ship_error_noShip", var_1_5))

		return

	local var_1_7 = {}
	local var_1_8 = {}
	local var_1_9 = var_1_0.equipData
	local var_1_10 = 0
	local var_1_11 = 0

	for iter_1_0, iter_1_1 in ipairs(var_1_9):
		local var_1_12 = False

		if iter_1_0 == 6:
			if iter_1_1:
				var_1_12 = iter_1_1 and iter_1_1.shipId == var_1_5
			else
				var_1_12 = not var_1_6.spWeapon

			if not var_1_12:
				if iter_1_1 and iter_1_1.shipId:
					table.insert(var_1_8, var_1_4(iter_1_1.shipId, 0))

				table.insert(var_1_8, var_1_4(var_1_5, iter_1_1 and iter_1_1.uid or 0))

				if var_1_6.spWeapon or iter_1_1 and iter_1_1.shipId:
					var_1_11 = var_1_11 + 1
		else
			if iter_1_1:
				var_1_12 = iter_1_1 and iter_1_1.shipId == var_1_5 and iter_1_1.shipPos == iter_1_0
			else
				var_1_12 = not var_1_6.equipments[iter_1_0]

			if not var_1_12:
				if var_1_6.equipments[iter_1_0]:
					table.insert(var_1_7, var_1_3(var_1_5, 0, iter_1_0))

				if iter_1_1 and iter_1_1.shipId and iter_1_1.shipId != var_1_5:
					table.insert(var_1_8, var_1_3(iter_1_1.shipId, 0, iter_1_1.shipPos))

				table.insert(var_1_8, var_1_3(var_1_5, iter_1_1 and iter_1_1.id or 0, iter_1_0))

				if var_1_6.equipments[iter_1_0] or iter_1_1 and iter_1_1.shipId:
					var_1_10 = var_1_10 + 1

	if var_1_10 > 0 and getProxy(PlayerProxy).getData().getMaxEquipmentBag() < var_1_2.getCapacity() + var_1_10:
		NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)

		return

	if var_1_11 > 0 and var_1_2.GetSpWeaponCapacity() < var_1_2.GetSpWeaponCount() + var_1_11:
		pg.TipsMgr.GetInstance().ShowTips(i18n("spweapon_tip_bag_no_enough"))

		return

	seriesAsync(table.mergeArray(var_1_7, var_1_8), function()
		arg_1_0.sendNotification(GAME.SHIP_EQUIP_ALL_CHANGE_DONE, var_1_5)
		pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_import_success")))

return var_0_0
