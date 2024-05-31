local var_0_0 = class("SkinShopDownloadRequest")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.downloadui = GameObject.Find("/OverlayCamera/Overlay/UIMain/DialogPanel")

def var_0_0.Start(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.Refresh(True, arg_2_1, arg_2_2)

def var_0_0.Refresh(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = BundleWizard.Inst.GetGroupMgr("L2D")
	local var_3_1 = var_3_0.state

	if var_3_1 == DownloadState.None or var_3_1 == DownloadState.CheckFailure:
		var_3_0.CheckD()

	local var_3_2 = False
	local var_3_3 = False
	local var_3_4 = var_3_0.CheckF(arg_3_2)

	if var_3_4 == DownloadState.None:
		-- block empty
	elif var_3_4 == DownloadState.Checking:
		-- block empty
	elif var_3_4 == DownloadState.CheckToUpdate and arg_3_1:
		VersionMgr.Inst.RequestUIForUpdateF("L2D", arg_3_2, True)
	elif var_3_4 == DownloadState.CheckToUpdate and not isActive(arg_3_0.downloadui):
		var_3_3 = True
	elif var_3_4 == DownloadState.CheckOver:
		-- block empty
	elif var_3_4 == DownloadState.CheckFailure:
		var_3_3 = True
	elif var_3_4 == DownloadState.Updating:
		-- block empty
	elif var_3_4 == DownloadState.UpdateFailure:
		var_3_3 = True
	elif var_3_4 == DownloadState.UpdateSuccess:
		var_3_3 = True
		var_3_2 = checkABExist(arg_3_2)

	if arg_3_0.live2dTimer:
		arg_3_0.live2dTimer.Stop()

		arg_3_0.live2dTimer = None

	if var_3_4 == DownloadState.CheckToUpdate or var_3_4 == DownloadState.UpdateFailure or var_3_4 == DownloadState.Updating:
		arg_3_0.live2dTimer = Timer.New(function()
			arg_3_0.Refresh(False, arg_3_2, arg_3_3), 0.5, 1)

		arg_3_0.live2dTimer.Start()

	if var_3_3:
		arg_3_3(var_3_2)

def var_0_0.Dispose(arg_5_0):
	if arg_5_0.live2dTimer:
		arg_5_0.live2dTimer.Stop()

		arg_5_0.live2dTimer = None

return var_0_0
