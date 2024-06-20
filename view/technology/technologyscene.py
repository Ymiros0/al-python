local var_0_0 = class("TechnologyScene", import("..base.BaseUI"))

var_0_0.PageBase = 1
var_0_0.PageQueue = 2
var_0_0.rarityColor = {
	["1"] = {
		"#4B7BC6FF",
		{
			0.06274509803921569,
			0.29411764705882354,
			0.8745098039215686,
			0.6705882352941176
		}
	},
	["2"] = {
		"#776AB0FF",
		{
			0.29411764705882354,
			0.23529411764705882,
			0.5764705882352941,
			0.6705882352941176
		}
	},
	["3"] = {
		"#B76642FF",
		{
			0.7490196078431373,
			0.28627450980392155,
			0.06274509803921569,
			0.6705882352941176
		}
	},
	["4"] = {
		"#368B78FF",
		{
			0.12941176470588237,
			0.4980392156862745,
			0.5019607843137255,
			0.6705882352941176
		}
	}
}

def var_0_0.getUIName(arg_1_0):
	return "TechnologyUI"

def var_0_0.onBackPressed(arg_2_0):
	if arg_2_0.contextData.selectedIndex:
		arg_2_0.cancelSelected()

		return

	if arg_2_0.contextData.page == var_0_0.PageQueue:
		arg_2_0.setPage(var_0_0.PageBase)

		return

	var_0_0.super.onBackPressed(arg_2_0)

def var_0_0.ResUISettings(arg_3_0):
	return True

def var_0_0.setTechnologys(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.technologyVOs = arg_4_1
	arg_4_0.technologyQueue = arg_4_2

def var_0_0.setRefreshFlag(arg_5_0, arg_5_1):
	arg_5_0.flag = arg_5_1

def var_0_0.setPlayer(arg_6_0, arg_6_1):
	arg_6_0.player = arg_6_1

def var_0_0.init(arg_7_0):
	arg_7_0.backBtn = arg_7_0._tf.Find("blur_panel/adapt/top/back")
	arg_7_0.basePage = arg_7_0._tf.Find("main/base_page")
	arg_7_0.srcollView = arg_7_0.basePage.Find("srcoll_rect/content")
	arg_7_0.srcollViewCG = arg_7_0.srcollView.GetComponent(typeof(CanvasGroup))
	arg_7_0.helpBtn = arg_7_0.basePage.Find("help_btn")
	arg_7_0.refreshBtn = arg_7_0.basePage.Find("refresh_btn")

	setText(arg_7_0.refreshBtn.Find("Text"), i18n("technology_daily_refresh"))

	arg_7_0.settingsBtn = arg_7_0.basePage.Find("settings_btn")
	arg_7_0.selectetPanel = arg_7_0.basePage.Find("selecte_panel")

	setActive(arg_7_0.selectetPanel, False)
	setText(arg_7_0.selectetPanel.Find("consume_panel/bg/label/Text"), i18n("technology_consume"))
	setText(arg_7_0.selectetPanel.Find("consume_panel/bg/task_panel/label/Text"), i18n("technology_request"))

	arg_7_0.arrLeftBtn = arg_7_0.selectetPanel.Find("left_arr_btn")
	arg_7_0.arrRightBtn = arg_7_0.selectetPanel.Find("right_arr_btn")
	arg_7_0.technologyTpl = arg_7_0.selectetPanel.Find("technology_card")
	arg_7_0.descTxt = arg_7_0.selectetPanel.Find("desc/bg/Text").GetComponent(typeof(Text))
	arg_7_0.timerTxt = arg_7_0.selectetPanel.Find("timer/bg/Text").GetComponent(typeof(Text))
	arg_7_0.itemContainer = arg_7_0.selectetPanel.Find("consume_panel/bg/container")
	arg_7_0.itemTpl = arg_7_0.findTF("item_tpl", arg_7_0.itemContainer)
	arg_7_0.emptyTF = arg_7_0.selectetPanel.Find("consume_panel/bg/empty")
	arg_7_0.taskPanel = arg_7_0.selectetPanel.Find("consume_panel/bg/task_panel")
	arg_7_0.taskSlider = arg_7_0.taskPanel.Find("slider").GetComponent(typeof(Slider))
	arg_7_0.taskDesc = arg_7_0.taskPanel.Find("slider/Text").GetComponent(typeof(Text))
	arg_7_0.descBG = arg_7_0.selectetPanel.Find("desc/bg").GetComponent(typeof(Image))
	arg_7_0.queuePage = arg_7_0._tf.Find("main/queue_page")
	arg_7_0.queueView = arg_7_0.queuePage.Find("queue_rect/content")

	local var_7_0 = arg_7_0._tf.Find("blur_panel/adapt/right")

	arg_7_0.btnAwardQueue = var_7_0.Find("btn_award")

	setText(arg_7_0.btnAwardQueue.Find("Text"), i18n("technology_queue_getaward"))

	arg_7_0.btnAwardQueueDisable = var_7_0.Find("btn_award_disable")

	setText(arg_7_0.btnAwardQueueDisable.Find("Text"), i18n("technology_queue_getaward"))

	arg_7_0.btnQueue = arg_7_0._tf.Find("blur_panel/adapt/left/btn_queue")
	arg_7_0.cardtimer = {}
	arg_7_0.queueTimer = {}
	arg_7_0.queueCardTimer = {}

def var_0_0.updateSettingsBtn(arg_8_0):
	local var_8_0 = arg_8_0.findTF("RedPoint", arg_8_0.settingsBtn)
	local var_8_1 = arg_8_0.findTF("TipText", arg_8_0.settingsBtn)

	setText(var_8_1, i18n("tec_settings_btn_word"))

	local var_8_2 = arg_8_0.findTF("TargetCatchup", arg_8_0.settingsBtn)
	local var_8_3 = arg_8_0.findTF("Selected", var_8_2)
	local var_8_4 = arg_8_0.findTF("ActCatchup", arg_8_0.settingsBtn)

	arg_8_0.updateSettingBtnVersion()

	local var_8_5 = False
	local var_8_6 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BLUEPRINT_CATCHUP)

	if var_8_6 and not var_8_6.isEnd():
		local var_8_7 = var_8_6.data1
		local var_8_8 = var_8_6.getConfig("config_id")
		local var_8_9 = pg.activity_event_blueprint_catchup[var_8_8].char_choice
		local var_8_10 = pg.activity_event_blueprint_catchup[var_8_8].obtain_max

		if var_8_7 < var_8_10:
			local var_8_11 = arg_8_0.findTF("Selected/CharImg", var_8_4)

			setImageSprite(var_8_11, LoadSprite("TecCatchup/QChar" .. var_8_9, tostring(var_8_9)))

			local var_8_12 = arg_8_0.findTF("Selected/ProgressText", var_8_4)

			setText(var_8_12, var_8_7 .. "/" .. var_8_10)

			local var_8_13 = var_8_6.stopTime - pg.TimeMgr.GetInstance().GetServerTime()

			if arg_8_0.actCatchupTimer:
				arg_8_0.actCatchupTimer.Stop()

				arg_8_0.actCatchupTimer = None

			local var_8_14 = arg_8_0.findTF("TimeLeft/Day", var_8_4)
			local var_8_15 = arg_8_0.findTF("TimeLeft/Hour", var_8_4)
			local var_8_16 = arg_8_0.findTF("TimeLeft/Min", var_8_4)
			local var_8_17 = arg_8_0.findTF("TimeLeft/NumText", var_8_4)

			local function var_8_18()
				local var_9_0, var_9_1, var_9_2, var_9_3 = pg.TimeMgr.GetInstance().parseTimeFrom(var_8_13)

				var_8_13 = var_8_13 - 1

				if var_9_0 >= 1:
					setActive(var_8_14, True)
					setActive(var_8_15, False)
					setActive(var_8_16, False)
					setText(var_8_17, var_9_0)
				elif var_9_0 <= 0 and var_9_1 > 0:
					setActive(var_8_14, False)
					setActive(var_8_15, True)
					setActive(var_8_16, False)
					setText(var_8_17, var_9_1)
				elif var_9_0 <= 0 and var_9_1 <= 0 and (var_9_2 > 0 or var_9_3 > 0):
					setActive(var_8_14, False)
					setActive(var_8_15, False)
					setActive(var_8_16, True)
					setText(var_8_17, math.max(var_9_2, 1))
				elif var_9_0 <= 0 and var_9_1 <= 0 and var_9_2 <= 0 and var_9_3 <= 0 and arg_8_0.actCatchupTimer:
					arg_8_0.actCatchupTimer.Stop()

					arg_8_0.actCatchupTimer = None

					setActive(var_8_4, False)

			arg_8_0.actCatchupTimer = Timer.New(var_8_18, 1, -1, 1)

			arg_8_0.actCatchupTimer.Start()
			arg_8_0.actCatchupTimer.func()

			var_8_5 = True

	setActive(var_8_4, var_8_5)
	setActive(var_8_2, True)

	local var_8_19 = getProxy(TechnologyProxy)
	local var_8_20 = var_8_19.isOpenTargetCatchup()
	local var_8_21 = var_8_19.isOnCatchup()

	if var_8_20:
		if not var_8_21:
			setActive(var_8_3, False)
			setActive(var_8_0, True)
		else
			local var_8_22 = var_8_19.getCurCatchupTecInfo()
			local var_8_23 = var_8_22.tecID
			local var_8_24 = var_8_22.groupID
			local var_8_25 = var_8_22.printNum
			local var_8_26 = var_8_19.getCatchupData(var_8_23).isUr(var_8_24) and pg.technology_catchup_template[var_8_23].obtain_max_per_ur or pg.technology_catchup_template[var_8_23].obtain_max

			if var_8_26 <= var_8_25:
				setActive(var_8_3, False)
				setActive(var_8_0, False)
			else
				setActive(var_8_3, True)
				setActive(var_8_0, False)

				local var_8_27 = arg_8_0.findTF("CharImg", var_8_3)

				setImageSprite(var_8_27, LoadSprite("TecCatchup/QChar" .. var_8_24, tostring(var_8_24)))

				local var_8_28 = arg_8_0.findTF("ProgressText", var_8_3)

				setText(var_8_28, var_8_25 .. "/" .. var_8_26)
	else
		setActive(var_8_3, False)
		setActive(var_8_0, False)

def var_0_0.updateSettingBtnVersion(arg_10_0):
	local var_10_0 = getProxy(TechnologyProxy).getTendency(2)
	local var_10_1 = arg_10_0.settingsBtn.Find("tag")

	setActive(var_10_1, var_10_0 > 0)

	if var_10_0 > 0:
		GetImageSpriteFromAtlasAsync("technologycard", "version_" .. var_10_0, var_10_1.Find("Image"), True)

def var_0_0.setPage(arg_11_0, arg_11_1):
	arg_11_0.contextData.page = arg_11_1

	setActive(arg_11_0.basePage, arg_11_1 == var_0_0.PageBase)
	setActive(arg_11_0.queuePage, arg_11_1 == var_0_0.PageQueue)
	setActive(arg_11_0._tf.Find("blur_panel/adapt/top/title"), arg_11_1 == var_0_0.PageBase)
	setActive(arg_11_0._tf.Find("blur_panel/adapt/left"), arg_11_1 == var_0_0.PageBase)
	setActive(arg_11_0._tf.Find("blur_panel/adapt/top/title_queue"), arg_11_1 == var_0_0.PageQueue)
	setActive(arg_11_0._tf.Find("blur_panel/adapt/right"), arg_11_1 == var_0_0.PageQueue)

	if arg_11_1 == var_0_0.PageBase:
		for iter_11_0, iter_11_1 in ipairs(arg_11_0.technologyVOs):
			if iter_11_1.isActivate():
				if arg_11_0.enhancelTimer:
					arg_11_0.enhancelTimer.Stop()

				arg_11_0.enhancelTimer = Timer.New(function()
					arg_11_0.srcollView.GetComponent("EnhancelScrollView").SetHorizontalTargetItemIndex(arg_11_0.technologyCards[iter_11_0].GetComponent("EnhanceItem").scrollViewItemIndex)

					arg_11_0.enhancelTimer = None, 0.35, 1)

				arg_11_0.enhancelTimer.Start()

				break

def var_0_0.didEnter(arg_13_0):
	arg_13_0.initTechnologys()
	arg_13_0.initQueue()
	arg_13_0.setPage(arg_13_0.contextData.page or var_0_0.PageBase)
	onButton(arg_13_0, arg_13_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.technology_help_text.tip
		}), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.refreshBtn, function()
		if tobool(getProxy(TechnologyProxy).getActivateTechnology()):
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("technology_canot_refresh")
			})

			return

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("technology_refresh_tip"),
			def onYes:()
				arg_13_0.emit(TechnologyMediator.ON_REFRESH)
		}), SFX_PANEL)

	local var_13_0 = getProxy(TechnologyProxy).getConfigMaxVersion()

	onButton(arg_13_0, arg_13_0.settingsBtn, function()
		arg_13_0.emit(TechnologyMediator.ON_CLICK_SETTINGS_BTN), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.backBtn, function()
		arg_13_0.onBackPressed(), SOUND_BACK)
	onButton(arg_13_0, arg_13_0.selectetPanel, function()
		arg_13_0.cancelSelected(), SFX_PANEL)
	arg_13_0.updateRefreshBtn(arg_13_0.flag)
	arg_13_0.updateSettingsBtn()

def var_0_0.initTechnologys(arg_20_0):
	arg_20_0.technologyCards = {}
	arg_20_0.lastButtonListener = arg_20_0.lastButtonListener or {}

	if not arg_20_0.itemList:
		arg_20_0.itemList = UIItemList.New(arg_20_0.srcollView, arg_20_0.srcollView.GetChild(0))

		arg_20_0.itemList.make(function(arg_21_0, arg_21_1, arg_21_2)
			arg_21_1 = arg_21_1 + 1

			if arg_21_0 == UIItemList.EventUpdate:
				arg_21_2.name = arg_21_1
				arg_20_0.technologyCards[arg_21_1] = arg_21_2

				arg_20_0.updateTechnologyTF(arg_21_2, arg_21_1, "base")

				local var_21_0 = GetOrAddComponent(arg_21_2, typeof(Button)).onClick

				if arg_20_0.lastButtonListener[arg_21_2]:
					var_21_0.RemoveListener(arg_20_0.lastButtonListener[arg_21_2])

				arg_20_0.lastButtonListener[arg_21_2] = function()
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL)

					if arg_20_0.technologyVOs[arg_21_1].isCompleted():
						arg_20_0.emit(TechnologyMediator.ON_FINISHED, {
							id = arg_20_0.technologyVOs[arg_21_1].id,
							pool_id = arg_20_0.technologyVOs[arg_21_1].poolId
						})
					else
						arg_20_0.onSelected(arg_21_2, arg_21_1)

				var_21_0.AddListener(arg_20_0.lastButtonListener[arg_21_2]))

	arg_20_0.itemList.align(#arg_20_0.technologyVOs)
	setActive(arg_20_0.srcollView, True)

def var_0_0.initQueue(arg_23_0):
	if not arg_23_0.queueItemList:
		arg_23_0.queueItemList = UIItemList.New(arg_23_0.btnQueue, arg_23_0.btnQueue.GetChild(0))

		arg_23_0.queueItemList.make(function(arg_24_0, arg_24_1, arg_24_2)
			arg_24_1 = arg_24_1 + 1

			if arg_24_0 == UIItemList.EventUpdate:
				arg_24_2.name = arg_24_1

				if arg_23_0.queueTimer[arg_24_1]:
					arg_23_0.queueTimer[arg_24_1].Stop()

					arg_23_0.queueTimer[arg_24_1] = None

				local var_24_0 = {}
				local var_24_1 = arg_23_0.technologyQueue[arg_24_1]

				if not var_24_1:
					var_24_0.empty = True
				else
					local var_24_2 = pg.TimeMgr.GetInstance().GetServerTime()
					local var_24_3 = var_24_1.time
					local var_24_4 = var_24_1.getConfig("time")

					if var_24_2 < var_24_3 - var_24_4:
						var_24_0.waiting = True
					elif var_24_2 < var_24_3:
						var_24_0.doing = True
						arg_23_0.queueTimer[arg_24_1] = Timer.New(function()
							local var_25_0 = pg.TimeMgr.GetInstance().GetServerTime()

							if var_25_0 < var_24_3:
								setSlider(arg_24_2.Find("doing"), 0, var_24_4, var_24_4 - var_24_3 + var_25_0)
							else
								arg_23_0.updateQueueChange(), 1, -1)

						arg_23_0.queueTimer[arg_24_1].Start()
						arg_23_0.queueTimer[arg_24_1].func()
					else
						var_24_0.complete = True

				eachChild(arg_24_2, function(arg_26_0)
					setActive(arg_26_0, var_24_0[arg_26_0.name])))

	arg_23_0.queueItemList.align(TechnologyConst.QUEUE_TOTAL_COUNT)
	onButton(arg_23_0, arg_23_0.btnQueue, function()
		arg_23_0.setPage(var_0_0.PageQueue), SFX_PANEL)

	if not arg_23_0.queueCardItemList:
		arg_23_0.queueCardItemList = UIItemList.New(arg_23_0.queueView, arg_23_0.queueView.GetChild(0))

		arg_23_0.queueCardItemList.make(function(arg_28_0, arg_28_1, arg_28_2)
			arg_28_1 = arg_28_1 + 1

			if arg_28_0 == UIItemList.EventUpdate:
				arg_28_2.name = arg_28_1

				arg_23_0.updateTechnologyTF(arg_28_2, arg_28_1, "queue"))

	arg_23_0.queueCardItemList.align(TechnologyConst.QUEUE_TOTAL_COUNT)
	onButton(arg_23_0, arg_23_0.btnAwardQueue, function()
		if arg_23_0.technologyQueue[1] and arg_23_0.technologyQueue[1].isCompleted():
			arg_23_0.emit(TechnologyMediator.ON_FINISH_QUEUE), SFX_CONFIRM)
	setActive(arg_23_0.btnAwardQueue, arg_23_0.technologyQueue[1] and arg_23_0.technologyQueue[1].isCompleted())
	setActive(arg_23_0.btnAwardQueueDisable, not isActive(arg_23_0.btnAwardQueue))

def var_0_0.updateRefreshBtn(arg_30_0, arg_30_1):
	setButtonEnabled(arg_30_0.refreshBtn, arg_30_1 == 0)

def var_0_0.onSelected(arg_31_0, arg_31_1, arg_31_2):
	if not arg_31_2:
		return

	if not arg_31_0.technologyVOs[arg_31_2]:
		return

	arg_31_0.contextData.selectedIndex = arg_31_2

	arg_31_0.updateTechnologyTF(arg_31_0.technologyTpl, arg_31_2, "desc")

	arg_31_0.srcollViewCG.alpha = 0.3

	setActive(arg_31_1, False)
	setActive(arg_31_0.selectetPanel, True)

	local var_31_0 = {}

	eachChild(arg_31_0.srcollView, function(arg_32_0)
		var_31_0[tonumber(arg_32_0.name)] = arg_32_0)

	local function var_31_1(arg_33_0, arg_33_1)
		local var_33_0 = {}
		local var_33_1 = arg_33_0
		local var_33_2 = var_31_0[arg_33_0].localPosition.x

		for iter_33_0, iter_33_1 in ipairs(var_31_0):
			var_33_0[iter_33_0] = var_31_0[iter_33_0].localPosition.x - var_33_2

		for iter_33_2, iter_33_3 in ipairs(var_33_0):
			if iter_33_3 != 0 and (var_33_0[var_33_1] == 0 or arg_33_1 and (iter_33_3 > 0 and var_33_0[var_33_1] > 0 and iter_33_3 > var_33_0[var_33_1] or iter_33_3 < 0 and (var_33_0[var_33_1] > 0 or iter_33_3 > var_33_0[var_33_1])) or not arg_33_1 and (iter_33_3 < 0 and var_33_0[var_33_1] < 0 and iter_33_3 < var_33_0[var_33_1] or iter_33_3 > 0 and (var_33_0[var_33_1] < 0 or iter_33_3 < var_33_0[var_33_1]))):
				var_33_1 = iter_33_2

		return var_31_0[var_33_1]

	onButton(arg_31_0, arg_31_0.arrLeftBtn, function()
		if arg_31_0.inAnim:
			return

		arg_31_0.cancelSelected()
		triggerButton(var_31_1(arg_31_2, True)), SFX_PANEL)
	onButton(arg_31_0, arg_31_0.arrRightBtn, function()
		if arg_31_0.inAnim:
			return

		arg_31_0.cancelSelected()
		triggerButton(var_31_1(arg_31_2, False)), SFX_PANEL)

def var_0_0.cancelSelected(arg_36_0):
	if not arg_36_0.technologyVOs[arg_36_0.contextData.selectedIndex or 0]:
		return

	local var_36_0 = arg_36_0.technologyCards[arg_36_0.contextData.selectedIndex]

	arg_36_0.contextData.selectedIndex = None

	setActive(var_36_0, True)
	removeOnButton(arg_36_0.arrLeftBtn)
	removeOnButton(arg_36_0.arrRightBtn)
	setActive(arg_36_0.selectetPanel, False)

	arg_36_0.srcollViewCG.alpha = 1
	arg_36_0.inAnim = True

	if arg_36_0.timer:
		arg_36_0.timer.Stop()

		arg_36_0.timer = None

	arg_36_0.timer = Timer.New(function()
		arg_36_0.inAnim = None, 0.2, 1)

	arg_36_0.timer.Start()

	if arg_36_0.extraTimer:
		arg_36_0.extraTimer.Stop()

		arg_36_0.extraTimer = None

def var_0_0.updateTechnology(arg_38_0, arg_38_1):
	local var_38_0

	for iter_38_0, iter_38_1 in ipairs(arg_38_0.technologyVOs):
		if iter_38_1.id == arg_38_1.id:
			arg_38_0.technologyVOs[iter_38_0] = arg_38_1
			var_38_0 = iter_38_0

			break

	local var_38_1 = arg_38_0.technologyCards[var_38_0]

	arg_38_0.updateTechnologyTF(var_38_1, var_38_0, "base")

	if arg_38_0.contextData.selectedIndex and arg_38_0.technologyVOs[arg_38_0.contextData.selectedIndex].id == arg_38_1.id:
		arg_38_0.updateTechnologyTF(arg_38_0.technologyTpl, var_38_0, "desc")

def var_0_0.updateQueueChange(arg_39_0):
	arg_39_0.queueItemList.align(#arg_39_0.technologyQueue)
	arg_39_0.queueCardItemList.align(TechnologyConst.QUEUE_TOTAL_COUNT)
	setActive(arg_39_0.btnAwardQueue, arg_39_0.technologyQueue[1] and arg_39_0.technologyQueue[1].isCompleted())
	setActive(arg_39_0.btnAwardQueueDisable, not isActive(arg_39_0.btnAwardQueue))

	local var_39_0 = getProxy(TechnologyProxy).getActivateTechnology()

	if var_39_0:
		arg_39_0.updateTechnology(var_39_0)

def var_0_0.updateTechnologyTF(arg_40_0, arg_40_1, arg_40_2, arg_40_3):
	local var_40_0

	if arg_40_3 == "queue":
		var_40_0 = arg_40_0.technologyQueue[arg_40_2]

		local var_40_1 = not tobool(var_40_0)

		setActive(arg_40_1.Find("frame"), not var_40_1)
		setActive(arg_40_1.Find("empty"), var_40_1)

		if var_40_1:
			return
	else
		var_40_0 = arg_40_0.technologyVOs[arg_40_2]

	arg_40_0.updateInfo(arg_40_1, var_40_0, arg_40_3)
	arg_40_0.updateInfoVersionPickUp(arg_40_1, var_40_0)

	local var_40_2 = var_40_0.getConfig("time")
	local var_40_3 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_40_4 = var_40_0.time

	switch(arg_40_3, {
		def base:()
			if arg_40_0.cardtimer[arg_40_2]:
				arg_40_0.cardtimer[arg_40_2].Stop()

				arg_40_0.cardtimer[arg_40_2] = None

			local var_41_0 = arg_40_1.Find("frame/marks/time")
			local var_41_1 = arg_40_1.Find("frame/marks/Text")
			local var_41_2 = var_0_0.rarityColor[var_40_0.getConfig("bg")]

			GetComponent(var_41_0, "Shadow").effectColor = Color.New(unpack(var_41_2[2]))

			local var_41_3 = {}

			if var_40_4 <= 0:
				var_41_3.blue = True

				setText(var_41_1, setColorStr(i18n("technology_detail"), var_41_2[1]))
				setText(var_41_0, pg.TimeMgr.GetInstance().DescCDTime(var_40_0.getConfig("time")))
			elif var_40_3 < var_40_4 - var_40_2:
				var_41_3.blue = True

				setText(var_41_1, setColorStr(i18n("technology_queue_waiting"), var_41_2[1]))
				setText(var_41_0, pg.TimeMgr.GetInstance().DescCDTime(var_40_0.getConfig("time")))

				arg_40_0.cardtimer[arg_40_2] = Timer.New(function()
					arg_40_0.updateTechnology(var_40_0), var_40_4 - var_40_2 - var_40_3)

				arg_40_0.cardtimer[arg_40_2].Start()
			elif var_40_3 < var_40_4:
				var_41_3.blue = True

				setText(var_41_1, setColorStr(i18n("technology_queue_processing"), var_41_2[1]))

				arg_40_0.cardtimer[arg_40_2] = Timer.New(function()
					local var_43_0 = var_40_0.time
					local var_43_1 = pg.TimeMgr.GetInstance().GetServerTime()

					if var_43_1 < var_43_0:
						setText(var_41_0, pg.TimeMgr.GetInstance().DescCDTime(var_43_0 - var_43_1))
					else
						arg_40_0.updateTechnology(var_40_0), 1, -1)

				arg_40_0.cardtimer[arg_40_2].Start()
				arg_40_0.cardtimer[arg_40_2].func()
			else
				var_41_3.green = True

				if var_40_0.isCompleted():
					setText(var_41_1, setColorStr(i18n("technology_queue_complete"), var_41_2[1]))
				else
					setText(var_41_1, setColorStr(i18n("technology_mission_unfinish"), var_41_2[1]))

				setText(var_41_0, "00.00.00")

			eachChild(arg_40_1.Find("frame/marks/line"), function(arg_44_0)
				setActive(arg_44_0, var_41_3[arg_44_0.name])),
		def queue:()
			if arg_40_0.queueCardTimer[arg_40_2]:
				arg_40_0.queueCardTimer[arg_40_2].Stop()

				arg_40_0.queueCardTimer[arg_40_2] = None

			local var_45_0 = arg_40_1.Find("frame/marks/time")
			local var_45_1 = arg_40_1.Find("frame/marks/Text")
			local var_45_2 = var_0_0.rarityColor[var_40_0.getConfig("bg")]

			GetComponent(var_45_0, "Shadow").effectColor = Color.New(unpack(var_45_2[2]))

			local var_45_3 = {}

			if var_40_4 <= 0:
				assert(False, "error queue")
			elif var_40_3 < var_40_4 - var_40_2:
				var_45_3.blue = True

				setText(var_45_1, setColorStr(i18n("technology_queue_waiting"), var_45_2[1]))
				setText(var_45_0, pg.TimeMgr.GetInstance().DescCDTime(var_40_0.getConfig("time")))
			elif var_40_3 < var_40_4:
				var_45_3.blue = True

				setText(var_45_1, setColorStr(i18n("technology_queue_processing"), var_45_2[1]))

				arg_40_0.queueCardTimer[arg_40_2] = Timer.New(function()
					local var_46_0 = var_40_0.time
					local var_46_1 = pg.TimeMgr.GetInstance().GetServerTime()

					if var_46_1 < var_46_0:
						setText(var_45_0, pg.TimeMgr.GetInstance().DescCDTime(var_46_0 - var_46_1)), 1, -1)

				arg_40_0.queueCardTimer[arg_40_2].Start()
				arg_40_0.queueCardTimer[arg_40_2].func()
			else
				var_45_3.green = True

				setText(var_45_1, setColorStr(i18n("technology_queue_complete"), var_45_2[1]))
				setText(var_45_0, "00.00.00")

			eachChild(arg_40_1.Find("frame/marks/line"), function(arg_47_0)
				setActive(arg_47_0, var_45_3[arg_47_0.name]))
			setActive(arg_40_1.Find("frame/mask"), var_40_4 > 0 and var_40_3 < var_40_4 - var_40_2),
		def desc:()
			arg_40_0.descTxt.text = var_40_0.getConfig("desc")
			arg_40_0.descBG.sprite = GetSpriteFromAtlas("ui/TechnologyUI_atlas", var_40_0.getConfig("rarity"))

			local var_48_0 = var_40_0.getConfig("consume")
			local var_48_1 = UIItemList.New(arg_40_0.itemContainer, arg_40_0.itemTpl)

			var_48_1.make(function(arg_49_0, arg_49_1, arg_49_2)
				arg_49_1 = arg_49_1 + 1

				if arg_49_0 == UIItemList.EventUpdate:
					arg_40_0.updateItem(arg_49_2, var_40_0, var_48_0[arg_49_1])
					setActive(arg_49_2.Find("check"), var_40_0.isActivate())
					setActive(arg_49_2.Find("icon_bg/count"), not var_40_0.isActivate()))
			var_48_1.align(#var_48_0)
			setActive(arg_40_0.emptyTF, not var_48_0 or #var_48_0 <= 0)

			local var_48_2 = var_40_0.getConfig("condition")

			if var_48_2 > 0:
				local var_48_3 = getProxy(TaskProxy).getTaskById(var_48_2) or Task.New({
					id = var_48_2
				})

				arg_40_0.taskSlider.value = var_48_3.progress / var_48_3.getConfig("target_num")
				arg_40_0.taskDesc.text = var_48_3.getConfig("desc") .. "(" .. var_48_3.progress .. "/" .. var_48_3.getConfig("target_num") .. ")"
			else
				arg_40_0.taskDesc.text = i18n("technology_task_none_tip")
				arg_40_0.taskSlider.value = 0

			if arg_40_0.extraTimer:
				arg_40_0.extraTimer.Stop()

				arg_40_0.extraTimer = None

			local var_48_4 = {}

			if var_40_4 <= 0:
				var_48_4.start_btn = True
				arg_40_0.timerTxt.text = pg.TimeMgr.GetInstance().DescCDTime(var_40_2)
			elif var_40_3 < var_40_4 - var_40_2:
				var_48_4.stop_btn = True
				var_48_4.join_btn = var_40_0.finishCondition()
				var_48_4.lock_join_btn = not var_48_4.join_btn
				arg_40_0.timerTxt.text = pg.TimeMgr.GetInstance().DescCDTime(var_40_2)
			elif var_40_3 < var_40_4:
				var_48_4.stop_btn = True
				var_48_4.join_btn = var_40_0.finishCondition()
				var_48_4.lock_join_btn = not var_48_4.join_btn
				arg_40_0.extraTimer = Timer.New(function()
					local var_50_0 = pg.TimeMgr.GetInstance().GetServerTime()

					if var_50_0 < var_40_4:
						arg_40_0.timerTxt.text = pg.TimeMgr.GetInstance().DescCDTime(var_40_4 - var_50_0), 1, -1)

				arg_40_0.extraTimer.Start()
				arg_40_0.extraTimer.func()
			else
				if var_40_0.isCompleted():
					var_48_4.finish_btn = True
				else
					var_48_4.stop_btn = True
					var_48_4.lock_join_btn = True

				arg_40_0.timerTxt.text = "00.00.00"

			eachChild(arg_40_1.Find("frame/btns"), function(arg_51_0)
				setActive(arg_51_0, var_48_4[arg_51_0.name]))

			local var_48_5 = arg_40_1.Find("frame/btns/start_btn")

			onButton(arg_40_0, var_48_5, function()
				if getProxy(TechnologyProxy).getActivateTechnology():
					pg.TipsMgr.GetInstance().ShowTips(i18n("technology_is_actived"))

					return

				local var_52_0 = var_40_0.getConfig("consume")

				if #var_52_0 > 0:
					local var_52_1 = getDropInfo(var_52_0)

					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("technology_task_build_tip", var_52_1),
						def onYes:()
							arg_40_0.emit(TechnologyMediator.ON_START, {
								id = var_40_0.id,
								pool_id = var_40_0.poolId
							})
					})
				else
					arg_40_0.emit(TechnologyMediator.ON_START, {
						id = var_40_0.id,
						pool_id = var_40_0.poolId
					}), SFX_PANEL)
			setButtonEnabled(var_48_5, var_40_0.hasResToStart())

			local var_48_6 = arg_40_1.Find("frame/btns/stop_btn")

			onButton(arg_40_0, var_48_6, function()
				if not var_40_0.isActivate():
					return

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("technology_stop_tip"),
					def onYes:()
						arg_40_0.emit(TechnologyMediator.ON_STOP, {
							id = var_40_0.id,
							pool_id = var_40_0.poolId
						})
				}), SFX_PANEL)

			local var_48_7 = arg_40_1.Find("frame/btns/join_btn")

			onButton(arg_40_0, var_48_7, function()
				if #arg_40_0.technologyQueue == TechnologyConst.QUEUE_TOTAL_COUNT:
					pg.TipsMgr.GetInstance().ShowTips(i18n("technology_queue_full"))

					return

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("technology_queue_in_doublecheck"),
					def onYes:()
						arg_40_0.emit(TechnologyMediator.ON_JOIN_QUEUE, {
							id = var_40_0.id,
							pool_id = var_40_0.poolId
						})
				}), SFX_PANEL)

			local var_48_8 = arg_40_1.Find("frame/btns/lock_join_btn")

			onButton(arg_40_0, var_48_8, function()
				pg.TipsMgr.GetInstance().ShowTips(i18n("technology_queue_in_mission_incomplete")), SFX_PANEL)

			local var_48_9 = arg_40_1.Find("frame/btns/finish_btn")

			onButton(arg_40_0, var_48_9, function()
				arg_40_0.emit(TechnologyMediator.ON_FINISHED, {
					id = var_40_0.id,
					pool_id = var_40_0.poolId
				}), SFX_PANEL)
	})

def var_0_0.dfs(arg_60_0, arg_60_1, arg_60_2):
	if arg_60_1.name != "item_tpl":
		for iter_60_0 = 1, arg_60_1.childCount:
			arg_60_0.dfs(arg_60_1.GetChild(iter_60_0 - 1), arg_60_2)
	else
		arg_60_2(arg_60_1)

local var_0_1 = {
	tag_red = "F15F34FF",
	tag_blue = "2541E3FF"
}

def var_0_0.updateInfo(arg_61_0, arg_61_1, arg_61_2, arg_61_3):
	setImageSprite(arg_61_1.Find("frame"), GetSpriteFromAtlas("technologycard", arg_61_2.getConfig("bg") .. (arg_61_3 == "desc" and "_l" or "")))
	setImageSprite(arg_61_1.Find("frame/icon_mask/icon"), GetSpriteFromAtlas("technologyshipicon/" .. arg_61_2.getConfig("bg_icon"), arg_61_2.getConfig("bg_icon")), True)
	setImageSprite(arg_61_1.Find("frame/top/label"), GetSpriteFromAtlas("technologycard", arg_61_2.getConfig("label")))
	setImageSprite(arg_61_1.Find("frame/top/label/text"), GetSpriteFromAtlas("technologycard", arg_61_2.getConfig("label_color")), True)
	setImageSprite(arg_61_1.Find("frame/top/label/version"), GetSpriteFromAtlas("technologycard", "version_" .. arg_61_2.getConfig("blueprint_version")), True)
	setImageColor(arg_61_1.Find("frame/top/pick_up"), Color.NewHex(var_0_1[arg_61_2.getConfig("label")]))
	setText(arg_61_1.Find("frame/name_bg/Text"), arg_61_2.getConfig("name"))
	setText(arg_61_1.Find("frame/sub_name"), arg_61_2.getConfig("sub_name") or "")

	local var_61_0 = arg_61_2.getConfig("drop_client")
	local var_61_1 = arg_61_1.Find("frame/item_container")
	local var_61_2 = 0

	arg_61_0.dfs(var_61_1, function(arg_62_0)
		var_61_2 = var_61_2 + 1

		setActive(arg_62_0, var_61_2 <= #var_61_0)

		if var_61_2 <= #var_61_0:
			arg_61_0.updateItem(arg_62_0, arg_61_2, var_61_0[var_61_2]))
	switch(arg_61_3, {
		def desc:()
			return
	}, function()
		setActive(var_61_1.GetChild(1), #var_61_0 > 2)

		var_61_1.GetChild(0).GetComponent("HorizontalLayoutGroup").padding.right = #var_61_0 == 4 and 25 or 0
		var_61_1.GetChild(1).GetComponent("HorizontalLayoutGroup").padding.left = #var_61_0 == 4 and 25 or 0)

def var_0_0.updateInfoVersionPickUp(arg_65_0, arg_65_1, arg_65_2):
	local var_65_0 = getProxy(TechnologyProxy).getTendency(2)

	setActive(arg_65_1.Find("frame/top/pick_up"), var_65_0 == arg_65_2.getConfig("blueprint_version"))

def var_0_0.updateItem(arg_66_0, arg_66_1, arg_66_2, arg_66_3):
	local var_66_0 = Drop.Create(arg_66_3)

	updateDrop(arg_66_1, setmetatable({
		count = 0
	}, {
		__index = var_66_0
	}))

	local var_66_1 = arg_66_0.findTF("icon_bg/count", arg_66_1)

	if not IsNil(var_66_1):
		setColorCount(var_66_1, var_66_0.getOwnedCount(), var_66_0.count)

	onButton(arg_66_0, arg_66_1, function()
		local var_67_0 = var_66_0.getConfig("display_icon") or {}

		if #var_67_0 > 0:
			local var_67_1 = {
				type = MSGBOX_TYPE_ITEM_BOX,
				items = _.map(var_67_0, function(arg_68_0)
					return {
						type = arg_68_0[1],
						id = arg_68_0[2]
					}),
				content = var_66_0.getConfig("display")
			}

			function var_67_1.itemFunc(arg_69_0)
				arg_66_0.emit(var_0_0.ON_DROP, arg_69_0, function()
					pg.MsgboxMgr.GetInstance().ShowMsgBox(var_67_1))

			pg.MsgboxMgr.GetInstance().ShowMsgBox(var_67_1)
		else
			arg_66_0.emit(var_0_0.ON_DROP, var_66_0), SFX_PANEL)

def var_0_0.updatePickUpVersionChange(arg_71_0):
	arg_71_0.updateSettingBtnVersion()

	for iter_71_0, iter_71_1 in ipairs(arg_71_0.technologyCards):
		arg_71_0.updateInfoVersionPickUp(iter_71_1, arg_71_0.technologyVOs[iter_71_0])

	for iter_71_2, iter_71_3 in ipairs(arg_71_0.technologyQueue):
		arg_71_0.updateInfoVersionPickUp(arg_71_0.queueCardItemList.container.GetChild(iter_71_2 - 1), iter_71_3)

def var_0_0.clearTimer(arg_72_0, ...):
	if arg_72_0.timer:
		arg_72_0.timer.Stop()

		arg_72_0.timer = None

	if arg_72_0.extraTimer:
		arg_72_0.extraTimer.Stop()

		arg_72_0.extraTimer = None

	if arg_72_0.enhancelTimer:
		arg_72_0.enhancelTimer.Stop()

		arg_72_0.enhancelTimer = None

	for iter_72_0, iter_72_1 in pairs(arg_72_0.cardtimer):
		iter_72_1.Stop()

	arg_72_0.cardtimer = {}

	for iter_72_2, iter_72_3 in pairs(arg_72_0.queueTimer):
		iter_72_3.Stop()

	arg_72_0.queueTimer = {}

	for iter_72_4, iter_72_5 in pairs(arg_72_0.queueCardTimer):
		iter_72_5.Stop()

	arg_72_0.queueCardTimer = {}

	if arg_72_0.actCatchupTimer:
		arg_72_0.actCatchupTimer.Stop()

		arg_72_0.actCatchupTimer = None

def var_0_0.willExit(arg_73_0):
	arg_73_0.clearTimer()

	arg_73_0.cardtimer = None
	arg_73_0.queueTimer = None
	arg_73_0.queueCardTimer = None

return var_0_0