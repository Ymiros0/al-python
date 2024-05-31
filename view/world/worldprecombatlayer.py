local var_0_0 = class("WorldPreCombatLayer", import("..base.BaseUI"))
local var_0_1 = import("..ship.FormationUI")
local var_0_2 = {
	[99] = True
}

def var_0_0.getUIName(arg_1_0):
	return "WorldPreCombatUI"

def var_0_0.init(arg_2_0):
	arg_2_0.eventTriggers = {}
	arg_2_0.middle = arg_2_0.findTF("middle")
	arg_2_0.right = arg_2_0.findTF("right")
	arg_2_0.top = arg_2_0.findTF("top")
	arg_2_0.moveLayer = arg_2_0.findTF("moveLayer")
	arg_2_0.backBtn = arg_2_0.top.Find("back_btn")
	arg_2_0.playerResOb = arg_2_0.top.Find("playerRes")
	arg_2_0.resPanel = WorldResource.New()

	tf(arg_2_0.resPanel._go).SetParent(tf(arg_2_0.playerResOb), False)

	arg_2_0.strategyInfo = arg_2_0.findTF("strategy_info", arg_2_0.top)

	setActive(arg_2_0.strategyInfo, False)

	arg_2_0.mainGS = arg_2_0.middle.Find("gear_score/main/Text")
	arg_2_0.vanguardGS = arg_2_0.middle.Find("gear_score/vanguard/Text")

	setText(arg_2_0.mainGS, 0)
	setText(arg_2_0.vanguardGS, 0)

	arg_2_0.gridTFs = {
		vanguard = {},
		main = {}
	}
	arg_2_0.gridFrame = arg_2_0.middle.Find("mask/GridFrame")

	for iter_2_0 = 1, 3:
		arg_2_0.gridTFs[TeamType.Vanguard][iter_2_0] = arg_2_0.gridFrame.Find("vanguard_" .. iter_2_0)
		arg_2_0.gridTFs[TeamType.Main][iter_2_0] = arg_2_0.gridFrame.Find("main_" .. iter_2_0)

	arg_2_0.heroContainer = arg_2_0.middle.Find("HeroContainer")
	arg_2_0.strategy = arg_2_0.middle.Find("strategy")

	setActive(arg_2_0.strategy, False)

	arg_2_0.fleet = arg_2_0.findTF("middle/fleet")
	arg_2_0.ship_tpl = findTF(arg_2_0.fleet, "shiptpl")
	arg_2_0.empty_tpl = findTF(arg_2_0.fleet, "emptytpl")

	setActive(arg_2_0.ship_tpl, False)
	setActive(arg_2_0.empty_tpl, False)

	arg_2_0.autoToggle = arg_2_0.right.Find("auto_toggle")
	arg_2_0.autoSubToggle = arg_2_0.right.Find("sub_toggle_container/sub_toggle")
	arg_2_0.startBtn = arg_2_0.right.Find("start")
	arg_2_0.infoBtn = arg_2_0.right.Find("information")
	arg_2_0.heroInfo = arg_2_0.getTpl("heroInfo")
	arg_2_0.starTpl = arg_2_0.getTpl("star_tpl")
	arg_2_0.energyDescTF = arg_2_0.findTF("energy_desc")
	arg_2_0.energyDescTextTF = arg_2_0.findTF("energy_desc/Text")
	arg_2_0.normaltab = arg_2_0.right.Find("normal")
	arg_2_0.informationtab = arg_2_0.right.Find("infomation")
	arg_2_0.buffInfo = arg_2_0.normaltab.Find("buff")
	arg_2_0.bossInfo = arg_2_0.normaltab.Find("boss")
	arg_2_0.spoilsContainer = arg_2_0.normaltab.Find("spoils/items/items_container")
	arg_2_0.spoilsItem = arg_2_0.normaltab.Find("spoils/items/item_tpl")
	arg_2_0.digits = arg_2_0.Clone2Full(arg_2_0.informationtab.Find("target/simple/digits"), 3)
	arg_2_0.digitExtras = arg_2_0.Clone2Full(arg_2_0.informationtab.Find("target/detail"), 3)
	arg_2_0.dropright = arg_2_0.informationtab.Find("spoils/right")
	arg_2_0.dropleft = arg_2_0.informationtab.Find("spoils/left")
	arg_2_0.dropitems = arg_2_0.Clone2Full(arg_2_0.informationtab.Find("spoils/items_container"), 3)

	setActive(arg_2_0.informationtab.Find("target/simple"), True)
	setActive(arg_2_0.informationtab.Find("target/detail"), False)

	for iter_2_1 = 1, #arg_2_0.digitExtras:
		local var_2_0 = arg_2_0.digitExtras[iter_2_1]

		setText(var_2_0.Find("desc"), i18n("world_mapbuff_compare_txt") .. "：")

def var_0_0.uiStartAnimating(arg_3_0):
	setAnchoredPosition(arg_3_0.middle, {
		x = -840
	})
	setAnchoredPosition(arg_3_0.right, {
		x = 470
	})
	setAnchoredPosition(arg_3_0.top, {
		y = arg_3_0.top.rect.height
	})

	local var_3_0 = 0
	local var_3_1 = 0.3

	shiftPanel(arg_3_0.middle, 0, None, var_3_1, var_3_0, True, True)
	shiftPanel(arg_3_0.right, 0, None, var_3_1, var_3_0, True, True, None)
	shiftPanel(arg_3_0.top, None, 0, var_3_1, var_3_0, True, True, None, None)

def var_0_0.uiExitAnimating(arg_4_0):
	local var_4_0 = 0
	local var_4_1 = 0.3

	shiftPanel(arg_4_0.middle, -840, None, var_4_1, var_4_0, True, True)
	shiftPanel(arg_4_0.right, 470, None, var_4_1, var_4_0, True, True)
	shiftPanel(arg_4_0.top, None, arg_4_0.top.rect.height, var_4_1, var_4_0, True, True, None, None)

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0.backBtn, function()
		GetOrAddComponent(arg_5_0._tf, typeof(CanvasGroup)).interactable = False

		arg_5_0.uiExitAnimating()
		LeanTween.delayedCall(0.3, System.Action(function()
			arg_5_0.emit(var_0_0.ON_CLOSE))), SFX_CANCEL)
	onToggle(arg_5_0, arg_5_0.autoToggle, function(arg_8_0)
		arg_5_0.emit(WorldPreCombatMediator.OnAuto, {
			isOn = not arg_8_0,
			toggle = arg_5_0.autoToggle
		})

		if arg_8_0 and nowWorld().GetSubAidFlag():
			setActive(arg_5_0.autoSubToggle, True)
			onToggle(arg_5_0, arg_5_0.autoSubToggle, function(arg_9_0)
				arg_5_0.emit(WorldPreCombatMediator.OnSubAuto, {
					isOn = not arg_9_0,
					toggle = arg_5_0.autoSubToggle
				}), SFX_PANEL, SFX_PANEL)
			triggerToggle(arg_5_0.autoSubToggle, ys.Battle.BattleState.IsAutoSubActive(SYSTEM_WORLD))
		else
			setActive(arg_5_0.autoSubToggle, False), SFX_PANEL, SFX_PANEL)
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0._tf)
	arg_5_0.updateCharacters()
	arg_5_0.updateStageView()
	triggerToggle(arg_5_0.autoToggle, ys.Battle.BattleState.IsAutoBotActive(SYSTEM_WORLD))

	local var_5_0 = arg_5_0.GetCurrentAttachment()
	local var_5_1 = var_5_0.GetBattleStageId()
	local var_5_2 = pg.expedition_data_template[var_5_1]

	assert(var_5_2, "expedition_data_template not exist. " .. var_5_1)

	local var_5_3 = pg.world_expedition_data[var_5_1]
	local var_5_4 = var_5_3 and var_5_3.battle_type and var_5_3.battle_type != 0

	onNextTick(function()
		arg_5_0.uiStartAnimating())

	arg_5_0.contextData.entetagain = True

	setActive(arg_5_0.infoBtn, var_5_4)
	onButton(arg_5_0, arg_5_0.infoBtn, function()
		arg_5_0.emit(WorldPreCombatMediator.OnOpenSublayer, Context.New({
			mediator = WorldBossInformationMediator,
			viewComponent = WorldBossInformationLayer
		}), True, function()
			arg_5_0.closeView()))
	onButton(arg_5_0, arg_5_0.startBtn, function()
		arg_5_0.emit(WorldPreCombatMediator.OnStartBattle, var_5_0.GetBattleStageId(), arg_5_0.getCurrentFleet(), var_5_0), SFX_UI_WEIGHANCHOR)

def var_0_0.onBackPressed(arg_14_0):
	if arg_14_0.strategyPanel and arg_14_0.strategyPanel._go and isActive(arg_14_0.strategyPanel._go):
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		arg_14_0.hideStrategyInfo()
	else
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(arg_14_0.backBtn)

def var_0_0.setPlayerInfo(arg_15_0, arg_15_1):
	arg_15_0.resPanel.setPlayer(arg_15_1)
	setActive(arg_15_0.resPanel._tf, nowWorld().IsSystemOpen(WorldConst.SystemResource))

def var_0_0.getCurrentFleet(arg_16_0):
	return nowWorld().GetFleet()

def var_0_0.GetCurrentAttachment(arg_17_0):
	local var_17_0 = nowWorld().GetActiveMap()
	local var_17_1 = var_17_0.GetFleet()

	return var_17_0.GetCell(var_17_1.row, var_17_1.column).GetAliveAttachment(), var_17_0.config.difficulty

def var_0_0.updateStageView(arg_18_0):
	setActive(arg_18_0.normaltab, False)
	setActive(arg_18_0.informationtab, True)
	arg_18_0.UpdateInformationtab()

def var_0_0.UpdateNormaltab(arg_19_0):
	local var_19_0, var_19_1 = arg_19_0.GetCurrentAttachment()
	local var_19_2 = var_19_0.GetBattleStageId()
	local var_19_3 = pg.world_expedition_data[var_19_2]
	local var_19_4 = {}

	for iter_19_0, iter_19_1 in ipairs(var_19_3.award_display_world):
		if var_19_1 == iter_19_1[1]:
			var_19_4 = iter_19_1[2]

	local var_19_5 = UIItemList.New(arg_19_0.spoilsContainer, arg_19_0.spoilsItem)

	var_19_5.make(function(arg_20_0, arg_20_1, arg_20_2)
		local var_20_0 = arg_20_2
		local var_20_1 = var_19_4[arg_20_1 + 1]
		local var_20_2 = {
			type = var_20_1[1],
			id = var_20_1[2]
		}

		updateDrop(var_20_0, var_20_2)
		onButton(arg_19_0, var_20_0, function()
			arg_19_0.emit(var_0_0.ON_DROP, var_20_2), SFX_PANEL))
	var_19_5.align(#var_19_4)

local var_0_3 = "fe2222"
local var_0_4 = "92fc63"

def var_0_0.UpdateInformationtab(arg_22_0):
	local var_22_0, var_22_1 = arg_22_0.GetCurrentAttachment()
	local var_22_2 = var_22_0.GetBattleStageId()
	local var_22_3 = pg.world_expedition_data[var_22_2]

	assert(var_22_3, "world_expedition_data not exist. " .. var_22_2)

	local var_22_4 = {}

	for iter_22_0, iter_22_1 in ipairs(var_22_3.award_display_world):
		if var_22_1 == iter_22_1[1]:
			var_22_4 = iter_22_1[2]

	local var_22_5 = 0

	local function var_22_6()
		for iter_23_0 = 1, #arg_22_0.dropitems:
			local var_23_0 = arg_22_0.dropitems[iter_23_0].Find("item_tpl")
			local var_23_1 = var_22_4[iter_23_0 + var_22_5]

			setActive(var_23_0, var_23_1 != None)

			if var_23_1:
				local var_23_2 = {
					type = var_23_1[1],
					id = var_23_1[2]
				}

				updateDrop(var_23_0, var_23_2)
				setScrollText(var_23_0.Find("ScrollMask/DropName"), var_23_2.getConfig("name"))
				onButton(arg_22_0, var_23_0, function()
					arg_22_0.emit(var_0_0.ON_DROP, var_23_2), SFX_PANEL)

		setActive(arg_22_0.dropleft, var_22_5 > 0)
		setActive(arg_22_0.dropright, #var_22_4 - var_22_5 > #arg_22_0.dropitems)

	onButton(arg_22_0, arg_22_0.dropright, function()
		var_22_5 = var_22_5 + 1

		var_22_6())
	onButton(arg_22_0, arg_22_0.dropleft, function()
		var_22_5 = var_22_5 - 1

		var_22_6())
	var_22_6()

	local var_22_7 = nowWorld()
	local var_22_8 = ys.Battle.BattleFormulas
	local var_22_9 = var_22_7.GetWorldMapDifficultyBuffLevel()
	local var_22_10 = {
		var_22_9[1] * (1 + var_22_3.expedition_sairenvalueA / 10000),
		var_22_9[2] * (1 + var_22_3.expedition_sairenvalueB / 10000),
		var_22_9[3] * (1 + var_22_3.expedition_sairenvalueC / 10000)
	}
	local var_22_11 = var_22_7.GetWorldMapBuffLevel()
	local var_22_12, var_22_13, var_22_14 = var_22_8.WorldMapRewardAttrEnhance(var_22_10, var_22_11)
	local var_22_15 = 1 - var_22_8.WorldMapRewardHealingRate(var_22_10, var_22_11)
	local var_22_16 = {
		var_22_12,
		var_22_13,
		var_22_15
	}

	for iter_22_2 = 1, #arg_22_0.digits:
		local var_22_17 = arg_22_0.digits[iter_22_2]

		setText(var_22_17.Find("digit"), string.format("%d", var_22_10[iter_22_2]))

		local var_22_18 = iter_22_2 == 3 and 1 - var_22_16[iter_22_2] or var_22_16[iter_22_2] + 1

		setText(var_22_17.Find("desc"), i18n("world_mapbuff_attrtxt_" .. iter_22_2) .. string.format("%3d%%", var_22_18 * 100))

	for iter_22_3 = 1, #arg_22_0.digitExtras:
		local var_22_19 = arg_22_0.digitExtras[iter_22_3]

		setText(var_22_19.Find("enemy"), string.format("%d", var_22_10[iter_22_3]))
		setText(var_22_19.Find("ally"), string.format("%d", var_22_11[iter_22_3]))
		setText(var_22_19.Find("result"), string.format("%d%%", var_22_16[iter_22_3] * 100))
		setTextColor(var_22_19.Find("result"), var_22_16[iter_22_3] > 0 and arg_22_0.TransformColor(var_0_3) or arg_22_0.TransformColor(var_0_4))
		setText(var_22_19.Find("result/arrow"), var_22_16[iter_22_3] == 0 and "" or var_22_16[iter_22_3] > 0 and "↑" or "↓")

		if var_22_16[iter_22_3] != 0:
			setTextColor(var_22_19.Find("result/arrow"), var_22_16[iter_22_3] > 0 and arg_22_0.TransformColor(var_0_3) or arg_22_0.TransformColor(var_0_4))

	onButton(arg_22_0, arg_22_0.informationtab.Find("target/bg"), function()
		local var_27_0 = arg_22_0.informationtab.Find("target/simple")
		local var_27_1 = arg_22_0.informationtab.Find("target/detail")
		local var_27_2 = go(var_27_0).activeSelf

		setActive(var_27_0, not var_27_2)
		setActive(var_27_1, var_27_2), SFX_PANEL)

def var_0_0.updateCharacters(arg_28_0):
	pg.UIMgr.GetInstance().LoadingOn()
	arg_28_0.resetGrid(TeamType.Vanguard)
	arg_28_0.resetGrid(TeamType.Main)
	arg_28_0.loadAllCharacter(function()
		arg_28_0.updateFleetView()
		arg_28_0.displayFleetInfo()
		pg.UIMgr.GetInstance().LoadingOff())

def var_0_0.flushCharacters(arg_30_0):
	arg_30_0.resetGrid(TeamType.Vanguard)
	arg_30_0.resetGrid(TeamType.Main)
	arg_30_0.setAllCharacterPos(True)
	arg_30_0.updateFleetView()

def var_0_0.updateFleetView(arg_31_0):
	local function var_31_0(arg_32_0, arg_32_1)
		removeAllChildren(arg_32_0)

		for iter_32_0 = 1, 3:
			if arg_32_1[iter_32_0]:
				local var_32_0 = cloneTplTo(arg_31_0.ship_tpl, arg_32_0)

				updateShip(var_32_0, arg_32_1[iter_32_0])

				local var_32_1 = WorldConst.FetchWorldShip(arg_32_1[iter_32_0].id)
				local var_32_2 = var_32_1.IsHpSafe()
				local var_32_3 = var_32_1.IsAlive()
				local var_32_4 = findTF(var_32_0, "blood/fillarea/green")
				local var_32_5 = findTF(var_32_0, "blood/fillarea/red")

				setActive(var_32_4, var_32_2)
				setActive(var_32_5, not var_32_2)

				;(var_32_2 and var_32_4 or var_32_5).GetComponent("Image").fillAmount = var_32_1.hpRant * 0.0001

				setActive(var_32_0.Find("broken"), var_32_1.IsBroken())
				setActive(var_32_0.Find("mask"), not var_32_3)

	local var_31_1 = arg_31_0.getCurrentFleet()

	var_31_0(arg_31_0.fleet.Find("main"), var_31_1.GetTeamShipVOs(TeamType.Main, True))
	var_31_0(arg_31_0.fleet.Find("vanguard"), var_31_1.GetTeamShipVOs(TeamType.Vanguard, True))

def var_0_0.loadAllCharacter(arg_33_0, arg_33_1):
	removeAllChildren(arg_33_0.heroContainer)

	arg_33_0.characterList = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {}
	}

	local function var_33_0(arg_34_0, arg_34_1, arg_34_2, arg_34_3)
		if arg_33_0.exited:
			arg_34_0.Dispose()

			return

		local var_34_0 = arg_34_0.model
		local var_34_1 = WorldConst.FetchWorldShip(arg_34_1.id)

		arg_33_0.characterList[arg_34_2][arg_34_3] = arg_34_0

		tf(var_34_0).SetParent(arg_33_0.heroContainer, False)

		tf(var_34_0).localScale = Vector3(0.65, 0.65, 1)

		pg.ViewUtils.SetLayer(tf(var_34_0), Layer.UI)
		arg_33_0.enabledCharacter(var_34_0, True, arg_34_2)
		arg_33_0.setCharacterPos(arg_34_2, arg_34_3, var_34_0)
		arg_33_0.sortSiblingIndex()

		local var_34_2 = cloneTplTo(arg_33_0.heroInfo, var_34_0)

		setAnchoredPosition(var_34_2, {
			x = 0,
			y = 0
		})

		var_34_2.localScale = Vector3(2, 2, 1)

		SetActive(var_34_2, True)

		var_34_2.name = "info"

		local var_34_3 = findTF(var_34_2, "info")
		local var_34_4 = findTF(var_34_3, "stars")
		local var_34_5 = arg_34_1.getEnergy() <= Ship.ENERGY_MID
		local var_34_6 = findTF(var_34_3, "energy")

		if var_34_5:
			local var_34_7, var_34_8 = arg_34_1.getEnergyPrint()
			local var_34_9 = GetSpriteFromAtlas("energy", var_34_7)

			if not var_34_9:
				warning("找不到疲劳")

			setImageSprite(var_34_6, var_34_9)

		setActive(var_34_6, var_34_5)

		local var_34_10 = arg_34_1.getStar()

		for iter_34_0 = 1, var_34_10:
			cloneTplTo(arg_33_0.starTpl, var_34_4)

		local var_34_11 = GetSpriteFromAtlas("shiptype", shipType2print(arg_34_1.getShipType()))

		if not var_34_11:
			warning("找不到船形, shipConfigId. " .. arg_34_1.configId)

		setImageSprite(findTF(var_34_3, "type"), var_34_11, True)
		setText(findTF(var_34_3, "frame/lv_contain/lv"), arg_34_1.level)

		local var_34_12 = var_34_1.IsHpSafe()
		local var_34_13 = findTF(var_34_3, "blood")
		local var_34_14 = findTF(var_34_13, "fillarea/green")
		local var_34_15 = findTF(var_34_13, "fillarea/red")

		setActive(var_34_14, var_34_12)
		setActive(var_34_15, not var_34_12)

		var_34_13.GetComponent(typeof(Slider)).fillRect = var_34_12 and var_34_14 or var_34_15

		setSlider(var_34_13, 0, 10000, var_34_1.hpRant)
		setActive(var_34_13.Find("broken"), var_34_1.IsBroken())

		local var_34_16 = getProxy(ActivityProxy).getBuffShipList()[arg_34_1.getGroupId()]
		local var_34_17 = var_34_3.Find("expbuff")

		setActive(var_34_17, var_34_16 != None)

		if var_34_16:
			local var_34_18 = var_34_16 / 100
			local var_34_19 = var_34_16 % 100
			local var_34_20 = tostring(var_34_18)

			if var_34_19 > 0:
				var_34_20 = var_34_20 .. "." .. tostring(var_34_19)

			setText(var_34_17.Find("text"), string.format("EXP +%s%%", var_34_20))

	local var_33_1 = {}

	local function var_33_2(arg_35_0)
		local var_35_0 = arg_33_0.getCurrentFleet().GetTeamShipVOs(arg_35_0, False)

		for iter_35_0, iter_35_1 in ipairs(var_35_0):
			table.insert(var_33_1, function(arg_36_0)
				local var_36_0 = SpineRole.New(iter_35_1)

				var_36_0.Load(function()
					var_33_0(var_36_0, iter_35_1, arg_35_0, iter_35_0)
					onNextTick(arg_36_0)))

	var_33_2(TeamType.Vanguard)
	var_33_2(TeamType.Main)
	seriesAsync(var_33_1, function(arg_38_0)
		if arg_33_0.exited:
			return

		if arg_33_1:
			arg_33_1())

def var_0_0.showEnergyDesc(arg_39_0, arg_39_1, arg_39_2):
	if LeanTween.isTweening(go(arg_39_0.energyDescTF)):
		LeanTween.cancel(go(arg_39_0.energyDescTF))

		arg_39_0.energyDescTF.localScale = Vector3.one

	setText(arg_39_0.energyDescTextTF, arg_39_2)

	arg_39_0.energyDescTF.position = arg_39_1

	setActive(arg_39_0.energyDescTF, True)
	LeanTween.scale(arg_39_0.energyDescTF, Vector3.zero, 0.2).setDelay(1).setFrom(Vector3.one).setOnComplete(System.Action(function()
		arg_39_0.energyDescTF.localScale = Vector3.one

		setActive(arg_39_0.energyDescTF, False)))

def var_0_0.setAllCharacterPos(arg_41_0, arg_41_1):
	for iter_41_0, iter_41_1 in ipairs(arg_41_0.characterList[TeamType.Vanguard]):
		arg_41_0.setCharacterPos(TeamType.Vanguard, iter_41_0, tf(iter_41_1.model), arg_41_1)

	for iter_41_2, iter_41_3 in ipairs(arg_41_0.characterList[TeamType.Main]):
		arg_41_0.setCharacterPos(TeamType.Main, iter_41_2, tf(iter_41_3.model), arg_41_1)

	arg_41_0.sortSiblingIndex()

def var_0_0.setCharacterPos(arg_42_0, arg_42_1, arg_42_2, arg_42_3, arg_42_4):
	SetActive(arg_42_3, True)

	local var_42_0 = arg_42_0.gridTFs[arg_42_1][arg_42_2]
	local var_42_1 = var_42_0.localPosition

	LeanTween.cancel(go(arg_42_3))

	if arg_42_4:
		tf(arg_42_3).localPosition = Vector3(var_42_1.x + 2, var_42_1.y - 80, var_42_1.z)

		LeanTween.moveLocalY(go(arg_42_3), var_42_1.y - 110, 0.5).setDelay(0.5)
	else
		tf(arg_42_3).localPosition = Vector3(var_42_1.x + 2, var_42_1.y - 110, var_42_1.z)

	SetActive(var_42_0.Find("shadow"), True)
	arg_42_3.GetComponent("SpineAnimUI").SetAction("stand", 0)

def var_0_0.resetGrid(arg_43_0, arg_43_1):
	local var_43_0 = arg_43_0.gridTFs[arg_43_1]

	for iter_43_0, iter_43_1 in ipairs(var_43_0):
		SetActive(iter_43_1.Find("shadow"), False)

def var_0_0.switchToEditMode(arg_44_0):
	local function var_44_0(arg_45_0)
		for iter_45_0, iter_45_1 in ipairs(arg_45_0):
			local var_45_0 = iter_45_1.model
			local var_45_1 = tf(var_45_0).Find("mouseChild")

			if var_45_1:
				local var_45_2 = var_45_1.GetComponent("EventTriggerListener")

				arg_44_0.eventTriggers[var_45_2] = True

				if var_45_2:
					var_45_2.RemovePointEnterFunc()

				if iter_45_0 == arg_44_0._shiftIndex:
					var_45_1.GetComponent(typeof(Image)).enabled = True

	var_44_0(arg_44_0.characterList[TeamType.Vanguard])
	var_44_0(arg_44_0.characterList[TeamType.Main])

	arg_44_0._shiftIndex = None

	arg_44_0.flushCharacters()

def var_0_0.switchToShiftMode(arg_46_0, arg_46_1, arg_46_2):
	for iter_46_0 = 1, 3:
		local var_46_0 = arg_46_0.gridTFs[TeamType.Vanguard][iter_46_0]
		local var_46_1 = arg_46_0.gridTFs[TeamType.Main][iter_46_0]

		setActive(var_46_0.Find("tip"), False)
		setActive(var_46_1.Find("tip"), False)
		setActive(arg_46_0.gridTFs[arg_46_2][iter_46_0].Find("shadow"), False)

	local var_46_2 = arg_46_0.characterList[arg_46_2]

	for iter_46_1, iter_46_2 in ipairs(var_46_2):
		local var_46_3 = iter_46_2.model

		if var_46_3 != arg_46_1:
			local var_46_4 = arg_46_0.gridTFs[arg_46_2][iter_46_1]

			LeanTween.moveLocalY(var_46_3, var_46_4.localPosition.y - 80, 0.5)

			local var_46_5 = tf(var_46_3).Find("mouseChild").GetComponent("EventTriggerListener")

			arg_46_0.eventTriggers[var_46_5] = True

			var_46_5.AddPointEnterFunc(function()
				for iter_47_0, iter_47_1 in ipairs(var_46_2):
					if iter_47_1.model == var_46_3:
						arg_46_0.shift(arg_46_0._shiftIndex, iter_47_0, arg_46_2)

						break)
		else
			arg_46_0._shiftIndex = iter_46_1
			tf(var_46_3).Find("mouseChild").GetComponent(typeof(Image)).enabled = False

		var_46_3.GetComponent("SpineAnimUI").SetAction("normal", 0)

def var_0_0.shift(arg_48_0, arg_48_1, arg_48_2, arg_48_3):
	local var_48_0 = arg_48_0.characterList[arg_48_3]
	local var_48_1 = arg_48_0.gridTFs[arg_48_3]
	local var_48_2 = var_48_0[arg_48_2].model
	local var_48_3 = var_48_1[arg_48_1].localPosition

	tf(var_48_2).localPosition = Vector3(var_48_3.x + 2, var_48_3.y - 80, var_48_3.z)

	LeanTween.cancel(var_48_2)

	var_48_0[arg_48_1], var_48_0[arg_48_2] = var_48_0[arg_48_2], var_48_0[arg_48_1]

	local var_48_4 = arg_48_0.getCurrentFleet()
	local var_48_5 = var_48_4.GetTeamShips(arg_48_3, False)

	var_48_4.SwitchShip(var_48_5[arg_48_1].id, var_48_5[arg_48_2].id)

	arg_48_0._shiftIndex = arg_48_2

	arg_48_0.sortSiblingIndex()

def var_0_0.sortSiblingIndex(arg_49_0):
	local var_49_0 = 3
	local var_49_1 = 0

	while var_49_0 > 0:
		local var_49_2 = arg_49_0.characterList[TeamType.Main][var_49_0]
		local var_49_3 = arg_49_0.characterList[TeamType.Vanguard][var_49_0]

		if var_49_2:
			local var_49_4 = var_49_2.model

			tf(var_49_4).SetSiblingIndex(var_49_1)

			var_49_1 = var_49_1 + 1

		if var_49_3:
			local var_49_5 = var_49_3.model

			tf(var_49_5).SetSiblingIndex(var_49_1)

			var_49_1 = var_49_1 + 1

		var_49_0 = var_49_0 - 1

def var_0_0.enabledTeamCharacter(arg_50_0, arg_50_1, arg_50_2):
	local var_50_0 = arg_50_0.characterList[arg_50_1]

	for iter_50_0, iter_50_1 in ipairs(var_50_0):
		arg_50_0.enabledCharacter(iter_50_1.model, arg_50_2, arg_50_1)

def var_0_0.enabledCharacter(arg_51_0, arg_51_1, arg_51_2, arg_51_3):
	if arg_51_2:
		local var_51_0, var_51_1, var_51_2 = tf(arg_51_1).Find("mouseChild")

		if var_51_0:
			SetActive(var_51_0, True)
		else
			local var_51_3 = GameObject("mouseChild")

			tf(var_51_3).SetParent(tf(arg_51_1))

			tf(var_51_3).localPosition = Vector3.zero

			local var_51_4 = GetOrAddComponent(var_51_3, "ModelDrag")
			local var_51_5 = GetOrAddComponent(var_51_3, "EventTriggerListener")

			arg_51_0.eventTriggers[var_51_5] = True

			var_51_4.Init()

			local var_51_6 = var_51_3.GetComponent(typeof(RectTransform))

			var_51_6.sizeDelta = Vector2(2.5, 2.5)
			var_51_6.pivot = Vector2(0.5, 0)
			var_51_6.anchoredPosition = Vector2(0, 0)

			local var_51_7
			local var_51_8
			local var_51_9
			local var_51_10

			var_51_5.AddBeginDragFunc(function()
				var_51_7 = UnityEngine.Screen.width
				var_51_8 = UnityEngine.Screen.height
				var_51_9 = rtf(arg_51_0._tf).rect.width / var_51_7
				var_51_10 = rtf(arg_51_0._tf).rect.height / var_51_8

				LeanTween.cancel(go(arg_51_1))
				arg_51_0.switchToShiftMode(arg_51_1, arg_51_3)
				arg_51_1.GetComponent("SpineAnimUI").SetAction("tuozhuai", 0)
				tf(arg_51_1).SetParent(arg_51_0.moveLayer, False)
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_HOME_DRAG))
			var_51_5.AddDragFunc(function(arg_53_0, arg_53_1)
				rtf(arg_51_1).anchoredPosition = Vector2((arg_53_1.position.x - var_51_7 / 2) * var_51_9 + 20, (arg_53_1.position.y - var_51_8 / 2) * var_51_10 - 20))
			var_51_5.AddDragEndFunc(function(arg_54_0, arg_54_1)
				arg_51_1.GetComponent("SpineAnimUI").SetAction("tuozhuai", 0)
				tf(arg_51_1).SetParent(arg_51_0.heroContainer, False)
				arg_51_0.switchToEditMode()
				arg_51_0.sortSiblingIndex()
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_HOME_PUT))
	else
		SetActive(tf(arg_51_1).Find("mouseChild"), False)

def var_0_0.displayFleetInfo(arg_55_0):
	local var_55_0 = arg_55_0.getCurrentFleet()
	local var_55_1 = _.reduce(var_55_0.GetTeamShipVOs(TeamType.Vanguard, False), 0, function(arg_56_0, arg_56_1)
		return arg_56_0 + arg_56_1.getShipCombatPower())
	local var_55_2 = _.reduce(var_55_0.GetTeamShipVOs(TeamType.Main, False), 0, function(arg_57_0, arg_57_1)
		return arg_57_0 + arg_57_1.getShipCombatPower())

	var_0_1.tweenNumText(arg_55_0.vanguardGS, var_55_1)
	var_0_1.tweenNumText(arg_55_0.mainGS, var_55_2)

def var_0_0.hideStrategyInfo(arg_58_0):
	if arg_58_0.strategyPanel:
		arg_58_0.strategyPanel.detach()

def var_0_0.recycleCharacterList(arg_59_0, arg_59_1, arg_59_2):
	for iter_59_0, iter_59_1 in ipairs(arg_59_1):
		if arg_59_2[iter_59_0]:
			arg_59_2[iter_59_0].Dispose()

			arg_59_2[iter_59_0] = None

def var_0_0.willExit(arg_60_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_60_0._tf)

	if arg_60_0.resPanel:
		arg_60_0.resPanel.exit()

		arg_60_0.resPanel = None

	if arg_60_0.eventTriggers:
		for iter_60_0, iter_60_1 in pairs(arg_60_0.eventTriggers):
			ClearEventTrigger(iter_60_0)

		arg_60_0.eventTriggers = None

	if arg_60_0.tweens:
		cancelTweens(arg_60_0.tweens)

	local var_60_0 = arg_60_0.getCurrentFleet()

	arg_60_0.recycleCharacterList(var_60_0.GetTeamShipVOs(TeamType.Main, False), arg_60_0.characterList[TeamType.Main])
	arg_60_0.recycleCharacterList(var_60_0.GetTeamShipVOs(TeamType.Vanguard, False), arg_60_0.characterList[TeamType.Vanguard])

def var_0_0.Clone2Full(arg_61_0, arg_61_1):
	local var_61_0 = {}
	local var_61_1 = arg_61_0.GetChild(0)
	local var_61_2 = arg_61_0.childCount

	for iter_61_0 = 0, var_61_2 - 1:
		table.insert(var_61_0, arg_61_0.GetChild(iter_61_0))

	for iter_61_1 = var_61_2, arg_61_1 - 1:
		local var_61_3 = cloneTplTo(var_61_1, arg_61_0)

		table.insert(var_61_0, tf(var_61_3))

	return var_61_0

def var_0_0.TransformColor(arg_62_0):
	local var_62_0 = tonumber(string.sub(arg_62_0, 1, 2), 16)
	local var_62_1 = tonumber(string.sub(arg_62_0, 3, 4), 16)
	local var_62_2 = tonumber(string.sub(arg_62_0, 5, 6), 16)

	return Color.New(var_62_0 / 255, var_62_1 / 255, var_62_2 / 255)

return var_0_0
