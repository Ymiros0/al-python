﻿return {
	time = 0,
	name = "航速提高",
	init_effect = "",
	color = "red",
	picture = "",
	desc = "航速提高30%",
	stack = 1,
	id = 59100,
	icon = 59100,
	last_effect = "",
	blink = {
		0,
		0.7,
		1,
		0.3,
		0.3
	},
	effect_list = {
		{
			type = "BattleBuffFixVelocity",
			trigger = {
				"onAttach"
			},
			arg_list = {
				add = 0,
				mul = 3000
			}
		}
	}
}
