﻿return {
	init_effect = "",
	name = "2023 闪乱联动 地脉机关-缭SP 我方控制",
	time = 0,
	picture = "",
	desc = "",
	stack = 1,
	id = 200678,
	icon = 200678,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onAttach"
			},
			arg_list = {
				skill_id = 200678,
				target = "TargetSelf"
			}
		},
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				time = 20,
				target = "TargetSelf",
				skill_id = 200678
			}
		}
	}
}
