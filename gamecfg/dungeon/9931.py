return {
	map_id = 10001,
	id = 9931,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 600,
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
							monsterTemplateID = 901,
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
							monsterTemplateID = 911,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								55
							},
							buffList = {
								8001
							}
						},
						{
							monsterTemplateID = 901,
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
					waveIndex = 102,
					conditionType = 0,
					preWaves = {
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 902,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-5,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 902,
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
							monsterTemplateID = 903,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 903,
							moveCast = True,
							delay = 0,
							corrdinate = {
								10,
								0,
								51
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
					conditionType = 0,
					preWaves = {
						102
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 915,
							reinforceDelay = 6,
							delay = 0,
							moveCast = True,
							corrdinate = {
								5,
								0,
								55
							},
							bossData = {
								hpBarNum = 50,
								icon = "lingyangzhe"
							},
							buffList = {
								8601
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 904,
							moveCast = True,
							delay = 1,
							score = 20,
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
							monsterTemplateID = 905,
							moveCast = True,
							delay = 1,
							score = 20,
							corrdinate = {
								0,
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
					waveIndex = 104,
					conditionType = 1,
					preWaves = {
						103
					},
					triggerParam = {},
					spawn = {}
				},
				{
					triggerType = 8,
					waveIndex = 901,
					preWaves = {
						104
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {
		vanguard_unitList = {
			{
				tmpID = 900931,
				configId = 900931,
				skinId = 499090,
				id = 1,
				level = 120,
				equipment = {
					False,
					False,
					False
				},
				properties = {
					cannon = 450,
					air = 0,
					antiaircraft = 150,
					torpedo = 350,
					durability = 7500,
					reload = 150,
					armor = 0,
					dodge = 50,
					speed = 25.2,
					luck = 0,
					hit = 130
				},
				skills = {
					{
						id = 19710,
						level = 10
					},
					{
						id = 19720,
						level = 10
					},
					{
						id = 19002,
						level = 1
					},
					{
						id = 30062,
						level = 1
					}
				}
			}
		},
		main_unitList = {
			{
				tmpID = 100011,
				configId = 100011,
				skinId = 100010,
				id = 1,
				level = 120,
				equipment = {
					False,
					False,
					False
				},
				properties = {
					cannon = 1,
					air = 1,
					antiaircraft = 1,
					torpedo = 1,
					durability = 900000,
					reload = 1,
					armor = 1,
					dodge = 0,
					speed = 1,
					luck = 1,
					hit = 1
				}
			}
		}
	}
}
