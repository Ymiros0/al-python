return {
	map_id = 10001,
	id = 801410,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-75,
				20,
				90,
				70
			},
			playerArea = {
				-75,
				20,
				42,
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
					waveIndex = 1001,
					preWaves = {},
					triggerParams = {
						timeout = 1
					}
				},
				{
					triggerType = 1,
					waveIndex = 1002,
					preWaves = {},
					triggerParams = {
						timeout = 15
					}
				},
				{
					triggerType = 1,
					waveIndex = 1003,
					preWaves = {},
					triggerParams = {
						timeout = 30
					}
				},
				{
					triggerType = 0,
					waveIndex = 2001,
					conditionType = 1,
					preWaves = {
						1001
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 8013,
							moveCast = True,
							delay = 0,
							corrdinate = {
								5,
								0,
								85
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 10,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20007
								},
								{
									switchParam = 10,
									dive = "STATE_RAID",
									index = 1,
									switchType = 1,
									setAI = 20009
								}
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 2002,
					conditionType = 1,
					preWaves = {
						1002,
						2001
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 8013,
							moveCast = True,
							delay = 0,
							corrdinate = {
								5,
								0,
								30
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 10,
									dive = "STATE_RAID",
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20008
								},
								{
									switchParam = 10,
									dive = "STATE_DIVE",
									index = 1,
									switchType = 1,
									setAI = 20009
								}
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 2003,
					conditionType = 1,
					preWaves = {
						1003,
						2002
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 8013,
							moveCast = True,
							delay = 0,
							corrdinate = {
								5,
								0,
								55
							},
							buffList = {
								8001
							},
							phase = {
								{
									switchParam = 99,
									dive = "STATE_RAID",
									index = 0,
									switchType = 1,
									setAI = 20009
								}
							}
						}
					}
				},
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
						timeout = 13
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 26
					}
				},
				{
					triggerType = 1,
					waveIndex = 204,
					preWaves = {},
					triggerParams = {
						timeout = 39
					}
				},
				{
					triggerType = 1,
					waveIndex = 205,
					preWaves = {},
					triggerParams = {
						timeout = 30
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
							monsterTemplateID = 8002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8005,
							reinforceDelay = 3,
							delay = 2,
							moveCast = True,
							corrdinate = {
								8,
								0,
								55
							}
						},
						{
							monsterTemplateID = 8002,
							moveCast = True,
							delay = 1,
							corrdinate = {
								-8,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 8023,
							moveCast = True,
							delay = 0,
							corrdinate = {
								30,
								0,
								85
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 8023,
							moveCast = True,
							delay = 0,
							corrdinate = {
								30,
								0,
								25
							},
							buffList = {
								8001,
								8002
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 8001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-8,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-8,
								0,
								45
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8004,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8021,
							delay = 0,
							chance = 0.5,
							corrdinate = {
								20,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8004,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 103,
					conditionType = 0,
					preWaves = {
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 8001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-11,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8003,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8021,
							moveCast = True,
							delay = 0,
							corrdinate = {
								22,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 8006,
							reinforceDelay = 3,
							delay = 0,
							moveCast = True,
							corrdinate = {
								0,
								0,
								55
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 8023,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								30
							},
							buffList = {
								8001,
								8002
							}
						}
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						103
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
