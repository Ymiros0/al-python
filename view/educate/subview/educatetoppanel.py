local var_0_0 = class("EducateTopPanel", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "EducateTopPanel"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.helpBtn = arg_2_0.findTF("content/btns/help")
	arg_2_0.homeBtn = arg_2_0.findTF("content/btns/home")
	arg_2_0.refresh = arg_2_0.findTF("content/btns/refresh")

	arg_2_0.addListener()

def var_0_0.addListener(arg_3_0):
	onButton(arg_3_0, arg_3_0.refresh, function()
		arg_3_0.emit(EducateBaseUI.EDUCATE_ON_MSG_TIP, {
			content = i18n("child_refresh_sure_tip"),
			def onYes:()
				pg.m02.sendNotification(GAME.EDUCATE_REFRESH)
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.child_main_help.tip
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.homeBtn, function()
		arg_3_0.emit(EducateBaseUI.ON_HOME), SFX_PANEL)

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
