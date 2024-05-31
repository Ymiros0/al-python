local var_0_0 = class("AssignedItemPanel")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)
	arg_1_0.isInited = False
	arg_1_0.selectedVO = None
	arg_1_0.count = 1
	arg_1_0.view = arg_1_2

def var_0_0.findTF(arg_2_0, arg_2_1):
	return findTF(arg_2_0._tf, arg_2_1)

def var_0_0.show(arg_3_0):
	setActive(arg_3_0._tf, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf)

def var_0_0.hide(arg_4_0):
	setActive(arg_4_0._tf, False)

	arg_4_0.selectedVO = None
	arg_4_0.itemVO = None
	arg_4_0.count = 1

	pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf, arg_4_0.view._tf)

	if arg_4_0.selectedItem:
		triggerToggle(arg_4_0.selectedItem, False)

	arg_4_0.selectedItem = None

def var_0_0.init(arg_5_0):
	arg_5_0.isInited = True
	arg_5_0.ulist = UIItemList.New(arg_5_0.findTF("got/bottom/scroll/list"), arg_5_0.findTF("got/bottom/scroll/list/tpl"))
	arg_5_0.confirmBtn = arg_5_0.findTF("calc/confirm")
	arg_5_0.rightArr = arg_5_0.findTF("calc/value_bg/add")
	arg_5_0.leftArr = arg_5_0.findTF("calc/value_bg/mius")
	arg_5_0.maxBtn = arg_5_0.findTF("calc/max")
	arg_5_0.valueText = arg_5_0.findTF("calc/value_bg/Text")
	arg_5_0.itemTF = arg_5_0.findTF("item/bottom/item")
	arg_5_0.nameTF = arg_5_0.findTF("item/bottom/name_bg/name")
	arg_5_0.descTF = arg_5_0.findTF("item/bottom/desc")

	onButton(arg_5_0, arg_5_0._tf, function()
		arg_5_0.hide(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.rightArr, function()
		if not arg_5_0.itemVO:
			return

		arg_5_0.count = math.min(arg_5_0.count + 1, arg_5_0.itemVO.count)

		arg_5_0.updateValue(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.leftArr, function()
		if not arg_5_0.itemVO:
			return

		arg_5_0.count = math.max(arg_5_0.count - 1, 1)

		arg_5_0.updateValue(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.maxBtn, function()
		if not arg_5_0.itemVO:
			return

		arg_5_0.count = arg_5_0.itemVO.count

		arg_5_0.updateValue(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.confirmBtn, function()
		if not arg_5_0.selectedVO or not arg_5_0.itemVO or arg_5_0.count <= 0:
			return

		arg_5_0.view.emit(EquipmentMediator.ON_USE_ITEM, arg_5_0.itemVO.id, arg_5_0.count, arg_5_0.selectedVO)
		arg_5_0.hide(), SFX_PANEL)

def var_0_0.updateValue(arg_11_0):
	setText(arg_11_0.valueText, arg_11_0.count)
	arg_11_0.ulist.each(function(arg_12_0, arg_12_1)
		setText(arg_12_1.Find("item/bg/icon_bg/count"), arg_11_0.count))

def var_0_0.update(arg_13_0, arg_13_1):
	arg_13_0.itemVO = arg_13_1

	if not arg_13_0.isInited:
		arg_13_0.init()

	local var_13_0 = arg_13_1.getConfig("display_icon")

	arg_13_0.selectedItem = None

	arg_13_0.ulist.make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate:
			local var_14_0 = var_13_0[arg_14_1 + 1]
			local var_14_1 = {
				type = var_14_0[1],
				id = var_14_0[2],
				count = var_14_0[3]
			}

			updateDrop(arg_14_2.Find("item/bg"), var_14_1)

			local var_14_2 = arg_14_2.Find("item/bg/icon_bg/count")

			onToggle(arg_13_0, arg_14_2, function(arg_15_0)
				if arg_15_0:
					arg_13_0.selectedVO = arg_13_1.getConfig("usage_arg")[arg_14_1 + 1]

					setText(var_14_2, arg_13_0.count * var_14_0[3])

					arg_13_0.selectedItem = arg_14_2, SFX_PANEL)
			setScrollText(arg_14_2.Find("name_bg/Text"), var_14_1.getConfig("name")))
	arg_13_0.ulist.align(#var_13_0)
	arg_13_0.updateValue()
	updateDrop(arg_13_0.itemTF.Find("bg"), {
		type = DROP_TYPE_ITEM,
		id = arg_13_1.id,
		count = arg_13_1.count
	})
	setText(arg_13_0.nameTF, arg_13_1.getConfig("name"))
	setText(arg_13_0.descTF, arg_13_1.getConfig("display"))

def var_0_0.dispose(arg_16_0):
	pg.DelegateInfo.Dispose(arg_16_0)

return var_0_0
