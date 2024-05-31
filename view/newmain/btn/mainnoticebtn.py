local var_0_0 = class("MainNoticeBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	if #getProxy(ServerNoticeProxy).getServerNotices(False) > 0:
		arg_1_0.emit(NewMainMediator.OPEN_NOTICE)
	else
		pg.TipsMgr.GetInstance().ShowTips(i18n("no_notice_tip"))

return var_0_0
