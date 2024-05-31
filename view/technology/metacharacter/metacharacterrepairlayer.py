local var_0_0 = class("MetaCharacterRepairLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MetaCharacterRepairUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initTipText()
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()

	for iter_2_0, iter_2_1 in ipairs(MetaCharacterConst.REPAIR_ATTRS):
		if not arg_2_0.curMetaCharacterVO.getAttrVO(iter_2_1).isLock():
			triggerToggle(arg_2_0.attrTFList[iter_2_1], True)

			break

def var_0_0.didEnter(arg_3_0):
	arg_3_0.doRepairProgressPanelAni()
	arg_3_0.updateAttrListPanel()
	arg_3_0.updateRepairBtn(True)
	arg_3_0.updateDetailPanel()
	arg_3_0.TryPlayGuide()

def var_0_0.willExit(arg_4_0):
	return

def var_0_0.onBackPressed(arg_5_0):
	if isActive(arg_5_0.repairEffectBoxPanel):
		arg_5_0.closeRepairEffectBoxPanel()

		return
	elif isActive(arg_5_0.detailPanel):
		arg_5_0.closeDetailPanel()

		return
	else
		arg_5_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.initTipText(arg_6_0):
	local var_6_0 = arg_6_0.findTF("Repair/AttrListPanel/AttrItemContainer/AttrItemCannon/SelectedPanel/AttrRepairTipText")
	local var_6_1 = arg_6_0.findTF("Repair/AttrListPanel/AttrItemContainer/AttrItemTorpedo/SelectedPanel/AttrRepairTipText")
	local var_6_2 = arg_6_0.findTF("Repair/AttrListPanel/AttrItemContainer/AttrItemAir/SelectedPanel/AttrRepairTipText")
	local var_6_3 = arg_6_0.findTF("Repair/AttrListPanel/AttrItemContainer/AttrItemReload/SelectedPanel/AttrRepairTipText")

	setText(var_6_0, i18n("meta_repair"))
	setText(var_6_1, i18n("meta_repair"))
	setText(var_6_2, i18n("meta_repair"))
	setText(var_6_3, i18n("meta_repair"))

def var_0_0.initData(arg_7_0):
	arg_7_0.metaCharacterProxy = getProxy(MetaCharacterProxy)
	arg_7_0.bayProxy = getProxy(BayProxy)
	arg_7_0.attrTFList = {}
	arg_7_0.curAttrName = None
	arg_7_0.curMetaShipID = arg_7_0.contextData.shipID
	arg_7_0.curShipVO = None
	arg_7_0.curMetaCharacterVO = None

	arg_7_0.updateData()

def var_0_0.findUI(arg_8_0):
	arg_8_0.repairPanel = arg_8_0.findTF("Repair")
	arg_8_0.attrListPanel = arg_8_0.findTF("AttrListPanel", arg_8_0.repairPanel)
	arg_8_0.attrItemContainer = arg_8_0.findTF("AttrItemContainer", arg_8_0.attrListPanel)
	arg_8_0.attrCannonTF = arg_8_0.findTF("AttrItemCannon", arg_8_0.attrItemContainer)
	arg_8_0.attrTorpedoTF = arg_8_0.findTF("AttrItemTorpedo", arg_8_0.attrItemContainer)
	arg_8_0.attrAirTF = arg_8_0.findTF("AttrItemAir", arg_8_0.attrItemContainer)
	arg_8_0.attrReloadTF = arg_8_0.findTF("AttrItemReload", arg_8_0.attrItemContainer)
	arg_8_0.attrTFList.cannon = arg_8_0.attrCannonTF
	arg_8_0.attrTFList.torpedo = arg_8_0.attrTorpedoTF
	arg_8_0.attrTFList.air = arg_8_0.attrAirTF
	arg_8_0.attrTFList.reload = arg_8_0.attrReloadTF
	arg_8_0.repairPercentText = arg_8_0.findTF("SynProgressPanel/SynRate/NumTextText", arg_8_0.repairPanel)
	arg_8_0.repairSliderTF = arg_8_0.findTF("SynProgressPanel/Slider", arg_8_0.repairPanel)
	arg_8_0.repairBtn = arg_8_0.findTF("RepairBtn", arg_8_0.repairPanel)
	arg_8_0.repairBtnDisable = arg_8_0.findTF("RepairBtnDisable", arg_8_0.repairPanel)
	arg_8_0.showDetailLine = arg_8_0.findTF("ShowDetailLine")
	arg_8_0.showDetailBtn = arg_8_0.findTF("ShowDetailBtn", arg_8_0.showDetailLine)
	arg_8_0.detailPanel = arg_8_0.findTF("Detail")
	arg_8_0.detailBG = arg_8_0.findTF("BG", arg_8_0.detailPanel)
	arg_8_0.detailTF = arg_8_0.findTF("Panel", arg_8_0.detailPanel)
	arg_8_0.detailCloseBtn = arg_8_0.findTF("CloseBtn", arg_8_0.detailTF)
	arg_8_0.detailLineTpl = arg_8_0.findTF("DetailLineTpl", arg_8_0.detailTF)
	arg_8_0.detailItemTpl = arg_8_0.findTF("DetailItemTpl", arg_8_0.detailTF)
	arg_8_0.detailItemContainer = arg_8_0.findTF("ScrollView/Viewport/Content", arg_8_0.detailTF)
	arg_8_0.repairEffectBoxPanel = arg_8_0.findTF("RepairEffectBox")

def var_0_0.addListener(arg_9_0):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.attrTFList):
		onToggle(arg_9_0, iter_9_1, function(arg_10_0)
			if arg_10_0 == True:
				arg_9_0.curAttrName = iter_9_0

				arg_9_0.updateRepairBtn()
			else
				arg_9_0.curAttrName = None

				arg_9_0.updateRepairBtn(True), SFX_PANEL)

	onButton(arg_9_0, arg_9_0.repairBtn, function()
		pg.m02.sendNotification(GAME.REPAIR_META_CHARACTER, {
			shipID = arg_9_0.curMetaShipID,
			attr = arg_9_0.curAttrName
		}), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.showDetailBtn, function()
		if not isActive(arg_9_0.detailPanel):
			arg_9_0.openDetailPanel(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.showDetailLine, function()
		if not isActive(arg_9_0.detailPanel):
			arg_9_0.openDetailPanel(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.detailCloseBtn, function()
		arg_9_0.closeDetailPanel(), SFX_CANCEL)
	onButton(arg_9_0, arg_9_0.detailBG, function()
		arg_9_0.closeDetailPanel(), SFX_CANCEL)

def var_0_0.TryPlayGuide(arg_16_0):
	pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0027")

def var_0_0.doRepairProgressPanelAni(arg_17_0):
	local var_17_0 = arg_17_0.curMetaCharacterVO.getRepairRate()
	local var_17_1 = GetComponent(arg_17_0.repairSliderTF, typeof(Slider))

	var_17_1.minValue = 0
	var_17_1.maxValue = 1

	local var_17_2 = var_17_1.value

	if var_17_0 > 0:
		local var_17_3 = 0.5

		arg_17_0.managedTween(LeanTween.value, None, go(arg_17_0.repairSliderTF), var_17_2, var_17_0, var_17_3).setOnUpdate(System.Action_float(function(arg_18_0)
			arg_17_0.updateRepairProgressPanel(arg_18_0))).setOnComplete(System.Action(function()
			arg_17_0.updateRepairProgressPanel(var_17_0)))
	else
		arg_17_0.updateRepairProgressPanel(var_17_0)

def var_0_0.updateRepairProgressPanel(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_1 or arg_20_0.curMetaCharacterVO.getRepairRate()

	setSlider(arg_20_0.repairSliderTF, 0, 1, var_20_0)
	setText(arg_20_0.repairPercentText, string.format("%d", var_20_0 * 100))

def var_0_0.updateAttrListPanel(arg_21_0):
	for iter_21_0, iter_21_1 in ipairs(MetaCharacterConst.REPAIR_ATTRS):
		arg_21_0.updateAttrItem(arg_21_0.attrTFList[iter_21_1], iter_21_1)

def var_0_0.updateAttrItem(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_0.findTF("LockPanel", arg_22_1)
	local var_22_1 = arg_22_0.findTF("UnSelectPanel", arg_22_1)
	local var_22_2 = arg_22_0.findTF("SelectedPanel", arg_22_1)
	local var_22_3 = arg_22_0.findTF("TitleImg", var_22_2)

	GetComponent(var_22_3, "Image").SetNativeSize()

	local var_22_4 = arg_22_0.curMetaCharacterVO.getAttrVO(arg_22_2)

	if var_22_4.isLock():
		setActive(var_22_1, False)
		setActive(var_22_2, False)
		setActive(var_22_0, True)

		arg_22_1.GetComponent("Toggle").interactable = False
	else
		local var_22_5 = arg_22_1.GetComponent("Toggle")

		setActive(var_22_1, not var_22_5.isOn)
		setActive(var_22_2, var_22_5.isOn)
		setActive(var_22_0, False)

		var_22_5.interactable = True

		local var_22_6 = arg_22_0.findTF("ValueText", var_22_1)
		local var_22_7 = arg_22_0.findTF("ValueText", var_22_2)
		local var_22_8 = arg_22_0.findTF("AttrRepairValue/CurValueText", var_22_2)
		local var_22_9 = arg_22_0.findTF("AttrRepairValue/Image", var_22_2)
		local var_22_10 = arg_22_0.findTF("AttrRepairValue/NextValueText", var_22_2)
		local var_22_11 = arg_22_0.findTF("IconTpl", var_22_2)
		local var_22_12 = arg_22_0.findTF("ItemCount", var_22_2)
		local var_22_13 = arg_22_0.findTF("NumText", var_22_12)
		local var_22_14 = var_22_4.getAddition()

		setText(var_22_6, "+" .. var_22_14)
		setText(var_22_7, "+" .. var_22_14)
		setText(var_22_8, "+" .. var_22_14)

		local var_22_15 = var_22_4.getLevel()
		local var_22_16 = var_22_4.isMaxLevel()
		local var_22_17

		if not var_22_16:
			var_22_17 = var_22_4.getItem()
		else
			var_22_17 = var_22_4.getItemByLevel(var_22_15 - 1)

		local var_22_18 = var_22_17.getItemId()
		local var_22_19 = var_22_17.getTotalCnt()
		local var_22_20 = getProxy(BagProxy).getItemCountById(var_22_18)

		if var_22_20 < var_22_19:
			var_22_20 = setColorStr(var_22_20, COLOR_RED)

		setText(var_22_13, var_22_20 .. "/" .. var_22_19)

		local var_22_21 = {
			type = DROP_TYPE_ITEM,
			id = var_22_18,
			count = var_22_19
		}

		updateDrop(var_22_11, var_22_21, {
			hideName = True
		})
		onButton(arg_22_0, var_22_11, function()
			arg_22_0.emit(BaseUI.ON_DROP, var_22_21), SFX_PANEL)
		setActive(var_22_9, not var_22_16)
		setActive(var_22_10, not var_22_16)

		if var_22_16:
			setText(var_22_10, var_22_14)
		else
			local var_22_22 = var_22_17.getAdditionValue()

			setText(var_22_10, "+" .. var_22_14 + var_22_22)

		if var_22_16:
			setActive(var_22_11, False)
			setActive(var_22_12, False)
		else
			setActive(var_22_11, True)
			setActive(var_22_12, True)

def var_0_0.updateRepairBtn(arg_24_0, arg_24_1):
	if arg_24_1 == True:
		setActive(arg_24_0.repairBtn, False)
		setActive(arg_24_0.repairBtnDisable, False)

		return

	local var_24_0 = arg_24_0.curMetaCharacterVO.getAttrVO(arg_24_0.curAttrName)
	local var_24_1 = var_24_0.getLevel()
	local var_24_2 = var_24_0.isMaxLevel()
	local var_24_3

	if not var_24_2:
		var_24_3 = var_24_0.getItem()
	else
		var_24_3 = var_24_0.getItemByLevel(var_24_1 - 1)

	local var_24_4 = var_24_3.getItemId()
	local var_24_5 = var_24_3.getTotalCnt() <= getProxy(BagProxy).getItemCountById(var_24_4)

	if var_24_2:
		setActive(arg_24_0.repairBtn, False)
		setActive(arg_24_0.repairBtnDisable, False)
	elif not var_24_5:
		setActive(arg_24_0.repairBtn, False)
		setActive(arg_24_0.repairBtnDisable, True)
	else
		setActive(arg_24_0.repairBtn, True)
		setActive(arg_24_0.repairBtnDisable, False)

def var_0_0.updateDetailItem(arg_25_0, arg_25_1, arg_25_2):
	local var_25_0 = arg_25_0.findTF("LineContainer", arg_25_1)
	local var_25_1 = arg_25_0.findTF("LockPanel", arg_25_1)
	local var_25_2 = arg_25_0.findTF("TipText", var_25_1)
	local var_25_3 = arg_25_2.progress

	setText(var_25_2, i18n("meta_repair_effect_unlock", var_25_3))

	local var_25_4 = arg_25_0.curMetaCharacterVO.getRepairRate()

	setActive(var_25_1, not (var_25_3 <= var_25_4 * 100))

	local var_25_5 = arg_25_2.getAttrAdditionList()
	local var_25_6 = #var_25_5
	local var_25_7 = arg_25_2.getDescs()
	local var_25_8 = var_25_6 + #var_25_7 + 1
	local var_25_9 = UIItemList.New(var_25_0, arg_25_0.detailLineTpl)

	var_25_9.make(function(arg_26_0, arg_26_1, arg_26_2)
		local var_26_0 = arg_25_0.findTF("AttrLine", arg_26_2)
		local var_26_1 = arg_25_0.findTF("UnlockTipLine", arg_26_2)
		local var_26_2 = arg_25_0.findTF("Text", arg_26_2)

		if arg_26_0 == UIItemList.EventUpdate:
			arg_26_1 = arg_26_1 + 1

			if arg_26_1 == 1:
				setActive(var_26_0, False)
				setActive(var_26_1, False)
				setActive(var_26_2, True)
				setText(var_26_2, i18n("meta_repair_effect_unlock", var_25_3))

				return

			if arg_26_1 <= var_25_6 + 1:
				setActive(var_26_0, True)
				setActive(var_26_1, False)

				local var_26_3 = arg_25_0.findTF("AttrIcon", var_26_0)
				local var_26_4 = arg_25_0.findTF("AttrNameText", var_26_0)
				local var_26_5 = arg_25_0.findTF("NumText", var_26_0)
				local var_26_6 = var_25_5[arg_26_1 - 1]
				local var_26_7 = var_26_6[1]
				local var_26_8 = var_26_6[2]

				setImageSprite(var_26_3, LoadSprite("attricon", var_26_7))
				setText(var_26_4, AttributeType.Type2Name(var_26_7))
				setText(var_26_5, "+" .. var_26_8)
			else
				setActive(var_26_0, False)
				setActive(var_26_1, True)

				local var_26_9 = arg_25_0.findTF("Text", var_26_1)
				local var_26_10 = var_25_7[arg_26_1 - 1 - var_25_6]

				setScrollText(var_26_9, var_26_10))
	var_25_9.align(var_25_8)

def var_0_0.updateDetailPanel(arg_27_0):
	setActive(arg_27_0.detailPanel, False)

	local var_27_0 = arg_27_0.curMetaCharacterVO.getEffects()

	arg_27_0.detailList = UIItemList.New(arg_27_0.detailItemContainer, arg_27_0.detailItemTpl)

	arg_27_0.detailList.make(function(arg_28_0, arg_28_1, arg_28_2)
		if arg_28_0 == UIItemList.EventUpdate:
			local var_28_0 = var_27_0[arg_28_1 + 1]

			arg_27_0.updateDetailItem(arg_28_2, var_28_0))
	arg_27_0.detailList.align(#var_27_0)

def var_0_0.updateData(arg_29_0):
	arg_29_0.curShipVO = arg_29_0.bayProxy.getShipById(arg_29_0.curMetaShipID)
	arg_29_0.curMetaCharacterVO = arg_29_0.curShipVO.getMetaCharacter()

def var_0_0.checkSpecialEffect(arg_30_0):
	local var_30_0 = arg_30_0.bayProxy.getShipById(arg_30_0.curMetaShipID).getMetaCharacter()
	local var_30_1 = var_30_0.getRepairRate() * 100
	local var_30_2 = arg_30_0.curMetaCharacterVO.getRepairRate() * 100
	local var_30_3 = var_30_0.getEffects()

	for iter_30_0, iter_30_1 in ipairs(var_30_3):
		local var_30_4 = iter_30_1.progress

		if var_30_2 < var_30_4 and var_30_4 <= var_30_1:
			arg_30_0.openRepairEffectBoxPanel(iter_30_1)

			break

def var_0_0.openRepairEffectBoxPanel(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_1.getAttrAdditionList()
	local var_31_1 = #var_31_0
	local var_31_2 = arg_31_1.getDescs()
	local var_31_3 = #var_31_2
	local var_31_4 = 1 + var_31_1 + var_31_3
	local var_31_5 = arg_31_1.progress
	local var_31_6 = arg_31_0.findTF("BG", arg_31_0.repairEffectBoxPanel)
	local var_31_7 = arg_31_0.findTF("Box/BtnContainer/ConfirmBtn", arg_31_0.repairEffectBoxPanel)

	onButton(arg_31_0, var_31_7, function()
		arg_31_0.closeRepairEffectBoxPanel(), SFX_CANCEL)

	local var_31_8 = arg_31_0.findTF("Box/Panel/TypeRepairEffect", arg_31_0.repairEffectBoxPanel)
	local var_31_9 = arg_31_0.findTF("DetailLineTpl", var_31_8)
	local var_31_10 = UIItemList.New(var_31_8, var_31_9)

	var_31_10.make(function(arg_33_0, arg_33_1, arg_33_2)
		local var_33_0 = arg_31_0.findTF("AttrLine", arg_33_2)
		local var_33_1 = arg_31_0.findTF("UnlockTipLine", arg_33_2)

		if arg_33_0 == UIItemList.EventUpdate:
			arg_33_1 = arg_33_1 + 1

			if arg_33_1 == 1:
				setActive(var_33_0, False)
				setActive(var_33_1, True)

				local var_33_2 = arg_31_0.findTF("Text", var_33_1)

				setScrollText(var_33_2, i18n("meta_repair_effect_special", var_31_5))
			elif arg_33_1 > 1 and arg_33_1 <= 1 + var_31_1:
				setActive(var_33_0, True)
				setActive(var_33_1, False)

				local var_33_3 = arg_31_0.findTF("AttrIcon", var_33_0)
				local var_33_4 = arg_31_0.findTF("AttrNameText", var_33_0)
				local var_33_5 = arg_31_0.findTF("NumText", var_33_0)
				local var_33_6 = var_31_0[arg_33_1 - 1]
				local var_33_7 = var_33_6[1]
				local var_33_8 = var_33_6[2]

				setImageSprite(var_33_3, LoadSprite("attricon", var_33_7))
				setText(var_33_4, AttributeType.Type2Name(var_33_7))
				setText(var_33_5, "+" .. var_33_8)
			elif arg_33_1 > 1 + var_31_1 and arg_33_1 <= var_31_4:
				setActive(var_33_0, False)
				setActive(var_33_1, True)

				local var_33_9 = arg_31_0.findTF("Text", var_33_1)
				local var_33_10 = var_31_2[arg_33_1 - (1 + var_31_1)]

				setScrollText(var_33_9, var_33_10))
	var_31_10.align(var_31_4)
	setActive(arg_31_0.repairEffectBoxPanel, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_31_0.repairEffectBoxPanel, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

def var_0_0.closeRepairEffectBoxPanel(arg_34_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_34_0.repairEffectBoxPanel)
	setActive(arg_34_0.repairEffectBoxPanel, False)

def var_0_0.openDetailPanel(arg_35_0):
	setActive(arg_35_0.detailPanel, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_35_0.detailPanel, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

	arg_35_0.isOpening = True

	arg_35_0.managedTween(LeanTween.value, None, go(arg_35_0.detailTF), arg_35_0.detailTF.rect.width, 0, 0.3).setOnUpdate(System.Action_float(function(arg_36_0)
		setAnchoredPosition(arg_35_0.detailTF, {
			x = arg_36_0
		}))).setOnComplete(System.Action(function()
		arg_35_0.isOpening = None))

def var_0_0.closeDetailPanel(arg_38_0):
	if arg_38_0.isClosing or arg_38_0.isOpening:
		return

	arg_38_0.isClosing = True

	arg_38_0.managedTween(LeanTween.value, None, go(arg_38_0.detailTF), 0, arg_38_0.detailTF.rect.width, 0.3).setOnUpdate(System.Action_float(function(arg_39_0)
		setAnchoredPosition(arg_38_0.detailTF, {
			x = arg_39_0
		}))).setOnComplete(System.Action(function()
		arg_38_0.isClosing = None

		setActive(arg_38_0.detailPanel, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_38_0.detailPanel)))

return var_0_0
