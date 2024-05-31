ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleCardPuzzleCardEffectQueue")

var_0_0.Battle.BattleCardPuzzleCardEffectQueue = var_0_1
var_0_1.__name = "BattleCardPuzzleCardEffectQueue"
var_0_1.QUEUE_TYPE_NORMAL = "normal"
var_0_1.QUEUE_TYPE_RETURN = "return"

function var_0_1.Ctor(arg_1_0, arg_1_1)
	arg_1_0._card = arg_1_1
	arg_1_0._holdForInputMark = false
	arg_1_0._condition = nil
	arg_1_0._moveAfterCast = nil
	arg_1_0._effectList = {}
	arg_1_0._headEffect = nil
end

function var_0_1.SetQueueType(arg_2_0, arg_2_1)
	arg_2_0._queueType = arg_2_1
end

function var_0_1.GetQueueType(arg_3_0)
	return arg_3_0._queueType
end

function var_0_1.ConfigData(arg_4_0, arg_4_1)
	arg_4_0._condition = arg_4_1.condition
	arg_4_0._branch = arg_4_1.branch

	local var_4_0 = #arg_4_1
	local var_4_1 = -1

	while var_4_0 > 0 do
		local var_4_2 = arg_4_1[var_4_0]

		assert(var_0_0.Battle[var_4_2.type] ~= nil, "找不到对应的卡牌效果类型>>" .. var_4_2.type .. "<<，检查卡牌ID：" .. arg_4_0._card:GetCardID())

		local var_4_3 = var_0_0.Battle[var_4_2.type].New(var_4_2)

		if var_4_3:HoldForInput() then
			arg_4_0._holdForInputMark = true
		end

		if var_4_3:MoveCardAfterCast() ~= arg_4_0._moveAfterCast then
			arg_4_0._moveAfterCast = var_4_3:MoveCardAfterCast()
		end

		var_4_3:ConfigCard(arg_4_0._card)
		var_4_3:SetQueue(arg_4_0)

		arg_4_0._effectList[var_4_3] = var_4_1
		var_4_0 = var_4_0 - 1
		var_4_1 = var_4_3
	end

	arg_4_0._headEffect = var_4_1
end

function var_0_1.Start(arg_5_0)
	if arg_5_0._headEffect == -1 then
		arg_5_0._card:QueueFinish(arg_5_0)
	else
		arg_5_0._headEffect:Execute()
	end
end

function var_0_1.EffectFinale(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0._effectList[arg_6_1]

	if var_6_0 == -1 then
		arg_6_0._card:QueueFinish(arg_6_0)
	else
		var_6_0:Execute()
	end
end

function var_0_1.GetBranch(arg_7_0)
	return arg_7_0._branch
end

function var_0_1.GetHoldForInputMark(arg_8_0)
	return arg_8_0._holdForInputMark
end

function var_0_1.GetMoveAfterCast(arg_9_0)
	return arg_9_0._moveAfterCast
end

function var_0_1.GetCondition(arg_10_0)
	return arg_10_0._condition
end
