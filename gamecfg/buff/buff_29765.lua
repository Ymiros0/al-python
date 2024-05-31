﻿return {
	effect_list = {
		{
			type = "BattleBuffCount",
			trigger = {
				"onFire"
			},
			arg_list = {
				countType = 29765,
				countTarget = 10,
				gunnerBonus = true,
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
				skill_id = 29762,
				countType = 29765
			}
		}
	},
	{
		desc = "主炮每进行15次攻击，触发专属弹幕-可怖"
	},
	desc_get = "主炮每进行15次攻击，触发专属弹幕-可怖",
	name = "专属弹幕-可怖Ⅱ-正常",
	init_effect = "",
	time = 0,
	color = "red",
	picture = "",
	desc = "主炮每进行15次攻击，触发专属弹幕-可怖",
	stack = 1,
	id = 29765,
	icon = 29760,
	last_effect = ""
}
