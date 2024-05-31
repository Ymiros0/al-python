local var_0_0 = class("RandomDockYardMediator", import("view.base.ContextMediator"))

var_0_0.OPEN_INDEX = "RandomDockYardMediator:OPEN_INDEX"
var_0_0.ON_ADD_SHIPS = "RandomDockYardMediator:ON_ADD_SHIPS"
var_0_0.ON_REMOVE_SHIPS = "RandomDockYardMediator:ON_REMOVE_SHIPS"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_ADD_SHIPS, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.CHANGE_RANDOM_SHIPS, {
			addList = arg_2_1,
			deleteList = {}
		})
	end)
	arg_1_0:bind(var_0_0.ON_REMOVE_SHIPS, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(GAME.CHANGE_RANDOM_SHIPS, {
			addList = {},
			deleteList = arg_3_1
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_INDEX, function(arg_4_0, arg_4_1)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = RandomDockYardIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_4_1
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_5_0)
	return {
		GAME.CHANGE_RANDOM_SHIPS_DONE
	}
end

function var_0_0.handleNotification(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1:getName()
	local var_6_1 = arg_6_1:getBody()

	if var_6_0 == GAME.CHANGE_RANDOM_SHIPS_DONE then
		arg_6_0.viewComponent:OnChangeRandomShips()
	end
end

return var_0_0
