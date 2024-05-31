local var_0_0 = class("EquipmentInfoLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EquipmentInfoUI"

var_0_0.PANEL_DESTROY = "Destroy"
var_0_0.PANEL_REVERT = "Revert"
var_0_0.Left = 1
var_0_0.Middle = 2
var_0_0.Right = 3
var_0_0.pos = {
	{
		-353,
		30,
		0
	},
	{
		0,
		30,
		0
	},
	{
		353,
		30,
		0
	}
}

def var_0_0.init(arg_2_0):
	local var_2_0 = {
		"default",
		"replace",
		"display",
		"destroy",
		"revert"
	}

	arg_2_0.toggles = {}

	for iter_2_0, iter_2_1 in ipairs(var_2_0):
		arg_2_0[iter_2_1 .. "Panel"] = arg_2_0.findTF(iter_2_1)
		arg_2_0.toggles[iter_2_1 .. "Panel"] = arg_2_0.findTF("toggle_controll/" .. iter_2_1)

	arg_2_0.sample = arg_2_0.findTF("sample")

	setActive(arg_2_0.sample, False)
	setActive(arg_2_0.defaultPanel.Find("transform_tip"), False)

	arg_2_0.txtQuickEnable = findTF(arg_2_0._tf, "txtQuickEnable")

	setText(arg_2_0.txtQuickEnable, i18n("ship_equip_check"))

	arg_2_0.equipDestroyConfirmWindow = EquipDestoryConfirmWindow.New(arg_2_0._tf, arg_2_0.event)

def var_0_0.setEquipment(arg_3_0, arg_3_1):
	arg_3_0.equipmentVO = arg_3_1

def var_0_0.setShip(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.shipVO = arg_4_1
	arg_4_0.oldShipVO = arg_4_2

def var_0_0.setPlayer(arg_5_0, arg_5_1):
	arg_5_0.player = arg_5_1

def var_0_0.checkOverGold(arg_6_0, arg_6_1):
	local var_6_0 = _.detect(arg_6_1, function(arg_7_0)
		return arg_7_0.type == DROP_TYPE_RESOURCE and arg_7_0.id == 1).count or 0

	if arg_6_0.player.GoldMax(var_6_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_destroy"))

		return False

	return True

def var_0_0.setDestroyCount(arg_8_0, arg_8_1):
	arg_8_1 = math.clamp(arg_8_1, 1, arg_8_0.equipmentVO.count)

	if arg_8_0.destroyCount != arg_8_1:
		arg_8_0.destroyCount = arg_8_1

		arg_8_0.updateDestroyCount()

def var_0_0.didEnter(arg_9_0):
	setActive(arg_9_0.txtQuickEnable, arg_9_0.contextData.quickFlag or False)

	local var_9_0 = defaultValue(arg_9_0.contextData.type, EquipmentInfoMediator.TYPE_DEFAULT)

	arg_9_0.isShowUnique = table.contains(EquipmentInfoMediator.SHOW_UNIQUE, var_9_0)

	onButton(arg_9_0, arg_9_0._tf.Find("bg"), function()
		if isActive(arg_9_0.destroyPanel):
			triggerToggle(arg_9_0.toggles.defaultPanel, True)

			return

		arg_9_0.closeView(), SOUND_BACK)
	arg_9_0.initAndSetBtn(var_9_0)

	if var_9_0 == EquipmentInfoMediator.TYPE_DEFAULT:
		arg_9_0.updateOperation1()
	elif var_9_0 == EquipmentInfoMediator.TYPE_SHIP:
		arg_9_0.updateOperation2()
	elif var_9_0 == EquipmentInfoMediator.TYPE_REPLACE:
		arg_9_0.updateOperation3()
	elif var_9_0 == EquipmentInfoMediator.TYPE_DISPLAY:
		arg_9_0.updateOperation4()

	pg.UIMgr.GetInstance().BlurPanel(arg_9_0._tf, True, {
		weight = arg_9_0.getWeightFromData()
	})

def var_0_0.initAndSetBtn(arg_11_0, arg_11_1):
	if arg_11_1 == EquipmentInfoMediator.TYPE_DEFAULT or arg_11_1 == EquipmentInfoMediator.TYPE_SHIP:
		arg_11_0.defaultEquipTF = arg_11_0.findTF("equipment", arg_11_0.defaultPanel) or arg_11_0.cloneSampleTo(arg_11_0.defaultPanel, var_0_0.Middle, "equipment")
		arg_11_0.defaultReplaceBtn = arg_11_0.findTF("actions/action_button_3", arg_11_0.defaultPanel)
		arg_11_0.defaultDestroyBtn = arg_11_0.findTF("actions/action_button_1", arg_11_0.defaultPanel)
		arg_11_0.defaultEnhanceBtn = arg_11_0.findTF("actions/action_button_2", arg_11_0.defaultPanel)
		arg_11_0.defaultUnloadBtn = arg_11_0.findTF("actions/action_button_4", arg_11_0.defaultPanel)
		arg_11_0.defaultRevertBtn = arg_11_0.findTF("info/equip/revert_btn", arg_11_0.defaultEquipTF)
		arg_11_0.defaultTransformTipBar = arg_11_0.findTF("transform_tip", arg_11_0.defaultEquipTF)

		if arg_11_1 == EquipmentInfoMediator.TYPE_DEFAULT and not arg_11_0.defaultTransformTipBar:
			local var_11_0 = arg_11_0.defaultPanel.Find("transform_tip")

			setParent(var_11_0, arg_11_0.defaultEquipTF)

			local var_11_1 = var_11_0.sizeDelta

			var_11_1.y = 0
			var_11_0.sizeDelta = var_11_1

			setAnchoredPosition(var_11_0, Vector2.zero)

			arg_11_0.defaultTransformTipBar = var_11_0

		onButton(arg_11_0, arg_11_0.defaultReplaceBtn, function()
			local var_12_0, var_12_1 = ShipStatus.ShipStatusCheck("onModify", arg_11_0.shipVO)

			if not var_12_0:
				pg.TipsMgr.GetInstance().ShowTips(var_12_1)

				return

			arg_11_0.emit(EquipmentInfoMediator.ON_CHANGE), SFX_PANEL)
		onButton(arg_11_0, arg_11_0.defaultEnhanceBtn, function()
			if arg_11_0.shipVO:
				local var_13_0, var_13_1 = ShipStatus.ShipStatusCheck("onModify", arg_11_0.shipVO)

				if not var_13_0:
					pg.TipsMgr.GetInstance().ShowTips(var_13_1)

					return

			arg_11_0.emit(EquipmentInfoMediator.ON_INTENSIFY), SFX_PANEL)
		onButton(arg_11_0, arg_11_0.defaultUnloadBtn, function()
			local var_14_0, var_14_1 = ShipStatus.ShipStatusCheck("onModify", arg_11_0.shipVO)

			if not var_14_0:
				pg.TipsMgr.GetInstance().ShowTips(var_14_1)

				return

			arg_11_0.emit(EquipmentInfoMediator.ON_UNEQUIP), SFX_UI_DOCKYARD_EQUIPOFF)
		onButton(arg_11_0, arg_11_0.defaultDestroyBtn, function()
			triggerToggle(arg_11_0.toggles.destroyPanel, True)

			if not arg_11_0.initDestroyPanel:
				arg_11_0.initAndSetBtn(var_0_0.PANEL_DESTROY)

			arg_11_0.updateEquipmentPanel(arg_11_0.destroyEquipTF, arg_11_0.equipmentVO)

			if arg_11_0.equipmentVO.count > 0:
				arg_11_0.setDestroyCount(1), SFX_PANEL)
		onButton(arg_11_0, arg_11_0.defaultRevertBtn, function()
			triggerToggle(arg_11_0.toggles.revertPanel, True)

			if not arg_11_0.initRevertPanel:
				arg_11_0.initAndSetBtn(var_0_0.PANEL_REVERT)

			arg_11_0.updateRevertPanel(), SFX_PANEL)
	elif arg_11_1 == EquipmentInfoMediator.TYPE_REPLACE:
		arg_11_0.replaceSrcEquipTF = arg_11_0.findTF("equipment", arg_11_0.replacePanel) or arg_11_0.cloneSampleTo(arg_11_0.replacePanel, var_0_0.Left, "equipment")
		arg_11_0.replaceDstEquipTF = arg_11_0.findTF("equipment_on_ship", arg_11_0.replacePanel) or arg_11_0.cloneSampleTo(arg_11_0.replacePanel, var_0_0.Right, "equipment_on_ship")
		arg_11_0.replaceCancelBtn = arg_11_0.findTF("actions/cancel_button", arg_11_0.replacePanel)
		arg_11_0.replaceConfirmBtn = arg_11_0.findTF("actions/action_button_2", arg_11_0.replacePanel)

		onButton(arg_11_0, arg_11_0.replaceCancelBtn, function()
			if isActive(arg_11_0.destroyPanel):
				triggerToggle(arg_11_0.toggles.defaultPanel, True)

				return

			arg_11_0.closeView(), SFX_CANCEL)
		onButton(arg_11_0, arg_11_0.replaceConfirmBtn, function()
			local var_18_0, var_18_1 = arg_11_0.shipVO.canEquipAtPos(arg_11_0.equipmentVO, arg_11_0.contextData.pos)

			if not var_18_0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_equipmentInfoLayer_error_canNotEquip", var_18_1))

				return

			if arg_11_0.contextData.quickCallback:
				arg_11_0.contextData.quickCallback()
				arg_11_0.closeView()
			else
				arg_11_0.emit(EquipmentInfoMediator.ON_EQUIP), SFX_UI_DOCKYARD_EQUIPADD)
	elif arg_11_1 == EquipmentInfoMediator.TYPE_DISPLAY:
		arg_11_0.displayEquipTF = arg_11_0.findTF("equipment", arg_11_0.displayPanel) or arg_11_0.cloneSampleTo(arg_11_0.displayPanel, var_0_0.Middle, "equipment")
		arg_11_0.displayMoveBtn = arg_11_0.findTF("actions/move_button", arg_11_0.displayPanel)
		arg_11_0.defaultTransformTipBar = arg_11_0.findTF("transform_tip", arg_11_0.displayEquipTF)

		if arg_11_0.contextData.showTransformTip and not arg_11_0.defaultTransformTipBar:
			local var_11_2 = arg_11_0.defaultPanel.Find("transform_tip")

			setParent(var_11_2, arg_11_0.displayEquipTF)

			local var_11_3 = var_11_2.sizeDelta

			var_11_3.y = 0
			var_11_2.sizeDelta = var_11_3

			setAnchoredPosition(var_11_2, Vector2.zero)

			arg_11_0.defaultTransformTipBar = var_11_2

		onButton(arg_11_0, arg_11_0.displayMoveBtn, function()
			arg_11_0.emit(EquipmentInfoMediator.ON_MOVE, arg_11_0.shipVO.id))
	elif arg_11_1 == var_0_0.PANEL_DESTROY:
		arg_11_0.initDestroyPanel = True
		arg_11_0.destroyEquipTF = arg_11_0.findTF("equipment", arg_11_0.destroyPanel) or arg_11_0.cloneSampleTo(arg_11_0.destroyPanel, var_0_0.Left, "equipment")
		arg_11_0.destroyCounter = arg_11_0.findTF("destroy", arg_11_0.destroyPanel)
		arg_11_0.destroyValue = arg_11_0.findTF("count/number_panel/value", arg_11_0.destroyCounter)
		arg_11_0.destroyLeftButton = arg_11_0.findTF("count/number_panel/left", arg_11_0.destroyCounter)
		arg_11_0.destroyRightButton = arg_11_0.findTF("count/number_panel/right", arg_11_0.destroyCounter)
		arg_11_0.destroyBonusList = arg_11_0.findTF("got/list", arg_11_0.destroyCounter)
		arg_11_0.destroyBonusItem = arg_11_0.findTF("got/item", arg_11_0.destroyCounter)
		arg_11_0.destroyCancelBtn = arg_11_0.findTF("actions/cancel_button", arg_11_0.destroyPanel)
		arg_11_0.destroyConfirmBtn = arg_11_0.findTF("actions/destroy_button", arg_11_0.destroyPanel)

		onButton(arg_11_0, arg_11_0.destroyLeftButton, function()
			arg_11_0.setDestroyCount(arg_11_0.destroyCount - 1), SFX_PANEL)
		onButton(arg_11_0, arg_11_0.destroyRightButton, function()
			arg_11_0.setDestroyCount(arg_11_0.destroyCount + 1), SFX_PANEL)
		onButton(arg_11_0, arg_11_0.findTF("count/max", arg_11_0.destroyCounter), function()
			arg_11_0.setDestroyCount(arg_11_0.equipmentVO.count), SFX_PANEL)
		onButton(arg_11_0, arg_11_0.destroyCancelBtn, function()
			triggerToggle(arg_11_0.toggles.defaultPanel, True), SFX_CANCEL)
		onButton(arg_11_0, arg_11_0.destroyConfirmBtn, function()
			if not arg_11_0.checkOverGold(arg_11_0.awards):
				return

			local var_24_0 = {}

			if arg_11_0.equipmentVO.isImportance():
				table.insert(var_24_0, function(arg_25_0)
					arg_11_0.equipDestroyConfirmWindow.Load()
					arg_11_0.equipDestroyConfirmWindow.ActionInvoke("Show", {
						setmetatable({
							count = arg_11_0.destroyCount
						}, {
							__index = arg_11_0.equipmentVO
						})
					}, arg_25_0))

			seriesAsync(var_24_0, function()
				arg_11_0.emit(EquipmentInfoMediator.ON_DESTROY, arg_11_0.destroyCount)), SFX_UI_EQUIPMENT_RESOLVE)
	elif arg_11_1 == var_0_0.PANEL_REVERT:
		arg_11_0.initRevertPanel = True
		arg_11_0.revertEquipTF = arg_11_0.findTF("equipment", arg_11_0.revertPanel) or arg_11_0.cloneSampleTo(arg_11_0.revertPanel, var_0_0.Left, "equipment")
		arg_11_0.revertAwardContainer = arg_11_0.findTF("item_panel/got/list", arg_11_0.revertPanel)
		arg_11_0.revertCancelBtn = arg_11_0.findTF("actions/cancel_button", arg_11_0.revertPanel)
		arg_11_0.revertConfirmBtn = arg_11_0.findTF("actions/revert_button", arg_11_0.revertPanel)
		arg_11_0.itemTpl = arg_11_0.getTpl("item_panel/got/item", arg_11_0.revertPanel)

		onButton(arg_11_0, arg_11_0.revertCancelBtn, function()
			triggerToggle(arg_11_0.toggles.defaultPanel, True), SFX_CANCEL)
		onButton(arg_11_0, arg_11_0.revertConfirmBtn, function()
			if not arg_11_0.checkOverGold(arg_11_0.awards):
				return

			local var_28_0 = arg_11_0.equipmentVO

			arg_11_0.emit(EquipmentInfoMediator.ON_REVERT, var_28_0.id), SFX_UI_EQUIPMENT_RESOLVE)

def var_0_0.updateOperation1(arg_29_0):
	triggerToggle(arg_29_0.toggles.defaultPanel, True)
	arg_29_0.updateEquipmentPanel(arg_29_0.defaultEquipTF, arg_29_0.equipmentVO)
	setActive(arg_29_0.defaultRevertBtn, not LOCK_EQUIP_REVERT and arg_29_0.fromEquipmentView and arg_29_0.equipmentVO.getConfig("level") > 1 and getProxy(BagProxy).getItemCountById(Item.REVERT_EQUIPMENT_ID) > 0)
	setActive(arg_29_0.defaultReplaceBtn, False)
	setActive(arg_29_0.defaultUnloadBtn, False)
	setActive(arg_29_0.defaultDestroyBtn, arg_29_0.contextData.destroy and arg_29_0.equipmentVO.count > 0)
	arg_29_0.UpdateTransformTipBar(arg_29_0.equipmentVO)

def var_0_0.updateOperation2(arg_30_0):
	triggerToggle(arg_30_0.toggles.defaultPanel, True)
	arg_30_0.updateEquipmentPanel(arg_30_0.defaultEquipTF, arg_30_0.shipVO.getEquip(arg_30_0.contextData.pos))
	setActive(arg_30_0.defaultDestroyBtn, False)
	setActive(arg_30_0.defaultReplaceBtn, True)
	setActive(arg_30_0.defaultUnloadBtn, True)
	setActive(arg_30_0.defaultRevertBtn, False)

	local var_30_0 = arg_30_0.findTF("head", arg_30_0.defaultEquipTF)

	setActive(var_30_0, arg_30_0.shipVO)

	if arg_30_0.shipVO:
		setImageSprite(findTF(var_30_0, "Image"), LoadSprite("qicon/" .. arg_30_0.shipVO.getPainting()))

	if arg_30_0.defaultTransformTipBar:
		setActive(arg_30_0.defaultTransformTipBar, False)

def var_0_0.updateOperation3(arg_31_0):
	triggerToggle(arg_31_0.toggles.replacePanel, True)

	local var_31_0 = arg_31_0.shipVO.getEquip(arg_31_0.contextData.pos)

	if var_31_0:
		local var_31_1 = var_31_0.GetPropertiesInfo()
		local var_31_2 = arg_31_0.equipmentVO.GetPropertiesInfo()

		if EquipType.getCompareGroup(var_31_0.configId) == EquipType.getCompareGroup(arg_31_0.equipmentVO.configId):
			Equipment.InsertAttrsCompare(var_31_1.attrs, var_31_2.attrs, arg_31_0.shipVO)

		arg_31_0.updateEquipmentPanel(arg_31_0.replaceSrcEquipTF, var_31_0, var_31_1)
		arg_31_0.updateEquipmentPanel(arg_31_0.replaceDstEquipTF, arg_31_0.equipmentVO, var_31_2)
	else
		arg_31_0.updateEquipmentPanel(arg_31_0.replaceSrcEquipTF, var_31_0)
		arg_31_0.updateEquipmentPanel(arg_31_0.replaceDstEquipTF, arg_31_0.equipmentVO)

	local var_31_3 = arg_31_0.findTF("head", arg_31_0.replaceDstEquipTF)

	setActive(var_31_3, arg_31_0.oldShipVO)

	if arg_31_0.oldShipVO:
		setImageSprite(findTF(var_31_3, "Image"), LoadSprite("qicon/" .. arg_31_0.oldShipVO.getPainting()))

def var_0_0.updateOperation4(arg_32_0):
	triggerToggle(arg_32_0.toggles.displayPanel, True)
	arg_32_0.updateEquipmentPanel(arg_32_0.displayEquipTF, arg_32_0.equipmentVO)
	setActive(arg_32_0.displayMoveBtn, arg_32_0.shipVO)

	local var_32_0 = arg_32_0.findTF("head", arg_32_0.displayEquipTF)

	setActive(var_32_0, arg_32_0.shipVO)

	if arg_32_0.shipVO:
		setImageSprite(findTF(var_32_0, "Image"), LoadSprite("qicon/" .. arg_32_0.shipVO.getPainting()))

	arg_32_0.UpdateTransformTipBar(arg_32_0.equipmentVO)

def var_0_0.updateRevertPanel(arg_33_0):
	local var_33_0 = arg_33_0.equipmentVO.GetRootEquipment()
	local var_33_1 = arg_33_0.equipmentVO.GetPropertiesInfo()
	local var_33_2 = var_33_0.GetPropertiesInfo()

	Equipment.InsertAttrsCompare(var_33_1.attrs, var_33_2.attrs, arg_33_0.shipVO)
	arg_33_0.updateEquipmentPanel(arg_33_0.revertEquipTF, var_33_0, var_33_2, arg_33_0.equipmentVO.getConfig("level"))
	arg_33_0.updateOperationAward(arg_33_0.revertAwardContainer, arg_33_0.itemTpl, arg_33_0.equipmentVO.getRevertAwards())

def var_0_0.updateDestroyCount(arg_34_0):
	local var_34_0 = arg_34_0.destroyCount

	setText(arg_34_0.destroyValue, var_34_0)

	local var_34_1 = {}
	local var_34_2 = 0
	local var_34_3 = arg_34_0.equipmentVO.getConfig("destory_item") or {}
	local var_34_4 = var_34_2 + (arg_34_0.equipmentVO.getConfig("destory_gold") or 0) * var_34_0

	for iter_34_0, iter_34_1 in ipairs(var_34_3):
		table.insert(var_34_1, {
			type = DROP_TYPE_ITEM,
			id = iter_34_1[1],
			count = iter_34_1[2] * var_34_0
		})

	table.insert(var_34_1, {
		id = 1,
		type = DROP_TYPE_RESOURCE,
		count = var_34_4
	})
	arg_34_0.updateOperationAward(arg_34_0.destroyBonusList, arg_34_0.destroyBonusItem, var_34_1)

def var_0_0.updateOperationAward(arg_35_0, arg_35_1, arg_35_2, arg_35_3):
	arg_35_0.awards = arg_35_3

	if arg_35_1.childCount == 0:
		for iter_35_0 = 1, #arg_35_3:
			cloneTplTo(arg_35_2, arg_35_1)

	for iter_35_1 = 1, #arg_35_3:
		local var_35_0 = arg_35_1.GetChild(iter_35_1 - 1)
		local var_35_1 = arg_35_3[iter_35_1]

		updateDrop(var_35_0, var_35_1)
		onButton(arg_35_0, var_35_0, function()
			arg_35_0.emit(var_0_0.ON_DROP, var_35_1), SFX_PANEL)
		setText(findTF(var_35_0, "name_panel/name"), getText(findTF(var_35_0, "name")))
		setText(findTF(var_35_0, "name_panel/number"), " x " .. getText(findTF(var_35_0, "icon_bg/count")))
		setActive(findTF(var_35_0, "icon_bg/count"), False)

def var_0_0.updateEquipmentPanel(arg_37_0, arg_37_1, arg_37_2, arg_37_3, arg_37_4):
	local var_37_0 = arg_37_0.findTF("info", arg_37_1)
	local var_37_1 = arg_37_0.findTF("empty", arg_37_1)

	setActive(var_37_0, arg_37_2)
	setActive(var_37_1, not arg_37_2)

	if arg_37_2:
		local var_37_2 = findTF(var_37_0, "name")

		setScrollText(findTF(var_37_2, "mask/Text"), arg_37_2.getConfig("name"))
		setActive(findTF(var_37_2, "unique"), arg_37_2.isUnique() and arg_37_0.isShowUnique)

		local var_37_3 = findTF(var_37_0, "equip")

		setImageSprite(findTF(var_37_3, "bg"), GetSpriteFromAtlas("ui/equipmentinfoui_atlas", "equip_bg_" .. EquipmentRarity.Rarity2Print(arg_37_2.getConfig("rarity"))))
		updateEquipment(var_37_3, arg_37_2, {
			noIconColorful = True
		})
		setActive(findTF(var_37_3, "revert_btn"), False)
		setActive(findTF(var_37_3, "slv"), arg_37_4 or arg_37_2.getConfig("level") > 1)
		setText(findTF(var_37_3, "slv/Text"), arg_37_4 and arg_37_4 - 1 or arg_37_2.getConfig("level") - 1)
		setActive(findTF(var_37_3, "slv/next"), arg_37_4)
		setText(findTF(var_37_3, "slv/next/Text"), arg_37_2.getConfig("level") - 1)

		local var_37_4 = arg_37_0.findTF("tier", var_37_3)

		setActive(var_37_4, arg_37_2)

		local var_37_5 = arg_37_2.getConfig("tech") or 1

		eachChild(var_37_4, function(arg_38_0)
			setActive(arg_38_0, tostring(var_37_5) == arg_38_0.gameObject.name))
		setImageSprite(findTF(var_37_3, "title"), GetSpriteFromAtlas("equiptype", EquipType.type2Tag(arg_37_2.getConfig("type"))))
		setText(var_37_3.Find("speciality/Text"), arg_37_2.getConfig("speciality") != "无" and arg_37_2.getConfig("speciality") or i18n1("—"))
		updateEquipInfo(var_37_0.Find("attributes/view/content"), arg_37_3 or arg_37_2.GetPropertiesInfo(), arg_37_2.GetSkill(), arg_37_0.shipVO)

def var_0_0.UpdateTransformTipBar(arg_39_0, arg_39_1):
	if not arg_39_0.defaultTransformTipBar:
		return

	local var_39_0 = pg.SystemOpenMgr.GetInstance().isOpenSystem(getProxy(PlayerProxy).getData().level, "EquipmentTransformTreeMediator")
	local var_39_1 = EquipmentProxy.GetTransformTargets(Equipment.GetEquipRootStatic(arg_39_1.id))

	setActive(arg_39_0.defaultTransformTipBar, not LOCK_EQUIPMENT_TRANSFORM and var_39_0 and #var_39_1 > 0)

	if isActive(arg_39_0.defaultTransformTipBar):
		local var_39_2 = pg.equip_upgrade_data

		UIItemList.StaticAlign(arg_39_0.defaultTransformTipBar.Find("list"), arg_39_0.defaultTransformTipBar.Find("list/transformTarget"), #var_39_1, function(arg_40_0, arg_40_1, arg_40_2)
			if arg_40_0 == UIItemList.EventUpdate:
				setActive(arg_40_2.Find("link"), arg_40_1 > 0)

				local var_40_0 = var_39_2[var_39_1[arg_40_1 + 1]]
				local var_40_1 = var_40_0 and var_40_0.target_id

				if not var_40_1:
					setActive(arg_40_2, False)

					return

				updateDrop(arg_40_2.Find("item"), {
					type = DROP_TYPE_EQUIP,
					id = var_40_1
				})
				onButton(arg_39_0, arg_40_2.Find("item"), function()
					local var_41_0 = CreateShell(arg_39_1)

					if arg_39_0.shipVO:
						var_41_0.shipId = arg_39_0.shipVO.id
						var_41_0.shipPos = arg_39_0.contextData.pos

					arg_39_0.emit(EquipmentInfoMediator.OPEN_LAYER, Context.New({
						mediator = EquipmentTransformMediator,
						viewComponent = EquipmentTransformLayer,
						data = {
							fromStoreHouse = True,
							formulaId = var_39_1[arg_40_1 + 1],
							sourceEquipmentInstance = {
								type = DROP_TYPE_EQUIP,
								id = arg_39_1.id,
								template = var_41_0
							}
						}
					})), SFX_PANEL)
				arg_40_2.Find("mask/name").GetComponent("ScrollText").SetText(Equipment.getConfigData(var_40_1).name))

def var_0_0.cloneSampleTo(arg_42_0, arg_42_1, arg_42_2, arg_42_3, arg_42_4):
	local var_42_0 = cloneTplTo(arg_42_0.sample, arg_42_1, arg_42_3)

	var_42_0.localPosition = Vector3.New(var_0_0.pos[arg_42_2][1], var_0_0.pos[arg_42_2][2], var_0_0.pos[arg_42_2][3])

	if arg_42_4:
		var_42_0.SetSiblingIndex(arg_42_4)

	return var_42_0

def var_0_0.willExit(arg_43_0):
	arg_43_0.equipDestroyConfirmWindow.Destroy()
	pg.UIMgr.GetInstance().UnblurPanel(arg_43_0._tf)

def var_0_0.onBackPressed(arg_44_0):
	if arg_44_0.equipDestroyConfirmWindow.isShowing():
		arg_44_0.equipDestroyConfirmWindow.Hide()

		return

	if isActive(arg_44_0.destroyPanel):
		triggerToggle(arg_44_0.toggles.defaultPanel, True)

		return

	arg_44_0.closeView()

return var_0_0
