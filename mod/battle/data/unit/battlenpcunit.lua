ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = var_0_0.Battle.BattleAttr
local var_0_5 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleNPCUnit = class("BattleNPCUnit", var_0_0.Battle.BattleEnemyUnit)

local var_0_6 = var_0_0.Battle.BattleNPCUnit

function var_0_6.SetTemplate(arg_1_0, arg_1_1, arg_1_2)
	var_0_6.super.SetTemplate(arg_1_0, arg_1_1)

	arg_1_0._tmpData = setmetatable({}, {
		__index = var_0_0.Battle.BattleDataFunction.GetMonsterTmpDataFromID(arg_1_0._tmpID)
	})

	if arg_1_2.template then
		for iter_1_0, iter_1_1 in pairs(arg_1_2.template) do
			arg_1_0._tmpData[iter_1_0] = iter_1_1
		end

		arg_1_0._tmpData.id = arg_1_1
	end

	if arg_1_2.attr then
		var_0_4.SetAttr(arg_1_0, arg_1_2.attr)
	else
		arg_1_0:SetAttr()
	end

	local var_1_0 = arg_1_2.currentHP or arg_1_0:GetMaxHP()

	arg_1_0:SetCurrentHP(var_1_0)
	arg_1_0:InitCldComponent()
end
