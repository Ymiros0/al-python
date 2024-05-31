ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffMountExpand", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffMountExpand = var_0_1
var_0_1.__name = "BattleBuffMountExpand"

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._weaponIndex = arg_2_0._tempData.arg_list.index
end

function var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2)
	arg_3_1:ExpandWeaponMount(arg_3_0._weaponIndex)
end
