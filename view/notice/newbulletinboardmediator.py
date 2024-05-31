local var_0_0 = class("NewBulletinBoardMediator", import("..base.ContextMediator"))

var_0_0.SET_STOP_REMIND = "set_stop_remind"
var_0_0.GO_SCENE = "go_scene"
var_0_0.TRACK_OPEN_URL = "track_open_url"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(ServerNoticeProxy)

	var_1_0.setStopNewTip()

	local var_1_1 = var_1_0.getServerNotices(False)

	arg_1_0.viewComponent.initNotices(var_1_1)
	arg_1_0.bind(var_0_0.SET_STOP_REMIND, function(arg_2_0, arg_2_1)
		getProxy(ServerNoticeProxy).setStopRemind(arg_2_1))
	arg_1_0.bind(var_0_0.GO_SCENE, function(arg_3_0, arg_3_1, ...)
		arg_1_0.sendNotification(GAME.GO_SCENE, arg_3_1, ...))
	arg_1_0.bind(var_0_0.TRACK_OPEN_URL, function(arg_4_0, arg_4_1)
		TrackConst.Track(TrackConst.TRACK_NEW_BULLETIN_OPEN_URL, TrackConst.EVENT_NEW_BULLETIN_OPEN_URL, arg_4_1))

def var_0_0.initNotificationHandleDic(arg_5_0):
	arg_5_0.handleDic = {}

return var_0_0
