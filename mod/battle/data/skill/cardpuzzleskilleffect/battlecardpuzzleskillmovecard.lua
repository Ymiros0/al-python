ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent
local var_0_2 = class("BattleCardPuzzleSkillMoveCard", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillMoveCard = var_0_2
var_0_2.__name = "BattleCardPuzzleSkillMoveCard"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._moveFrom = arg_1_0._tempData.arg_list.move_from or 0
	arg_1_0._moveTo = arg_1_0._tempData.arg_list.move_to
	arg_1_0._moveID = arg_1_0._tempData.arg_list.move_ID_list
	arg_1_0._moveLabel = arg_1_0._tempData.arg_list.move_label_list
	arg_1_0._moveOP = arg_1_0._tempData.arg_list.move_op or var_0_1.FUNC_NAME_ADD
	arg_1_0._moveOther = arg_1_0._tempData.arg_list.move_other
	arg_1_0._moveAll = arg_1_0._tempData.arg_list.move_all
	arg_1_0._op = arg_1_0._tempData.arg_list.shuffle or 1
end

function var_0_2.MoveCardAfterCast(arg_2_0)
	if arg_2_0._moveID or arg_2_0._moveLabel then
		return var_0_2.super.MoveCardAfterCast(arg_2_0)
	else
		return arg_2_0._moveTo
	end
end

function var_0_2.SkillEffectHandler(arg_3_0)
	local var_3_0 = arg_3_0._card:GetClient()
	local var_3_1 = var_3_0:GetCardPileByIndex(arg_3_0._moveTo)
	local var_3_2 = var_3_0:GetCardPileByIndex(arg_3_0._moveFrom)

	if arg_3_0._moveID then
		local var_3_3 = {
			value = arg_3_0._moveID,
			type = var_0_1.SEARCH_BY_ID,
			total = arg_3_0._moveAll
		}
		local var_3_4 = var_3_2:Search(var_3_3)

		for iter_3_0, iter_3_1 in ipairs(var_3_4) do
			var_3_1[arg_3_0._moveOP](var_3_1, iter_3_1)
			var_3_2:Remove(iter_3_1, arg_3_0._moveTo)
		end
	elseif arg_3_0._moveLabel then
		local var_3_5 = {
			value = arg_3_0._moveLabel,
			type = var_0_1.SEARCH_BY_LABEL,
			total = arg_3_0._moveAll
		}
		local var_3_6 = var_3_2:Search(var_3_5)

		for iter_3_2, iter_3_3 in ipairs(var_3_6) do
			var_3_1[arg_3_0._moveOP](var_3_1, iter_3_3)
			var_3_2:Remove(iter_3_3, arg_3_0._moveTo)
		end
	elseif arg_3_0._moveOther then
		local var_3_7 = var_3_2:GetCardList()

		for iter_3_4, iter_3_5 in ipairs(var_3_7) do
			if iter_3_5 ~= arg_3_0._card then
				var_3_1[arg_3_0._moveOP](var_3_1, iter_3_5)
				var_3_2:Remove(iter_3_5, arg_3_0._moveTo)
			end
		end
	else
		var_3_1[arg_3_0._moveOP](var_3_1, arg_3_0._card)
	end

	if arg_3_0._op == 1 then
		var_3_1:Shuffle()
	end

	arg_3_0:Finale()
end
