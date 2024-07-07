from packages.luatable import pairs

import BattleEvent
from Framework.base.mvc.Command import Command
from mod.battle.BattleState import BattleState
from mod.battle.data import BattleConfig
from mod.battle.data.BattleDataProxy import BattleDataProxy
from mod.battle.data.vo.BattleManualWeaponAutoBot import BattleManualWeaponAutoBot #!
from mod.battle.data.vo.BattleJoyStickAutoBot import BattleJoyStickAutoBot #!
from mod.battle.view.camera.BattleCameraUtil import BattleCameraUtil #!

class BattleControllerWeaponCommand(Command):
	__name = "BattleControllerWeaponCommand"

	def Initialize(arg_2_0):
		super.Initialize(arg_2_0)

		arg_2_0._dataProxy = arg_2_0._state.GetProxyByName(BattleDataProxy.__name)

		arg_2_0.InitBattleEvent()

		arg_2_0._focusBlockCast = False

	def ActiveBot(arg_3_0, arg_3_1, arg_3_2):
		arg_3_0._manualWeaponAutoBot.SetActive(arg_3_1, arg_3_2)
		arg_3_0._joyStickAutoBot.SetActive(arg_3_1)

	def TryAutoSub(arg_4_0):
		var_4_0 = arg_4_0.GetState().GetBattleType()

		if BattleState.IsAutoSubActive(var_4_0):
			var_4_1 = arg_4_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE)._submarineVO

			if var_4_1.GetUseable() and var_4_1.GetCount() > 0:
				arg_4_0._dataProxy.SubmarineStrike(BattleConfig.FRIENDLY_CODE)
				var_4_1.Cast()

	def GetWeaponBot(arg_5_0):
		return arg_5_0._manualWeaponAutoBot

	def GetBotActiveDuration(arg_6_0):
		return arg_6_0._manualWeaponAutoBot.GetTotalActiveDuration()

	def GetStickBot(arg_7_0):
		return arg_7_0._joyStickAutoBot

	def InitBattleEvent(arg_8_0):
		arg_8_0._dataProxy.RegisterEventListener(arg_8_0, BattleEvent.COMMON_DATA_INIT_FINISH, arg_8_0.onUnitInitFinish)
		arg_8_0._dataProxy.RegisterEventListener(arg_8_0, BattleEvent.JAMMING, arg_8_0.onJamming)

	def Update(arg_9_0, arg_9_1):
		if arg_9_0._jammingFlag:
			return

		if not arg_9_0._focusBlockCast:
			arg_9_0._manualWeaponAutoBot.Update()

		for iter_9_0, iter_9_1 in pairs(arg_9_0._fleetList):
			iter_9_1.UpdateManualWeaponVO(arg_9_1)

	def onJamming(arg_10_0, arg_10_1):
		arg_10_0._jammingFlag = arg_10_1.Data.jammingFlag

	def onUnitInitFinish(arg_11_0, arg_11_1):
		arg_11_0._fleetList = arg_11_0._dataProxy.GetFleetList()

		var_11_0 = arg_11_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE)

		var_11_0.RegisterEventListener(arg_11_0, BattleEvent.REFRESH_FLEET_FORMATION, arg_11_0.onFleetFormationUpdate)
		var_11_0.RegisterEventListener(arg_11_0, BattleEvent.OVERRIDE_AUTO_BOT, arg_11_0.onOverrideAutoBot)

		arg_11_0._manualWeaponAutoBot = BattleManualWeaponAutoBot.New(var_11_0)
		arg_11_0._joyStickAutoBot = BattleJoyStickAutoBot.New(arg_11_0._dataProxy, var_11_0)

		BattleCameraUtil.GetInstance().RegisterEventListener(arg_11_0, BattleEvent.CAMERA_FOCUS, arg_11_0.onCameraFocus)

	def onFleetFormationUpdate(arg_12_0, arg_12_1):
		arg_12_0._joyStickAutoBot.FleetFormationUpdate()

	def onOverrideAutoBot(arg_13_0, arg_13_1):
		arg_13_0._joyStickAutoBot.SwitchStrategy(BattleJoyStickAutoBot.AUTO_PILOT)

	def onCameraFocus(arg_14_0, arg_14_1):
		var_14_0 = arg_14_1.Data

		if var_14_0.unit != None:
			arg_14_0._focusBlockCast = True
		else:
			var_14_1 = var_14_0.duration + var_14_0.extraBulletTime

			LeanTween.delayedCall(var_14_1, System.Action(lambda: setattr(arg_14_0,'_focusBlockCast', False))) #????

	def Dispose(arg_16_0):
		var_16_0 = arg_16_0._dataProxy.GetFleetByIFF(BattleConfig.FRIENDLY_CODE)

		var_16_0.UnregisterEventListener(arg_16_0, BattleEvent.REFRESH_FLEET_FORMATION)
		var_16_0.UnregisterEventListener(arg_16_0, BattleEvent.OVERRIDE_AUTO_BOT)
		arg_16_0._dataProxy.UnregisterEventListener(arg_16_0, BattleEvent.COMMON_DATA_INIT_FINISH)
		BattleCameraUtil.GetInstance().UnregisterEventListener(arg_16_0, BattleEvent.CAMERA_FOCUS)
		arg_16_0._joyStickAutoBot.Dispose()

		arg_16_0._joyStickAutoBot = None

		arg_16_0._manualWeaponAutoBot.Dispose()

		arg_16_0._manualWeaponAutoBot = None

		super.Dispose(arg_16_0)
