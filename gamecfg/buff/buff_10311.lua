﻿return {
	init_effect = "",
	name = "神射手",
	time = 1,
	picture = "",
	desc = "使得非装备武器发射的子弹暴击率提高100%",
	stack = 1,
	id = 10311,
	icon = 10311,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffAddBulletAttr",
			trigger = {
				"onBulletCreate"
			},
			arg_list = {
				attr = "cri",
				number = 1,
				index = {
					-1
				}
			}
		}
	}
}
