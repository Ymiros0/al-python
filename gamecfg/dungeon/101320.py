return {
	map_id = 10009,
	id = 101320,
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
						timeout = 18
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 33
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
							monsterTemplateID = 1001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								14,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								3,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								25,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								14,
								0,
								30
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
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 1002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								22,
								0,
								85
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1009,
							moveCast = True,
							delay = 0,
							corrdinate = {
								8,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1003,
							reinforceDelay = 5,
							delay = 0,
							moveCast = True,
							corrdinate = {
								22,
								0,
								55
							}
						},
						{
							monsterTemplateID = 1009,
							moveCast = True,
							delay = 0,
							corrdinate = {
								8,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								22,
								0,
								25
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
					conditionType = 1,
					preWaves = {
						102
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 1030,
							moveCast = True,
							delay = 6,
							corrdinate = {
								19,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 1012,
							reinforceDelay = 5,
							delay = 0,
							moveCast = True,
							corrdinate = {
								8,
								0,
								55
							}
						},
						{
							monsterTemplateID = 1030,
							moveCast = True,
							delay = 6,
							corrdinate = {
								19,
								0,
								45
							},
							buffList = {
								8001,
								8002
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 1001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								8,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 1001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								8,
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
