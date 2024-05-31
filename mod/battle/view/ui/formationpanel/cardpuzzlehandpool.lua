ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleCardPuzzleEvent

var_0_0.Battle.CardPuzzleHandPool = class("CardPuzzleHandPool")

local var_0_3 = var_0_0.Battle.CardPuzzleHandPool

var_0_3.__name = "CardPuzzleHandPool"

function var_0_3.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1

	arg_1_0:init()
	pg.DelegateInfo.New(arg_1_0)
end

function var_0_3.SetCardPuzzleComponent(arg_2_0, arg_2_1)
	arg_2_0._cardPuzzleInfo = arg_2_1
	arg_2_0._hand = arg_2_0._cardPuzzleInfo:GetHand()

	for iter_2_0 = 1, var_0_0.Battle.BattleFleetCardPuzzleHand.MAX_HAND do
		arg_2_0:instCardView()
	end

	arg_2_0._hand:RegisterEventListener(arg_2_0, var_0_2.UPDATE_CARDS, arg_2_0.onUpdateCards)
	arg_2_0._cardPuzzleInfo:RegisterEventListener(arg_2_0, var_0_2.UPDATE_FLEET_ATTR, arg_2_0.onUpdateFleetAttr)
	arg_2_0:onUpdateCards()
end

function var_0_3.onUpdateCards(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0._hand:GetCardList()

	for iter_3_0 = 1, arg_3_0._hand.MAX_HAND do
		arg_3_0._cardList[iter_3_0]:SetCardInfo(var_3_0[iter_3_0])
	end
end

function var_0_3.onUpdateFleetAttr(arg_4_0, arg_4_1)
	for iter_4_0 = 1, arg_4_0._hand.MAX_HAND do
		arg_4_0._cardList[iter_4_0]:UpdateTotalCost()
	end
end

function var_0_3.init(arg_5_0)
	var_0_0.EventListener.AttachEventListener(arg_5_0)

	arg_5_0._cardList = {}
	arg_5_0._cardContainer = arg_5_0._go.transform:Find("card_container")
	arg_5_0._cardTpl = arg_5_0._go.transform:Find("card_tpl")
end

function var_0_3.updateHandCard(arg_6_0)
	for iter_6_0, iter_6_1 in ipairs(arg_6_0._cardList) do
		iter_6_1:updateCardView()
	end
end

function var_0_3.sort(arg_7_0)
	return
end

function var_0_3.instCardView(arg_8_0)
	local var_8_0 = cloneTplTo(arg_8_0._cardTpl, arg_8_0._cardContainer)
	local var_8_1 = var_0_0.Battle.CardPuzzleHandCardButton.New(go(var_8_0))

	table.insert(arg_8_0._cardList, var_8_1)
	var_8_1:ConfigCallback(function(arg_9_0)
		arg_8_0._cardPuzzleInfo:PlayCard(arg_9_0)
	end)

	return var_8_1
end

function var_0_3.test(arg_10_0, arg_10_1)
	arg_10_0._testContainer = arg_10_1

	LoadAndInstantiateAsync("UI", "CardTowerCardCombat", function(arg_11_0)
		arg_10_0._cardPool = pg.Pool.New(arg_10_0._testContainer, arg_11_0, 7, 20, false, false):InitSize()

		local var_11_0 = arg_10_0._hand:GetCardList()

		for iter_11_0, iter_11_1 in ipairs(var_11_0) do
			local var_11_1 = arg_10_0._cardPool:GetObject()
			local var_11_2 = var_11_1.transform

			var_11_2.localScale = Vector3(0.57, 0.57, 0)

			local var_11_3 = var_0_0.Battle.CardPuzzleCombatCard.New(var_11_2)

			var_11_3:SetCardInfo(iter_11_1)
			var_11_3:UpdateView()

			arg_10_0._modelClick = GetOrAddComponent(var_11_1, "ModelDrag")
			arg_10_0._modelPress = GetOrAddComponent(var_11_1, "UILongPressTrigger")
			arg_10_0._dragDelegate = GetOrAddComponent(var_11_1, "EventTriggerListener")

			pg.DelegateInfo.Add(arg_10_0, arg_10_0._modelClick.onModelClick)
			arg_10_0._modelClick.onModelClick:AddListener(function()
				return
			end)
			pg.DelegateInfo.Add(arg_10_0, arg_10_0._modelPress.onLongPressed)

			arg_10_0._modelPress.longPressThreshold = 1

			arg_10_0._modelPress.onLongPressed:RemoveAllListeners()
			arg_10_0._modelPress.onLongPressed:AddListener(function()
				return
			end)
		end
	end, true, true)
end

function var_0_3.Dispose(arg_14_0)
	arg_14_0._cardTpl = nil
	arg_14_0._cardContainer = nil
	arg_14_0._cardList = nil

	pg.DelegateInfo.Dispose(arg_14_0)
end
