return {
	init_effect = "",
	name = "防卫者AT·FIELDlv2",
	time = 40,
	last_effect = "ATdun",
	picture = "",
	desc = "AT·FIELD",
	stack = 1,
	id = 79061,
	icon = 30000003,
	last_effect_cld_scale = True,
	effect_list = {
		{
			type = "BattleBuffBarrier",
			trigger = {
				"onUpdate",
				"onRemove",
				"onAttach",
				"onTakeDamage"
			},
			arg_list = {
				durability = 30000,
				cld_data = {
					box = {
						range = 28
					},
					offset = {
						0,
						4,
						0
					}
				}
			}
		}
	}
}
