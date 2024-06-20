return {
	effect_list = {
		{
			type = "BattleBuffCount",
			trigger = {
				"onFire"
			},
			arg_list = {
				countTarget = 10,
				countType = 20120,
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
				skill_id = 20122,
				countType = 20120
			}
		}
	},
	{
		desc = "主炮每进行10次攻击，触发全弹发射-布鲁克林级II"
	},
	init_effect = "",
	name = "全弹发射",
	time = 0,
	color = "red",
	picture = "",
	desc = "主炮每进行10次攻击，触发全弹发射-布鲁克林级II",
	stack = 1,
	id = 20122,
	icon = 20100,
	last_effect = ""
}