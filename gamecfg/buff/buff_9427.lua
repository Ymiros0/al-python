﻿return {
	init_effect = "",
	name = "古立特联动 梦芽支援弹幕LV2",
	time = 10,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 9427,
	icon = 9427,
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
				time = 5,
				rant = 10000,
				skill_id = 9426
			}
		}
	}
}
