local var_0_0 = class("SculptureScene", import("view.base.BaseUI"))

var_0_0.OPEN_GRATITUDE_PAGE = "SculptureScene.OPEN_GRATITUDE_PAGE"

local var_0_1 = 5
local var_0_2 = 6

def var_0_0.getUIName(arg_1_0):
	return "SculptureUI"

def var_0_0.SetActivity(arg_2_0, arg_2_1):
	arg_2_0.activity = arg_2_1

def var_0_0.GetBaseActivity(arg_3_0):
	return getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

def var_0_0.OnUpdateActivity(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	arg_4_0.SetActivity(arg_4_3)

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.cards):
		if iter_4_1.id == arg_4_2:
			iter_4_1.Flush(arg_4_3)

			break

	if arg_4_1 == SculptureActivity.STATE_FINSIH:
		if arg_4_0.gratitudePage and arg_4_0.gratitudePage.GetLoaded():
			arg_4_0.gratitudePage.Flush(arg_4_3)

		arg_4_0.UpdateAward()
	elif arg_4_1 == SculptureActivity.STATE_UNLOCK:
		arg_4_0.EnterDrawLinePage(arg_4_2)
		arg_4_0.UpdateRes()
	elif arg_4_1 == SculptureActivity.STATE_DRAW:
		arg_4_0.EnterPuzzlePage(arg_4_2)
	elif arg_4_1 == SculptureActivity.STATE_JOINT:
		arg_4_0.EnterPresentedPage(arg_4_2)

def var_0_0.init(arg_5_0):
	arg_5_0.backBtn = arg_5_0.findTF("back")
	arg_5_0.helpBtn = arg_5_0.findTF("help")
	arg_5_0.awardBtn = arg_5_0.findTF("award")
	arg_5_0.awardTxt = arg_5_0.findTF("award/Text").GetComponent(typeof(Text))
	arg_5_0.ore = arg_5_0.findTF("ore")
	arg_5_0.oreIcon = arg_5_0.findTF("ore/icon").GetComponent(typeof(Image))
	arg_5_0.oreTxt = arg_5_0.findTF("ore/Text").GetComponent(typeof(Text))
	arg_5_0.feather = arg_5_0.findTF("feather")
	arg_5_0.featherIcon = arg_5_0.findTF("feather/icon").GetComponent(typeof(Image))
	arg_5_0.featherTxt = arg_5_0.findTF("feather/Text").GetComponent(typeof(Text))
	arg_5_0.tpl = arg_5_0.findTF("frame/content/tpl")

	setActive(arg_5_0.tpl, False)

	arg_5_0.tpls = {}
	arg_5_0.drawLinePage = SculptureDrawLinePage.New(arg_5_0._tf, arg_5_0.event, arg_5_0.contextData)
	arg_5_0.puzzlePage = SculpturePuzzlePage.New(arg_5_0._tf, arg_5_0.event, arg_5_0.contextData)
	arg_5_0.presentedPage = SculpturePresentedPage.New(arg_5_0._tf, arg_5_0.event, arg_5_0.contextData)
	arg_5_0.gratitudePage = SculptureGratitudePage.New(arg_5_0._tf, arg_5_0.event, arg_5_0.contextDat)
	arg_5_0.awardInfoPage = SculptureAwardInfoPage.New(arg_5_0._tf, arg_5_0.event, arg_5_0.contextDat)
	arg_5_0.resMsgBoxPage = SculptureResMsgBoxPage.New(arg_5_0._tf, arg_5_0.event)
	arg_5_0.contextData.msgBoxPage = SculptureMsgBoxPage.New(arg_5_0._tf, arg_5_0.event)
	arg_5_0.contextData.tipPage = SculptureTipPage.New(arg_5_0._tf, arg_5_0.event)
	arg_5_0.contextData.miniMsgBox = SculptureMiniMsgBoxPage.New(arg_5_0._tf, arg_5_0.event)
	Input.multiTouchEnabled = False

	arg_5_0.bind(var_0_0.OPEN_GRATITUDE_PAGE, function(arg_6_0, arg_6_1)
		arg_5_0.gratitudePage.ExecuteAction("Show", arg_6_1, arg_5_0.activity, function()
			if arg_5_0.presentedPage and arg_5_0.presentedPage.GetLoaded():
				arg_5_0.presentedPage.Hide()))

def var_0_0.didEnter(arg_8_0):
	seriesAsync({
		function(arg_9_0)
			arg_8_0.UpdateResIcon()
			arg_8_0.UpdateRes()
			arg_8_0.UpdateAward()
			arg_8_0.InitMainView(arg_9_0),
		function(arg_10_0)
			arg_8_0.RegisterEvent(arg_10_0)
	})

def var_0_0.UpdateResIcon(arg_11_0):
	local var_11_0 = pg.activity_workbench_item[var_0_1]

	arg_11_0.oreIcon.sprite = LoadSprite("props/" .. var_11_0.icon)

	local var_11_1 = pg.activity_workbench_item[var_0_2]

	arg_11_0.featherIcon.sprite = LoadSprite("props/" .. var_11_1.icon)
	rtf(arg_11_0.oreIcon.gameObject).sizeDelta = Vector2(80, 80)
	rtf(arg_11_0.featherIcon.gameObject).sizeDelta = Vector2(80, 80)

def var_0_0.InitMainView(arg_12_0, arg_12_1):
	arg_12_0.cards = {}

	local var_12_0 = {}

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.activity.getConfig("config_data")):
		table.insert(var_12_0, function(arg_13_0)
			local var_13_0 = #arg_12_0.tpls > 0
			local var_13_1 = var_13_0 and table.remove(arg_12_0.tpls, 1) or Object.Instantiate(arg_12_0.tpl, arg_12_0.tpl.parent).transform

			setActive(var_13_1, True)

			local var_13_2 = arg_12_0.CreateNewCard(var_13_1, iter_12_1)

			table.insert(arg_12_0.cards, var_13_2)

			if not var_13_0:
				onNextTick(arg_13_0)
			else
				arg_13_0())

	seriesAsync(var_12_0, arg_12_1)

def var_0_0.UpdateRes(arg_14_0):
	local var_14_0 = arg_14_0.GetBaseActivity()

	arg_14_0.oreTxt.text = var_14_0.getVitemNumber(var_0_1)
	arg_14_0.featherTxt.text = var_14_0.getVitemNumber(var_0_2)

def var_0_0.UpdateAward(arg_15_0):
	local var_15_0, var_15_1 = arg_15_0.activity.GetAwardProgress()

	arg_15_0.awardTxt.text = var_15_0 .. "/" .. var_15_1

def var_0_0.CreateNewCard(arg_16_0, arg_16_1, arg_16_2):
	local var_16_0 = SculptureCard.New(arg_16_1)

	var_16_0.Update(arg_16_2, arg_16_0.activity)
	onButton(arg_16_0, var_16_0.continueBtn, function()
		local var_17_0 = arg_16_0.activity.GetSculptureState(arg_16_2)

		if var_17_0 == SculptureActivity.STATE_UNLOCK:
			arg_16_0.EnterDrawLinePage(arg_16_2)
		elif var_17_0 == SculptureActivity.STATE_DRAW:
			arg_16_0.EnterPuzzlePage(arg_16_2), SFX_PANEL)
	onButton(arg_16_0, var_16_0.lockBtn, function()
		local var_18_0, var_18_1 = arg_16_0.activity._GetComsume(arg_16_2)
		local var_18_2 = arg_16_0.activity.GetResorceName(arg_16_2)

		arg_16_0.contextData.msgBoxPage.ExecuteAction("Show", {
			nextBtn = True,
			content = arg_16_0.activity.getDataConfig(arg_16_2, "describe"),
			consume = var_18_1,
			consumeId = var_18_0,
			def onYes:()
				arg_16_0.emit(SculptureMediator.ON_UNLOCK_SCULPTURE, arg_16_2),
			iconName = arg_16_0.activity.GetResorceName(arg_16_2),
			title = var_18_2 .. "_title"
		}), SFX_PANEL)
	onButton(arg_16_0, var_16_0.finishBtn, function()
		local var_20_0 = arg_16_0.activity.GetResorceName(arg_16_2)

		arg_16_0.contextData.msgBoxPage.ExecuteAction("Show", {
			content = arg_16_0.activity.getDataConfig(arg_16_2, "describe"),
			title = var_20_0 .. "_title"
		}), SFX_PANEL)
	onButton(arg_16_0, var_16_0.tr, function()
		if arg_16_0.activity.GetSculptureState(arg_16_2) == SculptureActivity.STATE_FINSIH:
			triggerButton(var_16_0.finishBtn)
		else
			triggerButton(var_16_0.continueBtn), SFX_PANEL)
	onButton(arg_16_0, var_16_0.presentedBtn, function()
		arg_16_0.EnterPresentedPage(arg_16_2), SFX_PANEL)

	return var_16_0

def var_0_0.RegisterEvent(arg_23_0, arg_23_1):
	onButton(arg_23_0, arg_23_0.backBtn, function()
		arg_23_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_23_0, arg_23_0.awardBtn, function()
		arg_23_0.awardInfoPage.ExecuteAction("Show", arg_23_0.activity), SFX_PANEL)
	onButton(arg_23_0, arg_23_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.gift_act_help.tip
		}), SFX_PANEL)
	onButton(arg_23_0, arg_23_0.ore, function()
		arg_23_0.resMsgBoxPage.ExecuteAction("Show", var_0_1), SFX_PANEL)
	onButton(arg_23_0, arg_23_0.feather, function()
		arg_23_0.resMsgBoxPage.ExecuteAction("Show", var_0_2), SFX_PANEL)

def var_0_0.EnterDrawLinePage(arg_29_0, arg_29_1):
	arg_29_0.drawLinePage.ExecuteAction("Show", arg_29_1, arg_29_0.activity)

def var_0_0.EnterPresentedPage(arg_30_0, arg_30_1):
	arg_30_0.presentedPage.ExecuteAction("Show", arg_30_1, arg_30_0.activity, function()
		if arg_30_0.puzzlePage and arg_30_0.puzzlePage.GetLoaded():
			arg_30_0.puzzlePage.Hide())

def var_0_0.EnterPuzzlePage(arg_32_0, arg_32_1):
	arg_32_0.puzzlePage.ExecuteAction("Show", arg_32_1, arg_32_0.activity, function()
		if arg_32_0.drawLinePage and arg_32_0.drawLinePage.GetLoaded():
			arg_32_0.drawLinePage.Hide())

def var_0_0.onBackPressed(arg_34_0):
	var_0_0.super.onBackPressed(arg_34_0)

def var_0_0.willExit(arg_35_0):
	for iter_35_0, iter_35_1 in ipairs(arg_35_0.cards):
		iter_35_1.Dispose()

	arg_35_0.cards = None

	if arg_35_0.contextData.msgBoxPage:
		arg_35_0.contextData.msgBoxPage.Destroy()

		arg_35_0.contextData.msgBoxPage = None

	if arg_35_0.drawLinePage:
		arg_35_0.drawLinePage.Destroy()

		arg_35_0.drawLinePage = None

	if arg_35_0.contextData.tipPage:
		arg_35_0.contextData.tipPage.Destroy()

		arg_35_0.contextData.tipPage = None

	if arg_35_0.puzzlePage:
		arg_35_0.puzzlePage.Destroy()

		arg_35_0.puzzlePage = None

	if arg_35_0.contextData.miniMsgBox:
		arg_35_0.contextData.miniMsgBox.Destroy()

		arg_35_0.contextData.miniMsgBox = None

	if arg_35_0.awardInfoPage:
		arg_35_0.awardInfoPage.Destroy()

		arg_35_0.awardInfoPage = None

	if arg_35_0.resMsgBoxPage:
		arg_35_0.resMsgBoxPage.Destroy()

		arg_35_0.resMsgBoxPage = None

	Input.multiTouchEnabled = True

return var_0_0
