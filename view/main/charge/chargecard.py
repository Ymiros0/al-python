local var_0_0 = class("ChargeCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.icon = arg_1_0.tr.Find("real_tpl/item_icon")
	arg_1_0.iconTF = arg_1_0.icon.GetComponent(typeof(Image))
	arg_1_0.tipTF = arg_1_0.tr.Find("real_tpl/tip")
	arg_1_0.tipText = arg_1_0.tipTF.GetComponent(typeof(Text))
	arg_1_0.count = arg_1_0.tr.Find("real_tpl/count")
	arg_1_0.resIcon = arg_1_0.tr.Find("real_tpl/count/icon").GetComponent(typeof(Image))
	arg_1_0.resCount = arg_1_0.tr.Find("real_tpl/count/Text").GetComponent(typeof(Text))
	arg_1_0.priceTf = arg_1_0.tr.Find("real_tpl/prince_bg/contain/Text")
	arg_1_0.price = arg_1_0.priceTf.GetComponent(typeof(Text))
	arg_1_0.freeTag = arg_1_0.tr.Find("real_tpl/prince_bg/contain/FreeText")
	arg_1_0.tecShipBuyTag = arg_1_0.tr.Find("real_tpl/prince_bg/contain/BuyText")
	arg_1_0.contain = arg_1_0.tr.Find("real_tpl/prince_bg/contain")
	arg_1_0.rmb = arg_1_0.tr.Find("real_tpl/prince_bg/contain/icon_rmb")
	arg_1_0.gem = arg_1_0.tr.Find("real_tpl/prince_bg/contain/icon_gem")
	arg_1_0.mask = arg_1_0.tr.Find("real_tpl/mask")
	arg_1_0.maskState = arg_1_0.mask.Find("state")
	arg_1_0.name = arg_1_0.tr.Find("real_tpl/item_name_mask/item_name")
	arg_1_0.important = arg_1_0.tr.Find("real_tpl/important")
	arg_1_0.grid = arg_1_0.tr.Find("real_tpl/important/grid")
	arg_1_0.importantTip = arg_1_0.tr.Find("real_tpl/important/tip")
	arg_1_0.desc = arg_1_0.tr.Find("real_tpl/desc")
	arg_1_0.selfTpl = arg_1_0.tr.Find("real_tpl/important/item")
	arg_1_0.limitText = arg_1_0.tr.Find("real_tpl/LimitText")
	arg_1_0.countDown = arg_1_0.tr.Find("real_tpl/countDown")
	arg_1_0.countDownTm = arg_1_0.countDown.Find("Text")
	arg_1_0.viewBtn = arg_1_0.tr.Find("real_tpl/view")
	arg_1_0.timeLeftTag = arg_1_0.tr.Find("real_tpl/time_left")
	arg_1_0.dayLeftTag = arg_1_0.tr.Find("real_tpl/time_left/day")
	arg_1_0.hourLeftTag = arg_1_0.tr.Find("real_tpl/time_left/hour")
	arg_1_0.minLeftTag = arg_1_0.tr.Find("real_tpl/time_left/min")
	arg_1_0.numLeftText = arg_1_0.timeLeftTag.Find("Text")
	arg_1_0.focusTip = arg_1_0.tr.Find("real_tpl/focus_tip")
	arg_1_0.tag = arg_1_0.tr.Find("real_tpl/tag")
	arg_1_0.tags = {}

	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/hot"))
	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/new"))
	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/advice"))
	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/double"))
	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/activity"))
	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/time"))
	table.insert(arg_1_0.tags, arg_1_0.tr.Find("real_tpl/tag/discount"))
	setActive(arg_1_0.countDown, False)

def var_0_0.update(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.goods = arg_2_1

	local var_2_0 = arg_2_1.isChargeType() and arg_2_1.isTecShipShowGift()

	setActive(arg_2_0.desc, True)
	setText(arg_2_0.desc, "")
	setActive(arg_2_0.rmb, arg_2_1.isChargeType() and not var_2_0)
	setActive(arg_2_0.gem, not arg_2_1.isChargeType() and not arg_2_1.isFree())
	setText(arg_2_0.freeTag, i18n("shop_free_tag"))
	setText(arg_2_0.tecShipBuyTag, i18n("word_buy"))
	setActive(arg_2_0.tecShipBuyTag, var_2_0)
	setActive(arg_2_0.freeTag, arg_2_1.isFree())
	setActive(arg_2_0.priceTf, not arg_2_1.isFree() and not var_2_0)
	setActive(arg_2_0.focusTip, arg_2_1.isFree())
	setActive(arg_2_0.icon, arg_2_1.isChargeType())
	setActive(arg_2_0.contain, True)
	setActive(arg_2_0.countDown, False)

	if arg_2_0.viewBtn:
		setActive(arg_2_0.viewBtn, arg_2_1.isChargeType() and arg_2_1.CanViewSkinProbability())

	if arg_2_1.isChargeType():
		arg_2_0.updateCharge(arg_2_1, arg_2_2, arg_2_3)
	else
		arg_2_0.updateGemItem(arg_2_1, arg_2_2)

	arg_2_0.destoryTimer()

def var_0_0.updateCharge(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	setActive(arg_3_0.tag, True)
	setActive(arg_3_0.mask, False)
	setActive(arg_3_0.maskState, False)

	arg_3_0.tipText.text = ""

	setText(arg_3_0.desc, "")

	local var_3_0 = not table.contains(arg_3_3, arg_3_1.id)
	local var_3_1 = var_3_0 and arg_3_1.firstPayDouble()
	local var_3_2 = var_3_1 and 4 or arg_3_1.getConfig("tag")

	setActive(arg_3_0.timeLeftTag, False)
	setActive(arg_3_0.tag, var_3_2 > 0)

	if var_3_2 > 0:
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.tags):
			setActive(iter_3_1, iter_3_0 == var_3_2)

	setActive(arg_3_0.timeLeftTag, False)

	local var_3_3, var_3_4 = arg_3_1.inTime()

	if var_3_3 and not arg_3_1.isFree() and var_3_4 and var_3_4 > 0:
		local var_3_5, var_3_6, var_3_7 = pg.TimeMgr.GetInstance().parseTimeFrom(var_3_4)

		if var_3_5 > 0:
			setActive(arg_3_0.timeLeftTag, True)
			setActive(arg_3_0.dayLeftTag, True)
			setActive(arg_3_0.hourLeftTag, False)
			setActive(arg_3_0.minLeftTag, False)
			setText(arg_3_0.numLeftText, var_3_5)
		elif var_3_6 > 0:
			setActive(arg_3_0.timeLeftTag, True)
			setActive(arg_3_0.dayLeftTag, False)
			setActive(arg_3_0.hourLeftTag, True)
			setActive(arg_3_0.minLeftTag, False)
			setText(arg_3_0.numLeftText, var_3_6)
		elif var_3_7 > 0:
			setActive(arg_3_0.timeLeftTag, True)
			setActive(arg_3_0.dayLeftTag, False)
			setActive(arg_3_0.hourLeftTag, False)
			setActive(arg_3_0.minLeftTag, True)
			setText(arg_3_0.numLeftText, var_3_7)
		else
			setActive(arg_3_0.timeLeftTag, True)
			setActive(arg_3_0.dayLeftTag, False)
			setActive(arg_3_0.hourLeftTag, False)
			setActive(arg_3_0.minLeftTag, True)
			setText(arg_3_0.numLeftText, 0)

		local var_3_8 = 60
		local var_3_9 = 3600
		local var_3_10 = 86400
		local var_3_11

		if var_3_10 <= var_3_4:
			var_3_11 = var_3_4 % var_3_10
		elif var_3_9 <= var_3_4:
			var_3_11 = var_3_4 % var_3_9
		elif var_3_8 <= var_3_4:
			var_3_11 = var_3_4 % var_3_8

		if var_3_11 and var_3_11 > 0:
			if arg_3_0.countDownTimer:
				arg_3_0.countDownTimer.Stop()

				arg_3_0.countDownTimer = None

			arg_3_0.countDownTimer = Timer.New(function()
				arg_3_0.updateGemItem(arg_3_1, arg_3_2), var_3_11, 1)

			arg_3_0.countDownTimer.Start()

	setActive(arg_3_0.resIcon, not arg_3_1.isItemBox())
	setActive(arg_3_0.resCount, not arg_3_1.isItemBox())

	local var_3_12 = arg_3_1.isGem()

	setActive(arg_3_0.name, not var_3_12)
	setScrollText(arg_3_0.name, arg_3_1.getConfig("name_display"))
	setActive(arg_3_0.important, arg_3_1.isItemBox() or arg_3_1.isGiftBox())
	setActive(arg_3_0.count, var_3_12 or arg_3_1.isMonthCard())

	if arg_3_1.isItemBox() or arg_3_1.isGiftBox() or arg_3_1.isPassItem():
		arg_3_0.updateImport(arg_3_1.getConfig("display"), arg_3_1.getConfig("descrip"))

	local var_3_13 = arg_3_1.getConfig("limit_type")
	local var_3_14 = arg_3_1.buyCount
	local var_3_15 = arg_3_1.getLimitCount()

	if var_3_13 == 2:
		setText(arg_3_0.limitText, i18n("charge_limit_all", var_3_15 - var_3_14, var_3_15))
		setActive(arg_3_0.mask, var_3_15 - var_3_14 <= 0)
	elif var_3_13 == 4:
		setText(arg_3_0.limitText, i18n("charge_limit_daily", var_3_15 - var_3_14, var_3_15))
		setActive(arg_3_0.mask, var_3_15 - var_3_14 <= 0)
	else
		setText(arg_3_0.limitText, "")

	if arg_3_1.isGem():
		setActive(arg_3_0.tipTF, True)

		if var_3_1:
			local var_3_16 = arg_3_1.getConfig("gem") * arg_3_1.getConfig("first_pay_double")

			arg_3_0.tipText.text = i18n("charge_double_gem_tip", var_3_16)
		elif arg_3_1.hasExtraGem():
			arg_3_0.tipText.text = i18n("charge_extra_gem_tip", arg_3_1.getConfig("extra_gem"))
		else
			setActive(arg_3_0.tipTF, False)
	elif arg_3_1.isGiftBox():
		-- block empty
	elif arg_3_1.isMonthCard():
		local var_3_17 = arg_3_2.getCardById(VipCard.MONTH)

		if var_3_17 and not var_3_17.isExpire():
			local var_3_18 = var_3_17.getLeftDate()
			local var_3_19 = pg.TimeMgr.GetInstance().GetServerTime()
			local var_3_20 = math.floor((var_3_18 - var_3_19) / 86400)
			local var_3_21 = arg_3_1.getConfig("limit_arg") or 0

			setActive(arg_3_0.mask, var_3_21 < var_3_20)
			setText(arg_3_0.limitText, i18n("charge_month_card_lefttime_tip", var_3_20))

		setText(arg_3_0.desc, string.gsub(arg_3_1.getConfig("descrip"), "$1", var_3_0 and arg_3_1.getConfig("gem") or arg_3_1.getConfig("extra_gem")))
	elif arg_3_1.isItemBox():
		-- block empty
	elif arg_3_1.isPassItem():
		-- block empty

	arg_3_0.resCount.text = "x" .. arg_3_1.getConfig("gem")
	arg_3_0.price.text = arg_3_1.getConfig("money")

	if PLATFORM_CODE == PLATFORM_CHT and arg_3_1.IsLocalPrice():
		setActive(arg_3_0.rmb, False)

	arg_3_0.iconTF.sprite = GetSpriteFromAtlas("chargeicon/1", "")

	LoadSpriteAsync("chargeicon/" .. arg_3_1.getConfig("picture"), function(arg_5_0)
		if arg_5_0:
			arg_3_0.iconTF.sprite = arg_5_0

			arg_3_0.iconTF.SetNativeSize())
	setButtonEnabled(arg_3_0.tr, not isActive(arg_3_0.mask))

def var_0_0.updateGemItem(arg_6_0, arg_6_1, arg_6_2):
	setActive(arg_6_0.mask, False)
	setActive(arg_6_0.maskState, False)
	setText(arg_6_0.limitText, "")

	arg_6_0.tipText.text = ""

	local var_6_0 = arg_6_1.getLimitCount()
	local var_6_1 = arg_6_1.buyCount or 0

	if var_6_0 > 0:
		setText(arg_6_0.limitText, i18n("charge_limit_all", var_6_0 - var_6_1, var_6_0))
		setActive(arg_6_0.mask, var_6_0 <= var_6_1)

	local var_6_2 = arg_6_1.getConfig("group_limit")

	if var_6_2 > 0:
		local var_6_3 = arg_6_1.getConfig("group_type") or 0

		if var_6_3 == 1:
			setText(arg_6_0.limitText, i18n("charge_limit_daily", var_6_2 - arg_6_1.groupCount, var_6_2))
		elif var_6_3 == 2:
			setText(arg_6_0.limitText, i18n("charge_limit_weekly", var_6_2 - arg_6_1.groupCount, var_6_2))
		elif var_6_3 == 3:
			setText(arg_6_0.limitText, i18n("charge_limit_monthly", var_6_2 - arg_6_1.groupCount, var_6_2))

	arg_6_0.price.text = arg_6_1.getConfig("resource_num")
	arg_6_0.tipText.text = ""

	setActive(arg_6_0.count, False)
	setActive(arg_6_0.icon, True)
	setText(arg_6_0.desc, "")

	local var_6_4 = arg_6_1.getConfig("tag")

	setActive(arg_6_0.tag, var_6_4 > 0)

	if var_6_4 > 0:
		for iter_6_0, iter_6_1 in ipairs(arg_6_0.tags):
			setActive(iter_6_1, iter_6_0 == var_6_4)

	setActive(arg_6_0.timeLeftTag, False)

	local var_6_5, var_6_6 = arg_6_1.inTime()

	if var_6_5 and not arg_6_1.isFree() and var_6_6 and var_6_6 > 0:
		local var_6_7, var_6_8, var_6_9 = pg.TimeMgr.GetInstance().parseTimeFrom(var_6_6)

		if var_6_7 > 0:
			setActive(arg_6_0.timeLeftTag, True)
			setActive(arg_6_0.dayLeftTag, True)
			setActive(arg_6_0.hourLeftTag, False)
			setActive(arg_6_0.minLeftTag, False)
			setText(arg_6_0.numLeftText, var_6_7)
		elif var_6_8 > 0:
			setActive(arg_6_0.timeLeftTag, True)
			setActive(arg_6_0.dayLeftTag, False)
			setActive(arg_6_0.hourLeftTag, True)
			setActive(arg_6_0.minLeftTag, False)
			setText(arg_6_0.numLeftText, var_6_8)
		elif var_6_9 > 0:
			setActive(arg_6_0.timeLeftTag, True)
			setActive(arg_6_0.dayLeftTag, False)
			setActive(arg_6_0.hourLeftTag, False)
			setActive(arg_6_0.minLeftTag, True)
			setText(arg_6_0.numLeftText, var_6_9)
		else
			setActive(arg_6_0.timeLeftTag, True)
			setActive(arg_6_0.dayLeftTag, False)
			setActive(arg_6_0.hourLeftTag, False)
			setActive(arg_6_0.minLeftTag, True)
			setText(arg_6_0.numLeftText, 0)

		local var_6_10 = 60
		local var_6_11 = 3600
		local var_6_12 = 86400
		local var_6_13

		if var_6_12 <= var_6_6:
			var_6_13 = var_6_6 % var_6_12
		elif var_6_11 <= var_6_6:
			var_6_13 = var_6_6 % var_6_11
		elif var_6_10 <= var_6_6:
			var_6_13 = var_6_6 % var_6_10

		if var_6_13 and var_6_13 > 0:
			if arg_6_0.countDownTimer:
				arg_6_0.countDownTimer.Stop()

				arg_6_0.countDownTimer = None

			arg_6_0.countDownTimer = Timer.New(function()
				arg_6_0.updateGemItem(arg_6_1, arg_6_2), var_6_13, 1)

			arg_6_0.countDownTimer.Start()

	setActive(arg_6_0.name, True)

	local var_6_14 = arg_6_1.getConfig("effect_args")

	if #var_6_14 > 0:
		local var_6_15 = Item.getConfigData(var_6_14[1])

		if var_6_15:
			setScrollText(arg_6_0.name, var_6_15.name)
			arg_6_0.updateImport(var_6_15.display_icon, var_6_15.display)

		arg_6_0.iconTF.sprite = GetSpriteFromAtlas("chargeicon/1", "")

		LoadSpriteAsync(var_6_15.icon, function(arg_8_0)
			if arg_8_0:
				arg_6_0.iconTF.sprite = arg_8_0

				arg_6_0.iconTF.SetNativeSize())

	setButtonEnabled(arg_6_0.tr, not isActive(arg_6_0.mask))

def var_0_0.updateImport(arg_9_0, arg_9_1, arg_9_2):
	setActive(arg_9_0.important, True)

	local var_9_0 = {}

	for iter_9_0, iter_9_1 in ipairs(arg_9_1):
		table.insert(var_9_0, Drop.Create(iter_9_1))

	for iter_9_2 = 1, arg_9_0.grid.childCount:
		local var_9_1 = arg_9_0.grid.GetChild(iter_9_2 - 1)

		if iter_9_2 <= #var_9_0:
			setActive(var_9_1, True)
			updateDrop(var_9_1, var_9_0[iter_9_2])
		else
			setActive(var_9_1, False)

	setText(arg_9_0.importantTip, string.gsub(arg_9_2, "$1", #var_9_0))

def var_0_0.updateCountdown(arg_10_0, arg_10_1):
	local var_10_0 = False

	if arg_10_1:
		local var_10_1 = pg.TimeMgr.GetInstance()

		var_10_0 = var_10_1.DiffDay(var_10_1.GetServerTime(), pg.TimeMgr.GetInstance().Table2ServerTime(arg_10_1)) < 365

	setActive(arg_10_0.countDown, var_10_0)

	local var_10_2 = pg.TimeMgr.GetInstance()

	local function var_10_3()
		if arg_10_0.updateTimer:
			arg_10_0.updateTimer.Stop()

			arg_10_0.updateTimer = None

	var_10_3()

	local var_10_4 = var_10_2.Table2ServerTime(arg_10_1)

	arg_10_0.updateTimer = Timer.New(function()
		local var_12_0 = var_10_2.GetServerTime()

		if var_12_0 > var_10_4:
			var_10_3()

		local var_12_1 = var_10_4 - var_12_0

		var_12_1 = var_12_1 < 0 and 0 or var_12_1

		local var_12_2 = math.floor(var_12_1 / 86400)

		if var_12_2 > 0:
			setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_2 .. i18n("word_date"))
		else
			local var_12_3 = math.floor(var_12_1 / 3600)

			if var_12_3 > 0:
				setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_3 .. i18n("word_hour"))
			else
				local var_12_4 = math.floor(var_12_1 / 60)

				if var_12_4 > 0:
					setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_4 .. i18n("word_minute"))
				else
					setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_1 .. i18n("word_second")), 1, -1)

	arg_10_0.updateTimer.Start()
	arg_10_0.updateTimer.func()

def var_0_0.destoryTimer(arg_13_0):
	if arg_13_0.updateTimer:
		arg_13_0.updateTimer.Stop()

		arg_13_0.updateTimer = None

	if arg_13_0.countDownTimer:
		arg_13_0.countDownTimer.Stop()

		arg_13_0.countDownTimer = None

return var_0_0
