﻿return {
	init_effect = "",
	name = "防鱼雷隔舱T2",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "受到鱼雷伤害减少20%，同类效果取最大值，不可叠加",
	stack = 1,
	id = 6020,
	icon = 6020,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onStartGame"
			},
			arg_list = {
				skill_id = 6020,
				group = {
					id = 6010,
					level = 2
				}
			}
		}
	}
}
