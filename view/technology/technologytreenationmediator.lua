﻿local var_0_0 = class("TechnologyTreeNationMediator", import("..base.ContextMediator"))

function var_0_0.register(arg_1_0)
	arg_1_0:bind(TechnologyConst.CLICK_UP_TEC_BTN, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.START_CAMP_TEC, {
			tecID = arg_2_1,
			levelID = arg_2_2
		})
	end)
	arg_1_0:bind(TechnologyConst.FINISH_UP_TEC, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(GAME.FINISH_CAMP_TEC, {
			tecID = arg_3_1,
			levelID = arg_3_2
		})
	end)
	arg_1_0:bind(TechnologyConst.OPEN_ALL_BUFF_DETAIL, function()
		arg_1_0:addSubLayers(Context.New({
			mediator = AllBuffDetailMediator,
			viewComponent = AllBuffDetailLayer,
			data = {}
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_5_0)
	return {
		TechnologyConst.START_TEC_BTN_SUCCESS,
		TechnologyConst.FINISH_TEC_SUCCESS,
		TechnologyConst.CLOSE_TECHNOLOGY_NATION_LAYER_NOTIFICATION,
		TechnologyConst.GOT_TEC_CAMP_AWARD,
		TechnologyConst.GOT_TEC_CAMP_AWARD_ONESTEP
	}
end

function var_0_0.handleNotification(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1:getName()
	local var_6_1 = arg_6_1:getBody()

	if var_6_0 == TechnologyConst.START_TEC_BTN_SUCCESS then
		arg_6_0.viewComponent:updateTecListData()
		arg_6_0.viewComponent:updateTecItem(var_6_1)
	elseif var_6_0 == TechnologyConst.FINISH_TEC_SUCCESS then
		arg_6_0.viewComponent:updateTecListData()
		arg_6_0.viewComponent:updateTecItem(var_6_1)
	elseif var_6_0 == TechnologyConst.CLOSE_TECHNOLOGY_NATION_LAYER_NOTIFICATION then
		arg_6_0.viewComponent:closeMyself()
	elseif var_6_0 == TechnologyConst.GOT_TEC_CAMP_AWARD then
		local var_6_2 = var_6_1.awardList
		local var_6_3 = var_6_1.groupID
		local var_6_4 = var_6_1.tecID

		arg_6_0.viewComponent:updateTecItem(var_6_3)
		arg_6_0.viewComponent:updateOneStepBtn()
		arg_6_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_6_2)
	elseif var_6_0 == TechnologyConst.GOT_TEC_CAMP_AWARD_ONESTEP then
		local var_6_5 = var_6_1.awardList

		arg_6_0.viewComponent:updateTecItemList()
		arg_6_0.viewComponent:updateOneStepBtn()
		arg_6_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_6_5)
	end
end

return var_0_0
