local var_0_0 = class("GameRoomExchangeCoinCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.times
	local var_1_2 = var_1_0.price

	pg.ConnectionMgr.GetInstance().Send(26124, {
		times = var_1_1
	}, 26125, function(arg_2_0)
		if arg_2_0.result == 0:
			arg_1_0.coinMax = pg.gameset.game_coin_max.key_value
			arg_1_0.myCoinCount = getProxy(GameRoomProxy).getCoin()

			local var_2_0 = arg_1_0.coinMax - arg_1_0.myCoinCount

			if var_2_0 < var_1_1:
				var_1_1 = var_2_0

			local var_2_1 = id2res(GameRoomProxy.coin_res_id)

			getProxy(GameRoomProxy).setPayCoinCount(var_1_1)

			local var_2_2 = getProxy(PlayerProxy).getRawData()

			var_2_2.addResources({
				[var_2_1] = var_1_1 or 0
			})
			var_2_2.consume({
				gold = var_1_2 or 0
			})
			getProxy(PlayerProxy).updatePlayer(var_2_2)

			local var_2_3 = pg.player_resource[GameRoomProxy.coin_res_id].itemid
			local var_2_4 = {
				{
					id = var_2_3,
					type = DROP_TYPE_ITEM,
					count = var_1_1
				}
			}

			pg.m02.sendNotification(GAME.GAME_ROOM_AWARD_DONE, var_2_4)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
