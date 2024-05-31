local var_0_0 = class("CommanderPaintingUtil")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.rect = arg_1_1.parent.rect

	local var_1_0 = arg_1_1.parent.parent.Find("background")

	arg_1_0._tf = arg_1_1
	arg_1_0.zoomDelegate = GetOrAddComponent(arg_1_1, "MultiTouchZoom")
	arg_1_0.dragDelegate = GetOrAddComponent(arg_1_1, "EventTriggerListener")
	arg_1_0.initPosition = arg_1_0._tf.localPosition

def var_0_0.Fold(arg_2_0):
	arg_2_0.zoomDelegate.SetZoomTarget(arg_2_0._tf)

	arg_2_0.zoomDelegate.enabled = True
	arg_2_0.dragDelegate.enabled = True

	LeanTween.move(rtf(arg_2_0._tf), Vector3.zero, 0.5)

	local var_2_0 = arg_2_0._tf.Find("fitter").GetChild(0)

	if var_2_0:
		var_2_0.GetComponent(typeof(Image)).raycastTarget = True

	local var_2_1 = arg_2_0._tf
	local var_2_2 = var_2_1.anchoredPosition.x
	local var_2_3 = var_2_1.anchoredPosition.y
	local var_2_4 = var_2_1.rect.width
	local var_2_5 = var_2_1.rect.height
	local var_2_6 = arg_2_0.rect.width / UnityEngine.Screen.width
	local var_2_7 = arg_2_0.rect.height / UnityEngine.Screen.height
	local var_2_8 = var_2_4 / 2
	local var_2_9 = var_2_5 / 2
	local var_2_10
	local var_2_11
	local var_2_12 = True
	local var_2_13 = False

	arg_2_0.dragDelegate.AddPointDownFunc(function(arg_3_0)
		if Input.touchCount == 1 or IsUnityEditor:
			var_2_13 = True
			var_2_12 = True
		elif Input.touchCount >= 2:
			var_2_12 = False
			var_2_13 = False)
	arg_2_0.dragDelegate.AddPointUpFunc(function(arg_4_0)
		if Input.touchCount <= 2:
			var_2_12 = True)
	arg_2_0.dragDelegate.AddBeginDragFunc(function(arg_5_0, arg_5_1)
		var_2_13 = False
		var_2_10 = arg_5_1.position.x * var_2_6 - var_2_8 - var_2_1.localPosition.x
		var_2_11 = arg_5_1.position.y * var_2_7 - var_2_9 - var_2_1.localPosition.y)
	arg_2_0.dragDelegate.AddDragFunc(function(arg_6_0, arg_6_1)
		if var_2_12:
			local var_6_0 = arg_2_0._tf.localPosition

			arg_2_0._tf.localPosition = Vector3(arg_6_1.position.x * var_2_6 - var_2_8 - var_2_10, arg_6_1.position.y * var_2_7 - var_2_9 - var_2_11, -22))

def var_0_0.UnFold(arg_7_0):
	LeanTween.move(rtf(arg_7_0._tf), arg_7_0.initPosition, 0.5)

	arg_7_0.zoomDelegate.enabled = False
	arg_7_0.dragDelegate.enabled = False

	arg_7_0.dragDelegate.AddPointDownFunc(None)
	arg_7_0.dragDelegate.AddPointUpFunc(None)
	arg_7_0.dragDelegate.AddBeginDragFunc(None)
	arg_7_0.dragDelegate.AddDragFunc(None)

	local var_7_0 = arg_7_0._tf.Find("fitter").GetChild(0)

	if var_7_0:
		var_7_0.GetComponent(typeof(Image)).raycastTarget = False

def var_0_0.Dispose(arg_8_0):
	arg_8_0.UnFold()

return var_0_0
