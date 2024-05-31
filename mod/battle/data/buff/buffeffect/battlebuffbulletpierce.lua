ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffBulletPierce = class("BattleBuffBulletPierce", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffBulletPierce.__name = "BattleBuffBulletPierce"

function var_0_0.Battle.BattleBuffBulletPierce.Ctor(arg_1_0, arg_1_1)
	var_0_0.Battle.BattleBuffBulletPierce.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_0.Battle.BattleBuffBulletPierce.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._number = arg_2_0._tempData.arg_list.number
	arg_2_0._rate = arg_2_0._tempData.arg_list.rate
	arg_2_0._bulletType = arg_2_0._tempData.arg_list.bulletType or 0
end

function var_0_0.Battle.BattleBuffBulletPierce.onBulletCreate(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = arg_3_3._bullet

	if arg_3_0:IsHappen(tonumber(arg_3_0._rate)) and (arg_3_0._bulletType == var_3_0._tempData.type or arg_3_0._bulletType == 0) then
		var_3_0._pierceCount = arg_3_0._number
	end
end
