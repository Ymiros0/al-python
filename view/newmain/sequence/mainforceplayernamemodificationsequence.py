local var_0_0 = class("MainForcePlayerNameModificationSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	if getProxy(PlayerProxy).getRawData().WhetherServerModifiesName():
		arg_1_0.ShowModityPlayerNameWindow(arg_1_1)
	else
		arg_1_1()

def var_0_0.ShowModityPlayerNameWindow(arg_2_0, arg_2_1):
	arg_2_0.renameWindow = arg_2_0.renameWindow or ForcePlayerNameModificationPage.New(pg.UIMgr.GetInstance().OverlayMain)

	arg_2_0.renameWindow.ExecuteAction("Show", function()
		arg_2_0.Clear())

def var_0_0.Clear(arg_4_0):
	if arg_4_0.renameWindow:
		arg_4_0.renameWindow.Destroy()

		arg_4_0.renameWindow = None

def var_0_0.Dispose(arg_5_0):
	arg_5_0.Clear()

return var_0_0
