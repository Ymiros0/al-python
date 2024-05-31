local var_0_0 = class("Dorm3dGiftMediator", import("view.base.ContextMediator"))

var_0_0.GIVE_GIFT = "Dorm3dGiftMediator.GIVE_GIFT"
var_0_0.DO_TALK = "Dorm3dGiftMediator.DO_TALK"
var_0_0.CHECK_LEVEL_UP = "Dorm3dGiftMediator.CHECK_LEVEL_UP"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.GIVE_GIFT, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.APARTMENT_GIVE_GIFT, {
			count = 1,
			groupId = arg_1_0.viewComponent.apartment.configId,
			giftId = arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.DO_TALK, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(Dorm3dSceneMediator.OTHER_DO_TALK, {
			moveCamera = false,
			talkId = arg_3_1,
			callback = arg_3_2
		})
	end)
	arg_1_0:bind(var_0_0.CHECK_LEVEL_UP, function(arg_4_0)
		arg_1_0:sendNotification(Dorm3dSceneMediator.OTHER_CHECK_LEVEL_UP)
	end)
	arg_1_0.viewComponent:SetApartment(getProxy(ApartmentProxy):getApartment(arg_1_0.contextData.groupId))
end

function var_0_0.initNotificationHandleDic(arg_5_0)
	arg_5_0.handleDic = {
		[ApartmentProxy.UPDATE_APARTMENT] = function(arg_6_0, arg_6_1)
			local var_6_0 = arg_6_1:getBody()

			if var_6_0.configId == arg_6_0.contextData.groupId then
				arg_6_0.viewComponent:SetApartment(var_6_0)
				arg_6_0.viewComponent:UpdateFavorPanel()
			end
		end,
		[ApartmentProxy.UPDATE_GIFT_COUNT] = function(arg_7_0, arg_7_1)
			local var_7_0 = arg_7_1:getBody()

			arg_7_0.viewComponent:SingleUpdateGift(var_7_0)
		end,
		[GAME.APARTMENT_GIVE_GIFT_DONE] = function(arg_8_0, arg_8_1)
			local var_8_0 = arg_8_1:getBody()

			arg_8_0.viewComponent:AfterGiveGift(var_8_0)
		end
	}
end

function var_0_0.remove(arg_9_0)
	return
end

return var_0_0
