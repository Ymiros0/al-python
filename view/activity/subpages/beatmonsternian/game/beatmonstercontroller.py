local var_0_0 = class("BeatMonsterController")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.mediator = BeatMonsterMeidator.New(arg_1_0)
	arg_1_0.model = BeatMonsterModel.New(arg_1_0)

def var_0_0.SetUp(arg_2_0, arg_2_1, arg_2_2):
	seriesAsync({
		function(arg_3_0)
			arg_2_0.OnDisenabelUIEvent = arg_2_2

			arg_2_0.InitStage(arg_2_1)

			local var_3_0 = arg_2_0.model.GetPlayableStory()

			if not var_3_0:
				arg_3_0()

				return

			arg_2_0.mediator.PlayStory(var_3_0, arg_3_0),
		function(arg_4_0)
			if arg_2_1.hp > 0:
				arg_2_0.mediator.DoCurtainUp(arg_4_0)
			else
				arg_4_0(),
		function(arg_5_0)
			arg_2_0.mediator.OnInited()
	})

def var_0_0.NetData(arg_6_0, arg_6_1):
	arg_6_0.model.UpdateData(arg_6_1)
	arg_6_0.mediator.OnMonsterHpUpdate(arg_6_0.model.mosterNian.hp)
	arg_6_0.mediator.OnAttackCntUpdate(arg_6_0.model.attackCnt, arg_6_0.isFake or arg_6_0.model.mosterNian.hp <= 0)

def var_0_0.InitStage(arg_7_0, arg_7_1):
	arg_7_0.model.AddMonsterNian(arg_7_1.hp, arg_7_1.maxHp)
	arg_7_0.model.AddFuShun()

	local var_7_0 = arg_7_0.model.mosterNian.hp
	local var_7_1 = arg_7_0.model.mosterNian.maxHp

	arg_7_0.mediator.OnAddMonsterNian(var_7_0, var_7_1)
	arg_7_0.mediator.OnAddFuShun(var_7_0)
	arg_7_0.model.SetAttackCnt(arg_7_1.leftCount)
	arg_7_0.mediator.OnAttackCntUpdate(arg_7_0.model.attackCnt, arg_7_0.isFake or arg_7_0.model.mosterNian.hp <= 0)
	arg_7_0.model.SetStorys(arg_7_1.storys)

def var_0_0.Input(arg_8_0, arg_8_1):
	if arg_8_0.isOnAction:
		return

	arg_8_0.RemoveInputTimer()
	arg_8_0.UpdateActionStr(arg_8_1)

	local var_8_0 = arg_8_0.model.IsMatchAction()
	local var_8_1 = var_8_0 and 0.5 or BeatMonsterNianConst.INPUT_TIME

	if var_8_0:
		arg_8_0.OnDisenabelUIEvent(True)

		arg_8_0.isOnAction = True

	arg_8_0.inputTimer = Timer.New(function()
		local var_9_0 = arg_8_0.model.GetMatchAction()
		local var_9_1 = arg_8_0.model.GetMonsterAction()

		arg_8_0.UpdateActionStr("")

		if var_8_0:
			arg_8_0.StartAction(var_9_0, var_9_1), var_8_1, 1)

	arg_8_0.inputTimer.Start()

def var_0_0.StartAction(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0.RemoveAnimationTimer()

	local var_10_0

	seriesAsync({
		function(arg_11_0)
			arg_10_0.SendRequestToServer(function(arg_12_0)
				var_10_0 = arg_12_0

				arg_11_0()),
		function(arg_13_0)
			arg_10_0.mediator.OnChangeFuShunAction(arg_10_1)
			arg_10_0.mediator.OnChangeNianAction(arg_10_2)

			arg_10_0.animationTimer = Timer.New(arg_13_0, 2, 1)

			arg_10_0.animationTimer.Start(),
		function(arg_14_0)
			local var_14_0 = arg_10_0.model.mosterNian.hp
			local var_14_1 = arg_10_0.model.mosterNian.maxHp

			arg_10_0.mediator.OnUIHpUpdate(var_14_0, var_14_1, arg_14_0),
		function(arg_15_0)
			local var_15_0 = arg_10_0.model.GetPlayableStory()

			if not var_15_0:
				arg_15_0()

				return

			arg_10_0.mediator.PlayStory(var_15_0, arg_15_0),
		function(arg_16_0)
			if not var_10_0 or #var_10_0 == 0:
				arg_16_0()

				return

			arg_10_0.mediator.DisplayAwards(var_10_0, arg_16_0),
		function(arg_17_0)
			arg_10_0.isOnAction = False

			arg_10_0.OnDisenabelUIEvent(False)
	})

def var_0_0.SendRequestToServer(arg_18_0, arg_18_1):
	if arg_18_0.isFake:
		arg_18_0.NetData({
			hp = arg_18_0.model.RandomDamage(),
			maxHp = arg_18_0.model.GetMonsterMaxHp(),
			leftCount = arg_18_0.model.GetAttackCount() - 1,
			storys = {}
		})
		arg_18_1()
	else
		pg.m02.sendNotification(GAME.ACT_BEAT_MONSTER_NIAN, {
			cmd = 1,
			activity_id = ActivityConst.BEAT_MONSTER_NIAN_2020,
			callback = arg_18_1
		})

def var_0_0.UpdateActionStr(arg_19_0, arg_19_1):
	arg_19_0.model.UpdateActionStr(arg_19_1)

	local var_19_0 = arg_19_0.model.GetActionStr()

	arg_19_0.mediator.OnInputChange(var_19_0)

def var_0_0.RemoveInputTimer(arg_20_0):
	if arg_20_0.inputTimer:
		arg_20_0.inputTimer.Stop()

		arg_20_0.inputTimer = None

def var_0_0.RemoveAnimationTimer(arg_21_0):
	if arg_21_0.animationTimer:
		arg_21_0.animationTimer.Stop()

		arg_21_0.animationTimer = None

def var_0_0.ReStartGame(arg_22_0):
	arg_22_0.isFake = True

	arg_22_0.NetData({
		hp = 10,
		leftCount = 10,
		maxHp = 10,
		storys = {}
	})
	arg_22_0.mediator.OnUIHpUpdate(10, 10)

def var_0_0.Dispose(arg_23_0):
	arg_23_0.RemoveAnimationTimer()
	arg_23_0.RemoveInputTimer()
	arg_23_0.mediator.Dispose()
	arg_23_0.model.Dispose()

	arg_23_0.OnDisenabelUIEvent = None

return var_0_0
