local var_0_0 = class("UpGradeEquipmentCommands", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.pos
	local var_1_3 = var_1_0.equipmentId
	local var_1_4

	if var_1_1:
		var_1_4 = getProxy(BayProxy).getShipById(var_1_1).getEquip(var_1_2)

		assert(var_1_4, "can not find equipment at ship.")
	else
		var_1_4 = getProxy(EquipmentProxy).getEquipmentById(var_1_3)

		assert(var_1_4, "can not find equipment. " .. var_1_3)

	if not Equipment.canUpgrade(var_1_4.configId):
		pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_max_level"))

		return

	local var_1_5 = var_1_1 and 14002 or 14004
	local var_1_6 = var_1_1 and 14003 or 14005
	local var_1_7 = var_1_1 and {
		ship_id = var_1_1,
		pos = var_1_2
	} or {
		type = 0,
		equip_id = var_1_3
	}

	pg.ConnectionMgr.GetInstance().Send(var_1_5, var_1_7, var_1_6, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(BayProxy)
			local var_2_1 = getProxy(BagProxy)
			local var_2_2 = getProxy(EquipmentProxy)
			local var_2_3 = getProxy(PlayerProxy)
			local var_2_4
			local var_2_5

			if var_1_1:
				var_2_4 = var_2_0.getShipById(var_1_1)
				var_2_5 = var_2_4.getEquip(var_1_2)
			else
				var_2_5 = var_2_2.getEquipmentById(var_1_3)

			local var_2_6 = var_2_3.getData()
			local var_2_7 = var_2_5.getConfig("trans_use_gold")

			var_2_6.consume({
				gold = var_2_7
			})
			var_2_3.updatePlayer(var_2_6)

			local var_2_8 = var_2_5.getConfig("trans_use_item")

			for iter_2_0, iter_2_1 in ipairs(var_2_8):
				var_2_1.removeItemById(iter_2_1[1], iter_2_1[2])

			local var_2_9 = var_2_5.MigrateTo(var_2_5.getConfig("next"))

			if var_2_4:
				var_2_4.updateEquip(var_1_2, var_2_9)
				var_2_0.updateShip(var_2_4)
			elif var_2_5:
				var_2_2.removeEquipmentById(var_2_5.id, 1)
				var_2_2.addEquipmentById(var_2_9.id, 1, True)

			arg_1_0.sendNotification(GAME.UPGRADE_EQUIPMENTS_DONE, {
				ship = var_2_4,
				equip = var_2_5,
				newEquip = var_2_9
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("equipment_upgrade_erro", arg_2_0.result)))

return var_0_0
