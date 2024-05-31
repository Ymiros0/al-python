local var_0_0 = class("ActivityMediator", import("..base.ContextMediator"))

var_0_0.EVENT_GO_SCENE = "event go scene"
var_0_0.EVENT_OPERATION = "event operation"
var_0_0.GO_SHOPS_LAYER = "event go shop layer"
var_0_0.GO_SHOPS_LAYER_STEEET = "event go shop layer in shopstreet"
var_0_0.BATTLE_OPERA = "event difficult sel"
var_0_0.GO_BACKYARD = "event go backyard"
var_0_0.GO_LOTTERY = "event go lottery"
var_0_0.EVENT_COLORING_ACHIEVE = "event coloring achieve"
var_0_0.ON_TASK_SUBMIT = "event on task submit"
var_0_0.ON_TASK_SUBMIT_ONESTEP = "event on task submit one step"
var_0_0.ON_TASK_GO = "event on task go"
var_0_0.OPEN_LAYER = "event OPEN_LAYER"
var_0_0.CLOSE_LAYER = "event CLOSE_LAYER"
var_0_0.EVENT_PT_OPERATION = "event pt op"
var_0_0.BLACKWHITEGRID = "black white grid"
var_0_0.MEMORYBOOK = "memory book"
var_0_0.RETURN_AWARD_OP = "event return award op"
var_0_0.SHOW_AWARD_WINDOW = "event show award window"
var_0_0.GO_DODGEM = "event go:dgem"
var_0_0.GO_SUBMARINE_RUN = "event go sumbarine run"
var_0_0.ON_SIMULATION_COMBAT = "event simulation combat"
var_0_0.ON_AIRFIGHT_COMBAT = "event perform airfight combat"
var_0_0.SPECIAL_BATTLE_OPERA = "special battle opera"
var_0_0.NEXT_DISPLAY_AWARD = "next display awards"
var_0_0.GO_PRAY_POOL = "go pray pool"
var_0_0.SELECT_ACTIVITY = "event select activity"
var_0_0.FETCH_INSTARGRAM = "fetch instagram"
var_0_0.MUSIC_GAME_OPERATOR = "get music game final prize"
var_0_0.SHOW_NEXT_ACTIVITY = "show next activity"
var_0_0.OPEN_RED_PACKET_LAYER = "ActivityMediator.OPEN_RED_PACKET_LAYER"
var_0_0.GO_MINI_GAME = "ActivityMediator.GO_MINI_GAME"
var_0_0.GO_DECODE_MINI_GAME = "ActivityMediator.GO_DECODE_MINI_GAME"
var_0_0.ON_BOBING_RESULT = "on bobing result"
var_0_0.ACTIVITY_PERMANENT = "ActivityMediator.ACTIVITY_PERMANENT"
var_0_0.FINISH_ACTIVITY_PERMANENT = "ActivityMediator.FINISH_ACTIVITY_PERMANENT"
var_0_0.ON_SHAKE_BEADS_RESULT = "on shake beads result"
var_0_0.GO_PERFORM_COMBAT = "ActivityMediator.GO_PERFORM_COMBAT"
var_0_0.ON_AWARD_WINDOW = "ActivityMediator.ON_AWARD_WINDOW"
var_0_0.GO_CARDPUZZLE_COMBAT = "ActivityMediator.GO_CARDPUZZLE_COMBAT"
var_0_0.CHARGE = "ActivityMediator.CHARGE"
var_0_0.BUY_ITEM = "ActivityMediator.BUY_ITEM"
var_0_0.OPEN_CHARGE_ITEM_PANEL = "ActivityMediator.OPEN_CHARGE_ITEM_PANEL"
var_0_0.OPEN_CHARGE_BIRTHDAY = "ActivityMediator.OPEN_CHARGE_BIRTHDAY"
var_0_0.STORE_DATE = "ActivityMediator.STORE_DATE"
var_0_0.ON_ACT_SHOPPING = "ActivityMediator.ON_ACT_SHOPPING"

def var_0_0.register(arg_1_0):
	arg_1_0.UIAvalibleCallbacks = {}

	arg_1_0.bind(var_0_0.ON_AWARD_WINDOW, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		arg_1_0.viewComponent.ShowAwardWindow(arg_2_1, arg_2_2, arg_2_3))
	arg_1_0.bind(var_0_0.GO_DECODE_MINI_GAME, function(arg_3_0)
		pg.m02.sendNotification(GAME.REQUEST_MINI_GAME, {
			type = MiniGameRequestCommand.REQUEST_HUB_DATA,
			def callback:()
				pg.m02.sendNotification(GAME.GO_MINI_GAME, 11)
		}))
	arg_1_0.bind(var_0_0.GO_MINI_GAME, function(arg_5_0, arg_5_1)
		pg.m02.sendNotification(GAME.GO_MINI_GAME, arg_5_1))
	arg_1_0.bind(var_0_0.GO_SUBMARINE_RUN, function(arg_6_0, arg_6_1)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_SUBMARINE_RUN,
			stageId = arg_6_1
		}))
	arg_1_0.bind(var_0_0.GO_DODGEM, function(arg_7_0)
		local var_7_0 = ys.Battle.BattleConfig.BATTLE_DODGEM_STAGES[math.random(#ys.Battle.BattleConfig.BATTLE_DODGEM_STAGES)]

		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_DODGEM,
			stageId = var_7_0
		}))
	arg_1_0.bind(var_0_0.ON_SIMULATION_COMBAT, function(arg_8_0, arg_8_1, arg_8_2)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_SIMULATION,
			stageId = arg_8_1.stageId,
			warnMsg = arg_8_1.warnMsg,
			exitCallback = arg_8_2
		}))
	arg_1_0.bind(var_0_0.ON_AIRFIGHT_COMBAT, function(arg_9_0, arg_9_1, arg_9_2)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_AIRFIGHT,
			stageId = arg_9_1.stageId,
			exitCallback = arg_9_2
		}))
	arg_1_0.bind(var_0_0.RETURN_AWARD_OP, function(arg_10_0, arg_10_1)
		if arg_10_1.cmd == ActivityConst.RETURN_AWARD_OP_SHOW_AWARD_OVERVIEW:
			arg_1_0.viewComponent.ShowWindow(ReturnerAwardWindow, arg_10_1.arg1)
		elif arg_10_1.cmd == ActivityConst.RETURN_AWARD_OP_SHOW_RETURNER_AWARD_OVERVIEW:
			arg_1_0.viewComponent.ShowWindow(TaskAwardWindow, arg_10_1.arg1)
		else
			arg_1_0.sendNotification(GAME.RETURN_AWARD_OP, arg_10_1))
	arg_1_0.bind(var_0_0.SHOW_AWARD_WINDOW, function(arg_11_0, arg_11_1, arg_11_2)
		arg_1_0.viewComponent.ShowWindow(arg_11_1, arg_11_2))
	arg_1_0.bind(var_0_0.EVENT_PT_OPERATION, function(arg_12_0, arg_12_1)
		arg_1_0.sendNotification(GAME.ACT_NEW_PT, arg_12_1))
	arg_1_0.bind(var_0_0.OPEN_LAYER, function(arg_13_0, arg_13_1)
		arg_1_0.addSubLayers(arg_13_1))
	arg_1_0.bind(var_0_0.OPEN_RED_PACKET_LAYER, function(arg_14_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = RedPacketMediator,
			viewComponent = RedPacketLayer
		})))
	arg_1_0.bind(var_0_0.CLOSE_LAYER, function(arg_15_0, arg_15_1)
		local var_15_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(arg_15_1)

		if var_15_0:
			arg_1_0.sendNotification(GAME.REMOVE_LAYERS, {
				context = var_15_0
			}))
	arg_1_0.bind(var_0_0.EVENT_OPERATION, function(arg_16_0, arg_16_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, arg_16_1))
	arg_1_0.bind(var_0_0.EVENT_GO_SCENE, function(arg_17_0, arg_17_1, arg_17_2)
		if arg_17_1 == SCENE.SUMMER_FEAST:
			pg.NewStoryMgr.GetInstance().Play("TIANHOUYUYI1", function()
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SUMMER_FEAST))
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, arg_17_1, arg_17_2))
	arg_1_0.bind(var_0_0.BLACKWHITEGRID, function()
		if not getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BLACKWHITE):
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		arg_1_0.addSubLayers(Context.New({
			viewComponent = BlackWhiteGridLayer,
			mediator = BlackWhiteGridMediator
		})))
	arg_1_0.bind(var_0_0.MEMORYBOOK, function()
		if not getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA):
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		arg_1_0.addSubLayers(Context.New({
			viewComponent = MemoryBookLayer,
			mediator = MemoryBookMediator
		})))
	arg_1_0.bind(var_0_0.GO_SHOPS_LAYER, function(arg_21_0, arg_21_1)
		if not getProxy(ActivityProxy).getActivityById(arg_21_1.actId):
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, arg_21_1 or {
			warp = NewShopsScene.TYPE_ACTIVITY
		}))
	arg_1_0.bind(var_0_0.GO_SHOPS_LAYER_STEEET, function(arg_22_0, arg_22_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, arg_22_1 or {
			warp = NewShopsScene.TYPE_SHOP_STREET
		}))
	arg_1_0.bind(var_0_0.BATTLE_OPERA, function()
		local var_23_0 = getProxy(ChapterProxy)
		local var_23_1, var_23_2 = var_23_0.getLastMapForActivity()

		if not var_23_1 or not var_23_0.getMapById(var_23_1).isUnlock():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))
		else
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
				chapterId = var_23_2,
				mapIdx = var_23_1
			}))
	arg_1_0.bind(var_0_0.SPECIAL_BATTLE_OPERA, function()
		local var_24_0 = getProxy(ChapterProxy)
		local var_24_1, var_24_2 = var_24_0.getLastMapForActivity()

		if not var_24_1 or not var_24_0.getMapById(var_24_1).isUnlock():
			local var_24_3 = getProxy(ChapterProxy)
			local var_24_4 = var_24_3.getActiveChapter()

			var_24_1 = var_24_4 and var_24_4.getConfig("map")

			if not var_24_4:
				local var_24_5 = Map.lastMap and var_24_3.getMapById(Map.lastMap)

				if var_24_5 and var_24_5.isUnlock():
					var_24_1 = Map.lastMap
				else
					var_24_1 = var_24_3.getLastUnlockMap().id

			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
				chapterId = var_24_4 and var_24_4.id,
				mapIdx = var_24_1
			})
		else
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
				chapterId = var_24_2,
				mapIdx = var_24_1
			}))
	arg_1_0.bind(var_0_0.GO_LOTTERY, function(arg_25_0)
		local var_25_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_LOTTERY)

		arg_1_0.addSubLayers(Context.New({
			mediator = LotteryMediator,
			viewComponent = LotteryLayer,
			data = {
				activityId = var_25_0.id
			}
		})))
	arg_1_0.bind(var_0_0.GO_BACKYARD, function(arg_26_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.COURTYARD))
	arg_1_0.bind(var_0_0.EVENT_COLORING_ACHIEVE, function(arg_27_0, arg_27_1)
		arg_1_0.sendNotification(GAME.COLORING_ACHIEVE, arg_27_1))
	arg_1_0.bind(var_0_0.ON_TASK_SUBMIT, function(arg_28_0, arg_28_1, arg_28_2)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_28_1.id, arg_28_2))
	arg_1_0.bind(var_0_0.ON_TASK_SUBMIT_ONESTEP, function(arg_29_0, arg_29_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
			resultList = arg_29_1
		}))
	arg_1_0.bind(var_0_0.ON_TASK_GO, function(arg_30_0, arg_30_1)
		arg_1_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_30_1
		}))
	arg_1_0.bind(var_0_0.GO_PRAY_POOL, function(arg_31_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.GETBOAT, {
			goToPray = True
		}))
	arg_1_0.bind(var_0_0.FETCH_INSTARGRAM, function(arg_32_0, ...)
		arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_FETCH, ...))
	arg_1_0.bind(var_0_0.MUSIC_GAME_OPERATOR, function(arg_33_0, ...)
		arg_1_0.sendNotification(GAME.SEND_MINI_GAME_OP, ...))
	arg_1_0.bind(var_0_0.SELECT_ACTIVITY, function(arg_34_0, arg_34_1)
		arg_1_0.viewComponent.verifyTabs(arg_34_1))
	arg_1_0.bind(var_0_0.SHOW_NEXT_ACTIVITY, function(arg_35_0)
		arg_1_0.showNextActivity())
	arg_1_0.bind(var_0_0.ACTIVITY_PERMANENT, function(arg_36_0, arg_36_1)
		if PlayerPrefs.GetString("permanent_time", "") != pg.gameset.permanent_mark.description:
			PlayerPrefs.SetString("permanent_time", pg.gameset.permanent_mark.description)
			arg_1_0.viewComponent.updateEntrances()

		local var_36_0 = getProxy(ActivityPermanentProxy).getDoingActivity()

		if var_36_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("activity_permanent_tips3"))
			arg_1_0.viewComponent.verifyTabs(var_36_0.id)
		else
			arg_1_0.addSubLayers(Context.New({
				mediator = ActivityPermanentMediator,
				viewComponent = ActivityPermanentLayer,
				data = {
					finishId = arg_36_1
				}
			})))
	arg_1_0.bind(var_0_0.FINISH_ACTIVITY_PERMANENT, function(arg_37_0)
		local var_37_0 = getProxy(ActivityPermanentProxy).getDoingActivity()

		assert(var_37_0.canPermanentFinish(), "error permanent activity finish")
		arg_1_0.sendNotification(GAME.ACTIVITY_PERMANENT_FINISH, {
			activity_id = var_37_0.id
		}))
	arg_1_0.bind(var_0_0.GO_PERFORM_COMBAT, function(arg_38_0, arg_38_1, arg_38_2)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_PERFORM,
			stageId = arg_38_1.stageId,
			memory = arg_38_1.memory
		}))
	arg_1_0.bind(var_0_0.NEXT_DISPLAY_AWARD, function(arg_39_0, arg_39_1, arg_39_2)
		arg_1_0.nextDisplayAwards = arg_39_1)
	arg_1_0.bind(var_0_0.GO_CARDPUZZLE_COMBAT, function(arg_40_0, arg_40_1)
		arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_CARDPUZZLE,
			combatID = arg_40_1
		}))
	arg_1_0.bind(var_0_0.CHARGE, function(arg_41_0, arg_41_1)
		arg_1_0.sendNotification(GAME.CHARGE_OPERATION, {
			shopId = arg_41_1
		}))
	arg_1_0.bind(var_0_0.BUY_ITEM, function(arg_42_0, arg_42_1, arg_42_2)
		arg_1_0.sendNotification(GAME.SHOPPING, {
			id = arg_42_1,
			count = arg_42_2
		}))
	arg_1_0.bind(var_0_0.OPEN_CHARGE_ITEM_PANEL, function(arg_43_0, arg_43_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeItemPanelMediator,
			viewComponent = ChargeItemPanelLayer,
			data = {
				panelConfig = arg_43_1
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_CHARGE_BIRTHDAY, function(arg_44_0, arg_44_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeBirthdayMediator,
			viewComponent = ChargeBirthdayLayer,
			data = {}
		})))
	arg_1_0.bind(var_0_0.STORE_DATE, function(arg_45_0, arg_45_1)
		arg_1_0.sendNotification(GAME.ACTIVITY_STORE_DATE, {
			activity_id = arg_45_1.actId,
			intValue = arg_45_1.intValue or 0,
			strValue = arg_45_1.strValue or "",
			callback = arg_45_1.callback
		}))
	arg_1_0.bind(var_0_0.ON_ACT_SHOPPING, function(arg_46_0, arg_46_1, arg_46_2, arg_46_3, arg_46_4)
		arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			activity_id = arg_46_1,
			cmd = arg_46_2,
			arg1 = arg_46_3,
			arg2 = arg_46_4
		}))

	local var_1_0 = getProxy(ActivityProxy)

	arg_1_0.viewComponent.setActivities(var_1_0.getPanelActivities())

	local var_1_1 = getProxy(PlayerProxy).getRawData()

	arg_1_0.viewComponent.setPlayer(var_1_1)

	local var_1_2 = getProxy(BayProxy).getShipById(var_1_1.character)

	arg_1_0.viewComponent.setFlagShip(var_1_2)

def var_0_0.onUIAvalible(arg_47_0):
	arg_47_0.UIAvalible = True

	_.each(arg_47_0.UIAvalibleCallbacks, function(arg_48_0)
		arg_48_0())

def var_0_0.initNotificationHandleDic(arg_49_0):
	arg_49_0.handleDic = {
		[ActivityProxy.ACTIVITY_ADDED] = function(arg_50_0, arg_50_1)
			local var_50_0 = arg_50_1.getBody()

			if var_50_0.getConfig("type") == ActivityConst.ACTIVITY_TYPE_LOTTERY:
				return

			arg_50_0.viewComponent.updateActivity(var_50_0)

			if ActivityConst.AOERLIANG_TASK_ID == var_50_0.id:
				arg_50_0.viewComponent.update_task_list_auto_aoerliang(var_50_0),
		[ActivityProxy.ACTIVITY_UPDATED] = function(...)
			arg_49_0.handleDic[ActivityProxy.ACTIVITY_ADDED](...),
		[ActivityProxy.ACTIVITY_DELETED] = function(arg_52_0, arg_52_1)
			local var_52_0 = arg_52_1.getBody()

			arg_52_0.viewComponent.removeActivity(var_52_0),
		[ActivityProxy.ACTIVITY_OPERATION_DONE] = function(arg_53_0, arg_53_1)
			local var_53_0 = arg_53_1.getBody()

			if ActivityConst.AOERLIANG_TASK_ID == var_53_0:
				return

			if ActivityConst.HOLOLIVE_MORNING_ID == var_53_0:
				local var_53_1 = arg_53_0.viewComponent.pageDic[ActivityConst.HOLOLIVE_MORNING_ID]

			arg_53_0.showNextActivity(),
		[ActivityProxy.ACTIVITY_SHOW_AWARDS] = function(arg_54_0, arg_54_1)
			local var_54_0 = arg_54_1.getBody()
			local var_54_1 = var_54_0.awards

			if arg_54_0.nextDisplayAwards and #arg_54_0.nextDisplayAwards > 0:
				for iter_54_0 = 1, #arg_54_0.nextDisplayAwards:
					table.insert(var_54_1, arg_54_0.nextDisplayAwards[iter_54_0])

			arg_54_0.nextDisplayAwards = {}

			arg_54_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_54_1, var_54_0.callback),
		[ActivityProxy.ACTIVITY_SHOW_BB_RESULT] = function(arg_55_0, arg_55_1)
			local var_55_0 = arg_55_1.getBody()

			arg_55_0.viewComponent.emit(ActivityMediator.ON_BOBING_RESULT, var_55_0),
		[ActivityProxy.ACTIVITY_SHOW_LOTTERY_AWARD_RESULT] = function(arg_56_0, arg_56_1)
			local var_56_0 = arg_56_1.getBody()
			local var_56_1 = var_56_0.activityID

			arg_56_0.viewComponent.pageDic[var_56_1].showLotteryAwardResult(var_56_0.awards, var_56_0.number, var_56_0.callback),
		[ActivityProxy.ACTIVITY_SHOW_SHAKE_BEADS_RESULT] = function(arg_57_0, arg_57_1)
			local var_57_0 = arg_57_1.getBody()

			arg_57_0.viewComponent.emit(ActivityMediator.ON_SHAKE_BEADS_RESULT, var_57_0),
		[GAME.COLORING_ACHIEVE_DONE] = function(arg_58_0, arg_58_1)
			arg_58_0.viewComponent.playBonusAnim(function()
				local var_59_0 = arg_58_1.getBody()

				arg_58_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_59_0.drops, function()
					arg_58_0.viewComponent.flush_coloring())),
		[GAME.SUBMIT_TASK_DONE] = function(arg_61_0, arg_61_1)
			local var_61_0 = arg_61_1.getBody()

			arg_61_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_61_0, function()
				arg_61_0.viewComponent.updateTaskLayers()),
		[GAME.ACT_NEW_PT_DONE] = function(arg_63_0, arg_63_1)
			local var_63_0 = arg_63_1.getBody()

			arg_63_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_63_0.awards, var_63_0.callback),
		[GAME.BEGIN_STAGE_DONE] = function(arg_64_0, arg_64_1)
			local var_64_0 = arg_64_1.getBody()

			arg_64_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_64_0),
		[GAME.RETURN_AWARD_OP_DONE] = function(arg_65_0, arg_65_1)
			local var_65_0 = arg_65_1.getBody()

			arg_65_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_65_0.awards),
		[VoteProxy.VOTE_ORDER_BOOK_DELETE] = function(arg_66_0, arg_66_1)
			return,
		[VoteProxy.VOTE_ORDER_BOOK_UPDATE] = function(...)
			arg_49_0.handleDic[VoteProxy.VOTE_ORDER_BOOK_DELETE](...),
		[GAME.REMOVE_LAYERS] = function(arg_68_0, arg_68_1)
			if arg_68_1.getBody().context.mediator == VoteFameHallMediator:
				arg_68_0.viewComponent.updateEntrances()

			arg_68_0.viewComponent.removeLayers(),
		[GAME.MONOPOLY_AWARD_DONE] = function(arg_69_0, arg_69_1)
			local var_69_0 = arg_69_1.getBody()
			local var_69_1 = arg_69_0.viewComponent.pageDic[arg_69_0.viewComponent.activity.id]

			if var_69_1 and var_69_1.activity.getConfig("type") == ActivityConst.ACTIVITY_TYPE_MONOPOLY and var_69_1.onAward:
				var_69_1.onAward(var_69_0.awards, var_69_0.callback)
			else
				arg_69_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_69_0.awards, var_69_0.callback),
		[GAME.SEND_MINI_GAME_OP_DONE] = function(arg_70_0, arg_70_1)
			local var_70_0 = arg_70_1.getBody()
			local var_70_1 = {
				function(arg_71_0)
					local var_71_0 = var_70_0.awards

					if #var_71_0 > 0:
						if arg_70_0.viewComponent:
							arg_70_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_71_0, arg_71_0)
						else
							arg_70_0.emit(BaseUI.ON_ACHIEVE, var_71_0, arg_71_0)
					else
						arg_71_0()
			}

			seriesAsync(var_70_1, function()
				arg_70_0.viewComponent.updateTaskLayers()),
		[GAME.ACTIVITY_PERMANENT_START_DONE] = function(arg_73_0, arg_73_1)
			local var_73_0 = arg_73_1.getBody()

			arg_73_0.viewComponent.verifyTabs(var_73_0.id),
		[GAME.ACTIVITY_PERMANENT_FINISH_DONE] = function(arg_74_0, arg_74_1)
			local var_74_0 = arg_74_1.getBody()

			arg_74_0.viewComponent.emit(ActivityMediator.ACTIVITY_PERMANENT, var_74_0.activity_id),
		[GAME.MEMORYBOOK_UNLOCK_AWARD_DONE] = function(arg_75_0, arg_75_1)
			local var_75_0 = arg_75_1.getBody()

			arg_75_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_75_0.awards),
		[GAME.LOAD_LAYERS] = function(arg_76_0, arg_76_1)
			local var_76_0 = arg_76_1.getBody()

			arg_76_0.viewComponent.loadLayers(),
		[GAME.CHARGE_SUCCESS] = function(arg_77_0, arg_77_1)
			local var_77_0 = arg_77_1.getBody()

			arg_77_0.viewComponent.updateTaskLayers()

			local var_77_1 = Goods.Create({
				shop_id = var_77_0.shopId
			}, Goods.TYPE_CHARGE)

			arg_77_0.viewComponent.OnChargeSuccess(var_77_1),
		[GAME.SHOPPING_DONE] = function(arg_78_0, arg_78_1)
			local var_78_0 = arg_78_1.getBody()

			arg_78_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_78_0.awards, function()
				arg_78_0.viewComponent.updateTaskLayers()),
		[GAME.ACT_MANUAL_SIGN_DONE] = function(arg_80_0, arg_80_1)
			local var_80_0 = arg_80_1.getBody()

			arg_80_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_80_0.awards),
		[ActivityProxy.ACTIVITY_SHOP_SHOW_AWARDS] = function(arg_81_0, arg_81_1)
			local var_81_0 = arg_81_1.getBody()

			arg_81_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_81_0.awards, function()
				local var_82_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.UR_EXCHANGE_MOGADOR_ID)

				if var_82_0 and not var_82_0.isShow():
					arg_81_0.viewComponent.removeActivity(ActivityConst.UR_EXCHANGE_MOGADOR_ID)

				arg_81_0.viewComponent.updateTaskLayers()
				var_81_0.callback())
	}

def var_0_0.showNextActivity(arg_83_0):
	local var_83_0 = getProxy(ActivityProxy)

	if not var_83_0:
		return

	local var_83_1 = var_83_0.findNextAutoActivity()

	if var_83_1:
		if var_83_1.id == ActivityConst.BLACK_FRIDAY_SIGNIN_ACT_ID:
			arg_83_0.contextData.showByNextAct = True

			arg_83_0.viewComponent.verifyTabs(ActivityConst.BLACK_FRIDAY_ACT_ID)
		else
			arg_83_0.viewComponent.verifyTabs(var_83_1.id)

		local var_83_2 = var_83_1.getConfig("type")

		if var_83_2 == ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN:
			arg_83_0.sendNotification(GAME.ACTIVITY_OPERATION, {
				cmd = 1,
				activity_id = var_83_1.id
			})
		elif var_83_2 == ActivityConst.ACTIVITY_TYPE_MONTHSIGN:
			local var_83_3 = var_83_1.getSpecialData("reMonthSignDay") != None and 3 or 1

			arg_83_0.sendNotification(GAME.ACTIVITY_OPERATION, {
				activity_id = var_83_1.id,
				cmd = var_83_3,
				arg1 = var_83_1.getSpecialData("reMonthSignDay")
			})
		elif var_83_2 == ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN:
			arg_83_0.sendNotification(GAME.ACTIVITY_OPERATION, {
				activity_id = var_83_1.id,
				cmd = var_83_1.data1 < 7 and 1 or 2
			})
		elif var_83_1.id == ActivityConst.SHADOW_PLAY_ID:
			var_83_1.clientData1 = 1

			arg_83_0.showNextActivity()
	elif not arg_83_0.viewComponent.activity:
		local var_83_4 = var_83_0.getPanelActivities()
		local var_83_5 = arg_83_0.contextData.id or arg_83_0.contextData.type and checkExist(_.detect(var_83_4, function(arg_84_0)
			return arg_84_0.getConfig("type") == arg_83_0.contextData.type), {
			"id"
		}) or 0

		arg_83_0.viewComponent.verifyTabs(var_83_5)

return var_0_0
