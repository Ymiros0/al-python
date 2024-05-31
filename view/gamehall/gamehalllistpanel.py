local var_0_0 = class("GameHallListPanel")
local var_0_1 = False

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.content = findTF(arg_1_0._tf, "ad/viewport/content")
	arg_1_0.listTpl = findTF(arg_1_0.content, "listTpl")

	setActive(arg_1_0.listTpl, False)

	arg_1_0.gameRoomDatas = {}

	for iter_1_0, iter_1_1 in ipairs(pg.game_room_template.all):
		local var_1_0 = pg.game_room_template[iter_1_1].unlock_time

		if pg.TimeMgr.GetInstance().Table2ServerTime({
			year = var_1_0[1][1],
			month = var_1_0[1][2],
			day = var_1_0[1][3],
			hour = var_1_0[2][1],
			min = var_1_0[2][2],
			sec = var_1_0[2][3]
		}) < pg.TimeMgr.GetInstance().GetServerTime():
			table.insert(arg_1_0.gameRoomDatas, Clone(pg.game_room_template[iter_1_1]))

	for iter_1_2 = 1, #arg_1_0.gameRoomDatas:
		local var_1_1 = tf(instantiate(go(arg_1_0.listTpl)))
		local var_1_2 = arg_1_0.gameRoomDatas[iter_1_2]

		setParent(var_1_1, arg_1_0.content)
		setActive(var_1_1, True)

		local var_1_3 = var_1_2.icon
		local var_1_4 = var_1_2.id
		local var_1_5 = getProxy(GameRoomProxy).getRoomScore(var_1_4)

		setActive(findTF(var_1_1, "empty"), var_1_5 == 0)
		setActive(findTF(var_1_1, "total"), var_1_5 > 0)
		setActive(findTF(var_1_1, "txtScore"), var_1_5 > 0)

		local var_1_6

		if var_1_5 < 10:
			var_1_6 = "00" .. var_1_5
		elif var_1_5 < 100:
			var_1_6 = "0" .. var_1_5
		else
			var_1_6 = "" .. var_1_5

		setText(findTF(var_1_1, "txtScore"), var_1_6)
		setImageSprite(findTF(var_1_1, "mask/gameIcon"), LoadSprite("gamehallicon/" .. var_1_3), True)
		onButton(arg_1_0._event, var_1_1, function()
			arg_1_0._event.emit(GameHallMediator.OPEN_MINI_GAME, var_1_2), SFX_CANCEL)

def var_0_0.setVisible(arg_3_0, arg_3_1):
	setActive(arg_3_0._tf, arg_3_1)

	if arg_3_1:
		local var_3_0 = getProxy(GameRoomProxy).ticketMaxTip()

		if var_3_0 and not GameRoomProxy.ticket_remind:
			GameRoomProxy.ticket_remind = True

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = var_3_0,
				def onYes:()
					return,
				def onNo:()
					arg_3_0.setVisible(False)
			})

def var_0_0.getVisible(arg_6_0):
	return isActive(arg_6_0._tf)

def var_0_0.dispose(arg_7_0):
	return

return var_0_0
