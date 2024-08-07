return {
	map_id = 10007,
	id = 10101330,
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
					triggerType = 1,
					waveIndex = 204,
					preWaves = {},
					triggerParams = {
						timeout = 44
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
							monsterTemplateID = 101001,
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
							monsterTemplateID = 101001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101009,
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
							monsterTemplateID = 101001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101001,
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
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 101003,
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
							monsterTemplateID = 101006,
							reinforceDelay = 5,
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
							monsterTemplateID = 101001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
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
							monsterTemplateID = 101001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101001,
							moveCast = True,
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
							monsterTemplateID = 101014,
							moveCast = True,
							delay = 0,
							corrdinate = {
								6,
								0,
								55
							},
							buffList = {
								8015,
								8016,
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101001,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 101001,
							moveCast = True,
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
