﻿local var_0_0 = class("BossRushBattleResultMediator", import("view.base.ContextMediator"))

var_0_0.ON_SETTLE = "BossRushBattleResultMediator:ON_SETTLE"
var_0_0.BEGIN_STAGE = "BossRushBattleResultMediator:BEGIN_STAGE"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_SETTLE, function()
		if not arg_1_0.contextData.win or arg_1_0.contextData.system == SYSTEM_BOSS_RUSH_EX then
			arg_1_0:sendNotification(GAME.GO_BACK)

			return
		end

		seriesAsync({
			function(arg_3_0)
				arg_1_0:ShowTotalAward(arg_1_0.contextData.awards)
			end
		})
	end)
	arg_1_0:bind(var_0_0.BEGIN_STAGE, function(arg_4_0)
		local var_4_0, var_4_1 = getProxy(ActivityProxy):GetContinuousTime()

		arg_1_0:sendNotification(GAME.BEGIN_STAGE, {
			system = arg_1_0.contextData.system,
			actId = arg_1_0.contextData.actId,
			continuousBattleTimes = var_4_0,
			totalBattleTimes = var_4_1
		})
	end)
	arg_1_0:sendNotification(NewBattleResultMediator.ON_ENTER_BATTLE_RESULT)
end

function var_0_0.listNotificationInterests(arg_5_0)
	return {
		NewBattleResultMediator.SET_SKIP_FLAG,
		GAME.BOSSRUSH_TRACE_DONE,
		GAME.BOSSRUSH_TRACE_ERROR,
		GAME.BEGIN_STAGE_DONE,
		GAME.BEGIN_STAGE_ERRO,
		ContinuousOperationMediator.ON_REENTER
	}
end

function var_0_0.handleNotification(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1:getName()
	local var_6_1 = arg_6_1:getBody()

	if var_6_0 == nil then
		-- block empty
	elseif var_6_0 == GAME.BEGIN_STAGE_DONE then
		arg_6_0:sendNotification(GAME.CHANGE_SCENE, SCENE.COMBATLOAD, var_6_1)
	elseif var_6_0 == GAME.BEGIN_STAGE_ERRO then
		if var_6_1 == 3 then
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				hideNo = true,
				content = i18n("battle_preCombatMediator_timeout"),
				onYes = function()
					arg_6_0.viewComponent:emit(BaseUI.ON_CLOSE)
				end
			})
		end
	elseif var_6_0 == GAME.BOSSRUSH_TRACE_DONE then
		arg_6_0.viewComponent:emit(var_0_0.BEGIN_STAGE)
	elseif var_6_0 == GAME.BOSSRUSH_TRACE_ERROR then
		arg_6_0:sendNotification(GAME.GO_BACK)
	elseif var_6_0 == NewBattleResultMediator.SET_SKIP_FLAG then
		if var_6_1 then
			getProxy(ActivityProxy):UseContinuousTime()
			existCall(arg_6_0.viewComponent.HideConfirmPanel, arg_6_0.viewComponent)

			if not (function()
				local var_8_0 = getProxy(ActivityProxy):GetContinuousTime()

				if not var_8_0 or var_8_0 <= 0 then
					return
				end

				if getProxy(BayProxy):getShipCount() >= getProxy(PlayerProxy):getRawData():getMaxShipBag() then
					return
				end

				local var_8_1 = arg_6_0.contextData.seriesData
				local var_8_2 = arg_6_0.contextData.system
				local var_8_3 = arg_6_0.contextData.seriesData.mode
				local var_8_4 = var_8_1:GetFleets()
				local var_8_5 = var_8_4[#var_8_4]
				local var_8_6 = _.slice(var_8_4, 1, #var_8_4 - 1)

				if (function()
					local var_9_0 = 0
					local var_9_1 = pg.battle_cost_template[var_8_2]
					local var_9_2 = var_8_1:GetOilLimit()
					local var_9_3 = var_9_1.oil_cost > 0

					local function var_9_4(arg_10_0, arg_10_1)
						local var_10_0 = 0

						if var_9_3 then
							var_10_0 = arg_10_0:GetCostSum().oil

							if arg_10_1 > 0 then
								var_10_0 = math.min(arg_10_1, var_10_0)
							end
						end

						return var_10_0
					end

					local var_9_5 = #var_8_1:GetExpeditionIds()

					if var_8_3 == BossRushSeriesData.MODE.SINGLE then
						var_9_0 = var_9_0 + var_9_4(var_8_6[1], var_9_2[1])
						var_9_0 = var_9_0 + var_9_4(var_8_5, var_9_2[2])
						var_9_0 = var_9_0 * var_9_5
					else
						var_9_0 = var_9_4(var_8_5, var_9_2[2]) * var_9_5

						_.each(var_8_6, function(arg_11_0)
							var_9_0 = var_9_0 + var_9_4(arg_11_0, var_9_2[1])
						end)
					end

					return var_9_0
				end)() > getProxy(PlayerProxy):getRawData().oil then
					return
				end

				if var_8_3 == BossRushSeriesData.MODE.SINGLE and _.any(var_8_4, function(arg_12_0)
					return _.any(arg_12_0:GetRawShipIds(), function(arg_13_0)
						return getProxy(BayProxy):RawGetShipById(arg_13_0):getEnergy() <= pg.gameset.series_enemy_mood_limit.key_value
					end)
				end) then
					return
				end

				return true
			end)() then
				getProxy(ActivityProxy):AddBossRushAwards(arg_6_0.contextData.awards)

				local var_6_2 = getProxy(ActivityProxy):PopBossRushAwards()

				arg_6_0:ShowTotalAward(var_6_2)

				return
			end

			arg_6_0:sendNotification(NewBattleResultMediator.ON_COMPLETE_BATTLE_RESULT)
		end
	elseif var_6_0 == ContinuousOperationMediator.ON_REENTER then
		getProxy(ActivityProxy):AddBossRushAwards(arg_6_0.contextData.awards)

		if not var_6_1.autoFlag or not arg_6_0.contextData.win then
			local var_6_3 = getProxy(ActivityProxy):PopBossRushAwards()

			arg_6_0:ShowTotalAward(var_6_3)

			return
		end

		local var_6_4 = getProxy(ActivityProxy):GetContinuousTime()

		if var_6_4 and var_6_4 > 0 then
			arg_6_0:sendNotification(GAME.BOSSRUSH_TRACE, {
				actId = arg_6_0.contextData.actId,
				seriesId = arg_6_0.contextData.seriesData.id,
				mode = arg_6_0.contextData.seriesData.mode
			})

			return
		end

		local var_6_5 = getProxy(ActivityProxy):PopBossRushAwards()

		arg_6_0:ShowTotalAward(var_6_5)
	end
end

function var_0_0.ShowTotalAward(arg_14_0, arg_14_1)
	getProxy(ContextProxy):GetPrevContext(1):addChild(Context.New({
		mediator = BossRushTotalRewardPanelMediator,
		viewComponent = BossRushTotalRewardPanel,
		data = {
			isLayer = true,
			rewards = arg_14_1
		}
	}))
	arg_14_0:sendNotification(GAME.GO_BACK)
end

function var_0_0.remove(arg_15_0)
	return
end

return var_0_0
