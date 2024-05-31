local var_0_0 = class("GameRoomWeekCoinCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	pg.ConnectionMgr.GetInstance().Send(26122, {
		type = 0
	}, 26123, function(arg_2_0)
		local var_2_0

		if arg_2_0.result == 0:
			arg_1_0.coinMax = pg.gameset.game_coin_max.key_value
			arg_1_0.myCoinCount = getProxy(GameRoomProxy).getCoin()

			local var_2_1 = arg_1_0.coinMax - arg_1_0.myCoinCount
			local var_2_2 = pg.gameset.game_coin_initial.key_value

			if var_2_1 < var_2_2:
				var_2_2 = var_2_1

			local var_2_3 = id2res(GameRoomProxy.coin_res_id)

			getProxy(PlayerProxy).getRawData().addResources({
				[var_2_3] = var_2_2 or 0
			})

			local var_2_4 = pg.player_resource[GameRoomProxy.coin_res_id].itemid
			local var_2_5 = {
				{
					id = var_2_4,
					type = DROP_TYPE_ITEM,
					count = var_2_2
				}
			}

			getProxy(GameRoomProxy).setWeekly()
			pg.m02.sendNotification(GAME.GAME_ROOM_AWARD_DONE, var_2_5)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
