local var_0_0 = class("MonthCardOutDateTipPanel", import(".MsgboxSubPanel"))

def var_0_0.SetMonthCardEndDateLocal():
	local var_1_0 = getProxy(PlayerProxy).getRawData()

	if not var_1_0 or not var_1_0.id:
		return

	local var_1_1 = var_1_0.getCardById(VipCard.MONTH)

	if not var_1_1 or var_1_1.leftDate == 0:
		return

	PlayerPrefs.SetInt("MonthCardEndDate" .. var_1_0.id, var_1_1.getLeftDate())
	PlayerPrefs.Save()

def var_0_0.GetMonthCardEndDate():
	local var_2_0 = getProxy(PlayerProxy).getRawData()

	if not var_2_0 or not var_2_0.id:
		return 0

	return PlayerPrefs.GetInt("MonthCardEndDate" .. var_2_0.id, 0)

def var_0_0.SetMonthCardTipDate(arg_3_0):
	if not arg_3_0:
		return

	local var_3_0 = getProxy(PlayerProxy).getRawData()

	if not var_3_0 or not var_3_0.id:
		return

	PlayerPrefs.SetInt("MonthCardTipDate" .. var_3_0.id, arg_3_0)
	PlayerPrefs.Save()

def var_0_0.GetMonthCardTipDate():
	local var_4_0 = getProxy(PlayerProxy).getRawData()

	if not var_4_0 or not var_4_0.id:
		return 0

	return PlayerPrefs.GetInt("MonthCardTipDate" .. var_4_0.id, 0)

def var_0_0.SetMonthCardTagDate():
	local var_5_0 = getProxy(PlayerProxy).getRawData()

	if not var_5_0 or not var_5_0.id:
		return

	local var_5_1 = pg.TimeMgr.GetInstance().GetNextTime(0, 0, 0)

	PlayerPrefs.SetInt("MonthCardTagDate" .. var_5_0.id, var_5_1)
	PlayerPrefs.Save()

def var_0_0.GetShowMonthCardTag():
	local var_6_0 = getProxy(PlayerProxy).getRawData()

	if not var_6_0 or not var_6_0.id:
		return False

	local var_6_1 = var_6_0.getCardById(VipCard.MONTH)

	if not var_6_1 or var_6_1.leftDate == 0:
		return False

	local var_6_2 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_6_3 = var_6_1.getLeftDate()

	if var_6_2 < var_6_3 - 259200 or var_6_3 < var_6_2:
		return False

	return var_6_2 > PlayerPrefs.GetInt("MonthCardTagDate" .. var_6_0.id, 0)

def var_0_0.TryShowMonthCardTipPanel(arg_7_0):
	local function var_7_0()
		if arg_7_0:
			arg_7_0()

	local var_7_1 = var_0_0.GetMonthCardEndDate()

	if var_7_1 == 0:
		var_7_0()

		return

	local var_7_2 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_7_3 = var_0_0.GetMonthCardTipDate()

	if var_7_2 >= var_7_1 - 259200 and var_7_3 < var_7_1 - 259200:
		var_0_0.SetMonthCardTipDate(var_7_2)

		local var_7_4 = pg.TimeMgr.GetInstance().STimeDescS(math.min(var_7_2, var_7_1), "*t")
		local var_7_5 = i18n("trade_card_tips4", var_7_4.year, var_7_4.month, var_7_4.day)
		local var_7_6 = pg.TimeMgr.GetInstance().STimeDescS(var_7_1, "*t")
		local var_7_7 = i18n("trade_card_tips4", var_7_6.year, var_7_6.month, var_7_6.day)
		local var_7_8 = var_7_1 <= var_7_2

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			type = MSGBOX_TYPE_MONTH_CARD_TIP,
			title = pg.MsgboxMgr.TITLE_INFORMATION,
			content = i18n(var_7_8 and "trade_card_tips2" or "trade_card_tips3", var_7_7),
			dateText = var_7_5,
			yesText = i18n("trade_card_tips1"),
			weight = LayerWeightConst.TOP_LAYER,
			onClose = var_7_0,
			def onYes:()
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.CHARGE, {
					confirmMonthCard = True,
					wrap = ChargeScene.TYPE_DIAMOND
				})
		})

		return

	var_7_0()

def var_0_0.getUIName(arg_10_0):
	return "Msgbox4MonthCardTip"

def var_0_0.Init(arg_11_0):
	var_0_0.super.Init(arg_11_0)
	setText(arg_11_0._tf.Find("NameText"), pg.ship_data_statistics[312011].name)

def var_0_0.UpdateView(arg_12_0, arg_12_1):
	arg_12_0.PreRefresh(arg_12_1)

	rtf(arg_12_0.viewParent._window).sizeDelta = Vector2.New(960, 685)

	setText(arg_12_0._tf.Find("Desc"), arg_12_1.content)
	setText(arg_12_0._tf.Find("Date"), arg_12_1.dateText)
	arg_12_0.PostRefresh(arg_12_1)

return var_0_0
