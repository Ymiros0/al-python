ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleSubmarineFuncVO = class("BattleSubmarineFuncVO")
var_0_0.Battle.BattleSubmarineFuncVO.__name = "BattleSubmarineFuncVO"

local var_0_3 = var_0_0.Battle.BattleSubmarineFuncVO

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)

	arg_1_0._current = arg_1_1
	arg_1_0._defaultMax = arg_1_1
	arg_1_0._active = True

	arg_1_0.ResetMax()

def var_0_3.Update(arg_2_0, arg_2_1):
	if arg_2_0._active and arg_2_0._current < arg_2_0._max:
		local var_2_0 = arg_2_1 - arg_2_0._reloadStartTime

		if var_2_0 >= arg_2_0._max:
			arg_2_0.ResetMax()

			arg_2_0._current = arg_2_0._max
			arg_2_0._reloadStartTime = None

			arg_2_0.DispatchOverLoadChange()
		else
			arg_2_0._current = var_2_0

def var_0_3.SetActive(arg_3_0, arg_3_1):
	arg_3_0._active = arg_3_1

def var_0_3.ResetCurrent(arg_4_0):
	arg_4_0._current = 0
	arg_4_0._reloadStartTime = pg.TimeMgr.GetInstance().GetCombatTime()

	arg_4_0.DispatchOverLoadChange()

def var_0_3.ResetMax(arg_5_0):
	arg_5_0._max = arg_5_0._defaultMax

def var_0_3.SetMax(arg_6_0, arg_6_1):
	arg_6_0._max = arg_6_1

def var_0_3.GetMax(arg_7_0):
	return arg_7_0._max

def var_0_3.GetTotal(arg_8_0):
	return 0

def var_0_3.GetCurrent(arg_9_0):
	return arg_9_0._current

def var_0_3.IsOverLoad(arg_10_0):
	return arg_10_0._current < arg_10_0._max

def var_0_3.DispatchOverLoadChange(arg_11_0):
	local var_11_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE)

	arg_11_0.DispatchEvent(var_11_0)

def var_0_3.Dispose(arg_12_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_12_0._focusTimer)

	arg_12_0._focusTimer = None

	var_0_0.EventDispatcher.DetachEventDispatcher(arg_12_0)
