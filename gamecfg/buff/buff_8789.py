return {
	time = 0,
	name = "2020德系活动 欧根亲王 不破之盾",
	init_effect = "",
	stack = 1,
	id = 8789,
	picture = "",
	last_effect = "",
	desc = "",
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
				count = 15,
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
					local var_1_0 = arg_1_0 * 3

					return Vector3(math.sin(var_1_0) * 3, 0.75, math.cos(var_1_0) * 3),
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
				effect = "shield02",
				count = 15,
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
					local var_3_0 = arg_3_0 * 3 + 1.256

					return Vector3(math.sin(var_3_0) * 3, 0.75, math.cos(var_3_0) * 3),
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
				effect = "shield02",
				count = 15,
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
					local var_5_0 = arg_5_0 * 3 + 2.512

					return Vector3(math.sin(var_5_0) * 3, 0.75, math.cos(var_5_0) * 3),
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
				effect = "shield02",
				count = 15,
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
					local var_7_0 = arg_7_0 * 3 - 1.256

					return Vector3(math.sin(var_7_0) * 3, 0.75, math.cos(var_7_0) * 3),
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
				effect = "shield02",
				count = 15,
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
				def centerPosFun:(arg_9_0)
					local var_9_0 = arg_9_0 * 3 - 2.512

					return Vector3(math.sin(var_9_0) * 3, 0.75, math.cos(var_9_0) * 3),
				def rotationFun:(arg_10_0)
					return Vector3(0, arg_10_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 54, 0)
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
				effect = "shield05",
				count = 2,
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
				def centerPosFun:(arg_11_0)
					local var_11_0 = arg_11_0 * 3

					return Vector3(math.sin(var_11_0) * 5, 0.75, math.cos(var_11_0) * 5),
				def rotationFun:(arg_12_0)
					return Vector3(0, arg_12_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
			}
		},
		{
			id = 7,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 2,
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
				def centerPosFun:(arg_13_0)
					local var_13_0 = arg_13_0 * 3 + 1.256

					return Vector3(math.sin(var_13_0) * 5, 0.75, math.cos(var_13_0) * 5),
				def rotationFun:(arg_14_0)
					return Vector3(0, arg_14_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 162, 0)
			}
		},
		{
			id = 8,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 2,
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
				def centerPosFun:(arg_15_0)
					local var_15_0 = arg_15_0 * 3 + 2.512

					return Vector3(math.sin(var_15_0) * 5, 0.75, math.cos(var_15_0) * 5),
				def rotationFun:(arg_16_0)
					return Vector3(0, arg_16_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 234, 0)
			}
		},
		{
			id = 9,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 2,
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
				def centerPosFun:(arg_17_0)
					local var_17_0 = arg_17_0 * 3 - 1.256

					return Vector3(math.sin(var_17_0) * 5, 0.75, math.cos(var_17_0) * 5),
				def rotationFun:(arg_18_0)
					return Vector3(0, arg_18_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 18, 0)
			}
		},
		{
			id = 10,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 2,
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
				def centerPosFun:(arg_19_0)
					local var_19_0 = arg_19_0 * 3 - 2.512

					return Vector3(math.sin(var_19_0) * 5, 0.75, math.cos(var_19_0) * 5),
				def rotationFun:(arg_20_0)
					return Vector3(0, arg_20_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 54, 0)
			}
		}
	}
}
