local var_0_0 = class("CourtYardCalcUtil")
local var_0_1 = 78.2
local var_0_2 = 39

def var_0_0.Screen2Local(arg_1_0, arg_1_1):
	local var_1_0 = GameObject.Find("UICamera").GetComponent("Camera")
	local var_1_1 = arg_1_0.GetComponent("RectTransform")

	return (LuaHelper.ScreenToLocal(var_1_1, arg_1_1, var_1_0))

def var_0_0.Map2Local(arg_2_0):
	local var_2_0 = (arg_2_0.x - arg_2_0.y) * (var_0_1 / 2)
	local var_2_1 = (arg_2_0.x + arg_2_0.y) * (var_0_2 / 2)

	return Vector2(var_2_0, var_2_1)

def var_0_0.Local2Map(arg_3_0):
	local var_3_0 = math.floor(arg_3_0.x / var_0_1 + arg_3_0.y / var_0_2)
	local var_3_1 = math.floor(arg_3_0.y / var_0_2 - arg_3_0.x / var_0_1)

	return Vector2(var_3_0, var_3_1)

def var_0_0.World2Local(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.InverseTransformPoint(arg_4_1)

	return Vector3(var_4_0.x, var_4_0.y, 0)

def var_0_0.local2RelativeLocal(arg_5_0, arg_5_1, arg_5_2):
	return arg_5_0 + var_0_0.Map2Local(Vector2(arg_5_1, arg_5_2))

def var_0_0.TrPosition2LocalPos(arg_6_0, arg_6_1, arg_6_2):
	if arg_6_0 == arg_6_1:
		return arg_6_2
	else
		local var_6_0 = arg_6_0.TransformPoint(arg_6_2)
		local var_6_1 = arg_6_1.InverseTransformPoint(var_6_0)

		return Vector3(var_6_1.x, var_6_1.y, 0)

def var_0_0.IsHappen(arg_7_0):
	return arg_7_0 >= math.random(0, 100)

def var_0_0.HalfProbability():
	return var_0_0.IsHappen(50)

def var_0_0.GetSign(arg_9_0):
	if arg_9_0 <= 0:
		return -1
	else
		return 1

def var_0_0.GetTransformSign(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0
	local var_10_1 = arg_10_1.localScale.x * arg_10_0.localScale.x

	while var_10_0.parent != arg_10_1:
		var_10_0 = var_10_0.parent
		var_10_1 = var_10_1 * var_10_0.localScale.x

	return var_0_0.GetSign(var_10_1)

return var_0_0
