ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleConst
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleCardPuzzleConfig
local var_0_8 = var_0_0.Battle.BattleAttr
local var_0_9 = var_0_0.Battle.BattleDataFunction
local var_0_10 = var_0_0.Battle.CardPuzzleBoardClicker
local var_0_11 = var_0_0.Battle.BattleVariable
local var_0_12 = class("BattleFleetCardPuzzleComponent")

var_0_0.Battle.BattleFleetCardPuzzleComponent = var_0_12
var_0_12.__name = "BattleFleetCardPuzzleComponent"
var_0_12.CARD_PILE_INDEX_DISCARD = -1
var_0_12.CARD_PILE_INDEX_HAND = 0
var_0_12.CARD_PILE_INDEX_DECK = 1
var_0_12.CARD_PILE_INDEX_MOVE_DECK = 2

def var_0_12.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._fleetVO = arg_1_1

	arg_1_0.init()

def var_0_12.CustomConfigID(arg_2_0, arg_2_1):
	arg_2_0._customCombatID = arg_2_1

	arg_2_0._energy.CustomConfig(arg_2_0._customCombatID)
	arg_2_0._moveDeck.CustomConfig(arg_2_0._customCombatID)

def var_0_12.Dispose(arg_3_0):
	var_0_0.EventDispatcher.DetachEventDispatcher(arg_3_0)
	var_0_0.EventListener.DetachEventListener(arg_3_0)

	arg_3_0._fleetVO = None

def var_0_12.GetPuzzleDungeonID(arg_4_0):
	return arg_4_0._customCombatID

def var_0_12.GetTotalCommonHP(arg_5_0):
	return arg_5_0._maxCommonHP

def var_0_12.GetCurrentCommonHP(arg_6_0):
	return arg_6_0._currentCommonHP

def var_0_12.GetEnergy(arg_7_0):
	return arg_7_0._energy

def var_0_12.EnergyUpdate(arg_8_0):
	arg_8_0._fleetAttr.SetAttr("BaseEnergy", arg_8_0._energy.GetCurrentEnergy())

def var_0_12.AppendUnit(arg_9_0, arg_9_1):
	arg_9_1.RegisterEventListener(arg_9_0, var_0_3.UPDATE_COMMON_HP, arg_9_0.onUpdateCommonHP)

	arg_9_0._maxCommonHP = arg_9_0._maxCommonHP + arg_9_1.GetAttrByName("maxHP")
	arg_9_0._currentCommonHP = arg_9_0._maxCommonHP

	local var_9_0

	arg_9_0._cardPuzzleAA.AppendCrewUnit(arg_9_1)

	if arg_9_1.IsMainFleetUnit():
		arg_9_0._mainUnit = arg_9_1
		var_9_0 = TeamType.TeamPos.FLAG_SHIP
	else
		arg_9_0._scoutUnit = arg_9_1

		arg_9_0._cardPuzzleAA.SwitchHost(arg_9_1)

		var_9_0 = TeamType.TeamPos.LEADER

	local var_9_1 = var_0_0.Event.New(var_0_3.UPDATE_FLEET_SHIP, {
		teamType = var_9_0
	})

	arg_9_0.DispatchEvent(var_9_1)

def var_0_12.InitCardPuzzleData(arg_10_0, arg_10_1):
	arg_10_0._fleetVO.GetUnitBound().SwtichDBRGL()

	local var_10_0 = arg_10_1.relicList

	for iter_10_0, iter_10_1 in ipairs(var_10_0):
		table.insert(arg_10_0._relicList, iter_10_1)

		local var_10_1 = iter_10_1.GetEffects()

		for iter_10_2, iter_10_3 in ipairs(var_10_1):
			if iter_10_3.type == CardPuzzleGift.EFFECT_TYPE.BATTLE_BUFF:
				for iter_10_4, iter_10_5 in ipairs(iter_10_3.arg_list):
					local var_10_2 = var_0_0.Battle.BattleFleetBuffUnit.New(iter_10_5)

					arg_10_0._fleetBuff.AttachCardPuzzleBuff(var_10_2)

def var_0_12.RemoveUnit(arg_11_0, arg_11_1):
	arg_11_1.UnregisterEventListener(arg_11_0, var_0_3.UPDATE_COMMON_HP)

def var_0_12.GetMainUnit(arg_12_0):
	return arg_12_0._mainUnit

def var_0_12.GetScoutUnit(arg_13_0):
	return arg_13_0._scoutUnit

def var_0_12.AttachMoveController(arg_14_0, arg_14_1):
	arg_14_0._moveController = arg_14_1

def var_0_12.TakeoverMovecontroller(arg_15_0, arg_15_1, arg_15_2):
	arg_15_0._moveController.InputTargetPoint(arg_15_1, arg_15_2)
	arg_15_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.FLEET_MOVE_TO, {
		pos = arg_15_1
	}))

def var_0_12.ReturnMovecontroller(arg_16_0):
	arg_16_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.FLEET_MOVE_TO, {}))

def var_0_12.PlayCard(arg_17_0, arg_17_1):
	if arg_17_0.CheckCardCastable(arg_17_1):
		local function var_17_0()
			local var_18_0 = arg_17_1.GetTotalCost()

			arg_17_0._energy.ConsumeEnergy(var_18_0)
			arg_17_0._hand.Remove(arg_17_1)
			arg_17_0._hand.EnterCoolDownByType(arg_17_1.GetCardType(), arg_17_1.GetCardCD())

			if arg_17_1.GetMoveAfterCast() == var_0_12.CARD_PILE_INDEX_DISCARD:
				arg_17_0._discard.Add(arg_17_1)

			arg_17_0.TryDrawCard()

		arg_17_1.Precast(var_17_0)

		return True
	else
		return False

def var_0_12.ReturnCard(arg_19_0, arg_19_1):
	if arg_19_0.CheckCardReturnable(arg_19_1):
		local function var_19_0()
			local var_20_0 = arg_19_1.GetReturnCost()

			arg_19_0._energy.ConsumeEnergy(var_20_0)
			arg_19_0._hand.Remove(arg_19_1)
			arg_19_0.TryDrawCard()

		arg_19_1.Retrun(var_19_0)

		return True
	else
		return False

def var_0_12.PlayMoveCard(arg_21_0, arg_21_1):
	arg_21_1.SetInputPoint(arg_21_0._clickToScenePoint)
	arg_21_1.Precast()
	arg_21_0._moveDeck.Remove(arg_21_1)

def var_0_12.CheckCardCastable(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_1.GetTotalCost()
	local var_22_1 = arg_22_1.GetCastCondition() != False

	if var_22_0 <= arg_22_0._energy.GetCurrentEnergy() and var_22_1:
		return True

def var_0_12.CheckCardReturnable(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_1.GetReturnCost()

	if var_23_0 and var_23_0 <= arg_23_0._energy.GetCurrentEnergy():
		return True

def var_0_12.SetDragingCard(arg_24_0, arg_24_1):
	arg_24_0._dragingCard = arg_24_1

def var_0_12.GetDragingCard(arg_25_0):
	return arg_25_0._dragingCard

def var_0_12.SendUpdateAim(arg_26_0):
	local var_26_0 = arg_26_0._dragingCard and arg_26_0._dragingCard.GetCardInfo().GetCardEffectTargetFilterList() or {}

	arg_26_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.UPDATE_CARD_TARGET_FILTER, {
		targetFilterList = var_26_0
	}))

def var_0_12.Start(arg_27_0):
	arg_27_0._fleetBuff.Trigger(var_0_5.BuffEffectType.ON_START_GAME)

	for iter_27_0, iter_27_1 in pairs(var_0_7.CustomAttrInitList):
		arg_27_0._fleetAttr.AddBaseAttr(iter_27_0, iter_27_1)

	if arg_27_0._customCombatID and var_0_9.GetPuzzleDungeonTemplate(arg_27_0._customCombatID):
		local var_27_0 = var_0_9.GetPuzzleDungeonTemplate(arg_27_0._customCombatID)
		local var_27_1 = var_27_0.deck

		for iter_27_2, iter_27_3 in ipairs(var_27_1):
			local var_27_2 = arg_27_0.GenerateCard(iter_27_3)

			arg_27_0._deck.Add(var_27_2)

		local var_27_3 = var_27_0.init_move
		local var_27_4 = 0

		while var_27_4 < var_27_3:
			local var_27_5 = arg_27_0.GenerateCard(var_0_7.BASE_MOVE_ID)

			arg_27_0._moveDeck.Add(var_27_5)

			var_27_4 = var_27_4 + 1

		if var_27_0.init_shuffle != var_0_0.Battle.BattleFleetCardPuzzleDeck.NOT_INIT_SHUFFLE:
			arg_27_0._deck.Shuffle()
	else
		arg_27_0._deck.Shuffle()

	arg_27_0._energy.Start()
	arg_27_0.TryDrawCard()
	arg_27_0.SetClickEnable(True)

def var_0_12.Update(arg_28_0, arg_28_1):
	arg_28_0._energy.Update(arg_28_1)
	arg_28_0._fleetBuff.Update(arg_28_1)
	arg_28_0._cardPuzzleAA.Update(arg_28_1)
	arg_28_0.updateMoveDeck(arg_28_1)
	arg_28_0._hand.Update(arg_28_1)

def var_0_12.UpdateClickPos(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	var_0_10 = var_0_10 or var_0_0.Battle.CardPuzzleBoardClicker

	if arg_29_3 == var_0_10.CLICK_STATE_CLICK:
		arg_29_0._uiPoint.Set(arg_29_1, arg_29_2)
		var_0_0.Battle.BattleVariable.UIPosToScenePos(arg_29_0._uiPoint, arg_29_0._clickToScenePoint)
		arg_29_0._fleetVO.GetUnitBound().FixCardPuzzleInput(arg_29_0._clickToScenePoint)
		arg_29_0._clickToScenePointCache.Copy(arg_29_0._clickToScenePoint)
		arg_29_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.ON_BOARD_CLICK, {
			click = arg_29_3
		}))
	elif arg_29_3 == var_0_10.CLICK_STATE_DRAG:
		arg_29_0._uiPoint.Set(arg_29_1, arg_29_2)
		var_0_0.Battle.BattleVariable.UIPosToScenePos(arg_29_0._uiPoint, arg_29_0._clickToScenePoint)
		arg_29_0._fleetVO.GetUnitBound().FixCardPuzzleInput(arg_29_0._clickToScenePoint)

		if not arg_29_0._clickToScenePointCache.Equals(arg_29_0._clickToScenePoint):
			arg_29_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.ON_BOARD_CLICK, {
				click = arg_29_3
			}))

		arg_29_0._clickToScenePointCache.Copy(arg_29_0._clickToScenePoint)
	elif arg_29_3 == var_0_10.CLICK_STATE_RELEASE:
		if arg_29_0._clickEnable:
			local var_29_0 = arg_29_0._moveDeck.TryPlayTopMoveCard()

			if var_29_0:
				arg_29_0.PlayMoveCard(var_29_0)

		arg_29_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.ON_BOARD_CLICK, {
			click = arg_29_3
		}))

def var_0_12.SetClickEnable(arg_30_0, arg_30_1):
	arg_30_0._clickEnable = arg_30_1

def var_0_12.GetClickEnable(arg_31_0):
	return arg_31_0._clickEnable

def var_0_12.BlockComponentByCard(arg_32_0, arg_32_1):
	arg_32_1 = not arg_32_1

	arg_32_0.SetClickEnable(arg_32_1)
	arg_32_0.DispatchEvent(var_0_0.Event.New(var_0_3.COMMON_BUTTON_ENABLE, {
		flag = arg_32_1
	}))

def var_0_12.LongPressCard(arg_33_0, arg_33_1, arg_33_2):
	if arg_33_2:
		arg_33_0.DispatchEvent(var_0_0.Event.New(var_0_3.SHOW_CARD_DETAIL, {
			card = arg_33_1
		}))
		arg_33_0.DispatchBulletTime(0.1)
	else
		arg_33_0.DispatchEvent(var_0_0.Event.New(var_0_3.SHOW_CARD_DETAIL, {}))
		arg_33_0.DispatchBulletTime()

def var_0_12.DispatchBulletTime(arg_34_0, arg_34_1):
	if arg_34_1:
		var_0_11.AppendIFFFactor(var_0_6.FOE_CODE, "check_card", arg_34_1)
		var_0_11.AppendIFFFactor(var_0_6.FRIENDLY_CODE, "check_card", arg_34_1)
	else
		var_0_11.RemoveIFFFactor(var_0_6.FOE_CODE, "check_card")
		var_0_11.RemoveIFFFactor(var_0_6.FRIENDLY_CODE, "check_card")

	arg_34_0.DispatchEvent(var_0_0.Event.New(var_0_3.LONG_PRESS_BULLET_TIME, {
		timeScale = arg_34_1
	}))

def var_0_12.dispatchClick(arg_35_0, arg_35_1):
	if arg_35_0._clickEnable:
		arg_35_0._fleetVO.DispatchEvent(var_0_0.Event.New(var_0_3.ON_BOARD_CLICK, {
			click = arg_35_1
		}))

def var_0_12.GetHand(arg_36_0):
	return arg_36_0._hand

def var_0_12.GetDeck(arg_37_0):
	return arg_37_0._deck

def var_0_12.GetRelicList(arg_38_0):
	return arg_38_0._relicList

def var_0_12.GetTouchScreenPoint(arg_39_0):
	return arg_39_0._clickToScenePoint

def var_0_12.GetMoveDeck(arg_40_0):
	return arg_40_0._moveDeck

def var_0_12.GetCardPileByIndex(arg_41_0, arg_41_1):
	return arg_41_0._cardPileList[arg_41_1]

def var_0_12.GetFleetVO(arg_42_0):
	return arg_42_0._fleetVO

def var_0_12.GetAttrManager(arg_43_0):
	return arg_43_0._fleetAttr

def var_0_12.GetBuffManager(arg_44_0):
	return arg_44_0._fleetBuff

def var_0_12.GetCardPuzzleAAUnit(arg_45_0):
	return arg_45_0._cardPuzzleAA

def var_0_12.TryDrawCard(arg_46_0):
	while not arg_46_0._hand.IsFull() and arg_46_0._deck.GetLength() > 0:
		local var_46_0 = arg_46_0._deck.Pop()

		arg_46_0._hand.Add(var_46_0)

		local var_46_1 = var_46_0.GetTotalCost()
		local var_46_2 = arg_46_0._energy.FillToCooldown(var_46_1)

		var_46_0.SetBaseEnergyFillDuration(var_46_2)

def var_0_12.FlushHandOverheat(arg_47_0):
	local var_47_0 = arg_47_0._hand.GetCardList()

	for iter_47_0, iter_47_1 in ipairs(var_47_0):
		local var_47_1 = iter_47_1.GetTotalCost()
		local var_47_2 = arg_47_0._energy.FillToCooldown(var_47_1)

		iter_47_1.SetBaseEnergyFillDuration(var_47_2)

def var_0_12.HoldForInput(arg_48_0, arg_48_1):
	arg_48_0._holdingCard = arg_48_1

def var_0_12.GenerateCard(arg_49_0, arg_49_1):
	local var_49_0 = var_0_0.Battle.BattleCardPuzzleCard.New(arg_49_0)

	var_49_0.SetCardTemplate(arg_49_1)

	return var_49_0

def var_0_12.UpdateAttrByBuff(arg_50_0, arg_50_1, arg_50_2):
	return

def var_0_12.AddAttrBySkill(arg_51_0, arg_51_1, arg_51_2):
	arg_51_0._fleetAttr.AddBaseAttr(arg_51_1, arg_51_2)

def var_0_12.UpdateAttrBySet(arg_52_0, arg_52_1, arg_52_2):
	arg_52_0._fleetAttr.SetAttr(arg_52_1, arg_52_2)

def var_0_12.DispatchUpdateAttr(arg_53_0, arg_53_1):
	local var_53_0 = var_0_0.Event.New(var_0_3.UPDATE_FLEET_ATTR, {
		attrName = arg_53_1
	})

	arg_53_0.DispatchEvent(var_53_0)

	if arg_53_0._dragingCard:
		arg_53_0.SendUpdateAim()

def var_0_12.IsAAActive(arg_54_0):
	return arg_54_0._fleetAttr.GetCurrent("CardAntiaircraft") > 0

def var_0_12.ConsumeAACounter(arg_55_0, arg_55_1):
	local var_55_0 = (arg_55_1 or 1) * -1

	arg_55_0._fleetAttr.AddBaseAttr("CardAntiaircraft", var_55_0)

def var_0_12.init(arg_56_0):
	arg_56_0._maxCommonHP = 0
	arg_56_0._currentCommonHP = 0
	arg_56_0._fleetAttr = var_0_0.Battle.BattleFleetCardPuzzleAttribute.New(arg_56_0)
	arg_56_0._fleetBuff = var_0_0.Battle.BattleFleetCardPuzzleFleetBuffManager.New(arg_56_0)
	arg_56_0._energy = var_0_0.Battle.BattleFleetCardPuzzleEnergy.New(arg_56_0)
	arg_56_0._deck = var_0_0.Battle.BattleFleetCardPuzzleDeck.New(arg_56_0, var_0_12.CARD_PILE_INDEX_DECK)
	arg_56_0._hand = var_0_0.Battle.BattleFleetCardPuzzleHand.New(arg_56_0, var_0_12.CARD_PILE_INDEX_HAND)
	arg_56_0._discard = var_0_0.Battle.BattleFleetCardPuzzleDiscard.New(arg_56_0, var_0_12.CARD_PILE_INDEX_DISCARD)
	arg_56_0._moveDeck = var_0_0.Battle.BattleFleetCardPuzzleMoveDeck.New(arg_56_0, var_0_12.CARD_PILE_INDEX_MOVE_DECK)
	arg_56_0._cardPileList = {
		[var_0_12.CARD_PILE_INDEX_DISCARD] = arg_56_0._discard,
		[var_0_12.CARD_PILE_INDEX_HAND] = arg_56_0._hand,
		[var_0_12.CARD_PILE_INDEX_DECK] = arg_56_0._deck,
		[var_0_12.CARD_PILE_INDEX_MOVE_DECK] = arg_56_0._moveDeck
	}
	arg_56_0._uiPoint = Vector2.New(0, 0)
	arg_56_0._clickToScenePoint = Vector3.New(0, 0, 0)
	arg_56_0._clickToScenePointCache = Vector3.New(0, 0, 0)
	arg_56_0._scoutUnit = None
	arg_56_0._mainUnit = None
	arg_56_0._relicList = {}
	arg_56_0._cardPuzzleAA = var_0_0.Battle.BattleFleetCardPuzzleAntiAirUnit.New(arg_56_0)

	function arg_56_0._fleetVO.GetFleetAntiAirWeapon()
		return arg_56_0._cardPuzzleAA

	arg_56_0.initEvent()

def var_0_12.initEvent(arg_58_0):
	arg_58_0._hand.RegisterEventListener(arg_58_0, var_0_3.UPDATE_CARDS, arg_58_0.onUpdateHands)
	arg_58_0._deck.RegisterEventListener(arg_58_0, var_0_3.UPDATE_CARDS, arg_58_0.onUpdateDeck)

def var_0_12.onUpdateHands(arg_59_0, arg_59_1):
	local var_59_0 = arg_59_0._hand.GetCardList()
	local var_59_1 = {}

	for iter_59_0, iter_59_1 in ipairs(var_59_0):
		local var_59_2 = iter_59_1.GetLabels()

		for iter_59_2, iter_59_3 in ipairs(var_59_2):
			var_59_1[iter_59_3] = (var_59_1[iter_59_3] or 0) + 1

	arg_59_0._fleetAttr.SetAttr("HandCount", #var_59_0)

	for iter_59_4, iter_59_5 in pairs(var_59_1):
		arg_59_0._fleetAttr.SetAttr(iter_59_4 .. "LabelInHand", iter_59_5)

	local var_59_3 = var_0_0.Event.New(var_0_3.UPDATE_FLEET_ATTR, {})

	arg_59_0.DispatchEvent(var_59_3)

def var_0_12.onUpdateDeck(arg_60_0, arg_60_1):
	local var_60_0 = arg_60_0._deck.GetCardList()

	arg_60_0._fleetAttr.SetAttr("DeckCount", #var_60_0)

	local var_60_1 = arg_60_1.Data

	if var_60_1.type == var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent.FUNC_NAME_ADD or var_60_1.type == var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent.FUNC_NAME_BOTTOM:
		arg_60_0.TryDrawCard()

def var_0_12.updateMoveDeck(arg_61_0, arg_61_1):
	arg_61_0._moveDeck.Update(arg_61_1)

	if arg_61_0._moveDeck.GetGeneratePorcess() >= 1:
		arg_61_0._moveDeck.RestartGenrate()

		local var_61_0 = arg_61_0.GenerateCard(var_0_7.BASE_MOVE_ID)

		arg_61_0._moveDeck.Add(var_61_0)

def var_0_12.onUpdateCommonHP(arg_62_0, arg_62_1):
	local var_62_0 = arg_62_1.Data.dHP

	arg_62_0._currentCommonHP = math.clamp(arg_62_0._currentCommonHP + var_62_0, 0, arg_62_0._maxCommonHP)
