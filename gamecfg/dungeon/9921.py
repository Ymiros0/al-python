return {
	map_id = 10001,
	id = 9921,
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
							monsterTemplateID = 903,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-10,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 913,
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
							monsterTemplateID = 903,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-10,
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
							monsterTemplateID = 905,
							moveCast = True,
							delay = 0,
							corrdinate = {
								-10,
								0,
								55
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
								5,
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
								5,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 915,
							moveCast = True,
							delay = 0,
							corrdinate = {
								23,
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
							reinforceDelay = 2,
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
								8532
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
								-10,
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
								-10,
								0,
								20
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
					speed = 33,
					luck = 1,
					hit = 1
				}
			}
		},
		main_unitList = {
			{
				tmpID = 900921,
				configId = 900921,
				skinId = 499060,
				id = 1,
				level = 120,
				equipment = {
					False,
					False,
					False
				},
				properties = {
					cannon = 0,
					air = 500,
					antiaircraft = 350,
					torpedo = 0,
					durability = 15000,
					reload = 1000,
					armor = 0,
					dodge = 60,
					speed = 34,
					luck = 0,
					hit = 100
				},
				skills = {
					{
						id = 19460,
						level = 10
					},
					{
						id = 19470,
						level = 10
					},
					{
						id = 19480,
						level = 10
					},
					{
						id = 19002,
						level = 1
					},
					{
						id = 2,
						level = 1
					},
					{
						id = 8530,
						level = 1
					}
				}
			}
		}
	}
}
