﻿return {
	init_effect = "",
	name = "TBD(VT-8)",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "更换舰载机",
	stack = 1,
	id = 6349,
	icon = 6320,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffShiftWeapon",
			trigger = {
				"onAttach"
			},
			arg_list = {
				detach_id = 18069,
				weapon_id = 18169
			}
		}
	}
}
