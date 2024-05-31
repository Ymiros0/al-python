local var_0_0 = class("RegisterPanelView", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "RegisterPanelView"

def var_0_0.OnLoaded(arg_2_0):
	return

def var_0_0.SetShareData(arg_3_0, arg_3_1):
	arg_3_0.shareData = arg_3_1

def var_0_0.OnInit(arg_4_0):
	arg_4_0.registerPanel = arg_4_0._tf
	arg_4_0.registerUsername = arg_4_0.findTF("account/username", arg_4_0.registerPanel)
	arg_4_0.cancelButton = arg_4_0.findTF("cancel_button", arg_4_0.registerPanel)
	arg_4_0.confirmButton = arg_4_0.findTF("confirm_button", arg_4_0.registerPanel)

	arg_4_0.InitEvent()

def var_0_0.InitEvent(arg_5_0):
	onButton(arg_5_0, arg_5_0.confirmButton, function()
		local var_6_0 = getInputText(arg_5_0.registerUsername)

		if var_6_0 == "":
			pg.TipsMgr.GetInstance().ShowTips(i18n("login_loginScene_error_noUserName"))
			ActivateInputField(arg_5_0.registerUsername)

			return

		local var_6_1 = User.New({
			arg3 = "",
			arg2 = "",
			type = 2,
			arg1 = var_6_0
		})

		if var_6_1:
			arg_5_0.event.emit(LoginMediator.ON_REGISTER, var_6_1), SFX_CONFIRM)
	onButton(arg_5_0, arg_5_0.cancelButton, function()
		arg_5_0.emit(LoginSceneConst.SWITCH_SUB_VIEW, {
			LoginSceneConst.DEFINE.LOGIN_PANEL_VIEW
		}), SFX_CANCEL)

def var_0_0.Clear(arg_8_0):
	return

def var_0_0.OnDestroy(arg_9_0):
	return

return var_0_0
