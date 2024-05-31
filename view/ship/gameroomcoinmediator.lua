local var_0_0 = class("GameRoomCoinMediator", import("..base.ContextMediator"))

var_0_0.CHANGE_VISIBLE = "GameRoomCoinMediator:CHANGE_VISIBLE"
var_0_0.CHANGE_COIN_NUM = "GameRoomCoinMediator:CHANGE COIN COUNT"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(GameRoomCoinMediator.CHANGE_COIN_NUM, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.GAME_COIN_COUNT_CHANGE, arg_2_1)
	end)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GameRoomCoinMediator.CHANGE_VISIBLE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GameRoomCoinMediator.CHANGE_VISIBLE then
		arg_4_0.viewComponent:changeVisible(var_4_1)
	end
end

return var_0_0
