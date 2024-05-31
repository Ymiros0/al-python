local var_0_0 = class("TowerClimbingController")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.view = TowerClimbingView.New(arg_1_0)

def var_0_0.SetCallBack(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.OnGameEndCallBack = arg_2_1
	arg_2_0.OnOverMapScore = arg_2_2

def var_0_0.SetUp(arg_3_0, arg_3_1):
	arg_3_0.NetUpdateData(arg_3_1)
	arg_3_0.view.OnEnter()

def var_0_0.NetUpdateData(arg_4_0, arg_4_1):
	arg_4_0.data = arg_4_1

def var_0_0.StartGame(arg_5_0, arg_5_1):
	if arg_5_0.enterGame:
		return

	arg_5_0.enterGame = True

	seriesAsync({
		function(arg_6_0)
			arg_5_0.map = TowerClimbingMapVO.New(arg_5_1, arg_5_0.view)

			arg_5_0.view.OnCreateMap(arg_5_0.map, arg_6_0),
		function(arg_7_0)
			arg_5_0.map.Init(arg_5_0.data, arg_7_0),
		function(arg_8_0)
			arg_5_0.view.DoEnter(arg_8_0)
	}, function()
		arg_5_0.IsStarting = True

		arg_5_0.MainLoop()
		arg_5_0.view.OnStartGame())

def var_0_0.EnterBlock(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_0.map.GetPlayer().IsFatalInjured():
		return

	if arg_10_0.map.GetPlayer().IsDeath():
		return

	if arg_10_1.normal == Vector2.up:
		arg_10_0.map.GetPlayer().UpdateStand(True)

		arg_10_0.level = arg_10_2

		arg_10_0.map.SetCurrentLevel(arg_10_2)

def var_0_0.StayBlock(arg_11_0, arg_11_1, arg_11_2):
	if arg_11_0.map.GetPlayer().IsFatalInjured():
		return

	if arg_11_0.map.GetPlayer().IsDeath():
		return

	if _.any(arg_11_1, function(arg_12_0)
		return arg_12_0.normal == Vector2.up) and not arg_11_0.map.GetPlayer().IsIdle() and arg_11_2 == Vector2(0, 0):
		arg_11_0.map.GetPlayer().Idle()

def var_0_0.ExitBlock(arg_13_0, arg_13_1):
	if arg_13_0.map.GetPlayer().IsFatalInjured():
		return

	if arg_13_0.map.GetPlayer().IsDeath():
		return

	if arg_13_0.level == arg_13_1:
		arg_13_0.map.GetPlayer().UpdateStand(False)

def var_0_0.EnterAttacker(arg_14_0):
	if arg_14_0.map.GetPlayer().IsFatalInjured():
		return

	if arg_14_0.map.GetPlayer().IsDeath():
		return

	arg_14_0.map.GetPlayer().BeInjured()
	arg_14_0.map.GetPlayer().AddInvincibleEffect(TowerClimbingGameSettings.INVINCEIBLE_TIME)

def var_0_0.EnterGround(arg_15_0):
	if arg_15_0.map.GetPlayer().IsFatalInjured():
		return

	if arg_15_0.map.GetPlayer().IsDeath():
		return

	arg_15_0.map.GetPlayer().BeFatalInjured(function()
		if not arg_15_0.map.GetPlayer().IsDeath():
			arg_15_0.map.GetPlayer().AddInvincibleEffect(TowerClimbingGameSettings.INVINCEIBLE_TIME)
			arg_15_0.map.GetPlayer().UpdateStand(True)
			arg_15_0.map.ReBornPlayer()
			arg_15_0.map.GetPlayer().Idle())

	if not arg_15_0.map.GetPlayer().IsDeath():
		arg_15_0.map.SetGroundSleep(TowerClimbingGameSettings.GROUND_SLEEP_TIME)

def var_0_0.OnStickChange(arg_17_0, arg_17_1):
	if arg_17_0.map.GetPlayer().IsFatalInjured():
		return

	if arg_17_1 > 0.05:
		arg_17_0.map.GetPlayer().MoveRight()
	elif arg_17_1 < -0.05:
		arg_17_0.map.GetPlayer().MoveLeft()

def var_0_0.MainLoop(arg_18_0):
	if not arg_18_0.handle:
		arg_18_0.handle = UpdateBeat.CreateListener(arg_18_0.Update, arg_18_0)

	UpdateBeat.AddListener(arg_18_0.handle)

def var_0_0.Update(arg_19_0):
	arg_19_0.view.Update()
	arg_19_0.map.Update()

	if arg_19_0.IsStarting and arg_19_0.map.GetPlayer().IsDeath():
		arg_19_0.EndGame()

def var_0_0.PlayerJump(arg_20_0):
	arg_20_0.map.GetPlayer().Jump()

def var_0_0.PlayerIdle(arg_21_0):
	arg_21_0.map.GetPlayer().Idle()

local function var_0_1(arg_22_0)
	arg_22_0.IsStarting = False

	if arg_22_0.handle:
		UpdateBeat.RemoveListener(arg_22_0.handle)

def var_0_0.EndGame(arg_23_0):
	var_0_1(arg_23_0)

	local var_23_0 = arg_23_0.map.GetPlayer()

	arg_23_0.view.OnEndGame(var_23_0.score, var_23_0.mapScore, arg_23_0.map.id)

	if arg_23_0.OnGameEndCallBack:
		arg_23_0.OnGameEndCallBack(var_23_0.score, var_23_0.higestscore, var_23_0.pageIndex, arg_23_0.map.id)

	if arg_23_0.OnOverMapScore and var_23_0.IsOverMapScore():
		arg_23_0.OnOverMapScore(arg_23_0.map.id, var_23_0.score)

def var_0_0.updateHighScore(arg_24_0, arg_24_1):
	arg_24_0.highScores = arg_24_1

	arg_24_0.view.SetHighScore(arg_24_1)

def var_0_0.ExitGame(arg_25_0):
	var_0_1(arg_25_0)
	arg_25_0.view.OnExitGame()

	if arg_25_0.map:
		arg_25_0.map.Dispose()

		arg_25_0.map = None

	arg_25_0.enterGame = None

def var_0_0.onBackPressed(arg_26_0):
	return arg_26_0.view.onBackPressed()

def var_0_0.Dispose(arg_27_0):
	arg_27_0.ExitGame()
	arg_27_0.view.Dispose()

return var_0_0
