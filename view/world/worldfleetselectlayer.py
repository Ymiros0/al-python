local var_0_0 = class("WorldFleetSelectLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "WorldFleetSelect"

def var_0_0.init(arg_2_0):
	arg_2_0.rtBg = arg_2_0._tf.Find("bg")

	local var_2_0 = nowWorld().GetRealm()

	eachChild(arg_2_0.rtBg, function(arg_3_0)
		setActive(arg_3_0, arg_3_0.name == tostring(var_2_0)))

	arg_2_0.rtPanel = arg_2_0._tf.Find("panel")
	arg_2_0.rtShipTpl = arg_2_0.rtPanel.Find("shiptpl")

	setActive(arg_2_0.rtShipTpl, False)

	arg_2_0.rtEmptyTpl = arg_2_0.rtPanel.Find("emptytpl")

	setActive(arg_2_0.rtEmptyTpl, False)

	arg_2_0.rtScroll = arg_2_0.rtPanel.Find("bg")
	arg_2_0.rtContent = arg_2_0.rtScroll.Find("content")
	arg_2_0.rtFleets = {
		[FleetType.Normal] = arg_2_0.rtContent.Find("fleet"),
		[FleetType.Submarine] = arg_2_0.rtContent.Find("sub")
	}
	arg_2_0.btnBack = arg_2_0.rtPanel.Find("btnBack")
	arg_2_0.btnGo = arg_2_0.rtPanel.Find("start_button")
	arg_2_0.commanderToggle = arg_2_0.rtPanel.Find("commander_btn")
	arg_2_0.formationToggle = arg_2_0.rtPanel.Find("formation_btn")
	arg_2_0.tfLimitTip = arg_2_0.rtPanel.Find("limit_tip")

	setText(arg_2_0.tfLimitTip.Find("Text"), i18n("world_fleet_choose"))

	arg_2_0.tfLimitSub = arg_2_0.rtPanel.Find("limit_world/limit_sub")

	setText(arg_2_0.tfLimitSub.Find("Text"), i18n("ship_limit_notice"))

	arg_2_0.tfLimitContainer = arg_2_0.rtPanel.Find("limit_world/limit_list")
	arg_2_0.tfLimitTpl = arg_2_0.tfLimitContainer.Find("condition")

	arg_2_0.buildCommanderPanel()

def var_0_0.didEnter(arg_4_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_4_0.rtPanel)
	onButton(arg_4_0, arg_4_0.btnGo, function()
		local var_5_0, var_5_1 = arg_4_0.CheckValid()

		if var_5_0:
			arg_4_0.emit(WorldFleetSelectMediator.OnGO)
		else
			pg.TipsMgr.GetInstance().ShowTips(var_5_1), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.btnBack, function()
		arg_4_0.closeView(), SFX_CANCEL)

	local function var_4_0(arg_7_0)
		arg_4_0.contextData.showCommander = arg_7_0

		for iter_7_0, iter_7_1 in pairs(arg_4_0.rtFleets):
			for iter_7_2 = 1, #arg_4_0.contextData.fleets[iter_7_0]:
				arg_4_0.updateCommanderBtn(iter_7_1.GetChild(iter_7_2 - 1))

	onToggle(arg_4_0, arg_4_0.commanderToggle, function(arg_8_0)
		if arg_8_0:
			var_4_0(arg_8_0), SFX_PANEL)
	onToggle(arg_4_0, arg_4_0.formationToggle, function(arg_9_0)
		if arg_9_0:
			var_4_0(not arg_9_0), SFX_PANEL)
	arg_4_0.UpdateFleets()
	scrollTo(arg_4_0.rtContent, None, arg_4_0.contextData.scrollY)

	arg_4_0.contextData.showCommander = defaultValue(arg_4_0.contextData.showCommander, True)

	triggerToggle(arg_4_0.contextData.showCommander and arg_4_0.commanderToggle or arg_4_0.formationToggle, True)
	arg_4_0.CheckWorldResetAward()

def var_0_0.willExit(arg_10_0):
	arg_10_0.contextData.scrollY = GetComponent(arg_10_0.rtContent, typeof(ScrollRect)).normalizedPosition.y

	pg.UIMgr.GetInstance().UnblurPanel(arg_10_0.rtPanel, arg_10_0._tf)
	arg_10_0.destroyCommanderPanel()

def var_0_0.onBackPressed(arg_11_0):
	if arg_11_0.levelCMDFormationView.isShowing():
		arg_11_0.levelCMDFormationView.ActionInvoke("Hide")
	else
		arg_11_0.closeView()

def var_0_0.UpdateFleets(arg_12_0):
	local var_12_0 = arg_12_0.contextData.fleets

	for iter_12_0, iter_12_1 in pairs(var_12_0):
		local var_12_1 = arg_12_0.rtFleets[iter_12_0]
		local var_12_2 = UIItemList.New(var_12_1, var_12_1.GetChild(0))

		var_12_2.make(function(arg_13_0, arg_13_1, arg_13_2)
			if arg_13_0 == UIItemList.EventUpdate:
				arg_12_0.UpdateFleet(arg_13_2, iter_12_0, arg_13_1 + 1))
		var_12_2.align(#var_12_0[iter_12_0])
		setActive(var_12_1, #var_12_0[iter_12_0] > 0)

	arg_12_0.updateEliteLimit()

def var_0_0.IsPropertyLimitationSatisfy(arg_14_0):
	local var_14_0 = getProxy(BayProxy).getRawData()
	local var_14_1 = pg.gameset.world_fleet_unlock_level.description
	local var_14_2 = {}

	for iter_14_0, iter_14_1 in ipairs(var_14_1):
		var_14_2[iter_14_1[1]] = 0

	local var_14_3 = 0

	for iter_14_2, iter_14_3 in ipairs(arg_14_0.contextData.fleets[FleetType.Normal]):
		if arg_14_0.GetTeamShipCount(iter_14_3[TeamType.Main]) == 0 or arg_14_0.GetTeamShipCount(iter_14_3[TeamType.Vanguard]) == 0:
			-- block empty
		else
			local var_14_4 = {}
			local var_14_5 = {}
			local var_14_6 = 0

			for iter_14_4, iter_14_5 in ipairs(var_14_1):
				local var_14_7, var_14_8, var_14_9, var_14_10 = unpack(iter_14_5)

				if string.sub(var_14_7, 1, 5) == "fleet":
					var_14_4[var_14_7] = 0
					var_14_5[var_14_7] = var_14_10

			for iter_14_6, iter_14_7 in pairs(iter_14_3):
				for iter_14_8 = 1, 3:
					local var_14_11 = iter_14_7[iter_14_8] and var_14_0[iter_14_7[iter_14_8]]

					if var_14_11:
						var_14_3 = var_14_3 + 1
						var_14_6 = var_14_6 + 1

						local var_14_12 = intProperties(var_14_11.getProperties())

						for iter_14_9, iter_14_10 in pairs(var_14_2):
							if string.sub(iter_14_9, 1, 5) == "fleet":
								if iter_14_9 == "fleet_totle_level":
									var_14_4[iter_14_9] = var_14_4[iter_14_9] + var_14_11.level
							elif iter_14_9 == "level":
								var_14_2[iter_14_9] = iter_14_10 + var_14_11.level
							else
								var_14_2[iter_14_9] = iter_14_10 + var_14_12[iter_14_9]

			for iter_14_11, iter_14_12 in pairs(var_14_4):
				if iter_14_11 == "fleet_totle_level" and iter_14_12 > var_14_5[iter_14_11]:
					var_14_2[iter_14_11] = var_14_2[iter_14_11] + 1

	local var_14_13 = {}

	for iter_14_13, iter_14_14 in ipairs(var_14_1):
		local var_14_14, var_14_15, var_14_16, var_14_17 = unpack(iter_14_14)

		if var_14_14 == "level" and var_14_3 > 0:
			var_14_2[var_14_14] = math.ceil(var_14_2[var_14_14] / var_14_3)

		var_14_13[iter_14_13] = AttributeType.EliteConditionCompare(var_14_15, var_14_2[var_14_14], var_14_16) and 1 or 0

	return var_14_13, var_14_2

def var_0_0.updateEliteLimit(arg_15_0):
	local var_15_0 = pg.gameset.world_fleet_unlock_level.description

	if #var_15_0 == 0:
		return

	local var_15_1, var_15_2 = arg_15_0.IsPropertyLimitationSatisfy()
	local var_15_3 = UIItemList.New(arg_15_0.tfLimitContainer, arg_15_0.tfLimitTpl)

	var_15_3.make(function(arg_16_0, arg_16_1, arg_16_2)
		arg_16_1 = arg_16_1 + 1

		if arg_16_0 == UIItemList.EventUpdate:
			local var_16_0 = var_15_0[arg_16_1]
			local var_16_1, var_16_2, var_16_3, var_16_4 = unpack(var_16_0)

			if var_15_1[arg_16_1] == 1:
				arg_16_2.Find("Text").GetComponent(typeof(Text)).color = Color.New(1, 0.9607843137254902, 0.5019607843137255)
			else
				arg_16_2.Find("Text").GetComponent(typeof(Text)).color = Color.New(0.9568627450980393, 0.30196078431372547, 0.30196078431372547)

			local var_16_5 = (AttributeType.EliteCondition2Name(var_16_1, var_16_4) .. AttributeType.eliteConditionCompareTip(var_16_2) .. var_16_3) .. "（" .. var_15_2[var_16_1] .. "）"

			setText(arg_16_2.Find("Text"), var_16_5))
	var_15_3.align(#var_15_0)

def var_0_0.updateCommanderBtn(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_1.Find("btn_recom")
	local var_17_1 = arg_17_1.Find("btn_clear")
	local var_17_2 = arg_17_1.Find("commander")

	setActive(var_17_0, not arg_17_0.contextData.showCommander)
	setActive(var_17_1, not arg_17_0.contextData.showCommander)
	setActive(var_17_2, arg_17_0.contextData.showCommander)

def var_0_0.UpdateFleet(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = arg_18_1.Find("commander")

	arg_18_0.updateCommanders(var_18_0, arg_18_2, arg_18_3)

	local var_18_1 = arg_18_0.contextData.fleets[arg_18_2][arg_18_3]
	local var_18_2 = (arg_18_2 == FleetType.Submarine and 10 or 0) + arg_18_3

	setText(arg_18_1.Find("bg/name"), Fleet.DEFAULT_NAME[var_18_2])

	if arg_18_2 == FleetType.Normal:
		arg_18_0.UpdateShips(arg_18_1.Find(TeamType.Main), TeamType.Main, var_18_1)
		arg_18_0.UpdateShips(arg_18_1.Find(TeamType.Vanguard), TeamType.Vanguard, var_18_1)
		setActive(arg_18_1.Find("selected"), arg_18_0.GetTeamShipCount(var_18_1[TeamType.Main]) > 0 and arg_18_0.GetTeamShipCount(var_18_1[TeamType.Vanguard]) > 0)
	elif arg_18_2 == FleetType.Submarine:
		arg_18_0.UpdateShips(arg_18_1.Find(TeamType.Submarine), TeamType.Submarine, var_18_1)
		setActive(arg_18_1.Find("selected"), arg_18_0.GetTeamShipCount(var_18_1[TeamType.Submarine]) > 0)

	local var_18_3 = arg_18_1.Find("btn_recom")
	local var_18_4 = arg_18_1.Find("btn_clear")

	onButton(arg_18_0, var_18_3, function()
		arg_18_0.RecommendFormation(arg_18_2, arg_18_3)
		arg_18_0.UpdateFleet(arg_18_1, arg_18_2, arg_18_3)
		arg_18_0.updateEliteLimit(), SFX_PANEL)
	onButton(arg_18_0, var_18_4, function()
		if arg_18_0.GetTeamShipCount(var_18_1[TeamType.Main]) > 0 or arg_18_0.GetTeamShipCount(var_18_1[TeamType.Vanguard]) > 0 or arg_18_0.GetTeamShipCount(var_18_1[TeamType.Submarine]) > 0:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("battle_preCombatLayer_clear_confirm"),
				def onYes:()
					var_18_1[TeamType.Main] = {}
					var_18_1[TeamType.Vanguard] = {}
					var_18_1[TeamType.Submarine] = {}

					arg_18_0.UpdateFleet(arg_18_1, arg_18_2, arg_18_3)
					arg_18_0.updateEliteLimit()
			}), SFX_CANCEL)

def var_0_0.updateCommanders(arg_22_0, arg_22_1, arg_22_2, arg_22_3):
	local var_22_0 = arg_22_0.contextData.fleets[arg_22_2][arg_22_3]
	local var_22_1 = Fleet.New({
		ship_list = {},
		commanders = var_22_0.commanders
	})

	for iter_22_0 = 1, 2:
		local var_22_2 = var_22_1.getCommanderByPos(iter_22_0)
		local var_22_3 = arg_22_1.Find("pos" .. iter_22_0)
		local var_22_4 = var_22_3.Find("add")
		local var_22_5 = var_22_3.Find("info")

		setActive(var_22_4, not var_22_2)
		setActive(var_22_5, var_22_2)

		if var_22_2:
			local var_22_6 = Commander.rarity2Frame(var_22_2.getRarity())

			setImageSprite(var_22_5.Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_22_6))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_22_2.getPainting(), "", var_22_5.Find("mask/icon"))
		else
			local var_22_7 = 1

			while var_22_0.commanders[var_22_7] and var_22_0.commanders[var_22_7].pos != iter_22_0:
				var_22_7 = var_22_7 + 1

			if var_22_0.commanders[var_22_7]:
				table.remove(var_22_0.commanders, var_22_7)

		onButton(arg_22_0, var_22_4, function()
			arg_22_0.openCommanderPanel(var_22_1, arg_22_2, arg_22_3), SFX_PANEL)
		onButton(arg_22_0, var_22_5, function()
			arg_22_0.openCommanderPanel(var_22_1, arg_22_2, arg_22_3), SFX_PANEL)

def var_0_0.UpdateShips(arg_25_0, arg_25_1, arg_25_2, arg_25_3):
	local var_25_0 = getProxy(BayProxy)
	local var_25_1 = arg_25_3[arg_25_2]
	local var_25_2 = {}

	for iter_25_0, iter_25_1 in ipairs({
		TeamType.Vanguard,
		TeamType.Main,
		TeamType.Submarine
	}):
		for iter_25_2 = 1, 3:
			local var_25_3 = arg_25_3[iter_25_1][iter_25_2] and var_25_0.getShipById(arg_25_3[iter_25_1][iter_25_2]) or None

			table.insert(var_25_2, var_25_3)

			if not var_25_3:
				arg_25_3[iter_25_1][iter_25_2] = None

	removeAllChildren(arg_25_1)

	for iter_25_3 = 1, 3:
		local var_25_4
		local var_25_5

		if var_25_1[iter_25_3]:
			var_25_4 = cloneTplTo(arg_25_0.rtShipTpl, arg_25_1, "ship_" .. var_25_1[iter_25_3])
			var_25_5 = var_25_0.getShipById(var_25_1[iter_25_3])

			updateShip(var_25_4, var_25_5)
		else
			var_25_4 = cloneTplTo(arg_25_0.rtEmptyTpl, arg_25_1, "empty")

			setActive(var_25_4.Find("ship_type"), False)

		onButton(arg_25_0, var_25_4.Find("icon_bg"), function()
			arg_25_0.emit(WorldFleetSelectMediator.OnSelectShip, arg_25_2, var_25_1, iter_25_3), SFX_PANEL)

		local var_25_6 = GetOrAddComponent(var_25_4.Find("icon_bg"), typeof(UILongPressTrigger))

		pg.DelegateInfo.Add(arg_25_0, var_25_6.onLongPressed)
		var_25_6.onLongPressed.RemoveAllListeners()
		var_25_6.onLongPressed.AddListener(function()
			if not var_25_5:
				arg_25_0.emit(WorldFleetSelectMediator.OnSelectShip, arg_25_2, var_25_1, iter_25_3)
			else
				arg_25_0.emit(WorldFleetSelectMediator.OnShipDetail, {
					shipId = var_25_5.id,
					shipVOs = var_25_2
				}))

def var_0_0.setCommanderPrefabs(arg_28_0, arg_28_1):
	arg_28_0.commanderPrefabs = arg_28_1

def var_0_0.openCommanderPanel(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	arg_29_0.levelCMDFormationView.setCallback(function(arg_30_0)
		if arg_30_0.type == LevelUIConst.COMMANDER_OP_SHOW_SKILL:
			arg_29_0.emit(WorldFleetSelectMediator.OnCommanderSkill, arg_30_0.skill)
		elif arg_30_0.type == LevelUIConst.COMMANDER_OP_ADD:
			arg_29_0.contextData.eliteCommanderSelected = {
				fleetType = arg_29_2,
				fleetIndex = arg_29_3,
				pos = arg_30_0.pos
			}

			arg_29_0.emit(WorldFleetSelectMediator.OnSelectEliteCommander, arg_29_2, arg_29_3, arg_30_0.pos)
			arg_29_0.closeCommanderPanel()
		else
			arg_29_0.emit(WorldFleetSelectMediator.OnCommanderFormationOp, {
				FleetType = LevelUIConst.FLEET_TYPE_WORLD,
				data = arg_30_0,
				fleets = arg_29_0.contextData.fleets,
				fleetType = arg_29_2,
				fleetIndex = arg_29_3
			}))
	arg_29_0.levelCMDFormationView.Load()
	arg_29_0.levelCMDFormationView.ActionInvoke("update", arg_29_1, arg_29_0.commanderPrefabs)
	arg_29_0.levelCMDFormationView.ActionInvoke("Show")

def var_0_0.closeCommanderPanel(arg_31_0):
	arg_31_0.levelCMDFormationView.ActionInvoke("Hide")

def var_0_0.updateCommanderFleet(arg_32_0, arg_32_1):
	if arg_32_0.levelCMDFormationView.isShowing():
		arg_32_0.levelCMDFormationView.ActionInvoke("updateFleet", arg_32_1)

def var_0_0.updateCommanderPrefab(arg_33_0):
	if arg_33_0.levelCMDFormationView.isShowing():
		arg_33_0.levelCMDFormationView.ActionInvoke("updatePrefabs", arg_33_0.commanderPrefabs)

def var_0_0.buildCommanderPanel(arg_34_0):
	arg_34_0.levelCMDFormationView = LevelCMDFormationView.New(arg_34_0._tf, arg_34_0.event, arg_34_0.contextData)

def var_0_0.destroyCommanderPanel(arg_35_0):
	arg_35_0.levelCMDFormationView.Destroy()

	arg_35_0.levelCMDFormationView = None

def var_0_0.CheckValid(arg_36_0):
	for iter_36_0, iter_36_1 in pairs(arg_36_0.contextData.fleets):
		if iter_36_0 == FleetType.Normal:
			for iter_36_2, iter_36_3 in ipairs(iter_36_1):
				if arg_36_0.GetTeamShipCount(iter_36_3[TeamType.Main]) == 0 or arg_36_0.GetTeamShipCount(iter_36_3[TeamType.Vanguard]) == 0:
					return False, i18n("world_fleet_formation_not_valid", Fleet.DEFAULT_NAME[iter_36_2])

	local var_36_0, var_36_1 = arg_36_0.IsPropertyLimitationSatisfy()
	local var_36_2 = 1

	for iter_36_4, iter_36_5 in ipairs(var_36_0):
		var_36_2 = var_36_2 * iter_36_5

	if var_36_2 != 1:
		return False, i18n("elite_disable_property_unsatisfied")

	return True

def var_0_0.GetTeamShipCount(arg_37_0, arg_37_1):
	local var_37_0 = 0

	for iter_37_0 = 1, 3:
		if arg_37_1[iter_37_0]:
			var_37_0 = var_37_0 + 1

	return var_37_0

def var_0_0.RecommendFormation(arg_38_0, arg_38_1, arg_38_2):
	local var_38_0 = {
		[FleetType.Normal] = {
			TeamType.Main,
			TeamType.Vanguard
		},
		[FleetType.Submarine] = {
			TeamType.Submarine
		}
	}
	local var_38_1 = {}

	for iter_38_0, iter_38_1 in pairs(arg_38_0.contextData.fleets):
		for iter_38_2, iter_38_3 in ipairs(iter_38_1):
			for iter_38_4, iter_38_5 in ipairs(var_38_0[iter_38_0]):
				for iter_38_6 = 1, 3:
					local var_38_2 = iter_38_3[iter_38_5][iter_38_6]

					if var_38_2:
						table.insert(var_38_1, var_38_2)

	local var_38_3 = arg_38_0.contextData.fleets[arg_38_1][arg_38_2]
	local var_38_4 = getProxy(BayProxy)

	for iter_38_7, iter_38_8 in ipairs(var_38_0[arg_38_1]):
		for iter_38_9 = 1, 3:
			if not var_38_3[iter_38_8][iter_38_9]:
				local var_38_5 = var_38_4.getWorldRecommendShip(iter_38_8, var_38_1)

				if var_38_5:
					var_38_3[iter_38_8][iter_38_9] = var_38_5.id

					table.insert(var_38_1, var_38_5.id)

def var_0_0.CheckWorldResetAward(arg_39_0):
	local var_39_0 = {}
	local var_39_1 = nowWorld()
	local var_39_2 = var_39_1.resetAward

	if var_39_2 and #var_39_2 > 0:
		local var_39_3 = pg.gameset.world_resetting_story.description[1]

		if #var_39_3 > 0:
			table.insert(var_39_0, function(arg_40_0)
				pg.NewStoryMgr.GetInstance().Play(var_39_3, arg_40_0, True))

		table.insert(var_39_0, function(arg_41_0)
			local var_41_0

			var_41_0 = {
				hideYes = True,
				hideNo = True,
				type = MSGBOX_TYPE_WORLD_RESET,
				def itemFunc:(arg_42_0)
					arg_39_0.emit(var_0_0.ON_DROP, arg_42_0, function()
						pg.MsgboxMgr.GetInstance().ShowMsgBox(var_41_0)),
				drops = var_39_2,
				tipWord = i18n("world_recycle_item_transform"),
				onNo = arg_41_0
			}

			pg.MsgboxMgr.GetInstance().ShowMsgBox(var_41_0))

	if var_39_1.resetLimitTip:
		table.insert(var_39_0, function(arg_44_0)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				content = i18n("world_resource_fill")
			}))

	seriesAsync(var_39_0, function()
		var_39_1.ClearResetAward())

return var_0_0
