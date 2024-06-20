return {
	map_id = 10001,
	id = 1404110,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-70,
				20,
				90,
				70
			},
			playerArea = {
				-70,
				20,
				37,
				68
			},
			enemyArea = {},
			mainUnitPosition = {
				{
					Vector3(-105, 0, 58),
					Vector3(-105, 0, 78),
					Vector3(-105, 0, 38)
				},
				[-1] = {
					Vector3(15, 0, 58),
					Vector3(15, 0, 78),
					Vector3(15, 0, 38)
				}
			},
			fleetCorrdinate = {
				-80,
				0,
				75
			},
			waves = {
				{
					triggerType = 1,
					waveIndex = 100,
					preWaves = {},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 1,
					waveIndex = 202,
					preWaves = {},
					triggerParams = {
						timeout = 10
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 22
					}
				},
				{
					triggerType = 1,
					waveIndex = 204,
					preWaves = {},
					triggerParams = {
						timeout = 36
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 14001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14025,
							reinforceDelay = 5,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								55
							},
							buffList = {
								9651
							}
						},
						{
							monsterTemplateID = 14002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								20,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								20,
								0,
								45
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								30
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 3,
							corrdinate = {
								30,
								0,
								28
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 3,
							corrdinate = {
								30,
								0,
								73
							},
							buffList = {
								8001,
								8002
							}
						}
					}
				},
				{
					triggerType = 1,
					waveIndex = 301,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						301
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 14029,
							reinforceDelay = 6,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								55
							},
							buffList = {
								9651
							}
						},
						{
							monsterTemplateID = 14005,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-15,
								0,
								55
							},
							buffList = {
								9674
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 14001,
							moveCast = True,
							delay = 2,
							corrdinate = {
								10,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14001,
							moveCast = True,
							delay = 2,
							corrdinate = {
								10,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					airFighter = {
						{
							interval = 10,
							onceNumber = 3,
							formation = 10005,
							delay = 0,
							templateID = 350010,
							totalNumber = 3,
							weaponID = {
								350008
							},
							attr = {
								airPower = 40,
								maxHP = 1200,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 2001,
					conditionType = 1,
					preWaves = {
						301
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 14020,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								55
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 20,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20009
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 1,
									switchParam = 180
								}
							}
						}
					}
				},
				{
					triggerType = 1,
					waveIndex = 302,
					conditionType = 1,
					preWaves = {
						102,
						203
					},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 103,
					conditionType = 1,
					preWaves = {
						302
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 14027,
							reinforceDelay = 5,
							delay = 0,
							moveCast = True,
							corrdinate = {
								10,
								0,
								55
							},
							buffList = {
								9651
							}
						},
						{
							monsterTemplateID = 14003,
							moveCast = True,
							delay = 0,
							corrdinate = {
								15,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 14024,
							moveCast = True,
							delay = 0,
							corrdinate = {
								8,
								0,
								65
							},
							buffList = {
								8001,
								8007,
								8625,
								8630,
								9700
							}
						},
						{
							monsterTemplateID = 14024,
							moveCast = True,
							delay = 0,
							corrdinate = {
								8,
								0,
								45
							},
							buffList = {
								8001,
								8007,
								8625,
								8630,
								9700
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 3,
							corrdinate = {
								30,
								0,
								32
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 2,
							corrdinate = {
								30,
								0,
								53
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 3,
							corrdinate = {
								30,
								0,
								78
							},
							buffList = {
								8001,
								8002
							}
						}
					}
				},
				{
					triggerType = 1,
					waveIndex = 303,
					conditionType = 0,
					preWaves = {
						103,
						102,
						101
					},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 104,
					conditionType = 0,
					preWaves = {
						303
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 14032,
							reinforceDelay = 6,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								70
							},
							buffList = {
								8050,
								8051
							}
						},
						{
							monsterTemplateID = 14028,
							reinforceDelay = 6,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								40
							},
							buffList = {
								8050,
								8051,
								9651
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 14001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								10,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								10,
								0,
								30
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 2,
							corrdinate = {
								30,
								0,
								28
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 2,
							corrdinate = {
								30,
								0,
								53
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 14019,
							moveCast = True,
							delay = 2,
							corrdinate = {
								30,
								0,
								78
							},
							buffList = {
								8001,
								8002
							}
						}
					},
					airFighter = {
						{
							interval = 10,
							onceNumber = 3,
							formation = 10005,
							delay = 0,
							templateID = 350010,
							totalNumber = 3,
							weaponID = {
								350008
							},
							attr = {
								airPower = 40,
								maxHP = 1200,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 2002,
					conditionType = 1,
					preWaves = {
						303
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 14020,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								55
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 20,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20009
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 1,
									switchParam = 180
								}
							}
						}
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					conditionType = 0,
					preWaves = {
						104,
						2002
					},
					triggerParams = {}
				},
				{
					triggerType = 10,
					waveIndex = 1000,
					conditionType = 0,
					preWaves = {
						100
					},
					triggerParam = {},
					blockFlags = {
						9600
					},
					spawn = {
						{
							life_time = 5,
							prefab = "suligao_dengta_stg",
							delay = 8,
							behaviours = 10024,
							IFF = 1,
							coordinate = {
								-15,
								0,
								55
							},
							cld_data = {
								30,
								60
							}
						},
						{
							life_time = 5,
							prefab = "suligao_dengta_stg",
							delay = 20,
							behaviours = 10024,
							IFF = 1,
							coordinate = {
								-15,
								0,
								55
							},
							cld_data = {
								30,
								60
							}
						},
						{
							life_time = 5,
							prefab = "suligao_dengta_stg",
							delay = 34,
							behaviours = 10024,
							IFF = 1,
							coordinate = {
								-15,
								0,
								55
							},
							cld_data = {
								30,
								60
							}
						}
					}
				}
			}
		}
	},
	fleet_prefab = {}
}