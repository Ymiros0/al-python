from packages.Vector3 import Vector3
from packages.luatable import table, ipairs

from main import PLATFORM_CODE
from mod.battle.data import BattleConfig
from Framework.tolua.tolua import Camera, Color, GameObject, Image, Material, PlayerPrefs, Screen, Shader #!
from Framework.tolua.typeof import typeof #!
from const import OPEN_SPECIAL_IP_BGM, SHOW_TOUCH_EFFECT
from mgr.ShaderMgr import ShaderMgr
from mgr.LayerWeightMgr import LayerWeightMgr
from mgr.const import LayerWeightConst
from mgr.pool.PoolMgr import PoolMgr #!
from support.helpers import ReflectionHelp #!
from support.helpers.M02 import buildTempAB
from support.helpers.UnitySupport import tf, setActive, SetActive, setParent, seriesAsync, go #!
from view.ui.DebugPanel import DebugPanel
from view.ui.LoadingPanel import LoadingPanel
from RunPaintingFilte import PLATFORM_US

import DevicePerformanceUtil #???? Injected
import DevicePerformanceLevel #Literally never defined
import StickController
import LeanTween
import System

class UIMgr:
	_loadPanel = None
	CameraUI = 1
	CameraLevel = 2
	CameraOverlay = 3
	OptimizedBlur = 1
	StaticBlur = 2
	PartialBlur = 3

	def Init(arg_1_0, arg_1_1):
		print("initializing ui manager...")

		arg_1_0.mainCamera = GameObject.Find("MainCamera")
		arg_1_0.mainCameraComp = arg_1_0.mainCamera.GetComponent("Camera")
		arg_1_0.uiCamera = tf(GameObject.Find("UICamera"))
		arg_1_0.uiCameraComp = arg_1_0.uiCamera.GetComponent("Camera")
		arg_1_0.uiCameraComp.allowMSAA = False
		arg_1_0.levelCamera = tf(GameObject.Find("LevelCamera"))
		arg_1_0.levelCameraComp = arg_1_0.levelCamera.GetComponent("Camera")
		arg_1_0.levelCameraComp.allowMSAA = False
		arg_1_0.overlayCamera = tf(GameObject.Find("OverlayCamera"))
		arg_1_0.overlayCameraComp = arg_1_0.overlayCamera.GetComponent("Camera")
		arg_1_0.overlayCameraComp.allowMSAA = False
		arg_1_0.UIMain = arg_1_0.uiCamera.Find("Canvas/UIMain")
		arg_1_0.LevelMain = arg_1_0.levelCamera.Find("Canvas/UIMain")
		arg_1_0.OverlayMain = arg_1_0.overlayCamera.Find("Overlay/UIMain")
		arg_1_0.OverlayToast = arg_1_0.overlayCamera.Find("Overlay/UIOverlay")
		arg_1_0.OverlayEffect = arg_1_0.overlayCamera.Find("Overlay/UIEffect")
		arg_1_0._normalUIMain = None
		arg_1_0._cameraBlurPartial = arg_1_0.uiCamera.GetComponent("UIPartialBlur")
		arg_1_0._levelCameraPartial = arg_1_0.levelCamera.GetComponent("UIPartialBlur")

		ReflectionHelp.RefCallMethod(typeof("UIPartialBlur"), "Cleanup", arg_1_0._levelCameraPartial)

		arg_1_0._levelCameraPartial.blurCam = arg_1_0.levelCameraComp
		arg_1_0.cameraBlurs = table({
			UIMgr.CameraUI: table(
				arg_1_0.uiCamera.GetComponent("BlurOptimized"),
				arg_1_0.uiCamera.GetComponent("UIStaticBlur"),
				arg_1_0._cameraBlurPartial
			),
			UIMgr.CameraLevel: table(
				arg_1_0.levelCamera.GetComponent("BlurOptimized"),
				arg_1_0.levelCamera.GetComponent("UIStaticBlur"),
				arg_1_0._levelCameraPartial
			),
			UIMgr.CameraOverlay: table(
				arg_1_0.overlayCamera.GetComponent("BlurOptimized"),
				(arg_1_0.overlayCamera.GetComponent("UIStaticBlur"))
			)
		})
		arg_1_0.camLockStatus = table({
			UIMgr.CameraUI: False,
			UIMgr.CameraLevel: False,
			UIMgr.CameraOverlay: False
		})

		def var_1_0(arg_2_0):
			if arg_2_0 == None:
				return

			arg_2_0.downsample = 2
			arg_2_0.blurSize = 4
			arg_2_0.blurIterations = 2

		def var_1_1(arg_3_0):
			if arg_3_0 == None:
				return

			arg_3_0.downsample = 2
			arg_3_0.blurSize = 1.5
			arg_3_0.blurIteration = 4

		def var_1_2(arg_4_0):
			if arg_4_0 == None:
				return

			arg_4_0.downsample = 2
			arg_4_0.blurSize = 4
			arg_4_0.blurIterations = 1

		def var_1_3(arg_5_0):
			if arg_5_0 == None:
				return

			arg_5_0.downsample = 2
			arg_5_0.blurSize = 1.5
			arg_5_0.blurIteration = 1

		var_1_4 = DevicePerformanceUtil.GetDeviceLevel()

		for iter_1_0, iter_1_1 in ipairs(arg_1_0.cameraBlurs):
			if var_1_4 == DevicePerformanceLevel.Low:
				var_1_2(iter_1_1[UIMgr.OptimizedBlur])
				var_1_3(iter_1_1[UIMgr.PartialBlur])
			else:
				var_1_0(iter_1_1[UIMgr.OptimizedBlur])
				var_1_1(iter_1_1[UIMgr.PartialBlur])

		arg_1_0.defaultMaterial = Material.New(Shader.Find("UI/Default"))
		arg_1_0.partialBlurMaterial = Material.New(Shader.Find("UI/UIMgr.PartialBlur"))
		arg_1_0._debugPanel = DebugPanel.New()

		setActive(arg_1_0.uiCamera, False)
		def _function(arg_6_0):
			def _function_inner(arg_7_0):
				arg_1_0._common_ui_bundle = arg_7_0

				arg_6_0()
			buildTempAB("ui/commonui_atlas", _function_inner)
		def _function2(arg_8_0):
			def _function_inner(arg_9_0):
				arg_1_0._skinicon_bundle = arg_9_0

				arg_8_0()
			buildTempAB("skinicon", _function_inner)
		def _function3(arg_10_0):
			def _function_inner(arg_11_0):
				arg_1_0._attricon_bundle = arg_11_0

				arg_10_0()
			buildTempAB("attricon", _function_inner)
		def _function4(arg_12_0):
			setActive(arg_1_0.uiCamera, True)

			arg_1_0._loadPanel = LoadingPanel.New(arg_12_0)
		def _function5(arg_13_0):
			def _function_inner(arg_14_0):
				setParent(arg_14_0, arg_1_0.OverlayEffect)

				var_14_0 = PlayerPrefs.GetInt(SHOW_TOUCH_EFFECT, 1) > 0

				SetActive(arg_1_0.OverlayEffect, var_14_0)
				arg_13_0()
			PoolMgr().GetUI("ClickEffect", True, _function_inner)

		seriesAsync(table(
			_function,
			_function2,
			_function3,
			_function4,
			_function5
		), arg_1_1)

	def Loading(arg_15_0, arg_15_1):
		arg_15_0._loadPanel.appendInfo(arg_15_1)

	def LoadingOn(arg_16_0, arg_16_1):
		arg_16_0._loadPanel.on(arg_16_1)

	def displayLoadingBG(arg_17_0, arg_17_1):
		arg_17_0._loadPanel.displayBG(arg_17_1)

	def LoadingOff(arg_18_0):
		arg_18_0._loadPanel.off()

	def OnLoading(arg_19_0):
		return arg_19_0._loadPanel.onLoading()

	def LoadingRetainCount(arg_20_0):
		return arg_20_0._loadPanel.getRetainCount()

	def AddDebugButton(arg_21_0, arg_21_1, arg_21_2):
		arg_21_0._debugPanel.addCustomBtn(arg_21_1, arg_21_2)

	def AddWorldTestButton(arg_22_0, arg_22_1, arg_22_2):
		def _func():
			arg_22_0._debugPanel.hidePanel()
			arg_22_2()
		arg_22_0._debugPanel.addCustomBtn(arg_22_1, _func)

	_maxbianjie = 50
	_maxbianjieInv = 0.02
	_maxbianjieSqr = 2500
	_followRange = 0
	_stick = None
	_areaImg = None
	_stickImg = None
	_stickCom = None
	_normalColor = Color(255, 255, 255, 1)
	_darkColor = Color(255, 255, 255, 0.5)
	_firstPos = Vector3.zero

	def AttachStickOb(arg_24_0, arg_24_1):
		arg_24_0.hrz = 0
		arg_24_0.vtc = 0
		arg_24_0.fingerId = -1

		var_24_0 = arg_24_1.Find("Area")

		arg_24_0._stick = var_24_0.Find("Stick")
		arg_24_0._areaImg = var_24_0.GetComponent(typeof(Image))
		arg_24_0._stickImg = arg_24_0._stick.GetComponent(typeof(Image))
		arg_24_0._stickCom = arg_24_1.GetComponent(typeof(StickController))
		arg_24_0._stickCom.StickBorderRate = 1

		arg_24_0._stickCom.SetStickFunc(lambda arg_25_0, arg_25_1: arg_24_0.UpdateStick(arg_25_0, arg_25_1))

		arg_24_0._firstPos = var_24_0.localPosition
		arg_24_0.vtc = 0

		arg_24_0.SetActive(True)

	def SetActive(arg_26_0, arg_26_1):
		arg_26_0._stickActive = arg_26_1

	def Marching(arg_27_0):
		var_27_0 = BattleConfig

		def march(arg_28_0):
			arg_27_0.hrz = var_27_0.START_SPEED_CONST_B * (arg_28_0 - var_27_0.START_SPEED_CONST_A) * (arg_28_0 - var_27_0.START_SPEED_CONST_A)

		LeanTween.value(go(arg_27_0._stick), 0, 0.625, 1.8).setOnUpdate(System.Action_float(march)).setOnComplete(System.Action(lambda: setattr(arg_27_0, 'hrz', 0)))

	def UpdateStick(arg_30_0, arg_30_1, arg_30_2):
		if not arg_30_0._stickActive:
			return

		if arg_30_2 == -2:
			arg_30_0.SetOutput(arg_30_1.x, arg_30_1.y, -2)

			return
		elif arg_30_2 == -1:
			arg_30_0.SetOutput(0, 0, arg_30_2)

			return

		var_30_0 = arg_30_1

		var_30_0.z = 0

		var_30_1 = var_30_0.SqrMagnitude()

		if var_30_1 > arg_30_0._maxbianjieSqr:
			var_30_0 = var_30_0 / var_30_1**0.5

			var_30_2 = var_30_0 * arg_30_0._maxbianjie

			if arg_30_1 - var_30_2 != arg_30_0._firstPos:
				var_30_3 = arg_30_0._firstPos

			arg_30_0._stick.localPosition = var_30_2

			arg_30_0.SetOutput(var_30_0.x, var_30_0.y, arg_30_2)
		else:
			arg_30_0._stick.localPosition = arg_30_1

			arg_30_0.SetOutput(var_30_0.x * arg_30_0._maxbianjieInv, var_30_0.y * arg_30_0._maxbianjieInv, arg_30_2)

	def SetOutput(self, arg_31_1, arg_31_2, arg_31_3):
		self.hrz = arg_31_1
		self.vtc = arg_31_2

		var_31_0 = (arg_31_3 >= 0 and 1 or 0) - (self.fingerId >= 0 and 1 or 0)

		if var_31_0 != 0 and self._areaImg and self._stickImg:
			self._areaImg.color = var_31_0 > 0 and self._normalColor or self._darkColor
			self._stickImg.color = var_31_0 > 0 and self._normalColor or self._darkColor

		if arg_31_3 < 0:
			self._stick.localPosition = Vector3.zero

		self.fingerId = arg_31_3

	def ClearStick(arg_32_0):
		arg_32_0._stick.localPosition = Vector3.zero

		arg_32_0._stickCom.ClearStickFunc()

		arg_32_0._stick = None
		arg_32_0._areaImg = None
		arg_32_0._stickImg = None
		arg_32_0._stickCom = None

	var_0_2 = table()
	var_0_3 = False

	def OverlayPanel(arg_33_0, arg_33_1, arg_33_2):
		arg_33_2 = arg_33_2 or table()
		arg_33_2.globalBlur = False

		LayerWeightMgr.GetInstance().Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_33_1, arg_33_2)

	def UnOverlayPanel(arg_34_0, arg_34_1, arg_34_2):
		LayerWeightMgr.GetInstance().DelFromOverlay(arg_34_1, arg_34_2 or arg_34_0.UIMain)

	def BlurPanel(arg_35_0, arg_35_1, arg_35_2, arg_35_3):
		arg_35_3 = arg_35_3 or table()
		arg_35_3.globalBlur = True
		arg_35_3.staticBlur = arg_35_2

		LayerWeightMgr.GetInstance().Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_35_1, arg_35_3)

	def UnblurPanel(arg_36_0, arg_36_1, arg_36_2):
		LayerWeightMgr.GetInstance().DelFromOverlay(arg_36_1, arg_36_2 or arg_36_0.UIMain)

	def OverlayPanelPB(arg_37_0, arg_37_1, arg_37_2):
		arg_37_2 = arg_37_2 or table()
		arg_37_2.globalBlur = False

		LayerWeightMgr.GetInstance().Add2Overlay(LayerWeightConst.UI_TYPE_SUB, arg_37_1, arg_37_2)

	def PartialBlurTfs(arg_38_0, arg_38_1):
		var_0_3 = True
		var_0_2 = arg_38_1

		arg_38_0.UpdatePBEnable(True)

	def ShutdownPartialBlur(arg_39_0):
		var_0_3 = False
		var_0_2 = table()

		arg_39_0.UpdatePBEnable(False)

	def RevertPBMaterial(arg_40_0, arg_40_1):
		for iter_40_0, iter_40_1 in ipairs(arg_40_1):
			var_40_0 = iter_40_1.GetComponent(typeof(Image))

			assert(var_40_0, "mask should be an image.")

			var_40_0.material = arg_40_0.defaultMaterial

	def UpdatePBEnable(self, arg_41_1):
		if arg_41_1:
			if self.var_0_2 != None:
				for iter_41_0, iter_41_1 in ipairs(self.var_0_2):
					var_41_0 = iter_41_1.GetComponent(typeof(Image))

					assert(var_41_0, "mask should be an image.")

					var_41_0.material = arg_41_1 and self.partialBlurMaterial or None

			if self.levelCameraComp.enabled:
				self.cameraBlurs[UIMgr.CameraLevel][UIMgr.PartialBlur].enabled = True
				self.cameraBlurs[UIMgr.CameraUI][UIMgr.PartialBlur].enabled = False
			else:
				self.cameraBlurs[UIMgr.CameraLevel][UIMgr.PartialBlur].enabled = False
				self.cameraBlurs[UIMgr.CameraUI][UIMgr.PartialBlur].enabled = True
		else:
			for iter_41_2, iter_41_3 in ipairs(self.cameraBlurs):
				if iter_41_3[UIMgr.PartialBlur]:
					iter_41_3[UIMgr.PartialBlur].enabled = False

	def BlurCamera(arg_42_0, arg_42_1, arg_42_2, arg_42_3):
		if not arg_42_0.camLockStatus[arg_42_1] or arg_42_3:
			var_42_0 = arg_42_0.cameraBlurs[arg_42_1][UIMgr.OptimizedBlur]
			var_42_1 = arg_42_0.cameraBlurs[arg_42_1][UIMgr.StaticBlur]

			if arg_42_2:
				var_42_0.enabled = True
				var_42_0.staticBlur = True
				var_42_1.enabled = False
			else:
				var_42_0.enabled = True
				var_42_0.staticBlur = False
				var_42_1.enabled = False

			if arg_42_3:
				arg_42_0.camLockStatus[arg_42_1] = True

	def UnblurCamera(arg_43_0, arg_43_1, arg_43_2):
		if not arg_43_0.camLockStatus[arg_43_1] or arg_43_2:
			var_43_0 = arg_43_0.cameraBlurs[arg_43_1][UIMgr.OptimizedBlur]

			arg_43_0.cameraBlurs[arg_43_1][UIMgr.StaticBlur].enabled = False
			var_43_0.enabled = False

			if arg_43_2:
				arg_43_0.camLockStatus[arg_43_1] = False

	def GetStaticRtt(arg_44_0, arg_44_1):
		var_44_0 = arg_44_0.cameraBlurs[arg_44_1][UIMgr.OptimizedBlur]

		return (ReflectionHelp.RefGetField(typeof("UnityStandardAssets.ImageEffects.BlurOptimized"), "staticRtt", var_44_0))

	def SetMainCamBlurTexture(arg_45_0, arg_45_1):
		var_45_0 = arg_45_0.mainCamera.GetComponent(typeof(Camera))
		var_45_1 = ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "GetTemporary", table(
			typeof("System.Int32"),
			typeof("System.Int32"),
			typeof("System.Int32")
		), table(
			Screen.width,
			Screen.height,
			0
		))

		var_45_0.targetTexture = var_45_1

		var_45_0.Render()

		var_45_2 = ShaderMgr.GetInstance().BlurTexture(var_45_1)

		var_45_0.targetTexture = None

		ReflectionHelp.RefCallStaticMethod(typeof("UnityEngine.RenderTexture"), "ReleaseTemporary", table(
			typeof("UnityEngine.RenderTexture")
		), table(
			var_45_1
		))

		arg_45_1.uvRect = var_45_0.rect
		arg_45_1.texture = var_45_2

		return var_45_2

	def GetMainCamera(arg_46_0):
		return arg_46_0.mainCamera

	def InitBgmCfg(arg_47_0, arg_47_1):
		arg_47_0.isDefaultBGM = False

		if OPEN_SPECIAL_IP_BGM and PLATFORM_CODE == PLATFORM_US:
			if IsUnityEditor:
				if arg_47_1:
					arg_47_1()

				return

			var_47_0 = table(
				"Malaysia",
				"Indonesia"
			)
			var_47_1 = "https.//pro.ip-api.com/json/?key=TShzQlq7O9KuthI"
			var_47_2 = ""

			def var_47_3(arg_48_0):
				import re
				var_48_0 = "\"country\".\"(.*?)\","
				res = re.search(var_48_0, arg_48_0)
				if res:
					arg_48_0 = res.group(1)

				return arg_48_0

			def var_47_4(arg_49_0):
				var_49_0 = False

				for iter_49_0, iter_49_1 in ipairs(var_47_0):
					if iter_49_1 == arg_49_0:
						var_49_0 = True

				return var_49_0

			def _func(arg_50_0, arg_50_1):
				var_50_0 = var_47_3(arg_50_1)

				originalPrint("content. " + arg_50_1)
				originalPrint("country is. " + var_50_0)

				arg_47_0.isDefaultBGM = var_47_4(var_50_0)

				originalPrint("IP limit. " + str(arg_47_0.isDefaultBGM))

				if arg_47_1:
					arg_47_1()

			VersionMgr.Inst.WebRequest(var_47_1, _func)
		elif arg_47_1:
			arg_47_1()

	def IsDefaultBGM(arg_51_0):
		return arg_51_0.isDefaultBGM
