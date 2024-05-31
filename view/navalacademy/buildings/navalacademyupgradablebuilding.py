local var_0_0 = class("NavalAcademyUpgradableBuilding", import(".NavalAcademyBuilding"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.nameTF = findTF(arg_1_0._tf, "name")
	arg_1_0.levelTxt = findTF(arg_1_0._tf, "name/level").GetComponent(typeof(Text))
	arg_1_0.timeTF = findTF(arg_1_0._tf, "time")
	arg_1_0.timeTxt = findTF(arg_1_0._tf, "time/Text").GetComponent(typeof(Text))
	arg_1_0.floatTF = findTF(arg_1_0._tf, "float")
	arg_1_0.floatTxt = arg_1_0.floatTF.Find("Text").GetComponent(typeof(Text))
	arg_1_0.bubble = findTF(arg_1_0._tf, "popup")
	arg_1_0.heigh = arg_1_0.bubble.localPosition.y

	setActive(arg_1_0.floatTF, False)
	setText(findTF(arg_1_0._tf, "time/label"), i18n("class_label_upgrading"))

def var_0_0.OnInit(arg_2_0):
	arg_2_0.UpdateResField()
	arg_2_0.UpdateBubble()

def var_0_0.FloatAni(arg_3_0):
	LeanTween.moveLocalY(go(arg_3_0.bubble), arg_3_0.heigh + 20, 2).setFrom(arg_3_0.heigh).setLoopPingPong()

def var_0_0.UpdateBubble(arg_4_0):
	local var_4_0 = arg_4_0.GetResField().HasRes()

	if var_4_0:
		arg_4_0.FloatAni()

	setActive(arg_4_0.bubble, var_4_0)
	onButton(arg_4_0, arg_4_0.bubble, function()
		local var_5_0 = arg_4_0.GetResField()

		arg_4_0.emit(NavalAcademyMediator.ON_GET_RES, var_5_0.GetResourceType()), SFX_PANEL)

def var_0_0.PlayGetResAnim(arg_6_0, arg_6_1):
	arg_6_0.UpdateBubble()

	arg_6_0.floatTxt.text = "+" .. arg_6_1

	setActive(arg_6_0.floatTF, True)
	LeanTween.moveY(rtf(arg_6_0.floatTF), 30, 1).setFrom(0).setOnComplete(System.Action(function()
		setActive(arg_6_0.floatTF, False)))

def var_0_0.UpdateResField(arg_8_0):
	arg_8_0.RemoveTimer()

	local var_8_0 = arg_8_0.GetResField()

	arg_8_0.levelTxt.text = "Lv." .. var_8_0.GetLevel()

	local var_8_1 = var_8_0.IsStarting()

	setActive(arg_8_0.timeTF, var_8_1)
	setActive(arg_8_0.nameTF, not var_8_1)

	if var_8_1:
		arg_8_0.AddTimer()

	arg_8_0.RefreshTip()

def var_0_0.AddTimer(arg_9_0):
	local var_9_0 = arg_9_0.GetResField()

	arg_9_0.timer = Timer.New(function()
		local var_10_0 = var_9_0.GetDuration()

		if var_10_0 and var_10_0 > 0:
			arg_9_0.timeTxt.text = pg.TimeMgr.GetInstance().DescCDTime(var_10_0)
		else
			arg_9_0.UpdateResField(), 1, -1)

	arg_9_0.timer.Start()
	arg_9_0.timer.func()

def var_0_0.RemoveTimer(arg_11_0):
	if arg_11_0.timer:
		arg_11_0.timer.Stop()

		arg_11_0.timer = None

def var_0_0.IsTip(arg_12_0):
	return arg_12_0.GetResField().CanUpgrade()

def var_0_0.Dispose(arg_13_0):
	var_0_0.super.Dispose(arg_13_0)
	arg_13_0.RemoveTimer()

	if LeanTween.isTweening(go(arg_13_0.floatTF)):
		LeanTween.cancel(go(arg_13_0.floatTF))

	LeanTween.cancel(go(arg_13_0.bubble))

def var_0_0.GetResField(arg_14_0):
	assert(False)

return var_0_0
