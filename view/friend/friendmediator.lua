﻿local var_0_0 = class("FriendMediator", import("..base.ContextMediator"))

var_0_0.SEARCH_FRIEND = "FriendMediator:SEARCH_FRIEND"
var_0_0.ADD_FRIEND = "FriendMediator:ADD_FRIEND"
var_0_0.ACCEPT_REQUEST = "FriendMediator:ACCEPT_REQUEST"
var_0_0.REFUSE_REQUEST = "FriendMediator:REFUSE_REQUEST"
var_0_0.DELETE_FRIEND = "FriendMediator:DELETE_FRIEND"
var_0_0.OPEN_RESUME = "FriendMediator:OPEN_RESUME"
var_0_0.OPEN_RESUME_BY_VO = "FriendMediator:OPEN_RESUME_BY_VO"
var_0_0.REFUSE_ALL_REQUEST = "FriendMediator:REFUSE_ALL_REQUEST"
var_0_0.OPEN_CHATROOM = "FriendMediator:OPEN_CHATROOM"
var_0_0.VISIT_BACKYARD = "FriendMediator:VISIT_BACKYRAD"
var_0_0.RELIEVE_BLACKLIST = "FriendMediator:RELIEVE_BLACKLIST"
var_0_0.GET_BLACK_LIST = "FriendMediator:GET_BLACK_LIST"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(FriendProxy)
	local var_1_1 = var_1_0:getAllFriends()

	arg_1_0.viewComponent:setFriendVOs(var_1_1)

	local var_1_2 = getProxy(PlayerProxy):getData()

	arg_1_0.viewComponent:setPlayer(var_1_2)

	local var_1_3 = getProxy(NotificationProxy):getRequests()

	arg_1_0.viewComponent:setRequests(var_1_3)

	local var_1_4 = var_1_0:getBlackList()

	arg_1_0.viewComponent:setBlackList(var_1_4)
	arg_1_0:bind(var_0_0.GET_BLACK_LIST, function(arg_2_0)
		arg_1_0:sendNotification(GAME.GET_BLACK_LIST)
	end)
	arg_1_0:bind(var_0_0.SEARCH_FRIEND, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(GAME.FRIEND_SEARCH, {
			type = arg_3_1,
			keyword = arg_3_2
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_CHATROOM, function(arg_4_0, arg_4_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = ChatRoomMediator,
			viewComponent = ChatRoomLayer,
			data = {
				friendVO = arg_4_1
			}
		}))
	end)
	arg_1_0:bind(var_0_0.ADD_FRIEND, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0:sendNotification(GAME.FRIEND_SEND_REQUEST, {
			id = arg_5_1,
			msg = arg_5_2
		})
	end)
	arg_1_0:bind(var_0_0.ACCEPT_REQUEST, function(arg_6_0, arg_6_1)
		arg_1_0:sendNotification(GAME.FRIEND_ACCEPT_REQUEST, arg_6_1)
	end)
	arg_1_0:bind(var_0_0.REFUSE_ALL_REQUEST, function(arg_7_0)
		arg_1_0:sendNotification(GAME.FRIEND_REJECT_REQUEST, 0)
	end)
	arg_1_0:bind(var_0_0.REFUSE_REQUEST, function(arg_8_0, arg_8_1, arg_8_2)
		arg_1_0:sendNotification(GAME.FRIEND_REJECT_REQUEST, arg_8_1.id)

		if arg_8_2 then
			arg_1_0:sendNotification(GAME.FRIEND_ADD_BLACKLIST, arg_8_1)
		end
	end)
	arg_1_0:bind(var_0_0.DELETE_FRIEND, function(arg_9_0, arg_9_1)
		arg_1_0:sendNotification(GAME.FRIEND_DELETE, arg_9_1)
	end)
	arg_1_0:bind(var_0_0.OPEN_RESUME, function(arg_10_0, arg_10_1)
		arg_1_0:sendNotification(GAME.FRIEND_SEARCH, {
			type = SearchFriendCommand.SEARCH_TYPE_RESUME,
			keyword = arg_10_1
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_RESUME_BY_VO, function(arg_11_0, arg_11_1)
		arg_1_0:openResume(arg_11_1)
	end)
	arg_1_0:bind(var_0_0.VISIT_BACKYARD, function(arg_12_0, arg_12_1)
		arg_1_0:sendNotification(GAME.VISIT_BACKYARD, arg_12_1)
	end)
	arg_1_0:bind(var_0_0.RELIEVE_BLACKLIST, function(arg_13_0, arg_13_1)
		arg_1_0:sendNotification(GAME.FRIEND_RELIEVE_BLACKLIST, arg_13_1)
	end)
	arg_1_0:updateChatNotification()
end

function var_0_0.updateChatNotification(arg_14_0)
	local var_14_0 = getProxy(FriendProxy):getNewMsgCount()

	arg_14_0.viewComponent:updateChatNotification(var_14_0)
end

function var_0_0.openResume(arg_15_0, arg_15_1)
	arg_15_0:addSubLayers(Context.New({
		mediator = resumeMediator,
		viewComponent = resumeLayer,
		data = {
			player = arg_15_1
		}
	}))
end

function var_0_0.listNotificationInterests(arg_16_0)
	return {
		GAME.FRIEND_SEARCH_DONE,
		GAME.FRIEND_SEND_REQUEST_DONE,
		NotificationProxy.FRIEND_REQUEST_REMOVED,
		NotificationProxy.FRIEND_REQUEST_ADDED,
		FriendProxy.FRIEND_REMOVED,
		FriendProxy.FRIEND_ADDED,
		FriendProxy.FRIEND_UPDATED,
		GAME.VISIT_BACKYARD_DONE,
		GAME.FRIEND_RELIEVE_BLACKLIST_DONE,
		FriendProxy.RELIEVE_BLACKLIST,
		FriendProxy.BLACK_LIST_UPDATED,
		FriendProxy.ADD_INTO_BLACKLIST
	}
end

function var_0_0.handleNotification(arg_17_0, arg_17_1)
	local var_17_0 = arg_17_1:getName()
	local var_17_1 = arg_17_1:getBody()

	if var_17_0 == GAME.FRIEND_SEARCH_DONE then
		if var_17_1.type == SearchFriendCommand.SEARCH_TYPE_RESUME then
			arg_17_0:openResume(var_17_1.list[1])
		else
			arg_17_0.viewComponent:setSearchResult(var_17_1.list)
			arg_17_0.viewComponent:updatePage(FriendScene.SEARCH_PAGE)

			if table.getCount(var_17_1.list) > 0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("friend_search_succeed"))
			end
		end
	elseif var_17_0 == GAME.FRIEND_SEND_REQUEST_DONE then
		arg_17_0.viewComponent:removeSearchResult(var_17_1)
		arg_17_0.viewComponent:updatePage(FriendScene.SEARCH_PAGE)
	elseif var_17_0 == NotificationProxy.FRIEND_REQUEST_REMOVED or var_17_0 == NotificationProxy.FRIEND_REQUEST_ADDED then
		local var_17_2 = getProxy(NotificationProxy):getRequests()

		arg_17_0.viewComponent:setRequests(var_17_2)
		arg_17_0.viewComponent:updatePage(FriendScene.REQUEST_PAGE)
		arg_17_0.viewComponent:updateRequestTip()
	elseif var_17_0 == FriendProxy.FRIEND_REMOVED or var_17_0 == FriendProxy.FRIEND_ADDED or var_17_0 == FriendProxy.FRIEND_UPDATED then
		local var_17_3 = getProxy(FriendProxy):getAllFriends()

		arg_17_0.viewComponent:setFriendVOs(var_17_3)
		arg_17_0.viewComponent:updatePage(FriendScene.FRIEND_PAGE)

		if var_17_0 == FriendProxy.FRIEND_UPDATED then
			arg_17_0:updateChatNotification()
		end
	elseif var_17_0 == FriendProxy.RELIEVE_BLACKLIST or var_17_0 == FriendProxy.BLACK_LIST_UPDATED or var_17_0 == FriendProxy.ADD_INTO_BLACKLIST then
		local var_17_4 = getProxy(FriendProxy):getBlackList()

		arg_17_0.viewComponent:setBlackList(var_17_4)
		arg_17_0.viewComponent:updatePage(FriendScene.BLACKLIST_PAGE)
	elseif var_17_0 == GAME.VISIT_BACKYARD_DONE then
		arg_17_0:sendNotification(GAME.GO_SCENE, SCENE.COURTYARD, {
			player = var_17_1.player,
			dorm = var_17_1.dorm,
			mode = CourtYardConst.SYSTEM_VISIT
		})
	end
end

return var_0_0
