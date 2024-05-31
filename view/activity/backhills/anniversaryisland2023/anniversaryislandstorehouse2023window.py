local var_0_0 = class("AnniversaryIslandStoreHouse2023Window", import("view.base.BaseUI"))

def var_0_0.Ctor(arg_1_0):
	var_0_0.super.Ctor(arg_1_0)

	arg_1_0.loader = AutoLoader.New()

def var_0_0.getUIName(arg_2_0):
	return "AnniversaryIslandStoreHouse2023Window"

local var_0_1 = "ui/AtelierCommonUI_atlas"

def var_0_0.preload(arg_3_0, arg_3_1):
	table.ParallelIpairsAsync({
		var_0_1
	}, function(arg_4_0, arg_4_1, arg_4_2)
		arg_3_0.loader.LoadBundle(arg_4_1, arg_4_2), arg_3_1)

def var_0_0.init(arg_5_0):
	arg_5_0.storehouseRect = arg_5_0._tf.Find("Window/ScrollView").GetComponent("LScrollRect")

	setActive(arg_5_0._tf.Find("Window/ScrollView/Item"), False)

def var_0_0.SetActivity(arg_6_0, arg_6_1):
	arg_6_0.items = arg_6_1.GetAllVitems()
	arg_6_0.itemList = {}

	table.Foreach(arg_6_0.items, function(arg_7_0, arg_7_1)
		if arg_7_1 <= 0:
			return

		table.insert(arg_6_0.itemList, WorkBenchItem.New({
			configId = arg_7_0,
			count = arg_7_1
		})))
	table.sort(arg_6_0.itemList, function(arg_8_0, arg_8_1)
		return arg_8_0.GetConfigID() < arg_8_1.GetConfigID())

def var_0_0.didEnter(arg_9_0):
	function arg_9_0.storehouseRect.onUpdateItem(arg_10_0, arg_10_1)
		arg_10_0 = arg_10_0 + 1

		local var_10_0 = tf(arg_10_1)
		local var_10_1 = arg_9_0.itemList[arg_10_0]

		arg_9_0.UpdateItem(var_10_0.Find("IconBG"), var_10_1)
		setScrollText(var_10_0.Find("NameBG/Rect/Name"), var_10_1.GetName())
		onButton(arg_9_0, var_10_0, function()
			arg_9_0.emit(WorkBenchItemDetailMediator.SHOW_DETAIL, var_10_1), SFX_PANEL)

	onButton(arg_9_0, arg_9_0._tf.Find("Window/Close"), function()
		arg_9_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_9_0, arg_9_0._tf.Find("BG"), function()
		arg_9_0.onBackPressed())
	arg_9_0.UpdateView()

def var_0_0.UpdateView(arg_14_0):
	local var_14_0 = arg_14_0.itemList

	setActive(arg_14_0._tf.Find("Window/Empty"), #var_14_0 == 0)
	setActive(arg_14_0._tf.Find("Window/ScrollView"), #var_14_0 > 0)
	arg_14_0.storehouseRect.SetTotalCount(#var_14_0)

def var_0_0.UpdateItem(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = "icon_frame_" .. arg_15_2.GetRarity()

	arg_15_0.loader.GetSpriteQuiet(var_0_1, var_15_0, arg_15_1)
	arg_15_0.loader.GetSpriteQuiet(arg_15_2.GetIconPath(), "", arg_15_1.Find("Icon"))

	if not IsNil(arg_15_1.Find("Text")):
		setText(arg_15_1.Find("Text"), arg_15_2.count)

def var_0_0.willExit(arg_16_0):
	arg_16_0.loader.Clear()

return var_0_0
