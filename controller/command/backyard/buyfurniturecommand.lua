local var_0_0 = class("BuyFurnitureCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.furnitureIds
	local var_1_2 = var_1_0.type
	local var_1_3 = getProxy(DormProxy)
	local var_1_4 = getProxy(PlayerProxy)
	local var_1_5 = var_1_4:getData()

	if #var_1_1 == 0 or not var_1_2 then
		return
	end

	local var_1_6 = 0

	for iter_1_0, iter_1_1 in ipairs(var_1_1) do
		local var_1_7 = Furniture.New({
			id = iter_1_1
		})

		if not var_1_7:inTime() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("buy_furniture_overtime"))

			return
		elseif var_1_2 == 4 then
			local var_1_8 = var_1_7:getPrice(4)

			assert(var_1_8 > 0, "furniture price should more than zero>>" .. var_1_7.id)

			var_1_6 = var_1_6 + var_1_8
		elseif var_1_2 == 6 then
			local var_1_9 = var_1_7:getPrice(6)

			assert(var_1_9 > 0, "furniture price should more than zero>>" .. var_1_7.id)

			var_1_6 = var_1_6 + var_1_9
		end
	end

	if var_1_6 > var_1_5:getResById(var_1_2) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_resource"))

		return
	end

	local function var_1_10()
		pg.ConnectionMgr.GetInstance():Send(19006, {
			furniture_id = var_1_1,
			currency = var_1_2
		}, 19007, function(arg_3_0)
			if arg_3_0.result == 0 then
				var_1_5:consume({
					[id2res(var_1_2)] = var_1_6
				})
				var_1_4:updatePlayer(var_1_5)

				local var_3_0 = var_1_1[1]
				local var_3_1 = pg.furniture_data_template[var_3_0]

				if var_3_1 and var_3_1.themeId > 0 then
					var_1_3:ResetSystemTheme(var_3_1.themeId)
				end

				var_1_3:AddFurnitrues(var_1_1)
				arg_1_0:UpdateLinkActivity(var_1_1)
				arg_1_0:sendNotification(GAME.BUY_FURNITURE_DONE, var_1_3:getData(), var_1_1)
				pg.TipsMgr.GetInstance():ShowTips(i18n("common_buy_success"))
			else
				pg.TipsMgr.GetInstance():ShowTips(errorTip("backyard_buyFurniture_error", arg_3_0.result))
			end
		end)
	end

	if var_1_2 == 4 then
		local var_1_11 = i18n("word_furniture")

		if #var_1_1 == 1 then
			var_1_11 = Furniture.New({
				id = var_1_1[1]
			}):getConfig("name")
		end

		if _BackyardMsgBoxMgr then
			_BackyardMsgBoxMgr:Show({
				content = i18n("charge_scene_buy_confirm_backyard", var_1_6, var_1_11),
				onYes = function()
					var_1_10()
				end
			})
		else
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("charge_scene_buy_confirm", var_1_6, var_1_11),
				onYes = function()
					var_1_10()
				end
			})
		end
	else
		var_1_10()
	end
end

function var_0_0.UpdateLinkActivity(arg_6_0, arg_6_1)
	local var_6_0 = getProxy(ActivityProxy)
	local var_6_1 = var_6_0:getActivityByType(ActivityConst.ACTIVITY_TYPE_LINK_COLLECT)

	if var_6_1 and not var_6_1:isEnd() then
		local var_6_2 = pg.activity_limit_item_guide.get_id_list_by_activity[var_6_1.id]

		assert(var_6_2, "activity_limit_item_guide not exist activity id: " .. var_6_1.id)

		for iter_6_0, iter_6_1 in ipairs(arg_6_1) do
			for iter_6_2, iter_6_3 in ipairs(var_6_2) do
				local var_6_3 = pg.activity_limit_item_guide[iter_6_3]

				if var_6_3.type == DROP_TYPE_FURNITURE and iter_6_1 == var_6_3.drop_id then
					local var_6_4 = var_6_1:getKVPList(1, var_6_3.id) + 1

					var_6_1:updateKVPList(1, var_6_3.id, var_6_4)
				end
			end
		end

		var_6_0:updateActivity(var_6_1)
	end
end

return var_0_0
