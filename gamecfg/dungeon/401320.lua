﻿return {
	map_id = 10001,
	id = 401320,
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
					key = true,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 4011,
							moveCast = true,
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
							monsterTemplateID = 4006,
							moveCast = true,
							delay = 0,
							corrdinate = {
								11,
								0,
								55
							}
						},
						{
							monsterTemplateID = 4011,
							moveCast = true,
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
					airFighter = {
						{
							interval = 10,
							onceNumber = 3,
							formation = 10006,
							delay = 0,
							templateID = 314083,
							totalNumber = 6,
							weaponID = {
								314523
							},
							attr = {
								airPower = 85,
								maxHP = 55,
								attackRating = 23
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
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 4010,
							moveCast = true,
							delay = 0,
							corrdinate = {
								33,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 4007,
							moveCast = true,
							delay = 0,
							corrdinate = {
								22,
								0,
								60
							},
							buffList = {
								8024,
								8025
							}
						},
						{
							monsterTemplateID = 4010,
							moveCast = true,
							delay = 0,
							corrdinate = {
								8,
								0,
								45
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
						101,
						102
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 4017,
							moveCast = true,
							delay = 0,
							corrdinate = {
								8,
								0,
								55
							},
							buffList = {
								8024,
								8025
							}
						},
						{
							monsterTemplateID = 4026,
							reinforceDelay = 5,
							delay = 0,
							team = 1,
							moveCast = true,
							corrdinate = {
								15,
								0,
								40
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 4011,
							moveCast = true,
							delay = 0,
							corrdinate = {
								19,
								0,
								85
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 4011,
							moveCast = true,
							delay = 0,
							corrdinate = {
								19,
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
