local var_0_0 = class("CryptolaliaScrollRect")
local var_0_1 = 150

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.tpl = arg_1_1.gameObject
	arg_1_0.tpls = {
		arg_1_0.tpl
	}
	arg_1_0.startPosition = arg_1_1.localPosition
	arg_1_0.eventTriggerListener = arg_1_1.parent.GetComponent(typeof(EventTriggerListener))
	arg_1_0.animation = arg_1_2
	arg_1_0.items = {}

local function var_0_2(arg_2_0)
	if #arg_2_0.tpls > 0:
		return table.remove(arg_2_0.tpls, 1)
	else
		return Object.Instantiate(arg_2_0.tpl, arg_2_0.tpl.transform.parent)

def NewTpl(arg_3_0, arg_3_1):
	return Object.Instantiate(arg_3_1, arg_3_0.tpl.transform.parent)

def var_0_0.Make(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.OnItemInit = arg_4_1
	arg_4_0.OnSelect = arg_4_2

def var_0_0.Align(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0.totalCnt = math.max(5, arg_5_1)
	arg_5_0.midIndex = math.ceil(arg_5_0.totalCnt / 2)

	local var_5_0 = {}

	for iter_5_0 = 1, arg_5_0.totalCnt:
		table.insert(var_5_0, function(arg_6_0)
			local var_6_0 = CryptolaliaScrollRectItem.New(var_0_2(arg_5_0), arg_5_0.midIndex, iter_5_0)

			if arg_5_0.OnItemInit:
				arg_5_0.OnItemInit(var_6_0)

			if var_6_0.IsMidIndex() and arg_5_0.OnSelect:
				arg_5_0.OnSelect(var_6_0)

			table.insert(arg_5_0.items, var_6_0)

			if iter_5_0 % 3 == 0:
				onNextTick(arg_6_0)
			else
				arg_6_0())

	seriesAsync(var_5_0, arg_5_2)

def var_0_0.SetUp(arg_7_0):
	for iter_7_0, iter_7_1 in ipairs(arg_7_0.items):
		onButton(arg_7_0, iter_7_1._go, function()
			if arg_7_0.inAnimation:
				return

			arg_7_0.JumpToMid(iter_7_1.GetIndex()), SFX_PANEL)

	arg_7_0.AddDrag()

def var_0_0.AddDrag(arg_9_0):
	arg_9_0.eventTriggerListener.AddBeginDragFunc(function(arg_10_0, arg_10_1)
		arg_9_0.position = arg_10_1.position)
	arg_9_0.eventTriggerListener.AddDragEndFunc(function(arg_11_0, arg_11_1)
		if not arg_9_0.position:
			return

		local var_11_0 = arg_11_1.position - arg_9_0.position

		if math.abs(var_11_0.x) > var_0_1 and math.abs(var_11_0.y) > var_0_1:
			if var_11_0.x >= 0:
				arg_9_0.OnListUp()

			if var_11_0.x < 0:
				arg_9_0.OnListDown()

		arg_9_0.position = None)

def var_0_0.OnListUp(arg_12_0):
	local var_12_0 = arg_12_0.midIndex + 1

	arg_12_0.trigger(var_12_0)

def var_0_0.OnListDown(arg_13_0):
	local var_13_0 = arg_13_0.midIndex - 1

	arg_13_0.trigger(var_13_0)

def var_0_0.trigger(arg_14_0, arg_14_1):
	local var_14_0

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.items):
		if iter_14_1.GetIndex() == arg_14_1:
			var_14_0 = iter_14_1

			break

	if var_14_0 and var_14_0.CanInteractable():
		arg_14_0.JumpToMid(var_14_0.GetIndex())

def var_0_0.JumpToMid(arg_15_0, arg_15_1):
	local var_15_0 = math.abs(arg_15_0.midIndex - arg_15_1)
	local var_15_1 = arg_15_0.midIndex - arg_15_1 <= 0
	local var_15_2 = {}

	for iter_15_0 = 1, var_15_0:
		table.insert(var_15_2, function(arg_16_0)
			local var_16_0 = var_15_1 and arg_15_0.midIndex + 1 or arg_15_0.midIndex - 1

			if iter_15_0 == var_15_0:
				arg_15_0.Step(arg_15_0.midIndex - var_16_0, arg_16_0)
			else
				arg_15_0.Step(arg_15_0.midIndex - var_16_0, onNextTick(arg_16_0)))

	seriesAsync(var_15_2)

def var_0_0.Step1(arg_17_0, arg_17_1, arg_17_2):
	if arg_17_0.inAnimation:
		arg_17_0.ClearAnimation()

	local var_17_0 = {}
	local var_17_1

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.items):
		local var_17_2 = iter_17_1.GetIndex() + arg_17_1
		local var_17_3 = var_17_2

		if var_17_3 > arg_17_0.totalCnt:
			var_17_3 = var_17_3 - arg_17_0.totalCnt
			arg_17_0.sinker = CryptolaliaScrollRectItem.New(NewTpl(arg_17_0, iter_17_1._go), arg_17_0.midIndex, 0)
		elif var_17_3 <= 0:
			var_17_3 = arg_17_0.totalCnt - math.abs(var_17_3)
			arg_17_0.sinker = CryptolaliaScrollRectItem.New(NewTpl(arg_17_0, iter_17_1._go), arg_17_0.midIndex, arg_17_0.totalCnt + 1)

		if var_17_3 == arg_17_0.midIndex:
			var_17_1 = iter_17_1

		table.insert(var_17_0, function(arg_18_0)
			iter_17_1.UpdateIndexWithAnim(var_17_3, var_17_2, arg_18_0))

	if arg_17_0.sinker:
		table.insert(var_17_0, function(arg_19_0)
			local var_19_0 = arg_17_0.sinker.GetIndex() + arg_17_1

			arg_17_0.sinker.UpdateIndexWithAnim(var_19_0, var_19_0, arg_19_0))

	table.insert(var_17_0, function(arg_20_0)
		arg_17_0.animation.Play(arg_17_1).OnComplete(arg_20_0).OnTrigger(function()
			if arg_17_0.OnSelect:
				arg_17_0.OnSelect(var_17_1)))

	arg_17_0.inAnimation = True

	parallelAsync(var_17_0, function()
		arg_17_0.ClearAnimation()
		arg_17_2())

def var_0_0.Step(arg_23_0, arg_23_1, arg_23_2):
	if arg_23_0.inAnimation:
		arg_23_0.ClearAnimation()

	local var_23_0 = {}
	local var_23_1
	local var_23_2 = {}
	local var_23_3

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.items):
		local var_23_4 = iter_23_1.GetIndex() + arg_23_1

		if var_23_4 > arg_23_0.totalCnt:
			var_23_4 = var_23_4 - arg_23_0.totalCnt
			arg_23_0.sinker = CryptolaliaScrollRectItem.New(NewTpl(arg_23_0, iter_23_1._go), arg_23_0.midIndex, 0)
			var_23_3 = arg_23_0.sinker.GetPosition()
		elif var_23_4 <= 0:
			var_23_4 = arg_23_0.totalCnt - math.abs(var_23_4)
			arg_23_0.sinker = CryptolaliaScrollRectItem.New(NewTpl(arg_23_0, iter_23_1._go), arg_23_0.midIndex, arg_23_0.totalCnt + 1)
			var_23_3 = arg_23_0.sinker.GetPosition()

		if var_23_4 == arg_23_0.midIndex:
			var_23_1 = iter_23_1

		iter_23_1.UpdateIndexSilence(var_23_4)
		table.insert(var_23_2, iter_23_1.GetPosition())

	table.insert(var_23_0, function(arg_24_0)
		arg_23_0.animation.Play(arg_23_1).OnComplete(arg_24_0).OnUpdate(function(arg_25_0)
			for iter_25_0, iter_25_1 in ipairs(arg_23_0.items):
				iter_25_1.SetPosition(var_23_2[iter_25_0] + arg_25_0)

			if arg_23_0.sinker:
				arg_23_0.sinker.SetPosition(var_23_3 + arg_25_0)).OnLastUpdate(function()
			for iter_26_0, iter_26_1 in ipairs(arg_23_0.items):
				iter_26_1.Refresh()).OnTrigger(function()
			if arg_23_0.OnSelect:
				arg_23_0.OnSelect(var_23_1)))

	arg_23_0.inAnimation = True

	parallelAsync(var_23_0, function()
		arg_23_0.ClearAnimation()
		arg_23_2())

def var_0_0.ClearAnimation(arg_29_0):
	if arg_29_0.inAnimation:
		arg_29_0.animation.Stop()

		for iter_29_0, iter_29_1 in ipairs(arg_29_0.items):
			iter_29_1.ClearAnimation()

		if arg_29_0.sinker:
			Object.Destroy(arg_29_0.sinker._go)

			arg_29_0.sinker = None

		arg_29_0.inAnimation = False

def var_0_0.Dispose(arg_30_0):
	for iter_30_0, iter_30_1 in ipairs(arg_30_0.items):
		iter_30_1.Dispose()

	arg_30_0.ClearAnimation()

	arg_30_0.items = None
	arg_30_0.OnItemInit = None
	arg_30_0.OnSelect = None

	pg.DelegateInfo.Dispose(arg_30_0)
	arg_30_0.eventTriggerListener.AddBeginDragFunc(None)
	arg_30_0.eventTriggerListener.AddDragEndFunc(None)

	arg_30_0.eventTriggerListener = None

return var_0_0
