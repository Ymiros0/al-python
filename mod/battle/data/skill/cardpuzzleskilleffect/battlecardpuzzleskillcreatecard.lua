ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFleetCardPuzzleCardManageComponent
local var_0_2 = class("BattleCardPuzzleSkillCreateCard", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillCreateCard = var_0_2
var_0_2.__name = "BattleCardPuzzleSkillCreateCard"
var_0_2.MOVE_OP_Add = "Add"
var_0_2.MOVE_OP_BOTTOM = "Bottom"

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._cardID = arg_1_0._tempData.arg_list.card_id
	arg_1_0._moveTo = arg_1_0._tempData.arg_list.move_to
	arg_1_0._moveOP = arg_1_0._tempData.arg_list.move_op or var_0_1.FUNC_NAME_ADD
	arg_1_0._op = arg_1_0._tempData.arg_list.shuffle or 1
end

function var_0_2.SkillEffectHandler(arg_2_0)
	local var_2_0 = arg_2_0._card:GetClient()
	local var_2_1 = var_2_0:GenerateCard(arg_2_0._cardID)
	local var_2_2 = var_2_0:GetCardPileByIndex(arg_2_0._moveTo)

	var_2_2[arg_2_0._moveOP](var_2_2, var_2_1)

	if arg_2_0._op == 1 then
		var_2_2:Shuffle()
	end

	arg_2_0:Finale()
end
