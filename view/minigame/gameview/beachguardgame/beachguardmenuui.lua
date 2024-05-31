local var_0_0 = class("BeachGuardMenuUI")
local var_0_1 = "beach_guard_chaijun"
local var_0_2 = "beach_guard_jianye"
local var_0_3 = "beach_guard_lituoliao"
local var_0_4 = "beach_guard_bominghan"
local var_0_5 = "beach_guard_nengdai"
local var_0_6 = "beach_guard_m_craft"
local var_0_7 = "beach_guard_m_atk"
local var_0_8 = "beach_guard_m_guard"
local var_0_9 = "beach_guard_m_craft_name"
local var_0_10 = "beach_guard_m_atk_name"
local var_0_11 = "beach_guard_m_guard_name"
local var_0_12 = "beach_guard_e1"
local var_0_13 = "beach_guard_e2"
local var_0_14 = "beach_guard_e3"
local var_0_15 = "beach_guard_e4"
local var_0_16 = "beach_guard_e5"
local var_0_17 = "beach_guard_e6"
local var_0_18 = "beach_guard_e7"
local var_0_19 = "beach_guard_e1_desc"
local var_0_20 = "beach_guard_e2_desc"
local var_0_21 = "beach_guard_e3_desc"
local var_0_22 = "beach_guard_e4_desc"
local var_0_23 = "beach_guard_e5_desc"
local var_0_24 = "beach_guard_e6_desc"
local var_0_25 = "beach_guard_e7_desc"
local var_0_26 = {
	{
		{
			id = 900913,
			icon = "char_1_icon",
			img = "char_1",
			img_desc = "char_1_desc",
			desc = var_0_1
		},
		{
			id = 319011,
			icon = "char_2_icon",
			img = "char_2",
			img_desc = "char_2_desc",
			desc = var_0_2
		},
		{
			id = 605021,
			icon = "char_3_icon",
			img = "char_3",
			img_desc = "char_3_desc",
			desc = var_0_3
		},
		{
			id = 102231,
			icon = "char_4_icon",
			img = "char_4",
			img_desc = "char_4_desc",
			desc = var_0_4
		},
		{
			id = 302211,
			icon = "char_5_icon",
			img = "char_5",
			img_desc = "char_5_desc",
			desc = var_0_5
		},
		{
			img = "m_craft",
			icon = "m_craft_icon",
			name = var_0_9,
			desc = var_0_6
		},
		{
			img = "m_atk",
			icon = "m_atk_icon",
			name = var_0_10,
			desc = var_0_7
		},
		{
			img = "m_guard",
			icon = "m_guard_icon",
			name = var_0_11,
			desc = var_0_8
		}
	},
	{
		{
			img = "e1",
			icon = "e1_icon",
			name = var_0_12,
			desc = var_0_19
		},
		{
			img = "e2",
			icon = "e2_icon",
			name = var_0_13,
			desc = var_0_20
		},
		{
			img = "e3",
			icon = "e3_icon",
			name = var_0_14,
			desc = var_0_21
		},
		{
			img = "e4",
			icon = "e4_icon",
			name = var_0_15,
			desc = var_0_22
		},
		{
			img = "e5",
			icon = "e5_icon",
			name = var_0_16,
			desc = var_0_23
		},
		{
			img = "e6",
			icon = "e6_icon",
			name = var_0_17,
			desc = var_0_24
		},
		{
			img = "e7",
			icon = "e7_icon",
			name = var_0_18,
			desc = var_0_25
		}
	},
	{}
}

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_3
	arg_1_0._gameData = arg_1_2
	arg_1_0.menuUI = findTF(arg_1_0._tf, "ui/menuUI")
	arg_1_0.battleScrollRect = GetComponent(findTF(arg_1_0.menuUI, "ad/battList"), typeof(ScrollRect))
	arg_1_0.totalTimes = arg_1_0._gameData.total_times
	arg_1_0.battleItems = {}
	arg_1_0.dropItems = {}

	GetComponent(findTF(arg_1_0.menuUI, "desc"), typeof(Image)):SetNativeSize()
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/rightPanelBg/arrowUp"), function()
		local var_2_0 = arg_1_0.battleScrollRect.normalizedPosition.y + 1 / (arg_1_0.totalTimes - 4)

		if var_2_0 > 1 then
			var_2_0 = 1
		end

		scrollTo(arg_1_0.battleScrollRect, 0, var_2_0)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/rightPanelBg/arrowDown"), function()
		local var_3_0 = arg_1_0.battleScrollRect.normalizedPosition.y - 1 / (arg_1_0.totalTimes - 4)

		if var_3_0 < 0 then
			var_3_0 = 0
		end

		scrollTo(arg_1_0.battleScrollRect, 0, var_3_0)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/btnBack"), function()
		arg_1_0._event:emit(BeachGuardGameView.CLOSE_GAME)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnRule"), function()
		arg_1_0._event:emit(BeachGuardGameView.SHOW_RULE)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnStart"), function()
		arg_1_0._event:emit(BeachGuardGameView.READY_START)
	end, SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/btnGameBook"), function()
		if isActive(arg_1_0.bookUI) then
			setActive(arg_1_0.bookUI, false)
		else
			setActive(arg_1_0.bookUI, true)
		end
	end, SFX_CANCEL)

	local var_1_0 = findTF(arg_1_0.menuUI, "tplBattleItem")
	local var_1_1 = arg_1_0._gameData.drop

	for iter_1_0 = 1, 7 do
		local var_1_2 = tf(instantiate(var_1_0))

		var_1_2.name = "battleItem_" .. iter_1_0

		setParent(var_1_2, findTF(arg_1_0.menuUI, "ad/battList/Viewport/Content"))

		local var_1_3 = iter_1_0

		GetSpriteFromAtlasAsync(arg_1_0._gameData.path, "battleDesc" .. var_1_3, function(arg_8_0)
			if arg_8_0 then
				setImageSprite(findTF(var_1_2, "state_open/desc"), arg_8_0, true)
				setImageSprite(findTF(var_1_2, "state_clear/desc"), arg_8_0, true)
				setImageSprite(findTF(var_1_2, "state_current/desc"), arg_8_0, true)
				setImageSprite(findTF(var_1_2, "state_closed/desc"), arg_8_0, true)
			end
		end)

		local var_1_4 = findTF(var_1_2, "icon")
		local var_1_5 = {
			type = var_1_1[iter_1_0][1],
			id = var_1_1[iter_1_0][2],
			amount = var_1_1[iter_1_0][3]
		}

		updateDrop(var_1_4, var_1_5)
		onButton(arg_1_0._event, var_1_4, function()
			arg_1_0._event:emit(BaseUI.ON_DROP, var_1_5)
		end, SFX_PANEL)
		table.insert(arg_1_0.dropItems, var_1_4)
		setActive(var_1_2, true)
		table.insert(arg_1_0.battleItems, var_1_2)
	end

	arg_1_0.bookUI = findTF(arg_1_0.menuUI, "bookUI")

	setActive(arg_1_0.bookUI, false)
	onButton(arg_1_0._event, findTF(arg_1_0.bookUI, "bottom"), function()
		if isActive(arg_1_0.bookUI) then
			setActive(arg_1_0.bookUI, false)
		end
	end, SFX_PANEL)

	arg_1_0.selectTagIndex = nil
	arg_1_0.selectGridIndex = nil
	arg_1_0.bookUITags = {}
	arg_1_0.grids = {}
	arg_1_0.iconImage = findTF(arg_1_0.bookUI, "bg/icon/img")
	arg_1_0.iconDesc = findTF(arg_1_0.bookUI, "bg/icon/img_desc")
	arg_1_0.descBoundTxt = findTF(arg_1_0.bookUI, "bg/descBound/desc")
	arg_1_0.descBoundTitle = findTF(arg_1_0.bookUI, "bg/descBound/title")

	local var_1_6 = 8

	for iter_1_1 = 1, 3 do
		local var_1_7 = iter_1_1
		local var_1_8 = findTF(arg_1_0.bookUI, "bg/tag" .. iter_1_1)

		if iter_1_1 == 3 then
			setActive(var_1_8, false)
		end

		onButton(arg_1_0._event, var_1_8, function()
			arg_1_0:selectBookTag(var_1_7)
		end, SFX_PANEL)
		table.insert(arg_1_0.bookUITags, var_1_8)
	end

	local var_1_9 = findTF(arg_1_0.bookUI, "bg/gridTpl")

	for iter_1_2 = 1, var_1_6 do
		local var_1_10 = iter_1_2
		local var_1_11 = tf(instantiate(var_1_9))

		setActive(var_1_11, true)
		setParent(var_1_11, findTF(arg_1_0.bookUI, "container/Viewport/Content"))
		onButton(arg_1_0._event, var_1_11, function()
			arg_1_0:selectGrid(var_1_10)
		end, SFX_PANEL)
		table.insert(arg_1_0.grids, var_1_11)
	end

	arg_1_0:selectBookTag(1)
end

function var_0_0.selectBookTag(arg_13_0, arg_13_1)
	if arg_13_0.selectTagIndex ~= arg_13_1 then
		arg_13_0.selectTagIndex = arg_13_1
		arg_13_0.bookDatas = var_0_26[arg_13_1]

		for iter_13_0 = 1, #arg_13_0.bookUITags do
			if arg_13_1 == iter_13_0 then
				setActive(findTF(arg_13_0.bookUITags[iter_13_0], "select"), true)
			else
				setActive(findTF(arg_13_0.bookUITags[iter_13_0], "select"), false)
			end
		end

		for iter_13_1 = 1, #arg_13_0.grids do
			local var_13_0 = arg_13_0.grids[iter_13_1]

			if iter_13_1 <= #arg_13_0.bookDatas then
				local var_13_1 = arg_13_0.bookDatas[iter_13_1]
				local var_13_2 = GetSpriteFromAtlas(arg_13_0._gameData.path, var_13_1.icon)
				local var_13_3

				if var_13_1.id then
					var_13_3 = pg.ship_data_statistics[var_13_1.id].name
				else
					var_13_3 = i18n(var_13_1.name)
				end

				setText(findTF(var_13_0, "name"), var_13_3)
				setImageSprite(findTF(var_13_0, "icon"), var_13_2, true)
				setActive(var_13_0, true)
			else
				setActive(var_13_0, false)
			end
		end

		arg_13_0.selectGridIndex = nil

		arg_13_0:selectGrid(1)
	end
end

function var_0_0.selectGrid(arg_14_0, arg_14_1)
	if arg_14_0.selectGridIndex ~= arg_14_1 then
		arg_14_0.selectGridIndex = arg_14_1

		local var_14_0 = arg_14_0.bookDatas[arg_14_1]

		for iter_14_0 = 1, #arg_14_0.grids do
			local var_14_1 = arg_14_0.grids[iter_14_0]

			if iter_14_0 == arg_14_1 then
				setActive(findTF(var_14_1, "select"), true)
			else
				setActive(findTF(var_14_1, "select"), false)
			end
		end

		if var_14_0.img then
			local var_14_2 = GetSpriteFromAtlas(arg_14_0._gameData.path, var_14_0.img)

			setImageSprite(arg_14_0.iconImage, var_14_2, true)
			setActive(arg_14_0.iconImage, true)
		else
			setActive(arg_14_0.iconImage, false)
		end

		if var_14_0.img_desc then
			local var_14_3 = GetSpriteFromAtlas(arg_14_0._gameData.path, var_14_0.img_desc)

			setImageSprite(arg_14_0.iconDesc, var_14_3, true)
			setActive(arg_14_0.iconDesc, true)
		else
			setActive(arg_14_0.iconDesc, false)
		end

		local var_14_4 = i18n(var_14_0.desc)

		setText(arg_14_0.descBoundTxt, var_14_4)
	end
end

function var_0_0.updateBookUI(arg_15_0)
	return
end

function var_0_0.show(arg_16_0, arg_16_1)
	setActive(arg_16_0.menuUI, arg_16_1)
end

function var_0_0.update(arg_17_0, arg_17_1)
	local var_17_0 = arg_17_0:getGameUsedTimes(arg_17_1)
	local var_17_1 = arg_17_0:getGameTimes(arg_17_1)

	for iter_17_0 = 1, #arg_17_0.battleItems do
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_open"), false)
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_closed"), false)
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_clear"), false)
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_current"), false)

		if iter_17_0 <= var_17_0 then
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_clear/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], true)
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_clear"), true)
		elseif iter_17_0 == var_17_0 + 1 and var_17_1 >= 1 then
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_current"), true)
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_current/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], true)
		elseif var_17_0 < iter_17_0 and iter_17_0 <= var_17_0 + var_17_1 then
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_open"), true)
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_open/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], true)
		else
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_closed"), true)
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_closed/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], true)
		end
	end

	local var_17_2 = 1 - (var_17_0 - 3 < 0 and 0 or var_17_0 - 3) / (arg_17_0.totalTimes - 4)

	if var_17_2 > 1 then
		var_17_2 = 1
	end

	scrollTo(arg_17_0.battleScrollRect, 0, var_17_2)
	setActive(findTF(arg_17_0.menuUI, "btnStart/tip"), var_17_1 > 0)
	arg_17_0:CheckGet(arg_17_1)
end

function var_0_0.CheckGet(arg_18_0, arg_18_1)
	setActive(findTF(arg_18_0.menuUI, "got"), false)

	local var_18_0 = arg_18_0:getUltimate(arg_18_1)

	if var_18_0 and var_18_0 ~= 0 then
		setActive(findTF(arg_18_0.menuUI, "got"), true)
	end

	if var_18_0 == 0 then
		if arg_18_0._gameData.total_times > arg_18_0:getGameUsedTimes(arg_18_1) then
			return
		end

		pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_18_1.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_18_0.menuUI, "got"), true)
	end
end

function var_0_0.getGameTimes(arg_19_0, arg_19_1)
	return arg_19_1.count
end

function var_0_0.getGameUsedTimes(arg_20_0, arg_20_1)
	return arg_20_1.usedtime
end

function var_0_0.getUltimate(arg_21_0, arg_21_1)
	return arg_21_1.ultimate
end

return var_0_0
