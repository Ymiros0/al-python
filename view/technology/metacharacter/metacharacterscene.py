local var_0_0 = class("MetaCharacterScene", import("...base.BaseUI"))

var_0_0.PAGES = {
	REPAIR = 3,
	ENERGY = 1,
	TACTICS = 2,
	SYN = 4
}
var_0_0.PAGES_EVENTS = {
	MetaCharacterMediator.ON_ENERGY,
	MetaCharacterMediator.ON_TACTICS,
	MetaCharacterMediator.ON_REPAIR,
	MetaCharacterMediator.ON_SYN
}
var_0_0.SCALE_ON_PITCH = {
	x = 1.7,
	y = 1.7
}
var_0_0.ON_SKILL = "MetaCharacterScene.ON_SKILL"

def var_0_0.getUIName(arg_1_0):
	return "MetaCharacterUI"

def var_0_0.init(arg_2_0):
	Input.multiTouchEnabled = False

	arg_2_0.initUITextTips()
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()
	arg_2_0.initMetaProgressList()
	arg_2_0.initBannerList()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.overLayPanel(True)
	arg_3_0.updateStart()
	arg_3_0.autoOpenFunc()

def var_0_0.willExit(arg_4_0):
	Input.multiTouchEnabled = True

	arg_4_0.overLayPanel(False)

def var_0_0.initUITextTips(arg_5_0):
	local var_5_0 = arg_5_0.findTF("HidePanel/ScrollPanel/ListPanel/BannerTpl/ForScale")
	local var_5_1 = arg_5_0.findTF("Empty/ActType/TipText", var_5_0)
	local var_5_2 = arg_5_0.findTF("Empty/BuildType/TipText", var_5_0)
	local var_5_3 = arg_5_0.findTF("Active/ActType/Text", var_5_0)
	local var_5_4 = arg_5_0.findTF("Active/BuildType/Text", var_5_0)

	setText(var_5_1, i18n("meta_syn_rate"))
	setText(var_5_2, i18n("meta_build"))
	setText(var_5_3, i18n("meta_repair_rate"))
	setText(var_5_4, i18n("meta_build"))

	local var_5_5 = arg_5_0.findTF("HidePanel/PTPanel/Progress/Story/TipText1")
	local var_5_6 = arg_5_0.findTF("HidePanel/PTPanel/Progress/Story/TipText2")

	setText(var_5_5, i18n("meta_story_tip_1"))
	setText(var_5_6, i18n("meta_story_tip_2"))

	local var_5_7 = arg_5_0.findTF("HidePanel/ActTimeTip/Tip")

	setText(var_5_7, i18n("meta_acttime_limit"))

def var_0_0.initData(arg_6_0):
	arg_6_0.metaProgressVOList = {}
	arg_6_0.curMetaGroupID = None
	arg_6_0.curMetaProgress = None
	arg_6_0.toggleList = {}
	arg_6_0.bannerTFList = {}
	arg_6_0.curPageIndex = None
	arg_6_0.curMetaIndex = None
	arg_6_0.metaCharacterProxy = getProxy(MetaCharacterProxy)
	arg_6_0.bayProxy = getProxy(BayProxy)
	arg_6_0.indexDatas = {}

def var_0_0.findUI(arg_7_0):
	arg_7_0.shipImg = arg_7_0.findTF("HidePanel/ShipImg")
	arg_7_0.shipNameImg = arg_7_0.findTF("HidePanel/NameImg")
	arg_7_0.noCharTF = arg_7_0.findTF("BG/NoCharacter")
	arg_7_0.indexBtn = arg_7_0.findTF("blur_panel/adapt/top/index")
	arg_7_0.hidePanel = arg_7_0.findTF("HidePanel")
	arg_7_0.scrollPanel = arg_7_0.findTF("ScrollPanel", arg_7_0.hidePanel)
	arg_7_0.bannerListPanel = arg_7_0.findTF("ListPanel", arg_7_0.scrollPanel)
	arg_7_0.bannerContainer = arg_7_0.findTF("Container", arg_7_0.bannerListPanel)
	arg_7_0.bannerTpl = arg_7_0.findTF("BannerTpl", arg_7_0.bannerListPanel)
	arg_7_0.actTimePanel = arg_7_0.findTF("ActTimeTip", arg_7_0.hidePanel)
	arg_7_0.actTimeText = arg_7_0.findTF("Text", arg_7_0.actTimePanel)
	arg_7_0.menuPanel = arg_7_0.findTF("MenuPanel", arg_7_0.hidePanel)
	arg_7_0.energyBtn = arg_7_0.findTF("EnergyBtn", arg_7_0.menuPanel)
	arg_7_0.repairBtn = arg_7_0.findTF("RepairBtn", arg_7_0.menuPanel)
	arg_7_0.tacticsBtn = arg_7_0.findTF("TacticsBtn", arg_7_0.menuPanel)
	arg_7_0.synBtn = arg_7_0.findTF("SynBtn", arg_7_0.menuPanel)
	arg_7_0.synDecorateTF = arg_7_0.findTF("SynDecorate", arg_7_0.menuPanel)
	arg_7_0.synBtnLimitTimeTF = arg_7_0.findTF("Limit", arg_7_0.synBtn)
	arg_7_0.synBtnLock = arg_7_0.findTF("LockMask", arg_7_0.synBtn)
	arg_7_0.ptPanel = arg_7_0.findTF("PTPanel", arg_7_0.hidePanel)
	arg_7_0.ptRedBarImg = arg_7_0.findTF("RedBar", arg_7_0.ptPanel)
	arg_7_0.ptPreviewBtn = arg_7_0.findTF("PreviewBtn", arg_7_0.ptPanel)
	arg_7_0.ptGetBtn = arg_7_0.findTF("SynBtn", arg_7_0.ptPanel)
	arg_7_0.ptGetBtnTag = arg_7_0.findTF("Tag", arg_7_0.ptGetBtn)
	arg_7_0.ptShowWayBtn = arg_7_0.findTF("ShowWayBtn", arg_7_0.ptPanel)

	local var_7_0 = arg_7_0.findTF("Progress", arg_7_0.ptPanel)

	arg_7_0.ptProgressImg = arg_7_0.findTF("CircleProgress/ProgressImg", var_7_0)
	arg_7_0.ptProgressScaleLine = arg_7_0.findTF("CircleProgress/ScaleLine", var_7_0)
	arg_7_0.ptInfoPanel = arg_7_0.findTF("PT", var_7_0)
	arg_7_0.ptProgressRedRightNumText = arg_7_0.findTF("ProgressTextBG/PointRedText/RightNumText", arg_7_0.ptInfoPanel)
	arg_7_0.ptProgressRedLeftNumText = arg_7_0.findTF("ProgressTextBG/PointRedText/LeftNumText", arg_7_0.ptInfoPanel)
	arg_7_0.ptProgressWhiteRightNumText = arg_7_0.findTF("ProgressTextBG/PointText/RightNumText", arg_7_0.ptInfoPanel)
	arg_7_0.ptProgressWhiteLeftNumText = arg_7_0.findTF("ProgressTextBG/PointText/LeftNumText", arg_7_0.ptInfoPanel)
	arg_7_0.ptIcon = arg_7_0.findTF("PTProgressText/PTIcon", arg_7_0.ptInfoPanel)
	arg_7_0.ptProgressRedText = arg_7_0.findTF("PTProgressRedText", arg_7_0.ptInfoPanel)
	arg_7_0.ptProgressWhiteText = arg_7_0.findTF("PTProgressText", arg_7_0.ptInfoPanel)
	arg_7_0.storyInfoPanel = arg_7_0.findTF("Story", var_7_0)

	local var_7_1 = arg_7_0.findTF("TipText1", arg_7_0.storyInfoPanel)
	local var_7_2 = arg_7_0.findTF("TipText2", arg_7_0.storyInfoPanel)

	arg_7_0.storyNameText = arg_7_0.findTF("StroyNameText", arg_7_0.storyInfoPanel)
	arg_7_0.getShipBtn = arg_7_0.findTF("FinishBtn", var_7_0)
	arg_7_0.goGetPanel = arg_7_0.findTF("GoGetPanel", arg_7_0.hidePanel)
	arg_7_0.goGetBtn = arg_7_0.findTF("GoGetBtn", arg_7_0.goGetPanel)
	arg_7_0.blurPanel = arg_7_0.findTF("blur_panel")

	local var_7_3 = arg_7_0.findTF("adapt", arg_7_0.blurPanel)

	arg_7_0.backBtn = arg_7_0.findTF("top/back", var_7_3)
	arg_7_0.helpBtn = arg_7_0.findTF("top/help", var_7_3)
	arg_7_0.toggleBtnsTF = arg_7_0.findTF("left/Btns", var_7_3)
	arg_7_0.toggleList[1] = arg_7_0.findTF("Energy", arg_7_0.toggleBtnsTF)
	arg_7_0.toggleList[2] = arg_7_0.findTF("Tactics", arg_7_0.toggleBtnsTF)
	arg_7_0.toggleList[3] = arg_7_0.findTF("Repair", arg_7_0.toggleBtnsTF)
	arg_7_0.toggleList[4] = arg_7_0.findTF("Syn", arg_7_0.toggleBtnsTF)
	arg_7_0.synToggleLock = arg_7_0.findTF("SynLock", arg_7_0.toggleBtnsTF)

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.backBtn, function()
		local var_9_0 = arg_8_0.curPageIndex

		if var_9_0:
			arg_8_0.enterMenuPage(False)
			arg_8_0.emit(var_0_0.PAGES_EVENTS[arg_8_0.curPageIndex], None, False)

			if var_9_0 == var_0_0.PAGES.REPAIR:
				arg_8_0.backFromRepair()
			else
				arg_8_0.backFromNotRepair()
		else
			arg_8_0.closeView(), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.meta_help.tip
		}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.indexBtn, function()
		arg_8_0.openIndexLayer(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.goGetBtn, function()
		local var_12_0 = arg_8_0.getCurMetaProgressVO()
		local var_12_1 = var_12_0.isPassType()
		local var_12_2 = var_12_0.isBuildType()

		if var_12_1:
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.CRUSING)
		elif var_12_2:
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.GETBOAT, {
				page = BuildShipScene.PAGE_BUILD,
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.ptPreviewBtn, function()
		arg_8_0.emit(MetaCharacterMediator.OPEN_PT_PREVIEW_LAYER, arg_8_0.getCurMetaProgressVO()), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.ptGetBtn, function()
		local var_14_0 = arg_8_0.getCurMetaProgressVO()
		local var_14_1 = var_14_0.getMetaProgressPTState()

		if var_14_1 == MetaProgress.STATE_CAN_AWARD:
			local var_14_2, var_14_3 = arg_8_0.getOneStepPTAwardLevelAndCount()

			pg.m02.sendNotification(GAME.GET_META_PT_AWARD, {
				groupID = var_14_0.id,
				targetCount = var_14_3
			})
		elif var_14_1 == MetaProgress.STATE_LESS_PT:
			local var_14_4 = False
			local var_14_5 = nowWorld()

			if var_14_5:
				var_14_4 = var_14_5.IsSystemOpen(WorldConst.SystemWorldBoss)

			local var_14_6 = var_14_4 and "meta_pt_notenough" or "meta_boss_unlock"

			pg.TipsMgr.GetInstance().ShowTips(i18n(var_14_6))
		elif var_14_1 == MetaProgress.STATE_LESS_STORY:
			pg.TipsMgr.GetInstance().ShowTips(i18n("meta_story_lock")), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.ptShowWayBtn, function()
		local var_15_0 = False
		local var_15_1 = nowWorld()

		if var_15_1:
			var_15_0 = var_15_1.IsSystemOpen(WorldConst.SystemWorldBoss)

		local var_15_2 = var_15_0 and "meta_pt_notenough" or "meta_boss_unlock"

		pg.TipsMgr.GetInstance().ShowTips(i18n(var_15_2)), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.getShipBtn, function()
		local var_16_0 = arg_8_0.getCurMetaProgressVO()
		local var_16_1, var_16_2 = var_16_0.metaPtData.GetResProgress()

		pg.m02.sendNotification(GAME.GET_META_PT_AWARD, {
			groupID = var_16_0.id,
			targetCount = var_16_2
		}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.synToggleLock, function()
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.synBtnLock, function()
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")))
	onButton(arg_8_0, arg_8_0.findTF("RepairBtn", arg_8_0.repairBtn), function()
		arg_8_0.switchPage(var_0_0.PAGES.REPAIR), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.energyBtn, function()
		arg_8_0.isMainOpenLayerTag = True

		arg_8_0.switchPage(var_0_0.PAGES.ENERGY), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.tacticsBtn, function()
		arg_8_0.isMainOpenLayerTag = True

		arg_8_0.switchPage(var_0_0.PAGES.TACTICS), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.synBtn, function()
		if not isActive(arg_8_0.synBtnLock):
			arg_8_0.isMainOpenLayerTag = True

			arg_8_0.switchPage(var_0_0.PAGES.SYN), SFX_PANEL)

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.toggleList):
		onToggle(arg_8_0, iter_8_1, function(arg_23_0)
			if arg_8_0.curPageIndex == iter_8_0 and arg_23_0 == True:
				return

			local var_23_0 = arg_8_0.getCurMetaProgressVO().getShip()

			if arg_8_0.curPageIndex == iter_8_0 and arg_23_0 == False:
				arg_8_0.enterMenuPage(False)
				arg_8_0.emit(var_0_0.PAGES_EVENTS[iter_8_0], var_23_0.id, False)

			if arg_8_0.curPageIndex != iter_8_0 and arg_23_0 == True:
				arg_8_0.enterMenuPage(True)

				arg_8_0.curPageIndex = iter_8_0

				arg_8_0.emit(var_0_0.PAGES_EVENTS[iter_8_0], var_23_0.id, True))

def var_0_0.resetToggleList(arg_24_0):
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.toggleList):
		setActive(arg_24_0.findTF("On", iter_24_1), False)
		setActive(arg_24_0.findTF("Off", iter_24_1), True)

def var_0_0.initMetaProgressList(arg_25_0):
	arg_25_0.metaProgressVOList = arg_25_0.getMetaProgressListForShow()

	arg_25_0.fillMetaProgressList()

def var_0_0.fillMetaProgressList(arg_26_0):
	if #arg_26_0.metaProgressVOList < 5:
		for iter_26_0 = #arg_26_0.metaProgressVOList + 1, 5:
			table.insert(arg_26_0.metaProgressVOList, False)

def var_0_0.initBannerList(arg_27_0):
	arg_27_0.scrollUIItemList = UIItemList.New(arg_27_0.bannerContainer, arg_27_0.bannerTpl)

	arg_27_0.scrollUIItemList.make(function(arg_28_0, arg_28_1, arg_28_2)
		if arg_28_0 == UIItemList.EventUpdate:
			table.insert(arg_27_0.bannerTFList, arg_28_2)

			local var_28_0 = arg_27_0.metaProgressVOList[arg_28_1 + 1]

			arg_27_0.updateBannerTF(var_28_0, arg_28_2, arg_28_1 + 1))

def var_0_0.updateBannerTF(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	local var_29_0 = arg_29_2
	local var_29_1 = arg_29_0.findTF("ForScale", arg_29_2)
	local var_29_2 = arg_29_0.findTF("WillCome", var_29_1)
	local var_29_3 = arg_29_0.findTF("Empty", var_29_1)
	local var_29_4 = arg_29_0.findTF("Active", var_29_1)

	if arg_29_1:
		local var_29_5 = arg_29_1.isInAct()
		local var_29_6 = arg_29_0.findTF("ActType/Tag", var_29_3)
		local var_29_7 = arg_29_0.findTF("BuildType/Tag", var_29_3)
		local var_29_8 = arg_29_0.findTF("ActType/Tag", var_29_4)
		local var_29_9 = arg_29_0.findTF("BuildType/Tag", var_29_4)

		setActive(var_29_6, var_29_5)
		setActive(var_29_7, var_29_5)
		setActive(var_29_8, var_29_5)
		setActive(var_29_9, var_29_5)

	if arg_29_1:
		local var_29_10 = Ship.New({
			configId = tonumber(arg_29_1.configId .. 1)
		}).getName()
		local var_29_11
		local var_29_12 = arg_29_0.findTF("Empty/ActType/ShipNameMask/ShipNameText", var_29_1)

		setText(var_29_12, var_29_10)
		setScrollText(var_29_12, var_29_10)
		setActive(var_29_12, True)

		local var_29_13 = arg_29_0.findTF("Empty/BuildType/ShipNameMask/ShipNameText", var_29_1)

		setText(var_29_13, var_29_10)
		setScrollText(var_29_13, var_29_10)
		setActive(var_29_13, True)

		local var_29_14 = arg_29_0.findTF("Empty/PassType/ShipNameMask/ShipNameText", var_29_1)

		setText(var_29_14, var_29_10)
		setScrollText(var_29_14, var_29_10)
		setActive(var_29_14, True)

		local var_29_15 = arg_29_0.findTF("Active/ActType/ShipNameMask/ShipNameText", var_29_1)

		setText(var_29_15, var_29_10)
		setScrollText(var_29_15, var_29_10)
		setActive(var_29_15, True)

		local var_29_16 = arg_29_0.findTF("Active/BuildType/ShipNameMask/ShipNameText", var_29_1)

		setText(var_29_16, var_29_10)
		setScrollText(var_29_16, var_29_10)
		setActive(var_29_16, True)

		local var_29_17 = arg_29_0.findTF("Active/PassType/ShipNameMask/ShipNameText", var_29_1)

		setText(var_29_17, var_29_10)
		setScrollText(var_29_17, var_29_10)
		setActive(var_29_17, True)

	if arg_29_1 == False:
		setActive(var_29_2, True)
		setActive(var_29_3, False)
		setActive(var_29_4, False)
	else
		setActive(var_29_2, False)

		local var_29_18 = arg_29_1.isUnlocked()

		setActive(var_29_3, not var_29_18)
		setActive(var_29_4, var_29_18)

		local var_29_19 = arg_29_1.isPtType()
		local var_29_20 = arg_29_1.isPassType()
		local var_29_21 = arg_29_1.isBuildType()

		if not var_29_18:
			local var_29_22 = arg_29_0.findTF("Empty/ActType", var_29_1)
			local var_29_23 = arg_29_0.findTF("Empty/BuildType", var_29_1)
			local var_29_24 = arg_29_0.findTF("Empty/PassType", var_29_1)

			setActive(var_29_22, var_29_19)
			setActive(var_29_23, var_29_21)
			setActive(var_29_24, var_29_20)

			local var_29_25, var_29_26 = arg_29_1.getBannerPathAndName()
			local var_29_27 = LoadSprite(var_29_25, var_29_26)

			setImageSprite(var_29_22, var_29_27)
			setImageSprite(var_29_23, var_29_27)
			setImageSprite(var_29_24, var_29_27)

			if var_29_19:
				local var_29_28 = arg_29_0.findTF("NumText", var_29_22)
				local var_29_29 = string.format("%d", arg_29_1.getSynRate() * 100) .. "%"

				setText(var_29_28, var_29_29)

				local var_29_30 = arg_29_0.findTF("Slider", var_29_22)

				setSlider(var_29_30, 0, 1, arg_29_1.getSynRate())
				setActive(var_29_30, False)

			local var_29_31 = pg.ship_strengthen_meta[arg_29_1.configId].ship_id
			local var_29_32 = Ship.New({
				configId = var_29_31
			})
			local var_29_33 = var_29_32.getMaxStar()
			local var_29_34 = var_29_32.getStar()
			local var_29_35 = arg_29_0.findTF("Empty/StarTpl", var_29_1)
			local var_29_36 = arg_29_0.findTF("Empty/Stars", var_29_1)
			local var_29_37 = UIItemList.New(var_29_36, var_29_35)

			var_29_37.make(function(arg_30_0, arg_30_1, arg_30_2)
				if arg_30_0 == UIItemList.EventUpdate:
					arg_30_1 = arg_30_1 + 1

					local var_30_0 = arg_29_0.findTF("On", arg_30_2)

					setActive(var_30_0, arg_30_1 <= var_29_34))
			var_29_37.align(var_29_33)
		else
			local var_29_38 = arg_29_0.findTF("Active/ActType", var_29_1)
			local var_29_39 = arg_29_0.findTF("Active/BuildType", var_29_1)
			local var_29_40 = arg_29_0.findTF("Active/PassType", var_29_1)

			setActive(var_29_38, var_29_19)
			setActive(var_29_39, var_29_21)
			setActive(var_29_40, var_29_20)

			local var_29_41, var_29_42 = arg_29_1.getBannerPathAndName()
			local var_29_43 = LoadSprite(var_29_41, var_29_42)

			setImageSprite(arg_29_0.findTF("Active", var_29_1), LoadSprite(var_29_41, var_29_42))

			local var_29_44 = arg_29_1.getShip()
			local var_29_45 = var_29_44.getMetaCharacter()

			if var_29_19:
				local var_29_46 = arg_29_0.findTF("NumText", var_29_38)
				local var_29_47 = string.format("%d", var_29_45.getRepairRate() * 100) .. "%"

				setText(var_29_46, var_29_47)

				local var_29_48 = arg_29_0.findTF("Slider", var_29_38)

				setSlider(var_29_48, 0, 1, var_29_45.getRepairRate())
				setActive(var_29_48, False)

			local var_29_49 = var_29_44.getMaxStar()
			local var_29_50 = var_29_44.getStar()
			local var_29_51 = arg_29_0.findTF("Active/StarTpl", var_29_1)
			local var_29_52 = arg_29_0.findTF("Active/Stars", var_29_1)
			local var_29_53 = UIItemList.New(var_29_52, var_29_51)

			var_29_53.make(function(arg_31_0, arg_31_1, arg_31_2)
				if arg_31_0 == UIItemList.EventUpdate:
					arg_31_1 = arg_31_1 + 1

					local var_31_0 = arg_29_0.findTF("On", arg_31_2)

					setActive(var_31_0, arg_31_1 <= var_29_50))
			var_29_53.align(var_29_49)

	onButton(arg_29_0, var_29_0, function()
		if arg_29_0.curMetaIndex != arg_29_3:
			if arg_29_0.curMetaIndex and arg_29_0.curMetaIndex > 0:
				arg_29_0.changeBannerOnClick(arg_29_0.bannerTFList[arg_29_0.curMetaIndex], False)

			arg_29_0.curMetaIndex = arg_29_3

			arg_29_0.changeBannerOnClick(var_29_0, True)
			arg_29_0.updateMain(), SFX_PANEL)

	if arg_29_1 == False:
		setButtonEnabled(var_29_0, False)
	else
		setButtonEnabled(var_29_0, True)

def var_0_0.changeBannerOnClick(arg_33_0, arg_33_1, arg_33_2):
	local var_33_0 = arg_33_1.GetComponent("LayoutElement")
	local var_33_1 = arg_33_0.findTF("ForScale", arg_33_1)

	if arg_33_2 == True:
		setLocalScale(var_33_1, var_0_0.SCALE_ON_PITCH)

		var_33_0.preferredWidth = 338.3
		var_33_0.preferredHeight = 102
	else
		setLocalScale(var_33_1, Vector2.one)

		var_33_0.preferredWidth = 199
		var_33_0.preferredHeight = 60

	local var_33_2 = arg_33_0.findTF("SelectedTag", var_33_1)

	setActive(var_33_2, arg_33_2)

def var_0_0.updateBannerShipName(arg_34_0, arg_34_1):
	local var_34_0 = arg_34_0.findTF("ForScale", arg_34_1)
	local var_34_1 = arg_34_0.findTF("SelectedTag", var_34_0)
	local var_34_2 = isActive(var_34_1)
	local var_34_3
	local var_34_4 = arg_34_0.findTF("Empty/ActType/ShipNameText", var_34_0)

	setActive(var_34_4, var_34_2)

	local var_34_5 = arg_34_0.findTF("Empty/BuildType/ShipNameText", var_34_0)

	setActive(var_34_5, var_34_2)

	local var_34_6 = arg_34_0.findTF("Active/ActType/ShipNameText", var_34_0)

	setActive(var_34_6, var_34_2)

	local var_34_7 = arg_34_0.findTF("Active/BuildType/ShipNameText", var_34_0)

	setActive(var_34_7, var_34_2)

	local var_34_8
	local var_34_9 = arg_34_0.findTF("Empty/ActType/TipText", var_34_0)

	setActive(var_34_9, not var_34_2)

	local var_34_10 = arg_34_0.findTF("Empty/BuildType/TipText", var_34_0)

	setActive(var_34_10, not var_34_2)

	local var_34_11 = arg_34_0.findTF("Active/ActType/Text", var_34_0)

	setActive(var_34_11, not var_34_2)

	local var_34_12 = arg_34_0.findTF("Active/BuildType/Text", var_34_0)

	setActive(var_34_12, not var_34_2)

def var_0_0.updateBannerUIList(arg_35_0):
	arg_35_0.bannerTFList = {}

	arg_35_0.scrollUIItemList.align(#arg_35_0.metaProgressVOList)

def var_0_0.updateStart(arg_36_0):
	local var_36_0 = False

	for iter_36_0, iter_36_1 in ipairs(arg_36_0.metaProgressVOList):
		if iter_36_1 != False:
			var_36_0 = True

			break

	local var_36_1 = arg_36_0.findTF("On", arg_36_0.indexBtn)

	setActive(var_36_1, not arg_36_0.isDefaultStatus())
	setActive(arg_36_0.noCharTF, not var_36_0)
	setActive(arg_36_0.hidePanel, var_36_0)

	if not var_36_0:
		return

	arg_36_0.resetBannerListScale()
	arg_36_0.updateBannerUIList()

	arg_36_0.curMetaIndex = None

	if var_36_0:
		triggerButton(arg_36_0.bannerTFList[1])

def var_0_0.resetBannerListScale(arg_37_0):
	for iter_37_0, iter_37_1 in ipairs(arg_37_0.bannerTFList):
		local var_37_0 = iter_37_1.GetComponent("LayoutElement")
		local var_37_1 = arg_37_0.findTF("ForScale", iter_37_1)

		setLocalScale(var_37_1, Vector2.one)

		var_37_0.preferredWidth = 199
		var_37_0.preferredHeight = 60

def var_0_0.updateMain(arg_38_0, arg_38_1):
	local var_38_0 = arg_38_0.getCurMetaProgressVO()
	local var_38_1 = var_38_0.isUnlocked()

	setActive(arg_38_0.menuPanel, var_38_1)
	setActive(arg_38_0.ptPanel, not var_38_1)
	setActive(arg_38_0.goGetPanel, not var_38_1)
	arg_38_0.updateActTimePanel()

	if not var_38_1:
		local var_38_2 = var_38_0.isPtType()
		local var_38_3 = var_38_0.isPassType()
		local var_38_4 = var_38_0.isBuildType()

		setActive(arg_38_0.ptPanel, var_38_2)
		setActive(arg_38_0.goGetPanel, var_38_3 or var_38_4)

		if var_38_2:
			arg_38_0.updatePTPanel(arg_38_1)
	else
		arg_38_0.TryPlayGuide()

	arg_38_0.updateRedPoints()

	local var_38_5, var_38_6 = var_38_0.getPaintPathAndName()

	setImageSprite(arg_38_0.shipImg, LoadSprite(var_38_5, var_38_6), True)

	local var_38_7, var_38_8 = var_38_0.getBGNamePathAndName()

	setImageSprite(arg_38_0.shipNameImg, LoadSprite(var_38_7, var_38_8), True)

	local var_38_9 = var_38_0.id
	local var_38_10 = MetaCharacterConst.UIConfig[var_38_9]

	setLocalPosition(arg_38_0.shipImg, {
		x = var_38_10[1],
		y = var_38_10[2]
	})
	setLocalScale(arg_38_0.shipImg, {
		x = var_38_10[3],
		y = var_38_10[4]
	})

def var_0_0.TryPlayGuide(arg_39_0):
	pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0024")

def var_0_0.updateActTimePanel(arg_40_0):
	local var_40_0 = arg_40_0.getCurMetaProgressVO()
	local var_40_1 = var_40_0.isUnlocked()
	local var_40_2 = var_40_0.isInAct()

	setActive(arg_40_0.actTimePanel, not var_40_1 and var_40_2)
	setActive(arg_40_0.synBtnLimitTimeTF, var_40_2)

	if var_40_2:
		local var_40_3 = var_40_0.timeConfig[1][1]
		local var_40_4 = var_40_0.timeConfig[2][1]
		local var_40_5 = "%d.%d.%d-%d.%d.%d"
		local var_40_6 = string.format(var_40_5, var_40_3[1], var_40_3[2], var_40_3[3], var_40_4[1], var_40_4[2], var_40_4[3])

		setText(arg_40_0.actTimeText, var_40_6)

		local var_40_7 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_40_0.timeConfig[2])
		local var_40_8 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_40_9 = pg.TimeMgr.GetInstance().DiffDay(var_40_8, var_40_7)
		local var_40_10 = arg_40_0.findTF("Text", arg_40_0.synBtnLimitTimeTF)

		setText(var_40_10, i18n("meta_pt_left", var_40_9))

def var_0_0.updatePTPanel(arg_41_0, arg_41_1):
	local var_41_0 = arg_41_0.getCurMetaProgressVO()
	local var_41_1 = var_41_0.getSynRate()
	local var_41_2 = var_41_1 * 100
	local var_41_3 = tonumber(tostring(var_41_2))

	setImageSprite(arg_41_0.ptIcon, LoadSprite(var_41_0.getPtIconPath()))
	setFillAmount(arg_41_0.ptProgressImg, var_41_1)
	setActive(arg_41_0.ptProgressScaleLine, var_41_1 < 1)

	arg_41_0.ptProgressScaleLine.localEulerAngles = Vector3(0, 0, -360 * var_41_1)

	local var_41_4 = string.format("%d", var_41_3)
	local var_41_5 = (var_41_3 - math.floor(var_41_3)) * 100 == 0
	local var_41_6 = string.format("%2d", (var_41_3 - math.floor(var_41_3)) * 100)

	var_41_6 = var_41_5 and var_41_6 .. "0%" or var_41_6 .. "%"

	setText(arg_41_0.ptProgressRedLeftNumText, var_41_4)
	setText(arg_41_0.ptProgressWhiteLeftNumText, var_41_4)
	setText(arg_41_0.ptProgressRedRightNumText, var_41_6)
	setText(arg_41_0.ptProgressWhiteRightNumText, var_41_6)

	local var_41_7, var_41_8, var_41_9 = var_41_0.metaPtData.GetResProgress()

	setText(arg_41_0.ptProgressRedText, (var_41_9 >= 1 and setColorStr(var_41_7, COLOR_GREEN) or setColorStr(var_41_7, COLOR_RED)) .. "/" .. var_41_8)
	setText(arg_41_0.ptProgressWhiteText, (var_41_9 >= 1 and setColorStr(var_41_7, COLOR_GREEN) or setColorStr(var_41_7, COLOR_RED)) .. "/" .. var_41_8)

	local var_41_10 = var_41_0.getMetaProgressPTState()

	if var_41_10 == MetaProgress.STATE_CAN_FINISH:
		setActive(arg_41_0.ptRedBarImg, True)
		setActive(arg_41_0.ptPreviewBtn, False)
		setActive(arg_41_0.ptGetBtn, False)
		setActive(arg_41_0.ptShowWayBtn, False)
		setActive(arg_41_0.ptInfoPanel, False)
		setActive(arg_41_0.storyInfoPanel, False)
		setActive(arg_41_0.getShipBtn, True)
	elif var_41_10 == MetaProgress.STATE_CAN_AWARD:
		setActive(arg_41_0.ptRedBarImg, False)
		setActive(arg_41_0.ptPreviewBtn, True)
		setActive(arg_41_0.ptGetBtn, True)
		setActive(arg_41_0.ptShowWayBtn, False)
		setActive(arg_41_0.ptGetBtnTag, True)
		setActive(arg_41_0.ptInfoPanel, True)
		setActive(arg_41_0.storyInfoPanel, False)
		setActive(arg_41_0.getShipBtn, False)
		setImageAlpha(arg_41_0.ptPreviewBtn, 0)
		setImageAlpha(arg_41_0.ptGetBtn, 0)
		setImageAlpha(arg_41_0.ptGetBtnTag, 0)
		setImageAlpha(arg_41_0.ptShowWayBtn, 0)
	elif var_41_10 == MetaProgress.STATE_LESS_STORY:
		setActive(arg_41_0.ptRedBarImg, True)
		setActive(arg_41_0.ptPreviewBtn, True)
		setActive(arg_41_0.ptGetBtn, True)
		setActive(arg_41_0.ptShowWayBtn, False)
		setActive(arg_41_0.ptGetBtnTag, False)
		setActive(arg_41_0.ptInfoPanel, False)
		setActive(arg_41_0.storyInfoPanel, True)
		setActive(arg_41_0.getShipBtn, False)

		local var_41_11 = var_41_0.getCurLevelStoryName()

		setText(arg_41_0.storyNameText, var_41_11)
	elif var_41_10 == MetaProgress.STATE_LESS_PT:
		setActive(arg_41_0.ptRedBarImg, False)
		setActive(arg_41_0.ptPreviewBtn, True)
		setActive(arg_41_0.ptGetBtn, False)
		setActive(arg_41_0.ptShowWayBtn, True)
		setActive(arg_41_0.ptGetBtnTag, False)
		setActive(arg_41_0.ptInfoPanel, True)
		setActive(arg_41_0.storyInfoPanel, False)
		setActive(arg_41_0.getShipBtn, False)
		setImageAlpha(arg_41_0.ptPreviewBtn, 0)
		setImageAlpha(arg_41_0.ptGetBtn, 0)
		setImageAlpha(arg_41_0.ptShowWayBtn, 0)

	if var_41_1 > 0 and not arg_41_1:
		if var_41_10 == MetaProgress.STATE_CAN_AWARD or var_41_10 == MetaProgress.STATE_LESS_PT:
			local var_41_12 = math.min(var_41_1, 1)

			arg_41_0.managedTween(LeanTween.value, None, go(arg_41_0.ptPanel), 0, var_41_1, var_41_12).setOnUpdate(System.Action_float(function(arg_42_0)
				setFillAmount(arg_41_0.ptProgressImg, arg_42_0)
				setActive(arg_41_0.ptProgressScaleLine, arg_42_0 < 1)

				arg_41_0.ptProgressScaleLine.localEulerAngles = Vector3(0, 0, -360 * arg_42_0)

				local var_42_0 = arg_42_0 * 100
				local var_42_1 = string.format("%d", var_42_0)
				local var_42_2 = (var_42_0 - math.floor(var_42_0)) * 100 == 0
				local var_42_3 = string.format("%2d", (var_42_0 - math.floor(var_42_0)) * 100)

				var_42_3 = var_42_2 and var_42_3 .. "0%" or var_42_3 .. "%"

				setText(arg_41_0.ptProgressRedLeftNumText, var_42_1)
				setText(arg_41_0.ptProgressWhiteLeftNumText, var_42_1)
				setText(arg_41_0.ptProgressRedRightNumText, var_42_3)
				setText(arg_41_0.ptProgressWhiteRightNumText, var_42_3))).setOnComplete(System.Action(function()
				setFillAmount(arg_41_0.ptProgressImg, var_41_1)
				setActive(arg_41_0.ptProgressScaleLine, var_41_1 < 1)

				arg_41_0.ptProgressScaleLine.localEulerAngles = Vector3(0, 0, -360 * var_41_1)

				local var_43_0 = string.format("%d", var_41_3)
				local var_43_1 = (var_41_3 - math.floor(var_41_3)) * 100 == 0
				local var_43_2 = string.format("%2d", (var_41_3 - math.floor(var_41_3)) * 100)

				var_43_2 = var_43_1 and var_43_2 .. "0%" or var_43_2 .. "%"

				setText(arg_41_0.ptProgressRedLeftNumText, var_43_0)
				setText(arg_41_0.ptProgressWhiteLeftNumText, var_43_0)
				setText(arg_41_0.ptProgressRedRightNumText, var_43_2)
				setText(arg_41_0.ptProgressWhiteRightNumText, var_43_2)
				arg_41_0.managedTween(LeanTween.value, None, go(arg_41_0.ptPanel), 0, 1, var_41_12 / 2).setOnUpdate(System.Action_float(function(arg_44_0)
					setImageAlpha(arg_41_0.ptPreviewBtn, arg_44_0)
					setImageAlpha(arg_41_0.ptGetBtn, arg_44_0)
					setImageAlpha(arg_41_0.ptGetBtnTag, arg_44_0)
					setImageAlpha(arg_41_0.ptShowWayBtn, arg_44_0))).setOnComplete(System.Action(function()
					setImageAlpha(arg_41_0.ptPreviewBtn, 1)
					setImageAlpha(arg_41_0.ptGetBtn, 1)
					setImageAlpha(arg_41_0.ptGetBtnTag, 1)
					setImageAlpha(arg_41_0.ptShowWayBtn, 1)))))
	else
		setImageAlpha(arg_41_0.ptPreviewBtn, 1)
		setImageAlpha(arg_41_0.ptGetBtn, 1)
		setImageAlpha(arg_41_0.ptGetBtnTag, 1)
		setImageAlpha(arg_41_0.ptShowWayBtn, 1)

def var_0_0.updateRedPoints(arg_46_0):
	local var_46_0 = arg_46_0.getCurMetaProgressVO()
	local var_46_1 = var_46_0.id
	local var_46_2 = MetaCharacterConst.isMetaRepairRedTag(var_46_1)

	setActive(arg_46_0.findTF("RepairBtn/Tag", arg_46_0.repairBtn), var_46_2)

	local var_46_3 = not MetaCharacterConst.filteMetaRepairAble(var_46_0)

	setActive(arg_46_0.findTF("Finish", arg_46_0.repairBtn), var_46_3)

	local var_46_4 = MetaCharacterConst.isMetaEnergyRedTag(var_46_1)

	setActive(arg_46_0.findTF("Tag", arg_46_0.energyBtn), var_46_4)

	local var_46_5 = not MetaCharacterConst.filteMetaEnergyAble(var_46_0)

	setActive(arg_46_0.findTF("Finish", arg_46_0.energyBtn), var_46_5)

	local var_46_6 = not MetaCharacterConst.filteMetaTacticsAble(var_46_0)

	setActive(arg_46_0.findTF("Finish", arg_46_0.tacticsBtn), var_46_6)

	local var_46_7 = MetaCharacterConst.isMetaTacticsRedTag(var_46_1)
	local var_46_8 = var_46_0.metaShipVO

	if var_46_8:
		local var_46_9 = arg_46_0.metaCharacterProxy.getMetaTacticsInfoByShipID(var_46_8.id).getTacticsStateForShow()

		setActive(arg_46_0.findTF("Tag", arg_46_0.tacticsBtn), False)
		setActive(arg_46_0.findTF("Learnable", arg_46_0.tacticsBtn), var_46_9 == MetaTacticsInfo.States.LearnAble)
		setActive(arg_46_0.findTF("Learning", arg_46_0.tacticsBtn), var_46_9 == MetaTacticsInfo.States.Learning)
		setActive(arg_46_0.findTF("LearnFinish", arg_46_0.tacticsBtn), var_46_9 == MetaTacticsInfo.States.LearnFinished and var_46_7)
	else
		setActive(arg_46_0.findTF("Tag", arg_46_0.tacticsBtn), False)
		setActive(arg_46_0.findTF("Learnable", arg_46_0.tacticsBtn), False)
		setActive(arg_46_0.findTF("Learning", arg_46_0.tacticsBtn), False)
		setActive(arg_46_0.findTF("LearnFinish", arg_46_0.tacticsBtn), False)

	local var_46_10 = var_46_0.isPtType()
	local var_46_11 = var_46_0.isInAct()
	local var_46_12 = var_46_0.isInArchive()
	local var_46_13 = var_46_10

	setActive(arg_46_0.synDecorateTF, var_46_13)
	setActive(arg_46_0.synBtn, var_46_10)
	setActive(arg_46_0.synBtnLock, var_46_10 and not var_46_11 and not var_46_12)
	setActive(arg_46_0.toggleList[4], var_46_10)
	setActive(arg_46_0.synToggleLock, var_46_10 and not var_46_11 and not var_46_12)

	local var_46_14

	if var_46_13:
		var_46_14 = MetaCharacterConst.isMetaSynRedTag(var_46_1)

		setActive(arg_46_0.findTF("Tag", arg_46_0.synBtn), var_46_14)

	local var_46_15 = not MetaCharacterConst.filteMetaSynAble(var_46_0)

	setActive(arg_46_0.findTF("Finish", arg_46_0.synBtn), var_46_15)
	setActive(arg_46_0.findTF("Tip", arg_46_0.toggleList[var_0_0.PAGES.REPAIR]), var_46_2)
	setActive(arg_46_0.findTF("Tip", arg_46_0.toggleList[var_0_0.PAGES.ENERGY]), var_46_4)
	setActive(arg_46_0.findTF("Tip", arg_46_0.toggleList[var_0_0.PAGES.TACTICS]), var_46_7)
	setActive(arg_46_0.findTF("Tip", arg_46_0.toggleList[var_0_0.PAGES.SYN]), var_46_14)

	for iter_46_0, iter_46_1 in ipairs(arg_46_0.metaProgressVOList):
		local var_46_16 = arg_46_0.bannerTFList[iter_46_0]
		local var_46_17 = arg_46_0.findTF("ForScale/RedPoint", var_46_16)

		if iter_46_1:
			setActive(var_46_17, MetaCharacterConst.isMetaBannerRedPoint(iter_46_1.id))
		else
			setActive(var_46_17, False)

def var_0_0.getCurMetaProgressVO(arg_47_0):
	local var_47_0 = arg_47_0.curMetaIndex

	return arg_47_0.metaProgressVOList[var_47_0]

def var_0_0.refreshBannerTF(arg_48_0):
	local var_48_0 = arg_48_0.getCurMetaProgressVO()
	local var_48_1 = arg_48_0.bannerTFList[arg_48_0.curMetaIndex]

	arg_48_0.updateBannerTF(var_48_0, var_48_1, arg_48_0.curMetaIndex)

def var_0_0.enterMenuPage(arg_49_0, arg_49_1):
	setActive(arg_49_0.hidePanel, not arg_49_1)
	setActive(arg_49_0.indexBtn, not arg_49_1)
	setActive(arg_49_0.toggleBtnsTF, arg_49_1)

def var_0_0.switchPage(arg_50_0, arg_50_1):
	if not arg_50_0.curPageIndex:
		if arg_50_1 == 1:
			setActive(arg_50_0.toggleBtnsTF, True)

		triggerToggle(arg_50_0.toggleList[arg_50_1], True)

def var_0_0.backFromRepair(arg_51_0):
	setActive(arg_51_0.menuPanel, False)
	arg_51_0.managedTween(LeanTween.alpha, None, arg_51_0.shipImg, 1, 0.3).setFrom(0).setOnComplete(System.Action(function()
		setActive(arg_51_0.menuPanel, True)
		setActive(arg_51_0.hidePanel, True)))

def var_0_0.backFromNotRepair(arg_53_0):
	local var_53_0 = arg_53_0.getCurMetaProgressVO().id
	local var_53_1 = MetaCharacterConst.UIConfig[var_53_0]

	setActive(arg_53_0.menuPanel, False)

	local var_53_2 = -250
	local var_53_3 = var_53_1[1]

	arg_53_0.managedTween(LeanTween.moveX, None, rtf(arg_53_0.shipImg), var_53_3, 0.3).setFrom(var_53_2).setOnComplete(System.Action(function()
		setActive(arg_53_0.menuPanel, True)
		setActive(arg_53_0.hidePanel, True)))

def var_0_0.autoOpenFunc(arg_55_0):
	if arg_55_0.contextData.autoOpenShipConfigID:
		local var_55_0 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(arg_55_0.contextData.autoOpenShipConfigID)
		local var_55_1 = arg_55_0.getMetaProgressListForShow()
		local var_55_2 = 0

		for iter_55_0, iter_55_1 in ipairs(var_55_1):
			if iter_55_1 and iter_55_1.id == var_55_0:
				triggerButton(arg_55_0.bannerTFList[iter_55_0])

				arg_55_0.contextData.autoOpenShipConfigID = None

	if arg_55_0.contextData.autoOpenTactics:
		triggerButton(arg_55_0.tacticsBtn)

		arg_55_0.contextData.autoOpenTactics = None

	if arg_55_0.contextData.autoOpenEnergy:
		triggerButton(arg_55_0.energyBtn)

		arg_55_0.contextData.autoOpenEnergy = None

	if arg_55_0.contextData.autoOpenSyn:
		if arg_55_0.getCurMetaProgressVO().isUnlocked():
			triggerButton(arg_55_0.synBtn)

		arg_55_0.contextData.autoOpenSyn = None

	if arg_55_0.contextData.lastPageIndex:
		triggerToggle(arg_55_0.toggleList[arg_55_0.contextData.lastPageIndex], True)

		arg_55_0.contextData.lastPageIndex = None

def var_0_0.openIndexLayer(arg_56_0):
	if not arg_56_0.indexDatas:
		arg_56_0.indexDatas = {}

	local var_56_0 = {
		indexDatas = Clone(arg_56_0.indexDatas),
		customPanels = {
			minHeight = 650,
			typeIndex = {
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.TypeIndexs,
				names = ShipIndexConst.TypeNames
			},
			rarityIndex = {
				mode = CustomIndexLayer.Mode.AND,
				options = ShipIndexConst.MetaRarityIndexs,
				names = ShipIndexConst.MetaRarityNames
			},
			extraIndex = {
				mode = CustomIndexLayer.Mode.OR,
				options = ShipIndexConst.MetaExtraIndexs,
				names = ShipIndexConst.MetaExtraNames
			}
		},
		groupList = {
			{
				dropdown = False,
				titleTxt = "indexsort_type",
				titleENTxt = "indexsort_typeeng",
				tags = {
					"typeIndex"
				}
			},
			{
				dropdown = False,
				titleTxt = "indexsort_rarity",
				titleENTxt = "indexsort_rarityeng",
				tags = {
					"rarityIndex"
				}
			},
			{
				dropdown = False,
				titleTxt = "indexsort_extraindex",
				titleENTxt = "indexsort_indexeng",
				tags = {
					"extraIndex"
				}
			}
		},
		def callback:(arg_57_0)
			if not isActive(arg_56_0._tf):
				return

			arg_56_0.indexDatas.typeIndex = arg_57_0.typeIndex
			arg_56_0.indexDatas.rarityIndex = arg_57_0.rarityIndex
			arg_56_0.indexDatas.extraIndex = arg_57_0.extraIndex
			arg_56_0.metaProgressVOList = arg_56_0.getMetaProgressListForShow()

			arg_56_0.fillMetaProgressList()
			arg_56_0.updateStart()
	}

	arg_56_0.emit(MetaCharacterMediator.OPEN_INDEX_LAYER, var_56_0)

def var_0_0.isDefaultStatus(arg_58_0):
	return (not arg_58_0.indexDatas.typeIndex or arg_58_0.indexDatas.typeIndex == ShipIndexConst.TypeAll) and (not arg_58_0.indexDatas.rarityIndex or arg_58_0.indexDatas.rarityIndex == ShipIndexConst.RarityAll) and (not arg_58_0.indexDatas.extraIndex or arg_58_0.indexDatas.extraIndex == ShipIndexConst.MetaExtraAll)

def var_0_0.overLayPanel(arg_59_0, arg_59_1):
	if arg_59_1 == True:
		pg.UIMgr.GetInstance().OverlayPanel(arg_59_0.blurPanel, {
			groupName = LayerWeightConst.GROUP_META
		})
	elif arg_59_1 == False:
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_59_0.blurPanel, arg_59_0._tf)

def var_0_0.getMetaProgressListForShow(arg_60_0):
	local var_60_0 = {}
	local var_60_1 = arg_60_0.metaCharacterProxy.getMetaProgressVOList()
	local var_60_2
	local var_60_3
	local var_60_4

	for iter_60_0, iter_60_1 in ipairs(var_60_1):
		local var_60_5 = MetaCharacterConst.filteMetaByType(iter_60_1, arg_60_0.indexDatas.typeIndex)
		local var_60_6 = MetaCharacterConst.filteMetaByRarity(iter_60_1, arg_60_0.indexDatas.rarityIndex)
		local var_60_7 = MetaCharacterConst.filteMetaExtra(iter_60_1, arg_60_0.indexDatas.extraIndex)

		if var_60_5 and var_60_6 and var_60_7 and iter_60_1.isShow():
			if iter_60_1.isPtType() and iter_60_1.isInAct():
				var_60_2 = iter_60_1
			elif iter_60_1.isPassType() and iter_60_1.isInAct():
				var_60_3 = iter_60_1
			elif iter_60_1.isBuildType() and iter_60_1.isInAct():
				var_60_4 = iter_60_1
			else
				table.insert(var_60_0, iter_60_1)

	if var_60_4:
		table.insert(var_60_0, 1, var_60_4)

	if var_60_3:
		table.insert(var_60_0, 1, var_60_3)

	if var_60_2:
		table.insert(var_60_0, 1, var_60_2)

	return var_60_0

def var_0_0.filteMetaProgressList(arg_61_0):
	local var_61_0 = arg_61_0.getMetaProgressListForShow()
	local var_61_1 = {}

	for iter_61_0, iter_61_1 in ipairs(var_61_0):
		local var_61_2 = MetaCharacterConst.filteMetaByType(iter_61_1, arg_61_0.indexDatas.typeIndex)
		local var_61_3 = MetaCharacterConst.filteMetaByRarity(iter_61_1, arg_61_0.indexDatas.rarityIndex)
		local var_61_4 = MetaCharacterConst.filteMetaExtra(iter_61_1, arg_61_0.indexDatas.extraIndex)

		if var_61_2 and var_61_3 and var_61_4:
			table.insert(var_61_1, iter_61_1)

	return var_61_1

def var_0_0.getOneStepPTAwardLevelAndCount(arg_62_0):
	local var_62_0 = arg_62_0.getCurMetaProgressVO()
	local var_62_1 = var_62_0.metaPtData.GetResProgress()
	local var_62_2 = var_62_0.metaPtData.targets
	local var_62_3 = var_62_0.getStoryIndexList()
	local var_62_4 = var_62_0.unlockPTLevel
	local var_62_5 = 0

	for iter_62_0 = 1, var_62_4 - 1:
		local var_62_6 = False
		local var_62_7 = False

		if var_62_1 >= var_62_2[iter_62_0]:
			var_62_6 = True

		local var_62_8 = var_62_3[iter_62_0]

		if var_62_8 == 0:
			var_62_7 = True
		elif pg.NewStoryMgr.GetInstance().IsPlayed(var_62_8):
			var_62_7 = True

		if var_62_6 and var_62_7:
			var_62_5 = iter_62_0
		else
			break

	return var_62_5, var_62_2[var_62_5]

return var_0_0
