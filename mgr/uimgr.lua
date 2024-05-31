pg = pg or {}

local var_0_0 = singletonClass("UIMgr")

pg.UIMgr = var_0_0

local var_0_1 = pg

var_0_0._loadPanel = nil
var_0_0.CameraUI = 1
var_0_0.CameraLevel = 2
var_0_0.CameraOverlay = 3
var_0_0.OptimizedBlur = 1
var_0_0.StaticBlur = 2
var_0_0.PartialBlur = 3

function var_0_0.Init(arg_1_0, arg_1_1)
	print("initializing ui manager...")

	arg_1_0.mainCamera = GameObject.Find("MainCamera")
	arg_1_0.mainCameraComp = arg_1_0.mainCamera:GetComponent("Camera")
	arg_1_0.uiCamera = tf(GameObject.Find("UICamera"))
	arg_1_0.uiCameraComp = arg_1_0.uiCamera:GetComponent("Camera")
	arg_1_0.uiCameraComp.allowMSAA = false
	arg_1_0.levelCamera = tf(GameObject.Find("LevelCamera"))
	arg_1_0.levelCameraComp = arg_1_0.levelCamera:GetComponent("Camera")
	arg_1_0.levelCameraComp.allowMSAA = false
	arg_1_0.overlayCamera = tf(GameObject.Find("OverlayCamera"))
	arg_1_0.overlayCameraComp = arg_1_0.overlayCamera:GetComponent("Camera")
	arg_1_0.overlayCameraComp.allowMSAA = false
	arg_1_0.UIMain = arg_1_0.uiCamera:Find("Canvas/UIMain")
	arg_1_0.LevelMain = arg_1_0.levelCamera:Find("Canvas/UIMain")
	arg_1_0.OverlayMain = arg_1_0.overlayCamera:Find("Overlay/UIMain")
	arg_1_0.OverlayToast = arg_1_0.overlayCamera:Find("Overlay/UIOverlay")
	arg_1_0.OverlayEffect = arg_1_0.overlayCamera:Find("Overlay/UIEffect")
	arg_1_0._normalUIMain = nil
	arg_1_0._cameraBlurPartial = arg_1_0.uiCamera:GetComponent("UIPartialBlur")
	arg_1_0._levelCameraPartial = arg_1_0.levelCamera:GetComponent("UIPartialBlur")

	ReflectionHelp.RefCallMethod(typeof("UIPartialBlur"), "Cleanup", arg_1_0._levelCameraPartial)

	arg_1_0._levelCameraPartial.blurCam = arg_1_0.levelCameraComp
	arg_1_0.cameraBlurs = {
		[var_0_0.CameraUI] = {
			arg_1_0.uiCamera:GetComponent("BlurOptimized"),
			arg_1_0.uiCamera:GetComponent("UIStaticBlur"),
			arg_1_0._cameraBlurPartial
		},
		[var_0_0.CameraLevel] = {
			arg_1_0.levelCamera:GetComponent("BlurOptimized"),
			arg_1_0.levelCamera:GetComponent("UIStaticBlur"),
			arg_1_0._levelCameraPartial
		},
		[var_0_0.CameraOverlay] = {
			arg_1_0.overlayCamera:GetComponent("BlurOptimized"),
			(arg_1_0.overlayCamera:GetComponent("UIStaticBlur"))
		}
	}
	arg_1_0.camLockStatus = {
		[var_0_0.CameraUI] = false,
		[var_0_0.CameraLevel] = false,
		[var_0_0.CameraOverlay] = false
	}

	local function var_1_0(arg_2_0)
		if arg_2_0 == nil then
			return
		end

		arg_2_0.downsample = 2
		arg_2_0.blurSize = 4
		arg_2_0.blurIterations = 2
	end

	local function var_1_1(arg_3_0)
		if arg_3_0 == nil then
			return
		end

		arg_3_0.downsample = 2
		arg_3_0.blurSize = 1.5
		arg_3_0.blurIteration = 4
	end

	local function var_1_2(arg_4_0)
		if arg_4_0 == nil then
			return
		end

		arg_4_0.downsample = 2
		arg_4_0.blurSize = 4
		arg_4_0.blurIterations = 1
	end

	local function var_1_3(arg_5_0)
		if arg_5_0 == nil then
			return
		end

		arg_5_0.downsample = 2
		arg_5_0.blurSize = 1.5
		arg_5_0.blurIteration = 1
	end

	local var_1_4 = DevicePerformanceUtil.GetDeviceLevel()

	for iter_1_0, iter_1_1 in ipairs(arg_1_0.cameraBlurs) do
		if var_1_4 == DevicePerformanceLevel.Low then
			var_1_2(iter_1_1[var_0_0.OptimizedBlur])
			var_1_3(iter_1_1[var_0_0.PartialBlur])
		else
			var_1_0(iter_1_1[var_0_0.OptimizedBlur])
			var_1_1(iter_1_1[var_0_0.PartialBlur])
		end
	end

	arg_1_0.defaultMaterial = Material.New(Shader.Find("UI/Default"))
	arg_1_0.partialBlurMaterial = Material.New(Shader.Find("UI/PartialBlur"))
	arg_1_0._debugPanel = DebugPanel.New()

	setActive(arg_1_0.uiCamera, false)
	seriesAsync({
		function(arg_6_0)
			buildTempAB("ui/commonui_atlas", function(arg_7_0)
				arg_1_0._common_ui_bundle = arg_7_0

				arg_6_0()
			end)
		end,
		function(arg_8_0)
			buildTempAB("skinicon", function(arg_9_0)
				arg_1_0._skinicon_bundle = arg_9_0

				arg_8_0()
			end)
		end,
		function(arg_10_0)
			buildTempAB("attricon", function(arg_11_0)
				arg_1_0._attricon_bundle = arg_11_0

				arg_10_0()
			end)
		end,
		function(arg_12_0)
			setActive(arg_1_0.uiCamera, true)

			arg_1_0._loadPanel = LoadingPanel.New(arg_12_0)
		end,
		function(arg_13_0)
			PoolMgr.GetInstance():GetUI("ClickEffect", true, function(arg_14_0)
				setParent(arg_14_0, arg_1_0.OverlayEffect)

				local var_14_0 = PlayerPrefs.GetInt(SHOW_TOUCH_EFFECT, 1) > 0

				SetActive(arg_1_0.OverlayEffect, var_14_0)
				arg_13_0()
			end)
		end
	}, arg_1_1)
end

function var_0_0.Loading(arg_15_0, arg_15_1)
	arg_15_0._loadPanel:appendInfo(arg_15_1)
end

function var_0_0.LoadingOn(arg_16_0, arg_16_1)
	arg_16_0._loadPanel:on(arg_16_1)
end

function var_0_0.displayLoadingBG(arg_17_0, arg_17_1)
	arg_17_0._loadPanel:displayBG(arg_17_1)
end

function var_0_0.LoadingOff(arg_18_0)
	arg_18_0._loadPanel:off()
end

function var_0_0.OnLoading(arg_19_0)
	return arg_19_0._loadPanel:onLoading()
end

function var_0_0.LoadingRetainCount(arg_20_0)
	return arg_20_0._loadPanel:getRetainCount()
end

function var_0_0.AddDebugButton(arg_21_0, arg_21_1, arg_21_2)
	arg_21_0._debugPanel:addCustomBtn(arg_21_1, arg_21_2)
end

function var_0_0.AddWorldTestButton(arg_22_0, arg_22_1, arg_22_2)
	arg_22_0._debugPanel:addCustomBtn(arg_22_1, function()
		arg_22_0._debugPanel:hidePanel()
		arg_22_2()
	end)
end

var_0_0._maxbianjie = 50
var_0_0._maxbianjieInv = 0.02
var_0_0._maxbianjieSqr = 2500
var_0_0._followRange = 0
var_0_0._stick = nil
var_0_0._areaImg = nil
var_0_0._stickImg = nil
var_0_0._stickCom = nil
var_0_0._normalColor = Color(255, 255, 255, 1)
var_0_0._darkColor = Color(255, 255, 255, 0.5)
var_0_0._firstPos = Vector3.zero

function var_0_0.AttachStickOb(arg_24_0, arg_24_1)
	arg_24_0.hrz = 0
	arg_24_0.vtc = 0
	arg_24_0.fingerId = -1

	local var_24_0 = arg_24_1:Find("Area")

	arg_24_0._stick = var_24_0:Find("Stick")
	arg_24_0._areaImg = var_24_0:GetComponent(typeof(Image))
	arg_24_0._stickImg = arg_24_0._stick:GetComponent(typeof(Image))
	arg_24_0._stickCom = arg_24_1:GetComponent(typeof(StickController))
	arg_24_0._stickCom.StickBorderRate = 1

	arg_24_0._stickCom:SetStickFunc(function(arg_25_0, arg_25_1)
		arg_24_0:UpdateStick(arg_25_0, arg_25_1)
	end)

	arg_24_0._firstPos = var_24_0.localPosition
	arg_24_0.vtc = 0

	arg_24_0:SetActive(true)
end

function var_0_0.SetActive(arg_26_0, arg_26_1)
	arg_26_0._stickActive = arg_26_1
end

function var_0_0.Marching(arg_27_0)
	local var_27_0 = ys.Battle.BattleConfig

	LeanTween.value(go(arg_27_0._stick), 0, 0.625, 1.8):setOnUpdate(System.Action_float(function(arg_28_0)
		arg_27_0.hrz = var_27_0.START_SPEED_CONST_B * (arg_28_0 - var_27_0.START_SPEED_CONST_A) * (arg_28_0 - var_27_0.START_SPEED_CONST_A)
	end)):setOnComplete(System.Action(function()
		arg_27_0.hrz = 0
	end))
end

function var_0_0.UpdateStick(arg_30_0, arg_30_1, arg_30_2)
	if not arg_30_0._stickActive then
		return
	end

	if arg_30_2 == -2 then
		arg_30_0:SetOutput(arg_30_1.x, arg_30_1.y, -2)

		return
	elseif arg_30_2 == -1 then
		arg_30_0:SetOutput(0, 0, arg_30_2)

		return
	end

	local var_30_0 = arg_30_1

	var_30_0.z = 0

	local var_30_1 = var_30_0:SqrMagnitude()

	if var_30_1 > arg_30_0._maxbianjieSqr then
		var_30_0 = var_30_0 / math.sqrt(var_30_1)

		local var_30_2 = var_30_0 * arg_30_0._maxbianjie

		if arg_30_1 - var_30_2 ~= arg_30_0._firstPos then
			local var_30_3 = arg_30_0._firstPos
		end

		arg_30_0._stick.localPosition = var_30_2

		arg_30_0:SetOutput(var_30_0.x, var_30_0.y, arg_30_2)
	else
		arg_30_0._stick.localPosition = arg_30_1

		arg_30_0:SetOutput(var_30_0.x * arg_30_0._maxbianjieInv, var_30_0.y * arg_30_0._maxbianjieInv, arg_30_2)
	end
end

function var_0_0.SetOutput(arg_31_0, arg_31_1, arg_31_2, arg_31_3)
	arg_31_0.hrz = arg_31_1
	arg_31_0.vtc = arg_31_2

	local var_31_0 = (arg_31_3 >= 0 and 1 or 0) - (arg_31_0.fingerId >= 0 and 1 or 0)

	if var_31_0 ~= 0 and arg_31_0._areaImg and arg_31_0._stickImg then
		arg_31_0._areaImg.color = var_31_0 > 0 and var_0_0._normalColor or var_0_0._darkColor
		arg_31_0._stickImg.color = var_31_0 > 0 and var_0_0._normalColor or var_0_0._darkColor
	end

	if arg_31_3 < 0 then
		arg_31_0._stick.localPosition = Vector3.zero
	end

	arg_31_0.fingerId = arg_31_3
end

function var_0_0.ClearStick(arg_32_0)
	arg_32_0._stick.localPosition = Vector3.zero

	arg_32_0._stickCom:ClearStickFunc()

	arg_32_0._stick = nil
	arg_32_0._areaImg = nil
	arg_32_0._stickImg = nil
	arg_32_0._stickCom = nil
end

local var_0_2 = {}
local var_0_3 = false

function var_0_0.OverlayPanel(arg_33_0, arg_33_1, arg_33_2)
	arg_33_2 = arg_33_2 or {}
	arg_33_2.globalBlur = false

	var_0_1.LayerWeightMgr.GetInstance():Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_33_1, arg_33_2)
end

function var_0_0.UnOverlayPanel(arg_34_0, arg_34_1, arg_34_2)
	var_0_1.LayerWeightMgr.GetInstance():DelFromOverlay(arg_34_1, arg_34_2 or arg_34_0.UIMain)
end

function var_0_0.BlurPanel(arg_35_0, arg_35_1, arg_35_2, arg_35_3)
	arg_35_3 = arg_35_3 or {}
	arg_35_3.globalBlur = true
	arg_35_3.staticBlur = arg_35_2

	var_0_1.LayerWeightMgr.GetInstance():Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_35_1, arg_35_3)
end

function var_0_0.UnblurPanel(arg_36_0, arg_36_1, arg_36_2)
	var_0_1.LayerWeightMgr.GetInstance():DelFromOverlay(arg_36_1, arg_36_2 or arg_36_0.UIMain)
end

function var_0_0.OverlayPanelPB(arg_37_0, arg_37_1, arg_37_2)
	arg_37_2 = arg_37_2 or {}
	arg_37_2.globalBlur = false

	var_0_1.LayerWeightMgr.GetInstance():Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_37_1, arg_37_2)
end

function var_0_0.PartialBlurTfs(arg_38_0, arg_38_1)
	var_0_3 = true
	var_0_2 = arg_38_1

	arg_38_0:UpdatePBEnable(true)
end

function var_0_0.ShutdownPartialBlur(arg_39_0)
	var_0_3 = false
	var_0_2 = {}

	arg_39_0:UpdatePBEnable(false)
end

function var_0_0.RevertPBMaterial(arg_40_0, arg_40_1)
	for iter_40_0, iter_40_1 in ipairs(arg_40_1) do
		local var_40_0 = iter_40_1:GetComponent(typeof(Image))

		assert(var_40_0, "mask should be an image.")

		var_40_0.material = arg_40_0.defaultMaterial
	end
end

function var_0_0.UpdatePBEnable(arg_41_0, arg_41_1)
	if arg_41_1 then
		if var_0_2 ~= nil then
			for iter_41_0, iter_41_1 in ipairs(var_0_2) do
				local var_41_0 = iter_41_1:GetComponent(typeof(Image))

				assert(var_41_0, "mask should be an image.")

				var_41_0.material = arg_41_1 and arg_41_0.partialBlurMaterial or nil
			end
		end

		if arg_41_0.levelCameraComp.enabled then
			arg_41_0.cameraBlurs[var_0_0.CameraLevel][var_0_0.PartialBlur].enabled = true
			arg_41_0.cameraBlurs[var_0_0.CameraUI][var_0_0.PartialBlur].enabled = false
		else
			arg_41_0.cameraBlurs[var_0_0.CameraLevel][var_0_0.PartialBlur].enabled = false
			arg_41_0.cameraBlurs[var_0_0.CameraUI][var_0_0.PartialBlur].enabled = true
		end
	else
		for iter_41_2, iter_41_3 in ipairs(arg_41_0.cameraBlurs) do
			if iter_41_3[var_0_0.PartialBlur] then
				iter_41_3[var_0_0.PartialBlur].enabled = false
			end
		end
	end
end

function var_0_0.BlurCamera(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
	if not arg_42_0.camLockStatus[arg_42_1] or arg_42_3 then
		local var_42_0 = arg_42_0.cameraBlurs[arg_42_1][var_0_0.OptimizedBlur]
		local var_42_1 = arg_42_0.cameraBlurs[arg_42_1][var_0_0.StaticBlur]

		if arg_42_2 then
			var_42_0.enabled = true
			var_42_0.staticBlur = true
			var_42_1.enabled = false
		else
			var_42_0.enabled = true
			var_42_0.staticBlur = false
			var_42_1.enabled = false
		end

		if arg_42_3 then
			arg_42_0.camLockStatus[arg_42_1] = true
		end
	end
end

function var_0_0.UnblurCamera(arg_43_0, arg_43_1, arg_43_2)
	if not arg_43_0.camLockStatus[arg_43_1] or arg_43_2 then
		local var_43_0 = arg_43_0.cameraBlurs[arg_43_1][var_0_0.OptimizedBlur]

		arg_43_0.cameraBlurs[arg_43_1][var_0_0.StaticBlur].enabled = false
		var_43_0.enabled = false

		if arg_43_2 then
			arg_43_0.camLockStatus[arg_43_1] = false
		end
	end
end

function var_0_0.GetStaticRtt(arg_44_0, arg_44_1)
	local var_44_0 = arg_44_0.cameraBlurs[arg_44_1][var_0_0.OptimizedBlur]

	return (ReflectionHelp.RefGetField(typeof("UnityStandardAssets.ImageEffects.BlurOptimized"), "staticRtt", var_44_0))
end

function var_0_0.SetMainCamBlurTexture(arg_45_0, arg_45_1)
	local var_45_0 = arg_45_0.mainCamera:GetComponent(typeof(Camera))
	local var_45_1 = ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "GetTemporary", {
		typeof("System.Int32"),
		typeof("System.Int32"),
		typeof("System.Int32")
	}, {
		Screen.width,
		Screen.height,
		0
	})

	var_45_0.targetTexture = var_45_1

	var_45_0:Render()

	local var_45_2 = var_0_1.ShaderMgr.GetInstance():BlurTexture(var_45_1)

	var_45_0.targetTexture = nil

	ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "ReleaseTemporary", {
		typeof("UnityEngine.RenderTexture")
	}, {
		var_45_1
	})

	arg_45_1.uvRect = var_45_0.rect
	arg_45_1.texture = var_45_2

	return var_45_2
end

function var_0_0.GetMainCamera(arg_46_0)
	return arg_46_0.mainCamera
end

function var_0_0.InitBgmCfg(arg_47_0, arg_47_1)
	arg_47_0.isDefaultBGM = false

	if OPEN_SPECIAL_IP_BGM and PLATFORM_CODE == PLATFORM_US then
		if IsUnityEditor then
			if arg_47_1 then
				arg_47_1()
			end

			return
		end

		local var_47_0 = {
			"Malaysia",
			"Indonesia"
		}
		local var_47_1 = "https://pro.ip-api.com/json/?key=TShzQlq7O9KuthI"
		local var_47_2 = ""

		local function var_47_3(arg_48_0)
			local var_48_0 = "\"country\":\""
			local var_48_1 = "\","
			local var_48_2, var_48_3 = string.find(arg_48_0, var_48_0)

			if var_48_3 then
				arg_48_0 = string.sub(arg_48_0, var_48_3 + 1)
			end

			local var_48_4 = string.find(arg_48_0, var_48_1)

			if var_48_4 then
				arg_48_0 = string.sub(arg_48_0, 1, var_48_4 - 1)
			end

			return arg_48_0
		end

		local function var_47_4(arg_49_0)
			local var_49_0 = false

			for iter_49_0, iter_49_1 in ipairs(var_47_0) do
				if iter_49_1 == arg_49_0 then
					var_49_0 = true
				end
			end

			return var_49_0
		end

		VersionMgr.Inst:WebRequest(var_47_1, function(arg_50_0, arg_50_1)
			local var_50_0 = var_47_3(arg_50_1)

			originalPrint("content: " .. arg_50_1)
			originalPrint("country is: " .. var_50_0)

			arg_47_0.isDefaultBGM = var_47_4(var_50_0)

			originalPrint("IP limit: " .. tostring(arg_47_0.isDefaultBGM))

			if arg_47_1 then
				arg_47_1()
			end
		end)
	elseif arg_47_1 then
		arg_47_1()
	end
end

function var_0_0.IsDefaultBGM(arg_51_0)
	return arg_51_0.isDefaultBGM
end
