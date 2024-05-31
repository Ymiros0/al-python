﻿return {
	effect_list = {
		{
			type = "BattleBuffCount",
			trigger = {
				"onFire"
			},
			arg_list = {
				countTarget = 15,
				countType = 23040,
				index = {
					1
				}
			}
		},
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onBattleBuffCount"
			},
			arg_list = {
				target = "TargetSelf",
				skill_id = 23041,
				countType = 23040
			}
		}
	},
	{
		desc = "主炮每进行15次攻击，触发全弹发射-1936A型I"
	},
	init_effect = "",
	name = "全弹发射",
	time = 0,
	color = "red",
	picture = "",
	desc = "主炮每进行15次攻击，触发全弹发射-1936A型I",
	stack = 1,
	id = 23041,
	icon = 20000,
	last_effect = ""
}
