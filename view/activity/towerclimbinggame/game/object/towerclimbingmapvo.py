local var_0_0 = class("TowerClimbingMapVO")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.view = arg_1_2
	arg_1_0.nextBlockIndex = 0
	arg_1_0.level = 0
	arg_1_0.higestLevel = 0
	arg_1_0.id = arg_1_1

	assert(arg_1_0.id, arg_1_1)

def var_0_0.Init(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.mapWidth = arg_2_1.screenWidth
	arg_2_0.mapHeight = arg_2_1.screenHeight
	arg_2_0.awards = arg_2_1.awards[arg_2_0.id]

	seriesAsync({
		function(arg_3_0)
			arg_2_0.InitBlock(arg_3_0),
		function(arg_4_0)
			arg_2_0.InitPlayer(arg_2_1, arg_4_0),
		function(arg_5_0)
			arg_2_0.InitGround(arg_2_1, arg_5_0),
		function(arg_6_0)
			local var_6_0 = arg_2_0.blocks[1]

			assert(var_6_0)
			arg_2_0.player.SetPosition(var_6_0.position)
			arg_2_0.SendMapEvent("OnPlayerLifeUpdate", arg_2_0.player.life)
			arg_6_0()
	}, arg_2_2)

def var_0_0.InitGround(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = TowerClimbingGameSettings.MANJUU_START_POS

	arg_7_0.ground = {
		sleepTime = 0,
		IsRuning = False,
		position = var_7_0,
		name = arg_7_1.npcName
	}

	arg_7_0.SendMapEvent("OnCreateGround", arg_7_0.ground, arg_7_2)

def var_0_0.InitBlock(arg_8_0, arg_8_1):
	arg_8_0.blocks = {}

	local var_8_0 = {}
	local var_8_1 = TowerClimbingGameSettings.GetBlockInitCnt(arg_8_0.mapHeight)

	for iter_8_0 = 1, var_8_1:
		table.insert(var_8_0, function(arg_9_0)
			local var_9_0 = arg_8_0.CreateBlock()

			table.insert(arg_8_0.blocks, var_9_0)
			arg_8_0.SendMapEvent("OnCreateBlock", var_9_0, arg_9_0))

	parallelAsync(var_8_0, arg_8_1)

local function var_0_1(arg_10_0, arg_10_1)
	if arg_10_0 == 1:
		return TowerClimbingGameSettings.HEAD_BLOCK_TYPE
	else
		local var_10_0 = TowerClimbingGameSettings.MapId2BlockType[arg_10_1]

		assert(var_10_0, arg_10_1)

		local var_10_1 = math.random(1, 100)

		for iter_10_0, iter_10_1 in ipairs(var_10_0):
			if var_10_1 <= iter_10_1[2]:
				return iter_10_1[1]

		assert(False)

local function var_0_2(arg_11_0, arg_11_1)
	if not arg_11_1:
		return TowerClimbingGameSettings.BLOCK_START_POSITION
	else
		local var_11_0 = arg_11_1.position
		local var_11_1 = arg_11_1.width
		local var_11_2 = TowerClimbingGameSettings.BLOCK_INTERVAL_HEIGHT
		local var_11_3 = TowerClimbingGameSettings.BLOCK_MAX_INTERVAL_WIDTH[1]
		local var_11_4 = TowerClimbingGameSettings.BLOCK_MAX_INTERVAL_WIDTH[2]
		local var_11_5 = TowerClimbingGameSettings.BOUNDS[1]
		local var_11_6 = TowerClimbingGameSettings.BOUNDS[2]
		local var_11_7 = {}
		local var_11_8 = var_11_0.x + var_11_1 / 2
		local var_11_9 = var_11_6 - var_11_8 - arg_11_0

		if var_11_3 < var_11_9:
			local var_11_10 = math.min(var_11_4, var_11_9)
			local var_11_11 = var_11_3

			if var_11_9 >= 0:
				var_11_11 = 0

			local var_11_12 = math.random(var_11_11, var_11_10)

			table.insert(var_11_7, var_11_8 + var_11_12 + arg_11_0 / 2)

		local var_11_13 = var_11_0.x - var_11_1 / 2
		local var_11_14 = math.abs(var_11_5 - var_11_13) - arg_11_0

		if var_11_3 < var_11_14:
			local var_11_15 = math.min(var_11_4, var_11_14)
			local var_11_16 = var_11_3

			if var_11_14 >= 0:
				var_11_16 = 0

			local var_11_17 = math.random(var_11_16, var_11_15)

			table.insert(var_11_7, var_11_13 - var_11_17 - arg_11_0 / 2)

		assert(#var_11_7 > 0, var_11_9 .. " & " .. var_11_14 .. " - " .. arg_11_0 .. " - " .. var_11_0.x .. "-" .. var_11_1)

		local var_11_18 = math.random(1, #var_11_7)

		return Vector2(var_11_7[var_11_18], var_11_0.y + var_11_2)

def var_0_0.CreateBlock(arg_12_0):
	arg_12_0.nextBlockIndex = arg_12_0.nextBlockIndex + 1

	local var_12_0 = arg_12_0.blocks[#arg_12_0.blocks]
	local var_12_1 = var_0_1(arg_12_0.nextBlockIndex, arg_12_0.id)
	local var_12_2 = var_0_2(var_12_1[2], var_12_0)

	return {
		id = arg_12_0.nextBlockIndex,
		type = var_12_1[1],
		width = var_12_1[2],
		position = var_12_2,
		isActive = not var_12_0,
		level = arg_12_0.nextBlockIndex
	}

def var_0_0.ActicveNextBlock(arg_13_0, arg_13_1):
	for iter_13_0, iter_13_1 in ipairs(arg_13_0.blocks):
		if iter_13_1.level == arg_13_1:
			iter_13_1.isActive = True

			arg_13_0.SendMapEvent("OnActiveBlock", iter_13_1)

			if arg_13_0.player.IsInvincible():
				arg_13_0.SendMapEvent("OnEnableStab", iter_13_1, False)

			break

def var_0_0.DeactiveAboveBlocks(arg_14_0, arg_14_1):
	for iter_14_0, iter_14_1 in ipairs(arg_14_0.blocks):
		if arg_14_1 < iter_14_1.level and iter_14_1.isActive == True:
			iter_14_1.isActive = False

			arg_14_0.SendMapEvent("OnActiveBlock", iter_14_1)

def var_0_0.AddNewBlock(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.CreateBlock()

	table.insert(arg_15_0.blocks, var_15_0)
	arg_15_0.SendMapEvent("OnCreateBlock", var_15_0, arg_15_1)

def var_0_0.DoSink(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	local var_16_0 = {}

	table.insert(var_16_0, function(arg_17_0)
		arg_16_0.SendMapEvent("SinkHandler", TowerClimbingGameSettings.SINK_DISTANCE * arg_16_2))
	table.insert(var_16_0, 1, function(arg_18_0)
		if not arg_16_0.ground.IsRuning:
			arg_18_0()

			return

		local var_18_0 = arg_16_0.ground.position
		local var_18_1 = var_18_0.y - TowerClimbingGameSettings.SINK_DISTANCE * arg_16_2

		arg_16_0.ground.position = Vector2(var_18_0.x, var_18_1)

		arg_16_0.SendMapEvent("OnGroundPositionChange", arg_16_0.ground.position)
		arg_18_0())
	parallelAsync(var_16_0, arg_16_3)

def var_0_0.CheckCorssBoundBlocks(arg_19_0, arg_19_1):
	local var_19_0 = 0

	for iter_19_0 = #arg_19_0.blocks, 1, -1:
		local var_19_1 = arg_19_0.blocks[iter_19_0]

		if var_19_0 >= var_19_1.position.y:
			local var_19_2 = var_19_1.level

			table.remove(arg_19_0.blocks, iter_19_0)
			arg_19_0.SendMapEvent("OnBlockDestory", var_19_2)
		elif TowerClimbingGameSettings.MANJUU_HEIGHT + arg_19_0.ground.position.y >= var_19_1.position.y:
			var_19_1.isActive = False

			arg_19_0.SendMapEvent("OnActiveBlock", var_19_1)

	arg_19_1()

def var_0_0.InitPlayer(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0 = arg_20_1.life
	local var_20_1 = arg_20_1.score
	local var_20_2 = arg_20_1.shipId
	local var_20_3 = arg_20_1.higestscore
	local var_20_4 = arg_20_1.pageIndex
	local var_20_5 = arg_20_1.mapScores[arg_20_0.id]

	arg_20_0.player = TowerClimbingPlayerVO.New(arg_20_0.view, {
		id = var_20_2,
		life = var_20_0,
		score = var_20_1,
		higestscore = var_20_3,
		pageIndex = var_20_4,
		mapScore = var_20_5
	})

	arg_20_0.SendMapEvent("OnCreatePlayer", arg_20_0.player, arg_20_2)

def var_0_0.GetPlayer(arg_21_0):
	return arg_21_0.player

def var_0_0.GetBlocks(arg_22_0):
	return arg_22_0.blocks

def var_0_0.SetCurrentLevel(arg_23_0, arg_23_1):
	if arg_23_1 > arg_23_0.level:
		arg_23_0.ActicveNextBlock(arg_23_1 + 1)
	elif arg_23_1 < arg_23_0.level:
		arg_23_0.DeactiveAboveBlocks(arg_23_1 + 1)

	arg_23_0.level = arg_23_1

	if arg_23_1 > arg_23_0.higestLevel:
		local var_23_0 = arg_23_1 - arg_23_0.higestLevel

		arg_23_0.higestLevel = arg_23_1

		arg_23_0.player.AddScore()
		arg_23_0.DoCheck(var_23_0)
		arg_23_0.OverHigestScore()

def var_0_0.OverHigestScore(arg_24_0):
	local function var_24_0(arg_25_0)
		for iter_25_0, iter_25_1 in ipairs(arg_24_0.awards):
			if arg_25_0 == iter_25_1:
				return True

		return False

	if arg_24_0.player.IsOverHigestScore() and var_24_0(arg_24_0.player.score):
		arg_24_0.SendMapEvent("OnReachAwardScore")

def var_0_0.DoCheck(arg_26_0, arg_26_1):
	if arg_26_0.higestLevel <= 1:
		return

	seriesAsync({
		function(arg_27_0)
			arg_26_0.AddNewBlock(arg_27_0),
		function(arg_28_0)
			parallelAsync({
				function(arg_29_0)
					arg_26_0.DoSink(arg_26_0.higestLevel, arg_26_1, arg_29_0),
				function(arg_30_0)
					local var_30_0 = TowerClimbingGameSettings.SINK_DISTANCE * arg_26_1

					arg_26_0.SendMapEvent("OnSink", var_30_0, arg_30_0)
			}, arg_28_0),
		function(arg_31_0)
			arg_26_0.CheckCorssBoundBlocks(arg_31_0),
		function(arg_32_0)
			arg_26_0.CheckGroundState()
			arg_32_0()
	})

def var_0_0.CheckGroundState(arg_33_0):
	if not arg_33_0.ground.IsRuning and arg_33_0.higestLevel >= TowerClimbingGameSettings.GROUND_RISE_UP_LEVEL:
		arg_33_0.ground.IsRuning = True

		arg_33_0.SendMapEvent("OnGroundRuning")

def var_0_0.ReBornPlayer(arg_34_0):
	local var_34_0 = {}
	local var_34_1

	for iter_34_0, iter_34_1 in ipairs(arg_34_0.blocks):
		if iter_34_1.isActive:
			table.insert(var_34_0, iter_34_1)

	assert(#var_34_0 > 0)

	local var_34_2 = _.detect(var_34_0, function(arg_35_0)
		return arg_35_0.level == arg_34_0.higestLevel)

	if not var_34_2:
		table.sort(var_34_0, function(arg_36_0, arg_36_1)
			return arg_36_0.position.y > arg_36_1.position.y)

		var_34_2 = var_34_0[1]

	arg_34_0.player.SetPosition(var_34_2.position + Vector2(0, 10))

def var_0_0.AddPlayerInvincibleEffect(arg_37_0, arg_37_1):
	for iter_37_0, iter_37_1 in ipairs(arg_37_0.blocks):
		if iter_37_1.isActive:
			arg_37_0.SendMapEvent("OnEnableStab", iter_37_1, not arg_37_1)

	if arg_37_0.ground.IsRuning:
		arg_37_0.SendMapEvent("OnEnableGround", not arg_37_1)

local function var_0_3(arg_38_0)
	local var_38_0 = TowerClimbingGameSettings.GROUND_RISE_UP_SPEED
	local var_38_1 = var_38_0[#var_38_0][2]

	for iter_38_0, iter_38_1 in ipairs(var_38_0):
		if arg_38_0 < iter_38_1[1]:
			var_38_1 = iter_38_1[2]

			break

	return var_38_1

def var_0_0.Update(arg_39_0):
	if arg_39_0.ground.sleepTime > 0:
		arg_39_0.ground.sleepTime = arg_39_0.ground.sleepTime - Time.deltaTime

		arg_39_0.SendMapEvent("OnGroundSleepTimeChange", arg_39_0.ground.sleepTime)

	if arg_39_0.ground.IsRuning and arg_39_0.ground.sleepTime <= 0:
		local var_39_0 = arg_39_0.ground.position
		local var_39_1 = var_0_3(arg_39_0.higestLevel)

		arg_39_0.ground.position = Vector2(var_39_0.x, var_39_0.y + var_39_1 * Time.deltaTime)

		arg_39_0.SendMapEvent("OnGroundPositionChange", arg_39_0.ground.position)

	if arg_39_0.player.IsInvincible():
		local var_39_2 = arg_39_0.player.GetInvincibleTime()

		if var_39_2 == TowerClimbingGameSettings.INVINCEIBLE_TIME:
			arg_39_0.AddPlayerInvincibleEffect(True)

		local var_39_3 = var_39_2 - Time.deltaTime

		arg_39_0.player.SetInvincibleTime(var_39_3)

		if not arg_39_0.player.IsInvincible():
			arg_39_0.AddPlayerInvincibleEffect(False)

def var_0_0.SetGroundSleep(arg_40_0, arg_40_1):
	if arg_40_0.ground.IsRuning:
		arg_40_0.ground.position = Vector2(arg_40_0.ground.position.x, arg_40_0.ground.position.y - TowerClimbingGameSettings.GROUND_SLIDE_DOWNWARD_DISTANCE)

		arg_40_0.SendMapEvent("OnGroundPositionChange", arg_40_0.ground.position)

		arg_40_0.ground.sleepTime = arg_40_1

def var_0_0.SendMapEvent(arg_41_0, arg_41_1, ...):
	local var_41_0 = arg_41_0.view.map

	var_41_0[arg_41_1](var_41_0, unpack({
		...
	}))

def var_0_0.Dispose(arg_42_0):
	if arg_42_0.player:
		arg_42_0.player.Dispose()

		arg_42_0.player = None

	if arg_42_0.ground:
		arg_42_0.ground = None

	if arg_42_0.blocks:
		arg_42_0.blocks = None

return var_0_0
