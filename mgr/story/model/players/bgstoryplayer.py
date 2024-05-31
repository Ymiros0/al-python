local var_0_0 = class("BgStoryPlayer", import(".DialogueStoryPlayer"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.subImage = arg_1_0.findTF("sub", arg_1_0.bgPanel).GetComponent(typeof(Image))
	arg_1_0.bgRecord = None

def var_0_0.Reset(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	var_0_0.super.super.Reset(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	setActive(arg_2_0.bgPanel, True)
	setActive(arg_2_0.subImage.gameObject, False)
	setActive(arg_2_0.actorPanel, False)
	arg_2_0.RecyclePainting({
		"actorLeft",
		"actorMiddle",
		"actorRgiht"
	})

def var_0_0.OnBgUpdate(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.GetBgName()

	if arg_3_0.bgRecord != var_3_0:
		arg_3_0.bgRecord = var_3_0

		local var_3_1 = arg_3_1.GetFadeSpeed()

		arg_3_0.TweenValueForcanvasGroup(arg_3_0.bgPanelCg, 0, 1, var_3_1, 0, None)

def var_0_0.UpdateBg(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.GetSubBg()

	if var_4_0:
		setActive(arg_4_0.subImage.gameObject, True)

		arg_4_0.subImage.sprite = arg_4_0.GetBg(var_4_0)

	if not arg_4_1.GetBgName():
		return

	var_0_0.super.UpdateBg(arg_4_0, arg_4_1)

def var_0_0.OnInit(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if arg_5_1.ShouldBlackScreen():
		setActive(arg_5_0.curtain, True)
		arg_5_0.curtain.SetAsLastSibling()
		arg_5_3()
	else
		var_0_0.super.OnInit(arg_5_0, arg_5_1, arg_5_2, arg_5_3)

def var_0_0.OnEnter(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	if arg_6_1.ShouldBlackScreen():
		arg_6_0.DelayCall(arg_6_1.ShouldBlackScreen(), function()
			setActive(arg_6_0.curtain, True)
			arg_6_0.curtain.SetAsFirstSibling()
			assert(not arg_6_1.ExistOption())
			arg_6_3()
			triggerButton(arg_6_0._go))
	else
		local var_6_0 = arg_6_1.GetUnscaleDelay()

		if arg_6_0.autoNext:
			var_6_0 = var_6_0 - arg_6_0.script.GetTriggerDelayTime()

		arg_6_0.UnscaleDelayCall(var_6_0, function()
			var_0_0.super.OnEnter(arg_6_0, arg_6_1, arg_6_2, arg_6_3))

def var_0_0.GetSideTF(arg_9_0, arg_9_1):
	local var_9_0
	local var_9_1
	local var_9_2
	local var_9_3

	if DialogueStep.SIDE_LEFT == arg_9_1:
		var_9_0, var_9_1, var_9_2, var_9_3 = None, arg_9_0.nameLeft, arg_9_0.nameLeftTxt
	elif DialogueStep.SIDE_RIGHT == arg_9_1:
		var_9_0, var_9_1, var_9_2, var_9_3 = None, arg_9_0.nameRight, arg_9_0.nameRightTxt
	elif DialogueStep.SIDE_MIDDLE == arg_9_1:
		var_9_0, var_9_1, var_9_2, var_9_3 = None, arg_9_0.nameLeft, arg_9_0.nameLeftTxt

	return var_9_0, var_9_1, var_9_2, var_9_3

def var_0_0.Clear(arg_10_0, arg_10_1):
	arg_10_0.bgs = {}
	arg_10_0.goCG.alpha = 1
	arg_10_0.callback = None
	arg_10_0.autoNext = None
	arg_10_0.script = None
	arg_10_0.subImage.sprite = None

	arg_10_0.OnClear()

	if arg_10_1:
		arg_10_1()

	pg.DelegateInfo.New(arg_10_0)

def var_0_0.StoryEnd(arg_11_0):
	var_0_0.super.StoryEnd(arg_11_0)

	arg_11_0.bgRecord = None
	arg_11_0.bgImage.sprite = None

return var_0_0
