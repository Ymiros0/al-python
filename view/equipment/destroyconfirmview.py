local var_0_0 = class("DestroyConfirmView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "StoreHouseDestroyConfirmView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.destroyBonusList = arg_2_0._tf.Find("frame/bg/scrollview/list")
	arg_2_0.destroyBonusItem = arg_2_0.destroyBonusList.Find("equipment_tpl")
	arg_2_0.destroyNoGotTip = arg_2_0._tf.Find("frame/bg/tip")

	setText(arg_2_0.findTF("frame/title_text/Text"), i18n("equipment_select_device_destroy_bonus_tip"))
	setText(arg_2_0.destroyNoGotTip, i18n("equipment_select_device_destroy_nobonus_tip"))
	onButton(arg_2_0, arg_2_0.findTF("frame/actions/cancel_btn"), function()
		arg_2_0.Hide(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0._tf, function()
		arg_2_0.Hide(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.findTF("frame/top/btnBack"), function()
		arg_2_0.Hide(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.findTF("frame/actions/confirm_btn"), function()
		arg_2_0.emit(EquipmentMediator.ON_DESTROY, arg_2_0.selectedIds)
		arg_2_0.confirmBtnCB()
		arg_2_0.Hide(), SFX_UI_EQUIPMENT_RESOLVE)

def var_0_0.Show(arg_7_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_7_0._tf)
	setActive(arg_7_0._tf, True)

def var_0_0.Hide(arg_8_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_8_0._tf, arg_8_0._parentTf)
	setActive(arg_8_0._tf, False)

def var_0_0.SetConfirmBtnCB(arg_9_0, arg_9_1):
	arg_9_0.confirmBtnCB = arg_9_1

def var_0_0.DisplayDestroyBonus(arg_10_0, arg_10_1):
	arg_10_0.selectedIds = arg_10_1

	local var_10_0 = {}
	local var_10_1 = 0

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.selectedIds):
		if Equipment.CanInBag(iter_10_1[1]):
			local var_10_2 = Equipment.getConfigData(iter_10_1[1])
			local var_10_3 = var_10_2.destory_item or {}

			var_10_1 = var_10_1 + (var_10_2.destory_gold or 0) * iter_10_1[2]

			for iter_10_2, iter_10_3 in ipairs(var_10_3):
				local var_10_4 = False

				for iter_10_4, iter_10_5 in ipairs(var_10_0):
					if iter_10_3[1] == var_10_0[iter_10_4].id:
						var_10_0[iter_10_4].count = var_10_0[iter_10_4].count + iter_10_3[2] * iter_10_1[2]
						var_10_4 = True

						break

				if not var_10_4:
					table.insert(var_10_0, {
						type = DROP_TYPE_ITEM,
						id = iter_10_3[1],
						count = iter_10_3[2] * iter_10_1[2]
					})

	if var_10_1 > 0:
		table.insert(var_10_0, {
			id = 1,
			type = DROP_TYPE_RESOURCE,
			count = var_10_1
		})

	setActive(arg_10_0.destroyNoGotTip, #var_10_0 <= 0)

	if not arg_10_0.destroyList:
		arg_10_0.destroyList = UIItemList.New(arg_10_0.destroyBonusList, arg_10_0.destroyBonusItem)

	arg_10_0.destroyList.make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate:
			local var_11_0 = var_10_0[arg_11_1 + 1]

			if var_11_0.type == DROP_TYPE_SHIP:
				arg_10_0.hasShip = True

			updateDrop(arg_11_2, var_11_0)

			local var_11_1, var_11_2 = contentWrap(var_11_0.getConfig("name"), 10, 2)

			if var_11_1:
				var_11_2 = var_11_2 .. "..."

			setText(arg_11_2.Find("name"), var_11_2)
			onButton(arg_10_0, arg_11_2, function()
				if var_11_0.type == DROP_TYPE_RESOURCE or var_11_0.type == DROP_TYPE_ITEM:
					arg_10_0.emit(BaseUI.ON_ITEM, var_11_0.getConfig("id"))
				elif var_11_0.type == DROP_TYPE_EQUIP:
					arg_10_0.emit(BaseUI.ON_EQUIPMENT, {
						equipmentId = var_11_0.getConfig("id"),
						type = EquipmentInfoMediator.TYPE_DISPLAY
					}), SFX_PANEL))
	arg_10_0.destroyList.align(#var_10_0)

return var_0_0
