local var_0_0 = class("TechnologyTreeScene", import("..base.BaseUI"))

var_0_0.NationTrige = {
	All = 0,
	Mot = 3,
	Meta = 2,
	Other = 1
}
var_0_0.TypeTrige = {
	All = 0,
	Other = 1
}

def var_0_0.getUIName(arg_1_0):
	return "TechnologyTreeUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.initNationToggleUIList()
	arg_2_0.initTecClassUIList()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.initTypeToggleUIList()
	arg_3_0.updateTecItemList()
	arg_3_0.addBtnListener()
	setText(arg_3_0.pointNumText, arg_3_0.point)
	arg_3_0.updateRedPoint(getProxy(TechnologyNationProxy).getShowRedPointTag())

	if not PlayerPrefs.HasKey("first_comein_technologytree"):
		triggerButton(arg_3_0.helpBtn)
		PlayerPrefs.SetInt("first_comein_technologytree", 1)
		PlayerPrefs.Save()

def var_0_0.updateRedPoint(arg_4_0, arg_4_1):
	setActive(arg_4_0.redPointImg, arg_4_1)

def var_0_0.willExit(arg_5_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_5_0.blurPanel, arg_5_0._tf)

	arg_5_0.rightLSC.onReturnItem = None

	if arg_5_0.emptyPage:
		arg_5_0.emptyPage.Destroy()

		arg_5_0.emptyPage = None

def var_0_0.initData(arg_6_0):
	TechnologyConst.CreateMetaClassConfig()

	arg_6_0.nationToggleList = {}
	arg_6_0.typeToggleList = {}
	arg_6_0.nationSelectedList = {}
	arg_6_0.typeSelectedList = {}
	arg_6_0.nationSelectedCount = 0
	arg_6_0.typeSelectedCount = 0
	arg_6_0.lastNationTrige = None
	arg_6_0.lastTypeTrige = None
	arg_6_0.countInEveryRow = 5
	arg_6_0.collectionProxy = getProxy(CollectionProxy)
	arg_6_0.nationProxy = getProxy(TechnologyNationProxy)
	arg_6_0.curClassIDList = None
	arg_6_0.groupIDGotList = {}

	local var_6_0 = arg_6_0.collectionProxy.shipGroups

	for iter_6_0, iter_6_1 in pairs(var_6_0):
		arg_6_0.groupIDGotList[#arg_6_0.groupIDGotList + 1] = iter_6_1.id

	arg_6_0.point = arg_6_0.nationProxy.getPoint()
	arg_6_0.expanded = {}

def var_0_0.findUI(arg_7_0):
	arg_7_0.nationAllToggle = None
	arg_7_0.nationAllToggleCom = None
	arg_7_0.nationMetaToggle = arg_7_0.findTF("Adapt/Left/MetaToggle")
	arg_7_0.nationMetaToggleCom = GetComponent(arg_7_0.nationMetaToggle, "Toggle")
	arg_7_0.nationMotToggle = arg_7_0.findTF("Adapt/Left/MotToggle")
	arg_7_0.nationMotToggleCom = GetComponent(arg_7_0.nationMotToggle, "Toggle")
	arg_7_0.typeAllToggle = None
	arg_7_0.typeAllToggleCom = None
	arg_7_0.blurPanel = arg_7_0.findTF("blur_panel")
	arg_7_0.adapt = arg_7_0.findTF("adapt", arg_7_0.blurPanel)
	arg_7_0.backBtn = arg_7_0.findTF("top/back", arg_7_0.adapt)
	arg_7_0.homeBtn = arg_7_0.findTF("top/option", arg_7_0.adapt)
	arg_7_0.additionDetailBtn = arg_7_0.findTF("AdditionDetailBtn", arg_7_0.adapt)
	arg_7_0.switchBtn = arg_7_0.findTF("SwitchToggle", arg_7_0.adapt)
	arg_7_0.pointTF = arg_7_0.findTF("PointCount", arg_7_0.adapt)
	arg_7_0.pointNumText = arg_7_0.findTF("PointCount/PointNumText", arg_7_0.adapt)
	arg_7_0.redPointImg = arg_7_0.findTF("RedPoint", arg_7_0.switchBtn)
	arg_7_0.helpBtn = arg_7_0.findTF("help_btn", arg_7_0.adapt)
	arg_7_0.leftContainer = arg_7_0.findTF("Adapt/Left/Scroll View/Content")
	arg_7_0.selectNationItem = arg_7_0.findTF("SelectCampItem")
	arg_7_0.bottomContainer = arg_7_0.findTF("Adapt/Bottom/Content")
	arg_7_0.selectTypeItem = arg_7_0.findTF("SelectTypeItem")
	arg_7_0.rightContainer = arg_7_0.findTF("Adapt/Right/Container")
	arg_7_0.rightLSC = arg_7_0.rightContainer.GetComponent("LScrollRect")
	arg_7_0.rightLayoutGroup = arg_7_0.rightContainer.GetComponent("VerticalLayoutGroup")
	arg_7_0.headItem = arg_7_0.findTF("HeadItem")
	arg_7_0.rowHeight = arg_7_0.headItem.rect.height
	arg_7_0.maxRowHeight = 853.5
	arg_7_0.emptyPage = BaseEmptyListPage.New(arg_7_0.findTF("Adapt/Right/ViewPort"), arg_7_0.event)

def var_0_0.onBackPressed(arg_8_0):
	triggerButton(arg_8_0.backBtn)

def var_0_0.addBtnListener(arg_9_0):
	onButton(arg_9_0, arg_9_0.backBtn, function()
		arg_9_0.closeView(), SFX_CANCEL)
	onButton(arg_9_0, arg_9_0.additionDetailBtn, function()
		arg_9_0.emit(TechnologyConst.OPEN_ALL_BUFF_DETAIL))
	onToggle(arg_9_0, arg_9_0.switchBtn, function(arg_12_0)
		if arg_12_0:
			setActive(arg_9_0.pointTF, False)
			pg.UIMgr.GetInstance().OverlayPanel(arg_9_0.blurPanel, {
				weight = LayerWeightConst.SECOND_LAYER
			})
			arg_9_0.emit(TechnologyConst.OPEN_TECHNOLOGY_NATION_LAYER)
		else
			setActive(arg_9_0.pointTF, True)
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_9_0.blurPanel, arg_9_0._tf)
			arg_9_0.emit(TechnologyConst.CLOSE_TECHNOLOGY_NATION_LAYER), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.helpBtn, function()
		if pg.gametip.help_technologytree:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = pg.gametip.help_technologytree.tip,
				weight = LayerWeightConst.TOP_LAYER
			}), SFX_PANEL)

def var_0_0.initNationToggleUIList(arg_14_0):
	arg_14_0.nationAllToggle = None
	arg_14_0.nationAllToggleCom = None
	arg_14_0.nationMetaToggle = arg_14_0.findTF("Adapt/Left/MetaToggle")
	arg_14_0.nationMetaToggleCom = GetComponent(arg_14_0.nationMetaToggle, "Toggle")
	arg_14_0.nationMotToggle = arg_14_0.findTF("Adapt/Left/MotToggle")
	arg_14_0.nationMotToggleCom = GetComponent(arg_14_0.nationMotToggle, "Toggle")

	setActive(arg_14_0.nationMetaToggle, not LOCK_TEC_META)

	if LOCK_TEC_META:
		local var_14_0 = arg_14_0.findTF("Adapt/Left/Scroll View")

		var_14_0.offsetMin = Vector2.New(var_14_0.offsetMin.x, 0)

	local var_14_1 = UIItemList.New(arg_14_0.leftContainer, arg_14_0.selectNationItem)

	var_14_1.make(function(arg_15_0, arg_15_1, arg_15_2)
		if arg_15_0 == UIItemList.EventUpdate:
			arg_14_0.findTF("UnSelectedImg", arg_15_2).GetComponent("Image").sprite, arg_14_0.findTF("SelectedImg", arg_15_2).GetComponent("Image").sprite = TechnologyConst.GetNationSpriteByIndex(arg_15_1 + 1)

			if arg_15_1 == 0:
				arg_14_0.nationAllToggle = arg_15_2
				arg_14_0.nationAllToggleCom = GetComponent(arg_15_2, "Toggle")
				arg_14_0.nationAllToggleCom.interactable = False

				triggerToggle(arg_15_2, True)
			else
				arg_14_0.nationToggleList[arg_15_1] = arg_15_2

				triggerToggle(arg_15_2, False)

			setActive(arg_15_2, True))
	var_14_1.align(#TechnologyConst.NationResName)
	setActive(arg_14_0.nationMotToggle, not LOCK_TEC_MOT)

	if not LOCK_TEC_MOT:
		setParent(arg_14_0.nationMotToggle, arg_14_0.leftContainer)

	onToggle(arg_14_0, arg_14_0.nationAllToggle, function(arg_16_0)
		if arg_16_0 == True:
			arg_14_0.lastNationTrige = var_0_0.NationTrige.All
			arg_14_0.nationAllToggleCom.interactable = False
			arg_14_0.nationSelectedCount = 0
			arg_14_0.nationSelectedList = {}

			arg_14_0.updateTecItemList()
			arg_14_0.updateNationToggleUIList()
		else
			arg_14_0.nationAllToggleCom.interactable = True, SFX_PANEL)
	onToggle(arg_14_0, arg_14_0.nationMetaToggle, function(arg_17_0)
		if arg_17_0 == True:
			arg_14_0.lastNationTrige = var_0_0.NationTrige.Meta
			arg_14_0.nationMetaToggleCom.interactable = False
			arg_14_0.nationSelectedCount = 0
			arg_14_0.nationSelectedList = {}

			arg_14_0.updateTecItemList()
			arg_14_0.updateNationToggleUIList()
		else
			arg_14_0.nationMetaToggleCom.interactable = True, SFX_PANEL)
	onToggle(arg_14_0, arg_14_0.nationMotToggle, function(arg_18_0)
		if arg_18_0 == True:
			arg_14_0.lastNationTrige = var_0_0.NationTrige.Mot
			arg_14_0.nationMotToggleCom.interactable = False
			arg_14_0.nationSelectedCount = 0
			arg_14_0.nationSelectedList = {}

			arg_14_0.updateTecItemList()
			arg_14_0.updateNationToggleUIList()
		else
			arg_14_0.nationMotToggleCom.interactable = True, SFX_PANEL)

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.nationToggleList):
		onToggle(arg_14_0, iter_14_1, function(arg_19_0)
			if arg_19_0 == True:
				arg_14_0.lastNationTrige = var_0_0.NationTrige.Other
				arg_14_0.nationSelectedCount = arg_14_0.nationSelectedCount + 1

				table.insert(arg_14_0.nationSelectedList, TechnologyConst.NationOrder[iter_14_0])

				if arg_14_0.nationSelectedCount < #arg_14_0.nationToggleList:
					arg_14_0.updateNationToggleUIList()
					arg_14_0.updateTecItemList()
				elif arg_14_0.nationSelectedCount == #arg_14_0.nationToggleList:
					arg_14_0.updateNationToggleUIList()
			elif arg_14_0.nationSelectedCount > 0:
				arg_14_0.nationSelectedCount = arg_14_0.nationSelectedCount - 1

				local var_19_0 = table.indexof(arg_14_0.nationSelectedList, TechnologyConst.NationOrder[iter_14_0], 1)

				if var_19_0:
					table.remove(arg_14_0.nationSelectedList, var_19_0)

				if arg_14_0.nationSelectedCount > 0:
					arg_14_0.updateNationToggleUIList()
					arg_14_0.updateTecItemList()
				elif arg_14_0.nationSelectedCount == 0:
					arg_14_0.updateNationToggleUIList(), SFX_PANEL)

def var_0_0.updateNationToggleUIList(arg_20_0):
	if arg_20_0.lastNationTrige == var_0_0.NationTrige.All:
		_.each(arg_20_0.nationToggleList, function(arg_21_0)
			triggerToggle(arg_21_0, False)
			onNextTick(function()
				local var_22_0 = arg_20_0.findTF("UnSelectedImg", arg_21_0)

				setActive(var_22_0, True)))
		triggerToggle(arg_20_0.nationMetaToggle, False)
		triggerToggle(arg_20_0.nationMotToggle, False)
	elif arg_20_0.lastNationTrige == var_0_0.NationTrige.Meta:
		triggerToggle(arg_20_0.nationAllToggle, False)
		_.each(arg_20_0.nationToggleList, function(arg_23_0)
			triggerToggle(arg_23_0, False))
		triggerToggle(arg_20_0.nationMotToggle, False)
	elif arg_20_0.lastNationTrige == var_0_0.NationTrige.Mot:
		triggerToggle(arg_20_0.nationAllToggle, False)
		_.each(arg_20_0.nationToggleList, function(arg_24_0)
			triggerToggle(arg_24_0, False))
		triggerToggle(arg_20_0.nationMetaToggle, False)
	elif arg_20_0.lastNationTrige == var_0_0.NationTrige.Other:
		if arg_20_0.nationSelectedCount <= 0 or arg_20_0.nationSelectedCount >= #arg_20_0.nationToggleList:
			triggerToggle(arg_20_0.nationAllToggle, True)
		else
			triggerToggle(arg_20_0.nationAllToggle, False)
			triggerToggle(arg_20_0.nationMetaToggle, False)
			triggerToggle(arg_20_0.nationMotToggle, False)

def var_0_0.initTypeToggleUIList(arg_25_0):
	arg_25_0.typeAllToggle = None
	arg_25_0.typeAllToggleCom = None

	local var_25_0 = UIItemList.New(arg_25_0.bottomContainer, arg_25_0.selectTypeItem)

	var_25_0.make(function(arg_26_0, arg_26_1, arg_26_2)
		if arg_26_0 == UIItemList.EventUpdate:
			arg_25_0.findTF("UnSelectedImg", arg_26_2).GetComponent("Image").sprite, arg_25_0.findTF("SelectedImg", arg_26_2).GetComponent("Image").sprite = TechnologyConst.GetTypeSpriteByIndex(arg_26_1 + 1)
			arg_26_1 = arg_26_1 + 1

			if arg_26_1 == #TechnologyConst.TypeResName:
				arg_25_0.typeAllToggle = arg_26_2
				arg_25_0.typeAllToggleCom = GetComponent(arg_26_2, "Toggle")
				arg_25_0.typeAllToggleCom.interactable = False

				triggerToggle(arg_26_2, True)
			else
				arg_25_0.typeToggleList[arg_26_1] = arg_26_2

				triggerToggle(arg_26_2, False)

			setActive(arg_26_2, True))
	var_25_0.align(#TechnologyConst.TypeResName)
	onToggle(arg_25_0, arg_25_0.typeAllToggle, function(arg_27_0)
		arg_25_0.lastTypeTrige = var_0_0.TypeTrige.All

		if arg_27_0 == True:
			arg_25_0.typeAllToggleCom.interactable = False
			arg_25_0.typeSelectedCount = 0
			arg_25_0.typeSelectedList = {}

			arg_25_0.updateTecItemList()
			arg_25_0.updateTypeToggleUIList()
		else
			arg_25_0.typeAllToggleCom.interactable = True)

	for iter_25_0, iter_25_1 in ipairs(arg_25_0.typeToggleList):
		onToggle(arg_25_0, iter_25_1, function(arg_28_0)
			arg_25_0.lastTypeTrige = var_0_0.TypeTrige.Other

			if arg_28_0 == True:
				arg_25_0.typeSelectedCount = arg_25_0.typeSelectedCount + 1

				for iter_28_0, iter_28_1 in ipairs(TechnologyConst.TypeOrder[iter_25_0]):
					table.insert(arg_25_0.typeSelectedList, iter_28_1)

				if arg_25_0.typeSelectedCount < #arg_25_0.typeToggleList:
					arg_25_0.updateTypeToggleUIList()
					arg_25_0.updateTecItemList()
				elif arg_25_0.typeSelectedCount == #arg_25_0.typeToggleList:
					arg_25_0.updateTypeToggleUIList()
			elif arg_25_0.typeSelectedCount > 0:
				arg_25_0.typeSelectedCount = arg_25_0.typeSelectedCount - 1

				for iter_28_2, iter_28_3 in ipairs(TechnologyConst.TypeOrder[iter_25_0]):
					local var_28_0 = table.indexof(arg_25_0.typeSelectedList, iter_28_3, 1)

					if var_28_0:
						table.remove(arg_25_0.typeSelectedList, var_28_0)

				if arg_25_0.typeSelectedCount > 0:
					arg_25_0.updateTypeToggleUIList()
					arg_25_0.updateTecItemList()
				elif arg_25_0.typeSelectedCount == 0:
					arg_25_0.updateTypeToggleUIList(), SFX_PANEL)

def var_0_0.updateTypeToggleUIList(arg_29_0):
	if arg_29_0.lastTypeTrige == var_0_0.TypeTrige.All:
		_.each(arg_29_0.typeToggleList, function(arg_30_0)
			triggerToggle(arg_30_0, False)
			onNextTick(function()
				local var_31_0 = arg_29_0.findTF("UnSelectedImg", arg_30_0)

				setActive(var_31_0, True)))
	elif arg_29_0.lastTypeTrige == var_0_0.TypeTrige.Other:
		if arg_29_0.typeSelectedCount <= 0 or arg_29_0.typeSelectedCount >= #arg_29_0.typeToggleList:
			triggerToggle(arg_29_0.typeAllToggle, True)
		else
			triggerToggle(arg_29_0.typeAllToggle, False)

def var_0_0.updatePreferredHeight(arg_32_0, arg_32_1, arg_32_2):
	local var_32_0 = tf(arg_32_1).Find("ShipScrollView/ShipContainer")
	local var_32_1 = arg_32_2 + arg_32_0.rowHeight

	arg_32_0.rightLayoutGroup.padding.bottom = arg_32_0.rightLayoutGroup.padding.bottom + var_32_1 - GetComponent(arg_32_1, "LayoutElement").preferredHeight
	GetComponent(arg_32_1, "LayoutElement").preferredHeight = var_32_1

	local var_32_2 = tf(arg_32_1).Find("ClickBtn/ArrowBtn")

	setLocalRotation(var_32_2, {
		z = arg_32_2 > 0 and 0 or 180
	})

def var_0_0.onClassItemUpdate(arg_33_0, arg_33_1, arg_33_2):
	local var_33_0 = arg_33_0.findTF("Name/NameText", arg_33_2)
	local var_33_1 = arg_33_0.findTF("CampBG", arg_33_2)
	local var_33_2 = arg_33_0.findTF("Level/LevelImg", arg_33_2)
	local var_33_3 = arg_33_0.findTF("Level/TypeTextImg", arg_33_2)
	local var_33_4 = arg_33_0.findTF("ClickBtn", arg_33_2)
	local var_33_5 = arg_33_0.findTF("ArrowBtn", var_33_4)
	local var_33_6 = arg_33_0.getClassConfigForShow(arg_33_1 + 1)
	local var_33_7 = var_33_6.name
	local var_33_8 = var_33_6.nation
	local var_33_9 = var_33_6.shiptype
	local var_33_10 = var_33_6.t_level
	local var_33_11 = var_33_6.ships
	local var_33_12 = arg_33_0.isMetaOn()
	local var_33_13 = arg_33_0.isMotOn()

	setText(var_33_0, var_33_7)

	local var_33_14

	if var_33_12 or var_33_13:
		setActive(var_33_2, False)
		setActive(var_33_3, False)

		if var_33_12:
			var_33_14 = GetSpriteFromAtlas("TecNation", "bg_nation_meta")
		elif var_33_13:
			var_33_14 = GetSpriteFromAtlas("TecNation", "bg_nation_mot")
	else
		setImageSprite(var_33_2, GetSpriteFromAtlas("TecClassLevelIcon", "T" .. var_33_10), True)
		setImageSprite(var_33_3, GetSpriteFromAtlas("ShipType", "ch_title_" .. var_33_9), True)
		setActive(var_33_2, True)
		setActive(var_33_3, True)

		var_33_14 = GetSpriteFromAtlas("TecNation", "bg_nation_" .. var_33_8)

	setImageSprite(var_33_1, var_33_14)

	local var_33_15 = arg_33_0.findTF("ClickBtn/ArrowBtn", arg_33_2)

	setLocalRotation(var_33_15, {
		z = 180
	})

	local var_33_16 = arg_33_0.findTF("ShipScrollView/ShipContainer", arg_33_2)

	arg_33_0.updateShipItemList(var_33_11, var_33_16)

	arg_33_0.expanded[arg_33_1] = 0

	arg_33_0.updatePreferredHeight(arg_33_2, arg_33_0.expanded[arg_33_1])
	setActive(var_33_4, #var_33_11 > 5)
	onButton(arg_33_0, var_33_4, function()
		if defaultValue(arg_33_0.expanded[arg_33_1], 0) > 0:
			arg_33_0.expanded[arg_33_1] = 0
		else
			arg_33_0.expanded[arg_33_1] = var_33_16.rect.height - arg_33_0.rowHeight

		arg_33_0.updatePreferredHeight(arg_33_2, arg_33_0.expanded[arg_33_1]), SFX_PANEL)

def var_0_0.onClassItemReturn(arg_35_0, arg_35_1, arg_35_2):
	if defaultValue(arg_35_0.expanded[arg_35_1], 0) > 0:
		arg_35_0.expanded[arg_35_1] = 0

		arg_35_0.updatePreferredHeight(arg_35_2, arg_35_0.expanded[arg_35_1])

def var_0_0.initTecClassUIList(arg_36_0):
	function arg_36_0.rightLSC.onUpdateItem(arg_37_0, arg_37_1)
		arg_36_0.onClassItemUpdate(arg_37_0, arg_37_1)

	function arg_36_0.rightLSC.onReturnItem(arg_38_0, arg_38_1)
		arg_36_0.onClassItemReturn(arg_38_0, arg_38_1)

def var_0_0.updateTecItemList(arg_39_0):
	arg_39_0.expanded = {}

	local var_39_0 = arg_39_0.getClassIDListForShow()

	if arg_39_0.rightLSC.totalCount != 0:
		arg_39_0.rightLSC.SetTotalCount(0)

	arg_39_0.rightLSC.SetTotalCount(#var_39_0)
	arg_39_0.rightLSC.BeginLayout()
	arg_39_0.rightLSC.EndLayout()

	local var_39_1 = #var_39_0

	if var_39_1 <= 0:
		arg_39_0.emptyPage.ExecuteAction("ShowOrHide", True)
		arg_39_0.emptyPage.ExecuteAction("SetEmptyText", i18n("technology_filter_placeholder"))
	elif var_39_1 > 0 and arg_39_0.emptyPage.GetLoaded():
		arg_39_0.emptyPage.ExecuteAction("ShowOrHide", False)

def var_0_0.updateShipItemList(arg_40_0, arg_40_1, arg_40_2):
	local var_40_0 = UIItemList.New(arg_40_2, arg_40_0.headItem)

	var_40_0.make(function(arg_41_0, arg_41_1, arg_41_2)
		if arg_41_0 == UIItemList.EventUpdate:
			local var_41_0 = arg_40_0.findTF("BaseImg", arg_41_2)
			local var_41_1 = arg_40_0.findTF("BaseImg/CharImg", arg_41_2)
			local var_41_2 = arg_40_0.findTF("NameBG", arg_41_2)
			local var_41_3 = arg_40_0.findTF("NameText", var_41_2)
			local var_41_4 = arg_40_0.findTF("Frame", arg_41_2)
			local var_41_5 = arg_40_0.findTF("Star", arg_41_2)
			local var_41_6 = arg_40_0.findTF("Star/StarImg", arg_41_2)
			local var_41_7 = arg_40_0.findTF("Info", arg_41_2)
			local var_41_8 = arg_40_0.findTF("PointText", var_41_7)
			local var_41_9 = arg_40_0.findTF("BuffGet", var_41_7)
			local var_41_10 = arg_40_0.findTF("TypeIcon", var_41_9)
			local var_41_11 = arg_40_0.findTF("AttrIcon", var_41_10)
			local var_41_12 = arg_40_0.findTF("NumText", var_41_10)
			local var_41_13 = arg_40_0.findTF("Lock", var_41_7)
			local var_41_14 = arg_40_0.findTF("BuffComplete", var_41_7)
			local var_41_15 = arg_40_0.findTF("TypeIcon", var_41_14)
			local var_41_16 = arg_40_0.findTF("AttrIcon", var_41_15)
			local var_41_17 = arg_40_0.findTF("NumText", var_41_15)
			local var_41_18 = arg_40_0.findTF("BottomBG", arg_41_2)
			local var_41_19 = arg_40_0.findTF("BottomBG/StatusUnknow", arg_41_2)
			local var_41_20 = arg_40_0.findTF("BottomBG/StatusResearching", arg_41_2)
			local var_41_21 = arg_40_0.findTF("ViewIcon", arg_41_2)
			local var_41_22 = arg_40_0.findTF("keyansaohguang", arg_41_2)
			local var_41_23 = arg_40_1[arg_41_1 + 1]

			setText(var_41_3, shortenString(ShipGroup.getDefaultShipNameByGroupID(var_41_23), 6))

			local var_41_24 = var_41_23 * 10 + 1

			setImageSprite(var_41_0, GetSpriteFromAtlas("shipraritybaseicon", "base_" .. pg.ship_data_statistics[var_41_24].rarity))
			LoadSpriteAsync("shipmodels/" .. Ship.getPaintingName(var_41_24), function(arg_42_0)
				if arg_42_0 and not arg_40_0.exited:
					setImageSprite(var_41_1, arg_42_0, True)

					rtf(var_41_1).pivot = getSpritePivot(arg_42_0))

			if table.indexof(arg_40_0.groupIDGotList, var_41_23, 1):
				local var_41_25 = pg.fleet_tech_ship_template[var_41_23].add_get_shiptype[1]
				local var_41_26 = pg.fleet_tech_ship_template[var_41_23].add_get_attr
				local var_41_27 = pg.fleet_tech_ship_template[var_41_23].add_get_value

				setImageSprite(var_41_10, GetSpriteFromAtlas("ui/technologytreeui_atlas", "label_" .. var_41_25))
				setImageSprite(var_41_11, GetSpriteFromAtlas("attricon", pg.attribute_info_by_type[var_41_26].name))
				setText(var_41_12, "+" .. var_41_27)
				setActive(var_41_9, True)

				local var_41_28 = arg_40_0.collectionProxy.getShipGroup(var_41_23)

				if var_41_28.maxLV < TechnologyConst.SHIP_LEVEL_FOR_BUFF:
					setActive(var_41_20, True)
					setActive(var_41_19, False)
					setActive(var_41_14, False)
					setImageSprite(var_41_4, GetSpriteFromAtlas("ui/technologytreeui_atlas", "card_bg_normal"))
					setActive(var_41_18, True)
					setActive(var_41_21, True)
					setActive(var_41_13, True)
					setActive(var_41_22, False)

					if var_41_28.star == pg.fleet_tech_ship_template[var_41_23].max_star:
						setText(var_41_8, "+" .. pg.fleet_tech_ship_template[var_41_23].pt_get + pg.fleet_tech_ship_template[var_41_23].pt_upgrage)
					else
						setText(var_41_8, "+" .. pg.fleet_tech_ship_template[var_41_23].pt_get)
				else
					local var_41_29 = pg.fleet_tech_ship_template[var_41_23].add_level_shiptype[1]
					local var_41_30 = pg.fleet_tech_ship_template[var_41_23].add_level_attr
					local var_41_31 = pg.fleet_tech_ship_template[var_41_23].add_level_value

					setImageSprite(var_41_15, GetSpriteFromAtlas("ui/technologytreeui_atlas", "label_" .. var_41_29))
					setImageSprite(var_41_16, GetSpriteFromAtlas("attricon", pg.attribute_info_by_type[var_41_30].name))
					setText(var_41_17, "+" .. var_41_31)
					setActive(var_41_14, True)

					if var_41_28.star == pg.fleet_tech_ship_template[var_41_23].max_star:
						setText(var_41_8, "+" .. pg.fleet_tech_ship_template[var_41_23].pt_get + pg.fleet_tech_ship_template[var_41_23].pt_level + pg.fleet_tech_ship_template[var_41_23].pt_upgrage)
						setImageSprite(var_41_4, GetSpriteFromAtlas("ui/technologytreeui_atlas", "card_bg_finished"))
						setActive(var_41_18, False)
						setActive(var_41_21, False)
						setActive(var_41_20, False)
						setActive(var_41_19, False)
						setActive(var_41_22, True)
					else
						setText(var_41_8, "+" .. pg.fleet_tech_ship_template[var_41_23].pt_get + pg.fleet_tech_ship_template[var_41_23].pt_level)
						setImageSprite(var_41_4, GetSpriteFromAtlas("ui/technologytreeui_atlas", "card_bg_normal"))
						setActive(var_41_18, True)
						setActive(var_41_21, True)
						setActive(var_41_20, True)
						setActive(var_41_19, False)
						setActive(var_41_22, False)

					setActive(var_41_13, False)

				setImageColor(var_41_1, Color.New(1, 1, 1, 1))
				setActive(var_41_2, True)
				setActive(var_41_7, True)
				setActive(var_41_5, True)

				if var_41_28.star == pg.fleet_tech_ship_template[var_41_23].max_star:
					setActive(var_41_6, True)
				else
					setActive(var_41_6, False)

				onButton(arg_40_0, arg_41_2, function()
					arg_40_0.emit(TechnologyConst.OPEN_SHIP_BUFF_DETAIL, var_41_23, var_41_28.maxLV, var_41_28.star))
			else
				setImageSprite(var_41_4, GetSpriteFromAtlas("ui/technologytreeui_atlas", "card_bg_normal"))
				setImageColor(var_41_1, Color.New(0, 0, 0, 0.4))
				setActive(var_41_21, False)
				setActive(var_41_2, False)
				setActive(var_41_7, False)
				setActive(var_41_20, False)
				setActive(var_41_19, True)
				setActive(var_41_5, False)
				setActive(var_41_13, False)
				setActive(var_41_22, False)
				removeOnButton(arg_41_2)

			setActive(arg_41_2, True))
	var_40_0.align(#arg_40_1)

def var_0_0.getClassIDListForShow(arg_44_0, arg_44_1, arg_44_2):
	arg_44_1 = arg_44_1 or arg_44_0.nationSelectedList
	arg_44_2 = arg_44_2 or arg_44_0.typeSelectedList

	local var_44_0 = arg_44_0.isMetaOn()
	local var_44_1 = arg_44_0.isMotOn()

	if not var_44_0 and not var_44_1:
		local var_44_2 = TechnologyConst.GetOrderClassList()
		local var_44_3

		if #arg_44_1 == 0 and #arg_44_2 == 0:
			var_44_3 = var_44_2
		else
			local var_44_4 = #arg_44_1 == 0 and TechnologyConst.NationOrder or arg_44_1

			var_44_3 = _.select(var_44_2, function(arg_45_0)
				local var_45_0 = pg.fleet_tech_ship_class[arg_45_0].nation

				if table.contains(var_44_4, var_45_0):
					if #arg_44_0.typeSelectedList == 0:
						return True
					else
						local var_45_1 = pg.fleet_tech_ship_class[arg_45_0].shiptype

						return table.contains(arg_44_0.typeSelectedList, var_45_1)
				else
					return False)

		arg_44_0.curClassIDList = var_44_3

		return var_44_3
	elif var_44_0:
		arg_44_0.curMetaClassIDList = TechnologyConst.GetOrderMetaClassList(arg_44_2)

		return arg_44_0.curMetaClassIDList
	elif var_44_1:
		arg_44_0.curMotClassIDList = TechnologyConst.GetOrderMotClassList(arg_44_2)

		return arg_44_0.curMotClassIDList

def var_0_0.getClassConfigForShow(arg_46_0, arg_46_1):
	local var_46_0 = arg_46_0.isMetaOn()
	local var_46_1 = arg_46_0.isMotOn()

	if not var_46_0 and not var_46_1:
		local var_46_2 = arg_46_0.curClassIDList[arg_46_1]

		return pg.fleet_tech_ship_class[var_46_2]
	elif var_46_0:
		local var_46_3 = arg_46_0.curMetaClassIDList[arg_46_1]

		return TechnologyConst.GetMetaClassConfig(var_46_3, arg_46_0.typeSelectedList)
	elif var_46_1:
		local var_46_4 = arg_46_0.curMotClassIDList[arg_46_1]

		return TechnologyConst.GetMotClassConfig(var_46_4, arg_46_0.typeSelectedList)

def var_0_0.isMetaOn(arg_47_0):
	if arg_47_0.lastNationTrige == var_0_0.NationTrige.All:
		return False
	elif arg_47_0.lastNationTrige == var_0_0.NationTrige.Mot:
		return False

	return arg_47_0.nationMetaToggleCom.isOn

def var_0_0.isMotOn(arg_48_0):
	if arg_48_0.lastNationTrige == var_0_0.NationTrige.All:
		return False
	elif arg_48_0.lastNationTrige == var_0_0.NationTrige.Meta:
		return False

	return arg_48_0.nationMotToggleCom.isOn

return var_0_0
