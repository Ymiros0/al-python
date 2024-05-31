local var_0_0 = class("GuildMainMediator", import("..base.ContextMediator"))

var_0_0.OPEN_MEMBER = "GuildMainMediator.OPEN_MEMBER"
var_0_0.CLOSE_MEMBER = "GuildMainMediator.CLOSE_MEMBER"
var_0_0.OPEN_APPLY = "GuildMainMediator.OPEN_APPLY"
var_0_0.CLOSE_APPLY = "GuildMainMediator.CLOSE_APPLY"
var_0_0.MODIFY = "GuildMainMediator.MODIFY"
var_0_0.DISSOLVE = "GuildMainMediator.DISSOLVE"
var_0_0.QUIT = "GuildMainMediator.QUIT"
var_0_0.ON_BACK = "GuildMainMediator.ON_BACK"
var_0_0.REBUILD_ALL = "GuildMainMediator.REBUILD_ALL"
var_0_0.ON_REBUILD_LOG_ALL = "GuildMainMediator.ON_REBUILD_LOG_ALL"
var_0_0.SEND_MSG = "GuildMainMediator.SEND_MSG"
var_0_0.OPEN_EMOJI = "GuildMainMediator.OPEN_EMOJI"
var_0_0.OPEN_OFFICE = "GuildMainMediator.OPEN_OFFICE"
var_0_0.OPEN_TECH = "GuildMainMediator.OPEN_TECH"
var_0_0.OPEN_BATTLE = "GuildMainMediator.OPEN_BATTLE"
var_0_0.CLOSE_OFFICE = "GuildMainMediator.CLOSE_OFFICE"
var_0_0.CLOSE_TECH = "GuildMainMediator.CLOSE_TECH"
var_0_0.CLOSE_BATTLE = "GuildMainMediator.CLOSE_BATTLE"
var_0_0.ON_FETCH_CAPITAL = "GuildOfficeMediator.ON_FETCH_CAPITAL"
var_0_0.ON_FETCH_CAPITAL_LOG = "GuildOfficeMediator.ON_FETCH_CAPITAL_LOG"
var_0_0.OPEN_EVENT_REPORT = "GuildOfficeMediator.OPEN_EVENT_REPORT"
var_0_0.OPEN_EVENT = "GuildOfficeMediator.OPEN_EVENT"
var_0_0.OPEN_MAIN = "GuildOfficeMediator.OPEN_MAIN"
var_0_0.SWITCH_TO_OFFICE = "GuildOfficeMediator.SWITCH_TO_OFFICE"
var_0_0.OPEN_SHOP = "GuildMainMediator.OPEN_SHOP"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(ContextProxy)
	local var_1_1 = var_1_0.GetPrevContext(1)

	if var_1_1.mediator == NewGuildMediator:
		var_1_0.RemoveContext(var_1_1)

	local var_1_2 = getProxy(GuildProxy)
	local var_1_3 = var_1_2.getData()

	arg_1_0.viewComponent.setGuildVO(var_1_3)

	local var_1_4 = var_1_2.getChatMsgs()

	arg_1_0.viewComponent.setChatMsgs(var_1_4)
	arg_1_0.bind(var_0_0.OPEN_SHOP, function()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
			warp = NewShopsScene.TYPE_GUILD
		}))
	arg_1_0.bind(var_0_0.OPEN_MAIN, function()
		arg_1_0.closePage(GuildEventReportMediator))
	arg_1_0.bind(var_0_0.OPEN_EVENT, function(arg_4_0)
		arg_1_0.viewComponent.openPage(GuildMainScene.TOGGLE_TAG[6]))
	arg_1_0.bind(var_0_0.OPEN_EVENT_REPORT, function(arg_5_0)
		arg_1_0.sendNotification(GAME.GUILD_OPEN_EVENT_REPORT))
	arg_1_0.bind(var_0_0.ON_FETCH_CAPITAL, function(arg_6_0)
		arg_1_0.sendNotification(GAME.GUILD_REFRESH_CAPITAL))

	local var_1_5 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayerVO(var_1_5)
	arg_1_0.bind(var_0_0.ON_BACK, function(arg_7_0)
		arg_1_0.sendNotification(GAME.GO_BACK))
	arg_1_0.bind(var_0_0.REBUILD_ALL, function(arg_8_0)
		local var_8_0 = getProxy(GuildProxy).getChatMsgs()

		arg_1_0.viewComponent.UpdateAllChat(var_8_0))
	arg_1_0.bind(var_0_0.OPEN_MEMBER, function()
		arg_1_0.closePage(GuildEventReportMediator)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = GuildMemberLayer,
			mediator = GuildMemberMediator
		})))
	arg_1_0.bind(var_0_0.CLOSE_MEMBER, function()
		arg_1_0.closePage(GuildMemberMediator))
	arg_1_0.bind(var_0_0.OPEN_APPLY, function()
		arg_1_0.closePage(GuildEventReportMediator)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = GuildRequestLayer,
			mediator = GuildRequestMediator
		})))
	arg_1_0.bind(var_0_0.CLOSE_APPLY, function()
		arg_1_0.closePage(GuildRequestMediator))
	arg_1_0.bind(var_0_0.MODIFY, function(arg_13_0, arg_13_1, arg_13_2, arg_13_3)
		arg_1_0.sendNotification(GAME.MODIFY_GUILD_INFO, {
			type = arg_13_1,
			int = arg_13_2,
			string = arg_13_3
		}))
	arg_1_0.bind(var_0_0.DISSOLVE, function(arg_14_0, arg_14_1)
		arg_1_0.sendNotification(GAME.GUILD_DISSOLVE, arg_14_1))
	arg_1_0.bind(var_0_0.QUIT, function(arg_15_0, arg_15_1)
		arg_1_0.sendNotification(GAME.GUILD_QUIT, arg_15_1))
	arg_1_0.bind(var_0_0.ON_REBUILD_LOG_ALL, function(arg_16_0)
		local var_16_0 = getProxy(GuildProxy).getData().getLogs()

		arg_1_0.viewComponent.UpdateAllLog(var_16_0))
	arg_1_0.bind(var_0_0.SEND_MSG, function(arg_17_0, arg_17_1)
		arg_1_0.sendNotification(GAME.GUILD_SEND_MSG, arg_17_1))
	arg_1_0.bind(var_0_0.OPEN_EMOJI, function(arg_18_0, arg_18_1, arg_18_2)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = EmojiLayer,
			mediator = EmojiMediator,
			data = {
				pos = arg_18_1,
				callback = arg_18_2,
				def emojiIconCallback:(arg_19_0)
					arg_1_0.viewComponent.insertEmojiToInputText(arg_19_0)
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_OFFICE, function()
		arg_1_0.closePage(GuildEventReportMediator)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = GuildOfficeLayer,
			mediator = GuildOfficeMediator
		})))
	arg_1_0.bind(var_0_0.CLOSE_OFFICE, function()
		arg_1_0.closePage(GuildOfficeMediator))
	arg_1_0.bind(var_0_0.OPEN_TECH, function()
		arg_1_0.closePage(GuildEventReportMediator)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = GuildTechnologyLayer,
			mediator = GuildTechnologyMediator
		})))
	arg_1_0.bind(var_0_0.CLOSE_TECH, function()
		arg_1_0.closePage(GuildTechnologyMediator))
	arg_1_0.bind(var_0_0.ON_FETCH_CAPITAL_LOG, function(arg_24_0)
		if var_1_2.getData().shouldRequestCapitalLog():
			arg_1_0.sendNotification(GAME.GUILD_FETCH_CAPITAL_LOG)
		else
			arg_1_0.viewComponent.openResourceLog())
	arg_1_0.bind(var_0_0.OPEN_BATTLE, function()
		arg_1_0.closePage(GuildEventReportMediator)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = GuildEventLayer,
			mediator = GuildEventMediator
		})))
	arg_1_0.bind(var_0_0.CLOSE_BATTLE, function()
		arg_1_0.closePage(GuildEventMediator))

	local var_1_6 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayerVO(var_1_6)

def var_0_0.closePage(arg_27_0, arg_27_1):
	local var_27_0 = getProxy(ContextProxy).getContextByMediator(arg_27_1)

	if var_27_0:
		arg_27_0.sendNotification(GAME.REMOVE_LAYERS, {
			context = var_27_0
		})

def var_0_0.listNotificationInterests(arg_28_0):
	return {
		GuildProxy.GUILD_UPDATED,
		GuildProxy.EXIT_GUILD,
		GAME.MODIFY_GUILD_INFO_DONE,
		GuildProxy.NEW_MSG_ADDED,
		GuildProxy.LOG_ADDED,
		GuildProxy.REQUEST_COUNT_UPDATED,
		GuildProxy.REQUEST_DELETED,
		GAME.GUILD_GET_REQUEST_LIST_DONE,
		GAME.REMOVE_LAYERS,
		PlayerProxy.UPDATED,
		GAME.GUILD_FETCH_CAPITAL_LOG_DONE,
		GAME.GUILD_COMMIT_DONATE_DONE,
		GuildProxy.ON_DELETED_MEMBER,
		GuildProxy.ON_ADDED_MEMBER,
		GAME.GUILD_OPEN_EVENT_REPORT,
		GuildProxy.BATTLE_BTN_FLAG_CHANGE,
		GAME.BEGIN_STAGE_DONE,
		GAME.SUBMIT_GUILD_REPORT_DONE,
		GuildTechnologyMediator.ON_OPEN_OFFICE,
		GAME.OPEN_MSGBOX_DONE,
		GuildProxy.TECHNOLOGY_START,
		GAME.GO_WORLD_BOSS_SCENE,
		GAME.GUILD_START_TECH_DONE,
		GuildMainMediator.SWITCH_TO_OFFICE,
		GAME.ON_GUILD_JOIN_EVENT_DONE,
		GAME.GUILD_JOIN_MISSION_DONE,
		GAME.GUILD_GET_SUPPLY_AWARD_DONE,
		GAME.LOAD_LAYERS,
		GAME.REMOVE_LAYERS
	}

def var_0_0.handleNotification(arg_29_0, arg_29_1):
	local var_29_0 = arg_29_1.getName()
	local var_29_1 = arg_29_1.getBody()

	if var_29_0 == GuildProxy.GUILD_UPDATED:
		arg_29_0.viewComponent.setGuildVO(var_29_1)
	elif var_29_0 == GuildProxy.EXIT_GUILD:
		arg_29_0.viewComponent.emit(var_0_0.ON_BACK)
	elif var_29_0 == GAME.MODIFY_GUILD_INFO_DONE:
		arg_29_0.viewComponent.initTheme()
	elif var_29_0 == GuildProxy.NEW_MSG_ADDED:
		arg_29_0.viewComponent.Append(var_29_1, -1)
	elif var_29_0 == GuildProxy.LOG_ADDED:
		arg_29_0.viewComponent.AppendLog(var_29_1, True)
	elif var_29_0 == GuildProxy.REQUEST_COUNT_UPDATED or var_29_0 == GuildProxy.REQUEST_DELETED or var_29_0 == GAME.GUILD_GET_REQUEST_LIST_DONE:
		local var_29_2 = getProxy(GuildProxy)

		arg_29_0.viewComponent.UpdateNotices(GuildMainScene.NOTIFY_TYPE_APPLY)
	elif var_29_0 == GAME.GUILD_FETCH_CAPITAL_LOG_DONE:
		arg_29_0.viewComponent.openResourceLog()
	elif var_29_0 == PlayerProxy.UPDATED:
		arg_29_0.viewComponent.setPlayerVO(var_29_1)
		arg_29_0.viewComponent.UpdateRes()
	elif var_29_0 == GAME.GUILD_COMMIT_DONATE_DONE or var_29_0 == GAME.GUILD_GET_SUPPLY_AWARD_DONE:
		arg_29_0.viewComponent.UpdateNotices(GuildMainScene.NOTIFY_TYPE_OFFICE)
	elif GuildProxy.ON_DELETED_MEMBER == var_29_0:
		arg_29_0.viewComponent.OnDeleteMember(var_29_1.member)
	elif GuildProxy.ON_ADDED_MEMBER == var_29_0:
		arg_29_0.viewComponent.OnAddMember(var_29_1.member)
	elif var_29_0 == GAME.GUILD_OPEN_EVENT_REPORT:
		arg_29_0.addSubLayers(Context.New({
			viewComponent = GuildEventReportLayer,
			mediator = GuildEventReportMediator
		}))
	elif var_29_0 == GAME.SUBMIT_GUILD_REPORT_DONE:
		arg_29_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_29_1.awards, var_29_1.callback)
		arg_29_0.viewComponent.OnReportUpdated()
		arg_29_0.viewComponent.UpdateNotices(GuildMainScene.NOTIFY_TYPE_BATTLE)
		arg_29_0.viewComponent.UpdateNotices(GuildMainScene.NOTIFY_TYPE_MAIN)
	elif var_29_0 == GuildProxy.BATTLE_BTN_FLAG_CHANGE or var_29_0 == GAME.ON_GUILD_JOIN_EVENT_DONE or var_29_0 == GAME.GUILD_ACTIVE_EVENT_DONE or var_29_0 == GAME.GUILD_JOIN_MISSION_DONE:
		arg_29_0.viewComponent.UpdateNotices(GuildMainScene.NOTIFY_TYPE_BATTLE)
	elif var_29_0 == GAME.BEGIN_STAGE_DONE:
		arg_29_0.sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_29_1)
	elif var_29_0 == GuildTechnologyMediator.ON_OPEN_OFFICE:
		local var_29_3 = arg_29_0.contextData.toggles[GuildMainScene.TOGGLE_TAG[4]]

		triggerToggle(var_29_3, True)
	elif var_29_0 == GAME.OPEN_MSGBOX_DONE:
		pg.GuildLayerMgr.GetInstance().OnShowMsgBox()
	elif var_29_0 == GuildProxy.TECHNOLOGY_START:
		arg_29_0.viewComponent.UpdateNotices(GuildMainScene.NOTIFY_TYPE_TECH)
	elif var_29_0 == GAME.GUILD_START_TECH_DONE:
		local var_29_4 = getProxy(PlayerProxy).getData()

		arg_29_0.viewComponent.setPlayerVO(var_29_4)
		arg_29_0.viewComponent.UpdateRes()
	elif var_29_0 == GAME.GO_WORLD_BOSS_SCENE:
		arg_29_0.contextData.page = None
	elif var_29_0 == GuildMainMediator.SWITCH_TO_OFFICE:
		arg_29_0.viewComponent.TriggerOfficePage()
	elif var_29_0 == GAME.LOAD_LAYERS:
		if var_29_1.context.mediator == AwardInfoMediator:
			pg.GuildLayerMgr.GetInstance().UnBlurTopPanel()
	elif var_29_0 == GAME.REMOVE_LAYERS and var_29_1.context.mediator == AwardInfoMediator:
		pg.GuildLayerMgr.GetInstance()._BlurTopPanel()

return var_0_0
