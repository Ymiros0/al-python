local var_0_0 = class("StreetShopPage", import(".BaseShopPage"))

def var_0_0.getUIName(arg_1_0):
	return "StreetShop"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.timerText = arg_2_0.findTF("timer_bg/Text").GetComponent(typeof(Text))
	arg_2_0.refreshBtn = arg_2_0.findTF("refresh_btn")
	arg_2_0.actTip = arg_2_0.findTF("tip/tip_activity").GetComponent(typeof(Text))

	local var_2_0 = getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP_STREET)
	local var_2_1 = _.select(var_2_0, function(arg_3_0)
		return arg_3_0 and not arg_3_0.isEnd())

	setActive(arg_2_0.actTip, #var_2_1 > 0)

	arg_2_0.actTip.text = arg_2_0.GenTip(var_2_1)
	arg_2_0.helpBtn = arg_2_0.findTF("tip/help")

	setActive(arg_2_0.helpBtn, #var_2_1 > 1)

	arg_2_0.activitys = var_2_1

def var_0_0.GenTip(arg_4_0, arg_4_1):
	local var_4_0 = ""

	if #arg_4_1 == 1:
		local var_4_1 = arg_4_1[1]

		var_4_0 = i18n("shop_street_activity_tip", var_4_1.GetShopTime())
	elif #arg_4_1 > 1:
		var_4_0 = arg_4_0.GenTipForMultiAct(arg_4_1)

	return var_4_0

def var_0_0.GenTipForMultiAct(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1[1]
	local var_5_1 = var_5_0.getStartTime()
	local var_5_2 = var_5_0.stopTime
	local var_5_3 = _.all(arg_5_1, function(arg_6_0)
		return arg_6_0.getStartTime() == var_5_1)
	local var_5_4 = _.all(arg_5_1, function(arg_7_0)
		return arg_7_0.stopTime == var_5_2)
	local var_5_5 = var_5_0

	if not var_5_4:
		table.sort(arg_5_1, function(arg_8_0, arg_8_1)
			return arg_8_0.stopTime < arg_8_1.stopTime)

		var_5_5 = arg_5_1[1]
	elif not var_5_3 and var_5_4:
		table.sort(arg_5_1, function(arg_9_0, arg_9_1)
			return arg_9_0.getStartTime() < arg_9_1.getStartTime())

		var_5_5 = arg_5_1[1]

	return i18n("shop_street_activity_tip", var_5_5.GetShopTime())

def var_0_0.GenHelpContent(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_2.getConfig("config_data")

	for iter_10_0, iter_10_1 in ipairs(var_10_0):
		local var_10_1 = iter_10_1[1]
		local var_10_2 = pg.shop_template[var_10_1].effect_args[1]
		local var_10_3 = Item.getConfigData(var_10_2).name
		local var_10_4 = arg_10_2.GetShopTime()

		table.insert(arg_10_1, i18n("shop_street_Equipment_skin_box_help", var_10_3, var_10_4))

def var_0_0.OnInit(arg_11_0):
	onButton(arg_11_0, arg_11_0.helpBtn, function()
		local var_12_0 = {}

		table.sort(arg_11_0.activitys, function(arg_13_0, arg_13_1)
			return arg_13_0.getStartTime() < arg_13_1.getStartTime())
		_.each(arg_11_0.activitys, function(arg_14_0)
			arg_11_0.GenHelpContent(var_12_0, arg_14_0))

		local var_12_1 = table.concat(var_12_0, "\n\n")

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = var_12_1
		}), SFX_PANEL)
	onButton(arg_11_0, arg_11_0.refreshBtn, function()
		local var_15_0 = ShoppingStreet.getRiseShopId(ShopArgs.ShoppingStreetUpgrade, arg_11_0.shop.flashCount)

		if not var_15_0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("shopStreet_refresh_max_count"))

			return

		local var_15_1 = pg.shop_template[var_15_0]

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			noText = "text_cancel",
			hideNo = False,
			yesText = "text_confirm",
			content = i18n("refresh_shopStreet_question", i18n("word_" .. id2res(var_15_1.resource_type) .. "_icon"), var_15_1.resource_num, arg_11_0.shop.flashCount),
			def onYes:()
				arg_11_0.emit(NewShopsMediator.REFRESH_STREET_SHOP, var_15_0)
		}), SFX_PANEL)

def var_0_0.ResUISettings(arg_17_0):
	return {
		showType = PlayerResUI.TYPE_ALL
	}

def var_0_0.OnUpdatePlayer(arg_18_0):
	local var_18_0 = arg_18_0.player

def var_0_0.OnSetUp(arg_19_0):
	arg_19_0.RemoveTimer()
	arg_19_0.AddTimer()

def var_0_0.OnUpdateAll(arg_20_0):
	arg_20_0.InitCommodities()
	arg_20_0.OnSetUp()

def var_0_0.OnUpdateCommodity(arg_21_0, arg_21_1):
	local var_21_0

	for iter_21_0, iter_21_1 in pairs(arg_21_0.cards):
		if iter_21_1.goodsVO.id == arg_21_1.id:
			var_21_0 = iter_21_1

	if var_21_0:
		var_21_0.update(arg_21_1)

def var_0_0.OnInitItem(arg_22_0, arg_22_1):
	local var_22_0 = GoodsCard.New(arg_22_1)

	onButton(arg_22_0, var_22_0.go, function()
		local var_23_0 = var_22_0.goodsVO

		if not var_23_0.canPurchase():
			pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit"))

			return

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			yesText = "text_exchange",
			type = MSGBOX_TYPE_SINGLE_ITEM,
			drop = {
				id = var_23_0.getConfig("effect_args")[1],
				type = var_23_0.getConfig("type"),
				count = var_23_0.getConfig("num")
			},
			def onYes:()
				arg_22_0.Purchase(var_23_0)
		}), SFX_PANEL)

	arg_22_0.cards[arg_22_1] = var_22_0

def var_0_0.OnUpdateItem(arg_25_0, arg_25_1, arg_25_2):
	local var_25_0 = arg_25_0.cards[arg_25_2]

	if not var_25_0:
		arg_25_0.OnInitItem(arg_25_2)

		var_25_0 = arg_25_0.cards[arg_25_2]

	local var_25_1 = arg_25_0.displays[arg_25_1 + 1]

	var_25_0.update(var_25_1)

def var_0_0.Purchase(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_1.getConfig("resource_type")

	if var_26_0 == 4 or var_26_0 == 14:
		local var_26_1 = arg_26_0.player.getResById(var_26_0)
		local var_26_2 = Item.New({
			id = arg_26_1.getConfig("effect_args")[1]
		})
		local var_26_3 = arg_26_1.getConfig("resource_num") * (arg_26_1.discount / 100)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("charge_scene_buy_confirm", var_26_3, var_26_2.getConfig("name")),
			def onYes:()
				arg_26_0.emit(NewShopsMediator.ON_SHOPPING, arg_26_1.id, 1)
		})
	else
		arg_26_0.emit(NewShopsMediator.ON_SHOPPING, arg_26_1.id, 1)

def var_0_0.RemoveTimer(arg_28_0):
	if arg_28_0.timer:
		arg_28_0.timer.Stop()

		arg_28_0.timer = None

def var_0_0.AddTimer(arg_29_0):
	local var_29_0 = arg_29_0.shop

	arg_29_0.timer = Timer.New(function()
		if var_29_0.isUpdateGoods():
			arg_29_0.RemoveTimer()
			arg_29_0.emit(NewShopsMediator.REFRESH_STREET_SHOP)
		else
			local var_30_0 = pg.TimeMgr.GetInstance().GetServerTime()
			local var_30_1 = var_29_0.nextFlashTime - var_30_0

			arg_29_0.timerText.text = pg.TimeMgr.GetInstance().DescCDTime(var_30_1), 1, -1)

	arg_29_0.timer.Start()
	arg_29_0.timer.func()

def var_0_0.OnDestroy(arg_31_0):
	arg_31_0.RemoveTimer()

	if arg_31_0.isShowing():
		arg_31_0.Hide()

return var_0_0
