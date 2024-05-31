ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = class("BattleCustomWarningLabel")

var_0_0.Battle.BattleCustomWarningLabel = var_0_2
var_0_2.__name = "BattleCustomWarningLabel"

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._expire = False

def var_0_2.ConfigData(arg_2_0, arg_2_1):
	setText(arg_2_0._tf.Find("text"), i18n(arg_2_1.dialogue))

	arg_2_0._duration = arg_2_1.duration

	local var_2_0 = (arg_2_1.x + 1) * 0.5
	local var_2_1 = (arg_2_1.y + 1) * 0.5

	arg_2_0._tf.anchorMin = Vector2(var_2_0, var_2_1)
	arg_2_0._tf.anchorMax = Vector2(var_2_0, var_2_1)
	arg_2_0._startTimeStamp = pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_2.GetDuration(arg_3_0):
	return arg_3_0._duration

def var_0_2.SetExpire(arg_4_0):
	arg_4_0._expire = True

def var_0_2.IsExpire(arg_5_0):
	return arg_5_0._expire

def var_0_2.Update(arg_6_0):
	if arg_6_0._duration > 0 and pg.TimeMgr.GetInstance().GetCombatTime() - arg_6_0._startTimeStamp > arg_6_0._duration:
		arg_6_0.SetExpire()

def var_0_2.Dispose(arg_7_0):
	Destroy(arg_7_0._go)

	arg_7_0._go = None
	arg_7_0._tf = None
