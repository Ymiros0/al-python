local var_0_0 = class("DestroyShipsCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipIds

	if not var_1_0.destroyEquipment:
		local var_1_2 = False

	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_1):
		local var_1_5 = var_1_3.getShipById(iter_1_1)

		if var_1_5 == None:
			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_error_noShip", iter_1_1))

			return

		table.insert(var_1_4, var_1_5)

	pg.ConnectionMgr.GetInstance().Send(12004, {
		ship_id_list = var_1_1
	}, 12005, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(EquipmentProxy)
			local var_2_1 = {}
			local var_2_2 = {}

			for iter_2_0, iter_2_1 in ipairs(var_1_4):
				var_1_3.removeShip(iter_2_1)

				for iter_2_2, iter_2_3 in ipairs(iter_2_1.equipments):
					if iter_2_3:
						var_2_0.addEquipment(iter_2_3)

						if not var_2_1[iter_2_3.id]:
							var_2_1[iter_2_3.id] = iter_2_3.clone()
						else
							var_2_1[iter_2_3.id].count = var_2_1[iter_2_3.id].count + 1

					if iter_2_1.getEquipSkin(iter_2_2) != 0:
						var_2_0.addEquipmentSkin(iter_2_1.getEquipSkin(iter_2_2), 1)
						iter_2_1.updateEquipmentSkin(iter_2_2, 0)
						pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_skin_unload"))

				local var_2_3 = iter_2_1.GetSpWeapon()

				if var_2_3:
					iter_2_1.UpdateSpWeapon(None)
					var_2_0.AddSpWeapon(var_2_3)
					pg.TipsMgr.GetInstance().ShowTips(i18n("spweapon_tip_unload"))

				table.insert(var_2_2, iter_2_1.id)

			local var_2_4, var_2_5, var_2_6 = ShipCalcHelper.CalcDestoryRes(var_1_4)
			local var_2_7 = {}

			if var_2_4 > 0:
				table.insert(var_2_7, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResGold,
					count = var_2_4
				}))

			if var_2_5 > 0:
				table.insert(var_2_7, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResOil,
					count = var_2_5
				}))

			local var_2_8 = table.mergeArray(var_2_7, var_2_6)

			for iter_2_4, iter_2_5 in ipairs(var_2_8):
				arg_1_0.sendNotification(GAME.ADD_ITEM, iter_2_5)

			arg_1_0.sendNotification(GAME.DESTROY_SHIP_DONE, {
				destroiedShipIds = var_2_2,
				bonus = var_2_8,
				equipments = var_2_1
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_destoryShips", arg_2_0.result)))

def var_0_0.CheckShareSkin(arg_3_0, arg_3_1):
	if not arg_3_1.propose:
		return

	local var_3_0 = arg_3_1.getProposeSkin()

	if not var_3_0:
		return

	local var_3_1 = {}
	local var_3_2 = {}

	for iter_3_0, iter_3_1 in pairs(getProxy(BayProxy).getRawData()):
		if iter_3_1.skinId == var_3_0.id:
			if iter_3_1.groupId == arg_3_1.groupId:
				table.insert(var_3_1, iter_3_1)
			else
				table.insert(var_3_2, iter_3_1)

	if #var_3_1 <= 0:
		for iter_3_2, iter_3_3 in ipairs(var_3_2):
			iter_3_3.skinId = iter_3_3.getConfig("skin_id")

	if #var_3_2 > 0:
		local var_3_3 = table.concat(_.map(var_3_2, function(arg_4_0)
			return arg_4_0.getName()), ", ")

		pg.TipsMgr.GetInstance().ShowTips(i18n("retire_marry_skin", var_3_3))

return var_0_0
