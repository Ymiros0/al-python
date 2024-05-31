local var_0_0 = class("ResolveEquipmentLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "ResolveEquipmentUI"

def var_0_0.setPlayer(arg_2_0, arg_2_1):
	arg_2_0.player = arg_2_1

def var_0_0.setEquipments(arg_3_0, arg_3_1):
	arg_3_0.equipmentVOs = arg_3_1

	arg_3_0.setEquipmentByIds(arg_3_1)

def var_0_0.setEquipmentByIds(arg_4_0, arg_4_1):
	arg_4_0.equipmentVOByIds = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_1):
		arg_4_0.equipmentVOByIds[iter_4_1.id] = iter_4_1

def var_0_0.init(arg_5_0):
	arg_5_0.mainPanel = arg_5_0.findTF("main")

	setActive(arg_5_0.mainPanel, True)

	arg_5_0.viewRect = arg_5_0.findTF("main/frame/view").GetComponent("LScrollRect")
	arg_5_0.backBtn = arg_5_0.findTF("main/top/btnBack")
	arg_5_0.cancelBtn = arg_5_0.findTF("main/cancel_btn")
	arg_5_0.okBtn = arg_5_0.findTF("main/ok_btn")

	pg.UIMgr.GetInstance().BlurPanel(arg_5_0._tf, False, {})

	arg_5_0.selectedIds = {}
	arg_5_0.selecteAllTF = arg_5_0.findTF("main/all_toggle")
	arg_5_0.selecteAllToggle = arg_5_0.selecteAllTF.GetComponent(typeof(Toggle))
	arg_5_0.destroyConfirm = arg_5_0.findTF("destroy_confirm")
	arg_5_0.destroyBonusList = arg_5_0.destroyConfirm.Find("got/scrollview/list")
	arg_5_0.destroyBonusItem = arg_5_0.destroyConfirm.Find("got/scrollview/item")

	setActive(arg_5_0.destroyConfirm, False)
	setActive(arg_5_0.destroyBonusItem, False)

	arg_5_0.equipDestroyConfirmWindow = EquipDestoryConfirmWindow.New(arg_5_0._tf, arg_5_0.event)

def var_0_0.didEnter(arg_6_0):
	arg_6_0.initEquipments()
	onButton(arg_6_0, arg_6_0.backBtn, function()
		arg_6_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_6_0, arg_6_0.cancelBtn, function()
		arg_6_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_6_0, arg_6_0.okBtn, function()
		local var_9_0 = {}

		if underscore.any(arg_6_0.selectedIds, function(arg_10_0)
			local var_10_0 = arg_6_0.equipmentVOByIds[arg_10_0[1]]

			return var_10_0.getConfig("rarity") >= 4 or var_10_0.getConfig("level") > 1):
			table.insert(var_9_0, function(arg_11_0)
				arg_6_0.equipDestroyConfirmWindow.Load()
				arg_6_0.equipDestroyConfirmWindow.ActionInvoke("Show", underscore.map(arg_6_0.selectedIds, function(arg_12_0)
					return setmetatable({
						count = arg_12_0[2]
					}, {
						__index = arg_6_0.equipmentVOByIds[arg_12_0[1]]
					})), arg_11_0))

		seriesAsync(var_9_0, function()
			if #arg_6_0.selectedIds <= 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("err_resloveequip_nochoice"))

				return

			setActive(arg_6_0.mainPanel, False)
			setActive(arg_6_0.destroyConfirm, True)
			arg_6_0.displayDestroyBonus()), SFX_CONFIRM)
	onButton(arg_6_0, findTF(arg_6_0.destroyConfirm, "actions/cancel_button"), function()
		setActive(arg_6_0.destroyConfirm, False)
		setActive(arg_6_0.mainPanel, True)
		pg.UIMgr.GetInstance().UnblurPanel(arg_6_0.destroyConfirm, arg_6_0._tf), SFX_CANCEL)
	onButton(arg_6_0, findTF(arg_6_0.destroyConfirm, "actions/destroy_button"), function()
		local var_15_0 = {}

		seriesAsync(var_15_0, function()
			arg_6_0.emit(ResolveEquipmentMediator.ON_RESOLVE, arg_6_0.selectedIds)), SFX_UI_EQUIPMENT_RESOLVE)
	onToggle(arg_6_0, arg_6_0.selecteAllTF, function(arg_17_0)
		if arg_6_0.isManual:
			return

		if arg_17_0:
			arg_6_0.selecteAllEquips()
		else
			arg_6_0.unselecteAllEquips(), SFX_PANEL)

def var_0_0.OnResolveEquipDone(arg_18_0):
	setActive(arg_18_0.destroyConfirm, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_18_0._tf)
	setActive(arg_18_0.mainPanel, False)
	arg_18_0.unselecteAllEquips()

def var_0_0.onBackPressed(arg_19_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_19_0.destroyConfirm):
		triggerButton(findTF(arg_19_0.destroyConfirm, "actions/cancel_button"))
	elif arg_19_0.equipDestroyConfirmWindow.isShowing():
		arg_19_0.equipDestroyConfirmWindow.Hide()
	else
		triggerButton(arg_19_0.cancelBtn)

def var_0_0.selectedLowRarityEquipment(arg_20_0):
	arg_20_0.selectedIds = {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.equipmentVOs):
		if iter_20_1.getConfig("level") <= 1 and iter_20_1.getConfig("rarity") < 4:
			arg_20_0.selectEquip(iter_20_1, iter_20_1.count)

	arg_20_0.updateSelected()

def var_0_0.selecteAllEquips(arg_21_0):
	arg_21_0.selectedIds = {}

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.equipmentVOs):
		arg_21_0.selectEquip(iter_21_1, iter_21_1.count)

	arg_21_0.updateSelected()

def var_0_0.unselecteAllEquips(arg_22_0):
	arg_22_0.selectedIds = {}

	arg_22_0.updateSelected()

def var_0_0.displayDestroyBonus(arg_23_0):
	local var_23_0 = {}
	local var_23_1 = 0

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.selectedIds):
		if Equipment.CanInBag(iter_23_1[1]):
			local var_23_2 = Equipment.getConfigData(iter_23_1[1])
			local var_23_3 = var_23_2.destory_item or {}

			var_23_1 = var_23_1 + (var_23_2.destory_gold or 0) * iter_23_1[2]

			for iter_23_2, iter_23_3 in ipairs(var_23_3):
				local var_23_4 = False

				for iter_23_4, iter_23_5 in ipairs(var_23_0):
					if iter_23_3[1] == var_23_0[iter_23_4].id:
						var_23_0[iter_23_4].count = var_23_0[iter_23_4].count + iter_23_3[2] * iter_23_1[2]
						var_23_4 = True

						break

				if not var_23_4:
					table.insert(var_23_0, {
						type = DROP_TYPE_ITEM,
						id = iter_23_3[1],
						count = iter_23_3[2] * iter_23_1[2]
					})

	if var_23_1 > 0:
		table.insert(var_23_0, {
			id = 1,
			type = DROP_TYPE_RESOURCE,
			count = var_23_1
		})

	for iter_23_6 = #var_23_0, arg_23_0.destroyBonusList.childCount - 1:
		Destroy(arg_23_0.destroyBonusList.GetChild(iter_23_6))

	for iter_23_7 = arg_23_0.destroyBonusList.childCount, #var_23_0 - 1:
		cloneTplTo(arg_23_0.destroyBonusItem, arg_23_0.destroyBonusList)

	for iter_23_8 = 1, #var_23_0:
		local var_23_5 = arg_23_0.destroyBonusList.GetChild(iter_23_8 - 1)
		local var_23_6 = var_23_0[iter_23_8]

		if var_23_6.type == DROP_TYPE_SHIP:
			arg_23_0.hasShip = True

		local var_23_7 = var_23_5.Find("icon_bg/icon/icon")

		GetComponent(var_23_5.Find("icon_bg/icon"), typeof(Image)).enabled = True

		if not IsNil(var_23_7):
			setActive(var_23_7, False)

		updateDrop(var_23_5, var_23_6)

		local var_23_8, var_23_9 = contentWrap(var_23_6.getConfig("name"), 10, 2)

		if var_23_8:
			var_23_9 = var_23_9 .. "..."

		setText(var_23_5.Find("name"), var_23_9)
		onButton(arg_23_0, var_23_5, function()
			if var_23_6.type == DROP_TYPE_RESOURCE or var_23_6.type == DROP_TYPE_ITEM:
				arg_23_0.emit(var_0_0.ON_ITEM, var_23_6.getConfig("id"))
			elif var_23_6.type == DROP_TYPE_EQUIP:
				arg_23_0.emit(var_0_0.ON_EQUIPMENT, {
					equipmentId = var_23_6.getConfig("id"),
					type = EquipmentInfoMediator.TYPE_DISPLAY
				}), SFX_PANEL)

def var_0_0.initEquipments(arg_25_0):
	function arg_25_0.viewRect.onInitItem(arg_26_0)
		arg_25_0.onInitItem(arg_26_0)

	function arg_25_0.viewRect.onUpdateItem(arg_27_0, arg_27_1)
		arg_25_0.onUpdateItem(arg_27_0, arg_27_1)

	function arg_25_0.viewRect.onStart()
		arg_25_0.selectedLowRarityEquipment()

	arg_25_0.cards = {}

	arg_25_0.filterEquipments()

def var_0_0.filterEquipments(arg_29_0):
	table.sort(arg_29_0.equipmentVOs, CompareFuncs({
		function(arg_30_0)
			return -arg_30_0.getConfig("rarity"),
		function(arg_31_0)
			return arg_31_0.id
	}))
	arg_29_0.viewRect.SetTotalCount(#arg_29_0.equipmentVOs, -1)

def var_0_0.onInitItem(arg_32_0, arg_32_1):
	local var_32_0 = EquipmentItem.New(arg_32_1)

	onButton(arg_32_0, var_32_0.go, function()
		arg_32_0.selectEquip(var_32_0.equipmentVO, var_32_0.equipmentVO.count), SFX_PANEL)
	onButton(arg_32_0, var_32_0.reduceBtn, function()
		arg_32_0.selectEquip(var_32_0.equipmentVO, 1), SFX_PANEL)

	arg_32_0.cards[arg_32_1] = var_32_0

def var_0_0.onUpdateItem(arg_35_0, arg_35_1, arg_35_2):
	local var_35_0 = arg_35_0.cards[arg_35_2]

	if not var_35_0:
		arg_35_0.onInitItem(arg_35_2)

		var_35_0 = arg_35_0.cards[arg_35_2]

	local var_35_1 = arg_35_0.equipmentVOs[arg_35_1 + 1]

	var_35_0.update(var_35_1, True)

def var_0_0.isSelectedAll(arg_36_0):
	for iter_36_0, iter_36_1 in pairs(arg_36_0.equipmentVOByIds):
		local var_36_0 = False

		for iter_36_2, iter_36_3 in pairs(arg_36_0.selectedIds):
			if iter_36_3[1] == iter_36_1.id and iter_36_1.count == iter_36_3[2]:
				var_36_0 = True

		if var_36_0 == False:
			return False

	return True

def var_0_0.selectEquip(arg_37_0, arg_37_1, arg_37_2):
	if not arg_37_0.checkDestroyGold(arg_37_1, arg_37_2):
		return

	if arg_37_1.isImportance():
		pg.TipsMgr.GetInstance().ShowTips(i18n("retire_importantequipment_tips"))

		return

	local var_37_0 = False
	local var_37_1
	local var_37_2 = 0

	for iter_37_0, iter_37_1 in pairs(arg_37_0.selectedIds):
		if iter_37_1[1] == arg_37_1.id:
			var_37_0 = True
			var_37_1 = iter_37_0
			var_37_2 = iter_37_1[2]

			break

	if not var_37_0:
		table.insert(arg_37_0.selectedIds, {
			arg_37_1.id,
			arg_37_2
		})
	elif var_37_2 - arg_37_2 > 0:
		arg_37_0.selectedIds[var_37_1][2] = var_37_2 - arg_37_2
	else
		table.remove(arg_37_0.selectedIds, var_37_1)

	arg_37_0.updateSelected()

	local var_37_3 = arg_37_0.isSelectedAll()

	arg_37_0.isManual = True

	triggerToggle(arg_37_0.selecteAllTF, var_37_3)

	arg_37_0.isManual = None

def var_0_0.updateSelected(arg_38_0):
	for iter_38_0, iter_38_1 in pairs(arg_38_0.cards):
		if iter_38_1.equipmentVO:
			local var_38_0 = False
			local var_38_1 = 0

			for iter_38_2, iter_38_3 in pairs(arg_38_0.selectedIds):
				if iter_38_1.equipmentVO.id == iter_38_3[1]:
					var_38_0 = True
					var_38_1 = iter_38_3[2]

					break

			iter_38_1.updateSelected(var_38_0, var_38_1)

def var_0_0.checkDestroyGold(arg_39_0, arg_39_1, arg_39_2):
	local var_39_0 = 0
	local var_39_1 = False

	for iter_39_0, iter_39_1 in pairs(arg_39_0.selectedIds):
		local var_39_2 = iter_39_1[2]

		if Equipment.CanInBag(iter_39_1[1]):
			var_39_0 = var_39_0 + (Equipment.getConfigData(iter_39_1[1]).destory_gold or 0) * var_39_2

		if arg_39_1 and iter_39_1[1] == arg_39_1.configId:
			var_39_1 = True

	if not var_39_1 and arg_39_1 and arg_39_2 > 0:
		var_39_0 = var_39_0 + (arg_39_1.getConfig("destory_gold") or 0) * arg_39_2

	if arg_39_0.player.GoldMax(var_39_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_destroy"))

		return False

	return True

def var_0_0.willExit(arg_40_0):
	arg_40_0.equipDestroyConfirmWindow.Destroy()
	pg.UIMgr.GetInstance().UnblurPanel(arg_40_0._tf, pg.UIMgr.GetInstance().UIMain)

return var_0_0
