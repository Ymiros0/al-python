return {
	init_effect = "",
	name = "",
	time = 5,
	color = "blue",
	picture = "",
	desc = "",
	stack = 1,
	id = 15516,
	icon = 15510,
	last_effect = "",
	effect_list = {
		{
			id = 1,
			type = "BattleBuffShieldWall",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield02",
				count = 5,
				bulletType = 1,
				cld_list = {
					{
						box = {
							4,
							6,
							9
						},
						offset = {
							0,
							0,
							0
						}
					}
				},
				def centerPosFun:(arg_1_0)
					return Vector3(3, -1.8, 0.5),
				def rotationFun:(arg_2_0)
					return Vector3(0, 192, 0)
			}
		}
	}
}
