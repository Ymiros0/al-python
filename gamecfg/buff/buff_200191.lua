﻿return {
	init_effect = "",
	name = "2022莱莎联动 战斗BUFF 破甲弹幕LV3 破甲效果",
	time = 8,
	color = "red",
	picture = "",
	desc = "",
	stack = 1,
	id = 200191,
	icon = 200191,
	last_effect = "Darkness",
	effect_list = {
		{
			type = "BattleBuffAddAttr",
			trigger = {
				"onAttach",
				"onRemove"
			},
			arg_list = {
				attr = "injureRatio",
				number = 0.1
			}
		}
	}
}
