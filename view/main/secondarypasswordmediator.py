local var_0_0 = class("SecondaryPasswordMediator", import("view.base.ContextMediator"))

var_0_0.CONFIRM_PASSWORD = "SecondaryPasswordMediator.CONFIRM_PASSWORD"
var_0_0.SET_PASSWORD = "SecondaryPasswordMediator.SET_PASSWORD"
var_0_0.CANCEL_OPERATION = "SecondaryPasswordMediator.CANCEL_OPERATION"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.CONFIRM_PASSWORD, function(arg_2_0, arg_2_1)
		if arg_1_0.contextData.type == pg.SecondaryPWDMgr.CHANGE_SETTING or arg_1_0.contextData.type == pg.SecondaryPWDMgr.CLOSE_PASSWORD:
			arg_1_0.sendNotification(GAME.SET_PASSWORD_SETTINGS, {
				pwd = arg_2_1,
				settings = arg_1_0.contextData.settings
			})
		else
			arg_1_0.sendNotification(GAME.CONFIRM_PASSWORD, {
				pwd = arg_2_1
			}))
	arg_1_0.bind(var_0_0.SET_PASSWORD, function(arg_3_0, arg_3_1, arg_3_2)
		arg_3_2 = var_0_0.ClipUnicodeStr(arg_3_2, 20)

		arg_1_0.sendNotification(GAME.SET_PASSWORD, {
			pwd = arg_3_1,
			tip = arg_3_2,
			settings = arg_1_0.contextData.settings
		}))
	arg_1_0.bind(var_0_0.CANCEL_OPERATION, function()
		arg_1_0.sendNotification(GAME.CANCEL_LIMITED_OPERATION))

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		GAME.CONFIRM_PASSWORD_DONE,
		GAME.SET_PASSWORD_SETTINGS_DONE,
		GAME.FETCH_PASSWORD_STATE_DONE,
		GAME.SET_PASSWORD_DONE
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()
	local var_6_2 = getProxy(SecondaryPWDProxy)
	local var_6_3 = var_6_2.getRawData()

	if var_6_0 == GAME.FETCH_PASSWORD_STATE_DONE:
		if not var_6_2.GetPermissionState():
			arg_6_0.sendNotification(GAME.CANCEL_LIMITED_OPERATION)

			local var_6_4 = {
				mode = "showresttime",
				title = "warning",
				hideNo = True,
				type = MSGBOX_TYPE_SECONDPWD,
				def onPreShow:()
					arg_6_0.viewComponent.emit(BaseUI.ON_CLOSE)
			}

			pg.MsgboxMgr.GetInstance().ShowMsgBox(var_6_4)
	elif var_6_0 == GAME.CONFIRM_PASSWORD_DONE or var_6_0 == GAME.SET_PASSWORD_SETTINGS_DONE:
		local var_6_5 = var_6_1.result

		if var_6_5 > 0:
			if var_6_5 == 9:
				var_6_3.fail_count = var_6_3.fail_count + 1

				if var_6_3.fail_count >= 5:
					arg_6_0.sendNotification(GAME.FETCH_PASSWORD_STATE)
				else
					pg.TipsMgr.GetInstance().ShowTips(string.format(i18n("secondarypassword_incorrectpwd_error"), 5 - var_6_3.fail_count))
			elif var_6_5 == 40 or var_6_5 == 1:
				arg_6_0.sendNotification(GAME.FETCH_PASSWORD_STATE)
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("", var_6_5))

			arg_6_0.viewComponent.UpdateView()
			arg_6_0.viewComponent.ClearInputs()
		else
			arg_6_0.CloseAndCallback()
	elif var_6_0 == GAME.SET_PASSWORD_DONE:
		local var_6_6 = var_6_1.result

		if var_6_6 > 0:
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", var_6_6))
			arg_6_0.sendNotification(GAME.FETCH_PASSWORD_STATE)
		else
			arg_6_0.CloseAndCallback()

def var_0_0.CloseAndCallback(arg_8_0):
	local var_8_0 = arg_8_0.contextData.callback

	arg_8_0.viewComponent.emit(BaseUI.ON_CLOSE)

	if var_8_0:
		var_8_0()

def var_0_0.ClipUnicodeStr(arg_9_0, arg_9_1):
	local var_9_0, var_9_1 = utf8_to_unicode(arg_9_0)

	if arg_9_1 < var_9_1:
		local var_9_2 = string.sub(var_9_0, 1, -7)
		local var_9_3, var_9_4 = utf8_to_unicode(unicode_to_utf8(var_9_2))

		while arg_9_1 < var_9_4 - 1:
			var_9_2 = string.sub(var_9_2, 1, -7)

			local var_9_5

			var_9_5, var_9_4 = utf8_to_unicode(unicode_to_utf8(var_9_2))

		return string.sub(unicode_to_utf8(var_9_2), 1, -2)

	return arg_9_0

return var_0_0
