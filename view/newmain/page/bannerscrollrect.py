local var_0_0 = class("BannerScrollRect")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.container = arg_1_1
	arg_1_0.dotContainer = arg_1_2

	local var_1_0 = arg_1_1.Find("item")

	arg_1_0.items = {
		var_1_0
	}

	local var_1_1 = arg_1_2.Find("dot")

	arg_1_0.dots = {
		var_1_1
	}
	arg_1_0.itemWidth = var_1_0.sizeDelta.x
	arg_1_0.dotStartPosX = var_1_1.localPosition.x
	arg_1_0.dotWidth = var_1_1.sizeDelta.x
	arg_1_0.total = 0
	arg_1_0.index = 1
	arg_1_0.dragEvent = arg_1_0.container.GetComponent("EventTriggerListener")

def var_0_0.GetItem(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0.items[arg_2_1]

	if not var_2_0:
		local var_2_1 = arg_2_0.items[1]

		var_2_0 = Object.Instantiate(var_2_1, var_2_1.transform.parent)
		arg_2_0.items[arg_2_1] = var_2_0

	return var_2_0

def var_0_0.GetDot(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.dots[arg_3_1]

	if not var_3_0:
		local var_3_1 = arg_3_0.dots[1]

		var_3_0 = Object.Instantiate(var_3_1, var_3_1.transform.parent)
		arg_3_0.dots[arg_3_1] = var_3_0

	return var_3_0

def var_0_0.AddChild(arg_4_0):
	arg_4_0.total = arg_4_0.total + 1

	local var_4_0 = arg_4_0.GetDot(arg_4_0.total)
	local var_4_1 = arg_4_0.GetItem(arg_4_0.total)

	setActive(var_4_1, True)
	setActive(var_4_0, True)
	arg_4_0.UpdateItemPosition(arg_4_0.total, var_4_1)
	arg_4_0.UpdateDotPosition(arg_4_0.total, var_4_0)

	return var_4_1

def var_0_0.UpdateItemPosition(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = (arg_5_1 - 1) * arg_5_0.itemWidth

	arg_5_2.localPosition = Vector3(var_5_0, arg_5_2.localPosition.y, 0)

def var_0_0.UpdateDotPosition(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.dotStartPosX + (arg_6_1 - 1) * (arg_6_0.dotWidth + 15)

	arg_6_2.localPosition = Vector3(var_6_0, arg_6_2.localPosition.y, 0)

def var_0_0.SetUp(arg_7_0):
	if arg_7_0.total == 0:
		arg_7_0.Disable()

		return

	arg_7_0.container.localPosition = Vector3(0, 0, 0)

	arg_7_0.ScrollTo(1)
	arg_7_0.AutoScroll()
	arg_7_0.AddDrag()

def var_0_0.AutoScroll(arg_8_0):
	arg_8_0.RemoveTimer()

	arg_8_0.timer = Timer.New(function()
		local var_9_0 = (arg_8_0.index + 1) % arg_8_0.total

		if var_9_0 == 0:
			var_9_0 = arg_8_0.total

		arg_8_0.ScrollTo(var_9_0), 5, -1, True)

	arg_8_0.timer.Start()

def var_0_0.ScrollTo(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.index or 1
	local var_10_1 = (arg_10_1 - 1) * arg_10_0.itemWidth

	arg_10_0.animating = True

	LeanTween.moveLocalX(go(arg_10_0.container), -1 * var_10_1, 0.2).setEase(LeanTweenType.easeInOutSine).setOnComplete(System.Action(function()
		arg_10_0.animating = False))

	local var_10_2 = arg_10_0.dots[var_10_0]

	arg_10_0.TriggerDot(var_10_2, False)

	local var_10_3 = arg_10_0.dots[arg_10_1]

	arg_10_0.TriggerDot(var_10_3, True)

	arg_10_0.index = arg_10_1

def var_0_0.TriggerDot(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = arg_12_2 and Color.New(1, 1, 1, 1) or Color.New(0.4, 0.45, 0.55)

	arg_12_1.GetComponent(typeof(Image)).color = var_12_0

def var_0_0.AddDrag(arg_13_0):
	local var_13_0 = 0
	local var_13_1

	arg_13_0.dragEvent.AddBeginDragFunc(function(arg_14_0, arg_14_1)
		if arg_13_0.animating:
			return

		arg_13_0.Puase()

		var_13_0 = arg_14_1.position.x
		var_13_1 = arg_13_0.container.localPosition)
	arg_13_0.dragEvent.AddDragFunc(function(arg_15_0, arg_15_1)
		if arg_13_0.animating or not var_13_1:
			return

		local var_15_0 = (arg_15_1.position.x - var_13_0) * 0.5

		arg_13_0.container.localPosition = Vector3(var_13_1.x + var_15_0, var_13_1.y, 0))
	arg_13_0.dragEvent.AddDragEndFunc(function(arg_16_0, arg_16_1)
		if arg_13_0.animating or not var_13_1:
			return

		local var_16_0 = arg_16_1.position.x - var_13_0
		local var_16_1 = math.floor(math.abs(var_16_0 / arg_13_0.itemWidth) + 0.5)
		local var_16_2 = var_16_0 < 0 and arg_13_0.index + var_16_1 or arg_13_0.index - var_16_1
		local var_16_3 = math.clamp(var_16_2, 1, arg_13_0.total)

		arg_13_0.ScrollTo(var_16_3)
		arg_13_0.Resume())

def var_0_0.Reset(arg_17_0):
	arg_17_0.RemoveTimer()
	ClearEventTrigger(arg_17_0.dragEvent)
	LeanTween.cancel(go(arg_17_0.container))

	arg_17_0.total = 0
	arg_17_0.index = 1
	arg_17_0.animating = False

	arg_17_0.Disable()

def var_0_0.Disable(arg_18_0):
	for iter_18_0, iter_18_1 in ipairs(arg_18_0.items):
		setActive(iter_18_1, False)

	for iter_18_2, iter_18_3 in ipairs(arg_18_0.dots):
		arg_18_0.TriggerDot(iter_18_3, False)
		setActive(iter_18_3, False)

def var_0_0.Puase(arg_19_0):
	arg_19_0.RemoveTimer()

def var_0_0.Resume(arg_20_0):
	if arg_20_0.total == 0:
		return

	arg_20_0.AutoScroll()

def var_0_0.RemoveTimer(arg_21_0):
	if arg_21_0.timer:
		arg_21_0.timer.Stop()

		arg_21_0.timer = None

def var_0_0.Dispose(arg_22_0):
	arg_22_0.Reset()

	for iter_22_0, iter_22_1 in ipairs(arg_22_0.items):
		Object.Destroy(iter_22_1.gameObject)

	for iter_22_2, iter_22_3 in ipairs(arg_22_0.dots):
		Object.Destroy(iter_22_3.gameObject)

	arg_22_0.items = None
	arg_22_0.dots = None

return var_0_0
