return {
	init_effect = "",
	name = "",
	time = 20,
	picture = "",
	desc = "",
	stack = 1,
	id = 150001,
	icon = 150000,
	last_effect = "",
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
				effect = "bulunnusi_hudun_01",
				count = 7,
				bulletType = 1,
				cld_list = {
					{
						box = {
							3,
							5,
							8
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_1_0)
					local var_1_0 = arg_1_0 * 3

					return Vector3(math.sin(var_1_0) * 4, 0.75, math.cos(var_1_0) * 4),
				def rotationFun:(arg_2_0)
					return Vector3(0, arg_2_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
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
				effect = "bulunnusi_hudun_01",
				count = 7,
				bulletType = 1,
				cld_list = {
					{
						box = {
							3,
							5,
							8
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_3_0)
					local var_3_0 = arg_3_0 * 3 + ys.Battle.BattleConfig.SHIELD_CENTER_CONST_2

					return Vector3(math.sin(var_3_0) * 4, 0.75, math.cos(var_3_0) * 4),
				def rotationFun:(arg_4_0)
					return Vector3(0, arg_4_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 210, 0)
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
				effect = "bulunnusi_hudun_01",
				count = 7,
				bulletType = 1,
				cld_list = {
					{
						box = {
							3,
							5,
							8
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_5_0)
					local var_5_0 = arg_5_0 * 3 + ys.Battle.BattleConfig.SHIELD_CENTER_CONST_4

					return Vector3(math.sin(var_5_0) * 4, 0.75, math.cos(var_5_0) * 4),
				def rotationFun:(arg_6_0)
					return Vector3(0, arg_6_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 30, 0)
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
				effect = "bulunnusi_hudun_01",
				count = 7,
				bulletType = 1,
				cld_list = {
					{
						box = {
							3,
							5,
							8
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_7_0)
					local var_7_0 = arg_7_0 * 3 + 1.0466666666666666

					return Vector3(math.sin(var_7_0) * 4, 0.75, math.cos(var_7_0) * 4),
				def rotationFun:(arg_8_0)
					return Vector3(0, arg_8_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 150, 0)
			}
		},
		{
			id = 5,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "bulunnusi_hudun_01",
				count = 7,
				bulletType = 1,
				cld_list = {
					{
						box = {
							3,
							5,
							8
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_9_0)
					local var_9_0 = arg_9_0 * 3 + 3.14

					return Vector3(math.sin(var_9_0) * 4, 0.75, math.cos(var_9_0) * 4),
				def rotationFun:(arg_10_0)
					return Vector3(0, arg_10_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
			}
		},
		{
			id = 6,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "bulunnusi_hudun_01",
				count = 7,
				bulletType = 1,
				cld_list = {
					{
						box = {
							3,
							5,
							8
						},
						offset = {
							1.02,
							0,
							1.22
						}
					}
				},
				def centerPosFun:(arg_11_0)
					local var_11_0 = arg_11_0 * 3 + 5.233333333333333

					return Vector3(math.sin(var_11_0) * 4, 0.75, math.cos(var_11_0) * 4),
				def rotationFun:(arg_12_0)
					return Vector3(0, arg_12_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 150, 0)
			}
		}
	}
}
