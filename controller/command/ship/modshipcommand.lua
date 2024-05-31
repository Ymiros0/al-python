local var_0_0 = class("ModShipCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.shipId
	local var_1_2 = var_1_0.shipIds or {}
	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = var_1_3:getShipById(var_1_1)
	local var_1_5 = Clone(var_1_4)

	if not var_1_4 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_error_noShip", var_1_1))

		return
	end

	if table.getCount(var_1_2) == 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("word_materal_no_enough"))

		return
	end

	local var_1_6 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_2) do
		local var_1_7 = var_1_3:getShipById(iter_1_1)

		if not var_1_7 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_error_noShip", iter_1_1))

			return
		end

		table.insert(var_1_6, var_1_7)
	end

	pg.ConnectionMgr.GetInstance():Send(12017, {
		ship_id = var_1_1,
		material_id_list = var_1_2
	}, 12018, function(arg_2_0)
		if arg_2_0.result == 0 then
			pg.TrackerMgr.GetInstance():Tracking(TRACKING_SHIP_INTENSIFY, #var_1_2)

			local var_2_0 = {}
			local var_2_1 = getProxy(EquipmentProxy)

			for iter_2_0, iter_2_1 in ipairs(var_1_6) do
				for iter_2_2, iter_2_3 in ipairs(iter_2_1.equipments) do
					if iter_2_3 then
						var_2_1:addEquipment(iter_2_3)

						if not var_2_0[iter_2_3.id] then
							var_2_0[iter_2_3.id] = iter_2_3:clone()
						else
							var_2_0[iter_2_3.id].count = var_2_0[iter_2_3.id].count + 1
						end
					end

					if iter_2_1:getEquipSkin(iter_2_2) ~= 0 then
						var_2_1:addEquipmentSkin(iter_2_1:getEquipSkin(iter_2_2), 1)
						iter_2_1:updateEquipmentSkin(iter_2_2, 0)
						pg.TipsMgr.GetInstance():ShowTips(i18n("equipment_skin_unload"))
					end
				end

				local var_2_2 = iter_2_1:GetSpWeapon()

				if var_2_2 then
					iter_2_1:UpdateSpWeapon(nil)
					var_2_1:AddSpWeapon(var_2_2)
				end

				var_1_3:removeShip(iter_2_1)
			end

			local var_2_3 = ShipModLayer.getModExpAdditions(var_1_4, var_1_6)

			for iter_2_4, iter_2_5 in pairs(var_2_3) do
				var_1_4:addModAttrExp(iter_2_4, iter_2_5)
			end

			var_1_3:updateShip(var_1_4)
			arg_1_0:sendNotification(GAME.MOD_SHIP_DONE, {
				oldShip = var_1_5,
				newShip = var_1_4,
				equipments = var_2_0
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("ship_modShip_error", arg_2_0.result))
		end
	end)
end

return var_0_0
