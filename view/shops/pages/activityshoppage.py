local var_0_0 = class("ActivityShopPage", import(".BaseShopPage"))

def var_0_0.getUIName(arg_1_0):
	return "ActivityShop"

def var_0_0.GetPaintingName(arg_2_0):
	assert(arg_2_0.shop)

	local var_2_0 = pg.activity_template[arg_2_0.shop.activityId]
	local var_2_1 = getProxy(ActivityProxy).checkHxActivity(arg_2_0.shop.activityId)

	if var_2_0 and var_2_0.config_client:
		if var_2_0.config_client.use_secretary or var_2_1:
			local var_2_2 = getProxy(PlayerProxy).getData()
			local var_2_3 = getProxy(SettingsProxy).getCurrentSecretaryIndex()

			arg_2_0.tempFlagShip = getProxy(BayProxy).getShipById(var_2_2.characters[1])

			return arg_2_0.tempFlagShip.getPainting(), True, "build"
		elif var_2_0.config_client.painting:
			return var_2_0.config_client.painting

	return "aijiang_pt"

def var_0_0.GetBg(arg_3_0, arg_3_1):
	return (arg_3_1.getBgPath())

def var_0_0.GetPaintingEnterVoice(arg_4_0):
	local var_4_0, var_4_1, var_4_2 = arg_4_0.shop.GetEnterVoice()

	return var_4_1, var_4_0, var_4_2

def var_0_0.GetPaintingCommodityUpdateVoice(arg_5_0):
	local var_5_0, var_5_1, var_5_2 = arg_5_0.shop.GetPurchaseVoice()

	return var_5_1, var_5_0, var_5_2

def var_0_0.GetPaintingAllPurchaseVoice(arg_6_0):
	local var_6_0, var_6_1, var_6_2 = arg_6_0.shop.GetPurchaseAllVoice()

	return var_6_1, var_6_0, var_6_2

def var_0_0.GetPaintingTouchVoice(arg_7_0):
	local var_7_0, var_7_1, var_7_2 = arg_7_0.shop.GetTouchVoice()

	return var_7_1, var_7_0, var_7_2

def var_0_0.OnLoaded(arg_8_0):
	local var_8_0 = arg_8_0.findTF("res_battery").GetComponent(typeof(Image))
	local var_8_1 = arg_8_0.findTF("res_battery/icon").GetComponent(typeof(Image))
	local var_8_2 = arg_8_0.findTF("res_battery/Text").GetComponent(typeof(Text))
	local var_8_3 = arg_8_0.findTF("res_battery/label").GetComponent(typeof(Text))
	local var_8_4 = arg_8_0.findTF("res_battery1").GetComponent(typeof(Image))
	local var_8_5 = arg_8_0.findTF("res_battery1/icon").GetComponent(typeof(Image))
	local var_8_6 = arg_8_0.findTF("res_battery1/Text").GetComponent(typeof(Text))
	local var_8_7 = arg_8_0.findTF("res_battery1/label").GetComponent(typeof(Text))

	arg_8_0.resTrList = {
		{
			var_8_0,
			var_8_1,
			var_8_2,
			var_8_3
		},
		{
			var_8_4,
			var_8_5,
			var_8_6,
			var_8_7
		}
	}
	arg_8_0.eventResCnt = arg_8_0.findTF("event_res_battery/Text").GetComponent(typeof(Text))
	arg_8_0.time = arg_8_0.findTF("Text").GetComponent(typeof(Text))

def var_0_0.OnInit(arg_9_0):
	return

def var_0_0.OnUpdatePlayer(arg_10_0):
	if arg_10_0.shop.IsEventShop():
		local var_10_0 = arg_10_0.shop.getResId()

		arg_10_0.eventResCnt.text = arg_10_0.player.getResource(var_10_0)
	else
		local var_10_1 = arg_10_0.shop.GetResList()

		for iter_10_0, iter_10_1 in pairs(arg_10_0.resTrList):
			local var_10_2 = iter_10_1[1]
			local var_10_3 = iter_10_1[2]
			local var_10_4 = iter_10_1[3]
			local var_10_5 = var_10_1[iter_10_0]

			setActive(var_10_2, var_10_5 != None)

			if var_10_5 != None:
				var_10_4.text = arg_10_0.player.getResource(var_10_5)

def var_0_0.OnSetUp(arg_11_0):
	arg_11_0.SetResIcon()
	arg_11_0.UpdateTip()

def var_0_0.OnUpdateAll(arg_12_0):
	arg_12_0.InitCommodities()

def var_0_0.OnUpdateCommodity(arg_13_0, arg_13_1):
	local var_13_0

	for iter_13_0, iter_13_1 in pairs(arg_13_0.cards):
		if iter_13_1.goodsVO.id == arg_13_1.id:
			var_13_0 = iter_13_1

			break

	if var_13_0:
		local var_13_1, var_13_2, var_13_3 = arg_13_0.shop.getBgPath()

		var_13_0.update(arg_13_1, None, var_13_2, var_13_3)

def var_0_0.SetResIcon(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0.shop.GetResList()

	for iter_14_0, iter_14_1 in ipairs(arg_14_0.resTrList):
		local var_14_1 = iter_14_1[1]
		local var_14_2 = iter_14_1[2]
		local var_14_3 = iter_14_1[3]
		local var_14_4 = iter_14_1[4]
		local var_14_5 = var_14_0[iter_14_0]

		if var_14_5 != None:
			local var_14_6 = Drop.New({
				type = arg_14_1 or DROP_TYPE_RESOURCE,
				id = var_14_5
			})

			GetSpriteFromAtlasAsync(var_14_6.getIcon(), "", function(arg_15_0)
				var_14_2.sprite = arg_15_0)

			var_14_4.text = var_14_6.getName()

	local var_14_7 = arg_14_0.shop.IsEventShop()

	setActive(arg_14_0.findTF("res_battery"), not var_14_7)
	setActive(arg_14_0.findTF("res_battery1"), not var_14_7 and #var_14_0 > 1)
	setActive(arg_14_0.findTF("event_res_battery"), var_14_7)

def var_0_0.UpdateTip(arg_16_0):
	local var_16_0 = #arg_16_0.shop.GetResList() > 1 and 25 or 27

	arg_16_0.time.text = "<size=" .. var_16_0 .. ">" .. i18n("activity_shop_lable", arg_16_0.shop.getOpenTime()) .. "</size>"

def var_0_0.OnInitItem(arg_17_0, arg_17_1):
	local var_17_0 = ActivityGoodsCard.New(arg_17_1)

	var_17_0.tagImg.raycastTarget = False

	onButton(arg_17_0, var_17_0.tr, function()
		arg_17_0.OnClickCommodity(var_17_0.goodsVO, function(arg_19_0, arg_19_1)
			arg_17_0.OnPurchase(arg_19_0, arg_19_1)), SFX_PANEL)

	arg_17_0.cards[arg_17_1] = var_17_0

def var_0_0.OnUpdateItem(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0 = arg_20_0.cards[arg_20_2]

	if not var_20_0:
		arg_20_0.OnInitItem(arg_20_2)

		var_20_0 = arg_20_0.cards[arg_20_2]

	local var_20_1 = arg_20_0.displays[arg_20_1 + 1]
	local var_20_2, var_20_3, var_20_4 = arg_20_0.shop.getBgPath()

	var_20_0.update(var_20_1, None, var_20_3, var_20_4)

def var_0_0.TipPurchase(arg_21_0, arg_21_1, arg_21_2, arg_21_3, arg_21_4):
	local var_21_0, var_21_1 = arg_21_1.GetTranCntWhenFull(arg_21_2)

	if var_21_0 > 0:
		local var_21_2 = math.max(arg_21_2 - var_21_0, 0)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("pt_shop_tran_tip", var_21_2, arg_21_3, var_21_0 * var_21_1.count, var_21_1.getConfig("name")),
			onYes = arg_21_4
		})
	else
		arg_21_4()

def var_0_0.OnPurchase(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_1.getConfig("commodity_type")
	local var_22_1 = arg_22_1.getConfig("commodity_id")

	if var_22_0 == DROP_TYPE_ITEM:
		local var_22_2 = getProxy(BagProxy).RawGetItemById(var_22_1)

		if var_22_2 and var_22_2.IsShipExpType() and var_22_2.IsMaxCnt():
			pg.TipsMgr.GetInstance().ShowTips(i18n("item_is_max_cnt"))

			return

	local var_22_3 = arg_22_0.shop.activityId

	arg_22_0.emit(NewShopsMediator.ON_ACT_SHOPPING, var_22_3, 1, arg_22_1.id, arg_22_2)
	arg_22_0.emit(NewShopsMediator.UR_EXCHANGE_TRACKING, var_22_1)

def var_0_0.OnClickCommodity(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = arg_23_1.CheckCntLimit()

	if not var_23_0:
		return

	if var_23_0 and not arg_23_1.CheckArgLimit():
		local var_23_1, var_23_2, var_23_3, var_23_4 = arg_23_1.CheckArgLimit()

		if var_23_2 == ShopArgs.LIMIT_ARGS_META_SHIP_EXISTENCE:
			local var_23_5 = ShipGroup.getDefaultShipConfig(var_23_4) or {}

			pg.TipsMgr.GetInstance().ShowTips(i18n("meta_shop_exchange_limit_tip", var_23_5.name or ""))
		elif var_23_2 == ShopArgs.LIMIT_ARGS_SALE_START_TIME:
			local var_23_6 = {
				year = var_23_4[1][1],
				month = var_23_4[1][2],
				day = var_23_4[1][3],
				hour = var_23_4[2][1],
				min = var_23_4[2][2],
				sec = var_23_4[2][3]
			}

			pg.TipsMgr.GetInstance().ShowTips(i18n("meta_shop_exchange_limit_2_tip", var_23_6.year, var_23_6.month, var_23_6.day, var_23_6.hour, var_23_6.min, var_23_6.sec))

		return

	var_0_0.super.OnClickCommodity(arg_23_0, arg_23_1, arg_23_2)

def var_0_0.Show(arg_24_0):
	var_0_0.super.Show(arg_24_0)

	if arg_24_0.shop.GetBGM() != "":
		pg.BgmMgr.GetInstance().Push(arg_24_0.__cname, arg_24_0.shop.GetBGM())

def var_0_0.Hide(arg_25_0):
	var_0_0.super.Hide(arg_25_0)

	if arg_25_0.shop.GetBGM() != "":
		pg.BgmMgr.GetInstance().Pop(arg_25_0.__cname)

return var_0_0
