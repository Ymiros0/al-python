local var_0_0 = class("BlueprintQuickExchangeView", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "BlueprintQuickExchangeUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.rtBg = arg_2_0._tf.Find("bg")

	onButton(arg_2_0, arg_2_0.rtBg, function()
		arg_2_0.Hide(), SFX_CANCEL)

	arg_2_0.rtPreview = arg_2_0._tf.Find("window/preview/got")
	arg_2_0.rtEmpty = arg_2_0.rtPreview.Find("empty")

	setText(arg_2_0.rtEmpty.Find("Text"), i18n("blueprint_exchange_empty_tip"))

	local var_2_0 = arg_2_0.rtPreview.Find("list")

	arg_2_0.itemList = UIItemList.New(var_2_0, var_2_0.Find("item"))

	arg_2_0.itemList.make(function(arg_4_0, arg_4_1, arg_4_2)
		arg_4_1 = arg_4_1 + 1

		if arg_4_0 == UIItemList.EventUpdate:
			local var_4_0 = arg_2_0.displayList[arg_4_1]
			local var_4_1 = arg_2_0.awardList[arg_4_1].count

			updateDrop(arg_4_2.Find("icon"), var_4_0)
			onButton(arg_2_0, arg_4_2.Find("icon"), function()
				arg_2_0.emit(BaseUI.ON_DROP, var_4_0), SFX_PANEL)
			setText(arg_4_2.Find("calc/value"), arg_2_0.countList[arg_4_1])
			setScrollText(arg_4_2.Find("name/Text"), var_4_0.getConfig("name"))
			setText(arg_4_2.Find("kc"), i18n("tec_tip_material_stock") .. "." .. var_4_0.count)
			pressPersistTrigger(arg_4_2.Find("calc/plus"), 0.5, function()
				if var_4_0.count > arg_2_0.countList[arg_4_1] and arg_2_0.count + var_4_1 <= arg_2_0.need:
					arg_2_0.countList[arg_4_1] = arg_2_0.countList[arg_4_1] + 1

					setText(arg_4_2.Find("calc/value"), arg_2_0.countList[arg_4_1])

					arg_2_0.count = arg_2_0.count + var_4_1

					setText(arg_2_0.rtExchange.Find("bg/count"), setColorStr(arg_2_0.count, "#FFEC6E") .. "/" .. arg_2_0.need), None, True, True, 0.1, SFX_PANEL)
			pressPersistTrigger(arg_4_2.Find("calc/minus"), 0.5, function()
				if arg_2_0.countList[arg_4_1] > 0:
					arg_2_0.countList[arg_4_1] = arg_2_0.countList[arg_4_1] - 1

					setText(arg_4_2.Find("calc/value"), arg_2_0.countList[arg_4_1])

					arg_2_0.count = arg_2_0.count - var_4_1

					setText(arg_2_0.rtExchange.Find("bg/count"), setColorStr(arg_2_0.count, "#FFEC6E") .. "/" .. arg_2_0.need), None, True, True, 0.1, SFX_PANEL)
			onButton(arg_2_0, arg_4_2.Find("calc/max"), function()
				if var_4_0.count > arg_2_0.countList[arg_4_1] and arg_2_0.count + var_4_1 <= arg_2_0.need:
					local var_8_0 = math.floor((arg_2_0.need - arg_2_0.count + var_4_1 - 1) / var_4_1)
					local var_8_1 = math.min(var_8_0, var_4_0.count - arg_2_0.countList[arg_4_1])

					arg_2_0.countList[arg_4_1] = arg_2_0.countList[arg_4_1] + var_8_1

					setText(arg_4_2.Find("calc/value"), arg_2_0.countList[arg_4_1])

					arg_2_0.count = arg_2_0.count + var_4_1 * var_8_1

					setText(arg_2_0.rtExchange.Find("bg/count"), setColorStr(arg_2_0.count, "#FFEC6E") .. "/" .. arg_2_0.need)))
	setText(arg_2_0._tf.Find("window/cancel_button/label"), i18n("word_cancel"))
	onButton(arg_2_0, arg_2_0._tf.Find("window/cancel_button"), function()
		arg_2_0.Hide(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0._tf.Find("window/confirm_button"), function()
		if arg_2_0.count <= 0:
			return

		local var_10_0 = {}

		for iter_10_0, iter_10_1 in ipairs(arg_2_0.displayList):
			if arg_2_0.countList[iter_10_0] > 0:
				table.insert(var_10_0, {
					id = iter_10_1.id,
					count = arg_2_0.countList[iter_10_0],
					arg = Item.getConfigData(iter_10_1.id).usage_arg[arg_2_0.awardList[iter_10_0].index]
				})

		arg_2_0.emit(ShipBluePrintMediator.QUICK_EXCHAGE_BLUEPRINT, var_10_0)
		arg_2_0.Hide(), SFX_CANCEL)

	arg_2_0.rtResult = arg_2_0._tf.Find("window/result")
	arg_2_0.rtTarget = arg_2_0.rtResult.Find("target")
	arg_2_0.rtExchange = arg_2_0.rtResult.Find("exchange")

	setText(arg_2_0.rtExchange.Find("bg/title"), i18n("blueprint_exchange_select_display"))

	arg_2_0.toggleSwitch = arg_2_0.rtResult.Find("switch")

	setText(arg_2_0.toggleSwitch.Find("front/Text_off"), i18n("show_design_demand_count"))
	setText(arg_2_0.toggleSwitch.Find("front/Text_on"), i18n("show_fate_demand_count"))
	onToggle(arg_2_0, arg_2_0.toggleSwitch, function(arg_11_0)
		arg_2_0.isSwitch = arg_11_0

		arg_2_0.UpdateResult())

def var_0_0.Show(arg_12_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_12_0._tf)
	setActive(arg_12_0._tf, True)

def var_0_0.Hide(arg_13_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_13_0._tf, arg_13_0._parentTf)
	setActive(arg_13_0._tf, False)

def var_0_0.UpdateBlueprint(arg_14_0, arg_14_1):
	arg_14_0.blueprintVO = arg_14_1

	local var_14_0 = Drop.New({
		type = DROP_TYPE_ITEM,
		id = arg_14_1.getItemId()
	})

	changeToScrollText(arg_14_0.rtResult.Find("title/Text"), var_14_0.getName())

	arg_14_0.displayList = {}
	arg_14_0.awardList = {}

	local var_14_1 = getProxy(BagProxy)

	for iter_14_0, iter_14_1 in ipairs(pg.gameset.general_blueprint_list.description):
		local var_14_2 = var_14_1.getItemCountById(iter_14_1)

		if var_14_2 > 0:
			local var_14_3

			for iter_14_2, iter_14_3 in ipairs(Drop.New({
				type = DROP_TYPE_ITEM,
				id = iter_14_1
			}).getConfig("display_icon")):
				if iter_14_3[1] == DROP_TYPE_ITEM and iter_14_3[2] == var_14_0.id:
					var_14_3 = {
						index = iter_14_2,
						count = iter_14_3[3]
					}

			if var_14_3:
				table.insert(arg_14_0.displayList, {
					type = DROP_TYPE_ITEM,
					id = iter_14_1,
					count = var_14_2
				})
				table.insert(arg_14_0.awardList, var_14_3)

	setActive(arg_14_0.rtEmpty, #arg_14_0.displayList == 0)
	setActive(arg_14_0.itemList.container, #arg_14_0.displayList > 0)
	updateDrop(arg_14_0.rtResult.Find("target/IconTpl"), var_14_0)
	GetImageSpriteFromAtlasAsync("ui/fragresolveui_atlas", "bg_" .. ItemRarity.Rarity2Print(var_14_0.getConfig("rarity")), arg_14_0.rtResult.Find("target/bg"))

	arg_14_0.countList = underscore.map(arg_14_0.displayList, function(arg_15_0)
		return 0)
	arg_14_0.count = 0

	arg_14_0.itemList.align(#arg_14_0.displayList)
	triggerToggle(arg_14_0.toggleSwitch, arg_14_1.canFateSimulation())

def var_0_0.UpdateResult(arg_16_0):
	arg_16_0.bagProxy = arg_16_0.bagProxy or getProxy(BagProxy)
	arg_16_0.need = math.max(arg_16_0.blueprintVO.getUseageMaxItem() + (arg_16_0.isSwitch and arg_16_0.blueprintVO.getFateMaxLeftOver() or 0) - arg_16_0.bagProxy.getItemCountById(arg_16_0.blueprintVO.getItemId()), 0)

	local var_16_0 = #arg_16_0.displayList

	while var_16_0 > 0 and arg_16_0.count > arg_16_0.need:
		if arg_16_0.countList[var_16_0] > 0:
			local var_16_1 = arg_16_0.awardList[var_16_0].count
			local var_16_2 = math.floor((arg_16_0.count - arg_16_0.need + var_16_1 - 1) / var_16_1)

			if var_16_2 > arg_16_0.countList[var_16_0]:
				arg_16_0.count = arg_16_0.count - var_16_1 * arg_16_0.countList[var_16_0]
				arg_16_0.countList[var_16_0] = 0
			else
				arg_16_0.count = arg_16_0.count - var_16_1 * var_16_2
				arg_16_0.countList[var_16_0] = arg_16_0.countList[var_16_0] - var_16_2

			setText(arg_16_0.itemList.container.GetChild(var_16_0 - 1).Find("calc/value"), arg_16_0.countList[var_16_0])

		var_16_0 = var_16_0 - 1

	setText(arg_16_0.rtExchange.Find("bg/count"), setColorStr(arg_16_0.count, "#FFEC6E") .. "/" .. arg_16_0.need)

return var_0_0
