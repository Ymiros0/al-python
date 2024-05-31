local var_0_0 = class("DestroyEquipmentsCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = {}
	local var_1_2 = getProxy(EquipmentProxy)
	local var_1_3

	for iter_1_0, iter_1_1 in ipairs(var_1_0.equipments):
		local var_1_4 = iter_1_1[1]
		local var_1_5 = iter_1_1[2]
		local var_1_6 = var_1_2.getEquipmentById(var_1_4)

		if not var_1_6:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_destroyEquipments_error_noEquip"))

			return

		if var_1_5 > var_1_6.count:
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_destroyEquipments_error_notEnoughEquip"))

			return

		table.insert(var_1_1, {
			id = var_1_4,
			count = var_1_5
		})

		if not var_1_3:
			local var_1_7 = False

			if var_1_6.isImportance():
				var_1_7 = True

			if var_1_6.getConfig("rarity") >= EquipmentRarity.Gold:
				var_1_7 = True

			if var_1_6.getConfig("id") % 20 >= 10:
				var_1_7 = True

			var_1_3 = var_1_7 and var_1_4

	local var_1_8 = {}

	if var_1_3:
		table.insert(var_1_8, function(arg_2_0)
			local var_2_0 = pg.SecondaryPWDMgr

			var_2_0.LimitedOperation(var_2_0.RESOLVE_EQUIPMENT, var_1_3, arg_2_0))

	seriesAsync(var_1_8, function()
		pg.ConnectionMgr.GetInstance().Send(14008, {
			equip_list = var_1_1
		}, 14009, function(arg_4_0)
			if arg_4_0.result == 0:
				local var_4_0 = getProxy(PlayerProxy).getData()
				local var_4_1 = {}
				local var_4_2 = 0

				local function var_4_3(arg_5_0, arg_5_1)
					print("remove. " .. arg_5_0 .. " " .. arg_5_1)

					local var_5_0 = var_1_2.getEquipmentById(arg_5_0)

					var_1_2.removeEquipmentById(arg_5_0, arg_5_1)

					local var_5_1 = var_5_0.getConfig("destory_item") or {}
					local var_5_2 = var_5_0.getConfig("destory_gold") or 0

					var_4_2 = var_4_2 + var_5_2 * arg_5_1

					for iter_5_0, iter_5_1 in ipairs(var_5_1):
						local var_5_3 = False

						for iter_5_2, iter_5_3 in ipairs(var_4_1):
							if iter_5_1[1] == var_4_1[iter_5_2].id:
								var_4_1[iter_5_2].count = var_4_1[iter_5_2].count + iter_5_1[2] * arg_5_1
								var_5_3 = True

								break

						if not var_5_3:
							table.insert(var_4_1, Drop.New({
								type = DROP_TYPE_ITEM,
								id = iter_5_1[1],
								count = iter_5_1[2] * arg_5_1
							}))

				arg_1_0.sendNotification(EquipmentMediator.NO_UPDATE)

				for iter_4_0, iter_4_1 in ipairs(var_1_1):
					var_4_3(iter_4_1.id, iter_4_1.count)

				table.insert(var_4_1, Drop.New({
					id = 1,
					type = DROP_TYPE_RESOURCE,
					count = var_4_2
				}))

				for iter_4_2, iter_4_3 in ipairs(var_4_1):
					arg_1_0.sendNotification(GAME.ADD_ITEM, iter_4_3)

				if not LOCK_QUOTA_SHOP:
					local var_4_4 = QuotaShop.New()

					getProxy(ShopsProxy).updateQuotaShop(var_4_4)

				arg_1_0.sendNotification(GAME.DESTROY_EQUIPMENTS_DONE, var_4_1)
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("equipment_destroyEquipments", arg_4_0.result))))

return var_0_0
