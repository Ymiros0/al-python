return {
	effect_list = {
		{
			type = "BattleBuffCount",
			trigger = {
				"onFire"
			},
			arg_list = {
				countType = 29800,
				countTarget = 16,
				gunnerBonus = True,
				index = {
					1
				}
			}
		},
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onBattleBuffCount"
			},
			arg_list = {
				buff_id = 29805,
				target = "TargetSelf",
				countType = 29800
			}
		}
	},
	{
		desc = "主炮每进行10次攻击，触发全弹发射-鞍山级III"
	},
	init_effect = "",
	name = "全弹发射",
	time = 0,
	color = "red",
	picture = "",
	desc = "主炮每进行16次攻击，触发全弹发射-鞍山级III",
	stack = 1,
	id = 29801,
	icon = 20000,
	last_effect = ""
}