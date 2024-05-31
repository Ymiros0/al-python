return {
	time = 0,
	name = "对雷暴AT立场弱化版（减少防雷击次数，减伤80%降至70%）",
	init_effect = "",
	stack = 1,
	id = 8886,
	picture = "",
	last_effect = "",
	desc = "",
	effect_list = {
		{
			type = "BattleBuffAddAttr",
			trigger = {
				"onAttach"
			},
			arg_list = {
				attr = "injureRatioByBulletTorpedo",
				number = -0.7
			}
		},
		{
			id = 1,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 3,
				bulletType = 3,
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
					local var_1_0 = arg_1_0 * 3

					return Vector3(math.sin(var_1_0) * 2, 0.75, math.cos(var_1_0) * 2),
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
				effect = "shield05",
				count = 3,
				bulletType = 3,
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
					local var_3_0 = arg_3_0 * 3 + 1.256

					return Vector3(math.sin(var_3_0) * 2, 0.75, math.cos(var_3_0) * 2),
				def rotationFun:(arg_4_0)
					return Vector3(0, arg_4_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 162, 0)
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
				effect = "shield05",
				count = 3,
				bulletType = 3,
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
					local var_5_0 = arg_5_0 * 3 + 2.512

					return Vector3(math.sin(var_5_0) * 2, 0.75, math.cos(var_5_0) * 2),
				def rotationFun:(arg_6_0)
					return Vector3(0, arg_6_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 234, 0)
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
				effect = "shield05",
				count = 3,
				bulletType = 3,
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
					local var_7_0 = arg_7_0 * 3 - 1.256

					return Vector3(math.sin(var_7_0) * 2, 0.75, math.cos(var_7_0) * 2),
				def rotationFun:(arg_8_0)
					return Vector3(0, arg_8_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 18, 0)
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
				effect = "shield05",
				count = 3,
				bulletType = 3,
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
				def centerPosFun:(arg_9_0)
					local var_9_0 = arg_9_0 * 3 - 2.512

					return Vector3(math.sin(var_9_0) * 2, 0.75, math.cos(var_9_0) * 2),
				def rotationFun:(arg_10_0)
					return Vector3(0, arg_10_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 54, 0)
			}
		}
	}
}
