local var_0_0 = class("MsgboxSubPanel", BaseSubPanel)

def var_0_0.Load(arg_1_0):
	if arg_1_0._state != var_0_0.STATES.NONE:
		return

	arg_1_0._state = var_0_0.STATES.LOADING

	pg.UIMgr.GetInstance().LoadingOn()

	local var_1_0 = PoolMgr.GetInstance()

	var_1_0.GetUI(arg_1_0.getUIName(), False, function(arg_2_0)
		if arg_1_0._state == var_0_0.STATES.DESTROY:
			pg.UIMgr.GetInstance().LoadingOff()
			var_1_0.ReturnUI(arg_1_0.getUIName(), arg_2_0)
		else
			arg_1_0.Loaded(arg_2_0)
			arg_1_0.Init())

def var_0_0.SetWindowSize(arg_3_0, arg_3_1):
	setSizeDelta(arg_3_0.viewParent._window, arg_3_1)

def var_0_0.UpdateView(arg_4_0, arg_4_1):
	arg_4_0.PreRefresh(arg_4_1)
	arg_4_0.OnRefresh(arg_4_1)
	arg_4_0.PostRefresh(arg_4_1)

def var_0_0.PreRefresh(arg_5_0, arg_5_1):
	arg_5_0.viewParent.commonSetting(arg_5_1)
	arg_5_0.Show()

def var_0_0.PostRefresh(arg_6_0, arg_6_1):
	arg_6_0.viewParent.Loaded(arg_6_1)

def var_0_0.OnRefresh(arg_7_0, arg_7_1):
	return

def var_0_0.closeView(arg_8_0):
	pg.MsgboxMgr.GetInstance().hide()

return var_0_0
