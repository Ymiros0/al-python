local var_0_0 = class("ChargeDiamondCard")

var_0_0.NewTagType = 2
var_0_0.DoubleTagType = 4

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.firstTag = arg_1_0.tr.Find("FirstTag")
	arg_1_0.iconImg = arg_1_0.tr.Find("IconImg")
	arg_1_0.diamondCountText = arg_1_0.tr.Find("Count/Text")
	arg_1_0.tipTF = arg_1_0.tr.Find("Tip")
	arg_1_0.firstTipTag = arg_1_0.tr.Find("Tip/Text/FirstTag")
	arg_1_0.exTipTag = arg_1_0.tr.Find("Tip/Text/EXTag")
	arg_1_0.firstEXTip = arg_1_0.tr.Find("Tip/Text/NumText")
	arg_1_0.priceText = arg_1_0.tr.Find("Price/Text")
	arg_1_0.priceIcon = arg_1_0.tr.Find("Price/Icon")
	arg_1_0.monthTF = arg_1_2
	arg_1_0.goods = None
	arg_1_0.parentContext = arg_1_3

def var_0_0.update(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.goods = arg_2_1

	if arg_2_1.isMonthCard():
		setActive(arg_2_0.tr, False)
		arg_2_0.updateForMonthTF(arg_2_1, arg_2_2)

		return

	local var_2_0 = not table.contains(arg_2_3, arg_2_1.id) and arg_2_1.firstPayDouble()
	local var_2_1 = var_2_0 and var_0_0.DoubleTagType or arg_2_1.getConfig("tag")

	setActive(arg_2_0.firstTag, var_2_1 == var_0_0.DoubleTagType)

	if var_2_0:
		local var_2_2 = arg_2_1.getConfig("gem")

		setText(arg_2_0.firstEXTip, var_2_2)
		setActive(arg_2_0.firstTipTag, True)
		setActive(arg_2_0.exTipTag, False)
		setActive(arg_2_0.firstEXTip, True)
		setActive(arg_2_0.tipTF, True)
	elif arg_2_1.hasExtraGem():
		local var_2_3 = arg_2_1.getConfig("extra_gem")

		setText(arg_2_0.firstEXTip, var_2_3)
		setActive(arg_2_0.firstTipTag, False)
		setActive(arg_2_0.exTipTag, True)
		setActive(arg_2_0.firstEXTip, True)
		setActive(arg_2_0.tipTF, True)
	else
		setActive(arg_2_0.tipTF, False)

	setText(arg_2_0.diamondCountText, arg_2_1.getConfig("gem"))
	setText(arg_2_0.priceText, arg_2_1.getConfig("money"))

	if PLATFORM_CODE == PLATFORM_CHT:
		setActive(arg_2_0.priceIcon, not arg_2_1.IsLocalPrice())

	LoadSpriteAsync("chargeicon/" .. arg_2_1.getConfig("picture"), function(arg_3_0)
		if arg_3_0:
			setImageSprite(arg_2_0.iconImg, arg_3_0, True))

def var_0_0.updateForMonthTF(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_0.monthTF.Find("IconImg")
	local var_4_1 = arg_4_0.monthTF.Find("ResCountText")
	local var_4_2 = arg_4_0.monthTF.Find("Price/Text")
	local var_4_3 = arg_4_0.monthTF.Find("ItemIconTpl")
	local var_4_4 = arg_4_0.monthTF.Find("ItemIconList")
	local var_4_5 = arg_4_0.monthTF.Find("Mask")
	local var_4_6 = arg_4_0.monthTF.Find("Mask/LimitText")
	local var_4_7 = arg_4_0.monthTF.Find("Price/Icon")

	setText(arg_4_0.monthTF.Find("Tip/Text"), i18n("monthly_card_tip"))

	local var_4_8 = arg_4_1.getConfig("gem") + arg_4_1.getConfig("extra_gem")

	setText(var_4_1, "x" .. var_4_8)
	setText(var_4_2, arg_4_1.getConfig("money"))

	if PLATFORM_CODE == PLATFORM_CHT:
		setActive(var_4_7, not arg_4_1.IsLocalPrice())

	local var_4_9 = arg_4_1.getConfig("display")

	if #var_4_9 == 0:
		var_4_9 = arg_4_1.getConfig("extra_service_item")

	if var_4_9 and #var_4_9 > 0:
		local var_4_10 = {}

		for iter_4_0, iter_4_1 in ipairs(var_4_9):
			table.insert(var_4_10, {
				type = iter_4_1[1],
				id = iter_4_1[2],
				count = iter_4_1[3]
			})

		local var_4_11 = UIItemList.New(var_4_4, var_4_3)

		var_4_11.make(function(arg_5_0, arg_5_1, arg_5_2)
			if arg_5_0 == UIItemList.EventUpdate:
				updateDrop(arg_5_2, var_4_10[arg_5_1 + 1]))
		var_4_11.align(#var_4_10)

	local var_4_12 = arg_4_2.getCardById(VipCard.MONTH)

	if var_4_12 and not var_4_12.isExpire():
		local var_4_13 = var_4_12.getLeftDate()
		local var_4_14 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_4_15 = math.floor((var_4_13 - var_4_14) / 86400)
		local var_4_16 = arg_4_1.getConfig("limit_arg") or 0

		setActive(var_4_5, var_4_16 < var_4_15)
		setText(var_4_6, i18n("charge_month_card_lefttime_tip", var_4_15))
	else
		setActive(var_4_5, False)

	local var_4_17 = MonthCardOutDateTipPanel.GetShowMonthCardTag()

	setActive(arg_4_0.monthTF.Find("monthcard_tag"), var_4_17)
	setActive(arg_4_0.monthTF.Find("NewTag"), not var_4_17)
	onButton(arg_4_0.parentContext, var_4_0, function()
		triggerButton(arg_4_0.tr), SFX_PANEL)

def var_0_0.destoryTimer(arg_7_0):
	return

return var_0_0
