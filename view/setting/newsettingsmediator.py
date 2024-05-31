local var_0_0 = class("NewSettingsMediator", import("..base.ContextMediator"))

var_0_0.SHOW_DESC = "NewSettingsMediator.SHOW_DESC"
var_0_0.ON_LOGOUT = "NewSettingsMediator.ON_LOGOUT"
var_0_0.ON_SECON_PWD_STATE_CHANGE = "NewSettingsMediator.ON_SECON_PWD_STATE_CHANGE"
var_0_0.OPEN_YOSTAR_ALERT_VIEW = "NewSettingsMediator.OPEN_YOSTAR_ALERT_VIEW"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_LOGOUT, function(arg_2_0)
		arg_1_0.sendNotification(GAME.LOGOUT, {
			code = 0
		}))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		var_0_0.SHOW_DESC,
		var_0_0.ON_SECON_PWD_STATE_CHANGE,
		var_0_0.OPEN_YOSTAR_ALERT_VIEW,
		GAME.EXCHANGECODE_USE_SUCCESS,
		GAME.ON_GET_TRANSCODE,
		GAME.ON_SOCIAL_LINKED,
		GAME.ON_SOCIAL_UNLINKED,
		GAME.CHANGE_RANDOM_SHIP_MODE_DONE
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == var_0_0.SHOW_DESC:
		arg_4_0.viewComponent.OnShowDescWindow(var_4_1)
	elif var_4_0 == GAME.EXCHANGECODE_USE_SUCCESS:
		arg_4_0.viewComponent.OnClearExchangeCode()
	elif var_4_0 == GAME.ON_GET_TRANSCODE:
		arg_4_0.viewComponent.OnShowTranscode(var_4_1.transcode)
	elif var_4_0 == GAME.ON_SOCIAL_LINKED or var_4_0 == GAME.ON_SOCIAL_UNLINKED:
		arg_4_0.viewComponent.OnCheckAllAccountState()
		arg_4_0.viewComponent.CloseYostarAlertView()
		pg.UIMgr.GetInstance().LoadingOff()
	elif var_4_0 == var_0_0.ON_SECON_PWD_STATE_CHANGE:
		arg_4_0.viewComponent.OnSecondPwdStateChange()
	elif var_4_0 == var_0_0.OPEN_YOSTAR_ALERT_VIEW:
		arg_4_0.viewComponent.OpenYostarAlertView()
	elif var_4_0 == GAME.CHANGE_RANDOM_SHIP_MODE_DONE:
		arg_4_0.viewComponent.OnRandomFlagShipModeUpdate()

return var_0_0
