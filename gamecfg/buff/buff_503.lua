﻿return {
	init_effect = "",
	name = "活动buff-建筑效果-战斗伤害提高",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "舰队伤害提高",
	stack = 1,
	id = 503,
	icon = 503,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddAttr",
			trigger = {
				"onAttach"
			},
			arg_list = {
				attr = "damageRatioBullet",
				number = 0.02
			}
		}
	}
}
