return {
	effect_list = {
		{
			type = "BattleBuffCount",
			trigger = {
				"onFire"
			},
			arg_list = {
				countTarget = 8,
				countType = 21140,
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
				skill_id = 21142,
				countType = 21140
			}
		}
	},
	{
		desc = "主炮每进行8次攻击，触发全弹发射-爱丁堡级II"
	},
	init_effect = "",
	name = "全弹发射",
	time = 0,
	color = "red",
	picture = "",
	desc = "主炮每进行8次攻击，触发全弹发射-爱丁堡级II",
	stack = 1,
	id = 21142,
	icon = 20100,
	last_effect = ""
}
