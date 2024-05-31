ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleConst
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleAttr
local var_0_8 = var_0_0.Battle.BattleDataFunction
local var_0_9 = var_0_0.Battle.BattleAttr
local var_0_10 = class("BattleFleetCardPuzzleFleetBuffManager")

var_0_0.Battle.BattleFleetCardPuzzleFleetBuffManager = var_0_10
var_0_10.__name = "BattleFleetCardPuzzleFleetBuffManager"

function var_0_10.Ctor(arg_1_0, arg_1_1)
	arg_1_0._client = arg_1_1

	arg_1_0:init()
end

function var_0_10.Trigger(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = {}

	for iter_2_0, iter_2_1 in pairs(arg_2_0._buffList) do
		if iter_2_1:IsResponTo(arg_2_1) then
			table.insert(var_2_0, iter_2_1)
		end
	end

	for iter_2_2, iter_2_3 in ipairs(var_2_0) do
		iter_2_3:onTrigger(arg_2_1, arg_2_2)
	end
end

function var_0_10.Update(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0._buffList

	for iter_3_0, iter_3_1 in pairs(var_3_0) do
		iter_3_1:Update(arg_3_1)
	end
end

function var_0_10.AttachCardPuzzleBuff(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1:GetID()
	local var_4_1 = arg_4_0:GetCardPuzzleBuff(var_4_0)

	if var_4_1 then
		var_4_1:Stack()
	else
		arg_4_0._buffList[var_4_0] = arg_4_1

		arg_4_1:Attach(arg_4_0._client)
	end
end

function var_0_10.GetCardPuzzleBuff(arg_5_0, arg_5_1)
	return arg_5_0._buffList[arg_5_1]
end

function var_0_10.GetCardPuzzleBuffList(arg_6_0)
	return arg_6_0._buffList
end

function var_0_10.init(arg_7_0)
	arg_7_0._buffList = {}
end
