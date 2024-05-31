local var_0_0 = class("BossRushPassedLayer", import("view.challenge.ChallengePassedLayer"))

var_0_0.GROW_TIME = 0.55

def var_0_0.getUIName(arg_1_0):
	return "BossRushPassedUI"

def var_0_0.didEnter(arg_2_0):
	arg_2_0.tweenObjs = {}

	pg.UIMgr.GetInstance().OverlayPanel(arg_2_0._tf)
	arg_2_0.updateSlider(arg_2_0.curIndex)
	arg_2_0.moveSlider(arg_2_0.curIndex)
	onButton(arg_2_0, arg_2_0._tf, function()
		arg_2_0.emit(var_0_0.ON_CLOSE))
	arg_2_0._tf.GetComponent("DftAniEvent").SetEndEvent(function(arg_4_0)
		arg_2_0.emit(var_0_0.ON_CLOSE))

def var_0_0.willExit(arg_5_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_5_0._tf)
	LeanTween.cancel(go(arg_5_0.slider))

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.tweenObjs):
		LeanTween.cancel(iter_5_1)

	arg_5_0.tweenObjs = {}

def var_0_0.onBackPressed(arg_6_0):
	triggerButton(arg_6_0._tf)

def var_0_0.initData(arg_7_0):
	arg_7_0.curIndex = arg_7_0.contextData.curIndex

def var_0_0.updateSlider(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1 or arg_8_0.curIndex
	local var_8_1 = arg_8_0.contextData.maxIndex

	if var_8_1 < var_8_0:
		var_8_0 = var_8_0 % var_8_1 == 0 and var_8_1 or var_8_0 % var_8_1

	local var_8_2 = 1 / (var_8_1 - 1)
	local var_8_3 = (var_8_0 - 1) * var_8_2

	arg_8_0.sliderSC.value = var_8_3

	local var_8_4 = GetComponent(arg_8_0.squareTpl, typeof(LayoutElement)).preferredWidth
	local var_8_5 = var_8_4 * 0.5
	local var_8_6 = (arg_8_0.squareContainer.rect.width - var_8_4) * var_8_2

	arg_8_0.squareList.make(function(arg_9_0, arg_9_1, arg_9_2)
		local var_9_0 = arg_8_0.findTF("UnFinished", arg_9_2)
		local var_9_1 = arg_8_0.findTF("Finished", arg_9_2)
		local var_9_2 = arg_8_0.findTF("Challengeing", arg_9_2)
		local var_9_3 = arg_8_0.findTF("Arrow", arg_9_2)

		local function var_9_4()
			setActive(var_9_1, True)
			setActive(var_9_0, False)
			setActive(var_9_2, False)

		local function var_9_5()
			setActive(var_9_1, False)
			setActive(var_9_0, True)
			setActive(var_9_2, False)

		local function var_9_6()
			setActive(var_9_1, False)
			setActive(var_9_0, False)
			setActive(var_9_2, True)

		if arg_9_0 == UIItemList.EventUpdate:
			if arg_9_1 + 1 < var_8_0:
				setActive(var_9_3, False)
				var_9_4()
			elif arg_9_1 + 1 == var_8_0:
				setActive(var_9_3, True)
				var_9_6()
			elif arg_9_1 + 1 > var_8_0:
				setActive(var_9_3, False)
				var_9_5()

			setAnchoredPosition(arg_9_2, {
				y = 0,
				x = var_8_5 + var_8_6 * arg_9_1
			}))
	arg_8_0.squareList.align(var_8_1)

def var_0_0.moveSlider(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1 or arg_13_0.curIndex
	local var_13_1 = arg_13_0.contextData.maxIndex

	if var_13_1 < var_13_0:
		var_13_0 = var_13_0 % var_13_1 == 0 and var_13_1 or var_13_0 % var_13_1

	local var_13_2 = 1 / (var_13_1 - 1)
	local var_13_3 = (var_13_0 - 1) * var_13_2
	local var_13_4 = var_13_0 * var_13_2

	LeanTween.value(go(arg_13_0.slider), var_13_3, var_13_4, var_0_0.GROW_TIME).setDelay(1.4).setOnUpdate(System.Action_float(function(arg_14_0)
		arg_13_0.sliderSC.value = arg_14_0)).setOnComplete(System.Action(function()
		arg_13_0.updateSlider(var_13_0 + 1)))

return var_0_0
