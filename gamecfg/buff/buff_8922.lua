﻿return {
	init_effect = "",
	name = "2022毛系活动 D面精神同步非实体炮弹跨射",
	time = 3,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 8922,
	icon = 8922,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				quota = 1,
				target = "TargetSelf",
				time = 1,
				rant = 10000,
				skill_id = 8922
			}
		}
	}
}
