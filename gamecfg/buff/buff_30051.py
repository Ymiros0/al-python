return {
	effect_list = {
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onStartGame"
			},
			arg_list = {
				skill_id = 30051,
				minWeaponNumber = 1,
				check_weapon = True,
				label = {
					"DD",
					"MG"
				}
			}
		},
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onStartGame"
			},
			arg_list = {
				skill_id = 30052,
				minWeaponNumber = 1,
				check_weapon = True,
				label = {
					"CL",
					"MG"
				}
			}
		}
	},
	{
		desc = "主炮每进行10次攻击，触发专属弹幕-舒尔茨II"
	},
	desc_get = "",
	name = "专属弹幕-舒尔茨",
	init_effect = "",
	time = 0,
	color = "red",
	picture = "",
	desc = "",
	stack = 1,
	id = 30051,
	icon = 30040,
	last_effect = ""
}