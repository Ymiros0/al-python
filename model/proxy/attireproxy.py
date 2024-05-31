local var_0_0 = class("AttireProxy", import(".NetProxy"))

var_0_0.ATTIREFRAME_UPDATED = "AttireProxy.ATTIREFRAME_UPDATED"
var_0_0.ATTIREFRAME_ADDED = "AttireProxy.ATTIREFRAME_ADDED"
var_0_0.ATTIREFRAME_EXPIRED = "AttireProxy.ATTIREFRAME_EXPIRED"

local var_0_1 = pg.item_data_frame
local var_0_2 = pg.item_data_chat
local var_0_3 = False

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}
	arg_1_0.timers = {}
	arg_1_0.expiredChaces = {}
	arg_1_0.data.iconFrames = {}
	arg_1_0.data.chatFrames = {}

	for iter_1_0, iter_1_1 in ipairs(var_0_1.all):
		if iter_1_1 == 0:
			arg_1_0.data.iconFrames[iter_1_1] = IconFrame.New({_time = 0,
				id = iter_1_1
			})
		else
			arg_1_0.data.iconFrames[iter_1_1] = IconFrame.New({
				id = iter_1_1
			})

	for iter_1_2, iter_1_3 in ipairs(var_0_2.all):
		if iter_1_3 == 0:
			arg_1_0.data.chatFrames[iter_1_3] = ChatFrame.New({_time = 0,
				id = iter_1_3
			})
		else
			arg_1_0.data.chatFrames[iter_1_3] = ChatFrame.New({
				id = iter_1_3
			})

	arg_1_0.on(11003, function(arg_2_0)
		for iter_2_0, iter_2_1 in ipairs(arg_2_0.icon_frame_list):
			local var_2_0 = arg_1_0.data.iconFrames[iter_2_1.id]

			var_2_0.updateData(iter_2_1)
			arg_1_0.updateAttireFrame(var_2_0)
			arg_1_0.addExpiredTimer(var_2_0)

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.chat_frame_list or {}):
			local var_2_1 = arg_1_0.data.chatFrames[iter_2_3.id]

			var_2_1.updateData(iter_2_3)
			arg_1_0.updateAttireFrame(var_2_1)
			arg_1_0.addExpiredTimer(var_2_1))

	if var_0_3:
		arg_1_0.timer = Timer.New(function()
			local var_3_0 = {}
			local var_3_1 = {
				101,
				102,
				201,
				301
			}

			for iter_3_0 = 1, 5:
				local var_3_2 = math.random(1, 4)
				local var_3_3 = Drop.New({
					count = 1,
					type = iter_3_0 % 2 == 0 and DROP_TYPE_ICON_FRAME or DROP_TYPE_CHAT_FRAME,
					id = var_3_1[var_3_2]
				})

				arg_1_0.sendNotification(GAME.ADD_ITEM, var_3_3)
				table.insert(var_3_0, var_3_3)

			table.insert(var_3_0, Drop.New({
				count = 1000,
				type = DROP_TYPE_RESOURCE,
				id = PlayerConst.ResGold
			}))
			arg_1_0.sendNotification(GAME.ACT_NEW_PT_DONE, {
				awards = var_3_0
			}), 10, 1)

		arg_1_0.timer.Start()

def var_0_0.getDataAndTrophys(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.getData()

	if arg_4_1:
		arg_4_0.clearNew()

	var_4_0.trophys = getProxy(CollectionProxy).getTrophys()

	return var_4_0

def var_0_0.clearNew(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0.data.iconFrames):
		iter_5_1.clearNew()

	for iter_5_2, iter_5_3 in pairs(arg_5_0.data.chatFrames):
		iter_5_3.clearNew()

def var_0_0.getExpiredChaces(arg_6_0):
	local var_6_0 = {}

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.expiredChaces):
		table.insert(var_6_0, iter_6_1)

	arg_6_0.expiredChaces = {}

	return var_6_0

def var_0_0.getAttireFrame(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0

	if arg_7_1 == AttireConst.TYPE_ICON_FRAME:
		var_7_0 = arg_7_0.data.iconFrames[arg_7_2]
	elif arg_7_1 == AttireConst.TYPE_CHAT_FRAME:
		var_7_0 = arg_7_0.data.chatFrames[arg_7_2]

	return var_7_0

def var_0_0.addAttireFrame(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getType()
	local var_8_1 = arg_8_0.getAttireFrame(var_8_0, arg_8_1.id)

	if arg_8_1.expiredType() and var_8_1 and not var_8_1.isExpired():
		local var_8_2 = var_8_1.getExpiredTime() + arg_8_1.getConfig("time_second")

		arg_8_1.updateEndTime(var_8_2)

	if var_8_0 == AttireConst.TYPE_ICON_FRAME:
		arg_8_0.data.iconFrames[arg_8_1.id] = arg_8_1
	elif var_8_0 == AttireConst.TYPE_CHAT_FRAME:
		arg_8_0.data.chatFrames[arg_8_1.id] = arg_8_1

	arg_8_0.addExpiredTimer(arg_8_1)
	arg_8_0.sendNotification(var_0_0.ATTIREFRAME_ADDED, arg_8_1.clone())

def var_0_0.updateAttireFrame(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getType()

	if var_9_0 == AttireConst.TYPE_ICON_FRAME:
		assert(arg_9_0.data.iconFrames[arg_9_1.id])

		arg_9_0.data.iconFrames[arg_9_1.id] = arg_9_1
	elif var_9_0 == AttireConst.TYPE_CHAT_FRAME:
		assert(arg_9_0.data.chatFrames[arg_9_1.id])

		arg_9_0.data.chatFrames[arg_9_1.id] = arg_9_1

	arg_9_0.sendNotification(var_0_0.ATTIREFRAME_UPDATED, arg_9_1.clone())

def var_0_0.addExpiredTimer(arg_10_0, arg_10_1):
	arg_10_0.removeExpiredTimer(arg_10_1)

	if not arg_10_1.expiredType():
		return

	local function var_10_0()
		local var_11_0 = getProxy(PlayerProxy)
		local var_11_1 = var_11_0.getData()
		local var_11_2 = arg_10_1.getType()

		if var_11_1.getAttireByType(var_11_2) == arg_10_1.id:
			var_11_1.updateAttireFrame(var_11_2, 0)
			var_11_0.updatePlayer(var_11_1)

		table.insert(arg_10_0.expiredChaces, arg_10_1)
		arg_10_0.sendNotification(var_0_0.ATTIREFRAME_EXPIRED, arg_10_1.clone())

	local var_10_1 = arg_10_1.getExpiredTime() - pg.TimeMgr.GetInstance().GetServerTime()

	if var_10_1 > 0:
		local var_10_2 = arg_10_1.getTimerKey()

		arg_10_0.timers[var_10_2] = Timer.New(function()
			var_10_0()
			arg_10_0.removeExpiredTimer(arg_10_1), var_10_1, 1)

		arg_10_0.timers[var_10_2].Start()
	else
		var_10_0()

def var_0_0.removeExpiredTimer(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1.getTimerKey()

	if arg_13_0.timers[var_13_0]:
		arg_13_0.timers[var_13_0].Stop()

		arg_13_0.timers[var_13_0] = None

def var_0_0.remove(arg_14_0):
	for iter_14_0, iter_14_1 in pairs(arg_14_0.timers):
		iter_14_1.Stop()

	arg_14_0.timers = {}

def var_0_0.needTip(arg_15_0):
	local var_15_0 = {}
	local var_15_1 = arg_15_0.getDataAndTrophys()
	local var_15_2 = {
		var_15_1.iconFrames,
		var_15_1.chatFrames,
		var_15_1.trophys
	}

	local function var_15_3(arg_16_0)
		local var_16_0 = False

		for iter_16_0, iter_16_1 in pairs(arg_16_0):
			if iter_16_1.isNew():
				var_16_0 = True

				break

		return var_16_0

	for iter_15_0, iter_15_1 in ipairs(var_15_2):
		if iter_15_0 == 1 or iter_15_0 == 2:
			table.insert(var_15_0, var_15_3(iter_15_1))
		else
			table.insert(var_15_0, False)

	return var_15_0

def var_0_0.IsShowRedDot(arg_17_0):
	return _.any(arg_17_0.needTip(), function(arg_18_0)
		return arg_18_0 == True)

return var_0_0
