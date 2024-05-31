local var_0_0 = class("RevertEquipmentCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id

	pg.ConnectionMgr.GetInstance().Send(14010, {
		equip_id = var_1_0
	}, 14011, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(EquipmentProxy)
			local var_2_1 = var_2_0.getEquipmentById(var_1_0)

			var_2_0.removeEquipmentById(var_2_1.id, 1)

			local var_2_2 = var_2_1.GetRootEquipment()

			var_2_0.addEquipmentById(var_2_2.id, var_2_2.count)
			getProxy(BagProxy).removeItemById(Item.REVERT_EQUIPMENT_ID, 1)

			local var_2_3 = var_2_1.getRevertAwards()

			for iter_2_0, iter_2_1 in pairs(var_2_3):
				arg_1_0.sendNotification(GAME.ADD_ITEM, iter_2_1)

			arg_1_0.sendNotification(GAME.REVERT_EQUIPMENT_DONE, {
				awards = var_2_3
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("equipment_destroyEquipments", arg_2_0.result)))

return var_0_0
