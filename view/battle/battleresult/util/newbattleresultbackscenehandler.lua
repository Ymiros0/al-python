local var_0_0 = class("NewBattleResultBackSceneHandler", pm.Mediator)

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0)
	pg.m02:registerMediator(arg_1_0)

	arg_1_0.contextData = arg_1_1
end

function var_0_0.Execute(arg_2_0)
	local var_2_0 = arg_2_0.contextData
	local var_2_1 = var_2_0.system

	if var_2_1 == SYSTEM_DUEL then
		arg_2_0:ExitDuelSystem(var_2_0)
	elseif var_2_1 == SYSTEM_ACT_BOSS then
		arg_2_0:ExitActBossSystem(var_2_0)
	elseif var_2_1 == SYSTEM_ROUTINE or var_2_1 == SYSTEM_SUB_ROUTINE then
		arg_2_0:ExitRoutineSystem(var_2_0)
	elseif var_2_1 == SYSTEM_SCENARIO then
		arg_2_0:ExitScenarioSystem(var_2_0)
	elseif var_2_1 == SYSTEM_CHALLENGE then
		arg_2_0:ExitChallengeSystem(var_2_0)
	elseif var_2_1 == SYSTEM_HP_SHARE_ACT_BOSS or var_2_1 == SYSTEM_BOSS_EXPERIMENT or var_2_1 == SYSTEM_ACT_BOSS_SP then
		arg_2_0:ExitShareBossSystem(var_2_0)
	elseif var_2_1 == SYSTEM_WORLD_BOSS then
		arg_2_0:ExitWorldBossSystem(var_2_0)
	elseif var_2_1 == SYSTEM_WORLD then
		arg_2_0:ExitWorldSystem(var_2_0)
	elseif var_2_1 == SYSTEM_BOSS_RUSH or var_2_1 == SYSTEM_BOSS_RUSH_EX then
		if arg_2_0:CheckBossRushSystem(var_2_0) then
			arg_2_0:ResultRushBossSystem(var_2_0)
		end
	elseif var_2_1 == SYSTEM_LIMIT_CHALLENGE then
		arg_2_0:ExitLimitChallengeSystem(var_2_0)
	elseif var_2_1 == SYSTEM_BOSS_SINGLE then
		arg_2_0:ExitBossSingleSystem(var_2_0)
	else
		arg_2_0:ExitCommonSystem(var_2_0)
	end

	getProxy(MetaCharacterProxy):clearLastMetaSkillExpInfoList()
end

function var_0_0.ExitDuelSystem(arg_3_0, arg_3_1)
	local var_3_0 = getProxy(ContextProxy):getContextByMediator(MilitaryExerciseMediator)

	if var_3_0 then
		local var_3_1 = var_3_0:getContextByMediator(ExercisePreCombatMediator)

		var_3_0:removeChild(var_3_1)
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitActBossSystem(arg_4_0, arg_4_1)
	local var_4_0, var_4_1 = getProxy(ContextProxy):getContextByMediator(ActivityBossPreCombatMediator)

	if var_4_0 then
		var_4_1:removeChild(var_4_0)
	end

	if getProxy(ContextProxy):getCurrentContext():getContextByMediator(ContinuousOperationMediator) then
		arg_4_0:CheckActBossSystem(arg_4_1)
	else
		pg.m02:sendNotification(GAME.GO_BACK)
	end
end

function var_0_0.ExitRoutineSystem(arg_5_0, arg_5_1)
	local var_5_0 = getProxy(ContextProxy):getContextByMediator(DailyLevelMediator)

	if var_5_0 then
		local var_5_1 = var_5_0:getContextByMediator(PreCombatMediator)

		var_5_0:removeChild(var_5_1)
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitScenarioSystem(arg_6_0, arg_6_1)
	if arg_6_1.needHelpMessage then
		getProxy(ChapterProxy):StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.BATTLE_FAILED)
	end

	local var_6_0 = getProxy(ContextProxy):getContextByMediator(LevelMediator2)

	if var_6_0 then
		local var_6_1 = var_6_0:getContextByMediator(ChapterPreCombatMediator)

		if var_6_1 then
			var_6_0:removeChild(var_6_1)
		end
	end

	if arg_6_1.score > ys.Battle.BattleConst.BattleScore.C then
		arg_6_0:ShowExtraChapterActSocre(arg_6_1)
	end

	getProxy(ChapterProxy):WriteBackOnExitBattleResult()
	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitChallengeSystem(arg_7_0, arg_7_1)
	getProxy(ChallengeProxy):WriteBackOnExitBattleResult(arg_7_0.contextData.score, arg_7_0.contextData.mode)

	if not arg_7_1.goToNext then
		arg_7_1.goToNext = nil

		local var_7_0 = getProxy(ContextProxy):getContextByMediator(ChallengeMainMediator)

		if var_7_0 then
			local var_7_1 = var_7_0:getContextByMediator(ChallengePreCombatMediator)

			var_7_0:removeChild(var_7_1)
		end
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitShareBossSystem(arg_8_0, arg_8_1)
	local var_8_0, var_8_1 = getProxy(ContextProxy):getContextByMediator(ActivityBossPreCombatMediator)

	if var_8_0 then
		var_8_1:removeChild(var_8_0)
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitWorldBossSystem(arg_9_0, arg_9_1)
	local var_9_0 = getProxy(ContextProxy):getContextByMediator(WorldBossMediator)
	local var_9_1 = var_9_0:getContextByMediator(WorldBossFormationMediator)

	if var_9_1 then
		var_9_0:removeChild(var_9_1)
	end

	pg.m02:sendNotification(GAME.WORLD_BOSS_BATTLE_QUIT, {
		id = arg_9_1.bossId
	})
	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitWorldSystem(arg_10_0, arg_10_1)
	local var_10_0 = getProxy(ContextProxy):getContextByMediator(WorldMediator)
	local var_10_1 = var_10_0:getContextByMediator(WorldPreCombatMediator) or var_10_0:getContextByMediator(WorldBossInformationMediator)

	if var_10_1 then
		var_10_0:removeChild(var_10_1)
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ResultRushBossSystem(arg_11_0, arg_11_1)
	local var_11_0 = getProxy(ContextProxy):GetPrevContext(1)
	local var_11_1 = var_11_0:getContextByMediator(BossRushPreCombatMediator)

	if var_11_1 then
		var_11_0:removeChild(var_11_1)
	end

	local var_11_2 = var_11_0:getContextByMediator(BossRushFleetSelectMediator)

	if var_11_2 then
		var_11_0:removeChild(var_11_2)
	end

	if not (arg_11_1.score > ys.Battle.BattleConst.BattleScore.C) and arg_11_1.system == SYSTEM_BOSS_RUSH_EX then
		arg_11_0:addSubLayers(Context.New({
			mediator = BattleFailTipMediator,
			viewComponent = BattleFailTipLayer,
			data = {
				mainShips = arg_11_1.newMainShips,
				battleSystem = arg_11_1.system
			},
			onRemoved = function()
				pg.m02:sendNotification(GAME.GO_BACK)
			end
		}))

		return
	end

	pg.m02:sendNotification(GAME.BOSSRUSH_SETTLE, {
		actId = arg_11_1.actId
	})
end

function var_0_0.ExitRushBossSystem(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0 = arg_13_1.system
	local var_13_1 = arg_13_1.actId
	local var_13_2 = arg_13_2.seriesData
	local var_13_3 = arg_13_1.score > ys.Battle.BattleConst.BattleScore.C
	local var_13_4 = var_13_0 == SYSTEM_BOSS_RUSH and BossRushBattleResultMediator or BossRushBattleResultMediator
	local var_13_5 = var_13_0 == SYSTEM_BOSS_RUSH and BossRushBattleResultLayer or BossRushEXBattleResultLayer

	arg_13_0:addSubLayers(Context.New({
		mediator = var_13_4,
		viewComponent = var_13_5,
		data = {
			awards = arg_13_2.awards,
			system = var_13_0,
			actId = var_13_1,
			seriesData = var_13_2,
			win = var_13_3
		}
	}), true)
	LoadContextCommand.RemoveLayerByMediator(NewBattleResultMediator)
end

function var_0_0.ExitLimitChallengeSystem(arg_14_0, arg_14_1)
	local var_14_0 = getProxy(ContextProxy):getContextByMediator(LimitChallengeMediator)

	if var_14_0 then
		local var_14_1 = var_14_0:getContextByMediator(LimitChallengePreCombatMediator)

		if var_14_1 then
			var_14_0:removeChild(var_14_1)
		end
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

function var_0_0.ExitBossSingleSystem(arg_15_0, arg_15_1)
	local var_15_0, var_15_1 = getProxy(ContextProxy):getContextByMediator(BossSinglePreCombatMediator)

	if var_15_0 then
		var_15_1:removeChild(var_15_0)
	end

	if getProxy(ContextProxy):getCurrentContext():getContextByMediator(BossSingleContinuousOperationMediator) then
		arg_15_0:CheckBossSingleSystem(arg_15_1)
	else
		pg.m02:sendNotification(GAME.GO_BACK)
	end
end

function var_0_0.ExitCommonSystem(arg_16_0, arg_16_1)
	local var_16_0 = getProxy(ContextProxy):getContextByMediator(LevelMediator2)

	if var_16_0 then
		local var_16_1 = var_16_0:getContextByMediator(PreCombatMediator)

		if var_16_1 then
			var_16_0:removeChild(var_16_1)
		end
	end

	pg.m02:sendNotification(GAME.GO_BACK)
end

local function var_0_1()
	local var_17_0 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_EXTRA_CHAPTER_RANK)
	local var_17_1 = {}

	for iter_17_0, iter_17_1 in ipairs(var_17_0) do
		if iter_17_1 and not iter_17_1:isEnd() then
			table.insert(var_17_1, iter_17_1)
		end
	end

	return var_17_1
end

function var_0_0.ShowExtraChapterActSocre(arg_18_0, arg_18_1)
	local var_18_0 = getProxy(ChapterProxy)
	local var_18_1 = var_18_0:getActiveChapter()
	local var_18_2 = var_18_1 and var_18_0:getMapById(var_18_1:getConfig("map"))
	local var_18_3 = var_0_1()

	for iter_18_0, iter_18_1 in ipairs(var_18_3) do
		local var_18_4 = iter_18_1:getConfig("config_data")
		local var_18_5 = arg_18_1.stageId

		if var_18_4[1] == var_18_5 and var_18_2 and var_18_2:isActExtra() then
			local var_18_6 = math.floor(arg_18_1.statistics._totalTime)
			local var_18_7 = ActivityLevelConst.getShipsPower(arg_18_1.prefabFleet or arg_18_1.oldMainShips)
			local var_18_8, var_18_9 = ActivityLevelConst.getExtraChapterSocre(var_18_5, var_18_6, var_18_7, iter_18_1)
			local var_18_10 = var_18_9 < var_18_8 and i18n("extra_chapter_record_updated") or i18n("extra_chapter_record_not_updated")

			if var_18_9 < var_18_8 then
				iter_18_1.data1 = var_18_8

				getProxy(ActivityProxy):updateActivity(iter_18_1)

				var_18_9 = var_18_8
			end

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				hideNo = true,
				content = i18n("extra_chapter_socre_tip", var_18_8, var_18_9, var_18_10),
				weight = LayerWeightConst.SECOND_LAYER
			})
		end
	end
end

local function var_0_2(arg_19_0)
	local var_19_0 = getProxy(ActivityProxy):getActivityById(arg_19_0.actId)
	local var_19_1 = var_19_0:getConfig("config_id")
	local var_19_2 = pg.activity_event_worldboss[var_19_1]
	local var_19_3 = var_19_0:IsOilLimit(arg_19_0.stageId)
	local var_19_4 = getProxy(FleetProxy):getActivityFleets()[arg_19_0.actId]
	local var_19_5 = 0
	local var_19_6 = var_19_2.use_oil_limit[arg_19_0.mainFleetId]

	local function var_19_7(arg_20_0, arg_20_1)
		local var_20_0 = arg_20_0:GetCostSum().oil

		if arg_20_1 > 0 then
			var_20_0 = math.min(var_20_0, arg_20_1)
		end

		var_19_5 = var_19_5 + var_20_0
	end

	var_19_7(var_19_4[arg_19_0.mainFleetId], var_19_3 and var_19_6[1] or 0)
	var_19_7(var_19_4[arg_19_0.mainFleetId + 10], var_19_3 and var_19_6[2] or 0)

	return var_19_5
end

local function var_0_3(arg_21_0, arg_21_1)
	local var_21_0 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(ContinuousOperationMediator)
	local var_21_1 = var_21_0 and var_21_0.data.autoFlag or nil
	local var_21_2 = getProxy(ChapterProxy):PopActBossRewards()

	LoadContextCommand.LoadLayerOnTopContext(Context.New({
		mediator = ActivityBossTotalRewardPanelMediator,
		viewComponent = ActivityBossTotalRewardPanel,
		data = {
			onClose = function()
				pg.m02:sendNotification(GAME.GO_BACK)
			end,
			stopReason = arg_21_1,
			rewards = var_21_2,
			isAutoFight = var_21_1,
			continuousBattleTimes = arg_21_0.continuousBattleTimes,
			totalBattleTimes = arg_21_0.totalBattleTimes
		}
	}))
end

local function var_0_4(arg_23_0, arg_23_1)
	local var_23_0 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(BossSingleContinuousOperationMediator)
	local var_23_1 = var_23_0 and var_23_0.data.autoFlag or nil
	local var_23_2 = getProxy(ChapterProxy):PopBossSingleRewards()

	LoadContextCommand.LoadLayerOnTopContext(Context.New({
		mediator = BossSingleTotalRewardPanelMediator,
		viewComponent = BossSingleTotalRewardPanel,
		data = {
			onClose = function()
				pg.m02:sendNotification(GAME.GO_BACK)
			end,
			stopReason = arg_23_1,
			rewards = var_23_2,
			isAutoFight = var_23_1,
			continuousBattleTimes = arg_23_0.continuousBattleTimes,
			totalBattleTimes = arg_23_0.totalBattleTimes
		}
	}))
end

local function var_0_5()
	local var_25_0 = pg.GuildMsgBoxMgr.GetInstance()

	if var_25_0:GetShouldShowBattleTip() then
		local var_25_1 = getProxy(GuildProxy):getRawData()
		local var_25_2 = var_25_1 and var_25_1:getWeeklyTask()

		if var_25_2 and var_25_2.id ~= 0 then
			var_25_0:SubmitTask(function(arg_26_0, arg_26_1)
				if arg_26_1 then
					var_25_0:CancelShouldShowBattleTip()
				end
			end)
		end
	end
end

function var_0_0.CheckActBossSystem(arg_27_0, arg_27_1)
	pg.m02:sendNotification(ContinuousOperationMediator.CONTINUE_OPERATION)

	if var_0_2(arg_27_1) > getProxy(PlayerProxy):getRawData().oil then
		var_0_3(arg_27_1, i18n("multiple_sorties_stop_reason1"))

		return
	end

	if getProxy(BayProxy):getShipCount() >= getProxy(PlayerProxy):getRawData():getMaxShipBag() then
		var_0_3(arg_27_1, i18n("multiple_sorties_stop_reason3"))

		return
	end

	local var_27_0 = getProxy(FleetProxy):getActivityFleets()[arg_27_1.actId][arg_27_1.mainFleetId]
	local var_27_1 = _.map(_.values(var_27_0.ships), function(arg_28_0)
		local var_28_0 = getProxy(BayProxy):getShipById(arg_28_0)

		if var_28_0 and var_28_0.energy == Ship.ENERGY_LOW then
			return var_28_0
		end
	end)

	if #var_27_1 > 0 then
		local var_27_2 = Fleet.DEFAULT_NAME_BOSS_ACT[arg_27_1.mainFleetId]
		local var_27_3 = _.map(var_27_1, function(arg_29_0)
			return "「" .. arg_29_0:getConfig("name") .. "」"
		end)

		var_0_3(arg_27_1, i18n("multiple_sorties_stop_reason2", var_27_2, table.concat(var_27_3, "")))

		return
	end

	if arg_27_1.statistics._battleScore <= ys.Battle.BattleConst.BattleScore.C then
		var_0_3(arg_27_1, i18n("multiple_sorties_stop_reason4"))

		return
	end

	var_0_5()

	local var_27_4 = getProxy(ContextProxy)
	local var_27_5 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(ContinuousOperationMediator)

	if var_27_5 and not var_27_5.data.autoFlag then
		var_0_3(arg_27_1)

		return
	end

	if arg_27_1.continuousBattleTimes < 1 then
		var_0_3(arg_27_1)

		return
	end

	pg.m02:sendNotification(NewBattleResultMediator.ON_COMPLETE_BATTLE_RESULT)
end

function var_0_0.ContinuousBossRush(arg_30_0, arg_30_1, arg_30_2, arg_30_3, arg_30_4, arg_30_5, arg_30_6)
	seriesAsync({
		function(arg_31_0)
			arg_30_0:addSubLayers(Context.New({
				mediator = ChallengePassedMediator,
				viewComponent = BossRushPassedLayer,
				data = {
					curIndex = arg_30_3 - 1,
					maxIndex = #arg_30_4
				},
				onRemoved = arg_31_0
			}))
		end,
		function(arg_32_0)
			pg.m02:sendNotification(GAME.BEGIN_STAGE, {
				system = arg_30_1,
				actId = arg_30_2,
				continuousBattleTimes = arg_30_5,
				totalBattleTimes = arg_30_6
			})
		end
	})
end

function var_0_0.CheckBossRushSystem(arg_33_0, arg_33_1)
	local var_33_0 = getProxy(ContextProxy)
	local var_33_1 = arg_33_1.score > ys.Battle.BattleConst.BattleScore.C
	local var_33_2 = arg_33_1.actId
	local var_33_3 = getProxy(ActivityProxy):getActivityById(var_33_2):GetSeriesData()

	assert(var_33_3)

	local var_33_4 = var_33_3:GetStaegLevel() + 1
	local var_33_5 = var_33_3:GetExpeditionIds()

	if var_33_0:getCurrentContext():getContextByMediator(ContinuousOperationMediator) then
		var_0_5()
	end

	local var_33_6 = var_33_0:getCurrentContext():getContextByMediator(ContinuousOperationMediator)
	local var_33_7 = not var_33_6 or var_33_6.data.autoFlag
	local var_33_8 = not var_33_1 or var_33_4 > #var_33_5 or not var_33_7

	if not var_33_8 then
		arg_33_0:ContinuousBossRush(arg_33_1.system, var_33_2, var_33_4, var_33_5, arg_33_1.continuousBattleTimes, arg_33_1.totalBattleTimes)
	end

	return var_33_8
end

local function var_0_6(arg_34_0)
	local var_34_0 = getProxy(ActivityProxy):getActivityById(arg_34_0.actId):GetEnemyDataByStageId(arg_34_0.stageId):GetOilLimit()
	local var_34_1 = getProxy(FleetProxy):getActivityFleets()[arg_34_0.actId]
	local var_34_2 = 0

	local function var_34_3(arg_35_0, arg_35_1)
		local var_35_0 = arg_35_0:GetCostSum().oil

		if arg_35_1 > 0 then
			var_35_0 = math.min(var_35_0, arg_35_1)
		end

		var_34_2 = var_34_2 + var_35_0
	end

	var_34_3(var_34_1[arg_34_0.mainFleetId], var_34_0[1] or 0)
	var_34_3(var_34_1[arg_34_0.mainFleetId + 10], var_34_0[2] or 0)

	return var_34_2
end

function var_0_0.CheckBossSingleSystem(arg_36_0, arg_36_1)
	pg.m02:sendNotification(BossSingleContinuousOperationMediator.CONTINUE_OPERATION)

	if var_0_6(arg_36_1) > getProxy(PlayerProxy):getRawData().oil then
		var_0_4(arg_36_1, i18n("multiple_sorties_stop_reason1"))

		return
	end

	if getProxy(BayProxy):getShipCount() >= getProxy(PlayerProxy):getRawData():getMaxShipBag() then
		var_0_4(arg_36_1, i18n("multiple_sorties_stop_reason3"))

		return
	end

	local var_36_0 = getProxy(FleetProxy):getActivityFleets()[arg_36_1.actId][arg_36_1.mainFleetId]
	local var_36_1 = _.map(_.values(var_36_0.ships), function(arg_37_0)
		local var_37_0 = getProxy(BayProxy):getShipById(arg_37_0)

		if var_37_0 and var_37_0.energy == Ship.ENERGY_LOW then
			return var_37_0
		end
	end)

	if #var_36_1 > 0 then
		local var_36_2 = Fleet.DEFAULT_NAME_BOSS_ACT[arg_36_1.mainFleetId]
		local var_36_3 = _.map(var_36_1, function(arg_38_0)
			return "「" .. arg_38_0:getConfig("name") .. "」"
		end)

		var_0_4(arg_36_1, i18n("multiple_sorties_stop_reason2", var_36_2, table.concat(var_36_3, "")))

		return
	end

	if arg_36_1.statistics._battleScore <= ys.Battle.BattleConst.BattleScore.C then
		var_0_4(arg_36_1, i18n("multiple_sorties_stop_reason4"))

		return
	end

	var_0_5()

	local var_36_4 = getProxy(ContextProxy)
	local var_36_5 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(BossSingleContinuousOperationMediator)

	if var_36_5 and not var_36_5.data.autoFlag then
		var_0_4(arg_36_1)

		return
	end

	if arg_36_1.continuousBattleTimes < 1 then
		var_0_4(arg_36_1)

		return
	end

	pg.m02:sendNotification(NewBattleResultMediator.ON_COMPLETE_BATTLE_RESULT)
end

local function var_0_7(arg_39_0, arg_39_1)
	local var_39_0 = getProxy(ActivityProxy):getActivityById(arg_39_0)
	local var_39_1 = var_39_0:getConfig("config_id")
	local var_39_2 = pg.activity_event_worldboss[var_39_1].ticket
	local var_39_3 = getProxy(PlayerProxy):getRawData():getResource(var_39_2)

	if var_39_0:GetStageBonus(arg_39_1) == 0 and getProxy(SettingsProxy):isTipActBossExchangeTicket() == 1 and var_39_3 > 0 then
		return true
	end

	return false
end

local function var_0_8(arg_40_0)
	pg.m02:sendNotification(GAME.BEGIN_STAGE, {
		stageId = arg_40_0.stageId,
		mainFleetId = arg_40_0.mainFleetId,
		system = arg_40_0.system,
		actId = arg_40_0.actId,
		rivalId = arg_40_0.rivalId,
		continuousBattleTimes = arg_40_0.continuousBattleTimes,
		totalBattleTimes = arg_40_0.totalBattleTimes
	})
end

function var_0_0.listNotificationInterests(arg_41_0)
	return {
		GAME.BOSSRUSH_SETTLE_DONE,
		ContinuousOperationMediator.ON_REENTER,
		BossSingleContinuousOperationMediator.ON_REENTER
	}
end

function var_0_0.handleNotification(arg_42_0, arg_42_1)
	local var_42_0 = arg_42_1:getName()
	local var_42_1 = arg_42_1:getBody()

	if var_42_0 == GAME.BOSSRUSH_SETTLE_DONE then
		arg_42_0:ExitRushBossSystem(arg_42_0.contextData, var_42_1)
	elseif var_42_0 == ContinuousOperationMediator.ON_REENTER then
		if not var_42_1.autoFlag then
			var_0_3(arg_42_0.contextData)

			return
		end

		if var_0_7(arg_42_0.contextData.actId, arg_42_0.contextData.stageId) then
			pg.m02:sendNotification(GAME.ACT_BOSS_EXCHANGE_TICKET, {
				stageId = arg_42_0.contextData.stageId
			})
		else
			var_0_8(arg_42_0.contextData)
		end
	elseif var_42_0 == BossSingleContinuousOperationMediator.ON_REENTER then
		if not var_42_1.autoFlag then
			var_0_4(arg_42_0.contextData)

			return
		end

		var_0_8(arg_42_0.contextData)
	end
end

function var_0_0.addSubLayers(arg_43_0, arg_43_1, arg_43_2, arg_43_3)
	assert(isa(arg_43_1, Context), "should be an instance of Context")

	local var_43_0 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(NewBattleResultMediator)

	if arg_43_2 then
		while var_43_0.parent do
			var_43_0 = var_43_0.parent
		end
	end

	arg_43_0:sendNotification(GAME.LOAD_LAYERS, {
		parentContext = var_43_0,
		context = arg_43_1,
		callback = arg_43_3
	})
end

function var_0_0.Dispose(arg_44_0)
	pg.m02:removeMediator(arg_44_0.__cname)
end

return var_0_0
