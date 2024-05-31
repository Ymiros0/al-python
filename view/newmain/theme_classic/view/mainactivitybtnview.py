local var_0_0 = class("MainActivityBtnView", import("...base.MainBaseView"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.initPos = None
	arg_1_0.isInit = None
	arg_1_0.actBtnTpl = arg_1_1.Find("actBtn")
	arg_1_0.linkBtnTopFoldableHelper = MainFoldableHelper.New(arg_1_0._tf.parent.Find("link_top"), Vector2(0, 1))
	arg_1_0.checkNotchRatio = NotchAdapt.CheckNotchRatio

	arg_1_0.InitBtns()
	arg_1_0.Register()

def var_0_0.InitBtns(arg_2_0):
	arg_2_0.activityBtns = {
		MainActSummaryBtn.New(arg_2_0.actBtnTpl, arg_2_0.event, True),
		MainActEscortBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActMapBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActBossBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActBackHillBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActAtelierBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainLanternFestivalBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActBossRushBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActAprilFoolBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActMedalCollectionBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActSenranBtn.New(arg_2_0.actBtnTpl, arg_2_0.event),
		MainActBossSingleBtn.New(tpl, event)
	}
	arg_2_0.specailBtns = {
		MainActInsBtn.New(arg_2_0._tf, arg_2_0.event),
		MainActTraingCampBtn.New(arg_2_0._tf, arg_2_0.event),
		MainActRefluxBtn.New(arg_2_0._tf, arg_2_0.event),
		MainActNewServerBtn.New(arg_2_0._tf, arg_2_0.event),
		MainActDelegationBtn.New(arg_2_0._tf, arg_2_0.event),
		MainIslandActDelegationBtn.New(arg_2_0._tf, arg_2_0.event),
		MainVoteEntranceBtn.New(arg_2_0._tf, arg_2_0.event)
	}

	if pg.SdkMgr.GetInstance().CheckAudit():
		arg_2_0.specailBtns = {
			MainActTraingCampBtn.New(arg_2_0._tf, arg_2_0.event)
		}

def var_0_0.Register(arg_3_0):
	arg_3_0.bind(GAME.REMOVE_LAYERS, function(arg_4_0, arg_4_1)
		arg_3_0.OnRemoveLayer(arg_4_1.context))
	arg_3_0.bind(MiniGameProxy.ON_HUB_DATA_UPDATE, function(arg_5_0)
		arg_3_0.Refresh())
	arg_3_0.bind(GAME.SEND_MINI_GAME_OP_DONE, function(arg_6_0)
		arg_3_0.Refresh())
	arg_3_0.bind(GAME.GET_FEAST_DATA_DONE, function(arg_7_0)
		arg_3_0.Refresh())
	arg_3_0.bind(GAME.FETCH_VOTE_INFO_DONE, function(arg_8_0)
		arg_3_0.Refresh())
	arg_3_0.bind(GAME.ZERO_HOUR_OP_DONE, function(arg_9_0)
		arg_3_0.Refresh())

def var_0_0.GetBtn(arg_10_0, arg_10_1):
	for iter_10_0, iter_10_1 in ipairs(arg_10_0.activityBtns):
		if isa(iter_10_1, arg_10_1):
			return iter_10_1

	for iter_10_2, iter_10_3 in ipairs(arg_10_0.specailBtns):
		if isa(iter_10_3, arg_10_1):
			return iter_10_3

	return None

def var_0_0.OnRemoveLayer(arg_11_0, arg_11_1):
	local var_11_0

	if arg_11_1.mediator == LotteryMediator:
		var_11_0 = arg_11_0.GetBtn(MainActLotteryBtn)
	elif arg_11_1.mediator == InstagramMediator:
		var_11_0 = arg_11_0.GetBtn(MainActInsBtn)

	if var_11_0 and var_11_0.InShowTime():
		var_11_0.OnInit()

def var_0_0.Init(arg_12_0):
	arg_12_0.Flush()

	arg_12_0.isInit = True

def var_0_0.FilterActivityBtns(arg_13_0):
	local var_13_0 = {}
	local var_13_1 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.activityBtns):
		if iter_13_1.InShowTime():
			table.insert(var_13_0, iter_13_1)
		else
			table.insert(var_13_1, iter_13_1)

	table.sort(var_13_0, function(arg_14_0, arg_14_1)
		return arg_14_0.config.group_id < arg_14_1.config.group_id)

	return var_13_0, var_13_1

def var_0_0.FilterSpActivityBtns(arg_15_0):
	local var_15_0 = {}
	local var_15_1 = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.specailBtns):
		if iter_15_1.InShowTime():
			table.insert(var_15_0, iter_15_1)
		else
			table.insert(var_15_1, iter_15_1)

	return var_15_0, var_15_1

def var_0_0.Flush(arg_16_0):
	if arg_16_0.checkNotchRatio != NotchAdapt.CheckNotchRatio:
		arg_16_0.checkNotchRatio = NotchAdapt.CheckNotchRatio
		arg_16_0.initPos = None

	local var_16_0, var_16_1 = arg_16_0.FilterActivityBtns()

	for iter_16_0, iter_16_1 in ipairs(var_16_0):
		iter_16_1.Init(iter_16_0)

	for iter_16_2, iter_16_3 in ipairs(var_16_1):
		iter_16_3.Clear()

	local var_16_2 = #var_16_0

	assert(var_16_2 <= 4, "活动按钮不能超过4个")

	local var_16_3 = var_16_2 <= 3
	local var_16_4 = var_16_3 and 1 or 0.85
	local var_16_5 = var_16_3 and 390 or 420

	arg_16_0._tf.localScale = Vector3(var_16_4, var_16_4, 1)
	arg_16_0.initPos = arg_16_0.initPos or arg_16_0._tf.localPosition
	arg_16_0._tf.localPosition = Vector3(arg_16_0.initPos.x, var_16_5, 0)

	local var_16_6, var_16_7 = arg_16_0.FilterSpActivityBtns()

	for iter_16_4, iter_16_5 in pairs(var_16_6):
		iter_16_5.Init(not var_16_3)

	for iter_16_6, iter_16_7 in pairs(var_16_7):
		iter_16_7.Clear()

def var_0_0.Refresh(arg_17_0):
	if not arg_17_0.isInit:
		return

	arg_17_0.Flush()

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.specailBtns):
		if iter_17_1.InShowTime():
			iter_17_1.Refresh()

def var_0_0.Disable(arg_18_0):
	for iter_18_0, iter_18_1 in ipairs(arg_18_0.specailBtns):
		if iter_18_1.InShowTime():
			iter_18_1.Disable()

def var_0_0.Dispose(arg_19_0):
	var_0_0.super.Dispose(arg_19_0)
	arg_19_0.linkBtnTopFoldableHelper.Dispose()

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.activityBtns):
		iter_19_1.Dispose()

	for iter_19_2, iter_19_3 in ipairs(arg_19_0.specailBtns):
		iter_19_3.Dispose()

	arg_19_0.specailBtns = None
	arg_19_0.activityBtns = None

def var_0_0.Fold(arg_20_0, arg_20_1, arg_20_2):
	var_0_0.super.Fold(arg_20_0, arg_20_1, arg_20_2)
	arg_20_0.linkBtnTopFoldableHelper.Fold(arg_20_1, arg_20_2)

def var_0_0.GetDirection(arg_21_0):
	return Vector2(1, 0)

return var_0_0
