ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleSkillChangeDiveState = class("BattleSkillChangeDiveState", var_0_0.Battle.BattleSkillEffect)
var_0_0.Battle.BattleSkillChangeDiveState.__name = "BattleSkillChangeDiveState"

local var_0_1 = var_0_0.Battle.BattleSkillChangeDiveState

function var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._state = arg_1_0._tempData.arg_list.state
	arg_1_0._expose = arg_1_0._tempData.arg_list.expose
end

function var_0_1.DoDataEffect(arg_2_0, arg_2_1, arg_2_2)
	if arg_2_2:IsAlive() then
		local var_2_0 = arg_2_2:GetOxyState() or arg_2_2:InitOxygen()

		arg_2_2:ChangeOxygenState(arg_2_0._state)
		var_2_0:SetForceExpose(arg_2_0._expose)
	end
end
