﻿local var_0_0 = class("FeastMediator", import("view.backYard.CourtYardMediator"))

var_0_0.SET_UP = "FeastMediator:SET_UP"
var_0_0.MAKE_TICKET = "FeastMediator:MAKE_TICKET"
var_0_0.GIVE_TICKET = "FeastMediator:GIVE_TICKET"
var_0_0.GIVE_GIFT = "FeastMediator:GIVE_GIFT"
var_0_0.EVENT_PT_OPERATION = "FeastMediator:EVENT_PT_OPERATION"
var_0_0.ON_SUBMIT = "FeastMediator:ON_SUBMIT"
var_0_0.ON_GO = "FeastMediator:ON_GO"
var_0_0.ON_SUBMIT_ONE_KEY = "FeastMediator:ON_SUBMIT_ONE_KEY"
var_0_0.ON_SHIP_ENTER_FEAST = "FeastMediator:ON_SHIP_ENTER_FEAST"

function var_0_0.register(arg_1_0)
	arg_1_0.caches = {}

	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST)

	arg_1_0:bind(var_0_0.SET_UP, function(arg_2_0, arg_2_1)
		local var_2_0 = arg_1_0:GenCourtYardData(arg_2_1)

		_courtyard = CourtYardBridge.New(var_2_0)
	end)
	arg_1_0:bind(var_0_0.MAKE_TICKET, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(GAME.FEAST_OP, {
			activityId = var_1_0.id,
			cmd = FeastDorm.OP_MAKE_TICKET,
			arg1 = arg_3_1
		})
	end)
	arg_1_0:bind(var_0_0.GIVE_TICKET, function(arg_4_0, arg_4_1)
		arg_1_0:sendNotification(GAME.FEAST_OP, {
			activityId = var_1_0.id,
			cmd = FeastDorm.OP_GIVE_TICKET,
			arg1 = arg_4_1
		})
	end)
	arg_1_0:bind(var_0_0.GIVE_GIFT, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.FEAST_OP, {
			activityId = var_1_0.id,
			cmd = FeastDorm.OP_GIVE_GIFT,
			arg1 = arg_5_1
		})
	end)
	arg_1_0:bind(var_0_0.EVENT_PT_OPERATION, function(arg_6_0, arg_6_1)
		arg_1_0:sendNotification(GAME.ACT_NEW_PT, arg_6_1)
	end)
	arg_1_0:bind(var_0_0.ON_SUBMIT, function(arg_7_0, arg_7_1)
		arg_1_0:sendNotification(GAME.SUBMIT_TASK, arg_7_1)
	end)
	arg_1_0:bind(var_0_0.ON_GO, function(arg_8_0, arg_8_1)
		arg_1_0:HandleTaskGo(arg_8_1)
	end)
	arg_1_0:bind(var_0_0.ON_SUBMIT_ONE_KEY, function(arg_9_0, arg_9_1)
		arg_1_0:sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
			resultList = arg_9_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_SHIP_ENTER_FEAST, function(arg_10_0, arg_10_1)
		if _courtyard then
			_courtyard:GetController():ShipEnterFeast(arg_10_1)
		end
	end)
	arg_1_0:sendNotification(GAME.FEAST_OP, {
		activityId = var_1_0.id,
		cmd = FeastDorm.OP_ENTER
	})
end

function var_0_0.HandleTaskGo(arg_11_0, arg_11_1)
	if arg_11_1:IsActRoutineType() and arg_11_1:getConfig("sub_type") == 430 then
		-- block empty
	elseif arg_11_1:IsActRoutineType() and arg_11_1:getConfig("sub_type") == 431 then
		arg_11_0.viewComponent:emit(FeastScene.GO_INTERACTION)
	elseif arg_11_1:IsActType() and (arg_11_1:getConfig("sub_type") == 432 or arg_11_1:getConfig("sub_type") == 433) then
		arg_11_0.viewComponent:emit(FeastScene.GO_INVITATION)
	elseif arg_11_1:IsActType() and arg_11_1:getConfig("sub_type") == 417 then
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 56)
	else
		arg_11_0:sendNotification(GAME.TASK_GO, {
			taskVO = arg_11_1
		})
	end
end

function var_0_0.listNotificationInterests(arg_12_0)
	return {
		CourtYardEvent._QUIT,
		CourtYardEvent._INITED,
		CourtYardEvent._FEAST_INTERACTION,
		GAME.ACT_NEW_PT_DONE,
		GAME.SUBMIT_TASK_DONE,
		GAME.FEAST_OP_DONE,
		TaskProxy.TASK_ADDED,
		TaskProxy.TASK_UPDATED,
		TaskProxy.TASK_REMOVED,
		ActivityProxy.ACTIVITY_UPDATED
	}
end

function var_0_0.handleNotification(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1:getName()
	local var_13_1 = arg_13_1:getBody()
	local var_13_2 = arg_13_1:getType()

	if var_13_0 == CourtYardEvent._QUIT then
		arg_13_0.viewComponent:emit(BaseUI.ON_BACK)
	elseif var_13_0 == CourtYardEvent._INITED then
		arg_13_0.viewComponent:OnCourtYardLoaded()
	elseif var_13_0 == CourtYardEvent._FEAST_INTERACTION then
		local var_13_3 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_FEAST)

		if not var_13_3 or var_13_3:isEnd() then
			return
		end

		local var_13_4 = var_13_1.groupId
		local var_13_5 = var_13_1.special

		arg_13_0:sendNotification(GAME.FEAST_OP, {
			activityId = var_13_3.id,
			cmd = FeastDorm.OP_INTERACTION,
			arg1 = var_13_4,
			arg2 = var_13_5
		})
	elseif var_13_0 == GAME.FEAST_OP_DONE then
		local var_13_6 = 0
		local var_13_7 = true

		if var_13_1.cmd == FeastDorm.OP_INTERACTION then
			_courtyard:GetController():UpdateBubble(var_13_1.groupId, var_13_1.value)

			if var_13_1.chat and var_13_1.chat ~= "" then
				_courtyard:GetController():UpdateChatBubble(var_13_1.groupId, var_13_1.chat)
			end

			var_13_6 = CourtYardConst.FEAST_EFFECT_TIME
		elseif var_13_1.cmd == FeastDorm.OP_GIVE_TICKET then
			local var_13_8 = getProxy(FeastProxy):getRawData():GetFeastShip(var_13_1.groupId)

			_courtyard:GetController():AddShipWithSpecialPosition(var_13_8)
			arg_13_0.viewComponent:emit(FeastScene.ON_GOT_TICKET, var_13_1.awards)

			local var_13_9 = getProxy(FeastProxy):getRawData():GetInvitedFeastShip(var_13_1.groupId)

			var_13_7 = false
		elseif var_13_1.cmd == FeastDorm.OP_RANDOM_SHIPS then
			_courtyard:GetController():ExitAllShip()

			local var_13_10 = {}

			for iter_13_0, iter_13_1 in ipairs(var_13_1.ships or {}) do
				table.insert(var_13_10, function(arg_14_0)
					_courtyard:GetController():AddShip(iter_13_1)
					onNextTick(arg_14_0)
				end)
			end

			seriesAsync(var_13_10)
		elseif var_13_1.cmd == FeastDorm.OP_GIVE_GIFT then
			arg_13_0.viewComponent:emit(FeastScene.ON_GOT_GIFT, var_13_1.awards)

			local var_13_11 = getProxy(FeastProxy):getRawData():GetInvitedFeastShip(var_13_1.groupId)

			var_13_7 = false
		elseif var_13_1.cmd == FeastDorm.OP_MAKE_TICKET then
			arg_13_0.viewComponent:emit(FeastScene.ON_MAKE_TICKET, var_13_1.groupId)
		end

		if #var_13_1.awards > 0 and var_13_7 then
			local var_13_12 = var_13_1.cmd == FeastDorm.OP_INTERACTION and #arg_13_0.caches == 0 and var_13_6 or 0

			table.insert(arg_13_0.caches, {
				var_13_1.awards,
				var_13_12
			})

			if #arg_13_0.caches == 1 then
				arg_13_0:DisplayAwards()
			end
		end
	elseif var_13_0 == TaskProxy.TASK_ADDED or var_13_0 == TaskProxy.TASK_UPDATED or var_13_0 == TaskProxy.TASK_REMOVED then
		arg_13_0.viewComponent:emit(FeastScene.ON_TASK_UPDATE)
	elseif var_13_0 == ActivityProxy.ACTIVITY_UPDATED then
		if var_13_1.id == ActivityConst.FEAST_PT_ACT then
			arg_13_0.viewComponent:emit(FeastScene.ON_ACT_UPDATE)
		end
	elseif var_13_0 == GAME.SUBMIT_TASK_DONE then
		arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1, function()
			local var_15_0 = var_13_2

			getProxy(FeastProxy):HandleTaskStories(var_15_0)
		end)
	elseif var_13_0 == GAME.ACT_NEW_PT_DONE then
		arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1.awards, function()
			return
		end)
	end
end

function var_0_0.DisplayAwards(arg_17_0)
	local var_17_0 = arg_17_0.caches[1]
	local var_17_1 = var_17_0[1]
	local var_17_2 = var_17_0[2]
	local var_17_3 = {}

	if var_17_2 > 0 then
		table.insert(var_17_3, function(arg_18_0)
			if not arg_17_0.viewComponent then
				return
			end

			onDelayTick(arg_18_0, var_17_2, 1)
		end)
	end

	table.insert(var_17_3, function(arg_19_0)
		if not arg_17_0.viewComponent then
			return
		end

		arg_17_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_17_1, arg_19_0)
	end)
	seriesAsync(var_17_3, function()
		table.remove(arg_17_0.caches, 1)

		if #arg_17_0.caches > 0 then
			arg_17_0:DisplayAwards()
		end
	end)
end

return var_0_0
