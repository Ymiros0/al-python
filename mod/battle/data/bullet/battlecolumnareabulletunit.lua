ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = Vector3.up
local var_0_4 = var_0_0.Battle.BattleVariable
local var_0_5 = var_0_0.Battle.BattleConfig
local var_0_6 = var_0_0.Battle.BattleConst
local var_0_7 = var_0_0.Battle.BattleTargetChoise
local var_0_8 = class("BattleColumnAreaBulletUnit", var_0_0.Battle.BattleAreaBulletUnit)

var_0_8.__name = "BattleColumnAreaBulletUnit"
var_0_0.Battle.BattleColumnAreaBulletUnit = var_0_8
var_0_8.AreaType = var_0_6.AreaType.COLUMN

function var_0_8.InitCldComponent(arg_1_0)
	local var_1_0 = arg_1_0:GetTemplate().cld_box
	local var_1_1 = arg_1_0:GetTemplate().cld_offset

	arg_1_0._cldComponent = var_0_0.Battle.BattleColumnCldComponent.New(var_1_0[1], var_1_0[3])

	local var_1_2 = {
		type = var_0_6.CldType.AOE,
		UID = arg_1_0:GetUniqueID(),
		IFF = arg_1_0:GetIFF()
	}

	arg_1_0._cldComponent:SetCldData(var_1_2)
end

function var_0_8.GetBoxSize(arg_2_0)
	local var_2_0 = arg_2_0._cldComponent:GetCldBoxSize()

	return Vector3(var_2_0.range, var_2_0.range, var_2_0.tickness)
end
