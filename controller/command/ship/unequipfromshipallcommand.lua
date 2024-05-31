﻿local var_0_0 = class("UnEquipFromShipAllCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().shipId
	local var_1_1 = getProxy(BayProxy):getShipById(var_1_0)

	if var_1_1 == nil then
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_error_noShip", var_1_0))

		return
	end

	local var_1_2 = #var_1_1.equipments
	local var_1_3 = 0

	for iter_1_0, iter_1_1 in pairs(var_1_1.equipments) do
		if iter_1_1 then
			var_1_3 = var_1_3 + 1
		end
	end

	local var_1_4 = getProxy(PlayerProxy):getData()
	local var_1_5 = getProxy(EquipmentProxy):getCapacity()

	if var_1_4:getMaxEquipmentBag() < var_1_5 + var_1_3 then
		NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)

		return
	end

	local var_1_6 = var_1_1:GetSpWeapon()
	local var_1_7 = getProxy(EquipmentProxy):GetSpWeaponCapacity()
	local var_1_8 = getProxy(EquipmentProxy):GetSpWeaponCount()

	if var_1_6 and var_1_7 <= var_1_8 then
		NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), OpenSpWeaponPage, gotoChargeScene)

		return
	end

	arg_1_0:fun(var_1_1, 1, var_1_2, function()
		if var_1_6 then
			arg_1_0:sendNotification(GAME.EQUIP_SPWEAPON_TO_SHIP, {
				shipId = var_1_0
			})
		end
	end)
end

function var_0_0.fun(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4)
	if arg_3_3 < arg_3_2 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_unequip_all_success"))
		arg_3_0:sendNotification(GAME.UNEQUIP_FROM_SHIP_DONE, arg_3_1)
		existCall(arg_3_4)

		return
	end

	local var_3_0 = getProxy(BayProxy)
	local var_3_1 = arg_3_1:getEquip(arg_3_2)

	if not var_3_1 then
		arg_3_0:fun(arg_3_1, arg_3_2 + 1, arg_3_3, arg_3_4)

		return
	end

	pg.ConnectionMgr.GetInstance():Send(12006, {
		equip_id = 0,
		type = 0,
		ship_id = arg_3_1.id,
		pos = arg_3_2
	}, 12007, function(arg_4_0)
		if arg_4_0.result == 0 then
			local var_4_0 = getProxy(EquipmentProxy)

			arg_3_1:updateEquip(arg_3_2, nil)
			var_3_0:updateShip(arg_3_1)
			var_4_0:addEquipment(var_3_1)
			arg_3_0:fun(arg_3_1, arg_3_2 + 1, arg_3_3, arg_3_4)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("ship_unequipFromShip", arg_4_0.result))
		end
	end)
end

return var_0_0
