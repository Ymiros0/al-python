local var_0_0 = class("FriendInfoMediator", import("..base.ContextMediator"))

var_0_0.OPEND_FRIEND = "FriendInfoMediator.OPEND_FRIEND"
var_0_0.OPEN_RESUME = "FriendInfoMediator.OPEN_RESUME"
var_0_0.OPEN_BACKYARD = "FriendInfoMediator.OPEN_BACKYARD"
var_0_0.TOGGLE_BLACK = "FriendInfoMediator.TOGGLE_BLACK"
var_0_0.INFORM = "FriendInfoMediator.INFORM"
var_0_0.INFORM_BACKYARD = "FriendInfoMediator.INFORM_BACKYARD"

def var_0_0.register(arg_1_0):
	local var_1_0 = arg_1_0.contextData.friend

	assert(var_1_0, "friend is None")
	arg_1_0.viewComponent.setFriend(var_1_0)
	arg_1_0.bind(var_0_0.INFORM_BACKYARD, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4)
		arg_1_0.sendNotification(GAME.INFORM_THEME_TEMPLATE, {
			uid = arg_2_1,
			content = arg_2_2,
			tid = arg_2_3,
			playerName = arg_2_4
		}))
	arg_1_0.bind(var_0_0.OPEND_FRIEND, function(arg_3_0)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			limit = 20,
			yesText = "text_apply",
			type = MSGBOX_TYPE_INPUT,
			placeholder = i18n("friend_request_msg_placeholder"),
			title = i18n("friend_request_msg_title"),
			def onYes:(arg_4_0)
				arg_1_0.sendNotification(GAME.FRIEND_SEND_REQUEST, {
					id = var_1_0.id,
					msg = arg_4_0
				})
		}))
	arg_1_0.bind(var_0_0.OPEN_RESUME, function(arg_5_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = resumeMediator,
			viewComponent = resumeLayer,
			data = {
				player = var_1_0,
				parent = arg_1_0.contextData.parent,
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_NOTIFICATION
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_BACKYARD, function(arg_6_0)
		arg_1_0.sendNotification(GAME.VISIT_BACKYARD, var_1_0.id))
	arg_1_0.bind(var_0_0.TOGGLE_BLACK, function(arg_7_0)
		local var_7_0 = getProxy(FriendProxy)
		local var_7_1 = var_1_0.id

		if var_7_0.getBlackPlayerById(var_7_1) != None:
			arg_1_0.sendNotification(GAME.FRIEND_RELIEVE_BLACKLIST, var_7_1)
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = False,
				content = i18n("friend_confirm_add_blacklist", var_1_0.name),
				def onYes:()
					arg_1_0.sendNotification(GAME.FRIEND_ADD_BLACKLIST, var_1_0)
			}))
	arg_1_0.bind(var_0_0.INFORM, function(arg_9_0, arg_9_1, arg_9_2, arg_9_3)
		arg_1_0.sendNotification(GAME.INFORM, {
			playerId = arg_9_1,
			info = arg_9_2,
			content = arg_9_3
		}))

	local var_1_1 = getProxy(FriendProxy)

	if not var_1_1.getBlackList():
		arg_1_0.sendNotification(GAME.GET_BLACK_LIST)

	arg_1_0.viewComponent.setFriendProxy(var_1_1)

def var_0_0.listNotificationInterests(arg_10_0):
	return {
		GAME.VISIT_BACKYARD_DONE,
		GAME.GET_BLACK_LIST_DONE,
		GAME.FRIEND_ADD_BLACKLIST_DONE,
		GAME.FRIEND_RELIEVE_BLACKLIST_DONE,
		GAME.INFORM_DONE,
		GAME.INFORM_THEME_TEMPLATE_DONE,
		GAME.FINISH_STAGE
	}

def var_0_0.handleNotification(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.getName()
	local var_11_1 = arg_11_1.getBody()

	if var_11_0 == GAME.VISIT_BACKYARD_DONE:
		arg_11_0.viewComponent.emit(BaseUI.ON_CLOSE)
		arg_11_0.sendNotification(GAME.GO_SCENE, SCENE.COURTYARD, {
			player = var_11_1.player,
			dorm = var_11_1.dorm,
			mode = CourtYardConst.SYSTEM_VISIT
		})
	elif var_11_0 == GAME.GET_BLACK_LIST_DONE or var_11_0 == GAME.FRIEND_ADD_BLACKLIST_DONE or var_11_0 == GAME.FRIEND_RELIEVE_BLACKLIST_DONE:
		arg_11_0.viewComponent.updateBlack()
	elif var_11_0 == GAME.INFORM_DONE or var_11_0 == GAME.INFORM_THEME_TEMPLATE_DONE:
		arg_11_0.viewComponent.closeInfromPanel()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			parent = arg_11_0.contextData.parent,
			content = i18n("inform_sueecss_tip")
		})
	elif var_11_0 == GAME.FINISH_STAGE:
		arg_11_0.viewComponent.closeView()

return var_0_0
