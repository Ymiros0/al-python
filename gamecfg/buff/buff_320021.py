return {
	init_effect = "",
	name = "正面装甲",
	time = 8,
	picture = "",
	desc = "正面装甲",
	stack = 1,
	id = 320021,
	icon = 320021,
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
