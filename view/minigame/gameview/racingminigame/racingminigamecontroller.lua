local var_0_0 = class("RacingMiniGameController")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.binder = arg_1_1

	arg_1_0:InitTimer()
	arg_1_0:InitGameUI(arg_1_2)
end

local function var_0_1(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_0:GetComponentsInChildren(typeof(Animator), true)

	for iter_2_0 = 0, var_2_0.Length - 1 do
		var_2_0[iter_2_0].speed = arg_2_1
	end
end

local function var_0_2(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0:GetComponentsInChildren(typeof(SpineAnimUI), true)

	for iter_3_0 = 0, var_3_0.Length - 1 do
		if IsNil(var_3_0[iter_3_0]) then
			-- block empty
		elseif arg_3_1 then
			var_3_0[iter_3_0]:Pause()
		else
			var_3_0[iter_3_0]:Resume()
		end
	end
end

function var_0_0.InitTimer(arg_4_0)
	arg_4_0.timer = Timer.New(function()
		arg_4_0:OnTimer(RacingMiniGameConfig.TIME_INTERVAL)
	end, RacingMiniGameConfig.TIME_INTERVAL, -1)

	if IsUnityEditor and not arg_4_0.handle then
		arg_4_0.handle = UpdateBeat:CreateListener(function()
			if Input.GetKeyDown(KeyCode.W) then
				arg_4_0.up = true
			end

			if Input.GetKeyUp(KeyCode.W) then
				arg_4_0.up = false
			end

			if Input.GetKeyDown(KeyCode.S) then
				arg_4_0.down = true
			end

			if Input.GetKeyUp(KeyCode.S) then
				arg_4_0.down = false
			end

			if Input.GetKeyDown(KeyCode.Space) then
				arg_4_0.boost = true
			end

			if Input.GetKeyUp(KeyCode.Space) then
				arg_4_0.boost = false
			end
		end, arg_4_0)

		UpdateBeat:AddListener(arg_4_0.handle)
	end
end

function var_0_0.InitGameUI(arg_7_0, arg_7_1)
	arg_7_0.rtViewport = arg_7_1:Find("Viewport")
	arg_7_0.bgSingleSize = arg_7_0.rtViewport.rect.width
	arg_7_0.rtBgContent = arg_7_0.rtViewport:Find("BgContent")
	arg_7_0.rtMainContent = arg_7_0.rtViewport:Find("MainContent")
	arg_7_0.singleHeight = arg_7_0.rtMainContent.rect.height / 3
	arg_7_0.rtRes = arg_7_1:Find("Resource")
	arg_7_0.rtController = arg_7_1:Find("Controller")

	for iter_7_0, iter_7_1 in ipairs({
		"up",
		"down",
		"boost"
	}) do
		local var_7_0 = GetOrAddComponent(arg_7_0.rtController:Find("bottom/btn_" .. iter_7_1), typeof(EventTriggerListener))

		var_7_0:AddPointDownFunc(function()
			arg_7_0[iter_7_1] = true
		end)
		var_7_0:AddPointUpFunc(function()
			arg_7_0[iter_7_1] = false
		end)
	end

	if RacingMiniGameConfig.BOOST_BUTTON_TYPE_CHANGE then
		RemoveComponent(arg_7_0.rtController:Find("bottom/btn_boost"), typeof(EventTriggerListener))
		onButton(arg_7_0.binder, arg_7_0.rtController:Find("bottom/btn_boost"), function()
			if not arg_7_0.target.isBlock then
				local var_10_0 = RacingMiniGameConfig.M_LIST
				local var_10_1 = RacingMiniGameConfig.S_LIST

				arg_7_0.enginePower = math.clamp(arg_7_0.enginePower + RacingMiniGameConfig.BOOST_RATE[2], var_10_0[1], var_10_0[#var_10_0])

				if arg_7_0.target.state == "base" then
					arg_7_0.target:Show("accel")
				end
			end
		end)
	end

	arg_7_0.rtTime = arg_7_0.rtController:Find("top/time")

	setText(arg_7_0.rtTime:Find("Text/plus"), "+" .. RacingMiniGameConfig.ITEM_ADD_TIME .. "s")
	arg_7_0.rtTime:Find("Text/plus"):GetComponent(typeof(DftAniEvent)):SetEndEvent(function()
		setActive(arg_7_0.rtTime:Find("Text/plus"), false)
	end)

	arg_7_0.rtDis = arg_7_0.rtController:Find("top/dis")
	arg_7_0.rtPower = arg_7_0.rtController:Find("bottom/speed")
	arg_7_0.rtFriend = arg_7_0.rtController:Find("top/friend")
	arg_7_0.queue = {}
end

function var_0_0.ResetGame(arg_12_0)
	arg_12_0.timeCount = 0
	arg_12_0.timeAll = RacingMiniGameConfig.ALL_TIME

	if arg_12_0.target then
		arg_12_0.target:Clear()

		arg_12_0.target = nil
	end

	while #arg_12_0.queue > 0 do
		arg_12_0.queue[#arg_12_0.queue]:Clear()
	end

	arg_12_0.enginePower = 0
	arg_12_0.chargeDis = 0
	arg_12_0.disCount = 0
	arg_12_0.rateDic = {}
	arg_12_0.itemCountDic = {}
end

function var_0_0.ReadyGame(arg_13_0, arg_13_1)
	local var_13_0 = getProxy(PlayerProxy):getRawData()

	arg_13_0.rankData = underscore.filter(arg_13_1, function(arg_14_0)
		return arg_14_0.player_id ~= var_13_0.id
	end)

	table.sort(arg_13_0.rankData, CompareFuncs({
		function(arg_15_0)
			return arg_15_0.score
		end
	}))

	arg_13_0.target = RacingMiniNameSpace.Motorcycle.New(cloneTplTo(arg_13_0.rtRes:Find("qiye_minigame"), arg_13_0.rtMainContent:Find(-2)), NewPos(0, 0), arg_13_0)

	table.insert(arg_13_0.queue, RacingMiniNameSpace.StartMark.New(cloneTplTo(arg_13_0.rtRes:Find("start_mark"), arg_13_0.rtMainContent:Find(-2)), NewPos(550, 0), arg_13_0))
	arg_13_0:UpdateDisplay()
	onNextTick(function()
		arg_13_0:PauseGame()
	end)
end

function var_0_0.StartGame(arg_17_0)
	arg_17_0.isStart = true

	arg_17_0:ResumeGame()
end

function var_0_0.EndGame(arg_18_0, arg_18_1)
	arg_18_0.isStart = false

	arg_18_0:PauseGame()

	arg_18_0.result = arg_18_1 or 0
	arg_18_0.point = arg_18_0.disCount / 20
	arg_18_0.point = arg_18_0.point - arg_18_0.point % 0.01

	arg_18_0.binder:openUI("result")
end

function var_0_0.ResumeGame(arg_19_0)
	arg_19_0.isPause = false

	arg_19_0.timer:Start()
	var_0_1(arg_19_0.rtViewport, 1)
	var_0_2(arg_19_0.rtViewport, false)
end

function var_0_0.PauseGame(arg_20_0)
	arg_20_0.isPause = true

	arg_20_0.timer:Stop()
	var_0_1(arg_20_0.rtViewport, 0)
	var_0_2(arg_20_0.rtViewport, true)
end

local function var_0_3(arg_21_0, arg_21_1)
	local var_21_0 = arg_21_1.pos - arg_21_0.pos
	local var_21_1 = {}

	for iter_21_0 = 1, 2 do
		var_21_1[iter_21_0] = {}
		var_21_1[iter_21_0][1] = arg_21_0.colliderSize[iter_21_0][1] - arg_21_1.colliderSize[iter_21_0][2]
		var_21_1[iter_21_0][2] = arg_21_0.colliderSize[iter_21_0][2] - arg_21_1.colliderSize[iter_21_0][1]
	end

	return var_21_1[1][1] < var_21_0.x and var_21_0.x < var_21_1[1][2] and var_21_1[2][1] < var_21_0.y and var_21_0.y < var_21_1[2][2]
end

function var_0_0.OnTimer(arg_22_0, arg_22_1)
	arg_22_0.timeCount = arg_22_0.timeCount + arg_22_1

	if arg_22_0.timeCount > arg_22_0.timeAll then
		arg_22_0:EndGame(1)

		return
	end

	if arg_22_0.target.invincibleTime then
		arg_22_0.target:UpdateInvincibility(arg_22_1)
	end

	local var_22_0 = NewPos(0, 0)
	local var_22_1 = arg_22_0:GetSpeed(RacingMiniGameConfig.BOOST_RATE[not arg_22_0.target.isBlock and arg_22_0.boost and 2 or 1] * arg_22_1)

	var_22_0.x = var_22_1 * arg_22_1

	if not arg_22_0.target.isBlock then
		if var_22_1 > 0 then
			if arg_22_0.up then
				var_22_0.y = var_22_0.y + 1
			end

			if arg_22_0.down then
				var_22_0.y = var_22_0.y - 1
			end

			var_22_0.y = var_22_0.y * arg_22_0.singleHeight / RacingMiniGameConfig.Y_COVER_TIME * (arg_22_0.target.isVertigo and RacingMiniGameConfig.Y_OBSTACLE_REDUCE or 1) * arg_22_1

			if arg_22_0.target.state == "base" and arg_22_0.boost then
				arg_22_0.target:Show("accel")
			end
		elseif not arg_22_0.target.isVertigo and arg_22_0.target.state ~= "base" then
			arg_22_0.target:Show("base")
		end
	end

	arg_22_0.target:UpdatePos(var_22_0 * NewPos(0, 1), arg_22_0.singleHeight)
	setParent(arg_22_0.target.rt, arg_22_0.rtMainContent:Find(math.clamp(math.floor((arg_22_0.target.pos.y + arg_22_0.singleHeight) * 3 / 2 / arg_22_0.singleHeight) - 1, -1, 1) - 1))

	local var_22_2 = 1

	while var_22_2 <= #arg_22_0.queue do
		local var_22_3 = arg_22_0.queue[var_22_2]

		var_22_3:UpdatePos(var_22_0 * NewPos(-1, 0))

		if not var_22_3.isTriggered and var_22_3.colliderSize and var_0_3(var_22_3, arg_22_0.target) then
			var_22_3:Trigger(arg_22_0.target)
		end

		if var_22_3.pos.x < -arg_22_0.bgSingleSize then
			var_22_3:Clear()
		else
			var_22_2 = var_22_2 + 1
		end
	end

	local var_22_4 = arg_22_0.rtBgContent.anchoredPosition.x - var_22_0.x

	if var_22_4 < -arg_22_0.bgSingleSize / 2 then
		var_22_4 = var_22_4 + arg_22_0.bgSingleSize
	end

	setAnchoredPosition(arg_22_0.rtBgContent, {
		x = var_22_4
	})

	arg_22_0.chargeDis = arg_22_0.chargeDis - var_22_0.x

	if arg_22_0.chargeDis <= 0 then
		arg_22_0:CreateNewObject()
	end

	arg_22_0.disCount = arg_22_0.disCount + var_22_0.x

	arg_22_0:UpdateDisplay()
end

function var_0_0.UpdateDisplay(arg_23_0)
	local var_23_0 = arg_23_0.timeAll - arg_23_0.timeCount

	setText(arg_23_0.rtTime:Find("Text"), string.format("%02d:%02ds", math.floor(var_23_0), math.floor((var_23_0 - math.floor(var_23_0)) * 100)))

	local var_23_1 = arg_23_0.disCount / 20

	setText(arg_23_0.rtDis, string.format("%.2fm", var_23_1 - var_23_1 % 0.01))

	local var_23_2 = RacingMiniGameConfig.BUOY_POWER_LIST
	local var_23_3 = RacingMiniGameConfig.BUOY_POS_LIST
	local var_23_4

	for iter_23_0, iter_23_1 in ipairs(var_23_2) do
		if iter_23_1 >= arg_23_0.enginePower then
			var_23_4 = iter_23_0

			break
		end
	end

	setAnchoredPosition(arg_23_0.rtPower:Find("range/buoy"), {
		x = var_23_4 > 1 and var_23_3[var_23_4 - 1] + (arg_23_0.enginePower - var_23_2[var_23_4 - 1]) / (var_23_2[var_23_4] - var_23_2[var_23_4 - 1]) * (var_23_3[var_23_4] - var_23_3[var_23_4 - 1]) or 0
	})

	if arg_23_0.target.isVertigo then
		var_23_4 = 1
	end

	for iter_23_2, iter_23_3 in ipairs(arg_23_0.target.effectList) do
		setActive(iter_23_3, var_23_4 - 1 == iter_23_2)
	end

	local var_23_5 = RacingMiniGameConfig.FRIEND_DIS_LIST

	arg_23_0.friendIndex = defaultValue(arg_23_0.friendIndex, 1)

	while arg_23_0.friendIndex < #var_23_5 and var_23_5[arg_23_0.friendIndex + 1] < arg_23_0.disCount / 20 do
		arg_23_0.friendIndex = arg_23_0.friendIndex + 1
		arg_23_0.friendDirty = true
	end

	if arg_23_0.friendDirty then
		arg_23_0.friendDirty = false

		while #arg_23_0.rankData > 0 and arg_23_0.rankData[1].score / 100 < var_23_5[arg_23_0.friendIndex] do
			table.remove(arg_23_0.rankData, 1)
		end

		local var_23_6

		for iter_23_4, iter_23_5 in ipairs(arg_23_0.rankData) do
			if arg_23_0.friendIndex == #var_23_5 or iter_23_5.score / 100 < var_23_5[arg_23_0.friendIndex + 1] then
				var_23_6 = iter_23_4
			else
				break
			end
		end

		setActive(arg_23_0.rtFriend, var_23_6)

		if var_23_6 then
			arg_23_0.friendInfo = arg_23_0.rankData[math.random(var_23_6)]
		else
			arg_23_0.friendInfo = nil
		end

		if arg_23_0.friendInfo then
			setText(arg_23_0.rtFriend:Find("Text"), arg_23_0.friendInfo.name)
			setText(arg_23_0.rtFriend:Find("point"), string.format("%.2fm", arg_23_0.friendInfo.score / 100))
		end
	end
end

local var_0_4 = {
	TrafficCone = "roadblocks",
	Mire = "mire",
	Roadblock = "roadblocks",
	SpeedBumps = "speed_bumps",
	Bomb = "roadblocks",
	MoreTime = "more_time",
	Invincibility = "invincibility"
}

function var_0_0.CreateNewObject(arg_24_0)
	local var_24_0

	for iter_24_0, iter_24_1 in ipairs(RacingMiniGameConfig.FIELD_CONFIG) do
		if arg_24_0.timeCount < iter_24_1.time then
			break
		else
			var_24_0 = iter_24_1
		end
	end

	local var_24_1 = {}
	local var_24_2 = 0

	for iter_24_2 = -1, 1 do
		arg_24_0.rateDic[iter_24_2] = defaultValue(arg_24_0.rateDic[iter_24_2], 0)

		local var_24_3 = math.random() / (2 - iter_24_2)
		local var_24_4

		if var_24_3 < arg_24_0.rateDic[iter_24_2] then
			var_24_2 = var_24_2 + 1
			var_24_1[iter_24_2] = true
		else
			var_24_1[iter_24_2] = false
		end
	end

	if var_24_2 == 3 then
		var_24_1[math.random(3) - 2] = false
	end

	for iter_24_3 = -1, 1 do
		if var_24_1[iter_24_3] then
			classCfg = var_24_0.obstacle_distribution
		else
			classCfg = var_24_0.item_distribution
		end

		rate = math.random()

		local var_24_5 = 0
		local var_24_6 = 0

		for iter_24_4, iter_24_5 in ipairs(classCfg) do
			var_24_6 = var_24_6 + iter_24_5[2]
		end

		local var_24_7

		for iter_24_6, iter_24_7 in ipairs(classCfg) do
			var_24_5 = var_24_5 + iter_24_7[2]

			if var_24_5 > rate * var_24_6 then
				var_24_7 = iter_24_7[1]

				break
			end
		end

		if var_24_7 and superof(RacingMiniNameSpace[var_24_7], RacingMiniNameSpace.Item) then
			if defaultValue(arg_24_0.itemCountDic[var_24_7], 0) < defaultValue(var_24_0.item_create_limit[var_24_7], 0) then
				arg_24_0.itemCountDic[var_24_7] = defaultValue(arg_24_0.itemCountDic[var_24_7], 0) + 1
			else
				var_24_7 = nil
			end
		end

		if var_24_7 then
			local var_24_8 = RacingMiniNameSpace[var_24_7].New(cloneTplTo(arg_24_0.rtRes:Find(var_0_4[var_24_7]), arg_24_0.rtMainContent:Find(iter_24_3)), NewPos(arg_24_0.bgSingleSize * 1.5 + arg_24_0.chargeDis, iter_24_3 * arg_24_0.singleHeight), arg_24_0)

			table.insert(arg_24_0.queue, var_24_8)

			arg_24_0.rateDic[iter_24_3] = arg_24_0.rateDic[iter_24_3] * var_24_0.continue_reduce
		else
			arg_24_0.rateDic[iter_24_3] = arg_24_0.rateDic[iter_24_3] + var_24_0.bye_plus
		end
	end

	arg_24_0.chargeDis = arg_24_0.chargeDis + var_24_0.recharge_dis
end

function var_0_0.GetSpeed(arg_25_0, arg_25_1)
	local var_25_0
	local var_25_1 = RacingMiniGameConfig.M_LIST
	local var_25_2 = RacingMiniGameConfig.S_LIST

	for iter_25_0 = 1, #var_25_1 - 1 do
		if var_25_1[iter_25_0 + 1] > arg_25_0.enginePower then
			var_25_0 = var_25_2[iter_25_0] + (arg_25_0.enginePower - var_25_1[iter_25_0]) / (var_25_1[iter_25_0 + 1] - var_25_1[iter_25_0]) * (var_25_2[iter_25_0 + 1] - var_25_2[iter_25_0])

			break
		end
	end

	var_25_0 = var_25_0 or var_25_2[#var_25_2]
	arg_25_0.enginePower = math.clamp(arg_25_0.enginePower + arg_25_1, var_25_1[1], var_25_1[#var_25_1])

	return var_25_0 * 10
end

function var_0_0.AddTime(arg_26_0, arg_26_1)
	arg_26_0.timeAll = arg_26_0.timeAll + arg_26_1

	setActive(arg_26_0.rtTime:Find("Text/plus"), true)
end

function var_0_0.SetEnginePower(arg_27_0, arg_27_1)
	arg_27_0.enginePower = math.min(arg_27_0.enginePower, arg_27_1)
end

function var_0_0.willExit(arg_28_0)
	if arg_28_0.handle then
		UpdateBeat:RemoveListener(arg_28_0.handle)
	end
end

return var_0_0
