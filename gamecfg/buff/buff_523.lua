﻿return {
	init_effect = "",
	name = "活动buff-祭典祈愿效果-战斗伤害提高",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "舰队伤害提高",
	stack = 1,
	id = 523,
	icon = 523,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddAttr",
			trigger = {
				"onAttach"
			},
			arg_list = {
				attr = "damageRatioBullet",
				number = 0.03
			}
		}
	}
}
