local var_0_0 = class("CatteryAddHomeExpAnim")
local var_0_1 = 1

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0.expSlider = findTF(arg_1_0._tf, "slider").GetComponent(typeof(Slider))
	arg_1_0.levelTxt = findTF(arg_1_0._tf, "level").GetComponent(typeof(Text))
	arg_1_0.expTxt = findTF(arg_1_0._tf, "exp").GetComponent(typeof(Text))
	arg_1_0.addition = findTF(arg_1_0._tf, "addition")
	arg_1_0.additionExp = findTF(arg_1_0._tf, "addition/exp")
	arg_1_0.additionExpTxt = arg_1_0.additionExp.Find("Text").GetComponent(typeof(Text))
	arg_1_0.additionItem = findTF(arg_1_0._tf, "addition/item")
	arg_1_0.additionItemImg = findTF(arg_1_0._tf, "addition/item/icon")
	arg_1_0.animRiseH = arg_1_0.addition.localPosition.y

	setActive(arg_1_0._tf, False)

def var_0_0.Action(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5):
	setActive(arg_2_0._tf, True)

	arg_2_0.callback = arg_2_5

	local var_2_0 = arg_2_0.GetAwardOffset(arg_2_3, arg_2_4)

	setAnchoredPosition(arg_2_0.addition, {
		x = var_2_0
	})
	arg_2_0.RefreshAward(arg_2_3, arg_2_4)
	arg_2_0.RefreshHome(arg_2_2)

def var_0_0.GetAwardOffset(arg_3_0, arg_3_1, arg_3_2):
	return (arg_3_1 or arg_3_2) and -82 or -15

def var_0_0.RefreshAward(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_1:
		GetImageSpriteFromAtlasAsync("Props/20010", "", arg_4_0.additionItemImg)
	elif arg_4_2:
		GetImageSpriteFromAtlasAsync("Props/dormMoney", "", arg_4_0.additionItemImg)

	setActive(arg_4_0.additionItem, arg_4_1 or arg_4_2)

def var_0_0.RefreshHome(arg_5_0, arg_5_1):
	local var_5_0 = getProxy(CommanderProxy).GetCommanderHome()

	arg_5_0.additionExpTxt.text = arg_5_1 .. "<size=40>EXP</size>"

	if var_5_0.exp - arg_5_1 < 0:
		arg_5_0.DoUpgradeAnim(var_5_0, arg_5_1)
	else
		arg_5_0.DoAddExpAnim(var_5_0, arg_5_1)

def var_0_0.DoUpgradeAnim(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.levelTxt.text = "LV." .. arg_6_1.GetLevel() - 1

	if arg_6_2 == 0:
		arg_6_0.IfIsMaxLevel(arg_6_1, arg_6_2, True)

		return

	local var_6_0 = arg_6_1.GetPrevLevelExp()
	local var_6_1 = var_6_0 - math.abs(arg_6_1.exp - arg_6_2)

	arg_6_0.expTxt.text = "<color=#92FC63FF>" .. var_6_1 .. "/</color>" .. var_6_0

	local var_6_2 = var_6_1 / var_6_0

	arg_6_0.expSlider.value = var_6_2

	local var_6_3 = arg_6_1.GetNextLevelExp()
	local var_6_4 = arg_6_1.exp / var_6_3

	arg_6_0.AddExpAnim(var_6_2, 1, var_6_1, var_6_0, var_6_0, function()
		arg_6_0.levelTxt.text = "LV." .. arg_6_1.GetLevel()

		arg_6_0.AddExpAnim(0, var_6_4, 0, arg_6_1.exp, var_6_3, function()
			arg_6_0.IfIsMaxLevel(arg_6_1, arg_6_2)))
	arg_6_0.AdditionAnim(var_0_1, function()
		if arg_6_0.callback:
			arg_6_0.callback()

		arg_6_0.callback = None)

def var_0_0.DoAddExpAnim(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0.levelTxt.text = "LV." .. arg_10_1.GetLevel()

	if arg_10_2 == 0:
		arg_10_0.IfIsMaxLevel(arg_10_1, arg_10_2, True)

		return

	local var_10_0 = arg_10_1.GetNextLevelExp()
	local var_10_1 = arg_10_1.exp / var_10_0
	local var_10_2 = arg_10_1.exp - arg_10_2
	local var_10_3 = var_10_2 / var_10_0

	arg_10_0.AddExpAnim(var_10_3, var_10_1, var_10_2, arg_10_1.exp, var_10_0)
	arg_10_0.AdditionAnim(var_0_1, function()
		if arg_10_0.callback:
			arg_10_0.callback()

		arg_10_0.callback = None

		arg_10_0.IfIsMaxLevel(arg_10_1, arg_10_2))

def var_0_0.IfIsMaxLevel(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	if arg_12_1.IsMaxLevel():
		arg_12_0.expTxt.text = "MAX"
		arg_12_0.expSlider.value = 1

	arg_12_0.HideOrShowAddition(arg_12_2)

	if arg_12_3:
		if not IsNil(arg_12_0.additionItem) and isActive(arg_12_0.additionItem):
			arg_12_0.AdditionAnim(var_0_1, function()
				if arg_12_0.callback:
					arg_12_0.callback()

				arg_12_0.callback = None)
		else
			Timer.New(function()
				if arg_12_0.callback:
					arg_12_0.callback()

				arg_12_0.callback = None, var_0_1, 1).Start()

def var_0_0.HideOrShowAddition(arg_15_0, arg_15_1):
	setActive(arg_15_0.additionExp, arg_15_1 > 0)

def var_0_0.Clear(arg_16_0):
	if not IsNil(arg_16_0.expSlider) and LeanTween.isTweening(go(arg_16_0.expSlider)):
		LeanTween.cancel(go(arg_16_0.expSlider))

	if not IsNil(arg_16_0.expTxt) and LeanTween.isTweening(go(arg_16_0.expTxt)):
		LeanTween.cancel(go(arg_16_0.expTxt))

	if not IsNil(arg_16_0.addition) and LeanTween.isTweening(go(arg_16_0.addition)):
		LeanTween.cancel(go(arg_16_0.addition))

def var_0_0.Hide(arg_17_0):
	arg_17_0.Clear()
	setActive(arg_17_0._tf, False)

def var_0_0.Dispose(arg_18_0):
	arg_18_0.Hide()

def var_0_0.AddExpAnim(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5, arg_19_6):
	parallelAsync({
		function(arg_20_0)
			LeanTween.value(go(arg_19_0.expSlider), arg_19_1, arg_19_2, var_0_1).setOnUpdate(System.Action_float(function(arg_21_0)
				arg_19_0.expSlider.value = arg_21_0)).setOnComplete(System.Action(arg_20_0)),
		function(arg_22_0)
			LeanTween.value(go(arg_19_0.expTxt), arg_19_3, arg_19_4, var_0_1).setOnUpdate(System.Action_float(function(arg_23_0)
				local var_23_0 = math.ceil(arg_23_0)

				arg_19_0.expTxt.text = "<color=#92FC63FF>" .. var_23_0 .. "/</color>" .. arg_19_5)).setOnComplete(System.Action(arg_22_0))
	}, function()
		if arg_19_6:
			arg_19_6())

def var_0_0.AdditionAnim(arg_25_0, arg_25_1, arg_25_2):
	setActive(arg_25_0.addition, True)
	LeanTween.value(go(arg_25_0.addition), arg_25_0.animRiseH, arg_25_0.animRiseH + 25, arg_25_1).setOnUpdate(System.Action_float(function(arg_26_0)
		arg_25_0.addition.localPosition = Vector3(arg_25_0.addition.localPosition.x, arg_26_0, 0))).setOnComplete(System.Action(function()
		setActive(arg_25_0.addition, False)
		arg_25_2()

		arg_25_0.addition.localPosition = Vector3(arg_25_0.addition.localPosition.x, 0, 0)))

return var_0_0
