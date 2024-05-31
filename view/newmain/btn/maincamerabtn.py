local var_0_0 = class("MainCameraBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	arg_1_0.OpenCamera()

def var_0_0.Flush(arg_2_0, arg_2_1):
	local var_2_0 = pg.SdkMgr.GetInstance().IsAUPackage()

	setActive(arg_2_0._tf, not var_2_0)

def var_0_0.OpenCamera(arg_3_0):
	if pg.SdkMgr.GetInstance().IsYunPackage():
		pg.TipsMgr.GetInstance().ShowTips("指挥官，当前平台不支持该功能哦")

		return

	local var_3_0
	local var_3_1

	local function var_3_2()
		arg_3_0.emit(NewMainMediator.GO_SNAPSHOT)

	local function var_3_3()
		if CameraHelper.IsAndroid():
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("apply_permission_camera_tip3"),
				def onYes:()
					CameraHelper.RequestCamera(var_3_2, var_3_3)
			})
		elif CameraHelper.IsIOS():
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("apply_permission_camera_tip2")
			})

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		content = i18n("apply_permission_camera_tip1"),
		def onYes:()
			CameraHelper.RequestCamera(var_3_2, var_3_3)
	})

return var_0_0
