local var_0_0 = class("EquipCodeShareLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EquipCodeShareUI"

def var_0_0.setShipGroup(arg_2_0, arg_2_1):
	arg_2_0.shipGroup = arg_2_1
	arg_2_0.codes = arg_2_1.getEquipCodes()

	local var_2_0 = {}

	arg_2_0.firstPool = underscore(arg_2_0.codes).chain().filter(function(arg_3_0)
		return arg_3_0.new == 0 and arg_3_0.state == 0).sort(CompareFuncs({
		function(arg_4_0)
			return -arg_4_0.like
	})).first(12).each(function(arg_5_0)
		var_2_0[arg_5_0.id] = True).sort(CompareFuncs({
		function(arg_6_0)
			return -arg_6_0.evaPoint
	})).value()
	arg_2_0.oldPool = underscore.filter(arg_2_0.codes, function(arg_7_0)
		return arg_7_0.new == 0 and not var_2_0[arg_7_0.id])
	arg_2_0.newPool = underscore.filter(arg_2_0.codes, function(arg_8_0)
		return arg_8_0.new == 1)

local function var_0_1(arg_9_0, arg_9_1, arg_9_2)
	setActive(arg_9_0.Find("IconTpl"), tobool(arg_9_1))

	if not arg_9_1:
		return

	updateEquipment(arg_9_0.Find("IconTpl"), arg_9_1)

	if not arg_9_0.Find("IconTpl/icon_bg/equip_flag"):
		return

	setActive(arg_9_0.Find("IconTpl/icon_bg/equip_flag"), arg_9_2)

	if not arg_9_2:
		return

	setImageSprite(arg_9_0.Find("IconTpl/icon_bg/equip_flag/Image"), LoadSprite("qicon/" .. arg_9_2.getPainting()))

local function var_0_2(arg_10_0, arg_10_1, arg_10_2)
	setActive(arg_10_0.Find("Icon"), arg_10_1)
	setActive(arg_10_0.Find("IconShadow"), arg_10_1)

	if not arg_10_1:
		return

	UpdateSpWeaponSlot(arg_10_0, arg_10_1)

	if not arg_10_0.Find("Icon/equip_flag"):
		return

	setActive(arg_10_0.Find("Icon/equip_flag"), arg_10_2)

	if not arg_10_2:
		return

	setImageSprite(arg_10_0.Find("Icon/equip_flag/Image"), LoadSprite("qicon/" .. arg_10_2.getPainting()))

local var_0_3 = {
	customPanels = {
		minHeight = 650,
		labelIndex = {
			mode = CustomIndexLayer.Mode.AND,
			options = IndexConst.ECodeLabelIndexs,
			names = IndexConst.ECodeLabelNames
		}
	},
	groupList = {
		{
			dropdown = False,
			titleTxt = "indexsort_label",
			titleENTxt = "indexsort_labeleng",
			tags = {
				"labelIndex"
			}
		}
	}
}

def var_0_0.init(arg_11_0):
	onButton(arg_11_0, arg_11_0._tf.Find("BG"), function()
		arg_11_0.closeView(), SFX_CANCEL)

	arg_11_0.rtMainPanel = arg_11_0._tf.Find("mainPanel")

	onButton(arg_11_0, arg_11_0.rtMainPanel.Find("top_panel/btnBack"), function()
		arg_11_0.closeView(), SFX_CANCEL)

	arg_11_0.indexData = arg_11_0.indexData or {}

	local var_11_0 = arg_11_0.rtMainPanel.Find("top_panel/btn_filter")

	onButton(arg_11_0, var_11_0, function()
		arg_11_0.emit(EquipCodeShareMediator.OPEN_TAG_INDEX, setmetatable({
			indexDatas = Clone(arg_11_0.indexData),
			def callback:(arg_15_0)
				arg_11_0.indexData.labelIndex = arg_15_0.labelIndex

				local var_15_0 = arg_11_0.isDefaultFilter()

				setImageAlpha(var_11_0, var_15_0 and 1 or 0)
				setActive(var_11_0.Find("on"), not var_15_0)

				arg_11_0.refreshCount = 0

				arg_11_0.refreshCodes()
		}, {
			__index = var_0_3
		})), SFX_PANEL)

	arg_11_0.rtShipCard = arg_11_0.rtMainPanel.Find("left_panel/ship_tpl")

	onButton(arg_11_0, arg_11_0.rtMainPanel.Find("left_panel/btn_refresh"), function()
		arg_11_0.refreshCodes(), SFX_PANEL)

	local var_11_1 = arg_11_0.rtMainPanel.Find("right_panel/content/container")

	arg_11_0.itemList = UIItemList.New(var_11_1, var_11_1.Find("tpl"))

	local var_11_2 = pg.equip_data_template
	local var_11_3 = pg.spweapon_data_statistics

	arg_11_0.itemList.make(function(arg_17_0, arg_17_1, arg_17_2)
		arg_17_1 = arg_17_1 + 1

		if arg_17_0 == UIItemList.EventUpdate:
			local var_17_0 = arg_11_0.filterCodes[arg_17_1]
			local var_17_1 = {}
			local var_17_2
			local var_17_3
			local var_17_4, var_17_5

			var_17_4, var_17_5, var_17_1[1], var_17_1[2] = unpack(string.split(var_17_0.str, "&"))

			for iter_17_0, iter_17_1 in ipairs(parseEquipCode(var_17_4)):
				if iter_17_0 == 6:
					var_0_2(arg_17_2.Find("left/equipments/SpSlot"), var_11_3[iter_17_1] and SpWeapon.New({
						id = iter_17_1
					}) or False)
				else
					var_0_1(arg_17_2.Find("left/equipments").GetChild(iter_17_0 - 1), var_11_2[iter_17_1] and Equipment.New({
						id = iter_17_1
					}) or False)

			for iter_17_2, iter_17_3 in ipairs(var_17_1):
				setText(arg_17_2.Find("left/tags/" .. iter_17_2 .. "/Text"), i18n("equip_share_label_" .. iter_17_3))

			setText(arg_17_2.Find("right/like/Text"), var_17_0.like)
			onButton(arg_11_0, arg_17_2.Find("right/like/btn_like"), function()
				if var_17_0.afterLike:
					pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_like_limited"))
				else
					function arg_11_0.successCallback()
						arg_11_0.successCallback = None

						setText(arg_17_2.Find("right/like/Text"), var_17_0.like)

					arg_11_0.emit(EquipCodeShareMediator.LIKE_EQUIP_CODE, arg_11_0.shipGroup.id, var_17_0.id), SFX_PANEL)
			onButton(arg_11_0, arg_17_2.Find("right/like/btn_impeach"), function()
				arg_11_0.impeachCodeId = var_17_0.id

				setActive(arg_11_0.rtMainPanel, False)
				setActive(arg_11_0.impackPanel, True)
				triggerToggle(arg_11_0.impackPanel.Find("window/msg_panel/content/options/tpl"), True), SFX_PANEL)
			onButton(arg_11_0, arg_17_2.Find("right/btn_copy"), function()
				UniPasteBoard.SetClipBoardString(var_17_4)
				pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_export_success")), SFX_CONFIRM))
	setText(arg_11_0.rtMainPanel.Find("right_panel/content/nothing/Text_2"), i18n("equipcode_share_listempty"))
	setText(arg_11_0.rtMainPanel.Find("top_panel/title/name"), i18n("equipcode_share_title"))
	setText(arg_11_0.rtMainPanel.Find("top_panel/title/name/name_en"), i18n("equipcode_share_titleeng"))
	arg_11_0.initImpeachPanel()
	pg.UIMgr.GetInstance().BlurPanel(arg_11_0._tf, False, {
		groupName = arg_11_0.getGroupNameFromData(),
		weight = arg_11_0.getWeightFromData()
	})

def var_0_0.refreshLikeCommand(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = underscore.detect(arg_22_0.codes, function(arg_23_0)
		return arg_23_0.id == arg_22_1)

	var_22_0.afterLike = True
	var_22_0.like = var_22_0.like + (arg_22_2 and 1 or 0)

	existCall(arg_22_0.successCallback)

def var_0_0.initImpeachPanel(arg_24_0):
	arg_24_0.impackPanel = arg_24_0._tf.Find("impeachPanel")

	setText(arg_24_0.impackPanel.Find("window/top/bg/impeach/title"), i18n("report_sent_title"))
	onButton(arg_24_0, arg_24_0.impackPanel.Find("window/top/btnBack"), function()
		arg_24_0.onBackPressed(), SFX_CANCEL)

	local var_24_0 = {
		{
			"equipcode_report_type_1",
			"equipcode_report_type_1"
		},
		{
			"equipcode_report_type_2",
			"equipcode_report_type_2"
		}
	}
	local var_24_1 = arg_24_0.impackPanel.Find("window/msg_panel/content")

	setText(var_24_1.Find("title"), i18n("report_sent_desc"))

	local var_24_2 = UIItemList.New(var_24_1.Find("options"), var_24_1.Find("options/tpl"))

	var_24_2.make(function(arg_26_0, arg_26_1, arg_26_2)
		arg_26_1 = arg_26_1 + 1

		if arg_26_0 == UIItemList.EventUpdate:
			local var_26_0 = var_24_0[arg_26_1]

			setText(arg_26_2.Find("Text"), i18n(var_26_0[1]))
			setText(arg_26_2.Find("Text_2"), i18n(var_26_0[2]))
			onToggle(arg_24_0, arg_26_2, function(arg_27_0)
				arg_24_0.impeachOption = arg_26_1))
	var_24_2.align(#var_24_0)

	local var_24_3 = var_24_1.Find("other/field/input")

	onButton(arg_24_0, arg_24_0.impackPanel.Find("window/button_container/button"), function()
		arg_24_0.emit(EquipCodeShareMediator.IMPEACH_EQUIP_CODE, arg_24_0.shipGroup.id, arg_24_0.impeachCodeId, arg_24_0.impeachOption)
		arg_24_0.onBackPressed(), SFX_CONFIRM)

def var_0_0.onBackPressed(arg_29_0):
	if isActive(arg_29_0.impackPanel):
		setActive(arg_29_0.rtMainPanel, True)
		setActive(arg_29_0.impackPanel, False)

		return

	arg_29_0.closeView()

def var_0_0.didEnter(arg_30_0):
	arg_30_0.flushShip()

	arg_30_0.refreshCount = 0

	arg_30_0.refreshCodes()

def var_0_0.flushShip(arg_31_0):
	arg_31_0.head = arg_31_0.rtMainPanel.Find("left_panel/ship_tpl")
	arg_31_0.iconType = arg_31_0.head.Find("content/main_bg/type_mask/type_icon").GetComponent(typeof(Image))
	arg_31_0.imageBg = arg_31_0.head.Find("content/icon_bg").GetComponent(typeof(Image))
	arg_31_0.imageFrame = arg_31_0.head.Find("content/main_bg/frame")
	arg_31_0.iconShip = arg_31_0.head.Find("content/icon").GetComponent(typeof(Image))
	arg_31_0.labelName = arg_31_0.head.Find("content/main_bg/name_mask/name").GetComponent(typeof(Text))
	arg_31_0.scrollText = arg_31_0.head.Find("content/main_bg/name_mask/name").GetComponent(typeof(ScrollText))
	arg_31_0.stars = arg_31_0.head.Find("content/main_bg/stars")
	arg_31_0.star = arg_31_0.stars.Find("tpl")

	local var_31_0 = arg_31_0.shipGroup.shipConfig
	local var_31_1 = arg_31_0.shipGroup.getPainting(arg_31_0.showTrans)
	local var_31_2 = arg_31_0.shipGroup.rarity2bgPrint(arg_31_0.showTrans)

	setShipCardFrame(arg_31_0.imageFrame, var_31_2, None)
	GetImageSpriteFromAtlasAsync("bg/star_level_card_" .. var_31_2, "", arg_31_0.imageBg)

	arg_31_0.iconShip.sprite = GetSpriteFromAtlas("shipYardIcon/unknown", "")

	LoadImageSpriteAsync("shipYardIcon/" .. var_31_1, arg_31_0.iconShip)

	arg_31_0.labelName.text = arg_31_0.shipGroup.getName(arg_31_0.showTrans)

	if arg_31_0.scrollText:
		arg_31_0.scrollText.SetText(arg_31_0.shipGroup.getName(arg_31_0.showTrans))

	local var_31_3 = GetSpriteFromAtlas("shiptype", shipType2print(arg_31_0.shipGroup.getShipType(arg_31_0.showTrans)))

	if not var_31_3:
		warning("找不到船形, shipConfigId. " .. var_31_0.id)

	arg_31_0.iconType.sprite = var_31_3

	local var_31_4 = pg.ship_data_template[var_31_0.id].star_max

	for iter_31_0 = arg_31_0.stars.childCount, var_31_4 - 1:
		local var_31_5 = cloneTplTo(arg_31_0.star, arg_31_0.stars)

def var_0_0.isDefaultFilter(arg_32_0):
	return underscore(arg_32_0.indexData).chain().keys().all(function(arg_33_0)
		return arg_32_0.indexData[arg_33_0] == var_0_3.customPanels[arg_33_0].options[1]).value()

def var_0_0.codesFilter(arg_34_0, arg_34_1):
	return underscore.filter(arg_34_1, function(arg_35_0)
		return IndexConst.filterEquipCodeByLable(arg_35_0, arg_34_0.indexData.labelIndex))

def var_0_0.refreshCodes(arg_36_0):
	arg_36_0.refreshCount = arg_36_0.refreshCount + 1
	arg_36_0.filterCodes = {}

	if arg_36_0.refreshCount > 4 or not arg_36_0.isDefaultFilter():
		local var_36_0 = arg_36_0.codesFilter(arg_36_0.codes)

		if #var_36_0 > 4:
			for iter_36_0 = 1, 4:
				local var_36_1 = math.random(#var_36_0)

				table.insert(arg_36_0.filterCodes, var_36_0[var_36_1])
				table.remove(var_36_0, var_36_1)
		else
			arg_36_0.filterCodes = var_36_0

		table.sort(arg_36_0.filterCodes, CompareFuncs({
			function(arg_37_0)
				return -arg_37_0.like
		}, False))
	else
		if #arg_36_0.firstPool < 3:
			arg_36_0.filterCodes = underscore.rest(arg_36_0.firstPool, 1)
		elif #arg_36_0.firstPool < arg_36_0.refreshCount * 3:
			local var_36_2 = underscore.rest(arg_36_0.firstPool, 1)

			for iter_36_1 = 1, 3:
				local var_36_3 = math.random(#var_36_2)

				table.insert(arg_36_0.filterCodes, var_36_2[var_36_3])
				table.remove(var_36_2, var_36_3)
		else
			arg_36_0.filterCodes = underscore.slice(arg_36_0.firstPool, (arg_36_0.refreshCount - 1) * 3 + 1, 3)

		local var_36_4 = {
			underscore.rest(arg_36_0.newPool, 1),
			underscore.rest(arg_36_0.oldPool, 1),
			underscore.filter(arg_36_0.firstPool, function(arg_38_0)
				return underscore.all(arg_36_0.filterCodes, function(arg_39_0)
					return arg_39_0.id != arg_38_0.id))
		}
		local var_36_5

		while #arg_36_0.filterCodes < 4:
			if var_36_5 and #var_36_5 > 0:
				local var_36_6 = math.random(#var_36_5)

				table.insert(arg_36_0.filterCodes, var_36_5[var_36_6])
				table.remove(var_36_5, var_36_6)
			elif #var_36_4 > 0:
				var_36_5 = table.remove(var_36_4, 1)
			else
				break

	arg_36_0.itemList.align(#arg_36_0.filterCodes)
	setActive(arg_36_0.rtMainPanel.Find("right_panel/content/nothing"), #arg_36_0.filterCodes == 0)

def var_0_0.willExit(arg_40_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_40_0._tf)

return var_0_0
