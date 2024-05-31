local var_0_0 = class("PipeGameMenuUI")
local var_0_1

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._tf = arg_1_1
	var_0_1 = PipeGameVo
	arg_1_0._event = arg_1_2
	arg_1_0.menuUI = findTF(arg_1_0._tf, "ui/menuUI")
	arg_1_0.battleScrollRect = GetComponent(findTF(arg_1_0.menuUI, "battList"), typeof(ScrollRect))
	arg_1_0.totalTimes = var_0_1.total_times
	arg_1_0.battleItems = {}
	arg_1_0.dropItems = {}
	arg_1_0.textLastTimes = findTF(arg_1_0.menuUI, "lastTimes/desc")
	arg_1_0.btnRank = findTF(arg_1_0.menuUI, "btnRank")
	arg_1_0.btnHome = findTF(arg_1_0.menuUI, "btnHome")
	arg_1_0.imgHelp = findTF(arg_1_0.menuUI, "imgHelp")

	setActive(arg_1_0.imgHelp, false)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "rightPanelBg/arrowUp"), function()
		local var_2_0 = arg_1_0.battleScrollRect.normalizedPosition.y + 1 / (arg_1_0.totalTimes - 4)

		if var_2_0 > 1 then
			var_2_0 = 1
		end

		scrollTo(arg_1_0.battleScrollRect, 0, var_2_0)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "rightPanelBg/arrowDown"), function()
		local var_3_0 = arg_1_0.battleScrollRect.normalizedPosition.y - 1 / (arg_1_0.totalTimes - 4)

		if var_3_0 < 0 then
			var_3_0 = 0
		end

		scrollTo(arg_1_0.battleScrollRect, 0, var_3_0)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnBack"), function()
		arg_1_0._event:emit(PipeGameEvent.CLOSE_GAME)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnRule"), function()
		setActive(arg_1_0.imgHelp, true)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, arg_1_0.imgHelp, function()
		setActive(arg_1_0.imgHelp, false)
	end, SFX_CANCEL)

	arg_1_0.btnStart = findTF(arg_1_0.menuUI, "btnStart")

	onButton(arg_1_0._event, arg_1_0.btnStart, function()
		arg_1_0._event:emit(PipeGameEvent.READY_START)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, arg_1_0.btnRank, function()
		arg_1_0._event:emit(PipeGameEvent.SHOW_RANK)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, arg_1_0.btnHome, function()
		arg_1_0._event:emit(PipeGameEvent.ON_HOME)
	end, SFX_CANCEL)

	local var_1_0 = findTF(arg_1_0.menuUI, "tplBattleItem")
	local var_1_1 = var_0_1.drop

	for iter_1_0 = 1, 7 do
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
			arg_1_0._event:emit(BaseUI.ON_DROP, var_1_6)
		end, SFX_PANEL)
		table.insert(arg_1_0.dropItems, var_1_5)
		setActive(var_1_3, true)
		table.insert(arg_1_0.battleItems, var_1_3)

		local var_1_7 = var_0_1.GetGameUseTimes()
		local var_1_8 = var_0_1.GetGameTimes()
	end
end

function var_0_0.show(arg_11_0, arg_11_1)
	setActive(arg_11_0.menuUI, arg_11_1)
end

function var_0_0.update(arg_12_0, arg_12_1)
	arg_12_0.mgHubData = arg_12_1

	local var_12_0 = arg_12_0:getGameUsedTimes(arg_12_1)
	local var_12_1 = arg_12_0:getGameTimes(arg_12_1)

	setText(arg_12_0.textLastTimes, var_12_1)

	for iter_12_0 = 1, 7 do
		setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_open"), false)
		setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_closed"), false)
		setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_clear"), false)
		setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_current"), false)

		if iter_12_0 <= var_12_0 then
			SetParent(arg_12_0.dropItems[iter_12_0], findTF(arg_12_0.battleItems[iter_12_0], "state_clear/icon"))
			setActive(arg_12_0.dropItems[iter_12_0], true)
			setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_clear"), true)
		elseif iter_12_0 == var_12_0 + 1 and var_12_1 >= 1 then
			setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_current"), true)
			SetParent(arg_12_0.dropItems[iter_12_0], findTF(arg_12_0.battleItems[iter_12_0], "state_current/icon"))
			setActive(arg_12_0.dropItems[iter_12_0], true)
		elseif var_12_0 < iter_12_0 and iter_12_0 <= var_12_0 + var_12_1 then
			setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_open"), true)
			SetParent(arg_12_0.dropItems[iter_12_0], findTF(arg_12_0.battleItems[iter_12_0], "state_open/icon"))
			setActive(arg_12_0.dropItems[iter_12_0], true)
		else
			setActive(findTF(arg_12_0.battleItems[iter_12_0], "state_closed"), true)
			SetParent(arg_12_0.dropItems[iter_12_0], findTF(arg_12_0.battleItems[iter_12_0], "state_closed/icon"))
			setActive(arg_12_0.dropItems[iter_12_0], true)
		end
	end

	local var_12_2 = 1 - (var_12_0 - 3 < 0 and 0 or var_12_0 - 3) / (arg_12_0.totalTimes - 4)

	if var_12_2 > 1 then
		var_12_2 = 1
	end

	scrollTo(arg_12_0.battleScrollRect, 0, var_12_2)
end

function var_0_0.CheckGet(arg_13_0)
	local var_13_0 = arg_13_0.mgHubData

	setActive(findTF(arg_13_0.menuUI, "got"), false)

	local var_13_1 = arg_13_0:getUltimate(var_13_0)

	if var_13_1 and var_13_1 ~= 0 then
		setActive(findTF(arg_13_0.menuUI, "got"), true)
	end

	if var_13_1 == 0 then
		if var_0_1.total_times > arg_13_0:getGameUsedTimes(var_13_0) then
			return
		end

		pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_13_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_13_0.menuUI, "got"), true)
	end
end

function var_0_0.getGameTimes(arg_14_0, arg_14_1)
	return arg_14_1.count
end

function var_0_0.getGameUsedTimes(arg_15_0, arg_15_1)
	return arg_15_1.usedtime
end

function var_0_0.getUltimate(arg_16_0, arg_16_1)
	return arg_16_1.ultimate
end

return var_0_0
