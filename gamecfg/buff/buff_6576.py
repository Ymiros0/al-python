return {
	init_effect = "",
	name = "",
	time = 0,
	color = "red",
	picture = "",
	desc = "",
	stack = 1,
	id = 6572,
	icon = 6570,
	last_effect = "",
	effect_list = {
		{
			type = "BattleBuffShiftBullet",
			trigger = {
				"onAttach",
				"onRemove"
			},
			arg_list = {
				bullet_id = 1840,
				index = {
					3
				}
			}
		},
		{
			type = "BattleBuffCancelBuff",
			trigger = {
				"onTorpedoWeaponFire"
			},
			arg_list = {
				count = 1
			}
		}
	}
}
