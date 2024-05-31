local var_0_0 = class("GameRoomProxy", import(".NetProxy"))

var_0_0.coin_res_id = 11
var_0_0.ticket_res_id = 12
var_0_0.ticket_remind = False

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}
	arg_1_0.rooms = {}

	arg_1_0.on(26120, function(arg_2_0)
		arg_1_0.weekly = arg_2_0.weekly_free
		arg_1_0.monthlyTicket = arg_2_0.monthly_ticket

		if arg_2_0.rooms:
			for iter_2_0, iter_2_1 in ipairs(arg_2_0.rooms):
				table.insert(arg_1_0.rooms, {
					roomId = iter_2_1.roomid,
					maxScore = iter_2_1.max_score
				})

		arg_1_0.payCoinCount = arg_2_0.pay_coin_count
		arg_1_0.firstEnter = arg_2_0.first_enter)

def var_0_0.getRoomScore(arg_3_0, arg_3_1):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0.rooms):
		if iter_3_1.roomId == arg_3_1:
			return iter_3_1.maxScore

	return 0

def var_0_0.storeGameScore(arg_4_0, arg_4_1, arg_4_2):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.rooms):
		if iter_4_1.roomId == arg_4_1 and arg_4_2 > iter_4_1.maxScore:
			iter_4_1.maxScore = arg_4_2

			return

	table.insert(arg_4_0.rooms, {
		roomId = arg_4_1,
		maxScore = arg_4_2
	})

def var_0_0.getCoin(arg_5_0):
	return getProxy(PlayerProxy).getRawData().getResource(var_0_0.coin_res_id)

def var_0_0.getTicket(arg_6_0):
	return getProxy(PlayerProxy).getRawData().getResource(var_0_0.ticket_res_id)

def var_0_0.getMonthlyTicket(arg_7_0):
	return arg_7_0.monthlyTicket

def var_0_0.setMonthlyTicket(arg_8_0, arg_8_1):
	arg_8_0.monthlyTicket = arg_8_0.monthlyTicket + arg_8_1

def var_0_0.lastMonthlyTicket(arg_9_0):
	local var_9_0 = pg.gameset.game_ticket_month.key_value - arg_9_0.monthlyTicket

	return var_9_0 < 0 and 0 or var_9_0

def var_0_0.lastTicketMax(arg_10_0):
	local var_10_0 = pg.gameset.game_room_remax.key_value - arg_10_0.getTicket()

	return var_10_0 < 0 and 0 or var_10_0

def var_0_0.ticketMaxTip(arg_11_0):
	if arg_11_0.lastMonthlyTicket() <= 200:
		return i18n("game_ticket_max_month")
	elif arg_11_0.lastTicketMax() <= 200:
		return i18n("game_ticket_max_all")

	return None

def var_0_0.getFirstEnter(arg_12_0):
	return arg_12_0.firstEnter == 0

def var_0_0.getPayCoinCount(arg_13_0):
	return arg_13_0.payCoinCount

def var_0_0.setPayCoinCount(arg_14_0, arg_14_1):
	arg_14_0.payCoinCount = arg_14_0.payCoinCount + arg_14_1

def var_0_0.setFirstEnter(arg_15_0):
	arg_15_0.firstEnter = 1

def var_0_0.getWeekly(arg_16_0):
	return arg_16_0.weekly == 0

def var_0_0.setWeekly(arg_17_0):
	arg_17_0.weekly = 1

def var_0_0.getTip(arg_18_0):
	if arg_18_0.firstEnter == 0:
		return True

	if arg_18_0.weekly == 0:
		return True

	return False

return var_0_0
