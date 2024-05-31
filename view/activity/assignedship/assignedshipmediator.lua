﻿local var_0_0 = class("AssignedShipMediator", import("...base.ContextMediator"))

var_0_0.ON_USE_ITEM = "AssignedShipMediator:ON_USE_ITEM"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_USE_ITEM, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		arg_1_0:sendNotification(GAME.USE_ITEM, {
			id = arg_2_1,
			count = arg_2_2,
			arg = arg_2_3
		})
	end)
	arg_1_0.viewComponent:setItemVO(arg_1_0.contextData.itemVO)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		GAME.USE_ITEM_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == GAME.USE_ITEM_DONE then
		arg_4_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_4_1, function()
			triggerButton(arg_4_0.viewComponent.backBtn)
		end)
	end
end

return var_0_0
