from packages.Vector3 import Vector2, Vector3
from packages.luatable import table, pairs, ipairs

from Framework.base.mvc.Mediator import Mediator
from Framework.tolua.tolua import Button, Screen, PlayerPrefs, Camera, GameObject, Animator #!
from Framework.tolua.typeof import typeof #!
from mod.battle import BattleEvent, BattleUnitEvent
from mod.battle.BattleState import BattleState
from mod.battle.data import BattleConfig, BattleConst
from mod.battle.data.BattleDataProxy import BattleDataProxy
from mod.battle.data.BattleVariable import BattleVariable
from mod.battle.view.BattleResourceManager import BattleResourceManager #!
from mod.battle.view.scene.BattleMap import BattleMap #!
from mgr.EffectMgr import EffectMgr #!
from mgr.SeriesGuideMgr import SeriesGuideMgr #!
from mgr.UIMgr import UIMgr #!
from support.helpers.UnitySupport import setActive, SetActive, triggerToggle, eachChild, setParent, go #!
from BattleFXPool import BattleFXPool #!
from formationpanel.BattleTimerView import BattleTimerView #!
from formationpanel.BattleEnmeyHpBarView import BattleEnmeyHpBarView #!
from formationpanel.BattleAirStrikeIconView import BattleAirStrikeIconView #!
from formationpanel.BattleCommonWarningView import BattleCommonWarningView #!
from formationpanel.BattleScoreBarView import BattleScoreBarView #!
from formationpanel.BattleDuelDamageRateView import BattleDuelDamageRateView #!
from formationpanel.BattleSimulationBuffCountView import BattleSimulationBuffCountView #!
from formationpanel.BattleMainDamagedView import BattleMainDamagedView #!
from formationpanel.BattleInkView import BattleInkView #!
from formationpanel.BattleReisalinAPView import BattleReisalinAPView #!
from formationpanel.BattleDebugConsole import BattleDebugConsole #!
from formationpanel.BattleCameraSlider import BattleCameraSlider #!
from formationpanel.BattleSkillView import BattleSkillView #!
from formationpanel.BattleOpticalSightView import BattleOpticalSightView #!
from formationpanel.BattleGridmanSkillFloatView import BattleGridmanSkillFloatView #!
from formationpanel.CardPuzzleCommonHPBar import CardPuzzleCommonHPBar #!
from formationpanel.CardPuzzleEnergyBar import CardPuzzleEnergyBar #!
from formationpanel.CardPuzzleBoardClicker import CardPuzzleBoardClicker #!
from formationpanel.CardPuzzleFleetHead import CardPuzzleFleetHead #!
from formationpanel.CardPuzzleCardDetail import CardPuzzleCardDetail #!
from formationpanel.CardPuzzleMovePile import CardPuzzleMovePile #!
from formationpanel.CardPuzzleDeckPool import CardPuzzleDeckPool #!
from formationpanel.CardPuzzleFleetIconList import CardPuzzleFleetIconList #!
from formationpanel.CardPuzzleHandBoard import CardPuzzleHandBoard #!
from formationpanel.CardPuzzleGoalRemind import CardPuzzleGoalRemind #!
from camera.BattleCameraUtil import BattleCameraUtil #!
from const import *
import BattleCardPuzzleEvent #!
from model.const import TeamType

import CameraMgr #???? Injected
import System
import LeanTween
import DftAniEvent
import Destroy

class BattleUIMediator(Mediator):

	BattleUIMediator = 	__name = "BattleUIMediator"

	def __init__(arg_1_0):
		super().__init__(arg_1_0)

	def SetBattleUI(arg_2_0):
		arg_2_0._ui = arg_2_0._state.GetUI()

	def Initialize(arg_3_0):
		super().Initialize(arg_3_0)

		arg_3_0._dataProxy = arg_3_0._state.GetProxyByName(BattleDataProxy.__name)
		arg_3_0._uiMGR = UIMgr.GetInstance()
		arg_3_0._fxPool = BattleFXPool.GetInstance()
		arg_3_0._updateViewList = {}

		arg_3_0.SetBattleUI()
		arg_3_0.AddUIEvent()
		arg_3_0.InitCamera()
		arg_3_0.InitGuide()

	def Reinitialize(arg_4_0):
		arg_4_0._skillView.Dispose()

	def EnableComponent(arg_5_0, arg_5_1):
		arg_5_0._ui.findTF("PauseBtn").GetComponent(typeof(Button)).enabled = arg_5_1

		arg_5_0._skillView.EnableWeaponButton(arg_5_1)

	def EnableJoystick(arg_6_0, arg_6_1):
		arg_6_0._stickController.enabled = arg_6_1

		setActive(arg_6_0._joystick, arg_6_1)

	def EnableWeaponButton(arg_7_0, arg_7_1):
		arg_7_0._skillView.EnableWeaponButton(arg_7_1)

	def EnableSkillFloat(arg_8_0, arg_8_1):
		arg_8_0._ui.EnableSkillFloat(arg_8_1)

	def GetAppearFX(arg_9_0):
		return arg_9_0._appearEffect

	def DisableComponent(arg_10_0):
		arg_10_0._ui.findTF("PauseBtn").GetComponent(typeof(Button)).enabled = False

		arg_10_0._skillView.DisableWeapnButton()
		SetActive(arg_10_0._ui.findTF("HPBarContainer"), False)
		SetActive(arg_10_0._ui.findTF("flagShipMark"), False)

		if arg_10_0._jammingView:
			arg_10_0._jammingView.Eliminate(False)

		if arg_10_0._inkView:
			arg_10_0._inkView.SetActive(False)

	def ActiveDebugConsole(arg_11_0):
		arg_11_0._debugConsoleView.SetActive(True)

	def OpeningEffect(arg_12_0, arg_12_1, arg_12_2):
		arg_12_0._uiMGR.SetActive(False)

		if arg_12_2 == SYSTEM_SUBMARINE_RUN:
			arg_12_0._skillView.SubmarineButton()

			var_12_0 = BattleConfig.JOY_STICK_DEFAULT_PREFERENCE

			arg_12_0._joystick.anchorMin = Vector2(var_12_0.x, var_12_0.y)
			arg_12_0._joystick.anchorMax = Vector2(var_12_0.x, var_12_0.y)
		elif arg_12_2 == SYSTEM_SUB_ROUTINE:
			arg_12_0._skillView.SubRoutineButton()
		elif arg_12_2 == SYSTEM_AIRFIGHT:
			arg_12_0._skillView.AirFightButton()
		elif arg_12_2 == SYSTEM_DEBUG:
			arg_12_0._skillView.NormalButton()
		elif arg_12_2 == SYSTEM_CARDPUZZLE:
			arg_12_0._skillView.CardPuzzleButton()
		else:
			var_12_1 = SeriesGuideMgr.GetInstance()

			if var_12_1.currIndex and var_12_1.isEnd():
				arg_12_0._skillView.NormalButton()
			else:
				var_12_2 = arg_12_0._dataProxy.GetDungeonData().skill_hide or {}

				arg_12_0._skillView.CustomButton(var_12_2)
		def _func(_):
			arg_12_0._uiMGR.SetActive(True)
			arg_12_0.EnableComponent(True)

			if arg_12_1:
				arg_12_1()
		arg_12_0._ui._go.GetComponent("DftAniEvent").SetEndEvent(_func)
		SetActive(arg_12_0._ui._go, True)
		arg_12_0._skillView.ButtonInitialAnima()

	def InitScene(arg_14_0):
		arg_14_0._mapId = arg_14_0._dataProxy._mapId
		arg_14_0._seaView = BattleMap.New(arg_14_0._mapId)

	def InitJoystick(arg_15_0):
		arg_15_0._joystick = arg_15_0._ui.findTF("Stick")

		var_15_0 = BattleConfig.JOY_STICK_DEFAULT_PREFERENCE
		var_15_1 = arg_15_0._joystick
		var_15_2 = Screen.dpi / CameraMgr.instance.finalWidth * 5

		if var_15_2 <= 0:
			var_15_2 = 1

		var_15_3 = PlayerPrefs.GetFloat("joystick_scale", var_15_0.scale)
		var_15_4 = PlayerPrefs.GetFloat("joystick_anchorX", var_15_0.x)
		var_15_5 = PlayerPrefs.GetFloat("joystick_anchorY", var_15_0.y)
		var_15_6 = var_15_2 * var_15_3

		arg_15_0._joystick.localScale = Vector3(var_15_6, var_15_6, 1)
		var_15_1.anchoredPosition = var_15_1.anchoredPosition * var_15_6
		arg_15_0._joystick.anchorMin = Vector2(var_15_4, var_15_5)
		arg_15_0._joystick.anchorMax = Vector2(var_15_4, var_15_5)
		arg_15_0._stickController = arg_15_0._joystick.GetComponent("StickController")

		arg_15_0._uiMGR.AttachStickOb(arg_15_0._joystick)

	def InitTimer(arg_16_0):
		if arg_16_0._dataProxy.GetInitData().battleType == SYSTEM_DUEL:
			arg_16_0._timerView = BattleTimerView.New(arg_16_0._ui.findTF("DuelTimer"))
		else:
			arg_16_0._timerView = BattleTimerView.New(arg_16_0._ui.findTF("Timer"))

	def InitEnemyHpBar(arg_17_0):
		arg_17_0._enemyHpBar = BattleEnmeyHpBarView.New(arg_17_0._ui.findTF("EnemyHPBar"))

	def InitAirStrikeIcon(arg_18_0):
		arg_18_0._airStrikeView = BattleAirStrikeIconView.New(arg_18_0._ui.findTF("AirFighterContainer/AirStrikeIcon"))
		arg_18_0._airSupportTF = arg_18_0._ui.findTF("AirSupportLabel")

	def InitCommonWarning(arg_19_0):
		arg_19_0._warningView = BattleCommonWarningView.New(arg_19_0._ui.findTF("WarningView"))
		arg_19_0._updateViewList[arg_19_0._warningView] = True

	def InitScoreBar(arg_20_0):
		arg_20_0._scoreBarView = BattleScoreBarView.New(arg_20_0._ui.findTF("DodgemCountBar"))

	def InitAirFightScoreBar(arg_21_0):
		arg_21_0._scoreBarView = BattleScoreBarView.New(arg_21_0._ui.findTF("AirFightCountBar"))

	def InitAutoBtn(arg_22_0):
		arg_22_0._autoBtn = arg_22_0._ui.findTF("AutoBtn")

		var_22_0 = BattleConfig.AUTO_DEFAULT_PREFERENCE
		var_22_1 = PlayerPrefs.GetFloat("auto_scale", var_22_0.scale)
		var_22_2 = PlayerPrefs.GetFloat("auto_anchorX", var_22_0.x)
		var_22_3 = PlayerPrefs.GetFloat("auto_anchorY", var_22_0.y)

		arg_22_0._autoBtn.localScale = Vector3(var_22_1, var_22_1, 1)
		arg_22_0._autoBtn.anchorMin = Vector2(var_22_2, var_22_3)
		arg_22_0._autoBtn.anchorMax = Vector2(var_22_2, var_22_3)

	def InitDuelRateBar(arg_23_0):
		arg_23_0._duelRateBar = BattleDuelDamageRateView.New(arg_23_0._ui.findTF("DuelDamageRate"))

		return arg_23_0._duelRateBar

	def InitSimulationBuffCounting(arg_24_0):
		arg_24_0._simulationBuffCountView = BattleSimulationBuffCountView.New(arg_24_0._ui.findTF("SimulationWarning"))

		return arg_24_0._simulationBuffCountView

	def InitMainDamagedView(arg_25_0):
		arg_25_0._mainDamagedView = BattleMainDamagedView.New(arg_25_0._ui.findTF("HPWarning"))

	def InitInkView(arg_26_0, arg_26_1):
		arg_26_0._inkView = BattleInkView.New(arg_26_0._ui.findTF("InkContainer"))

		arg_26_1.RegisterEventListener(arg_26_0, BattleEvent.FLEET_HORIZON_UPDATE, arg_26_0.onFleetHorizonUpdate)

	def InitDebugConsole(arg_27_0):
		arg_27_0._debugConsoleView = arg_27_0._debugConsoleView or BattleDebugConsole.New(arg_27_0._ui.findTF("Debug_Console"), arg_27_0._state)

	def InitCameraGestureSlider(arg_28_0):
		arg_28_0._gesture = BattleCameraSlider.New(arg_28_0._ui.findTF("CameraController"))

		BattleCameraUtil.GetInstance().SetCameraSilder(arg_28_0._gesture)
		arg_28_0._cameraUtil.SwitchCameraPos("FOLLOW_GESTURE")

	def InitAlchemistAPView(arg_29_0):
		arg_29_0._alchemistAP = BattleReisalinAPView.New(arg_29_0._ui.findTF("APPanel"))

	def InitGuide(arg_30_0):
		return

	def InitCamera(arg_31_0):
		arg_31_0._camera = UIMgr.GetInstance().GetMainCamera().GetComponent(typeof(Camera))
		arg_31_0._uiCamera = GameObject.Find("UICamera").GetComponent(typeof(Camera))
		arg_31_0._cameraUtil = BattleCameraUtil.GetInstance()

		arg_31_0._cameraUtil.RegisterEventListener(arg_31_0, BattleEvent.CAMERA_FOCUS, arg_31_0.onCameraFocus)
		arg_31_0._cameraUtil.RegisterEventListener(arg_31_0, BattleEvent.SHOW_PAINTING, arg_31_0.onShowPainting)
		arg_31_0._cameraUtil.RegisterEventListener(arg_31_0, BattleEvent.BULLET_TIME, arg_31_0.onBulletTime)

	def Update(arg_32_0):
		for iter_32_0, iter_32_1 in pairs(arg_32_0._updateViewList):
			iter_32_0.Update()

	def AddUIEvent(arg_33_0):
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.STAGE_DATA_INIT_FINISH, arg_33_0.onStageInit)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.COMMON_DATA_INIT_FINISH, arg_33_0.onCommonInit)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.ADD_FLEET, arg_33_0.onAddFleet)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.ADD_UNIT, arg_33_0.onAddUnit)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.REMOVE_UNIT, arg_33_0.onRemoveUnit)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.HIT_ENEMY, arg_33_0.onEnemyHit)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.ADD_AIR_FIGHTER_ICON, arg_33_0.onAddAirStrike)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.REMOVE_AIR_FIGHTER_ICON, arg_33_0.onRemoveAirStrike)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.UPDATE_AIR_SUPPORT_LABEL, arg_33_0.onUpdateAirSupportLabel)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.UPDATE_HOSTILE_SUBMARINE, arg_33_0.onUpdateHostileSubmarine)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.UPDATE_ENVIRONMENT_WARNING, arg_33_0.onUpdateEnvironmentWarning)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.UPDATE_COUNT_DOWN, arg_33_0.onUpdateCountDown)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.HIDE_INTERACTABLE_BUTTONS, arg_33_0.OnHideButtons)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.ADD_UI_FX, arg_33_0.OnAddUIFX)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.EDIT_CUSTOM_WARNING_LABEL, arg_33_0.onEditCustomWarning)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleEvent.GRIDMAN_SKILL_FLOAT, arg_33_0.onGridmanSkillFloat)
		arg_33_0._dataProxy.RegisterEventListener(arg_33_0, BattleCardPuzzleEvent.CARD_PUZZLE_INIT, arg_33_0.OnCardPuzzleInit)

	def RemoveUIEvent(arg_34_0):
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.COMMON_DATA_INIT_FINISH)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.STAGE_DATA_INIT_FINISH)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.ADD_FLEET)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.ADD_UNIT)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.REMOVE_UNIT)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.HIT_ENEMY)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_COUNT_DOWN)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.ADD_AIR_FIGHTER_ICON)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.REMOVE_AIR_FIGHTER_ICON)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_AIR_SUPPORT_LABEL)
		arg_34_0._cameraUtil.UnregisterEventListener(arg_34_0, BattleEvent.SHOW_PAINTING)
		arg_34_0._cameraUtil.UnregisterEventListener(arg_34_0, BattleEvent.CAMERA_FOCUS)
		arg_34_0._cameraUtil.UnregisterEventListener(arg_34_0, BattleEvent.BULLET_TIME)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.ADD_SUBMARINE_WARINING)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.REMOVE_SUBMARINE_WARINING)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_DODGEM_SCORE)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_DODGEM_COMBO)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleEvent.SHOW_BUFFER)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleUnitEvent.POINT_HIT_CHARGE)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleUnitEvent.POINT_HIT_CANCEL)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleEvent.MANUAL_SUBMARINE_SHIFT)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleEvent.FLEET_BLIND)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleEvent.FLEET_HORIZON_UPDATE)
		arg_34_0._userFleet.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_FLEET_ATTR)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_HOSTILE_SUBMARINE)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.UPDATE_ENVIRONMENT_WARNING)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.HIDE_INTERACTABLE_BUTTONS)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.ADD_UI_FX)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.EDIT_CUSTOM_WARNING_LABEL)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleEvent.GRIDMAN_SKILL_FLOAT)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleCardPuzzleEvent.CARD_PUZZLE_INIT)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleCardPuzzleEvent.UPDATE_FLEET_SHIP)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleCardPuzzleEvent.COMMON_BUTTON_ENABLE)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleCardPuzzleEvent.LONG_PRESS_BULLET_TIME)
		arg_34_0._dataProxy.UnregisterEventListener(arg_34_0, BattleCardPuzzleEvent.SHOW_CARD_DETAIL)

	def ShowSkillPainting(arg_35_0, arg_35_1, arg_35_2, arg_35_3):
		arg_35_3 = arg_35_3 or 1

		var_35_0

		if arg_35_2:
			var_35_0 = arg_35_2.cutin_cover

		arg_35_0._ui.CutInPainting(arg_35_1.GetTemplate(), arg_35_3, arg_35_1.GetIFF(), var_35_0)

	def ShowSkillFloat(arg_36_0, arg_36_1, arg_36_2, arg_36_3):
		arg_36_0._ui.SkillHrzPop(arg_36_2, arg_36_1, arg_36_3)

	def ShowSkillFloatCover(arg_37_0, arg_37_1, arg_37_2, arg_37_3):
		arg_37_0._ui.SkillHrzPopCover(arg_37_2, arg_37_1, arg_37_3)

	def SeaSurfaceShift(arg_38_0, arg_38_1, arg_38_2, arg_38_3, arg_38_4):
		var_38_0 = arg_38_3 or BattleConfig.calcInterval

		arg_38_0._seaView.ShiftSurface(arg_38_1, arg_38_2, var_38_0, arg_38_4)

	def ShowAutoBtn(arg_39_0):
		SetActive(arg_39_0._autoBtn.transform, True)

		var_39_0 = arg_39_0.GetState().GetBattleType()

		triggerToggle(arg_39_0._autoBtn, BattleState.IsAutoBotActive(var_39_0))

	def ShowTimer(arg_40_0):
		arg_40_0._timerView.SetActive(True)

	def ShowDuelBar(arg_41_0):
		arg_41_0._duelRateBar.SetActive(True)

	def ShowSimulationView(arg_42_0):
		arg_42_0._simulationBuffCountView.SetActive(True)

	def ShowPauseButton(arg_43_0, arg_43_1):
		setActive(arg_43_0._ui.findTF("PauseBtn"), arg_43_1)

	def ShowDodgemScoreBar(arg_44_0):
		arg_44_0.InitScoreBar()
		arg_44_0._dataProxy.RegisterEventListener(arg_44_0, BattleEvent.UPDATE_DODGEM_SCORE, arg_44_0.onUpdateDodgemScore)
		arg_44_0._dataProxy.RegisterEventListener(arg_44_0, BattleEvent.UPDATE_DODGEM_COMBO, arg_44_0.onUpdateDodgemCombo)
		arg_44_0._scoreBarView.UpdateScore(0)
		arg_44_0._scoreBarView.SetActive(True)

	def ShowAirFightScoreBar(arg_45_0):
		arg_45_0.InitAirFightScoreBar()
		arg_45_0._dataProxy.RegisterEventListener(arg_45_0, BattleEvent.UPDATE_DODGEM_SCORE, arg_45_0.onUpdateDodgemScore)
		arg_45_0._dataProxy.RegisterEventListener(arg_45_0, BattleEvent.UPDATE_DODGEM_COMBO, arg_45_0.onUpdateDodgemCombo)
		arg_45_0._scoreBarView.UpdateScore(0)
		arg_45_0._scoreBarView.SetActive(True)

	def onStageInit(arg_46_0, arg_46_1):
		arg_46_0.InitJoystick()
		arg_46_0.InitScene()
		arg_46_0.InitTimer()
		arg_46_0.InitEnemyHpBar()
		arg_46_0.InitAirStrikeIcon()
		arg_46_0.InitCommonWarning()
		arg_46_0.InitAutoBtn()
		arg_46_0.InitMainDamagedView()

	def onEnemyHit(arg_47_0, arg_47_1):
		var_47_0 = arg_47_1.Data

		if var_47_0.GetDiveInvisible() and not var_47_0.GetDiveDetected():
			return

		var_47_1 = arg_47_0._enemyHpBar.GetCurrentTarget()

		if var_47_1:
			if var_47_1 != var_47_0:
				arg_47_0._enemyHpBar.SwitchTarget(var_47_0, arg_47_0._dataProxy.GetUnitList())
		else:
			arg_47_0._enemyHpBar.SwitchTarget(var_47_0, arg_47_0._dataProxy.GetUnitList())

	def onEnemyHpUpdate(arg_48_0, arg_48_1):
		var_48_0 = arg_48_1.Dispatcher

		if var_48_0 == arg_48_0._enemyHpBar.GetCurrentTarget() and (not var_48_0.GetDiveInvisible() or var_48_0.GetDiveDetected()):
			arg_48_0._enemyHpBar.UpdateHpBar()

	def onPlayerMainUnitHpUpdate(arg_49_0, arg_49_1):
		if arg_49_1.Data.dHP < 0:
			arg_49_0._mainDamagedView.Play()

	def onSkillFloat(arg_50_0, arg_50_1):
		var_50_0 = arg_50_1.Data
		var_50_1 = var_50_0.coverHrzIcon
		var_50_2 = var_50_0.commander
		var_50_3 = var_50_0.skillName
		var_50_4 = arg_50_1.Dispatcher

		if var_50_1:
			arg_50_0.ShowSkillFloatCover(var_50_4, var_50_3, var_50_1)
		else:
			arg_50_0.ShowSkillFloat(var_50_4, var_50_3, var_50_2)

	def onCommonInit(arg_51_0, arg_51_1):
		arg_51_0._skillView = BattleSkillView.New(arg_51_0, arg_51_1.Data)
		arg_51_0._updateViewList[arg_51_0._skillView] = True
		arg_51_0._userFleet = arg_51_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE)

		arg_51_0._userFleet.RegisterEventListener(arg_51_0, BattleEvent.SHOW_BUFFER, arg_51_0.onShowBuffer)
		arg_51_0._userFleet.RegisterEventListener(arg_51_0, BattleUnitEvent.POINT_HIT_CHARGE, arg_51_0.onPointHitSight)
		arg_51_0._userFleet.RegisterEventListener(arg_51_0, BattleUnitEvent.POINT_HIT_CANCEL, arg_51_0.onPointHitSight)
		arg_51_0._userFleet.RegisterEventListener(arg_51_0, BattleEvent.MANUAL_SUBMARINE_SHIFT, arg_51_0.onManualSubShift)
		arg_51_0._userFleet.RegisterEventListener(arg_51_0, BattleEvent.FLEET_BLIND, arg_51_0.onFleetBlind)
		arg_51_0._userFleet.RegisterEventListener(arg_51_0, BattleEvent.UPDATE_FLEET_ATTR, arg_51_0.onFleetAttrUpdate)

		arg_51_0._sightView = BattleOpticalSightView.New(arg_51_0._ui.findTF("ChargeAreaContainer"))

		arg_51_0._sightView.SetFleetVO(arg_51_0._userFleet)

		var_51_0, var_51_1, var_51_2, var_51_3 = arg_51_0._dataProxy.GetTotalBounds()

		arg_51_0._sightView.SetAreaBound(var_51_2, var_51_3)

		if arg_51_0._dataProxy.GetInitData().ChapterBuffIDs:
			for iter_51_0, iter_51_1 in ipairs(arg_51_0._dataProxy.GetInitData().ChapterBuffIDs):
				if iter_51_1 == 9727:
					var_51_4 = True

					break

		if len(arg_51_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE).GetSupportUnitList()) > 0:
			var_51_5 = True

		if var_51_5 and not var_51_4:
			arg_51_0._airAdavantageTF = arg_51_0._airSupportTF.Find("player_advantage")
		elif var_51_4 and not var_51_5:
			arg_51_0._airAdavantageTF = arg_51_0._airSupportTF.Find("enemy_advantage")
		elif var_51_4 and var_51_5:
			arg_51_0._airAdavantageTF = arg_51_0._airSupportTF.Find("draw")

	def onAddFleet(arg_52_0, arg_52_1):
		var_52_0 = arg_52_1.Data.fleetVO

		if PlayerPrefs.GetInt(BATTLE_EXPOSE_LINE, 1) == 1:
			arg_52_0.SetFleetCloakLine(var_52_0)

	def SetFleetCloakLine(arg_53_0, arg_53_1):
		if len(arg_53_1.GetCloakList()) > 0:
			var_53_0 = arg_53_1.GetIFF()
			var_53_1 = arg_53_1.GetFleetVisionLine()
			var_53_2 = arg_53_1.GetFleetExposeLine()

			arg_53_0._seaView.SetExposeLine(var_53_0, var_53_1, var_53_2)

	def onAddUnit(arg_54_0, arg_54_1):
		var_54_0 = arg_54_1.Data.type
		var_54_1 = arg_54_1.Data.unit

		if var_54_0 == BattleConst.UnitType.PLAYER_UNIT or var_54_0 == BattleConst.UnitType.ENEMY_UNIT or var_54_0 == BattleConst.UnitType.BOSS_UNIT:
			arg_54_0.registerUnitEvent(var_54_1)

		if var_54_1.IsBoss() and arg_54_0._dataProxy.GetActiveBossCount() == 1:
			arg_54_0.AddBossWarningUI()
		elif var_54_0 == BattleConst.UnitType.ENEMY_UNIT:
			arg_54_0.registerNPCUnitEvent(var_54_1)
		elif var_54_0 == BattleConst.UnitType.PLAYER_UNIT and var_54_1.IsMainFleetUnit() and var_54_1.GetIFF() == BattleConfig.FRIENDLY_CODE:
			arg_54_0.registerPlayerMainUnitEvent(var_54_1)

		var_54_2 = var_54_1.GetTemplate().nationality

		if table.contains(BattleConfig.ALCHEMIST_AP_UI, var_54_2) and var_54_1.GetIFF() == BattleConfig.FRIENDLY_CODE:
			arg_54_0.InitAlchemistAPView()

	def onSubmarineDetected(arg_55_0, arg_55_1):
		var_55_0 = arg_55_1.Dispatcher

		if arg_55_0._enemyHpBar.GetCurrentTarget() and arg_55_0._enemyHpBar.GetCurrentTarget() == var_55_0 and var_55_0.GetDiveDetected() == False:
			arg_55_0._enemyHpBar.RemoveUnit()

	def onRemoveUnit(arg_56_0, arg_56_1):
		var_56_0 = arg_56_1.Data.unit
		var_56_1 = arg_56_1.Data.type

		if var_56_1 == BattleConst.UnitType.PLAYER_UNIT or var_56_1 == BattleConst.UnitType.ENEMY_UNIT or var_56_1 == BattleConst.UnitType.BOSS_UNIT:
			arg_56_0.unregisterUnitEvent(var_56_0)

		if var_56_1 == BattleConst.UnitType.ENEMY_UNIT and not var_56_0.IsBoss():
			arg_56_0.unregisterNPCUnitEvent(var_56_0)
		elif var_56_0.GetIFF() == BattleConfig.FRIENDLY_CODE and var_56_0.IsMainFleetUnit():
			arg_56_0.unregisterPlayerMainUnitEvent(var_56_0)

		if arg_56_1.Data.deadReason == BattleConst.UnitDeathReason.LEAVE and arg_56_0._enemyHpBar.GetCurrentTarget() and arg_56_0._enemyHpBar.GetCurrentTarget() == arg_56_1.Data.unit:
			arg_56_0._enemyHpBar.RemoveUnit(arg_56_1.Data.deadReason)

	def onUpdateCountDown(arg_57_0, arg_57_1):
		arg_57_0._timerView.SetCountDownText(arg_57_0._dataProxy.GetCountDown())

	def onUpdateDodgemScore(arg_58_0, arg_58_1):
		var_58_0 = arg_58_1.Data.totalScore

		arg_58_0._scoreBarView.UpdateScore(var_58_0)

	def onUpdateDodgemCombo(arg_59_0, arg_59_1):
		var_59_0 = arg_59_1.Data.combo

		arg_59_0._scoreBarView.UpdateCombo(var_59_0)

	def onAddAirStrike(arg_60_0, arg_60_1):
		var_60_0 = arg_60_1.Data.index
		var_60_1 = arg_60_0._dataProxy.GetAirFighterInfo(var_60_0)

		arg_60_0._airStrikeView.AppendIcon(var_60_0, var_60_1)

	def onRemoveAirStrike(arg_61_0, arg_61_1):
		var_61_0 = arg_61_1.Data.index
		var_61_1 = arg_61_0._dataProxy.GetAirFighterInfo(var_61_0)

		arg_61_0._airStrikeView.RemoveIcon(var_61_0, var_61_1)

	def onUpdateAirSupportLabel(arg_62_0, arg_62_1):
		var_62_0 = arg_62_0._dataProxy.GetAirFighterList()
		var_62_1 = 0

		for iter_62_0, iter_62_1 in ipairs(var_62_0):
			var_62_1 = var_62_1 + iter_62_1.totalNumber

		if var_62_1 == 0 or arg_62_0._warningView.GetCount() > 0:
			eachChild(arg_62_0._airSupportTF, lambda arg_63_0: setActive(arg_63_0, False))
		elif arg_62_0._airAdavantageTF:
			setActive(arg_62_0._airAdavantageTF, True)

	def onUpdateHostileSubmarine(arg_64_0, arg_64_1):
		var_64_0 = arg_64_0._dataProxy.GetEnemySubmarineCount()

		arg_64_0._warningView.UpdateHostileSubmarineCount(var_64_0)
		arg_64_0.onUpdateAirSupportLabel()

	def onUpdateEnvironmentWarning(arg_65_0, arg_65_1):
		if arg_65_1.Data.isActive:
			arg_65_0._warningView.ActiveWarning(arg_65_0._warningView.WARNING_TYPE_ARTILLERY)
		else:
			arg_65_0._warningView.DeactiveWarning(arg_65_0._warningView.WARNING_TYPE_ARTILLERY)

	def onCameraFocus(arg_66_0, arg_66_1):
		var_66_0 = arg_66_1.Data

		if var_66_0.unit != None:
			var_66_1 = var_66_0.skill or False

			arg_66_0.EnableComponent(False)
			arg_66_0.EnableSkillFloat(var_66_1)
		else:
			var_66_2 = var_66_0.duration + var_66_0.extraBulletTime

			def _func():
				arg_66_0.EnableComponent(True)
				arg_66_0.EnableSkillFloat(True)

			LeanTween.delayedCall(arg_66_0._ui._go, var_66_2, System.Action(_func)) #????

	def onShowPainting(arg_68_0, arg_68_1):
		var_68_0 = arg_68_1.Data

		arg_68_0.ShowSkillPainting(var_68_0.caster, var_68_0.skill, var_68_0.speed)

	def onBulletTime(arg_69_0, arg_69_1):
		var_69_0 = arg_69_1.Data
		var_69_1 = var_69_0.key
		var_69_2 = var_69_0.rate

		if var_69_2:
			BattleVariable.AppendMapFactor(var_69_1, var_69_2)
		else:
			BattleVariable.RemoveMapFactor(var_69_1)

		arg_69_0._seaView.UpdateSpeedScaler()

	def onShowBuffer(arg_70_0, arg_70_1):
		var_70_0 = arg_70_1.Data.dist

		arg_70_0._seaView.UpdateBufferAlpha(var_70_0)

	def onManualSubShift(arg_71_0, arg_71_1):
		var_71_0 = arg_71_1.Data.state

		arg_71_0._skillView.ShiftSubmarineManualButton(var_71_0)

	def onPointHitSight(arg_72_0, arg_72_1):
		var_72_0 = arg_72_1.ID

		if var_72_0 == BattleUnitEvent.POINT_HIT_CHARGE:
			arg_72_0._sightView.SetActive(True)

			arg_72_0._updateViewList[arg_72_0._sightView] = True
		elif var_72_0 == BattleUnitEvent.POINT_HIT_CANCEL:
			arg_72_0._sightView.SetActive(False)

			arg_72_0._updateViewList[arg_72_0._sightView] = None

	def onFleetBlind(arg_73_0, arg_73_1):
		var_73_0 = arg_73_1.Data.isBlind
		var_73_1 = arg_73_1.Dispatcher

		if not arg_73_0._inkView:
			arg_73_0.InitInkView(var_73_1)

		if var_73_0:
			var_73_2 = var_73_1.GetUnitList()

			arg_73_0._inkView.SetActive(True, var_73_2)
			arg_73_0._skillView.HideSkillButton(True)

			arg_73_0._updateViewList[arg_73_0._inkView] = True
		else:
			arg_73_0._inkView.SetActive(False)
			arg_73_0._skillView.HideSkillButton(False)

			arg_73_0._updateViewList[arg_73_0._inkView] = None

	def onFleetHorizonUpdate(arg_74_0, arg_74_1):
		if not arg_74_0._inkView:
			return

		var_74_0 = arg_74_1.Dispatcher.GetUnitList()

		arg_74_0._inkView.UpdateHollow(var_74_0)

	def onFleetAttrUpdate(arg_75_0, arg_75_1):
		if arg_75_0._alchemistAP:
			var_75_0 = arg_75_1.Dispatcher
			var_75_1 = arg_75_1.Data.attr
			var_75_2 = arg_75_1.Data.value

			if var_75_1 == arg_75_0._alchemistAP.GetAttrName():
				arg_75_0._alchemistAP.UpdateAP(var_75_2)

	def OnAddUIFX(arg_76_0, arg_76_1):
		var_76_0 = arg_76_1.Data.FXID
		var_76_1 = arg_76_1.Data.position
		var_76_2 = arg_76_1.Data.localScale
		var_76_3 = arg_76_1.Data.orderDiff

		arg_76_0.AddUIFX(var_76_3, var_76_0, var_76_1, var_76_2)

	def AddUIFX(arg_77_0, arg_77_1, arg_77_2, arg_77_3, arg_77_4):
		var_77_0 = arg_77_0._fxPool.GetFX(arg_77_2)

		arg_77_1 = arg_77_1 or 1

		var_77_1

		var_77_1 = arg_77_1 > 0

		var_77_2 = arg_77_0._ui.AddUIFX(var_77_0, arg_77_1)

		arg_77_4 = arg_77_4 or 1
		var_77_0.transform.localScale = Vector3(arg_77_4 / var_77_2.x, arg_77_4 / var_77_2.y, arg_77_4 / var_77_2.z)

		EffectMgr.GetInstance().PlayBattleEffect(var_77_0, arg_77_3, True)

	def AddBossWarningUI(arg_78_0):
		arg_78_0._dataProxy.BlockManualCast(True)

		var_78_0 = BattleResourceManager.GetInstance()

		arg_78_0._appearEffect = var_78_0.InstBossWarningUI()

		var_78_1 = arg_78_0._appearEffect.GetComponent(typeof(Animator))
		
		def Pause():
			var_78_1.speed = 0,
		def Resume():
			var_78_1.speed = 1
		var_78_2 = table(
			Pause,
			Resume
		)

		arg_78_0._state.SetTakeoverProcess(var_78_2)

		var_78_1.speed = 1 / arg_78_0._state.GetTimeScaleRate()

		setParent(arg_78_0._appearEffect, arg_78_0._ui.uiCanvas, False)
		def _func(arg_81_0):
			arg_78_0._userFleet.CoupleEncourage()
			arg_78_0._dataProxy.BlockManualCast(False)
			arg_78_0._state.ClearTakeoverProcess()
			var_78_0.DestroyOb(arg_78_0._appearEffect)

			arg_78_0._appearEffect = None

		arg_78_0._appearEffect.GetComponent(typeof(DftAniEvent)).SetEndEvent(_func) #???? Injected
		SetActive(arg_78_0._appearEffect, True)

	def OnHideButtons(arg_82_0, arg_82_1):
		var_82_0 = arg_82_1.Data.isActive

		arg_82_0._skillView.HideSkillButton(not var_82_0)
		SetActive(arg_82_0._autoBtn.transform, var_82_0)

	def onEditCustomWarning(arg_83_0, arg_83_1):
		var_83_0 = arg_83_1.Data.labelData

		arg_83_0._warningView.EditCustomWarning(var_83_0)

	def onGridmanSkillFloat(arg_84_0, arg_84_1):
		if not arg_84_0._gridmanSkillFloat:
			var_84_0 = BattleResourceManager.GetInstance().InstGridmanSkillUI()

			arg_84_0._gridmanSkillFloat = BattleGridmanSkillFloatView.New(var_84_0)

			setParent(var_84_0, arg_84_0._ui.uiCanvas, False)

		var_84_1 = arg_84_1.Data
		var_84_2 = var_84_1.type
		var_84_3 = var_84_1.IFF

		if var_84_2 == 5:
			arg_84_0._gridmanSkillFloat.DoFusionFloat(var_84_3)
		else:
			arg_84_0._gridmanSkillFloat.DoSkillFloat(var_84_2, var_84_3)

	def registerUnitEvent(arg_85_0, arg_85_1):
		arg_85_1.RegisterEventListener(arg_85_0, BattleUnitEvent.SKILL_FLOAT, arg_85_0.onSkillFloat)
		arg_85_1.RegisterEventListener(arg_85_0, BattleUnitEvent.CUT_INT, arg_85_0.onShowPainting)

	def registerNPCUnitEvent(arg_86_0, arg_86_1):
		arg_86_1.RegisterEventListener(arg_86_0, BattleUnitEvent.UPDATE_HP, arg_86_0.onEnemyHpUpdate)

		var_86_0 = arg_86_1.GetTemplate().type

		if table.contains(TeamType.SubShipType, var_86_0):
			arg_86_1.RegisterEventListener(arg_86_0, BattleUnitEvent.SUBMARINE_DETECTED, arg_86_0.onSubmarineDetected)

	def registerPlayerMainUnitEvent(arg_87_0, arg_87_1):
		arg_87_1.RegisterEventListener(arg_87_0, BattleUnitEvent.UPDATE_HP, arg_87_0.onPlayerMainUnitHpUpdate)

	def unregisterUnitEvent(arg_88_0, arg_88_1):
		arg_88_1.UnregisterEventListener(arg_88_0, BattleUnitEvent.SKILL_FLOAT)
		arg_88_1.UnregisterEventListener(arg_88_0, BattleUnitEvent.CUT_INT)

	def unregisterNPCUnitEvent(arg_89_0, arg_89_1):
		arg_89_1.UnregisterEventListener(arg_89_0, BattleUnitEvent.SKILL_FLOAT)
		arg_89_1.UnregisterEventListener(arg_89_0, BattleUnitEvent.CUT_INT)
		arg_89_1.UnregisterEventListener(arg_89_0, BattleUnitEvent.UPDATE_HP)

		var_89_0 = arg_89_1.GetTemplate().type

		if table.contains(TeamType.SubShipType, var_89_0):
			arg_89_1.UnregisterEventListener(arg_89_0, BattleUnitEvent.SUBMARINE_DETECTED)

	def unregisterPlayerMainUnitEvent(arg_90_0, arg_90_1):
		arg_90_1.UnregisterEventListener(arg_90_0, BattleUnitEvent.UPDATE_HP)

	def Dispose(arg_91_0):
		LeanTween.cancel(arg_91_0._ui._go)
		arg_91_0._uiMGR.ClearStick()

		arg_91_0._uiMGR = None

		if arg_91_0._appearEffect:
			Destroy(arg_91_0._appearEffect)

		arg_91_0.RemoveUIEvent()

		arg_91_0._updateViewList = None

		arg_91_0._timerView.Dispose()
		arg_91_0._enemyHpBar.Dispose()
		arg_91_0._skillView.Dispose()
		arg_91_0._seaView.Dispose()
		arg_91_0._airStrikeView.Dispose()
		arg_91_0._sightView.Dispose()
		arg_91_0._mainDamagedView.Dispose()
		arg_91_0._warningView.Dispose()

		arg_91_0._seaView = None
		arg_91_0._enemyHpBar = None
		arg_91_0._skillView = None
		arg_91_0._timerView = None
		arg_91_0._joystick = None
		arg_91_0._airStrikeView = None
		arg_91_0._warningView = None
		arg_91_0._mainDamagedView = None

		if arg_91_0._duelRateBar:
			arg_91_0._duelRateBar.Dispose()

			arg_91_0._duelRateBar = None

		if arg_91_0._simulationBuffCountView:
			arg_91_0._simulationBuffCountView.Dispose()

			arg_91_0._simulationBuffCountView = None

		if arg_91_0._jammingView:
			arg_91_0._jammingView.Dispose()

			arg_91_0._jammingView = None

		if arg_91_0._inkView:
			arg_91_0._inkView.Dispose()

			arg_91_0._inkView = None

		if arg_91_0._alchemistAP:
			arg_91_0._alchemistAP.Dispose()

			arg_91_0._alchemistAP = None

		if arg_91_0._gridmanSkillFloat:
			arg_91_0._gridmanSkillFloat.Dispose()

		if go(arg_91_0._ui.findTF("CardPuzzleConsole")).activeSelf:
			arg_91_0.DisposeCardPuzzleComponent()

		super().Dispose(arg_91_0)

	def OnCardPuzzleInit(arg_92_0, arg_92_1):
		arg_92_0._cardPuzzleComponent = arg_92_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE).GetCardPuzzleComponent()

		arg_92_0.ShowCardPuzzleComponent()
		arg_92_0.RegisterCardPuzzleEvent()

	def RegisterCardPuzzleEvent(arg_93_0):
		arg_93_0._cardPuzzleComponent.RegisterEventListener(arg_93_0, BattleCardPuzzleEvent.UPDATE_FLEET_SHIP, arg_93_0.onUpdateFleetShip)
		arg_93_0._cardPuzzleComponent.RegisterEventListener(arg_93_0, BattleCardPuzzleEvent.COMMON_BUTTON_ENABLE, arg_93_0.onBlockCommonButton)
		arg_93_0._cardPuzzleComponent.RegisterEventListener(arg_93_0, BattleCardPuzzleEvent.LONG_PRESS_BULLET_TIME, arg_93_0.onLongPressBulletTime)
		arg_93_0._cardPuzzleComponent.RegisterEventListener(arg_93_0, BattleCardPuzzleEvent.SHOW_CARD_DETAIL, arg_93_0.onShowCardDetail)

	def ShowCardPuzzleComponent(arg_94_0):
		setActive(arg_94_0._ui.findTF("CardPuzzleConsole"), True)
		arg_94_0.InitCardPuzzleCommonHPBar()
		arg_94_0.InitCardPuzzleEnergyBar()
		arg_94_0.IntCardPuzzleFleetHead()
		arg_94_0.InitCameraCardBoardClicker()
		arg_94_0.InitCardPuzzleMovePile()
		arg_94_0.InitCardPuzzleDeckPile()
		arg_94_0.InitCardPuzzleIconList()
		arg_94_0.InitCardPuzzleHandBoard()
		arg_94_0.InitCardPuzzleCardDetail()
		arg_94_0.InitCardPuzzleGoalRemind()

	def InitCardPuzzleCommonHPBar(arg_95_0):
		arg_95_0._cardPuzzleHPBar = CardPuzzleCommonHPBar.New(arg_95_0._ui.findTF("CardPuzzleConsole/commonHP"))

		arg_95_0._cardPuzzleHPBar.SetCardPuzzleComponent(arg_95_0._cardPuzzleComponent)

		arg_95_0._updateViewList[arg_95_0._cardPuzzleHPBar] = True

	def InitCardPuzzleEnergyBar(arg_96_0):
		arg_96_0._cardPuzzleEnergyBar = CardPuzzleEnergyBar.New(arg_96_0._ui.findTF("CardPuzzleConsole/energy_block"))

		arg_96_0._cardPuzzleEnergyBar.SetCardPuzzleComponent(arg_96_0._cardPuzzleComponent)

		arg_96_0._updateViewList[arg_96_0._cardPuzzleEnergyBar] = True

	def InitCameraCardBoardClicker(arg_97_0):
		arg_97_0._cardPuzzleBoardClicker = CardPuzzleBoardClicker.New(arg_97_0._ui.findTF("CardBoardController"))

		arg_97_0._cardPuzzleBoardClicker.SetCardPuzzleComponent(arg_97_0._cardPuzzleComponent)

	def IntCardPuzzleFleetHead(arg_98_0):
		arg_98_0._cardPuzzleFleetHead = CardPuzzleFleetHead.New(arg_98_0._ui.findTF("CardPuzzleConsole/fleet"))

		arg_98_0._cardPuzzleFleetHead.SetCardPuzzleComponent(arg_98_0._cardPuzzleComponent)

	def InitCardPuzzleMovePile(arg_99_0):
		arg_99_0._cardPuzzleMovePile = CardPuzzleMovePile.New(arg_99_0._ui.findTF("CardPuzzleConsole/movedeck"))

		arg_99_0._cardPuzzleMovePile.SetCardPuzzleComponent(arg_99_0._cardPuzzleComponent)

		arg_99_0._updateViewList[arg_99_0._cardPuzzleMovePile] = True

	def InitCardPuzzleDeckPile(arg_100_0):
		arg_100_0._cardPuzzleDeckPile = CardPuzzleDeckPool.New(arg_100_0._ui.findTF("CardPuzzleConsole/deck"))

		arg_100_0._cardPuzzleDeckPile.SetCardPuzzleComponent(arg_100_0._cardPuzzleComponent)

	def InitCardPuzzleIconList(arg_101_0):
		arg_101_0._cardPuzzleStatusIcon = CardPuzzleFleetIconList.New(arg_101_0._ui.findTF("CardPuzzleConsole/statusIcon"))

		arg_101_0._cardPuzzleStatusIcon.SetCardPuzzleComponent(arg_101_0._cardPuzzleComponent)

		arg_101_0._updateViewList[arg_101_0._cardPuzzleStatusIcon] = True

	def InitCardPuzzleHandBoard(arg_102_0):
		arg_102_0._cardPuzzleHandBoard = CardPuzzleHandBoard.New(arg_102_0._ui.findTF("CardPuzzleConsole/cardboard"), arg_102_0._ui.findTF("CardPuzzleConsole/hand"))

		arg_102_0._cardPuzzleHandBoard.SetCardPuzzleComponent(arg_102_0._cardPuzzleComponent)

		arg_102_0._updateViewList[arg_102_0._cardPuzzleHandBoard] = True

	def InitCardPuzzleGoalRemind(arg_103_0):
		arg_103_0._cardPuzzleGoalRemind = CardPuzzleGoalRemind.New(arg_103_0._ui.findTF("CardPuzzleConsole/goal"))

		arg_103_0._cardPuzzleGoalRemind.SetCardPuzzleComponent(arg_103_0._cardPuzzleComponent)

	def InitCardPuzzleCardDetail(arg_104_0):
		arg_104_0._cardPuzzleCardDetail = CardPuzzleCardDetail.New(arg_104_0._ui.findTF("CardPuzzleConsole/cardDetail"))

	def DisposeCardPuzzleComponent(arg_105_0):
		arg_105_0._cardPuzzleHPBar.Dispose()
		arg_105_0._cardPuzzleEnergyBar.Dispose()
		arg_105_0._cardPuzzleBoardClicker.Dispose()
		arg_105_0._cardPuzzleFleetHead.Dispose()
		arg_105_0._cardPuzzleMovePile.Dispose()
		arg_105_0._cardPuzzleDeckPile.Dispose()
		arg_105_0._cardPuzzleStatusIcon.Dispose()
		arg_105_0._cardPuzzleHandBoard.Dispose()
		arg_105_0._cardPuzzleGoalRemind.Dispose()
		arg_105_0._cardPuzzleCardDetail.Dispose()

	def onUpdateFleetBuff(arg_106_0):
		return

	def onUpdateFleetShip(arg_107_0, arg_107_1):
		arg_107_0._cardPuzzleFleetHead.UpdateShipIcon(arg_107_1.Data.teamType)

	def onBlockCommonButton(arg_108_0, arg_108_1):
		var_108_0 = arg_108_1.Data.flag

		arg_108_0.EnableComponent(var_108_0)

	def onLongPressBulletTime(arg_109_0, arg_109_1):
		var_109_0 = arg_109_1.Data.timeScale

		arg_109_0._state.ScaleTimer(var_109_0)

	def onShowCardDetail(arg_110_0, arg_110_1):
		var_110_0 = arg_110_1.Data.card

		if var_110_0:
			arg_110_0._cardPuzzleCardDetail.Active(True)
			arg_110_0._cardPuzzleCardDetail.SetReferenceCard(var_110_0)
		else:
			arg_110_0._cardPuzzleCardDetail.Active(False)
