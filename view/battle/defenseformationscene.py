local var_0_0 = class("DefenseFormationScene", import("..base.BaseUI"))

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

def var_0_0.getUIName(arg_1_0):
	return "ExerciseFormationUI"

def var_0_0.init(arg_2_0):
	arg_2_0.eventTriggers = {}
	arg_2_0._blurLayer = arg_2_0.findTF("blur_panel")
	arg_2_0.backBtn = arg_2_0.findTF("top/back_btn", arg_2_0._blurLayer)
	arg_2_0._bottomPanel = arg_2_0.findTF("bottom", arg_2_0._blurLayer)
	arg_2_0._detailToggle = arg_2_0.findTF("toggle_list/detail_toggle", arg_2_0._bottomPanel)
	arg_2_0._formationToggle = arg_2_0.findTF("toggle_list/formation_toggle", arg_2_0._bottomPanel)
	arg_2_0._starTpl = arg_2_0.findTF("star_tpl")
	arg_2_0._heroInfoTpl = arg_2_0.findTF("heroInfo")
	arg_2_0._gridTFs = {
		vanguard = {},
		main = {}
	}
	arg_2_0._gridFrame = arg_2_0.findTF("GridFrame")

	for iter_2_0 = 1, 3:
		arg_2_0._gridTFs[TeamType.Main][iter_2_0] = arg_2_0._gridFrame.Find("main_" .. iter_2_0)
		arg_2_0._gridTFs[TeamType.Vanguard][iter_2_0] = arg_2_0._gridFrame.Find("vanguard_" .. iter_2_0)

	arg_2_0._heroContainer = arg_2_0.findTF("HeroContainer")
	arg_2_0._fleetInfo = arg_2_0.findTF("fleet_info", arg_2_0._blurLayer)
	arg_2_0._fleetNameText = arg_2_0.findTF("fleet_name/Text", arg_2_0._fleetInfo)
	arg_2_0._buffPanel = arg_2_0.findTF("buff_list")
	arg_2_0._buffGroup = arg_2_0.findTF("buff_group", arg_2_0._buffPanel)
	arg_2_0._buffModel = arg_2_0.getTpl("buff_model", arg_2_0._buffPanel)
	arg_2_0._propertyFrame = arg_2_0.findTF("property_frame", arg_2_0._blurLayer)
	arg_2_0._cannonPower = arg_2_0.findTF("cannon/Text", arg_2_0._propertyFrame)
	arg_2_0._torpedoPower = arg_2_0.findTF("torpedo/Text", arg_2_0._propertyFrame)
	arg_2_0._AAPower = arg_2_0.findTF("antiaircraft/Text", arg_2_0._propertyFrame)
	arg_2_0._airPower = arg_2_0.findTF("air/Text", arg_2_0._propertyFrame)
	arg_2_0._cost = arg_2_0.findTF("cost/Text", arg_2_0._propertyFrame)
	arg_2_0._mainGS = arg_2_0.findTF("gear_score/main/Text")
	arg_2_0._vanguardGS = arg_2_0.findTF("gear_score/vanguard/Text")
	arg_2_0._airDominanceFrame = arg_2_0.findTF("ac", arg_2_0._propertyFrame)

	if arg_2_0._airDominanceFrame:
		setActive(arg_2_0._airDominanceFrame, False)

	arg_2_0._attrFrame = arg_2_0.findTF("attr_frame", arg_2_0._blurLayer)
	arg_2_0._cardTpl = arg_2_0._tf.GetComponent(typeof(ItemList)).prefabItem[0]
	arg_2_0._cards = {}
	arg_2_0._cards[TeamType.Main] = {}
	arg_2_0._cards[TeamType.Vanguard] = {}

	setActive(arg_2_0._attrFrame, False)
	setActive(arg_2_0._cardTpl, False)
	setAnchoredPosition(arg_2_0._bottomPanel, {
		y = -90
	})

	arg_2_0._formationLogic = BaseFormation.New(arg_2_0._tf, arg_2_0._heroContainer, arg_2_0._heroInfoTpl, arg_2_0._gridTFs)

	arg_2_0.Register()

def var_0_0.Register(arg_3_0):
	arg_3_0._formationLogic.AddHeroInfoModify(function(arg_4_0, arg_4_1)
		local var_4_0 = arg_4_1.getConfigTable()
		local var_4_1 = pg.ship_data_template[arg_4_1.configId]
		local var_4_2 = findTF(arg_4_0, "info")
		local var_4_3 = findTF(var_4_2, "stars")
		local var_4_4 = arg_4_1.getStar()

		for iter_4_0 = 1, var_4_4:
			cloneTplTo(arg_3_0._starTpl, var_4_3)

		local var_4_5 = GetSpriteFromAtlas("shiptype", shipType2print(arg_4_1.getShipType()))

		if not var_4_5:
			warning("找不到船形, shipConfigId. " .. arg_4_1.configId)

		setImageSprite(findTF(var_4_2, "type"), var_4_5, True)
		setText(findTF(var_4_2, "frame/lv_contain/lv"), arg_4_1.level))
	arg_3_0._formationLogic.AddLongPress(function(arg_5_0, arg_5_1, arg_5_2)
		arg_3_0.emit(DefenseFormationMedator.OPEN_SHIP_INFO, arg_5_1.id, arg_5_2, var_0_0.TOGGLE_FORMATION)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))
	arg_3_0._formationLogic.AddClick(function(arg_6_0, arg_6_1)
		arg_3_0.emit(DefenseFormationMedator.CHANGE_FLEET_SHIP, arg_6_0, arg_6_1)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))
	arg_3_0._formationLogic.AddBeginDrag(function(arg_7_0)
		local var_7_0 = findTF(arg_7_0, "info")

		setButtonEnabled(arg_3_0.backBtn, False)
		setToggleEnabled(arg_3_0._detailToggle, False)
		SetActive(var_7_0, False))
	arg_3_0._formationLogic.AddEndDrag(function(arg_8_0)
		local var_8_0 = findTF(arg_8_0, "info")

		setButtonEnabled(arg_3_0.backBtn, True)
		setToggleEnabled(arg_3_0._detailToggle, True)
		SetActive(var_8_0, True))
	arg_3_0._formationLogic.AddShiftOnly(function(arg_9_0)
		arg_3_0.emit(DefenseFormationMedator.CHANGE_FLEET_SHIPS_ORDER, arg_9_0))
	arg_3_0._formationLogic.AddRemoveShip(function(arg_10_0, arg_10_1)
		arg_3_0.emit(DefenseFormationMedator.REMOVE_SHIP, arg_10_0, arg_10_1))

	local function var_3_0(arg_11_0)
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("defense_formation_tip_npc"),
			onYes = arg_11_0,
			onNo = arg_11_0
		})

	arg_3_0._formationLogic.AddCheckRemove(function(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4)
		if not arg_12_3.canRemove(arg_12_2):
			pg.TipsMgr.GetInstance().ShowTips(i18n("ship_formationUI_removeError_onlyShip", arg_12_2.getName(), "", Fleet.C_TEAM_NAME[arg_12_4]))
			arg_12_0()
		elif table.getCount(arg_12_3.mainShips) == 1 and arg_12_4 == TeamType.Main or table.getCount(arg_12_3.vanguardShips) == 1 and arg_12_4 == TeamType.Vanguard:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("exercise_clear_fleet_tip"),
				def onYes:()
					if not getProxy(FleetProxy).getFleetById(1).ExistActNpcShip():
						arg_12_1()
					else
						var_3_0(arg_12_0),
				onNo = arg_12_0
			})
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				zIndex = -30,
				hideNo = False,
				content = i18n("ship_formationUI_quest_remove", arg_12_2.getName()),
				onYes = arg_12_1,
				onNo = arg_12_0
			}))
	arg_3_0._formationLogic.AddGridTipClick(function(arg_14_0, arg_14_1)
		arg_3_0.emit(DefenseFormationMedator.CHANGE_FLEET_SHIP, None, arg_14_0))

def var_0_0.setShips(arg_15_0, arg_15_1):
	arg_15_0.shipVOs = arg_15_1

	arg_15_0._formationLogic.SetShipVOs(arg_15_1)

def var_0_0.SetFleet(arg_16_0, arg_16_1):
	arg_16_0._currentFleetVO = arg_16_1

	arg_16_0._formationLogic.SetFleetVO(arg_16_1)

def var_0_0.UpdateFleetView(arg_17_0, arg_17_1):
	arg_17_0.displayFleetInfo()
	arg_17_0._formationLogic.ResetGrid(TeamType.Vanguard)
	arg_17_0._formationLogic.ResetGrid(TeamType.Main)
	arg_17_0.resetFormationComponent()
	arg_17_0.updateAttrFrame()

	if arg_17_1:
		arg_17_0._formationLogic.LoadAllCharacter()
	else
		arg_17_0._formationLogic.SetAllCharacterPos()

def var_0_0.SetFleetNameLabel(arg_18_0):
	setText(arg_18_0._fleetNameText, i18n("exercise_formation_title"))

def var_0_0.didEnter(arg_19_0):
	onButton(arg_19_0, arg_19_0.backBtn, function()
		if arg_19_0._currentDragDelegate:
			LuaHelper.triggerEndDrag(arg_19_0._currentDragDelegate)

		if arg_19_0._attrFrame.gameObject.activeSelf:
			triggerToggle(arg_19_0._formationToggle, True)
		else
			local function var_20_0()
				arg_19_0.emit(var_0_0.ON_BACK)

			arg_19_0.emit(DefenseFormationMedator.COMMIT_FLEET, var_20_0), SOUND_BACK)
	onToggle(arg_19_0, arg_19_0._detailToggle, function(arg_22_0)
		if arg_19_0._currentDragDelegate:
			LuaHelper.triggerEndDrag(arg_19_0._currentDragDelegate)

		if arg_22_0:
			arg_19_0.displayAttrFrame(), SFX_PANEL)
	onToggle(arg_19_0, arg_19_0._formationToggle, function(arg_23_0)
		if arg_19_0._currentDragDelegate:
			LuaHelper.triggerEndDrag(arg_19_0._currentDragDelegate)

		if arg_23_0:
			arg_19_0.hideAttrFrame(), SFX_PANEL)
	onButton(arg_19_0, arg_19_0._attrFrame, function()
		triggerToggle(arg_19_0._formationToggle, True), SFX_PANEL)
	arg_19_0.UpdateFleetView(True)

	if arg_19_0.contextData.toggle != None:
		triggerToggle(arg_19_0[arg_19_0.contextData.toggle], True)

	shiftPanel(arg_19_0._bottomPanel, None, 0, None, 0.5, True, True)

def var_0_0.resetFormationComponent(arg_25_0):
	local var_25_0 = {}

	removeAllChildren(arg_25_0._buffGroup)

	for iter_25_0, iter_25_1 in ipairs(var_25_0):
		local var_25_1 = cloneTplTo(arg_25_0._buffModel, arg_25_0._buffGroup)

		tf(var_25_1).SetAsFirstSibling()
		SetActive(var_25_1.Find("dot_list/" .. iter_25_1.type), True)

		var_25_1.Find("buff_describe").GetComponent(typeof(Text)).text = iter_25_1.describe

	SetActive(arg_25_0._gridTFs.main[1].Find("flag"), #arg_25_0._currentFleetVO.getTeamByName(TeamType.Main) != 0)

def var_0_0.shiftCard(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	local var_26_0 = arg_26_0._cards[arg_26_3]

	if #var_26_0 > 0:
		var_26_0[arg_26_1], var_26_0[arg_26_2] = var_26_0[arg_26_2], var_26_0[arg_26_1]

	arg_26_0._shiftIndex = arg_26_2

def var_0_0.sortCardSiblingIndex(arg_27_0):
	local var_27_0 = arg_27_0._cards[TeamType.Main]
	local var_27_1 = arg_27_0._cards[TeamType.Vanguard]

	if #var_27_0 > 0 or #var_27_1 > 0:
		for iter_27_0 = 1, #var_27_0:
			var_27_0[iter_27_0].tr.SetSiblingIndex(iter_27_0)

		for iter_27_1 = 1, #var_27_1:
			var_27_1[iter_27_1].tr.SetSiblingIndex(iter_27_1)

def var_0_0.displayFleetInfo(arg_28_0):
	local var_28_0 = arg_28_0._currentFleetVO.GetPropertiesSum()
	local var_28_1 = arg_28_0._currentFleetVO.GetGearScoreSum(TeamType.Vanguard)
	local var_28_2 = arg_28_0._currentFleetVO.GetGearScoreSum(TeamType.Main)
	local var_28_3 = arg_28_0._currentFleetVO.GetCostSum()

	arg_28_0.tweenNumText(arg_28_0._cannonPower, var_28_0.cannon)
	arg_28_0.tweenNumText(arg_28_0._torpedoPower, var_28_0.torpedo)
	arg_28_0.tweenNumText(arg_28_0._AAPower, var_28_0.antiAir)
	arg_28_0.tweenNumText(arg_28_0._airPower, var_28_0.air)
	arg_28_0.tweenNumText(arg_28_0._cost, var_28_3.oil)
	arg_28_0.tweenNumText(arg_28_0._vanguardGS, var_28_1)
	arg_28_0.tweenNumText(arg_28_0._mainGS, var_28_2)
	setActive(arg_28_0.findTF("gear_score"), True)
	arg_28_0.SetFleetNameLabel()

def var_0_0.hideAttrFrame(arg_29_0):
	SetActive(arg_29_0._attrFrame, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_29_0._blurLayer, arg_29_0._tf)

def var_0_0.displayAttrFrame(arg_30_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_30_0._blurLayer, False)
	SetActive(arg_30_0._attrFrame, True)
	arg_30_0.initAttrFrame()

def var_0_0.initAttrFrame(arg_31_0):
	local var_31_0 = {
		[TeamType.Main] = "main",
		[TeamType.Vanguard] = "vanguard"
	}
	local var_31_1 = {
		[TeamType.Main] = arg_31_0._currentFleetVO.mainShips,
		[TeamType.Vanguard] = arg_31_0._currentFleetVO.vanguardShips
	}
	local var_31_2 = False

	for iter_31_0, iter_31_1 in pairs(var_31_1):
		local var_31_3 = arg_31_0._cards[iter_31_0]

		if #var_31_3 == 0:
			local var_31_4 = arg_31_0.findTF(var_31_0[iter_31_0] .. "/list", arg_31_0._attrFrame)

			for iter_31_2 = 1, 3:
				local var_31_5 = cloneTplTo(arg_31_0._cardTpl, var_31_4).gameObject

				table.insert(var_31_3, FormationCard.New(var_31_5))

			var_31_2 = True

	if var_31_2:
		arg_31_0.updateAttrFrame()

def var_0_0.updateAttrFrame(arg_32_0):
	local var_32_0 = {
		[TeamType.Main] = arg_32_0._currentFleetVO.mainShips,
		[TeamType.Vanguard] = arg_32_0._currentFleetVO.vanguardShips
	}

	for iter_32_0, iter_32_1 in pairs(var_32_0):
		local var_32_1 = arg_32_0._cards[iter_32_0]

		if #var_32_1 > 0:
			for iter_32_2 = 1, 3:
				if iter_32_2 <= #iter_32_1:
					local var_32_2 = arg_32_0.shipVOs[iter_32_1[iter_32_2]]

					var_32_1[iter_32_2].update(var_32_2)
					var_32_1[iter_32_2].updateProps(arg_32_0.getCardAttrProps(var_32_2))
				else
					var_32_1[iter_32_2].update(None)

				arg_32_0.attachOnCardButton(var_32_1[iter_32_2], iter_32_0)

	arg_32_0.updateUltimateTitle()
	setActive(arg_32_0.findTF(TeamType.Submarine, arg_32_0._attrFrame), False)

def var_0_0.updateUltimateTitle(arg_33_0):
	local var_33_0 = arg_33_0._cards[TeamType.Main]

	if #var_33_0 > 0:
		for iter_33_0 = 1, #var_33_0:
			setActive(var_33_0[iter_33_0].shipState, iter_33_0 == 1)

	local var_33_1 = arg_33_0._cards[TeamType.Vanguard]

	if #var_33_1 > 0:
		for iter_33_1 = 1, #var_33_1:
			setActive(var_33_1[iter_33_1].shipState, False)

def var_0_0.getCardAttrProps(arg_34_0, arg_34_1):
	local var_34_0 = arg_34_1.getProperties()
	local var_34_1 = arg_34_1.getShipCombatPower()
	local var_34_2 = arg_34_1.getBattleTotalExpend()

	return {
		{
			i18n("word_attr_durability"),
			tostring(math.floor(var_34_0.durability))
		},
		{
			i18n("word_attr_luck"),
			"" .. tostring(math.floor(var_34_2))
		},
		{
			i18n("word_synthesize_power"),
			"<color=#ffff00>" .. var_34_1 .. "</color>"
		}
	}

def var_0_0.attachOnCardButton(arg_35_0, arg_35_1, arg_35_2):
	local var_35_0 = GetOrAddComponent(arg_35_1.go, "EventTriggerListener")

	arg_35_0.eventTriggers[var_35_0] = True

	var_35_0.RemovePointClickFunc()
	var_35_0.RemoveBeginDragFunc()
	var_35_0.RemoveDragFunc()
	var_35_0.RemoveDragEndFunc()
	var_35_0.AddPointClickFunc(function(arg_36_0, arg_36_1)
		if not arg_35_0.carddrag and arg_36_0 == arg_35_1.go:
			if arg_35_1.shipVO:
				arg_35_0.emit(DefenseFormationMedator.OPEN_SHIP_INFO, arg_35_1.shipVO.id, arg_35_0._currentFleetVO, var_0_0.TOGGLE_DETAIL)
			else
				arg_35_0.emit(DefenseFormationMedator.CHANGE_FLEET_SHIP, arg_35_1.shipVO, arg_35_2)

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_PANEL))

	if arg_35_1.shipVO:
		local var_35_1 = arg_35_0._cards[arg_35_2]
		local var_35_2 = arg_35_1.tr.parent.GetComponent("ContentSizeFitter")
		local var_35_3 = arg_35_1.tr.parent.GetComponent("HorizontalLayoutGroup")
		local var_35_4 = arg_35_1.tr.rect.width * 0.5
		local var_35_5
		local var_35_6 = 0
		local var_35_7 = {}

		local function var_35_8()
			for iter_37_0 = 1, #var_35_1:
				if var_35_1[iter_37_0] != arg_35_1:
					var_35_1[iter_37_0].tr.anchoredPosition = var_35_1[iter_37_0].tr.anchoredPosition * 0.5 + Vector2(var_35_7[iter_37_0].x, var_35_7[iter_37_0].y) * 0.5

			if var_35_5 and var_35_6 <= Time.realtimeSinceStartup:
				var_35_0.OnDrag(var_35_5)

				var_35_5 = None

		local function var_35_9()
			for iter_38_0 = 1, #var_35_1:
				var_35_1[iter_38_0].tr.anchoredPosition = var_35_7[iter_38_0]

		local var_35_10 = Timer.New(var_35_8, 0.03333333333333333, -1)

		var_35_0.AddBeginDragFunc(function()
			if arg_35_0.carddrag:
				return

			arg_35_0._currentDragDelegate = var_35_0
			arg_35_0.carddrag = arg_35_1
			var_35_2.enabled = False
			var_35_3.enabled = False

			arg_35_1.tr.SetSiblingIndex(#var_35_1)

			for iter_39_0 = 1, #var_35_1:
				if var_35_1[iter_39_0] == arg_35_1:
					arg_35_0._shiftIndex = iter_39_0

				var_35_7[iter_39_0] = var_35_1[iter_39_0].tr.anchoredPosition

			var_35_10.Start()
			LeanTween.scale(arg_35_1.paintingTr, Vector3(1.1, 1.1, 0), 0.3))
		var_35_0.AddDragFunc(function(arg_40_0, arg_40_1)
			if arg_35_0.carddrag != arg_35_1:
				return

			local var_40_0 = arg_35_1.tr.localPosition

			var_40_0.x = arg_35_0.change2ScrPos(arg_35_1.tr.parent, arg_40_1.position).x
			arg_35_1.tr.localPosition = var_40_0

			if var_35_6 > Time.realtimeSinceStartup:
				var_35_5 = arg_40_1

				return

			local var_40_1 = 1

			for iter_40_0 = 1, #var_35_1:
				if var_35_1[iter_40_0] != arg_35_1 and var_35_1[iter_40_0].shipVO and arg_35_1.tr.localPosition.x > var_35_1[iter_40_0].tr.localPosition.x + (var_40_1 < arg_35_0._shiftIndex and 1.1 or -1.1) * var_35_4:
					var_40_1 = var_40_1 + 1

			if arg_35_0._shiftIndex != var_40_1:
				arg_35_0._formationLogic.Shift(arg_35_0._shiftIndex, var_40_1, arg_35_2)
				arg_35_0.shiftCard(arg_35_0._shiftIndex, var_40_1, arg_35_2)

				var_35_6 = Time.realtimeSinceStartup + 0.15)
		var_35_0.AddDragEndFunc(function(arg_41_0, arg_41_1)
			if arg_35_0.carddrag != arg_35_1:
				return

			arg_35_0._currentDragDelegate = None
			var_35_0.enabled = False

			local var_41_0 = math.min(math.abs(arg_35_1.tr.anchoredPosition.x - var_35_7[arg_35_0._shiftIndex].x) / 200, 1) * 0.3

			LeanTween.value(arg_35_1.go, arg_35_1.tr.anchoredPosition.x, var_35_7[arg_35_0._shiftIndex].x, var_41_0).setEase(LeanTweenType.easeOutCubic).setOnUpdate(System.Action_float(function(arg_42_0)
				local var_42_0 = arg_35_1.tr.anchoredPosition

				var_42_0.x = arg_42_0
				arg_35_1.tr.anchoredPosition = var_42_0)).setOnComplete(System.Action(function()
				var_35_9()

				var_35_2.enabled = True
				var_35_3.enabled = True
				arg_35_0._shiftIndex = None

				var_35_10.Stop()
				arg_35_0.updateUltimateTitle()
				arg_35_0._formationLogic.SortSiblingIndex()
				arg_35_0.sortCardSiblingIndex()
				arg_35_0.emit(DefenseFormationMedator.CHANGE_FLEET_SHIPS_ORDER, arg_35_0._currentFleetVO)
				LeanTween.scale(arg_35_1.paintingTr, Vector3(1, 1, 0), 0.3)

				var_35_0.enabled = True
				arg_35_0.carddrag = None)))

def var_0_0.change2ScrPos(arg_44_0, arg_44_1, arg_44_2):
	local var_44_0 = GameObject.Find("OverlayCamera").GetComponent("Camera")

	return (LuaHelper.ScreenToLocal(arg_44_1, arg_44_2, var_44_0))

def var_0_0.tweenNumText(arg_45_0, arg_45_1, arg_45_2):
	LeanTween.value(go(arg_45_0), 0, math.floor(arg_45_1), arg_45_2 or 0.7).setOnUpdate(System.Action_float(function(arg_46_0)
		setText(arg_45_0, math.floor(arg_46_0))))

def var_0_0.GetFleetCount(arg_47_0):
	return 1

def var_0_0.recyclePainting(arg_48_0):
	for iter_48_0, iter_48_1 in pairs(arg_48_0._cards):
		for iter_48_2, iter_48_3 in ipairs(iter_48_1):
			iter_48_3.clear()

def var_0_0.willExit(arg_49_0):
	if arg_49_0.eventTriggers:
		for iter_49_0, iter_49_1 in pairs(arg_49_0.eventTriggers):
			ClearEventTrigger(iter_49_0)

		arg_49_0.eventTriggers = None

	if arg_49_0._attrFrame.gameObject.activeSelf:
		pg.UIMgr.GetInstance().UnblurPanel(arg_49_0._blurLayer, arg_49_0._tf)

	pg.TimeMgr.GetInstance().RemoveTimer(arg_49_0.ActiveToggletimer1)

	arg_49_0.ActiveToggletimer1 = None

	pg.TimeMgr.GetInstance().RemoveTimer(arg_49_0.ActiveToggletimer)

	arg_49_0.ActiveToggletimer = None

	arg_49_0._formationLogic.Destroy()
	arg_49_0.recyclePainting()

return var_0_0