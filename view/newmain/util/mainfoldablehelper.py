local var_0_0 = class("MainFoldableHelper")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0.foldPosition = arg_1_0.InitFoldPositions(arg_1_2)

def var_0_0.IsInit(arg_2_0):
	return arg_2_0._tf != None

def var_0_0.InitFoldPositions(arg_3_0, arg_3_1):
	if not arg_3_0.IsInit():
		return None

	local var_3_0 = arg_3_0._tf.anchoredPosition
	local var_3_1 = 1500
	local var_3_2 = 200
	local var_3_3 = var_3_0.x
	local var_3_4 = 0
	local var_3_5 = var_3_0.y
	local var_3_6 = 0

	if arg_3_1.x > 0:
		var_3_4 = var_3_0.x + var_3_1
	elif arg_3_1.x < 0:
		var_3_4 = var_3_0.x - var_3_1

	if arg_3_1.y > 0:
		var_3_6 = var_3_0.y + var_3_2
	elif arg_3_1.y < 0:
		var_3_6 = var_3_0.y - var_3_2

	return Vector4(var_3_3, var_3_4, var_3_5, var_3_6)

def var_0_0.Fold(arg_4_0, arg_4_1, arg_4_2):
	if not arg_4_0.IsInit():
		return

	LeanTween.cancel(arg_4_0._tf.gameObject)

	local var_4_0 = arg_4_0.foldPosition

	if var_4_0.y != 0:
		local var_4_1 = arg_4_1 and Vector2(var_4_0.x, var_4_0.y) or Vector2(var_4_0.y, var_4_0.x)

		arg_4_0.LeanTweenValue(var_4_1, arg_4_2, True)

	if var_4_0.w != 0:
		local var_4_2 = arg_4_1 and Vector2(var_4_0.z, var_4_0.w) or Vector2(var_4_0.w, var_4_0.z)

		arg_4_0.LeanTweenValue(var_4_2, arg_4_2, False)

def var_0_0.LeanTweenValue(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local function var_5_0(arg_6_0)
		if arg_5_3:
			setAnchoredPosition(arg_5_0._tf.gameObject, {
				x = arg_6_0
			})
		else
			setAnchoredPosition(arg_5_0._tf.gameObject, {
				y = arg_6_0
			})

	if arg_5_2 <= 0:
		var_5_0(arg_5_1.y)

		return

	LeanTween.value(arg_5_0._tf.gameObject, arg_5_1.x, arg_5_1.y, arg_5_2).setOnUpdate(System.Action_float(var_5_0)).setEase(LeanTweenType.easeInOutExpo)

def var_0_0.Dispose(arg_7_0):
	if not arg_7_0.IsInit():
		return None

	LeanTween.cancel(arg_7_0._tf.gameObject)

return var_0_0
