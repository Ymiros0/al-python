ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleCardPuzzleFleetBuffEffect = class("BattleCardPuzzleFleetBuffEffect")
var_0_0.Battle.BattleCardPuzzleFleetBuffEffect.__name = "BattleCardPuzzleFleetBuffEffect"

local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleFleetBuffEffect

var_0_2.FX_TYPE_NOR = 0
var_0_2.FX_TYPE_MOD_ATTR = 1

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tempData = Clone(arg_1_1)
	arg_1_0._type = arg_1_0._tempData.type

	arg_1_0.SetActive()

def var_0_2.GetEffectType(arg_2_0):
	return var_0_2.FX_TYPE_NOR

def var_0_2.SetArgs(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0._cardPuzzleComponent = arg_3_1
	arg_3_0._fleetBuff = arg_3_2

def var_0_2.Trigger(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0[arg_4_1](arg_4_0, arg_4_2)

def var_0_2.onAttach(arg_5_0):
	arg_5_0.onTrigger()

def var_0_2.onRemove(arg_6_0):
	arg_6_0.onTrigger()

def var_0_2.onUpdate(arg_7_0, arg_7_1):
	if arg_7_0._tempData.arg_list.INR:
		local var_7_0 = arg_7_0._tempData.arg_list.INR

		if not arg_7_0._lastTimeStamp or var_7_0 < arg_7_1 - arg_7_0._lastTimeStamp:
			arg_7_0.onTrigger()

			arg_7_0._lastTimeStamp = arg_7_1
	else
		arg_7_0.onTrigger()

def var_0_2.onPlus(arg_8_0):
	arg_8_0.onTrigger()

def var_0_2.onDeduct(arg_9_0):
	arg_9_0.onTrigger()

def var_0_2.onStartGame(arg_10_0):
	arg_10_0.onTrigger()

def var_0_2.IsActive(arg_11_0):
	return arg_11_0._isActive

def var_0_2.SetActive(arg_12_0):
	arg_12_0._isActive = True

def var_0_2.NotActive(arg_13_0):
	arg_13_0._isActive = False

def var_0_2.Clear(arg_14_0):
	return

def var_0_2.Dispose(arg_15_0):
	return
