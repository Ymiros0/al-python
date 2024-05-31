local var_0_0 = class("PlayerVitaeLive2dBtn", import(".PlayerVitaeBaseBtn"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.Load(arg_1_0.tf)
	setActive(arg_1_0.tf, True)

def var_0_0.InitBtn(arg_2_0):
	return

def var_0_0.GetBgName(arg_3_0):
	local var_3_0
	local var_3_1
	local var_3_2 = arg_3_0.IsHrzType() and "share/btn_l2d_atlas" or "admiralui_atlas"

	if arg_3_0.ship and arg_3_0.ship.GetSkinConfig().spine_use_live2d == 1:
		var_3_1 = arg_3_0.IsHrzType() and "spine_painting_bg" or "sp"
	else
		var_3_1 = arg_3_0.IsHrzType() and "live2d_bg" or "l2d"

	return var_3_2, var_3_1

def var_0_0.IsActive(arg_4_0):
	return True

def var_0_0.Update(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	var_0_0.super.Update(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	arg_5_0.NewGo()
	arg_5_0.RequesetLive2dRes()

def var_0_0.RequesetLive2dRes(arg_6_0):
	local var_6_0 = arg_6_0.ship
	local var_6_1 = "live2d/" .. string.lower(var_6_0.getPainting())
	local var_6_2 = HXSet.autoHxShiftPath(var_6_1, None, True)

	arg_6_0.StartCheckUpdate(var_6_2)

def var_0_0.StartCheckUpdate(arg_7_0, arg_7_1):
	local var_7_0 = BundleWizard.Inst.GetGroupMgr("L2D")
	local var_7_1 = var_7_0.state

	if var_7_1 == DownloadState.None or var_7_1 == DownloadState.CheckFailure:
		var_7_0.CheckD()

	local var_7_2 = var_7_0.CheckF(arg_7_1)

	if var_7_2 == DownloadState.CheckToUpdate or var_7_2 == DownloadState.UpdateFailure:
		arg_7_0.ShowOrHide(True)
		arg_7_0.UpdateBtnState(False, False)
		onButton(arg_7_0, arg_7_0.tf, function()
			VersionMgr.Inst.RequestUIForUpdateF("L2D", arg_7_1, True), SFX_PANEL)
	elif var_7_2 == DownloadState.Updating:
		arg_7_0.ShowOrHide(True)
		arg_7_0.UpdateBtnState(True, False)
		removeOnButton(arg_7_0.tf)
	else
		local var_7_3 = checkABExist(arg_7_1)

		arg_7_0.ShowOrHide(var_7_3)

		if var_7_3:
			arg_7_0.UpdateBtnState(False, False)
			var_0_0.super.InitBtn(arg_7_0)

	if arg_7_0.live2dTimer:
		arg_7_0.live2dTimer.Stop()

		arg_7_0.live2dTimer = None

	if var_7_2 == DownloadState.CheckToUpdate or var_7_2 == DownloadState.UpdateFailure or var_7_2 == DownloadState.Updating:
		arg_7_0.live2dTimer = Timer.New(function()
			arg_7_0.StartCheckUpdate(arg_7_1), 0.5, 1)

		arg_7_0.live2dTimer.Start()

def var_0_0.GetDefaultValue(arg_10_0):
	return getProxy(SettingsProxy).getCharacterSetting(arg_10_0.ship.id, SHIP_FLAG_L2D)

def var_0_0.OnSwitch(arg_11_0, arg_11_1):
	getProxy(SettingsProxy).setCharacterSetting(arg_11_0.ship.id, SHIP_FLAG_L2D, arg_11_1)

	return True

def var_0_0.OnDispose(arg_12_0):
	if arg_12_0.live2dTimer:
		arg_12_0.live2dTimer.Stop()

		arg_12_0.live2dTimer = None

def var_0_0.Load(arg_13_0, arg_13_1):
	var_0_0.super.Load(arg_13_0, arg_13_1)

	if arg_13_0.IsHrzType():
		arg_13_1.gameObject.name = "live2d"

	arg_13_0.tf.GetComponent(typeof(Image)).SetNativeSize()

return var_0_0
