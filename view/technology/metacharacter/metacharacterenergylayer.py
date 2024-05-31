local var_0_0 = class("MetaCharacterEnergyLayer", import("...base.BaseUI"))
local var_0_1 = pg.ship_meta_breakout

def var_0_0.getUIName(arg_1_0):
	return "MetaCharacterEnergyUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initUITipText()
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updateShipImg()
	arg_3_0.updateNamePanel()
	arg_3_0.updateChar()
	arg_3_0.updateAttrPanel()
	arg_3_0.updateMaterialPanel()
	arg_3_0.initPreviewPanel()
	arg_3_0.enablePartialBlur()

	if arg_3_0.contextData.isMainOpen:
		arg_3_0.contextData.isMainOpen = None

		arg_3_0.moveShipImg(True)

	arg_3_0.moveRightPanel()
	arg_3_0.TryPlayGuide()

def var_0_0.willExit(arg_4_0):
	arg_4_0.moveShipImg(False)
	arg_4_0.recycleChar()

	if arg_4_0.previewer:
		arg_4_0.previewer.clear()

		arg_4_0.previewer = None

	arg_4_0.disablePartialBlur()

def var_0_0.onBackPressed(arg_5_0):
	if isActive(arg_5_0.previewTF):
		arg_5_0.closePreviewPanel()

		return
	else
		arg_5_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.initUITipText(arg_6_0):
	local var_6_0 = arg_6_0.findTF("Preview/FinalAttrPanel/TitleText")
	local var_6_1 = arg_6_0.findTF("Preview/FinalAttrPanel/TipText")
	local var_6_2 = arg_6_0.findTF("RightPanel/MaterialPanel/StarMax/Text")
	local var_6_3 = arg_6_0.findTF("RightPanel/MaterialPanel/TipText")

	setText(var_6_0, i18n("meta_energy_preview_title"))
	setText(var_6_1, i18n("meta_energy_preview_tip"))
	setText(var_6_2, i18n("word_level_upperLimit"))
	setText(var_6_3, i18n("meta_break"))

def var_0_0.initData(arg_7_0):
	arg_7_0.shipPrefab = None
	arg_7_0.shipModel = None
	arg_7_0.metaCharacterProxy = getProxy(MetaCharacterProxy)
	arg_7_0.bayProxy = getProxy(BayProxy)
	arg_7_0.curMetaShipID = arg_7_0.contextData.shipID
	arg_7_0.curShipVO = None
	arg_7_0.curMetaCharacterVO = None

	arg_7_0.updateData()

def var_0_0.initUI(arg_8_0):
	arg_8_0.shipImg = arg_8_0.findTF("ShipImg")
	arg_8_0.nameTF = arg_8_0.findTF("NamePanel")
	arg_8_0.nameScrollText = arg_8_0.findTF("NameMask/NameText", arg_8_0.nameTF)
	arg_8_0.shipTypeImg = arg_8_0.findTF("TypeImg", arg_8_0.nameTF)
	arg_8_0.enNameText = arg_8_0.findTF("NameENText", arg_8_0.nameTF)

	local var_8_0 = arg_8_0.findTF("StarTpl", arg_8_0.nameTF)
	local var_8_1 = arg_8_0.findTF("StarContainer", arg_8_0.nameTF)

	arg_8_0.nameTFStarUIList = UIItemList.New(var_8_1, var_8_0)
	arg_8_0.previewBtn = arg_8_0.findTF("PreviewBtn")
	arg_8_0.rightPanel = arg_8_0.findTF("RightPanel")
	arg_8_0.qCharContain = arg_8_0.findTF("DetailPanel/QChar", arg_8_0.rightPanel)
	arg_8_0.starTpl = arg_8_0.findTF("DetailPanel/RarePanel/StarTpl", arg_8_0.rightPanel)

	setActive(arg_8_0.starTpl, False)

	arg_8_0.starsFrom = arg_8_0.findTF("DetailPanel/RarePanel/StarsFrom", arg_8_0.rightPanel)
	arg_8_0.starsTo = arg_8_0.findTF("DetailPanel/RarePanel/StarsTo", arg_8_0.rightPanel)
	arg_8_0.starOpera = arg_8_0.findTF("DetailPanel/RarePanel/OpImg", arg_8_0.rightPanel)
	arg_8_0.starFromList = UIItemList.New(arg_8_0.starsFrom, arg_8_0.starTpl)
	arg_8_0.starToList = UIItemList.New(arg_8_0.starsTo, arg_8_0.starTpl)
	arg_8_0.attrTpl = arg_8_0.findTF("DetailPanel/AttrTpl", arg_8_0.rightPanel)

	setActive(arg_8_0.attrTpl, False)

	arg_8_0.attrsContainer = arg_8_0.findTF("DetailPanel/AttrsContainer", arg_8_0.rightPanel)
	arg_8_0.attrsList = UIItemList.New(arg_8_0.attrsContainer, arg_8_0.attrTpl)
	arg_8_0.materialPanel = arg_8_0.findTF("MaterialPanel", arg_8_0.rightPanel)
	arg_8_0.levelNumText = arg_8_0.findTF("Info/LevelTipText", arg_8_0.materialPanel)
	arg_8_0.infoTF = arg_8_0.findTF("Info", arg_8_0.materialPanel)
	arg_8_0.repairRateText = arg_8_0.findTF("Info/ProgressTipText", arg_8_0.materialPanel)
	arg_8_0.materialTF = arg_8_0.findTF("Info/Material", arg_8_0.materialPanel)
	arg_8_0.breakOutTipImg = arg_8_0.findTF("TipText", arg_8_0.materialPanel)
	arg_8_0.goldTF = arg_8_0.findTF("Gold", arg_8_0.materialPanel)
	arg_8_0.goldNumText = arg_8_0.findTF("NumText", arg_8_0.goldTF)
	arg_8_0.starMaxTF = arg_8_0.findTF("StarMax", arg_8_0.materialPanel)
	arg_8_0.activeBtn = arg_8_0.findTF("ActiveBtn", arg_8_0.materialPanel)
	arg_8_0.activeBtnDisable = arg_8_0.findTF("ActiveBtnDisable", arg_8_0.materialPanel)
	arg_8_0.previewTF = arg_8_0.findTF("Preview")
	arg_8_0.previewBG = arg_8_0.findTF("BG", arg_8_0.previewTF)
	arg_8_0.previewPanel = arg_8_0.findTF("PreviewPanel", arg_8_0.previewTF)
	arg_8_0.stages = arg_8_0.findTF("StageScrollRect/Stages", arg_8_0.previewPanel)
	arg_8_0.stagesSnap = arg_8_0.findTF("StageScrollRect", arg_8_0.previewPanel).GetComponent("HorizontalScrollSnap")
	arg_8_0.breakView = arg_8_0.findTF("Content/Text", arg_8_0.previewPanel)
	arg_8_0.sea = arg_8_0.findTF("Sea", arg_8_0.previewPanel)
	arg_8_0.rawImage = arg_8_0.sea.GetComponent("RawImage")

	setActive(arg_8_0.rawImage, False)

	arg_8_0.healTF = arg_8_0.findTF("Resources/Heal")
	arg_8_0.healTF.transform.localPosition = Vector3(-360, 50, 40)

	setActive(arg_8_0.healTF, False)

	arg_8_0.seaLoading = arg_8_0.findTF("BG/Loading", arg_8_0.previewPanel)
	arg_8_0.previewAttrTpl = arg_8_0.findTF("FinalAttrPanel/AttrTpl", arg_8_0.previewTF)
	arg_8_0.previewAttrContainer = arg_8_0.findTF("FinalAttrPanel/AttrsContainer", arg_8_0.previewTF)
	arg_8_0.previewAttrUIItemList = UIItemList.New(arg_8_0.previewAttrContainer, arg_8_0.previewAttrTpl)

def var_0_0.addListener(arg_9_0):
	onButton(arg_9_0, arg_9_0.previewBtn, function()
		arg_9_0.openPreviewPanel(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.previewBG, function()
		arg_9_0.closePreviewPanel(), SFX_CANCEL)
	onButton(arg_9_0, arg_9_0.activeBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("meta_energy_active_box_tip"),
			def onYes:()
				pg.m02.sendNotification(GAME.ENERGY_META_ACTIVATION, {
					shipId = arg_9_0.curMetaShipID
				}),
			weight = LayerWeightConst.TOP_LAYER
		}), SFX_PANEL)

def var_0_0.updateData(arg_14_0):
	arg_14_0.curShipVO = arg_14_0.bayProxy.getShipById(arg_14_0.curMetaShipID)
	arg_14_0.curMetaCharacterVO = arg_14_0.curShipVO.getMetaCharacter()

def var_0_0.TryPlayGuide(arg_15_0):
	pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0026")

def var_0_0.updateShipImg(arg_16_0):
	local var_16_0, var_16_1 = MetaCharacterConst.GetMetaCharacterPaintPath(arg_16_0.curMetaCharacterVO.id, True)

	setImageSprite(arg_16_0.shipImg, LoadSprite(var_16_0, var_16_1), True)

	local var_16_2 = arg_16_0.curMetaCharacterVO.id
	local var_16_3 = MetaCharacterConst.UIConfig[var_16_2]

	setLocalPosition(arg_16_0.shipImg, {
		x = var_16_3[5],
		y = var_16_3[6]
	})
	setLocalScale(arg_16_0.shipImg, {
		x = var_16_3[3],
		y = var_16_3[4]
	})

def var_0_0.updateNamePanel(arg_17_0):
	local var_17_0 = arg_17_0.curShipVO
	local var_17_1 = arg_17_0.curMetaCharacterVO
	local var_17_2 = var_17_0.getName()

	setScrollText(arg_17_0.nameScrollText, var_17_2)

	local var_17_3 = var_17_0.getShipType()

	setImageSprite(arg_17_0.shipTypeImg, LoadSprite("shiptype", var_17_3))

	local var_17_4 = var_17_0.getConfig("english_name")

	setText(arg_17_0.enNameText, var_17_4)

	local var_17_5 = var_17_0.getMaxStar()
	local var_17_6 = var_17_0.getStar()

	arg_17_0.nameTFStarUIList.make(function(arg_18_0, arg_18_1, arg_18_2)
		if arg_18_0 == UIItemList.EventUpdate:
			local var_18_0 = arg_17_0.findTF("empty", arg_18_2)
			local var_18_1 = arg_17_0.findTF("on", arg_18_2)

			arg_18_1 = arg_18_1 + 1

			setActive(var_18_1, arg_18_1 <= var_17_6))
	arg_17_0.nameTFStarUIList.align(var_17_5)

def var_0_0.updateChar(arg_19_0):
	return

def var_0_0.recycleChar(arg_20_0):
	if arg_20_0.shipPrefab and arg_20_0.shipModel:
		PoolMgr.GetInstance().ReturnSpineChar(arg_20_0.shipPrefab, arg_20_0.shipModel)

		arg_20_0.shipPrefab = None
		arg_20_0.shipModel = None

def var_0_0.updateAttrPanel(arg_21_0):
	local var_21_0 = arg_21_0.curShipVO
	local var_21_1 = arg_21_0.curMetaCharacterVO.getBreakOutInfo()

	local function var_21_2(arg_22_0, arg_22_1)
		local var_22_0 = var_21_1.getNextInfo()
		local var_22_1 = Clone(var_21_0)

		var_22_1.configId = var_22_0.id

		local var_22_2 = MetaCharacterConst.ENERGY_ATTRS[arg_22_0 + 1]
		local var_22_3 = 0
		local var_22_4 = 0

		if AttributeType.Expend != var_22_2:
			local var_22_5 = var_21_0.getShipProperties()
			local var_22_6 = var_22_1.getShipProperties()

			var_22_3 = math.floor(var_22_5[var_22_2])
			var_22_4 = math.floor(var_22_6[var_22_2])
		else
			var_22_3 = math.floor(var_21_0.getBattleTotalExpend())
			var_22_4 = math.floor(var_22_1.getBattleTotalExpend())

		setText(arg_22_1.Find("NameText"), AttributeType.Type2Name(var_22_2))
		setText(arg_22_1.Find("CurValueText"), var_22_3)
		setActive(arg_22_1.Find("AddValueText"), True)
		setText(arg_22_1.Find("AddValueText"), "+" .. var_22_4 - var_22_3)
		setText(arg_22_1.Find("NextValueText"), var_22_4)
		arg_21_0.starFromList.align(var_21_0.getStar())
		arg_21_0.starToList.align(var_22_1.getStar())

	local function var_21_3(arg_23_0, arg_23_1)
		local var_23_0 = var_21_0.getShipProperties()
		local var_23_1 = MetaCharacterConst.ENERGY_ATTRS[arg_23_0 + 1]
		local var_23_2 = 0

		if AttributeType.Expend != var_23_1:
			local var_23_3 = var_21_0.getShipProperties()

			var_23_2 = math.floor(var_23_3[var_23_1])
		else
			var_23_2 = math.floor(var_21_0.getBattleTotalExpend())

		setText(arg_23_1.Find("NameText"), AttributeType.Type2Name(var_23_1))
		setText(arg_23_1.Find("CurValueText"), var_23_2)
		setText(arg_23_1.Find("NextValueText"), setColorStr(var_23_2, COLOR_GREEN))
		setText(arg_23_1.Find("AddValueText"), "+0")
		setActive(arg_23_1.Find("AddValueText"), False)
		arg_21_0.starFromList.align(var_21_0.getStar())
		arg_21_0.starToList.align(0)

	arg_21_0.attrsList.make(function(arg_24_0, arg_24_1, arg_24_2)
		if arg_24_0 == UIItemList.EventUpdate:
			if var_21_1.hasNextInfo():
				var_21_2(arg_24_1, arg_24_2)
				setActive(arg_21_0.starOpera, True)
			else
				var_21_3(arg_24_1, arg_24_2)
				setActive(arg_21_0.starOpera, False))
	arg_21_0.attrsList.align(#MetaCharacterConst.ENERGY_ATTRS)

def var_0_0.updateMaterialPanel(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.curShipVO
	local var_25_1 = arg_25_0.curMetaCharacterVO
	local var_25_2 = var_25_1.getBreakOutInfo()
	local var_25_3 = getProxy(BagProxy)

	if not var_25_2.hasNextInfo():
		setActive(arg_25_0.infoTF, False)
		setActive(arg_25_0.breakOutTipImg, False)
		setActive(arg_25_0.goldTF, False)
		setActive(arg_25_0.starMaxTF, True)
		setActive(arg_25_0.activeBtn, False)
		setActive(arg_25_0.activeBtnDisable, True)

		return
	else
		setActive(arg_25_0.infoTF, True)
		setActive(arg_25_0.breakOutTipImg, True)
		setActive(arg_25_0.goldTF, True)
		setActive(arg_25_0.starMaxTF, False)
		setActive(arg_25_0.activeBtn, True)
		setActive(arg_25_0.activeBtnDisable, False)

	local var_25_4 = True
	local var_25_5
	local var_25_6
	local var_25_7, var_25_8 = var_25_2.getConsume()
	local var_25_9
	local var_25_10
	local var_25_11
	local var_25_12 = var_25_8[1].itemId
	local var_25_13 = var_25_8[1].count
	local var_25_14 = var_25_3.getItemCountById(var_25_12)
	local var_25_15 = arg_25_0.findTF("Item", arg_25_0.materialTF)
	local var_25_16 = arg_25_0.findTF("icon_bg/count", var_25_15)
	local var_25_17 = {
		type = DROP_TYPE_ITEM,
		id = var_25_12,
		count = var_25_14
	}

	updateDrop(var_25_15, var_25_17, {
		hideName = True
	})
	onButton(arg_25_0, var_25_15, function()
		arg_25_0.emit(BaseUI.ON_DROP, var_25_17), SFX_PANEL)
	setText(var_25_16, setColorStr(var_25_14, var_25_14 < var_25_13 and COLOR_RED or COLOR_GREEN) .. "/" .. var_25_13)

	if var_25_14 < var_25_13:
		var_25_4 = False

	local var_25_18 = getProxy(PlayerProxy).getData().gold

	setText(arg_25_0.goldNumText, var_25_18 < var_25_7 and setColorStr(var_25_7, COLOR_RED) or var_25_7)

	if var_25_18 < var_25_7:
		var_25_4 = False

		onButton(arg_25_0, arg_25_0.activeBtnDisable, function()
			local var_27_0 = Item.getConfigData(59001).name
			local var_27_1 = i18n("switch_to_shop_tip_2", i18n("word_gold"))
			local var_27_2 = i18n("text_noRes_info_tip", var_27_0, var_25_7 - var_25_18)
			local var_27_3 = var_27_1 .. "\n" .. i18n("text_noRes_tip", var_27_2)

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = var_27_3,
				weight = LayerWeightConst.SECOND_LAYER,
				def onYes:()
					local var_28_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(MetaCharacterMediator)

					if var_28_0:
						var_28_0.data.autoOpenShipConfigID = arg_25_0.curShipVO.configId
						var_28_0.data.autoOpenEnergy = True

					arg_25_0.closeView()
					gotoChargeScene(ChargeScene.TYPE_ITEM)
			}), SFX_PANEL)

	local var_25_19 = arg_25_0.levelNumText
	local var_25_20 = arg_25_0.repairRateText
	local var_25_21
	local var_25_22
	local var_25_23, var_25_24 = var_25_2.getLimited()
	local var_25_25 = var_25_0.level

	var_25_25 = var_25_23 > var_25_0.level and setColorStr(var_25_25, COLOR_RED) or setColorStr(var_25_25, COLOR_GREEN)

	setText(var_25_19, i18n("meta_energy_ship_level_need", var_25_25, var_25_23))

	local var_25_26 = var_25_1.getRepairRate() * 100 .. "%%"

	var_25_26 = var_25_1.getRepairRate() < var_25_24 / 100 and setColorStr(var_25_26, COLOR_RED) or setColorStr(var_25_26, COLOR_GREEN)

	setText(var_25_20, i18n("meta_energy_ship_repairrate_need", var_25_26, var_25_24 .. "%%"))

	if var_25_23 > var_25_0.level:
		var_25_4 = False

	if var_25_1.getRepairRate() < var_25_24 / 100:
		var_25_4 = False

	setActive(arg_25_0.activeBtn, var_25_4)
	setActive(arg_25_0.activeBtnDisable, not var_25_4)

def var_0_0.moveShipImg(arg_29_0, arg_29_1):
	local var_29_0 = arg_29_0.curMetaCharacterVO.id
	local var_29_1 = MetaCharacterConst.UIConfig[var_29_0]
	local var_29_2 = arg_29_1 and -2000 or var_29_1[5]
	local var_29_3 = arg_29_1 and var_29_1[5] or -2000

	arg_29_0.managedTween(LeanTween.moveX, None, rtf(arg_29_0.shipImg), var_29_3, 0.2).setFrom(var_29_2)

def var_0_0.moveRightPanel(arg_30_0):
	local var_30_0 = 2000
	local var_30_1 = 577.64

	arg_30_0.managedTween(LeanTween.moveX, None, rtf(arg_30_0.rightPanel), var_30_1, 0.2).setFrom(var_30_0)

def var_0_0.updatePreviewAttrListPanel(arg_31_0):
	local var_31_0 = arg_31_0.curShipVO
	local var_31_1 = arg_31_0.curMetaCharacterVO
	local var_31_2 = {
		AttributeType.Durability,
		AttributeType.Cannon,
		AttributeType.Torpedo,
		AttributeType.AntiAircraft,
		AttributeType.Air,
		AttributeType.Reload,
		AttributeType.ArmorType,
		AttributeType.Dodge
	}
	local var_31_3 = Clone(var_31_0)

	var_31_3.level = 125

	local var_31_4 = var_31_3.getMetaCharacter()
	local var_31_5 = intProperties(var_31_4.getFinalAddition(var_31_3))

	arg_31_0.previewAttrUIItemList.make(function(arg_32_0, arg_32_1, arg_32_2)
		if arg_32_0 == UIItemList.EventUpdate:
			local var_32_0 = arg_31_0.findTF("AttrIcon", arg_32_2)
			local var_32_1 = arg_31_0.findTF("NameText", arg_32_2)
			local var_32_2 = arg_31_0.findTF("AddValueText", arg_32_2)
			local var_32_3 = var_31_2[arg_32_1 + 1]

			setImageSprite(var_32_0, LoadSprite("attricon", var_32_3))
			setText(var_32_1, AttributeType.Type2Name(var_32_3))

			if var_32_3 == AttributeType.ArmorType:
				setText(var_32_2, var_31_3.getShipArmorName())
			else
				setText(var_32_2, var_31_5[var_32_3] or 0))
	arg_31_0.previewAttrUIItemList.align(#var_31_2)

def var_0_0.initPreviewPanel(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_0.curShipVO
	local var_33_1 = arg_33_0.curMetaCharacterVO

	arg_33_0.breakIds = arg_33_0.getAllBreakIDs(var_33_1.id)

	for iter_33_0 = 1, 3:
		local var_33_2 = arg_33_0.breakIds[iter_33_0]
		local var_33_3 = var_0_1[var_33_2]
		local var_33_4 = arg_33_0.findTF("Stage" .. iter_33_0, arg_33_0.stages)

		onToggle(arg_33_0, var_33_4, function(arg_34_0)
			if arg_34_0:
				local var_34_0 = var_33_3.breakout_view
				local var_34_1 = checkExist(pg.ship_data_template[var_33_3.breakout_id], {
					"specific_type"
				}) or {}

				for iter_34_0, iter_34_1 in ipairs(var_34_1):
					var_34_0 = var_34_0 .. "/" .. i18n(ShipType.SpecificTableTips[iter_34_1])

				changeToScrollText(arg_33_0.breakView, var_34_0)
				arg_33_0.switchStage(var_33_2), SFX_PANEL)

		if iter_33_0 == 1:
			triggerToggle(var_33_4, True)

	onButton(arg_33_0, arg_33_0.seaLoading, function()
		if not arg_33_0.previewer:
			arg_33_0.showBarrage())
	arg_33_0.updatePreviewAttrListPanel()

def var_0_0.closePreviewPanel(arg_36_0):
	if arg_36_0.previewer:
		arg_36_0.previewer.clear()

		arg_36_0.previewer = None

	setActive(arg_36_0.previewTF, False)
	setActive(arg_36_0.rawImage, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_36_0.previewTF, arg_36_0._tf)

def var_0_0.openPreviewPanel(arg_37_0):
	setActive(arg_37_0.previewTF, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_37_0.previewTF, False, {
		weight = LayerWeightConst.TOP_LAYER
	})
	arg_37_0.playLoadingAni()

def var_0_0.playLoadingAni(arg_38_0):
	setActive(arg_38_0.seaLoading, True)

def var_0_0.stopLoadingAni(arg_39_0):
	setActive(arg_39_0.seaLoading, False)

def var_0_0.getAllBreakIDs(arg_40_0, arg_40_1):
	local var_40_0 = {}

	for iter_40_0, iter_40_1 in ipairs(var_0_1.all):
		if math.floor(iter_40_1 / 10) == arg_40_1:
			table.insert(var_40_0, iter_40_1)

	return var_40_0

def var_0_0.getWaponIdsById(arg_41_0, arg_41_1):
	return var_0_1[arg_41_1].weapon_ids

def var_0_0.getAllWeaponIds(arg_42_0):
	local var_42_0 = {}

	for iter_42_0, iter_42_1 in ipairs(arg_42_0.breakIds):
		local var_42_1 = Clone(var_0_1[iter_42_1].weapon_ids)
		local var_42_2 = {
			def __add:(arg_43_0, arg_43_1)
				for iter_43_0, iter_43_1 in ipairs(arg_43_0):
					if not table.contains(arg_43_1, iter_43_1):
						table.insert(arg_43_1, iter_43_1)

				return arg_43_1
		}

		setmetatable(var_42_0, var_42_2)

		var_42_0 = var_42_0 + var_42_1

	return var_42_0

def var_0_0.showBarrage(arg_44_0):
	local var_44_0 = arg_44_0.bayProxy.getShipById(arg_44_0.curMetaShipID)
	local var_44_1 = var_44_0.getMetaCharacter()

	arg_44_0.previewer = WeaponPreviewer.New(arg_44_0.rawImage)

	arg_44_0.previewer.configUI(arg_44_0.healTF)
	arg_44_0.previewer.setDisplayWeapon(arg_44_0.getWaponIdsById(arg_44_0.breakOutId))
	arg_44_0.previewer.load(40000, var_44_0, arg_44_0.getAllWeaponIds(), function()
		arg_44_0.stopLoadingAni())

def var_0_0.switchStage(arg_46_0, arg_46_1):
	if arg_46_0.breakOutId == arg_46_1:
		return

	arg_46_0.breakOutId = arg_46_1

	if arg_46_0.previewer:
		arg_46_0.previewer.setDisplayWeapon(arg_46_0.getWaponIdsById(arg_46_0.breakOutId))

def var_0_0.enablePartialBlur(arg_47_0):
	if arg_47_0._tf:
		local var_47_0 = {}

		table.insert(var_47_0, arg_47_0.previewBtn)
		table.insert(var_47_0, arg_47_0.rightPanel)
		pg.UIMgr.GetInstance().OverlayPanelPB(arg_47_0._tf, {
			pbList = var_47_0,
			groupName = LayerWeightConst.GROUP_META,
			weight = LayerWeightConst.BASE_LAYER - 1
		})

def var_0_0.disablePartialBlur(arg_48_0):
	if arg_48_0._tf:
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_48_0._tf)

return var_0_0
