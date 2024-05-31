local var_0_0 = class("CourtYardFurnitureAnimatorAgent", import(".CourtYardAgent"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.maskSpineAnimUIs = {}

	for iter_1_0, iter_1_1 in pairs(arg_1_0.masks):
		local var_1_0 = GetOrAddComponent(iter_1_1.Find("spine"), typeof(SpineAnimUI))

		table.insert(arg_1_0.maskSpineAnimUIs, var_1_0)

	arg_1_0.spineTF = arg_1_0._tf.Find("spine_icon")
	arg_1_0.spineAnimUI = GetOrAddComponent(arg_1_0.spineTF.Find("spine"), typeof(SpineAnimUI))

	arg_1_0.SetState(CourtYardFurniture.STATE_IDLE)

def var_0_0.State2Action(arg_2_0, arg_2_1):
	if arg_2_1 == CourtYardFurniture.STATE_IDLE:
		return arg_2_0.data.GetFirstSlot().GetSpineDefaultAction(), True
	elif arg_2_1 == CourtYardFurniture.STATE_TOUCH:
		return arg_2_0.data.GetTouchAction()
	elif arg_2_1 == CourtYardFurniture.STATE_TOUCH_PREPARE:
		return arg_2_0.data.GetTouchPrepareAction()
	elif arg_2_1 == CourtYardFurniture.STATE_PLAY_MUSIC:
		return arg_2_0.data.GetMusicData().action, True

def var_0_0.SetState(arg_3_0, arg_3_1):
	local var_3_0, var_3_1 = arg_3_0.State2Action(arg_3_1)

	if not var_3_0 or var_3_0 == "":
		return

	arg_3_0._PlayAction(var_3_0, var_3_1, function()
		arg_3_0.OnAnimtionFinish(arg_3_1))

	if arg_3_1 == CourtYardFurniture.STATE_IDLE:
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.maskSpineAnimUIs):
			iter_3_1.SetAction(var_3_0, 0)

def var_0_0.GetNormalAnimationName(arg_5_0):
	return arg_5_0.State2Action(CourtYardFurniture.STATE_IDLE)

def var_0_0.RestartAnimation(arg_6_0, arg_6_1):
	arg_6_0.spineAnimUI.SetAction(arg_6_1, 0)

def var_0_0._PlayAction(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = not arg_7_2 and function(arg_8_0)
		if arg_8_0 == "finish":
			arg_7_0.spineAnimUI.SetActionCallBack(None)
			arg_7_3() or None

	arg_7_0.spineAnimUI.SetActionCallBack(var_7_0)
	arg_7_0.spineAnimUI.SetAction(arg_7_1, 0)

def var_0_0.PlayInteractioAnim(arg_9_0, arg_9_1):
	parallelAsync({
		function(arg_10_0)
			arg_9_0.PlayMaskAction(arg_9_1, arg_10_0),
		function(arg_11_0)
			arg_9_0._PlayAction(arg_9_1, False, arg_11_0)
	}, function()
		arg_9_0.OnAnimtionFinish(CourtYardFurniture.STATE_INTERACT))

def var_0_0.PlayMaskAction(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in ipairs(arg_13_0.maskSpineAnimUIs):
		table.insert(var_13_0, function(arg_14_0)
			iter_13_1.SetActionCallBack(function(arg_15_0)
				if arg_15_0 == "finish":
					iter_13_1.SetActionCallBack(None)
					arg_14_0())
			iter_13_1.SetAction(arg_13_1, 0))

	parallelAsync(var_13_0, arg_13_2)

def var_0_0.Dispose(arg_16_0):
	arg_16_0.spineAnimUI.SetActionCallBack(None)
	Object.Destroy(arg_16_0.spineAnimUI)

	arg_16_0.spineAnimUI = None

	Object.Destroy(arg_16_0.spineTF.gameObject)

	arg_16_0.spineTF = None

	for iter_16_0, iter_16_1 in ipairs(arg_16_0.maskSpineAnimUIs):
		iter_16_1.SetActionCallBack(None)
		Object.Destroy(iter_16_1)

	arg_16_0.maskSpineAnimUIs = None

	var_0_0.super.Dispose()

return var_0_0
