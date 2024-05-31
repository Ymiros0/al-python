﻿local var_0_0 = class("UseItemCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = var_1_0.arg
	local var_1_4 = getProxy(BagProxy)
	local var_1_5 = var_1_4:getItemById(var_1_1)
	local var_1_6 = var_1_5:getConfig("usage")
	local var_1_7 = var_1_0.skip_check
	local var_1_8 = var_1_0.callback

	if var_1_2 == 0 then
		return
	end

	if var_1_2 > var_1_5.count then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

		return
	end

	if not var_0_0.Check(var_1_5, var_1_2) then
		return
	end

	if var_1_6 == ItemUsage.GUILD_DONATE or var_1_6 == ItemUsage.GUILD_OPERATION then
		if not getProxy(GuildProxy):getRawData() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("not_exist_guild_use_item"))

			return
		end
	elseif var_1_6 == ItemUsage.SKIN_SHOP_DISCOUNT then
		local var_1_9, var_1_10 = var_1_5:GetConsumeForSkinShopDiscount(var_1_3[1])
		local var_1_11 = getProxy(PlayerProxy):getRawData():getResource(var_1_10)

		if var_1_9 > 0 and var_1_11 < var_1_9 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_resource"))

			return
		end
	end

	pg.ConnectionMgr.GetInstance():Send(15002, {
		id = var_1_1,
		count = var_1_2,
		arg = var_1_3
	}, 15003, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = {}

			var_1_4:removeItemById(var_1_1, var_1_2)

			if var_1_6 == ItemUsage.FOOD then
				arg_1_0:sendNotification(GAME.ADD_FOOD, {
					id = var_1_1,
					count = var_1_2
				})
			elseif var_1_6 == ItemUsage.DROP or var_1_6 == ItemUsage.DROP_TEMPLATE or var_1_6 == ItemUsage.DROP_APPOINTED or var_1_6 == ItemUsage.INVITATION or var_1_6 == ItemUsage.SKIN_SELECT then
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)
			elseif var_1_6 == ItemUsage.SKIN_SHOP_DISCOUNT then
				var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)

				local var_2_1, var_2_2 = var_1_5:GetConsumeForSkinShopDiscount(var_1_3[1])

				if var_2_1 > 0 then
					local var_2_3 = getProxy(PlayerProxy):getData()

					var_2_3:consume({
						[id2res(var_2_2)] = var_2_1
					})
					getProxy(PlayerProxy):updatePlayer(var_2_3)
				end

				arg_1_0:sendNotification(GAME.SKIN_SHOPPIGN_DONE, {
					id = var_1_3[1]
				})
			elseif var_1_6 == ItemUsage.DORM_LV_UP then
				arg_1_0:sendNotification(GAME.EXTEND_BACKYARD_AREA)
			elseif var_1_6 == ItemUsage.GUILD_DONATE then
				local var_2_4 = getProxy(GuildProxy):getRawData()

				if var_2_4 then
					var_2_4:AddExtraDonateCnt(var_1_2)
					pg.TipsMgr.GetInstance():ShowTips(i18n("guild_use_donateitem_success", var_1_2))
				end
			elseif var_1_6 == ItemUsage.GUILD_OPERATION then
				local var_2_5 = getProxy(GuildProxy):getRawData()

				if var_2_5 then
					var_2_5:AddExtraBattleCnt(var_1_2)
					pg.TipsMgr.GetInstance():ShowTips(i18n("guild_use_battleitem_success", var_1_2))
				end
			elseif var_1_6 == ItemUsage.REDUCE_COMMANDER_TIME then
				arg_1_0:sendNotification(GAME.REFRESH_COMMANDER_BOXES)
			else
				assert(false, "未处理类型" .. var_1_6)
			end

			local var_2_6 = QRJ_ITEM_ID_RANGE

			if var_1_1 >= var_2_6[1] and var_1_1 <= var_2_6[2] then
				table.sort(var_2_0, function(arg_3_0, arg_3_1)
					return arg_3_0.count < arg_3_1.count
				end)
			end

			if var_1_8 then
				var_1_8(var_2_0)
			end

			arg_1_0:sendNotification(GAME.USE_ITEM_DONE, var_2_0)
		else
			if var_1_8 then
				var_1_8({})
			end

			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

function var_0_0.Check(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0:GetOverflowCheckItems(arg_4_1)
	local var_4_1 = GetItemsOverflowDic(var_4_0)
	local var_4_2, var_4_3 = CheckOverflow(var_4_1)

	if not var_4_2 then
		switch(var_4_3, {
			gold = function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title"))
			end,
			oil = function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("oil_max_tip_title"))
			end,
			equip = function()
				NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)
			end,
			ship = function()
				NoPosMsgBox(i18n("switch_to_shop_tip_noDockyard"), openDockyardClear, gotoChargeScene, openDockyardIntensify)
			end
		})

		return false
	end

	return true
end

return var_0_0
