local var_0_0 = class("LaunchBallTaskMgr")

var_0_0.type_split = 1
var_0_0.type_series_split = 2
var_0_0.type_close_split = 3
var_0_0.type_over_split = 4
var_0_0.type_many_split = 5
var_0_0.type_pass_skill = 200
var_0_0.type_pass_skill_split = 201
var_0_0.type_trigger_skill = 300
var_0_0.type_trigger_skill_split = 301
var_0_0.type_trigger_skill_split_all = 302
var_0_0.type_trigger_skill_time = 303
var_0_0.type_player_target_round = 400
var_0_0.type_player_round = 401

def var_0_0.CheckTaskUpdate(arg_1_0):
	local var_1_0 = arg_1_0.player
	local var_1_1 = LaunchBallActivityMgr.GetPlayerZhuanshuIndex(var_1_0)
	local var_1_2

	if var_1_1 and not LaunchBallActivityMgr.CheckZhuanShuAble(ActivityConst.MINIGAME_ZUMA, var_1_1):
		return

	local var_1_3 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_ZUMA_TASK).getConfig("config_client")
	local var_1_4 = {}

	for iter_1_0 = 1, #var_1_3:
		if var_1_3[iter_1_0].player == var_1_0:
			var_1_4 = var_1_3[iter_1_0].task

	local var_1_5 = {}

	for iter_1_1 = 1, #var_1_4:
		local var_1_6 = var_1_4[iter_1_1][1]
		local var_1_7 = var_1_4[iter_1_1][2]
		local var_1_8 = var_1_4[iter_1_1][3]
		local var_1_9 = var_1_4[iter_1_1][4]
		local var_1_10 = getProxy(TaskProxy).getTaskById(var_1_7)

		if var_1_10 and var_1_10.getTaskStatus() == 0:
			local var_1_11 = 0
			local var_1_12 = var_1_10.getTargetNumber()
			local var_1_13 = var_1_10.getProgress()

			if var_1_6 == var_0_0.type_split and arg_1_0.split_count != 0:
				var_1_11 = var_1_12 < arg_1_0.split_count + var_1_13 and var_1_12 or arg_1_0.split_count + var_1_13
			elif var_1_6 == var_0_0.type_player_target_round:
				if var_1_9 == arg_1_0.round:
					var_1_11 = var_1_13 + 1
			elif var_1_6 == var_0_0.type_player_round:
				var_1_11 = var_1_13 + 1
			elif var_1_6 == var_0_0.type_trigger_skill and arg_1_0.use_skill != 0:
				var_1_11 = var_1_13 + arg_1_0.use_skill
			elif var_1_6 == var_0_0.type_series_split and arg_1_0.series_count != 0:
				var_1_11 = var_1_13 + arg_1_0.series_count
			elif var_1_6 == var_0_0.type_close_split and arg_1_0.mix_count != 0:
				var_1_11 = var_1_13 + arg_1_0.mix_count
			elif var_1_6 == var_0_0.type_over_split and arg_1_0.over_count != 0:
				var_1_11 = var_1_13 + arg_1_0.over_count
			elif var_1_6 == var_0_0.type_many_split and arg_1_0.many_count != 0:
				var_1_11 = var_1_13 + arg_1_0.many_count
			elif var_1_6 == var_0_0.type_pass_skill and arg_1_0.use_pass_skill != 0:
				var_1_11 = var_1_13 + arg_1_0.use_pass_skill
			elif var_1_6 == var_0_0.type_trigger_skill_split and arg_1_0.skill_count != 0:
				if var_1_8 <= arg_1_0.skill_count:
					var_1_11 = var_1_12
			elif var_1_6 == var_0_0.type_trigger_skill_split_all and arg_1_0.skill_count != 0:
				var_1_11 = var_1_13 + arg_1_0.skill_count
			elif var_1_6 == var_0_0.type_pass_skill_split and arg_1_0.pass_skill_count != 0:
				var_1_11 = var_1_13 + arg_1_0.pass_skill_count
			elif var_1_6 == var_0_0.type_trigger_skill_time and arg_1_0.double_skill_time and var_1_8 >= arg_1_0.double_skill_time:
				var_1_11 = var_1_12

			if var_1_11 and var_1_11 != 0:
				if var_1_12 < var_1_11:
					var_1_11 = var_1_12

				table.insert(var_1_5, {
					id = var_1_7,
					progress = var_1_11
				})

	for iter_1_2 = 1, #var_1_5:
		pg.m02.sendNotification(GAME.UPDATE_TASK_PROGRESS, {
			taskId = var_1_5[iter_1_2].id,
			progress = var_1_5[iter_1_2].progress
		})

def var_0_0.GetRedTip():
	local var_2_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.MINIGAME_ZUMA_TASK)

	if var_2_0 and not var_2_0.isEnd():
		local var_2_1 = var_2_0.getConfig("config_data")
		local var_2_2 = getProxy(TaskProxy)

		return underscore.any(var_2_1, function(arg_3_0)
			assert(var_2_2.getTaskVO(arg_3_0), "without this task." .. arg_3_0)

			return var_2_2.getTaskVO(arg_3_0).getTaskStatus() == 1)

	return False

return var_0_0
