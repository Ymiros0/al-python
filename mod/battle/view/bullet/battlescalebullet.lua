ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleScaleBullet = class("BattleScaleBullet", var_0_0.Battle.BattleBullet)
var_0_0.Battle.BattleScaleBullet.__name = "BattleScaleBullet"

local var_0_1 = var_0_0.Battle.BattleScaleBullet

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.Update(arg_2_0, arg_2_1)
	var_0_1.super.Update(arg_2_0, arg_2_1)
	arg_2_0:updateModelScale()
end

function var_0_1.updateModelScale(arg_3_0)
	local var_3_0

	var_3_0.x, var_3_0 = arg_3_0._bulletData:GetBoxSize().x * 2, arg_3_0._tf.localScale
	arg_3_0._tf.localScale = var_3_0
end
