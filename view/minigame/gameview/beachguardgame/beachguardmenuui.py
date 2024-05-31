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

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_3
	arg_1_0._gameData = arg_1_2
	arg_1_0.menuUI = findTF(arg_1_0._tf, "ui/menuUI")
	arg_1_0.battleScrollRect = GetComponent(findTF(arg_1_0.menuUI, "ad/battList"), typeof(ScrollRect))
	arg_1_0.totalTimes = arg_1_0._gameData.total_times
	arg_1_0.battleItems = {}
	arg_1_0.dropItems = {}

	GetComponent(findTF(arg_1_0.menuUI, "desc"), typeof(Image)).SetNativeSize()
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/rightPanelBg/arrowUp"), function()
		local var_2_0 = arg_1_0.battleScrollRect.normalizedPosition.y + 1 / (arg_1_0.totalTimes - 4)

		if var_2_0 > 1:
			var_2_0 = 1

		scrollTo(arg_1_0.battleScrollRect, 0, var_2_0), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/rightPanelBg/arrowDown"), function()
		local var_3_0 = arg_1_0.battleScrollRect.normalizedPosition.y - 1 / (arg_1_0.totalTimes - 4)

		if var_3_0 < 0:
			var_3_0 = 0

		scrollTo(arg_1_0.battleScrollRect, 0, var_3_0), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/btnBack"), function()
		arg_1_0._event.emit(BeachGuardGameView.CLOSE_GAME), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnRule"), function()
		arg_1_0._event.emit(BeachGuardGameView.SHOW_RULE), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "btnStart"), function()
		arg_1_0._event.emit(BeachGuardGameView.READY_START), SFX_CANCEL)
	onButton(arg_1_0._event, findTF(arg_1_0.menuUI, "ad/btnGameBook"), function()
		if isActive(arg_1_0.bookUI):
			setActive(arg_1_0.bookUI, False)
		else
			setActive(arg_1_0.bookUI, True), SFX_CANCEL)

	local var_1_0 = findTF(arg_1_0.menuUI, "tplBattleItem")
	local var_1_1 = arg_1_0._gameData.drop

	for iter_1_0 = 1, 7:
		local var_1_2 = tf(instantiate(var_1_0))

		var_1_2.name = "battleItem_" .. iter_1_0

		setParent(var_1_2, findTF(arg_1_0.menuUI, "ad/battList/Viewport/Content"))

		local var_1_3 = iter_1_0

		GetSpriteFromAtlasAsync(arg_1_0._gameData.path, "battleDesc" .. var_1_3, function(arg_8_0)
			if arg_8_0:
				setImageSprite(findTF(var_1_2, "state_open/desc"), arg_8_0, True)
				setImageSprite(findTF(var_1_2, "state_clear/desc"), arg_8_0, True)
				setImageSprite(findTF(var_1_2, "state_current/desc"), arg_8_0, True)
				setImageSprite(findTF(var_1_2, "state_closed/desc"), arg_8_0, True))

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

	arg_1_0.bookUI = findTF(arg_1_0.menuUI, "bookUI")

	setActive(arg_1_0.bookUI, False)
	onButton(arg_1_0._event, findTF(arg_1_0.bookUI, "bottom"), function()
		if isActive(arg_1_0.bookUI):
			setActive(arg_1_0.bookUI, False), SFX_PANEL)

	arg_1_0.selectTagIndex = None
	arg_1_0.selectGridIndex = None
	arg_1_0.bookUITags = {}
	arg_1_0.grids = {}
	arg_1_0.iconImage = findTF(arg_1_0.bookUI, "bg/icon/img")
	arg_1_0.iconDesc = findTF(arg_1_0.bookUI, "bg/icon/img_desc")
	arg_1_0.descBoundTxt = findTF(arg_1_0.bookUI, "bg/descBound/desc")
	arg_1_0.descBoundTitle = findTF(arg_1_0.bookUI, "bg/descBound/title")

	local var_1_6 = 8

	for iter_1_1 = 1, 3:
		local var_1_7 = iter_1_1
		local var_1_8 = findTF(arg_1_0.bookUI, "bg/tag" .. iter_1_1)

		if iter_1_1 == 3:
			setActive(var_1_8, False)

		onButton(arg_1_0._event, var_1_8, function()
			arg_1_0.selectBookTag(var_1_7), SFX_PANEL)
		table.insert(arg_1_0.bookUITags, var_1_8)

	local var_1_9 = findTF(arg_1_0.bookUI, "bg/gridTpl")

	for iter_1_2 = 1, var_1_6:
		local var_1_10 = iter_1_2
		local var_1_11 = tf(instantiate(var_1_9))

		setActive(var_1_11, True)
		setParent(var_1_11, findTF(arg_1_0.bookUI, "container/Viewport/Content"))
		onButton(arg_1_0._event, var_1_11, function()
			arg_1_0.selectGrid(var_1_10), SFX_PANEL)
		table.insert(arg_1_0.grids, var_1_11)

	arg_1_0.selectBookTag(1)

def var_0_0.selectBookTag(arg_13_0, arg_13_1):
	if arg_13_0.selectTagIndex != arg_13_1:
		arg_13_0.selectTagIndex = arg_13_1
		arg_13_0.bookDatas = var_0_26[arg_13_1]

		for iter_13_0 = 1, #arg_13_0.bookUITags:
			if arg_13_1 == iter_13_0:
				setActive(findTF(arg_13_0.bookUITags[iter_13_0], "select"), True)
			else
				setActive(findTF(arg_13_0.bookUITags[iter_13_0], "select"), False)

		for iter_13_1 = 1, #arg_13_0.grids:
			local var_13_0 = arg_13_0.grids[iter_13_1]

			if iter_13_1 <= #arg_13_0.bookDatas:
				local var_13_1 = arg_13_0.bookDatas[iter_13_1]
				local var_13_2 = GetSpriteFromAtlas(arg_13_0._gameData.path, var_13_1.icon)
				local var_13_3

				if var_13_1.id:
					var_13_3 = pg.ship_data_statistics[var_13_1.id].name
				else
					var_13_3 = i18n(var_13_1.name)

				setText(findTF(var_13_0, "name"), var_13_3)
				setImageSprite(findTF(var_13_0, "icon"), var_13_2, True)
				setActive(var_13_0, True)
			else
				setActive(var_13_0, False)

		arg_13_0.selectGridIndex = None

		arg_13_0.selectGrid(1)

def var_0_0.selectGrid(arg_14_0, arg_14_1):
	if arg_14_0.selectGridIndex != arg_14_1:
		arg_14_0.selectGridIndex = arg_14_1

		local var_14_0 = arg_14_0.bookDatas[arg_14_1]

		for iter_14_0 = 1, #arg_14_0.grids:
			local var_14_1 = arg_14_0.grids[iter_14_0]

			if iter_14_0 == arg_14_1:
				setActive(findTF(var_14_1, "select"), True)
			else
				setActive(findTF(var_14_1, "select"), False)

		if var_14_0.img:
			local var_14_2 = GetSpriteFromAtlas(arg_14_0._gameData.path, var_14_0.img)

			setImageSprite(arg_14_0.iconImage, var_14_2, True)
			setActive(arg_14_0.iconImage, True)
		else
			setActive(arg_14_0.iconImage, False)

		if var_14_0.img_desc:
			local var_14_3 = GetSpriteFromAtlas(arg_14_0._gameData.path, var_14_0.img_desc)

			setImageSprite(arg_14_0.iconDesc, var_14_3, True)
			setActive(arg_14_0.iconDesc, True)
		else
			setActive(arg_14_0.iconDesc, False)

		local var_14_4 = i18n(var_14_0.desc)

		setText(arg_14_0.descBoundTxt, var_14_4)

def var_0_0.updateBookUI(arg_15_0):
	return

def var_0_0.show(arg_16_0, arg_16_1):
	setActive(arg_16_0.menuUI, arg_16_1)

def var_0_0.update(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_0.getGameUsedTimes(arg_17_1)
	local var_17_1 = arg_17_0.getGameTimes(arg_17_1)

	for iter_17_0 = 1, #arg_17_0.battleItems:
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_open"), False)
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_closed"), False)
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_clear"), False)
		setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_current"), False)

		if iter_17_0 <= var_17_0:
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_clear/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], True)
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_clear"), True)
		elif iter_17_0 == var_17_0 + 1 and var_17_1 >= 1:
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_current"), True)
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_current/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], True)
		elif var_17_0 < iter_17_0 and iter_17_0 <= var_17_0 + var_17_1:
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_open"), True)
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_open/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], True)
		else
			setActive(findTF(arg_17_0.battleItems[iter_17_0], "state_closed"), True)
			SetParent(arg_17_0.dropItems[iter_17_0], findTF(arg_17_0.battleItems[iter_17_0], "state_closed/icon"))
			setActive(arg_17_0.dropItems[iter_17_0], True)

	local var_17_2 = 1 - (var_17_0 - 3 < 0 and 0 or var_17_0 - 3) / (arg_17_0.totalTimes - 4)

	if var_17_2 > 1:
		var_17_2 = 1

	scrollTo(arg_17_0.battleScrollRect, 0, var_17_2)
	setActive(findTF(arg_17_0.menuUI, "btnStart/tip"), var_17_1 > 0)
	arg_17_0.CheckGet(arg_17_1)

def var_0_0.CheckGet(arg_18_0, arg_18_1):
	setActive(findTF(arg_18_0.menuUI, "got"), False)

	local var_18_0 = arg_18_0.getUltimate(arg_18_1)

	if var_18_0 and var_18_0 != 0:
		setActive(findTF(arg_18_0.menuUI, "got"), True)

	if var_18_0 == 0:
		if arg_18_0._gameData.total_times > arg_18_0.getGameUsedTimes(arg_18_1):
			return

		pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = arg_18_1.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
		setActive(findTF(arg_18_0.menuUI, "got"), True)

def var_0_0.getGameTimes(arg_19_0, arg_19_1):
	return arg_19_1.count

def var_0_0.getGameUsedTimes(arg_20_0, arg_20_1):
	return arg_20_1.usedtime

def var_0_0.getUltimate(arg_21_0, arg_21_1):
	return arg_21_1.ultimate

return var_0_0
