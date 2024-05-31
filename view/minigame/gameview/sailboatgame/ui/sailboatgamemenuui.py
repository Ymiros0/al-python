local var_0_0 = class("SailBoatGameMenuUI")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	var_0_1 = SailBoatGameVo
	arg_1_0._event = arg_1_2
	arg_1_0.menuUI = findTF(arg_1_0._tf, "ui/menuUI")
	arg_1_0.battleScrollRect = GetComponent(findTF(arg_1_0.menuUI, "battList"), typeof(ScrollRect))
	arg_1_0.totalTimes = var_0_1.total_times
	arg_1_0.battleItems = {}
	arg_1_0.dropItems = {}

	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_2_0 = arg_1_0.battleScrollRect.normalizedPosition.y + 1 / (arg_1_0.totalTimes - 4)

		if var_2_0 > 1:
			var_2_0 = 1

		scrollTo(arg_1_0.battleScrollRect, 0, var_2_0), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_3_0 = arg_1_0.battleScrollRect.normalizedPosition.y - 1 / (arg_1_0.totalTimes - 4)

		if var_3_0 < 0:
			var_3_0 = 0

		scrollTo(arg_1_0.battleScrollRect, 0, var_3_0), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnBack"), function()
		arg_1_0._event.emit(SailBoatGameView.CLOSE_GAME), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnRule"), function()
		arg_1_0._event.emit(SailBoatGameView.SHOW_RULE), SFX_CANCEL)

	arg_1_0.btnStart = findTF(arg_1_0.menuUI, "btnStart")

	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnStart"), function()
		arg_1_0._event.emit(SailBoatGameView.OPEN_EQUIP_UI), SFX_CANCEL)

	local var_1_0 = findTF(arg_1_0.menuUI, "tplBattleItem")
	local var_1_1 = var_0_1.drop

	arg_1_0._chapters = {}

	for iter_1_0 = 1, 7:
		local var_1_2 = iter_1_0
		local var_1_3 = tf(instantiate(var_1_0))

		var_1_3.name = "battleItem_" .. iter_1_0

		setParent(var_1_3, findTF(arg_1_0.menuUI, "battList/Viewport/Content"))

		local var_1_4 = iter_1_0
		local var_1_5 = findTF(var_1_3, "icon")
		local var_1_6 = {
			type = var_1_1[iter_1_0][1],
			id = var_1_1[iter_1_0][2],
			amount = var_1_1[iter_1_0][3]
		}

		updateDrop(var_1_5, var_1_6)
		onButton(arg_1_0._event, var_1_5, function()
			arg_1_0._event.emit(BaseUI.ON_DROP, var_1_6), SFX_PANEL)
		table.insert(arg_1_0.dropItems, var_1_5)
		setActive(var_1_3, True)
		table.insert(arg_1_0.battleItems, var_1_3)

		local var_1_7 = var_0_1.GetGameUseTimes()
		local var_1_8 = var_0_1.GetGameTimes()
		local var_1_9 = findTF(arg_1_0.menuUI, "chapter/" .. iter_1_0 .. "/icon_bg/icon")
		local var_1_10 = {
			type = var_1_1[iter_1_0][1],
			id = var_1_1[iter_1_0][2],
			amount = var_1_1[iter_1_0][3]
		}

		updateDrop(var_1_9, var_1_10)
		onButton(arg_1_0._event, var_1_9, function()
			arg_1_0._event.emit(BaseUI.ON_DROP, var_1_10), SFX_PANEL)

		local var_1_11 = findTF(arg_1_0.menuUI, "chapter/" .. iter_1_0)

		onButton(arg_1_0._event, var_1_11, function()
			if var_1_7 == 7 and var_1_8 == 0:
				var_0_1.selectRound = var_1_4

				arg_1_0.update(arg_1_0.mgHubData), SFX_CONFIRM)
		table.insert(arg_1_0._chapters, var_1_11)

def var_0_0.show(arg_10_0, arg_10_1):
	setActive(arg_10_0.menuUI, arg_10_1)

def var_0_0.update(arg_11_0, arg_11_1):
	arg_11_0.mgHubData = arg_11_1

	local var_11_0 = arg_11_0.getGameUsedTimes(arg_11_1)
	local var_11_1 = arg_11_0.getGameTimes(arg_11_1)

	for iter_11_0 = 1, 7:
		setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_open"), False)
		setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_closed"), False)
		setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_clear"), False)
		setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_current"), False)

		if iter_11_0 <= var_11_0:
			SetParent(arg_11_0.dropItems[iter_11_0], findTF(arg_11_0.battleItems[iter_11_0], "state_clear/icon"))
			setActive(arg_11_0.dropItems[iter_11_0], True)
			setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_clear"), True)
		elif iter_11_0 == var_11_0 + 1 and var_11_1 >= 1:
			setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_current"), True)
			SetParent(arg_11_0.dropItems[iter_11_0], findTF(arg_11_0.battleItems[iter_11_0], "state_current/icon"))
			setActive(arg_11_0.dropItems[iter_11_0], True)
		elif var_11_0 < iter_11_0 and iter_11_0 <= var_11_0 + var_11_1:
			setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_open"), True)
			SetParent(arg_11_0.dropItems[iter_11_0], findTF(arg_11_0.battleItems[iter_11_0], "state_open/icon"))
			setActive(arg_11_0.dropItems[iter_11_0], True)
		else
			setActive(findTF(arg_11_0.battleItems[iter_11_0], "state_closed"), True)
			SetParent(arg_11_0.dropItems[iter_11_0], findTF(arg_11_0.battleItems[iter_11_0], "state_closed/icon"))
			setActive(arg_11_0.dropItems[iter_11_0], True)

		setActive(findTF(arg_11_0._chapters[iter_11_0], "close"), False)
		setActive(findTF(arg_11_0._chapters[iter_11_0], "got"), False)
		setActive(findTF(arg_11_0._chapters[iter_11_0], "active"), False)
		setActive(findTF(arg_11_0._chapters[iter_11_0], "icon_bg"), False)

		if iter_11_0 <= var_11_0:
			setActive(findTF(arg_11_0._chapters[iter_11_0], "got"), True)
		elif iter_11_0 == var_11_0 + 1 and var_11_1 >= 1:
			setActive(findTF(arg_11_0._chapters[iter_11_0], "active"), True)
			setActive(findTF(arg_11_0._chapters[iter_11_0], "icon_bg"), True)
		elif var_11_0 < iter_11_0 and iter_11_0 <= var_11_0 + var_11_1:
			-- block empty
		else
			setActive(findTF(arg_11_0._chapters[iter_11_0], "close"), True)

		if var_0_1.selectRound == iter_11_0:
			setActive(findTF(arg_11_0._chapters[iter_11_0], "active"), True)

	local var_11_2 = 1 - (var_11_0 - 3 < 0 and 0 or var_11_0 - 3) / (arg_11_0.totalTimes - 4)

	if var_11_2 > 1:
		var_11_2 = 1

	scrollTo(arg_11_0.battleScrollRect, 0, var_11_2)

def var_0_0.CheckGet(arg_12_0):
	local var_12_0 = arg_12_0.mgHubData

	setActive(findTF(arg_12_0.menuUI, "got"), False)

	local var_12_1 = arg_12_0.getUltimate(var_12_0)

	if var_12_1 and var_12_1 != 0:
		setActive(findTF(arg_12_0.menuUI, "got"), True)

	if var_12_1 == 0:
		if var_0_1.total_times > arg_12_0.getGameUsedTimes(var_12_0):
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_12_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_12_0.menuUI, "got"), True)

def var_0_0.getGameTimes(arg_13_0, arg_13_1):
	return arg_13_1.count

def var_0_0.getGameUsedTimes(arg_14_0, arg_14_1):
	return arg_14_1.usedtime

def var_0_0.getUltimate(arg_15_0, arg_15_1):
	return arg_15_1.ultimate

return var_0_0
