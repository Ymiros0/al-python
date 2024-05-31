local var_0_0 = class("AvatarFrameProxy", import(".NetProxy"))

var_0_0.FRAME_TASK_UPDATED = "frame task updated"
var_0_0.FRAME_TASK_TIME_OUT = "frame task time out"

def var_0_0.register(arg_1_0):
	arg_1_0.avatarFrames = {}
	arg_1_0.actTasks = {}

	arg_1_0.on(20201, function(arg_2_0)
		arg_1_0.avatarFrames = {}

		local function var_2_0(arg_3_0, arg_3_1)
			local var_3_0 = {}

			for iter_3_0, iter_3_1 in ipairs(arg_3_1):
				local var_3_1 = arg_1_0.createAvatarFrameTask(arg_3_0, iter_3_1)

				table.insert(var_3_0, var_3_1)

			table.insert(arg_1_0.avatarFrames, {
				actId = arg_3_0,
				tasks = var_3_0
			})

		local var_2_1 = getProxy(ActivityTaskProxy)

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.info):
			local var_2_2 = iter_2_1.act_id
			local var_2_3 = iter_2_1.tasks
			local var_2_4 = pg.activity_template[var_2_2].type

			if var_2_4 == ActivityConst.ACTIVITY_TYPE_PT_OTHER:
				var_2_0(var_2_2, var_2_3)
			elif var_2_4 == ActivityConst.ACTIVITY_TYPE_TASK_RYZA or var_2_4 == ActivityConst.ACTIVITY_TYPE_HOTSPRING_2:
				var_2_1.initActList(var_2_2, var_2_3))
	arg_1_0.on(20202, function(arg_4_0)
		local function var_4_0(arg_5_0, arg_5_1)
			for iter_5_0, iter_5_1 in ipairs(arg_5_1):
				arg_1_0.updateAvatarTask(arg_5_0, iter_5_1)

		local var_4_1 = getProxy(ActivityTaskProxy)

		for iter_4_0, iter_4_1 in ipairs(arg_4_0.info):
			local var_4_2 = iter_4_1.act_id
			local var_4_3 = iter_4_1.tasks
			local var_4_4 = pg.activity_template[var_4_2].type

			if var_4_4 == ActivityConst.ACTIVITY_TYPE_PT_OTHER:
				var_4_0(var_4_2, var_4_3)
			elif var_4_4 == ActivityConst.ACTIVITY_TYPE_TASK_RYZA or var_4_4 == ActivityConst.ACTIVITY_TYPE_HOTSPRING_2:
				var_4_1.updateActList(var_4_2, var_4_3)

		arg_1_0.facade.sendNotification(var_0_0.FRAME_TASK_UPDATED))
	arg_1_0.on(20203, function(arg_6_0)
		local function var_6_0(arg_7_0, arg_7_1)
			for iter_7_0, iter_7_1 in ipairs(arg_7_1):
				local var_7_0 = arg_1_0.createAvatarFrameTask(arg_7_0, iter_7_1)

				arg_1_0.addAvatarTask(arg_7_0, var_7_0)

		local var_6_1 = getProxy(ActivityTaskProxy)

		for iter_6_0, iter_6_1 in ipairs(arg_6_0.info):
			local var_6_2 = iter_6_1.act_id
			local var_6_3 = iter_6_1.tasks
			local var_6_4 = pg.activity_template[var_6_2].type

			if var_6_4 == ActivityConst.ACTIVITY_TYPE_PT_OTHER:
				var_6_0(var_6_2, var_6_3)
			elif var_6_4 == ActivityConst.ACTIVITY_TYPE_TASK_RYZA or var_6_4 == ActivityConst.ACTIVITY_TYPE_HOTSPRING_2:
				var_6_1.addActList(var_6_2, var_6_3)

		arg_1_0.facade.sendNotification(var_0_0.FRAME_TASK_UPDATED))
	arg_1_0.on(20204, function(arg_8_0)
		local function var_8_0(arg_9_0, arg_9_1)
			for iter_9_0, iter_9_1 in ipairs(arg_9_1):
				arg_1_0.removeAvatarTask(arg_9_0, iter_9_1.id)

		local var_8_1 = getProxy(ActivityTaskProxy)

		for iter_8_0, iter_8_1 in ipairs(arg_8_0.info):
			local var_8_2 = iter_8_1.act_id
			local var_8_3 = iter_8_1.tasks
			local var_8_4 = pg.activity_template[var_8_2].type

			if var_8_4 == ActivityConst.ACTIVITY_TYPE_PT_OTHER:
				var_8_0(var_8_2, var_8_3)
			elif var_8_4 == ActivityConst.ACTIVITY_TYPE_TASK_RYZA or var_8_4 == ActivityConst.ACTIVITY_TYPE_HOTSPRING_2:
				var_8_1.removeActList(var_8_2, var_8_3)

		arg_1_0.facade.sendNotification(var_0_0.FRAME_TASK_UPDATED))

def var_0_0.createAvatarFrameTask(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = pg.activity_template[arg_10_1].config_id

	return (AvatarFrameTask.New(arg_10_1, var_10_0, arg_10_2))

def var_0_0.updateAvatarTask(arg_11_0, arg_11_1, arg_11_2):
	for iter_11_0 = 1, #arg_11_0.avatarFrames:
		if arg_11_0.avatarFrames[iter_11_0].actId == arg_11_1:
			local var_11_0 = arg_11_0.avatarFrames[iter_11_0]

			for iter_11_1 = #var_11_0.tasks, 1, -1:
				if var_11_0.tasks[iter_11_1].id == arg_11_2.id:
					var_11_0.tasks[iter_11_1].updateProgress(arg_11_2.progress)

def var_0_0.addAvatarTask(arg_12_0, arg_12_1, arg_12_2):
	for iter_12_0 = 1, #arg_12_0.avatarFrames:
		if arg_12_0.avatarFrames[iter_12_0].actId == arg_12_1:
			local var_12_0 = arg_12_0.avatarFrames[iter_12_0]

			for iter_12_1 = #var_12_0.tasks, 1, -1:
				if var_12_0.tasks[iter_12_1].id == arg_12_2.id:
					table.remove(var_12_0.tasks, iter_12_1)

			table.insert(var_12_0.tasks, arg_12_2)

def var_0_0.removeAvatarTask(arg_13_0, arg_13_1, arg_13_2):
	for iter_13_0 = 1, #arg_13_0.avatarFrames:
		if arg_13_0.avatarFrames[iter_13_0].actId == arg_13_1:
			local var_13_0 = arg_13_0.avatarFrames[iter_13_0]

			for iter_13_1 = #var_13_0.tasks, 1, -1:
				if var_13_0.tasks[iter_13_1].id == arg_13_2:
					table.remove(var_13_0.tasks, iter_13_1)

def var_0_0.getAvatarFrameById(arg_14_0, arg_14_1):
	for iter_14_0 = 1, #arg_14_0.avatarFrames:
		if arg_14_0.avatarFrames[iter_14_0].actId == arg_14_1:
			return Clone(arg_14_0.avatarFrames[iter_14_0])

	return None

def var_0_0.getAllAvatarFrame(arg_15_0):
	return Clone(arg_15_0.avatarFrames)

def var_0_0.getCanReceiveCount(arg_16_0):
	local var_16_0 = 0

	for iter_16_0 = 1, #arg_16_0.avatarFrames:
		local var_16_1 = arg_16_0.avatarFrames[iter_16_0]

		for iter_16_1, iter_16_2 in ipairs(var_16_1.tasks):
			if iter_16_2.getTaskStatus() == 1:
				var_16_0 = var_16_0 + 1

	return var_16_0

def var_0_0.clearTimeOut(arg_17_0):
	if not arg_17_0.avatarFrames or #arg_17_0.avatarFrames == 0:
		return

	local var_17_0 = False

	for iter_17_0 = #arg_17_0.avatarFrames, 1, -1:
		local var_17_1 = arg_17_0.avatarFrames[iter_17_0].actId
		local var_17_2 = getProxy(ActivityProxy).getActivityById(var_17_1)

		if not var_17_2 or var_17_2.isEnd():
			table.remove(arg_17_0.avatarFrames, iter_17_0)

			var_17_0 = True

	if var_17_0:
		arg_17_0.facade.sendNotification(var_0_0.FRAME_TASK_UPDATED)
		arg_17_0.facade.sendNotification(var_0_0.FRAME_TASK_TIME_OUT)

return var_0_0
