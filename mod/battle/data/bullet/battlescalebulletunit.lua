ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = Vector3.up
local var_0_4 = var_0_0.Battle.BattleVariable
local var_0_5 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleScaleBulletUnit = class("BattleScaleBulletUnit", var_0_0.Battle.BattleBulletUnit)
var_0_0.Battle.BattleScaleBulletUnit.__name = "BattleScaleBulletUnit"

local var_0_6 = var_0_0.Battle.BattleScaleBulletUnit

function var_0_6.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_6.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._scaleX = 0
end

function var_0_6.Update(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_0._tempData.cld_box

	if arg_2_0._scaleX + var_2_0[1] > arg_2_0._scaleLimit then
		arg_2_0:calcSpeed()
	else
		arg_2_0:UpdateCLDBox()
	end

	var_0_6.super.Update(arg_2_0, arg_2_1)
end

function var_0_6.SetTemplateData(arg_3_0, arg_3_1)
	var_0_6.super.SetTemplateData(arg_3_0, arg_3_1)

	arg_3_0._scaleSpeed = arg_3_0._tempData.extra_param.scaleSpeed
	arg_3_0._scaleLimit = arg_3_0._tempData.extra_param.cldMax
end

function var_0_6.InitSpeed(arg_4_0, arg_4_1)
	var_0_6.super.InitSpeed(arg_4_0, arg_4_1)
	arg_4_0:calcScaleSpeed()
end

function var_0_6.calcScaleSpeed(arg_5_0)
	local var_5_0 = arg_5_0._scaleSpeed * 0.5
	local var_5_1 = math.deg2Rad * arg_5_0._yAngle

	arg_5_0._speed = Vector3(var_5_0 * math.cos(var_5_1), 0, var_5_0 * math.sin(var_5_1))
end

function var_0_6.UpdateCLDBox(arg_6_0)
	local var_6_0 = arg_6_0._tempData.cld_box

	arg_6_0._scaleX = arg_6_0._scaleX + arg_6_0._scaleSpeed

	arg_6_0._cldComponent:ResetSize(var_6_0[1] + arg_6_0._scaleX, var_6_0[2], var_6_0[3])
end

function var_0_6.GetRadian(arg_7_0)
	local var_7_0 = arg_7_0._radCache or arg_7_0:GetYAngle() * math.deg2Rad
	local var_7_1 = arg_7_0._cosCache or math.cos(var_7_0)
	local var_7_2 = arg_7_0._sinCache or math.sin(var_7_0)

	return var_7_0, var_7_1, var_7_2
end
