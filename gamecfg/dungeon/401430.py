return {
	map_id = 10001,
	id = 401430,
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
							monsterTemplateID = 4005,
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
							monsterTemplateID = 4002,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								50
							}
						},
						{
							monsterTemplateID = 4000,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								60
							}
						},
						{
							monsterTemplateID = 4005,
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
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 4019,
							moveCast = True,
							delay = 0,
							corrdinate = {
								22,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 4017,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								55
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 4019,
							moveCast = True,
							delay = 0,
							corrdinate = {
								22,
								0,
								40
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
							monsterTemplateID = 4015,
							moveCast = True,
							delay = 0,
							corrdinate = {
								16,
								0,
								40
							},
							buffList = {
								8024,
								8025
							}
						},
						{
							monsterTemplateID = 4014,
							moveCast = True,
							delay = 0,
							corrdinate = {
								16,
								0,
								70
							},
							buffList = {
								8024,
								8025
							}
						},
						{
							monsterTemplateID = 4030,
							reinforceDelay = 5,
							delay = 0,
							moveCast = True,
							corrdinate = {
								20,
								0,
								55
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 4021,
							reinforceDelay = 5,
							delay = 0,
							moveCast = True,
							corrdinate = {
								5,
								0,
								55
							},
							buffList = {
								50002
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 4029,
							moveCast = True,
							delay = 0,
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
							monsterTemplateID = 4029,
							moveCast = True,
							delay = 0,
							corrdinate = {
								30,
								0,
								40
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
