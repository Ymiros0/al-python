local var_0_0 = class("MainActivityBtnView", import("...base.MainBaseView"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.initPos = nil
	arg_1_0.isInit = nil
	arg_1_0.actBtnTpl = arg_1_1:Find("actBtn")
	arg_1_0.linkBtnTopFoldableHelper = MainFoldableHelper.New(arg_1_0._tf.parent:Find("link_top"), Vector2(0, 1))
	arg_1_0.checkNotchRatio = NotchAdapt.CheckNotchRatio

	arg_1_0:InitBtns()
	arg_1_0:Register()
end

function var_0_0.InitBtns(arg_2_0)
	arg_2_0.activityBtns = {
		MainActSummaryBtn.New(arg_2_0.actBtnTpl, arg_2_0.event, true),
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

	if pg.SdkMgr.GetInstance():CheckAudit() then
		arg_2_0.specailBtns = {
			MainActTraingCampBtn.New(arg_2_0._tf, arg_2_0.event)
		}
	end
end

function var_0_0.Register(arg_3_0)
	arg_3_0:bind(GAME.REMOVE_LAYERS, function(arg_4_0, arg_4_1)
		arg_3_0:OnRemoveLayer(arg_4_1.context)
	end)
	arg_3_0:bind(MiniGameProxy.ON_HUB_DATA_UPDATE, function(arg_5_0)
		arg_3_0:Refresh()
	end)
	arg_3_0:bind(GAME.SEND_MINI_GAME_OP_DONE, function(arg_6_0)
		arg_3_0:Refresh()
	end)
	arg_3_0:bind(GAME.GET_FEAST_DATA_DONE, function(arg_7_0)
		arg_3_0:Refresh()
	end)
	arg_3_0:bind(GAME.FETCH_VOTE_INFO_DONE, function(arg_8_0)
		arg_3_0:Refresh()
	end)
	arg_3_0:bind(GAME.ZERO_HOUR_OP_DONE, function(arg_9_0)
		arg_3_0:Refresh()
	end)
end

function var_0_0.GetBtn(arg_10_0, arg_10_1)
	for iter_10_0, iter_10_1 in ipairs(arg_10_0.activityBtns) do
		if isa(iter_10_1, arg_10_1) then
			return iter_10_1
		end
	end

	for iter_10_2, iter_10_3 in ipairs(arg_10_0.specailBtns) do
		if isa(iter_10_3, arg_10_1) then
			return iter_10_3
		end
	end

	return nil
end

function var_0_0.OnRemoveLayer(arg_11_0, arg_11_1)
	local var_11_0

	if arg_11_1.mediator == LotteryMediator then
		var_11_0 = arg_11_0:GetBtn(MainActLotteryBtn)
	elseif arg_11_1.mediator == InstagramMediator then
		var_11_0 = arg_11_0:GetBtn(MainActInsBtn)
	end

	if var_11_0 and var_11_0:InShowTime() then
		var_11_0:OnInit()
	end
end

function var_0_0.Init(arg_12_0)
	arg_12_0:Flush()

	arg_12_0.isInit = true
end

function var_0_0.FilterActivityBtns(arg_13_0)
	local var_13_0 = {}
	local var_13_1 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.activityBtns) do
		if iter_13_1:InShowTime() then
			table.insert(var_13_0, iter_13_1)
		else
			table.insert(var_13_1, iter_13_1)
		end
	end

	table.sort(var_13_0, function(arg_14_0, arg_14_1)
		return arg_14_0.config.group_id < arg_14_1.config.group_id
	end)

	return var_13_0, var_13_1
end

function var_0_0.FilterSpActivityBtns(arg_15_0)
	local var_15_0 = {}
	local var_15_1 = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_0.specailBtns) do
		if iter_15_1:InShowTime() then
			table.insert(var_15_0, iter_15_1)
		else
			table.insert(var_15_1, iter_15_1)
		end
	end

	return var_15_0, var_15_1
end

function var_0_0.Flush(arg_16_0)
	if arg_16_0.checkNotchRatio ~= NotchAdapt.CheckNotchRatio then
		arg_16_0.checkNotchRatio = NotchAdapt.CheckNotchRatio
		arg_16_0.initPos = nil
	end

	local var_16_0, var_16_1 = arg_16_0:FilterActivityBtns()

	for iter_16_0, iter_16_1 in ipairs(var_16_0) do
		iter_16_1:Init(iter_16_0)
	end

	for iter_16_2, iter_16_3 in ipairs(var_16_1) do
		iter_16_3:Clear()
	end

	local var_16_2 = #var_16_0

	assert(var_16_2 <= 4, "活动按钮不能超过4个")

	local var_16_3 = var_16_2 <= 3
	local var_16_4 = var_16_3 and 1 or 0.85
	local var_16_5 = var_16_3 and 390 or 420

	arg_16_0._tf.localScale = Vector3(var_16_4, var_16_4, 1)
	arg_16_0.initPos = arg_16_0.initPos or arg_16_0._tf.localPosition
	arg_16_0._tf.localPosition = Vector3(arg_16_0.initPos.x, var_16_5, 0)

	local var_16_6, var_16_7 = arg_16_0:FilterSpActivityBtns()

	for iter_16_4, iter_16_5 in pairs(var_16_6) do
		iter_16_5:Init(not var_16_3)
	end

	for iter_16_6, iter_16_7 in pairs(var_16_7) do
		iter_16_7:Clear()
	end
end

function var_0_0.Refresh(arg_17_0)
	if not arg_17_0.isInit then
		return
	end

	arg_17_0:Flush()

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.specailBtns) do
		if iter_17_1:InShowTime() then
			iter_17_1:Refresh()
		end
	end
end

function var_0_0.Disable(arg_18_0)
	for iter_18_0, iter_18_1 in ipairs(arg_18_0.specailBtns) do
		if iter_18_1:InShowTime() then
			iter_18_1:Disable()
		end
	end
end

function var_0_0.Dispose(arg_19_0)
	var_0_0.super.Dispose(arg_19_0)
	arg_19_0.linkBtnTopFoldableHelper:Dispose()

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.activityBtns) do
		iter_19_1:Dispose()
	end

	for iter_19_2, iter_19_3 in ipairs(arg_19_0.specailBtns) do
		iter_19_3:Dispose()
	end

	arg_19_0.specailBtns = nil
	arg_19_0.activityBtns = nil
end

function var_0_0.Fold(arg_20_0, arg_20_1, arg_20_2)
	var_0_0.super.Fold(arg_20_0, arg_20_1, arg_20_2)
	arg_20_0.linkBtnTopFoldableHelper:Fold(arg_20_1, arg_20_2)
end

function var_0_0.GetDirection(arg_21_0)
	return Vector2(1, 0)
end

return var_0_0
