local var_0_0 = class("SnapshotScene", import("..base.BaseUI"))

var_0_0.SELECT_CHAR_PANEL = "SnapshotScene.SELECT_CHAR_PANEL"
var_0_0.SHARE_PANEL = "SnapshotScene.SHARE_PANEL"
var_0_0.SHOW_PAINT = 0
var_0_0.SHOW_LIVE2D = 1
var_0_0.SHOW_SPINE = 2
var_0_0.STATE_TAKE_PHOTO = 0
var_0_0.STATE_TAKE_VIDEO = 1

def var_0_0.getUIName(arg_1_0):
	return "snapshot"

def var_0_0.init(arg_2_0):
	setActive(pg.UIMgr.GetInstance().OverlayEffect, False)

	arg_2_0.dummy = arg_2_0.findTF("SnapshotInvisible")

	arg_2_0.SetDummyForIOS(True)

	arg_2_0.ui = arg_2_0.findTF("ui")
	arg_2_0.backBtn = arg_2_0.findTF("ui/back")
	arg_2_0.switchDirBtn = arg_2_0.findTF("ui/switchDir")
	arg_2_0.takeBtn = arg_2_0.findTF("ui/bg/take")
	arg_2_0.videoTakeImg = arg_2_0.findTF("ui/bg/take/videoTakeImg")

	SetActive(arg_2_0.videoTakeImg, False)

	arg_2_0.switchCamBtn = arg_2_0.findTF("ui/bg/switchCam")
	arg_2_0.selectCharBtn = arg_2_0.findTF("ui/bg/selectChar")
	arg_2_0.l2dCtrlPanl = arg_2_0.findTF("ui/bg/l2dBgImg")
	arg_2_0.l2dStopBtnGo = arg_2_0.findTF("ui/bg/l2dBgImg/stopBtn")
	arg_2_0.l2dPlayBtnGo = arg_2_0.findTF("ui/bg/l2dBgImg/playBtn")

	SetActive(arg_2_0.l2dPlayBtnGo, False)

	arg_2_0.l2dAnimationBtnGo = arg_2_0.findTF("ui/bg/l2dBgImg/animationsBtn").gameObject
	arg_2_0.l2dAnimations = arg_2_0.findTF("ui/bg/animationsBg")
	arg_2_0.l2dAnimationBackBtnTrans = arg_2_0.findTF("animationsBackBtn", arg_2_0.l2dAnimations)

	SetActive(arg_2_0.l2dAnimations, False)

	arg_2_0.selectedID = 1
	arg_2_0.scrollItems = {}
	arg_2_0.isPause = False
	arg_2_0.animTpl = arg_2_0.findTF("animation_tpl", arg_2_0.l2dAnimations)

	SetActive(arg_2_0.animTpl, False)

	arg_2_0.animLayout = arg_2_0.findTF("animation_container/animations", arg_2_0.l2dAnimations)
	arg_2_0.animContainer = arg_2_0.findTF("animation_container", arg_2_0.l2dAnimations).GetComponent("LScrollRect")
	arg_2_0.animContainer.decelerationRate = 0.1

	function arg_2_0.animContainer.onInitItem(arg_3_0)
		arg_2_0.onInitItem(arg_3_0)

	function arg_2_0.animContainer.onUpdateItem(arg_4_0, arg_4_1)
		arg_2_0.onUpdateItem(arg_4_0, arg_4_1)

	function arg_2_0.animContainer.onReturnItem(arg_5_0, arg_5_1)
		arg_2_0.onReturnItem(arg_5_0, arg_5_1)

	function arg_2_0.animContainer.onStart()
		arg_2_0.updateSelectedItem()

	arg_2_0.paintBtn = arg_2_0.findTF("ui/bg/paintBtn")
	arg_2_0.live2dBtn = arg_2_0.findTF("ui/bg/l2dBgImg/live2dBtn")
	arg_2_0.spineBtn = arg_2_0.findTF("ui/bg/spineBtn")
	arg_2_0.modePnlTF = arg_2_0.findTF("ui/bg/modePnl")
	arg_2_0.takePhotoBtn = arg_2_0.findTF("ui/bg/modePnl/takePhotoBtn")
	arg_2_0.takeVideoBtn = arg_2_0.findTF("ui/bg/modePnl/takeVideoBtn")
	arg_2_0.stopRecBtn = arg_2_0.findTF("stopRec")
	arg_2_0.snapshot = arg_2_0.findTF("snapshot")
	arg_2_0.webcam = arg_2_0.snapshot.GetComponent(typeof(WebCam))
	arg_2_0.ysScreenShoter = arg_2_0.snapshot.GetComponent(typeof(YSTool.YSScreenShoter))
	arg_2_0.ysScreenRecorder = arg_2_0.snapshot.GetComponent(typeof(YSTool.YSScreenRecorder))
	arg_2_0.paint = arg_2_0.findTF("container/paint")
	arg_2_0.live2d = arg_2_0.findTF("live2d", arg_2_0.paint)
	arg_2_0.spine = arg_2_0.findTF("spine", arg_2_0.paint)
	arg_2_0.paintSkin = None
	arg_2_0.showLive2d = False
	arg_2_0.showType = var_0_0.SHOW_PAINT
	arg_2_0.state = var_0_0.STATE_TAKE_PHOTO

	arg_2_0.setSkinAndLive2d(arg_2_0.contextData.skinId, arg_2_0.contextData.live2d)

	arg_2_0.verticalEulerAngle = 90
	arg_2_0.horizontalEulerAngle = 0
	arg_2_0.rotateUseTime = 0.2
	arg_2_0.isVertical = False
	arg_2_0.backBtnImg = arg_2_0.findTF("ui/back/Image")
	arg_2_0.selectCharBtnImg = arg_2_0.findTF("ui/bg/selectChar/Image")
	arg_2_0.switchCamBtnImg = arg_2_0.findTF("ui/bg/switchCam/Image")
	arg_2_0.l2dBtnImg = arg_2_0.findTF("ui/bg/paintBtn/Image")
	arg_2_0.l2dStopBtnImg = arg_2_0.findTF("ui/bg/l2dBgImg/stopBtn/Image")
	arg_2_0.l2dPlayBtnImg = arg_2_0.findTF("ui/bg/l2dBgImg/playBtn/Image")
	arg_2_0.l2d2PaintBtnImg = arg_2_0.findTF("ui/bg/l2dBgImg/live2dBtn/Image")
	arg_2_0.takePhotoVerticalText = arg_2_0.findTF("ui/bg/modePnl/takePhotoBtn/verticalText")
	arg_2_0.takePhotoHorizontalText = arg_2_0.findTF("ui/bg/modePnl/takePhotoBtn/horizontalText")
	arg_2_0.takePhotoVerticalText.GetComponent("Text").text = i18n("word_photo_mode")
	arg_2_0.takePhotoHorizontalText.GetComponent("Text").text = i18n("word_photo_mode")

	SetActive(arg_2_0.takePhotoHorizontalText, False)

	arg_2_0.takeVideoVerticalText = arg_2_0.findTF("ui/bg/modePnl/takeVideoBtn/verticalText")
	arg_2_0.takeVideoHorizontalText = arg_2_0.findTF("ui/bg/modePnl/takeVideoBtn/horizontalText")
	arg_2_0.takeVideoVerticalText.GetComponent("Text").text = i18n("word_video_mode")
	arg_2_0.takeVideoHorizontalText.GetComponent("Text").text = i18n("word_video_mode")

	SetActive(arg_2_0.takeVideoHorizontalText, False)

	arg_2_0.isFlipping = False
	arg_2_0.videoTipPanel = arg_2_0.findTF("videoTipPanel")

	setActive(arg_2_0.videoTipPanel, False)

def var_0_0.back(arg_7_0):
	if arg_7_0.exited:
		return

	arg_7_0.emit(var_0_0.ON_BACK)

def var_0_0.saveVideo(arg_8_0):
	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		content = i18n("word_save_video"),
		def onYes:()
			YARecorder.Inst.DiscardVideo()
	})

def var_0_0.didEnter(arg_10_0):
	onButton(arg_10_0, arg_10_0.backBtn, function()
		arg_10_0.back())
	onButton(arg_10_0, arg_10_0.switchDirBtn, function()
		arg_10_0.isVertical = not arg_10_0.isVertical

		arg_10_0.updateUIDirection()
		arg_10_0.updateCameraCanvas())
	onButton(arg_10_0, arg_10_0.takeBtn, function()
		if arg_10_0.state == var_0_0.STATE_TAKE_PHOTO:
			setActive(arg_10_0.ui, False)

			local function var_13_0(arg_14_0)
				warning("截图结果：" .. tostring(arg_14_0))
				setActive(arg_10_0.ui, True)

			local function var_13_1(arg_15_0)
				local var_15_0 = UnityEngine.Texture2D.New(Screen.width, Screen.height)

				Tex2DExtension.LoadImage(var_15_0, arg_15_0)
				arg_10_0.emit(var_0_0.SHARE_PANEL, var_15_0, arg_15_0)

				if PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance().GetChannelUID() == "2":
					print("start photo . play sound")
					NotificationMgr.Inst.PlayShutterSound()

			arg_10_0.ysScreenShoter.TakeScreenShotData(var_13_0, var_13_1)
		elif arg_10_0.state == var_0_0.STATE_TAKE_VIDEO:
			setActive(arg_10_0.ui, False)

			local function var_13_2(arg_16_0)
				if arg_16_0 != -1:
					setActive(arg_10_0.ui, True)
					LeanTween.moveX(arg_10_0.stopRecBtn, arg_10_0.stopRecBtn.rect.width, 0.15)

			local function var_13_3(arg_17_0)
				warning("开始录屏结果：" .. tostring(arg_17_0))

			local function var_13_4()
				setActive(arg_10_0.stopRecBtn, True)
				LeanTween.moveX(arg_10_0.stopRecBtn, 0, 0.15).setOnComplete(System.Action(function()
					arg_10_0.SetMute(True)
					arg_10_0.ysScreenRecorder.BeforeStart()
					arg_10_0.ysScreenRecorder.StartRecord(var_13_3, var_13_2)))

			local var_13_5 = PlayerPrefs.GetInt("hadShowForVideoTip")

			if not var_13_5 or var_13_5 <= 0:
				PlayerPrefs.SetInt("hadShowForVideoTip", 1)

				arg_10_0.findTF("Text", arg_10_0.videoTipPanel).GetComponent("Text").text = i18n("word_take_video_tip")

				onButton(arg_10_0, arg_10_0.videoTipPanel, function()
					setActive(arg_10_0.videoTipPanel, False)
					var_13_4()

					if PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance().GetChannelUID() == "2":
						print("start recording . play sound")
						NotificationMgr.Inst.PlayStartRecordSound())
				setActive(arg_10_0.videoTipPanel, True)
			else
				var_13_4())
	onButton(arg_10_0, arg_10_0.paintBtn, function()
		if arg_10_0.showType == var_0_0.SHOW_PAINT:
			arg_10_0.clearSkin()

			arg_10_0.showType = var_0_0.SHOW_LIVE2D

			arg_10_0.updateShowType()
			arg_10_0.updateSkin()
			arg_10_0.ResetL2dPanel())
	onButton(arg_10_0, arg_10_0.live2dBtn, function()
		if arg_10_0.showType == var_0_0.SHOW_LIVE2D:
			arg_10_0.clearSkin()

			arg_10_0.showType = var_0_0.SHOW_PAINT

			arg_10_0.updateShowType()
			arg_10_0.updateSkin())
	onButton(arg_10_0, arg_10_0.spineBtn, function()
		if arg_10_0.showType == var_0_0.SHOW_SPINE:
			arg_10_0.clearSkin()

			arg_10_0.showType = var_0_0.SHOW_PAINT

			arg_10_0.updateShowType()
			arg_10_0.updateSkin())

	local function var_10_0()
		if arg_10_0.state == var_0_0.STATE_TAKE_PHOTO:
			return

		arg_10_0.state = var_0_0.STATE_TAKE_PHOTO

		LeanTween.moveY(rtf(arg_10_0.modePnlTF), 56, 0.1)
		SetActive(arg_10_0.videoTakeImg, False)

	onButton(arg_10_0, arg_10_0.takePhotoBtn, var_10_0)
	onButton(arg_10_0, arg_10_0.takeVideoBtn, function()
		if CheckPermissionGranted(ANDROID_RECORD_AUDIO_PERMISSION) and CheckPermissionGranted(ANDROID_WRITE_EXTERNAL_PERMISSION):
			arg_10_0.changeToTakeVideo()
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("apply_permission_record_audio_tip1"),
				def onYes:()
					ApplyPermission({
						ANDROID_RECORD_AUDIO_PERMISSION,
						ANDROID_WRITE_EXTERNAL_PERMISSION
					})
			}))
	var_10_0()
	onButton(arg_10_0, arg_10_0.stopRecBtn, function()
		local function var_27_0(arg_28_0)
			warning("结束录屏结果：" .. tostring(arg_28_0))

		if not LeanTween.isTweening(go(arg_10_0.stopRecBtn)):
			LeanTween.moveX(arg_10_0.stopRecBtn, arg_10_0.stopRecBtn.rect.width, 0.15).setOnComplete(System.Action(function()
				setActive(arg_10_0.ui, True)
				setActive(arg_10_0.stopRecBtn, False)
				arg_10_0.ysScreenRecorder.StopRecord(var_27_0)

				if PLATFORM == PLATFORM_ANDROID:
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("word_save_video"),
						def onNo:()
							arg_10_0.ysScreenRecorder.DiscardVideo(),
						def onYes:()
							local var_31_0 = arg_10_0.ysScreenRecorder.GetVideoFilePath()

							warning("源录像路径：" .. tostring(var_31_0))
							MediaSaver.SaveVideoWithPath(var_31_0)
					})

				arg_10_0.SetMute(False))))
	setActive(arg_10_0.stopRecBtn, False)
	onButton(arg_10_0, arg_10_0.switchCamBtn, function()
		arg_10_0.isFlipping = not arg_10_0.isFlipping

		arg_10_0.webcam.SwitchCam()
		arg_10_0.updateCameraCanvas())
	onButton(arg_10_0, arg_10_0.selectCharBtn, function()
		arg_10_0.emit(var_0_0.SELECT_CHAR_PANEL))

	function arg_10_0.webcam.takeCallback(arg_34_0)
		setActive(arg_10_0.ui, True)

	onButton(arg_10_0, arg_10_0.l2dStopBtnGo, function()
		arg_10_0.isPause = True

		arg_10_0.UpdateL2dPlayState())
	onButton(arg_10_0, arg_10_0.l2dPlayBtnGo, function()
		arg_10_0.isPause = False

		arg_10_0.UpdateL2dPlayState())
	onButton(arg_10_0, arg_10_0.l2dAnimationBtnGo, function()
		arg_10_0.setLive2dAnimsPanelState(True))
	onButton(arg_10_0, arg_10_0.l2dAnimationBackBtnTrans, function()
		arg_10_0.setLive2dAnimsPanelState(False))
	cameraPaintViewAdjust(True)
	arg_10_0.updateCameraCanvas()
	arg_10_0.updateShowType()

def var_0_0.changeToTakeVideo(arg_39_0):
	if arg_39_0.state == var_0_0.STATE_TAKE_VIDEO:
		return

	arg_39_0.state = var_0_0.STATE_TAKE_VIDEO

	LeanTween.moveY(rtf(arg_39_0.modePnlTF), -56, 0.1)
	SetActive(arg_39_0.videoTakeImg, True)

def var_0_0.willExit(arg_40_0):
	arg_40_0.SetDummyForIOS(False)
	cameraPaintViewAdjust(False)
	arg_40_0.clearSkin()

	local var_40_0 = PlayerPrefs.GetInt(SHOW_TOUCH_EFFECT, 1) > 0

	setActive(pg.UIMgr.GetInstance().OverlayEffect, var_40_0)

def var_0_0.clearSkin(arg_41_0):
	if arg_41_0.paintSkin and arg_41_0.showType == var_0_0.SHOW_PAINT:
		retPaintingPrefab(arg_41_0.paint, arg_41_0.paintSkin)

	if arg_41_0.spineSkin and arg_41_0.showType == var_0_0.SHOW_SPINE:
		PoolMgr.GetInstance().ReturnSpineChar(arg_41_0.spineSkin, go(arg_41_0.findTF("model", arg_41_0.spine)))

	if arg_41_0.live2dCom:
		arg_41_0.live2dCom.FinishAction = None
		arg_41_0.live2dCom.EventAction = None

	if arg_41_0.live2dCom and arg_41_0.showType == var_0_0.SHOW_LIVE2D:
		Destroy(arg_41_0.live2dCom.gameObject)

		arg_41_0.live2dCom = None

	pg.Live2DMgr.GetInstance().StopLoadingLive2d(arg_41_0.live2dRequestId)

	arg_41_0.live2dRequestId = None

def var_0_0.checkSkin(arg_42_0, arg_42_1):
	local var_42_0 = pg.ship_skin_template[arg_42_1]

	assert(arg_42_1 == -1 or var_42_0, "invalid skin id " .. arg_42_1)

	arg_42_0.skin = var_42_0

	local var_42_1 = False

	if arg_42_0.contextData.tbId:
		arg_42_0.paintSkin = pg.secretary_special_ship[arg_42_0.contextData.tbId].prefab or "tbniang"
		var_42_1 = True
		arg_42_0.contextData.tbId = None
	elif arg_42_0.paintSkin != var_42_0.painting or var_42_0.spineSkin != var_42_0.prefab:
		arg_42_0.clearSkin()

		arg_42_0.paintSkin = var_42_0.painting
		arg_42_0.spineSkin = var_42_0.prefab
		arg_42_0.l2dAnims = var_42_0.l2d_animations

		if arg_42_0.l2dAnims == "":
			arg_42_0.l2dAnims = {
				"idle"
			}

		var_42_1 = True

	return var_42_1

def var_0_0.setSkinAndLive2d(arg_43_0, arg_43_1, arg_43_2):
	local var_43_0 = arg_43_0.checkSkin(arg_43_1)

	if arg_43_0.showType != var_0_0.SHOW_LIVE2D and arg_43_2:
		arg_43_0.showType = var_0_0.SHOW_LIVE2D

		arg_43_0.updateShowType()

		var_43_0 = True

	if var_43_0:
		arg_43_0.updateSkin()

def var_0_0.setSkin(arg_44_0, arg_44_1):
	if arg_44_0.checkSkin(arg_44_1):
		arg_44_0.updateSkin()

def var_0_0.setLive2d(arg_45_0, arg_45_1):
	if arg_45_0.showType != var_0_0.SHOW_LIVE2D and arg_45_1:
		arg_45_0.clearSkin()

		arg_45_0.showType = var_0_0.SHOW_LIVE2D

		arg_45_0.updateShowType()
		arg_45_0.updateSkin()

def var_0_0.updateShowType(arg_46_0):
	setActive(arg_46_0.paintBtn, False)
	arg_46_0.setLive2dAnimsPanelState(False)
	setActive(arg_46_0.live2dBtn, False)
	setActive(arg_46_0.l2dCtrlPanl, False)
	setActive(arg_46_0.spineBtn, False)

	if arg_46_0.showType == var_0_0.SHOW_PAINT:
		setActive(arg_46_0.paintBtn, True)
	elif arg_46_0.showType == var_0_0.SHOW_LIVE2D:
		setActive(arg_46_0.live2dBtn, True)
		SetActive(arg_46_0.l2dCtrlPanl, True)
	elif arg_46_0.showType == var_0_0.SHOW_SPINE:
		setActive(arg_46_0.spineBtn, True)

local function var_0_1(arg_47_0)
	if arg_47_0 == var_0_0.SHOW_PAINT:
		return 0.5, 2
	elif arg_47_0 == var_0_0.SHOW_LIVE2D:
		return 0.5, 2
	elif arg_47_0 == var_0_0.SHOW_SPINE:
		return 0.5, 4

def var_0_0.updateSkin(arg_48_0):
	if arg_48_0.showType == var_0_0.SHOW_LIVE2D and (not ResourceMgr.Inst.AssetExist("live2d/" .. arg_48_0.paintSkin) or not checkABExist("live2d/" .. arg_48_0.paintSkin)):
		arg_48_0.showType = var_0_0.SHOW_PAINT

		arg_48_0.updateShowType()

	local var_48_0 = arg_48_0.paint.GetComponent(typeof(Zoom))
	local var_48_1 = 0
	local var_48_2 = 0
	local var_48_3, var_48_4 = var_0_1(arg_48_0.showType)

	var_48_0.minZoom, var_48_0.maxZoom = var_48_3, var_48_4

	if var_48_4 < arg_48_0.paint.localScale.x:
		arg_48_0.paint.localScale = Vector3(var_48_4, var_48_4, var_48_4)
	elif var_48_3 > arg_48_0.paint.localScale.x:
		arg_48_0.paint.localScale = Vector3(var_48_3, var_48_3, var_48_3)

	if arg_48_0.showType == var_0_0.SHOW_LIVE2D:
		pg.UIMgr.GetInstance().LoadingOn()

		arg_48_0.live2dRequestId = pg.Live2DMgr.GetInstance().GetLive2DModelAsync(arg_48_0.paintSkin, function(arg_49_0)
			UIUtil.SetLayerRecursively(arg_49_0, LayerMask.NameToLayer("UI"))

			local var_49_0 = arg_49_0.transform

			var_49_0.SetParent(arg_48_0.live2d, True)

			var_49_0.localScale = Vector3(52, 52, 52)
			var_49_0.localPosition = BuildVector3(arg_48_0.skin.live2d_offset)

			local var_49_1 = arg_49_0.GetComponent(typeof(Live2dChar))
			local var_49_2 = pg.AssistantInfo.action2Id.idle

			var_49_1.SetAction(var_49_2)

			function var_49_1.FinishAction(arg_50_0)
				if arg_48_0.selectedID and arg_48_0.selectedID != pg.AssistantInfo.action2Id.idle:
					arg_48_0.setL2dAction(arg_48_0.selectedID)

			arg_48_0.live2dCom = var_49_1
			arg_48_0.live2dCom.name = arg_48_0.paintSkin
			arg_48_0.playActionId = pg.AssistantInfo.action2Id.idle
			arg_48_0.selectedID = pg.AssistantInfo.action2Id.idle
			arg_48_0.live2dAnimator = arg_49_0.GetComponent(typeof(Animator))

			local var_49_3 = arg_48_0.live2dCom.GetCubismParameter("Paramring")

			if var_49_3:
				if arg_48_0.contextData and arg_48_0.contextData.propose:
					arg_48_0.live2dCom.AddParameterValue(var_49_3, 1, CubismParameterBlendMode.Override)
				else
					arg_48_0.live2dCom.AddParameterValue(var_49_3, 0, CubismParameterBlendMode.Override)

			arg_48_0.ResetL2dPanel()
			arg_48_0.setLive2dAnimsPanelState(True)
			SetActive(arg_48_0.spine, False)
			SetActive(arg_48_0.live2d, True)
			pg.UIMgr.GetInstance().LoadingOff()

			local var_49_4 = arg_48_0.skin.lip_sync_gain
			local var_49_5 = arg_48_0.skin.lip_smoothing

			if var_49_4 and var_49_4 != 0:
				arg_48_0.live2d.GetChild(0).GetComponent("CubismCriSrcMouthInput").Gain = var_49_4

			if var_49_5 and var_49_5 != 0:
				arg_48_0.live2d.GetChild(0).GetComponent("CubismCriSrcMouthInput").Smoothing = var_49_5)
	elif arg_48_0.showType == var_0_0.SHOW_PAINT:
		SetActive(arg_48_0.live2d, False)
		SetActive(arg_48_0.spine, False)
		setPaintingPrefabAsync(arg_48_0.paint, arg_48_0.paintSkin, "mainNormal")
	elif arg_48_0.showType == var_0_0.SHOW_SPINE:
		SetActive(arg_48_0.live2d, False)
		SetActive(arg_48_0.spine, True)
		PoolMgr.GetInstance().GetSpineChar(arg_48_0.spineSkin, True, function(arg_51_0)
			arg_51_0.name = "model"

			local var_51_0 = arg_51_0.transform

			var_51_0.SetParent(arg_48_0.spine, True)

			var_51_0.localScale = Vector3(0.5, 0.5, 0.5)
			var_51_0.localPosition = Vector3.zero

			arg_48_0.playAction("normal"))

def var_0_0.playAction(arg_52_0, arg_52_1):
	if arg_52_0.showType != var_0_0.SHOW_SPINE:
		return

	GetOrAddComponent(arg_52_0.findTF("model", arg_52_0.spine), typeof(SpineAnimUI)).SetAction(arg_52_1, 0)

def var_0_0.ResetL2dPanel(arg_53_0):
	arg_53_0.selectedID = pg.AssistantInfo.action2Id.idle
	arg_53_0.isPause = False

	arg_53_0.UpdateL2dPlayState(True)
	arg_53_0.updateSelectedItem()

def var_0_0.UpdateL2dPlayState(arg_54_0, arg_54_1):
	if arg_54_0.showType != var_0_0.SHOW_LIVE2D:
		return

	if arg_54_0.isPause:
		SetActive(arg_54_0.l2dStopBtnGo, False)
		SetActive(arg_54_0.l2dPlayBtnGo, True)
	else
		SetActive(arg_54_0.l2dStopBtnGo, True)
		SetActive(arg_54_0.l2dPlayBtnGo, False)

	if not arg_54_1:
		arg_54_0.L2dAnimationState()

def var_0_0.L2dAnimationState(arg_55_0):
	if arg_55_0.showType != var_0_0.SHOW_LIVE2D:
		return

	if arg_55_0.isPause:
		arg_55_0.live2dAnimator.speed = 0
	else
		arg_55_0.live2dAnimator.speed = 1

def var_0_0.updateLive2dAnimationPanel(arg_56_0):
	SetActive(arg_56_0.l2dAnimations, arg_56_0.isShowL2dAnims)
	SetActive(arg_56_0.l2dAnimationBtnGo, not arg_56_0.isShowL2dAnims)

	if arg_56_0.isShowL2dAnims and #arg_56_0.l2dAnims > 1:
		arg_56_0.animContainer.SetTotalCount(#arg_56_0.l2dAnims, 0)

def var_0_0.setLive2dAnimsPanelState(arg_57_0, arg_57_1):
	arg_57_0.isShowL2dAnims = arg_57_1

	arg_57_0.updateLive2dAnimationPanel()

local var_0_2 = 3

def var_0_0.onInitItem(arg_58_0, arg_58_1):
	local var_58_0 = SnapshotItem.New(arg_58_1, False)

	onButton(arg_58_0, var_58_0.go, function()
		if arg_58_0.l2dClickCD and Time.fixedTime - arg_58_0.l2dClickCD < var_0_2:
			return

		if arg_58_0.selectedID == var_58_0.GetID():
			return

		if var_58_0.GetID() == 6 or var_58_0.GetID() == 7:
			arg_58_0.l2dClickCD = Time.fixedTime

		arg_58_0.selectedID = var_58_0.GetID()

		arg_58_0.updateSelectedItem()
		arg_58_0.setL2dAction(arg_58_0.selectedID), SFX_CONFIRM)

	arg_58_0.scrollItems[arg_58_1] = var_58_0

def var_0_0.setL2dAction(arg_60_0, arg_60_1):
	if arg_60_1 != pg.AssistantInfo.action2Id.idle:
		-- block empty

	if arg_60_0.live2dCom and arg_60_1:
		if arg_60_1 == pg.AssistantInfo.action2Id.idle:
			arg_60_0.live2dCom.SetAction(arg_60_1)
		elif arg_60_0.playActionId == pg.AssistantInfo.action2Id.idle:
			arg_60_0.live2dCom.SetAction(arg_60_1)
		elif arg_60_0.playActionId == arg_60_1:
			arg_60_0.live2dCom.SetAction(arg_60_1)

		arg_60_0.playActionId = arg_60_1

def var_0_0.onUpdateItem(arg_61_0, arg_61_1, arg_61_2):
	arg_61_1 = arg_61_1 + 1

	local var_61_0 = arg_61_0.scrollItems[arg_61_2]

	if not var_61_0:
		arg_61_0.onInitItem(arg_61_2)

		var_61_0 = arg_61_0.scrollItems[arg_61_2]

	local var_61_1 = arg_61_0.l2dAnims[arg_61_1]
	local var_61_2 = pg.AssistantInfo.action2Id[var_61_1]
	local var_61_3 = {
		id = var_61_2,
		name = i18n(var_61_1)
	}

	var_61_0.Update(var_61_3)

	if arg_61_0.isVertical:
		var_61_0.SetEulerAngle(arg_61_0.verticalEulerAngle)
	else
		var_61_0.SetEulerAngle(arg_61_0.horizontalEulerAngle)

	if var_61_0.GetID() == arg_61_0.selectedID:
		var_61_0.UpdateSelected(True)
	else
		var_61_0.UpdateSelected(False)

def var_0_0.onReturnItem(arg_62_0, arg_62_1, arg_62_2):
	return

def var_0_0.updateSelectedItem(arg_63_0):
	for iter_63_0, iter_63_1 in pairs(arg_63_0.scrollItems):
		if iter_63_1.HasInfo():
			if iter_63_1.GetID() == arg_63_0.selectedID:
				iter_63_1.UpdateSelected(True)
			else
				iter_63_1.UpdateSelected(False)

def var_0_0.updateUIDirection(arg_64_0):
	if arg_64_0.isVertical:
		local var_64_0 = arg_64_0.verticalEulerAngle
		local var_64_1 = arg_64_0.rotateUseTime

		LeanTween.rotateZ(go(arg_64_0.backBtnImg), var_64_0, var_64_1)
		LeanTween.rotateZ(go(arg_64_0.selectCharBtnImg), var_64_0, var_64_1)
		LeanTween.rotateZ(go(arg_64_0.switchCamBtnImg), var_64_0, var_64_1)
		LeanTween.rotateZ(go(arg_64_0.l2dBtnImg), var_64_0, var_64_1)
		LeanTween.rotateZ(go(arg_64_0.l2dStopBtnImg), var_64_0, var_64_1)
		LeanTween.rotateZ(go(arg_64_0.l2dPlayBtnImg), var_64_0, var_64_1)
		LeanTween.rotateZ(go(arg_64_0.l2d2PaintBtnImg), var_64_0, var_64_1)
		SetActive(arg_64_0.takePhotoVerticalText, False)
		SetActive(arg_64_0.takePhotoHorizontalText, True)
		SetActive(arg_64_0.takeVideoVerticalText, False)
		SetActive(arg_64_0.takeVideoHorizontalText, True)
		LeanTween.rotateZ(go(arg_64_0.paint), var_64_0, var_64_1)
		arg_64_0.updateListItemRotate(var_64_0, var_64_1)
	else
		local var_64_2 = arg_64_0.horizontalEulerAngle
		local var_64_3 = arg_64_0.rotateUseTime

		LeanTween.rotateZ(go(arg_64_0.backBtnImg), var_64_2, var_64_3)
		LeanTween.rotateZ(go(arg_64_0.selectCharBtnImg), var_64_2, var_64_3)
		LeanTween.rotateZ(go(arg_64_0.switchCamBtnImg), var_64_2, var_64_3)
		LeanTween.rotateZ(go(arg_64_0.l2dBtnImg), var_64_2, var_64_3)
		LeanTween.rotateZ(go(arg_64_0.l2dStopBtnImg), var_64_2, var_64_3)
		LeanTween.rotateZ(go(arg_64_0.l2dPlayBtnImg), var_64_2, var_64_3)
		LeanTween.rotateZ(go(arg_64_0.l2d2PaintBtnImg), var_64_2, var_64_3)
		SetActive(arg_64_0.takePhotoVerticalText, True)
		SetActive(arg_64_0.takePhotoHorizontalText, False)
		SetActive(arg_64_0.takeVideoVerticalText, True)
		SetActive(arg_64_0.takeVideoHorizontalText, False)
		LeanTween.rotateZ(go(arg_64_0.paint), var_64_2, var_64_3)
		arg_64_0.updateListItemRotate(var_64_2, var_64_3)

def var_0_0.updateListItemRotate(arg_65_0, arg_65_1, arg_65_2):
	for iter_65_0, iter_65_1 in pairs(arg_65_0.scrollItems):
		iter_65_1.RotateUI(arg_65_1, arg_65_2)

def var_0_0.updateCameraCanvas(arg_66_0):
	local var_66_0 = CameraMgr.instance.AspectRatio
	local var_66_1 = UnityEngine.Screen.width
	local var_66_2 = UnityEngine.Screen.height
	local var_66_3 = 1
	local var_66_4 = var_66_1 / var_66_2

	if var_66_4 < var_66_0:
		var_66_3 = var_66_0 / var_66_4
	elif var_66_0 < var_66_4:
		var_66_3 = var_66_4 / var_66_0

	if arg_66_0.isFlipping:
		arg_66_0.snapshot.localScale = Vector3(-var_66_3, var_66_3, 1)
	else
		arg_66_0.snapshot.localScale = Vector3(var_66_3, var_66_3, 1)

def var_0_0.SetDummyForIOS(arg_67_0, arg_67_1):
	if PLATFORM != PLATFORM_IPHONEPLAYER:
		setActive(arg_67_0.dummy, False)

		return

	local var_67_0 = pg.UIMgr.GetInstance().GetMainCamera().GetComponent(typeof(Camera))

	if arg_67_1:
		var_67_0.nearClipPlane = 0

		arg_67_0.dummy.SetParent(pg.UIMgr.GetInstance().GetMainCamera().transform)

		arg_67_0.dummy.localPosition = Vector3(0, 0, 3)
		arg_67_0.dummy.localRotation = Vector3(0, 0, 0)
		arg_67_0.dummy.localScale = Vector3(1, 1, 1)

		setActive(arg_67_0.dummy, True)
	else
		var_67_0.nearClipPlane = -100

		arg_67_0.dummy.SetParent(arg_67_0._tf)

		arg_67_0.dummy.localPosition = Vector3(0, 0, 0)
		arg_67_0.dummy.localRotation = Vector3(0, 0, 0)
		arg_67_0.dummy.localScale = Vector3(1, 1, 1)

def var_0_0.SetMute(arg_68_0, arg_68_1):
	if arg_68_1:
		CriAtom.SetCategoryVolume("Category_CV", 0)
		CriAtom.SetCategoryVolume("Category_BGM", 0)
		CriAtom.SetCategoryVolume("Category_SE", 0)
	else
		CriAtom.SetCategoryVolume("Category_CV", pg.CriMgr.GetInstance().getCVVolume())
		CriAtom.SetCategoryVolume("Category_BGM", pg.CriMgr.GetInstance().getBGMVolume())
		CriAtom.SetCategoryVolume("Category_SE", pg.CriMgr.GetInstance().getSEVolume())

return var_0_0
