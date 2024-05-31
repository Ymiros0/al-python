local var_0_0 = class("MiniGameShopPage", import(".BaseShopPage"))

def var_0_0.getUIName(arg_1_0):
	return "MiniGameShop"

def var_0_0.CanOpen(arg_2_0, arg_2_1, arg_2_2):
	return pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_2_2.level, "GameHallMediator")

def var_0_0.OnLoaded(arg_3_0):
	arg_3_0.mothMaxTF = arg_3_0.findTF("mothMax")

	local var_3_0 = pg.gameset.game_ticket_month.key_value
	local var_3_1 = getProxy(GameRoomProxy).getMonthlyTicket()

	setText(arg_3_0.mothMaxTF, i18n("game_ticket_current_month") .. var_3_1 .. "/" .. var_3_0)

def var_0_0.OnInit(arg_4_0):
	arg_4_0.purchaseWindow = MiniGameShopPurchasePanel.New(arg_4_0._tf, arg_4_0.event)
	arg_4_0.multiWindow = MiniGameShopMultiWindow.New(arg_4_0._tf, arg_4_0.event)
	arg_4_0.ticketTf = findTF(arg_4_0._tf, "res/Text")

	local var_4_0 = getProxy(GameRoomProxy).getTicket()

	setText(arg_4_0.ticketTf, var_4_0)

def var_0_0.OnSetUp(arg_5_0):
	arg_5_0.RemoveTimer()
	arg_5_0.AddTimer()

def var_0_0.OnUpdateAll(arg_6_0):
	arg_6_0.InitCommodities()
	arg_6_0.OnSetUp()

	if arg_6_0.purchaseWindow.isShowing():
		arg_6_0.purchaseWindow.ExecuteAction("Hide")

	if arg_6_0.multiWindow.isShowing():
		arg_6_0.multiWindow.ExecuteAction("Hide")

	local var_6_0 = getProxy(GameRoomProxy).getTicket()

	setText(arg_6_0.ticketTf, var_6_0)

def var_0_0.OnUpdateCommodity(arg_7_0, arg_7_1):
	local var_7_0

	for iter_7_0, iter_7_1 in pairs(arg_7_0.cards):
		if iter_7_1.goodsVO.id == arg_7_1.id:
			var_7_0 = iter_7_1

			break

	if var_7_0:
		var_7_0.update(arg_7_1)

def var_0_0.OnInitItem(arg_8_0, arg_8_1):
	local var_8_0 = MiniGameGoodsCard.New(arg_8_1)

	onButton(arg_8_0, var_8_0.go, function()
		if not var_8_0.goodsVO.CanPurchase():
			pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit"))

			return

		arg_8_0.OnClickCommodity(var_8_0.goodsVO), SFX_PANEL)

	arg_8_0.cards[arg_8_1] = var_8_0

def var_0_0.OnUpdateItem(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_0.cards[arg_10_2]

	if not var_10_0:
		arg_10_0.OnInitItem(arg_10_2)

		var_10_0 = arg_10_0.cards[arg_10_2]

	local var_10_1 = arg_10_0.displays[arg_10_1 + 1]

	var_10_0.update(var_10_1)

def var_0_0.OnClickCommodity(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1

	if var_11_0.Selectable():
		arg_11_0.purchaseWindow.ExecuteAction("Show", {
			id = var_11_0.id,
			count = var_11_0.GetMaxCnt(),
			type = var_11_0.getConfig("type"),
			price = var_11_0.getConfig("price"),
			displays = var_11_0.getConfig("goods"),
			num = var_11_0.getConfig("num"),
			def confirm:(arg_12_0, arg_12_1)
				arg_11_0.emit(NewShopsMediator.ON_MINI_GAME_SHOP_BUY, {
					id = arg_12_0,
					list = arg_12_1
				})
		})
	elif var_11_0.getConfig("goods_type") == 1:
		if var_11_0.GetLimit() > 1:
			arg_11_0.multiWindow.ExecuteAction("Show", var_11_0, function(arg_13_0)
				if not var_11_0.CanPurchaseCnt(arg_13_0):
					pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit"))

					return

				local var_13_0 = {}
				local var_13_1 = var_11_0.getConfig("goods")[1]

				table.insert(var_13_0, {
					num = arg_13_0,
					id = var_13_1
				})
				arg_11_0.emit(NewShopsMediator.ON_MINI_GAME_SHOP_BUY, {
					id = var_11_0.id,
					list = var_13_0
				}))
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				yesText = "text_exchange",
				content = i18n("guild_shop_exchange_tip"),
				def onYes:()
					if not var_11_0.CanPurchase():
						pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit"))

						return

					local var_14_0 = {}
					local var_14_1 = var_11_0.GetFirstDropId()

					for iter_14_0 = 1, #var_14_1:
						table.insert(var_14_0, {
							num = 1,
							id = var_14_1[iter_14_0]
						})

					arg_11_0.emit(NewShopsMediator.ON_MINI_GAME_SHOP_BUY, {
						id = var_11_0.id,
						list = var_14_0
					})
			})

def var_0_0.AddTimer(arg_15_0):
	arg_15_0.timer = Timer.New(function()
		local var_16_0 = tonumber(os.date("%d", pg.TimeMgr.GetInstance().GetServerTime()))

		if not arg_15_0.flush and arg_15_0.day and arg_15_0.day == var_16_0:
			arg_15_0.emit(NewShopsMediator.ON_MINI_GAME_SHOP_FLUSH)

			arg_15_0.flush = True

		arg_15_0.day = var_16_0, 1, -1)

	arg_15_0.timer.Start()

def var_0_0.RemoveTimer(arg_17_0):
	if arg_17_0.timer:
		arg_17_0.timer.Stop()

		arg_17_0.timer = None

def var_0_0.OnDestroy(arg_18_0):
	if arg_18_0.purchaseWindow.isShowing():
		arg_18_0.purchaseWindow.ExecuteAction("Hide")

	if arg_18_0.multiWindow.isShowing():
		arg_18_0.multiWindow.ExecuteAction("Hide")

	arg_18_0.RemoveTimer()

return var_0_0
