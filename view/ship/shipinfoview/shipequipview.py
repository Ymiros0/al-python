local var_0_0 = class("ShipEquipView", import("...base.BaseSubView"))

var_0_0.UNLOCK_EQUIPMENT_SKIN_POS = {
	1,
	2,
	3,
	4,
	5
}

def var_0_0.getUIName(arg_1_0):
	return "ShipEquipView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitEquipment()

def var_0_0.SetShareData(arg_3_0, arg_3_1):
	arg_3_0.shareData = arg_3_1

def var_0_0.GetShipVO(arg_4_0):
	if arg_4_0.shareData and arg_4_0.shareData.shipVO:
		return arg_4_0.shareData.shipVO

	return None

def var_0_0.UpdateUI(arg_5_0):
	local var_5_0 = arg_5_0.GetShipVO()

	arg_5_0.UpdateEquipments(var_5_0)

def var_0_0.InitEquipment(arg_6_0):
	arg_6_0.mainPanel = arg_6_0._parentTf.parent
	arg_6_0.equipRCon = arg_6_0._parentTf.Find("equipment_r_container")
	arg_6_0.equipLCon = arg_6_0._parentTf.Find("equipment_l_container")
	arg_6_0.equipBCon = arg_6_0._parentTf.Find("equipment_b_container")
	arg_6_0.equipmentR = arg_6_0.findTF("equipment_r")
	arg_6_0.equipmentL = arg_6_0.findTF("equipment_l")
	arg_6_0.equipmentB = arg_6_0.findTF("equipment_b")
	arg_6_0.equipmentR1 = arg_6_0.equipmentR.Find("equipment/equipment_r1")
	arg_6_0.equipmentR2 = arg_6_0.equipmentR.Find("equipment/equipment_r2")
	arg_6_0.equipmentR3 = arg_6_0.equipmentR.Find("equipment/equipment_r3")
	arg_6_0.equipmentL1 = arg_6_0.equipmentL.Find("equipment/equipment_l1")
	arg_6_0.equipmentL2 = arg_6_0.equipmentL.Find("equipment/equipment_l2")
	arg_6_0.equipSkinBtn = arg_6_0.equipmentR.Find("equipment_skin_btn")
	arg_6_0.equipmentB1 = arg_6_0.equipmentB.Find("equipment")
	arg_6_0.resource = arg_6_0._tf.Find("resource")
	arg_6_0.equipSkinLogicPanel = ShipEquipSkinLogicPanel.New(arg_6_0._tf.gameObject)

	arg_6_0.equipSkinLogicPanel.attach(arg_6_0)
	arg_6_0.equipSkinLogicPanel.setLabelResource(arg_6_0.resource)
	setActive(arg_6_0.equipSkinLogicPanel._go, True)
	setParent(arg_6_0.equipmentR, arg_6_0.equipRCon)
	setParent(arg_6_0.equipmentL, arg_6_0.equipLCon)
	setParent(arg_6_0.equipmentB, arg_6_0.equipBCon)
	setActive(arg_6_0.equipmentR, True)
	setActive(arg_6_0.equipmentL, True)
	setActive(arg_6_0.equipmentB, True)
	setActive(arg_6_0.equipSkinBtn, True)

	arg_6_0.equipmentPanels = {
		arg_6_0.equipmentR1,
		arg_6_0.equipmentR2,
		arg_6_0.equipmentR3,
		arg_6_0.equipmentL1,
		arg_6_0.equipmentL2
	}
	arg_6_0.onSelected = False

def var_0_0.InitEvent(arg_7_0):
	onButton(arg_7_0, arg_7_0.equipSkinBtn, function()
		local var_8_0, var_8_1 = ShipStatus.ShipStatusCheck("onModify", arg_7_0.GetShipVO())

		if not var_8_0:
			pg.TipsMgr.GetInstance().ShowTips(var_8_1)

			return

		arg_7_0.switch2EquipmentSkinPage())

	if arg_7_0.contextData.isInEquipmentSkinPage:
		arg_7_0.contextData.isInEquipmentSkinPage = None

		triggerButton(arg_7_0.equipSkinBtn)

def var_0_0.OnSelected(arg_9_0, arg_9_1):
	local var_9_0 = pg.UIMgr.GetInstance()

	if arg_9_1:
		local var_9_1 = {}
		local var_9_2 = {}
		local var_9_3 = {}

		local function var_9_4(arg_10_0, arg_10_1)
			eachChild(arg_10_0, function(arg_11_0)
				table.insert(arg_10_1, arg_11_0))

		var_9_4(arg_9_0.equipmentR.Find("skin"), var_9_2)
		var_9_4(arg_9_0.equipmentR.Find("equipment"), var_9_2)
		var_9_4(arg_9_0.equipmentL.Find("skin"), var_9_1)
		var_9_4(arg_9_0.equipmentL.Find("equipment"), var_9_1)
		var_9_4(arg_9_0.equipmentB, var_9_3)
		table.insert(var_9_1, arg_9_0.equipmentL.Find("equipment/equipment_l1"))
		var_9_0.OverlayPanelPB(arg_9_0.equipRCon, {
			pbList = var_9_2,
			groupName = LayerWeightConst.GROUP_SHIPINFOUI,
			overlayType = LayerWeightConst.OVERLAY_UI_ADAPT,
			weight = LayerWeightConst.LOWER_LAYER
		})
		var_9_0.OverlayPanelPB(arg_9_0.equipLCon, {
			pbList = var_9_1,
			groupName = LayerWeightConst.GROUP_SHIPINFOUI,
			overlayType = LayerWeightConst.OVERLAY_UI_ADAPT,
			weight = LayerWeightConst.LOWER_LAYER
		})
		var_9_0.OverlayPanelPB(arg_9_0.equipBCon, {
			pbList = var_9_3,
			groupName = LayerWeightConst.GROUP_SHIPINFOUI,
			overlayType = LayerWeightConst.OVERLAY_UI_ADAPT,
			weight = LayerWeightConst.LOWER_LAYER
		})
	else
		var_9_0.UnOverlayPanel(arg_9_0.equipRCon, arg_9_0._parentTf)
		var_9_0.UnOverlayPanel(arg_9_0.equipLCon, arg_9_0._parentTf)
		var_9_0.UnOverlayPanel(arg_9_0.equipBCon, arg_9_0._parentTf)

	arg_9_0.onSelected = arg_9_1

def var_0_0.UpdateEquipments(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_1.getActiveEquipments()

	for iter_12_0, iter_12_1 in ipairs(arg_12_1.equipments):
		local var_12_1 = var_12_0[iter_12_0]

		arg_12_0.UpdateEquipmentPanel(iter_12_0, iter_12_1, var_12_1)

	if arg_12_0.equipSkinLogicPanel:
		arg_12_0.equipSkinLogicPanel.updateAll(arg_12_1)

	if arg_12_0.contextData.openEquipUpgrade == True:
		arg_12_0.contextData.openEquipUpgrade = False

		local var_12_2 = 0
		local var_12_3 = arg_12_0.GetShipVO().equipments

		for iter_12_2, iter_12_3 in ipairs(var_12_3):
			if iter_12_3:
				var_12_2 = var_12_2 + 1

		if var_12_2 > 0:
			arg_12_0.emit(ShipMainMediator.OPEN_EQUIP_UPGRADE, arg_12_0.GetShipVO().id)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("fightfail_noequip"))

	setActive(arg_12_0.equipmentB, arg_12_1.IsSpweaponUnlock() and not LOCK_SP_WEAPON)

	local var_12_4 = arg_12_1.GetSpWeapon()

	arg_12_0.UpdateSpWeaponPanel(var_12_4)

def var_0_0.UpdateEquipmentPanel(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0 = arg_13_0.equipmentPanels[arg_13_1]
	local var_13_1 = findTF(var_13_0, "info")
	local var_13_2 = findTF(var_13_0, "empty")
	local var_13_3 = findTF(var_13_1, "efficiency")

	setActive(var_13_1, arg_13_2)
	setActive(var_13_2, not arg_13_2)

	local var_13_4 = arg_13_0.GetShipVO()
	local var_13_5 = {}

	for iter_13_0, iter_13_1 in pairs(var_13_4.skills):
		local var_13_6 = ys.Battle.BattleDataFunction.GetBuffTemplate(iter_13_1.id, iter_13_1.level)

		if var_13_6.shipInfoScene and var_13_6.shipInfoScene.equip:
			for iter_13_2, iter_13_3 in ipairs(var_13_6.shipInfoScene.equip):
				table.insert(var_13_5, iter_13_3)

	local var_13_7 = var_13_4.GetSpWeapon()

	if var_13_7 and var_13_7.GetEffect() != 0:
		local var_13_8 = var_13_7.GetEffect()
		local var_13_9 = ys.Battle.BattleDataFunction.GetBuffTemplate(var_13_8, 1)

		if var_13_9.shipInfoScene and var_13_9.shipInfoScene.equip:
			for iter_13_4, iter_13_5 in ipairs(var_13_9.shipInfoScene.equip):
				table.insert(var_13_5, iter_13_5)

	local var_13_10 = findTF(var_13_0, "panel_title/type")
	local var_13_11 = findTF(var_13_0, "skin_icon")

	if var_13_11:
		setActive(var_13_11, arg_13_2 and arg_13_2.hasSkin())

	local var_13_12 = EquipType.Types2Title(arg_13_1, var_13_4.configId)
	local var_13_13 = EquipType.LabelToName(var_13_12)

	var_13_10.GetComponent(typeof(Text)).text = var_13_13

	if arg_13_2:
		setActive(var_13_3, not arg_13_2.isDevice())

		if not arg_13_2.isDevice():
			local var_13_14 = pg.ship_data_statistics[var_13_4.configId]
			local var_13_15 = var_13_4.getEquipProficiencyByPos(arg_13_1)
			local var_13_16 = var_13_15 and var_13_15 * 100 or 0
			local var_13_17 = False

			if not (var_13_4.getFlag("inWorld") and arg_13_0.contextData.fromMediatorName == WorldMediator.__cname and WorldConst.FetchWorldShip(var_13_4.id).IsBroken()):
				for iter_13_6, iter_13_7 in ipairs(var_13_5):
					if arg_13_0.equipmentCheck(iter_13_7) and arg_13_0.equipmentEnhance(iter_13_7, arg_13_2):
						var_13_16 = var_13_16 + iter_13_7.number
						var_13_17 = True

			if var_13_16 - calcFloor(var_13_16) > 1e-09:
				var_13_16 = string.format("%.1f", var_13_16)
				GetComponent(findTF(var_13_3, "Text"), typeof(Text)).fontSize = 45
			else
				GetComponent(findTF(var_13_3, "Text"), typeof(Text)).fontSize = 50

			setButtonText(var_13_3, var_13_17 and setColorStr(var_13_16 .. "%", COLOR_GREEN) or var_13_16 .. "%")

		local var_13_18 = arg_13_0.findTF("IconTpl", var_13_1)

		updateEquipment(var_13_18, arg_13_2)

		local var_13_19 = arg_13_2.getConfig("name")

		if arg_13_2.getConfig("ammo_icon")[1]:
			setActive(findTF(var_13_1, "cont/icon_ammo"), True)
			setImageSprite(findTF(var_13_1, "cont/icon_ammo"), GetSpriteFromAtlas("ammo", arg_13_2.getConfig("ammo_icon")[1]))
		else
			setActive(findTF(var_13_1, "cont/icon_ammo"), False)

		setScrollText(arg_13_0.equipmentPanels[arg_13_1].Find("info/cont/name_mask/name"), var_13_19)

		local var_13_20 = var_13_1.Find("attrs")

		eachChild(var_13_20, function(arg_14_0)
			setActive(arg_14_0, False))

		local var_13_21 = arg_13_2.GetPropertiesInfo().attrs
		local var_13_22 = underscore.filter(var_13_21, function(arg_15_0)
			return not arg_15_0.type or arg_15_0.type != AttributeType.AntiSiren)
		local var_13_23 = arg_13_2.getConfig("skill_id")[1]
		local var_13_24 = var_13_23 and arg_13_2.isDevice() and {
			1,
			2,
			5
		} or {
			1,
			4,
			2,
			3
		}

		for iter_13_8, iter_13_9 in ipairs(var_13_24):
			local var_13_25 = var_13_20.Find("attr_" .. iter_13_9)
			local var_13_26 = findTF(var_13_25, "panel")
			local var_13_27 = findTF(var_13_25, "lock")

			setActive(var_13_25, True)

			if iter_13_9 == 5:
				setText(var_13_26.Find("values/value"), "")

				local var_13_28 = getSkillName(var_13_23)

				if PLATFORM_CODE == PLATFORM_US and string.len(var_13_28) > 15:
					GetComponent(var_13_26.Find("values/value_1"), typeof(Text)).fontSize = 24

				setText(var_13_26.Find("values/value_1"), getSkillName(var_13_23))
				setActive(var_13_27, False)
			elif #var_13_22 > 0:
				local var_13_29 = table.remove(var_13_22, 1)

				if arg_13_2.isAircraft() and var_13_29.type == AttributeType.CD:
					var_13_29 = var_13_4.getAircraftReloadCD()

				local var_13_30, var_13_31 = Equipment.GetInfoTrans(var_13_29, var_13_4)

				setText(var_13_26.Find("tag"), var_13_30)

				local var_13_32 = string.split(tostring(var_13_31), "/")

				if #var_13_32 >= 2:
					setText(var_13_26.Find("values/value"), var_13_32[1] .. "/")
					setText(var_13_26.Find("values/value_1"), var_13_32[2])
				else
					setText(var_13_26.Find("values/value"), var_13_31)
					setText(var_13_26.Find("values/value_1"), "")

				setActive(var_13_27, False)
			else
				setText(var_13_26.Find("tag"), "")
				setText(var_13_26.Find("values/value"), "")
				setText(var_13_26.Find("values/value_1"), "")
				setActive(var_13_27, True)

		onButton(arg_13_0, var_13_0, function()
			arg_13_0.emit(BaseUI.ON_EQUIPMENT, {
				type = EquipmentInfoMediator.TYPE_SHIP,
				shipId = var_13_4.id,
				pos = arg_13_1,
				LayerWeightMgr_weight = LayerWeightConst.SECOND_LAYER
			}), SFX_UI_DOCKYARD_EQUIPADD)
	else
		onButton(arg_13_0, var_13_0, function()
			if var_13_4:
				local var_17_0, var_17_1 = ShipStatus.ShipStatusCheck("onModify", var_13_4)

				if not var_17_0:
					pg.TipsMgr.GetInstance().ShowTips(var_17_1)

					return

				arg_13_0.emit(ShipMainMediator.ON_SELECT_EQUIPMENT, arg_13_1), SFX_UI_DOCKYARD_EQUIPADD)

def var_0_0.equipmentCheck(arg_18_0, arg_18_1):
	if not arg_18_0.GetShipVO():
		return False

	local var_18_0 = arg_18_1.check_type
	local var_18_1 = arg_18_1.check_indexList
	local var_18_2 = arg_18_1.check_label

	if not var_18_0 and not var_18_1 and not var_18_2:
		return True

	local var_18_3 = False
	local var_18_4 = {}
	local var_18_5 = Clone(arg_18_0.GetShipVO().equipments)

	if var_18_1:
		local var_18_6 = #var_18_5

		while var_18_6 > 0:
			if not table.contains(var_18_1, var_18_6):
				table.remove(var_18_5, var_18_6)

			var_18_6 = var_18_6 - 1

	if var_18_0:
		local var_18_7 = #var_18_5

		while var_18_7 > 0:
			local var_18_8 = var_18_5[var_18_7]

			if not var_18_8 or not table.contains(var_18_0, var_18_8.getConfig("type")):
				table.remove(var_18_5, var_18_7)

			var_18_7 = var_18_7 - 1

	if var_18_2:
		local var_18_9 = #var_18_5

		while var_18_9 > 0:
			local var_18_10 = var_18_5[var_18_9]

			if var_18_10:
				local var_18_11 = 1

				for iter_18_0, iter_18_1 in ipairs(var_18_2):
					if not table.contains(var_18_10.getConfig("label"), iter_18_1):
						var_18_11 = var_18_11 * 0

				if var_18_11 == 0:
					table.remove(var_18_5, var_18_9)
			else
				table.remove(var_18_5, var_18_9)

			var_18_9 = var_18_9 - 1

	return #var_18_5 > 0

def var_0_0.equipmentEnhance(arg_19_0, arg_19_1):
	local var_19_0 = 1
	local var_19_1 = arg_19_1.getConfig("label")

	if arg_19_0.label:
		var_19_0 = 1

		for iter_19_0, iter_19_1 in ipairs(arg_19_0.label):
			if not table.contains(var_19_1, iter_19_1):
				var_19_0 = 0

				break

	return var_19_0 == 1

def var_0_0.UpdateSpWeaponPanel(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_0.equipmentB1
	local var_20_1 = findTF(var_20_0, "info")
	local var_20_2 = findTF(var_20_0, "empty")

	setActive(var_20_1, arg_20_1)
	setActive(var_20_2, not arg_20_1)

	local var_20_3 = arg_20_0.GetShipVO()

	assert(var_20_3)

	if arg_20_1:
		UpdateSpWeaponSlot(var_20_1, arg_20_1, {
			20,
			20,
			20,
			20
		})

		local var_20_4 = var_20_1.Find("attrs")

		eachChild(var_20_4, function(arg_21_0)
			setActive(arg_21_0, False))

		local var_20_5 = arg_20_1.GetPropertiesInfo().attrs
		local var_20_6 = underscore.filter(var_20_5, function(arg_22_0)
			return not arg_22_0.type or arg_22_0.type != AttributeType.AntiSiren)

		for iter_20_0 = 1, 2:
			local var_20_7 = var_20_4.GetChild(iter_20_0 - 1)

			setActive(var_20_7, True)

			if #var_20_6 > 0:
				local var_20_8 = table.remove(var_20_6, 1)
				local var_20_9, var_20_10 = Equipment.GetInfoTrans(var_20_8, var_20_3)

				setText(var_20_7.Find("tag"), var_20_9)
				setText(var_20_7.Find("values/value"), var_20_10)
				setText(var_20_7.Find("values/value_1"), "")

		Canvas.ForceUpdateCanvases()

		local var_20_11 = var_20_1.Find("cont")

		;(function()
			local var_23_0 = var_20_11.GetChild(0)

			setText(var_23_0.Find("tag"), i18n("spweapon_ui_effect_tag"))

			local var_23_1 = arg_20_1.GetEffect()

			setActive(var_23_0, var_23_1 and var_23_1 > 0)

			if not var_23_1 or not (var_23_1 > 0):
				return

			setScrollText(var_23_0.Find("value/Text"), getSkillName(var_23_1)))()
		;(function()
			local var_24_0 = var_20_11.GetChild(1)

			setText(var_24_0.Find("tag"), i18n("spweapon_ui_skill_tag"))

			local var_24_1 = arg_20_1.GetActiveUpgradableSkill(var_20_3)

			setActive(var_24_0, var_24_1 and var_24_1 > 0)

			if not var_24_1 or not (var_24_1 > 0):
				return

			setScrollText(var_24_0.Find("value/Text"), getSkillName(var_24_1)))()
		onButton(arg_20_0, var_20_0, function()
			arg_20_0.emit(BaseUI.ON_SPWEAPON, {
				type = SpWeaponInfoLayer.TYPE_SHIP,
				shipId = var_20_3.id
			}), SFX_UI_DOCKYARD_EQUIPADD)
	else
		onButton(arg_20_0, var_20_0, function()
			if var_20_3:
				local var_26_0, var_26_1 = ShipStatus.ShipStatusCheck("onModify", var_20_3)

				if not var_26_0:
					pg.TipsMgr.GetInstance().ShowTips(var_26_1)

					return

				arg_20_0.emit(ShipMainMediator.ON_SELECT_SPWEAPON), SFX_UI_DOCKYARD_EQUIPADD)

def var_0_0.switch2EquipmentSkinPage(arg_27_0):
	if arg_27_0.equipSkinLogicPanel.isTweening():
		return

	arg_27_0.equipSkinLogicPanel.doSwitchAnim(arg_27_0.contextData.isInEquipmentSkinPage)

	arg_27_0.contextData.isInEquipmentSkinPage = not arg_27_0.contextData.isInEquipmentSkinPage

	setActive(arg_27_0.equipSkinBtn.Find("unsel"), not arg_27_0.contextData.isInEquipmentSkinPage)
	setActive(arg_27_0.equipSkinBtn.Find("sel"), arg_27_0.contextData.isInEquipmentSkinPage)
	arg_27_0.equipSkinLogicPanel.updateAll(arg_27_0.GetShipVO())

def var_0_0.OnDestroy(arg_28_0):
	setParent(arg_28_0.equipmentR, arg_28_0._tf)
	setParent(arg_28_0.equipmentL, arg_28_0._tf)
	setParent(arg_28_0.equipmentB, arg_28_0._tf)

	arg_28_0.shareData = None

return var_0_0
