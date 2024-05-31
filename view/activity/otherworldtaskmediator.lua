﻿local var_0_0 = class("OtherWorldTaskMediator", import("..base.ContextMediator"))

var_0_0.SUBMIT_TASK_ALL = "activity submit task all"
var_0_0.SUBMIT_TASK = "activity submit task "
var_0_0.TASK_GO = "activity task go "
var_0_0.SHOW_DETAIL = "activity task show detail"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.SUBMIT_TASK_ALL, function(arg_2_0, arg_2_1)
		arg_1_0:checkActStory(arg_2_1.activityId, arg_2_1.ids, function()
			arg_1_0:sendNotification(GAME.AVATAR_FRAME_AWARD, {
				act_id = arg_2_1.activityId,
				task_ids = arg_2_1.ids
			})
		end)
	end)
	arg_1_0:bind(var_0_0.SUBMIT_TASK, function(arg_4_0, arg_4_1)
		arg_1_0:checkActStory(arg_4_1.activityId, {
			arg_4_1.id
		}, function()
			arg_1_0:sendNotification(GAME.AVATAR_FRAME_AWARD, {
				act_id = arg_4_1.activityId,
				task_ids = {
					arg_4_1.id
				}
			})
		end)
	end)
	arg_1_0:bind(var_0_0.TASK_GO, function(arg_6_0, arg_6_1)
		arg_1_0.viewComponent:closeView()

		local var_6_0 = arg_6_1.taskVO:getConfig("scene")

		if var_6_0[1] == SCENE.OTHERWORLD_MAP then
			pg.SceneAnimMgr.GetInstance():OtherWorldCoverGoScene(SCENE.OTHERWORLD_MAP, {
				mode = var_6_0[2].mode
			})
		else
			arg_1_0:sendNotification(GAME.TASK_GO, {
				taskVO = arg_6_1.taskVO
			})
		end
	end)
	arg_1_0:bind(var_0_0.SHOW_DETAIL, function(arg_7_0, arg_7_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = AtelierMaterialDetailMediator,
			viewComponent = AtelierMaterialDetailLayer,
			data = {
				material = arg_7_1
			}
		}))
	end)
end

function var_0_0.checkActStory(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	local var_8_0 = pg.activity_template[arg_8_1].config_client.task_story

	if not var_8_0 then
		arg_8_3()

		return
	end

	local var_8_1 = {}

	for iter_8_0, iter_8_1 in ipairs(var_8_0) do
		local var_8_2 = iter_8_1[1]
		local var_8_3 = iter_8_1[2]

		if table.contains(arg_8_2, var_8_2) then
			table.insert(var_8_1, var_8_3)
		end
	end

	local var_8_4 = {}

	for iter_8_2, iter_8_3 in ipairs(var_8_1) do
		table.insert(var_8_4, function(arg_9_0)
			pg.NewStoryMgr.GetInstance():Play(iter_8_3, arg_9_0, true)
		end)
	end

	seriesAsync(var_8_4, function()
		arg_8_3()
	end)
end

function var_0_0.onUIAvalible(arg_11_0)
	return
end

function var_0_0.listNotificationInterests(arg_12_0)
	return {
		GAME.SUBMIT_AVATAR_TASK_DONE,
		GAME.ZERO_HOUR_OP_DONE
	}
end

function var_0_0.handleNotification(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_1:getName()
	local var_13_1 = arg_13_1:getBody()

	if var_13_0 == GAME.SUBMIT_AVATAR_TASK_DONE then
		if #var_13_1.awards > 0 then
			arg_13_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_13_1.awards)
		end

		if var_13_1.callback then
			-- block empty
		end

		arg_13_0.viewComponent:updateTask(true)
	elseif var_13_0 == GAME.ZERO_HOUR_OP_DONE then
		arg_13_0.viewComponent:updateTask(true)
	end
end

return var_0_0
