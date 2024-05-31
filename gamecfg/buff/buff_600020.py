return {
	icon = 600020,
	name = "",
	time = 0,
	stack = 1,
	id = 600020,
	picture = "",
	last_effect = "",
	desc = "",
	effect_list = {
		{
			type = "BattleBuffAddBuff",
			trigger = {
				"onAttach"
			},
			arg_list = {
				buff_id = 600013,
				exceptCaster = True,
				target = "TargetAllHelp"
			}
		},
		{
			type = "BattleBuffDeath",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				time = 0.1
			}
		}
	}
}
