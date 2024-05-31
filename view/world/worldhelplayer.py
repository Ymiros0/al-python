local var_0_0 = class("WorldHelpLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "WorldHelpUI"

def var_0_0.init(arg_2_0):
	arg_2_0.rtTitle = arg_2_0._tf.Find("title")
	arg_2_0.btnBack = arg_2_0.rtTitle.Find("btn_back")

	onButton(arg_2_0, arg_2_0.btnBack, function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.groupList = UIItemList.New(arg_2_0.rtTitle.Find("toggles"), arg_2_0.rtTitle.Find("toggles/toggle"))

	arg_2_0.groupList.make(function(arg_4_0, arg_4_1, arg_4_2)
		arg_4_1 = arg_4_1 + 1

		if arg_4_0 == UIItemList.EventUpdate:
			local var_4_0 = arg_2_0.titles[arg_4_1]

			setText(arg_4_2.Find("Text"), pg.world_help_data[var_4_0].name)
			onToggle(arg_2_0, arg_4_2, function(arg_5_0)
				if arg_5_0:
					if arg_2_0.curGroupId != var_4_0:
						arg_2_0.toggleAnim(arg_4_2, True)
						arg_2_0.setCurGroup(var_4_0)
				else
					arg_2_0.toggleAnim(arg_4_2, False), SFX_PANEL))

	arg_2_0.rtMain = arg_2_0._tf.Find("main")
	arg_2_0.rtScroll = arg_2_0.rtMain.Find("Scroll")

	onButton(arg_2_0, arg_2_0.rtMain.Find("left"), function()
		if LeanTween.isTweening(go(arg_2_0.rtScroll)):
			return

		if arg_2_0.curPageIndex > 1:
			local var_6_0 = {}

			table.insert(var_6_0, function(arg_7_0)
				arg_2_0.pageAnim(False, arg_7_0))
			table.insert(var_6_0, function(arg_8_0)
				arg_2_0.setCurPage(arg_2_0.curPageIndex - 1)
				arg_8_0())
			table.insert(var_6_0, function(arg_9_0)
				arg_2_0.pageAnim(True, arg_9_0))
			seriesAsync(var_6_0, function()
				return))
	onButton(arg_2_0, arg_2_0.rtMain.Find("right"), function()
		if LeanTween.isTweening(go(arg_2_0.rtScroll)):
			return

		if arg_2_0.curPageIndex < #arg_2_0.pageList:
			local var_11_0 = {}

			table.insert(var_11_0, function(arg_12_0)
				arg_2_0.pageAnim(False, arg_12_0))
			table.insert(var_11_0, function(arg_13_0)
				arg_2_0.setCurPage(arg_2_0.curPageIndex + 1)
				arg_13_0())
			table.insert(var_11_0, function(arg_14_0)
				arg_2_0.pageAnim(True, arg_14_0))
			seriesAsync(var_11_0, function()
				return))

def var_0_0.setCurGroup(arg_16_0, arg_16_1):
	local var_16_0 = {}

	if arg_16_0.curGroupId:
		table.insert(var_16_0, function(arg_17_0)
			arg_16_0.pageAnim(False, arg_17_0))

	arg_16_0.curGroupId = arg_16_1

	table.insert(var_16_0, function(arg_18_0)
		local var_18_0 = pg.world_help_data[arg_16_0.curGroupId]

		arg_16_0.pageList = {}

		local var_18_1 = nowWorld().GetProgress()

		for iter_18_0, iter_18_1 in ipairs(var_18_0.stage_help):
			if var_18_1 >= iter_18_1[1]:
				table.insert(arg_16_0.pageList, {
					id = iter_18_0,
					path = iter_18_1[2]
				})

		if #arg_16_0.pageList > 0:
			arg_16_0.setCurPage(1)

		arg_18_0())
	seriesAsync(var_16_0, function()
		arg_16_0.pageAnim(True))

def var_0_0.setCurPage(arg_20_0, arg_20_1):
	arg_20_0.curPageIndex = arg_20_1

	setText(arg_20_0.rtMain.Find("page/Text"), arg_20_0.curPageIndex .. "/" .. #arg_20_0.pageList)

	local var_20_0 = arg_20_0.rtScroll.Find("Card")

	setImageAlpha(var_20_0.Find("Image"), 0)
	GetSpriteFromAtlasAsync(arg_20_0.pageList[arg_20_1].path, "", function(arg_21_0)
		if arg_20_0.curPageIndex == arg_20_1:
			setImageSprite(var_20_0.Find("Image"), arg_21_0)
			setImageAlpha(var_20_0.Find("Image"), 1))

def var_0_0.getPageIndex(arg_22_0, arg_22_1):
	for iter_22_0, iter_22_1 in ipairs(arg_22_0.pageList):
		if iter_22_1.id == arg_22_1:
			return iter_22_0

	return 1

def var_0_0.pageAnim(arg_23_0, arg_23_1, arg_23_2):
	LeanTween.cancel(go(arg_23_0.rtScroll))

	local var_23_0 = GetOrAddComponent(arg_23_0.rtScroll, "CanvasGroup")

	var_23_0.alpha = arg_23_1 and 0 or 1

	LeanTween.alphaCanvas(var_23_0, arg_23_1 and 1 or 0, 0.3).setOnComplete(System.Action(function()
		return existCall(arg_23_2)))

def var_0_0.toggleAnim(arg_25_0, arg_25_1, arg_25_2):
	LeanTween.cancel(arg_25_1.gameObject)

	local var_25_0 = GetComponent(arg_25_1, typeof(LayoutElement))

	if arg_25_2:
		LeanTween.value(arg_25_1.gameObject, var_25_0.preferredWidth, 238, 0.15).setOnUpdate(System.Action_float(function(arg_26_0)
			var_25_0.preferredWidth = arg_26_0)).setOnComplete(System.Action(function()
			setActive(arg_25_1.Find("selected"), arg_25_2)))
	else
		setActive(arg_25_1.Find("selected"), arg_25_2)
		LeanTween.value(arg_25_1.gameObject, var_25_0.preferredWidth, 176, 0.15).setOnUpdate(System.Action_float(function(arg_28_0)
			var_25_0.preferredWidth = arg_28_0))

def var_0_0.didEnter(arg_29_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_29_0._tf)

	local var_29_0

	arg_29_0.titles = {}

	local var_29_1 = nowWorld().GetProgress()

	for iter_29_0, iter_29_1 in ipairs(pg.world_help_data.all):
		if var_29_1 >= pg.world_help_data[iter_29_1].stage:
			table.insert(arg_29_0.titles, iter_29_1)

			if arg_29_0.contextData.titleId == iter_29_1:
				var_29_0 = #arg_29_0.titles

	arg_29_0.groupList.align(#arg_29_0.titles)
	setActive(arg_29_0.rtScroll, #arg_29_0.titles > 0)

	if #arg_29_0.titles > 0:
		if var_29_0:
			triggerToggle(arg_29_0.groupList.container.GetChild(var_29_0 - 1), True)
			arg_29_0.setCurPage(arg_29_0.getPageIndex(arg_29_0.contextData.pageId))
		else
			triggerToggle(arg_29_0.groupList.container.GetChild(0), True)

def var_0_0.willExit(arg_30_0):
	LeanTween.cancel(go(arg_30_0.rtScroll))
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_30_0._tf)

return var_0_0
