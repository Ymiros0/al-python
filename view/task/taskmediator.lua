local var_0_0 = class("TaskMediator", import("..base.ContextMediator"))

var_0_0.ON_TASK_SUBMIT = "TaskMediator:ON_TASK_SUBMIT"
var_0_0.ON_TASK_GO = "TaskMediator:ON_TASK_GO"
var_0_0.TASK_FILTER = "TaskMediator:TASK_FILTER"
var_0_0.ON_SUBMIT_AVATAR_TASK = "TaskMediator:ON_SUBMIT_AVATAR_TASK"
var_0_0.ON_SUBMIT_WEEK_PROGREE = "TaskMediator:ON_SUBMIT_WEEK_PROGREE"
var_0_0.ON_BATCH_SUBMIT_WEEK_TASK = "TaskMediator:ON_BATCH_SUBMIT_WEEK_TASK"
var_0_0.ON_SUBMIT_WEEK_TASK = "TaskMediator:ON_SUBMIT_WEEK_TASK"
var_0_0.CLICK_GET_ALL = "TaskMediator:CLICK_GET_ALL"
var_0_0.ON_DROP = "TaskMediator:ON_DROP"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_SUBMIT_WEEK_TASK, function(arg_2_0, arg_2_1)
		arg_1_0:sendNotification(GAME.SUBMIT_WEEK_TASK, {
			id = arg_2_1.id
		})
	end)
	arg_1_0:bind(var_0_0.ON_SUBMIT_AVATAR_TASK, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(GAME.AVATAR_FRAME_AWARD, {
			act_id = arg_3_1.actId,
			task_ids = {
				arg_3_1.id
			}
		})
	end)
	arg_1_0:bind(var_0_0.ON_SUBMIT_WEEK_PROGREE, function(arg_4_0)
		arg_1_0:sendNotification(GAME.SUBMIT_WEEK_TASK_PROGRESS)
	end)
	arg_1_0:bind(var_0_0.ON_BATCH_SUBMIT_WEEK_TASK, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0:sendNotification(GAME.BATCH_SUBMIT_WEEK_TASK, {
			ids = arg_5_1,
			callback = arg_5_2
		})
	end)
	arg_1_0:bind(var_0_0.ON_DROP, function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_1.type == DROP_TYPE_EQUIP then
			arg_1_0:addSubLayers(Context.New({
				mediator = EquipmentInfoMediator,
				viewComponent = EquipmentInfoLayer,
				data = {
					equipmentId = arg_6_1:getConfig("id"),
					type = EquipmentInfoMediator.TYPE_DISPLAY,
					onRemoved = arg_6_2,
					LayerWeightMgr_weight = LayerWeightConst.THIRD_LAYER
				}
			}))
		elseif arg_6_1.type == DROP_TYPE_SPWEAPON then
			arg_1_0:addSubLayers(Context.New({
				mediator = SpWeaponInfoMediator,
				viewComponent = SpWeaponInfoLayer,
				data = {
					spWeaponConfigId = arg_6_1:getConfig("id"),
					type = SpWeaponInfoLayer.TYPE_DISPLAY,
					onRemoved = arg_6_2,
					LayerWeightMgr_weight = LayerWeightConst.THIRD_LAYER
				}
			}))
		else
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				type = MSGBOX_TYPE_SINGLE_ITEM,
				drop = arg_6_1,
				onNo = arg_6_2,
				onYes = arg_6_2,
				weight = LayerWeightConst.THIRD_LAYER
			})
		end
	end)
	arg_1_0:bind(var_0_0.ON_TASK_SUBMIT, function(arg_7_0, arg_7_1)
		local var_7_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.JYHZ_ACTIVITY_ID)

		if var_7_0 then
			local var_7_1 = var_7_0:getConfig("config_data")
			local var_7_2 = _.flatten(var_7_1)

			if arg_7_1.id == var_7_2[#var_7_2] then
				pg.NewStoryMgr.GetInstance():Play("YIXIAN8", function()
					arg_1_0:sendNotification(GAME.SUBMIT_TASK, arg_7_1.id)
				end)

				return
			end
		end

		if arg_7_1.index then
			arg_1_0:sendNotification(GAME.SUBMIT_TASK, {
				taskId = arg_7_1.id,
				index = arg_7_1.index
			})
		else
			arg_1_0:sendNotification(GAME.SUBMIT_TASK, arg_7_1.id)
		end
	end)
	arg_1_0:bind(var_0_0.ON_TASK_GO, function(arg_9_0, arg_9_1)
		arg_1_0:sendNotification(GAME.TASK_GO, {
			taskVO = arg_9_1
		})
	end)
	arg_1_0:SetTaskVOs()

	local var_1_0 = getProxy(TaskProxy)

	arg_1_0.viewComponent:SetWeekTaskProgressInfo(var_1_0:GetWeekTaskProgressInfo())
end

function var_0_0.SetTaskVOs(arg_10_0)
	local var_10_0 = getProxy(TaskProxy):getData()
	local var_10_1 = getProxy(BagProxy)

	for iter_10_0, iter_10_1 in pairs(var_10_0) do
		if iter_10_1:getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM then
			local var_10_2 = tonumber(iter_10_1:getConfig("target_id"))

			iter_10_1.progress = var_10_1:getItemCountById(tonumber(var_10_2))
		elseif iter_10_1:getConfig("sub_type") == TASK_SUB_TYPE_GIVE_VIRTUAL_ITEM then
			local var_10_3 = tonumber(iter_10_1:getConfig("target_id"))

			iter_10_1.progress = getProxy(ActivityProxy):getVirtualItemNumber(var_10_3)
		end
	end

	arg_10_0.viewComponent:setTaskVOs(var_10_0)
end

function var_0_0.enterLevel(arg_11_0, arg_11_1)
	local var_11_0 = getProxy(ChapterProxy):getChapterById(arg_11_1)

	if var_11_0 then
		local var_11_1 = {
			mapIdx = var_11_0:getConfig("map")
		}

		if var_11_0.active then
			var_11_1.chapterId = var_11_0.id
		else
			var_11_1.openChapterId = arg_11_1
		end

		arg_11_0:sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_11_1)
	end
end

function var_0_0.listNotificationInterests(arg_12_0)
	return {
		TaskProxy.TASK_ADDED,
		TaskProxy.TASK_UPDATED,
		TaskProxy.TASK_REMOVED,
		GAME.SUBMIT_TASK_DONE,
		var_0_0.TASK_FILTER,
		GAME.BEGIN_STAGE_DONE,
		GAME.CHAPTER_OP_DONE,
		TaskProxy.WEEK_TASK_UPDATED,
		TaskProxy.WEEK_TASKS_ADDED,
		TaskProxy.WEEK_TASKS_DELETED,
		GAME.SUBMIT_WEEK_TASK_DONE,
		GAME.SUBMIT_WEEK_TASK_PROGRESS_DONE,
		GAME.SUBMIT_AVATAR_TASK_DONE,
		TaskProxy.WEEK_TASK_RESET,
		GAME.MERGE_TASK_ONE_STEP_AWARD_DONE,
		AvatarFrameProxy.FRAME_TASK_TIME_OUT
	}
end

function var_0_0.handleNotification(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1:getName()
	local var_13_1 = arg_13_1:getBody()

	if var_13_0 == TaskProxy.TASK_ADDED then
		if var_13_1:getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM then
			local var_13_2 = tonumber(var_13_1:getConfig("target_id"))

			var_13_1.progress = getProxy(BagProxy):getItemCountById(tonumber(var_13_2))
		elseif var_13_1:getConfig("sub_type") == TASK_SUB_TYPE_GIVE_VIRTUAL_ITEM then
			local var_13_3 = tonumber(var_13_1:getConfig("target_id"))

			var_13_1.progress = getProxy(ActivityProxy):getVirtualItemNumber(var_13_3)
		end

		arg_13_0.viewComponent:addTask(var_13_1)
	elseif var_13_0 == GAME.CHAPTER_OP_DONE then
		if arg_13_0.chapterId then
			arg_13_0:enterLevel(arg_13_0.chapterId)

			arg_13_0.chapterId = nil
		end
	elseif var_13_0 == TaskProxy.TASK_UPDATED then
		if var_13_1:getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM then
			local var_13_4 = tonumber(var_13_1:getConfig("target_id"))

			var_13_1.progress = getProxy(BagProxy):getItemCountById(tonumber(var_13_4))
		elseif var_13_1:getConfig("sub_type") == TASK_SUB_TYPE_GIVE_VIRTUAL_ITEM then
			local var_13_5 = tonumber(var_13_1:getConfig("target_id"))

			var_13_1.progress = getProxy(ActivityProxy):getVirtualItemNumber(var_13_5)
		end

		arg_13_0.viewComponent:updateTask(var_13_1)
	elseif var_13_0 == TaskProxy.TASK_REMOVED then
		arg_13_0.viewComponent:removeTask(var_13_1)
	elseif var_13_0 == var_0_0.TASK_FILTER then
		arg_13_0.viewComponent:GoToFilter(var_13_1)
	elseif var_13_0 == GAME.SUBMIT_TASK_DONE then
		local var_13_6 = arg_13_1:getType()
		local var_13_7 = getProxy(TaskProxy)

		arg_13_0.viewComponent.onShowAwards = true

		arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1, function()
			arg_13_0.viewComponent.onShowAwards = nil

			arg_13_0:accepetActivityTask()
			arg_13_0.viewComponent:updateOneStepBtn()

			local var_14_0 = {}

			for iter_14_0, iter_14_1 in ipairs(var_13_6) do
				table.insert(var_14_0, function(arg_15_0)
					arg_13_0:PlayStoryForTaskAct(iter_14_1, arg_15_0)
				end)
			end

			if arg_13_0.refreshWeekTaskPageFlag then
				arg_13_0.viewComponent:RefreshWeekTaskPage()

				arg_13_0.refreshWeekTaskPageFlag = nil
			end

			table.insert(var_14_0, function(arg_16_0)
				getProxy(FeastProxy):HandleTaskStories(var_13_6, arg_16_0)
			end)

			if #var_14_0 > 0 then
				seriesAsync(var_14_0)
			end
		end)
	elseif var_13_0 == GAME.BEGIN_STAGE_DONE then
		arg_13_0:sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_13_1)
	elseif var_13_0 == TaskProxy.WEEK_TASKS_ADDED or var_13_0 == TaskProxy.WEEK_TASKS_DELETED or var_13_0 == TaskProxy.WEEK_TASK_UPDATED then
		arg_13_0.viewComponent:RefreshWeekTaskPage()
	elseif var_13_0 == GAME.SUBMIT_WEEK_TASK_DONE then
		arg_13_0.viewComponent:RefreshWeekTaskPageBefore(var_13_1.id)

		local function var_13_8()
			arg_13_0.viewComponent:RefreshWeekTaskPage()
		end

		if #var_13_1.awards > 0 then
			arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1.awards, var_13_8)
		else
			var_13_8()
		end
	elseif var_13_0 == GAME.SUBMIT_WEEK_TASK_PROGRESS_DONE then
		local function var_13_9()
			arg_13_0.viewComponent:RefreshWeekTaskProgress()
		end

		if #var_13_1.awards > 0 then
			arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1.awards, var_13_9)
		else
			var_13_9()
		end
	elseif var_13_0 == GAME.SUBMIT_AVATAR_TASK_DONE then
		local function var_13_10()
			arg_13_0.viewComponent:refreshPage()

			if var_13_1.callback then
				var_13_1.callback()
			end
		end

		if #var_13_1.awards > 0 then
			arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1.awards, var_13_10)
		else
			var_13_10()
		end
	elseif var_13_0 == TaskProxy.WEEK_TASK_RESET then
		arg_13_0:SetTaskVOs()
		arg_13_0.viewComponent:ResetWeekTaskPage()
	elseif var_13_0 == GAME.MERGE_TASK_ONE_STEP_AWARD_DONE then
		arg_13_0.refreshWeekTaskPageFlag = true

		arg_13_0:sendNotification(GAME.SUBMIT_TASK_DONE, var_13_1.awards, var_13_1.taskIds)
	elseif var_13_0 == AvatarFrameProxy.FRAME_TASK_TIME_OUT then
		arg_13_0.viewComponent:refreshPage()
	end
end

function var_0_0.accepetActivityTask(arg_20_0)
	arg_20_0:sendNotification(GAME.ACCEPT_ACTIVITY_TASK)
end

function var_0_0.PlayStoryForTaskAct(arg_21_0, arg_21_1, arg_21_2)
	local var_21_0 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST)
	local var_21_1

	for iter_21_0, iter_21_1 in ipairs(var_21_0) do
		if iter_21_1 and not iter_21_1:isEnd() then
			local var_21_2 = iter_21_1:getConfig("config_data")
			local var_21_3 = 0
			local var_21_4 = 0

			for iter_21_2, iter_21_3 in ipairs(var_21_2) do
				for iter_21_4, iter_21_5 in ipairs(iter_21_3) do
					if iter_21_5 == arg_21_1 then
						var_21_3 = iter_21_2
						var_21_4 = iter_21_4
					end
				end
			end

			local var_21_5 = iter_21_1:getConfig("config_client").story or {}

			if var_21_5[var_21_3] then
				local var_21_6 = var_21_5[var_21_3][var_21_4]

				if var_21_6 and not pg.NewStoryMgr.GetInstance():IsPlayed(var_21_6) then
					var_21_1 = var_21_6
				end
			end
		end
	end

	if var_21_1 then
		pg.NewStoryMgr.GetInstance():Play(var_21_1, arg_21_2)
	else
		arg_21_2()
	end
end

return var_0_0
