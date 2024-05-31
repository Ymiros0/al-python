local var_0_0 = class("EffectRedDotNode", import(".RedDotNode"))

def var_0_0.SetData(arg_1_0, arg_1_1):
	if IsNil(arg_1_0.gameObject) or not isActive(arg_1_0.gameObject):
		return

	local var_1_0

	if arg_1_0.gameObject.childCount > 0:
		var_1_0 = arg_1_0.gameObject.GetChild(0)

	if var_1_0:
		setActive(var_1_0, arg_1_1)

	local var_1_1 = arg_1_0.gameObject.Find("tip")

	if var_1_1:
		setActive(var_1_1, arg_1_1)

		if arg_1_1:
			arg_1_0.StartAnimation(var_1_1)

def var_0_0.StartAnimation(arg_2_0, arg_2_1):
	arg_2_0.RemoveTimer()

	local var_2_0 = arg_2_1.GetComponent(typeof(Animator))

	var_2_0.enabled = True
	arg_2_0.timer = Timer.New(function()
		if not var_2_0:
			return

		var_2_0.enabled = False
		var_2_0.gameObject.transform.localEulerAngles = Vector3.zero, 5, 1)

	arg_2_0.timer.Start()

def var_0_0.RemoveTimer(arg_4_0):
	if arg_4_0.timer:
		arg_4_0.timer.Stop()

		arg_4_0.timer = None

def var_0_0.Remove(arg_5_0):
	arg_5_0.RemoveTimer()

def var_0_0.Puase(arg_6_0):
	arg_6_0.RemoveTimer()

return var_0_0
