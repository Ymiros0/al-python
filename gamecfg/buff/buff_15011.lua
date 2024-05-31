﻿return {
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
				count = 6,
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
	},
	{
		time = 6
	},
	{
		time = 6
	},
	{
		time = 6
	},
	{
		time = 7
	},
	{
		time = 7
	},
	{
		time = 7
	},
	{
		time = 8
	},
	{
		time = 8
	},
	{
		time = 8
	},
	{
		time = 8
	},
	init_effect = "",
	name = "",
	time = 6,
	color = "blue",
	picture = "",
	desc = "",
	stack = 1,
	id = 15011,
	icon = 15011,
	last_effect = ""
}
