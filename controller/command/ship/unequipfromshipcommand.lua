local var_0_0 = class("UnequipFromShipCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.pos
	local var_1_3 = var_1_0.callback
	local var_1_4 = getProxy(BayProxy)
	local var_1_5 = var_1_4:getShipById(var_1_1)
	local var_1_6 = getProxy(PlayerProxy):getData()

	if getProxy(EquipmentProxy):getCapacity() >= var_1_6:getMaxEquipmentBag() then
		NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)

		if var_1_3 then
			var_1_3()
		end

		return
	end

	if var_1_5 == nil then
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_error_noShip", var_1_1))

		if var_1_3 then
			var_1_3()
		end

		return
	end

	local var_1_7 = var_1_5:getEquip(var_1_2)

	if not var_1_7 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_unequipFromShip_error_noEquip"))

		if var_1_3 then
			var_1_3()
		end

		return
	end

	pg.ConnectionMgr.GetInstance():Send(12006, {
		equip_id = 0,
		type = 0,
		ship_id = var_1_1,
		pos = var_1_2
	}, 12007, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(EquipmentProxy)

			var_1_5:updateEquip(var_1_2, nil)
			var_1_4:updateShip(var_1_5)
			var_1_7:setSkinId(0)
			var_2_0:addEquipment(var_1_7)
			arg_1_0:sendNotification(GAME.UNEQUIP_FROM_SHIP_DONE, var_1_5)
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_unequipFromShip_ok", var_1_7:getConfig("name")), "red")

			if var_1_5:getEquipSkin(var_1_2) > 0 and not var_1_5:checkCanEquipSkin(var_1_2, var_1_5:getEquipSkin(var_1_2)) then
				arg_1_0:sendNotification(GAME.EQUIP_EQUIPMENTSKIN_TO_SHIP, {
					equipmentSkinId = 0,
					shipId = var_1_1,
					pos = var_1_2
				})
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("ship_unequipFromShip", arg_2_0.result))
		end

		if var_1_3 then
			var_1_3()
		end
	end)
end

return var_0_0
