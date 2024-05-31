local var_0_0 = class("SixthAnniversaryIslandShopWindowMediator", import("..base.ContextMediator"))

var_0_0.SHOPPING_CONFIRM = "SixthAnniversaryIslandShopWindowMediator.SHOPPING_CONFIRM"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.SHOPPING_CONFIRM, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.ISLAND_SHOPPING, {
			shop = arg_1_0.contextData.shop,
			arg1 = arg_1_0.contextData.goods.id,
			arg2 = arg_2_1
		})
	end)
	arg_1_0.viewComponent:setGoods(arg_1_0.contextData.goods)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.ISLAND_SHOPPING_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.ISLAND_SHOPPING_DONE then
		arg_4_0.viewComponent:closeView()
	end
end

return var_0_0
