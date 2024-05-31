return {
	effect_list = {
		{
			id = 1,
			type = "BattleBuffShieldWall",
			trigger = {
				"onUpdate"
			},
			arg_list = {
				do_when_hit = "intercept",
				effect = "leigensitebao_longdun",
				count = 2,
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
							0
						}
					}
				},
				def centerPosFun:(arg_1_0)
					return Vector3(3, 1.5, 0.5),
				def rotationFun:(arg_2_0)
					return Vector3(0, 192, 0)
			}
		},
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onShieldBroken"
			},
			arg_list = {
				target = "TargetSelf",
				shieldBuffID = 16723,
				skill_id = 16721
			}
		},
		{
			type = "BattleBuffCastSkill",
			trigger = {
				"onRemove"
			},
			arg_list = {
				skill_id = 16721,
				target = "TargetSelf"
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
					count = 2,
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
								0
							}
						}
					},
					def centerPosFun:(arg_3_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_4_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
					count = 2,
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
								0
							}
						}
					},
					def centerPosFun:(arg_5_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_6_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
					count = 3,
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
								0
							}
						}
					},
					def centerPosFun:(arg_7_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_8_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
					count = 3,
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
								0
							}
						}
					},
					def centerPosFun:(arg_9_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_10_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
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
								2,
								0,
								0
							}
						}
					},
					def centerPosFun:(arg_11_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_12_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
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
								2,
								0,
								0
							}
						}
					},
					def centerPosFun:(arg_13_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_14_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
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
								0
							}
						}
					},
					def centerPosFun:(arg_15_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_16_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
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
								0
							}
						}
					},
					def centerPosFun:(arg_17_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_18_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
					count = 6,
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
								0
							}
						}
					},
					def centerPosFun:(arg_19_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_20_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	{
		effect_list = {
			{
				id = 1,
				type = "BattleBuffShieldWall",
				trigger = {
					"onUpdate"
				},
				arg_list = {
					do_when_hit = "intercept",
					effect = "leigensitebao_longdun",
					count = 6,
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
								0
							}
						}
					},
					def centerPosFun:(arg_21_0)
						return Vector3(3, 1.5, 0.5),
					def rotationFun:(arg_22_0)
						return Vector3(0, 192, 0)
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onShieldBroken"
				},
				arg_list = {
					target = "TargetSelf",
					shieldBuffID = 16723,
					skill_id = 16721
				}
			},
			{
				type = "BattleBuffCastSkill",
				trigger = {
					"onRemove"
				},
				arg_list = {
					skill_id = 16721,
					target = "TargetSelf"
				}
			}
		}
	},
	init_effect = "",
	name = "",
	time = 8,
	color = "blue",
	picture = "",
	desc = "",
	stack = 1,
	id = 16723,
	icon = 16723,
	last_effect = ""
}
