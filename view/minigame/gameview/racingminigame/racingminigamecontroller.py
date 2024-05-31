local var_0_0 = class("RacingMiniGameController")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.binder = arg_1_1

	arg_1_0.InitTimer()
	arg_1_0.InitGameUI(arg_1_2)

local function var_0_1(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_0.GetComponentsInChildren(typeof(Animator), True)

	for iter_2_0 = 0, var_2_0.Length - 1:
		var_2_0[iter_2_0].speed = arg_2_1

local function var_0_2(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0.GetComponentsInChildren(typeof(SpineAnimUI), True)

	for iter_3_0 = 0, var_3_0.Length - 1:
		if IsNil(var_3_0[iter_3_0]):
			-- block empty
		elif arg_3_1:
			var_3_0[iter_3_0].Pause()
		else
			var_3_0[iter_3_0].Resume()

def var_0_0.InitTimer(arg_4_0):
	arg_4_0.timer = Timer.New(function()
		arg_4_0.OnTimer(RacingMiniGameConfig.TIME_INTERVAL), RacingMiniGameConfig.TIME_INTERVAL, -1)

	if IsUnityEditor and not arg_4_0.handle:
		arg_4_0.handle = UpdateBeat.CreateListener(function()
			if Input.GetKeyDown(KeyCode.W):
				arg_4_0.up = True

			if Input.GetKeyUp(KeyCode.W):
				arg_4_0.up = False

			if Input.GetKeyDown(KeyCode.S):
				arg_4_0.down = True

			if Input.GetKeyUp(KeyCode.S):
				arg_4_0.down = False

			if Input.GetKeyDown(KeyCode.Space):
				arg_4_0.boost = True

			if Input.GetKeyUp(KeyCode.Space):
				arg_4_0.boost = False, arg_4_0)

		UpdateBeat.AddListener(arg_4_0.handle)

def var_0_0.InitGameUI(arg_7_0, arg_7_1):
	arg_7_0.rtViewport = arg_7_1.Find("Viewport")
	arg_7_0.bgSingleSize = arg_7_0.rtViewport.rect.width
	arg_7_0.rtBgContent = arg_7_0.rtViewport.Find("BgContent")
	arg_7_0.rtMainContent = arg_7_0.rtViewport.Find("MainContent")
	arg_7_0.singleHeight = arg_7_0.rtMainContent.rect.height / 3
	arg_7_0.rtRes = arg_7_1.Find("Resource")
	arg_7_0.rtController = arg_7_1.Find("Controller")

	for iter_7_0, iter_7_1 in ipairs({
		"up",
		"down",
		"boost"
	}):
		local var_7_0 = GetOrAddComponent(arg_7_0.rtController.Find("bottom/btn_" .. iter_7_1), typeof(EventTriggerListener))

		var_7_0.AddPointDownFunc(function()
			arg_7_0[iter_7_1] = True)
		var_7_0.AddPointUpFunc(function()
			arg_7_0[iter_7_1] = False)

	if RacingMiniGameConfig.BOOST_BUTTON_TYPE_CHANGE:
		RemoveComponent(arg_7_0.rtController.Find("bottom/btn_boost"), typeof(EventTriggerListener))
		onButton(arg_7_0.binder, arg_7_0.rtController.Find("bottom/btn_boost"), function()
			if not arg_7_0.target.isBlock:
				local var_10_0 = RacingMiniGameConfig.M_LIST
				local var_10_1 = RacingMiniGameConfig.S_LIST

				arg_7_0.enginePower = math.clamp(arg_7_0.enginePower + RacingMiniGameConfig.BOOST_RATE[2], var_10_0[1], var_10_0[#var_10_0])

				if arg_7_0.target.state == "base":
					arg_7_0.target.Show("accel"))

	arg_7_0.rtTime = arg_7_0.rtController.Find("top/time")

	setText(arg_7_0.rtTime.Find("Text/plus"), "+" .. RacingMiniGameConfig.ITEM_ADD_TIME .. "s")
	arg_7_0.rtTime.Find("Text/plus").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		setActive(arg_7_0.rtTime.Find("Text/plus"), False))

	arg_7_0.rtDis = arg_7_0.rtController.Find("top/dis")
	arg_7_0.rtPower = arg_7_0.rtController.Find("bottom/speed")
	arg_7_0.rtFriend = arg_7_0.rtController.Find("top/friend")
	arg_7_0.queue = {}

def var_0_0.ResetGame(arg_12_0):
	arg_12_0.timeCount = 0
	arg_12_0.timeAll = RacingMiniGameConfig.ALL_TIME

	if arg_12_0.target:
		arg_12_0.target.Clear()

		arg_12_0.target = None

	while #arg_12_0.queue > 0:
		arg_12_0.queue[#arg_12_0.queue].Clear()

	arg_12_0.enginePower = 0
	arg_12_0.chargeDis = 0
	arg_12_0.disCount = 0
	arg_12_0.rateDic = {}
	arg_12_0.itemCountDic = {}

def var_0_0.ReadyGame(arg_13_0, arg_13_1):
	local var_13_0 = getProxy(PlayerProxy).getRawData()

	arg_13_0.rankData = underscore.filter(arg_13_1, function(arg_14_0)
		return arg_14_0.player_id != var_13_0.id)

	table.sort(arg_13_0.rankData, CompareFuncs({
		function(arg_15_0)
			return arg_15_0.score
	}))

	arg_13_0.target = RacingMiniNameSpace.Motorcycle.New(cloneTplTo(arg_13_0.rtRes.Find("qiye_minigame"), arg_13_0.rtMainContent.Find(-2)), NewPos(0, 0), arg_13_0)

	table.insert(arg_13_0.queue, RacingMiniNameSpace.StartMark.New(cloneTplTo(arg_13_0.rtRes.Find("start_mark"), arg_13_0.rtMainContent.Find(-2)), NewPos(550, 0), arg_13_0))
	arg_13_0.UpdateDisplay()
	onNextTick(function()
		arg_13_0.PauseGame())

def var_0_0.StartGame(arg_17_0):
	arg_17_0.isStart = True

	arg_17_0.ResumeGame()

def var_0_0.EndGame(arg_18_0, arg_18_1):
	arg_18_0.isStart = False

	arg_18_0.PauseGame()

	arg_18_0.result = arg_18_1 or 0
	arg_18_0.point = arg_18_0.disCount / 20
	arg_18_0.point = arg_18_0.point - arg_18_0.point % 0.01

	arg_18_0.binder.openUI("result")

def var_0_0.ResumeGame(arg_19_0):
	arg_19_0.isPause = False

	arg_19_0.timer.Start()
	var_0_1(arg_19_0.rtViewport, 1)
	var_0_2(arg_19_0.rtViewport, False)

def var_0_0.PauseGame(arg_20_0):
	arg_20_0.isPause = True

	arg_20_0.timer.Stop()
	var_0_1(arg_20_0.rtViewport, 0)
	var_0_2(arg_20_0.rtViewport, True)

local function var_0_3(arg_21_0, arg_21_1)
	local var_21_0 = arg_21_1.pos - arg_21_0.pos
	local var_21_1 = {}

	for iter_21_0 = 1, 2:
		var_21_1[iter_21_0] = {}
		var_21_1[iter_21_0][1] = arg_21_0.colliderSize[iter_21_0][1] - arg_21_1.colliderSize[iter_21_0][2]
		var_21_1[iter_21_0][2] = arg_21_0.colliderSize[iter_21_0][2] - arg_21_1.colliderSize[iter_21_0][1]

	return var_21_1[1][1] < var_21_0.x and var_21_0.x < var_21_1[1][2] and var_21_1[2][1] < var_21_0.y and var_21_0.y < var_21_1[2][2]

def var_0_0.OnTimer(arg_22_0, arg_22_1):
	arg_22_0.timeCount = arg_22_0.timeCount + arg_22_1

	if arg_22_0.timeCount > arg_22_0.timeAll:
		arg_22_0.EndGame(1)

		return

	if arg_22_0.target.invincibleTime:
		arg_22_0.target.UpdateInvincibility(arg_22_1)

	local var_22_0 = NewPos(0, 0)
	local var_22_1 = arg_22_0.GetSpeed(RacingMiniGameConfig.BOOST_RATE[not arg_22_0.target.isBlock and arg_22_0.boost and 2 or 1] * arg_22_1)

	var_22_0.x = var_22_1 * arg_22_1

	if not arg_22_0.target.isBlock:
		if var_22_1 > 0:
			if arg_22_0.up:
				var_22_0.y = var_22_0.y + 1

			if arg_22_0.down:
				var_22_0.y = var_22_0.y - 1

			var_22_0.y = var_22_0.y * arg_22_0.singleHeight / RacingMiniGameConfig.Y_COVER_TIME * (arg_22_0.target.isVertigo and RacingMiniGameConfig.Y_OBSTACLE_REDUCE or 1) * arg_22_1

			if arg_22_0.target.state == "base" and arg_22_0.boost:
				arg_22_0.target.Show("accel")
		elif not arg_22_0.target.isVertigo and arg_22_0.target.state != "base":
			arg_22_0.target.Show("base")

	arg_22_0.target.UpdatePos(var_22_0 * NewPos(0, 1), arg_22_0.singleHeight)
	setParent(arg_22_0.target.rt, arg_22_0.rtMainContent.Find(math.clamp(math.floor((arg_22_0.target.pos.y + arg_22_0.singleHeight) * 3 / 2 / arg_22_0.singleHeight) - 1, -1, 1) - 1))

	local var_22_2 = 1

	while var_22_2 <= #arg_22_0.queue:
		local var_22_3 = arg_22_0.queue[var_22_2]

		var_22_3.UpdatePos(var_22_0 * NewPos(-1, 0))

		if not var_22_3.isTriggered and var_22_3.colliderSize and var_0_3(var_22_3, arg_22_0.target):
			var_22_3.Trigger(arg_22_0.target)

		if var_22_3.pos.x < -arg_22_0.bgSingleSize:
			var_22_3.Clear()
		else
			var_22_2 = var_22_2 + 1

	local var_22_4 = arg_22_0.rtBgContent.anchoredPosition.x - var_22_0.x

	if var_22_4 < -arg_22_0.bgSingleSize / 2:
		var_22_4 = var_22_4 + arg_22_0.bgSingleSize

	setAnchoredPosition(arg_22_0.rtBgContent, {
		x = var_22_4
	})

	arg_22_0.chargeDis = arg_22_0.chargeDis - var_22_0.x

	if arg_22_0.chargeDis <= 0:
		arg_22_0.CreateNewObject()

	arg_22_0.disCount = arg_22_0.disCount + var_22_0.x

	arg_22_0.UpdateDisplay()

def var_0_0.UpdateDisplay(arg_23_0):
	local var_23_0 = arg_23_0.timeAll - arg_23_0.timeCount

	setText(arg_23_0.rtTime.Find("Text"), string.format("%02d.%02ds", math.floor(var_23_0), math.floor((var_23_0 - math.floor(var_23_0)) * 100)))

	local var_23_1 = arg_23_0.disCount / 20

	setText(arg_23_0.rtDis, string.format("%.2fm", var_23_1 - var_23_1 % 0.01))

	local var_23_2 = RacingMiniGameConfig.BUOY_POWER_LIST
	local var_23_3 = RacingMiniGameConfig.BUOY_POS_LIST
	local var_23_4

	for iter_23_0, iter_23_1 in ipairs(var_23_2):
		if iter_23_1 >= arg_23_0.enginePower:
			var_23_4 = iter_23_0

			break

	setAnchoredPosition(arg_23_0.rtPower.Find("range/buoy"), {
		x = var_23_4 > 1 and var_23_3[var_23_4 - 1] + (arg_23_0.enginePower - var_23_2[var_23_4 - 1]) / (var_23_2[var_23_4] - var_23_2[var_23_4 - 1]) * (var_23_3[var_23_4] - var_23_3[var_23_4 - 1]) or 0
	})

	if arg_23_0.target.isVertigo:
		var_23_4 = 1

	for iter_23_2, iter_23_3 in ipairs(arg_23_0.target.effectList):
		setActive(iter_23_3, var_23_4 - 1 == iter_23_2)

	local var_23_5 = RacingMiniGameConfig.FRIEND_DIS_LIST

	arg_23_0.friendIndex = defaultValue(arg_23_0.friendIndex, 1)

	while arg_23_0.friendIndex < #var_23_5 and var_23_5[arg_23_0.friendIndex + 1] < arg_23_0.disCount / 20:
		arg_23_0.friendIndex = arg_23_0.friendIndex + 1
		arg_23_0.friendDirty = True

	if arg_23_0.friendDirty:
		arg_23_0.friendDirty = False

		while #arg_23_0.rankData > 0 and arg_23_0.rankData[1].score / 100 < var_23_5[arg_23_0.friendIndex]:
			table.remove(arg_23_0.rankData, 1)

		local var_23_6

		for iter_23_4, iter_23_5 in ipairs(arg_23_0.rankData):
			if arg_23_0.friendIndex == #var_23_5 or iter_23_5.score / 100 < var_23_5[arg_23_0.friendIndex + 1]:
				var_23_6 = iter_23_4
			else
				break

		setActive(arg_23_0.rtFriend, var_23_6)

		if var_23_6:
			arg_23_0.friendInfo = arg_23_0.rankData[math.random(var_23_6)]
		else
			arg_23_0.friendInfo = None

		if arg_23_0.friendInfo:
			setText(arg_23_0.rtFriend.Find("Text"), arg_23_0.friendInfo.name)
			setText(arg_23_0.rtFriend.Find("point"), string.format("%.2fm", arg_23_0.friendInfo.score / 100))

local var_0_4 = {
	TrafficCone = "roadblocks",
	Mire = "mire",
	Roadblock = "roadblocks",
	SpeedBumps = "speed_bumps",
	Bomb = "roadblocks",
	MoreTime = "more_time",
	Invincibility = "invincibility"
}

def var_0_0.CreateNewObject(arg_24_0):
	local var_24_0

	for iter_24_0, iter_24_1 in ipairs(RacingMiniGameConfig.FIELD_CONFIG):
		if arg_24_0.timeCount < iter_24_1.time:
			break
		else
			var_24_0 = iter_24_1

	local var_24_1 = {}
	local var_24_2 = 0

	for iter_24_2 = -1, 1:
		arg_24_0.rateDic[iter_24_2] = defaultValue(arg_24_0.rateDic[iter_24_2], 0)

		local var_24_3 = math.random() / (2 - iter_24_2)
		local var_24_4

		if var_24_3 < arg_24_0.rateDic[iter_24_2]:
			var_24_2 = var_24_2 + 1
			var_24_1[iter_24_2] = True
		else
			var_24_1[iter_24_2] = False

	if var_24_2 == 3:
		var_24_1[math.random(3) - 2] = False

	for iter_24_3 = -1, 1:
		if var_24_1[iter_24_3]:
			classCfg = var_24_0.obstacle_distribution
		else
			classCfg = var_24_0.item_distribution

		rate = math.random()

		local var_24_5 = 0
		local var_24_6 = 0

		for iter_24_4, iter_24_5 in ipairs(classCfg):
			var_24_6 = var_24_6 + iter_24_5[2]

		local var_24_7

		for iter_24_6, iter_24_7 in ipairs(classCfg):
			var_24_5 = var_24_5 + iter_24_7[2]

			if var_24_5 > rate * var_24_6:
				var_24_7 = iter_24_7[1]

				break

		if var_24_7 and superof(RacingMiniNameSpace[var_24_7], RacingMiniNameSpace.Item):
			if defaultValue(arg_24_0.itemCountDic[var_24_7], 0) < defaultValue(var_24_0.item_create_limit[var_24_7], 0):
				arg_24_0.itemCountDic[var_24_7] = defaultValue(arg_24_0.itemCountDic[var_24_7], 0) + 1
			else
				var_24_7 = None

		if var_24_7:
			local var_24_8 = RacingMiniNameSpace[var_24_7].New(cloneTplTo(arg_24_0.rtRes.Find(var_0_4[var_24_7]), arg_24_0.rtMainContent.Find(iter_24_3)), NewPos(arg_24_0.bgSingleSize * 1.5 + arg_24_0.chargeDis, iter_24_3 * arg_24_0.singleHeight), arg_24_0)

			table.insert(arg_24_0.queue, var_24_8)

			arg_24_0.rateDic[iter_24_3] = arg_24_0.rateDic[iter_24_3] * var_24_0.continue_reduce
		else
			arg_24_0.rateDic[iter_24_3] = arg_24_0.rateDic[iter_24_3] + var_24_0.bye_plus

	arg_24_0.chargeDis = arg_24_0.chargeDis + var_24_0.recharge_dis

def var_0_0.GetSpeed(arg_25_0, arg_25_1):
	local var_25_0
	local var_25_1 = RacingMiniGameConfig.M_LIST
	local var_25_2 = RacingMiniGameConfig.S_LIST

	for iter_25_0 = 1, #var_25_1 - 1:
		if var_25_1[iter_25_0 + 1] > arg_25_0.enginePower:
			var_25_0 = var_25_2[iter_25_0] + (arg_25_0.enginePower - var_25_1[iter_25_0]) / (var_25_1[iter_25_0 + 1] - var_25_1[iter_25_0]) * (var_25_2[iter_25_0 + 1] - var_25_2[iter_25_0])

			break

	var_25_0 = var_25_0 or var_25_2[#var_25_2]
	arg_25_0.enginePower = math.clamp(arg_25_0.enginePower + arg_25_1, var_25_1[1], var_25_1[#var_25_1])

	return var_25_0 * 10

def var_0_0.AddTime(arg_26_0, arg_26_1):
	arg_26_0.timeAll = arg_26_0.timeAll + arg_26_1

	setActive(arg_26_0.rtTime.Find("Text/plus"), True)

def var_0_0.SetEnginePower(arg_27_0, arg_27_1):
	arg_27_0.enginePower = math.min(arg_27_0.enginePower, arg_27_1)

def var_0_0.willExit(arg_28_0):
	if arg_28_0.handle:
		UpdateBeat.RemoveListener(arg_28_0.handle)

return var_0_0
