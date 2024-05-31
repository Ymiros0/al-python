local var_0_0 = class("AvatarFrameAwardCommand", pm.SimpleCommand)
local var_0_1

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody() or {}
	local var_1_1 = var_1_0.callback
	local var_1_2 = pg.activity_template[var_1_0.act_id].type

	pg.ConnectionMgr.GetInstance().Send(20205, {
		act_id = var_1_0.act_id,
		task_ids = var_1_0.task_ids
	}, 20206, function(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_2 == ActivityConst.ACTIVITY_TYPE_PT_OTHER:
				local var_2_0 = pg.activity_template[var_1_0.act_id].config_id
				local var_2_1 = pg.activity_event_avatarframe[var_2_0]
				local var_2_2 = Clone(var_2_1.award_display)[1]
				local var_2_3 = 0

				for iter_2_0, iter_2_1 in ipairs(var_1_0.task_ids):
					var_2_3 = var_2_3 + arg_1_0.getAwardNum(var_2_1, iter_2_1)

				local var_2_4 = getProxy(ActivityProxy).RawGetActivityById(var_1_0.act_id)

				if var_2_4:
					var_2_4.data1 = var_2_4.data1 + var_2_3

				var_2_2[3] = var_2_3

				local var_2_5 = Drop.Create(var_2_2)

				arg_1_0.sendNotification(GAME.SUBMIT_AVATAR_TASK_DONE, {
					awards = {
						var_2_5
					},
					callback = var_1_1
				})
			else
				local var_2_6 = PlayerConst.addTranDrop(arg_2_0.award_list)
				local var_2_7 = {}

				for iter_2_2 = 1, #var_1_0.task_ids:
					local var_2_8 = var_1_0.task_ids[iter_2_2]
					local var_2_9 = pg.task_data_template[var_2_8]
					local var_2_10 = var_2_9.award_display
					local var_2_11 = var_2_9.type
					local var_2_12 = var_2_9.sub_type
					local var_2_13 = tonumber(var_2_9.target_id)
					local var_2_14 = tonumber(var_2_9.target_id_2)
					local var_2_15 = var_2_9.target_num

					if var_2_11 == 6:
						local var_2_16 = getProxy(ActivityProxy).getActivityById(var_1_0.act_id)

						assert(var_2_16)

						local var_2_17 = var_2_16.GetFinishedTaskIds()

						if not table.contains(var_2_17, var_2_8):
							table.insert(var_2_17, var_2_8)
							getProxy(ActivityProxy).updateActivity(var_2_16)

					if var_2_11 == 6 and var_2_12 == 1006 and pg.activity_drop_type[var_2_13]:
						local var_2_18 = pg.activity_drop_type[var_2_13].activity_id
						local var_2_19 = getProxy(ActivityProxy).getActivityById(var_2_18)

						if var_2_19:
							var_2_19.subVitemNumber(var_2_14, var_2_15)
							getProxy(ActivityProxy).updateActivity(var_2_19)

				for iter_2_3, iter_2_4 in ipairs(arg_2_0.award_list):
					local var_2_20 = Drop.New({
						type = iter_2_4.type,
						id = iter_2_4.id,
						count = iter_2_4.number
					})

					table.insert(var_2_7, var_2_20)

				arg_1_0.sendNotification(GAME.SUBMIT_AVATAR_TASK_DONE, {
					awards = var_2_7,
					callback = var_1_1
				})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

def var_0_0.getAwardNum(arg_3_0, arg_3_1, arg_3_2):
	for iter_3_0 = 1, #AvatarFrameTask.fillter_task_type:
		local var_3_0 = AvatarFrameTask.fillter_task_type[iter_3_0]
		local var_3_1 = arg_3_1[var_3_0]

		for iter_3_1, iter_3_2 in ipairs(var_3_1):
			if arg_3_2 == iter_3_2[1]:
				if var_3_0 == AvatarFrameTask.type_task_level:
					return iter_3_2[6]
				elif var_3_0 == AvatarFrameTask.type_task_ship:
					return iter_3_2[4]

	print("找不到taskId." .. arg_3_2)

	return 0

return var_0_0
