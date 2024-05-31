local var_0_0 = class("ItemInfoMediator", import("..base.ContextMediator"))

var_0_0.USE_ITEM = "ItemInfoMediator:USE_ITEM"
var_0_0.COMPOSE_ITEM = "ItemInfoMediator:COMPOSE_ITEM"
var_0_0.SELL_BLUEPRINT = "sell blueprint"
var_0_0.EXCHANGE_LOVE_LETTER_ITEM = "ItemInfoMediator.EXCHANGE_LOVE_LETTER_ITEM"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.SELL_BLUEPRINT, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.FRAG_SELL, {
			arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.USE_ITEM, function(arg_3_0, arg_3_1, arg_3_2)
		local var_3_0 = getProxy(BagProxy):getItemById(arg_3_1)

		if not UseItemCommand.Check(var_3_0, arg_3_2) then
			arg_1_0.viewComponent:closeView()

			return
		end

		arg_1_0.viewComponent:PlayOpenBox(var_3_0:getConfig("display_effect"), function()
			arg_1_0:sendNotification(GAME.USE_ITEM, {
				id = arg_3_1,
				count = arg_3_2
			})
		end)
	end)
	arg_1_0:bind(var_0_0.COMPOSE_ITEM, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0:sendNotification(GAME.COMPOSE_ITEM, {
			id = arg_5_1,
			count = arg_5_2
		})
	end)
	arg_1_0:bind(var_0_0.EXCHANGE_LOVE_LETTER_ITEM, function(arg_6_0, arg_6_1)
		arg_1_0:sendNotification(GAME.EXCHANGE_LOVE_LETTER_ITEM, {
			activity_id = arg_6_1
		})
	end)
	arg_1_0.viewComponent:setDrop(arg_1_0.contextData.drop)
end

function var_0_0.listNotificationInterests(arg_7_0)
	return {
		BagProxy.ITEM_UPDATED,
		GAME.USE_ITEM_DONE,
		GAME.FRAG_SELL_DONE
	}
end

function var_0_0.handleNotification(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_1:getName()
	local var_8_1 = arg_8_1:getBody()

	if var_8_0 == BagProxy.ITEM_UPDATED then
		if var_8_1.id == arg_8_0.viewComponent.itemVO.id then
			if var_8_1.count <= 0 then
				arg_8_0.viewComponent:closeView()
			else
				arg_8_0.viewComponent:setItem(Drop.New({
					type = DROP_TYPE_ITEM,
					id = var_8_1.id,
					count = var_8_1.count
				}))
			end
		end
	elseif var_8_0 == GAME.USE_ITEM_DONE then
		arg_8_0.viewComponent:SetOperateCount(1)
	elseif var_8_0 == GAME.FRAG_SELL_DONE then
		arg_8_0.viewComponent:SetOperateCount(1)
	end
end

return var_0_0
