﻿return {
	map_id = 10001,
	id = 10104340,
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
						timeout = 13
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
					key = true,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 101001,
							moveCast = true,
							delay = 0,
							corrdinate = {
								22,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101012,
							moveCast = true,
							delay = 0,
							corrdinate = {
								8,
								0,
								55
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 101001,
							moveCast = true,
							delay = 0,
							corrdinate = {
								22,
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
					key = true,
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 101001,
							moveCast = true,
							delay = 0,
							corrdinate = {
								19,
								0,
								80
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101009,
							moveCast = true,
							delay = 0,
							corrdinate = {
								-3,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101027,
							moveCast = true,
							delay = 0,
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
							monsterTemplateID = 101001,
							moveCast = true,
							delay = 0,
							corrdinate = {
								19,
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
					key = true,
					waveIndex = 103,
					conditionType = 0,
					preWaves = {
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 101003,
							moveCast = true,
							delay = 0,
							corrdinate = {
								8,
								0,
								85
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 101027,
							moveCast = true,
							delay = 0,
							corrdinate = {
								20,
								0,
								70
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 101014,
							moveCast = true,
							delay = 0,
							corrdinate = {
								4,
								0,
								55
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 101027,
							moveCast = true,
							delay = 0,
							corrdinate = {
								20,
								0,
								40
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 101006,
							moveCast = true,
							delay = 0,
							corrdinate = {
								30,
								0,
								40
							},
							buffList = {
								8001
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
