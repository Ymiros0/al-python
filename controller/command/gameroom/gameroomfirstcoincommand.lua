local var_0_0 = class("GameRoomFirstCoinCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	print("")
	pg.ConnectionMgr.GetInstance():Send(26128, {
		type = 0
	}, 26129, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(GameRoomProxy):setFirstEnter()

			arg_1_0.coinMax = pg.gameset.game_coin_max.key_value
			arg_1_0.myCoinCount = getProxy(GameRoomProxy):getCoin()

			local var_2_0 = arg_1_0.coinMax - arg_1_0.myCoinCount
			local var_2_1 = pg.gameset.game_coin_initial.key_value

			if var_2_0 < var_2_1 then
				var_2_1 = var_2_0
			end

			local var_2_2 = id2res(GameRoomProxy.coin_res_id)

			getProxy(PlayerProxy):getRawData():addResources({
				[var_2_2] = var_2_1 or 0
			})

			local var_2_3 = pg.player_resource[GameRoomProxy.coin_res_id].itemid
			local var_2_4 = {
				{
					id = var_2_3,
					type = DROP_TYPE_ITEM,
					count = var_2_1
				}
			}

			pg.m02:sendNotification(GAME.ROOM_FIRST_COIN_DONE, var_2_4)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
