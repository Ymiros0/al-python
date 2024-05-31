ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleConfig
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent

var_0_0.Battle.CardPuzzleHandBoard = class("CardPuzzleHandBoard")

local var_0_4 = var_0_0.Battle.CardPuzzleHandBoard

var_0_4.__name = "CardPuzzleHandBoard"
var_0_4.BASE_GAP = 166
var_0_4.BASE_SIBLING = 4

function var_0_4.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._go = arg_1_1
	arg_1_0._areaGO = arg_1_2

	arg_1_0:init()
end

function var_0_4.SetCardPuzzleComponent(arg_2_0, arg_2_1)
	arg_2_0._cardPuzzleInfo = arg_2_1
	arg_2_0._hand = arg_2_0._cardPuzzleInfo:GetHand()

	arg_2_0._hand:RegisterEventListener(arg_2_0, var_0_3.UPDATE_CARDS, arg_2_0.onUpdateCards)
	arg_2_0._cardPuzzleInfo:RegisterEventListener(arg_2_0, var_0_3.UPDATE_FLEET_ATTR, arg_2_0.onUpdateFleetAttr)
	arg_2_0:onUpdateCards()
end

function var_0_4.Update(arg_3_0)
	for iter_3_0, iter_3_1 in ipairs(arg_3_0._activeCardList) do
		iter_3_1:Update()
	end

	for iter_3_2, iter_3_3 in ipairs(arg_3_0._freeCardList) do
		iter_3_3:Update()
	end
end

function var_0_4.onUpdateCards(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0._hand:GetCardList()
	local var_4_1 = #arg_4_0._activeCardList

	while var_4_1 > 0 do
		local var_4_2 = arg_4_0._activeCardList[var_4_1]
		local var_4_3 = var_4_2:GetCardInfo()

		if not table.contains(var_4_0, var_4_3) then
			if var_4_3:GetCurrentPile() == arg_4_0._cardPuzzleInfo.CARD_PILE_INDEX_DECK then
				arg_4_0:delayRecyleCard(var_4_2)
			else
				arg_4_0:recyleCard(var_4_2)
			end
		end

		var_4_1 = var_4_1 - 1
	end

	for iter_4_0, iter_4_1 in ipairs(var_4_0) do
		local var_4_4

		for iter_4_2, iter_4_3 in ipairs(arg_4_0._activeCardList) do
			if iter_4_3:GetCardInfo() == iter_4_1 then
				var_4_4 = iter_4_3

				break
			end
		end

		if not var_4_4 then
			local var_4_5 = arg_4_0:getCard()

			var_4_5:SetCardInfo(iter_4_1)
			var_4_5:UpdateView()

			local var_4_6 = iter_4_1:GetFromPile() == arg_4_0._cardPuzzleInfo.CARD_PILE_INDEX_DECK and arg_4_0._drawPos or arg_4_0._generatePos

			var_4_5:DrawAnima(var_4_6)
			var_4_5:SetMoveLerp(0.1)
			var_4_5:ChangeState(var_4_5.STATE_FREE)
			table.insert(arg_4_0._activeCardList, var_4_5)
		end
	end

	arg_4_0:updateCardReferenceInHand()
end

function var_0_4.getCard(arg_5_0)
	local var_5_0

	if #arg_5_0._idleCardList > 0 then
		var_5_0 = table.remove(arg_5_0._idleCardList, 1)
	else
		local var_5_1 = arg_5_0._resManager:InstCardPuzzleCard().transform

		var_5_1:SetParent(arg_5_0._cardContainer)

		var_5_1.localScale = Vector3(0.57, 0.57, 0)
		var_5_1.localPosition = Vector3.zero
		var_5_0 = var_0_0.Battle.CardPuzzleCombatCard.New(var_5_1)
	end

	local function var_5_2()
		return
	end

	local function var_5_3()
		var_5_0:ChangeState(var_5_0.STATE_FREE)
		arg_5_0._cardPuzzleInfo:LongPressCard(var_5_0, false)
	end

	local function var_5_4()
		if var_5_0:GetState() == var_5_0.STATE_LONG_PRESS then
			var_5_3()
		end

		if var_5_0:GetState() ~= var_5_0.STATE_LOCK then
			arg_5_0:LockCardInHand()
			arg_5_0:UnlockCardInHand(var_5_0)
			arg_5_0:setDragingCard(var_5_0)

			arg_5_0._holdingCard = var_5_0

			arg_5_0:activeHighlight(true)
			arg_5_0._cardPuzzleInfo:BlockComponentByCard(true)
			arg_5_0:SetAllCardBlockRayCast(false)
			var_5_0:SetSibling(#arg_5_0._activeCardList + var_0_4.BASE_SIBLING)
			var_5_0:SetMoveLerp(0.5)
			var_5_0:ChangeState(var_5_0.STATE_DRAG)
		end
	end

	local function var_5_5(arg_9_0)
		var_5_0:UpdateDragPosition(arg_9_0)
	end

	local function var_5_6()
		local var_10_0 = true

		arg_5_0:setDragingCard()

		if arg_5_0._cardEnterDeck then
			var_10_0 = arg_5_0:TryPlayReturnCard(var_5_0)
		else
			var_10_0 = (arg_5_0._cardEnterHand ~= true or false) and arg_5_0:TryPlayCard(var_5_0)
		end

		if not var_10_0 then
			var_5_0:SetMoveLerp()
			arg_5_0:updateCardReferenceInHand()
		end

		arg_5_0._cardEnterHand = nil
		arg_5_0._cardEnterDeck = nil

		arg_5_0:UnlockCardInHand()
		arg_5_0:activeHighlight(false)
		arg_5_0:SetAllCardBlockRayCast(true)
		onDelayTick(function()
			arg_5_0._cardPuzzleInfo:BlockComponentByCard(false)
		end, 0.06)
	end

	local function var_5_7()
		var_5_0:ChangeState(var_5_0.STATE_LONG_PRESS)
		arg_5_0._cardPuzzleInfo:LongPressCard(var_5_0, true)
	end

	var_5_0:ConfigOP(var_5_2, var_5_4, var_5_5, var_5_6, var_5_7, var_5_3)

	return var_5_0
end

function var_0_4.recyleCard(arg_13_0, arg_13_1)
	for iter_13_0, iter_13_1 in ipairs(arg_13_0._activeCardList) do
		if iter_13_1 == arg_13_1 then
			arg_13_1:SetToObjPoolRecylePos()
			table.remove(arg_13_0._activeCardList, iter_13_0)

			break
		end
	end

	table.insert(arg_13_0._idleCardList, arg_13_1)
end

function var_0_4.delayRecyleCard(arg_14_0, arg_14_1)
	arg_14_1:ChangeState(arg_14_1.STATE_LOCK)

	for iter_14_0, iter_14_1 in ipairs(arg_14_0._activeCardList) do
		if iter_14_1 == arg_14_1 then
			table.remove(arg_14_0._activeCardList, iter_14_0)

			break
		end
	end

	table.insert(arg_14_0._freeCardList, arg_14_1)
	arg_14_1:MoveToDeck(function()
		for iter_15_0, iter_15_1 in ipairs(arg_14_0._freeCardList) do
			if iter_15_1 == arg_14_1 then
				arg_14_1:SetToObjPoolRecylePos()
				table.remove(arg_14_0._freeCardList, iter_15_0)

				break
			end
		end

		table.insert(arg_14_0._idleCardList, arg_14_1)
	end, arg_14_0._drawPos)
end

function var_0_4.onUpdateFleetAttr(arg_16_0, arg_16_1)
	for iter_16_0, iter_16_1 in ipairs(arg_16_0._activeCardList) do
		iter_16_1:UpdateTotalCost()
		iter_16_1:UpdateBoostHint()

		local var_16_0 = iter_16_1:GetCardInfo()
	end
end

function var_0_4.init(arg_17_0)
	var_0_0.EventListener.AttachEventListener(arg_17_0)

	arg_17_0._cardContainer = arg_17_0._go.transform
	arg_17_0._resManager = var_0_0.Battle.BattleResourceManager.GetInstance()
	arg_17_0._activeCardList = {}
	arg_17_0._idleCardList = {}
	arg_17_0._freeCardList = {}
	arg_17_0._startPos = arg_17_0._cardContainer:Find("handStart").localPosition
	arg_17_0._generatePos = arg_17_0._cardContainer:Find("generateStart").localPosition
	arg_17_0._drawPos = arg_17_0._cardContainer:Find("drawStart").localPosition
	arg_17_0._cancelArea = arg_17_0._cardContainer:Find("cancel_area")
	arg_17_0._returnArea = arg_17_0._cardContainer:Find("return_area")
	arg_17_0._handDelegate = GetOrAddComponent(arg_17_0._cancelArea, "EventTriggerListener")
	arg_17_0._deckDelegate = GetOrAddComponent(arg_17_0._returnArea, "EventTriggerListener")
	arg_17_0._area = arg_17_0._areaGO.transform
	arg_17_0._cancelHint = arg_17_0._area:Find("hand_hint")
	arg_17_0._returnHint = arg_17_0._area:Find("deck_hint")
	arg_17_0._readyHint = arg_17_0._area:Find("cast_hint")
end

function var_0_4.updateCardReferenceInHand(arg_18_0)
	for iter_18_0, iter_18_1 in ipairs(arg_18_0._activeCardList) do
		local var_18_0 = arg_18_0:getcardGap()
		local var_18_1 = Vector3.New(arg_18_0._startPos.x + (iter_18_0 - 1) * var_18_0, arg_18_0._startPos.y, 0)

		iter_18_1:SetReferencePos(var_18_1)
		iter_18_1:SetSibling(iter_18_0 + var_0_4.BASE_SIBLING)
	end
end

function var_0_4.getcardGap(arg_19_0)
	local var_19_0 = #arg_19_0._activeCardList

	if #arg_19_0._activeCardList <= var_0_2.BASE_MAX_HAND then
		return var_0_4.BASE_GAP
	else
		return 830 / (var_19_0 - 1)
	end
end

function var_0_4.setDragingCard(arg_20_0, arg_20_1)
	arg_20_0._cardPuzzleInfo:SetDragingCard(arg_20_1)
	arg_20_0._cardPuzzleInfo:SendUpdateAim()
end

function var_0_4.sort(arg_21_0)
	return
end

function var_0_4.activeHighlight(arg_22_0, arg_22_1)
	if arg_22_1 then
		arg_22_0._handDelegate:AddPointEnterFunc(function()
			arg_22_0._cardEnterHand = true

			setActive(arg_22_0._cancelHint, true)
			setActive(arg_22_0._returnHint, false)
			setActive(arg_22_0._readyHint, false)
		end)
		arg_22_0._handDelegate:AddPointExitFunc(function()
			arg_22_0._cardEnterHand = false

			setActive(arg_22_0._cancelHint, false)
			setActive(arg_22_0._readyHint, true)
		end)
		arg_22_0._deckDelegate:AddPointEnterFunc(function()
			arg_22_0._cardEnterDeck = true

			setActive(arg_22_0._readyHint, false)

			local var_25_0 = arg_22_0._holdingCard:GetCardInfo():GetReturnCost() ~= nil

			setActive(arg_22_0._cancelHint, not var_25_0)
			setActive(arg_22_0._returnHint, var_25_0)
		end)
		arg_22_0._deckDelegate:AddPointExitFunc(function()
			arg_22_0._cardEnterDeck = false

			setActive(arg_22_0._cancelHint, false)
			setActive(arg_22_0._readyHint, true)
		end)
	else
		setActive(arg_22_0._cancelHint, false)
		setActive(arg_22_0._returnHint, false)
		setActive(arg_22_0._readyHint, false)
		arg_22_0._handDelegate:RemovePointEnterFunc()
		arg_22_0._handDelegate:RemovePointExitFunc()
		arg_22_0._deckDelegate:RemovePointEnterFunc()
		arg_22_0._deckDelegate:RemovePointExitFunc()
	end

	setActive(arg_22_0._cancelArea, arg_22_1)
	setActive(arg_22_0._returnArea, arg_22_1)
end

function var_0_4.LockCardInHand(arg_27_0)
	for iter_27_0, iter_27_1 in ipairs(arg_27_0._activeCardList) do
		iter_27_1:ChangeState(iter_27_1.STATE_LOCK)
	end
end

function var_0_4.SetAllCardBlockRayCast(arg_28_0, arg_28_1)
	for iter_28_0, iter_28_1 in ipairs(arg_28_0._activeCardList) do
		iter_28_1:BlockRayCast(arg_28_1)
	end
end

function var_0_4.UnlockCardInHand(arg_29_0, arg_29_1)
	if arg_29_1 then
		arg_29_1:ChangeState(var_0_0.Battle.CardPuzzleCombatCard.STATE_FREE)
	else
		for iter_29_0, iter_29_1 in ipairs(arg_29_0._activeCardList) do
			iter_29_1:ChangeState(var_0_0.Battle.CardPuzzleCombatCard.STATE_FREE)
		end
	end
end

function var_0_4.TryPlayCard(arg_30_0, arg_30_1)
	local var_30_0 = arg_30_1:GetCardInfo()

	return (arg_30_0._cardPuzzleInfo:PlayCard(var_30_0))
end

function var_0_4.TryPlayReturnCard(arg_31_0, arg_31_1)
	local var_31_0 = arg_31_1:GetCardInfo()

	return (arg_31_0._cardPuzzleInfo:ReturnCard(var_31_0))
end

function var_0_4.Dispose(arg_32_0)
	return
end
