﻿local var_0_0 = class("MetaCharActiveEnergyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().shipId
	local var_1_1 = getProxy(BayProxy)
	local var_1_2 = var_1_1:getShipById(var_1_0)

	if not var_1_2 then
		return
	end

	local var_1_3 = var_1_2:getMetaCharacter()
	local var_1_4 = var_1_3:getBreakOutInfo()
	local var_1_5 = var_1_4:getNextInfo()

	if not var_1_5 then
		return
	end

	local var_1_6, var_1_7 = var_1_4:getLimited()

	if var_1_6 > var_1_2.level or var_1_7 > var_1_3:getCurRepairExp() then
		pg.TipsMgr.GetInstance():ShowTips("level or repair progress is not enough")

		return
	end

	local var_1_8, var_1_9 = var_1_4:getConsume()
	local var_1_10 = getProxy(PlayerProxy):getData()

	if var_1_8 > var_1_10.gold then
		pg.TipsMgr.GetInstance():ShowTips("gold not enough")

		return
	end

	local var_1_11 = getProxy(BagProxy)

	if _.any(var_1_9, function(arg_2_0)
		return var_1_11:getItemCountById(arg_2_0.itemId) < arg_2_0.count
	end) then
		pg.TipsMgr.GetInstance():ShowTips("item not enough")

		return
	end

	print("63303 meta energy", var_1_2.id)
	pg.ConnectionMgr.GetInstance():Send(63303, {
		ship_id = var_1_2.id
	}, 63304, function(arg_3_0)
		if arg_3_0.result == 0 then
			print("63304 meta energy success", var_1_2.id)

			local var_3_0 = Clone(var_1_2)

			arg_1_0:updateStar(var_1_2, var_3_0.configId, var_1_5.id)
			var_1_1:updateShip(var_1_2)

			local var_3_1 = getProxy(CollectionProxy)
			local var_3_2 = var_3_1:getShipGroup(var_3_0.groupId)

			if var_3_2 then
				var_3_2.star = var_1_2:getStar()

				var_3_1:updateShipGroup(var_3_2)
			end

			var_1_10:consume({
				gold = var_1_8
			})
			getProxy(PlayerProxy):updatePlayer(var_1_10)

			for iter_3_0, iter_3_1 in pairs(var_1_9) do
				arg_1_0:sendNotification(GAME.CONSUME_ITEM, Drop.New({
					type = DROP_TYPE_ITEM,
					id = iter_3_1.itemId,
					count = iter_3_1.count
				}))
			end

			getProxy(MetaCharacterProxy):getMetaProgressVOByID(var_1_3.id):updateShip(var_1_2)
			arg_1_0:sendNotification(GAME.ENERGY_META_ACTIVATION_DONE, {
				newShip = var_1_2,
				oldShip = var_3_0
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_3_0.result))
		end
	end)
end

function var_0_0.updateStar(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	arg_4_1.configId = arg_4_3

	local var_4_0 = pg.ship_data_template[arg_4_1.configId]

	for iter_4_0, iter_4_1 in ipairs(var_4_0.buff_list) do
		if not arg_4_1.skills[iter_4_1] then
			arg_4_1.skills[iter_4_1] = {
				exp = 0,
				level = 1,
				id = iter_4_1
			}
		end
	end

	arg_4_1:updateMaxLevel(var_4_0.max_level)

	local var_4_1 = pg.ship_data_template[arg_4_2].buff_list

	for iter_4_2, iter_4_3 in ipairs(var_4_1) do
		if not table.contains(var_4_0.buff_list, iter_4_3) then
			arg_4_1.skills[iter_4_3] = nil
		end
	end
end

return var_0_0
