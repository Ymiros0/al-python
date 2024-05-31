ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.VigilantAntiSubState = class("VigilantAntiSubState", var_0_0.Battle.IAntiSubState)
var_0_0.Battle.VigilantAntiSubState.__name = "VigilantAntiSubState"

local var_0_1 = var_0_0.Battle.VigilantAntiSubState

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.OnVigilantEngage(arg_2_0, arg_2_1)
	return
end

function var_0_1.OnMineExplode(arg_3_0, arg_3_1)
	return
end

function var_0_1.OnSubmarinFloat(arg_4_0, arg_4_1)
	return
end

function var_0_1.OnHateChain(arg_5_0, arg_5_1)
	arg_5_1:OnEngageState(true)
end

function var_0_1.ToPreLevel(arg_6_0, arg_6_1)
	arg_6_1:OnSuspiciousState()
end

function var_0_1.GetWeaponUseable(arg_7_0)
	return {}
end

function var_0_1.CanDecay(arg_8_0)
	return true
end

function var_0_1.GetWarnMark(arg_9_0)
	return 2
end

function var_0_1.GetMeterSpeed(arg_10_0)
	return 1.3
end

function var_0_1.DecayDuration(arg_11_0)
	return 2
end
