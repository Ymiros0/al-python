﻿return {
	init_effect = "",
	name = "活动buff-舰船祈愿效果-战斗减伤提高",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "舰队减伤提高",
	stack = 1,
	id = 521,
	icon = 521,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddAttr",
			trigger = {
				"onAttach"
			},
			arg_list = {
				attr = "injureRatio",
				number = -0.03
			}
		}
	}
}
