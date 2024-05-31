local var_0_0 = class("LevelMediator2", import("..base.ContextMediator"))

var_0_0.ON_TRACKING = "LevelMediator2.ON_TRACKING"
var_0_0.ON_ELITE_TRACKING = "LevelMediator2.ON_ELITE_TRACKING"
var_0_0.ON_RETRACKING = "LevelMediator2.ON_RETRACKING"
var_0_0.ON_UPDATE_CUSTOM_FLEET = "LevelMediator2.ON_UPDATE_CUSTOM_FLEET"
var_0_0.ON_OP = "LevelMediator2.ON_OP"
var_0_0.ON_RESUME_SUBSTATE = "LevelMediator2.ON_RESUME_SUBSTATE"
var_0_0.ON_STAGE = "LevelMediator2.ON_STAGE"
var_0_0.ON_GO_TO_TASK_SCENE = "LevelMediator2.ON_GO_TO_TASK_SCENE"
var_0_0.ON_OPEN_EVENT_SCENE = "LevelMediator2.ON_OPEN_EVENT_SCENE"
var_0_0.ON_DAILY_LEVEL = "LevelMediator2.ON_DAILY_LEVEL"
var_0_0.ON_OPEN_MILITARYEXERCISE = "LevelMediator2.ON_OPEN_MILLITARYEXERCISE"
var_0_0.ON_OVERRIDE_CHAPTER = "LevelMediator2.ON_OVERRIDE_CHAPTER"
var_0_0.ON_TIME_UP = "LevelMediator2.ON_TIME_UP"
var_0_0.UPDATE_EVENT_LIST = "LevelMediator2.UPDATE_EVENT_LIST"
var_0_0.ON_START = "ON_START"
var_0_0.ON_ENTER_MAINLEVEL = "LevelMediator2.ON_ENTER_MAINLEVEL"
var_0_0.ON_DIDENTER = "LevelMediator2.ON_DIDENTER"
var_0_0.ON_PERFORM_COMBAT = "LevelMediator2.ON_PERFORM_COMBAT"
var_0_0.ON_ELITE_OEPN_DECK = "LevelMediator2.ON_ELITE_OEPN_DECK"
var_0_0.ON_ELITE_CLEAR = "LevelMediator2.ON_ELITE_CLEAR"
var_0_0.ON_ELITE_RECOMMEND = "LevelMediator2.ON_ELITE_RECOMMEND"
var_0_0.ON_ELITE_ADJUSTMENT = "LevelMediator2.ON_ELITE_ADJUSTMENT"
var_0_0.ON_SUPPORT_OPEN_DECK = "LevelMediator2.ON_SUPPORT_OPEN_DECK"
var_0_0.ON_SUPPORT_CLEAR = "LevelMediator2.ON_SUPPORT_CLEAR"
var_0_0.ON_SUPPORT_RECOMMEND = "LevelMediator2.ON_SUPPORT_RECOMMEND"
var_0_0.ON_ACTIVITY_MAP = "LevelMediator2.ON_ACTIVITY_MAP"
var_0_0.GO_ACT_SHOP = "LevelMediator2.GO_ACT_SHOP"
var_0_0.ON_SWITCH_NORMAL_MAP = "LevelMediator2.ON_SWITCH_NORMAL_MAP"
var_0_0.NOTICE_AUTOBOT_ENABLED = "LevelMediator2.NOTICE_AUTOBOT_ENABLED"
var_0_0.ON_EXTRA_RANK = "LevelMediator2.ON_EXTRA_RANK"
var_0_0.ON_STRATEGYING_CHAPTER = "LevelMediator2.ON_STRATEGYING_CHAPTER"
var_0_0.ON_SELECT_COMMANDER = "LevelMediator2.ON_SELECT_COMMANDER"
var_0_0.ON_SELECT_ELITE_COMMANDER = "LevelMediator2.ON_SELECT_ELITE_COMMANDER"
var_0_0.ON_COMMANDER_SKILL = "LevelMediator2.ON_COMMANDER_SKILL"
var_0_0.ON_SHIP_DETAIL = "LevelMediator2.ON_SHIP_DETAIL"
var_0_0.ON_CLICK_RECEIVE_REMASTER_TICKETS_BTN = "LevelMediator2.ON_CLICK_RECEIVE_REMASTER_TICKETS_BTN"
var_0_0.GET_REMASTER_TICKETS_DONE = "LevelMediator2.GET_REMASTER_TICKETS_DONE"
var_0_0.ON_FLEET_SHIPINFO = "LevelMediator2.ON_FLEET_SHIPINFO"
var_0_0.ON_STAGE_SHIPINFO = "LevelMediator2.ON_STAGE_SHIPINFO"
var_0_0.ON_SUPPORT_SHIPINFO = "LevelMediator2.ON_SUPPORT_SHIPINFO"
var_0_0.ON_COMMANDER_OP = "LevelMediator2.ON_COMMANDER_OP"
var_0_0.CLICK_CHALLENGE_BTN = "LevelMediator2.CLICK_CHALLENGE_BTN"
var_0_0.ON_SUBMIT_TASK = "LevelMediator2.ON_SUBMIT_TASK"
var_0_0.ON_VOTE_BOOK = "LevelMediator2.ON_VOTE_BOOK"
var_0_0.GET_CHAPTER_DROP_SHIP_LIST = "LevelMediator2.GET_CHAPTER_DROP_SHIP_LIST"
var_0_0.ON_CHAPTER_REMASTER_AWARD = "LevelMediator2.ON_CHAPTER_REMASTER_AWARD"
var_0_0.ENTER_WORLD = "LevelMediator2.ENTER_WORLD"
var_0_0.ON_OPEN_ACT_BOSS_BATTLE = "LevelMediator2.ON_OPEN_ACT_BOSS_BATTLE"
var_0_0.ON_BOSSRUSH_MAP = "LevelMediator2.ON_BOSSRUSH_MAP"
var_0_0.SHOW_ATELIER_BUFF = "LevelMediator2.SHOW_ATELIER_BUFF"
var_0_0.ON_SPITEM_CHANGED = "LevelMediator2.ON_SPITEM_CHANGED"
var_0_0.ON_BOSSSINGLE_MAP = "LevelMediator2.ON_BOSSSINGLE_MAP"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.bind(var_0_0.GET_CHAPTER_DROP_SHIP_LIST, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.GET_CHAPTER_DROP_SHIP_LIST, {
			chapterId = arg_2_1,
			callback = arg_2_2
		}))
	arg_1_0.bind(var_0_0.ON_VOTE_BOOK, function(arg_3_0, arg_3_1)
		return)
	arg_1_0.bind(var_0_0.ON_COMMANDER_OP, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.contextData.commanderOPChapter = arg_4_2

		arg_1_0.sendNotification(GAME.COMMANDER_FORMATION_OP, {
			data = arg_4_1
		}))
	arg_1_0.bind(var_0_0.ON_SELECT_COMMANDER, function(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
		FormationMediator.onSelectCommander(arg_5_1, arg_5_2)

		arg_1_0.contextData.selectedChapterVO = arg_5_3)
	arg_1_0.bind(var_0_0.ON_SELECT_ELITE_COMMANDER, function(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
		local var_6_0 = getProxy(ChapterProxy)
		local var_6_1 = arg_6_3.id

		arg_1_0.contextData.editEliteChapter = var_6_1

		local var_6_2 = arg_6_3.getEliteFleetCommanders()[arg_6_1] or {}
		local var_6_3

		if var_6_2[arg_6_2]:
			local var_6_4 = getProxy(CommanderProxy).getCommanderById(var_6_2[arg_6_2])

		local var_6_5

		if var_6_2[arg_6_2]:
			var_6_5 = getProxy(CommanderProxy).getCommanderById(var_6_2[arg_6_2])

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.COMMANDERCAT, {
			maxCount = 1,
			mode = CommanderCatScene.MODE_SELECT,
			activeCommander = var_6_5,
			ignoredIds = {},
			fleetType = CommanderCatScene.FLEET_TYPE_HARD_CHAPTER,
			chapterId = var_6_1,
			def onCommander:(arg_7_0)
				return True,
			def onSelected:(arg_8_0, arg_8_1)
				local var_8_0 = arg_8_0[1]

				arg_1_0.sendNotification(GAME.SELECT_ELIT_CHAPTER_COMMANDER, {
					chapterId = var_6_1,
					index = arg_6_1,
					pos = arg_6_2,
					commanderId = var_8_0,
					def callback:()
						arg_8_1()
				}),
			def onQuit:(arg_10_0)
				arg_1_0.sendNotification(GAME.SELECT_ELIT_CHAPTER_COMMANDER, {
					chapterId = var_6_1,
					index = arg_6_1,
					pos = arg_6_2,
					def callback:()
						arg_10_0()
				})
		}))
	arg_1_0.RegisterTrackEvent()
	arg_1_0.bind(var_0_0.ON_UPDATE_CUSTOM_FLEET, function(arg_12_0, arg_12_1)
		arg_1_0.sendNotification(GAME.UPDATE_CUSTOM_FLEET, {
			chapterId = arg_12_1.id
		}))
	arg_1_0.bind(var_0_0.ON_OP, function(arg_13_0, arg_13_1)
		arg_1_0.sendNotification(GAME.CHAPTER_OP, arg_13_1))
	arg_1_0.bind(var_0_0.ON_SWITCH_NORMAL_MAP, function(arg_14_0)
		local var_14_0 = getProxy(ChapterProxy)
		local var_14_1
		local var_14_2 = Map.lastMap and var_14_0.getMapById(Map.lastMap)

		if var_14_2 and var_14_2.isUnlock() and var_14_2.getMapType() == Map.SCENARIO:
			var_14_1 = Map.lastMap
		else
			var_14_1 = var_14_0.getLastUnlockMap().id

		if var_14_1:
			arg_1_0.viewComponent.setMap(var_14_1))
	arg_1_0.bind(var_0_0.ON_RESUME_SUBSTATE, function(arg_15_0, arg_15_1)
		arg_1_0.loadSubState(arg_15_1))
	arg_1_0.bind(var_0_0.ON_STAGE, function(arg_16_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChapterPreCombatMediator,
			viewComponent = ChapterPreCombatLayer
		}), False))
	arg_1_0.bind(var_0_0.ON_OPEN_MILITARYEXERCISE, function()
		if getProxy(ActivityProxy).getMilitaryExerciseActivity():
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.MILITARYEXERCISE)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_notStartOrEnd")))
	arg_1_0.bind(var_0_0.CLICK_CHALLENGE_BTN, function(arg_18_0)
		if LOCK_LIMIT_CHALLENGE:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.CHALLENGE_MAIN_SCENE)
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LIMIT_CHALLENGE))
	arg_1_0.bind(var_0_0.ON_DAILY_LEVEL, function(arg_19_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DAILYLEVEL))
	arg_1_0.bind(var_0_0.ON_GO_TO_TASK_SCENE, function(arg_20_0, arg_20_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.TASK, arg_20_1))
	arg_1_0.bind(var_0_0.ON_OPEN_EVENT_SCENE, function()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EVENT))
	arg_1_0.bind(var_0_0.ON_OVERRIDE_CHAPTER, function()
		local var_22_0 = arg_1_0.contextData.chapterVO

		getProxy(ChapterProxy).updateChapter(var_22_0))
	arg_1_0.bind(var_0_0.ON_TIME_UP, function()
		arg_1_0.onTimeUp())
	arg_1_0.bind(var_0_0.UPDATE_EVENT_LIST, function()
		arg_1_0.viewComponent.addbubbleMsgBox(function(arg_25_0)
			arg_1_0.OnEventUpdate(arg_25_0))

		local var_24_0 = getProxy(ChapterProxy).getActiveChapter(True)

		if var_24_0 and var_24_0.IsAutoFight():
			local var_24_1 = pg.GuildMsgBoxMgr.GetInstance()

			if var_24_1.GetShouldShowBattleTip():
				local var_24_2 = getProxy(GuildProxy).getRawData()
				local var_24_3 = var_24_2 and var_24_2.getWeeklyTask()

				if var_24_3 and var_24_3.id != 0:
					getProxy(ChapterProxy).AddExtendChapterDataTable(var_24_0.id, "ListGuildEventNotify", var_24_3.GetPresonTaskId(), var_24_3.GetPrivateTaskName())
					pg.GuildMsgBoxMgr.GetInstance().CancelShouldShowBattleTip()

				var_24_1.SubmitTask(function(arg_26_0, arg_26_1, arg_26_2)
					if arg_26_0:
						local var_26_0 = pg.task_data_template[arg_26_2].desc

						getProxy(ChapterProxy).AddExtendChapterDataTable(var_24_0.id, "ListGuildEventAutoReceiveNotify", arg_26_2, var_26_0))
		else
			arg_1_0.viewComponent.addbubbleMsgBox(function(arg_27_0)
				pg.GuildMsgBoxMgr.GetInstance().NotificationForBattle(arg_27_0)))
	arg_1_0.bind(var_0_0.ON_ELITE_CLEAR, function(arg_28_0, arg_28_1)
		local var_28_0 = arg_28_1.index
		local var_28_1 = arg_28_1.chapterVO

		var_28_1.clearEliterFleetByIndex(var_28_0)

		local var_28_2 = getProxy(ChapterProxy)

		var_28_2.updateChapter(var_28_1)
		var_28_2.duplicateEliteFleet(var_28_1)
		arg_1_0.viewComponent.RefreshFleetSelectView(var_28_1))
	arg_1_0.bind(var_0_0.NOTICE_AUTOBOT_ENABLED, function(arg_29_0, arg_29_1)
		arg_1_0.sendNotification(GAME.COMMON_FLAG, {
			flagID = BATTLE_AUTO_ENABLED
		}))
	arg_1_0.bind(var_0_0.ON_ELITE_RECOMMEND, function(arg_30_0, arg_30_1)
		local var_30_0 = arg_30_1.index
		local var_30_1 = arg_30_1.chapterVO
		local var_30_2 = getProxy(ChapterProxy)

		var_30_2.eliteFleetRecommend(var_30_1, var_30_0)
		var_30_2.updateChapter(var_30_1)
		var_30_2.duplicateEliteFleet(var_30_1)
		arg_1_0.viewComponent.RefreshFleetSelectView(var_30_1))
	arg_1_0.bind(var_0_0.ON_ELITE_ADJUSTMENT, function(arg_31_0, arg_31_1)
		local var_31_0 = getProxy(ChapterProxy)

		var_31_0.updateChapter(arg_31_1)
		var_31_0.duplicateEliteFleet(arg_31_1))
	arg_1_0.bind(var_0_0.ON_ELITE_OEPN_DECK, function(arg_32_0, arg_32_1)
		local var_32_0 = arg_32_1.shipType
		local var_32_1 = arg_32_1.fleetIndex
		local var_32_2 = arg_32_1.shipVO
		local var_32_3 = arg_32_1.fleet
		local var_32_4 = arg_32_1.chapter
		local var_32_5 = arg_32_1.teamType
		local var_32_6 = getProxy(BayProxy).getRawData()
		local var_32_7 = {}

		for iter_32_0, iter_32_1 in pairs(var_32_6):
			if not ShipType.ContainInLimitBundle(var_32_0, iter_32_1.getShipType()):
				table.insert(var_32_7, iter_32_0)

		arg_1_0.contextData.editEliteChapter = var_32_4.id

		local var_32_8 = {}

		for iter_32_2, iter_32_3 in pairs(var_32_3):
			table.insert(var_32_8, iter_32_2.id)

		local var_32_9, var_32_10, var_32_11 = arg_1_0.getDockCallbackFuncs(var_32_3, var_32_2, var_32_4, var_32_1)

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			useBlackBlock = True,
			selectedMin = 0,
			energyDisplay = True,
			ignoredIds = var_32_7,
			leastLimitMsg = i18n("ship_formationMediator_leastLimit"),
			quitTeam = var_32_2 != None,
			teamFilter = var_32_5,
			leftTopInfo = i18n("word_formation"),
			onShip = var_32_9,
			confirmSelect = var_32_10,
			onSelected = var_32_11,
			hideTagFlags = setmetatable({
				inElite = var_32_4.getConfig("formation")
			}, {
				__index = ShipStatus.TAG_HIDE_LEVEL
			}),
			otherSelectedIds = var_32_8
		}))
	arg_1_0.bind(var_0_0.ON_SUPPORT_OPEN_DECK, function(arg_33_0, arg_33_1)
		local var_33_0 = arg_33_1.shipType
		local var_33_1 = arg_33_1.shipVO
		local var_33_2 = arg_33_1.fleet
		local var_33_3 = arg_33_1.chapter
		local var_33_4 = arg_33_1.teamType
		local var_33_5 = getProxy(BayProxy).getRawData()
		local var_33_6 = {}

		for iter_33_0, iter_33_1 in pairs(var_33_5):
			if not ShipType.ContainInLimitBundle(var_33_0, iter_33_1.getShipType()):
				table.insert(var_33_6, iter_33_0)

		local var_33_7 = {}

		for iter_33_2, iter_33_3 in pairs(var_33_2):
			table.insert(var_33_7, iter_33_2.id)

		local var_33_8, var_33_9, var_33_10 = arg_1_0.getSupportDockCallbackFuncs(var_33_2, var_33_1, var_33_3)

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			useBlackBlock = True,
			selectedMin = 0,
			energyDisplay = True,
			ignoredIds = var_33_6,
			leastLimitMsg = i18n("ship_formationMediator_leastLimit"),
			quitTeam = var_33_1 != None,
			teamFilter = var_33_4,
			leftTopInfo = i18n("word_formation"),
			onShip = var_33_8,
			confirmSelect = var_33_9,
			onSelected = var_33_10,
			hideTagFlags = setmetatable({
				inSupport = var_33_3.getConfig("formation")
			}, {
				__index = ShipStatus.TAG_HIDE_SUPPORT
			}),
			otherSelectedIds = var_33_7
		})

		arg_1_0.contextData.selectedChapterVO = var_33_3)
	arg_1_0.bind(var_0_0.ON_SUPPORT_CLEAR, function(arg_34_0, arg_34_1)
		local var_34_0 = arg_34_1.index
		local var_34_1 = arg_34_1.chapterVO

		var_34_1.ClearSupportFleetList(var_34_0)

		local var_34_2 = getProxy(ChapterProxy)

		var_34_2.updateChapter(var_34_1)
		var_34_2.duplicateSupportFleet(var_34_1)
		arg_1_0.viewComponent.RefreshFleetSelectView(var_34_1))
	arg_1_0.bind(var_0_0.ON_SUPPORT_RECOMMEND, function(arg_35_0, arg_35_1)
		local var_35_0 = arg_35_1.index
		local var_35_1 = arg_35_1.chapterVO
		local var_35_2 = getProxy(ChapterProxy)

		var_35_2.SupportFleetRecommend(var_35_1, var_35_0)
		var_35_2.updateChapter(var_35_1)
		var_35_2.duplicateSupportFleet(var_35_1)
		arg_1_0.viewComponent.RefreshFleetSelectView(var_35_1))
	arg_1_0.bind(var_0_0.ON_ACTIVITY_MAP, function()
		local var_36_0 = getProxy(ChapterProxy)
		local var_36_1, var_36_2 = var_36_0.getLastMapForActivity()

		if not var_36_1 or not var_36_0.getMapById(var_36_1).isUnlock():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		arg_1_0.viewComponent.ShowSelectedMap(var_36_1, function()
			if var_36_2:
				local var_37_0 = var_36_0.getChapterById(var_36_2)

				arg_1_0.viewComponent.switchToChapter(var_37_0)))
	arg_1_0.bind(var_0_0.ON_BOSSRUSH_MAP, function()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.BOSSRUSH_MAIN))
	arg_1_0.bind(var_0_0.ON_BOSSSINGLE_MAP, function(arg_39_0, arg_39_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.OTHERWORLD_MAP, arg_39_1))
	arg_1_0.bind(var_0_0.GO_ACT_SHOP, function()
		local var_40_0 = pg.gameset.activity_res_id.key_value
		local var_40_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_LOTTERY)

		if var_40_1 and var_40_1.getConfig("config_client").resId == var_40_0 and not var_40_1.isEnd():
			arg_1_0.addSubLayers(Context.New({
				mediator = LotteryMediator,
				viewComponent = LotteryLayer,
				data = {
					activityId = var_40_1.id
				}
			}), False)
		else
			local var_40_2 = _.detect(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP), function(arg_41_0)
				return arg_41_0.getConfig("config_client").pt_id == var_40_0)
			local var_40_3 = var_40_2 and var_40_2.id

			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
				warp = NewShopsScene.TYPE_ACTIVITY,
				actId = var_40_3
			}))
	arg_1_0.bind(var_0_0.SHOW_ATELIER_BUFF, function(arg_42_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = AtelierBuffMediator,
			viewComponent = AtelierBuffLayer
		})))
	arg_1_0.bind(var_0_0.ON_SHIP_DETAIL, function(arg_43_0, arg_43_1)
		arg_1_0.contextData.selectedChapterVO = arg_43_1.chapter

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_43_1.id
		}))
	arg_1_0.bind(var_0_0.ON_FLEET_SHIPINFO, function(arg_44_0, arg_44_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_44_1.shipId,
			shipVOs = arg_44_1.shipVOs
		})

		arg_1_0.contextData.editEliteChapter = arg_44_1.chapter.id)
	arg_1_0.bind(var_0_0.ON_SUPPORT_SHIPINFO, function(arg_45_0, arg_45_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_45_1.shipId,
			shipVOs = arg_45_1.shipVOs
		})

		arg_1_0.contextData.selectedChapterVO = arg_45_1.chapter)
	arg_1_0.bind(var_0_0.ON_STAGE_SHIPINFO, function(arg_46_0, arg_46_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_46_1.shipId,
			shipVOs = arg_46_1.shipVOs
		}))
	arg_1_0.bind(var_0_0.ON_EXTRA_RANK, function(arg_47_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.BILLBOARD, {
			page = PowerRank.TYPE_EXTRA_CHAPTER
		}))
	arg_1_0.bind(var_0_0.ON_STRATEGYING_CHAPTER, function(arg_48_0)
		local var_48_0 = getProxy(ChapterProxy)
		local var_48_1 = var_48_0.getActiveChapter()

		assert(var_48_1)

		local var_48_2 = var_48_0.getMapById(var_48_1.getConfig("map"))

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			yesText = "text_forward",
			content = i18n("levelScene_chapter_is_activation", string.split(var_48_2.getConfig("name"), "|")[1] .. "." .. var_48_1.getConfig("chapter_name")),
			def onYes:()
				arg_1_0.viewComponent.switchToChapter(var_48_1),
			def onNo:()
				arg_1_0.contextData.chapterVO = var_48_1

				arg_1_0.viewComponent.emit(LevelMediator2.ON_OP, {
					type = ChapterConst.OpRetreat,
					exittype = ChapterConst.ExitFromMap
				}),
			def onClose:()
				return,
			noBtnType = pg.MsgboxMgr.BUTTON_RETREAT
		}))
	arg_1_0.bind(var_0_0.ON_COMMANDER_SKILL, function(arg_52_0, arg_52_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = CommanderSkillMediator,
			viewComponent = CommanderSkillLayer,
			data = {
				skill = arg_52_1
			}
		})))
	arg_1_0.bind(var_0_0.ON_PERFORM_COMBAT, function(arg_53_0, arg_53_1, arg_53_2)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_PERFORM,
			stageId = arg_53_1,
			exitCallback = arg_53_2
		}))
	arg_1_0.bind(var_0_0.ON_CLICK_RECEIVE_REMASTER_TICKETS_BTN, function(arg_54_0)
		arg_1_0.sendNotification(GAME.GET_REMASTER_TICKETS))
	arg_1_0.bind(var_0_0.ON_SUBMIT_TASK, function(arg_55_0, arg_55_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_55_1))
	arg_1_0.bind(var_0_0.ON_START, function(arg_56_0)
		local var_56_0 = getProxy(ChapterProxy).getActiveChapter()

		assert(var_56_0)

		local var_56_1 = var_56_0.fleet
		local var_56_2 = var_56_0.getStageId(var_56_1.line.row, var_56_1.line.column)

		seriesAsync({
			function(arg_57_0)
				local var_57_0 = {}

				for iter_57_0, iter_57_1 in pairs(var_56_1.ships):
					table.insert(var_57_0, iter_57_1)

				Fleet.EnergyCheck(var_57_0, var_56_1.name, function(arg_58_0)
					if arg_58_0:
						arg_57_0(), function(arg_59_0)
					if not arg_59_0:
						getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.SHIP_ENERGY_LOW)),
			function(arg_60_0)
				if getProxy(PlayerProxy).getRawData().GoldMax(1):
					local var_60_0 = i18n("gold_max_tip_title") .. i18n("resource_max_tip_battle")

					getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.GOLD_MAX)
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = var_60_0,
						onYes = arg_60_0,
						weight = LayerWeightConst.SECOND_LAYER
					})
				else
					arg_60_0(),
			function(arg_61_0)
				arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
					system = SYSTEM_SCENARIO,
					stageId = var_56_2
				})
		}))
	arg_1_0.bind(arg_1_0.ON_ENTER_MAINLEVEL, function(arg_62_0, arg_62_1)
		arg_1_0.DidEnterLevelMainUI(arg_62_1))
	arg_1_0.bind(arg_1_0.ON_DIDENTER, function(arg_63_0)
		arg_1_0.viewComponent.emit(LevelMediator2.UPDATE_EVENT_LIST))
	arg_1_0.bind(var_0_0.ENTER_WORLD, function(arg_64_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.WORLD))
	arg_1_0.bind(var_0_0.ON_CHAPTER_REMASTER_AWARD, function(arg_65_0, arg_65_1, arg_65_2)
		arg_1_0.sendNotification(GAME.CHAPTER_REMASTER_AWARD_RECEIVE, {
			chapterId = arg_65_1,
			pos = arg_65_2
		}))
	arg_1_0.bind(var_0_0.ON_OPEN_ACT_BOSS_BATTLE, function(arg_66_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ACT_BOSS_BATTLE, {
			showAni = True
		}))
	arg_1_0.bind(LevelUIConst.OPEN_NORMAL_CONTINUOUS_WINDOW, function(arg_67_0, arg_67_1, arg_67_2, arg_67_3, arg_67_4)
		local var_67_0 = _.map(arg_67_2, function(arg_68_0)
			local var_68_0 = getProxy(FleetProxy).getFleetById(arg_68_0)

			if not var_68_0 or var_68_0.getFleetType() == FleetType.Submarine:
				return

			return var_68_0)

		arg_1_0.DisplayContinuousWindow(arg_67_1, var_67_0, arg_67_3, arg_67_4))
	arg_1_0.bind(LevelUIConst.OPEN_ELITE_CONTINUOUS_WINDOW, function(arg_69_0, arg_69_1, arg_69_2, arg_69_3)
		local var_69_0 = arg_69_1.getEliteFleetList()
		local var_69_1 = getProxy(BayProxy).getRawData()
		local var_69_2 = _.map(var_69_0, function(arg_70_0)
			if #arg_70_0 == 0 or _.any(arg_70_0, function(arg_71_0)
				local var_71_0 = var_69_1[arg_71_0]

				return var_71_0 and var_71_0.getTeamType() == TeamType.Submarine):
				return

			return TypedFleet.New({
				fleetType = FleetType.Normal,
				ship_list = arg_70_0
			}))

		arg_1_0.DisplayContinuousWindow(arg_69_1, var_69_2, arg_69_2, arg_69_3))

	arg_1_0.player = var_1_0.getData()

	arg_1_0.viewComponent.updateRes(arg_1_0.player)

	local var_1_1 = getProxy(EventProxy)

	arg_1_0.viewComponent.updateEvent(var_1_1)

	local var_1_2 = getProxy(FleetProxy).GetRegularFleets()

	arg_1_0.viewComponent.updateFleet(var_1_2)

	local var_1_3 = getProxy(BayProxy)

	arg_1_0.viewComponent.setShips(var_1_3.getRawData())

	local var_1_4 = getProxy(ActivityProxy)

	arg_1_0.viewComponent.updateVoteBookBtn()

	local var_1_5 = getProxy(CommanderProxy).getPrefabFleet()

	arg_1_0.viewComponent.setCommanderPrefabs(var_1_5)

	local var_1_6 = var_1_4.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_RANK)

	for iter_1_0, iter_1_1 in ipairs(var_1_6):
		if iter_1_1.getConfig("config_id") == pg.gameset.activity_res_id.key_value:
			arg_1_0.viewComponent.updatePtActivity(iter_1_1)

			break

	local var_1_7 = getProxy(DailyLevelProxy)

	arg_1_0.viewComponent.setEliteQuota(var_1_7.eliteCount, pg.gameset.elite_quota.key_value)
	getProxy(ChapterProxy).updateActiveChapterShips()

	local var_1_8 = getProxy(BagProxy).getItemsByType(Item.SPECIAL_OPERATION_TICKET)

	arg_1_0.viewComponent.setSpecialOperationTickets(var_1_8)

def var_0_0.DidEnterLevelMainUI(arg_72_0, arg_72_1):
	arg_72_0.viewComponent.setMap(arg_72_1)

	local var_72_0 = arg_72_0.contextData.chapterVO

	if var_72_0 and var_72_0.active:
		arg_72_0.viewComponent.switchToChapter(var_72_0)
	elif arg_72_0.contextData.map.isSkirmish():
		arg_72_0.viewComponent.ShowCurtains(True)
		arg_72_0.viewComponent.doPlayAnim("TV01", function(arg_73_0)
			go(arg_73_0).SetActive(False)
			arg_72_0.viewComponent.ShowCurtains(False))

	if arg_72_0.contextData.preparedTaskList and #arg_72_0.contextData.preparedTaskList > 0:
		for iter_72_0, iter_72_1 in ipairs(arg_72_0.contextData.preparedTaskList):
			arg_72_0.sendNotification(GAME.SUBMIT_TASK, iter_72_1)

		table.clean(arg_72_0.contextData.preparedTaskList)

	if arg_72_0.contextData.StopAutoFightFlag:
		local var_72_1 = getProxy(ChapterProxy)
		local var_72_2 = var_72_1.getActiveChapter()

		if var_72_2:
			var_72_1.SetChapterAutoFlag(var_72_2.id, False)

			local var_72_3 = bit.bor(ChapterConst.DirtyAttachment, ChapterConst.DirtyStrategy)

			arg_72_0.viewComponent.updateChapterVO(var_72_2, var_72_3)

		arg_72_0.contextData.StopAutoFightFlag = None

	if arg_72_0.contextData.ToTrackingData:
		arg_72_0.sendNotification(arg_72_0.contextData.ToTrackingData[1], arg_72_0.contextData.ToTrackingData[2])

		arg_72_0.contextData.ToTrackingData = None

def var_0_0.RegisterTrackEvent(arg_74_0):
	arg_74_0.bind(var_0_0.ON_TRACKING, function(arg_75_0, arg_75_1, arg_75_2, arg_75_3, arg_75_4, arg_75_5)
		local var_75_0 = getProxy(ChapterProxy).getChapterById(arg_75_1, True)
		local var_75_1 = getProxy(ChapterProxy).GetLastFleetIndex()

		arg_74_0.sendNotification(GAME.TRACKING, {
			chapterId = arg_75_1,
			fleetIds = var_75_1,
			loopFlag = arg_75_2,
			operationItem = arg_75_3,
			duties = arg_75_4,
			autoFightFlag = arg_75_5
		}))
	arg_74_0.bind(var_0_0.ON_ELITE_TRACKING, function(arg_76_0, arg_76_1, arg_76_2, arg_76_3, arg_76_4, arg_76_5)
		arg_74_0.sendNotification(GAME.TRACKING, {
			chapterId = arg_76_1,
			loopFlag = arg_76_2,
			operationItem = arg_76_3,
			duties = arg_76_4,
			autoFightFlag = arg_76_5
		}))
	arg_74_0.bind(var_0_0.ON_RETRACKING, function(arg_77_0, arg_77_1, arg_77_2)
		local var_77_0 = arg_77_1.duties
		local var_77_1 = arg_77_1.getConfig("type") == Chapter.CustomFleet
		local var_77_2 = arg_77_1.GetActiveSPItemID()

		if var_77_1:
			arg_74_0.viewComponent.emit(LevelMediator2.ON_ELITE_TRACKING, arg_77_1.id, arg_77_1.loopFlag, var_77_2, var_77_0, arg_77_2)
		else
			arg_74_0.viewComponent.emit(LevelMediator2.ON_TRACKING, arg_77_1.id, arg_77_1.loopFlag, var_77_2, var_77_0, arg_77_2))

def var_0_0.NoticeVoteBook(arg_78_0, arg_78_1):
	arg_78_1()

def var_0_0.TryPlaySubGuide(arg_79_0):
	arg_79_0.viewComponent.tryPlaySubGuide()

def var_0_0.listNotificationInterests(arg_80_0):
	return {
		ChapterProxy.CHAPTER_UPDATED,
		ChapterProxy.CHAPTER_TIMESUP,
		PlayerProxy.UPDATED,
		DailyLevelProxy.ELITE_QUOTA_UPDATE,
		var_0_0.ON_TRACKING,
		var_0_0.ON_ELITE_TRACKING,
		var_0_0.ON_RETRACKING,
		GAME.TRACKING_DONE,
		GAME.TRACKING_ERROR,
		GAME.CHAPTER_OP_DONE,
		GAME.EVENT_LIST_UPDATE,
		GAME.BEGIN_STAGE_DONE,
		ActivityProxy.ACTIVITY_OPERATION_DONE,
		ActivityProxy.ACTIVITY_UPDATED,
		GAME.SUB_CHAPTER_REFRESH_DONE,
		GAME.SUB_CHAPTER_FETCH_DONE,
		CommanderProxy.PREFAB_FLEET_UPDATE,
		GAME.COOMMANDER_EQUIP_TO_FLEET_DONE,
		GAME.COMMANDER_ELIT_FORMATION_OP_DONE,
		GAME.SUBMIT_TASK_DONE,
		LevelUIConst.CONTINUOUS_OPERATION,
		var_0_0.ON_SPITEM_CHANGED,
		GAME.GET_REMASTER_TICKETS_DONE,
		VoteProxy.VOTE_ORDER_BOOK_DELETE,
		VoteProxy.VOTE_ORDER_BOOK_UPDATE,
		GAME.VOTE_BOOK_BE_UPDATED_DONE,
		BagProxy.ITEM_UPDATED,
		ChapterProxy.CHAPTER_AUTO_FIGHT_FLAG_UPDATED,
		ChapterProxy.CHAPTER_SKIP_PRECOMBAT_UPDATED,
		ChapterProxy.CHAPTER_REMASTER_INFO_UPDATED,
		GAME.CHAPTER_REMASTER_INFO_REQUEST_DONE,
		GAME.CHAPTER_REMASTER_AWARD_RECEIVE_DONE,
		GAME.STORY_UPDATE_DONE,
		GAME.STORY_END
	}

def var_0_0.handleNotification(arg_81_0, arg_81_1):
	local var_81_0 = arg_81_1.getName()
	local var_81_1 = arg_81_1.getBody()

	if var_81_0 == GAME.BEGIN_STAGE_DONE:
		arg_81_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_81_1)
	elif var_81_0 == VoteProxy.VOTE_ORDER_BOOK_DELETE or VoteProxy.VOTE_ORDER_BOOK_UPDATE == var_81_0:
		arg_81_0.viewComponent.updateVoteBookBtn()
	elif var_81_0 == PlayerProxy.UPDATED:
		arg_81_0.viewComponent.updateRes(var_81_1)
	elif var_81_0 == var_0_0.ON_TRACKING or var_81_0 == var_0_0.ON_ELITE_TRACKING or var_81_0 == var_0_0.ON_RETRACKING:
		arg_81_0.viewComponent.emit(var_81_0, unpackEx(var_81_1))
	elif var_81_0 == GAME.TRACKING_DONE:
		arg_81_0.waitingTracking = None

		arg_81_0.viewComponent.resetLevelGrid()

		arg_81_0.viewComponent.FirstEnterChapter = var_81_1.id

		arg_81_0.viewComponent.switchToChapter(var_81_1)
	elif var_81_0 == ChapterProxy.CHAPTER_UPDATED:
		arg_81_0.viewComponent.updateChapterVO(var_81_1.chapter, var_81_1.dirty)
	elif var_81_0 == GAME.COMMANDER_ELIT_FORMATION_OP_DONE:
		if arg_81_0.contextData.commanderOPChapter:
			local var_81_2 = getProxy(ChapterProxy).getChapterById(var_81_1.chapterId)

			arg_81_0.contextData.commanderOPChapter.eliteCommanderList = var_81_2.eliteCommanderList

			arg_81_0.viewComponent.RefreshFleetSelectView(arg_81_0.contextData.commanderOPChapter)
	elif var_81_0 == GAME.CHAPTER_OP_DONE:
		local var_81_3

		local function var_81_4()
			if var_81_3 and coroutine.status(var_81_3) == "suspended":
				local var_82_0, var_82_1 = coroutine.resume(var_81_3)

				assert(var_82_0, debug.traceback(var_81_3, var_82_1))

		var_81_3 = coroutine.create(function()
			local var_83_0 = var_81_1.type
			local var_83_1 = arg_81_0.contextData.chapterVO
			local var_83_2 = var_83_1.IsAutoFight()

			if var_83_0 == ChapterConst.OpRetreat and not var_81_1.id:
				var_83_1 = var_81_1.finalChapterLevelData

				if var_81_1.exittype and var_81_1.exittype == ChapterConst.ExitFromMap:
					arg_81_0.viewComponent.setChapter(None)
					arg_81_0.viewComponent.updateChapterTF(var_83_1.id)
					arg_81_0.OnExitChapter(var_83_1, var_81_1.win, var_81_1.extendData)

					return

				if var_83_1.existOni():
					local var_83_3 = var_83_1.checkOniState()

					if var_83_3:
						arg_81_0.viewComponent.displaySpResult(var_83_3, var_81_4)
						coroutine.yield()

				if var_83_1.isPlayingWithBombEnemy():
					arg_81_0.viewComponent.displayBombResult(var_81_4)
					coroutine.yield()

			local var_83_4 = var_81_1.items
			local var_83_5

			if var_83_4 and #var_83_4 > 0:
				if var_83_0 == ChapterConst.OpBox:
					local var_83_6 = var_83_1.fleet.line
					local var_83_7 = var_83_1.getChapterCell(var_83_6.row, var_83_6.column)

					if pg.box_data_template[var_83_7.attachmentId].type == ChapterConst.BoxDrop and ChapterConst.IsAtelierMap(arg_81_0.contextData.map):
						local var_83_8 = _.filter(var_83_4, function(arg_84_0)
							return arg_84_0.type == DROP_TYPE_RYZA_DROP)

						if #var_83_8 > 0:
							var_83_5 = AwardInfoLayer.TITLE.RYZA

							local var_83_9 = math.random(#var_83_8)
							local var_83_10 = AtelierMaterial.New({
								configId = var_83_8[var_83_9].id
							}).GetVoices()

							if var_83_10 and #var_83_10 > 0:
								local var_83_11 = var_83_10[math.random(#var_83_10)]
								local var_83_12, var_83_13, var_83_14 = ShipWordHelper.GetWordAndCV(var_83_11[1], var_83_11[2], None, PLATFORM_CODE != PLATFORM_US)

								arg_81_0.viewComponent.emit(LevelUIConst.ADD_TOAST_QUEUE, {
									iconScale = 0.75,
									Class = LevelStageAtelierMaterialToast,
									title = i18n("ryza_tip_toast_item_got"),
									desc = var_83_14,
									voice = var_83_13,
									icon = var_83_11[3]
								})

				seriesAsync({
					function(arg_85_0)
						getProxy(ChapterProxy).AddExtendChapterDataArray(var_83_1.id, "TotalDrops", _.filter(var_83_4, function(arg_86_0)
							return arg_86_0.type != DROP_TYPE_STRATEGY))
						arg_81_0.viewComponent.emit(BaseUI.ON_WORLD_ACHIEVE, {
							items = var_83_4,
							title = var_83_5,
							closeOnCompleted = var_83_2,
							removeFunc = arg_85_0
						}),
					function(arg_87_0)
						if var_83_0 == ChapterConst.OpBox and _.any(var_83_4, function(arg_88_0)
							if arg_88_0.type != DROP_TYPE_VITEM:
								return False

							return arg_88_0.getConfig("virtual_type") == 1):
							(function()
								local var_89_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

								if not var_89_0:
									return

								local var_89_1 = pg.activity_event_picturepuzzle[var_89_0.id]

								if not var_89_1:
									return

								if #table.mergeArray(var_89_0.data1_list, var_89_0.data2_list, True) < #var_89_1.pickup_picturepuzzle + #var_89_1.drop_picturepuzzle:
									return

								local var_89_2 = var_89_0.getConfig("config_client").comStory

								pg.NewStoryMgr.GetInstance().Play(var_89_2, arg_87_0))()

						if _.any(var_83_4, function(arg_90_0)
							if arg_90_0.type != DROP_TYPE_STRATEGY:
								return False

							return pg.strategy_data_template[arg_90_0.id].type == ChapterConst.StgTypeConsume):
							arg_81_0.viewComponent.levelStageView.popStageStrategy()

						arg_87_0()
				}, var_81_4)
				coroutine.yield()

			assert(var_83_1)

			if var_83_0 == ChapterConst.OpSkipBattle or var_83_0 == ChapterConst.OpPreClear:
				arg_81_0.viewComponent.levelStageView.tryAutoAction(function()
					if not arg_81_0.viewComponent.levelStageView:
						return

					arg_81_0.viewComponent.levelStageView.tryAutoTrigger())
			elif var_83_0 == ChapterConst.OpRetreat:
				local var_83_15 = getProxy(ContextProxy).getContextByMediator(LevelMediator2)

				if var_83_15:
					local var_83_16 = {}
					local var_83_17 = var_83_15.getContextByMediator(ChapterPreCombatMediator)

					if var_83_17:
						table.insert(var_83_16, var_83_17)

					_.each(var_83_16, function(arg_92_0)
						arg_81_0.sendNotification(GAME.REMOVE_LAYERS, {
							context = arg_92_0
						}))

				if var_81_1.id:
					getProxy(ChapterProxy).StopAutoFight(ChapterConst.AUTOFIGHT_STOP_REASON.BATTLE_FAILED)

					return

				local var_83_18 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN)

				if var_83_18 and not var_83_18.autoActionForbidden and not var_83_18.achieved and var_83_18.data1 == 7 and var_83_1.id == 204 and var_83_1.isClear():
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						modal = True,
						hideNo = True,
						content = "有新的签到奖励可以领取，点击确定前往",
						def onYes:()
							arg_81_0.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY),
						def onNo:()
							arg_81_0.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY)
					})

					return

				arg_81_0.OnExitChapter(var_83_1, var_81_1.win, var_81_1.extendData)
			elif var_83_0 == ChapterConst.OpMove:
				seriesAsync({
					function(arg_95_0)
						var_83_1 = arg_81_0.contextData.chapterVO

						local var_95_0 = var_81_1.fullpath[#var_81_1.fullpath]

						var_83_1.fleet.line = Clone(var_95_0)

						getProxy(ChapterProxy).updateChapter(var_83_1)
						arg_81_0.viewComponent.grid.moveFleet(var_81_1.path, var_81_1.fullpath, var_81_1.oldLine, arg_95_0),
					function(arg_96_0)
						if not var_81_1.teleportPaths:
							arg_96_0()

							return

						local var_96_0 = var_81_1.teleportPaths[1]
						local var_96_1 = var_81_1.teleportPaths[2]

						if not var_96_0 or not var_96_1:
							arg_96_0()

							return

						var_83_1 = arg_81_0.contextData.chapterVO

						local var_96_2 = var_83_1.getFleet(FleetType.Normal, var_96_0.row, var_96_0.column)

						if not var_96_2:
							arg_96_0()

							return

						var_96_2.line = Clone(var_81_1.teleportPaths[2])

						getProxy(ChapterProxy).updateChapter(var_83_1)

						local var_96_3 = arg_81_0.getViewComponent().grid.GetCellFleet(var_96_2.id)

						arg_81_0.getViewComponent().grid.TeleportCellByPortalWithCameraMove(var_96_2, var_96_3, var_81_1.teleportPaths, arg_96_0),
					function(arg_97_0)
						arg_81_0.playAIActions(var_81_1.aiActs, var_81_1.extraFlag, arg_97_0)
				}, function()
					var_83_1 = arg_81_0.contextData.chapterVO

					local var_98_0 = var_83_1.fleet.getStrategies()

					if _.any(var_98_0, function(arg_99_0)
						return arg_99_0.id == ChapterConst.StrategyExchange and arg_99_0.count > 0):
						arg_81_0.viewComponent.levelStageView.popStageStrategy()

					arg_81_0.viewComponent.grid.updateQuadCells(ChapterConst.QuadStateNormal)
					arg_81_0.viewComponent.levelStageView.updateAmbushRate(var_83_1.fleet.line, True)
					arg_81_0.viewComponent.levelStageView.updateStageStrategy()
					arg_81_0.viewComponent.levelStageView.updateFleetBuff()
					arg_81_0.viewComponent.levelStageView.updateBombPanel()
					arg_81_0.viewComponent.levelStageView.tryAutoTrigger())
			elif var_83_0 == ChapterConst.OpAmbush:
				arg_81_0.viewComponent.levelStageView.tryAutoTrigger()
			elif var_83_0 == ChapterConst.OpBox:
				arg_81_0.playAIActions(var_81_1.aiActs, var_81_1.extraFlag, function()
					if not arg_81_0.viewComponent.levelStageView:
						return

					arg_81_0.viewComponent.levelStageView.tryAutoTrigger())
			elif var_83_0 == ChapterConst.OpStory:
				arg_81_0.viewComponent.levelStageView.tryAutoTrigger()
			elif var_83_0 == ChapterConst.OpSwitch:
				arg_81_0.viewComponent.grid.adjustCameraFocus()
			elif var_83_0 == ChapterConst.OpEnemyRound:
				arg_81_0.playAIActions(var_81_1.aiActs, var_81_1.extraFlag, function()
					arg_81_0.viewComponent.levelStageView.updateBombPanel(True)

					local var_101_0 = var_83_1.fleet.getStrategies()

					if _.any(var_101_0, function(arg_102_0)
						return arg_102_0.id == ChapterConst.StrategyExchange and arg_102_0.count > 0):
						arg_81_0.viewComponent.levelStageView.updateStageStrategy()
						arg_81_0.viewComponent.levelStageView.popStageStrategy()

					arg_81_0.viewComponent.levelStageView.tryAutoTrigger()
					arg_81_0.viewComponent.updatePoisonAreaTip())
			elif var_83_0 == ChapterConst.OpSubState:
				arg_81_0.saveSubState(var_83_1.subAutoAttack)
				arg_81_0.viewComponent.grid.OnChangeSubAutoAttack()
			elif var_83_0 == ChapterConst.OpStrategy:
				if var_81_1.arg1 == ChapterConst.StrategyExchange:
					local var_83_19 = var_83_1.fleet.findSkills(FleetSkill.TypeStrategy)

					for iter_83_0, iter_83_1 in ipairs(var_83_19):
						if iter_83_1.GetType() == FleetSkill.TypeStrategy and iter_83_1.GetArgs()[1] == ChapterConst.StrategyExchange:
							local var_83_20 = var_83_1.fleet.findCommanderBySkillId(iter_83_1.id)

							arg_81_0.viewComponent.doPlayCommander(var_83_20)

							break

				arg_81_0.playAIActions(var_81_1.aiActs, var_81_1.extraFlag, function()
					arg_81_0.viewComponent.grid.updateQuadCells(ChapterConst.QuadStateNormal))
			elif var_83_0 == ChapterConst.OpSupply:
				arg_81_0.viewComponent.levelStageView.tryAutoTrigger()
			elif var_83_0 == ChapterConst.OpBarrier:
				arg_81_0.viewComponent.levelStageView.tryAutoTrigger()
			elif var_83_0 == ChapterConst.OpSubTeleport:
				seriesAsync({
					function(arg_104_0)
						local var_104_0 = _.detect(var_83_1.fleets, function(arg_105_0)
							return arg_105_0.id == var_81_1.id)

						var_104_0.line = {
							row = var_81_1.arg1,
							column = var_81_1.arg2
						}
						var_104_0.startPos = {
							row = var_81_1.arg1,
							column = var_81_1.arg2
						}

						local var_104_1 = var_81_1.fullpath[1]
						local var_104_2 = var_81_1.fullpath[#var_81_1.fullpath]
						local var_104_3 = var_83_1.findPath(None, var_104_1, var_104_2)
						local var_104_4 = pg.strategy_data_template[ChapterConst.StrategySubTeleport].arg[2]
						local var_104_5 = math.ceil(var_104_4 * #var_104_0.getShips(False) * var_104_3 - 1e-05)
						local var_104_6 = getProxy(PlayerProxy)
						local var_104_7 = var_104_6.getData()

						var_104_7.consume({
							oil = var_104_5
						})
						arg_81_0.viewComponent.updateRes(var_104_7)
						var_104_6.updatePlayer(var_104_7)
						arg_81_0.viewComponent.grid.moveSub(table.indexof(var_83_1.fleets, var_104_0), var_81_1.fullpath, None, function()
							local var_106_0 = bit.bor(ChapterConst.DirtyFleet, ChapterConst.DirtyAttachment, ChapterConst.DirtyChampionPosition)

							getProxy(ChapterProxy).updateChapter(var_83_1, var_106_0)

							var_83_1 = arg_81_0.contextData.chapterVO

							arg_104_0()),
					function(arg_107_0)
						if not var_81_1.teleportPaths:
							arg_107_0()

							return

						local var_107_0 = var_81_1.teleportPaths[1]
						local var_107_1 = var_81_1.teleportPaths[2]

						if not var_107_0 or not var_107_1:
							arg_107_0()

							return

						local var_107_2 = _.detect(var_83_1.fleets, function(arg_108_0)
							return arg_108_0.id == var_81_1.id)

						var_107_2.startPos = Clone(var_81_1.teleportPaths[2])
						var_107_2.line = Clone(var_81_1.teleportPaths[2])

						local var_107_3 = arg_81_0.getViewComponent().grid.GetCellFleet(var_107_2.id)

						arg_81_0.getViewComponent().grid.TeleportFleetByPortal(var_107_3, var_81_1.teleportPaths, function()
							local var_109_0 = bit.bor(ChapterConst.DirtyFleet, ChapterConst.DirtyAttachment, ChapterConst.DirtyChampionPosition)

							getProxy(ChapterProxy).updateChapter(var_83_1, var_109_0)

							var_83_1 = arg_81_0.contextData.chapterVO

							arg_107_0()),
					function(arg_110_0)
						arg_81_0.viewComponent.levelStageView.SwitchBottomStagePanel(False)
						arg_81_0.viewComponent.grid.TurnOffSubTeleport()
						arg_81_0.viewComponent.grid.updateQuadCells(ChapterConst.QuadStateNormal)
				}))

		var_81_4()
	elif var_81_0 == ChapterProxy.CHAPTER_TIMESUP:
		arg_81_0.onTimeUp()
	elif var_81_0 == GAME.EVENT_LIST_UPDATE:
		arg_81_0.viewComponent.addbubbleMsgBox(function(arg_111_0)
			arg_81_0.OnEventUpdate(arg_111_0))
	elif var_81_0 == GAME.VOTE_BOOK_BE_UPDATED_DONE:
		arg_81_0.viewComponent.addbubbleMsgBox(function(arg_112_0)
			arg_81_0.NoticeVoteBook(arg_112_0))
	elif var_81_0 == DailyLevelProxy.ELITE_QUOTA_UPDATE:
		local var_81_5 = getProxy(DailyLevelProxy)

		arg_81_0.viewComponent.setEliteQuota(var_81_5.eliteCount, pg.gameset.elite_quota.key_value)
	elif var_81_0 == ActivityProxy.ACTIVITY_OPERATION_DONE:
		arg_81_0.viewComponent.updateMapItems()
	elif var_81_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_81_1 and var_81_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_PT_RANK:
			arg_81_0.viewComponent.updatePtActivity(var_81_1)
	elif var_81_0 == GAME.GET_REMASTER_TICKETS_DONE:
		arg_81_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_81_1, function()
			arg_81_0.viewComponent.updateRemasterTicket())
	elif var_81_0 == CommanderProxy.PREFAB_FLEET_UPDATE:
		local var_81_6 = getProxy(CommanderProxy).getPrefabFleet()

		arg_81_0.viewComponent.setCommanderPrefabs(var_81_6)
		arg_81_0.viewComponent.updateCommanderPrefab()
	elif var_81_0 == GAME.COOMMANDER_EQUIP_TO_FLEET_DONE:
		local var_81_7 = getProxy(FleetProxy).GetRegularFleets()

		arg_81_0.viewComponent.updateFleet(var_81_7)
		arg_81_0.viewComponent.RefreshFleetSelectView()
	elif var_81_0 == GAME.SUBMIT_TASK_DONE:
		if arg_81_0.contextData.map and arg_81_0.contextData.map.isSkirmish():
			arg_81_0.viewComponent.updateMapItems()

		arg_81_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_81_1, function()
			if arg_81_0.contextData.map and arg_81_0.contextData.map.isSkirmish() and arg_81_0.contextData.TaskToSubmit:
				local var_114_0 = arg_81_0.contextData.TaskToSubmit

				arg_81_0.contextData.TaskToSubmit = None

				arg_81_0.sendNotification(GAME.SUBMIT_TASK, var_114_0))
	elif var_81_0 == BagProxy.ITEM_UPDATED:
		local var_81_8 = getProxy(BagProxy).getItemsByType(Item.SPECIAL_OPERATION_TICKET)

		arg_81_0.viewComponent.setSpecialOperationTickets(var_81_8)
	elif var_81_0 == ChapterProxy.CHAPTER_AUTO_FIGHT_FLAG_UPDATED:
		if not arg_81_0.getViewComponent().levelStageView:
			return

		arg_81_0.getViewComponent().levelStageView.ActionInvoke("UpdateAutoFightMark")
	elif var_81_0 == ChapterProxy.CHAPTER_SKIP_PRECOMBAT_UPDATED:
		if not arg_81_0.getViewComponent().levelStageView:
			return

		arg_81_0.getViewComponent().levelStageView.ActionInvoke("UpdateSkipPreCombatMark")
	elif var_81_0 == ChapterProxy.CHAPTER_REMASTER_INFO_UPDATED or var_81_0 == GAME.CHAPTER_REMASTER_INFO_REQUEST_DONE:
		arg_81_0.viewComponent.updateRemasterInfo()
		arg_81_0.viewComponent.updateRemasterBtnTip()
	elif var_81_0 == GAME.CHAPTER_REMASTER_AWARD_RECEIVE_DONE:
		arg_81_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_81_1)
	elif var_81_0 == GAME.STORY_UPDATE_DONE:
		arg_81_0.cachedStoryAwards = var_81_1
	elif var_81_0 == GAME.STORY_END:
		if arg_81_0.cachedStoryAwards:
			arg_81_0.viewComponent.emit(BaseUI.ON_ACHIEVE, arg_81_0.cachedStoryAwards.awards)

			arg_81_0.cachedStoryAwards = None
	elif var_81_0 == LevelUIConst.CONTINUOUS_OPERATION:
		arg_81_0.viewComponent.emit(LevelUIConst.CONTINUOUS_OPERATION, var_81_1)
	elif var_81_0 == GAME.TRACKING_ERROR:
		if arg_81_0.waitingTracking:
			arg_81_0.DisplayContinuousOperationResult(var_81_1.chapter, getProxy(ChapterProxy).PopContinuousData(SYSTEM_SCENARIO))

		arg_81_0.waitingTracking = None
	elif var_81_0 == var_0_0.ON_SPITEM_CHANGED:
		arg_81_0.viewComponent.emit(var_0_0.ON_SPITEM_CHANGED, var_81_1)

def var_0_0.OnExitChapter(arg_115_0, arg_115_1, arg_115_2, arg_115_3):
	assert(arg_115_1)
	seriesAsync({
		function(arg_116_0)
			if not arg_115_0.contextData.chapterVO:
				return arg_116_0()

			arg_115_0.viewComponent.switchToMap(arg_116_0),
		function(arg_117_0)
			arg_115_0.viewComponent.addbubbleMsgBox(function()
				arg_115_0.viewComponent.CleanBubbleMsgbox()
				arg_117_0()),
		function(arg_119_0)
			if not arg_115_2:
				return arg_119_0()

			local var_119_0 = getProxy(PlayerProxy).getData()

			if arg_115_1.id == 103 and not var_119_0.GetCommonFlag(BATTLE_AUTO_ENABLED):
				arg_115_0.viewComponent.HandleShowMsgBox({
					modal = True,
					hideNo = True,
					content = i18n("battle_autobot_unlock"),
					onYes = arg_119_0,
					onNo = arg_119_0
				})
				arg_115_0.viewComponent.emit(LevelMediator2.NOTICE_AUTOBOT_ENABLED, {})

				return

			arg_119_0(),
		function(arg_120_0)
			if not arg_115_2:
				return arg_120_0()

			if getProxy(ChapterProxy).getMapById(arg_115_1.getConfig("map")).isSkirmish():
				local var_120_0 = arg_115_1.id
				local var_120_1 = getProxy(SkirmishProxy).getRawData()
				local var_120_2 = _.detect(var_120_1, function(arg_121_0)
					return tonumber(arg_121_0.getConfig("event")) == var_120_0)

				if not var_120_2:
					arg_120_0()

					return

				local var_120_3 = getProxy(TaskProxy)
				local var_120_4 = var_120_2.getConfig("task_id")
				local var_120_5 = var_120_3.getTaskVO(var_120_4)

				if var_120_5 and var_120_5.getTaskStatus() == 1:
					arg_115_0.sendNotification(GAME.SUBMIT_TASK, var_120_4)

					if var_120_2 == var_120_1[#var_120_1]:
						local var_120_6 = getProxy(ActivityProxy)
						local var_120_7 = ActivityConst.ACTIVITY_ID_US_SKIRMISH_RE
						local var_120_8 = var_120_6.getActivityById(var_120_7)

						assert(var_120_8, "Missing Skirmish Activity " .. (var_120_7 or "NIL"))

						local var_120_9 = var_120_8.getConfig("config_data")
						local var_120_10 = var_120_9[#var_120_9][2]
						local var_120_11 = var_120_3.getTaskVO(var_120_10)

						if var_120_11 and var_120_11.getTaskStatus() < 2:
							arg_115_0.contextData.TaskToSubmit = var_120_10

			arg_120_0(),
		function(arg_122_0)
			if not arg_115_2:
				return arg_122_0()

			local var_122_0 = getProxy(ChapterProxy).getMapById(arg_115_1.getConfig("map"))

			if var_122_0.isRemaster():
				local var_122_1 = var_122_0.getRemaster()
				local var_122_2 = pg.re_map_template[var_122_1]
				local var_122_3 = Map.GetRearChaptersOfRemaster(var_122_1)

				assert(var_122_3)

				if _.any(var_122_3, function(arg_123_0)
					return arg_123_0 == arg_115_1.id):
					local var_122_4 = var_122_2.memory_group
					local var_122_5 = pg.memory_group[var_122_4].memories

					if _.any(var_122_5, function(arg_124_0)
						return not pg.NewStoryMgr.GetInstance().IsPlayed(pg.memory_template[arg_124_0].story, True)):
						_.each(var_122_5, function(arg_125_0)
							local var_125_0 = pg.memory_template[arg_125_0].story
							local var_125_1, var_125_2 = pg.NewStoryMgr.GetInstance().StoryName2StoryId(var_125_0)

							pg.NewStoryMgr.GetInstance().SetPlayedFlag(var_125_1))
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							yesText = "text_go",
							content = i18n("levelScene_remaster_story_tip", pg.memory_group[var_122_4].title),
							weight = LayerWeightConst.SECOND_LAYER,
							def onYes:()
								arg_115_0.sendNotification(GAME.GO_SCENE, SCENE.WORLD_COLLECTION, {
									page = WorldMediaCollectionScene.PAGE_MEMORTY,
									memoryGroup = var_122_4
								}),
							def onNo:()
								local var_127_0 = getProxy(PlayerProxy).getRawData().id

								PlayerPrefs.SetInt("MEMORY_GROUP_NOTIFICATION" .. var_127_0 .. " " .. var_122_4, 1)
								PlayerPrefs.Save()
								arg_122_0()
						})

						return

			arg_122_0(),
		function(arg_128_0)
			if arg_115_0.contextData.map and not arg_115_0.contextData.map.isUnlock():
				arg_115_0.viewComponent.emit(var_0_0.ON_SWITCH_NORMAL_MAP)

				return

			if not arg_115_3:
				return arg_128_0()

			local var_128_0 = arg_115_3 and arg_115_3.AutoFightFlag
			local var_128_1 = {}

			if arg_115_3 and arg_115_3.ResultDrops:
				for iter_128_0, iter_128_1 in ipairs(arg_115_3.ResultDrops):
					var_128_1 = table.mergeArray(var_128_1, iter_128_1)

			local var_128_2 = {}

			if arg_115_3 and arg_115_3.TotalDrops:
				for iter_128_2, iter_128_3 in ipairs(arg_115_3.TotalDrops):
					var_128_2 = table.mergeArray(var_128_2, iter_128_3)

			DropResultIntegration(var_128_2)

			local var_128_3 = getProxy(ChapterProxy).GetContinuousData(SYSTEM_SCENARIO)

			if var_128_3:
				var_128_3.MergeDrops(var_128_2, var_128_1)
				var_128_3.MergeEvents(arg_115_3.ListEventNotify, arg_115_3.ListGuildEventNotify, arg_115_3.ListGuildEventAutoReceiveNotify)

				if arg_115_2:
					var_128_3.ConsumeBattleTime()

				if var_128_3.IsActive() and var_128_3.GetRestBattleTime() > 0:
					arg_115_0.waitingTracking = True

					arg_115_0.viewComponent.emit(var_0_0.ON_RETRACKING, arg_115_1, var_128_0)

					return

				getProxy(ChapterProxy).PopContinuousData(SYSTEM_SCENARIO)
				arg_115_0.DisplayContinuousOperationResult(arg_115_1, var_128_3)
				arg_128_0()

				return

			local var_128_4 = var_128_0 != None

			if not var_128_4 and not arg_115_3.ResultDrops:
				return arg_128_0()

			local var_128_5
			local var_128_6

			if var_128_4:
				var_128_5 = i18n("autofight_rewards")
				var_128_6 = i18n("total_rewards_subtitle")
			else
				var_128_5 = i18n("settle_rewards_title")
				var_128_6 = i18n("settle_rewards_subtitle")

			arg_115_0.addSubLayers(Context.New({
				viewComponent = LevelStageTotalRewardPanel,
				mediator = LevelStageTotalRewardPanelMediator,
				data = {
					title = var_128_5,
					subTitle = var_128_6,
					chapter = arg_115_1,
					onClose = arg_128_0,
					rewards = var_128_2,
					resultRewards = var_128_1,
					events = arg_115_3.ListEventNotify,
					guildTasks = arg_115_3.ListGuildEventNotify,
					guildAutoReceives = arg_115_3.ListGuildEventAutoReceiveNotify,
					isAutoFight = var_128_0
				}
			}), True),
		function(arg_129_0)
			if Map.autoNextPage:
				Map.autoNextPage = None

				triggerButton(arg_115_0.viewComponent.btnNext)

			if arg_115_2:
				arg_115_0.viewComponent.RefreshMapBG()

			arg_115_0.TryPlaySubGuide()
	})

def var_0_0.DisplayContinuousWindow(arg_130_0, arg_130_1, arg_130_2, arg_130_3, arg_130_4):
	local var_130_0 = arg_130_1.getConfig("oil")
	local var_130_1 = arg_130_1.getPlayType()
	local var_130_2 = 0
	local var_130_3 = 0

	if var_130_1 == ChapterConst.TypeMultiStageBoss:
		local var_130_4 = pg.chapter_model_multistageboss[arg_130_1.id]

		var_130_2 = _.reduce(var_130_4.boss_refresh, 0, function(arg_131_0, arg_131_1)
			return arg_131_0 + arg_131_1)
		var_130_3 = #var_130_4.boss_refresh
	else
		var_130_2, var_130_3 = arg_130_1.getConfig("boss_refresh"), 1

	local var_130_5 = arg_130_1.getConfig("use_oil_limit")

	table.Foreach(arg_130_2, function(arg_132_0, arg_132_1)
		local var_132_0 = arg_130_4[arg_132_0]

		if var_132_0 == ChapterFleet.DUTY_IDLE:
			return

		local var_132_1 = arg_132_1.GetCostSum().oil

		if var_132_0 == ChapterFleet.DUTY_KILLALL:
			local var_132_2 = var_130_5[1] or 0
			local var_132_3 = var_132_1

			if var_132_2 > 0:
				var_132_3 = math.min(var_132_3, var_132_2)

			local var_132_4 = var_130_5[2] or 0
			local var_132_5 = var_132_1

			if var_132_4 > 0:
				var_132_5 = math.min(var_132_5, var_132_4)

			var_130_0 = var_130_0 + var_132_3 * var_130_2 + var_132_5 * var_130_3
		elif var_132_0 == ChapterFleet.DUTY_CLEANPATH:
			local var_132_6 = var_130_5[1] or 0
			local var_132_7 = var_132_1

			if var_132_6 > 0:
				var_132_7 = math.min(var_132_7, var_132_6)

			var_130_0 = var_130_0 + var_132_7 * var_130_2
		elif var_132_0 == ChapterFleet.DUTY_KILLBOSS:
			local var_132_8 = var_130_5[2] or 0
			local var_132_9 = var_132_1

			if var_132_8 > 0:
				var_132_9 = math.min(var_132_9, var_132_8)

			var_130_0 = var_130_0 + var_132_9 * var_130_3)

	local var_130_6 = arg_130_1.GetMaxBattleCount()
	local var_130_7 = arg_130_3 and arg_130_3 > 0
	local var_130_8 = arg_130_1.GetSpItems()
	local var_130_9 = var_130_8[1] and var_130_8[1].count or 0
	local var_130_10 = var_130_8[1] and var_130_8[1].id or 0
	local var_130_11 = arg_130_1.GetRestDailyBonus()

	arg_130_0.addSubLayers(Context.New({
		mediator = LevelContinuousOperationWindowMediator,
		viewComponent = LevelContinuousOperationWindow,
		data = {
			maxCount = var_130_6,
			oilCost = var_130_0,
			chapter = arg_130_1,
			extraRate = {
				rate = 2,
				enabled = var_130_7,
				extraCount = var_130_9,
				spItemId = var_130_10,
				freeBonus = var_130_11
			}
		}
	}))

def var_0_0.DisplayContinuousOperationResult(arg_133_0, arg_133_1, arg_133_2):
	local var_133_0 = i18n("autofight_rewards")
	local var_133_1 = i18n("total_rewards_subtitle")

	arg_133_0.addSubLayers(Context.New({
		viewComponent = LevelContinuousOperationTotalRewardPanel,
		mediator = LevelStageTotalRewardPanelMediator,
		data = {
			title = var_133_0,
			subTitle = var_133_1,
			chapter = arg_133_1,
			rewards = arg_133_2.GetDrops(),
			resultRewards = arg_133_2.GetSettlementDrops(),
			continuousData = arg_133_2,
			events = arg_133_2.GetEvents(1),
			guildTasks = arg_133_2.GetEvents(2),
			guildAutoReceives = arg_133_2.GetEvents(3)
		}
	}), True)

def var_0_0.OnEventUpdate(arg_134_0, arg_134_1):
	local var_134_0 = getProxy(EventProxy)

	arg_134_0.viewComponent.updateEvent(var_134_0)

	if pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_134_0.player.level, "EventMediator") and var_134_0.eventForMsg:
		local var_134_1 = var_134_0.eventForMsg.id or 0
		local var_134_2 = getProxy(ChapterProxy).getActiveChapter(True)

		if var_134_2 and var_134_2.IsAutoFight():
			getProxy(ChapterProxy).AddExtendChapterDataArray(var_134_2.id, "ListEventNotify", var_134_1)
			existCall(arg_134_1)
		else
			local var_134_3 = pg.collection_template[var_134_1] and pg.collection_template[var_134_1].title or ""

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				modal = False,
				hideNo = True,
				content = i18n("event_special_update", var_134_3),
				weight = LayerWeightConst.SECOND_LAYER,
				onYes = arg_134_1,
				onNo = arg_134_1
			})

		var_134_0.eventForMsg = None
	else
		existCall(arg_134_1)

def var_0_0.onTimeUp(arg_135_0):
	local var_135_0 = getProxy(ChapterProxy).getActiveChapter()

	if var_135_0 and not var_135_0.inWartime():
		local function var_135_1()
			arg_135_0.sendNotification(GAME.CHAPTER_OP, {
				type = ChapterConst.OpRetreat
			})

		if arg_135_0.contextData.chapterVO:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				modal = True,
				hideNo = True,
				content = i18n("battle_preCombatMediator_timeout"),
				onYes = var_135_1,
				onNo = var_135_1
			})
		else
			var_135_1()
			pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_chapter_timeout"))

def var_0_0.getDockCallbackFuncs(arg_137_0, arg_137_1, arg_137_2, arg_137_3, arg_137_4):
	local var_137_0 = getProxy(ChapterProxy)

	local function var_137_1(arg_138_0, arg_138_1)
		local var_138_0, var_138_1 = ShipStatus.ShipStatusCheck("inElite", arg_138_0, arg_138_1, {
			inElite = arg_137_3.getConfig("formation")
		})

		if not var_138_0:
			return var_138_0, var_138_1

		for iter_138_0, iter_138_1 in pairs(arg_137_1):
			if arg_138_0.isSameKind(iter_138_0):
				return False, i18n("ship_formationMediator_changeNameError_sameShip")

		return True

	local function var_137_2(arg_139_0, arg_139_1, arg_139_2)
		arg_139_1()

	local function var_137_3(arg_140_0)
		local var_140_0 = arg_137_3.getEliteFleetList()[arg_137_4]

		if arg_137_2:
			local var_140_1 = table.indexof(var_140_0, arg_137_2.id)

			assert(var_140_1)

			if arg_140_0[1]:
				var_140_0[var_140_1] = arg_140_0[1]
			else
				table.remove(var_140_0, var_140_1)
		else
			table.insert(var_140_0, arg_140_0[1])

		var_137_0.updateChapter(arg_137_3)
		var_137_0.duplicateEliteFleet(arg_137_3)

	return var_137_1, var_137_2, var_137_3

def var_0_0.getSupportDockCallbackFuncs(arg_141_0, arg_141_1, arg_141_2, arg_141_3):
	local var_141_0 = getProxy(ChapterProxy)

	local function var_141_1(arg_142_0, arg_142_1)
		local var_142_0, var_142_1 = ShipStatus.ShipStatusCheck("inSupport", arg_142_0, arg_142_1)

		if not var_142_0:
			return var_142_0, var_142_1

		for iter_142_0, iter_142_1 in pairs(arg_141_1):
			if arg_142_0.isSameKind(iter_142_0):
				return False, i18n("ship_formationMediator_changeNameError_sameShip")

		return True

	local function var_141_2(arg_143_0, arg_143_1, arg_143_2)
		arg_143_1()

	local function var_141_3(arg_144_0)
		local var_144_0 = arg_141_3.getSupportFleet()

		if arg_141_2:
			local var_144_1 = table.indexof(var_144_0, arg_141_2.id)

			assert(var_144_1)

			if arg_144_0[1]:
				var_144_0[var_144_1] = arg_144_0[1]
			else
				table.remove(var_144_0, var_144_1)
		else
			table.insert(var_144_0, arg_144_0[1])

		var_141_0.updateChapter(arg_141_3)
		var_141_0.duplicateSupportFleet(arg_141_3)

	return var_141_1, var_141_2, var_141_3

def var_0_0.playAIActions(arg_145_0, arg_145_1, arg_145_2, arg_145_3):
	if not arg_145_0.viewComponent.grid:
		arg_145_3()

		return

	local var_145_0 = getProxy(ChapterProxy)
	local var_145_1

	local function var_145_2()
		if var_145_1 and coroutine.status(var_145_1) == "suspended":
			local var_146_0, var_146_1 = coroutine.resume(var_145_1)

			assert(var_146_0, debug.traceback(var_145_1, var_146_1))

			if not var_146_0:
				arg_145_0.viewComponent.unfrozen(-1)
				arg_145_0.sendNotification(GAME.CHAPTER_OP, {
					type = ChapterConst.OpRequest
				})

	var_145_1 = coroutine.create(function()
		arg_145_0.viewComponent.frozen()

		local var_147_0 = {}
		local var_147_1 = arg_145_2 or 0

		for iter_147_0, iter_147_1 in ipairs(arg_145_1):
			local var_147_2 = arg_145_0.contextData.chapterVO
			local var_147_3, var_147_4 = iter_147_1.applyTo(var_147_2, True)

			assert(var_147_3, var_147_4)
			iter_147_1.PlayAIAction(arg_145_0.contextData.chapterVO, arg_145_0, function()
				local var_148_0, var_148_1, var_148_2 = iter_147_1.applyTo(var_147_2, False)

				if var_148_0:
					var_145_0.updateChapter(var_147_2, var_148_1)

					var_147_1 = bit.bor(var_147_1, var_148_2 or 0)

				onNextTick(var_145_2))
			coroutine.yield()

			if isa(iter_147_1, FleetAIAction) and iter_147_1.actType == ChapterConst.ActType_Poison and var_147_2.existFleet(FleetType.Normal, iter_147_1.line.row, iter_147_1.line.column):
				local var_147_5 = var_147_2.getFleetIndex(FleetType.Normal, iter_147_1.line.row, iter_147_1.line.column)

				table.insert(var_147_0, var_147_5)

		local var_147_6 = bit.band(var_147_1, ChapterConst.DirtyAutoAction)

		var_147_1 = bit.band(var_147_1, bit.bnot(ChapterConst.DirtyAutoAction))

		if var_147_1 != 0:
			local var_147_7 = arg_145_0.contextData.chapterVO

			var_145_0.updateChapter(var_147_7, var_147_1)

		seriesAsync({
			function(arg_149_0)
				if var_147_6 != 0:
					arg_145_0.viewComponent.levelStageView.tryAutoAction(arg_149_0)
				else
					arg_149_0(),
			function(arg_150_0)
				table.ParallelIpairsAsync(var_147_0, function(arg_151_0, arg_151_1, arg_151_2)
					arg_145_0.viewComponent.grid.showFleetPoisonDamage(arg_151_1, arg_151_2), arg_150_0),
			function(arg_152_0)
				arg_145_3()
				arg_145_0.viewComponent.unfrozen()
		}))

	var_145_2()

def var_0_0.saveSubState(arg_153_0, arg_153_1):
	local var_153_0 = getProxy(PlayerProxy).getRawData().id

	PlayerPrefs.SetInt("chapter_submarine_ai_type_" .. var_153_0, arg_153_1 + 1)
	PlayerPrefs.Save()

def var_0_0.loadSubState(arg_154_0, arg_154_1):
	local var_154_0 = getProxy(PlayerProxy).getRawData().id
	local var_154_1 = PlayerPrefs.GetInt("chapter_submarine_ai_type_" .. var_154_0, 1) - 1
	local var_154_2 = math.clamp(var_154_1, 0, 1)

	if var_154_2 != arg_154_1:
		arg_154_0.viewComponent.emit(LevelMediator2.ON_OP, {
			type = ChapterConst.OpSubState,
			arg1 = var_154_2
		})

def var_0_0.remove(arg_155_0):
	arg_155_0.removeSubLayers(LevelContinuousOperationWindowMediator)
	var_0_0.super.remove(arg_155_0)

return var_0_0
