local var_0_0 = class("Dorm3dPhotoLayer", import("view.base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "Dorm3dPhotoUI"
end

var_0_0.PANEL = {
	CAMERA = 2,
	LIGHTING = 3,
	ACTION = 1
}

function var_0_0.init(arg_2_0)
	arg_2_0.topPanel = arg_2_0._tf:Find("Top")
	arg_2_0.leftPanel = arg_2_0._tf:Find("Left")
	arg_2_0.btnAction = arg_2_0._tf:Find("Left/Action")
	arg_2_0.btnCamera = arg_2_0._tf:Find("Left/Camera")
	arg_2_0.btnLighting = arg_2_0._tf:Find("Left/Lighting")
	arg_2_0.sliderZoom = arg_2_0._tf:Find("Left/Zoom/Slider")
	arg_2_0.panelAction = arg_2_0._tf:Find("Left/ActionSelect")

	setActive(arg_2_0.panelAction, false)
	setActive(arg_2_0.panelAction:Find("Mask"), false)

	arg_2_0.panelCamera = arg_2_0._tf:Find("Left/CameraSettings")

	setActive(arg_2_0.panelCamera, false)

	arg_2_0.panelLightning = arg_2_0._tf:Find("Left/LightningSettings")

	setActive(arg_2_0.panelLightning, false)

	arg_2_0.rightPanel = arg_2_0._tf:Find("Right")
	arg_2_0.scrollZones = arg_2_0._tf:Find("Right/List/Scroll")
	arg_2_0.listZones = arg_2_0.scrollZones:Find("Content")
	arg_2_0.btnHideUI = arg_2_0._tf:Find("Right/HideUI")
	arg_2_0.btnReset = arg_2_0._tf:Find("Right/Reset")
	arg_2_0.btnFreeze = arg_2_0._tf:Find("Right/Freeze")
	arg_2_0.btnAnimSpeed = arg_2_0._tf:Find("Right/AnimSpeed")
	arg_2_0.listAnimSpeed = arg_2_0.btnAnimSpeed:Find("Bar")

	setActive(arg_2_0.listAnimSpeed, false)

	arg_2_0.textAnimSpeed = arg_2_0.btnAnimSpeed:Find("Speed")
	arg_2_0.btnAR = arg_2_0._tf:Find("Right/AR")
	arg_2_0.mask = arg_2_0._tf:Find("Mask")

	setActive(arg_2_0.mask, false)

	arg_2_0.btnFilm = arg_2_0._tf:Find("RightTop/Film")
	arg_2_0.btnShoot = arg_2_0._tf:Find("RightTop/Shot")
	arg_2_0.ysScreenShoter = arg_2_0._tf:Find("Shoter"):GetComponent(typeof(YSTool.YSScreenShoter))
	arg_2_0.ysScreenRecorder = arg_2_0._tf:Find("Shoter"):GetComponent(typeof(YSTool.YSScreenRecorder))
end

function var_0_0.SetSceneRoot(arg_3_0, arg_3_1)
	arg_3_0.scene = arg_3_1
end

function var_0_0.SetApartment(arg_4_0, arg_4_1)
	arg_4_0.apartment = arg_4_1:clone()
end

function var_0_0.onBackPressed(arg_5_0)
	if arg_5_0.recordState then
		triggerButton(arg_5_0.btnFilm)

		return
	end

	arg_5_0:closeView()
end

function var_0_0.didEnter(arg_6_0)
	onButton(arg_6_0, arg_6_0._tf:Find("Top/Back"), function()
		arg_6_0:onBackPressed()
	end, SFX_CANCEL)
	setSlider(arg_6_0.sliderZoom, 0, 1, 0)
	onSlider(arg_6_0, arg_6_0.sliderZoom, function(arg_8_0)
		local var_8_0 = (1 - arg_8_0) * 0.5 + 0.5

		arg_6_0.scene:SetPinchValue(var_8_0)
	end)

	arg_6_0.hideUI = false

	onButton(arg_6_0, arg_6_0.btnHideUI, function()
		if arg_6_0.hideUI then
			return
		end

		setActive(arg_6_0.mask, true)
		setActive(arg_6_0.topPanel, false)
		setActive(arg_6_0.leftPanel, false)
		setActive(arg_6_0.rightPanel, false)

		arg_6_0.hideUI = true
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.mask, function()
		if not arg_6_0.hideUI then
			return
		end

		setActive(arg_6_0.topPanel, true)
		setActive(arg_6_0.leftPanel, true)
		setActive(arg_6_0.rightPanel, true)
		setActive(arg_6_0.mask, false)

		arg_6_0.hideUI = false
	end)
	onButton(arg_6_0, arg_6_0.btnReset, function()
		return
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.btnAR, function()
		return
	end, SFX_PANEL)

	arg_6_0.recordState = nil

	onButton(arg_6_0, arg_6_0.btnFilm, function()
		arg_6_0.recordState = not arg_6_0.recordState

		local function var_13_0(arg_14_0)
			setActive(arg_6_0.topPanel, arg_14_0)
			setActive(arg_6_0.leftPanel, arg_14_0)
			setActive(arg_6_0.rightPanel, arg_14_0)
		end

		if arg_6_0.recordState then
			var_13_0(false)

			local function var_13_1(arg_15_0)
				if arg_15_0 ~= -1 then
					var_13_0(true)

					arg_6_0.recordState = nil
				end
			end

			local function var_13_2(arg_16_0)
				warning("开始录屏结果：" .. arg_16_0)
			end

			seriesAsync({
				function(arg_17_0)
					arg_17_0()
				end,
				function(arg_18_0)
					var_0_0.SetMute(true)
					arg_6_0.ysScreenRecorder:BeforeStart()
					arg_6_0.ysScreenRecorder:StartRecord(var_13_2, var_13_1)

					if PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance():GetChannelUID() == "2" then
						print("start recording : play sound")
						NotificationMgr.Inst:PlayStartRecordSound()
					end
				end
			})
		else
			local function var_13_3(arg_19_0)
				warning("结束录屏结果：" .. arg_19_0)
			end

			seriesAsync({
				function(arg_20_0)
					var_13_0(true)
					arg_6_0.ysScreenRecorder:StopRecord(var_13_3)

					if PLATFORM == PLATFORM_ANDROID then
						pg.MsgboxMgr.GetInstance():ShowMsgBox({
							content = i18n("word_save_video"),
							onNo = function()
								arg_6_0.ysScreenRecorder:DiscardVideo()
							end,
							onYes = function()
								local var_22_0 = arg_6_0.ysScreenRecorder:GetVideoFilePath()

								MediaSaver.SaveVideoWithPath(var_22_0)
							end
						})
					end

					var_0_0.SetMute(false)
				end
			})
		end
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.btnShoot, function()
		local function var_23_0(arg_24_0)
			setActive(arg_6_0.topPanel, arg_24_0)
			setActive(arg_6_0.leftPanel, arg_24_0)
			setActive(arg_6_0.rightPanel, arg_24_0)
			setActive(arg_6_0._tf:Find("RightTop"), arg_24_0)

			if PlayerPrefs.GetInt(SHOW_TOUCH_EFFECT, 1) > 0 then
				setActive(pg.UIMgr.GetInstance().OverlayEffect, arg_24_0)
			end
		end

		var_23_0(false)

		local function var_23_1(arg_25_0)
			warning("截图结果：" .. tostring(arg_25_0))
			var_23_0(true)
		end

		local function var_23_2(arg_26_0)
			local var_26_0 = UnityEngine.Texture2D.New(Screen.width, Screen.height)

			Tex2DExtension.LoadImage(var_26_0, arg_26_0)
			arg_6_0:emit(SnapshotScene.SHARE_PANEL, var_26_0, arg_26_0)

			if PLATFORM_CODE == PLATFORM_JP and pg.SdkMgr.GetInstance():GetChannelUID() == "2" then
				print("start photo : play sound")
				NotificationMgr.Inst:PlayShutterSound()
			end
		end

		arg_6_0.ysScreenShoter:TakeScreenShotData(var_23_1, var_23_2)
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.btnAnimSpeed, function()
		setActive(arg_6_0.listAnimSpeed, not isActive(arg_6_0.listAnimSpeed))
	end, SFX_PANEL)

	arg_6_0.activePanel = nil

	local var_6_0 = {
		{
			btn = arg_6_0.btnAction,
			panel = arg_6_0.panelAction,
			On = function()
				arg_6_0:UpdateActionPanel()
				setActive(arg_6_0.panelAction, true)
			end,
			Off = function()
				setActive(arg_6_0.panelAction, false)
			end
		},
		{
			btn = arg_6_0.btnCamera,
			panel = arg_6_0.panelCamera,
			On = function()
				arg_6_0:UpdateCameraPanel()
				setActive(arg_6_0.panelCamera, true)
			end,
			Off = function()
				setActive(arg_6_0.panelCamera, false)
			end
		},
		{
			btn = arg_6_0.btnLighting,
			panel = arg_6_0.panelLightning,
			On = function()
				arg_6_0:UpdateLightingPanel()
				setActive(arg_6_0.panelLightning, true)
			end,
			Off = function()
				setActive(arg_6_0.panelLightning, false)
			end
		}
	}

	table.Ipairs(var_6_0, function(arg_34_0, arg_34_1)
		onButton(arg_6_0, arg_34_1.btn, function()
			if arg_34_0 == arg_6_0.activePanel then
				arg_6_0.activePanel = nil

				arg_34_1.Off()
			else
				table.Ipairs(var_6_0, function(arg_36_0, arg_36_1)
					if arg_36_0 == arg_34_0 then
						return
					end

					arg_36_1.Off()
				end)

				arg_6_0.activePanel = arg_34_0

				arg_34_1.On()
			end
		end, SFX_PANEL)
	end)

	arg_6_0.zoneIndex = 1

	arg_6_0:InitData()
	arg_6_0:FirstEnterZone()

	local var_6_1 = arg_6_0.apartment:GetCameraZones()

	UIItemList.StaticAlign(arg_6_0.listZones, arg_6_0.listZones:GetChild(0), #var_6_1, function(arg_37_0, arg_37_1, arg_37_2)
		if arg_37_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_37_1 = arg_37_1 + 1

		local var_37_0 = var_6_1[arg_37_1]

		setText(arg_37_2:Find("Name"), var_37_0:GetName())
		onButton(arg_6_0, arg_37_2, function()
			if arg_6_0.zoneIndex == arg_37_1 then
				return
			end

			local var_38_0 = arg_6_0.zoneIndex

			setActive(arg_37_2:Find("Selected"), true)
			setActive(arg_6_0.listZones:GetChild(var_38_0 - 1):Find("Selected"), false)

			arg_6_0.zoneIndex = arg_37_1

			arg_6_0:RefreshData()
			arg_6_0:SwitchZone()
		end, SFX_PANEL)
	end)
	setActive(arg_6_0.listZones:GetChild(arg_6_0.zoneIndex - 1):Find("Selected"), true)
end

function var_0_0.InitData(arg_39_0)
	arg_39_0.cameraSettings = Clone(arg_39_0.scene:GetCameraSettings())
	arg_39_0.settingHideCharacter = false
	arg_39_0.settingFaceCamera = true
	arg_39_0.settingLightingColorIndex = nil
	arg_39_0.settingLightingStrength = 1
	arg_39_0.settingLightingAlpha = 1
	arg_39_0.settingFilterIndex = nil
	arg_39_0.settingFilterStrength = 1

	arg_39_0:RefreshData()
end

function var_0_0.RefreshData(arg_40_0)
	local var_40_0 = arg_40_0.apartment:GetCameraZones()[arg_40_0.zoneIndex]

	arg_40_0.animID = var_40_0:GetRegularAnims()[1]:GetConfigID()

	local function var_40_1(arg_41_0, arg_41_1)
		arg_41_0.min = arg_41_1[1]
		arg_41_0.max = arg_41_1[2]
		arg_41_0.value = math.clamp(arg_41_0.value, arg_41_1[1], arg_41_1[2])
	end

	var_40_1(arg_40_0.cameraSettings.depthOfField.focusDistance, var_40_0:GetFocusDistanceRange())
	var_40_1(arg_40_0.cameraSettings.depthOfField.blurRadius, var_40_0:GetDepthOfFieldBlurRange())
	var_40_1(arg_40_0.cameraSettings.postExposure, var_40_0:GetExposureRange())
	var_40_1(arg_40_0.cameraSettings.contrast, var_40_0:GetContrastRange())
	var_40_1(arg_40_0.cameraSettings.saturate, var_40_0:GetSaturationRange())

	arg_40_0.animSpeeds = var_40_0:GetAnimSpeeds()
	arg_40_0.animSpeed = 1
end

function var_0_0.FirstEnterZone(arg_42_0)
	local var_42_0 = arg_42_0.apartment:GetCameraZones()[arg_42_0.zoneIndex]

	arg_42_0.scene:EnterPhotoMode(var_42_0)
	arg_42_0:UpdateActionPanel()
	arg_42_0:UpdateCameraPanel()
	arg_42_0:UpdateLightingPanel()
	arg_42_0:UpdateAnimSpeedPanel()
end

function var_0_0.SwitchZone(arg_43_0)
	local var_43_0 = arg_43_0.apartment:GetCameraZones()[arg_43_0.zoneIndex]

	arg_43_0.scene:SwitchCameraZone(var_43_0)
	arg_43_0:UpdateActionPanel()
	arg_43_0:UpdateCameraPanel()
	arg_43_0:UpdateLightingPanel()
	arg_43_0:UpdateAnimSpeedPanel()
end

local var_0_1 = 0.2

function var_0_0.UpdateActionPanel(arg_44_0)
	if arg_44_0.activePanel ~= var_0_0.PANEL.ACTION then
		return
	end

	local var_44_0 = arg_44_0.apartment:GetCameraZones()[arg_44_0.zoneIndex]
	local var_44_1 = var_44_0:GetRegularAnims()

	arg_44_0.lastSelectedAnimBG = nil

	local function var_44_2(arg_45_0, arg_45_1)
		local var_45_0 = arg_45_0:GetConfigID()

		if arg_44_0.animID == var_45_0 then
			return
		end

		if arg_44_0.lastSelectedAnimBG then
			setActive(arg_44_0.lastSelectedAnimBG, false)
		end

		local var_45_1 = arg_44_0:GetAnimPlayList(var_45_0)
		local var_45_2 = Dorm3dCameraAnim.New({
			configId = arg_44_0.animID
		}):GetFinishAnimID()

		arg_44_0.animID = var_45_0
		arg_44_0.lastSelectedAnimBG = arg_45_1:Find("Selected")

		arg_44_0:BlockActionPanel(true)

		local var_45_3 = (table.indexof(var_45_1, _.detect(var_45_1, function(arg_46_0)
			return arg_46_0:GetConfigID() == var_45_2
		end)) or 0) + 1
		local var_45_4 = _.rest(var_45_1, var_45_3)
		local var_45_5 = arg_45_1:Find("Fill"):GetComponent(typeof(Image))

		setActive(arg_45_1:Find("Fill"), true)

		local function var_45_6()
			setActive(arg_45_1:Find("Selected"), true)
			setActive(arg_45_1:Find("Fill"), false)
			arg_44_0:BlockActionPanel(false)

			arg_44_0.animPlaying = nil
		end

		if #var_45_4 == 0 then
			var_45_6()

			return
		end

		local var_45_7 = _.reduce(var_45_4, 0, function(arg_48_0, arg_48_1)
			return arg_48_0 + math.max(var_0_1, arg_48_1:GetAnimTime())
		end)

		arg_44_0.animInfo = {
			index = 1,
			passedTime = 0,
			ratio = 0,
			animPlayList = var_45_4,
			totalTime = var_45_7,
			imgFill = var_45_5,
			startStamp = Time.time
		}
		arg_44_0.timerAnim = FrameTimer.New(function()
			local var_49_0 = arg_44_0.animInfo
			local var_49_1 = var_49_0.animPlayList[var_49_0.index]
			local var_49_2 = math.max(var_0_1, var_49_1:GetAnimTime())
			local var_49_3 = var_49_0.startStamp
			local var_49_4 = Time.time
			local var_49_5 = math.min(1, var_49_0.ratio + (var_49_4 - var_49_3) * arg_44_0.animSpeed / var_49_2)
			local var_49_6 = var_49_0.passedTime + var_49_2 * var_49_5

			var_45_5.fillAmount = var_49_6 / var_45_7

			if var_49_5 < 1 then
				return
			end

			var_49_0.index = var_49_0.index + 1
			var_49_0.ratio = 0
			var_49_0.passedTime = var_49_0.passedTime + var_49_2
			var_49_0.startStamp = var_49_4

			warning(var_49_0.startStamp)

			if var_49_0.index > #var_49_0.animPlayList then
				var_45_6()
				arg_44_0.timerAnim:Stop()

				arg_44_0.timerAnim = nil
				arg_44_0.animInfo = nil

				return
			end

			local var_49_7 = var_49_0.animPlayList[var_49_0.index]

			arg_44_0.scene:PlaySingleAction(var_49_7:GetStateName())
		end, 1, -1)

		local var_45_8 = arg_44_0.animInfo.animPlayList[1]

		if var_45_3 == 1 then
			arg_44_0.scene:SwitchAnim(var_45_8:GetStateName())
			onNextTick(function()
				arg_44_0.scene:ResetCharPosByZone(var_44_0)
			end)
		else
			arg_44_0.scene:PlaySingleAction(var_45_8:GetStateName())
		end

		arg_44_0.timerAnim:Start()
	end

	local var_44_3 = arg_44_0.panelAction:Find("Regular/List")

	UIItemList.StaticAlign(var_44_3, var_44_3:GetChild(0), #var_44_1, function(arg_51_0, arg_51_1, arg_51_2)
		if arg_51_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_51_1 = arg_51_1 + 1

		local var_51_0 = var_44_1[arg_51_1]

		setText(arg_51_2:Find("Name"), var_51_0:GetName())
		setActive(arg_51_2:Find("Fill"), false)
		setActive(arg_51_2:Find("Selected"), false)
		onButton(arg_44_0, arg_51_2, function()
			var_44_2(var_51_0, arg_51_2)
		end)
	end)

	local var_44_4, var_44_5 = table.Find(var_44_1, function(arg_53_0, arg_53_1)
		return arg_53_1:GetConfigID() == arg_44_0.animID
	end)

	arg_44_0.lastSelectedAnimBG = var_44_3:GetChild(var_44_5 - 1):Find("Selected")

	setActive(arg_44_0.lastSelectedAnimBG, true)

	local var_44_6 = var_44_0:GetSpecialAnims()
	local var_44_7 = arg_44_0.panelAction:Find("Special/Furnitures")

	arg_44_0.lastFurniture = nil
	arg_44_0.lastSelectedFurnitureBG = nil

	local var_44_8 = arg_44_0.panelAction:Find("Special/List")

	setActive(var_44_8, false)

	local var_44_9 = arg_44_0.panelAction:Find("Special/Arrow")

	setActive(var_44_9, false)

	local function var_44_10(arg_54_0, arg_54_1)
		if arg_44_0.lastSelectedFurnitureBG then
			setActive(arg_44_0.lastSelectedFurnitureBG, false)
		end

		arg_44_0.lastFurniture = arg_54_0
		arg_44_0.lastSelectedFurnitureBG = arg_54_1:Find("Selected")

		setActive(arg_44_0.lastSelectedFurnitureBG, true)
		setActive(var_44_8, true)
		setActive(var_44_9, true)

		var_44_9.position = arg_54_1.position
		var_44_9.anchoredPosition = var_44_9.anchoredPosition + Vector2(0, -60)

		local var_54_0 = arg_54_0.anims

		UIItemList.StaticAlign(var_44_8, var_44_8:GetChild(0), #var_54_0, function(arg_55_0, arg_55_1, arg_55_2)
			if arg_55_0 ~= UIItemList.EventUpdate then
				return
			end

			arg_55_1 = arg_55_1 + 1

			local var_55_0 = var_54_0[arg_55_1]

			setText(arg_55_2:Find("Name"), var_55_0:GetName())
			setActive(arg_55_2:Find("Fill"), false)
			setActive(arg_55_2:Find("Selected"), false)

			if var_55_0:GetConfigID() == arg_44_0.animID then
				arg_44_0.lastSelectedAnimBG = arg_55_2:Find("Selected")

				setActive(arg_44_0.lastSelectedAnimBG, true)
			end

			onButton(arg_44_0, arg_55_2, function()
				arg_44_0.apartment:ReplaceFurniture(arg_54_0.slotId, arg_54_0.furnitureId)
				arg_44_0.scene:RefreshSlots(arg_44_0.apartment)
				var_44_2(var_55_0, arg_55_2)
			end)
		end)
	end

	setActive(arg_44_0.panelAction:Find("Special"), #var_44_6 > 0)
	UIItemList.StaticAlign(var_44_7, var_44_7:GetChild(0), #var_44_6, function(arg_57_0, arg_57_1, arg_57_2)
		arg_57_1 = arg_57_1 + 1

		local var_57_0 = var_44_6[arg_57_1]
		local var_57_1 = Dorm3dFurniture.New({
			configId = var_57_0.furnitureId
		})
		local var_57_2 = tobool(_.detect(arg_44_0.apartment:GetFurnitures(), function(arg_58_0)
			return arg_58_0:GetConfigID() == var_57_0.furnitureId
		end))

		updateDrop(arg_57_2:Find("Icon"), {
			type = DROP_TYPE_DORM3D_FURNITURE,
			id = var_57_1:GetConfigID()
		})
		setText(arg_57_2:Find("Name"), var_57_1:GetName())
		setActive(arg_57_2:Find("Lock"), not var_57_2)
		onButton(arg_44_0, arg_57_2, function()
			if not var_57_2 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("furniture not unlock"))

				return
			end

			var_44_10(var_57_0, arg_57_2)
		end)
	end)
end

function var_0_0.BlockActionPanel(arg_60_0, arg_60_1)
	setActive(arg_60_0.panelAction:Find("Mask"), arg_60_1)
end

function var_0_0.GetAnimPlayList(arg_61_0, arg_61_1)
	local var_61_0 = arg_61_1
	local var_61_1 = {}

	while true do
		local var_61_2 = Dorm3dCameraAnim.New({
			configId = var_61_0
		})

		if not var_61_2 then
			return var_61_1
		end

		table.insert(var_61_1, 1, var_61_2)

		var_61_0 = var_61_2:GetPreAnimID()

		if var_61_0 == 0 then
			return var_61_1
		end
	end
end

function var_0_0.UpdateCameraPanel(arg_62_0)
	if arg_62_0.activePanel ~= var_0_0.PANEL.CAMERA then
		return
	end

	local var_62_0 = arg_62_0.apartment:GetCameraZones()[arg_62_0.zoneIndex]

	;(function()
		local var_63_0 = arg_62_0.panelCamera:Find("DepthOfField/Toggle")

		triggerToggleWithoutNotify(var_63_0, arg_62_0.cameraSettings.depthOfField.enabled)
		onToggle(arg_62_0, var_63_0, function(arg_64_0)
			arg_62_0.cameraSettings.depthOfField.enabled = arg_64_0

			arg_62_0:RefreshCamera()
		end, SFX_UI_TAG, SFX_UI_CANCEL)
	end)()
	;(function()
		local var_65_0 = arg_62_0.cameraSettings.depthOfField.focusDistance
		local var_65_1 = arg_62_0.panelCamera:Find("DepthOfField/List/FocusDistance/Slider")

		setSlider(var_65_1, var_65_0.min, var_65_0.max, var_65_0.value)
		onSlider(arg_62_0, var_65_1, function(arg_66_0)
			var_65_0.value = arg_66_0

			arg_62_0:RefreshCamera()
		end)
	end)()
	;(function()
		local var_67_0 = arg_62_0.cameraSettings.depthOfField.blurRadius
		local var_67_1 = arg_62_0.panelCamera:Find("DepthOfField/List/BlurRadius/Slider")

		setSlider(var_67_1, var_67_0.min, var_67_0.max, var_67_0.value)
		onSlider(arg_62_0, var_67_1, function(arg_68_0)
			var_67_0.value = arg_68_0

			arg_62_0:RefreshCamera()
		end)
	end)()
	;(function()
		local var_69_0 = arg_62_0.cameraSettings.postExposure
		local var_69_1 = arg_62_0.panelCamera:Find("PostExposure/Slider")

		setSlider(var_69_1, var_69_0.min, var_69_0.max, var_69_0.value)
		onSlider(arg_62_0, var_69_1, function(arg_70_0)
			var_69_0.value = arg_70_0

			arg_62_0:RefreshCamera()
		end)
	end)()
	;(function()
		local var_71_0 = arg_62_0.cameraSettings.contrast
		local var_71_1 = arg_62_0.panelCamera:Find("Contrast/Slider")

		setSlider(var_71_1, var_71_0.min, var_71_0.max, var_71_0.value)
		onSlider(arg_62_0, var_71_1, function(arg_72_0)
			var_71_0.value = arg_72_0

			arg_62_0:RefreshCamera()
		end)
	end)()
	;(function()
		local var_73_0 = arg_62_0.cameraSettings.saturate
		local var_73_1 = arg_62_0.panelCamera:Find("Saturation/Slider")

		setSlider(var_73_1, var_73_0.min, var_73_0.max, var_73_0.value)
		onSlider(arg_62_0, var_73_1, function(arg_74_0)
			var_73_0.value = arg_74_0

			arg_62_0:RefreshCamera()
		end)
	end)()
	;(function()
		local var_75_0 = arg_62_0.panelCamera:Find("FaceCamera/Toggle")

		triggerToggleWithoutNotify(var_75_0, arg_62_0.settingFaceCamera)
		setActive(var_75_0:Find("Selected"), arg_62_0.settingFaceCamera)
		onToggle(arg_62_0, var_75_0, function(arg_76_0)
			arg_62_0.settingFaceCamera = arg_76_0

			arg_62_0.scene:EnableHeadIK(arg_76_0)
		end, SFX_UI_TAG, SFX_UI_CANCEL)
	end)()
	;(function()
		local var_77_0 = arg_62_0.panelCamera:Find("HideCharacter/Toggle")

		triggerToggleWithoutNotify(var_77_0, arg_62_0.settingHideCharacter)
		setActive(var_77_0:Find("Selected"), arg_62_0.settingHideCharacter)
		onToggle(arg_62_0, var_77_0, function(arg_78_0)
			arg_62_0.settingHideCharacter = arg_78_0

			if arg_78_0 then
				arg_62_0.scene:SwitchLadyInterestInPhotoMode(false)
				arg_62_0.scene:HideCharacter()
			else
				arg_62_0.scene:SwitchLadyInterestInPhotoMode(true)
				arg_62_0.scene:RevertCharacter()
			end
		end, SFX_UI_TAG, SFX_UI_CANCEL)
	end)()
end

function var_0_0.RefreshCamera(arg_79_0)
	arg_79_0.scene:SettingCamera(arg_79_0.cameraSettings)
end

function var_0_0.UpdateAnimSpeedPanel(arg_80_0)
	local function var_80_0()
		if not arg_80_0.timerAnim then
			return
		end

		local var_81_0 = arg_80_0.animInfo
		local var_81_1 = var_81_0.animPlayList[var_81_0.index]
		local var_81_2 = math.max(var_0_1, var_81_1:GetAnimTime())
		local var_81_3 = var_81_0.startStamp
		local var_81_4 = Time.time

		var_81_0.ratio = math.min(1, var_81_0.ratio + (var_81_4 - var_81_3) * arg_80_0.animSpeed / var_81_2)
		var_81_0.startStamp = var_81_4
	end

	local var_80_1 = arg_80_0.animSpeeds

	UIItemList.StaticAlign(arg_80_0.listAnimSpeed, arg_80_0.listAnimSpeed:GetChild(0), #var_80_1, function(arg_82_0, arg_82_1, arg_82_2)
		if arg_82_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_82_1 = arg_82_1 + 1

		local var_82_0 = var_80_1[arg_82_1]

		setText(arg_82_2:Find("Text"), var_82_0)
		onButton(arg_80_0, arg_82_2, function()
			if arg_80_0.animSpeed == var_82_0 then
				return
			end

			if arg_80_0.animPlaying then
				return
			end

			var_80_0()

			arg_80_0.animSpeed = var_82_0

			arg_80_0.scene:SetCharacterAnimSpeed(var_82_0)
			arg_80_0:UpdateAnimSpeedPanel()
		end, SFX_PANEL)
	end)
	onButton(arg_80_0, arg_80_0.btnFreeze, function()
		if arg_80_0.animPlaying then
			return
		end

		local var_84_0 = 0

		if arg_80_0.animSpeed ~= 0 then
			arg_80_0.lastAnimSpeed = arg_80_0.animSpeed
		else
			var_84_0 = arg_80_0.lastAnimSpeed or 1
			arg_80_0.lastAnimSpeed = nil
		end

		var_80_0()

		arg_80_0.animSpeed = var_84_0

		arg_80_0.scene:SetCharacterAnimSpeed(var_84_0)
		arg_80_0:UpdateAnimSpeedPanel()
	end, SFX_PANEL)
	UIItemList.StaticAlign(arg_80_0.listAnimSpeed, arg_80_0.listAnimSpeed:GetChild(0), #var_80_1, function(arg_85_0, arg_85_1, arg_85_2)
		if arg_85_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_85_1 = arg_85_1 + 1

		local var_85_0 = var_80_1[arg_85_1]

		setActive(arg_85_2:Find("Selected"), arg_80_0.animSpeed == var_85_0)
	end)
	setActive(arg_80_0.btnFreeze:Find("Selected"), arg_80_0.animSpeed == 0)
	setText(arg_80_0.textAnimSpeed, "X" .. arg_80_0.animSpeed)
end

function var_0_0.UpdateLightingPanel(arg_86_0)
	if arg_86_0.activePanel ~= var_0_0.PANEL.LIGHTING then
		return
	end

	local var_86_0 = arg_86_0.apartment:GetCameraZones()[arg_86_0.zoneIndex]
	local var_86_1 = {
		{
			color = "FF0000",
			name = "红"
		},
		{
			color = "FFFF00",
			name = "黄"
		},
		{
			color = "0000FF",
			name = "蓝"
		},
		{
			color = "00FF00",
			name = "绿"
		},
		{
			color = "FF00FF",
			name = "紫"
		},
		{
			color = "FFFFFF",
			name = "白"
		}
	}

	local function var_86_2()
		if not arg_86_0.settingLightingColorIndex then
			arg_86_0.scene:RevertCharacterLight()

			return
		end

		local var_87_0 = var_86_1[arg_86_0.settingLightingColorIndex]

		arg_86_0.scene:SetCharacterLight(Color.NewHex(var_87_0.color), arg_86_0.settingLightingAlpha, arg_86_0.settingLightingStrength)
	end

	arg_86_0.lastSelectedColorBG = nil

	UIItemList.StaticAlign(arg_86_0.panelLightning:Find("Lighting/List"), arg_86_0.panelLightning:Find("Lighting/List"):GetChild(0), #var_86_1, function(arg_88_0, arg_88_1, arg_88_2)
		if arg_88_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_88_1 = arg_88_1 + 1

		local var_88_0 = var_86_1[arg_88_1]

		setText(arg_88_2:Find("Name"), var_88_0.name)

		if arg_86_0.settingLightingColorIndex == arg_88_1 then
			arg_86_0.lastSelectedColorBG = arg_88_2:Find("Selected")

			setActive(arg_86_0.lastSelectedColorBG, true)
		end

		onButton(arg_86_0, arg_88_2, function()
			if arg_86_0.settingLightingColorIndex ~= arg_88_1 then
				arg_86_0.settingLightingColorIndex = arg_88_1
			else
				arg_86_0.settingLightingColorIndex = nil
			end

			var_86_2()

			if arg_86_0.lastSelectedColorBG then
				setActive(arg_86_0.lastSelectedColorBG, false)
			end

			if arg_86_0.settingLightingColorIndex == arg_88_1 then
				arg_86_0.lastSelectedColorBG = arg_88_2:Find("Selected")

				setActive(arg_86_0.lastSelectedColorBG, true)
			end
		end, SFX_PANEL)
	end)
	;(function()
		local var_90_0 = arg_86_0.panelLightning:Find("Lighting/Sliders/Strength/Slider")

		setSlider(var_90_0, 0, 1, arg_86_0.settingLightingStrength)
		onSlider(arg_86_0, var_90_0, function(arg_91_0)
			arg_86_0.settingLightingStrength = arg_91_0

			var_86_2()
		end)
	end)()
	;(function()
		local var_92_0 = arg_86_0.panelLightning:Find("Lighting/Sliders/Alpha/Slider")

		setSlider(var_92_0, 0, 1, arg_86_0.settingLightingAlpha)
		onSlider(arg_86_0, var_92_0, function(arg_93_0)
			arg_86_0.settingLightingAlpha = arg_93_0

			var_86_2()
		end)
	end)()

	local var_86_3 = {
		{
			name = "泛紫",
			profile = "volume_purple"
		}
	}

	local function var_86_4()
		if not arg_86_0.settingFilterIndex then
			arg_86_0.scene:RevertVolumeProfile()

			return
		end

		local var_94_0 = var_86_3[arg_86_0.settingFilterIndex]

		arg_86_0.scene:SetVolumeProfile(var_94_0.profile, arg_86_0.settingFilterStrength)
	end

	arg_86_0.lastSelectedFilterBG = nil

	UIItemList.StaticAlign(arg_86_0.panelLightning:Find("Filter/List"), arg_86_0.panelLightning:Find("Filter/List"):GetChild(0), #var_86_3, function(arg_95_0, arg_95_1, arg_95_2)
		if arg_95_0 ~= UIItemList.EventUpdate then
			return
		end

		arg_95_1 = arg_95_1 + 1

		local var_95_0 = var_86_3[arg_95_1]

		setText(arg_95_2:Find("Name"), var_95_0.name)

		if arg_86_0.settingFilterIndex == arg_95_1 then
			arg_86_0.lastSelectedFilterBG = arg_95_2:Find("Selected")

			setActive(arg_86_0.lastSelectedFilterBG, true)
		end

		onButton(arg_86_0, arg_95_2, function()
			if arg_86_0.settingFilterIndex ~= arg_95_1 then
				arg_86_0.settingFilterIndex = arg_95_1
			else
				arg_86_0.settingFilterIndex = nil
			end

			var_86_4()

			if arg_86_0.lastSelectedFilterBG then
				setActive(arg_86_0.lastSelectedFilterBG, false)
			end

			if arg_86_0.settingFilterIndex == arg_95_1 then
				arg_86_0.lastSelectedFilterBG = arg_95_2:Find("Selected")

				setActive(arg_86_0.lastSelectedFilterBG, true)
			end
		end, SFX_PANEL)
	end)
	;(function()
		local var_97_0 = arg_86_0.panelLightning:Find("Filter/Sliders/Strength/Slider")

		setSlider(var_97_0, 0, 1, arg_86_0.settingFilterStrength)
		onSlider(arg_86_0, var_97_0, function(arg_98_0)
			arg_86_0.settingFilterStrength = arg_98_0

			var_86_4()
		end)
	end)()
end

function var_0_0.SetMute(arg_99_0)
	if arg_99_0 then
		CriAtom.SetCategoryVolume("Category_CV", 0)
		CriAtom.SetCategoryVolume("Category_BGM", 0)
		CriAtom.SetCategoryVolume("Category_SE", 0)
	else
		CriAtom.SetCategoryVolume("Category_CV", pg.CriMgr.GetInstance():getCVVolume())
		CriAtom.SetCategoryVolume("Category_BGM", pg.CriMgr.GetInstance():getBGMVolume())
		CriAtom.SetCategoryVolume("Category_SE", pg.CriMgr.GetInstance():getSEVolume())
	end
end

function var_0_0.willExit(arg_100_0)
	if arg_100_0.animSpeed ~= 1 then
		arg_100_0.scene:SetCharacterAnimSpeed(1)
	end

	if arg_100_0.settingHideCharacter then
		arg_100_0.scene:SwitchLadyInterestInPhotoMode(true)
		arg_100_0.scene:RevertCharacter()
	end

	if not arg_100_0.settingFaceCamera then
		arg_100_0.scene:EnableHeadIK(true)
	end

	arg_100_0.scene:RevertCharacterLight()
	arg_100_0.scene:RevertVolumeProfile()
	arg_100_0.scene:RevertCameraSettings()
	arg_100_0.scene:ExitPhotoMode()
end

return var_0_0
