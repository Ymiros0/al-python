local var_0_0 = class("EducateScheduleFilterLayer", import(".base.EducateBaseUI"))

local function var_0_1(arg_1_0)
	local var_1_0 = Clone(arg_1_0)

	table.remove(var_1_0, 1)

	return var_1_0

var_0_0.FILTER_CONFIG = {
	{
		tag = "typeIndex",
		dropdown = False,
		title = i18n("child_filter_type1"),
		options = var_0_1(EducatePlanIndexConst.TypeIndexs),
		names = var_0_1(EducatePlanIndexConst.TypeNames),
		default = EducatePlanIndexConst.TypeAll
	},
	{
		dropdown = True,
		title = i18n("child_filter_type2"),
		options = {
			EducatePlanIndexConst.AwardResIndexs,
			EducatePlanIndexConst.AwardNatureIndexs,
			EducatePlanIndexConst.AwardAttr1Indexs,
			EducatePlanIndexConst.AwardAttr2Indexs
		},
		names = {
			EducatePlanIndexConst.AwardResNames,
			EducatePlanIndexConst.AwardNatureNames,
			EducatePlanIndexConst.AwardAttr1Names,
			EducatePlanIndexConst.AwardAttr2Names
		},
		tags = {
			"awardResIndex",
			"awardNatureIndex",
			"awardAttr1Index",
			"awardAttr2Index"
		},
		defaults = {
			EducatePlanIndexConst.AwardResAll,
			EducatePlanIndexConst.AwardNatureAll,
			EducatePlanIndexConst.AwardAttr1All,
			EducatePlanIndexConst.AwardAttr2All
		}
	},
	{
		tag = "costIndex",
		dropdown = False,
		title = i18n("child_filter_type3"),
		options = var_0_1(EducatePlanIndexConst.CostIndexs),
		names = var_0_1(EducatePlanIndexConst.CostNames),
		default = EducatePlanIndexConst.CostAll
	}
}

def var_0_0.getUIName(arg_2_0):
	return "EducateScheduleIndexUI"

def var_0_0.init(arg_3_0):
	arg_3_0.anim = arg_3_0.findTF("anim_root").GetComponent(typeof(Animation))
	arg_3_0.animEvent = arg_3_0.findTF("anim_root").GetComponent(typeof(DftAniEvent))

	arg_3_0.animEvent.SetEndEvent(function()
		arg_3_0.emit(var_0_0.ON_CLOSE))

	arg_3_0.windowTF = arg_3_0.findTF("anim_root/window")

	setText(arg_3_0.findTF("top/title", arg_3_0.windowTF), i18n("child_filter_title"))

	arg_3_0.filterContainer = arg_3_0.findTF("frame/filter_content", arg_3_0.windowTF)
	arg_3_0.filterTpl = arg_3_0.findTF("anim_root/filter_tpl")
	arg_3_0.itemTpl = arg_3_0.findTF("anim_root/item_tpl")

	setActive(arg_3_0.filterTpl, False)
	setActive(arg_3_0.itemTpl, False)

	arg_3_0.dropdownPanel = arg_3_0.findTF("anim_root/dropdown_panel")
	arg_3_0.dropdownUIList = UIItemList.New(arg_3_0.findTF("dropdown/list", arg_3_0.dropdownPanel), arg_3_0.findTF("dropdown/list/tpl", arg_3_0.dropdownPanel))

	setActive(arg_3_0.dropdownPanel, False)
	setText(arg_3_0.findTF("sure_btn/Text", arg_3_0.windowTF), i18n("word_ok"))
	setText(arg_3_0.findTF("reset_btn/Text", arg_3_0.windowTF), i18n("word_reset"))

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0.findTF("sure_btn", arg_5_0.windowTF), function()
		if arg_5_0.contextData.callback:
			arg_5_0.contextData.callback(arg_5_0.contextData.indexDatas)

			arg_5_0.contextData.callback = None

		arg_5_0._close(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("reset_btn", arg_5_0.windowTF), function()
		arg_5_0.contextData.indexDatas = None

		removeAllChildren(arg_5_0.filterContainer)
		arg_5_0.initFilters(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.dropdownPanel, function()
		arg_5_0.closeDropdownPanel(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("anim_root/bg"), function()
		arg_5_0._close(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("top/close_btn", arg_5_0.windowTF), function()
		arg_5_0._close(), SFX_PANEL)
	arg_5_0.initDropdownPanel()
	arg_5_0.initFilters()
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0._tf, {
		groupName = LayerWeightConst.GROUP_EDUCATE,
		weight = LayerWeightConst.BASE_LAYER + 1
	})

def var_0_0.initDropdownPanel(arg_11_0):
	arg_11_0.dropdownUIList.make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate:
			local var_12_0 = arg_12_1 + 1 + 1
			local var_12_1 = arg_11_0.dropdownCfg.names[arg_11_0.dropdownCfgIndex][var_12_0]
			local var_12_2 = arg_11_0.dropdownCfg.options[arg_11_0.dropdownCfgIndex][var_12_0]
			local var_12_3 = arg_11_0.dropdownCfg.tags[arg_11_0.dropdownCfgIndex]
			local var_12_4 = arg_11_0.dropdownCfg.defaults[arg_11_0.dropdownCfgIndex]

			setActive(arg_11_0.findTF("line", arg_12_2), var_12_0 != #arg_11_0.dropdownCfg.options[arg_11_0.dropdownCfgIndex])
			setText(arg_11_0.findTF("Text", arg_12_2), var_12_1)
			onButton(arg_11_0, arg_12_2, function()
				if arg_11_0.contextData.indexDatas[var_12_3] == var_12_2:
					arg_11_0.contextData.indexDatas[var_12_3] = var_12_4
				else
					arg_11_0.contextData.indexDatas[var_12_3] = var_12_2

				arg_11_0.closeDropdownPanel()
				arg_11_0.uiList[arg_11_0.updateListIndex].align(#arg_11_0.dropdownCfg.options), SFX_PANEL))

def var_0_0.initFilters(arg_14_0):
	arg_14_0.contextData.indexDatas = arg_14_0.contextData.indexDatas or {}
	arg_14_0.uiList = {}

	for iter_14_0, iter_14_1 in ipairs(var_0_0.FILTER_CONFIG):
		local var_14_0 = cloneTplTo(arg_14_0.filterTpl, arg_14_0.filterContainer)

		setText(arg_14_0.findTF("title/title", var_14_0), iter_14_1.title)

		if not iter_14_1.dropdown:
			arg_14_0.initNormal(iter_14_0, iter_14_1, var_14_0)
		else
			arg_14_0.initDropdown(iter_14_0, iter_14_1, var_14_0)

def var_0_0.initNormal(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	local var_15_0 = arg_15_0.findTF("content/container", arg_15_3)
	local var_15_1 = UIItemList.New(var_15_0, arg_15_0.itemTpl)

	var_15_1.make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventInit:
			local var_16_0 = arg_16_1 + 1
			local var_16_1 = arg_15_2.names[var_16_0]
			local var_16_2 = arg_15_2.options[var_16_0]

			setText(arg_15_0.findTF("Text", arg_16_2), var_16_1)
			setActive(arg_15_0.findTF("line", arg_16_2), var_16_0 != #arg_15_2.names)
			setActive(arg_15_0.findTF("arrow", arg_16_2), False)

			if not arg_15_0.contextData.indexDatas[arg_15_2.tag]:
				arg_15_0.contextData.indexDatas[arg_15_2.tag] = arg_15_2.default

			onButton(arg_15_0, arg_16_2, function()
				if arg_15_0.contextData.indexDatas[arg_15_2.tag] == arg_15_2.default:
					arg_15_0.contextData.indexDatas[arg_15_2.tag] = var_16_2
				else
					arg_15_0.contextData.indexDatas[arg_15_2.tag] = bit.bxor(arg_15_0.contextData.indexDatas[arg_15_2.tag], var_16_2)

				if arg_15_0.contextData.indexDatas[arg_15_2.tag] == 0:
					arg_15_0.contextData.indexDatas[arg_15_2.tag] = arg_15_2.default

				var_15_1.align(#arg_15_2.options), SFX_PANEL)
		elif arg_16_0 == UIItemList.EventUpdate:
			local var_16_3 = arg_16_1 + 1
			local var_16_4 = arg_15_2.options[var_16_3]
			local var_16_5
			local var_16_6 = (arg_15_0.contextData.indexDatas[arg_15_2.tag] != arg_15_2.default or False) and bit.band(arg_15_0.contextData.indexDatas[arg_15_2.tag], var_16_4) > 0

			setActive(arg_15_0.findTF("selected", arg_16_2), var_16_6)
			setTextColor(arg_15_0.findTF("Text", arg_16_2), var_16_6 and Color.white or Color.NewHex("393a3c")))
	var_15_1.align(#arg_15_2.options)

	arg_15_0.uiList[arg_15_1] = var_15_1

def var_0_0.initDropdown(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = arg_18_0.findTF("content/container", arg_18_3)
	local var_18_1 = UIItemList.New(var_18_0, arg_18_0.itemTpl)

	var_18_1.make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventInit:
			local var_19_0 = arg_19_1 + 1
			local var_19_1 = arg_18_2.tags[var_19_0]
			local var_19_2 = arg_18_2.defaults[var_19_0]

			setActive(arg_18_0.findTF("line", arg_19_2), var_19_0 != #arg_18_2.tags)
			setActive(arg_18_0.findTF("arrow", arg_19_2), True)

			if not arg_18_0.contextData.indexDatas[var_19_1]:
				arg_18_0.contextData.indexDatas[var_19_1] = var_19_2

			onButton(arg_18_0, arg_19_2, function()
				arg_18_0.dropdownCfg = arg_18_2
				arg_18_0.dropdownCfgIndex = var_19_0
				arg_18_0.updateListIndex = arg_18_1

				local var_20_0 = arg_18_0._tf.InverseTransformPoint(arg_19_2.position)

				arg_18_0.showDropdownPanel(var_20_0), SFX_PANEL)
		elif arg_19_0 == UIItemList.EventUpdate:
			local var_19_3 = arg_19_1 + 1
			local var_19_4 = arg_18_2.tags[var_19_3]
			local var_19_5 = arg_18_2.defaults[var_19_3]
			local var_19_6 = ""
			local var_19_7 = True

			if arg_18_0.contextData.indexDatas[var_19_4] == var_19_5:
				var_19_7 = False
				var_19_6 = arg_18_2.names[var_19_3][1]
			else
				local var_19_8 = arg_18_2.options[var_19_3]

				for iter_19_0, iter_19_1 in ipairs(var_19_8):
					if arg_18_0.contextData.indexDatas[var_19_4] == iter_19_1:
						var_19_6 = arg_18_2.names[var_19_3][iter_19_0]

						break

			setText(arg_18_0.findTF("Text", arg_19_2), var_19_6)
			setActive(arg_18_0.findTF("selected", arg_19_2), var_19_7)
			setTextColor(arg_18_0.findTF("Text", arg_19_2), var_19_7 and Color.white or Color.NewHex("393a3c"))
			setImageColor(arg_18_0.findTF("arrow", arg_19_2), var_19_7 and Color.white or Color.NewHex("393a3c")))
	var_18_1.align(#arg_18_2.options)

	arg_18_0.uiList[arg_18_1] = var_18_1

def var_0_0.showDropdownPanel(arg_21_0, arg_21_1):
	setAnchoredPosition(arg_21_0.findTF("dropdown", arg_21_0.dropdownPanel), arg_21_1)
	setActive(arg_21_0.dropdownPanel, True)
	arg_21_0.dropdownUIList.align(#arg_21_0.dropdownCfg.options[arg_21_0.dropdownCfgIndex] - 1)

def var_0_0.closeDropdownPanel(arg_22_0):
	setActive(arg_22_0.dropdownPanel, False)

def var_0_0._close(arg_23_0):
	arg_23_0.anim.Play("anim_educate_scheduleindex_out")

def var_0_0.onBackPressed(arg_24_0):
	arg_24_0._close()

def var_0_0.willExit(arg_25_0):
	arg_25_0.animEvent.SetEndEvent(None)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_25_0._tf)

return var_0_0
