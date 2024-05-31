local var_0_0 = class("NewMainMediator", import("..base.ContextMediator"))

var_0_0.GO_SCENE = "NewMainMediator.GO_SCENE"
var_0_0.OPEN_MAIL = "NewMainMediator.OPEN_MAIL"
var_0_0.OPEN_NOTICE = "NewMainMediator.OPEN_NOTICE"
var_0_0.GO_SNAPSHOT = "NewMainMediator.GO_SNAPSHOT"
var_0_0.OPEN_COMMISION = "NewMainMediator.OPEN_COMMISION"
var_0_0.OPEN_CHATVIEW = "NewMainMediator.OPEN_CHATVIEW"
var_0_0.SKIP_SCENE = "NewMainMediator.SKIP_SCENE"
var_0_0.SKIP_ACTIVITY = "NewMainMediator.SKIP_ACTIVITY"
var_0_0.SKIP_SHOP = "NewMainMediator.SKIP_SHOP"
var_0_0.GO_MINI_GAME = "NewMainMediator.GO_MINI_GAME"
var_0_0.SKIP_ACTIVITY_MAP = "NewMainMediator.SKIP_ACTIVITY_MAP"
var_0_0.SKIP_ESCORT = "NewMainMediator.SKIP_ESCORT"
var_0_0.SKIP_INS = "NewMainMediator.SKIP_INS"
var_0_0.SKIP_LOTTERY = "NewMainMediator.SKIP_LOTTERY"
var_0_0.GO_SINGLE_ACTIVITY = "NewMainMediator.GO_SINGLE_ACTIVITY"
var_0_0.REFRESH_VIEW = "NewMainMediator.REFRESH_VIEW"
var_0_0.OPEN_DORM_SELECT_LAYER = "NewMainMediator.OPEN_DORM_SELECT_LAYER"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.GO_SINGLE_ACTIVITY, function(arg_2_0, arg_2_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ActivitySingleMediator,
			viewComponent = ActivitySingleScene,
			data = {
				id = arg_2_1
			}
		})))
	arg_1_0.bind(var_0_0.SKIP_LOTTERY, function(arg_3_0, arg_3_1)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = LotteryLayer,
			mediator = LotteryMediator,
			data = {
				activityId = arg_3_1
			}
		})))
	arg_1_0.bind(var_0_0.SKIP_INS, function(arg_4_0)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = InstagramLayer,
			mediator = InstagramMediator
		})))
	arg_1_0.bind(var_0_0.SKIP_ESCORT, function(arg_5_0)
		local var_5_0 = getProxy(ChapterProxy)
		local var_5_1 = var_5_0.getMapsByType(Map.ESCORT)[1]
		local var_5_2 = var_5_0.getActiveChapter()

		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
			chapterId = var_5_2 and var_5_2.getConfig("map") == var_5_1.id and var_5_2.id or None,
			mapIdx = var_5_1.id
		}))
	arg_1_0.bind(var_0_0.SKIP_ACTIVITY_MAP, function(arg_6_0)
		local var_6_0 = getProxy(ChapterProxy)
		local var_6_1, var_6_2 = var_6_0.getLastMapForActivity()

		warning(var_6_1)
		warning(var_6_1 and var_6_0.getMapById(var_6_1).isUnlock())

		if not var_6_1 or not var_6_0.getMapById(var_6_1).isUnlock():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
				chapterId = var_6_2,
				mapIdx = var_6_1
			}))
	arg_1_0.bind(var_0_0.SKIP_SHOP, function(arg_7_0, arg_7_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
			warp = arg_7_1 or NewShopsScene.TYPE_ACTIVITY
		}))
	arg_1_0.bind(var_0_0.SKIP_ACTIVITY, function(arg_8_0, arg_8_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = arg_8_1
		}))
	arg_1_0.bind(var_0_0.SKIP_SCENE, function(arg_9_0, arg_9_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, arg_9_1[1], arg_9_1[2]))
	arg_1_0.bind(var_0_0.GO_MINI_GAME, function(arg_10_0, arg_10_1)
		arg_1_0.sendNotification(GAME.GO_MINI_GAME, arg_10_1))
	arg_1_0.bind(var_0_0.GO_SCENE, function(arg_11_0, arg_11_1, arg_11_2)
		arg_1_0.sendNotification(GAME.GO_SCENE, arg_11_1, arg_11_2))
	arg_1_0.bind(var_0_0.GO_SNAPSHOT, function(arg_12_0)
		local var_12_0 = arg_1_0.viewComponent.bgView.ship
		local var_12_1 = var_12_0.skinId
		local var_12_2 = arg_1_0.viewComponent.paintingView.IsLive2DState()
		local var_12_3

		if isa(var_12_0, VirtualEducateCharShip):
			var_12_3 = var_12_0.educateCharId
			var_12_2 = False

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SNAPSHOT, {
			skinId = var_12_1,
			live2d = var_12_2,
			tbId = var_12_3,
			propose = arg_1_0.viewComponent.bgView.propose
		}))
	arg_1_0.bind(var_0_0.OPEN_MAIL, function(arg_13_0)
		if BATTLE_DEBUG:
			arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
				system = SYSTEM_DEBUG
			})
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.MAIL))
	arg_1_0.bind(var_0_0.OPEN_NOTICE, function(arg_14_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = NewBulletinBoardMediator,
			viewComponent = NewBulletinBoardLayer
		})))
	arg_1_0.bind(var_0_0.OPEN_COMMISION, function(arg_15_0)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = CommissionInfoLayer,
			mediator = CommissionInfoMediator
		})))
	arg_1_0.bind(var_0_0.OPEN_CHATVIEW, function(arg_16_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = NotificationMediator,
			viewComponent = NotificationLayer,
			data = {
				form = NotificationLayer.FORM_MAIN
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_DORM_SELECT_LAYER, function(arg_17_0)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DORM3DSELECT))

def var_0_0.listNotificationInterests(arg_18_0):
	local var_18_0 = {
		GAME.REMOVE_LAYERS,
		GAME.GET_GUILD_INFO_DONE,
		GAME.GET_GUILD_CHAT_LIST_DONE,
		GAME.ON_OPEN_INS_LAYER,
		GAME.BEGIN_STAGE_DONE,
		GAME.SEND_MINI_GAME_OP_DONE,
		GAME.FETCH_NPC_SHIP_DONE,
		GAME.ZERO_HOUR_OP_DONE,
		GAME.CONFIRM_GET_SHIP,
		GAME.WILL_LOGOUT,
		GAME.GET_FEAST_DATA_DONE,
		GAME.FETCH_VOTE_INFO_DONE,
		GAME.ROTATE_PAINTING_INDEX,
		GAME.LOAD_LAYERS,
		GAME.GUILD_GET_USER_INFO_DONE,
		GAME.GET_PUBLIC_GUILD_USER_DATA_DONE,
		NotificationProxy.FRIEND_REQUEST_ADDED,
		NotificationProxy.FRIEND_REQUEST_REMOVED,
		FriendProxy.FRIEND_NEW_MSG,
		FriendProxy.FRIEND_UPDATED,
		PlayerProxy.UPDATED,
		ChatProxy.NEW_MSG,
		GuildProxy.NEW_MSG_ADDED,
		ChapterProxy.CHAPTER_TIMESUP,
		TaskProxy.TASK_ADDED,
		TechnologyConst.UPDATE_REDPOINT_ON_TOP,
		MiniGameProxy.ON_HUB_DATA_UPDATE,
		var_0_0.REFRESH_VIEW
	}

	for iter_18_0, iter_18_1 in pairs(pg.redDotHelper.GetNotifyType()):
		for iter_18_2, iter_18_3 in pairs(iter_18_1):
			if not table.contains(var_18_0, iter_18_3):
				table.insert(var_18_0, iter_18_3)

	return var_18_0

def var_0_0.handleNotification(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_1.getName()
	local var_19_1 = arg_19_1.getBody()

	pg.redDotHelper.Notify(var_19_0)

	if var_19_0 == GAME.ON_OPEN_INS_LAYER:
		arg_19_0.viewComponent.emit(var_0_0.SKIP_INS)
	elif var_19_0 == NotificationProxy.FRIEND_REQUEST_ADDED or var_19_0 == NotificationProxy.FRIEND_REQUEST_REMOVED or var_19_0 == FriendProxy.FRIEND_NEW_MSG or var_19_0 == FriendProxy.FRIEND_UPDATED or var_19_0 == ChatProxy.NEW_MSG or var_19_0 == GuildProxy.NEW_MSG_ADDED or var_19_0 == GAME.GET_GUILD_INFO_DONE or var_19_0 == GAME.GET_GUILD_CHAT_LIST_DONE:
		arg_19_0.viewComponent.emit(GAME.ANY_CHAT_MSG_UPDATE)
	elif var_19_0 == GAME.BEGIN_STAGE_DONE:
		arg_19_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_19_1)
	elif var_19_0 == ChapterProxy.CHAPTER_TIMESUP:
		MainChapterTimeUpSequence.New().Execute()
	elif var_19_0 == TechnologyConst.UPDATE_REDPOINT_ON_TOP:
		MainTechnologySequence.New().Execute(function()
			return)
	elif var_19_0 == GAME.FETCH_NPC_SHIP_DONE:
		arg_19_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_19_1.items, var_19_1.callback)
	elif var_19_0 == var_0_0.REFRESH_VIEW:
		arg_19_0.viewComponent.setVisible(False)
		arg_19_0.viewComponent.setVisible(True)
	elif var_19_0 == GAME.CONFIRM_GET_SHIP:
		arg_19_0.addSubLayers(Context.New({
			mediator = BuildShipRemindMediator,
			viewComponent = BuildShipRemindLayer,
			data = {
				ships = var_19_1.ships
			},
			onRemoved = var_19_1.callback
		}))

	arg_19_0.viewComponent.emit(var_19_0, var_19_1)

return var_0_0
