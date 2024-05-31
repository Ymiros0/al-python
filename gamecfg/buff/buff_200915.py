return {
	init_effect = "",
	name = "2024偶像活动三期EX 欧根盾（普通）",
	time = 0,
	color = "yellow",
	picture = "",
	desc = "",
	stack = 1,
	id = 200915,
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
				effect = "shield02",
				count = 60,
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
				count = 60,
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
				count = 60,
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
				count = 60,
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
				count = 60,
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
				count = 10,
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
					local var_11_0 = arg_11_0 * -2.4

					return Vector3(math.sin(var_11_0) * 5, 0.75, math.cos(var_11_0) * 5),
				def rotationFun:(arg_12_0)
					return Vector3(0, arg_12_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
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
				count = 10,
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
					local var_13_0 = arg_13_0 * -2.4 + 0.785

					return Vector3(math.sin(var_13_0) * 5, 0.75, math.cos(var_13_0) * 5),
				def rotationFun:(arg_14_0)
					return Vector3(0, arg_14_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 135, 0)
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
				count = 10,
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
					local var_15_0 = arg_15_0 * -2.4 + 1.57

					return Vector3(math.sin(var_15_0) * 5, 0.75, math.cos(var_15_0) * 5),
				def rotationFun:(arg_16_0)
					return Vector3(0, arg_16_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 180, 0)
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
				count = 10,
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
					local var_17_0 = arg_17_0 * -2.4 + 2.355

					return Vector3(math.sin(var_17_0) * 5, 0.75, math.cos(var_17_0) * 5),
				def rotationFun:(arg_18_0)
					return Vector3(0, arg_18_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 225, 0)
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
				count = 10,
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
					local var_19_0 = arg_19_0 * -2.4 + 3.14

					return Vector3(math.sin(var_19_0) * 5, 0.75, math.cos(var_19_0) * 5),
				def rotationFun:(arg_20_0)
					return Vector3(0, arg_20_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 270, 0)
			}
		},
		{
			id = 11,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 10,
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
				def centerPosFun:(arg_21_0)
					local var_21_0 = arg_21_0 * -2.4 + 3.9250000000000003

					return Vector3(math.sin(var_21_0) * 5, 0.75, math.cos(var_21_0) * 5),
				def rotationFun:(arg_22_0)
					return Vector3(0, arg_22_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 315, 0)
			}
		},
		{
			id = 12,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 10,
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
				def centerPosFun:(arg_23_0)
					local var_23_0 = arg_23_0 * -2.4 + 4.71

					return Vector3(math.sin(var_23_0) * 5, 0.75, math.cos(var_23_0) * 5),
				def rotationFun:(arg_24_0)
					return Vector3(0, arg_24_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST, 0)
			}
		},
		{
			id = 13,
			type = "BattleBuffShieldWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "shield05",
				count = 10,
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
				def centerPosFun:(arg_25_0)
					local var_25_0 = arg_25_0 * -2.4 + 5.495

					return Vector3(math.sin(var_25_0) * 5, 0.75, math.cos(var_25_0) * 5),
				def rotationFun:(arg_26_0)
					return Vector3(0, arg_26_0 * -0.8 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 45, 0)
			}
		},
		{
			id = 14,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 10,
				effect = "shield06",
				damage = 12,
				attack_attribute = 1,
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
				def centerPosFun:(arg_27_0)
					local var_27_0 = arg_27_0 * 1.5

					return Vector3(math.sin(var_27_0) * 8, 0.75, math.cos(var_27_0) * 8),
				def rotationFun:(arg_28_0)
					return Vector3(0, arg_28_0 * 0.5 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
			}
		},
		{
			id = 15,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 10,
				effect = "shield06",
				damage = 12,
				attack_attribute = 1,
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
				def centerPosFun:(arg_29_0)
					local var_29_0 = arg_29_0 * 1.5 + 1.0466666666666666

					return Vector3(math.sin(var_29_0) * 8, 0.75, math.cos(var_29_0) * 8),
				def rotationFun:(arg_30_0)
					return Vector3(0, arg_30_0 * 0.5 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 150, 0)
			}
		},
		{
			id = 16,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 10,
				effect = "shield06",
				damage = 12,
				attack_attribute = 1,
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
				def centerPosFun:(arg_31_0)
					local var_31_0 = arg_31_0 * 1.5 + 2.0933333333333333

					return Vector3(math.sin(var_31_0) * 8, 0.75, math.cos(var_31_0) * 8),
				def rotationFun:(arg_32_0)
					return Vector3(0, arg_32_0 * 0.5 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 210, 0)
			}
		},
		{
			id = 17,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 10,
				effect = "shield06",
				damage = 12,
				attack_attribute = 1,
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
				def centerPosFun:(arg_33_0)
					local var_33_0 = arg_33_0 * 1.5 + 3.14

					return Vector3(math.sin(var_33_0) * 8, 0.75, math.cos(var_33_0) * 8),
				def rotationFun:(arg_34_0)
					return Vector3(0, arg_34_0 * 0.5 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 270, 0)
			}
		},
		{
			id = 18,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 10,
				effect = "shield06",
				damage = 12,
				attack_attribute = 1,
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
				def centerPosFun:(arg_35_0)
					local var_35_0 = arg_35_0 * 1.5 + 4.1866666666666665

					return Vector3(math.sin(var_35_0) * 8, 0.75, math.cos(var_35_0) * 8),
				def rotationFun:(arg_36_0)
					return Vector3(0, arg_36_0 * 0.5 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 330, 0)
			}
		},
		{
			id = 19,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 10,
				effect = "shield06",
				damage = 12,
				attack_attribute = 1,
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
				def centerPosFun:(arg_37_0)
					local var_37_0 = arg_37_0 * 1.5 + 5.233333333333333

					return Vector3(math.sin(var_37_0) * 8, 0.75, math.cos(var_37_0) * 8),
				def rotationFun:(arg_38_0)
					return Vector3(0, arg_38_0 * 0.5 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 30, 0)
			}
		}
	}
}
