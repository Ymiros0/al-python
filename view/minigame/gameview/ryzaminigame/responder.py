local var_0_0 = class("Responder")
local var_0_1 = {
	def __index:(arg_1_0, arg_1_1)
		arg_1_0[arg_1_1] = {}

		return arg_1_0[arg_1_1]
}

def var_0_0.Ctor(arg_2_0, arg_2_1):
	arg_2_0.binder = arg_2_1

def var_0_0.reset(arg_3_0):
	if arg_3_0.map:
		for iter_3_0, iter_3_1 in pairs(arg_3_0.map):
			underscore.each(iter_3_1, function(arg_4_0)
				Destroy(arg_4_0._tf))

	arg_3_0.timeRiver = {}
	arg_3_0.fireList = {}
	arg_3_0.eventRange = {}
	arg_3_0.map = setmetatable({}, var_0_1)
	arg_3_0.findingResult = {}
	arg_3_0.reactorRyza = None
	arg_3_0.enemyCount = 0

def var_0_0.AddListener(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	arg_5_0.eventRange[arg_5_1] = arg_5_0.eventRange[arg_5_1] or setmetatable({}, var_0_1)

	local var_5_0 = arg_5_0.eventRange[arg_5_1]

	for iter_5_0, iter_5_1 in ipairs(arg_5_3):
		table.insert(var_5_0[tostring(arg_5_2.pos + iter_5_1)], arg_5_2)

def var_0_0.RemoveListener(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	if not arg_6_3:
		return

	local var_6_0 = arg_6_0.eventRange[arg_6_1]

	for iter_6_0, iter_6_1 in ipairs(arg_6_3):
		table.removebyvalue(var_6_0[tostring(arg_6_2.pos + iter_6_1)], arg_6_2)

local var_0_2 = {
	{
		0,
		1
	},
	{
		1,
		0
	},
	{
		0,
		-1
	},
	{
		-1,
		0
	}
}

def var_0_0.InRange(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.binder.config.mapSize

	if arg_7_1.x < 0 or arg_7_1.y < 0 or arg_7_1.x >= var_7_0.x or arg_7_1.y >= var_7_0.y:
		return False
	else
		return True

def var_0_0.GetCrossFire(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = {
		0,
		0,
		0,
		0
	}

	for iter_8_0, iter_8_1 in ipairs(var_0_2):
		for iter_8_2 = 1, arg_8_2:
			local var_8_1 = arg_8_1 + NewPos(unpack(iter_8_1)) * iter_8_2
			local var_8_2 = arg_8_0.GetFirePassability(var_8_1)

			if var_8_2 < 2:
				var_8_0[iter_8_0] = iter_8_2

			if var_8_2 > 0:
				break

	local var_8_3 = {}

	for iter_8_3, iter_8_4 in ipairs(arg_8_0.timeRiver):
		if isa(iter_8_4, EnemyConductor):
			iter_8_4.CheckBlock(arg_8_1, var_8_0, var_8_3)

	local var_8_4 = {
		{
			0,
			0
		}
	}

	for iter_8_5, iter_8_6 in ipairs(var_0_2):
		for iter_8_7 = 1, var_8_0[iter_8_5]:
			table.insert(var_8_4, {
				iter_8_6[1] * iter_8_7,
				iter_8_6[2] * iter_8_7
			})

	return var_8_0, var_8_4, var_8_3

def var_0_0.getRangeList(arg_9_0, arg_9_1, arg_9_2):
	return underscore.map(arg_9_2, function(arg_10_0)
		return arg_9_1.pos + NewPos(unpack(arg_10_0)))

def var_0_0.EventCall(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4):
	if isa(arg_11_4, Reactor):
		if arg_11_4 == MoveRyza:
			arg_11_0.reactorRyza.React(arg_11_1, arg_11_2)
		else
			arg_11_4.React(arg_11_1, arg_11_2)
	else
		local var_11_0 = arg_11_0.eventRange[arg_11_1]

		if not var_11_0:
			return

		for iter_11_0, iter_11_1 in ipairs(arg_11_0.getRangeList(arg_11_3, arg_11_4)):
			for iter_11_2, iter_11_3 in ipairs(underscore.rest(var_11_0[tostring(iter_11_1)], 1)):
				iter_11_3.React(arg_11_1, arg_11_2)

def var_0_0.CreateCall(arg_12_0, arg_12_1):
	table.insert(arg_12_0.map[tostring(arg_12_1.pos)], arg_12_1)

	if arg_12_1.InTimeRiver():
		table.insert(arg_12_0.timeRiver, arg_12_1)

	if isa(arg_12_1, MoveRyza):
		arg_12_0.reactorRyza = arg_12_1
	elif isa(arg_12_1, MoveEnemy):
		arg_12_0.enemyCount = defaultValue(arg_12_0.enemyCount, 0) + 1
	elif isa(arg_12_1, EffectFire):
		table.insert(arg_12_0.fireList, arg_12_1)

def var_0_0.DestroyCall(arg_13_0, arg_13_1, arg_13_2):
	table.removebyvalue(arg_13_0.map[tostring(arg_13_1.pos)], arg_13_1)

	if arg_13_1.InTimeRiver():
		table.removebyvalue(arg_13_0.timeRiver, arg_13_1)

	arg_13_0.binder.emit(RyzaMiniGameView.EVENT_DESTROY, arg_13_1, arg_13_2)

	if isa(arg_13_1, MoveEnemy):
		arg_13_0.enemyCount = arg_13_0.enemyCount - 1

		if arg_13_0.enemyCount == 0:
			arg_13_0.GameFinish(True)
	elif isa(arg_13_1, EffectFire):
		table.removebyvalue(arg_13_0.fireList, arg_13_1)

def var_0_0.GetCellPassability(arg_14_0, arg_14_1):
	if not arg_14_0.InRange(arg_14_1):
		return False

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.map[tostring(arg_14_1)]):
		if not iter_14_1.CellPassability():
			return False, iter_14_1

	return True

def var_0_0.GetFirePassability(arg_15_0, arg_15_1):
	if not arg_15_0.InRange(arg_15_1):
		return 2

	return underscore.reduce(arg_15_0.map[tostring(arg_15_1)], 0, function(arg_16_0, arg_16_1)
		return math.max(arg_16_0, arg_16_1.FirePassability()))

def var_0_0.GetCellCanBomb(arg_17_0, arg_17_1):
	if not arg_17_0.InRange(arg_17_1):
		return False

	return underscore.all(arg_17_0.map[tostring(arg_17_1)], function(arg_18_0)
		return not isa(arg_18_0, ObjectBomb))

def var_0_0.TimeFlow(arg_19_0, arg_19_1):
	for iter_19_0, iter_19_1 in ipairs(arg_19_0.timeRiver):
		iter_19_1.TimeUpdate(arg_19_1)

def var_0_0.Create(arg_20_0, arg_20_1):
	arg_20_0.binder.emit(RyzaMiniGameView.EVENT_CREATE, arg_20_1)

def var_0_0.GetJoyStick(arg_21_0):
	return NewPos(arg_21_0.binder.uiMgr.hrz, -arg_21_0.binder.uiMgr.vtc)

def var_0_0.RyzaBomb(arg_22_0):
	arg_22_0.reactorRyza.SetBomb()

def var_0_0.GameFinish(arg_23_0, arg_23_1):
	arg_23_0.binder.emit(RyzaMiniGameView.EVENT_FINISH, arg_23_1)

def var_0_0.WindowFocrus(arg_24_0, arg_24_1):
	arg_24_0.binder.emit(RyzaMiniGameView.EVENT_WINDOW_FOCUS, arg_24_1)

def var_0_0.SyncStatus(arg_25_0, arg_25_1, arg_25_2, arg_25_3):
	arg_25_0.binder.emit(RyzaMiniGameView.EVENT_STATUS_SYNC, arg_25_1, arg_25_2, arg_25_3)

def var_0_0.UpdateHide(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0.binder.emit(RyzaMiniGameView.EVENT_UPDATE_HIDE, arg_26_1, arg_26_2)

def var_0_0.UpdatePos(arg_27_0, arg_27_1, arg_27_2):
	table.removebyvalue(arg_27_0.map[tostring(arg_27_1.pos)], arg_27_1)
	table.insert(arg_27_0.map[tostring(arg_27_2)], arg_27_1)

local function var_0_3(arg_28_0, arg_28_1)
	local var_28_0 = arg_28_1.pos - arg_28_0.pos

	for iter_28_0, iter_28_1 in ipairs(arg_28_0.range):
		for iter_28_2, iter_28_3 in ipairs(arg_28_1.range):
			local var_28_1 = {
				{},
				{}
			}

			for iter_28_4, iter_28_5 in ipairs(iter_28_1):
				var_28_1[iter_28_4][1] = iter_28_5[1] - iter_28_3[iter_28_4][2]
				var_28_1[iter_28_4][2] = iter_28_5[2] - iter_28_3[iter_28_4][1]

			if var_28_0.x > var_28_1[1][1] and var_28_0.x < var_28_1[1][2] and var_28_0.y > var_28_1[2][1] and var_28_0.y < var_28_1[2][2]:
				return True

	return False

def var_0_0.Wayfinding(arg_29_0, arg_29_1):
	if arg_29_0.reactorRyza.hide or arg_29_0.CollideRyza(arg_29_1):
		arg_29_0.findingResult[arg_29_1] = None

		return {
			arg_29_0.realPos
		}
	elif arg_29_0.findingResult[arg_29_1]:
		local var_29_0 = arg_29_0.findingResult[arg_29_1]

		if var_29_0.ryzaPos == arg_29_0.reactorRyza.pos and var_29_0.reactorPos == arg_29_1.pos:
			return var_29_0.path
		else
			arg_29_0.findingResult[arg_29_1] = None

	local var_29_1 = {
		arg_29_1.pos
	}
	local var_29_2 = {
		[tostring(arg_29_1.pos)] = 0
	}

	local function var_29_3(arg_30_0)
		local var_30_0 = {}

		while var_29_2[tostring(var_29_1[arg_30_0])] > 0:
			table.insert(var_30_0, var_29_1[arg_30_0])

			arg_30_0 = var_29_2[tostring(var_29_1[arg_30_0])]

		arg_29_0.findingResult[arg_29_1] = {
			ryzaPos = arg_29_0.reactorRyza.pos,
			reactorPos = arg_29_1.pos,
			path = var_30_0
		}

		return var_30_0

	local var_29_4 = 0
	local var_29_5

	while var_29_4 < #var_29_1:
		var_29_4 = var_29_4 + 1

		for iter_29_0, iter_29_1 in ipairs(var_0_2):
			local var_29_6 = var_29_1[var_29_4] + NewPos(unpack(iter_29_1))

			if var_29_2[tostring(var_29_6)] == None:
				if arg_29_0.GetCellPassability(var_29_6):
					var_29_2[tostring(var_29_6)] = var_29_4

					table.insert(var_29_1, var_29_6)

					if var_0_3({
						pos = arg_29_0.reactorRyza.realPos,
						range = arg_29_0.reactorRyza.GetCollideRange()
					}, {
						pos = var_29_6,
						range = arg_29_1.GetCollideRange()
					}):
						return var_29_3(#var_29_1)
				else
					var_29_2[tostring(var_29_6)] = False

		for iter_29_2, iter_29_3 in ipairs(var_0_2):
			local var_29_7 = NewPos(unpack(iter_29_3))
			local var_29_8 = NewPos(unpack(var_0_2[iter_29_2 % 4 + 1]))
			local var_29_9 = var_29_1[var_29_4] + var_29_7 + var_29_8

			if var_29_2[tostring(var_29_1[var_29_4] + var_29_7)] and var_29_2[tostring(var_29_1[var_29_4] + var_29_8)] and var_29_2[tostring(var_29_9)] == None and arg_29_0.GetCellPassability(var_29_9):
				var_29_2[tostring(var_29_9)] = var_29_4

				table.insert(var_29_1, var_29_9)

				if var_0_3({
					pos = arg_29_0.reactorRyza.realPos,
					range = arg_29_0.reactorRyza.GetCollideRange()
				}, {
					pos = var_29_9,
					range = arg_29_1.GetCollideRange()
				}):
					return var_29_3(#var_29_1)

def var_0_0.SearchRyza(arg_31_0, arg_31_1, arg_31_2):
	if arg_31_0.reactorRyza.hide:
		return False
	else
		return ((arg_31_1.realPos or arg_31_1.pos) - arg_31_0.reactorRyza.realPos).SqrMagnitude() < arg_31_2 * arg_31_2

def var_0_0.CollideRyza(arg_32_0, arg_32_1):
	return var_0_3({
		pos = arg_32_0.reactorRyza.realPos,
		range = arg_32_0.reactorRyza.GetCollideRange()
	}, {
		pos = arg_32_1.realPos,
		range = arg_32_1.GetCollideRange()
	})

def var_0_0.CollideFire(arg_33_0, arg_33_1):
	return underscore.filter(arg_33_0.fireList, function(arg_34_0)
		return var_0_3({
			pos = arg_34_0.pos,
			range = arg_34_0.GetCollideRange()
		}, {
			pos = arg_33_1.realPos,
			range = arg_33_1.GetCollideRange()
		}))

return var_0_0
