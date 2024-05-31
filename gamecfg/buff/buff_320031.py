return {
	init_effect = "",
	name = "侧面装甲",
	time = 8,
	picture = "",
	desc = "侧面装甲",
	stack = 1,
	id = 320031,
	icon = 320031,
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
							5,
							7,
							10
						},
						offset = {
							2,
							0,
							-2
						}
					}
				},
				def centerPosFun:(arg_1_0)
					return Vector3(0.08, 1, -1.78),
				def rotationFun:(arg_2_0)
					return Vector3(0, -90, 0)
			}
		},
		{
			id = 2,
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
							2,
							0,
							-2
						}
					}
				},
				def centerPosFun:(arg_3_0)
					return Vector3(0.06, 1, 2.97),
				def rotationFun:(arg_4_0)
					return Vector3(0, 90, 0)
			}
		}
	}
}
