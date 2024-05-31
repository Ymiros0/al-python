﻿local var_0_0 = class("DestroyShipsCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.shipIds

	if not var_1_0.destroyEquipment then
		local var_1_2 = false
	end

	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_1) do
		local var_1_5 = var_1_3:getShipById(iter_1_1)

		if var_1_5 == nil then
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_error_noShip", iter_1_1))

			return
		end

		table.insert(var_1_4, var_1_5)
	end

	pg.ConnectionMgr.GetInstance():Send(12004, {
		ship_id_list = var_1_1
	}, 12005, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = getProxy(EquipmentProxy)
			local var_2_1 = {}
			local var_2_2 = {}

			for iter_2_0, iter_2_1 in ipairs(var_1_4) do
				var_1_3:removeShip(iter_2_1)

				for iter_2_2, iter_2_3 in ipairs(iter_2_1.equipments) do
					if iter_2_3 then
						var_2_0:addEquipment(iter_2_3)

						if not var_2_1[iter_2_3.id] then
							var_2_1[iter_2_3.id] = iter_2_3:clone()
						else
							var_2_1[iter_2_3.id].count = var_2_1[iter_2_3.id].count + 1
						end
					end

					if iter_2_1:getEquipSkin(iter_2_2) ~= 0 then
						var_2_0:addEquipmentSkin(iter_2_1:getEquipSkin(iter_2_2), 1)
						iter_2_1:updateEquipmentSkin(iter_2_2, 0)
						pg.TipsMgr.GetInstance():ShowTips(i18n("equipment_skin_unload"))
					end
				end

				local var_2_3 = iter_2_1:GetSpWeapon()

				if var_2_3 then
					iter_2_1:UpdateSpWeapon(nil)
					var_2_0:AddSpWeapon(var_2_3)
					pg.TipsMgr.GetInstance():ShowTips(i18n("spweapon_tip_unload"))
				end

				table.insert(var_2_2, iter_2_1.id)
			end

			local var_2_4, var_2_5, var_2_6 = ShipCalcHelper.CalcDestoryRes(var_1_4)
			local var_2_7 = {}

			if var_2_4 > 0 then
				table.insert(var_2_7, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResGold,
					count = var_2_4
				}))
			end

			if var_2_5 > 0 then
				table.insert(var_2_7, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResOil,
					count = var_2_5
				}))
			end

			local var_2_8 = table.mergeArray(var_2_7, var_2_6)

			for iter_2_4, iter_2_5 in ipairs(var_2_8) do
				arg_1_0:sendNotification(GAME.ADD_ITEM, iter_2_5)
			end

			arg_1_0:sendNotification(GAME.DESTROY_SHIP_DONE, {
				destroiedShipIds = var_2_2,
				bonus = var_2_8,
				equipments = var_2_1
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("ship_destoryShips", arg_2_0.result))
		end
	end)
end

function var_0_0.CheckShareSkin(arg_3_0, arg_3_1)
	if not arg_3_1.propose then
		return
	end

	local var_3_0 = arg_3_1:getProposeSkin()

	if not var_3_0 then
		return
	end

	local var_3_1 = {}
	local var_3_2 = {}

	for iter_3_0, iter_3_1 in pairs(getProxy(BayProxy):getRawData()) do
		if iter_3_1.skinId == var_3_0.id then
			if iter_3_1.groupId == arg_3_1.groupId then
				table.insert(var_3_1, iter_3_1)
			else
				table.insert(var_3_2, iter_3_1)
			end
		end
	end

	if #var_3_1 <= 0 then
		for iter_3_2, iter_3_3 in ipairs(var_3_2) do
			iter_3_3.skinId = iter_3_3:getConfig("skin_id")
		end
	end

	if #var_3_2 > 0 then
		local var_3_3 = table.concat(_.map(var_3_2, function(arg_4_0)
			return arg_4_0:getName()
		end), ", ")

		pg.TipsMgr.GetInstance():ShowTips(i18n("retire_marry_skin", var_3_3))
	end
end

return var_0_0
