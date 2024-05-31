local var_0_0 = class("CastleGameMenuUI")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0.menuUI = findTF(arg_1_0._tf, "ui/menuUI")
	arg_1_0.battleScrollRect = GetComponent(findTF(arg_1_0.menuUI, "battList"), typeof(ScrollRect))
	arg_1_0.totalTimes = CastleGameVo.total_times
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
		arg_1_0._event.emit(BeachGuardGameView.CLOSE_GAME), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnRule"), function()
		arg_1_0._event.emit(BeachGuardGameView.SHOW_RULE), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnStart"), function()
		arg_1_0._event.emit(BeachGuardGameView.READY_START), SFX_CANCEL)

	local var_1_0 = findTF(arg_1_0.menuUI, "tplBattleItem")
	local var_1_1 = CastleGameVo.drop

	for iter_1_0 = 1, 7:
		local var_1_2 = tf(instantiate(var_1_0))

		var_1_2.name = "battleItem_" .. iter_1_0

		setParent(var_1_2, findTF(arg_1_0.menuUI, "battList/Viewport/Content"))

		local var_1_3 = iter_1_0

		GetSpriteFromAtlasAsync(CastleGameVo.ui_atlas, "battleDesc" .. var_1_3, function(arg_7_0)
			if arg_7_0:
				setImageSprite(findTF(var_1_2, "state_open/desc"), arg_7_0, True)
				setImageSprite(findTF(var_1_2, "state_clear/desc"), arg_7_0, True)
				setImageSprite(findTF(var_1_2, "state_current/desc"), arg_7_0, True)
				setImageSprite(findTF(var_1_2, "state_closed/desc"), arg_7_0, True))

		local var_1_4 = findTF(var_1_2, "icon")
		local var_1_5 = {
			type = var_1_1[iter_1_0][1],
			id = var_1_1[iter_1_0][2],
			amount = var_1_1[iter_1_0][3]
		}

		updateDrop(var_1_4, var_1_5)
		onButton(arg_1_0._event, var_1_4, function()
			arg_1_0._event.emit(BaseUI.ON_DROP, var_1_5), SFX_PANEL)
		table.insert(arg_1_0.dropItems, var_1_4)
		setActive(var_1_2, True)
		table.insert(arg_1_0.battleItems, var_1_2)

def var_0_0.show(arg_9_0, arg_9_1):
	setActive(arg_9_0.menuUI, arg_9_1)

def var_0_0.update(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_0.getGameUsedTimes(arg_10_1)
	local var_10_1 = arg_10_0.getGameTimes(arg_10_1)

	for iter_10_0 = 1, #arg_10_0.battleItems:
		setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_open"), False)
		setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_closed"), False)
		setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_clear"), False)
		setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_current"), False)

		if iter_10_0 <= var_10_0:
			SetParent(arg_10_0.dropItems[iter_10_0], findTF(arg_10_0.battleItems[iter_10_0], "state_clear/icon"))
			setActive(arg_10_0.dropItems[iter_10_0], True)
			setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_clear"), True)
		elif iter_10_0 == var_10_0 + 1 and var_10_1 >= 1:
			setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_current"), True)
			SetParent(arg_10_0.dropItems[iter_10_0], findTF(arg_10_0.battleItems[iter_10_0], "state_current/icon"))
			setActive(arg_10_0.dropItems[iter_10_0], True)
		elif var_10_0 < iter_10_0 and iter_10_0 <= var_10_0 + var_10_1:
			setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_open"), True)
			SetParent(arg_10_0.dropItems[iter_10_0], findTF(arg_10_0.battleItems[iter_10_0], "state_open/icon"))
			setActive(arg_10_0.dropItems[iter_10_0], True)
		else
			setActive(findTF(arg_10_0.battleItems[iter_10_0], "state_closed"), True)
			SetParent(arg_10_0.dropItems[iter_10_0], findTF(arg_10_0.battleItems[iter_10_0], "state_closed/icon"))
			setActive(arg_10_0.dropItems[iter_10_0], True)

	local var_10_2 = 1 - (var_10_0 - 3 < 0 and 0 or var_10_0 - 3) / (arg_10_0.totalTimes - 4)

	if var_10_2 > 1:
		var_10_2 = 1

	scrollTo(arg_10_0.battleScrollRect, 0, var_10_2)
	setActive(findTF(arg_10_0.menuUI, "btnStart/tip"), var_10_1 > 0)
	arg_10_0.CheckGet(arg_10_1)

def var_0_0.CheckGet(arg_11_0, arg_11_1):
	setActive(findTF(arg_11_0.menuUI, "got"), False)

	local var_11_0 = arg_11_0.getUltimate(arg_11_1)

	if var_11_0 and var_11_0 != 0:
		setActive(findTF(arg_11_0.menuUI, "got"), True)

	if var_11_0 == 0:
		if CastleGameVo.total_times > arg_11_0.getGameUsedTimes(arg_11_1):
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_11_1.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_11_0.menuUI, "got"), True)

def var_0_0.getGameTimes(arg_12_0, arg_12_1):
	return arg_12_1.count

def var_0_0.getGameUsedTimes(arg_13_0, arg_13_1):
	return arg_13_1.usedtime

def var_0_0.getUltimate(arg_14_0, arg_14_1):
	return arg_14_1.ultimate

return var_0_0
