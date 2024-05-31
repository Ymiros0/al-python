local var_0_0 = class("GameRoomCoinLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "GameRoomCoinUI"

def var_0_0.init(arg_2_0):
	arg_2_0.totalCount = 0
	arg_2_0.curCount = 0
	arg_2_0.maxCoin = 0

def var_0_0.didEnter(arg_3_0):
	arg_3_0.window = findTF(arg_3_0._tf, "ad/window")
	arg_3_0.text = findTF(arg_3_0._tf, "ad/window/text")

	local var_3_0 = arg_3_0.contextData.position

	arg_3_0.window.anchoredPosition = Vector2(var_3_0[1], var_3_0[2])
	arg_3_0.maxCoin = arg_3_0.contextData.coin_max

	onButton(arg_3_0, findTF(arg_3_0.window, "add"), function()
		if arg_3_0.lockCount:
			return

		arg_3_0.curCount = arg_3_0.curCount + 1

		arg_3_0.updateCount())
	onButton(arg_3_0, findTF(arg_3_0.window, "sub"), function()
		if arg_3_0.lockCount:
			return

		arg_3_0.curCount = arg_3_0.curCount - 1

		arg_3_0.updateCount())

	local var_3_1 = getProxy(GameRoomProxy)

	if var_3_1.lastMonthlyTicket() == 0 or var_3_1.lastTicketMax() == 0:
		arg_3_0.curCount = 0
		arg_3_0.lockCount = True
	else
		arg_3_0.curCount = 1
		arg_3_0.lockCount = False

	arg_3_0.updateUI()

def var_0_0.changeVisible(arg_6_0, arg_6_1):
	setActive(arg_6_0.window, arg_6_1)
	arg_6_0.updateUI()

def var_0_0.updateUI(arg_7_0):
	arg_7_0.updateCoin()
	arg_7_0.updateCount()

def var_0_0.updateCoin(arg_8_0):
	arg_8_0.totalCount = getProxy(GameRoomProxy).getCoin() or 0

	if arg_8_0.curCount > arg_8_0.totalCount:
		arg_8_0.curCount = 0

def var_0_0.updateCount(arg_9_0):
	if arg_9_0.curCount > arg_9_0.maxCoin:
		arg_9_0.curCount = arg_9_0.maxCoin

	if arg_9_0.curCount > arg_9_0.totalCount:
		arg_9_0.curCount = arg_9_0.totalCount

	if arg_9_0.curCount < 0:
		arg_9_0.curCount = 0

	setText(arg_9_0.text, arg_9_0.curCount .. "/" .. arg_9_0.totalCount)
	arg_9_0.emit(GameRoomCoinMediator.CHANGE_COIN_NUM, arg_9_0.curCount)

def var_0_0.onBackPressed(arg_10_0):
	return

def var_0_0.willExit(arg_11_0):
	return

return var_0_0
