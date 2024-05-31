ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent
local var_0_2 = class("BattleCardPuzzleSkillActiveCard", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillActiveCard = var_0_2
var_0_2.__name = "BattleCardPuzzleSkillActiveCard"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._activeFrom = arg_1_0._tempData.arg_list.active_from or 0
	arg_1_0._activeID = arg_1_0._tempData.arg_list.active_ID_list
	arg_1_0._activeLabel = arg_1_0._tempData.arg_list.active_label_list
	arg_1_0._activeAll = arg_1_0._tempData.arg_list.active_all
end

function var_0_2.SkillEffectHandler(arg_2_0)
	local var_2_0 = arg_2_0._card:GetClient():GetCardPileByIndex(arg_2_0._activeFrom)
	local var_2_1 = {
		value = arg_2_0._activeID or arg_2_0._activeLabel,
		total = arg_2_0._activeAll,
		type = arg_2_0._activeID and var_0_1.SEARCH_BY_ID or var_0_1.SEARCH_BY_LABEL
	}
	local var_2_2 = var_2_0:Search(var_2_1)

	for iter_2_0, iter_2_1 in ipairs(var_2_2) do
		iter_2_1:Active()
	end

	arg_2_0:Finale()
end
