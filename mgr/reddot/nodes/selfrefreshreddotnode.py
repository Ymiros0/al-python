local var_0_0 = class("SelfRefreshRedDotNode", import(".RedDotNode"))

def var_0_0.Init(arg_1_0):
	var_0_0.super.Init(arg_1_0)
	arg_1_0.AddTimer()

def var_0_0.AddTimer(arg_2_0):
	arg_2_0.RemoveTimer()

	arg_2_0.timer = Timer.New(function()
		arg_2_0.Check(), 10, -1)

	arg_2_0.timer.Start()

def var_0_0.Check(arg_4_0):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.types):
		pg.RedDotMgr.GetInstance().NotifyAll(iter_4_1)

def var_0_0.RemoveTimer(arg_5_0):
	if arg_5_0.timer:
		arg_5_0.timer.Stop()

		arg_5_0.timer = None

def var_0_0.Remove(arg_6_0):
	arg_6_0.RemoveTimer()

def var_0_0.Resume(arg_7_0):
	if arg_7_0.timer:
		arg_7_0.timer.Resume()

def var_0_0.Puase(arg_8_0):
	if arg_8_0.timer:
		arg_8_0.timer.Pause()

return var_0_0
