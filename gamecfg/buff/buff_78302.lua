﻿return {
	init_effect = "",
	name = "最终剧情战用敌方小自杀buff",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 78302,
	icon = 8636,
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
				time = 8,
				rant = 10000,
				skill_id = 78300
			}
		}
	}
}
