﻿return {
	init_effect = "",
	name = "司特莲库斯引力场_本体buff加强",
	time = 0,
	color = "yellow",
	last_effect = "yinlichang_qianyin",
	picture = "",
	desc = "",
	stack = 1,
	id = 79017,
	icon = 8636,
	last_effect_cld_scale = true,
	effect_list = {
		{
			type = "BattleBuffAura",
			trigger = {
				"onAttach"
			},
			arg_list = {
				buff_id = 79018,
				cld_data = {
					box = {
						range = 125
					}
				}
			}
		}
	}
}
