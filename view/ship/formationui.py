local var_0_0 = class("FormationUI", import("..base.BaseUI"))

var_0_0.RADIUS = 60
var_0_0.LONGPRESS_Y = 30
var_0_0.INTERVAL = math.pi / 2 / 6
var_0_0.MAX_FLEET_NUM = 6
var_0_0.MAX_SHIPP_NUM = 5
var_0_0.TOGGLE_DETAIL = "_detailToggle"
var_0_0.TOGGLE_FORMATION = "_formationToggle"
var_0_0.BUFF_TYEP = {
	blue = "blue",
	pink = "pink",
	cyan = "cyan"
}
var_0_0.TeamNum = {
	"FIRST",
	"SECOND",
	"THIRD",
	"FOURTH",
	"FIFTH",
	"SIXTH"
}

def var_0_0.getUIName(arg_1_0):
	return "FormationUI"

def var_0_0.setPlayer(arg_2_0, arg_2_1):
	arg_2_0.player = arg_2_1

def var_0_0.setCommanderPrefabFleet(arg_3_0, arg_3_1):
	arg_3_0.commanderPrefabFleets = arg_3_1

def var_0_0.init(arg_4_0):
	arg_4_0.eventTriggers = {}
	arg_4_0._blurLayer = arg_4_0.findTF("blur_panel")
	arg_4_0.backBtn = arg_4_0.findTF("top/back_btn", arg_4_0._blurLayer)
	arg_4_0._bgFleet = arg_4_0.findTF("bg_fleet")
	arg_4_0._bgSub = arg_4_0.findTF("bg_sub")
	arg_4_0._bottomPanel = arg_4_0.findTF("bottom", arg_4_0._blurLayer)
	arg_4_0._detailToggle = arg_4_0.findTF("toggle_list/detail_toggle", arg_4_0._bottomPanel)
	arg_4_0._formationToggle = arg_4_0.findTF("toggle_list/formation_toggle", arg_4_0._bottomPanel)
	arg_4_0._nextPage = arg_4_0.findTF("nextPage")
	arg_4_0._prevPage = arg_4_0.findTF("prevPage")
	arg_4_0._starTpl = arg_4_0.findTF("star_tpl")
	arg_4_0._heroInfoTpl = arg_4_0.findTF("heroInfo")
	arg_4_0.topPanel = arg_4_0.findTF("top", arg_4_0._blurLayer)
	arg_4_0._gridTFs = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {},
		[TeamType.Submarine] = {}
	}
	arg_4_0._gridFrame = arg_4_0.findTF("GridFrame")

	for iter_4_0 = 1, 3:
		arg_4_0._gridTFs[TeamType.Main][iter_4_0] = arg_4_0._gridFrame.Find("main_" .. iter_4_0)
		arg_4_0._gridTFs[TeamType.Vanguard][iter_4_0] = arg_4_0._gridFrame.Find("vanguard_" .. iter_4_0)
		arg_4_0._gridTFs[TeamType.Submarine][iter_4_0] = arg_4_0._gridFrame.Find("submarine_" .. iter_4_0)

	arg_4_0._heroContainer = arg_4_0.findTF("HeroContainer")
	arg_4_0._formationLogic = BaseFormation.New(arg_4_0._tf, arg_4_0._heroContainer, arg_4_0._heroInfoTpl, arg_4_0._gridTFs)
	arg_4_0._fleetInfo = arg_4_0.findTF("fleet_info", arg_4_0._blurLayer)
	arg_4_0._fleetNumText = arg_4_0.findTF("fleet_number", arg_4_0._fleetInfo)
	arg_4_0._fleetNameText = arg_4_0.findTF("fleet_name/Text", arg_4_0._fleetInfo)
	arg_4_0._fleetNameEditBtn = arg_4_0.findTF("edit_btn", arg_4_0._fleetInfo)
	arg_4_0._renamePanel = arg_4_0.findTF("changeName_panel")
	arg_4_0._renameConfirmBtn = arg_4_0._renamePanel.Find("frame/queren")
	arg_4_0._renameCancelBtn = arg_4_0._renamePanel.Find("frame/cancel")

	setLocalPosition(arg_4_0._renamePanel, {
		z = -45
	})

	arg_4_0._propertyFrame = arg_4_0.findTF("property_frame", arg_4_0._blurLayer)
	arg_4_0._cannonPower = arg_4_0.findTF("cannon/Text", arg_4_0._propertyFrame)
	arg_4_0._torpedoPower = arg_4_0.findTF("torpedo/Text", arg_4_0._propertyFrame)
	arg_4_0._AAPower = arg_4_0.findTF("antiaircraft/Text", arg_4_0._propertyFrame)
	arg_4_0._airPower = arg_4_0.findTF("air/Text", arg_4_0._propertyFrame)
	arg_4_0._airDominance = arg_4_0.findTF("ac/Text", arg_4_0._propertyFrame)
	arg_4_0._cost = arg_4_0.findTF("cost/Text", arg_4_0._propertyFrame)
	arg_4_0._mainGS = arg_4_0.findTF("gear_score/main")
	arg_4_0._vanguardGS = arg_4_0.findTF("gear_score/vanguard")
	arg_4_0._subGS = arg_4_0.findTF("gear_score/submarine")
	arg_4_0._arrUpVan = arg_4_0._vanguardGS.Find("up")
	arg_4_0._arrDownVan = arg_4_0._vanguardGS.Find("down")
	arg_4_0._arrUpMain = arg_4_0._mainGS.Find("up")
	arg_4_0._arrDownMain = arg_4_0._mainGS.Find("down")
	arg_4_0._arrUpSub = arg_4_0._subGS.Find("up")
	arg_4_0._arrDownSub = arg_4_0._subGS.Find("down")
	arg_4_0._attrFrame = arg_4_0.findTF("blur_panel/attr_frame")
	arg_4_0._cardTpl = arg_4_0._tf.GetComponent(typeof(ItemList)).prefabItem[0]
	arg_4_0._cards = {}
	arg_4_0._cards[TeamType.Main] = {}
	arg_4_0._cards[TeamType.Vanguard] = {}
	arg_4_0._cards[TeamType.Submarine] = {}

	setActive(arg_4_0._attrFrame, False)
	setActive(arg_4_0._cardTpl, False)

	arg_4_0.btnRegular = arg_4_0.findTF("fleet_select/regular", arg_4_0._bottomPanel)
	arg_4_0._regularEnFllet = arg_4_0.findTF("fleet/enFleet", arg_4_0.btnRegular)
	arg_4_0._regularNum = arg_4_0.findTF("fleet/num", arg_4_0.btnRegular)
	arg_4_0._regualrCnFleet = arg_4_0.findTF("fleet/CnFleet", arg_4_0.btnRegular)
	arg_4_0.btnSub = arg_4_0.findTF("fleet_select/sub", arg_4_0._bottomPanel)
	arg_4_0._subEnFllet = arg_4_0.findTF("fleet/enFleet", arg_4_0.btnSub)
	arg_4_0._subNum = arg_4_0.findTF("fleet/num", arg_4_0.btnSub)
	arg_4_0._subCnFleet = arg_4_0.findTF("fleet/CnFleet", arg_4_0.btnSub)
	arg_4_0.fleetToggleMask = arg_4_0.findTF("blur_panel/list_mask")
	arg_4_0.fleetToggleList = arg_4_0.findTF("list", arg_4_0.fleetToggleMask)
	arg_4_0.fleetToggles = {}

	for iter_4_1 = 1, var_0_0.MAX_FLEET_NUM:
		arg_4_0.fleetToggles[iter_4_1] = arg_4_0.findTF("item" .. iter_4_1, arg_4_0.fleetToggleList)

	arg_4_0._vanGSTxt = arg_4_0._vanguardGS.Find("Text").GetComponent("Text")
	arg_4_0._mainGSTxt = arg_4_0._mainGS.Find("Text").GetComponent("Text")
	arg_4_0._subGSTxt = arg_4_0._subGS.Find("Text").GetComponent("Text")
	arg_4_0.prevMainGS = arg_4_0.contextData.mainGS
	arg_4_0.prevVanGS = arg_4_0.contextData.vanGS
	arg_4_0.prevSubGS = arg_4_0.contextData.subGS
	arg_4_0.mainGSInited = arg_4_0.contextData.mainGS and True or False
	arg_4_0.VanGSInited = arg_4_0.contextData.vanGS and True or False
	arg_4_0.SubGSInited = arg_4_0.contextData.subGS and True or False
	arg_4_0._vanGSTxt.text = arg_4_0.prevVanGS or 0
	arg_4_0._mainGSTxt.text = arg_4_0.prevMainGS or 0
	arg_4_0._subGSTxt.text = arg_4_0.prevSubGS or 0
	arg_4_0.commanderFormationPanel = CommanderFormationPage.New(arg_4_0._tf, arg_4_0.event, arg_4_0.contextData)
	arg_4_0.index = {
		[FleetType.Normal] = 1,
		[FleetType.Submarine] = 1
	}

	setText(findTF(arg_4_0._tf, "gear_score/main/line/Image/text1"), i18n("pre_combat_main"))
	setText(findTF(arg_4_0._tf, "gear_score/vanguard/line/Image/text1"), i18n("pre_combat_vanguard"))
	setText(findTF(arg_4_0._tf, "gear_score/submarine/line/Image/text1"), i18n("pre_combat_submarine"))

def var_0_0.setShips(arg_5_0, arg_5_1):
	arg_5_0.shipVOs = arg_5_1

	arg_5_0._formationLogic.SetShipVOs(arg_5_0.shipVOs)

def var_0_0.SetFleets(arg_6_0, arg_6_1):
	arg_6_0._fleetVOs = _(arg_6_1).chain().values().filter(function(arg_7_0)
		return arg_7_0.isRegularFleet()).sort(function(arg_8_0, arg_8_1)
		return arg_8_0.id < arg_8_1.id).value()

	if arg_6_0._currentFleetVO:
		arg_6_0._currentFleetVO = arg_6_0.getFleetById(arg_6_0._currentFleetVO.id)

		arg_6_0._formationLogic.SetFleetVO(arg_6_0._currentFleetVO)

def var_0_0.getFleetById(arg_9_0, arg_9_1):
	return _.detect(arg_9_0._fleetVOs, function(arg_10_0)
		return arg_10_0.id == arg_9_1)

def var_0_0.UpdateFleetView(arg_11_0, arg_11_1):
	arg_11_0.displayFleetInfo()
	arg_11_0.updateFleetBg()
	arg_11_0._formationLogic.UpdateGridVisibility()
	arg_11_0._formationLogic.ResetGrid(TeamType.Vanguard)
	arg_11_0._formationLogic.ResetGrid(TeamType.Main)
	arg_11_0._formationLogic.ResetGrid(TeamType.Submarine)
	arg_11_0.resetFormationComponent()
	arg_11_0.updateAttrFrame()
	arg_11_0.updateFleetButton()

	if arg_11_1:
		arg_11_0._formationLogic.LoadAllCharacter()
	else
		arg_11_0._formationLogic.SetAllCharacterPos()

def var_0_0.updateFleetBg(arg_12_0):
	local var_12_0 = arg_12_0._currentFleetVO.getFleetType()

	setActive(arg_12_0._bgFleet, var_12_0 == FleetType.Normal)
	setActive(arg_12_0._bgSub, var_12_0 == FleetType.Submarine)

def var_0_0.updateFleetButton(arg_13_0):
	local var_13_0
	local var_13_1 = arg_13_0._currentFleetVO.getFleetType()

	arg_13_0.index[var_13_1] = arg_13_0._currentFleetVO.getIndex()

	local var_13_2 = arg_13_0.index[FleetType.Normal]

	setText(arg_13_0._regularEnFllet, var_0_0.TeamNum[var_13_2] .. " FLEET")
	setText(arg_13_0._regualrCnFleet, Fleet.DEFAULT_NAME[var_13_2])
	setText(arg_13_0._regularNum, var_13_2)

	local var_13_3 = arg_13_0.index[FleetType.Submarine]

	setText(arg_13_0._subEnFllet, var_0_0.TeamNum[var_13_3] .. " FLEET")
	setText(arg_13_0._subCnFleet, Fleet.DEFAULT_NAME[var_13_3])
	setText(arg_13_0._subNum, var_13_3)
	setActive(arg_13_0.btnRegular.Find("on"), var_13_1 == FleetType.Normal)
	setActive(arg_13_0.btnRegular.Find("off"), var_13_1 != FleetType.Normal)
	setActive(arg_13_0.btnSub.Find("on"), var_13_1 == FleetType.Submarine)
	setActive(arg_13_0.btnSub.Find("off"), var_13_1 != FleetType.Submarine)

def var_0_0.SetFleetNameLabel(arg_14_0):
	setText(arg_14_0._fleetNameText, arg_14_0.defaultFleetName(arg_14_0._currentFleetVO))

def var_0_0.ForceDropChar(arg_15_0):
	arg_15_0._formationLogic.ForceDropChar()

	if arg_15_0._currentDragDelegate:
		arg_15_0._forceDropCharacter = True

		LuaHelper.triggerEndDrag(arg_15_0._currentDragDelegate)

def var_0_0.quickExitFunc(arg_16_0):
	arg_16_0.ForceDropChar()

	local function var_16_0()
		GetOrAddComponent(arg_16_0._tf, typeof(CanvasGroup)).interactable = False

		arg_16_0.emit(var_0_0.ON_HOME)

	arg_16_0.emit(FormationMediator.COMMIT_FLEET, var_16_0)

def var_0_0.didEnter(arg_18_0):
	arg_18_0.isOpenCommander = pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_18_0.player.level, "CommanderCatMediator") and not LOCK_COMMANDER

	local var_18_0 = getProxy(ActivityProxy).getBuffShipList()

	arg_18_0._formationLogic.AddHeroInfoModify(function(arg_19_0, arg_19_1)
		local var_19_0 = arg_19_1.getConfigTable()
		local var_19_1 = pg.ship_data_template[arg_19_1.configId]
		local var_19_2 = findTF(arg_19_0, "info")
		local var_19_3 = findTF(var_19_2, "stars")
		local var_19_4 = findTF(var_19_2, "energy")
		local var_19_5 = arg_19_1.getStar()

		for iter_19_0 = 1, var_19_5:
			cloneTplTo(arg_18_0._starTpl, var_19_3)

		local var_19_6 = GetSpriteFromAtlas("shiptype", shipType2print(arg_19_1.getShipType()))

		if not var_19_6:
			warning("找不到船形, shipConfigId. " .. arg_19_1.configId)

		setImageSprite(findTF(var_19_2, "type"), var_19_6, True)
		setText(findTF(var_19_2, "frame/lv_contain/lv"), arg_19_1.level)

		if arg_19_1.energy <= Ship.ENERGY_MID:
			local var_19_7 = GetSpriteFromAtlas("energy", arg_19_1.getEnergyPrint())

			setImageSprite(var_19_4, var_19_7)
			setActive(var_19_4, True)

		local var_19_8 = var_18_0[arg_19_1.getGroupId()]
		local var_19_9 = var_19_2.Find("expbuff")

		setActive(var_19_9, var_19_8 != None)

		if var_19_8:
			local var_19_10 = var_19_8 / 100
			local var_19_11 = var_19_8 % 100
			local var_19_12 = tostring(var_19_10)

			if var_19_11 > 0:
				var_19_12 = var_19_12 .. "." .. tostring(var_19_11)

			setText(var_19_9.Find("text"), string.format("EXP +%s%%", var_19_12)))
	arg_18_0._formationLogic.AddLongPress(function(arg_20_0, arg_20_1, arg_20_2)
		arg_18_0.emit(FormationMediator.OPEN_SHIP_INFO, arg_20_1.id, arg_18_0._currentFleetVO, var_0_0.TOGGLE_FORMATION)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))
	arg_18_0._formationLogic.AddClick(function(arg_21_0, arg_21_1)
		arg_18_0.emit(FormationMediator.CHANGE_FLEET_SHIP, arg_21_0, arg_18_0._currentFleetVO, var_0_0.TOGGLE_FORMATION, arg_21_1)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))
	arg_18_0._formationLogic.AddBeginDrag(function(arg_22_0)
		local var_22_0 = findTF(arg_22_0, "info")

		SetActive(var_22_0, False))
	arg_18_0._formationLogic.AddEndDrag(function(arg_23_0)
		local var_23_0 = findTF(arg_23_0, "info")

		SetActive(var_23_0, True))
	arg_18_0._formationLogic.AddShiftOnly(function(arg_24_0)
		arg_18_0.emit(FormationMediator.CHANGE_FLEET_SHIPS_ORDER, arg_24_0))
	arg_18_0._formationLogic.AddRemoveShip(function(arg_25_0, arg_25_1)
		arg_18_0.emit(FormationMediator.REMOVE_SHIP, arg_25_0, arg_25_1))
	arg_18_0._formationLogic.AddCheckRemove(function(arg_26_0, arg_26_1, arg_26_2, arg_26_3, arg_26_4)
		if not arg_26_3.canRemove(arg_26_2):
			local var_26_0, var_26_1 = arg_26_3.getShipPos(arg_26_2)

			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_formationUI_removeError_onlyShip", arg_26_2.getConfigTable().name, arg_26_3.name, Fleet.C_TEAM_NAME[var_26_1]))
			arg_26_0()
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				zIndex = -30,
				hideNo = False,
				content = i18n("ship_formationUI_quest_remove", arg_26_2.getName()),
				onYes = arg_26_1,
				onNo = arg_26_0
			}))
	arg_18_0._formationLogic.AddGridTipClick(function(arg_27_0, arg_27_1)
		arg_18_0.emit(FormationMediator.CHANGE_FLEET_SHIP, None, arg_27_1, var_0_0.TOGGLE_FORMATION, arg_27_0))
	onButton(arg_18_0, arg_18_0.backBtn, function()
		arg_18_0.ForceDropChar()

		if arg_18_0._attrFrame.gameObject.activeSelf:
			triggerToggle(arg_18_0._formationToggle, True)
		else
			local function var_28_0()
				GetOrAddComponent(arg_18_0._tf, typeof(CanvasGroup)).interactable = False

				arg_18_0.emit(var_0_0.ON_BACK)

			arg_18_0.emit(FormationMediator.COMMIT_FLEET, var_28_0), SOUND_BACK)
	setActive(arg_18_0.findTF("stamp"), BATTLE_DEBUG or getProxy(TaskProxy).mingshiTouchFlagEnabled())

	if LOCK_CLICK_MINGSHI:
		setActive(arg_18_0.findTF("stamp"), False)

	onButton(arg_18_0, arg_18_0.findTF("stamp"), function()
		if BATTLE_DEBUG:
			print(arg_18_0._currentFleetVO.genRobotDataString())

		getProxy(TaskProxy).dealMingshiTouchFlag(6), SFX_CONFIRM)
	onButton(arg_18_0, arg_18_0._fleetNameEditBtn, function()
		arg_18_0.DisplayRenamePanel(True), SFX_PANEL)
	onButton(arg_18_0, arg_18_0._renameConfirmBtn, function()
		local var_32_0 = getInputText(findTF(arg_18_0._renamePanel, "frame/name_field"))

		arg_18_0.emit(FormationMediator.CHANGE_FLEET_NAME, arg_18_0._currentFleetVO.id, var_32_0), SFX_CONFIRM)
	onButton(arg_18_0, arg_18_0._renameCancelBtn, function()
		arg_18_0.DisplayRenamePanel(False), SFX_CANCEL)
	onToggle(arg_18_0, arg_18_0._detailToggle, function(arg_34_0)
		arg_18_0.ForceDropChar()

		if arg_34_0:
			arg_18_0.displayAttrFrame(), SFX_PANEL)
	onToggle(arg_18_0, arg_18_0._formationToggle, function(arg_35_0)
		arg_18_0.ForceDropChar()

		if arg_35_0:
			arg_18_0.hideAttrFrame(), SFX_PANEL)
	onButton(arg_18_0, arg_18_0._attrFrame, function()
		triggerToggle(arg_18_0._formationToggle, True), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.fleetToggleMask, function()
		setActive(arg_18_0.fleetToggleMask, False)
		arg_18_0.tweenTabArrow(True), SFX_CANCEL)
	onButton(arg_18_0, arg_18_0.btnRegular, function()
		arg_18_0.updateToggleList(_.filter(arg_18_0._fleetVOs, function(arg_39_0)
			return arg_39_0.getFleetType() == FleetType.Normal))

		local var_38_0 = arg_18_0._currentFleetVO.getFleetType() == FleetType.Normal
		local var_38_1 = arg_18_0.index[FleetType.Normal]

		triggerToggle(arg_18_0.fleetToggles[var_38_1], True)

		if var_38_0:
			setActive(arg_18_0.fleetToggleMask, True)
			arg_18_0.tweenTabArrow(False)
			setAnchoredPosition(arg_18_0.fleetToggleList, Vector3.New(209, 129)), SFX_PANEL)
	onButton(arg_18_0, arg_18_0.btnSub, function()
		arg_18_0.updateToggleList(_.filter(arg_18_0._fleetVOs, function(arg_41_0)
			return arg_41_0.getFleetType() == FleetType.Submarine))

		local var_40_0 = arg_18_0._currentFleetVO.getFleetType() == FleetType.Submarine
		local var_40_1 = arg_18_0.index[FleetType.Submarine]

		triggerToggle(arg_18_0.fleetToggles[var_40_1], True)

		if var_40_0:
			setActive(arg_18_0.fleetToggleMask, True)
			arg_18_0.tweenTabArrow(False)
			setAnchoredPosition(arg_18_0.fleetToggleList, Vector3.New(755, 129)), SFX_PANEL)
	onButton(arg_18_0, arg_18_0._prevPage, function()
		local var_42_0 = arg_18_0.selectFleetByStep(-1)

		arg_18_0.ForceDropChar()
		arg_18_0.emit(FormationMediator.ON_CHANGE_FLEET, var_42_0), SFX_PANEL)
	onButton(arg_18_0, arg_18_0._nextPage, function()
		local var_43_0 = arg_18_0.selectFleetByStep(1)

		arg_18_0.ForceDropChar()
		arg_18_0.emit(FormationMediator.ON_CHANGE_FLEET, var_43_0), SFX_PANEL)

	local var_18_1 = defaultValue(arg_18_0.contextData.number, 1)

	arg_18_0.SetCurrentFleetID(var_18_1)

	if arg_18_0.isOpenCommander:
		arg_18_0.commanderFormationPanel.ActionInvoke("Show")

	arg_18_0.UpdateFleetView(True)
	triggerToggle(arg_18_0[arg_18_0.contextData.toggle or var_0_0.TOGGLE_FORMATION], True)
	arg_18_0.tweenTabArrow(True)
	onButton(arg_18_0, arg_18_0._vanguardGS.Find("SonarTip"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.fleet_antisub_range_tip.tip
		}), SFX_PANEL)

def var_0_0.SetCurrentFleetID(arg_45_0, arg_45_1):
	arg_45_0._currentFleetVO = arg_45_0.getFleetById(arg_45_1)

	arg_45_0._formationLogic.SetFleetVO(arg_45_0._currentFleetVO)
	arg_45_0.updateCommanderFormation()

def var_0_0.updateCommanderFormation(arg_46_0):
	if arg_46_0.isOpenCommander:
		arg_46_0.commanderFormationPanel.Load()
		arg_46_0.commanderFormationPanel.ActionInvoke("Update", arg_46_0._currentFleetVO, arg_46_0.commanderPrefabFleets)

def var_0_0.selectFleetByStep(arg_47_0, arg_47_1):
	local var_47_0 = table.indexof(arg_47_0._fleetVOs, arg_47_0._currentFleetVO)

	while True:
		var_47_0 = var_47_0 + arg_47_1

		if var_47_0 < 1 or var_47_0 > #arg_47_0._fleetVOs:
			break

		local var_47_1 = arg_47_0._fleetVOs[var_47_0]

		if var_47_1.isUnlock():
			return var_47_1.id

def var_0_0.updateToggleList(arg_48_0, arg_48_1):
	local var_48_0 = arg_48_0.fleetToggleList.GetComponent(typeof(ToggleGroup))

	var_48_0.allowSwitchOff = True

	local var_48_1 = arg_48_0._currentFleetVO.id

	for iter_48_0 = 1, #arg_48_0.fleetToggles:
		local var_48_2 = arg_48_0.fleetToggles[iter_48_0]
		local var_48_3 = arg_48_1[iter_48_0]

		setActive(var_48_2, var_48_3)

		if var_48_3:
			local var_48_4 = var_48_2.GetComponent(typeof(Toggle))
			local var_48_5 = var_48_2.Find("lock")
			local var_48_6, var_48_7 = var_48_3.isUnlock()

			setToggleEnabled(var_48_2, var_48_6)
			setActive(var_48_5, not var_48_6)
			setActive(var_48_2.Find("on"), var_48_6 and var_48_1 == var_48_3.id)
			setActive(var_48_2.Find("off"), var_48_6 and var_48_1 != var_48_3.id)

			if var_48_6:
				var_48_4.isOn = var_48_3.id == var_48_1

				onToggle(arg_48_0, var_48_2, function(arg_49_0)
					if arg_49_0:
						setActive(arg_48_0.fleetToggleMask, False)
						arg_48_0.tweenTabArrow(True)

						if var_48_3.id != var_48_1:
							arg_48_0.ForceDropChar()
							arg_48_0.emit(FormationMediator.ON_CHANGE_FLEET, var_48_3.id), SFX_UI_TAG)
			else
				onButton(arg_48_0, var_48_5, function()
					pg.TipsMgr.GetInstance().ShowTips(var_48_7), SFX_UI_CLICK)

	var_48_0.allowSwitchOff = False

def var_0_0.resetFormationComponent(arg_51_0):
	SetActive(arg_51_0._gridTFs.main[1].Find("flag"), #arg_51_0._currentFleetVO.getTeamByName(TeamType.Main) != 0)
	SetActive(arg_51_0._gridTFs.submarine[1].Find("flag"), #arg_51_0._currentFleetVO.getTeamByName(TeamType.Submarine) != 0)

def var_0_0.sortCardSiblingIndex(arg_52_0):
	local var_52_0 = {
		TeamType.Main,
		TeamType.Vanguard,
		TeamType.Submarine
	}

	_.each(var_52_0, function(arg_53_0)
		local var_53_0 = arg_52_0._cards[arg_53_0]

		if #var_53_0 > 0:
			for iter_53_0 = 1, #var_53_0:
				var_53_0[iter_53_0].tr.SetSiblingIndex(iter_53_0 - 1))

def var_0_0.displayFleetInfo(arg_54_0):
	SetActive(arg_54_0._prevPage, arg_54_0.selectFleetByStep(-1))
	SetActive(arg_54_0._nextPage, arg_54_0.selectFleetByStep(1))
	setActive(arg_54_0.findTF("gear_score"), True)
	setActive(arg_54_0._vanguardGS, False)
	setActive(arg_54_0._mainGS, False)
	setActive(arg_54_0._subGS, False)

	local var_54_0 = arg_54_0._currentFleetVO.GetPropertiesSum()
	local var_54_1 = math.floor(arg_54_0._currentFleetVO.GetGearScoreSum(TeamType.Vanguard))
	local var_54_2 = math.floor(arg_54_0._currentFleetVO.GetGearScoreSum(TeamType.Main))
	local var_54_3 = math.floor(arg_54_0._currentFleetVO.GetGearScoreSum(TeamType.Submarine))
	local var_54_4 = arg_54_0._currentFleetVO.GetCostSum()

	arg_54_0.tweenNumText(arg_54_0._cannonPower, var_54_0.cannon)
	arg_54_0.tweenNumText(arg_54_0._torpedoPower, var_54_0.torpedo)
	arg_54_0.tweenNumText(arg_54_0._AAPower, var_54_0.antiAir)
	arg_54_0.tweenNumText(arg_54_0._airPower, var_54_0.air)
	arg_54_0.tweenNumText(arg_54_0._cost, var_54_4.oil)

	if OPEN_AIR_DOMINANCE:
		setActive(arg_54_0._airDominance.parent, True)
		arg_54_0.tweenNumText(arg_54_0._airDominance, arg_54_0._currentFleetVO.getFleetAirDominanceValue())
	else
		setActive(arg_54_0._airDominance.parent, False)

	local var_54_5 = arg_54_0._currentFleetVO.getFleetType()

	if var_54_5 == FleetType.Normal:
		setActive(arg_54_0._vanguardGS, True)
		setActive(arg_54_0._mainGS, True)
		setActive(arg_54_0._arrUpVan, False)
		setActive(arg_54_0._arrDownVan, False)
		setActive(arg_54_0._arrUpMain, False)
		setActive(arg_54_0._arrDownMain, False)

		arg_54_0.prevVanGS = tonumber(arg_54_0._vanGSTxt.text)

		arg_54_0.tweenNumText(arg_54_0._vanguardGS.Find("Text"), var_54_1)

		if arg_54_0.VanGSInited:
			setActive(arg_54_0._arrUpVan, var_54_1 > arg_54_0.prevVanGS)
			setActive(arg_54_0._arrDownVan, var_54_1 < arg_54_0.prevVanGS)

		arg_54_0.prevMainGS = tonumber(arg_54_0._mainGSTxt.text)

		arg_54_0.tweenNumText(arg_54_0._mainGS.Find("Text"), var_54_2)

		if arg_54_0.mainGSInited:
			setActive(arg_54_0._arrUpMain, var_54_2 > arg_54_0.prevMainGS)
			setActive(arg_54_0._arrDownMain, var_54_2 < arg_54_0.prevMainGS)

		arg_54_0.contextData.mainGS = var_54_2
		arg_54_0.contextData.vanGS = var_54_1
		arg_54_0.mainGSInited = True
		arg_54_0.VanGSInited = True

		local var_54_6 = arg_54_0._currentFleetVO.GetFleetSonarRange()

		setActive(arg_54_0._vanguardGS.Find("SonarActive"), var_54_6 > 0)
		setActive(arg_54_0._vanguardGS.Find("SonarInactive"), var_54_6 <= 0)

		local function var_54_7()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = pg.gametip.fleet_antisub_range_tip.tip
			})

		if var_54_6 > 0:
			setText(arg_54_0._vanguardGS.Find("SonarActive/Text"), math.floor(var_54_6))
			onButton(arg_54_0, arg_54_0._vanguardGS.Find("SonarActive"), var_54_7, SFX_PANEL)
		else
			onButton(arg_54_0, arg_54_0._vanguardGS.Find("SonarInactive"), var_54_7, SFX_PANEL)
	elif var_54_5 == FleetType.Submarine:
		setActive(arg_54_0._arrUpSub, False)
		setActive(arg_54_0._arrDownSub, False)
		setActive(arg_54_0._subGS, True)

		arg_54_0.prevSubGS = tonumber(arg_54_0._subGSTxt.text)

		arg_54_0.tweenNumText(arg_54_0._subGS.Find("Text"), var_54_3)

		if arg_54_0.SubGSInited:
			setActive(arg_54_0._arrUpSub, var_54_3 > arg_54_0.prevSubGS)
			setActive(arg_54_0._arrDownSub, var_54_3 < arg_54_0.prevSubGS)

		arg_54_0.contextData.subGS = var_54_3
		arg_54_0.SubGSInited = True

	arg_54_0.SetFleetNameLabel()
	setText(arg_54_0._fleetNumText, arg_54_0._currentFleetVO.getIndex())

def var_0_0.DisplayRenamePanel(arg_56_0, arg_56_1):
	SetActive(arg_56_0._renamePanel, arg_56_1)

	if arg_56_1:
		pg.UIMgr.GetInstance().BlurPanel(arg_56_0._renamePanel, False)

		local var_56_0 = getText(arg_56_0._fleetNameText)

		setInputText(findTF(arg_56_0._renamePanel, "frame/name_field"), var_56_0)
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_56_0._renamePanel, arg_56_0._tf)

def var_0_0.hideAttrFrame(arg_57_0):
	SetActive(arg_57_0._attrFrame, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_57_0._blurLayer, arg_57_0._tf)

def var_0_0.displayAttrFrame(arg_58_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_58_0._blurLayer, False)
	SetActive(arg_58_0._attrFrame, True)
	arg_58_0.initAttrFrame()

def var_0_0.initAttrFrame(arg_59_0):
	local var_59_0 = {
		[TeamType.Main] = arg_59_0._currentFleetVO.mainShips,
		[TeamType.Vanguard] = arg_59_0._currentFleetVO.vanguardShips,
		[TeamType.Submarine] = arg_59_0._currentFleetVO.subShips
	}
	local var_59_1 = False

	for iter_59_0, iter_59_1 in pairs(var_59_0):
		local var_59_2 = arg_59_0._cards[iter_59_0]

		if #var_59_2 == 0:
			local var_59_3 = arg_59_0.findTF(iter_59_0 .. "/list", arg_59_0._attrFrame)

			for iter_59_2 = 1, 3:
				local var_59_4 = cloneTplTo(arg_59_0._cardTpl, var_59_3).gameObject

				table.insert(var_59_2, FormationDetailCard.New(var_59_4))

			var_59_1 = True

	if var_59_1:
		arg_59_0.updateAttrFrame()

def var_0_0.updateAttrFrame(arg_60_0):
	local var_60_0 = {
		[TeamType.Main] = arg_60_0._currentFleetVO.mainShips,
		[TeamType.Vanguard] = arg_60_0._currentFleetVO.vanguardShips,
		[TeamType.Submarine] = arg_60_0._currentFleetVO.subShips
	}
	local var_60_1 = arg_60_0._currentFleetVO.getFleetType()

	for iter_60_0, iter_60_1 in pairs(var_60_0):
		local var_60_2 = arg_60_0._cards[iter_60_0]

		if #var_60_2 > 0:
			local var_60_3 = var_60_1 == FleetType.Submarine and iter_60_0 == TeamType.Vanguard

			for iter_60_2 = 1, 3:
				if iter_60_2 <= #iter_60_1:
					local var_60_4 = arg_60_0.shipVOs[iter_60_1[iter_60_2]]

					var_60_2[iter_60_2].update(var_60_4, var_60_3)
					var_60_2[iter_60_2].updateProps(arg_60_0.getCardAttrProps(var_60_4))
				else
					var_60_2[iter_60_2].update(None, var_60_3)

				arg_60_0.detachOnCardButton(var_60_2[iter_60_2])

				if not var_60_3:
					arg_60_0.attachOnCardButton(var_60_2[iter_60_2], iter_60_0)

	setActive(arg_60_0.findTF(TeamType.Main, arg_60_0._attrFrame), var_60_1 == FleetType.Normal)
	setActive(arg_60_0.findTF(TeamType.Submarine, arg_60_0._attrFrame), var_60_1 == FleetType.Submarine)
	setActive(arg_60_0.findTF(TeamType.Vanguard .. "/vanguard", arg_60_0._attrFrame), var_60_1 != FleetType.Submarine)
	arg_60_0.updateUltimateTitle()

def var_0_0.updateUltimateTitle(arg_61_0):
	local var_61_0 = arg_61_0._cards[TeamType.Main]
	local var_61_1 = arg_61_0._currentFleetVO.mainShips

	if #var_61_0 > 0:
		for iter_61_0 = 1, #var_61_0:
			go(var_61_0[iter_61_0].shipState).SetActive(iter_61_0 == 1)

def var_0_0.getCardAttrProps(arg_62_0, arg_62_1):
	local var_62_0 = arg_62_1.getProperties()
	local var_62_1 = arg_62_1.getShipCombatPower()
	local var_62_2 = arg_62_1.getBattleTotalExpend()

	return {
		{
			i18n("word_attr_durability"),
			tostring(math.floor(var_62_0.durability))
		},
		{
			i18n("word_attr_luck"),
			"" .. tostring(math.floor(var_62_2))
		},
		{
			i18n("word_synthesize_power"),
			"<color=#ffff00>" .. var_62_1 .. "</color>"
		}
	}

def var_0_0.detachOnCardButton(arg_63_0, arg_63_1):
	local var_63_0 = GetOrAddComponent(arg_63_1.go, "EventTriggerListener")

	var_63_0.RemovePointClickFunc()
	var_63_0.RemoveBeginDragFunc()
	var_63_0.RemoveDragFunc()
	var_63_0.RemoveDragEndFunc()

def var_0_0.attachOnCardButton(arg_64_0, arg_64_1, arg_64_2):
	local var_64_0 = GetOrAddComponent(arg_64_1.go, "EventTriggerListener")

	arg_64_0.eventTriggers[var_64_0] = True

	var_64_0.AddPointClickFunc(function(arg_65_0, arg_65_1)
		if not arg_64_0.carddrag and arg_65_0 == arg_64_1.go:
			if arg_64_1.shipVO:
				arg_64_0.emit(FormationMediator.OPEN_SHIP_INFO, arg_64_1.shipVO.id, arg_64_0._currentFleetVO, var_0_0.TOGGLE_DETAIL)
			else
				arg_64_0.emit(FormationMediator.CHANGE_FLEET_SHIP, arg_64_1.shipVO, arg_64_0._currentFleetVO, var_0_0.TOGGLE_DETAIL, arg_64_2)

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))

	if arg_64_1.shipVO:
		local var_64_1 = arg_64_0._cards[arg_64_2]
		local var_64_2 = arg_64_1.tr.parent.GetComponent("ContentSizeFitter")
		local var_64_3 = arg_64_1.tr.parent.GetComponent("HorizontalLayoutGroup")
		local var_64_4 = arg_64_1.tr.rect.width * 0.5
		local var_64_5 = {}

		var_64_0.AddBeginDragFunc(function()
			if arg_64_0.carddrag:
				return

			arg_64_0._currentDragDelegate = var_64_0
			arg_64_0.carddrag = arg_64_1
			var_64_2.enabled = False
			var_64_3.enabled = False

			arg_64_1.tr.SetSiblingIndex(#var_64_1)

			for iter_66_0 = 1, #var_64_1:
				if var_64_1[iter_66_0] == arg_64_1:
					arg_64_0._shiftIndex = iter_66_0

				var_64_5[iter_66_0] = var_64_1[iter_66_0].tr.anchoredPosition

			LeanTween.scale(arg_64_1.paintingTr, Vector3(1.1, 1.1, 0), 0.3))
		var_64_0.AddDragFunc(function(arg_67_0, arg_67_1)
			if arg_64_0.carddrag != arg_64_1:
				return

			local var_67_0 = arg_64_1.tr.localPosition

			var_67_0.x = arg_64_0.change2ScrPos(arg_64_1.tr.parent, arg_67_1.position).x
			arg_64_1.tr.localPosition = var_67_0

			local var_67_1 = 1

			for iter_67_0 = 1, #var_64_1:
				if var_64_1[iter_67_0] != arg_64_1 and var_64_1[iter_67_0].shipVO and arg_64_1.tr.localPosition.x > var_64_1[iter_67_0].tr.localPosition.x + (var_67_1 < arg_64_0._shiftIndex and 1.1 or -1.1) * var_64_4:
					var_67_1 = var_67_1 + 1

			if arg_64_0._shiftIndex != var_67_1:
				arg_64_0._formationLogic.Shift(arg_64_0._shiftIndex, var_67_1, arg_64_2)
				arg_64_0.shiftCard(arg_64_0._shiftIndex, var_67_1, arg_64_2)

				for iter_67_1 = 1, #var_64_1:
					if var_64_1[iter_67_1] and var_64_1[iter_67_1] != arg_64_1:
						var_64_1[iter_67_1].tr.anchoredPosition = var_64_5[iter_67_1])
		var_64_0.AddDragEndFunc(function(arg_68_0, arg_68_1)
			if arg_64_0.carddrag != arg_64_1:
				return

			function resetCard()
				for iter_69_0 = 1, #var_64_1:
					var_64_1[iter_69_0].tr.anchoredPosition = var_64_5[iter_69_0]

				var_64_2.enabled = True
				var_64_3.enabled = True
				arg_64_0._shiftIndex = None

				arg_64_0.updateUltimateTitle()
				arg_64_0._formationLogic.SortSiblingIndex()
				arg_64_0.sortCardSiblingIndex()
				arg_64_0.emit(FormationMediator.CHANGE_FLEET_SHIPS_ORDER, arg_64_0._currentFleetVO)

				var_64_0.enabled = True
				arg_64_0.carddrag = None

			local var_68_0 = arg_64_0._forceDropCharacter

			arg_64_0._forceDropCharacter = None
			arg_64_0._currentDragDelegate = None
			var_64_0.enabled = False

			if var_68_0:
				resetCard()

				arg_64_1.paintingTr.localScale = Vector3(1, 1, 0)
			else
				local var_68_1 = math.min(math.abs(arg_64_1.tr.anchoredPosition.x - var_64_5[arg_64_0._shiftIndex].x) / 200, 1) * 0.3

				LeanTween.value(arg_64_1.go, arg_64_1.tr.anchoredPosition.x, var_64_5[arg_64_0._shiftIndex].x, var_68_1).setEase(LeanTweenType.easeOutCubic).setOnUpdate(System.Action_float(function(arg_70_0)
					local var_70_0 = arg_64_1.tr.anchoredPosition

					var_70_0.x = arg_70_0
					arg_64_1.tr.anchoredPosition = var_70_0)).setOnComplete(System.Action(function()
					resetCard()
					LeanTween.scale(arg_64_1.paintingTr, Vector3(1, 1, 0), 0.3))))

def var_0_0.shiftCard(arg_72_0, arg_72_1, arg_72_2, arg_72_3):
	local var_72_0 = arg_72_0._cards[arg_72_3]

	if #var_72_0 > 0:
		var_72_0[arg_72_1], var_72_0[arg_72_2] = var_72_0[arg_72_2], var_72_0[arg_72_1]

	arg_72_0._shiftIndex = arg_72_2

def var_0_0.change2ScrPos(arg_73_0, arg_73_1, arg_73_2):
	local var_73_0 = pg.UIMgr.GetInstance().overlayCameraComp

	return (LuaHelper.ScreenToLocal(arg_73_1, arg_73_2, var_73_0))

def var_0_0.tweenNumText(arg_74_0, arg_74_1, arg_74_2, arg_74_3, arg_74_4):
	LeanTween.value(go(arg_74_0), arg_74_4 or 0, math.floor(arg_74_1), arg_74_2 or 0.7).setOnUpdate(System.Action_float(function(arg_75_0)
		setText(arg_74_0, math.floor(arg_75_0)))).setOnComplete(System.Action(function()
		if arg_74_3:
			arg_74_3()))

def var_0_0.defaultFleetName(arg_77_0):
	if arg_77_0.name == "" or arg_77_0.name == None:
		return Fleet.DEFAULT_NAME[arg_77_0.id]
	else
		return arg_77_0.name

def var_0_0.GetFleetCount(arg_78_0):
	local var_78_0 = 0

	for iter_78_0, iter_78_1 in pairs(arg_78_0._fleetVOs):
		var_78_0 = var_78_0 + 1

	return var_78_0

def var_0_0.tweenTabArrow(arg_79_0, arg_79_1):
	local var_79_0 = arg_79_0.btnRegular.Find("arr")
	local var_79_1 = arg_79_0.btnSub.Find("arr")

	setActive(var_79_0, arg_79_1)
	setActive(var_79_1, arg_79_1)

	if arg_79_1:
		LeanTween.moveLocalY(go(var_79_0), var_79_0.localPosition.y + 8, 0.8).setEase(LeanTweenType.easeInOutSine).setLoopPingPong(-1)
		LeanTween.moveLocalY(go(var_79_1), var_79_1.localPosition.y + 8, 0.8).setEase(LeanTweenType.easeInOutSine).setLoopPingPong(-1)
	else
		LeanTween.cancel(go(var_79_0))
		LeanTween.cancel(go(var_79_1))

		local var_79_2 = var_79_0.localPosition

		var_79_2.y = 80
		var_79_0.localPosition = var_79_2

		local var_79_3 = var_79_1.localPosition

		var_79_3.y = 80
		var_79_1.localPosition = var_79_3

def var_0_0.recyclePainting(arg_80_0):
	for iter_80_0, iter_80_1 in pairs(arg_80_0._cards):
		for iter_80_2, iter_80_3 in ipairs(iter_80_1):
			iter_80_3.clear()

def var_0_0.onBackPressed(arg_81_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_81_0._renamePanel):
		arg_81_0.DisplayRenamePanel(False)
	else
		triggerButton(arg_81_0.backBtn)

def var_0_0.willExit(arg_82_0):
	arg_82_0.commanderFormationPanel.Destroy()

	if arg_82_0._attrFrame.gameObject.activeSelf:
		pg.UIMgr.GetInstance().UnblurPanel(arg_82_0._blurLayer, arg_82_0._tf)

	arg_82_0._formationLogic.Destroy()
	arg_82_0.recyclePainting()
	arg_82_0.DisplayRenamePanel(False)
	arg_82_0.tweenTabArrow(False)

	if arg_82_0.tweens:
		cancelTweens(arg_82_0.tweens)

	if arg_82_0.eventTriggers:
		for iter_82_0, iter_82_1 in pairs(arg_82_0.eventTriggers):
			ClearEventTrigger(iter_82_0)

		arg_82_0.eventTriggers = None

return var_0_0
