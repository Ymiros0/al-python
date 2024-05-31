local var_0_0 = class("CommanderBuildPoolPanel", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CommanderBuildPoolUI"

local var_0_1 = 10

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.buildPoolList = UIItemList.New(arg_2_0._tf.Find("frame/bg/content/list"), arg_2_0._tf.Find("frame/bg/content/list/1"))

	local var_2_0 = arg_2_0._tf.Find("frame/bg/content/queue/list1/pos")

	arg_2_0.posListTop = UIItemList.New(arg_2_0._tf.Find("frame/bg/content/queue/list1"), var_2_0)
	arg_2_0.posListBottom = UIItemList.New(arg_2_0._tf.Find("frame/bg/content/queue/list2"), var_2_0)
	arg_2_0.autoBtn = arg_2_0._tf.Find("frame/bg/auto_btn")
	arg_2_0.startBtn = arg_2_0._tf.Find("frame/bg/start_btn")
	arg_2_0.selectedTxt = arg_2_0._tf.Find("statistics/Text").GetComponent(typeof(Text))
	arg_2_0.sprites = {
		arg_2_0._tf.Find("frame/bg/content/list/1/icon/iconImg").GetComponent(typeof(Image)).sprite,
		arg_2_0._tf.Find("frame/bg/content/list/2/icon/iconImg").GetComponent(typeof(Image)).sprite,
		arg_2_0._tf.Find("frame/bg/content/list/3/icon/iconImg").GetComponent(typeof(Image)).sprite
	}

	setText(arg_2_0.findTF("frame/bg/content/Text"), i18n("commander_use_box_tip"))
	setText(arg_2_0.findTF("frame/bg/content/queue/title/Text"), i18n("commander_use_box_queue"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf.Find("frame/bg/close_btn"), function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.autoBtn, function()
		if #arg_3_0.selected >= var_0_1:
			return

		arg_3_0.AutoSelect()
		arg_3_0.UpdatePos(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.startBtn, function()
		if #arg_3_0.selected == 0:
			return

		arg_3_0.contextData.msgBox.ExecuteAction("Show", {
			content = i18n("commander_select_box_tip", #arg_3_0.selected),
			def onYes:()
				arg_3_0.emit(CommanderCatMediator.BATCH_BUILD, arg_3_0.selected)
				arg_3_0.Hide()
		}), SFX_PANEL)

def var_0_0.AutoSelect(arg_9_0):
	local var_9_0 = arg_9_0.pools

	local function var_9_1()
		local var_10_0

		for iter_10_0, iter_10_1 in pairs(arg_9_0.counts):
			if iter_10_1 > 0:
				var_10_0 = iter_10_0

		return var_10_0

	local var_9_2 = var_0_1 - #arg_9_0.selected

	for iter_9_0 = 1, var_9_2:
		local var_9_3 = var_9_1()

		if var_9_3:
			arg_9_0.ReduceCount(var_9_3, -1)

def var_0_0.Show(arg_11_0, arg_11_1, arg_11_2):
	var_0_1 = arg_11_2
	arg_11_0.selected = {}
	arg_11_0.pools = arg_11_1

	local var_11_0 = arg_11_0.pools

	arg_11_0.counts = {}

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.pools):
		arg_11_0.counts[iter_11_1.id] = iter_11_1.getItemCount()

	arg_11_0.boxesTxt = {}

	table.sort(var_11_0, function(arg_12_0, arg_12_1)
		return arg_12_0.id < arg_12_1.id)
	arg_11_0.buildPoolList.make(function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_0 == UIItemList.EventUpdate:
			local var_13_0 = var_11_0[arg_13_1 + 1]

			local function var_13_1(arg_14_0)
				if #arg_11_0.selected < var_0_1 and arg_11_0.counts[var_13_0.id] > 0:
					arg_11_0.ReduceCount(var_13_0.id, -1)

			pressPersistTrigger(arg_13_2.Find("icon"), 0.5, var_13_1, None, True, True, 0.15, SFX_PANEL)
			setText(arg_13_2.Find("name"), var_13_0.getName())

			arg_11_0.boxesTxt[var_13_0.id] = arg_13_2.Find("Text")

			arg_11_0.ReduceCount(var_13_0.id, 0))
	arg_11_0.buildPoolList.align(#var_11_0)
	arg_11_0.UpdatePos()
	setActive(arg_11_0._tf, True)

	arg_11_0.isShow = True

def var_0_0.ReduceCount(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	assert(arg_15_2 == 1 or arg_15_2 == 0 or arg_15_2 == -1)

	local var_15_0 = arg_15_0.boxesTxt[arg_15_1]
	local var_15_1 = arg_15_0.counts[arg_15_1] + arg_15_2

	arg_15_0.counts[arg_15_1] = var_15_1

	setText(var_15_0, var_15_1)

	if arg_15_2 < 0:
		table.insert(arg_15_0.selected, arg_15_1)
		arg_15_0.UpdatePos()
	elif arg_15_2 > 0:
		table.remove(arg_15_0.selected, arg_15_3)
		arg_15_0.UpdatePos()

def var_0_0.poolId2Sprite(arg_16_0, arg_16_1):
	return arg_16_0.sprites[arg_16_1]

def var_0_0.UpdatePos(arg_17_0):
	local function var_17_0(arg_18_0, arg_18_1)
		local var_18_0 = arg_17_0.selected[arg_18_0]
		local var_18_1 = arg_18_1.Find("icon")

		if var_18_0:
			var_18_1.GetComponent(typeof(Image)).sprite = arg_17_0.poolId2Sprite(var_18_0)

			onButton(arg_17_0, var_18_1, function()
				arg_17_0.ReduceCount(var_18_0, 1, arg_18_0), SFX_PANEL)
		else
			setText(arg_18_1.Find("empty/Text"), arg_18_0)

		setActive(arg_18_1.Find("empty"), not var_18_0)
		setActive(var_18_1, var_18_0)

	arg_17_0.posListTop.make(function(arg_20_0, arg_20_1, arg_20_2)
		if arg_20_0 == UIItemList.EventUpdate:
			var_17_0(arg_20_1 + 1, arg_20_2))
	arg_17_0.posListTop.align(math.min(5, var_0_1))
	arg_17_0.posListBottom.make(function(arg_21_0, arg_21_1, arg_21_2)
		if arg_21_0 == UIItemList.EventUpdate:
			var_17_0(arg_21_1 + 6, arg_21_2))
	arg_17_0.posListBottom.align(math.max(0, math.min(5, var_0_1 - 5)))

	arg_17_0.selectedTxt.text = #arg_17_0.selected .. "/" .. var_0_1

def var_0_0.Hide(arg_22_0):
	setActive(arg_22_0._tf, False)

	arg_22_0.isShow = False

def var_0_0.OnDestroy(arg_23_0):
	return

return var_0_0
