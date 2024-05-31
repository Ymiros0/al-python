local var_0_0 = class("EquipDestoryConfirmWindow", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "DestoryConfirmWindow"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.closeBtn = arg_2_0.findTF("window/top/btnBack")

	setActive(arg_2_0.findTF("window/top/bg/infomation/title_en"), PLATFORM_CODE != PLATFORM_US)
	setText(arg_2_0.findTF("window/top/bg/infomation/title"), i18n("title_info"))

	arg_2_0.cancelBtn = arg_2_0.findTF("window/cancel_btn")
	arg_2_0.confirmBtn = arg_2_0.findTF("window/confirm_btn")

	setText(findTF(arg_2_0.confirmBtn, "pic"), i18n("destroy_confirm_access"))
	setText(findTF(arg_2_0.cancelBtn, "pic"), i18n("destroy_confirm_cancel"))

	arg_2_0.title = arg_2_0.findTF("window/content/Text")
	arg_2_0.label = arg_2_0.findTF("window/content/desc/label")

	setText(arg_2_0.label, i18n("destory_ship_before_tip"))

	arg_2_0.urLabel = arg_2_0.findTF("window/content/desc/label1")
	arg_2_0.urInput = arg_2_0.findTF("window/content/desc/InputField")
	arg_2_0.urOverflowLabel = arg_2_0.findTF("window/content/desc/label2")

	setText(arg_2_0.urOverflowLabel, i18n("destory_ur_pt_overflowa"))

	local var_2_0 = arg_2_0.findTF("Placeholder", arg_2_0.urInput)

	setText(var_2_0, i18n("box_ship_del_click"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		arg_3_0.Confirm(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf.Find("bg"), function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.SetCallBack(arg_8_0, arg_8_1):
	arg_8_0.callback = arg_8_1

def var_0_0.Confirm(arg_9_0):
	if arg_9_0.key:
		local var_9_0 = getInputText(arg_9_0.urInput)

		if arg_9_0.key != tonumber(var_9_0):
			pg.TipsMgr.GetInstance().ShowTips(i18n("destory_ship_input_erro"))

			return

		local var_9_1 = arg_9_0.callback

		arg_9_0.Hide()
		existCall(var_9_1)
	else
		local var_9_2 = arg_9_0.callback

		arg_9_0.Hide()
		existCall(var_9_2)

def var_0_0.Show(arg_10_0, arg_10_1, arg_10_2):
	var_0_0.super.Show(arg_10_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_10_0._tf)

	arg_10_0.key = None
	arg_10_0.equips = arg_10_1

	arg_10_0.SetCallBack(arg_10_2)
	arg_10_0.Updatelayout()
	arg_10_0.UpdateEquips()

def var_0_0.Updatelayout(arg_11_0):
	local var_11_0 = {}

	if underscore.any(arg_11_0.equips, function(arg_12_0)
		return arg_12_0.getConfig("rarity") >= 4):
		table.insert(var_11_0, i18n("destroy_high_rarity_tip"))

	if underscore.any(arg_11_0.equips, function(arg_13_0)
		return arg_13_0.getConfig("level") > 1):
		table.insert(var_11_0, i18n("destroy_high_intensify_tip", ""))

	setText(arg_11_0.title, i18n("destroy_eliteequipment_tip", table.concat(var_11_0, ",")))

	local var_11_1 = underscore.any(arg_11_0.equips, function(arg_14_0)
		return arg_14_0.isImportance())

	if var_11_1 and not arg_11_0.key:
		arg_11_0.key = math.random(100000, 999999)

		setText(arg_11_0.urLabel, i18n("destroy_equip_rarity_tip", arg_11_0.key))
	else
		setText(arg_11_0.urLabel, "")

	setActive(arg_11_0.urOverflowLabel, False)
	setActive(arg_11_0.urLabel, var_11_1)
	setActive(arg_11_0.urInput, var_11_1)

def var_0_0.UpdateEquips(arg_15_0):
	mergeSort(arg_15_0.equips, CompareFuncs({
		function(arg_16_0)
			return -arg_16_0.getConfig("rarity"),
		function(arg_17_0)
			return -arg_17_0.getConfig("level")
	}, True))

	if #arg_15_0.equips > 5:
		setActive(arg_15_0._tf.Find("window/content/ships"), True)
		setActive(arg_15_0._tf.Find("window/content/ships_single"), False)

		local var_15_0 = arg_15_0._tf.Find("window/content/ships/content").GetComponent("LScrollRect")

		function var_15_0.onUpdateItem(arg_18_0, arg_18_1)
			updateEquipment(tf(arg_18_1), arg_15_0.equips[arg_18_0 + 1])

		onNextTick(function()
			var_15_0.SetTotalCount(#arg_15_0.equips))
	else
		local var_15_1 = arg_15_0._tf.Find("window/content/ships_single")
		local var_15_2 = UIItemList.New(var_15_1, var_15_1.Find("IconTpl"))

		setActive(arg_15_0._tf.Find("window/content/ships"), False)
		setActive(arg_15_0._tf.Find("window/content/ships_single"), True)
		var_15_2.make(function(arg_20_0, arg_20_1, arg_20_2)
			if arg_20_0 == UIItemList.EventUpdate:
				updateEquipment(arg_20_2, arg_15_0.equips[arg_20_1 + 1]))
		var_15_2.align(#arg_15_0.equips)

def var_0_0.Hide(arg_21_0):
	var_0_0.super.Hide(arg_21_0)
	pg.UIMgr.GetInstance().UnblurPanel(arg_21_0._tf, arg_21_0._parentTf)

	arg_21_0.key = None
	arg_21_0.callback = None

	setInputText(arg_21_0.urInput, "")

def var_0_0.OnDestroy(arg_22_0):
	if arg_22_0.isShowing():
		arg_22_0.Hide()

return var_0_0
