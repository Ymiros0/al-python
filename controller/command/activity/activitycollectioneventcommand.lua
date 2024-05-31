local var_0_0 = class("ActivityCollectionEventCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.arg1
	local var_1_2 = var_1_0.onConfirm
	local var_1_3 = var_1_0.callBack
	local var_1_4 = getProxy(EventProxy)
	local var_1_5 = getProxy(ActivityProxy)
	local var_1_6 = var_1_5:getActivityByType(ActivityConst.ACTIVITY_TYPE_COLLECTION_EVENT)

	if not var_1_6 or var_1_6:isEnd() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(11202, {
		activity_id = var_1_6.id,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = var_1_0.arg_list
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0 then
			if var_1_0.cmd == ActivityConst.COLLETION_EVENT_OP_JOIN then
				EventStartCommand.OnStart(var_1_1)

				if var_1_3 then
					var_1_3()
				end

				if var_1_2 then
					var_1_2()
				end
			elseif var_1_0.cmd == ActivityConst.COLLETION_EVENT_OP_SUBMIT then
				table.insert(var_1_6.data1_list, var_1_1)
				var_1_5:updateActivity(var_1_6)

				local var_2_0 = {}
				local var_2_1 = var_1_6:getConfig("config_data")
				local var_2_2 = table.indexof(var_2_1, var_1_1)

				assert(var_2_2)

				local var_2_3 = var_1_6:getDayIndex()

				if var_2_2 < var_2_3 and var_2_3 <= #var_2_1 then
					local var_2_4 = var_2_1[var_2_3]

					table.insert(var_2_0, {
						finish_time = 0,
						over_time = 0,
						id = var_2_4,
						ship_id_list = {},
						activity_id = var_1_6.id
					})
				end

				EventFinishCommand.OnFinish(var_1_1, {
					exp = arg_2_0.number[1],
					drop_list = arg_2_0.award_list,
					new_collection = var_2_0,
					is_cri = arg_2_0.number[2]
				}, var_1_2)

				if var_1_3 then
					var_1_3()
				end
			elseif var_1_0.cmd == ActivityConst.COLLETION_EVENT_OP_GIVE_UP then
				EventGiveUpCommand.OnCancel(var_1_1)

				local var_2_5 = {}
				local var_2_6 = var_1_6:getConfig("config_data")
				local var_2_7 = table.indexof(var_2_6, var_1_1)

				assert(var_2_7)

				local var_2_8 = var_1_6:getDayIndex()

				if var_2_7 < var_2_8 and var_2_8 <= #var_2_6 then
					local var_2_9 = var_2_6[var_2_8]

					table.insert(var_2_5, {
						finish_time = 0,
						over_time = 0,
						id = var_2_9,
						ship_id_list = {},
						activity_id = var_1_6.id
					})
				end

				if #var_2_5 > 0 then
					local var_2_10, var_2_11 = var_1_4:findInfoById(var_1_1)

					table.remove(var_1_4.eventList, var_2_11)

					for iter_2_0, iter_2_1 in ipairs(var_2_5) do
						table.insert(var_1_4.eventList, EventInfo.New(iter_2_1))
					end
				end

				if var_1_3 then
					var_1_3()
				end

				if var_1_2 then
					var_1_2()
				end

				pg.m02:sendNotification(GAME.EVENT_LIST_UPDATE)
			end
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
