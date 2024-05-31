local var_0_0 = class("WorldCollectionMediator", import("..base.ContextMediator"))

var_0_0.ON_ACHIEVE_STAR = "WorldCollectionMediator.ON_ACHIEVE_STAR"
var_0_0.ON_ACHIEVE_OVERVIEW = "WorldCollectionMediator.ON_ACHIEVE_OVERVIEW"
var_0_0.ON_MAP = "WorldCollectionMediator.ON_MAP"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_ACHIEVE_STAR, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.WORLD_ACHIEVE, {
			list = arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_ACHIEVE_OVERVIEW, function(arg_3_0)
		arg_1_0:sendNotification(WorldMediator.OnOpenMarkMap, {
			mode = "Achievement"
		})
	end)
	arg_1_0:bind(var_0_0.ON_MAP, function(arg_4_0, arg_4_1)
		arg_1_0:sendNotification(var_0_0.ON_MAP, {
			entrance = arg_4_1,
			mapTypes = {
				"complete_chapter",
				"base_chapter"
			}
		})
	end)
	arg_1_0.viewComponent:SetAchievementList(nowWorld():GetAtlas():GetAchEntranceList())
end

function var_0_0.listNotificationInterests(arg_5_0)
	return {
		GAME.WORLD_ACHIEVE_DONE
	}
end

function var_0_0.handleNotification(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1:getName()
	local var_6_1 = arg_6_1:getBody()

	if var_6_0 == GAME.WORLD_ACHIEVE_DONE then
		arg_6_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_6_1.drops, function()
			arg_6_0.viewComponent:flushAchieveUpdate(var_6_1.list)
		end)
	end
end

return var_0_0
