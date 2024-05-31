﻿local var_0_0 = class("EducateTopPanel", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "EducateTopPanel"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0.helpBtn = arg_2_0:findTF("content/btns/help")
	arg_2_0.homeBtn = arg_2_0:findTF("content/btns/home")
	arg_2_0.refresh = arg_2_0:findTF("content/btns/refresh")

	arg_2_0:addListener()
end

function var_0_0.addListener(arg_3_0)
	onButton(arg_3_0, arg_3_0.refresh, function()
		arg_3_0:emit(EducateBaseUI.EDUCATE_ON_MSG_TIP, {
			content = i18n("child_refresh_sure_tip"),
			onYes = function()
				pg.m02:sendNotification(GAME.EDUCATE_REFRESH)
			end
		})
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.child_main_help.tip
		})
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.homeBtn, function()
		arg_3_0:emit(EducateBaseUI.ON_HOME)
	end, SFX_PANEL)
end

function var_0_0.OnDestroy(arg_8_0)
	return
end

return var_0_0
