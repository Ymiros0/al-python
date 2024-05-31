local var_0_0 = class("ShipModLayer", import("..base.BaseUI"))
local var_0_1 = 12

var_0_0.IGNORE_ID = 4

def var_0_0.getUIName(arg_1_0):
	return "ShipModUI"

def var_0_0.setShipVOs(arg_2_0, arg_2_1):
	arg_2_0.shipVOs = arg_2_1

def var_0_0.init(arg_3_0):
	arg_3_0.blurPanelTF = arg_3_0.findTF("blur_panel")
	arg_3_0.mainPanel = arg_3_0.findTF("blur_panel/main")
	arg_3_0.shipContainer = arg_3_0.findTF("bg/add_ship_panel/ships", arg_3_0.mainPanel)
	arg_3_0.attrsPanel = arg_3_0.findTF("bg/property_panel/attrs", arg_3_0.mainPanel)

	setText(arg_3_0.findTF("bg/add_ship_panel/title/tip", arg_3_0.mainPanel), i18n("ship_mod_exp_to_attr_tip"))

def var_0_0.didEnter(arg_4_0):
	onButton(arg_4_0, arg_4_0.findTF("ok_btn", arg_4_0.mainPanel), function()
		local function var_5_0()
			local var_6_0, var_6_1 = ShipStatus.ShipStatusCheck("onModify", arg_4_0.shipVO)

			if not var_6_0:
				pg.TipsMgr.GetInstance().ShowTips(var_6_1)

				return

			if not arg_4_0.contextData.materialShipIds or #arg_4_0.contextData.materialShipIds == 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_materal_no_enough"))

				return
			else
				arg_4_0.startModShip()

		if arg_4_0.shipVO.isActivityNpc():
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("npc_strength_tip"),
				onYes = var_5_0
			})
		else
			var_5_0(), SFX_CONFIRM)
	onButton(arg_4_0, arg_4_0.findTF("cancel_btn", arg_4_0.mainPanel), function()
		local var_7_0 = arg_4_0.contextData.materialShipIds

		if not var_7_0 or table.getCount(var_7_0) == 0:
			return

		arg_4_0.clearAllShip(), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.findTF("select_btn", arg_4_0.mainPanel), function()
		arg_4_0.emit(ShipModMediator.ON_AUTO_SELECT_SHIP), SFX_CANCEL)
	arg_4_0.initAttrs()

	arg_4_0.inited = True

	arg_4_0.emit(ShipModMediator.LOADEND, arg_4_0.mainPanel)
	arg_4_0.blurPanel(True)

def var_0_0.blurPanel(arg_9_0, arg_9_1):
	local var_9_0 = pg.UIMgr.GetInstance()

	if arg_9_1:
		var_9_0.OverlayPanelPB(arg_9_0.blurPanelTF, {
			pbList = {
				arg_9_0.mainPanel.Find("bg")
			},
			groupName = arg_9_0.getGroupNameFromData(),
			overlayType = LayerWeightConst.OVERLAY_UI_ADAPT
		})
	else
		var_9_0.UnOverlayPanel(arg_9_0.blurPanelTF, arg_9_0._tf)

def var_0_0.startModShip(arg_10_0):
	if not arg_10_0.hasAddition:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("ship_mod_no_addition_tip"),
			def onYes:()
				arg_10_0.emit(ShipModMediator.MOD_SHIP, arg_10_0.shipVO.id)
		})
	else
		arg_10_0.emit(ShipModMediator.MOD_SHIP, arg_10_0.shipVO.id)

def var_0_0.setShip(arg_12_0, arg_12_1):
	arg_12_0.shipVO = arg_12_1

	arg_12_0.initSelectedShips()

	if arg_12_0.inited:
		arg_12_0.initAttrs()

def var_0_0.clearAllShip(arg_13_0):
	for iter_13_0 = 1, var_0_1:
		local var_13_0 = arg_13_0.shipContainer.GetChild(iter_13_0 - 1)

		setActive(var_13_0.Find("IconTpl"), False)
		onButton(arg_13_0, var_13_0.Find("add"), function()
			arg_13_0.emit(ShipModMediator.ON_SELECT_MATERIAL_SHIPS), SFX_PANEL)

	arg_13_0.contextData.materialShipIds = None

	arg_13_0.updateAttrs()

def var_0_0.initSelectedShips(arg_15_0):
	local var_15_0 = arg_15_0.contextData.materialShipIds or {}
	local var_15_1 = table.getCount(var_15_0)

	for iter_15_0 = 1, var_0_1:
		local var_15_2 = arg_15_0.shipContainer.GetChild(iter_15_0 - 1)

		if iter_15_0 <= var_15_1:
			arg_15_0.updateShip(var_15_2, var_15_0[iter_15_0])
		else
			onButton(arg_15_0, var_15_2.Find("add"), function()
				arg_15_0.emit(ShipModMediator.ON_SELECT_MATERIAL_SHIPS), SFX_PANEL)

		setActive(var_15_2.Find("IconTpl"), iter_15_0 <= var_15_1)

def var_0_0.updateShip(arg_17_0, arg_17_1, arg_17_2):
	local var_17_0 = arg_17_0.shipVOs[arg_17_2]

	onButton(arg_17_0, arg_17_1, function()
		for iter_18_0, iter_18_1 in ipairs(arg_17_0.contextData.materialShipIds):
			if arg_17_2 == iter_18_1:
				local var_18_0 = arg_17_1.Find("add")

				setActive(arg_17_1.Find("IconTpl"), False)
				onButton(arg_17_0, var_18_0, function()
					arg_17_0.emit(ShipModMediator.ON_SELECT_MATERIAL_SHIPS), SFX_PANEL)
				table.remove(arg_17_0.contextData.materialShipIds, iter_18_0)
				arg_17_0.updateAttrs()

				break, SFX_PANEL)
	updateShip(arg_17_0.findTF("IconTpl", arg_17_1), var_17_0, {
		initStar = True
	})
	setText(arg_17_1.Find("IconTpl/icon_bg/lv/Text"), var_17_0.level)

def var_0_0.initAttrs(arg_20_0):
	arg_20_0.attrTFs = {}

	for iter_20_0, iter_20_1 in pairs(ShipModAttr.ID_TO_ATTR):
		if arg_20_0.IGNORE_ID != iter_20_0:
			local var_20_0 = arg_20_0.attrsPanel.Find("attr_" .. iter_20_0)

			arg_20_0.attrTFs[iter_20_0] = var_20_0

	arg_20_0.updateAttrs()

def var_0_0.updateAttrs(arg_21_0):
	arg_21_0.hasAddition = None

	for iter_21_0, iter_21_1 in pairs(arg_21_0.attrTFs):
		arg_21_0.updateAttr(iter_21_0)

def var_0_0.updateAttr(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_0.attrTFs[arg_22_1]
	local var_22_1 = arg_22_0.findTF("info", var_22_0)
	local var_22_2 = var_22_0.GetComponent(typeof(CanvasGroup))
	local var_22_3 = ShipModAttr.ID_TO_ATTR[arg_22_1]
	local var_22_4 = arg_22_0.shipVO.getModAttrTopLimit(var_22_3)
	local var_22_5 = intProperties(arg_22_0.shipVO.getShipProperties())
	local var_22_6 = arg_22_0.getMaterialShips(arg_22_0.contextData.materialShipIds)
	local var_22_7 = var_0_0.getExpAddition(arg_22_0.shipVO, var_22_6, var_22_3)
	local var_22_8 = arg_22_0.shipVO.getModExpRatio(var_22_3)
	local var_22_9 = math.max(arg_22_0.shipVO.getModExpRatio(var_22_3), 1)

	if var_22_7 != 0:
		arg_22_0.hasAddition = True

	local var_22_10 = arg_22_0.shipVO.getModAttrBaseMax(var_22_3)
	local var_22_11 = arg_22_0.getRemainExp(arg_22_0.shipVO, var_22_3)
	local var_22_12 = math.max(math.min(math.floor((var_22_11 + var_22_7) / var_22_9), var_22_10 - var_22_5[var_22_3]), 0)

	setText(arg_22_0.findTF("info_container/addition", var_22_1), "+" .. var_22_12)
	setText(arg_22_0.findTF("info_container/name", var_22_1), AttributeType.Type2Name(var_22_3))
	setText(arg_22_0.findTF("max_container/Text", var_22_1), var_22_10)
	setText(arg_22_0.findTF("info_container/value", var_22_1), var_22_5[var_22_3])

	var_22_2.alpha = var_22_5[var_22_3] == 0 and 0.3 or 1

	local var_22_13 = arg_22_0.findTF("prev_slider", var_22_1).GetComponent(typeof(Slider))

	arg_22_0.setSliderValue(var_22_13, (var_22_7 + var_22_11) / var_22_9)

	local var_22_14 = var_22_11 / var_22_9
	local var_22_15 = var_22_11 + var_22_7 .. "/" .. var_22_8

	if var_22_10 == var_22_5[var_22_3] and var_22_5[var_22_3] != 0:
		var_22_14 = 1
		var_22_15 = "MAX"

	local var_22_16 = arg_22_0.findTF("cur_slider", var_22_1).GetComponent(typeof(Slider))

	arg_22_0.setSliderValue(var_22_16, var_22_14)
	setText(arg_22_0.findTF("exp_container/Text", var_22_0), var_22_15)

def var_0_0.modAttrAnim(arg_23_0, arg_23_1, arg_23_2, arg_23_3):
	local var_23_0 = arg_23_3 or 0.3
	local var_23_1 = intProperties(arg_23_1.getShipProperties())
	local var_23_2 = intProperties(arg_23_2.getShipProperties())

	arg_23_0.tweens = {}

	for iter_23_0, iter_23_1 in pairs(arg_23_0.attrTFs):
		local var_23_3 = ShipModAttr.ID_TO_ATTR[iter_23_0]
		local var_23_4 = arg_23_1.getModAttrTopLimit(var_23_3)
		local var_23_5 = arg_23_0.shipVO.getModAttrBaseMax(var_23_3)

		if var_23_4 == 0:
			arg_23_0.updateAttr(iter_23_0)
		else
			local var_23_6 = arg_23_0.attrTFs[iter_23_0]
			local var_23_7 = arg_23_0.findTF("info", var_23_6)
			local var_23_8 = arg_23_0.findTF("info_container/value", var_23_7)
			local var_23_9 = var_23_1[var_23_3] - var_23_2[var_23_3]
			local var_23_10 = math.max(arg_23_1.getModExpRatio(var_23_3), 1)
			local var_23_11 = arg_23_0.findTF("cur_slider", var_23_7)
			local var_23_12 = arg_23_0.findTF("prev_slider", var_23_7)
			local var_23_13 = var_23_11.GetComponent(typeof(Slider))
			local var_23_14 = var_23_12.GetComponent(typeof(Slider))
			local var_23_15 = arg_23_0.getRemainExp(arg_23_1, var_23_3)
			local var_23_16 = arg_23_0.findTF("info_container/addition", var_23_7)
			local var_23_17 = arg_23_0.findTF("exp_container/Text", var_23_6)

			arg_23_0.setSliderValue(var_23_14, 0)
			setText(arg_23_0.findTF("exp_container/Text", var_23_6), var_23_15 .. "/" .. var_23_10)

			local function var_23_18(arg_24_0, arg_24_1)
				setText(var_23_8, arg_24_0)
				setText(var_23_16, "+" .. arg_24_1)

			if var_23_9 >= 1:
				local var_23_19 = var_23_2[var_23_3]

				arg_23_0.tweenValue(var_23_13, var_23_13.value, 1, var_23_0, None, function(arg_25_0)
					arg_23_0.setSliderValue(var_23_13, arg_25_0), function()
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_BREAK_OUT_FULL)

					var_23_19 = var_23_19 + 1

					var_23_18(var_23_19, var_23_1[var_23_3] - var_23_19)

					local var_26_0 = var_23_1[var_23_3] - var_23_19

					if var_26_0 > 0:
						arg_23_0.tweenValue(var_23_13, 0, 1, var_23_0, None, function(arg_27_0)
							arg_23_0.setSliderValue(var_23_13, arg_27_0), function()
							pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_BREAK_OUT_FULL)

							var_23_19 = var_23_19 + 1

							var_23_18(var_23_19, var_23_1[var_23_3] - var_23_19)

							if var_23_19 == var_23_1[var_23_3]:
								arg_23_0.tweenValue(var_23_13, 0, var_23_15 / var_23_10, var_23_0, None, function(arg_29_0)
									arg_23_0.setSliderValue(var_23_13, arg_29_0), function()
									if var_23_5 == var_23_1[var_23_3]:
										arg_23_0.setSliderValue(var_23_13, 1)
										setText(var_23_17, "MAX")), var_26_0)
					else
						arg_23_0.tweenValue(var_23_13, 0, var_23_15 / var_23_10, var_23_0, None, function(arg_31_0)
							arg_23_0.setSliderValue(var_23_13, arg_31_0), function()
							if var_23_5 == var_23_1[var_23_3]:
								arg_23_0.setSliderValue(var_23_13, 1)
								setText(var_23_17, "MAX")))
			else
				arg_23_0.tweenValue(var_23_13, var_23_13.value, var_23_15 / var_23_10, var_23_0, None, function(arg_33_0)
					arg_23_0.setSliderValue(var_23_13, arg_33_0), function()
					if var_23_5 == var_23_1[var_23_3]:
						arg_23_0.setSliderValue(var_23_13, 1)
						setText(var_23_17, "MAX"))

def var_0_0.tweenValue(arg_35_0, arg_35_1, arg_35_2, arg_35_3, arg_35_4, arg_35_5, arg_35_6, arg_35_7, arg_35_8):
	assert(not arg_35_0.exited, "tween after ui exited")

	if not arg_35_0.tweens:
		return

	arg_35_0.tweens[arg_35_1] = arg_35_1

	LeanTween.cancel(go(arg_35_1))

	local var_35_0 = LeanTween.value(go(arg_35_1), arg_35_2, arg_35_3, arg_35_4).setOnUpdate(System.Action_float(function(arg_36_0)
		if arg_35_6:
			arg_35_6(arg_36_0))).setDelay(arg_35_5 or 0).setOnComplete(System.Action(function()
		if arg_35_7:
			arg_35_7()))

	if arg_35_8 and arg_35_8 > 0:
		var_35_0.setRepeat(arg_35_8)

def var_0_0.getBuffExp():
	local var_38_0 = BuffHelper.GetShipModExpBuff()
	local var_38_1 = 0

	for iter_38_0, iter_38_1 in ipairs(var_38_0):
		var_38_1 = math.max(iter_38_1 and iter_38_1.getConfig("benefit_effect") / 100 or 0, var_38_1)

	return var_38_1

def var_0_0.getModExpAdditions(arg_39_0, arg_39_1):
	local var_39_0 = pg.ship_data_template
	local var_39_1 = var_39_0[arg_39_0.configId].group_type
	local var_39_2 = pg.ship_data_strengthen
	local var_39_3 = {}
	local var_39_4 = var_0_0.getBuffExp()

	for iter_39_0, iter_39_1 in pairs(ShipModAttr.ID_TO_ATTR):
		local var_39_5 = 0

		if iter_39_0 != ShipModLayer.IGNORE_ID:
			for iter_39_2, iter_39_3 in pairs(arg_39_1):
				local var_39_6 = var_39_0[iter_39_3.configId]
				local var_39_7 = var_39_6.strengthen_id

				assert(var_39_2[var_39_7], "ship_data_strengthen>>" .. var_39_7)

				local var_39_8 = var_39_2[var_39_7].attr_exp[iter_39_0 - 1]

				if var_39_6.group_type == var_39_1:
					var_39_8 = var_39_8 * 2

				var_39_5 = var_39_5 + var_39_8

		var_39_3[iter_39_1] = math.floor(var_39_5 * (1 + var_39_4))

	return var_39_3

def var_0_0.getMaterialShips(arg_40_0, arg_40_1):
	local var_40_0 = {}

	for iter_40_0, iter_40_1 in ipairs(arg_40_1 or {}):
		table.insert(var_40_0, arg_40_0.shipVOs[iter_40_1])

	return var_40_0

def var_0_0.getExpAddition(arg_41_0, arg_41_1, arg_41_2):
	local var_41_0 = var_0_0.getModExpAdditions(arg_41_0, arg_41_1)

	if arg_41_0.getModAttrTopLimit(arg_41_2) == 0:
		return 0, 0
	else
		local var_41_1 = Clone(arg_41_0)

		var_41_1.addModAttrExp(arg_41_2, var_41_0[arg_41_2])

		return var_41_1.getModProperties(arg_41_2) - arg_41_0.getModProperties(arg_41_2)

def var_0_0.getRemainExp(arg_42_0, arg_42_1):
	local var_42_0 = math.max(arg_42_0.getModExpRatio(arg_42_1), 1)

	return arg_42_0.getModProperties(arg_42_1) % var_42_0

def var_0_0.setSliderValue(arg_43_0, arg_43_1, arg_43_2):
	arg_43_1.value = arg_43_2 == 0 and arg_43_2 or math.max(arg_43_2, 0.08)

def var_0_0.willExit(arg_44_0):
	arg_44_0.blurPanel(False)

	for iter_44_0, iter_44_1 in pairs(arg_44_0.tweens or {}):
		LeanTween.cancel(go(iter_44_1))

	arg_44_0.tweens = None

def var_0_0.onBackPressed(arg_45_0):
	arg_45_0.emit(BaseUI.ON_BACK_PRESSED, True)

return var_0_0
