return {
	map_id = 10001,
	id = 1101130,
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
							monsterTemplateID = 11006,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-5,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 11034,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								65
							}
						},
						{
							monsterTemplateID = 11006,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-5,
								0,
								40
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
							templateID = 320010,
							totalNumber = 3,
							weaponID = {
								320008
							},
							attr = {
								airPower = 40,
								maxHP = 15,
								attackRating = 23
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
							monsterTemplateID = 11016,
							reinforceDelay = 7,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								70
							}
						},
						{
							monsterTemplateID = 11037,
							reinforceDelay = 7,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								40
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 11040,
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
						},
						{
							monsterTemplateID = 11003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 11003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
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
					conditionType = 1,
					preWaves = {
						102,
						203
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 11032,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								10,
								0,
								55
							},
							buffList = {
								8050,
								8051
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 11002,
							moveCast = True,
							delay = 0,
							score = 0,
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
							monsterTemplateID = 11002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 11002,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								70
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
							templateID = 320020,
							totalNumber = 3,
							weaponID = {
								320009
							},
							attr = {
								airPower = 40,
								maxHP = 15,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 104,
					conditionType = 0,
					preWaves = {
						103,
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 11035,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								65
							}
						},
						{
							monsterTemplateID = 11018,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								45
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 11005,
							moveCast = True,
							delay = 0,
							score = 0,
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
							monsterTemplateID = 11007,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								55
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 11005,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								30
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 11040,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 11040,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								45
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
						104
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
