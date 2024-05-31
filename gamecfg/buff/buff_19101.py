return {
	effect_list = {
		{
			id = 1,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield02",
				count = 8,
				bulletType = 1,
				cld_list = {
					{
						box = {
							4,
							6,
							9
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_1_0)
					local var_1_0 = arg_1_0 * 0.5

					return Vector3(math.sin(var_1_0) * 8, -0.5, math.cos(var_1_0) * 8),
				def rotationFun:(arg_2_0)
					return Vector3(0, arg_2_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST / 6 + 90, 0)
			}
		},
		{
			id = 2,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield02",
				count = 8,
				bulletType = 1,
				cld_list = {
					{
						box = {
							4,
							6,
							9
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_3_0)
					local var_3_0 = arg_3_0 * 1.5 + ys.Battle.BattleConfig.SHIELD_CENTER_CONST

					return Vector3(math.sin(var_3_0) * 5, -0.5, math.cos(var_3_0) * 5),
				def rotationFun:(arg_4_0)
					return Vector3(0, arg_4_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST / 2 - 90, 0)
			}
		},
		{
			id = 3,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield02",
				count = 8,
				bulletType = 1,
				cld_list = {
					{
						box = {
							4,
							6,
							9
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_5_0)
					local var_5_0 = arg_5_0 * 3

					return Vector3(math.sin(var_5_0) * 2.5, -0.5, math.cos(var_5_0) * 2.5),
				def rotationFun:(arg_6_0)
					return Vector3(0, arg_6_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
			}
		},
		{
			id = 4,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield02",
				count = 8,
				bulletType = 1,
				cld_list = {
					{
						box = {
							4,
							6,
							9
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_7_0)
					local var_7_0 = arg_7_0 * 3 + ys.Battle.BattleConfig.SHIELD_CENTER_CONST

					return Vector3(math.sin(var_7_0) * 2.5, -0.5, math.cos(var_7_0) * 2.5),
				def rotationFun:(arg_8_0)
					return Vector3(0, arg_8_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 90, 0)
			}
		}
	},
	{
		time = 5
	},
	{
		time = 6
	},
	{
		time = 7
	},
	{
		time = 8
	},
	{
		time = 9
	},
	{
		time = 10
	},
	{
		time = 11
	},
	{
		time = 12
	},
	{
		time = 13
	},
	{
		time = 15
	},
	init_effect = "",
	name = "全方位装甲",
	time = 5,
	picture = "",
	desc = "全方位装甲",
	stack = 1,
	id = 19101,
	icon = 19100,
	last_effect = ""
}
