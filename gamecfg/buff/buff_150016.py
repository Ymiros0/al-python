return {
	time = 0.5,
	name = "",
	init_effect = "",
	last_effect = "bulunnusi_jianqi",
	picture = "",
	desc = "",
	stack = 6,
	id = 150016,
	last_effect_cld_scale = True,
	effect_list = {
		{
			type = "BattleBuffAura",
			trigger = {
				"onAttach",
				"onStack"
			},
			arg_list = {
				friendly_fire = True,
				buff_id = 150017,
				cld_data = {
					box = {
						range = 15
					}
				}
			}
		}
	}
}
