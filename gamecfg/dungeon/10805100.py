return {
	map_id = 10008,
	id = 10805100,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-80,
				20,
				90,
				70
			},
			playerArea = {
				-80,
				20,
				45,
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
						timeout = 13
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 28
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
					triggerType = 0,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 108001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								5,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108004,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								5,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108007,
							reinforceDelay = 4,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								5,
								0,
								55
							}
						},
						{
							monsterTemplateID = 108001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								5,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 108023,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								55
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
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 108002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-18,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108009,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								55
							}
						},
						{
							monsterTemplateID = 108002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-18,
								0,
								45
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 108022,
							moveCast = True,
							delay = 0,
							score = 0,
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
							monsterTemplateID = 108022,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								75
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
					waveIndex = 103,
					conditionType = 1,
					preWaves = {
						102,
						203
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 108001,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-8,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108002,
							moveCast = True,
							delay = 1,
							score = 0,
							corrdinate = {
								3,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108002,
							moveCast = True,
							delay = 2,
							score = 0,
							corrdinate = {
								11,
								0,
								50
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108001,
							moveCast = True,
							delay = 3,
							score = 0,
							corrdinate = {
								19,
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
					waveIndex = 104,
					conditionType = 1,
					preWaves = {
						103,
						204
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 108007,
							reinforceDelay = 3,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								0,
								0,
								60
							}
						},
						{
							monsterTemplateID = 108003,
							moveCast = True,
							delay = 0,
							score = 10,
							corrdinate = {
								-18,
								0,
								50
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 108005,
							reinforceDelay = 3,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								0,
								0,
								40
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 108023,
							moveCast = True,
							delay = 3,
							score = 0,
							corrdinate = {
								30,
								0,
								75
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 108023,
							moveCast = True,
							delay = 3,
							score = 0,
							corrdinate = {
								30,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						}
					}
				},
				{
					triggerType = 5,
					waveIndex = 400,
					preWaves = {
						104,
						103,
						102,
						101
					},
					triggerParams = {
						bgm = "battle-boss-1"
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 105,
					conditionType = 0,
					preWaves = {
						101,
						102,
						103,
						104
					},
					triggerParam = {},
					spawn = {
						{
							score = 0,
							reinforceDelay = 3,
							monsterTemplateID = 10805100,
							delay = 0,
							moveCast = True,
							corrdinate = {
								0,
								0,
								55
							},
							bossData = {
								hpBarNum = 50,
								icon = "dian"
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 108023,
							moveCast = True,
							delay = 1,
							score = 10,
							corrdinate = {
								30,
								0,
								70
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 108023,
							moveCast = True,
							delay = 1,
							score = 10,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 108023,
							moveCast = True,
							delay = 1,
							score = 10,
							corrdinate = {
								30,
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
						105
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
