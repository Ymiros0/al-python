local var_0_0 = class("ChargeItemPanelLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "ChargeItemPanelUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()
	arg_2_0.initUIText()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updatePanel()
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0._tf)

def var_0_0.willExit(arg_4_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_4_0._tf)

def var_0_0.initData(arg_5_0):
	arg_5_0.panelConfig = arg_5_0.contextData.panelConfig

def var_0_0.initUIText(arg_6_0):
	local var_6_0 = arg_6_0.findTF("window/button_container/button_cancel/Image")
	local var_6_1 = arg_6_0.findTF("window/button_container/button_ok/Image")

	setText(var_6_0, i18n("text_cancel"))
	setText(var_6_1, i18n("text_buy"))

def var_0_0.findUI(arg_7_0):
	arg_7_0.bg = arg_7_0.findTF("back_sign")
	arg_7_0.detailWindow = arg_7_0.findTF("window")
	arg_7_0.cancelBtn = arg_7_0.findTF("button_container/button_cancel", arg_7_0.detailWindow)
	arg_7_0.confirmBtn = arg_7_0.findTF("button_container/button_ok", arg_7_0.detailWindow)
	arg_7_0.detailName = arg_7_0.findTF("goods/name", arg_7_0.detailWindow)
	arg_7_0.detailIcon = arg_7_0.findTF("goods/icon", arg_7_0.detailWindow)
	arg_7_0.detailExtraDrop = arg_7_0.findTF("goods/extra_drop", arg_7_0.detailWindow)
	arg_7_0.detailRmb = arg_7_0.findTF("prince_bg/contain/icon_rmb", arg_7_0.detailWindow)
	arg_7_0.detailGem = arg_7_0.findTF("prince_bg/contain/icon_gem", arg_7_0.detailWindow)
	arg_7_0.detailGold = arg_7_0.findTF("prince_bg/contain/icon_gold", arg_7_0.detailWindow)
	arg_7_0.detailPrice = arg_7_0.findTF("prince_bg/contain/Text", arg_7_0.detailWindow)
	arg_7_0.detailTag = arg_7_0.findTF("goods/tag", arg_7_0.detailWindow)
	arg_7_0.detailTags = {}

	table.insert(arg_7_0.detailTags, arg_7_0.findTF("hot", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0.findTF("new", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0.findTF("advice", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0.findTF("double", arg_7_0.detailTag))
	table.insert(arg_7_0.detailTags, arg_7_0.findTF("discount", arg_7_0.detailTag))

	arg_7_0.detailTagAdviceTF = arg_7_0.detailTags[3]
	arg_7_0.detailTagDoubleTF = arg_7_0.detailTags[4]
	arg_7_0.detailContain = arg_7_0.findTF("container", arg_7_0.detailWindow)

	if arg_7_0.detailContain:
		arg_7_0.normal = arg_7_0.findTF("normal_items", arg_7_0.detailContain)
		arg_7_0.detailTip = arg_7_0.findTF("Text", arg_7_0.normal)
		arg_7_0.detailItem = arg_7_0.findTF("item_tpl", arg_7_0.normal)
		arg_7_0.extra = arg_7_0.findTF("items", arg_7_0.detailContain)
		arg_7_0.extraTip = arg_7_0.findTF("Text", arg_7_0.extra)
		arg_7_0.detailItemList = arg_7_0.findTF("scrollview/list", arg_7_0.extra)
		arg_7_0.extraDesc = arg_7_0.findTF("Text", arg_7_0.detailContain)

	arg_7_0.detailNormalTip = arg_7_0.findTF("NormalTips", arg_7_0.detailWindow)

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.bg, function()
		arg_8_0.closeView(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.cancelBtn, function()
		arg_8_0.closeView(), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.confirmBtn, function()
		local function var_11_0()
			if arg_8_0.panelConfig.onYes:
				arg_8_0.panelConfig.onYes()
				arg_8_0.closeView()

		local var_11_1 = arg_8_0.panelConfig.limitArgs

		if var_11_1 and type(var_11_1) == "table":
			local var_11_2 = var_11_1[1]

			if var_11_2 and type(var_11_2) == "table" and #var_11_2 >= 2:
				local var_11_3 = var_11_2[1]
				local var_11_4 = var_11_2[2]
				local var_11_5 = getProxy(PlayerProxy).getRawData()

				if var_11_3 == "lv_70" and var_11_4 <= var_11_5.level:
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("lv70_package_tip"),
						def onYes:()
							var_11_0()
					})

					return

		var_11_0(), SFX_PANEL)

def var_0_0.updatePanel(arg_14_0):
	local var_14_0 = arg_14_0.panelConfig.icon
	local var_14_1 = arg_14_0.panelConfig.name and arg_14_0.panelConfig.name or ""
	local var_14_2 = arg_14_0.panelConfig.tipBonus or ""
	local var_14_3 = arg_14_0.panelConfig.bonusItem
	local var_14_4 = arg_14_0.panelConfig.tipExtra and arg_14_0.panelConfig.tipExtra or ""
	local var_14_5 = arg_14_0.panelConfig.extraItems and arg_14_0.panelConfig.extraItems or {}
	local var_14_6 = arg_14_0.panelConfig.price and arg_14_0.panelConfig.price or 0
	local var_14_7 = arg_14_0.panelConfig.isChargeType
	local var_14_8 = arg_14_0.panelConfig.isLocalPrice
	local var_14_9 = arg_14_0.panelConfig.isMonthCard
	local var_14_10 = arg_14_0.panelConfig.tagType
	local var_14_11 = arg_14_0.panelConfig.normalTip
	local var_14_12 = arg_14_0.panelConfig.extraDrop
	local var_14_13 = arg_14_0.panelConfig.isForceGold

	if arg_14_0.detailNormalTip:
		setActive(arg_14_0.detailNormalTip, var_14_11)

	if arg_14_0.detailContain:
		setActive(arg_14_0.detailContain, not var_14_11)

	if var_14_11:
		if arg_14_0.detailNormalTip.GetComponent("Text"):
			setText(arg_14_0.detailNormalTip, var_14_11)
		else
			setButtonText(arg_14_0.detailNormalTip, var_14_11)

	setActive(arg_14_0.detailTag, var_14_10 > 0)

	if var_14_10 > 0:
		for iter_14_0, iter_14_1 in ipairs(arg_14_0.detailTags):
			setActive(iter_14_1, iter_14_0 == var_14_10)

	GetImageSpriteFromAtlasAsync(var_14_0, "", arg_14_0.detailIcon, False)
	setText(arg_14_0.detailName, var_14_1)

	if arg_14_0.detailExtraDrop:
		setActive(arg_14_0.detailExtraDrop, var_14_12)

		if var_14_12:
			setText(arg_14_0.findTF("Text", arg_14_0.detailExtraDrop), i18n("battlepass_pay_acquire") .. "\n" .. var_14_12.count .. "x")
			updateDrop(arg_14_0.findTF("item/IconTpl", arg_14_0.detailExtraDrop), setmetatable({
				count = 1
			}, {
				__index = var_14_12
			}))

	if PLATFORM_CODE == PLATFORM_CHT:
		setActive(arg_14_0.detailRmb, var_14_7 and not var_14_8)
	else
		setActive(arg_14_0.detailRmb, var_14_7)

	setActive(arg_14_0.detailGem, not var_14_7 and not var_14_13)
	setActive(arg_14_0.detailGold, not var_14_7 and not isActive(arg_14_0.detailRmb) and not isActive(arg_14_0.detailGem))
	setText(arg_14_0.detailPrice, var_14_6)

	if arg_14_0.extraDesc != None:
		local var_14_14 = arg_14_0.panelConfig.descExtra or ""

		setActive(arg_14_0.extraDesc, #var_14_14 > 0)
		setText(arg_14_0.extraDesc, var_14_14)

	if arg_14_0.detailContain:
		setActive(arg_14_0.normal, var_14_9)

		if var_14_9:
			updateDrop(arg_14_0.detailItem, var_14_3)
			onButton(arg_14_0, arg_14_0.detailItem, function()
				return, SFX_PANEL)

			local var_14_15, var_14_16 = contentWrap(var_14_3.getConfig("name"), 10, 2)

			if var_14_15:
				var_14_16 = var_14_16 .. "..."

			setText(arg_14_0.findTF("name", arg_14_0.detailItem), var_14_16)
			setText(arg_14_0.detailTip, var_14_2)

		setText(arg_14_0.extraTip, var_14_4)

		for iter_14_2 = #var_14_5, arg_14_0.detailItemList.childCount - 1:
			Destroy(arg_14_0.detailItemList.GetChild(iter_14_2))

		for iter_14_3 = arg_14_0.detailItemList.childCount, #var_14_5 - 1:
			cloneTplTo(arg_14_0.detailItem, arg_14_0.detailItemList)

		for iter_14_4 = 1, #var_14_5:
			local var_14_17 = arg_14_0.detailItemList.GetChild(iter_14_4 - 1)

			updateDrop(var_14_17, var_14_5[iter_14_4])

			local var_14_18, var_14_19 = contentWrap(var_14_5[iter_14_4].getConfig("name"), 8, 2)

			if var_14_18:
				var_14_19 = var_14_19 .. "..."

			setText(arg_14_0.findTF("name", var_14_17), var_14_19)
			onButton(arg_14_0, var_14_17, function()
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					hideNo = True,
					type = MSGBOX_TYPE_SINGLE_ITEM,
					drop = var_14_5[iter_14_4]
				}), SFX_PANEL)

return var_0_0
