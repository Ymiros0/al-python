return {
	uiEffect = "AimEffectUI",
	name = "海伦娜-舰队之眼",
	cd = 0,
	painting = 1,
	id = 60008,
	picture = "0",
	aniEffect = "",
	desc = "舰队之眼",
	effect_list = {
		{
			target_choise = "TargetHarmRandom",
			type = "BattleSkillAddBuff",
			arg_list = {
				buff_id = 60015
			},
			targetAniEffect = {
				effect = "aim",
				posFun = function(arg_1_0, arg_1_1, arg_1_2)
					arg_1_2 = math.min(1, arg_1_2 / 40)

					local var_1_0 = arg_1_0.x - arg_1_1.x
					local var_1_1 = var_1_0 * (1 - arg_1_2)
					local var_1_2 = 1 * arg_1_2
					local var_1_3 = arg_1_0.z - arg_1_1.z + var_1_0 * (1 - arg_1_2) * arg_1_2

					if arg_1_2 >= 1 then
						var_1_3 = 0
					elseif arg_1_2 >= 0.8 then
						var_1_3 = var_1_3 * (-4 * arg_1_2 + 4)
					elseif arg_1_2 >= 0.5 then
						var_1_3 = var_1_3 * arg_1_2
					else
						var_1_3 = var_1_3 * (1 - arg_1_2)
					end

					return Vector3(var_1_1, var_1_2, var_1_3)
				end
			}
		}
	}
}
