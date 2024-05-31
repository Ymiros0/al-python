local var_0_0 = class("TechnologySettingsLayer", import("..base.BaseUI"))

var_0_0.TEC_PAGE_TENDENCY = 1
var_0_0.TEC_PAGE_CATCHUP_TARGET1 = 2
var_0_0.TEC_PAGE_CATCHUP_TARGET2 = 3
var_0_0.TEC_PAGE_CATCHUP_TARGET3 = 4
var_0_0.TEC_PAGE_CATCHUP_TARGET4 = 5
var_0_0.TEC_PAGE_CATCHUP_TARGET5 = 6
var_0_0.TEC_PAGE_CATCHUP_ACT = 99
var_0_0.PANEL_INTO_TIME = 0.15
var_0_0.SELECT_TENDENCY_FADE_TIME = 0.3
var_0_0.SELECT_CHAR_LIGHT_FADE_TIME = 0.3
var_0_0.CATCHUP_CLASSES = {
	import("view.technology.TargetCatchup.TargetCatchupPanel1"),
	import("view.technology.TargetCatchup.TargetCatchupPanel2"),
	import("view.technology.TargetCatchup.TargetCatchupPanel3"),
	import("view.technology.TargetCatchup.TargetCatchupPanel4"),
	import("view.technology.TargetCatchup.TargetCatchupPanel5")
}
var_0_0.CATCHUP_VERSION = 5

def var_0_0.getUIName(arg_1_0):
	return "TechnologySettingsUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()
	arg_2_0.initTendencyPage()
	arg_2_0.initActCatchupPage()

def var_0_0.didEnter(arg_3_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf)
	arg_3_0.resetLeftBtnUnsel()
	arg_3_0.updateTendencyBtn(arg_3_0.curTendency)
	arg_3_0.updateTargetCatchupBtns()
	arg_3_0.updateActCatchupBtn()
	triggerButton(arg_3_0.leftBtnList[1])
	triggerToggle(arg_3_0.showFinish, arg_3_0.showFinishFlag == 1 and True or False)

def var_0_0.willExit(arg_4_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf)

	if arg_4_0.actCatchupTimer:
		arg_4_0.actCatchupTimer.Stop()

		arg_4_0.actCatchupTimer = None

	for iter_4_0, iter_4_1 in pairs(arg_4_0.catchupPanels):
		iter_4_1.willExit()

	arg_4_0.loader.Clear()

def var_0_0.initData(arg_5_0):
	arg_5_0.technologyProxy = getProxy(TechnologyProxy)
	arg_5_0.bayProxy = getProxy(BayProxy)
	arg_5_0.bagProxy = getProxy(BagProxy)
	arg_5_0.curPageID = 0
	arg_5_0.curTendency = arg_5_0.technologyProxy.getTendency(2)
	arg_5_0.curSelectedIndex = 0
	arg_5_0.reSelectTag = False
	arg_5_0.actCatchup = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BLUEPRINT_CATCHUP)
	arg_5_0.isShowActCatchup = arg_5_0.actCatchup and not arg_5_0.actCatchup.isEnd()
	arg_5_0.loader = AutoLoader.New()

def var_0_0.findUI(arg_6_0):
	arg_6_0.bg = arg_6_0.findTF("BG")

	local var_6_0 = arg_6_0.findTF("BackTips/ClickText", arg_6_0.bg)

	setText(var_6_0, i18n("click_back_tip"))

	local var_6_1 = arg_6_0.findTF("Panel")
	local var_6_2 = arg_6_0.findTF("LeftScrollViewMask/LeftScrollView/LeftBtnList", var_6_1)

	arg_6_0.leftBtnList = {}
	arg_6_0.tendencyBtn = arg_6_0.findTF("TendencyBtn", var_6_2)
	arg_6_0.leftBtnList[var_0_0.TEC_PAGE_TENDENCY] = arg_6_0.tendencyBtn
	arg_6_0.catchupBtns = {}

	for iter_6_0 = 1, var_0_0.CATCHUP_VERSION:
		arg_6_0.catchupBtns[iter_6_0] = cloneTplTo(arg_6_0.findTF("TargetCatchupBtn_tpl", var_6_2), var_6_2)
		arg_6_0.leftBtnList[iter_6_0 + 1] = arg_6_0.catchupBtns[iter_6_0]

	arg_6_0.actCatchupBtn = arg_6_0.findTF("ActCatchupBtn", var_6_2)

	arg_6_0.actCatchupBtn.SetAsLastSibling()

	arg_6_0.leftBtnList[var_0_0.TEC_PAGE_CATCHUP_ACT] = arg_6_0.actCatchupBtn

	local var_6_3 = arg_6_0.findTF("RightPanelContainer", var_6_1)

	arg_6_0.rightPageTFList = {}
	arg_6_0.tendencyPanel = arg_6_0.findTF("TecTendencyPanel", var_6_3)
	arg_6_0.rightPageTFList[var_0_0.TEC_PAGE_TENDENCY] = arg_6_0.tendencyPanel
	arg_6_0.catchupPanels = {}
	arg_6_0.actCatchupPanel = arg_6_0.findTF("ActCatchupPanel", var_6_3)
	arg_6_0.rightPageTFList[var_0_0.TEC_PAGE_CATCHUP_ACT] = arg_6_0.actCatchupPanel
	arg_6_0.showFinish = arg_6_0.findTF("ShowFinishToggle")

	setText(arg_6_0.findTF("Label", arg_6_0.showFinish), i18n("tec_target_catchup_show_the_finished_version"))

	arg_6_0.showFinishFlag = PlayerPrefs.GetInt("isShowFinishCatchupVersion") or 0

	if var_0_0.CATCHUP_VERSION < 1:
		setActive(arg_6_0.showFinish, False)

def var_0_0.addListener(arg_7_0):
	onButton(arg_7_0, arg_7_0.bg, function()
		arg_7_0.closeView(), SFX_PANEL)

	for iter_7_0, iter_7_1 in pairs(arg_7_0.leftBtnList):
		onButton(arg_7_0, iter_7_1, function()
			if arg_7_0.onPageSwitchAnim:
				return

			if arg_7_0.curPageID != iter_7_0:
				arg_7_0.resetLeftBtnUnsel()
				setActive(arg_7_0.findTF("Selected", iter_7_1), True)
				arg_7_0.switchRightPage(iter_7_0), SFX_PANEL)

	onToggle(arg_7_0, arg_7_0.showFinish, function(arg_10_0)
		if var_0_0.CATCHUP_VERSION < 1:
			return

		for iter_10_0, iter_10_1 in pairs(arg_7_0.catchupBtns):
			if iter_10_0 <= var_0_0.CATCHUP_VERSION:
				if arg_7_0.technologyProxy.getCatchupState(iter_10_0) == TechnologyCatchup.STATE_FINISHED_ALL and not arg_10_0:
					setActive(iter_10_1, False)
				else
					setActive(iter_10_1, True)

		arg_7_0.showFinishFlag = arg_10_0 and 1 or 0

		PlayerPrefs.SetInt("isShowFinishCatchupVersion", arg_7_0.showFinishFlag)
		triggerButton(arg_7_0.leftBtnList[1]), SFX_PANEL)

def var_0_0.resetLeftBtnUnsel(arg_11_0):
	for iter_11_0, iter_11_1 in pairs(arg_11_0.leftBtnList):
		local var_11_0 = arg_11_0.findTF("Selected", iter_11_1)

		setActive(var_11_0, False)

def var_0_0.switchRightPage(arg_12_0, arg_12_1):
	seriesAsync({
		function(arg_13_0)
			if not arg_12_0.rightPageTFList[arg_12_1]:
				local var_13_0 = arg_12_1 - 1
				local var_13_1 = arg_12_0.findTF("Panel/RightPanelContainer")

				arg_12_0.catchupPanels[var_13_0] = var_0_0.CATCHUP_CLASSES[var_13_0].New(None, function()
					arg_12_0.rightPageTFList[arg_12_1] = arg_12_0.catchupPanels[var_13_0]._go

					setActive(arg_12_0.rightPageTFList[arg_12_1], False)
					SetParent(arg_12_0.rightPageTFList[arg_12_1], var_13_1, False)
					arg_13_0())
			else
				arg_13_0(),
		function(arg_15_0)
			local var_15_0 = arg_12_0.rightPageTFList[arg_12_0.curPageID]
			local var_15_1 = arg_12_0.rightPageTFList[arg_12_1]

			setActive(var_15_1, True)

			arg_12_0.onPageSwitchAnim = True

			arg_12_0.managedTween(LeanTween.alphaCanvas, function()
				arg_12_0.onPageSwitchAnim = False, GetOrAddComponent(var_15_1, typeof(CanvasGroup)), 1, var_0_0.PANEL_INTO_TIME).setFrom(0)

			if var_15_0:
				arg_12_0.managedTween(LeanTween.alphaCanvas, function()
					setActive(var_15_0, False), GetOrAddComponent(var_15_0, typeof(CanvasGroup)), 0, var_0_0.PANEL_INTO_TIME).setFrom(1)

			arg_12_0.curPageID = arg_12_1

			if arg_12_1 == var_0_0.TEC_PAGE_TENDENCY:
				arg_12_0.updateTendencyPage(arg_12_0.curTendency)
			elif arg_12_1 == var_0_0.TEC_PAGE_CATCHUP_ACT:
				arg_12_0.updateActCatchupPage()
			else
				arg_12_0.updateTargetCatchupPage(arg_12_1 - 1)
	})

def var_0_0.initTendencyPage(arg_18_0):
	local var_18_0 = getProxy(TechnologyProxy).getConfigMaxVersion()
	local var_18_1 = arg_18_0.findTF("TecItemList", arg_18_0.tendencyPanel)
	local var_18_2 = UIItemList.New(var_18_1, var_18_1.Find("tpl"))

	var_18_2.make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventUpdate:
			local var_19_0 = arg_19_1 > 0 and i18n("tec_tendency_x", i18n("number_" .. arg_19_1)) or i18n("tec_tendency_0")

			setText(arg_19_2.Find("UnSelect/Text"), var_19_0)
			setText(arg_19_2.Find("Selected/Text"), var_19_0)
			onButton(arg_18_0, arg_19_2, function()
				if arg_18_0.curTendency != arg_19_1:
					arg_18_0.emit(TechnologySettingsMediator.CHANGE_TENDENCY, arg_19_1), SFX_PANEL))
	var_18_2.align(var_18_0 + 1)

def var_0_0.updateTendencyPage(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_0.findTF("TecItemList", arg_21_0.tendencyPanel)

	setActive(var_21_0.GetChild(arg_21_0.curTendency).Find("Selected"), False)

	local var_21_1 = var_21_0.GetChild(arg_21_1).Find("Selected")

	setActive(var_21_1, True)
	setImageAlpha(var_21_1.Find("Image"), 0)
	arg_21_0.managedTween(LeanTween.alpha, None, var_21_1.Find("Image"), 1, var_0_0.SELECT_TENDENCY_FADE_TIME).setFrom(0)

	local var_21_2 = arg_21_0.findTF("TendencyNum", arg_21_0.tendencyPanel)

	setImageAlpha(var_21_2.Find("Image"), 0)

	if arg_21_1 > 0:
		GetImageSpriteFromAtlasAsync("ui/technologysettingsui_atlas", "right_tendency_num_" .. arg_21_1, var_21_2.Find("Image"), True)
		arg_21_0.managedTween(LeanTween.alpha, None, var_21_2.Find("Image"), 1, var_0_0.SELECT_TENDENCY_FADE_TIME).setFrom(0)

	arg_21_0.curTendency = arg_21_1

def var_0_0.updateTendencyBtn(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_1 > 0 and i18n("tec_tendency_cur_x", i18n("number_" .. arg_22_1)) or i18n("tec_tendency_cur_0")

	setText(arg_22_0.tendencyBtn.Find("UnSelect/Text"), var_22_0)
	setText(arg_22_0.tendencyBtn.Find("Selected/Text"), var_22_0)

def var_0_0.updateTargetCatchupPage(arg_23_0, arg_23_1):
	arg_23_0.catchupPanels[arg_23_1].updateTargetCatchupPage()

def var_0_0.updateTargetCatchupBtns(arg_24_0):
	for iter_24_0, iter_24_1 in pairs(arg_24_0.catchupBtns):
		if iter_24_0 <= var_0_0.CATCHUP_VERSION:
			local var_24_0 = arg_24_0.technologyProxy.getCatchupState(iter_24_0)
			local var_24_1 = var_24_0 == TechnologyCatchup.STATE_CATCHUPING
			local var_24_2 = arg_24_0.findTF("UnSelect/Text", iter_24_1)
			local var_24_3 = arg_24_0.findTF("Selected/Text", iter_24_1)
			local var_24_4 = arg_24_0.findTF("UnSelect/CharImg", iter_24_1)
			local var_24_5 = arg_24_0.findTF("Selected/CharImg", iter_24_1)
			local var_24_6 = arg_24_0.findTF("ProgressText", var_24_4)
			local var_24_7 = arg_24_0.findTF("ProgressText", var_24_5)

			setActive(var_24_4, var_24_1)
			setActive(var_24_5, var_24_1)

			if var_24_1:
				local var_24_8 = iter_24_0 > 0 and i18n("tec_target_catchup_selected_x", i18n("number_" .. iter_24_0)) or i18n("tec_target_catchup_selected_0")

				setText(var_24_2, var_24_8)
				setText(var_24_3, var_24_8)

				local var_24_9 = arg_24_0.technologyProxy.getCurCatchupTecInfo()
				local var_24_10 = var_24_9.tecID
				local var_24_11 = var_24_9.groupID
				local var_24_12 = var_24_9.printNum
				local var_24_13 = arg_24_0.technologyProxy.getCatchupData(var_24_10).isUr(var_24_11) and pg.technology_catchup_template[var_24_10].obtain_max_per_ur or pg.technology_catchup_template[var_24_10].obtain_max

				setImageSprite(var_24_4, LoadSprite("TecCatchup/QChar" .. var_24_11, tostring(var_24_11)))
				setImageSprite(var_24_5, LoadSprite("TecCatchup/QChar" .. var_24_11, tostring(var_24_11)))
				setText(var_24_6, var_24_12 .. "/" .. var_24_13)
				setText(var_24_7, var_24_12 .. "/" .. var_24_13)
			elif var_24_0 == TechnologyCatchup.STATE_UNSELECT:
				local var_24_14 = iter_24_0 > 0 and i18n("tec_target_catchup_none_x", i18n("number_" .. iter_24_0)) or i18n("tec_target_catchup_none_0")

				setText(var_24_2, var_24_14)
				setText(var_24_3, var_24_14)
			elif var_24_0 == TechnologyCatchup.STATE_FINISHED_ALL:
				local var_24_15 = iter_24_0 > 0 and i18n("tec_target_catchup_finish_x", i18n("number_" .. iter_24_0)) or i18n("tec_target_catchup_finish_0")

				setText(var_24_2, var_24_15)
				setText(var_24_3, var_24_15)

def var_0_0.initActCatchupPage(arg_25_0):
	if arg_25_0.isShowActCatchup:
		local var_25_0 = arg_25_0.actCatchup.getConfig("page_info").ui_name

		arg_25_0.loader.GetPrefab("ui/" .. var_25_0, "", function(arg_26_0)
			setParent(arg_26_0, arg_25_0.actCatchupPanel)
			setLocalScale(arg_26_0, {
				x = 0.925,
				y = 0.923
			})
			setAnchoredPosition(arg_26_0, Vector2.zero)

			arg_25_0.actCatchupTF = arg_25_0.findTF("AD", tf(arg_26_0))
			arg_25_0.actCatchupItemTF = arg_25_0.findTF("Award", arg_25_0.actCatchupTF)
			arg_25_0.actCatchupSliderTF = arg_25_0.findTF("Slider", arg_25_0.actCatchupTF)
			arg_25_0.actCatchupProgressText = arg_25_0.findTF("Progress", arg_25_0.actCatchupTF)

			local var_26_0 = arg_25_0.findTF("GoBtn", arg_25_0.actCatchupTF)

			if var_26_0:
				setActive(var_26_0, False)

			local var_26_1 = arg_25_0.findTF("FinishBtn", arg_25_0.actCatchupTF)

			if var_26_1:
				setActive(var_26_1, False)

			local var_26_2 = arg_25_0.actCatchup.data1
			local var_26_3 = arg_25_0.actCatchup.getConfig("config_id")
			local var_26_4 = pg.activity_event_blueprint_catchup[var_26_3].obtain_max
			local var_26_5 = arg_25_0.actCatchup.getConfig("config_client").itemid
			local var_26_6 = {
				type = DROP_TYPE_ITEM,
				id = var_26_5
			}

			updateDrop(arg_25_0.actCatchupItemTF, var_26_6)
			onButton(arg_25_0, arg_25_0.actCatchupItemTF, function()
				arg_25_0.emit(BaseUI.ON_DROP, var_26_6), SFX_PANEL)
			setSlider(arg_25_0.actCatchupSliderTF, 0, var_26_4, var_26_2)
			setText(arg_25_0.actCatchupProgressText, var_26_2 .. "/" .. var_26_4)
			setActive(arg_26_0, True))

def var_0_0.updateActCatchupPage(arg_28_0):
	return

def var_0_0.updateActCatchupBtn(arg_29_0):
	local var_29_0 = arg_29_0.findTF("UnSelect/Text", arg_29_0.actCatchupBtn)
	local var_29_1 = arg_29_0.findTF("Selected/Text", arg_29_0.actCatchupBtn)

	setText(var_29_0, i18n("tec_act_catchup_btn_word"))
	setText(var_29_1, i18n("tec_act_catchup_btn_word"))

	local var_29_2 = arg_29_0.findTF("UnSelect/CharImg", arg_29_0.actCatchupBtn)
	local var_29_3 = arg_29_0.findTF("Selected/CharImg", arg_29_0.actCatchupBtn)
	local var_29_4 = arg_29_0.findTF("ProgressText", var_29_2)
	local var_29_5 = arg_29_0.findTF("ProgressText", var_29_3)
	local var_29_6 = False
	local var_29_7 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BLUEPRINT_CATCHUP)

	if var_29_7 and not var_29_7.isEnd():
		local var_29_8 = var_29_7.data1
		local var_29_9 = var_29_7.getConfig("config_id")
		local var_29_10 = pg.activity_event_blueprint_catchup[var_29_9].char_choice
		local var_29_11 = pg.activity_event_blueprint_catchup[var_29_9].obtain_max

		setImageSprite(var_29_2, LoadSprite("TecCatchup/QChar" .. var_29_10, tostring(var_29_10)))
		setImageSprite(var_29_3, LoadSprite("TecCatchup/QChar" .. var_29_10, tostring(var_29_10)))
		setText(var_29_4, var_29_8 .. "/" .. var_29_11)
		setText(var_29_5, var_29_8 .. "/" .. var_29_11)

		local var_29_12 = var_29_7.stopTime - pg.TimeMgr.GetInstance().GetServerTime()

		if arg_29_0.actCatchupTimer:
			arg_29_0.actCatchupTimer.Stop()

			arg_29_0.actCatchupTimer = None

		local var_29_13 = arg_29_0.findTF("TimeLeft/Day", arg_29_0.actCatchupBtn)
		local var_29_14 = arg_29_0.findTF("TimeLeft/Hour", arg_29_0.actCatchupBtn)
		local var_29_15 = arg_29_0.findTF("TimeLeft/Min", arg_29_0.actCatchupBtn)
		local var_29_16 = arg_29_0.findTF("TimeLeft/NumText", arg_29_0.actCatchupBtn)

		local function var_29_17()
			local var_30_0, var_30_1, var_30_2, var_30_3 = pg.TimeMgr.GetInstance().parseTimeFrom(var_29_12)

			var_29_12 = var_29_12 - 1

			if var_30_0 >= 1:
				setActive(var_29_13, True)
				setActive(var_29_14, False)
				setActive(var_29_15, False)
				setText(var_29_16, var_30_0)
			elif var_30_0 <= 0 and var_30_1 > 0:
				setActive(var_29_13, False)
				setActive(var_29_14, True)
				setActive(var_29_15, False)
				setText(var_29_16, var_30_1)
			elif var_30_0 <= 0 and var_30_1 <= 0 and (var_30_2 > 0 or var_30_3 > 0):
				setActive(var_29_13, False)
				setActive(var_29_14, False)
				setActive(var_29_15, True)
				setText(var_29_16, math.max(var_30_2, 1))
			elif var_30_0 <= 0 and var_30_1 <= 0 and var_30_2 <= 0 and var_30_3 <= 0 and arg_29_0.actCatchupTimer:
				arg_29_0.actCatchupTimer.Stop()

				arg_29_0.actCatchupTimer = None

				arg_29_0.switchRightPage(var_0_0.TEC_PAGE_TENDENCY)
				setActive(arg_29_0.actCatchupBtn, False)

		arg_29_0.actCatchupTimer = Timer.New(var_29_17, 1, -1, 1)

		arg_29_0.actCatchupTimer.Start()
		arg_29_0.actCatchupTimer.func()

		var_29_6 = True

	setActive(arg_29_0.actCatchupBtn, var_29_6)

return var_0_0
