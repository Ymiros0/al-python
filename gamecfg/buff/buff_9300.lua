﻿return {
	init_effect = "",
	name = "白龙剧情战 触发龙宫机关-烈焰技能 buff3：触发技能，显示弹条与弹幕武器开火",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 9300,
	icon = 9300,
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
				time = 0,
				rant = 10000,
				skill_id = 9300
			}
		}
	}
}
