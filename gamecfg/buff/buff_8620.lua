﻿return {
	init_effect = "",
	name = "航空减伤100%",
	time = 0,
	color = "blue",
	picture = "",
	desc = "航空减伤",
	stack = 1,
	id = 8620,
	icon = 8620,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddAttr",
			trigger = {
				"onAttach",
				"onRemove"
			},
			arg_list = {
				attr = "injureRatioByAir",
				number = -1
			}
		}
	}
}
