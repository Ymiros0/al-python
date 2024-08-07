﻿local var_0_0 = class("QuickTaskCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = arg_1_1:getType()
	local var_1_2
	local var_1_3 = var_1_0
	local var_1_4 = getProxy(TaskProxy)
	local var_1_5 = var_1_4:getTaskById(var_1_3)

	if not var_1_5 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("task_is_not_existence", var_1_3))

		if var_1_1 then
			var_1_1(false)
		end

		return
	end

	if var_1_5:getConfig("quick_finish") > getProxy(BagProxy):getItemCountById(Item.QUICK_TASK_PASS_TICKET_ID) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

		if var_1_1 then
			var_1_1(false)
		end

		return
	end

	if var_1_4:isSubmitting(var_1_3) then
		return
	else
		var_1_4:addSubmittingTask(var_1_3)
	end

	local var_1_6 = {}

	if var_1_5:IsOverflowShipExpItem() then
		table.insert(var_1_6, function(arg_2_0)
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("player_expResource_mail_fullBag"),
				onYes = arg_2_0,
				onNo = function()
					var_1_4:removeSubmittingTask(var_1_3)

					if var_1_1 then
						var_1_1(false)
					end
				end
			})
		end)
	end

	seriesAsync(var_1_6, function()
		pg.ConnectionMgr.GetInstance():Send(20013, {
			id = var_1_5.id,
			item_cost = var_1_5:getConfig("quick_finish")
		}, 20014, function(arg_5_0)
			var_1_4:removeSubmittingTask(var_1_3)

			if arg_5_0.result == 0 then
				local var_5_0 = Item.QUICK_TASK_PASS_TICKET_ID
				local var_5_1 = var_1_5:getConfig("quick_finish")

				getProxy(BagProxy):removeItemById(tonumber(var_5_0), tonumber(var_5_1))
				var_0_0.AddGuildLivness(var_1_5)

				local var_5_2 = PlayerConst.addTranDrop(arg_5_0.award_list, {
					taskId = var_1_5.id
				})

				if var_1_5:getConfig("type") ~= 8 then
					var_1_4:removeTask(var_1_5)
				else
					var_1_5.submitTime = 1

					var_1_4:updateTask(var_1_5)
				end

				pg.TipsMgr.GetInstance():ShowTips(i18n("battlepass_task_quickfinish3"))
				arg_1_0:sendNotification(GAME.SUBMIT_TASK_DONE, var_5_2, {
					var_1_5.id
				})

				local var_5_3 = getProxy(ActivityProxy)
				local var_5_4 = var_5_3:getActivityByType(ActivityConst.ACTIVITY_TYPE_TASK_LIST_MONITOR)

				if var_5_4 and not var_5_4:isEnd() then
					local var_5_5 = var_5_4:getConfig("config_data")[1] or {}

					if table.contains(var_5_5, var_1_5.id) then
						var_5_3:monitorTaskList(var_5_4)
					end
				end

				if var_1_1 then
					var_1_1(true)
				end
			else
				pg.TipsMgr.GetInstance():ShowTips(errorTip("task_submitTask", arg_5_0.result))

				if var_1_1 then
					var_1_1(false)
				end
			end
		end)
	end)
end

function var_0_0.AddGuildLivness(arg_6_0)
	if arg_6_0:IsGuildAddLivnessType() then
		local var_6_0 = getProxy(GuildProxy)
		local var_6_1 = var_6_0:getData()
		local var_6_2 = 0
		local var_6_3 = false

		if var_6_1 and arg_6_0:isGuildTask() then
			var_6_1:setWeeklyTaskFlag(1)

			local var_6_4 = var_6_1:getWeeklyTask()

			if var_6_4 then
				var_6_2 = var_6_4:GetLivenessAddition()
			end

			var_6_3 = true
		elseif arg_6_0:IsRoutineType() then
			var_6_2 = pg.guildset.new_daily_task_guild_active.key_value
		elseif arg_6_0:IsWeeklyType() then
			var_6_2 = pg.guildset.new_weekly_task_guild_active.key_value
		end

		if var_6_1 and var_6_2 and var_6_2 > 0 then
			var_6_1:getMemberById(getProxy(PlayerProxy):getRawData().id):AddLiveness(var_6_2)

			var_6_3 = true
		end

		if var_6_3 then
			var_6_0:updateGuild(var_6_1)
		end
	end
end

return var_0_0
