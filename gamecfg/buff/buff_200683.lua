﻿return {
	init_effect = "",
	name = "2023 闪乱联动 地脉机关-缭 为全体恢复耐久 我方效果",
	time = 2,
	picture = "",
	desc = "",
	stack = 1,
	id = 200683,
	icon = 200683,
	last_effect = "Health",
	effect_list = {
		{
			type = "BattleBuffHP",
			trigger = {
				"onAttach"
			},
			arg_list = {
				maxHPRatio = 0.005
			}
		}
	}
}
