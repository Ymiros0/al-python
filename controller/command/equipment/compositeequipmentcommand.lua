﻿local var_0_0 = class("CompositeEquipmentCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.count
	local var_1_2 = var_1_0.id
	local var_1_3 = getProxy(BagProxy)
	local var_1_4 = var_1_3:getData()
	local var_1_5 = getProxy(PlayerProxy)
	local var_1_6 = var_1_5:getData()
	local var_1_7 = pg.compose_data_template[var_1_2]
	local var_1_8 = getProxy(EquipmentProxy)
	local var_1_9 = var_1_8:getCapacity()

	if var_1_6:getMaxEquipmentBag() < var_1_9 + var_1_1 then
		NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)

		return
	end

	if var_1_6.gold < var_1_7.gold_num * var_1_1 then
		GoShoppingMsgBox(i18n("switch_to_shop_tip_2", i18n("word_gold")), ChargeScene.TYPE_ITEM, {
			{
				59001,
				var_1_7.gold_num * var_1_1 - var_1_6.gold,
				var_1_7.gold_num * var_1_1
			}
		})

		return
	end

	if not var_1_4[var_1_7.material_id] then
		pg.TipsMgr.GetInstance():ShowTips(i18n("word_materal_no_enough"))

		return
	end

	if var_1_4[var_1_7.material_id].count < var_1_7.material_num * var_1_1 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("word_materal_no_enough"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(14006, {
		id = var_1_2,
		num = var_1_1
	}, 14007, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_8:addEquipmentById(var_1_7.equip_id, var_1_1)
			var_1_6:consume({
				gold = var_1_7.gold_num * var_1_1
			})
			var_1_5:updatePlayer(var_1_6)
			var_1_3:removeItemById(var_1_7.material_id, var_1_7.material_num * var_1_1)
			arg_1_0:sendNotification(GAME.COMPOSITE_EQUIPMENT_DONE, {
				equipment = Equipment.New({
					id = var_1_7.equip_id
				}),
				count = var_1_1,
				composeId = var_1_2
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("equipment_compositeEquipment", arg_2_0.result))
		end
	end)
end

return var_0_0
