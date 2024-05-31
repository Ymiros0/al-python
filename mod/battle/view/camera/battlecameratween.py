ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleCameraTween = class("BattleCameraTween")
var_0_0.Battle.BattleCameraTween.__name = "BattleCameraTween"

local var_0_3 = var_0_0.Battle.BattleCameraTween

def var_0_3.Ctor(arg_1_0):
	arg_1_0._point = Vector3.zero

def var_0_3.SetFromTo(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5, arg_2_6, arg_2_7):
	arg_2_0._point.Set(arg_2_2.x, arg_2_2.y, arg_2_2.z)

	local var_2_0 = LeanTween.value(go(arg_2_1), arg_2_2, arg_2_3, arg_2_4).setOnUpdateVector3(System.Action_UnityEngine_Vector3(function(arg_3_0)
		arg_2_0._point.Set(arg_3_0.x, arg_3_0.y, arg_3_0.z)))

	if arg_2_5 and arg_2_5 != 0:
		var_2_0.setDelay(arg_2_5)

	if arg_2_6:
		var_2_0.setEase(LeanTweenType.easeOutExpo)

	if arg_2_7:
		var_2_0.setOnComplete(System.Action(function()
			arg_2_7()))

def var_0_3.GetCameraPos(arg_5_0):
	return arg_5_0._point

def var_0_3.Dispose(arg_6_0):
	arg_6_0._point = None
