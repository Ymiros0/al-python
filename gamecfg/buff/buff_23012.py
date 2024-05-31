return {
	effect_list = {
		{
			type = "BattleBuffCount",
			trigger = {
				"onFire"
			},
			arg_list = {
				countType = 23010,
				countTarget = 10,
				gunnerBonus = True,
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
				skill_id = 23012,
				countType = 23010
			}
		}
	},
	{
		desc = "主炮每进行10次攻击，触发全弹发射-1934型II"
	},
	init_effect = "",
	name = "全弹发射",
	time = 0,
	color = "red",
	picture = "",
	desc = "主炮每进行10次攻击，触发全弹发射-1934型II",
	stack = 1,
	id = 23012,
	icon = 20000,
	last_effect = ""
}
