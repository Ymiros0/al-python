local var_0_0 = class("BossRushBattleResultMediator", import("view.base.ContextMediator"))

var_0_0.ON_SETTLE = "BossRushBattleResultMediator.ON_SETTLE"
var_0_0.BEGIN_STAGE = "BossRushBattleResultMediator.BEGIN_STAGE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_SETTLE, function()
		if not arg_1_0.contextData.win or arg_1_0.contextData.system == SYSTEM_BOSS_RUSH_EX:
			arg_1_0.sendNotification(GAME.GO_BACK)

			return

		seriesAsync({
			function(arg_3_0)
				arg_1_0.ShowTotalAward(arg_1_0.contextData.awards)
		}))
	arg_1_0.bind(var_0_0.BEGIN_STAGE, function(arg_4_0)
		local var_4_0, var_4_1 = getProxy(ActivityProxy).GetContinuousTime()

		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = arg_1_0.contextData.system,
			actId = arg_1_0.contextData.actId,
			continuousBattleTimes = var_4_0,
			totalBattleTimes = var_4_1
		}))
	arg_1_0.sendNotification(NewBattleResultMediator.ON_ENTER_BATTLE_RESULT)

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		NewBattleResultMediator.SET_SKIP_FLAG,
		GAME.BOSSRUSH_TRACE_DONE,
		GAME.BOSSRUSH_TRACE_ERROR,
		GAME.BEGIN_STAGE_DONE,
		GAME.BEGIN_STAGE_ERRO,
		ContinuousOperationMediator.ON_REENTER
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == None:
		-- block empty
	elif var_6_0 == GAME.BEGIN_STAGE_DONE:
		arg_6_0.sendNotification(GAME.CHANGE_SCENE, SCENE.COMBATLOAD, var_6_1)
	elif var_6_0 == GAME.BEGIN_STAGE_ERRO:
		if var_6_1 == 3:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("battle_preCombatMediator_timeout"),
				def onYes:()
					arg_6_0.viewComponent.emit(BaseUI.ON_CLOSE)
			})
	elif var_6_0 == GAME.BOSSRUSH_TRACE_DONE:
		arg_6_0.viewComponent.emit(var_0_0.BEGIN_STAGE)
	elif var_6_0 == GAME.BOSSRUSH_TRACE_ERROR:
		arg_6_0.sendNotification(GAME.GO_BACK)
	elif var_6_0 == NewBattleResultMediator.SET_SKIP_FLAG:
		if var_6_1:
			getProxy(ActivityProxy).UseContinuousTime()
			existCall(arg_6_0.viewComponent.HideConfirmPanel, arg_6_0.viewComponent)

			if not (function()
				local var_8_0 = getProxy(ActivityProxy).GetContinuousTime()

				if not var_8_0 or var_8_0 <= 0:
					return

				if getProxy(BayProxy).getShipCount() >= getProxy(PlayerProxy).getRawData().getMaxShipBag():
					return

				local var_8_1 = arg_6_0.contextData.seriesData
				local var_8_2 = arg_6_0.contextData.system
				local var_8_3 = arg_6_0.contextData.seriesData.mode
				local var_8_4 = var_8_1.GetFleets()
				local var_8_5 = var_8_4[#var_8_4]
				local var_8_6 = _.slice(var_8_4, 1, #var_8_4 - 1)

				if (function()
					local var_9_0 = 0
					local var_9_1 = pg.battle_cost_template[var_8_2]
					local var_9_2 = var_8_1.GetOilLimit()
					local var_9_3 = var_9_1.oil_cost > 0

					local function var_9_4(arg_10_0, arg_10_1)
						local var_10_0 = 0

						if var_9_3:
							var_10_0 = arg_10_0.GetCostSum().oil

							if arg_10_1 > 0:
								var_10_0 = math.min(arg_10_1, var_10_0)

						return var_10_0

					local var_9_5 = #var_8_1.GetExpeditionIds()

					if var_8_3 == BossRushSeriesData.MODE.SINGLE:
						var_9_0 = var_9_0 + var_9_4(var_8_6[1], var_9_2[1])
						var_9_0 = var_9_0 + var_9_4(var_8_5, var_9_2[2])
						var_9_0 = var_9_0 * var_9_5
					else
						var_9_0 = var_9_4(var_8_5, var_9_2[2]) * var_9_5

						_.each(var_8_6, function(arg_11_0)
							var_9_0 = var_9_0 + var_9_4(arg_11_0, var_9_2[1]))

					return var_9_0)() > getProxy(PlayerProxy).getRawData().oil:
					return

				if var_8_3 == BossRushSeriesData.MODE.SINGLE and _.any(var_8_4, function(arg_12_0)
					return _.any(arg_12_0.GetRawShipIds(), function(arg_13_0)
						return getProxy(BayProxy).RawGetShipById(arg_13_0).getEnergy() <= pg.gameset.series_enemy_mood_limit.key_value)):
					return

				return True)():
				getProxy(ActivityProxy).AddBossRushAwards(arg_6_0.contextData.awards)

				local var_6_2 = getProxy(ActivityProxy).PopBossRushAwards()

				arg_6_0.ShowTotalAward(var_6_2)

				return

			arg_6_0.sendNotification(NewBattleResultMediator.ON_COMPLETE_BATTLE_RESULT)
	elif var_6_0 == ContinuousOperationMediator.ON_REENTER:
		getProxy(ActivityProxy).AddBossRushAwards(arg_6_0.contextData.awards)

		if not var_6_1.autoFlag or not arg_6_0.contextData.win:
			local var_6_3 = getProxy(ActivityProxy).PopBossRushAwards()

			arg_6_0.ShowTotalAward(var_6_3)

			return

		local var_6_4 = getProxy(ActivityProxy).GetContinuousTime()

		if var_6_4 and var_6_4 > 0:
			arg_6_0.sendNotification(GAME.BOSSRUSH_TRACE, {
				actId = arg_6_0.contextData.actId,
				seriesId = arg_6_0.contextData.seriesData.id,
				mode = arg_6_0.contextData.seriesData.mode
			})

			return

		local var_6_5 = getProxy(ActivityProxy).PopBossRushAwards()

		arg_6_0.ShowTotalAward(var_6_5)

def var_0_0.ShowTotalAward(arg_14_0, arg_14_1):
	getProxy(ContextProxy).GetPrevContext(1).addChild(Context.New({
		mediator = BossRushTotalRewardPanelMediator,
		viewComponent = BossRushTotalRewardPanel,
		data = {
			isLayer = True,
			rewards = arg_14_1
		}
	}))
	arg_14_0.sendNotification(GAME.GO_BACK)

def var_0_0.remove(arg_15_0):
	return

return var_0_0
