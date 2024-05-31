local var_0_0 = class("TrophyGalleryMediator", import("..base.ContextMediator"))

var_0_0.ON_TROPHY_CLAIM = "TrophyGalleryMediator:ON_TROPHY_CLAIM"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(CollectionProxy)

	arg_1_0:bind(var_0_0.ON_TROPHY_CLAIM, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.TROPHY_CLAIM, {
			trophyID = arg_2_1
		})
	end)

	local var_1_1 = var_1_0:getTrophyGroup()
	local var_1_2 = var_1_0:getTrophys()

	arg_1_0.viewComponent:setTrophyGroups(var_1_1)
	arg_1_0.viewComponent:setTrophyList(var_1_2)
end

function var_0_0.listNotificationInterests(arg_3_0)
	return {
		CollectionProxy.TROPHY_UPDATE,
		GAME.TROPHY_CLAIM_DONE
	}
end

function var_0_0.handleNotification(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:getName()
	local var_4_1 = arg_4_1:getBody()

	if var_4_0 == CollectionProxy.TROPHY_UPDATE then
		-- block empty
	elseif var_4_0 == GAME.TROPHY_CLAIM_DONE then
		local var_4_2 = var_4_1.trophyID

		if pg.medal_template[var_4_2].hide == Trophy.ALWAYS_HIDE then
			return
		end

		local var_4_3 = math.floor(var_4_2 / 10)
		local var_4_4 = getProxy(CollectionProxy)
		local var_4_5 = var_4_4:getTrophyGroup()
		local var_4_6 = var_4_4:getTrophys()

		arg_4_0.viewComponent:setTrophyGroups(var_4_5)
		arg_4_0.viewComponent:setTrophyList(var_4_6)
		arg_4_0.viewComponent:PlayTrophyClaim(var_4_3)
	end
end

return var_0_0
