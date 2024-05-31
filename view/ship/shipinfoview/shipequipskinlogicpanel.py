local var_0_0 = class("ShipEquipSkinLogicPanel", import("...base.BasePanel"))
local var_0_1 = 0.2

def var_0_0.init(arg_1_0):
	arg_1_0.equipmentTFs = {
		arg_1_0.findTF("equipment_r/skin/equipment_r1"),
		arg_1_0.findTF("equipment_r/skin/equipment_r2"),
		arg_1_0.findTF("equipment_r/skin/equipment_r3"),
		arg_1_0.findTF("equipment_l/skin/equipment_l1"),
		arg_1_0.findTF("equipment_l/skin/equipment_l2")
	}
	arg_1_0.equipmentNormalTFs = {
		arg_1_0.findTF("equipment_r/equipment/equipment_r1"),
		arg_1_0.findTF("equipment_r/equipment/equipment_r2"),
		arg_1_0.findTF("equipment_r/equipment/equipment_r3"),
		arg_1_0.findTF("equipment_l/equipment/equipment_l1"),
		arg_1_0.findTF("equipment_l/equipment/equipment_l2")
	}
	arg_1_0.spweaponNormalTF = arg_1_0.findTF("equipment_b/equipment")
	arg_1_0.equipmentR = arg_1_0.findTF("equipment_r/equipment")
	arg_1_0.equipmentL = arg_1_0.findTF("equipment_l/equipment")
	arg_1_0.skinR = arg_1_0.findTF("equipment_r/skin")
	arg_1_0.skinL = arg_1_0.findTF("equipment_l/skin")
	arg_1_0.infoPanel = arg_1_0.findTF("info", arg_1_0.equipmentTFs[1])
	arg_1_0.inSkinPage = True

	for iter_1_0 = 1, 3:
		local var_1_0 = findTF(arg_1_0.skinR, "equipment_r" .. iter_1_0 .. "/info/equip/info/unMatch/txt")

		setText(var_1_0, i18n("equipskin_typewrong"))

		local var_1_1 = findTF(arg_1_0.skinR, "equipment_r" .. iter_1_0 .. "/info/equip/info/unMatch/forbid_en")

		setText(var_1_1, i18n("equipskin_typewrong_en"))

		local var_1_2 = findTF(arg_1_0.skinR, "equipment_r" .. iter_1_0 .. "/info/equip/add/Text")

		setText(var_1_2, i18n("equipskin_add"))

		local var_1_3 = findTF(arg_1_0.skinR, "equipment_r" .. iter_1_0 .. "/info/forbid")

		setText(var_1_3, i18n("equipskin_none"))

	for iter_1_1 = 1, 2:
		local var_1_4 = arg_1_0.equipmentTFs[3 + iter_1_1]
		local var_1_5 = var_1_4.Find("info")

		if IsNil(var_1_5):
			local var_1_6 = cloneTplTo(arg_1_0.infoPanel, var_1_4, "info")

		local var_1_7 = findTF(arg_1_0.skinL, "equipment_l" .. iter_1_1 .. "/forbid")

		setActive(var_1_7, False)

		local var_1_8 = findTF(arg_1_0.skinL, "equipment_l" .. iter_1_1 .. "/info/equip/info/unMatch/txt")

		setText(var_1_8, i18n("equipskin_typewrong"))

		local var_1_9 = findTF(arg_1_0.skinL, "equipment_l" .. iter_1_1 .. "/info/equip/info/unMatch/forbid_en")

		setText(var_1_9, i18n("equipskin_typewrong_en"))

		local var_1_10 = findTF(arg_1_0.skinL, "equipment_l" .. iter_1_1 .. "/info/equip/add/Text")

		setText(var_1_10, i18n("equipskin_add"))

		local var_1_11 = findTF(arg_1_0.skinL, "equipment_l" .. iter_1_1 .. "/info/forbid")

		setText(var_1_11, i18n("equipskin_none"))

	for iter_1_2 = 1, #arg_1_0.equipmentNormalTFs:
		local var_1_12 = findTF(arg_1_0.equipmentNormalTFs[iter_1_2], "empty/tip")

		setText(var_1_12, i18n("equip_add"))

	local var_1_13 = findTF(arg_1_0.spweaponNormalTF, "empty/tip")

	setText(var_1_13, i18n("equip_add"))

def var_0_0.setLabelResource(arg_2_0, arg_2_1):
	arg_2_0.resource = arg_2_1

def var_0_0.doSwitchAnim(arg_3_0, arg_3_1):
	if arg_3_0.isTweening():
		return

	arg_3_0.inSkinPage = arg_3_1

	arg_3_0.doAnim(arg_3_0.equipmentR, arg_3_0.skinR)
	arg_3_0.doAnim(arg_3_0.equipmentL, arg_3_0.skinL)

def var_0_0.isTweening(arg_4_0):
	if LeanTween.isTweening(go(arg_4_0.equipmentR)) or LeanTween.isTweening(go(arg_4_0.skinR)) or LeanTween.isTweening(go(arg_4_0.equipmentL)) or LeanTween.isTweening(go(arg_4_0.skinL)):
		return True

	return False

def var_0_0.doAnim(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_2.localPosition
	local var_5_1 = arg_5_1.localPosition
	local var_5_2 = arg_5_1.GetComponent(typeof(CanvasGroup))
	local var_5_3 = arg_5_2.GetComponent(typeof(CanvasGroup))

	LeanTween.moveLocal(go(arg_5_1), var_5_0, var_0_1)
	LeanTween.moveLocal(go(arg_5_2), var_5_1, var_0_1)

	local var_5_4 = 0.8
	local var_5_5 = 1

	if not arg_5_0.inSkinPage:
		var_5_4, var_5_5 = 1, 0.8

	LeanTween.value(go(arg_5_1), var_5_4, var_5_5, var_0_1).setOnUpdate(System.Action_float(function(arg_6_0)
		var_5_2.alpha = arg_6_0))
	LeanTween.value(go(arg_5_2), var_5_5, var_5_4, var_0_1).setOnUpdate(System.Action_float(function(arg_7_0)
		var_5_3.alpha = arg_7_0))

	var_5_3.blocksRaycasts = not arg_5_0.inSkinPage
	var_5_2.blocksRaycasts = arg_5_0.inSkinPage

	;(not arg_5_0.inSkinPage and arg_5_2 or arg_5_1).SetAsLastSibling()

def var_0_0.updateAll(arg_8_0, arg_8_1):
	if arg_8_1:
		for iter_8_0, iter_8_1 in ipairs(arg_8_0.equipmentTFs):
			if not not table.contains(ShipEquipView.UNLOCK_EQUIPMENT_SKIN_POS, iter_8_0):
				arg_8_0.updateEquipmentTF(arg_8_1, iter_8_0)

			local var_8_0 = arg_8_0.findTF("shadow", iter_8_1)

			if var_8_0:
				setActive(var_8_0, arg_8_0.inSkinPage)

		for iter_8_2, iter_8_3 in ipairs(arg_8_0.equipmentNormalTFs):
			local var_8_1 = arg_8_0.findTF("shadow", iter_8_3)

			if var_8_1:
				setActive(var_8_1, not arg_8_0.inSkinPage)

def var_0_0.updateEquipmentTF(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0.shipVO = arg_9_1

	if arg_9_1:
		local var_9_0 = arg_9_0.equipmentTFs[arg_9_2]

		removeOnButton(var_9_0)

		local var_9_1 = arg_9_1.getEquip(arg_9_2)
		local var_9_2 = arg_9_1.getEquipSkin(arg_9_2)
		local var_9_3 = var_9_0.Find("info")

		if IsNil(var_9_3):
			var_9_3 = cloneTplTo(arg_9_0.infoPanel, var_9_0, "info")

		local var_9_4 = arg_9_0.findTF("panel_title/type", var_9_0)
		local var_9_5 = EquipType.Types2Title(arg_9_2, arg_9_0.shipVO.configId)
		local var_9_6 = EquipType.LabelToName(var_9_5)

		var_9_4.GetComponent(typeof(Text)).text = var_9_6

		setActive(var_9_0.Find("unequip"), False)

		local var_9_7 = arg_9_1.getCanEquipSkin(arg_9_2)

		setActive(var_9_3.Find("forbid"), not var_9_7)

		local var_9_8 = var_9_3.Find("equip")

		setActive(var_9_8, var_9_7)

		if var_9_7:
			arg_9_0.updateEquipmentPanel(var_9_8, arg_9_2)

def var_0_0.updateEquipmentPanel(arg_10_0, arg_10_1, arg_10_2):
	if not arg_10_0.shipVO.getCanEquipSkin(arg_10_2):
		return

	local var_10_0 = arg_10_0.shipVO.getEquipSkin(arg_10_2) != 0
	local var_10_1 = arg_10_0.shipVO.getEquip(arg_10_2)
	local var_10_2 = arg_10_0.shipVO.getEquipSkin(arg_10_2)
	local var_10_3 = False

	if var_10_2 != 0:
		if var_10_1:
			local var_10_4 = var_10_1.getType()
			local var_10_5 = pg.equip_skin_template[var_10_2].equip_type

			if not table.contains(var_10_5, var_10_4):
				var_10_3 = True
		else
			var_10_3 = True

	local var_10_6 = arg_10_1.Find("add")
	local var_10_7 = arg_10_1.Find("info")
	local var_10_8 = var_10_7.Find("unMatch")
	local var_10_9 = var_10_7.Find("desc")

	setActive(var_10_7, var_10_0)
	setActive(var_10_6, not var_10_0)
	setActive(var_10_8, var_10_3)
	setActive(var_10_9, not var_10_3)

	if var_10_0:
		arg_10_0.updateSkinInfo(var_10_7, var_10_2)
		onButton(arg_10_0, arg_10_0.equipmentTFs[arg_10_2], function()
			arg_10_0.emit(ShipMainMediator.ON_SELECT_EQUIPMENT_SKIN, arg_10_2), SFX_PANEL)
	else
		onButton(arg_10_0, var_10_6.Find("icon"), function()
			arg_10_0.emit(ShipMainMediator.ON_SELECT_EQUIPMENT_SKIN, arg_10_2), SFX_PANEL)

def var_0_0.updateSkinInfo(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = pg.equip_skin_template[arg_13_2]

	assert(var_13_0, "miss config equip_skin_template >>" .. arg_13_2)
	setText(arg_13_1.Find("desc"), var_13_0.desc)
	setText(arg_13_1.Find("cont/name_mask/name"), shortenString(var_13_0.name, 10))
	updateDrop(arg_13_1.Find("IconTpl"), {
		type = DROP_TYPE_EQUIPMENT_SKIN,
		id = arg_13_2
	})

return var_0_0
