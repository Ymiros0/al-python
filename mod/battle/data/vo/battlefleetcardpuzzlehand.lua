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
local var_0_10 = var_0_0.Battle.BattleAttr
local var_0_11 = var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent
local var_0_12 = class("BattleFleetCardPuzzleHand")

var_0_0.Battle.BattleFleetCardPuzzleHand = var_0_12
var_0_12.__name = "BattleFleetCardPuzzleHand"

function var_0_12.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._cardPuzzleComponent = arg_1_1
	arg_1_0._indexID = arg_1_2

	arg_1_0:init()
end

function var_0_12.GetIndexID(arg_2_0)
	return arg_2_0._indexID
end

function var_0_12.EnterCoolDownByType(arg_3_0, arg_3_1, arg_3_2)
	if arg_3_2 > 0 then
		local var_3_0 = pg.TimeMgr.GetInstance():GetCombatTime()

		arg_3_0._typeCDTimeStampList[arg_3_1] = var_3_0 + arg_3_2

		local var_3_1 = {
			total = true,
			value = arg_3_1,
			type = var_0_11.SEARCH_BY_TYPE
		}
		local var_3_2 = arg_3_0:Search(var_3_1)

		for iter_3_0, iter_3_1 in ipairs(var_3_2) do
			iter_3_1:SetOverHeatDuration(arg_3_2)
		end
	end
end

function var_0_12.Add(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:GetCardType()
	local var_4_1 = arg_4_0._typeCDTimeStampList[var_4_0]

	if var_4_1 ~= -1 then
		local var_4_2 = var_4_1 - pg.TimeMgr.GetInstance():GetCombatTime()

		arg_4_1:SetOverHeatDuration(var_4_2)
	end
end

function var_0_12.Update(arg_5_0, arg_5_1)
	for iter_5_0, iter_5_1 in pairs(arg_5_0._typeCDTimeStampList) do
		if iter_5_1 < arg_5_1 then
			arg_5_0._typeCDTimeStampList[iter_5_0] = -1
		end
	end
end

function var_0_12.Dispose(arg_6_0)
	return
end

function var_0_12.GetCardList(arg_7_0)
	return arg_7_0._handCardList
end

function var_0_12.IsFull(arg_8_0)
	return arg_8_0:GetLength() >= var_0_7.BASE_MAX_HAND + arg_8_0._attrManager:GetCurrent("HandExtra")
end

function var_0_12.init(arg_9_0)
	arg_9_0._handCardList = {}

	var_0_0.EventDispatcher.AttachEventDispatcher(arg_9_0)
	var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent.AttachCardManager(arg_9_0)

	arg_9_0._attrManager = arg_9_0._cardPuzzleComponent:GetAttrManager()
	arg_9_0._typeCDTimeStampList = {}

	for iter_9_0, iter_9_1 in pairs(CardPuzzleCard.CARD_TYPE) do
		arg_9_0._typeCDTimeStampList[iter_9_1] = -1
	end
end
