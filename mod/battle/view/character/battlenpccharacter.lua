ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleNPCCharacter = class("BattleNPCCharacter", var_0_0.Battle.BattleEnemyCharacter)
var_0_0.Battle.BattleNPCCharacter.__name = "BattleNPCCharacter"

local var_0_2 = var_0_0.Battle.BattleNPCCharacter

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)

	arg_1_0._preCastBound = false
end

function var_0_2.SetHPColor(arg_2_0, arg_2_1)
	arg_2_0._HPColor = arg_2_1
end

function var_0_2.GetHPColor(arg_3_0)
	return arg_3_0._HPColor
end

function var_0_2.SetModleID(arg_4_0, arg_4_1)
	arg_4_0._prefab = arg_4_1
end

function var_0_2.GetModleID(arg_5_0)
	if arg_5_0._prefab then
		return arg_5_0._prefab
	else
		return arg_5_0._unitData:GetTemplate().prefab
	end
end

function var_0_2.SetUnvisible(arg_6_0)
	arg_6_0._isUnvisible = true
end

function var_0_2.MakeVisible(arg_7_0)
	if arg_7_0._isUnvisible then
		arg_7_0._go:SetActive(false)
		arg_7_0._HPBar:SetActive(false)
		arg_7_0._buffBar:SetActive(false)
	end
end
