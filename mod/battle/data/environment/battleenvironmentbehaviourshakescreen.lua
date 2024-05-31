ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleEnvironmentBehaviourShakeScreen", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourShakeScreen = var_0_3
var_0_3.__name = "BattleEnvironmentBehaviourShakeScreen"

function var_0_3.Ctor(arg_1_0)
	var_0_3.super.Ctor(arg_1_0)
end

function var_0_3.SetTemplate(arg_2_0, arg_2_1)
	var_0_3.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._shakeID = arg_2_0._tmpData.shake_ID
end

function var_0_3.doBehaviour(arg_3_0)
	var_0_0.Battle.BattleCameraUtil.GetInstance():StartShake(pg.shake_template[arg_3_0._shakeID])

	arg_3_0._state = var_0_3.STATE_OVERHEAT

	if arg_3_0._tmpData.reload_time then
		arg_3_0._CDstartTime = pg.TimeMgr.GetInstance():GetCombatTime()
	end
end
