local var_0_0 = class("BattleResultMediator", import("..base.ContextMediator"))

var_0_0.ON_BACK_TO_LEVEL_SCENE = "BattleResultMediator.ON_BACK_TO_LEVEL_SCENE"
var_0_0.ON_BACK_TO_DUEL_SCENE = "BattleResultMediator.ON_BACK_TO_DUEL_SCENE"
var_0_0.ON_GO_TO_TASK_SCENE = "BattleResultMediator.ON_GO_TO_TASK_SCENE"
var_0_0.GET_NEW_SHIP = "BattleResultMediator.GET_NEW_SHIP"
var_0_0.ON_GO_TO_MAIN_SCENE = "BattleResultMediator.ON_GO_TO_MAIN_SCENE"
var_0_0.ON_NEXT_CHALLENGE = "BattleResultMediator.ON_NEXT_CHALLENGE"
var_0_0.ON_CHALLENGE_RANK = "BattleResultMediator.ON_CHALLENGE_RANK"
var_0_0.ON_CHALLENGE_SHARE = "BattleResultMediator.ON_CHALLENGE_SHARE"
var_0_0.ON_CHALLENGE_DEFEAT_SCENE = "BattleResultMediator.ON_CHALLENGE_DEFEAT_SCENE"
var_0_0.DIRECT_EXIT = "BattleResultMediator.DIRECT_EXIT"
var_0_0.REENTER_STAGE = "BattleResultMediator.REENTER_STAGE"
var_0_0.OPEN_FAIL_TIP_LAYER = "BattleResultMediator.OPEN_FAIL_TIP_LAYER"
var_0_0.PRE_BATTLE_FAIL_EXIT = "BattleResultMediator.PRE_BATTLE_FAIL_EXIT"
var_0_0.ON_ENTER_BATTLE_RESULT = "BattleResultMediator.ON_ENTER_BATTLE_RESULT"
var_0_0.SET_SKIP_FLAG = "BattleResultMediator.SET_SKIP_FLAG"
var_0_0.ON_COMPLETE_BATTLE_RESULT = "BattleResultMediator.ON_COMPLETE_BATTLE_RESULT"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(PlayerProxy).getData()
	local var_1_1 = getProxy(FleetProxy)
	local var_1_2 = getProxy(BayProxy)
	local var_1_3 = getProxy(ChapterProxy)
	local var_1_4 = getProxy(ActivityProxy)
	local var_1_5 = arg_1_0.contextData.system

	if var_1_5 == SYSTEM_DUEL:
		local var_1_6 = getProxy(MilitaryExerciseProxy)
		local var_1_7 = var_1_6.getPreRivalById(arg_1_0.contextData.rivalId)

		assert(var_1_7, "should exist rival--" .. arg_1_0.contextData.rivalId)
		arg_1_0.viewComponent.setRivalVO(var_1_7)
		arg_1_0.viewComponent.setRank(var_1_0, var_1_6.getSeasonInfo())
	elif var_1_5 == SYSTEM_CHALLENGE:
		local var_1_8 = getProxy(ChallengeProxy)
		local var_1_9 = var_1_8.getUserChallengeInfo(arg_1_0.contextData.mode)

		arg_1_0.viewComponent.setChallengeInfo(var_1_9, var_1_8.userSeaonExpire(arg_1_0.contextData.mode))
	else
		if var_1_5 == SYSTEM_SCENARIO or var_1_5 == SYSTEM_ROUTINE or var_1_5 == SYSTEM_ACT_BOSS or var_1_5 == SYSTEM_BOSS_SINGLE or var_1_5 == SYSTEM_HP_SHARE_ACT_BOSS or var_1_5 == SYSTEM_SUB_ROUTINE or var_1_5 == SYSTEM_WORLD:
			local var_1_10 = _.detect(BuffHelper.GetBuffsByActivityType(ActivityConst.ACTIVITY_TYPE_BUFF), function(arg_2_0)
				return arg_2_0.getConfig("benefit_type") == "rookie_battle_exp")
			local var_1_11 = var_1_4.getBuffShipList()

			arg_1_0.viewComponent.setExpBuff(var_1_10, var_1_11)

		arg_1_0.viewComponent.setPlayer(var_1_0)

	local var_1_12

	if var_1_5 == SYSTEM_SCENARIO:
		var_1_12 = {}

		local var_1_13

		if var_1_5 == SYSTEM_SCENARIO:
			var_1_13 = var_1_3.getActiveChapter()

		local var_1_14 = var_1_13.fleet
		local var_1_15 = var_1_14[TeamType.Main]
		local var_1_16 = var_1_14[TeamType.Vanguard]

		for iter_1_0, iter_1_1 in ipairs(var_1_15):
			table.insert(var_1_12, iter_1_1)

		for iter_1_2, iter_1_3 in ipairs(var_1_16):
			table.insert(var_1_12, iter_1_3)

		local var_1_17 = _.detect(var_1_13.fleets, function(arg_3_0)
			return arg_3_0.getFleetType() == FleetType.Submarine)

		if var_1_17:
			local var_1_18 = var_1_17.getShipsByTeam(TeamType.Submarine, True)

			for iter_1_4, iter_1_5 in ipairs(var_1_18):
				table.insert(var_1_12, iter_1_5)

		arg_1_0.viewComponent.SetSkipFlag(var_1_3.GetChapterAutoFlag(var_1_13.id) == 1)
	elif var_1_5 == SYSTEM_WORLD:
		var_1_12 = {}

		local var_1_19 = nowWorld()
		local var_1_20 = var_1_19.GetActiveMap()
		local var_1_21 = var_1_20.GetFleet()
		local var_1_22 = var_1_21.GetTeamShipVOs(TeamType.Main, True)
		local var_1_23 = var_1_21.GetTeamShipVOs(TeamType.Vanguard, True)

		for iter_1_6, iter_1_7 in ipairs(var_1_22):
			table.insert(var_1_12, iter_1_7)

		for iter_1_8, iter_1_9 in ipairs(var_1_23):
			table.insert(var_1_12, iter_1_9)

		local var_1_24 = var_1_20.GetSubmarineFleet()

		if var_1_24:
			local var_1_25 = var_1_24.GetTeamShipVOs(TeamType.Submarine, True)

			for iter_1_10, iter_1_11 in ipairs(var_1_25):
				table.insert(var_1_12, iter_1_11)

		arg_1_0.viewComponent.SetSkipFlag(var_1_19.isAutoFight)
	elif var_1_5 == SYSTEM_CHALLENGE:
		arg_1_0.bind(var_0_0.ON_CHALLENGE_SHARE, function(arg_4_0)
			arg_1_0.addSubLayers(Context.New({
				mediator = ChallengeShareMediator,
				viewComponent = ChallengeShareLayer,
				data = {
					mode = arg_1_0.contextData.mode
				}
			})))
		arg_1_0.bind(var_0_0.ON_CHALLENGE_DEFEAT_SCENE, function(arg_5_0, arg_5_1)
			local var_5_0 = arg_5_1.callback

			arg_1_0.addSubLayers(Context.New({
				mediator = ChallengePassedMediator,
				viewComponent = ChallengePassedLayer,
				data = {
					mode = arg_1_0.contextData.mode
				},
				onRemoved = var_5_0
			})))
	elif var_1_5 == SYSTEM_WORLD_BOSS:
		local var_1_26 = nowWorld().GetBossProxy().GetFleet(arg_1_0.contextData.bossId)

		var_1_12 = getProxy(BayProxy).getShipsByFleet(var_1_26)

		local var_1_27 = arg_1_0.contextData.name

		arg_1_0.viewComponent.setTitle(var_1_27)
	elif var_1_5 == SYSTEM_DODGEM:
		-- block empty
	elif var_1_5 == SYSTEM_SUBMARINE_RUN:
		-- block empty
	elif var_1_5 == SYSTEM_REWARD_PERFORM:
		-- block empty
	elif var_1_5 == SYSTEM_AIRFIGHT:
		-- block empty
	elif var_1_5 == SYSTEM_CARDPUZZLE:
		-- block empty
	elif var_1_5 == SYSTEM_HP_SHARE_ACT_BOSS or var_1_5 == SYSTEM_ACT_BOSS or var_1_5 == SYSTEM_BOSS_SINGLE or var_1_5 == SYSTEM_BOSS_EXPERIMENT:
		local var_1_28 = arg_1_0.contextData.actId

		if var_1_5 == SYSTEM_HP_SHARE_ACT_BOSS:
			arg_1_0.viewComponent.setActId(var_1_28)

		local var_1_29 = var_1_1.getActivityFleets()[var_1_28]
		local var_1_30 = var_1_29[arg_1_0.contextData.mainFleetId]

		var_1_12 = var_1_2.getShipsByFleet(var_1_30)

		local var_1_31 = var_1_29[arg_1_0.contextData.mainFleetId + 10]
		local var_1_32 = var_1_2.getShipsByFleet(var_1_31)

		for iter_1_12, iter_1_13 in ipairs(var_1_32):
			table.insert(var_1_12, iter_1_13)
	elif var_1_5 == SYSTEM_GUILD:
		var_1_12 = {}

		local var_1_33 = getProxy(GuildProxy).getData().GetActiveEvent().GetBossMission()
		local var_1_34 = var_1_33.GetMainFleet()

		for iter_1_14, iter_1_15 in ipairs(var_1_34.GetShips()):
			table.insert(var_1_12, iter_1_15.ship)

		local var_1_35 = var_1_33.GetSubFleet()

		for iter_1_16, iter_1_17 in ipairs(var_1_35.GetShips()):
			table.insert(var_1_12, iter_1_17.ship)
	elif var_1_5 == SYSTEM_BOSS_RUSH or var_1_5 == SYSTEM_BOSS_RUSH_EX:
		local var_1_36 = arg_1_0.contextData.actId
		local var_1_37 = getProxy(ActivityProxy).getActivityById(var_1_36).GetSeriesData()

		assert(var_1_37)

		local var_1_38 = var_1_37.GetStaegLevel()
		local var_1_39 = var_1_37.GetFleetIds()
		local var_1_40 = var_1_39[var_1_38]

		if var_1_37.GetMode() == BossRushSeriesData.MODE.SINGLE:
			var_1_40 = var_1_39[1]

		local var_1_41 = var_1_1.getActivityFleets()[var_1_36][var_1_40]

		var_1_12 = var_1_2.getShipsByFleet(var_1_41)
	else
		local var_1_42 = arg_1_0.contextData.mainFleetId
		local var_1_43 = var_1_1.getFleetById(var_1_42)

		var_1_12 = var_1_2.getShipsByFleet(var_1_43)

	arg_1_0.viewComponent.setShips(var_1_12)
	arg_1_0.bind(var_0_0.ON_BACK_TO_LEVEL_SCENE, function(arg_6_0, arg_6_1)
		local var_6_0 = getProxy(ContextProxy)

		if var_1_5 == SYSTEM_DUEL:
			arg_1_0.viewComponent.emit(BattleResultMediator.ON_BACK_TO_DUEL_SCENE)

			return
		elif var_1_5 == SYSTEM_ACT_BOSS:
			local var_6_1, var_6_2 = var_6_0.getContextByMediator(PreCombatMediator)

			if var_6_1:
				var_6_2.removeChild(var_6_1)

			if var_6_0.getCurrentContext().getContextByMediator(ContinuousOperationMediator):
				arg_1_0.sendNotification(ContinuousOperationMediator.CONTINUE_OPERATION)
				existCall(arg_1_0.viewComponent.HideConfirmPanel, arg_1_0.viewComponent)

				local var_6_3 = getProxy(ActivityProxy).getActivityById(arg_1_0.contextData.actId)
				local var_6_4 = var_6_3.getConfig("config_id")
				local var_6_5 = pg.activity_event_worldboss[var_6_4]
				local var_6_6 = var_6_3.IsOilLimit(arg_1_0.contextData.stageId)
				local var_6_7 = getProxy(FleetProxy).getActivityFleets()[arg_1_0.contextData.actId]
				local var_6_8 = 0
				local var_6_9 = var_6_5.use_oil_limit[arg_1_0.contextData.mainFleetId]

				local function var_6_10(arg_7_0, arg_7_1)
					local var_7_0 = arg_7_0.GetCostSum().oil

					if arg_7_1 > 0:
						var_7_0 = math.min(var_7_0, arg_7_1)

					var_6_8 = var_6_8 + var_7_0

				var_6_10(var_6_7[arg_1_0.contextData.mainFleetId], var_6_6 and var_6_9[1] or 0)
				var_6_10(var_6_7[arg_1_0.contextData.mainFleetId + 10], var_6_6 and var_6_9[2] or 0)

				if var_6_8 > getProxy(PlayerProxy).getRawData().oil:
					local var_6_11 = i18n("multiple_sorties_stop_reason1")

					arg_1_0.DisplayTotalReward(var_6_11)

					return

				if getProxy(BayProxy).getShipCount() >= getProxy(PlayerProxy).getRawData().getMaxShipBag():
					local var_6_12 = i18n("multiple_sorties_stop_reason3")

					arg_1_0.DisplayTotalReward(var_6_12)

					return

				local var_6_13 = var_6_7[arg_1_0.contextData.mainFleetId]
				local var_6_14 = _.map(_.values(var_6_13.ships), function(arg_8_0)
					local var_8_0 = getProxy(BayProxy).getShipById(arg_8_0)

					if var_8_0 and var_8_0.energy == Ship.ENERGY_LOW:
						return var_8_0)

				if #var_6_14 > 0:
					local var_6_15 = Fleet.DEFAULT_NAME_BOSS_ACT[arg_1_0.contextData.mainFleetId]
					local var_6_16 = _.map(var_6_14, function(arg_9_0)
						return "「" .. arg_9_0.getConfig("name") .. "」")
					local var_6_17 = i18n("multiple_sorties_stop_reason2", var_6_15, table.concat(var_6_16, ""))

					arg_1_0.DisplayTotalReward(var_6_17)

					return

				if arg_1_0.contextData.statistics._battleScore <= ys.Battle.BattleConst.BattleScore.C:
					local var_6_18 = i18n("multiple_sorties_stop_reason4")

					arg_1_0.DisplayTotalReward(var_6_18)

					return

				local var_6_19 = pg.GuildMsgBoxMgr.GetInstance()

				if var_6_19.GetShouldShowBattleTip():
					local var_6_20 = getProxy(GuildProxy).getRawData()
					local var_6_21 = var_6_20 and var_6_20.getWeeklyTask()

					if var_6_21 and var_6_21.id != 0:
						var_6_19.SubmitTask(function(arg_10_0, arg_10_1)
							if arg_10_1:
								var_6_19.CancelShouldShowBattleTip())

				local var_6_22 = var_6_0.getCurrentContext().getContextByMediator(ContinuousOperationMediator)

				if var_6_22 and not var_6_22.data.autoFlag:
					arg_1_0.DisplayTotalReward()

					return

				if arg_1_0.contextData.continuousBattleTimes < 1:
					arg_1_0.DisplayTotalReward()

					return

				arg_1_0.sendNotification(BattleResultMediator.ON_COMPLETE_BATTLE_RESULT)

				return
		elif var_1_5 == SYSTEM_ROUTINE or var_1_5 == SYSTEM_SUB_ROUTINE:
			local var_6_23 = var_6_0.getContextByMediator(DailyLevelMediator)

			if var_6_23:
				local var_6_24 = var_6_23.getContextByMediator(PreCombatMediator)

				var_6_23.removeChild(var_6_24)
		elif var_1_5 == SYSTEM_SCENARIO:
			local var_6_25 = var_6_0.getContextByMediator(LevelMediator2)
			local var_6_26 = var_6_25.getContextByMediator(ChapterPreCombatMediator)

			if var_6_26:
				var_6_25.removeChild(var_6_26)

			if arg_1_0.contextData.score > 1:
				arg_1_0.showExtraChapterActSocre()

			local var_6_27 = getProxy(ChapterProxy)
			local var_6_28 = var_6_27.getActiveChapter()

			if var_6_28:
				if var_6_28.existOni():
					var_6_28.clearSubmarineFleet()
					var_6_27.updateChapter(var_6_28)
				elif var_6_28.isPlayingWithBombEnemy():
					var_6_28.fleets = {
						var_6_28.fleet
					}
					var_6_28.findex = 1

					var_6_27.updateChapter(var_6_28)
		elif var_1_5 == SYSTEM_CHALLENGE:
			local var_6_29 = getProxy(ChallengeProxy)
			local var_6_30 = arg_1_0.contextData.mode
			local var_6_31 = var_6_29.getUserChallengeInfo(var_6_30)

			if arg_1_0.contextData.score < ys.Battle.BattleConst.BattleScore.S:
				arg_1_0.sendNotification(GAME.CHALLENGE2_RESET, {
					mode = var_6_30
				})
			else
				local var_6_32 = var_6_31.IsFinish()

				var_6_31.updateLevelForward()

				if var_6_31.getMode() == ChallengeProxy.MODE_INFINITE and var_6_32:
					var_6_31.setInfiniteDungeonIDListByLevel()

			local var_6_33 = var_6_29.getChallengeInfo()

			if not var_6_29.userSeaonExpire(var_6_31.getMode()):
				var_6_33.checkRecord(var_6_31)

			if not arg_6_1.goToNext:
				local var_6_34 = var_6_0.getContextByMediator(ChallengeMainMediator)

				if var_6_34:
					local var_6_35 = var_6_34.getContextByMediator(ChallengePreCombatMediator)

					var_6_34.removeChild(var_6_35)
		elif var_1_5 == SYSTEM_HP_SHARE_ACT_BOSS:
			local var_6_36, var_6_37 = var_6_0.getContextByMediator(PreCombatMediator)

			if var_6_36:
				var_6_37.removeChild(var_6_36)
		elif var_1_5 == SYSTEM_WORLD_BOSS:
			local var_6_38 = var_6_0.getContextByMediator(WorldBossMediator)
			local var_6_39 = var_6_38.getContextByMediator(WorldBossFormationMediator)

			if var_6_39:
				var_6_38.removeChild(var_6_39)
		elif var_1_5 == SYSTEM_WORLD:
			local var_6_40 = var_6_0.getContextByMediator(WorldMediator)
			local var_6_41 = var_6_40.getContextByMediator(WorldPreCombatMediator) or var_6_40.getContextByMediator(WorldBossInformationMediator)

			if var_6_41:
				var_6_40.removeChild(var_6_41)
		elif var_1_5 == SYSTEM_BOSS_RUSH or var_1_5 == SYSTEM_BOSS_RUSH_EX:
			local var_6_42 = arg_1_0.contextData.score > ys.Battle.BattleConst.BattleScore.C
			local var_6_43 = arg_1_0.contextData.actId
			local var_6_44 = getProxy(ActivityProxy).getActivityById(var_6_43).GetSeriesData()

			assert(var_6_44)

			local var_6_45 = var_6_44.GetStaegLevel() + 1
			local var_6_46 = var_6_44.GetExpeditionIds()
			local var_6_47 = var_6_0.getCurrentContext().getContextByMediator(ContinuousOperationMediator)
			local var_6_48 = not var_6_47 or var_6_47.data.autoFlag

			if var_6_0.getCurrentContext().getContextByMediator(ContinuousOperationMediator):
				local var_6_49 = pg.GuildMsgBoxMgr.GetInstance()

				if var_6_49.GetShouldShowBattleTip():
					local var_6_50 = getProxy(GuildProxy).getRawData()
					local var_6_51 = var_6_50 and var_6_50.getWeeklyTask()

					if var_6_51 and var_6_51.id != 0:
						var_6_49.SubmitTask(function(arg_11_0, arg_11_1)
							if arg_11_1:
								var_6_49.CancelShouldShowBattleTip())

			if not var_6_42 or var_6_45 > #var_6_46 or not var_6_48:
				local var_6_52 = var_6_0.GetPrevContext(1)
				local var_6_53 = var_6_52.getContextByMediator(BossRushPreCombatMediator)

				if var_6_53:
					var_6_52.removeChild(var_6_53)

				local var_6_54 = var_6_52.getContextByMediator(BossRushFleetSelectMediator)

				if var_6_54:
					var_6_52.removeChild(var_6_54)

				arg_1_0.sendNotification(GAME.BOSSRUSH_SETTLE, {
					actId = arg_1_0.contextData.actId
				})
			else
				seriesAsync({
					function(arg_12_0)
						arg_1_0.addSubLayers(Context.New({
							mediator = ChallengePassedMediator,
							viewComponent = BossRushPassedLayer,
							data = {
								curIndex = var_6_45 - 1,
								maxIndex = #var_6_46
							},
							onRemoved = arg_12_0
						})),
					function(arg_13_0)
						arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
							system = arg_1_0.contextData.system,
							actId = var_6_43,
							continuousBattleTimes = arg_1_0.contextData.continuousBattleTimes,
							totalBattleTimes = arg_1_0.contextData.totalBattleTimes
						})
				})

			return
		elif var_1_5 == SYSTEM_CARDPUZZLE:
			-- block empty
		elif var_1_5 == SYSTEM_BOSS_SINGLE:
			local var_6_55, var_6_56 = var_6_0.getContextByMediator(PreCombatMediator)

			if var_6_55:
				var_6_56.removeChild(var_6_55)

			if var_6_0.getCurrentContext().getContextByMediator(BossSingleContinuousOperationMediator):
				arg_1_0.sendNotification(BossSingleContinuousOperationMediator.CONTINUE_OPERATION)
				existCall(arg_1_0.viewComponent.HideConfirmPanel, arg_1_0.viewComponent)

				local var_6_57 = getProxy(ActivityProxy).getActivityById(arg_1_0.contextData.actId)
				local var_6_58 = getProxy(FleetProxy).getActivityFleets()[arg_1_0.contextData.actId]
				local var_6_59 = 0
				local var_6_60 = var_6_57.GetOilLimits()[arg_1_0.contextData.mainFleetId]

				local function var_6_61(arg_14_0, arg_14_1)
					local var_14_0 = arg_14_0.GetCostSum().oil

					if arg_14_1 > 0:
						var_14_0 = math.min(var_14_0, arg_14_1)

					var_6_59 = var_6_59 + var_14_0

				var_6_61(var_6_58[arg_1_0.contextData.mainFleetId], var_6_60[1] or 0)
				var_6_61(var_6_58[arg_1_0.contextData.mainFleetId + 10], var_6_60[2] or 0)

				if var_6_59 > getProxy(PlayerProxy).getRawData().oil:
					local var_6_62 = i18n("multiple_sorties_stop_reason1")

					arg_1_0.DisplayBossSingleTotalReward(var_6_62)

					return

				if getProxy(BayProxy).getShipCount() >= getProxy(PlayerProxy).getRawData().getMaxShipBag():
					local var_6_63 = i18n("multiple_sorties_stop_reason3")

					arg_1_0.DisplayBossSingleTotalReward(var_6_63)

					return

				local var_6_64 = var_6_58[arg_1_0.contextData.mainFleetId]
				local var_6_65 = _.map(_.values(var_6_64.ships), function(arg_15_0)
					local var_15_0 = getProxy(BayProxy).getShipById(arg_15_0)

					if var_15_0 and var_15_0.energy == Ship.ENERGY_LOW:
						return var_15_0)

				if #var_6_65 > 0:
					local var_6_66 = Fleet.DEFAULT_NAME_BOSS_ACT[arg_1_0.contextData.mainFleetId]
					local var_6_67 = _.map(var_6_65, function(arg_16_0)
						return "「" .. arg_16_0.getConfig("name") .. "」")
					local var_6_68 = i18n("multiple_sorties_stop_reason2", var_6_66, table.concat(var_6_67, ""))

					arg_1_0.DisplayBossSingleTotalReward(var_6_68)

					return

				if arg_1_0.contextData.statistics._battleScore <= ys.Battle.BattleConst.BattleScore.C:
					local var_6_69 = i18n("multiple_sorties_stop_reason4")

					arg_1_0.DisplayBossSingleTotalReward(var_6_69)

					return

				local var_6_70 = pg.GuildMsgBoxMgr.GetInstance()

				if var_6_70.GetShouldShowBattleTip():
					local var_6_71 = getProxy(GuildProxy).getRawData()
					local var_6_72 = var_6_71 and var_6_71.getWeeklyTask()

					if var_6_72 and var_6_72.id != 0:
						var_6_70.SubmitTask(function(arg_17_0, arg_17_1)
							if arg_17_1:
								var_6_70.CancelShouldShowBattleTip())

				local var_6_73 = var_6_0.getCurrentContext().getContextByMediator(BossSingleContinuousOperationMediator)

				if var_6_73 and not var_6_73.data.autoFlag:
					arg_1_0.DisplayBossSingleTotalReward()

					return

				if arg_1_0.contextData.continuousBattleTimes < 1:
					arg_1_0.DisplayBossSingleTotalReward()

					return

				arg_1_0.sendNotification(BattleResultMediator.ON_COMPLETE_BATTLE_RESULT)

				return
		else
			local var_6_74 = var_6_0.getContextByMediator(LevelMediator2)

			if var_6_74:
				local var_6_75 = var_6_74.getContextByMediator(PreCombatMediator)

				var_6_74.removeChild(var_6_75)

		arg_1_0.sendNotification(GAME.GO_BACK))
	arg_1_0.bind(var_0_0.ON_GO_TO_MAIN_SCENE, function(arg_18_0)
		arg_1_0.sendNotification(GAME.CHANGE_SCENE, SCENE.MAINUI))
	arg_1_0.bind(var_0_0.ON_GO_TO_TASK_SCENE, function(arg_19_0)
		local var_19_0 = getProxy(ContextProxy).getContextByMediator(LevelMediator2)

		if var_19_0:
			local var_19_1 = var_19_0.getContextByMediator(PreCombatMediator)

			var_19_0.removeChild(var_19_1)

		arg_1_0.sendNotification(GAME.CHANGE_SCENE, SCENE.TASK))
	arg_1_0.bind(var_0_0.ON_BACK_TO_DUEL_SCENE, function(arg_20_0)
		local var_20_0 = getProxy(ContextProxy).getContextByMediator(MilitaryExerciseMediator)

		if var_20_0:
			local var_20_1 = var_20_0.getContextByMediator(ExercisePreCombatMediator)

			var_20_0.removeChild(var_20_1)

		arg_1_0.sendNotification(GAME.GO_BACK))
	arg_1_0.bind(var_0_0.GET_NEW_SHIP, function(arg_21_0, arg_21_1, arg_21_2, arg_21_3)
		arg_1_0.addSubLayers(Context.New({
			mediator = NewShipMediator,
			viewComponent = NewShipLayer,
			data = {
				ship = arg_21_1,
				autoExitTime = arg_21_3
			},
			onRemoved = arg_21_2
		})))
	arg_1_0.bind(var_0_0.OPEN_FAIL_TIP_LAYER, function(arg_22_0)
		setActive(arg_1_0.viewComponent._tf, False)
		arg_1_0.addSubLayers(Context.New({
			mediator = BattleFailTipMediator,
			viewComponent = BattleFailTipLayer,
			data = {
				mainShips = var_1_12,
				battleSystem = arg_1_0.contextData.system
			},
			def onRemoved:()
				arg_1_0.viewComponent.emit(BattleResultMediator.ON_BACK_TO_DUEL_SCENE)
		})))
	arg_1_0.bind(var_0_0.DIRECT_EXIT, function(arg_24_0, arg_24_1)
		arg_1_0.sendNotification(GAME.GO_BACK))
	arg_1_0.bind(var_0_0.REENTER_STAGE, function(arg_25_0)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			stageId = arg_1_0.contextData.stageId,
			mainFleetId = arg_1_0.contextData.mainFleetId,
			system = arg_1_0.contextData.system,
			actId = arg_1_0.contextData.actId,
			rivalId = arg_1_0.contextData.rivalId,
			continuousBattleTimes = arg_1_0.contextData.continuousBattleTimes,
			totalBattleTimes = arg_1_0.contextData.totalBattleTimes
		}))
	arg_1_0.bind(var_0_0.PRE_BATTLE_FAIL_EXIT, function(arg_26_0)
		if var_1_5 == SYSTEM_SCENARIO:
			getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.BATTLE_FAILED))
	arg_1_0.bind(GAME.ACT_BOSS_EXCHANGE_TICKET, function(arg_27_0, arg_27_1)
		arg_1_0.sendNotification(GAME.ACT_BOSS_EXCHANGE_TICKET, {
			stageId = arg_27_1
		}))

	local var_1_44 = 0

	if var_1_12:
		for iter_1_18, iter_1_19 in ipairs(var_1_12):
			var_1_44 = iter_1_19.getBattleTotalExpend() + var_1_44

	originalPrint("耗时：", arg_1_0.contextData.statistics._totalTime, "秒")
	originalPrint("编队基础油耗：", var_1_44)

	if arg_1_0.contextData.statistics._enemyInfoList:
		for iter_1_20, iter_1_21 in pairs(arg_1_0.contextData.statistics._enemyInfoList):
			originalPrint("目标ID>>", iter_1_21.id, "<< 受到伤害共 >>", iter_1_21.damage, "<< 点")

	local var_1_45 = False

	if var_1_5 == SYSTEM_SCENARIO:
		local var_1_46 = var_1_3.getActiveChapter()

		var_1_45 = getProxy(ChapterProxy).GetChapterAutoFlag(var_1_46.id) == 1
	elif var_1_5 == SYSTEM_WORLD:
		var_1_45 = nowWorld().isAutoFight

	local var_1_47 = PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0) > 0

	if ys.Battle.BattleState.IsAutoBotActive() and var_1_47 and not var_1_45:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_AUTO_BATTLE)
		LuaHelper.Vibrate()

	arg_1_0.sendNotification(var_0_0.ON_ENTER_BATTLE_RESULT)

def var_0_0.showExtraChapterActSocre(arg_28_0):
	local var_28_0 = getProxy(ActivityProxy)
	local var_28_1 = var_28_0.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_EXTRA_CHAPTER_RANK)
	local var_28_2 = getProxy(ChapterProxy)
	local var_28_3 = var_28_2.getActiveChapter()
	local var_28_4 = var_28_3 and var_28_2.getMapById(var_28_3.getConfig("map"))

	for iter_28_0, iter_28_1 in ipairs(var_28_1):
		if iter_28_1 and not iter_28_1.isEnd():
			local var_28_5 = iter_28_1.getConfig("config_data")
			local var_28_6 = arg_28_0.contextData.stageId

			if var_28_5[1] == var_28_6 and var_28_4 and var_28_4.isActExtra():
				local var_28_7 = math.floor(arg_28_0.contextData.statistics._totalTime)
				local var_28_8 = ActivityLevelConst.getShipsPower(arg_28_0.contextData.prefabFleet or arg_28_0.contextData.oldMainShips)
				local var_28_9, var_28_10 = ActivityLevelConst.getExtraChapterSocre(var_28_6, var_28_7, var_28_8, iter_28_1)
				local var_28_11 = var_28_10 < var_28_9 and i18n("extra_chapter_record_updated") or i18n("extra_chapter_record_not_updated")

				if var_28_10 < var_28_9:
					iter_28_1.data1 = var_28_9

					var_28_0.updateActivity(iter_28_1)

					var_28_10 = var_28_9

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					hideNo = True,
					content = i18n("extra_chapter_socre_tip", var_28_9, var_28_10, var_28_11),
					weight = LayerWeightConst.SECOND_LAYER
				})

def var_0_0.listNotificationInterests(arg_29_0):
	return {
		GAME.BEGIN_STAGE_DONE,
		GAME.ACT_BOSS_EXCHANGE_TICKET_DONE,
		ContinuousOperationMediator.CONTINUE_OPERATION,
		var_0_0.SET_SKIP_FLAG,
		GAME.BOSSRUSH_SETTLE_DONE,
		ContinuousOperationMediator.ON_REENTER,
		BossSingleContinuousOperationMediator.CONTINUE_OPERATION,
		BossSingleContinuousOperationMediator.ON_REENTER
	}

def var_0_0.handleNotification(arg_30_0, arg_30_1):
	local var_30_0 = arg_30_1.getName()
	local var_30_1 = arg_30_1.getBody()

	if var_30_0 == GAME.BEGIN_STAGE_DONE:
		arg_30_0.sendNotification(GAME.CHANGE_SCENE, SCENE.COMBATLOAD, var_30_1)
	elif var_30_0 == GAME.ACT_BOSS_EXCHANGE_TICKET_DONE:
		existCall(arg_30_0.viewComponent.OnActBossExchangeTicket, arg_30_0.viewComponent)
	elif var_30_0 == var_0_0.SET_SKIP_FLAG:
		arg_30_0.viewComponent.SetSkipFlag(var_30_1)
	elif var_30_0 == ContinuousOperationMediator.CONTINUE_OPERATION:
		arg_30_0.contextData.continuousBattleTimes = arg_30_0.contextData.continuousBattleTimes - 1
	elif var_30_0 == GAME.BOSSRUSH_SETTLE_DONE:
		local var_30_2 = arg_30_0.contextData.system
		local var_30_3 = arg_30_0.contextData.actId
		local var_30_4 = var_30_1.seriesData
		local var_30_5 = arg_30_0.contextData.score > ys.Battle.BattleConst.BattleScore.C

		if not var_30_5 and var_30_2 == SYSTEM_BOSS_RUSH_EX:
			arg_30_0.viewComponent.emit(BattleResultMediator.OPEN_FAIL_TIP_LAYER)

			return

		local var_30_6 = var_30_2 == SYSTEM_BOSS_RUSH and BossRushBattleResultMediator or BossRushBattleResultMediator
		local var_30_7 = var_30_2 == SYSTEM_BOSS_RUSH and BossRushBattleResultLayer or BossRushEXBattleResultLayer

		arg_30_0.addSubLayers(Context.New({
			mediator = var_30_6,
			viewComponent = var_30_7,
			data = {
				awards = var_30_1.awards,
				system = arg_30_0.contextData.system,
				actId = var_30_3,
				seriesData = var_30_4,
				win = var_30_5
			}
		}), True)
		arg_30_0.viewComponent.closeView()
	elif var_30_0 == ContinuousOperationMediator.ON_REENTER:
		if not var_30_1.autoFlag:
			arg_30_0.DisplayTotalReward()

			return

		local var_30_8 = getProxy(ActivityProxy).getActivityById(arg_30_0.contextData.actId)
		local var_30_9 = var_30_8.getConfig("config_id")
		local var_30_10 = pg.activity_event_worldboss[var_30_9].ticket
		local var_30_11 = getProxy(PlayerProxy).getRawData().getResource(var_30_10)

		if var_30_8.GetStageBonus(arg_30_0.contextData.stageId) == 0 and getProxy(SettingsProxy).isTipActBossExchangeTicket() == 1 and var_30_11 > 0:
			arg_30_0.sendNotification(GAME.ACT_BOSS_EXCHANGE_TICKET, {
				stageId = arg_30_0.contextData.stageId
			})

			return

		arg_30_0.viewComponent.emit(var_0_0.REENTER_STAGE)
	elif var_30_0 == BossSingleContinuousOperationMediator.CONTINUE_OPERATION:
		arg_30_0.contextData.continuousBattleTimes = arg_30_0.contextData.continuousBattleTimes - 1
	elif var_30_0 == BossSingleContinuousOperationMediator.ON_REENTER:
		if not var_30_1.autoFlag:
			arg_30_0.DisplayBossSingleTotalReward()

			return

		arg_30_0.viewComponent.emit(var_0_0.REENTER_STAGE)

def var_0_0.DisplayTotalReward(arg_31_0, arg_31_1):
	local var_31_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(ContinuousOperationMediator)
	local var_31_1 = var_31_0 and var_31_0.data.autoFlag or None
	local var_31_2 = getProxy(ChapterProxy).PopActBossRewards()

	LoadContextCommand.LoadLayerOnTopContext(Context.New({
		mediator = ActivityBossTotalRewardPanelMediator,
		viewComponent = ActivityBossTotalRewardPanel,
		data = {
			def onClose:()
				arg_31_0.viewComponent.emit(BaseUI.ON_BACK),
			stopReason = arg_31_1,
			rewards = var_31_2,
			isAutoFight = var_31_1,
			continuousBattleTimes = arg_31_0.contextData.continuousBattleTimes,
			totalBattleTimes = arg_31_0.contextData.totalBattleTimes
		}
	}))

def var_0_0.DisplayBossSingleTotalReward(arg_33_0, arg_33_1):
	local var_33_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(BossSingleContinuousOperationMediator)
	local var_33_1 = var_33_0 and var_33_0.data.autoFlag or None
	local var_33_2 = getProxy(ChapterProxy).PopBossSingleRewards()

	LoadContextCommand.LoadLayerOnTopContext(Context.New({
		mediator = BossSingleTotalRewardPanelMediator,
		viewComponent = BossSingleTotalRewardPanel,
		data = {
			def onClose:()
				arg_33_0.viewComponent.emit(BaseUI.ON_BACK),
			stopReason = arg_33_1,
			rewards = var_33_2,
			isAutoFight = var_33_1,
			continuousBattleTimes = arg_33_0.contextData.continuousBattleTimes,
			totalBattleTimes = arg_33_0.contextData.totalBattleTimes
		}
	}))

def var_0_0.GetResultView(arg_35_0):
	var_0_0.RESULT_VIEW_TRANSFORM = var_0_0.RESULT_VIEW_TRANSFORM or {
		[SYSTEM_CHALLENGE] = BattleChallengeResultLayer,
		[SYSTEM_DODGEM] = BattleDodgemResultLayer,
		[SYSTEM_SUBMARINE_RUN] = BattleSubmarineRunResultLayer,
		[SYSTEM_SUB_ROUTINE] = BattleSubmarineRoutineResultLayer,
		[SYSTEM_HP_SHARE_ACT_BOSS] = BattleContributionResultLayer,
		[SYSTEM_BOSS_EXPERIMENT] = BattleExperimentResultLayer,
		[SYSTEM_ACT_BOSS] = BattleActivityBossResultLayer,
		[SYSTEM_WORLD_BOSS] = BattleWorldBossResultLayer,
		[SYSTEM_REWARD_PERFORM] = BattleRewardPerformResultLayer,
		[SYSTEM_AIRFIGHT] = BattleAirFightResultLayer,
		[SYSTEM_GUILD] = BattleGuildBossResultLayer,
		[SYSTEM_CARDPUZZLE] = BattleAirFightResultLayer
	}

	return var_0_0.RESULT_VIEW_TRANSFORM[arg_35_0] or BattleResultLayer

return var_0_0
