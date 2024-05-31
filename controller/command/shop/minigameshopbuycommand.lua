local var_0_0 = class("MiniGameShopBuyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1

	var_1_1 = var_1_0 and var_1_0.callback

	local var_1_2 = var_1_0.id
	local var_1_3 = var_1_0.list
	local var_1_4 = pg.gameroom_shop_template[var_1_2]
	local var_1_5 = 0
	local var_1_6 = 0

	for iter_1_0, iter_1_1 in ipairs(var_1_3) do
		local var_1_7 = iter_1_1.id
		local var_1_8 = iter_1_1.num

		var_1_6 = var_1_6 + var_1_8
		var_1_5 = var_1_5 + var_1_4.price * var_1_8
	end

	if var_1_5 > getProxy(GameRoomProxy):getTicket() then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("game_ticket_notenough"),
			onYes = function()
				arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.GAME_HALL)
			end,
			onNo = function()
				return
			end
		})

		return
	end

	pg.ConnectionMgr.GetInstance():Send(26152, {
		goodsid = var_1_2,
		selected = var_1_3
	}, 26153, function(arg_4_0)
		local var_4_0

		if arg_4_0.result == 0 then
			local var_4_1 = id2res(GameRoomProxy.ticket_res_id)

			getProxy(PlayerProxy):getRawData():consume({
				[var_4_1] = var_1_5 or 0
			})

			local var_4_2 = getProxy(ShopsProxy):getMiniShop()

			var_4_2:consume(var_1_2, var_1_6)
			getProxy(ShopsProxy):setMiniShop(var_4_2)

			local var_4_3 = PlayerConst.addTranDrop(arg_4_0.drop_list)

			arg_1_0:sendNotification(GAME.MINI_GAME_SHOP_BUY_DONE, {
				list = var_4_3
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_4_0.result] .. arg_4_0.result)
		end
	end)
end

return var_0_0
