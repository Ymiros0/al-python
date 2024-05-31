ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSubmarineFuncButton", var_0_0.Battle.BattleWeaponButton)

var_0_0.Battle.BattleSubmarineFuncButton = var_0_1
var_0_1.__name = "BattleSubmarineFuncButton"

def var_0_1.Ctor(arg_1_0):
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0.eventTriggers = {}

def var_0_1.OnfilledEffect(arg_2_0):
	SetActive(arg_2_0._filledEffect, True)

def var_0_1.SetProgressInfo(arg_3_0, arg_3_1):
	arg_3_0._progressInfo = arg_3_1

	arg_3_0._progressInfo.RegisterEventListener(arg_3_0, var_0_0.Battle.BattleEvent.WEAPON_COUNT_PLUS, arg_3_0.OnfilledEffect)
	arg_3_0._progressInfo.RegisterEventListener(arg_3_0, var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE, arg_3_0.OnOverLoadChange)
	arg_3_0.OnOverLoadChange()
	arg_3_0.SetControllerActive(True)

def var_0_1.Update(arg_4_0):
	if arg_4_0._progressInfo.GetCurrent() < arg_4_0._progressInfo.GetMax():
		arg_4_0.updateProgressBar()

def var_0_1.Dispose(arg_5_0):
	if arg_5_0.eventTriggers:
		for iter_5_0, iter_5_1 in pairs(arg_5_0.eventTriggers):
			ClearEventTrigger(iter_5_0)

		arg_5_0.eventTriggers = None

	arg_5_0._progress = None
	arg_5_0._progressBar = None

	arg_5_0._progressInfo.UnregisterEventListener(arg_5_0, var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE)
	arg_5_0._progressInfo.UnregisterEventListener(arg_5_0, var_0_0.Battle.BattleEvent.WEAPON_COUNT_PLUS)
	var_0_0.EventListener.DetachEventListener(arg_5_0)
