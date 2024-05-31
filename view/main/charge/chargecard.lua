local var_0_0 = class("ChargeCard")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.go = arg_1_1
	arg_1_0.tr = tf(arg_1_1)
	arg_1_0.icon = arg_1_0.tr:Find("real_tpl/item_icon")
	arg_1_0.iconTF = arg_1_0.icon:GetComponent(typeof(Image))
	arg_1_0.tipTF = arg_1_0.tr:Find("real_tpl/tip")
	arg_1_0.tipText = arg_1_0.tipTF:GetComponent(typeof(Text))
	arg_1_0.count = arg_1_0.tr:Find("real_tpl/count")
	arg_1_0.resIcon = arg_1_0.tr:Find("real_tpl/count/icon"):GetComponent(typeof(Image))
	arg_1_0.resCount = arg_1_0.tr:Find("real_tpl/count/Text"):GetComponent(typeof(Text))
	arg_1_0.priceTf = arg_1_0.tr:Find("real_tpl/prince_bg/contain/Text")
	arg_1_0.price = arg_1_0.priceTf:GetComponent(typeof(Text))
	arg_1_0.freeTag = arg_1_0.tr:Find("real_tpl/prince_bg/contain/FreeText")
	arg_1_0.tecShipBuyTag = arg_1_0.tr:Find("real_tpl/prince_bg/contain/BuyText")
	arg_1_0.contain = arg_1_0.tr:Find("real_tpl/prince_bg/contain")
	arg_1_0.rmb = arg_1_0.tr:Find("real_tpl/prince_bg/contain/icon_rmb")
	arg_1_0.gem = arg_1_0.tr:Find("real_tpl/prince_bg/contain/icon_gem")
	arg_1_0.mask = arg_1_0.tr:Find("real_tpl/mask")
	arg_1_0.maskState = arg_1_0.mask:Find("state")
	arg_1_0.name = arg_1_0.tr:Find("real_tpl/item_name_mask/item_name")
	arg_1_0.important = arg_1_0.tr:Find("real_tpl/important")
	arg_1_0.grid = arg_1_0.tr:Find("real_tpl/important/grid")
	arg_1_0.importantTip = arg_1_0.tr:Find("real_tpl/important/tip")
	arg_1_0.desc = arg_1_0.tr:Find("real_tpl/desc")
	arg_1_0.selfTpl = arg_1_0.tr:Find("real_tpl/important/item")
	arg_1_0.limitText = arg_1_0.tr:Find("real_tpl/LimitText")
	arg_1_0.countDown = arg_1_0.tr:Find("real_tpl/countDown")
	arg_1_0.countDownTm = arg_1_0.countDown:Find("Text")
	arg_1_0.viewBtn = arg_1_0.tr:Find("real_tpl/view")
	arg_1_0.timeLeftTag = arg_1_0.tr:Find("real_tpl/time_left")
	arg_1_0.dayLeftTag = arg_1_0.tr:Find("real_tpl/time_left/day")
	arg_1_0.hourLeftTag = arg_1_0.tr:Find("real_tpl/time_left/hour")
	arg_1_0.minLeftTag = arg_1_0.tr:Find("real_tpl/time_left/min")
	arg_1_0.numLeftText = arg_1_0.timeLeftTag:Find("Text")
	arg_1_0.focusTip = arg_1_0.tr:Find("real_tpl/focus_tip")
	arg_1_0.tag = arg_1_0.tr:Find("real_tpl/tag")
	arg_1_0.tags = {}

	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/hot"))
	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/new"))
	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/advice"))
	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/double"))
	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/activity"))
	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/time"))
	table.insert(arg_1_0.tags, arg_1_0.tr:Find("real_tpl/tag/discount"))
	setActive(arg_1_0.countDown, false)
end

function var_0_0.update(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	arg_2_0.goods = arg_2_1

	local var_2_0 = arg_2_1:isChargeType() and arg_2_1:isTecShipShowGift()

	setActive(arg_2_0.desc, true)
	setText(arg_2_0.desc, "")
	setActive(arg_2_0.rmb, arg_2_1:isChargeType() and not var_2_0)
	setActive(arg_2_0.gem, not arg_2_1:isChargeType() and not arg_2_1:isFree())
	setText(arg_2_0.freeTag, i18n("shop_free_tag"))
	setText(arg_2_0.tecShipBuyTag, i18n("word_buy"))
	setActive(arg_2_0.tecShipBuyTag, var_2_0)
	setActive(arg_2_0.freeTag, arg_2_1:isFree())
	setActive(arg_2_0.priceTf, not arg_2_1:isFree() and not var_2_0)
	setActive(arg_2_0.focusTip, arg_2_1:isFree())
	setActive(arg_2_0.icon, arg_2_1:isChargeType())
	setActive(arg_2_0.contain, true)
	setActive(arg_2_0.countDown, false)

	if arg_2_0.viewBtn then
		setActive(arg_2_0.viewBtn, arg_2_1:isChargeType() and arg_2_1:CanViewSkinProbability())
	end

	if arg_2_1:isChargeType() then
		arg_2_0:updateCharge(arg_2_1, arg_2_2, arg_2_3)
	else
		arg_2_0:updateGemItem(arg_2_1, arg_2_2)
	end

	arg_2_0:destoryTimer()
end

function var_0_0.updateCharge(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	setActive(arg_3_0.tag, true)
	setActive(arg_3_0.mask, false)
	setActive(arg_3_0.maskState, false)

	arg_3_0.tipText.text = ""

	setText(arg_3_0.desc, "")

	local var_3_0 = not table.contains(arg_3_3, arg_3_1.id)
	local var_3_1 = var_3_0 and arg_3_1:firstPayDouble()
	local var_3_2 = var_3_1 and 4 or arg_3_1:getConfig("tag")

	setActive(arg_3_0.timeLeftTag, false)
	setActive(arg_3_0.tag, var_3_2 > 0)

	if var_3_2 > 0 then
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.tags) do
			setActive(iter_3_1, iter_3_0 == var_3_2)
		end
	end

	setActive(arg_3_0.timeLeftTag, false)

	local var_3_3, var_3_4 = arg_3_1:inTime()

	if var_3_3 and not arg_3_1:isFree() and var_3_4 and var_3_4 > 0 then
		local var_3_5, var_3_6, var_3_7 = pg.TimeMgr.GetInstance():parseTimeFrom(var_3_4)

		if var_3_5 > 0 then
			setActive(arg_3_0.timeLeftTag, true)
			setActive(arg_3_0.dayLeftTag, true)
			setActive(arg_3_0.hourLeftTag, false)
			setActive(arg_3_0.minLeftTag, false)
			setText(arg_3_0.numLeftText, var_3_5)
		elseif var_3_6 > 0 then
			setActive(arg_3_0.timeLeftTag, true)
			setActive(arg_3_0.dayLeftTag, false)
			setActive(arg_3_0.hourLeftTag, true)
			setActive(arg_3_0.minLeftTag, false)
			setText(arg_3_0.numLeftText, var_3_6)
		elseif var_3_7 > 0 then
			setActive(arg_3_0.timeLeftTag, true)
			setActive(arg_3_0.dayLeftTag, false)
			setActive(arg_3_0.hourLeftTag, false)
			setActive(arg_3_0.minLeftTag, true)
			setText(arg_3_0.numLeftText, var_3_7)
		else
			setActive(arg_3_0.timeLeftTag, true)
			setActive(arg_3_0.dayLeftTag, false)
			setActive(arg_3_0.hourLeftTag, false)
			setActive(arg_3_0.minLeftTag, true)
			setText(arg_3_0.numLeftText, 0)
		end

		local var_3_8 = 60
		local var_3_9 = 3600
		local var_3_10 = 86400
		local var_3_11

		if var_3_10 <= var_3_4 then
			var_3_11 = var_3_4 % var_3_10
		elseif var_3_9 <= var_3_4 then
			var_3_11 = var_3_4 % var_3_9
		elseif var_3_8 <= var_3_4 then
			var_3_11 = var_3_4 % var_3_8
		end

		if var_3_11 and var_3_11 > 0 then
			if arg_3_0.countDownTimer then
				arg_3_0.countDownTimer:Stop()

				arg_3_0.countDownTimer = nil
			end

			arg_3_0.countDownTimer = Timer.New(function()
				arg_3_0:updateGemItem(arg_3_1, arg_3_2)
			end, var_3_11, 1)

			arg_3_0.countDownTimer:Start()
		end
	end

	setActive(arg_3_0.resIcon, not arg_3_1:isItemBox())
	setActive(arg_3_0.resCount, not arg_3_1:isItemBox())

	local var_3_12 = arg_3_1:isGem()

	setActive(arg_3_0.name, not var_3_12)
	setScrollText(arg_3_0.name, arg_3_1:getConfig("name_display"))
	setActive(arg_3_0.important, arg_3_1:isItemBox() or arg_3_1:isGiftBox())
	setActive(arg_3_0.count, var_3_12 or arg_3_1:isMonthCard())

	if arg_3_1:isItemBox() or arg_3_1:isGiftBox() or arg_3_1:isPassItem() then
		arg_3_0:updateImport(arg_3_1:getConfig("display"), arg_3_1:getConfig("descrip"))
	end

	local var_3_13 = arg_3_1:getConfig("limit_type")
	local var_3_14 = arg_3_1.buyCount
	local var_3_15 = arg_3_1:getLimitCount()

	if var_3_13 == 2 then
		setText(arg_3_0.limitText, i18n("charge_limit_all", var_3_15 - var_3_14, var_3_15))
		setActive(arg_3_0.mask, var_3_15 - var_3_14 <= 0)
	elseif var_3_13 == 4 then
		setText(arg_3_0.limitText, i18n("charge_limit_daily", var_3_15 - var_3_14, var_3_15))
		setActive(arg_3_0.mask, var_3_15 - var_3_14 <= 0)
	else
		setText(arg_3_0.limitText, "")
	end

	if arg_3_1:isGem() then
		setActive(arg_3_0.tipTF, true)

		if var_3_1 then
			local var_3_16 = arg_3_1:getConfig("gem") * arg_3_1:getConfig("first_pay_double")

			arg_3_0.tipText.text = i18n("charge_double_gem_tip", var_3_16)
		elseif arg_3_1:hasExtraGem() then
			arg_3_0.tipText.text = i18n("charge_extra_gem_tip", arg_3_1:getConfig("extra_gem"))
		else
			setActive(arg_3_0.tipTF, false)
		end
	elseif arg_3_1:isGiftBox() then
		-- block empty
	elseif arg_3_1:isMonthCard() then
		local var_3_17 = arg_3_2:getCardById(VipCard.MONTH)

		if var_3_17 and not var_3_17:isExpire() then
			local var_3_18 = var_3_17:getLeftDate()
			local var_3_19 = pg.TimeMgr.GetInstance():GetServerTime()
			local var_3_20 = math.floor((var_3_18 - var_3_19) / 86400)
			local var_3_21 = arg_3_1:getConfig("limit_arg") or 0

			setActive(arg_3_0.mask, var_3_21 < var_3_20)
			setText(arg_3_0.limitText, i18n("charge_month_card_lefttime_tip", var_3_20))
		end

		setText(arg_3_0.desc, string.gsub(arg_3_1:getConfig("descrip"), "$1", var_3_0 and arg_3_1:getConfig("gem") or arg_3_1:getConfig("extra_gem")))
	elseif arg_3_1:isItemBox() then
		-- block empty
	elseif arg_3_1:isPassItem() then
		-- block empty
	end

	arg_3_0.resCount.text = "x" .. arg_3_1:getConfig("gem")
	arg_3_0.price.text = arg_3_1:getConfig("money")

	if PLATFORM_CODE == PLATFORM_CHT and arg_3_1:IsLocalPrice() then
		setActive(arg_3_0.rmb, false)
	end

	arg_3_0.iconTF.sprite = GetSpriteFromAtlas("chargeicon/1", "")

	LoadSpriteAsync("chargeicon/" .. arg_3_1:getConfig("picture"), function(arg_5_0)
		if arg_5_0 then
			arg_3_0.iconTF.sprite = arg_5_0

			arg_3_0.iconTF:SetNativeSize()
		end
	end)
	setButtonEnabled(arg_3_0.tr, not isActive(arg_3_0.mask))
end

function var_0_0.updateGemItem(arg_6_0, arg_6_1, arg_6_2)
	setActive(arg_6_0.mask, false)
	setActive(arg_6_0.maskState, false)
	setText(arg_6_0.limitText, "")

	arg_6_0.tipText.text = ""

	local var_6_0 = arg_6_1:getLimitCount()
	local var_6_1 = arg_6_1.buyCount or 0

	if var_6_0 > 0 then
		setText(arg_6_0.limitText, i18n("charge_limit_all", var_6_0 - var_6_1, var_6_0))
		setActive(arg_6_0.mask, var_6_0 <= var_6_1)
	end

	local var_6_2 = arg_6_1:getConfig("group_limit")

	if var_6_2 > 0 then
		local var_6_3 = arg_6_1:getConfig("group_type") or 0

		if var_6_3 == 1 then
			setText(arg_6_0.limitText, i18n("charge_limit_daily", var_6_2 - arg_6_1.groupCount, var_6_2))
		elseif var_6_3 == 2 then
			setText(arg_6_0.limitText, i18n("charge_limit_weekly", var_6_2 - arg_6_1.groupCount, var_6_2))
		elseif var_6_3 == 3 then
			setText(arg_6_0.limitText, i18n("charge_limit_monthly", var_6_2 - arg_6_1.groupCount, var_6_2))
		end
	end

	arg_6_0.price.text = arg_6_1:getConfig("resource_num")
	arg_6_0.tipText.text = ""

	setActive(arg_6_0.count, false)
	setActive(arg_6_0.icon, true)
	setText(arg_6_0.desc, "")

	local var_6_4 = arg_6_1:getConfig("tag")

	setActive(arg_6_0.tag, var_6_4 > 0)

	if var_6_4 > 0 then
		for iter_6_0, iter_6_1 in ipairs(arg_6_0.tags) do
			setActive(iter_6_1, iter_6_0 == var_6_4)
		end
	end

	setActive(arg_6_0.timeLeftTag, false)

	local var_6_5, var_6_6 = arg_6_1:inTime()

	if var_6_5 and not arg_6_1:isFree() and var_6_6 and var_6_6 > 0 then
		local var_6_7, var_6_8, var_6_9 = pg.TimeMgr.GetInstance():parseTimeFrom(var_6_6)

		if var_6_7 > 0 then
			setActive(arg_6_0.timeLeftTag, true)
			setActive(arg_6_0.dayLeftTag, true)
			setActive(arg_6_0.hourLeftTag, false)
			setActive(arg_6_0.minLeftTag, false)
			setText(arg_6_0.numLeftText, var_6_7)
		elseif var_6_8 > 0 then
			setActive(arg_6_0.timeLeftTag, true)
			setActive(arg_6_0.dayLeftTag, false)
			setActive(arg_6_0.hourLeftTag, true)
			setActive(arg_6_0.minLeftTag, false)
			setText(arg_6_0.numLeftText, var_6_8)
		elseif var_6_9 > 0 then
			setActive(arg_6_0.timeLeftTag, true)
			setActive(arg_6_0.dayLeftTag, false)
			setActive(arg_6_0.hourLeftTag, false)
			setActive(arg_6_0.minLeftTag, true)
			setText(arg_6_0.numLeftText, var_6_9)
		else
			setActive(arg_6_0.timeLeftTag, true)
			setActive(arg_6_0.dayLeftTag, false)
			setActive(arg_6_0.hourLeftTag, false)
			setActive(arg_6_0.minLeftTag, true)
			setText(arg_6_0.numLeftText, 0)
		end

		local var_6_10 = 60
		local var_6_11 = 3600
		local var_6_12 = 86400
		local var_6_13

		if var_6_12 <= var_6_6 then
			var_6_13 = var_6_6 % var_6_12
		elseif var_6_11 <= var_6_6 then
			var_6_13 = var_6_6 % var_6_11
		elseif var_6_10 <= var_6_6 then
			var_6_13 = var_6_6 % var_6_10
		end

		if var_6_13 and var_6_13 > 0 then
			if arg_6_0.countDownTimer then
				arg_6_0.countDownTimer:Stop()

				arg_6_0.countDownTimer = nil
			end

			arg_6_0.countDownTimer = Timer.New(function()
				arg_6_0:updateGemItem(arg_6_1, arg_6_2)
			end, var_6_13, 1)

			arg_6_0.countDownTimer:Start()
		end
	end

	setActive(arg_6_0.name, true)

	local var_6_14 = arg_6_1:getConfig("effect_args")

	if #var_6_14 > 0 then
		local var_6_15 = Item.getConfigData(var_6_14[1])

		if var_6_15 then
			setScrollText(arg_6_0.name, var_6_15.name)
			arg_6_0:updateImport(var_6_15.display_icon, var_6_15.display)
		end

		arg_6_0.iconTF.sprite = GetSpriteFromAtlas("chargeicon/1", "")

		LoadSpriteAsync(var_6_15.icon, function(arg_8_0)
			if arg_8_0 then
				arg_6_0.iconTF.sprite = arg_8_0

				arg_6_0.iconTF:SetNativeSize()
			end
		end)
	end

	setButtonEnabled(arg_6_0.tr, not isActive(arg_6_0.mask))
end

function var_0_0.updateImport(arg_9_0, arg_9_1, arg_9_2)
	setActive(arg_9_0.important, true)

	local var_9_0 = {}

	for iter_9_0, iter_9_1 in ipairs(arg_9_1) do
		table.insert(var_9_0, Drop.Create(iter_9_1))
	end

	for iter_9_2 = 1, arg_9_0.grid.childCount do
		local var_9_1 = arg_9_0.grid:GetChild(iter_9_2 - 1)

		if iter_9_2 <= #var_9_0 then
			setActive(var_9_1, true)
			updateDrop(var_9_1, var_9_0[iter_9_2])
		else
			setActive(var_9_1, false)
		end
	end

	setText(arg_9_0.importantTip, string.gsub(arg_9_2, "$1", #var_9_0))
end

function var_0_0.updateCountdown(arg_10_0, arg_10_1)
	local var_10_0 = false

	if arg_10_1 then
		local var_10_1 = pg.TimeMgr.GetInstance()

		var_10_0 = var_10_1:DiffDay(var_10_1:GetServerTime(), pg.TimeMgr.GetInstance():Table2ServerTime(arg_10_1)) < 365
	end

	setActive(arg_10_0.countDown, var_10_0)

	local var_10_2 = pg.TimeMgr.GetInstance()

	local function var_10_3()
		if arg_10_0.updateTimer then
			arg_10_0.updateTimer:Stop()

			arg_10_0.updateTimer = nil
		end
	end

	var_10_3()

	local var_10_4 = var_10_2:Table2ServerTime(arg_10_1)

	arg_10_0.updateTimer = Timer.New(function()
		local var_12_0 = var_10_2:GetServerTime()

		if var_12_0 > var_10_4 then
			var_10_3()
		end

		local var_12_1 = var_10_4 - var_12_0

		var_12_1 = var_12_1 < 0 and 0 or var_12_1

		local var_12_2 = math.floor(var_12_1 / 86400)

		if var_12_2 > 0 then
			setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_2 .. i18n("word_date"))
		else
			local var_12_3 = math.floor(var_12_1 / 3600)

			if var_12_3 > 0 then
				setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_3 .. i18n("word_hour"))
			else
				local var_12_4 = math.floor(var_12_1 / 60)

				if var_12_4 > 0 then
					setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_4 .. i18n("word_minute"))
				else
					setText(arg_10_0.countDownTm, i18n("skin_remain_time") .. var_12_1 .. i18n("word_second"))
				end
			end
		end
	end, 1, -1)

	arg_10_0.updateTimer:Start()
	arg_10_0.updateTimer.func()
end

function var_0_0.destoryTimer(arg_13_0)
	if arg_13_0.updateTimer then
		arg_13_0.updateTimer:Stop()

		arg_13_0.updateTimer = nil
	end

	if arg_13_0.countDownTimer then
		arg_13_0.countDownTimer:Stop()

		arg_13_0.countDownTimer = nil
	end
end

return var_0_0
