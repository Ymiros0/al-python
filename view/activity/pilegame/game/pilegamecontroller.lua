local var_0_0 = class("PileGameController")

var_0_0.STATE_IDLE = 0
var_0_0.STATE_PREPARE = 1
var_0_0.STATE_START = 2
var_0_0.STATE_DROPING = 3
var_0_0.STATE_STOP_DROP = 4
var_0_0.STATE_SINK = 5
var_0_0.STATE_SINK_DONE = 6
var_0_0.STATE_STOP_SHAKE = 7
var_0_0.STATE_END = 8
var_0_0.STATE_EXIT = 9
var_0_0.DROP_AREA_SAFE = 1
var_0_0.DROP_AREA_WARN = 2
var_0_0.DROP_AREA_DANGER = 3

function var_0_0.Ctor(arg_1_0)
	arg_1_0.model = PileGameModel.New(arg_1_0)
	arg_1_0.view = PileGameView.New(arg_1_0)
	arg_1_0.state = var_0_0.STATE_IDLE
	arg_1_0.locked = false
	arg_1_0.time = 0
	arg_1_0.shakePositions = {}
end

function var_0_0.SetUp(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.model:NetData(arg_2_1)
	arg_2_0.view:OnEnterGame(arg_2_1)

	arg_2_0.gameEndCb = arg_2_2
end

function var_0_0.StartGame(arg_3_0)
	seriesAsync({
		function(arg_4_0)
			arg_3_0.locked = false

			arg_3_0:OnInitGame()
			arg_3_0.view:DoCurtain(arg_4_0)

			if arg_3_0.gameStateCallback then
				arg_3_0.gameStateCallback(false)
			end
		end,
		function(arg_5_0)
			arg_3_0:OnPrepare(arg_5_0)
		end,
		function(arg_6_0)
			arg_3_0.state = var_0_0.STATE_PREPARE

			arg_3_0.view:OnGameStart()
		end
	})
end

function var_0_0.setGameStartCallback(arg_7_0, arg_7_1)
	arg_7_0.gameStateCallback = arg_7_1
end

function var_0_0.ExitGame(arg_8_0)
	arg_8_0.locked = false
	arg_8_0.shakePositions = {}
	arg_8_0.state = var_0_0.STATE_EXIT

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.model.items) do
		arg_8_0.view:OnRemovePile(iter_8_1)
	end

	if arg_8_0.gameStateCallback then
		arg_8_0.gameStateCallback(true)
	end

	arg_8_0.model:Clear()
	arg_8_0.view:OnGameExited()
end

function var_0_0.Drop(arg_9_0)
	if arg_9_0.state == var_0_0.STATE_START and not arg_9_0.locked then
		arg_9_0.state = var_0_0.STATE_DROPING

		arg_9_0:OnStartDrop()
	end
end

function var_0_0.OnInitGame(arg_10_0)
	if not arg_10_0.handle then
		arg_10_0.handle = UpdateBeat:CreateListener(arg_10_0.Update, arg_10_0)
	end

	UpdateBeat:AddListener(arg_10_0.handle)
	arg_10_0.model:AddDeathLineRight()
	arg_10_0.model:AddDeathLineLeft()
	arg_10_0.model:AddSafeLineRight()
	arg_10_0.model:AddSafeLineLeft()
	arg_10_0.model:AddGround()
	arg_10_0.view:InitSup(arg_10_0.model)
end

function var_0_0.OnPrepare(arg_11_0, arg_11_1)
	seriesAsync({
		function(arg_12_0)
			arg_11_0.view:UpdateScore(arg_11_0.model.score)
			arg_11_0.view:UpdateFailedCnt(arg_11_0.model.maxFailedCnt, arg_11_0.model.failedCnt)
			arg_12_0()
		end,
		function(arg_13_0)
			arg_11_0.item = arg_11_0.model:AddHeadPile()
			arg_11_0.item.position = Vector3(0, -arg_11_0.model.screen.y / 2, 0)

			arg_11_0.view:AddPile(arg_11_0.item, true, function()
				arg_11_0.view:OnItemPositionChange(arg_11_0.item)
				arg_13_0()
			end)
		end,
		function(arg_15_0)
			local var_15_0 = arg_11_0.item

			arg_11_0.item = arg_11_0.model:AddPileByRandom()
			arg_11_0.item.position = Vector3(0, -arg_11_0.model.screen.y / 2 + var_15_0.sizeDelta.y, 0)

			arg_11_0.view:AddPile(arg_11_0.item, false, function()
				arg_11_0.view:OnItemPositionChange(arg_11_0.item)
				arg_15_0()
			end)
		end
	}, arg_11_1)
end

function var_0_0.OnStartGame(arg_17_0, arg_17_1)
	local function var_17_0()
		arg_17_0.state = var_0_0.STATE_SINK_DONE
		arg_17_0.item = arg_17_0.model:AddPileByRandom()

		arg_17_0.view:AddPile(arg_17_0.item, false, function()
			arg_17_0.state = var_0_0.STATE_START
		end)
	end

	if arg_17_0.model:ShouldSink() then
		arg_17_0.state = var_0_0.STATE_SINK

		arg_17_0:DoSink(var_17_0)
	else
		var_17_0()
	end

	arg_17_0:RemoveLockTimer()

	if arg_17_1 then
		arg_17_0.locked = true
		arg_17_0.lockTimer = Timer.New(function()
			arg_17_0.locked = false
		end, PileGameConst.BAN_OP_TIME, 1)

		arg_17_0.lockTimer:Start()
	end
end

function var_0_0.RemoveLockTimer(arg_21_0)
	if arg_21_0.lockTimer then
		arg_21_0.lockTimer:Stop()

		arg_21_0.lockTimer = nil
	end
end

function var_0_0.OnEndGame(arg_22_0, arg_22_1)
	arg_22_0.state = var_0_0.STATE_END
	arg_22_0.time = 0
	arg_22_0.shakePositions = {}
	arg_22_0.locked = false

	local function var_22_0()
		arg_22_0.view:OnGameEnd(arg_22_0.model.score, arg_22_0.model.highestScore)

		if arg_22_0.model.score > arg_22_0.model.highestScore then
			arg_22_0.model:UpdateHighestScore()
		end

		arg_22_0.model.score = 0
	end

	if arg_22_0.gameEndCb then
		arg_22_0.gameEndCb(arg_22_0.model.score, arg_22_0.model.highestScore)
	end

	if arg_22_1 then
		local var_22_1 = arg_22_0.model:GetFirstItem().position.x
		local var_22_2 = arg_22_0.item.position.x > 0 and 1 or 0

		arg_22_0.view:OnCollapse(var_22_1, var_22_2, var_22_0)
	else
		var_22_0()
	end
end

function var_0_0.Update(arg_24_0)
	if arg_24_0.state == var_0_0.STATE_PREPARE then
		arg_24_0:OnStartGame()
	elseif arg_24_0.state == var_0_0.STATE_START then
		arg_24_0:Shuffling()
	elseif arg_24_0.state == var_0_0.STATE_DROPING then
		arg_24_0:Droping()
	elseif arg_24_0.state == var_0_0.STATE_STOP_DROP then
		arg_24_0:CheckCollide()
	end

	if #arg_24_0.shakePositions > 0 then
		arg_24_0:DoShake()
	end

	if arg_24_0.state >= var_0_0.STATE_START and arg_24_0.state < var_0_0.STATE_END then
		if arg_24_0.time >= PileGameConst.PLAY_SPE_ACTION_TIME then
			arg_24_0:PlaySpeAction()

			arg_24_0.time = 0
		end

		arg_24_0.time = arg_24_0.time + Time.deltaTime
	end
end

function var_0_0.PlaySpeAction(arg_25_0)
	for iter_25_0, iter_25_1 in pairs(arg_25_0.model.items) do
		if iter_25_1 ~= arg_25_0.item then
			arg_25_0.view:PlaySpeAction(iter_25_1)
		end
	end
end

function var_0_0.StopShake(arg_26_0)
	for iter_26_0, iter_26_1 in ipairs(arg_26_0.shakePositions) do
		iter_26_1[1].onTheMove = false
	end

	arg_26_0.shakePositions = {}
end

function var_0_0.CheckRock(arg_27_0)
	local var_27_0 = arg_27_0.model:GetTailItem()

	if arg_27_0.model:GetDropArea(var_27_0) == var_0_0.DROP_AREA_WARN then
		arg_27_0.shakePositions = arg_27_0.model:GetInitPos()
	end
end

function var_0_0.DoShake(arg_28_0)
	local var_28_0 = Time.deltaTime * PileGameConst.SHAKE_SPEED
	local var_28_1 = arg_28_0.shakePositions[1][1].position

	for iter_28_0, iter_28_1 in ipairs(arg_28_0.shakePositions) do
		local var_28_2 = iter_28_1[1]
		local var_28_3 = iter_28_1[2]
		local var_28_4 = iter_28_1[3]
		local var_28_5 = Vector3(var_28_3, var_28_2.position.y, 0)
		local var_28_6 = Vector3(var_28_4, var_28_2.position.y, 0)

		if var_28_2.onTheMove == true then
			var_28_2.position = Vector3.MoveTowards(var_28_2.position, var_28_5, var_28_0)
		else
			var_28_2.position = Vector3.MoveTowards(var_28_2.position, var_28_6, var_28_0)
		end

		if var_28_2.position.x == var_28_6.x and var_28_2.onTheMove == false then
			var_28_2.onTheMove = true
		elseif var_28_2.position.x == var_28_5.x and var_28_2.onTheMove == true then
			var_28_2.onTheMove = false
		end

		arg_28_0.view:OnItemPositionChange(var_28_2)
	end

	local var_28_7 = arg_28_0.shakePositions[1][1].position

	if var_28_7.x ~= var_28_1.x then
		arg_28_0.view:OnShake(var_28_7.x - var_28_1.x)
	end
end

function var_0_0.DoSink(arg_29_0, arg_29_1)
	local var_29_0 = {}

	for iter_29_0 = 1, #arg_29_0.model.items do
		table.insert(var_29_0, function(arg_30_0)
			local var_30_0

			var_30_0.position, var_30_0 = arg_29_0.model:GetNextPos(iter_29_0), arg_29_0.model.items[iter_29_0]

			arg_29_0.view:OnItemPositionChangeWithAnim(var_30_0, arg_30_0)
		end)
	end

	parallelAsync({
		function(arg_31_0)
			seriesAsync(var_29_0, arg_31_0)
		end,
		function(arg_32_0)
			local var_32_0 = arg_29_0.model:GetFirstItem()

			arg_29_0.view:DoSink(var_32_0.sizeDelta.y, arg_32_0)
		end
	}, function()
		local var_33_0 = arg_29_0.model:RemoveFirstItem()

		arg_29_0.view:OnRemovePile(var_33_0)
		arg_29_1()
	end)
end

function var_0_0.Shuffling(arg_34_0)
	local var_34_0 = Time.deltaTime * arg_34_0.item.speed
	local var_34_1 = arg_34_0.item.leftMaxPosition
	local var_34_2 = arg_34_0.item.rightMaxPosition

	if arg_34_0.item.onTheMove == false then
		arg_34_0.item.position = Vector3.MoveTowards(arg_34_0.item.position, var_34_2, var_34_0)
	else
		arg_34_0.item.position = Vector3.MoveTowards(arg_34_0.item.position, var_34_1, var_34_0)
	end

	if arg_34_0.item.position.x == var_34_2.x and arg_34_0.item.onTheMove == false then
		arg_34_0.item.onTheMove = true
	elseif arg_34_0.item.position.x == var_34_1.x and arg_34_0.item.onTheMove == true then
		arg_34_0.item.onTheMove = false
	end

	arg_34_0.view:OnItemPositionChange(arg_34_0.item)
	arg_34_0.view:OnItemIndexPositionChange(arg_34_0.item)
end

function var_0_0.OnStartDrop(arg_35_0)
	local var_35_0 = arg_35_0.model:GetDropArea(arg_35_0.item)

	if var_35_0 then
		local var_35_1 = arg_35_0.model:CanDropOnPrev(arg_35_0.item)

		arg_35_0.view:OnStartDrop(arg_35_0.item, var_35_0, var_35_1)
	end
end

function var_0_0.Droping(arg_36_0)
	local var_36_0 = Time.deltaTime * arg_36_0.item.dropSpeed

	arg_36_0.item.onTheMove = false

	local var_36_1 = arg_36_0.model.ground.position.y - 100
	local var_36_2 = Vector3(arg_36_0.item.position.x, var_36_1, 0)

	arg_36_0.item.position = Vector3.MoveTowards(arg_36_0.item.position, var_36_2, var_36_0)

	arg_36_0.view:OnItemPositionChange(arg_36_0.item)

	if arg_36_0.model:IsOverTailItem(arg_36_0.item) and #arg_36_0.shakePositions > 0 then
		arg_36_0:StopShake()
	end

	if arg_36_0.model:IsStopDrop(arg_36_0.item) then
		arg_36_0.state = var_0_0.STATE_STOP_DROP
	end
end

function var_0_0.CheckCollide(arg_37_0)
	local var_37_0 = arg_37_0.model:IsOnGround(arg_37_0.item)
	local var_37_1 = arg_37_0.model:GetIndex() == 1
	local var_37_2 = arg_37_0.model:IsOverDeathLine(arg_37_0.item)

	if var_37_1 and var_37_0 then
		arg_37_0:OnStartGame(true)
	elseif not var_37_1 and var_37_0 then
		arg_37_0.model:AddFailedCnt()
		arg_37_0.view:UpdateFailedCnt(arg_37_0.model.maxFailedCnt, arg_37_0.model.failedCnt, true, arg_37_0.item)
		arg_37_0.model:RemoveTailItem()
		arg_37_0.view:OnRemovePile(arg_37_0.item)

		if arg_37_0.model:IsMaxfailedCnt() then
			arg_37_0:OnEndGame(false)
		else
			arg_37_0:CheckRock()
			arg_37_0:OnStartGame(true)
		end
	elseif not var_37_0 and var_37_2 then
		arg_37_0:OnEndGame(true)
	elseif not var_37_0 and not var_37_2 then
		arg_37_0.model:AddScore()

		if arg_37_0.model:IsExceedingTheHighestScore() then
			arg_37_0.view:OnExceedingTheHighestScore()
		end

		arg_37_0.view:UpdateScore(arg_37_0.model.score, arg_37_0.item)
		arg_37_0:CheckRock()
		arg_37_0:OnStartGame(true)
	else
		assert(false, "Why is it running here?")
	end
end

function var_0_0.onBackPressed(arg_38_0)
	return arg_38_0.view:onBackPressed()
end

function var_0_0.Dispose(arg_39_0)
	arg_39_0.gameEndCb = nil
	arg_39_0.locked = false

	if arg_39_0.handle then
		UpdateBeat:RemoveListener(arg_39_0.handle)
	end

	arg_39_0:ExitGame()
	arg_39_0.model:Dispose()
	arg_39_0.view:Dispose()
	arg_39_0:RemoveLockTimer()

	arg_39_0.shakePositions = {}
end

return var_0_0
