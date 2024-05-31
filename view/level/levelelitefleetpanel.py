local var_0_0 = class("LevelEliteFleetPanel", import("..base.BasePanel"))
local var_0_1 = {
	vanguard = 1,
	submarine = 3,
	main = 2
}

def var_0_0.init(arg_1_0):
	var_0_0.super.init(arg_1_0)

	arg_1_0.tfShipTpl = arg_1_0.findTF("panel/shiptpl")
	arg_1_0.tfEmptyTpl = arg_1_0.findTF("panel/emptytpl")
	arg_1_0.tfFleets = {
		[FleetType.Normal] = {
			arg_1_0.findTF("panel/fleet/1"),
			arg_1_0.findTF("panel/fleet/2")
		},
		[FleetType.Submarine] = {
			arg_1_0.findTF("panel/sub/1")
		}
	}
	arg_1_0.tfLimit = arg_1_0.findTF("panel/limit")
	arg_1_0.tfLimitTips = arg_1_0.findTF("panel/limit_tip")
	arg_1_0.tfLimitElite = arg_1_0.findTF("panel/limit_elite")
	arg_1_0.tfLimitContainer = arg_1_0.findTF("panel/limit_elite/limit_list")
	arg_1_0.tfLimitTpl = arg_1_0.findTF("panel/limit_elite/condition")
	arg_1_0.btnBack = arg_1_0.findTF("panel/btnBack")
	arg_1_0.btnGo = arg_1_0.findTF("panel/start_button")
	arg_1_0.btnAdHelp = arg_1_0.findTF("panel/title/ADvalue/helpbtn")
	arg_1_0.commanderBtn = arg_1_0.findTF("panel/commander_btn")
	arg_1_0.toggleMask = arg_1_0.findTF("mask")

	setActive(arg_1_0.tfShipTpl, False)
	setActive(arg_1_0.tfEmptyTpl, False)
	setActive(arg_1_0.tfLimitTpl, False)
	setActive(arg_1_0.toggleMask, False)

	arg_1_0.onConfirm = None
	arg_1_0.onCancel = None
	arg_1_0.onClick = None
	arg_1_0.onLongPressed = None
	arg_1_0.onEliteClear = None
	arg_1_0.onEliteRecommend = None

def var_0_0.set(arg_2_0, arg_2_1):
	arg_2_0.chapter = arg_2_1
	arg_2_0.propetyLimitation = arg_2_0.chapter.getConfig("property_limitation")
	arg_2_0.eliteFleetList = arg_2_0.chapter.getEliteFleetList()
	arg_2_0.chapterADValue = arg_2_0.chapter.getConfig("air_dominance")
	arg_2_0.suggestionValue = math.max(arg_2_0.chapter.getConfig("best_air_dominance"), 150)
	arg_2_0.eliteCommanderList = arg_2_0.chapter.getEliteFleetCommanders()
	arg_2_0.typeLimitations = arg_2_0.chapter.getConfig("limitation")

	onButton(arg_2_0, arg_2_0.btnGo, function()
		if arg_2_0.onConfirm:
			arg_2_0.onConfirm(), SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_2_0, arg_2_0.btnAdHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("help_battle_ac")
		}), SFX_UI_CLICK)
	onButton(arg_2_0, arg_2_0.btnBack, function()
		if arg_2_0.onCancel:
			arg_2_0.onCancel(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0._tf, function()
		if arg_2_0.onCancel:
			arg_2_0.onCancel(), SFX_CANCEL)
	onToggle(arg_2_0, arg_2_0.commanderBtn, function(arg_7_0)
		arg_2_0.parent.contextData.EditingCommander = arg_7_0

		arg_2_0.flush(), SFX_PANEL)
	triggerToggle(arg_2_0.commanderBtn, arg_2_0.parent.contextData.EditingCommander)
	setActive(arg_2_0.commanderBtn, arg_2_0.parent.openedCommanerSystem)
	arg_2_0.flush()

def var_0_0.clear(arg_8_0):
	triggerToggle(arg_8_0.commanderBtn, False)

def var_0_0.flush(arg_9_0):
	arg_9_0.updateLimit()

	if OPEN_AIR_DOMINANCE and arg_9_0.chapterADValue > 0:
		setActive(arg_9_0.findTF("panel/title/ADvalue"), True)
		arg_9_0.updateFleetPanelADValue()
	else
		setActive(arg_9_0.findTF("panel/title/ADvalue"), False)

	arg_9_0.updateFleets()

def var_0_0.updateLimit(arg_10_0):
	setActive(arg_10_0.toggleMask, False)
	setActive(arg_10_0.tfLimit, False)
	setActive(arg_10_0.tfLimitTips, #arg_10_0.propetyLimitation == 0)
	setActive(arg_10_0.tfLimitElite, #arg_10_0.propetyLimitation > 0)
	removeAllChildren(arg_10_0.tfLimitContainer)

	if #arg_10_0.propetyLimitation > 0:
		local var_10_0, var_10_1 = arg_10_0.chapter.IsPropertyLimitationSatisfy()

		for iter_10_0, iter_10_1 in ipairs(arg_10_0.propetyLimitation):
			local var_10_2, var_10_3, var_10_4, var_10_5 = unpack(iter_10_1)
			local var_10_6 = cloneTplTo(arg_10_0.tfLimitTpl, arg_10_0.tfLimitContainer)

			if var_10_0[iter_10_0] == 1:
				arg_10_0.findTF("Text", var_10_6).GetComponent(typeof(Text)).color = Color.New(1, 0.9607843137254902, 0.5019607843137255)
			else
				arg_10_0.findTF("Text", var_10_6).GetComponent(typeof(Text)).color = Color.New(0.9568627450980393, 0.30196078431372547, 0.30196078431372547)

			setActive(var_10_6, True)

			local var_10_7 = (AttributeType.EliteCondition2Name(var_10_2, var_10_5) .. AttributeType.eliteConditionCompareTip(var_10_3) .. var_10_4) .. "（" .. var_10_1[var_10_2] .. "）"

			setText(arg_10_0.findTF("Text", var_10_6), var_10_7)

		setActive(arg_10_0.tfLimitElite.Find("sub"), arg_10_0.chapter.getConfig("submarine_num") > 0)

def var_0_0.updateFleetPanelADValue(arg_11_0):
	local var_11_0 = getProxy(BayProxy)
	local var_11_1 = 0

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.eliteFleetList):
		local var_11_2 = {}

		for iter_11_2, iter_11_3 in pairs(arg_11_0.eliteCommanderList[iter_11_0]):
			var_11_2[iter_11_2] = getProxy(CommanderProxy).getCommanderById(iter_11_3)

		for iter_11_4, iter_11_5 in ipairs(iter_11_1):
			var_11_1 = var_11_1 + calcAirDominanceValue(var_11_0.getShipById(iter_11_5), var_11_2)

	local var_11_3 = math.floor(var_11_1)
	local var_11_4 = arg_11_0.findTF("panel/title/ADvalue/Text")

	setText(var_11_4, i18n("level_scene_title_word_5"))
	setText(arg_11_0.findTF("Num1", var_11_4), setColorStr(var_11_3, var_11_3 < arg_11_0.suggestionValue and "#f1dc36" or COLOR_WHITE))
	setText(arg_11_0.findTF("Num2", var_11_4), arg_11_0.suggestionValue)

def var_0_0.initAddButton(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4):
	local var_12_0 = arg_12_0.eliteFleetList[arg_12_4]
	local var_12_1 = {}
	local var_12_2 = {}

	for iter_12_0, iter_12_1 in ipairs(var_12_0):
		var_12_1[arg_12_0.parent.shipVOs[iter_12_1]] = True

		if arg_12_2 == arg_12_0.parent.shipVOs[iter_12_1].getTeamType():
			table.insert(var_12_2, iter_12_1)

	local var_12_3 = findTF(arg_12_1, arg_12_2)

	removeAllChildren(var_12_3)

	local var_12_4 = 0
	local var_12_5 = False
	local var_12_6 = 0

	arg_12_3 = Clone(arg_12_3)

	table.sort(arg_12_3, function(arg_13_0, arg_13_1)
		local var_13_0 = type(arg_13_0)
		local var_13_1 = type(arg_13_1)

		if var_13_0 == var_13_1:
			return var_13_1 < var_13_0
		elif arg_13_1 == 0 or var_13_1 == "string" and arg_13_0 != 0:
			return True
		else
			return False)

	local var_12_7 = {}
	local var_12_8 = {}

	for iter_12_2 = 1, 3:
		local var_12_9
		local var_12_10
		local var_12_11
		local var_12_12 = var_12_2[iter_12_2] and arg_12_0.parent.shipVOs[var_12_2[iter_12_2]] or None

		if var_12_12:
			for iter_12_3, iter_12_4 in ipairs(arg_12_3):
				if ShipType.ContainInLimitBundle(iter_12_4, var_12_12.getShipType()):
					var_12_10 = var_12_12
					var_12_11 = iter_12_4

					table.remove(arg_12_3, iter_12_3)
					table.insert(var_12_7, iter_12_3)

					var_12_5 = var_12_5 or iter_12_4 != 0

					break
		else
			var_12_11 = arg_12_3[1]

			table.remove(arg_12_3, 1)
			table.insert(var_12_7, 1)

		if var_12_11 == 0:
			var_12_6 = var_12_6 + 1

		local var_12_13 = var_12_10 and cloneTplTo(arg_12_0.tfShipTpl, var_12_3) or cloneTplTo(arg_12_0.tfEmptyTpl, var_12_3)

		table.insert(var_12_8, var_12_13)
		setActive(var_12_13, True)

		if var_12_10:
			updateShip(var_12_13, var_12_10)
			setActive(arg_12_0.findTF("event_block", var_12_13), var_12_10.getFlag("inEvent"))

			var_12_1[var_12_10] = True
		else
			var_12_4 = var_12_4 + 1

		local var_12_14 = findTF(var_12_13, "icon_bg")

		setActive(arg_12_0.findTF("ship_type", var_12_13), True)

		if type(var_12_11) == "number":
			if var_12_11 != 0:
				local var_12_15 = GetSpriteFromAtlas("shiptype", ShipType.Type2CNLabel(var_12_11))

				setImageSprite(arg_12_0.findTF("ship_type", var_12_13), var_12_15, True)
			else
				setActive(arg_12_0.findTF("ship_type", var_12_13), False)
		elif type(var_12_11) == "string":
			local var_12_16 = GetSpriteFromAtlas("shiptype", ShipType.BundleType2CNLabel(var_12_11))

			setImageSprite(arg_12_0.findTF("ship_type", var_12_13), var_12_16, True)

		setActive(arg_12_0.findTF("ship_type", var_12_13), not var_12_10 and var_12_11 != 0)

		local var_12_17 = _.map(var_12_0, function(arg_14_0)
			return arg_12_0.parent.shipVOs[arg_14_0])

		table.sort(var_12_17, function(arg_15_0, arg_15_1)
			return var_0_1[arg_15_0.getTeamType()] < var_0_1[arg_15_1.getTeamType()] or var_0_1[arg_15_0.getTeamType()] == var_0_1[arg_15_1.getTeamType()] and table.indexof(var_12_0, arg_15_0.id) < table.indexof(var_12_0, arg_15_1.id))

		local var_12_18 = GetOrAddComponent(var_12_14, typeof(UILongPressTrigger))

		var_12_18.onReleased.RemoveAllListeners()
		var_12_18.onLongPressed.RemoveAllListeners()
		var_12_18.onReleased.AddListener(function()
			arg_12_0.onClick({
				shipType = var_12_11,
				fleet = var_12_1,
				chapter = arg_12_0.chapter,
				shipVO = var_12_10,
				fleetIndex = arg_12_4,
				teamType = arg_12_2
			}))
		var_12_18.onLongPressed.AddListener(function()
			if not var_12_10:
				arg_12_0.onClick({
					shipType = var_12_11,
					fleet = var_12_1,
					chapter = arg_12_0.chapter,
					shipVO = var_12_10,
					fleetIndex = arg_12_4,
					teamType = arg_12_2
				})
			else
				arg_12_0.onLongPressed({
					shipId = var_12_10.id,
					shipVOs = var_12_17,
					chapter = arg_12_0.chapter
				}))

	for iter_12_5 = 3, 1, -1:
		var_12_8[iter_12_5].SetSiblingIndex(var_12_7[iter_12_5] - 1)

	if (var_12_5 == True or var_12_6 == 3) and var_12_4 != 3:
		return True
	else
		return False

def var_0_0.initCommander(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = arg_18_3.getEliteFleetCommanders()[arg_18_1]

	for iter_18_0 = 1, 2:
		local var_18_1 = var_18_0[iter_18_0]
		local var_18_2

		if var_18_1:
			var_18_2 = getProxy(CommanderProxy).getCommanderById(var_18_1)

		local var_18_3 = arg_18_2.Find("pos" .. iter_18_0)
		local var_18_4 = var_18_3.Find("add")
		local var_18_5 = var_18_3.Find("info")

		setActive(var_18_4, not var_18_2)
		setActive(var_18_5, var_18_2)

		if var_18_2:
			local var_18_6 = Commander.rarity2Frame(var_18_2.getRarity())

			setImageSprite(var_18_5.Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_18_6))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_18_2.getPainting(), "", var_18_5.Find("mask/icon"))

		local var_18_7 = arg_18_3.wrapEliteFleet(arg_18_1)

		onButton(arg_18_0, var_18_4, function()
			arg_18_0.parent.openCommanderPanel(var_18_7, arg_18_3.id, arg_18_1), SFX_PANEL)
		onButton(arg_18_0, var_18_5, function()
			arg_18_0.parent.openCommanderPanel(var_18_7, arg_18_3.id, arg_18_1), SFX_PANEL)

def var_0_0.updateFleets(arg_21_0):
	for iter_21_0, iter_21_1 in ipairs(arg_21_0.tfFleets[FleetType.Normal]):
		local var_21_0 = arg_21_0.findTF("btn_clear", iter_21_1)
		local var_21_1 = arg_21_0.findTF("btn_recom", iter_21_1)
		local var_21_2 = arg_21_0.findTF("btn_select", iter_21_1)
		local var_21_3 = arg_21_0.findTF("blank", iter_21_1)
		local var_21_4 = arg_21_0.findTF("commander", iter_21_1)

		setActive(var_21_2, False)
		setActive(findTF(iter_21_1, "selected"), False)

		local var_21_5 = iter_21_0 <= arg_21_0.chapter.getConfig("group_num")

		setActive(findTF(iter_21_1, TeamType.Main), var_21_5)
		setActive(findTF(iter_21_1, TeamType.Vanguard), var_21_5)
		setActive(var_21_0, var_21_5 and not arg_21_0.contextData.EditingCommander)
		setActive(var_21_1, var_21_5 and not arg_21_0.contextData.EditingCommander)
		setActive(var_21_3, not var_21_5)
		setActive(var_21_4, var_21_5 and arg_21_0.contextData.EditingCommander)
		setText(arg_21_0.findTF("bg/name", iter_21_1), var_21_5 and Fleet.DEFAULT_NAME[iter_21_0] or "")

		if var_21_5:
			local var_21_6 = arg_21_0.typeLimitations[iter_21_0]
			local var_21_7 = var_21_6[1]
			local var_21_8 = var_21_6[2]
			local var_21_9 = arg_21_0.initAddButton(iter_21_1, TeamType.Main, var_21_7, iter_21_0)
			local var_21_10 = arg_21_0.initAddButton(iter_21_1, TeamType.Vanguard, var_21_8, iter_21_0)

			arg_21_0.initCommander(iter_21_0, var_21_4, arg_21_0.chapter)

			if var_21_9 and var_21_10:
				setActive(arg_21_0.findTF("selected", iter_21_1), True)

			onButton(arg_21_0, var_21_0, function()
				if #arg_21_0.eliteFleetList[iter_21_0] != 0:
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("battle_preCombatLayer_clear_confirm"),
						def onYes:()
							arg_21_0.onEliteClear({
								index = iter_21_0,
								chapterVO = arg_21_0.chapter
							})
					}))
			onButton(arg_21_0, var_21_1, function()
				local var_24_0 = #arg_21_0.eliteFleetList[iter_21_0]

				if var_24_0 != 6:
					if var_24_0 != 0:
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							content = i18n("battle_preCombatLayer_auto_confirm"),
							def onYes:()
								arg_21_0.onEliteRecommend({
									index = iter_21_0,
									chapterVO = arg_21_0.chapter
								})
						})
					else
						arg_21_0.onEliteRecommend({
							index = iter_21_0,
							chapterVO = arg_21_0.chapter
						}))

	for iter_21_2, iter_21_3 in ipairs(arg_21_0.tfFleets[FleetType.Submarine]):
		local var_21_11 = iter_21_2 + 2
		local var_21_12 = arg_21_0.findTF("btn_clear", iter_21_3)
		local var_21_13 = arg_21_0.findTF("btn_recom", iter_21_3)
		local var_21_14 = arg_21_0.findTF("btn_select", iter_21_3)
		local var_21_15 = arg_21_0.findTF("blank", iter_21_3)
		local var_21_16 = arg_21_0.findTF("commander", iter_21_3)

		setActive(var_21_14, False)
		setActive(findTF(iter_21_3, "selected"), False)
		setActive(findTF(iter_21_3, TeamType.Submarine), iter_21_2 <= arg_21_0.chapter.getConfig("submarine_num"))
		setActive(var_21_12, iter_21_2 <= arg_21_0.chapter.getConfig("submarine_num") and not arg_21_0.contextData.EditingCommander)
		setActive(var_21_13, iter_21_2 <= arg_21_0.chapter.getConfig("submarine_num") and not arg_21_0.contextData.EditingCommander)
		setActive(var_21_15, iter_21_2 > arg_21_0.chapter.getConfig("submarine_num"))
		setActive(var_21_16, iter_21_2 <= arg_21_0.chapter.getConfig("submarine_num") and arg_21_0.contextData.EditingCommander)
		setText(arg_21_0.findTF("bg/name", iter_21_3), iter_21_2 <= arg_21_0.chapter.getConfig("submarine_num") and Fleet.DEFAULT_NAME[Fleet.SUBMARINE_FLEET_ID + iter_21_2 - 1] or "")
		arg_21_0.initCommander(var_21_11, var_21_16, arg_21_0.chapter)

		if iter_21_2 <= arg_21_0.chapter.getConfig("submarine_num"):
			if arg_21_0.initAddButton(iter_21_3, TeamType.Submarine, {
				0,
				0,
				0
			}, var_21_11):
				setActive(arg_21_0.findTF("selected", iter_21_3), True)

			onButton(arg_21_0, var_21_12, function()
				if #arg_21_0.eliteFleetList[var_21_11] != 0:
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("battle_preCombatLayer_clear_confirm"),
						def onYes:()
							arg_21_0.onEliteClear({
								index = var_21_11,
								chapterVO = arg_21_0.chapter
							})
					}))
			onButton(arg_21_0, var_21_13, function()
				local var_28_0 = #arg_21_0.eliteFleetList[var_21_11]

				if var_28_0 != 3:
					if var_28_0 != 0:
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							content = i18n("battle_preCombatLayer_auto_confirm"),
							def onYes:()
								arg_21_0.onEliteRecommend({
									index = var_21_11,
									chapterVO = arg_21_0.chapter
								})
						})
					else
						arg_21_0.onEliteRecommend({
							index = var_21_11,
							chapterVO = arg_21_0.chapter
						}))

return var_0_0
