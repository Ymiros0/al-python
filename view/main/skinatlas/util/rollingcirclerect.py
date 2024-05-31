local var_0_0 = class("RollingCircleRect")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.childs = {}
	arg_1_0.tpl = arg_1_1
	arg_1_0.parent = arg_1_2

	arg_1_0.AddDragListener()

def var_0_0.SetCallback(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.binder = arg_2_1
	arg_2_0.OnSelected = arg_2_2
	arg_2_0.OnRelease = arg_2_3

def var_0_0.AddItem(arg_3_0, arg_3_1):
	local var_3_0
	local var_3_1 = #arg_3_0.childs

	if var_3_1 <= 0:
		var_3_0 = RollingCircleItem.New(arg_3_0.tpl, var_3_1 + 1, arg_3_1)

		var_3_0.Init()
	else
		local var_3_2 = Object.Instantiate(arg_3_0.tpl, arg_3_0.tpl.parent)

		var_3_0 = RollingCircleItem.New(var_3_2, var_3_1 + 1, arg_3_1)

		local var_3_3 = arg_3_0.childs[#arg_3_0.childs]
		local var_3_4 = arg_3_0.childs[1]

		var_3_0.SetPrev(var_3_3)
		var_3_0.SetNext(var_3_4)
		var_3_4.SetPrev(var_3_0)
		var_3_3.SetNext(var_3_0)
		var_3_0.Init()

	table.insert(arg_3_0.childs, var_3_0)
	onButton(arg_3_0, var_3_0._tr, function()
		arg_3_0.ScrollToCenter(var_3_0)

		if arg_3_0.OnRelease:
			arg_3_0.OnRelease(arg_3_0.binder, var_3_0), SFX_PANEL)

	return var_3_0

def var_0_0.ScrollTo(arg_5_0, arg_5_1):
	Canvas.ForceUpdateCanvases()

	local var_5_0 = _.detect(arg_5_0.childs, function(arg_6_0)
		return arg_6_0.GetID() == arg_5_1)

	if var_5_0:
		triggerButton(var_5_0._tr)

def var_0_0.AddDragListener(arg_7_0):
	local function var_7_0(arg_8_0)
		local var_8_0 = arg_8_0 > 0 and -1 or 1

		arg_7_0.Step(var_8_0)

	local function var_7_1()
		local var_9_0 = _.detect(arg_7_0.childs, function(arg_10_0)
			return arg_10_0.IsCenter(arg_7_0.GetCenterIndex()))

		if arg_7_0.OnRelease:
			arg_7_0.OnRelease(arg_7_0.binder, var_9_0)

	var_0_0.AddVerticalDrag(arg_7_0.parent, var_7_0, var_7_1)

def var_0_0.GetCenterIndex(arg_11_0):
	local var_11_0 = #arg_11_0.childs
	local var_11_1 = math.ceil(var_11_0 / 2)

	return math.min(4, var_11_1)

def var_0_0.ScrollToCenter(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_0.GetCenterIndex() - arg_12_1.GetIndex()

	if var_12_0 == 0:
		return

	arg_12_0.Step(var_12_0)

def var_0_0.Step(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1 > 0 and "GoForward" or "GoBack"
	local var_13_1 = math.abs(arg_13_1)
	local var_13_2 = arg_13_0.GetCenterIndex()

	for iter_13_0 = 1, var_13_1:
		for iter_13_1, iter_13_2 in ipairs(arg_13_0.childs):
			iter_13_2.Record()

		local var_13_3

		for iter_13_3, iter_13_4 in ipairs(arg_13_0.childs):
			iter_13_4[var_13_0](iter_13_4)

			if iter_13_4.IsCenter(var_13_2):
				var_13_3 = iter_13_4

		if arg_13_0.OnSelected:
			arg_13_0.OnSelected(arg_13_0.binder, var_13_3)

def var_0_0.AddVerticalDrag(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = GetOrAddComponent(arg_14_0, "EventTriggerListener")
	local var_14_1 = 90
	local var_14_2
	local var_14_3 = 0
	local var_14_4 = 0
	local var_14_5 = 0

	var_14_0.AddBeginDragFunc(function(arg_15_0, arg_15_1)
		var_14_3 = 0
		var_14_4 = 0
		var_14_2 = arg_15_1.position
		var_14_5 = var_14_2.y)
	var_14_0.AddDragFunc(function(arg_16_0, arg_16_1)
		if var_14_5 > arg_16_1.position.y and var_14_4 != 0:
			var_14_2 = arg_16_1.position
			var_14_4 = 0
		elif var_14_5 < arg_16_1.position.y and var_14_3 != 0:
			var_14_2 = arg_16_1.position
			var_14_3 = 0

		local var_16_0 = arg_16_1.position.y - var_14_2.y
		local var_16_1 = math.abs(math.floor(var_16_0 / var_14_1))

		if arg_14_1 and var_16_1 > var_14_3:
			var_14_3 = var_16_1

			arg_14_1(var_16_0)

		if arg_14_1 and var_16_1 < var_14_4:
			var_14_4 = var_16_1

			arg_14_1(var_16_0)

		var_14_5 = var_14_2.y)
	var_14_0.AddDragEndFunc(function(arg_17_0, arg_17_1)
		if arg_14_2:
			arg_14_2())

def var_0_0.Dispose(arg_18_0):
	pg.DelegateInfo.Dispose(arg_18_0)

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.childs):
		iter_18_1.Dispose()

	ClearEventTrigger(GetOrAddComponent(arg_18_0.parent, "EventTriggerListener"))

	arg_18_0.binder = None
	arg_18_0.OnSelected = None
	arg_18_0.OnRelease = None
	arg_18_0.childs = None

return var_0_0
