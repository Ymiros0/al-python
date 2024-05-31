ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleManualWeaponAutoBot = class("BattleManualWeaponAutoBot")
var_0_0.Battle.BattleManualWeaponAutoBot.__name = "BattleManualWeaponAutoBot"

local var_0_3 = var_0_0.Battle.BattleManualWeaponAutoBot

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._fleetVO = arg_1_1

	arg_1_0.init(arg_1_1)

def var_0_3.init(arg_2_0):
	arg_2_0._active = False
	arg_2_0._isPlayFocus = True
	arg_2_0._chargeVO = arg_2_0._fleetVO.GetChargeWeaponVO()
	arg_2_0._torpedoVO = arg_2_0._fleetVO.GetTorpedoWeaponVO()
	arg_2_0._AAVO = arg_2_0._fleetVO.GetAirAssistVO()
	arg_2_0._totalTime = 0
	arg_2_0._lastActiveTimeStamp = None

def var_0_3.Update(arg_3_0):
	if arg_3_0._active:
		if not arg_3_0._torpedoVO.IsOverLoad():
			arg_3_0._fleetVO.QuickCastTorpedo()

			return

		if not arg_3_0._AAVO.IsOverLoad():
			arg_3_0._fleetVO.UnleashAllInStrike()

			return

		if not arg_3_0._chargeVO.IsOverLoad():
			arg_3_0._fleetVO.QuickTagChrageWeapon(arg_3_0._isPlayFocus)

			return

def var_0_3.IsActive(arg_4_0):
	return arg_4_0._active

def var_0_3.SetActive(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_0._active != arg_5_1 and arg_5_1 == True:
		arg_5_0._lastActiveTimeStamp = pg.TimeMgr.GetInstance().GetCombatTime()
	elif arg_5_0._active != arg_5_1 and arg_5_1 == False and arg_5_0._lastActiveTimeStamp != None:
		local var_5_0 = pg.TimeMgr.GetInstance().GetCombatTime()

		arg_5_0._totalTime = arg_5_0._totalTime + (var_5_0 - arg_5_0._lastActiveTimeStamp)
		arg_5_0._lastActiveTimeStamp = None

	arg_5_0._fleetVO.AutoBotUpdated(arg_5_1)

	arg_5_0._active = arg_5_1
	arg_5_0._isPlayFocus = arg_5_2

def var_0_3.GetTotalActiveDuration(arg_6_0):
	if arg_6_0._lastActiveTimeStamp:
		local var_6_0 = pg.TimeMgr.GetInstance().GetCombatTime()

		arg_6_0._totalTime = arg_6_0._totalTime + (var_6_0 - arg_6_0._lastActiveTimeStamp)
		arg_6_0._lastActiveTimeStamp = None

	return arg_6_0._totalTime

def var_0_3.Dispose(arg_7_0):
	arg_7_0._chargeVO = None
	arg_7_0._torpedoVO = None
	arg_7_0._AAVO = None
	arg_7_0._dataProxy = None
	arg_7_0._uiMediator = None

	var_0_0.EventListener.DetachEventListener(arg_7_0)
