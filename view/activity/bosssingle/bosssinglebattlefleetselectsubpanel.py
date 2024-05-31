local var_0_0 = class("BossSingleBattleFleetSelectSubPanel", import("view.base.BaseSubPanel"))

def var_0_0.getUIName(arg_1_0):
	return "BossSingleFleetSelectView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.tfShipTpl = arg_2_0.findTF("panel/shiptpl")
	arg_2_0.tfEmptyTpl = arg_2_0.findTF("panel/emptytpl")
	arg_2_0.tfFleets = {
		[FleetType.Normal] = {
			arg_2_0.findTF("panel/fleet/1"),
			arg_2_0.findTF("panel/fleet/2")
		},
		[FleetType.Submarine] = {
			arg_2_0.findTF("panel/sub/1")
		}
	}
	arg_2_0.tfLimit = arg_2_0.findTF("panel/limit_list/limit")
	arg_2_0.tfLimitTips = arg_2_0.findTF("panel/limit_list/limit_tip")
	arg_2_0.tfLimitElite = arg_2_0.findTF("panel/limit_list/limit_elite")

	setText(arg_2_0.findTF("sub/Text", arg_2_0.tfLimitElite), i18n("ship_limit_notice"))

	arg_2_0.tfLimitContainer = arg_2_0.findTF("panel/limit_list/limit_elite/limit_list")
	arg_2_0.rtCostLimit = arg_2_0._tf.Find("panel/limit_list/cost_limit")
	arg_2_0.btnBack = arg_2_0.findTF("panel/btnBack")
	arg_2_0.btnGo = arg_2_0.findTF("panel/start_button")
	arg_2_0.btnTry = arg_2_0.findTF("panel/try_button")
	arg_2_0.btnASHelp = arg_2_0.findTF("panel/title/ASvalue")
	arg_2_0.commanderToggle = arg_2_0.findTF("panel/commander_btn")
	arg_2_0.formationToggle = arg_2_0.findTF("panel/formation_btn")
	arg_2_0.toggleMask = arg_2_0.findTF("mask")
	arg_2_0.toggleList = arg_2_0.findTF("mask/list")
	arg_2_0.toggles = {}

	for iter_2_0 = 0, arg_2_0.toggleList.childCount - 1:
		table.insert(arg_2_0.toggles, arg_2_0.toggleList.Find("item" .. iter_2_0 + 1))

	arg_2_0.btnSp = arg_2_0.findTF("panel/sp")
	arg_2_0.spMask = arg_2_0.findTF("mask_sp")

	setActive(arg_2_0.tfShipTpl, False)
	setActive(arg_2_0.tfEmptyTpl, False)
	setActive(arg_2_0.toggleMask, False)
	setActive(arg_2_0.btnSp, False)
	setActive(arg_2_0.spMask, False)
	setActive(arg_2_0.tfLimitElite, False)
	setActive(arg_2_0.tfLimitTips, False)
	setActive(arg_2_0.tfLimit, False)
	setActive(arg_2_0.findTF("panel/title/ASvalue"), False)
	setText(arg_2_0.findTF("panel/formation_btn/text"), i18n("autofight_formation"))
	setText(arg_2_0.findTF("panel/commander_btn/text"), i18n("autofight_cat"))
	setText(arg_2_0._tf.Find("panel/title/Image/text"), i18n("fleet_select_title"))
	arg_2_0.InitInteractable()

def var_0_0.InitInteractable(arg_3_0):
	onButton(arg_3_0, arg_3_0.btnGo, function()
		local var_4_0, var_4_1 = arg_3_0.CheckValid()

		if var_4_0:
			arg_3_0.OnCombat()
		else
			pg.TipsMgr.GetInstance().ShowTips(var_4_1), SFX_UI_WEIGHANCHOR_GO)
	onButton(arg_3_0, arg_3_0.btnBack, function()
		arg_3_0.OnCancel()
		arg_3_0.OnCommit(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.OnCancel()
		arg_3_0.OnCommit(), SFX_CANCEL)
	onToggle(arg_3_0, arg_3_0.commanderToggle, function(arg_7_0)
		if arg_7_0:
			arg_3_0.viewParent.contextData.showCommander = arg_7_0

			for iter_7_0, iter_7_1 in pairs(arg_3_0.tfFleets):
				for iter_7_2 = 1, #iter_7_1:
					arg_3_0.updateCommanderBtn(iter_7_0, iter_7_2), SFX_PANEL)
	onToggle(arg_3_0, arg_3_0.formationToggle, function(arg_8_0)
		if arg_8_0:
			arg_3_0.viewParent.contextData.showCommander = not arg_8_0

			for iter_8_0, iter_8_1 in pairs(arg_3_0.tfFleets):
				for iter_8_2 = 1, #iter_8_1:
					arg_3_0.updateCommanderBtn(iter_8_0, iter_8_2), SFX_PANEL)

def var_0_0.SetFleets(arg_9_0, arg_9_1):
	arg_9_0.fleets = {
		[FleetType.Normal] = {},
		[FleetType.Submarine] = {}
	}

	for iter_9_0, iter_9_1 in pairs(arg_9_1):
		iter_9_1.RemoveUnusedItems()

		if iter_9_1.isSubmarineFleet():
			if #arg_9_0.fleets[FleetType.Submarine] < arg_9_0.getLimitNums(FleetType.Submarine):
				table.insert(arg_9_0.fleets[FleetType.Submarine], iter_9_1)
		elif #arg_9_0.fleets[FleetType.Normal] < arg_9_0.getLimitNums(FleetType.Normal):
			table.insert(arg_9_0.fleets[FleetType.Normal], iter_9_1)

def var_0_0.SetOilLimit(arg_10_0, arg_10_1):
	local var_10_0 = _.any(arg_10_1, function(arg_11_0)
		return arg_11_0 > 0)

	setActive(arg_10_0.rtCostLimit, var_10_0)
	setText(arg_10_0.rtCostLimit.Find("text"), i18n("formationScene_use_oil_limit_tip_worldboss"))

	if var_10_0:
		local var_10_1 = 0
		local var_10_2 = arg_10_1[1]

		setActive(arg_10_0.rtCostLimit.Find("cost_noraml/Text"), var_10_2 > 0)

		if var_10_2 > 0:
			setText(arg_10_0.rtCostLimit.Find("cost_noraml/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_surface"), var_10_2))

		local var_10_3 = 0

		setActive(arg_10_0.rtCostLimit.Find("cost_boss/Text"), var_10_3 > 0)

		local var_10_4 = arg_10_1[2]

		setActive(arg_10_0.rtCostLimit.Find("cost_sub/Text"), var_10_4 > 0)

		if var_10_4 > 0:
			setText(arg_10_0.rtCostLimit.Find("cost_sub/Text"), string.format("%s(%d)", i18n("formationScene_use_oil_limit_submarine"), var_10_4))

def var_0_0.SetSettings(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4, arg_12_5):
	arg_12_0.groupNum = arg_12_1
	arg_12_0.submarineNum = arg_12_2
	arg_12_0.showTryBtn = arg_12_3
	arg_12_0.propetyLimitation = arg_12_4
	arg_12_0.index = arg_12_5

def var_0_0.UpdateView(arg_13_0):
	arg_13_0.clearFleets()
	arg_13_0.UpdateFleets()
	arg_13_0.updatePropetyLimit()

	local var_13_0 = not LOCK_COMMANDER and pg.SystemOpenMgr.GetInstance().isOpenSystem(getProxy(PlayerProxy).getRawData().level, "CommanderCatMediator")

	triggerToggle(arg_13_0.viewParent.contextData.showCommander and var_13_0 and arg_13_0.commanderToggle or arg_13_0.formationToggle, True)
	setActive(arg_13_0.commanderToggle, var_13_0)
	setActive(arg_13_0.btnTry, arg_13_0.showTryBtn)

def var_0_0.getLimitNums(arg_14_0, arg_14_1):
	local var_14_0 = 0

	if arg_14_1 == FleetType.Normal:
		var_14_0 = arg_14_0.groupNum
	elif arg_14_1 == FleetType.Submarine:
		var_14_0 = arg_14_0.submarineNum

	return var_14_0 or 0

def var_0_0.UpdateFleets(arg_15_0):
	for iter_15_0, iter_15_1 in pairs(arg_15_0.tfFleets):
		for iter_15_2 = 1, #iter_15_1:
			arg_15_0.updateFleet(iter_15_0, iter_15_2)

def var_0_0.updateFleet(arg_16_0, arg_16_1, arg_16_2):
	arg_16_0.updateCommanderBtn(arg_16_1, arg_16_2)

	local var_16_0 = arg_16_2 <= arg_16_0.getLimitNums(arg_16_1)
	local var_16_1 = var_16_0 and arg_16_0.fleets[arg_16_1][arg_16_2]
	local var_16_2 = arg_16_0.tfFleets[arg_16_1][arg_16_2]
	local var_16_3 = findTF(var_16_2, "bg/name")
	local var_16_4 = arg_16_0.findTF(TeamType.Main, var_16_2)
	local var_16_5 = arg_16_0.findTF(TeamType.Vanguard, var_16_2)
	local var_16_6 = arg_16_0.findTF(TeamType.Submarine, var_16_2)
	local var_16_7 = arg_16_0.findTF("btn_recom", var_16_2)
	local var_16_8 = arg_16_0.findTF("btn_clear", var_16_2)
	local var_16_9 = arg_16_0.findTF("selected", var_16_2)
	local var_16_10 = arg_16_0.findTF("commander", var_16_2)

	setActive(var_16_9, False)
	setText(var_16_3, "")

	if var_16_4:
		setActive(var_16_4, var_16_0 and var_16_1)

	if var_16_5:
		setActive(var_16_5, var_16_0 and var_16_1)

	if var_16_6:
		setActive(var_16_6, var_16_0 and var_16_1)

	if var_16_0 and var_16_1:
		setText(var_16_3, Fleet.DEFAULT_NAME_BOSS_SINGLE_ACT[var_16_1.id] or "")

		if arg_16_1 == FleetType.Submarine:
			arg_16_0.updateShips(var_16_6, var_16_1.subShips, var_16_1.id, TeamType.Submarine)
		else
			arg_16_0.updateShips(var_16_4, var_16_1.mainShips, var_16_1.id, TeamType.Main)
			arg_16_0.updateShips(var_16_5, var_16_1.vanguardShips, var_16_1.id, TeamType.Vanguard)

		arg_16_0.updateCommanders(var_16_10, var_16_1)
		onButton(arg_16_0, var_16_7, function()
			arg_16_0.emit(arg_16_0.viewParent.contextData.mediatorClass.ON_FLEET_RECOMMEND, var_16_1.id))
		onButton(arg_16_0, var_16_8, function()
			arg_16_0.emit(arg_16_0.viewParent.contextData.mediatorClass.ON_FLEET_CLEAR, var_16_1.id), SFX_UI_CLICK)

def var_0_0.updateShips(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4):
	removeAllChildren(arg_19_1)

	local var_19_0 = getProxy(BayProxy)

	for iter_19_0 = 1, 3:
		local var_19_1 = var_19_0.getShipById(arg_19_2[iter_19_0])
		local var_19_2 = var_19_1 and arg_19_0.tfShipTpl or arg_19_0.tfEmptyTpl
		local var_19_3 = cloneTplTo(var_19_2, arg_19_1)

		setActive(var_19_3, True)

		if var_19_1:
			updateShip(var_19_3, var_19_1)
			setActive(var_19_3.Find("event_block"), var_19_1.getFlag("inEvent"))

		setActive(arg_19_0.findTF("ship_type", var_19_3), False)

		local var_19_4 = GetOrAddComponent(var_19_3, typeof(UILongPressTrigger))

		var_19_4.onLongPressed.RemoveAllListeners()

		local function var_19_5()
			arg_19_0.emit(arg_19_0.viewParent.contextData.mediatorClass.ON_OPEN_DOCK, {
				fleet = arg_19_2,
				shipVO = var_19_1,
				fleetIndex = arg_19_3,
				teamType = arg_19_4
			})

		onButton(arg_19_0, var_19_3, var_19_5)
		var_19_4.onLongPressed.AddListener(function()
			if var_19_1:
				arg_19_0.OnLongPressShip(arg_19_2[iter_19_0], arg_19_3)
			else
				var_19_5())

def var_0_0.updateCommanderBtn(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_2 <= arg_22_0.getLimitNums(arg_22_1)
	local var_22_1 = var_22_0 and arg_22_0.fleets[arg_22_1][arg_22_2]
	local var_22_2 = arg_22_0.tfFleets[arg_22_1][arg_22_2]
	local var_22_3 = arg_22_0.findTF("btn_select", var_22_2)
	local var_22_4 = arg_22_0.findTF("btn_clear", var_22_2)
	local var_22_5 = arg_22_0.findTF("btn_recom", var_22_2)
	local var_22_6 = arg_22_0.findTF("blank", var_22_2)
	local var_22_7 = arg_22_0.findTF("commander", var_22_2)

	setActive(var_22_3, False)
	setActive(var_22_4, var_22_0 and not arg_22_0.viewParent.contextData.showCommander)
	setActive(var_22_5, var_22_0 and not arg_22_0.viewParent.contextData.showCommander)
	setActive(var_22_7, var_22_0 and var_22_1 and arg_22_0.viewParent.contextData.showCommander)
	setActive(var_22_6, not var_22_0 or var_22_0 and not var_22_1 and arg_22_0.viewParent.contextData.showCommander)

def var_0_0.updateCommanders(arg_23_0, arg_23_1, arg_23_2):
	for iter_23_0 = 1, 2:
		local var_23_0 = arg_23_2.getCommanderByPos(iter_23_0)
		local var_23_1 = arg_23_1.Find("pos" .. iter_23_0)
		local var_23_2 = var_23_1.Find("add")
		local var_23_3 = var_23_1.Find("info")

		setActive(var_23_2, not var_23_0)
		setActive(var_23_3, var_23_0)

		if var_23_0:
			local var_23_4 = Commander.rarity2Frame(var_23_0.getRarity())

			setImageSprite(var_23_3.Find("frame"), GetSpriteFromAtlas("weaponframes", "commander_" .. var_23_4))
			GetImageSpriteFromAtlasAsync("CommanderHrz/" .. var_23_0.getPainting(), "", var_23_3.Find("mask/icon"))

		onButton(arg_23_0, var_23_2, function()
			arg_23_0.InvokeParent("openCommanderPanel", arg_23_2, arg_23_2.id), SFX_PANEL)
		onButton(arg_23_0, var_23_3, function()
			arg_23_0.InvokeParent("openCommanderPanel", arg_23_2, arg_23_2.id), SFX_PANEL)

def var_0_0.clearFleets(arg_26_0):
	for iter_26_0, iter_26_1 in pairs(arg_26_0.tfFleets):
		_.each(iter_26_1, function(arg_27_0)
			arg_26_0.clearFleet(arg_27_0))

def var_0_0.clearFleet(arg_28_0, arg_28_1):
	local var_28_0 = arg_28_0.findTF(TeamType.Main, arg_28_1)
	local var_28_1 = arg_28_0.findTF(TeamType.Vanguard, arg_28_1)
	local var_28_2 = arg_28_0.findTF(TeamType.Submarine, arg_28_1)

	if var_28_0:
		removeAllChildren(var_28_0)

	if var_28_1:
		removeAllChildren(var_28_1)

	if var_28_2:
		removeAllChildren(var_28_2)

def var_0_0.updatePropetyLimit(arg_29_0):
	setActive(arg_29_0.toggleMask, False)
	setActive(arg_29_0.tfLimit, False)
	setActive(arg_29_0.tfLimitTips, False)
	setActive(arg_29_0.tfLimitElite, #arg_29_0.propetyLimitation > 0)

	if #arg_29_0.propetyLimitation > 0:
		local var_29_0 = UIItemList.New(arg_29_0.tfLimitContainer, arg_29_0.tfLimitContainer.GetChild(0))
		local var_29_1, var_29_2 = arg_29_0.IsPropertyLimitationSatisfy()

		var_29_0.make(function(arg_30_0, arg_30_1, arg_30_2)
			arg_30_1 = arg_30_1 + 1

			if arg_30_0 == UIItemList.EventUpdate:
				local var_30_0 = arg_29_0.propetyLimitation[arg_30_1]
				local var_30_1, var_30_2, var_30_3, var_30_4 = unpack(var_30_0)

				if var_29_1[arg_30_1] == 1:
					arg_29_0.findTF("Text", arg_30_2).GetComponent(typeof(Text)).color = Color.New(1, 0.9607843137254902, 0.5019607843137255)
				else
					arg_29_0.findTF("Text", arg_30_2).GetComponent(typeof(Text)).color = Color.New(0.9568627450980393, 0.30196078431372547, 0.30196078431372547)

				setActive(arg_30_2, True)

				local var_30_5 = AttributeType.EliteCondition2Name(var_30_1, var_30_4) .. AttributeType.eliteConditionCompareTip(var_30_2) .. var_30_3

				setText(arg_29_0.findTF("Text", arg_30_2), var_30_5))
		var_29_0.align(#arg_29_0.propetyLimitation)

def var_0_0.OnShow(arg_31_0):
	local var_31_0 = #getProxy(ContextProxy).getCurrentContext().children > 0 and LayerWeightConst.LOWER_LAYER or None

	pg.UIMgr.GetInstance().BlurPanel(arg_31_0._tf, None, {
		groupName = LayerWeightConst.GROUP_FORMATION_PAGE,
		weight = var_31_0
	})

def var_0_0.OnHide(arg_32_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_32_0._tf, arg_32_0.viewParent._tf)
	triggerToggle(arg_32_0.commanderToggle, False)

def var_0_0.OnCancel(arg_33_0):
	arg_33_0.InvokeParent("hideFleetEdit")

def var_0_0.OnCommit(arg_34_0):
	arg_34_0.InvokeParent("commitEdit")

def var_0_0.OnCombat(arg_35_0):
	arg_35_0.InvokeParent("commitEdit")
	arg_35_0.InvokeParent("commitCombat")

def var_0_0.OnLongPressShip(arg_36_0, arg_36_1, arg_36_2):
	arg_36_0.InvokeParent("openShipInfo", arg_36_1, arg_36_2)

def var_0_0.IsPropertyLimitationSatisfy(arg_37_0):
	local var_37_0 = getProxy(BayProxy).getRawData()
	local var_37_1 = arg_37_0.propetyLimitation
	local var_37_2 = {}

	for iter_37_0, iter_37_1 in ipairs(var_37_1):
		var_37_2[iter_37_1[1]] = 0

	local var_37_3 = 0
	local var_37_4 = {}

	for iter_37_2 = 1, 2:
		local var_37_5 = arg_37_0.fleets[FleetType.Normal][iter_37_2]

		if var_37_5:
			for iter_37_3, iter_37_4 in pairs(var_37_5.mainShips):
				table.insert(var_37_4, iter_37_4)

			for iter_37_5, iter_37_6 in pairs(var_37_5.vanguardShips):
				table.insert(var_37_4, iter_37_6)

	local var_37_6 = {}
	local var_37_7 = {}

	for iter_37_7, iter_37_8 in ipairs(var_37_1):
		local var_37_8, var_37_9, var_37_10, var_37_11 = unpack(iter_37_8)

		if string.sub(var_37_8, 1, 5) == "fleet":
			var_37_6[var_37_8] = 0
			var_37_7[var_37_8] = var_37_11

	for iter_37_9, iter_37_10 in ipairs(var_37_4):
		local var_37_12 = var_37_0[iter_37_10]

		var_37_3 = var_37_3 + 1

		local var_37_13 = intProperties(var_37_12.getProperties())

		for iter_37_11, iter_37_12 in pairs(var_37_2):
			if string.sub(iter_37_11, 1, 5) == "fleet":
				if iter_37_11 == "fleet_totle_level":
					var_37_6[iter_37_11] = var_37_6[iter_37_11] + var_37_12.level
			elif iter_37_11 == "level":
				var_37_2[iter_37_11] = iter_37_12 + var_37_12.level
			else
				var_37_2[iter_37_11] = iter_37_12 + var_37_13[iter_37_11]

	for iter_37_13, iter_37_14 in pairs(var_37_6):
		if iter_37_13 == "fleet_totle_level" and iter_37_14 > var_37_7[iter_37_13]:
			var_37_2[iter_37_13] = var_37_2[iter_37_13] + 1

	local var_37_14 = {}

	for iter_37_15, iter_37_16 in ipairs(var_37_1):
		local var_37_15, var_37_16, var_37_17 = unpack(iter_37_16)

		if var_37_15 == "level" and var_37_3 > 0:
			var_37_2[var_37_15] = math.ceil(var_37_2[var_37_15] / var_37_3)

		var_37_14[iter_37_15] = AttributeType.EliteConditionCompare(var_37_16, var_37_2[var_37_15], var_37_17) and 1 or 0

	return var_37_14, var_37_2

def var_0_0.CheckValid(arg_38_0):
	local var_38_0, var_38_1 = arg_38_0.viewParent.contextData.bossActivity.CheckCntByIdx(arg_38_0.index)

	if not var_38_0:
		return var_38_0, var_38_1

	local var_38_2, var_38_3 = arg_38_0.IsPropertyLimitationSatisfy()
	local var_38_4 = 1

	for iter_38_0, iter_38_1 in ipairs(var_38_2):
		var_38_4 = var_38_4 * iter_38_1

	if var_38_4 != 1:
		return False, i18n("elite_disable_property_unsatisfied")

	return True

return var_0_0
