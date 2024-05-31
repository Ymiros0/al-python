local var_0_0 = class("MetaCharacterRepairCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.shipID
	local var_1_2 = var_1_0.attr
	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = var_1_3:getShipById(var_1_1)
	local var_1_5 = var_1_4:getMetaCharacter()
	local var_1_6 = var_1_5:getAttrVO(var_1_2)
	local var_1_7 = var_1_6:getItem()
	local var_1_8 = var_1_7:getTotalCnt()
	local var_1_9 = var_1_7:getItemId()

	if var_1_8 > getProxy(BagProxy):getItemCountById(var_1_9) then
		return
	end

	if var_1_6:isMaxLevel() then
		return
	end

	print("63301 meta repair:", var_1_1, var_1_7.id)
	pg.ConnectionMgr.GetInstance():Send(63301, {
		ship_id = var_1_1,
		repair_id = var_1_7.id
	}, 63302, function(arg_2_0)
		if arg_2_0.result == 0 then
			print("63302 meta repair success:")
			var_1_6:levelUp()
			var_1_3:updateShip(var_1_4)
			getProxy(MetaCharacterProxy):getMetaProgressVOByID(var_1_5.id):updateShip(var_1_4)
			arg_1_0:sendNotification(GAME.CONSUME_ITEM, Drop.New({
				type = DROP_TYPE_ITEM,
				id = var_1_9,
				count = var_1_8
			}))
			arg_1_0:sendNotification(GAME.REPAIR_META_CHARACTER_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
