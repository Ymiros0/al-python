local var_0_0 = class("CourtYardShipAnimatorAgent", import(".CourtYardAgent"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.name = None

def var_0_0.State2AnimationName(arg_2_0, arg_2_1):
	if arg_2_1 == CourtYardShip.STATE_IDLE or arg_2_1 == CourtYardShip.STATE_STOP:
		return "stand2"
	elif arg_2_1 == CourtYardShip.STATE_MOVE:
		return "walk"
	elif arg_2_1 == CourtYardShip.STATE_DRAG:
		return "tuozhuai2"
	elif arg_2_1 == CourtYardShip.STATE_TOUCH:
		return "touch"
	elif arg_2_1 == CourtYardShip.STATE_GETAWARD:
		return "motou"
	elif arg_2_1 == CourtYardShip.STATE_INTERACT:
		-- block empty

def var_0_0.SetState(arg_3_0, arg_3_1):
	arg_3_0.RemoveAnimFinishTimer()

	local var_3_0 = arg_3_0.State2AnimationName(arg_3_1)

	if not var_3_0 or arg_3_0.name == var_3_0:
		return

	arg_3_0.PlayAction(var_3_0, function()
		arg_3_0.OnAnimtionFinish(arg_3_1))

def var_0_0.PlayInteractioAnim(arg_5_0, arg_5_1):
	arg_5_0.PlayAction(arg_5_1, function()
		arg_5_0.OnAnimtionFinish(CourtYardShip.STATE_INTERACT))
	arg_5_0.CheckMissTagAction(arg_5_1)

def var_0_0.PlayAction(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0.RemoveAnimFinishTimer()
	arg_7_0.spineAnimUI.SetActionCallBack(None)

	local function var_7_0(arg_8_0)
		if arg_8_0 == "finish":
			arg_7_0.spineAnimUI.SetActionCallBack(None)
			arg_7_2()

	arg_7_0.spineAnimUI.SetActionCallBack(var_7_0)
	arg_7_0.role.SetAction(arg_7_1)

	arg_7_0.name = arg_7_1

def var_0_0.CheckMissTagAction(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.data.GetInterActionData()
	local var_9_1 = pg.furniture_specail_action[var_9_0.GetOwner().configId]

	if var_9_1:
		local var_9_2 = _.detect(var_9_1.actions, function(arg_10_0)
			return arg_10_0[1] == arg_9_1)

		if var_9_2:
			arg_9_0.AddAnimFinishTimer(var_9_2[2])

def var_0_0.AddAnimFinishTimer(arg_11_0, arg_11_1):
	arg_11_0.animFinishTimer = Timer.New(function()
		arg_11_0.animFinishTimer.Stop()

		arg_11_0.animFinishTimer = None

		arg_11_0.OnAnimtionFinish(CourtYardShip.STATE_INTERACT), arg_11_1, 1)

	arg_11_0.animFinishTimer.Start()

def var_0_0.RemoveAnimFinishTimer(arg_13_0):
	if arg_13_0.animFinishTimer:
		arg_13_0.animFinishTimer.Stop()

		arg_13_0.animFinishTimer = None

def var_0_0.Dispose(arg_14_0):
	arg_14_0.RemoveAnimFinishTimer()
	var_0_0.super.Dispose(arg_14_0)
	arg_14_0.spineAnimUI.SetActionCallBack(None)

return var_0_0
