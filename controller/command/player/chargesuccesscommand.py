local var_0_0 = class("ChargeSuccessCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shopId
	local var_1_2 = var_1_0.payId
	local var_1_3 = var_1_0.gem
	local var_1_4 = var_1_0.gem_free
	local var_1_5 = Goods.Create({
		shop_id = var_1_1
	}, Goods.TYPE_CHARGE)
	local var_1_6 = getProxy(PlayerProxy)
	local var_1_7 = var_1_6.getData()

	if var_1_3 > 0:
		var_1_7.addResources({
			gem = var_1_3
		})

	if var_1_4 > 0:
		var_1_7.addResources({
			freeGem = var_1_4
		})

	if var_1_5.isMonthCard():
		local var_1_8 = var_1_7.getCardById(VipCard.MONTH)
		local var_1_9 = GetZeroTime() + 2419200

		if var_1_8 and var_1_8.leftDate != 0:
			var_1_8.leftDate = var_1_8.leftDate + 2592000
		else
			var_1_8 = VipCard.New({
				data = 0,
				type = VipCard.MONTH,
				left_date = var_1_9
			})

		var_1_7.addVipCard(var_1_8)

	var_1_6.updatePlayer(var_1_7)

	if var_1_5.isMonthCard():
		MonthCardOutDateTipPanel.SetMonthCardEndDateLocal()
		MonthCardOutDateTipPanel.SetMonthCardTipDate(0)

	local var_1_10 = getProxy(ShopsProxy)
	local var_1_11 = var_1_10.getChargedList() or {}
	local var_1_12 = False

	for iter_1_0, iter_1_1 in pairs(var_1_11):
		if iter_1_1.id == var_1_1:
			var_1_11[iter_1_0].increaseBuyCount()

			var_1_12 = True

			break

	if not var_1_12:
		var_1_11[var_1_1] = Goods.Create({
			pay_count = 1,
			shop_id = var_1_1
		}, Goods.TYPE_CHARGE)

	var_1_10.setChargedList(var_1_11)

	local var_1_13 = var_1_10.getFirstChargeList() or {}

	if _.is_empty(var_1_13):
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_PURCHASE_FIRST, var_1_2)

	if var_1_5.firstPayDouble():
		local var_1_14 = var_1_10.getFirstChargeList() or {}

		if not table.contains(var_1_14, var_1_1):
			table.insert(var_1_14, var_1_1)

		var_1_10.setFirstChargeList(var_1_14)

	local var_1_15 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CHARGEAWARD)

	if var_1_15 and var_1_15.data1 == 0:
		var_1_15.data1 = 1

	pg.TipsMgr.GetInstance().ShowTips(i18n("charge_success"))

return var_0_0
