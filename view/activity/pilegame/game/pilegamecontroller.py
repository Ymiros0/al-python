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

def var_0_0.Ctor(arg_1_0):
	arg_1_0.model = PileGameModel.New(arg_1_0)
	arg_1_0.view = PileGameView.New(arg_1_0)
	arg_1_0.state = var_0_0.STATE_IDLE
	arg_1_0.locked = False
	arg_1_0.time = 0
	arg_1_0.shakePositions = {}

def var_0_0.SetUp(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.model.NetData(arg_2_1)
	arg_2_0.view.OnEnterGame(arg_2_1)

	arg_2_0.gameEndCb = arg_2_2

def var_0_0.StartGame(arg_3_0):
	seriesAsync({
		function(arg_4_0)
			arg_3_0.locked = False

			arg_3_0.OnInitGame()
			arg_3_0.view.DoCurtain(arg_4_0)

			if arg_3_0.gameStateCallback:
				arg_3_0.gameStateCallback(False),
		function(arg_5_0)
			arg_3_0.OnPrepare(arg_5_0),
		function(arg_6_0)
			arg_3_0.state = var_0_0.STATE_PREPARE

			arg_3_0.view.OnGameStart()
	})

def var_0_0.setGameStartCallback(arg_7_0, arg_7_1):
	arg_7_0.gameStateCallback = arg_7_1

def var_0_0.ExitGame(arg_8_0):
	arg_8_0.locked = False
	arg_8_0.shakePositions = {}
	arg_8_0.state = var_0_0.STATE_EXIT

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.model.items):
		arg_8_0.view.OnRemovePile(iter_8_1)

	if arg_8_0.gameStateCallback:
		arg_8_0.gameStateCallback(True)

	arg_8_0.model.Clear()
	arg_8_0.view.OnGameExited()

def var_0_0.Drop(arg_9_0):
	if arg_9_0.state == var_0_0.STATE_START and not arg_9_0.locked:
		arg_9_0.state = var_0_0.STATE_DROPING

		arg_9_0.OnStartDrop()

def var_0_0.OnInitGame(arg_10_0):
	if not arg_10_0.handle:
		arg_10_0.handle = UpdateBeat.CreateListener(arg_10_0.Update, arg_10_0)

	UpdateBeat.AddListener(arg_10_0.handle)
	arg_10_0.model.AddDeathLineRight()
	arg_10_0.model.AddDeathLineLeft()
	arg_10_0.model.AddSafeLineRight()
	arg_10_0.model.AddSafeLineLeft()
	arg_10_0.model.AddGround()
	arg_10_0.view.InitSup(arg_10_0.model)

def var_0_0.OnPrepare(arg_11_0, arg_11_1):
	seriesAsync({
		function(arg_12_0)
			arg_11_0.view.UpdateScore(arg_11_0.model.score)
			arg_11_0.view.UpdateFailedCnt(arg_11_0.model.maxFailedCnt, arg_11_0.model.failedCnt)
			arg_12_0(),
		function(arg_13_0)
			arg_11_0.item = arg_11_0.model.AddHeadPile()
			arg_11_0.item.position = Vector3(0, -arg_11_0.model.screen.y / 2, 0)

			arg_11_0.view.AddPile(arg_11_0.item, True, function()
				arg_11_0.view.OnItemPositionChange(arg_11_0.item)
				arg_13_0()),
		function(arg_15_0)
			local var_15_0 = arg_11_0.item

			arg_11_0.item = arg_11_0.model.AddPileByRandom()
			arg_11_0.item.position = Vector3(0, -arg_11_0.model.screen.y / 2 + var_15_0.sizeDelta.y, 0)

			arg_11_0.view.AddPile(arg_11_0.item, False, function()
				arg_11_0.view.OnItemPositionChange(arg_11_0.item)
				arg_15_0())
	}, arg_11_1)

def var_0_0.OnStartGame(arg_17_0, arg_17_1):
	local function var_17_0()
		arg_17_0.state = var_0_0.STATE_SINK_DONE
		arg_17_0.item = arg_17_0.model.AddPileByRandom()

		arg_17_0.view.AddPile(arg_17_0.item, False, function()
			arg_17_0.state = var_0_0.STATE_START)

	if arg_17_0.model.ShouldSink():
		arg_17_0.state = var_0_0.STATE_SINK

		arg_17_0.DoSink(var_17_0)
	else
		var_17_0()

	arg_17_0.RemoveLockTimer()

	if arg_17_1:
		arg_17_0.locked = True
		arg_17_0.lockTimer = Timer.New(function()
			arg_17_0.locked = False, PileGameConst.BAN_OP_TIME, 1)

		arg_17_0.lockTimer.Start()

def var_0_0.RemoveLockTimer(arg_21_0):
	if arg_21_0.lockTimer:
		arg_21_0.lockTimer.Stop()

		arg_21_0.lockTimer = None

def var_0_0.OnEndGame(arg_22_0, arg_22_1):
	arg_22_0.state = var_0_0.STATE_END
	arg_22_0.time = 0
	arg_22_0.shakePositions = {}
	arg_22_0.locked = False

	local function var_22_0()
		arg_22_0.view.OnGameEnd(arg_22_0.model.score, arg_22_0.model.highestScore)

		if arg_22_0.model.score > arg_22_0.model.highestScore:
			arg_22_0.model.UpdateHighestScore()

		arg_22_0.model.score = 0

	if arg_22_0.gameEndCb:
		arg_22_0.gameEndCb(arg_22_0.model.score, arg_22_0.model.highestScore)

	if arg_22_1:
		local var_22_1 = arg_22_0.model.GetFirstItem().position.x
		local var_22_2 = arg_22_0.item.position.x > 0 and 1 or 0

		arg_22_0.view.OnCollapse(var_22_1, var_22_2, var_22_0)
	else
		var_22_0()

def var_0_0.Update(arg_24_0):
	if arg_24_0.state == var_0_0.STATE_PREPARE:
		arg_24_0.OnStartGame()
	elif arg_24_0.state == var_0_0.STATE_START:
		arg_24_0.Shuffling()
	elif arg_24_0.state == var_0_0.STATE_DROPING:
		arg_24_0.Droping()
	elif arg_24_0.state == var_0_0.STATE_STOP_DROP:
		arg_24_0.CheckCollide()

	if #arg_24_0.shakePositions > 0:
		arg_24_0.DoShake()

	if arg_24_0.state >= var_0_0.STATE_START and arg_24_0.state < var_0_0.STATE_END:
		if arg_24_0.time >= PileGameConst.PLAY_SPE_ACTION_TIME:
			arg_24_0.PlaySpeAction()

			arg_24_0.time = 0

		arg_24_0.time = arg_24_0.time + Time.deltaTime

def var_0_0.PlaySpeAction(arg_25_0):
	for iter_25_0, iter_25_1 in pairs(arg_25_0.model.items):
		if iter_25_1 != arg_25_0.item:
			arg_25_0.view.PlaySpeAction(iter_25_1)

def var_0_0.StopShake(arg_26_0):
	for iter_26_0, iter_26_1 in ipairs(arg_26_0.shakePositions):
		iter_26_1[1].onTheMove = False

	arg_26_0.shakePositions = {}

def var_0_0.CheckRock(arg_27_0):
	local var_27_0 = arg_27_0.model.GetTailItem()

	if arg_27_0.model.GetDropArea(var_27_0) == var_0_0.DROP_AREA_WARN:
		arg_27_0.shakePositions = arg_27_0.model.GetInitPos()

def var_0_0.DoShake(arg_28_0):
	local var_28_0 = Time.deltaTime * PileGameConst.SHAKE_SPEED
	local var_28_1 = arg_28_0.shakePositions[1][1].position

	for iter_28_0, iter_28_1 in ipairs(arg_28_0.shakePositions):
		local var_28_2 = iter_28_1[1]
		local var_28_3 = iter_28_1[2]
		local var_28_4 = iter_28_1[3]
		local var_28_5 = Vector3(var_28_3, var_28_2.position.y, 0)
		local var_28_6 = Vector3(var_28_4, var_28_2.position.y, 0)

		if var_28_2.onTheMove == True:
			var_28_2.position = Vector3.MoveTowards(var_28_2.position, var_28_5, var_28_0)
		else
			var_28_2.position = Vector3.MoveTowards(var_28_2.position, var_28_6, var_28_0)

		if var_28_2.position.x == var_28_6.x and var_28_2.onTheMove == False:
			var_28_2.onTheMove = True
		elif var_28_2.position.x == var_28_5.x and var_28_2.onTheMove == True:
			var_28_2.onTheMove = False

		arg_28_0.view.OnItemPositionChange(var_28_2)

	local var_28_7 = arg_28_0.shakePositions[1][1].position

	if var_28_7.x != var_28_1.x:
		arg_28_0.view.OnShake(var_28_7.x - var_28_1.x)

def var_0_0.DoSink(arg_29_0, arg_29_1):
	local var_29_0 = {}

	for iter_29_0 = 1, #arg_29_0.model.items:
		table.insert(var_29_0, function(arg_30_0)
			local var_30_0

			var_30_0.position, var_30_0 = arg_29_0.model.GetNextPos(iter_29_0), arg_29_0.model.items[iter_29_0]

			arg_29_0.view.OnItemPositionChangeWithAnim(var_30_0, arg_30_0))

	parallelAsync({
		function(arg_31_0)
			seriesAsync(var_29_0, arg_31_0),
		function(arg_32_0)
			local var_32_0 = arg_29_0.model.GetFirstItem()

			arg_29_0.view.DoSink(var_32_0.sizeDelta.y, arg_32_0)
	}, function()
		local var_33_0 = arg_29_0.model.RemoveFirstItem()

		arg_29_0.view.OnRemovePile(var_33_0)
		arg_29_1())

def var_0_0.Shuffling(arg_34_0):
	local var_34_0 = Time.deltaTime * arg_34_0.item.speed
	local var_34_1 = arg_34_0.item.leftMaxPosition
	local var_34_2 = arg_34_0.item.rightMaxPosition

	if arg_34_0.item.onTheMove == False:
		arg_34_0.item.position = Vector3.MoveTowards(arg_34_0.item.position, var_34_2, var_34_0)
	else
		arg_34_0.item.position = Vector3.MoveTowards(arg_34_0.item.position, var_34_1, var_34_0)

	if arg_34_0.item.position.x == var_34_2.x and arg_34_0.item.onTheMove == False:
		arg_34_0.item.onTheMove = True
	elif arg_34_0.item.position.x == var_34_1.x and arg_34_0.item.onTheMove == True:
		arg_34_0.item.onTheMove = False

	arg_34_0.view.OnItemPositionChange(arg_34_0.item)
	arg_34_0.view.OnItemIndexPositionChange(arg_34_0.item)

def var_0_0.OnStartDrop(arg_35_0):
	local var_35_0 = arg_35_0.model.GetDropArea(arg_35_0.item)

	if var_35_0:
		local var_35_1 = arg_35_0.model.CanDropOnPrev(arg_35_0.item)

		arg_35_0.view.OnStartDrop(arg_35_0.item, var_35_0, var_35_1)

def var_0_0.Droping(arg_36_0):
	local var_36_0 = Time.deltaTime * arg_36_0.item.dropSpeed

	arg_36_0.item.onTheMove = False

	local var_36_1 = arg_36_0.model.ground.position.y - 100
	local var_36_2 = Vector3(arg_36_0.item.position.x, var_36_1, 0)

	arg_36_0.item.position = Vector3.MoveTowards(arg_36_0.item.position, var_36_2, var_36_0)

	arg_36_0.view.OnItemPositionChange(arg_36_0.item)

	if arg_36_0.model.IsOverTailItem(arg_36_0.item) and #arg_36_0.shakePositions > 0:
		arg_36_0.StopShake()

	if arg_36_0.model.IsStopDrop(arg_36_0.item):
		arg_36_0.state = var_0_0.STATE_STOP_DROP

def var_0_0.CheckCollide(arg_37_0):
	local var_37_0 = arg_37_0.model.IsOnGround(arg_37_0.item)
	local var_37_1 = arg_37_0.model.GetIndex() == 1
	local var_37_2 = arg_37_0.model.IsOverDeathLine(arg_37_0.item)

	if var_37_1 and var_37_0:
		arg_37_0.OnStartGame(True)
	elif not var_37_1 and var_37_0:
		arg_37_0.model.AddFailedCnt()
		arg_37_0.view.UpdateFailedCnt(arg_37_0.model.maxFailedCnt, arg_37_0.model.failedCnt, True, arg_37_0.item)
		arg_37_0.model.RemoveTailItem()
		arg_37_0.view.OnRemovePile(arg_37_0.item)

		if arg_37_0.model.IsMaxfailedCnt():
			arg_37_0.OnEndGame(False)
		else
			arg_37_0.CheckRock()
			arg_37_0.OnStartGame(True)
	elif not var_37_0 and var_37_2:
		arg_37_0.OnEndGame(True)
	elif not var_37_0 and not var_37_2:
		arg_37_0.model.AddScore()

		if arg_37_0.model.IsExceedingTheHighestScore():
			arg_37_0.view.OnExceedingTheHighestScore()

		arg_37_0.view.UpdateScore(arg_37_0.model.score, arg_37_0.item)
		arg_37_0.CheckRock()
		arg_37_0.OnStartGame(True)
	else
		assert(False, "Why is it running here?")

def var_0_0.onBackPressed(arg_38_0):
	return arg_38_0.view.onBackPressed()

def var_0_0.Dispose(arg_39_0):
	arg_39_0.gameEndCb = None
	arg_39_0.locked = False

	if arg_39_0.handle:
		UpdateBeat.RemoveListener(arg_39_0.handle)

	arg_39_0.ExitGame()
	arg_39_0.model.Dispose()
	arg_39_0.view.Dispose()
	arg_39_0.RemoveLockTimer()

	arg_39_0.shakePositions = {}

return var_0_0
