﻿local var_0_0 = class("NewNavalTacticsAdditionSkillCard", import(".NewNavalTacticsSkillCard"))

function var_0_0.Update(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = arg_1_1.level
	local var_1_1 = arg_1_1:GetNextLevelExp()
	local var_1_2 = arg_1_1:GetExp()
	local var_1_3 = arg_1_1:IsMaxLevel()

	arg_1_1:AddExp(arg_1_2)

	local var_1_4 = false

	if not var_1_3 and arg_1_1:IsMaxLevel() then
		var_1_4 = true
	end

	local var_1_5 = arg_1_1:GetNextLevelExp()
	local var_1_6 = arg_1_1:GetExp()
	local var_1_7 = arg_1_1.level - var_1_0
	local var_1_8 = var_1_7 > 0

	arg_1_1.level = var_1_0

	var_0_0.super.Update(arg_1_0, arg_1_1, var_1_7)

	if var_1_4 then
		local var_1_9 = var_1_1 - var_1_2

		arg_1_0.nextTxt.text = var_1_2 .. "+<color=#A9F548FF>" .. var_1_9 .. "</color>/" .. var_1_1
	elseif var_1_8 then
		arg_1_0.nextTxt.text = "0+<color=#A9F548FF>" .. var_1_6 .. "</color>/" .. var_1_5
	else
		arg_1_0.nextTxt.text = var_1_2 .. "+<color=#A9F548FF>" .. arg_1_2 .. "</color>/" .. var_1_1
	end
end

return var_0_0
