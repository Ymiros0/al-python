﻿return {
	init_effect = "",
	name = "正面装甲",
	time = 10,
	picture = "",
	desc = "正面装甲",
	stack = 1,
	id = 7035,
	icon = 7035,
	last_effect = "",
	effect_list = {
		{
			id = 1,
			type = "BattleBuffShieldWall",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield02",
				count = 20,
				bulletType = 1,
				cld_list = {
					{
						box = {
							4,
							6,
							9
						},
						offset = {
							0,
							0,
							0
						}
					}
				},
				centerPosFun = function(arg_1_0)
					return Vector3(3, -1.8, 0.5)
				end,
				rotationFun = function(arg_2_0)
					return Vector3(0, 192, 0)
				end
			}
		}
	}
}
