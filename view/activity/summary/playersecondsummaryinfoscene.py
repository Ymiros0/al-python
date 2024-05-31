local var_0_0 = class("PlayerSecondSummaryInfoScene", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "PlayerSecondSummaryUI"

def var_0_0.setActivity(arg_2_0, arg_2_1):
	arg_2_0.activityVO = arg_2_1

def var_0_0.setPlayer(arg_3_0, arg_3_1):
	arg_3_0.palyerVO = arg_3_1

def var_0_0.setSummaryInfo(arg_4_0, arg_4_1):
	arg_4_0.summaryInfoVO = arg_4_1

def var_0_0.init(arg_5_0):
	arg_5_0.backBtn = arg_5_0.findTF("bg/back_btn")
	arg_5_0.pageContainer = arg_5_0.findTF("bg/main/pages")
	arg_5_0.pageFootContainer = arg_5_0.findTF("bg/main/foots")

	GetOrAddComponent(arg_5_0.pageFootContainer, typeof(CanvasGroup))
	setCanvasGroupAlpha(arg_5_0.pageFootContainer, 0)

def var_0_0.didEnter(arg_6_0):
	if arg_6_0.summaryInfoVO:
		arg_6_0.initSummaryInfo()
	else
		arg_6_0.emit(PlayerSummaryInfoMediator.GET_PLAYER_SUMMARY_INFO)

	onButton(arg_6_0, arg_6_0.backBtn, function()
		if arg_6_0.inAnim():
			return

		arg_6_0.closeView(), SFX_CANCEL)

def var_0_0.inAnim(arg_8_0):
	return arg_8_0.inAniming or arg_8_0.currPage and arg_8_0.pages[arg_8_0.currPage].inAnim()

def var_0_0.initSummaryInfo(arg_9_0):
	arg_9_0.loadingPage = SecondSummaryPage1.New(arg_9_0.findTF("page1", arg_9_0.pageContainer))

	arg_9_0.loadingPage.Init(arg_9_0.summaryInfoVO)

	arg_9_0.pages = {}

	local function var_9_0(arg_10_0, arg_10_1, arg_10_2)
		setActive(arg_10_0, False)

		local var_10_0 = arg_10_1.New(arg_10_0)

		table.insert(arg_9_0.pages, var_10_0)
		var_10_0.Init(arg_10_2)

	var_9_0(arg_9_0.pageContainer.Find("page2"), SecondSummaryPage2, arg_9_0.summaryInfoVO)
	var_9_0(arg_9_0.pageContainer.Find("page3"), SecondSummaryPage3, arg_9_0.summaryInfoVO)
	var_9_0(arg_9_0.pageContainer.Find("page6"), SecondSummaryPage6, arg_9_0.summaryInfoVO)

	local var_9_1 = arg_9_0.pageContainer.Find("page4")

	setActive(var_9_1, False)

	local var_9_2 = 0

	if #arg_9_0.summaryInfoVO.medalList > 0:
		var_9_2 = math.floor((#arg_9_0.summaryInfoVO.medalList - 1) / SecondSummaryPage4.PerPageCount) + 1

	for iter_9_0 = 1, var_9_2:
		var_9_0(cloneTplTo(var_9_1, arg_9_0.pageContainer, "page4_1_" .. iter_9_0), SecondSummaryPage4, setmetatable({
			pageType = SecondSummaryPage4.PageTypeFurniture,
			samePage = iter_9_0,
			activityVO = arg_9_0.activityVO
		}, {
			__index = arg_9_0.summaryInfoVO
		}))

	local var_9_3 = 0

	if #arg_9_0.summaryInfoVO.iconFrameList > 0:
		var_9_3 = math.floor((#arg_9_0.summaryInfoVO.iconFrameList - 1) / SecondSummaryPage4.PerPageCount) + 1

	for iter_9_1 = 1, var_9_3:
		var_9_0(cloneTplTo(var_9_1, arg_9_0.pageContainer, "page4_2_" .. iter_9_1), SecondSummaryPage4, setmetatable({
			pageType = SecondSummaryPage4.PageTypeIconFrame,
			samePage = iter_9_1,
			activityVO = arg_9_0.activityVO
		}, {
			__index = arg_9_0.summaryInfoVO
		}))

	var_9_0(arg_9_0.pageContainer.Find("page5"), SecondSummaryPage5, arg_9_0.summaryInfoVO)
	onButton(arg_9_0, arg_9_0.findTF("page5/share", arg_9_0.pageContainer), function()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeSecondSummary), SFX_CONFIRM)
	seriesAsync({
		function(arg_12_0)
			arg_9_0.inAniming = True

			arg_9_0.loadingPage.Show(arg_12_0),
		function(arg_13_0)
			arg_9_0.inAniming = False

			arg_9_0.loadingPage.Hide()
			arg_13_0()
	}, function()
		arg_9_0.registerDrag()
		arg_9_0.registerFootEvent(1))

def var_0_0.registerFootEvent(arg_15_0, arg_15_1):
	local var_15_0 = UIItemList.New(arg_15_0.pageFootContainer, arg_15_0.pageFootContainer.Find("dot"))

	var_15_0.make(function(arg_16_0, arg_16_1, arg_16_2)
		local var_16_0 = arg_16_1 + 1

		if arg_16_0 == UIItemList.EventUpdate:
			onToggle(arg_15_0, arg_16_2, function(arg_17_0)
				if arg_17_0:
					arg_15_0.pages[var_16_0].Show()

					arg_15_0.currPage = var_16_0
				else
					arg_15_0.pages[var_16_0].Hide()))
	var_15_0.align(#arg_15_0.pages)
	setCanvasGroupAlpha(arg_15_0.pageFootContainer, 1)
	triggerToggle(arg_15_0.pageFootContainer.GetChild(arg_15_1 - 1), True)

def var_0_0.registerDrag(arg_18_0):
	arg_18_0.addVerticalDrag(arg_18_0.findTF("bg"), function()
		arg_18_0.updatePageFoot(arg_18_0.currPage - 1), function()
		arg_18_0.updatePageFoot(arg_18_0.currPage + 1))

def var_0_0.updatePageFoot(arg_21_0, arg_21_1):
	if arg_21_0.inAnim() or not arg_21_0.pages[arg_21_1]:
		return

	triggerToggle(arg_21_0.pageFootContainer.GetChild(arg_21_1 - 1), True)

def var_0_0.addVerticalDrag(arg_22_0, arg_22_1, arg_22_2, arg_22_3):
	local var_22_0 = GetOrAddComponent(arg_22_1, "EventTriggerListener")
	local var_22_1
	local var_22_2 = 0
	local var_22_3 = 50

	var_22_0.AddBeginDragFunc(function(arg_23_0, arg_23_1)
		var_22_2 = 0
		var_22_1 = arg_23_1.position)
	var_22_0.AddDragFunc(function(arg_24_0, arg_24_1)
		var_22_2 = arg_24_1.position.x - var_22_1.x)
	var_22_0.AddDragEndFunc(function(arg_25_0, arg_25_1)
		if var_22_2 < -var_22_3:
			if arg_22_3:
				arg_22_3()
		elif var_22_2 > var_22_3 and arg_22_2:
			arg_22_2())

def var_0_0.willExit(arg_26_0):
	for iter_26_0, iter_26_1 in pairs(arg_26_0.pages):
		iter_26_1.Dispose()

	arg_26_0.pages = None
	arg_26_0.currPage = None

return var_0_0
