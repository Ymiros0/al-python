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
				centerPosFun = function(arg_1_0)
					local var_1_0 = arg_1_0 * 3

					return Vector3(math.sin(var_1_0) * 3, 0.75, math.cos(var_1_0) * 3)
				end,
				rotationFun = function(arg_2_0)
					return Vector3(0, arg_2_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
				end
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
				centerPosFun = function(arg_3_0)
					local var_3_0 = arg_3_0 * 3 + 2.512

					return Vector3(math.sin(var_3_0) * 3, 0.75, math.cos(var_3_0) * 3)
				end,
				rotationFun = function(arg_4_0)
					return Vector3(0, arg_4_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 234, 0)
				end
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
				centerPosFun = function(arg_5_0)
					local var_5_0 = arg_5_0 * 3 - 2.512

					return Vector3(math.sin(var_5_0) * 3, 0.75, math.cos(var_5_0) * 3)
				end,
				rotationFun = function(arg_6_0)
					return Vector3(0, arg_6_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 54, 0)
				end
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
				count = 4,
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
				centerPosFun = function(arg_7_0)
					local var_7_0 = arg_7_0 * 3

					return Vector3(math.sin(var_7_0) * 5, 0.75, math.cos(var_7_0) * 5)
				end,
				rotationFun = function(arg_8_0)
					return Vector3(0, arg_8_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
				end
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
				count = 4,
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
				centerPosFun = function(arg_9_0)
					local var_9_0 = arg_9_0 * 3 + 1.256

					return Vector3(math.sin(var_9_0) * 5, 0.75, math.cos(var_9_0) * 5)
				end,
				rotationFun = function(arg_10_0)
					return Vector3(0, arg_10_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 162, 0)
				end
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
				effect = "shield02",
				count = 4,
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
				centerPosFun = function(arg_11_0)
					local var_11_0 = arg_11_0 * 3 + 2.512

					return Vector3(math.sin(var_11_0) * 5, 0.75, math.cos(var_11_0) * 5)
				end,
				rotationFun = function(arg_12_0)
					return Vector3(0, arg_12_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 234, 0)
				end
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
				effect = "shield02",
				count = 4,
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
				centerPosFun = function(arg_13_0)
					local var_13_0 = arg_13_0 * 3 - 1.256

					return Vector3(math.sin(var_13_0) * 5, 0.75, math.cos(var_13_0) * 5)
				end,
				rotationFun = function(arg_14_0)
					return Vector3(0, arg_14_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 18, 0)
				end
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
				effect = "shield02",
				count = 4,
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
				centerPosFun = function(arg_15_0)
					local var_15_0 = arg_15_0 * 3 - 2.512

					return Vector3(math.sin(var_15_0) * 5, 0.75, math.cos(var_15_0) * 5)
				end,
				rotationFun = function(arg_16_0)
					return Vector3(0, arg_16_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 54, 0)
				end
			}
		},
		{
			id = 9,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 6,
				effect = "shield06",
				damage = 55,
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
				centerPosFun = function(arg_17_0)
					local var_17_0 = arg_17_0 * 3

					return Vector3(math.sin(var_17_0) * 8, 0.75, math.cos(var_17_0) * 8)
				end,
				rotationFun = function(arg_18_0)
					return Vector3(0, arg_18_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 90, 0)
				end
			}
		},
		{
			id = 10,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 6,
				effect = "shield06",
				damage = 55,
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
				centerPosFun = function(arg_19_0)
					local var_19_0 = arg_19_0 * 3 + ys.Battle.BattleConfig.SHIELD_CENTER_CONST_2

					return Vector3(math.sin(var_19_0) * 8, 0.75, math.cos(var_19_0) * 8)
				end,
				rotationFun = function(arg_20_0)
					return Vector3(0, arg_20_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST + 210, 0)
				end
			}
		},
		{
			id = 11,
			type = "BattleBuffDamageWall",
			trigger = {
				"onStack",
				"onUpdate"
			},
			arg_list = {
				count = 6,
				effect = "shield06",
				damage = 55,
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
				centerPosFun = function(arg_21_0)
					local var_21_0 = arg_21_0 * 3 + ys.Battle.BattleConfig.SHIELD_CENTER_CONST_4

					return Vector3(math.sin(var_21_0) * 8, 0.75, math.cos(var_21_0) * 8)
				end,
				rotationFun = function(arg_22_0)
					return Vector3(0, arg_22_0 * ys.Battle.BattleConfig.SHIELD_ROTATE_CONST - 20, 0)
				end
			}
		}
	},
	{
		time = 5
	},
	{
		time = 5.5
	},
	{
		time = 6
	},
	{
		time = 6.5
	},
	{
		time = 7
	},
	{
		time = 7.5
	},
	{
		time = 8
	},
	{
		time = 8.5
	},
	{
		time = 9
	},
	{
		time = 10
	},
	time = 1,
	name = "",
	init_effect = "",
	stack = 1,
	id = 15541,
	picture = "",
	last_effect = "",
	desc = ""
}
