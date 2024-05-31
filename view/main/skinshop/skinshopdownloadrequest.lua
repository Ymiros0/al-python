local var_0_0 = class("SkinShopDownloadRequest")

function var_0_0.Ctor(arg_1_0)
	arg_1_0.downloadui = GameObject.Find("/OverlayCamera/Overlay/UIMain/DialogPanel")
end

function var_0_0.Start(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0:Refresh(true, arg_2_1, arg_2_2)
end

function var_0_0.Refresh(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = BundleWizard.Inst:GetGroupMgr("L2D")
	local var_3_1 = var_3_0.state

	if var_3_1 == DownloadState.None or var_3_1 == DownloadState.CheckFailure then
		var_3_0:CheckD()
	end

	local var_3_2 = false
	local var_3_3 = false
	local var_3_4 = var_3_0:CheckF(arg_3_2)

	if var_3_4 == DownloadState.None then
		-- block empty
	elseif var_3_4 == DownloadState.Checking then
		-- block empty
	elseif var_3_4 == DownloadState.CheckToUpdate and arg_3_1 then
		VersionMgr.Inst:RequestUIForUpdateF("L2D", arg_3_2, true)
	elseif var_3_4 == DownloadState.CheckToUpdate and not isActive(arg_3_0.downloadui) then
		var_3_3 = true
	elseif var_3_4 == DownloadState.CheckOver then
		-- block empty
	elseif var_3_4 == DownloadState.CheckFailure then
		var_3_3 = true
	elseif var_3_4 == DownloadState.Updating then
		-- block empty
	elseif var_3_4 == DownloadState.UpdateFailure then
		var_3_3 = true
	elseif var_3_4 == DownloadState.UpdateSuccess then
		var_3_3 = true
		var_3_2 = checkABExist(arg_3_2)
	end

	if arg_3_0.live2dTimer then
		arg_3_0.live2dTimer:Stop()

		arg_3_0.live2dTimer = nil
	end

	if var_3_4 == DownloadState.CheckToUpdate or var_3_4 == DownloadState.UpdateFailure or var_3_4 == DownloadState.Updating then
		arg_3_0.live2dTimer = Timer.New(function()
			arg_3_0:Refresh(false, arg_3_2, arg_3_3)
		end, 0.5, 1)

		arg_3_0.live2dTimer:Start()
	end

	if var_3_3 then
		arg_3_3(var_3_2)
	end
end

function var_0_0.Dispose(arg_5_0)
	if arg_5_0.live2dTimer then
		arg_5_0.live2dTimer:Stop()

		arg_5_0.live2dTimer = nil
	end
end

return var_0_0
